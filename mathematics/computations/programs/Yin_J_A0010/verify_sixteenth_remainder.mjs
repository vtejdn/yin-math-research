// Sixteenth-root simple modules for the order-sixteen marking (1,6).
import assert from "node:assert/strict";

const primeLimit = 49152;
const printWitnesses = process.argv.includes("--witnesses");

function primesUpTo(limit) {
  const composite = new Uint8Array(limit + 1);
  const primes = [];
  for (let n = 2; n <= limit; n++) {
    if (composite[n]) continue;
    primes.push(n);
    for (let j = n * n; j <= limit; j += n) composite[j] = 1;
  }
  return primes;
}

function residue(n, p) {
  return ((n % p) + p) % p;
}

function power(base, exponent, p) {
  let result = 1;
  while (exponent > 0) {
    if (exponent % 2 === 1) result = result * base % p;
    base = base * base % p;
    exponent = Math.floor(exponent / 2);
  }
  return result;
}

function primitiveRoot(order, p) {
  for (let a = 2; a < p; a++) {
    const r = power(a, (p - 1) / order, p);
    if (power(r, order / 2, p) === p - 1) return r;
  }
  throw new Error("Missing required root");
}

// A list u encodes X^f = sum_j u[j] X^j in the marked field.
function factors(p) {
  const k = p % 16;
  const values = [];
  if (k === 1) {
    const r = primitiveRoot(16, p);
    for (let j = 1; j < 16; j += 2) values.push([power(r, j, p)]);
  } else if (k === 9) {
    const r = primitiveRoot(8, p);
    for (let j = 1; j < 8; j += 2) values.push([power(r, j, p), 0]);
  } else if (k === 7 || k === 15) {
    const b = k === 7 ? -1 : 1;
    for (let a = 0; a < p; a++) {
      const x = residue(a * a - 2 * b, p);
      if (x * x % p === 2) values.push([residue(-b, p), a]);
    }
  } else if (p <= 1024) {
    for (let a = 0; a < p; a++) {
      if (p % 8 === 3 && (a * a + 2) % p === 0) values.push([1, 0, a, 0]);
      if (p % 8 === 5 && (a * a + 1) % p === 0) values.push([a, 0, 0, 0]);
    }
  }
  let f = 1;
  while (power(p % 16, f, 16) !== 1) f++;
  assert.equal(values.length, p ** f <= 2 ** 40 ? 8 / f : 0);
  assert.equal(new Set(values.map(v => v.join(","))).size, values.length);
  for (const u of values) {
    assert.equal(u.length, f);
    // Reduce X^8 + 1 by the monic candidate.
    const coeff = [1, 0, 0, 0, 0, 0, 0, 0, 1];
    for (let i = 8; i >= f; i--) {
      const leading = coeff[i];
      coeff[i] = 0;
      for (let j = 0; j < f; j++) {
        coeff[i - f + j] = residue(coeff[i - f + j] + leading * u[j], p);
      }
    }
    assert(coeff.every(x => x === 0));
  }
  return values;
}

function orbit(u, initial, p) {
  const values = initial.slice();
  for (let i = u.length; i < 16; i++) {
    let next = 0;
    for (let j = 0; j < u.length; j++) next += u[j] * values[i - u.length + j];
    values.push(residue(next, p));
  }
  assert(values.some(x => x !== 0));
  for (let i = 0; i < 8; i++) assert.equal((values[i] + values[i+8]) % p, 0);
  return values;
}

function matchingFlows() {
  const lowMask = [], highMask = [], firstCount = [], cheaperRepair = [];
  for (let second = 0; second < 65536; second++) {
    for (let initial = 0; initial <= 1; initial++) {
      let previous = initial, first = 0, count = 0;
      for (let i = 0; i < 16; i++) {
        const next = previous + ((second >> ((i + 10) % 16)) & 1) - ((second >> i) & 1);
        if (next < 0 || next > 1) break;
        first |= next << i;
        count += next;
        previous = next;
        if (i !== 15 || previous !== initial) continue;
        let tOnly = 0, sOnly = 0;
        for (let v = 0; v < 16; v++) {
          const secondOut = (second >> v) & 1, secondIn = (second >> ((v + 10) % 16)) & 1;
          const firstOut = (first >> v) & 1, firstIn = (first >> ((v + 15) % 16)) & 1;
          if (secondIn && secondOut && !firstIn && !firstOut) tOnly++;
          if (firstIn && firstOut && !secondIn && !secondOut) sOnly++;
        }
        lowMask.push(second & 255);
        highMask.push(second >> 8);
        firstCount.push(count);
        cheaperRepair.push(Math.min(tOnly, sOnly));
      }
    }
  }
  assert.equal(firstCount.length, 2912);
  return {lowMask, highMask, firstCount, cheaperRepair};
}

const flows = matchingFlows();
const leastBit = Array.from({length: 256}, (_, i) => i ? Math.log2(i & -i) : 0);
const lowerSums = new Int32Array(256), upperSums = new Int32Array(256);

function check(p, entries, a, correction) {
  const period = 16 * p;
  const weights = entries.map(e => residue(6*a*p + 16*e + 8*p, period) - 8*p);
  weights[0] += correction * period;
  for (let mask = 1; mask < 256; mask++) {
    const i = leastBit[mask], remaining = mask & (mask - 1);
    lowerSums[mask] = lowerSums[remaining] + weights[i];
    upperSums[mask] = upperSums[remaining] + weights[8+i];
  }
  let lowest = Infinity, choice = -1, ties = 0;
  for (let j = 0; j < flows.firstCount.length; j++) {
    const cost = flows.firstCount[j] * a*p + lowerSums[flows.lowMask[j]] + upperSums[flows.highMask[j]];
    if (cost < lowest) {
      lowest = cost; choice = j; ties = 1;
    } else if (cost === lowest) {
      ties++;
    }
  }
  if (ties !== 1) return null;
  const allEdges = 16*a*p + weights.reduce((sum, w) => sum + w, 0);
  const spread = allEdges - 2*lowest;
  const defects = flows.cheaperRepair[choice];
  if (25*(2*spread + defects*period) > 198*period) return null;
  return {a, correction, lowest, spread, defects};
}

function witnesses(p, u) {
  const first = Array.from({length: u.length}, (_, j) => (j + 1) % p);
  const basic = orbit(u, first, p);
  for (let multiplier = 1; multiplier <= Math.min(20, p-1); multiplier++) {
    const entries = basic.map(e => multiplier*e % p);
    for (const a of [0, 1, 2, 3, 5]) {
      for (const correction of [0, 1, -1]) {
        const hit = check(p, entries, a, correction);
        if (hit) return {multiplier, first, ...hit};
      }
    }
  }
  // Two marked quartic factors require a different initial functional.
  const key = p + "/" + u.join(",");
  const exceptional = {
    "3/1,0,2,0": {first: [0, 1, 1, 0], a: 1},
    "13/5,0,0,0": {first: [9, 1, 0, 0], a: 2},
  }[key];
  assert(exceptional, key);
  const hit = check(p, orbit(u, exceptional.first, p), exceptional.a, 0);
  assert(hit);
  return {multiplier: 1, first: exceptional.first, exceptional: true, ...hit};
}

const counts = {1: 0, 2: 0, 4: 0}, exceptions = [];
let worstNumerator = 0, worstDenominator = 1;
for (const p of primesUpTo(primeLimit)) {
  if (p === 2) continue;
  for (const factor of factors(p)) {
    const hit = witnesses(p, factor);
    counts[factor.length]++;
    if (hit.exceptional) exceptions.push(p);
    const numerator = 2*hit.spread + hit.defects*16*p, denominator = 256*p;
    if (numerator*worstDenominator > worstNumerator*denominator) {
      worstNumerator = numerator; worstDenominator = denominator;
    }
    if (printWitnesses) console.log(JSON.stringify({p, factor, ...hit}));
  }
}
assert.deepEqual(counts, {1: 5000, 2: 7512, 4: 180});
assert.deepEqual(exceptions, [3, 13]);
assert(200*worstNumerator <= 99*worstDenominator);
console.log(JSON.stringify({counts, exceptions, worstNumerator, worstDenominator}));

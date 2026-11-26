// Exact cyclotomic norms of simple cycles of the two-step circulation graph.
import assert from "node:assert/strict";

const size = 25;
const radix = 2 ** size;
const mask = radix - 1;

function rotate(x) {
  return ((x << 1) | (x >>> (size - 1))) & mask;
}

// The two disjoint masks encode the positive and negative vertical edges.
function canonicalKey(positive, negative) {
  let key = Infinity;
  for (let i = 0; i < size; i++) {
    const candidate = Math.min(positive, negative) * radix + Math.max(positive, negative);
    key = Math.min(key, candidate);
    positive = rotate(positive);
    negative = rotate(negative);
  }
  return key;
}

function coefficients(positive, negative) {
  return Array.from({length: size}, (_, i) => ((positive >>> i) & 1) - ((negative >>> i) & 1));
}

function isUniversal(values) {
  return values.every((value, i) => value === values[i % 5]);
}

function enumerateCycles() {
  const adjacent = Array.from({length: size}, (_, i) =>
    [1, -1, 7, -7].map(step => ({target: (i + step + size) % size, step})));
  const representatives = new Set();
  let total = 0;
  let projectedZero = 0;
  let universalNonzero = 0;
  for (let start = 0; start < size; start++) {
    function visit(vertex, visited, depth, first, positive, negative) {
      for (const {target, step} of adjacent[vertex]) {
        if (target < start) continue;
        const nextPositive = step === 7 ? positive | (1 << vertex) : positive;
        const nextNegative = step === -7 ? negative | (1 << target) : negative;
        if (target === start) {
          // The least vertex fixes the base; its lesser neighbor fixes the direction.
          if (depth < 3 || first >= vertex) continue;
          total++;
          if ((nextPositive | nextNegative) === 0) {
            projectedZero++;
          } else {
            // Most projections fail periodicity after a single mask comparison.
            const fifthShift = ((nextPositive << 5) | (nextPositive >>> 20)) & mask;
            if (nextPositive === fifthShift && isUniversal(coefficients(nextPositive, nextNegative))) {
              universalNonzero++;
            }
          }
          representatives.add(canonicalKey(nextPositive, nextNegative));
        } else if ((visited & (1 << target)) === 0) {
          visit(target, visited | (1 << target), depth + 1,
                depth === 1 ? target : first, nextPositive, nextNegative);
        }
      }
    }
    visit(start, 1 << start, 1, -1, 0, 0);
  }
  assert.equal(total, 2303657);
  assert.equal(projectedZero, 1);
  assert.equal(universalNonzero, 31);
  assert.equal(representatives.size, 92032);
  return representatives;
}

function powMod(base, exponent, modulus) {
  let result = 1;
  while (exponent > 0) {
    if (exponent % 2) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exponent = Math.floor(exponent / 2);
  }
  return result;
}

function evaluationTable(prime) {
  assert.equal((prime - 1) % 25, 0);
  assert(Number.isSafeInteger(prime * prime));
  for (let d = 2; d * d <= prime; d++) assert.notEqual(prime % d, 0);
  let root = 1;
  for (let a = 2; a < prime && powMod(root, 5, prime) === 1; a++) {
    root = powMod(a, (prime - 1) / 25, prime);
  }
  assert.equal(powMod(root, 25, prime), 1);
  assert.notEqual(powMod(root, 5, prime), 1);
  const rows = [];
  for (let k = 1; k < size; k++) {
    if (k % 5 !== 0) {
      rows.push(Array.from({length: size}, (_, j) => powMod(root, j * k, prime)));
    }
  }
  return rows;
}

function normResidue(values, table, prime) {
  let product = 1;
  for (const row of table) {
    let value = 0;
    for (let j = 0; j < size; j++) value += row[j] * values[j];
    value = ((value % prime) + prime) % prime;
    product = (product * value) % prime;
  }
  return product;
}

function splitExceptionPrimes(norms) {
  const limit = Math.floor(Math.sqrt(5314180901));
  const composite = new Uint8Array(limit + 1);
  const primes = [];
  for (let p = 2; p <= limit; p++) {
    if (composite[p]) continue;
    primes.push(p);
    for (let j = p * p; j <= limit; j += p) composite[j] = 1;
  }
  const factors = new Set();
  for (let value of norms) {
    for (const p of primes) {
      if (p * p > value) break;
      if (value % p !== 0) continue;
      factors.add(p);
      do { value /= p; } while (value % p === 0);
    }
    if (value > 1) factors.add(value);
  }
  const exceptions = [...factors].filter(p => p > 100000 && p % 25 === 1).sort((x, y) => x - y);
  assert.equal(norms.size, 10234);
  assert.equal(factors.size, 5931);
  assert.equal(exceptions.length, 5426);
  assert.equal(exceptions.at(-1), 2227495051);
  return exceptions;
}

function main() {
  const representatives = enumerateCycles();
  const primes = [32000251, 32000651];
  const tables = primes.map(evaluationTable);
  const [a, b] = primes.map(BigInt);
  assert(a * b * 4n ** 10n > 125n ** 10n);
  const inverse = BigInt(powMod(primes[0], primes[1] - 2, primes[1]));
  assert.equal(a * inverse % b, 1n);
  let zero = 0;
  let maximum = 0n;
  const norms = new Set();
  for (const key of representatives) {
    const values = coefficients(Math.floor(key / radix), key % radix);
    const [x, y] = primes.map((p, i) => BigInt(normResidue(values, tables[i], p)));
    const norm = x + a * ((((y - x) * inverse) % b + b) % b);
    assert.equal(norm === 0n, isUniversal(values));
    if (norm === 0n) zero++;
    else norms.add(Number(norm));
    if (norm > maximum) maximum = norm;
  }
  assert.equal(zero, 7);
  assert.equal(maximum, 5314180901n);
  if (process.argv[2] === "--split-exceptions") {
    console.log(JSON.stringify(splitExceptionPrimes(norms)));
    return;
  }
  console.log("2303657 simple cycles; 92032 signed rotation classes of projections; " +
              "1 zero projection and 31 other universal cycles; maximum norm 5314180901.");
}

main();

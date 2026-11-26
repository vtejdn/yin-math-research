// Exact matching certificates for the finite primitive order-26 range.
import assert from "node:assert/strict";
import {markedFactors, mod, power} from "./phi26_factors.mjs";

const channels = 26, offsets = [0, 1, 10, 11], stride = channels + 1;
const upper = 725547;

// Reuse storage across the independent small assignments. Prices, costs and
// matrix indices in this finite interval are exact integers below 2^53.
const matrix = new Float64Array(channels * channels);
const u = new Float64Array(stride), v = new Float64Array(stride);
const owner = new Int32Array(stride), previous = new Int32Array(stride);
const distance = new Float64Array(stride), visited = new Uint8Array(stride);
const tight = new Int32Array(channels), reach = new Int32Array(channels);

function solveAssignment() {
  owner.fill(0);
  u.fill(0);
  v.fill(0);
  for (let i = 1; i <= channels; i++) {
    owner[0] = i;
    let row = 0;
    distance.fill(Infinity);
    visited.fill(0);
    do {
      visited[row] = 1;
      const col = owner[row], start = (col - 1) * channels;
      let next = 0, delta = Infinity;
      for (let j = 1; j <= channels; j++) {
        if (visited[j]) continue;
        const reduced = matrix[start + j - 1] - u[col] - v[j];
        if (reduced < distance[j]) {
          distance[j] = reduced;
          previous[j] = row;
        }
        if (distance[j] < delta) {
          next = j;
          delta = distance[j];
        }
      }
      for (let j = 0; j <= channels; j++) {
        if (visited[j]) {
          u[owner[j]] += delta;
          v[j] -= delta;
        } else {
          distance[j] -= delta;
        }
      }
      row = next;
    } while (owner[row] !== 0);
    while (row) {
      owner[row] = owner[previous[row]];
      row = previous[row];
    }
  }
}

function hasInvertibleBlocks() {
  for (let k = 0; k < channels; k++) {
    for (let i = 0; i < channels; i++) {
      if (reach[i] & (1 << k)) reach[i] |= reach[k];
    }
  }
  let checked = 0;
  for (let i = 0; i < channels; i++) {
    if (checked & (1 << i)) continue;
    const block = [];
    for (let j = 0; j < channels; j++) {
      if ((reach[i] & (1 << j)) && (reach[j] & (1 << i))) {
        block.push(j);
        checked |= 1 << j;
      }
    }
    if (block.length === 1) continue;
    if (block.length !== 2) return false;
    const rows = [];
    for (let j = 0; j < channels; j++) if (block.includes(owner[j + 1] - 1)) rows.push(j);
    const types = [];
    for (const input of block) {
      if (!rows.every(j => tight[input] & (1 << j))) return false;
      types.push(rows.map(j => mod(j - input, channels)).sort((a, b) => a - b).join(","));
    }
    if (!types.includes("0,1") || !types.includes("10,11")) return false;
  }
  return true;
}

function extremum(weights, base, sign) {
  const magnitude = Math.max(...weights.map(Math.abs)) + Math.abs(base);
  const penalty = (2 * channels + 1) * magnitude + 1;
  matrix.fill(penalty);
  for (let i = 0; i < channels; i++) {
    for (const k of offsets) {
      const first = k === 1 || k === 11 ? base : 0;
      const second = k >= 10 ? weights[i] : 0;
      matrix[i * channels + (i + k) % channels] = sign * (first + second);
    }
  }
  solveAssignment();

  // Certify optimality directly, independently of the search method.
  tight.fill(0);
  reach.fill(0);
  let score = 0, used = 0;
  for (let j = 0; j < channels; j++) {
    const i = owner[j + 1] - 1;
    assert(i >= 0 && !(used & (1 << i)));
    used |= 1 << i;
    assert(offsets.includes(mod(j - i, channels)));
    const cost = matrix[i * channels + j];
    assert(Number.isSafeInteger(u[i + 1]) && Number.isSafeInteger(v[j + 1]));
    assert(cost === u[i + 1] + v[j + 1]);
    score += cost;
  }
  for (let i = 0; i < channels; i++) {
    for (const k of offsets) {
      const j = (i + k) % channels, price = u[i + 1] + v[j + 1];
      const cost = matrix[i * channels + j];
      assert(price <= cost);
      if (price === cost) {
        tight[i] |= 1 << j;
        reach[i] |= 1 << (owner[j + 1] - 1);
      }
    }
  }
  return [sign * score, hasInvertibleBlocks()];
}

function orbit(p, factor, seed) {
  const values = seed.slice(), degree = factor.length - 1;
  for (let i = 0; i < channels; i++) {
    let next = 0;
    for (let j = 0; j < degree; j++) next -= factor[j] * values[i + j];
    values.push(mod(next, p));
  }
  for (let i = 0; i < degree; i++) assert.equal(values[channels + i], values[i]);
  for (let i = 0; i < 13; i++) assert.equal((values[i] + values[i + 13]) % p, 0);
  return values.slice(0, channels);
}

function matchingCertificate(p, values, a, flip) {
  const m = a ? 26 * p : p, base = a * p, half = Math.floor(m / 2);
  const weights = values.map(x => mod(10 * base + (a ? 26 : 1) * x + half, m) - half);
  weights[0] += flip * m;
  const [low, lowFull] = extremum(weights, base, 1);
  const [high, highFull] = extremum(weights, base, -1);
  if (p === 2) {
    assert.deepEqual([low, high, lowFull, highFull], [-208, 104, true, true]);
  }
  return (lowFull || highFull) && 884 * (high - low) <= 217 * channels * m;
}

function seeds(p, degree) {
  const result = [];
  if (degree === 12 && p > 12) {
    result.push(Array.from({length: 12}, (_, i) => i % 2 ? p - 1 : 1));
  }
  for (let j = 0; j < 5; j++) {
    result.push(Array.from({length: degree}, (_, i) => (1 + j * (1 + i)) % p));
  }
  for (let j = 1; j < Math.min(8, p); j++) {
    result.push(Array.from({length: degree}, (_, i) => i === 0 ? j : 1));
  }
  // Additional deterministic candidates. Acceptance always uses exact arithmetic.
  let state = 37;
  for (let j = 0; j < 20; j++) {
    result.push(Array.from({length: degree}, () => {
      state = (48271 * state) % 2147483647;
      return state % p;
    }));
  }
  return result.filter(seed => seed.some(x => x !== 0));
}

function certificate(p, factor) {
  const candidates = seeds(p, factor.length - 1).map(seed => orbit(p, factor, seed));
  for (const a of [0, 1, -1, 2, -2, 3, -3, 5, -5]) {
    for (const values of candidates) {
      const positive = values.slice(0, 13).map((x, i) => mod(i % 2 ? -x : x, p));
      if (positive.every(x => x > 0) && positive.reduce((s, x) => s + x, 0) <= 3 * p) {
        return "signed";
      }
      for (const flip of [1, -1, 0]) {
        if (matchingCertificate(p, values, a, flip)) return "matched";
      }
    }
  }
  return null;
}

function main() {
  assert(Number.isSafeInteger(12 * upper * upper));
  const composite = new Uint8Array(upper + 1);
  for (let q = 2; q * q <= upper; q++) {
    if (!composite[q]) for (let j = q * q; j <= upper; j += q) composite[j] = 1;
  }
  // In characteristic two the factor is Phi_13. In characteristic thirteen
  // the only simple factor is X+1. Count these two markings separately.
  assert.equal(power(2, 12, 13), 1);
  for (let k = 1; k < 12; k++) assert.notEqual(power(2, k, 13), 1);
  const binary = orbit(2, Array(13).fill(1), [...Array(11).fill(0), 1]);
  assert(matchingCertificate(2, binary, 2, 0));
  assert.equal(certificate(13, [1, 1]), "signed");
  let primes = 2;
  const counts = {"12_matched": 1, "1_signed": 1};
  for (let p = 3; p <= upper; p += 2) {
    if (composite[p] || p === 13) continue;
    primes++;
    let d = 1;
    while (power(p, d, 13) !== 1) d++;
    for (const factor of markedFactors(p, d)) {
      const result = certificate(p, factor);
      assert(result !== null, "No certificate for " + JSON.stringify([p, factor]));
      const key = d + "_" + result;
      counts[key] = (counts[key] || 0) + 1;
    }
  }
  const expected = {
    "1_signed":453, "1_matched":58144, "2_signed":4, "2_matched":29234,
    "3_signed":49, "3_matched":38919, "4_signed":4, "4_matched":29201,
    "6_signed":1, "6_matched":19427, "12_signed":19506, "12_matched":3
  };
  assert.equal(primes, 58457);
  assert.deepEqual(counts, expected);
  const markings = Object.values(counts).reduce((a, b) => a + b, 0);
  assert.equal(markings, 194945);
  console.log(JSON.stringify({primes, markings, counts}));
}

main();

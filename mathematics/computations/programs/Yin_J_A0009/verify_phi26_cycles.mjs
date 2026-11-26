// Simple circulation cycles for the primitive order-26 module, folded onto 13 coefficients.
import assert from "node:assert/strict";

const order = 26;
const half = 13;
const digitPlace = 5 ** (half - 1);

function gcd(a, b) {
  while (b) [a, b] = [b, a % b];
  return a;
}

function projectionKey(values) {
  const low = Math.min(...values);
  const high = Math.max(...values);
  if (low === high) return 0;
  let content = 0;
  for (const v of values) content = gcd(content, v - low);
  let forward = 0, negative = 0;
  for (const v of values) {
    forward = 5 * forward + (v - low) / content;
    negative = 5 * negative + (high - v) / content;
  }
  let key = Math.min(forward, negative);
  for (let i = 1; i < half; i++) {
    forward = Math.floor(forward / 5) + (forward % 5) * digitPlace;
    negative = Math.floor(negative / 5) + (negative % 5) * digitPlace;
    key = Math.min(key, forward, negative);
  }
  return key;
}

function enumerateProjections() {
  const graph = Array.from({length: order}, (_, i) => [1, -1, 10, -10].map(step => ({
    step, next: (i + step + order) % order,
  })));
  const values = new Int8Array(half);
  const nonzero = new Set();
  let cycles = 0, periodic = 0, alternating = 0;
  for (let start = 0; start < order; start++) {
    function visit(vertex, visited, length, first) {
      for (const {step, next} of graph[vertex]) {
        if (next < start || (next !== start && (visited & (1 << next)))) continue;
        if (next === start && (length < 3 || first >= vertex)) continue;
        const source = step === 10 ? vertex : next;
        const index = source % half;
        const increment = Math.abs(step) === 10 ? (step / 10) * (source % 2 ? -1 : 1) : 0;
        values[index] += increment;
        if (next === start) {
          cycles++;
          const key = projectionKey(values);
          if (key) nonzero.add(key);
          else if (values[0] === 0) periodic++;
          else alternating++;
        } else {
          visit(next, visited | (1 << next), length + 1, length === 1 ? next : first);
        }
        values[index] -= increment;
      }
    }
    visit(start, 1 << start, 1, -1);
  }
  assert.deepEqual([cycles, periodic, alternating, nonzero.size], [4004289, 1509, 106, 30967]);
  return nonzero;
}

function isPrime(p) {
  if (p < 2) return false;
  for (let d = 2; d * d <= p; d++) if (p % d === 0) return false;
  return true;
}

function power(base, exponent, prime) {
  let result = 1;
  while (exponent) {
    if (exponent % 2) result = result * base % prime;
    base = base * base % prime;
    exponent = Math.floor(exponent / 2);
  }
  return result;
}

function table(prime) {
  assert(isPrime(prime) && (prime - 1) % half === 0 && Number.isSafeInteger(prime * prime));
  let root = 1;
  for (let a = 2; root === 1; a++) root = power(a, (prime - 1) / half, prime);
  assert.equal(power(root, half, prime), 1);
  return Array.from({length: 12}, (_, i) =>
    Array.from({length: 13}, (_, j) => power(root, (i + 1) * j, prime)));
}

function normResidue(key, rows, prime) {
  const values = Array(half);
  for (let i = half - 1; i >= 0; i--) {
    values[i] = key % 5;
    key = Math.floor(key / 5);
  }
  let product = 1;
  for (const row of rows) {
    const sum = row.reduce((value, weight, j) => value + weight * values[j], 0);
    product = product * (sum % prime) % prime;
  }
  return product;
}

function main() {
  const keys = enumerateProjections();
  const primes = [1001027, 1001807];
  const tables = primes.map(table);
  const [a, b] = primes.map(BigInt);
  assert(a * b * 3n ** 6n > 169n ** 6n && a * b < 2n ** 53n);
  const inverse = BigInt(power(primes[0] % primes[1], primes[1] - 2, primes[1]));
  const norms = new Set();
  for (const key of keys) {
    const [x, y] = primes.map((p, i) => BigInt(normResidue(key, tables[i], p)));
    const norm = x + a * (((y - x) * inverse % b + b) % b);
    assert(norm > 0n && norm * 3n ** 6n <= 169n ** 6n);
    norms.add(Number(norm));
  }
  assert.equal(norms.size, 1957);
  assert.equal(Math.max(...norms), 2800409);
  const factors = new Set();
  for (let n of norms) {
    for (let d = 2; d * d <= n; d++) {
      if (n % d !== 0) continue;
      factors.add(d);
      do { n /= d; } while (n % d === 0);
    }
    if (n > 1) factors.add(n);
  }
  const exceptional = [...factors].filter(p => p > 725546 && p % 13 === 1).sort((x, y) => x - y);
  assert.equal(factors.size, 1345);
  assert.equal(exceptional.length, 20);
  assert.equal(exceptional.at(-1), 1799617);
  if (process.argv.includes("--split-exceptions")) console.log(JSON.stringify(exceptional));
  else console.log("4004289 cycles; 1509 periodic, 106 other zero evaluations; " +
    "30967 nonzero classes; 1957 primitive norms, maximum 2800409; 20 large split prime divisors.");
}

main();

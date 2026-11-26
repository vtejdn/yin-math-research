// Enumerate all two-root choices at the six fibers of the order-24 marking.
import assert from "node:assert/strict";

const powers = [0, 3, 4, 6, 7, 8, 10, 11, 14];

function mod(value, prime) {
  return ((value % prime) + prime) % prime;
}

function power(base, exponent, prime) {
  let value = 1;
  for (let i = 0; i < exponent; i++) value = value * base % prime;
  return value;
}

function rootPairs(roots, fiber) {
  const pairs = [];
  for (let i = fiber; i < 24; i += 6) {
    for (let j = i; j < 24; j += 6) pairs.push([roots[i], roots[j]]);
  }
  return pairs;
}

function multiplyQuadratic(poly, u, v, prime) {
  const out = new Array(poly.length + 2).fill(0);
  for (let j = 0; j < poly.length; j++) {
    out[j] = mod(out[j] + (u * v % prime) * poly[j], prime);
    out[j + 1] = mod(out[j + 1] - (u + v) * poly[j], prime);
    out[j + 2] = mod(out[j + 2] + poly[j], prime);
  }
  return out;
}

function factorTest(pairs, inverse, prime) {
  let tested = 0, possible = 0;
  function visit(poly, fiber) {
    if (fiber < 6) {
      for (const [u, v] of pairs[fiber]) {
        visit(multiplyQuadratic(poly, u, v, prime), fiber + 1);
      }
      return;
    }
    tested++;
    assert.notEqual(poly[0], 0);
    const b = mod(-poly[1] * inverse[poly[0]], prime);
    const c = mod(-(poly[2] + b * poly[1]) * inverse[poly[0]], prime);
    const coefficient = j => mod((poly[j] ?? 0) + b * poly[j - 1] + c * poly[j - 2], prime);
    if ([5, 9, 12, 13].every(j => coefficient(j) === 0)) possible++;
  }
  visit([1], 0);
  assert.equal(tested, 10 ** 6);
  return possible;
}

function addEvaluation(basis, input, prime, inverse) {
  const row = input.slice();
  for (let j = 0; j < row.length; j++) {
    if (!row[j]) continue;
    const multiplier = row[j];
    if (!basis[j]) {
      const expanded = basis.slice();
      expanded[j] = row.map(x => x * inverse[multiplier] % prime);
      return expanded;
    }
    for (let k = j; k < row.length; k++) row[k] = mod(row[k] - multiplier * basis[j][k], prime);
  }
  return basis;
}

function hermiteTest(pairs, roots, inverse, prime) {
  const evaluations = new Map(), derivatives = new Map();
  for (const u of roots) {
    evaluations.set(u, powers.map(j => power(u, j, prime)));
    derivatives.set(u, powers.map(j => j === 0 ? 0 : j * power(u, j - 1, prime) % prime));
  }
  let excluded = 0, possible = 0;
  function visit(basis, fiber) {
    if (basis.every(row => row !== null)) {
      excluded += 10 ** (6 - fiber);
      return;
    }
    if (fiber === 6) {
      possible++;
      return;
    }
    for (const [u, v] of pairs[fiber]) {
      const first = addEvaluation(basis, evaluations.get(u), prime, inverse);
      const second = u === v ? derivatives.get(u) : evaluations.get(v);
      visit(addEvaluation(first, second, prime, inverse), fiber + 1);
    }
  }
  visit(new Array(powers.length).fill(null), 0);
  assert.equal(excluded + possible, 10 ** 6);
  return possible;
}

for (const [prime, generator, expected] of [[97, 4, 0], [193, 7, 24]]) {
  for (let d = 2; d * d <= prime; d++) assert.notEqual(prime % d, 0);
  const roots = Array.from({length: 24}, (_, i) => power(generator, i, prime));
  assert.equal(new Set(roots).size, 24);
  assert.equal(power(generator, 24, prime), 1);
  const inverse = Array.from({length: prime}, (_, i) => power(i, prime - 2, prime));
  for (let i = 1; i < prime; i++) assert.equal(i * inverse[i] % prime, 1);
  const pairs = Array.from({length: 6}, (_, i) => rootPairs(roots, i));
  const factored = factorTest(pairs, inverse, prime);
  const hermite = hermiteTest(pairs, roots, inverse, prime);
  assert.equal(factored, expected);
  assert.equal(hermite, expected);
  console.log("Modulus", prime, "- possible patterns by factors and Hermite rows:", factored, hermite);
}

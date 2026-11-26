// Reduce the five double-eigenvalue fibers at order 20 modulo 101.
import assert from "node:assert/strict";

const prime = 101;
const root = 32;
const modulus = value => ((value % prime) + prime) % prime;
const powers = [1];
for (let i = 1; i <= 20; i++) powers.push(modulus(powers[i - 1] * root));
assert.equal(new Set(powers.slice(0, 20)).size, 20);
assert.equal(powers[20], 1);

const possiblePairs = Array.from({ length: 5 }, (_, fiber) => {
  const pairs = [];
  for (let j = 0; j < 4; j++) {
    for (let k = j; k < 4; k++) {
      const a = powers[fiber + 5 * j];
      const b = powers[fiber + 5 * k];
      pairs.push({ a, b, opposite: modulus(a + b) === 0 });
    }
  }
  return pairs;
});
function multiplyPair(poly, { a, b }) {
  const result = new Array(poly.length + 2).fill(0);
  for (let i = 0; i < poly.length; i++) {
    result[i] = modulus(result[i] + a * b * poly[i]);
    result[i + 1] = modulus(result[i + 1] - (a + b) * poly[i]);
    result[i + 2] = modulus(result[i + 2] + poly[i]);
  }
  return result;
}
const allowed = new Set([0, 3, 4, 6, 7, 8, 10, 11, 14]);
const missing = Array.from({ length: 15 }, (_, i) => i).filter(i => !allowed.has(i));
assert.deepEqual(missing, [1, 2, 5, 9, 12, 13]);
function quotientExists(poly) {
  const matrix = missing.map(i =>
    Array.from({ length: 5 }, (_, j) => poly[i - j] ?? 0)
  );
  let pivotRow = 0;
  for (let column = 0; column < 5; column++) {
    const index = matrix.findIndex((row, i) => i >= pivotRow && row[column] !== 0);
    if (index < 0) continue;
    [matrix[index], matrix[pivotRow]] = [matrix[pivotRow], matrix[index]];
    const pivot = matrix[pivotRow];
    for (const row of matrix.slice(pivotRow + 1)) {
      const entry = row[column];
      if (entry === 0) continue;
      for (let j = column; j < 5; j++) {
        row[j] = modulus(pivot[column] * row[j] - entry * pivot[j]);
      }
    }
    pivotRow++;
  }
  return pivotRow < 5;
}
const counts = new Array(6).fill(0);
let tested = 0;
function visit(fiber, poly, opposite) {
  if (fiber === 5) {
    tested++;
    if (quotientExists(poly)) counts[opposite]++;
    return;
  }
  for (const pair of possiblePairs[fiber]) {
    visit(fiber + 1, multiplyPair(poly, pair), opposite + Number(pair.opposite));
  }
}
visit(0, [1], 0);
assert.equal(tested, 100000);
assert.deepEqual(counts, [0, 0, 0, 0, 60, 32]);
console.log(JSON.stringify({ prime, root, tested, survivingByOppositePairs: counts }));

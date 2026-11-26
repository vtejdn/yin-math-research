// Conjugation on Sylow sevens and on Klein four subgroups for the order-168 factor.
import assert from "node:assert/strict";
import {identity, compose, inverse, key, permutations, cycleLengths, group, canonical,
  cyclicSubgroups, cheaperRepair, simpleCycles, certificate} from "./verify_small_permutations_sixteen.mjs";

const printWitnesses = process.argv.includes("--witnesses");
const conjugate = (h, g) => compose(compose(h, g), inverse(h));
const even = p => (p.length-cycleLengths(p).length) % 2 === 0;
const pop = mask => {
  let n = 0;
  while (mask) { mask &= mask-1; n++; }
  return n;
};

function normalizer() {
  const points = identity(7).map(i => i+1);
  // In the binary power basis these are an elementary transvection and multiplication
  // by X modulo X^3+X+1. Both act on the seven nonzero vectors.
  const x = points.map(i => (i ^ (i & 2 ? 1 : 0))-1);
  const y = points.map(i => ((i << 1) ^ (i & 4 ? 11 : 0))-1);
  assert.equal(group([x, y], 7).length, 168);
  const [first, second] = cyclicSubgroups(x, y, 7);
  assert.equal(first.length, 8);
  const inner = group([first, second], 8);
  const codes = new Set(inner.map(key));
  assert.equal(inner.length, 168);
  const full = permutations(8).filter(h => [first, second].every(g => codes.has(key(conjugate(h, g)))));
  assert.equal(full.length, 336);
  assert(full.every(g => even(g) === codes.has(key(g))));
  return full;
}

function kleinAction(x, y) {
  const d = x.length, one = key(identity(d));
  const involutions = group([x, y], d).filter(g =>
    even(g) && key(g) !== one && key(compose(g, g)) === one);
  const subgroups = [], ids = new Map();
  const subkey = list => list.map(key).sort().join("/");
  for (const a of involutions) for (const b of involutions) {
    const ab = compose(a, b);
    if (key(ab) === one || key(ab) !== key(compose(b, a))) continue;
    const members = [a, b, ab], code = subkey(members);
    if (!ids.has(code)) {
      ids.set(code, subgroups.length);
      subgroups.push(members);
    }
  }
  assert.equal(involutions.length, 21);
  assert.equal(subgroups.length, 14);
  const action = h => subgroups.map(members => ids.get(subkey(members.map(g => conjugate(h, g)))));
  return [action(x), action(y)];
}

function allFlows(x, y) {
  const d = x.length, backward = inverse(y), cycles = [];
  let covered = 0;
  for (let i = 0; i < d; i++) {
    if (covered & (1 << i)) continue;
    const cycle = [];
    let j = i;
    do {
      covered |= 1 << j; cycle.push(j); j = x[j];
    } while (j !== i);
    cycles.push(cycle);
  }
  const result = [];
  for (let n = 0; n < (1 << d); n++) {
    let firstMasks = [0];
    for (const cycle of cycles) {
      const possible = [];
      for (let initial = 0; initial <= 1; initial++) {
        let previous = initial, m = 0, valid = true;
        for (const i of cycle) {
          previous += ((n >> backward[i]) & 1) - ((n >> i) & 1);
          if (previous < 0 || previous > 1) { valid = false; break; }
          m |= previous << i;
        }
        if (valid && previous === initial) possible.push(m);
      }
      firstMasks = firstMasks.flatMap(m => possible.map(z => m | z));
      if (!firstMasks.length) break;
    }
    for (const m of firstMasks) result.push(m | (n << d));
  }
  return result;
}

function fourteen(x, y) {
  const [a, b] = kleinAction(x, y);
  assert.deepEqual(a, [1,0,4,5,6,13,7,10,9,11,8,2,3,12]);
  assert.deepEqual(b, [3,2,5,4,0,1,12,7,13,9,6,8,10,11]);
  const d = 14, block = 1 << d, masks = allFlows(a, b);
  assert.equal(masks.length, 2928);
  const adjustS = 16, adjustT = 16059, c = 2, anchor = 12505116;
  const costs = masks.map(f => {
    const sMask = f & (block-1), tMask = f >> d;
    return c*pop(sMask) + 6*c*pop(tMask) - 16*(pop(sMask & adjustS) + pop(tMask & adjustT));
  });
  const low = Math.min(...costs), high = Math.max(...costs);
  const optimal = masks.map((_, i) => i).filter(i => costs[i] === low);
  const index = masks.indexOf(anchor);
  assert(optimal.includes(index));
  assert.equal(optimal.length, 4);
  assert.equal(high-low, 52);
  const q = cheaperRepair(a, b, anchor);
  assert.equal(q, 0);
  assert(simpleCycles(a, b, masks, optimal, index));
  return {action: "Klein", c, adjustS, adjustT, anchor, low, spread: high-low,
    q, degree: d, numerator: 2*(high-low)+16*q};
}

const full = normalizer(), seen = new Set();
let original = 0, exceptional = 0, maxN = 0, maxD = 1;
for (const x of full) for (const y of full) {
  if (!even(y)) continue;
  const code = canonical(x, y);
  if (!code || seen.has(code)) continue;
  seen.add(code);
  if (group([x, y], 8).length !== 336) continue;
  let hit = certificate(x, y);
  if (hit) original++;
  else { hit = fourteen(x, y); exceptional++; }
  assert(40*hit.numerator <= 19*16*hit.degree);
  if (hit.numerator*maxD > maxN*hit.degree) {
    maxN = hit.numerator; maxD = hit.degree;
  }
  if (printWitnesses) console.log(JSON.stringify({x, y, ...hit}));
}
assert.equal(original, 68);
assert.equal(exceptional, 1);
console.log(JSON.stringify({normalizer: full.length, original, exceptional, maximum: [maxN, 16*maxD]}));

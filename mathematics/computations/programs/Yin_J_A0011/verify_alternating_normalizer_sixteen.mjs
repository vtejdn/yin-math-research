// Actions of the normalizer of A6 on its Sylow three subgroups and induced six-site actions.
import assert from "node:assert/strict";
import {pathToFileURL} from "node:url";
import {identity, compose, inverse, key, group, canonical, cycleLengths,
  cheaperRepair, simpleCycles, matchingFlows} from "./verify_small_permutations_sixteen.mjs";

const printWitnesses = process.argv.includes("--witnesses");
const pop = new Uint8Array(4096);
for (let i = 1; i < pop.length; i++) pop[i] = pop[i >> 1] + (i & 1);
const name = p => cycleLengths(p).join(",");
const triples = [];
for (let a = 0; a < 5; a++) for (let b = a + 1; b < 5; b++) for (let c = b + 1; c < 5; c++) {
  triples.push((1 << a) | (1 << b) | (1 << c));
}
function tripleAction(p) {
  return triples.map(mask => {
    let result = 0;
    for (let i = 0; i < 6; i++) if (mask & (1 << i)) result |= 1 << p[i];
    return triples.indexOf(result & 32 ? result ^ 63 : result);
  });
}

function transport(x, y, u, v, rootImage) {
  const map = Array(10).fill(-1), sites = [0];
  map[0] = rootImage;
  for (const i of sites) {
    for (const [next, after] of [[x[i], u[map[i]]], [y[i], v[map[i]]]]) {
      if (map[next] === -1) {
        map[next] = after;
        sites.push(next);
      } else if (map[next] !== after) return null;
    }
  }
  return sites.length === 10 && new Set(map).size === 10 ? map : null;
}

const a = [1,2,0,3,4,5], b = [0,2,3,4,5,1];
const x0 = tripleAction(a), y0 = tripleAction(b);
const inner = group([x0, y0], 10), six = group([a, b], 6);
const toSix = new Map(six.map(p => [key(tripleAction(p)), p]));
assert.equal(inner.length, 360);
assert.equal(toSix.size, 360);
const innerKeys = new Set(inner.map(key));
const normalizer = [];
for (const u of inner) if (name(u) === name(x0)) {
  for (const v of inner) if (name(v) === name(y0)) {
    for (let j = 0; j < 10; j++) {
      const h = transport(x0, y0, u, v, j);
      if (h) normalizer.push(h);
    }
  }
}
assert.equal(normalizer.length, 1440);
assert.equal(new Set(normalizer.map(key)).size, 1440);
assert(normalizer.every(h => innerKeys.has(key(compose(h, h)))));
const cosets = [], assigned = new Set(innerKeys);
for (const t of normalizer) if (!assigned.has(key(t))) {
  const coset = inner.map(n => compose(t, n));
  assert(coset.every(g => !assigned.has(key(g))));
  for (const g of coset) assigned.add(key(g));
  cosets.push(coset);
}
assert.equal(cosets.length, 3);
assert.equal(assigned.size, 1440);

function data(x, y) {
  const d = x.length, f = matchingFlows(x, y), mask = (1 << d) - 1;
  return {x, y, d, f, first: f.map(m => m & mask), second: f.map(m => m >> d),
    repair: f.map(m => cheaperRepair(x, y, m))};
}

// Any masks are valid lifts. A deterministic generator chooses candidate masks;
// each accepted witness is checked on the entire finite set of matching flows.
function tenSite(x, y) {
  const {d, f, first, second, repair} = data(x, y);
  const firstCounts = first.map(m => pop[m]), secondCounts = second.map(m => pop[m]);
  const costs = new Int32Array(f.length);
  let seed = 5538787;
  function randomWord() {
    seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5;
    return seed >>> 0;
  }
  for (let trial = 0; trial < 25000; trial++) {
    const c = [1,2,3,5,6,7][trial % 6], e = 6*c % 16;
    let adjustS = 0, adjustT = 0;
    for (let j = 0; j < d; j++) {
      if (randomWord() % 16 < c) adjustS |= 1 << j;
      if (randomWord() % 16 < e) adjustT |= 1 << j;
    }
    const total = d*(c+e) - 16*(pop[adjustS] + pop[adjustT]);
    let low = Infinity, admissible = true;
    for (let j = 0; j < f.length; j++) {
      const w = c*firstCounts[j] + e*secondCounts[j]
              - 16*(pop[adjustS & first[j]] + pop[adjustT & second[j]]);
      costs[j] = w;
      if (w < low) low = w;
      if (2*(total - 2*low) > 76) { admissible = false; break; }
    }
    if (!admissible) continue;
    const spread = total - 2*low;
    const optimal = f.map((_, j) => j).filter(j => costs[j] === low);
    for (const j of optimal) {
      const q = repair[j];
      if (2*spread + 16*q > 76) continue;
      if (simpleCycles(x, y, f, optimal, j)) {
        return {d, c, adjustS, adjustT, anchor: f[j], ties: optimal.length, spread, q};
      }
    }
  }
  return null;
}

function twelveSite(x, y) {
  const x2 = toSix.get(key(compose(x, x))), firstY = toSix.get(key(y));
  const secondY = toSix.get(key(compose(compose(inverse(x), y), x)));
  const xp = [...identity(6).map(i => 6+i), ...x2];
  const yp = [...firstY, ...secondY.map(i => 6+i)];
  const recipes = new Map([
    ["1,0,3,4,5,2,9,10,11,7,6,8", [1, 2048, 3242, 14196086, 1120, 4]],
    ["2,5,0,3,4,1,7,6,8,9,11,10", [3, 48, 0, 3900, 4224, 1]],
  ]);
  assert.deepEqual(xp, [6,7,8,9,10,11,0,1,5,4,3,2]);
  const [c, adjustS, adjustT, anchor, numFlows, ties] = recipes.get(key(yp));
  const {d, f, first, second, repair} = data(xp, yp);
  assert.equal(f.length, numFlows);
  const costs = f.map((_, j) => c*pop[first[j]] + (6*c % 16)*pop[second[j]]
    - 16*(pop[adjustS & first[j]] + pop[adjustT & second[j]]));
  const low = Math.min(...costs), spread = Math.max(...costs) - low;
  const optimal = f.map((_, j) => j).filter(j => costs[j] === low);
  const j = f.indexOf(anchor);
  assert(optimal.includes(j));
  assert.equal(optimal.length, ties);
  assert.equal(spread, 44);
  assert.equal(repair[j], 0);
  assert(simpleCycles(xp, yp, f, optimal, j));
  return {d, c, adjustS, adjustT, anchor, ties, spread, q: 0};
}

export {inner, normalizer, cosets};

if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) {
  const counts = [];
  let maximum = [0, 1];
  for (const coset of cosets) {
    const seen = new Set();
    let direct = 0, induced = 0;
    for (const x of coset) for (const y of inner) {
      const k = canonical(x, y);
      if (!k || seen.has(k)) continue;
      seen.add(k);
      if (group([x, y], 10).length !== 720) continue;
      let hit = tenSite(x, y);
      if (hit) direct++;
      else { hit = twelveSite(x, y); induced++; }
      const numerator = 2*hit.spread + 16*hit.q, denominator = 16*hit.d;
      assert(40*numerator <= 19*denominator);
      if (numerator*maximum[1] > denominator*maximum[0]) maximum = [numerator, denominator];
      if (printWitnesses) console.log(JSON.stringify({x, y, ...hit}));
    }
    counts.push([direct, induced]);
  }
  assert.deepEqual(counts, [[53,0],[78,0],[76,2]]);
  console.log(JSON.stringify({normalizer: normalizer.length, counts, maximum}));
}

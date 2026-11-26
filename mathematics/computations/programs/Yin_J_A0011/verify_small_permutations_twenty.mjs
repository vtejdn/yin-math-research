// Direct ten-phase endpoint certificates at C5 x C2 x C2.
import assert from "node:assert/strict";
import {pathToFileURL} from "node:url";
import {identity, compose, inverse, key, permutations, cycleLengths, group, canonical,
  cyclicSubgroups, matchingFlows, solvable, linearPairs, outer} from "./verify_small_permutations_sixteen.mjs";

const printWitnesses = process.argv.includes("--witnesses");
const pop = new Uint8Array(1 << 20);
for (let i = 1; i < pop.length; i++) pop[i] = pop[i >> 1] + (i & 1);

// Includes every parity of the second mark.
function* smallPairs(d) {
  const list = permutations(d), types = new Set(), seen = new Set();
  for (const x of list) {
    const type = key(cycleLengths(x));
    if (types.has(type)) continue;
    types.add(type);
    for (const y of list) {
      const code = canonical(x, y);
      if (!code || seen.has(code)) continue;
      seen.add(code);
      const image = group([x, y], d);
      if (image.length < 60) { assert(solvable(image)); continue; }
      yield {x, y, order: image.length};
    }
  }
}

function simpleZeroCycles(x, y, masks, optimal, anchor) {
  const d = x.length, f = masks[anchor], from = Array(d);
  let used = 0;
  for (const j of optimal) used |= masks[j] ^ f;
  for (let e = 0; e < 2*d; e++) if ((used >> e) & 1) {
    const i = e % d, p = e < d ? x : y, rev = Boolean((f >> e) & 1);
    const source = rev ? p[i] : i, target = rev ? i : p[i];
    if (from[source]) return false;
    from[source] = {target, perm: rev ? inverse(p) : p, s: e < d, sign: rev ? -1 : 1};
  }
  let seen = 0;
  for (let i = 0; i < d; i++) {
    if (!from[i] || (seen & (1 << i))) continue;
    let j = i, image = identity(d), s = 0, t = 0;
    do {
      if (!from[j] || (seen & (1 << j))) return false;
      seen |= 1 << j;
      const e = from[j];
      if (e.s) s += e.sign; else t += e.sign;
      image = compose(e.perm, image);
      j = e.target;
    } while (j !== i);
    if (s % 2 === 0 && t % 2 === 0 && (s+2*t) % 5 === 0 && image.every((v, k) => v === k)) {
      return false;
    }
  }
  return true;
}

function certificate(x, y) {
  const d = x.length, mask = (1 << d)-1, masks = matchingFlows(x, y);
  const counts = new Int32Array(masks.length);
  for (let a = 0; a <= 5; a++) for (const off of [0, 5]) {
    const b = (2*a+off) % 10;
    if (!a && !b) continue;
    const base = masks.map(f => a*pop[f & mask] + b*pop[f >> d]);
    const center = b > 5 ? mask << d : 0;
    for (let trial = 0; trial < 1 << (2*d); trial++) {
      const adjust = trial ^ center, all = d*(a+b)-10*pop[adjust];
      let low = Infinity, first = -1, ties = 0, admissible = true;
      for (let j = 0; j < masks.length; j++) {
        const cost = base[j] - 10*pop[masks[j] & adjust];
        counts[j] = cost;
        if (cost < low) { low = cost; first = j; ties = 1; }
        else if (cost === low) ties++;
        if (3*(all-2*low) > 7*d) { admissible = false; break; }
      }
      if (!admissible) continue;
      const optimal = ties === 1 ? [first] : masks.map((_, j) => j).filter(j => counts[j] === low);
      for (const j of optimal) if (simpleZeroCycles(x, y, masks, optimal, j)) {
        return {a, b, adjust, anchor: masks[j], low, ties, spread: all-2*low, d};
      }
    }
  }
  return null;
}

function cover(x, y) {
  const d = x.length;
  const test = (action, pair) => {
    assert(pair.every(p => new Set(p).size === p.length && p.every(i => i >= 0 && i < p.length)));
    const result = certificate(...pair);
    return result && {action, ...result};
  };
  let r = test("given", [x,y]);
  if (!r && d === 5) {
    const p = cyclicSubgroups(x,y,5);
    assert.equal(p[0].length, 6);
    r = test("cyclic", p);
  }
  if (!r && d === 6) r = test("factors", [outer(x), outer(y)]);
  if (!r && d === 7) {
    const p = cyclicSubgroups(x,y,7);
    assert.equal(p[0].length, 8);
    r = test("cyclic", p);
  }
  assert(r, [x,y].map(key).join("/"));
  return r;
}

function main() {
  const counts = {}, actions = {}, bounds = {};
  function register({x, y, order}) {
    const id = x.length + "/" + order, witness = cover(x,y);
    counts[id] = (counts[id] || 0) + 1;
    actions[id] ??= {};
    actions[id][witness.action] = (actions[id][witness.action] || 0) + 1;
    if (!bounds[id] || bounds[id][0]*witness.d < bounds[id][1]*witness.spread) {
      bounds[id] = [witness.spread, witness.d];
    }
    if (printWitnesses) console.log(JSON.stringify({x,y,order,...witness}));
  }
  for (const d of [5,6]) for (const r of smallPairs(d)) register(r);
  for (const r of linearPairs()) register(r);
  assert.deepEqual(counts, {"5/60":19,"5/120":57,"6/60":19,"6/72":24,
    "6/120":57,"6/360":106,"6/720":318,"7/168":114});
  console.log(JSON.stringify({counts, actions, bounds}));
}
if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) main();
export {certificate, simpleZeroCycles};

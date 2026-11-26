// Normal alternating subgroups on six letters for the noncyclic marking of order twenty.
import assert from "node:assert/strict";
import {compose, inverse, key, group, canonical} from "./verify_small_permutations_sixteen.mjs";
import {inner, normalizer, cosets} from "./verify_alternating_normalizer_sixteen.mjs";
import {witness} from "./verify_seven_permutations_twenty.mjs";

const printWitnesses = process.argv.includes("--witnesses");
const innerKeys = new Set(inner.map(key)), outer = new Map();
for (const [i, coset] of [inner, ...cosets].entries()) {
  for (const p of coset) outer.set(key(p), i);
}

// Simultaneous conjugation in the normalizer covers every first-mark conjugacy class.
// Rooted two-color graph codes then remove repeated transitive pairs.
const firstSeen = new Set(), seen = new Set(), counts = {};
let maximum = [0, 1];
for (const x of normalizer) {
  if (firstSeen.has(key(x))) continue;
  for (const h of normalizer) firstSeen.add(key(compose(compose(h,x),inverse(h))));
  for (const y of normalizer) {
    const u = outer.get(key(x)), v = outer.get(key(y));
    if (!u && !v) continue;
    const signature = canonical(x,y);
    if (!signature || seen.has(signature)) continue;
    const image = group([x,y],10);
    const inImage = new Set(image.map(key));
    if (![...innerKeys].every(g => inImage.has(g))) continue;
    seen.add(signature);
    const branch = u && v && u !== v ? "full" : String(u || v);
    assert.equal(image.length, branch === "full" ? 1440 : 720);
    const hit = witness(x,y);
    const stats = counts[branch] ??= [0,0,0];
    stats[hit.k === 1 ? 0 : hit.signed ? 2 : 1]++;
    if (hit.spread*maximum[1] > maximum[0]*hit.d) maximum = [hit.spread,hit.d];
    if (printWitnesses) console.log(JSON.stringify({branch,x,y,...hit}));
  }
}
assert.deepEqual(counts, {1:[103,43,13], 2:[156,50,28], 3:[140,65,29], full:[300,129,39]});
assert.deepEqual(maximum,[105,45]);
console.log(JSON.stringify({counts,maximum}));

// Exact small permutation twists for the cyclic order-sixteen marking (1,6).
import assert from "node:assert/strict";
import {pathToFileURL} from "node:url";

const printWitnesses = process.argv.includes("--witnesses");

function identity(d) {
  return Array.from({length: d}, (_, i) => i);
}
function compose(left, right) {
  return right.map(i => left[i]);
}
function inverse(p) {
  return identity(p.length).map(i => p.indexOf(i));
}
function key(p) {
  return p.join(",");
}
function permutations(d) {
  const result = [];
  function extend(p, used) {
    if (p.length === d) {
      result.push(p);
      return;
    }
    for (let i = 0; i < d; i++) if (!(used & (1 << i))) extend([...p, i], used | (1 << i));
  }
  extend([], 0);
  return result;
}
function cycleLengths(p) {
  let used = 0;
  const lengths = [];
  for (let i = 0; i < p.length; i++) {
    if (used & (1 << i)) continue;
    let j = i, length = 0;
    do {
      used |= (1 << j);
      j = p[j];
      length++;
    } while (j !== i);
    lengths.push(length);
  }
  return lengths.sort((a, b) => a - b);
}
function group(generators, d) {
  const one = identity(d);
  const elements = [one], seen = new Set([key(one)]);
  for (const x of elements) for (const g of generators) {
    const y = compose(x, g), code = key(y);
    if (!seen.has(code)) {
      seen.add(code);
      elements.push(y);
    }
  }
  return elements;
}
function solvable(elements) {
  const d = elements[0].length;
  while (elements.length > 1) {
    const comm = new Map();
    for (const a of elements) for (const b of elements) {
      const c = compose(compose(a, b), inverse(compose(b, a)));
      comm.set(key(c), c);
    }
    const derived = group([...comm.values()], d);
    if (derived.length === elements.length) return false;
    elements = derived;
  }
  return true;
}

// Rooted traversal labels both colored arrows, in order, at each visited site.
function canonical(x, y) {
  const d = x.length;
  let best;
  for (let root = 0; root < d; root++) {
    const sites = [root], labels = Array(d).fill(-1), code = [];
    labels[root] = 0;
    for (const i of sites) for (const j of [x[i], y[i]]) {
      if (labels[j] < 0) {
        labels[j] = sites.length;
        sites.push(j);
      }
      code.push(labels[j]);
    }
    if (sites.length !== d) return null;
    const value = code.join("");
    if (best === undefined || value < best) best = value;
  }
  return best;
}
function* smallPairs(d) {
  const elements = permutations(d), types = new Set(), seen = new Set();
  for (const x of elements) {
    const type = key(cycleLengths(x));
    if (types.has(type)) continue;
    types.add(type);
    for (const y of elements) {
      if ((d - cycleLengths(y).length) % 2) continue;
      const code = canonical(x, y);
      if (!code || seen.has(code)) continue;
      seen.add(code);
      const image = group([x, y], d);
      if (image.length < 60) {
        assert(solvable(image));
        continue;
      }
      yield {x, y, order: image.length};
    }
  }
}
function* linearPairs() {
  const elements = [];
  for (let a = 1; a < 8; a++) for (let b = 1; b < 8; b++) for (let c = 1; c < 8; c++) {
    const p = identity(7).map(i => {
      const v = i + 1;
      return ((v & 1 ? a : 0) ^ (v & 2 ? b : 0) ^ (v & 4 ? c : 0)) - 1;
    });
    if (new Set(p).size === 7 && !p.includes(-1)) elements.push(p);
  }
  assert.equal(elements.length, 168);
  const seen = new Set();
  for (const x of elements) for (const y of elements) {
    const code = canonical(x, y);
    if (!code || seen.has(code)) continue;
    seen.add(code);
    if (group([x, y], 7).length === 168) yield {x, y, order: 168};
  }
}

const pop = new Uint8Array(1 << 20);
for (let i = 1; i < pop.length; i++) pop[i] = pop[i >> 1] + (i & 1);

function matchingFlows(x, y) {
  const d = x.length, masks = new Set();
  for (let choices = 0; choices < 4**d; choices++) {
    let terms = choices, rows = 0, edges = 0;
    for (let j = 0; j < d; j++, terms >>= 2) {
      let row = j;
      if (terms & 1) {
        edges |= 1 << (d+j);
        row = y[row];
      }
      if (terms & 2) {
        edges |= 1 << row;
        row = x[row];
      }
      if (rows & (1 << row)) break;
      rows |= 1 << row;
    }
    if (rows === (1 << d)-1) masks.add(edges);
  }
  return [...masks];
}
function cheaperRepair(x, y, f) {
  const d = x.length;
  let throughS = 0, throughT = 0;
  for (let j = 0; j < d; j++) {
    const sOut = (f >> j) & 1, sIn = (f >> x.indexOf(j)) & 1;
    const tOut = (f >> (d+j)) & 1, tIn = (f >> (d+y.indexOf(j))) & 1;
    if (sIn && sOut && !tIn && !tOut) throughS++;
    if (tIn && tOut && !sIn && !sOut) throughT++;
  }
  return Math.min(throughS, throughT);
}

// Differences from an optimal circulation are exactly the recurrent tight edges.
function simpleCycles(x, y, masks, optimal, anchor) {
  const d = x.length, f = masks[anchor];
  let used = 0;
  for (const j of optimal) used |= masks[j] ^ f;
  const from = Array(d);
  for (let edge = 0; edge < 2*d; edge++) {
    if (!((used >> edge) & 1)) continue;
    const site = edge % d, p = edge < d ? x : y, backward = Boolean((f >> edge) & 1);
    const source = backward ? p[site] : site, target = backward ? site : p[site];
    if (from[source]) return false;
    from[source] = {target, perm: backward ? inverse(p) : p, weight: (backward ? -1 : 1)*(edge < d ? 1 : 6)};
  }
  let seen = 0;
  for (let i = 0; i < d; i++) {
    if (!from[i] || (seen & (1 << i))) continue;
    let j = i, image = identity(d), degree = 0;
    do {
      if (!from[j] || (seen & (1 << j))) return false;
      seen |= 1 << j;
      const next = from[j];
      degree += next.weight;
      image = compose(next.perm, image);
      j = next.target;
    } while (j !== i);
    if (degree % 16 === 0 && image.every((v, k) => v === k)) return false;
  }
  return true;
}

function certificate(x, y) {
  const d = x.length, block = 1 << d, all = block*block - 1;
  const masks = matchingFlows(x, y), costs = new Int32Array(masks.length);
  const repairs = masks.map(f => cheaperRepair(x, y, f));
  const partialThreshold = Math.floor(19*16*d/80);
  for (let c = 1; c <= 8; c++) {
    const b = 6*c % 16, centered = b > 8 ? (block-1) << d : 0;
    const base = masks.map(f => c*pop[f & (block-1)] + b*pop[f >> d]);
    for (let trial = 0; trial <= all; trial++) {
      const adjust = trial ^ centered, total = d*(c+b)-16*pop[adjust];
      let low = Infinity, first = -1, ties = 0, admissible = true;
      for (let j = 0; j < masks.length; j++) {
        const w = base[j]-16*pop[masks[j] & adjust];
        costs[j] = w;
        if (w < low) {
          low = w; ties = 1; first = j;
        } else if (w === low) ties++;
        if (total-2*low > partialThreshold) {
          admissible = false;
          break;
        }
      }
      if (!admissible) continue;
      const spread = total-2*low;
      const optimal = ties === 1 ? [first] : masks.map((_, j) => j).filter(j => costs[j] === low);
      for (const j of optimal) {
        const q = repairs[j], numerator = 2*spread + 16*q;
        if (40*numerator > 19*16*d) continue;
        if (!simpleCycles(x, y, masks, optimal, j)) continue;
        return {c, adjust, anchor: masks[j], ties, spread, q, numerator, degree: d};
      }
    }
  }
  return null;
}

function cyclicSubgroups(x, y, order) {
  const d = x.length, one = identity(d), oneKey = key(one);
  const image = group([x, y], d), subgroups = [], indices = new Map();
  const subgroupKey = els => els.map(key).sort().join("/");
  for (const g of image) {
    const els = [one];
    let z = g;
    while (key(z) !== oneKey && els.length <= order) {
      els.push(z);
      z = compose(z, g);
    }
    if (els.length !== order || key(z) !== oneKey) continue;
    const name = subgroupKey(els);
    if (!indices.has(name)) {
      indices.set(name, subgroups.length);
      subgroups.push(els);
    }
  }
  const action = g => {
    const gi = inverse(g);
    return subgroups.map(els => indices.get(subgroupKey(els.map(z => compose(compose(g, z), gi)))));
  };
  const pair = [action(x), action(y)];
  assert(pair.every(p => p.every(i => Number.isInteger(i))));
  return pair;
}

function sixFactorizations() {
  const edges = Array.from({length: 6}, () => Array(6)), matchings = [], totals = [];
  let number = 0;
  for (let i = 0; i < 6; i++) for (let j = i+1; j < 6; j++) edges[i][j] = edges[j][i] = number++;
  function pairSites(sites, mask) {
    if (!sites) {
      matchings.push(mask);
      return;
    }
    const i = Math.log2(sites & -sites);
    for (let j = i+1; j < 6; j++) if (sites & (1 << j)) {
      pairSites(sites ^ (1 << i) ^ (1 << j), mask | (1 << edges[i][j]));
    }
  }
  pairSites(63, 0);
  function extend(first, mask, subset) {
    if (mask === (1 << 15)-1) {
      totals.push(subset);
      return;
    }
    for (let i = first; i < matchings.length; i++) if (!(mask & matchings[i])) {
      extend(i+1, mask | matchings[i], subset | (1 << i));
    }
  }
  extend(0, 0, 0);
  assert.equal(matchings.length, 15);
  assert.equal(totals.length, 6);
  return p => {
    const matchAction = matchings.map(mask => {
      let image = 0;
      for (let i = 0; i < 6; i++) for (let j = i+1; j < 6; j++) if (mask & (1 << edges[i][j])) {
        image |= 1 << edges[p[i]][p[j]];
      }
      return matchings.indexOf(image);
    });
    return totals.map(subset => totals.indexOf(matchAction.reduce((acc, j, i) =>
        acc | (((subset >> i) & 1) << j), 0)));
  };
}
const outer = sixFactorizations();

function partitions(p) {
  // An unordered split into triples is represented by its side omitting site 5.
  const triples = [];
  for (let i = 0; i < 32; i++) if (pop[i] === 3) triples.push(i);
  assert.equal(triples.length, 10);
  return triples.map(t => {
    let u = 0;
    for (let i = 0; i < 6; i++) if (t & (1 << i)) u |= 1 << p[i];
    return triples.indexOf(u >= 32 ? 63 ^ u : u);
  });
}
function cover(x, y, order) {
  const d = x.length;
  const act = (name, pair) => {
    const [a, b] = pair;
    assert(a.length === b.length && a.every(v => v >= 0) && b.every(v => v >= 0));
    const result = certificate(a, b);
    return result && {action: name, ...result};
  };
  let result = act("given", [x, y]);
  if (!result && d === 5 && order === 120) {
    const pair = cyclicSubgroups(x, y, 5);
    assert.equal(pair[0].length, 6);
    result = act("Sylow", pair) || act("factorizations", pair.map(outer));
  }
  if (!result && d === 6) result = act("factorizations", [outer(x), outer(y)]);
  if (!result && d === 6) result = act("triples", [partitions(x), partitions(y)]);
  if (!result && d === 7) {
    const pair = cyclicSubgroups(x, y, 7);
    assert.equal(pair[0].length, 8);
    result = act("Sylow", pair);
  }
  assert(result, [key(x), key(y)]);
  return result;
}

const counts = {}, actions = {}, extremes = {};
function register(x, y, order) {
  const id = x.length + "/" + order;
  const witness = cover(x, y, order);
  counts[id] = (counts[id] || 0) + 1;
  actions[id] ??= {};
  actions[id][witness.action] = 1 + (actions[id][witness.action] || 0);
  const original = extremes[id];
  if (!original || original[0]*witness.degree < witness.numerator*original[1]) {
    extremes[id] = [witness.numerator, witness.degree];
  }
  if (printWitnesses) console.log(JSON.stringify({x, y, order, ...witness}));
}
if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) {
  for (const d of [5, 6]) for (const {x, y, order} of smallPairs(d)) register(x, y, order);
  for (const {x, y, order} of linearPairs()) register(x, y, order);
  assert.deepEqual(counts, {"5/60": 19, "5/120": 19, "6/60": 19, "6/72": 8,
    "6/120": 19, "6/360": 106, "6/720": 106, "7/168": 114});
  console.log(JSON.stringify({counts, actions, extremes}));
}

export {identity, compose, inverse, key, permutations, cycleLengths, group, canonical,
  cyclicSubgroups, cheaperRepair, simpleCycles, matchingFlows, certificate};

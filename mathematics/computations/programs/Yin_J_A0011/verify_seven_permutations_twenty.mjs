// Seven-site images and their ordinary or alternating two-subset actions.
import assert from "node:assert/strict";
import {identity, key, permutations, cycleLengths, canonical, solvable} from "./verify_small_permutations_sixteen.mjs";

const printWitnesses = process.argv.includes("--witnesses");
function* transitivePairs() {
  const elements = permutations(7), indices = new Uint16Array(1 << 21);
  function encode(p) { return p.reduce((n, j) => (n << 3) + j, 0); }
  for (let i = 0; i < elements.length; i++) indices[encode(elements[i])] = i;
  const times = [];
  function leftTable(i) {
    if (!times[i]) {
      const x = elements[i];
      times[i] = Uint16Array.from(elements, p => {
        let code = 0;
        for (const j of p) code = (code << 3) + x[j];
        return indices[code];
      });
    }
    return times[i];
  }
  const types = new Set(), seen = new Set(), visited = new Uint32Array(elements.length);
  const queue = new Uint16Array(elements.length);
  let tag = 0;
  for (let a = 0; a < elements.length; a++) {
    const x = elements[a], type = key(cycleLengths(x));
    if (types.has(type)) continue;
    types.add(type);
    for (let b = 0; b < elements.length; b++) {
      const y = elements[b], signature = canonical(x, y);
      if (!signature || seen.has(signature)) continue;
      seen.add(signature);
      const first = leftTable(a), second = leftTable(b), initial = indices[encode(identity(7))];
      let length = 1;
      tag++;
      queue[0] = initial; visited[initial] = tag;
      for (let j = 0; j < length; j++) {
        const old = queue[j];
        for (const next of [first[old], second[old]]) if (visited[next] !== tag) {
          visited[next] = tag; queue[length++] = next;
        }
      }
      if (length < 60) {
        assert(solvable(Array.from(queue.subarray(0, length), i => elements[i])));
      } else yield {x, y, order: length};
    }
  }
}

function subsetAction(p, k) {
  const lists = [];
  for (let mask = 0; mask < 128; mask++) {
    const members = identity(7).filter(i => mask & (1 << i));
    if (members.length === k) lists.push(members);
  }
  const maskOf = list => list.reduce((m, i) => m | (1 << i), 0);
  const masks = lists.map(maskOf), sites = [], signs = [];
  for (const list of lists) {
    const images = list.map(i => p[i]);
    let odd = 0;
    for (let i = 0; i < k; i++) for (let j = i+1; j < k; j++) odd ^= Number(images[i] > images[j]);
    sites.push(masks.indexOf(maskOf(images)));
    signs.push(odd);
  }
  return {sites, signs};
}

function optimum(x, y, weights) {
  const d = x.length, tails = [], heads = [];
  for (let i = 0; i < d; i++) {
    tails[i] = tails[d+i] = i;
    heads[i] = x[i]; heads[d+i] = y[i];
  }
  const used = new Uint8Array(2*d), predecessor = new Int16Array(d), distance = new Int32Array(d);
  for (;;) {
    distance.fill(0);
    let changed = -1;
    for (let sweep = 0; sweep < d; sweep++) {
      changed = -1;
      for (let e = 0; e < 2*d; e++) {
        const u = used[e] ? heads[e] : tails[e], v = used[e] ? tails[e] : heads[e];
        const cost = used[e] ? -weights[e] : weights[e];
        if (distance[v] > distance[u] + cost) {
          distance[v] = distance[u] + cost; predecessor[v] = e; changed = v;
        }
      }
      if (changed < 0) break;
    }
    if (changed < 0) break;
    // A further relaxation reaches a strictly negative directed residual cycle.
    for (let j = 0; j < d; j++) {
      const e = predecessor[changed];
      changed = used[e] ? heads[e] : tails[e];
    }
    const start = changed, cycle = [];
    let cost = 0;
    do {
      const e = predecessor[changed];
      cycle.push(e); cost += used[e] ? -weights[e] : weights[e];
      changed = used[e] ? heads[e] : tails[e];
    } while (changed !== start);
    assert(cost < 0);
    for (const e of cycle) used[e] ^= 1;
  }
  const low = weights.reduce((sum, w, e) => sum + used[e]*w, 0);
  return {used, distance, tails, heads, low};
}

function certifyZeroGraph(x, y, weights, state) {
  const d = x.length, {used, distance, tails, heads} = state;
  const adj = Array.from({length: d}, () => []), balance = new Int8Array(d);
  for (let e = 0; e < 2*d; e++) {
    let u = tails[e], v = heads[e], w = weights[e];
    if (used[e]) {
      balance[u]++; balance[v]--;
      [u, v] = [v, u]; w = -w;
    }
    assert(distance[u]+w >= distance[v]);
    if (distance[u]+w === distance[v]) adj[u].push([v,e]);
  }
  assert(balance.every(v => v === 0));
  const reach = adj.map((row, i) => row.reduce((bits, edge) => bits | (1 << edge[0]), 1 << i));
  for (let k = 0; k < d; k++) for (let i = 0; i < d; i++) {
    if ((reach[i] >> k) & 1) reach[i] |= reach[k];
  }
  let seen = 0;
  for (let i = 0; i < d; i++) {
    if ((seen >> i) & 1) continue;
    let component = 0;
    for (let j = 0; j < d; j++) if ((reach[i] >> j) & (reach[j] >> i) & 1) component |= 1 << j;
    seen |= component;
    let v = i, s = 0, t = 0;
    const edges = [];
    do {
      const internal = adj[v].filter(([j]) => (component >> j) & 1);
      if (!internal.length) { if (component !== 1 << i) return false; break; }
      if (internal.length !== 1) return false;
      const [next, e] = internal[0];
      edges.push(e);
      if (e < d) s += used[e] ? -1 : 1;
      else t += used[e] ? -1 : 1;
      v = next;
    } while (v !== i);
    if (!edges.length || s % 2 || t % 2 || (s+2*t) % 5) continue;
    let detected = false;
    for (let point = 0; point < d; point++) {
      let image = point;
      for (const e of edges) {
        const p = e < d ? x : y;
        image = used[e] ? p.indexOf(image) : p[image];
      }
      if (image !== point) { detected = true; break; }
    }
    if (!detected) return false;
  }
  return true;
}

// Candidate gauges are chosen by local minimization of absolute edge costs.
function lifts(x, y, A, B, random, dense) {
  const d = x.length, gauge = Array.from({length: d}, () => dense ? random() % 10 : 0);
  const prevX = identity(d).map(i => x.indexOf(i)), prevY = identity(d).map(i => y.indexOf(i));
  const centered = w => (w+45) % 10 - 5;
  for (let sweep = 0; sweep < 20; sweep++) {
    let changed = false;
    const start = random() % d;
    for (let j = 0; j < d; j++) {
      const i = (start+j) % d, old = gauge[i];
      let best = Infinity, choices = [];
      for (let t = 0; t < 10; t++) {
        gauge[i] = t;
        const cost = Math.abs(centered(A[i]+gauge[x[i]]-t)) + Math.abs(centered(A[prevX[i]]+t-gauge[prevX[i]]))
                   + Math.abs(centered(B[i]+gauge[y[i]]-t)) + Math.abs(centered(B[prevY[i]]+t-gauge[prevY[i]]));
        if (cost < best) { best = cost; choices = [t]; }
        else if (cost === best) choices.push(t);
      }
      gauge[i] = choices[random() % choices.length];
      if (gauge[i] !== old) changed = true;
    }
    if (!changed) break;
  }
  const weights = A.map((w,i) => centered(w+gauge[x[i]]-gauge[i]))
    .concat(B.map((w,i) => centered(w+gauge[y[i]]-gauge[i])));
  return {gauge, weights};
}

function witness(first, second) {
  const configs = [[1,0], [2,0], [2,1]].map(([k, signed]) => ({
    k, signed, one: subsetAction(first, k), two: subsetAction(second, k)
  }));
  const characters = [[1,2],[2,-1],[0,5],[5,0],[1,-3],[3,1],[2,4],[4,-2],[0,0],[5,5]];
  let seed = 3311001;
  function random() {
    seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5;
    return seed >>> 0;
  }
  for (let trial = 0; trial < 70; trial++) for (const config of configs) {
    const {k, signed, one, two} = config, x = one.sites, y = two.sites, d = x.length;
    const [a,b] = characters[trial % characters.length];
    assert.equal(Math.abs((b-2*a) % 5), 0);
    const A = one.signs.map(v => a + 5*signed*v), B = two.signs.map(v => b + 5*signed*v);
    const {gauge, weights} = lifts(x,y,A,B,random,trial >= 10);
    const state = optimum(x, y, weights);
    const total = weights.reduce((sum,w) => sum+w, 0), spread = total-2*state.low;
    if (3*spread > 7*d || !certifyZeroGraph(x, y, weights, state)) continue;
    return {k, signed, a, b, d, gauge, weights, low: state.low, spread,
      used: Array.from(state.used), potential: Array.from(state.distance)};
  }
  throw new Error("No certificate for " + key(first) + "/" + key(second));
}

const counts = {}, actions = {};
let maxN = 0, maxD = 1;
for (const {x,y,order} of transitivePairs()) {
  const w = witness(x,y);
  counts[order] = (counts[order] || 0)+1;
  const name = w.k === 1 ? "given" : w.signed ? "exterior" : "pairs";
  actions[order] ??= {};
  actions[order][name] = (actions[order][name] || 0)+1;
  if (w.spread*maxD > w.d*maxN) { maxN = w.spread; maxD = w.d; }
  if (printWitnesses) console.log(JSON.stringify({order,x,y,...w}));
}
assert.deepEqual(counts, {168:114, 2520:916, 5040:3090});
assert(3*maxN <= 7*maxD);
console.log(JSON.stringify({counts,actions,maximum:[maxN,maxD]}));

// Check all transitive six- and seven-point actions with the possible signs.
// Bits 0,...,d-1 refer to first-mark edges and d,...,2d-1 to second-mark edges.

import assert from "node:assert/strict";

function permutations(degree) {
  const result = [];
  function extend(prefix, used) {
    if (prefix.length === degree) {
      result.push(prefix);
      return;
    }
    for (let i = 0; i < degree; i++) {
      if (!(used & (1 << i))) extend([...prefix, i], used | (1 << i));
    }
  }
  extend([], 0);
  return result;
}

function parity(permutation) {
  let sign = 0;
  for (let i = 0; i < permutation.length; i++) {
    for (let j = 0; j < i; j++) sign ^= Number(permutation[j] > permutation[i]);
  }
  return sign;
}

function groupTable(degree) {
  const elements = permutations(degree);
  const index = new Uint16Array(1 << (3 * degree));
  for (const [i, element] of elements.entries()) {
    index[element.reduce((code, digit) => 8 * code + digit, 0)] = i;
  }
  const multiply = elements.map(left => Uint16Array.from(elements, right => {
    let code = 0;
    for (const digit of right) code = 8 * code + left[digit];
    return index[code];
  }));
  const inverse = multiply.map(row => row.indexOf(0));
  return {elements, multiply, inverse};
}

function subgroup(generators, multiply) {
  const found = new Uint8Array(multiply.length);
  const queue = [0];
  found[0] = 1;
  for (const position of queue) {
    for (const generator of generators) {
      const next = multiply[position][generator];
      if (!found[next]) {
        found[next] = 1;
        queue.push(next);
      }
    }
  }
  return queue;
}

function solvable(elements, multiply, inverse) {
  let group = elements;
  while (group.length > 1) {
    const commutators = new Set();
    for (const a of group) {
      for (const b of group) commutators.add(multiply[multiply[multiply[a][b]][inverse[a]]][inverse[b]]);
    }
    const derived = subgroup(commutators, multiply);
    if (derived.length === group.length) return false;
    group = derived;
  }
  return true;
}

function transitive(x, y) {
  const points = [0];
  let seen = 1;
  for (const i of points) {
    for (const j of [x[i], y[i]]) {
      if (!(seen & (1 << j))) {
        seen |= 1 << j;
        points.push(j);
      }
    }
  }
  return points.length === x.length;
}

function* representatives(degree) {
  const {elements, multiply, inverse} = groupTable(degree);
  const count = elements.length;
  const even = elements.map(p => parity(p) === 0);
  const conjugate = (h, a) => multiply[multiply[h][a]][inverse[h]];
  const seenX = new Uint8Array(count);
  for (let a = 0; a < count; a++) {
    if (seenX[a]) continue;
    const centralizer = [];
    for (let h = 0; h < count; h++) {
      const image = conjugate(h, a);
      seenX[image] = 1;
      if (image === a) centralizer.push(h);
    }
    const seenY = new Uint8Array(count);
    for (let b = 0; b < count; b++) {
      if (seenY[b] || !even[b]) continue;
      for (const h of centralizer) seenY[conjugate(h, b)] = 1;
      const x = elements[a], y = elements[b];
      if (!transitive(x, y)) continue;
      const generated = subgroup([a, b], multiply);
      if (generated.length < 60) {
        assert(solvable(generated, multiply, inverse));
        continue;
      }
      yield {x, y, evenX: even[a], order: generated.length};
    }
  }
}

const popcount = new Uint8Array(1 << 14);
for (let i = 1; i < popcount.length; i++) popcount[i] = popcount[i >> 1] + (i & 1);

function matchingFlows(x, y) {
  const degree = x.length;
  const flows = new Set();
  for (let choices = 0; choices < 4 ** degree; choices++) {
    let terms = choices, rows = 0, edges = 0;
    for (let j = 0; j < degree; j++, terms >>= 2) {
      let row = j;
      if (terms & 1) {
        edges |= 1 << (degree + j);
        row = y[row];
      }
      if (terms & 2) {
        edges |= 1 << row;
        row = x[row];
      }
      if (rows & (1 << row)) break;
      rows |= 1 << row;
    }
    if (rows === (1 << degree) - 1) flows.add(edges);
  }
  return [...flows];
}

const exceptions = new Map([
  ["023451/130542", [3, 3776, "413520"]],
  ["0134562/1243650", [1, 128, "0354162"]],
  ["0134562/2340156", [2, 13184, "0561234"]],
]);

function checkCycle(x, y, first, second) {
  const degree = x.length;
  const from = new Map();
  for (let k = 0; k < 2 * degree; k++) {
    if (!((first ^ second) & (1 << k))) continue;
    const site = k % degree, permutation = k < degree ? x : y;
    let start = site, end = permutation[site];
    const reversed = Boolean(first & (1 << k));
    if (reversed) [start, end] = [end, start];
    assert(!from.has(start));
    from.set(start, {end, permutation, reversed});
  }
  const start = Math.min(...from.keys());
  let vertex = start;
  let image = Array.from({length: degree}, (_, i) => i);
  do {
    const edge = from.get(vertex);
    assert(edge);
    from.delete(vertex);
    image = image.map(i => edge.reversed ? edge.permutation.indexOf(i) : edge.permutation[i]);
    vertex = edge.end;
  } while (vertex !== start);
  assert.equal(from.size, 0);
  assert(image.some((j, i) => j !== i));
  return image.join("");
}

function exceptionalCertificate(x, y, flows, recipe) {
  const [c, mask, expected] = recipe;
  const d = x.length;
  const costs = flows.map(f => c * popcount[f & ((1 << d) - 1)]
      + ((7 * c) % 25) * popcount[f >> d] - 25 * popcount[f & mask]);
  const low = Math.min(...costs), high = Math.max(...costs);
  const optimal = flows.filter((_, j) => costs[j] === low).sort((a, b) => a - b);
  assert.equal(optimal.length, 2);
  // Fix a traversal orientation for comparing its projective image with the stored permutation.
  const first = d === 6 ? optimal[1] : optimal[0];
  const other = optimal.find(f => f !== first);
  assert.equal(checkCycle(x, y, first, other), expected);
  assert(4 * (high - low) < 25 * d);
  return {c, mask, end: "low", width: high - low, cycle: expected};
}

function certificate(x, y, flows, n) {
  const d = x.length, block = 1 << d;
  const special = exceptions.get(x.join("") + "/" + y.join(""));
  if (n === 25 && special) return exceptionalCertificate(x, y, flows, special);
  const target = Math.floor((n * d - 1) / 4);
  const step = n === 25 ? 7 : 10;
  for (let c = 1; c < n; c++) {
    const b = step * c % n;
    const base = flows.map(f => popcount[f & (block - 1)] * c + popcount[f >> d] * b);
    const centered = (2 * c > n ? block - 1 : 0) | (2 * b > n ? (block - 1) << d : 0);
    for (let v = 0; v < block * block; v++) {
      const mask = v ^ centered;
      let low = Infinity, high = -Infinity, countLow = 0, countHigh = 0;
      for (let j = 0; j < flows.length; j++) {
        const w = base[j] - n * popcount[mask & flows[j]];
        if (w < low) { low = w; countLow = 1; }
        else if (w === low) countLow++;
        if (w > high) { high = w; countHigh = 1; }
        else if (w === high) countHigh++;
        if (high - low > target) break;
      }
      if (high - low <= target && (countLow === 1 || countHigh === 1)) {
        return {c, mask, end: countLow === 1 ? "low" : "high", width: high - low};
      }
    }
  }
  throw new Error(`No certificate for ${n}: ${x}/${y}`);
}

for (const degree of [6, 7]) {
  const stats = new Map();
  for (const {x, y, evenX, order} of representatives(degree)) {
    const flows = matchingFlows(x, y);
    for (const n of evenX ? [25, 26] : [26]) {
      const key = n + "/" + order;
      const record = stats.get(key) ?? [0, 0];
      record[0]++;
      const proof = certificate(x, y, flows, n);
      record[1] = Math.max(record[1], proof.width);
      if (process.argv.includes("--certificates")) {
        console.log(JSON.stringify({degree, n, order, x: x.join(""), y: y.join(""), ...proof}));
      }
      stats.set(key, record);
    }
  }
  const sorted = [...stats].sort(([a], [b]) => a.localeCompare(b));
  for (const [key, value] of sorted) console.log(degree, key, ...value);
  const count = n => sorted.filter(([k]) => k.startsWith(n + "/"))
      .reduce((sum, [, record]) => sum + record[0], 0);
  const maximum = n => Math.max(...sorted.filter(([k]) => k.startsWith(n + "/"))
      .map(([, record]) => record[1]));
  assert.deepEqual([count(25), count(26), maximum(25), maximum(26)],
      degree === 6 ? [125, 258, 37, 38] : [1030, 2060, 43, 45]);
}


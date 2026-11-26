// Exact prime-field polynomials and all primitive order-26 marked factors.
import assert from "node:assert/strict";

export function mod(x, p) {
  return (x % p + p) % p;
}

export function power(x, exponent, p) {
  let result = 1;
  while (exponent) {
    if (exponent % 2) result = result * x % p;
    x = x * x % p;
    exponent = Math.floor(exponent / 2);
  }
  return result;
}

function trim(poly) {
  while (poly.length && poly.at(-1) === 0) poly.pop();
  return poly;
}

function multiply(first, second, p) {
  if (!first.length || !second.length) return [];
  const result = Array(first.length + second.length - 1).fill(0);
  for (let i = 0; i < first.length; i++) {
    for (let j = 0; j < second.length; j++) {
      result[i + j] = (result[i + j] + first[i] * second[j]) % p;
    }
  }
  return trim(result);
}

function divide(poly, divisor, p) {
  assert.equal(divisor.at(-1), 1);
  const remainder = poly.slice();
  const quotient = Array(Math.max(0, poly.length - divisor.length + 1)).fill(0);
  for (let i = quotient.length - 1; i >= 0; i--) {
    const coefficient = remainder.pop();
    quotient[i] = coefficient;
    for (let j = 0; j < divisor.length - 1; j++) {
      remainder[i + j] = mod(remainder[i + j] - coefficient * divisor[j], p);
    }
  }
  return [trim(quotient), trim(remainder)];
}

function monic(poly, p) {
  const scale = power(poly.at(-1), p - 2, p);
  return poly.map(x => x * scale % p);
}

function gcd(first, second, p) {
  while (second.length) {
    second = monic(second, p);
    [first, second] = [second, divide(first, second, p)[1]];
  }
  return monic(first, p);
}

function powerModuloPolynomial(base, exponent, modulus, p) {
  function reducedProduct(a, b) {
    return divide(multiply(a, b, p), modulus, p)[1];
  }
  let result = [1];
  base = divide(base, modulus, p)[1];
  while (exponent) {
    if (exponent % 2) result = reducedProduct(result, base);
    base = reducedProduct(base, base);
    exponent = Math.floor(exponent / 2);
  }
  return result;
}

function tracePower(y, exponent, p) {
  let a = 2, b = y;
  for (const bit of exponent.toString(2)) {
    const odd = mod(a * b - y, p);
    if (bit === "0") [a, b] = [mod(a * a - 2, p), odd];
    else [a, b] = [odd, mod(b * b - 2, p)];
  }
  return a;
}

function factorWithTraces(phi, p, degree) {
  const traces = [];
  for (let j = 1; j < 13; j++) {
    const trace = Array(13).fill(0);
    for (let i = 0, exponent = j; i < degree; i++, exponent = exponent * p % 13) {
      trace[exponent]++;
    }
    traces.push(trim(trace));
  }

  function split(f) {
    if (f.length === degree + 1) return [f];
    for (let shift = 0; shift < p; shift++) {
      for (const trace of traces) {
        const translated = trace.slice();
        translated[0] = shift;
        const residue = powerModuloPolynomial(translated, (p - 1) / 2, f, p);
        residue[0] = mod((residue[0] || 0) - 1, p);
        const factor = gcd(f, trim(residue), p);
        if (factor.length > 1 && factor.length < f.length) {
          const [quotient, remainder] = divide(f, factor, p);
          assert.equal(remainder.length, 0);
          return [...split(quotient), ...split(factor)];
        }
      }
    }
    throw Error("No proper trace split at prime " + p);
  }
  return split(phi);
}

// First factor Phi_13. The primitive order-26 roots are the negatives
// of the primitive order-13 roots at the odd primes used here.
export function markedFactors(p, degree) {
  const phi = Array(13).fill(1);
  let factors;
  if (degree === 12) {
    factors = [phi];
  } else if (degree === 1) {
    let root = 1;
    for (let a = 2; root === 1; a++) root = power(a, (p - 1) / 13, p);
    factors = Array.from({length: 12}, (_, i) => [mod(-power(root, i + 1, p), p), 1]);
  } else if (degree === 2) {
    let v;
    for (let y = 0; y < p; y++) {
      v = tracePower(y, (p + 1) / 13, p);
      if (v !== 2 && tracePower(v, 13, p) === 2) break;
    }
    factors = Array.from({length: 6}, (_, i) => [1, mod(-tracePower(v, i + 1, p), p), 1]);
  } else {
    factors = factorWithTraces(phi, p, degree);
  }
  assert.equal(factors.length * degree, 12);
  for (const factor of factors) assert.equal(factor.length, degree + 1);
  const marked = factors.map(f => f.map((x, j) => (degree + j) % 2 ? mod(-x, p) : x));
  const target = phi.map((_, j) => j % 2 ? p - 1 : 1);
  assert.deepEqual(marked.reduce((a, b) => multiply(a, b, p), [1]), target);
  return marked;
}

"""Exact actual-law free moments; narrow floating-point kernel diagnostics.

The analytic reduction is in D_F0004 (T10)-(T13). No matrix approximation
to the free law is used. Polynomial tuples store coefficients in r.
"""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import math


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q, sign=1, shift=0):
    out = list(p) + [0] * max(0, len(q) + shift - len(p))
    for k, c in enumerate(q):
        out[k + shift] += sign * c
    return trim(out)


def mul(p, q):
    out = [0] * max(0, len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def normalize(word):
    out = []
    for letter, exponent in word:
        if not exponent:
            continue
        if out and out[-1][0] == letter:
            exponent += out.pop()[1]
        if exponent:
            out.append((letter, exponent))
    return tuple(out)


def cat(*words):
    return normalize(sum((tuple(w) for w in words), ()))


def star(word):
    return tuple((a, -n) for a, n in reversed(word))


def canonical_trace(word):
    word = normalize(word)
    while len(word) > 1 and word[0][0] == word[-1][0]:
        word = normalize(((word[0][0], word[0][1] + word[-1][1]),) + word[1:-1])
    if not word:
        return ()
    return min(word[i:] + word[:i] for i in range(len(word)))


def trace(word):
    return trace_cached(canonical_trace(word))


@lru_cache(None)
def trace_cached(word):
    if not word:
        return (1,)
    if sum(n for a, n in word if a == 0):
        return ()  # exact Haar-gauge invariance
    if len(word) == 1:
        return (0,) * abs(word[0][1]) + (1,)
    # In a centered alternating expansion, only V blocks can be removed:
    # every nonzero U block has zero scalar mean.
    positions = [i for i, (a, _) in enumerate(word) if a == 1]
    out = ()
    for size in range(1, len(positions) + 1):
        for removed in combinations(positions, size):
            removed = set(removed)
            power = sum(abs(word[i][1]) for i in removed)
            remaining = tuple(x for i, x in enumerate(word) if i not in removed)
            out = add(out, trace(remaining), 1 if size % 2 else -1, power)
    return out


def conditional(word):
    degree = sum(n for a, n in word if a == 0)
    return degree, trace(cat(((0, -degree),), word))


def gamma_block(letter, exponent):
    if letter == 0:
        block = ((0, exponent),)
        return [(1, block, ()), (-1, (), block)]
    out = []
    if exponent > 0:
        for k in range(exponent):
            out += [(1, cat(((1, k), (0, 1))), cat(((0, -1), (1, exponent-k)))),
                    (-1, normalize(((1, k),)), normalize(((1, exponent-k),)))]
    else:
        m = -exponent
        for k in range(m):
            out += [(-1, cat(((1, -k-1), (0, 1))), cat(((0, -1), (1, -m+1+k)))),
                    (1, normalize(((1, -k-1),)), normalize(((1, -m+1+k),)))]
    return out


def kernel(word):
    word = normalize(word)
    out = {}
    for index, (letter, exponent) in enumerate(word):
        for sign, left, right in gamma_block(letter, exponent):
            x = cat(star(word), word[:index], left)
            y = cat(right, word[index+1:])
            kx, cx = conditional(x)
            ky, cy = conditional(y)
            assert kx + ky == 0
            mode = abs(ky)  # real symmetric kernel uses cosine
            out[mode] = add(out.get(mode, ()), mul(cx, cy), sign)
    return {k: v for k, v in sorted(out.items()) if v}


def expected(a, n):
    out = {}
    for ell in range(1, n+1):
        p = (0,) * (2*ell) + (1,)
        for mode, sign in [(abs(a*(ell-1)-1), 1), (abs(a*ell), -1)]:
            out[mode] = add(out.get(mode, ()), p, sign)
    return {k: v for k, v in sorted(out.items()) if v}


def evaluate(poly, r):
    out = 0.0
    for c in reversed(poly):
        out = out*r + c
    return out


def scan(coefficients):
    worst = {"negative_ratio": 0.0}
    for r in (0.25, 0.5, math.sqrt(0.75), 0.95):
        sigma2 = 2*r*r/(1-r*r)**2
        values = {k: evaluate(v, r) for k, v in coefficients.items()}
        for j in range(1, 2049):
            theta = math.pi*j/2048
            q = math.fsum(v*math.cos(k*theta) for k, v in values.items())
            ratio = -q/(sigma2*4*math.sin(theta/2)**2)
            if ratio > worst["negative_ratio"]:
                worst = {"negative_ratio": ratio, "r": r,
                         "theta": theta, "q": q}
    return worst


def main():
    checks = 0
    for a in (-2, -1, 0, 1, 2):
        for n in (1, 2, 3, 4):
            assert kernel(((0, a), (1, 1))*n) == expected(a, n)
            checks += 1
    words = {
        "UV_power_3": ((0, 1), (1, 1))*3,
        "U2V_power_4": ((0, 2), (1, 1))*4,
        "commutator_U_V": ((0, 1), (1, 1), (0, -1), (1, -1)),
        "U_V2_Uinv_Vinv": ((0, 1), (1, 2), (0, -1), (1, -1)),
        "U_V_U2_Vinv": ((0, 1), (1, 1), (0, 2), (1, -1)),
        "U_V_Uinv_V_U_Vinv": ((0, 1), (1, 1), (0, -1), (1, 1), (0, 1), (1, -1)),
    }
    results = []
    for name, word in words.items():
        coefficients = kernel(word)
        results.append({"name": name, "word": word,
                        "cosine_coefficients_in_r": coefficients,
                        "floating_scan": scan(coefficients)})
    output = {"exact_known_formula_checks": checks,
              "scan_scope": {"r": [0.25, 0.5, "sqrt(3/4)", 0.95],
                             "theta": "pi*j/2048, j=1,...,2048"},
              "limits": "Exact coefficient recurrence; floating scan is not a proof of any bound.",
              "results": results}
    program = Path(__file__).resolve().parent
    repository = next(parent for parent in program.parents if (parent / "repository/config.json").is_file())
    output_home = repository / "mathematics/computations/outputs" / program.name
    output_home.mkdir(parents=True, exist_ok=True)
    destination = output_home / "results.json"
    temporary = destination.with_name(".results.partial")
    try:
        temporary.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({"checks": checks, "words": len(results),
                      "worst": max(results, key=lambda x: x['floating_scan']['negative_ratio'])}, indent=2))


if __name__ == "__main__":
    main()

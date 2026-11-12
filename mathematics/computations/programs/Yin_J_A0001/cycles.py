"""Exact finite signed color cycles; no actual-group word solver."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

FLIP = str.maketrans("aAbB", "AaBb")


def inverse(word: str) -> str:
    return word.translate(FLIP)[::-1]


def reduce_word(word: str) -> str:
    stack: list[str] = []
    for letter in word:
        if stack and stack[-1] == inverse(letter):
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


def representative(word: str) -> str:
    word = reduce_word(word)
    while len(word) > 1 and word[0] == inverse(word[-1]):
        word = word[1:-1]
    if not word:
        return ""
    return min(v[i:] + v[:i] for v in (word, inverse(word)) for i in range(len(v)))


def proper_cycles(n: int):
    def extend(colors: tuple[int, ...]):
        if len(colors) == n:
            if colors[-1] != colors[0]:
                yield colors
            return
        for color in range(3):
            if not colors or color != colors[-1]:
                yield from extend(colors + (color,))
    yield from extend(())


def proper_power(word: str):
    for length in range(1, len(word) // 2 + 1):
        if len(word) % length == 0 and word == word[:length] * (len(word) // length):
            return {"root": representative(word[:length]), "exponent": len(word) // length}
    return None


def cycle_table(n: int) -> dict:
    signed: Counter[str] = Counter()
    unsigned: Counter[str] = Counter()
    for colors in proper_cycles(n):
        letters = ["", "a", "b"]
        word = "".join(letters[c] if i % 2 else inverse(letters[c]) for i, c in enumerate(colors))
        key = representative(word)
        sign = (-1) ** colors.count(2)
        signed[key] += sign
        unsigned[key] += 1
    total = sum(unsigned.values())
    assert total == 2**n + 2, (n, total)
    assert "" not in unsigned
    assert all(abs(signed[w]) == unsigned[w] for w in unsigned)
    rows = [{"word": w, "signed_multiplicity": signed[w], "unsigned_multiplicity": unsigned[w],
             "a_occurrences": w.lower().count("a"), "b_occurrences": w.lower().count("b"),
             "proper_power": proper_power(w)} for w in sorted(unsigned, key=lambda w: (len(w), w))]
    return {"length": n, "color_count": total, "classes": len(rows),
            "positive_count": sum(v for v in signed.values() if v > 0),
            "negative_count": -sum(v for v in signed.values() if v < 0), "rows": rows}


def tree_moments(depth: int) -> list[int]:
    current = {0: 1}
    result = [1]
    for step in range(1, 2 * depth + 1):
        nxt: Counter[int] = Counter()
        for height, count in current.items():
            if height:
                nxt[height - 1] += count
            nxt[height + 1] += count * (3 if height == 0 else 2)
        current = nxt
        if step % 2 == 0:
            result.append(current[0])
    return result


def weighted_certificate(m: list[int]) -> dict:
    f = Fraction
    moments = [f(m[j]) - f(m[j + 1], 9) for j in range(5)]
    aa, bb, cc = moments[2:5]
    rr, ss = -moments[1], -moments[2]
    determinant = aa * cc - bb * bb
    x, y = (rr * cc - ss * bb) / determinant, (aa * ss - bb * rr) / determinant
    q = [f(1), x, y]
    square = [sum((q[i] * q[j] for i in range(3) for j in range(3) if i + j == k), f(0)) for k in range(5)]
    polynomial = square + [f(0)]
    for k, value in enumerate(square):
        polynomial[k + 1] -= value / 9
    value = sum(polynomial[j] * m[j] for j in range(6))
    assert value == moments[0] + x * moments[1] + y * moments[2]
    return {"q_coefficients": list(map(str, q)), "p_coefficients": list(map(str, polynomial)),
            "weighted_moment_determinant": str(determinant), "free_moment_value": str(value),
            "p_at_one": str(sum(polynomial)), "coefficient_of_m5": str(polynomial[-1])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lengths", type=int, nargs="+", default=[4, 6, 8, 10, 12])
    args = parser.parse_args()
    if any(n < 4 or n % 2 or n > 20 for n in args.lengths):
        parser.error("lengths must be even integers from 4 through 20")
    tables = [cycle_table(n) for n in args.lengths]
    moments = tree_moments(6)
    result = {"scope": "Exact free cyclic classes only; no actual-group relation assertions.",
              "tables": tables, "tree_moments": moments, "weighted_certificate": weighted_certificate(moments)}
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name
    output.mkdir(parents=True, exist_ok=True)
    destination = output / "cycles.json"
    staging = output / "cycles.json.pending"
    staging.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    staging.replace(destination)
    for table in tables:
        print({key: table[key] for key in ("length", "color_count", "classes", "positive_count", "negative_count")})
    print("tree_moments", moments)
    print("weighted_certificate", result["weighted_certificate"])
    print("output", destination)


if __name__ == "__main__":
    main()

"""Exact trinomial-preserving orbits and bounded Nielsen certificate search.

This is a free-word calculation, not an actual-group word solver.
Every reported Nielsen path must still be interpreted in a mathematical proof.
"""
from __future__ import annotations

from collections import deque
import json
from pathlib import Path

from cycles import cycle_table, inverse, reduce_word, representative


def substitute(word: str, images: tuple[str, str]) -> str:
    mapping = dict(zip("ab", images))
    mapping.update({inverse(k): inverse(v) for k, v in tuple(mapping.items())})
    return representative("".join(mapping[letter] for letter in word))


SYMMETRIES = (("A", "Ab"), ("A", "B"))
NIELSEN = (("b", "a"), ("A", "b"), ("a", "B"),
           ("ab", "b"), ("aB", "b"), ("ba", "b"), ("Ba", "b"),
           ("a", "ba"), ("a", "bA"), ("a", "ab"), ("a", "Ab"))


def orbits() -> list[list[str]]:
    words = {r["word"] for r in cycle_table(10)["rows"] if r["signed_multiplicity"] < 0}
    remaining = set(words)
    answer = []
    while remaining:
        first = min(remaining)
        orbit = {first}
        queue = [first]
        while queue:
            word = queue.pop()
            for images in SYMMETRIES:
                other = substitute(word, images)
                if other not in orbit:
                    orbit.add(other)
                    queue.append(other)
        assert orbit <= words
        remaining -= orbit
        answer.append(sorted(orbit))
    return sorted(answer, key=lambda row: (min(map(len, row)), row))


def nielsen_certificate(start: str, max_length: int = 10, max_nodes: int = 20000):
    targets = {representative("a"): {"kind": "cyclic"}}
    targets[representative("aaBBB")] = {"kind": "common_two_three"}
    for k in (-3, -2, -1, 1, 2, 3):
        power = "A" * k if k > 0 else "a" * (-k)
        target = representative("baB" + power)
        targets[target] = {"kind": "cyclic_normalizer", "k": k}
    queue = deque([start])
    predecessors = {start: None}
    while queue and len(predecessors) <= max_nodes:
        word = queue.popleft()
        if word in targets:
            path = []
            current = word
            while predecessors[current] is not None:
                previous, images = predecessors[current]
                path.append({"before": previous, "images": images, "after": current})
                current = previous
            path.reverse()
            assert all(substitute(step["before"], tuple(step["images"])) == step["after"] for step in path)
            original_images = ["a", "b"]
            for step in path:
                mapping = dict(zip("ab", step["images"]))
                mapping.update({inverse(k): inverse(v) for k, v in tuple(mapping.items())})
                original_images = [reduce_word("".join(mapping[x] for x in w)) for w in original_images]
            return {"target": word, **targets[word], "path": path,
                    "original_images": original_images,
                    "visited": len(predecessors)}
        for images in NIELSEN:
            other = substitute(word, images)
            if len(other) <= max_length and other not in predecessors:
                predecessors[other] = (word, images)
                queue.append(other)
    return {"kind": "not_found", "visited": len(predecessors),
            "scope": "No conclusion outside this bounded free-word search."}


def main() -> None:
    rows = cycle_table(10)["rows"]
    exceptional = {r["word"] for r in rows if r["unsigned_multiplicity"] != 10}
    assert exceptional == {"AAAAA", "BBBBB", "AbAbAbAbAb"}
    assert all(r["unsigned_multiplicity"] == 2 for r in rows if r["word"] in exceptional)
    assert sum(r["signed_multiplicity"] < 0 for r in rows) == 50
    table = []
    for orbit in orbits():
        start = min(orbit, key=lambda word: (len(word), word))
        certificate = nielsen_certificate(start)
        table.append({"orbit": orbit, "start": start, "certificate": certificate})
        print(start, len(orbit), certificate["kind"], certificate.get("k"),
              len(certificate.get("path", [])), certificate["visited"])
    directory = Path(__file__).resolve().parent
    output = directory.parent.parent / "outputs" / directory.name / "ten-cycle-orbits.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = output.with_suffix(".json.pending")
    staging.write_text(json.dumps({"max_length": 10, "max_nodes": 20000,
                                   "exceptional_multiplicity_classes": sorted(exceptional),
                                   "orbits": table}, indent=2) + "\n", encoding="utf-8")
    staging.replace(output)
    print("output", output)


if __name__ == "__main__":
    main()

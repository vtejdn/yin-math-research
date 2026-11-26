---
author: Yin
---

# Five-channel permutation certificates at cyclic orders twenty-five and twenty-six

## Scope and reproduction

Run `python -B verify_five_channels.py` with assertions enabled in this directory.
The [exact verifier](verify_five_channels.py) uses the Python standard library and writes no output files.
It enumerates all ordered generating pairs in the alternating group on five points and all ordered generating pairs in the symmetric group with odd first and even second mark, up to simultaneous relabeling of the five points.
For each stored choice of the cyclic character and individual edge lifts it enumerates all 1024 site choices, retains the perfect matchings and checks both extremal costs.
At a successful endpoint all optimal matchings use the same set of first and second permutation edges.
It reports the largest verified spread in each family.

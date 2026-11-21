---
author: Yin
---
# Fixed-depth endpoint capacities for the Gardam triples

The [verifier](verify.py) uses Python 3.10 or later and only its standard library.
Its explicit retained inputs are [J_A0006/verify.py](../Yin_J_A0006/verify.py), for the seven triple labels, and that file's existing dependency [J_A0005/verify.py](../Yin_J_A0005/verify.py), for the exact rewriting rules.
Run with assertions enabled:

~~~text
python -B mathematics/computations/programs/Yin_J_A0007/verify.py
~~~

The program writes no files and requires no downloaded sources, temporary scripts or saved search outputs.
Dependencies resolve relative to the program rather than the caller's working directory.
The [Claim](../../../claims/Yin_C_A0106_v3.md#statement) proves the arbitrary-radius capacity bounds and identifies the unchanged geometric input for the two-label corollary.

The exact scope is fixed: even paths of lengths zero through sixteen from a left root, and odd paths of lengths one through seventeen from a right root.
No command-line depth extension is supplied.
Normal forms use the existing complete rules with a cache limited to 50,000 entries, cleared between root cases.
Paths are counted by endpoint and final color, then aggregated by endpoint across the allowed lengths.
Different paths remain counted when their endpoints coincide.

The full maintained run checks the following histograms separately for all seven triples:

| Root | Multiplicity 1 | Multiplicity 2 | Multiplicity 3 | Distinct endpoints | Paths |
| --- | ---: | ---: | ---: | ---: | ---: |
| Left | 126,397 | 2,238 | 66 | 128,701 | 131,071 |
| Right | 250,257 | 5,577 | 244 | 256,078 | 262,143 |

It checks the total path count at each intermediate pair of steps.
It also verifies that all 127 left-root short endpoints through length six, and all 63 right-root short endpoints through length five, have multiplicity one in the final families.
The corresponding finite-subgraph arguments force at least 22 and 21 of these endpoints into any candidate right support; the program checks the arithmetic of the resulting bounds \(361\) and \(655\).
Pure pairing then forces even support size below \(655\), also excluding \(361\).

Together with the previously established nonexceptional cases, every nonzero coefficient supported on the seven positive generators has no finite right annihilator of support size at most \(361\), with no bound on that support's word lengths.
The finite program does not claim a result for unbounded depth or unrestricted right-support size.

A single retained triple can be checked with:

~~~text
python -B mathematics/computations/programs/Yin_J_A0007/verify.py --triple afg
~~~

That invocation checks only the selected triple.
The code reruns J5's finite overlap and presentation checks, but not its large rectangle searches.
It does not rerun J6's subgroup index or abelianization calculations.
Successful development execution is not an independent review.

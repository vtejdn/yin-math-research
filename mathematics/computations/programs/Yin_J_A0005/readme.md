---
author: Yin
---
# Exact Gardam word balls and bounded unique products

The [verifier](verify.py) uses Python 3.10 or later and only its standard library.
Run it with assertions enabled:

~~~text
python -B mathematics/computations/programs/Yin_J_A0005/verify.py
~~~

The command works from the repository root; an absolute path or a local invocation from this directory works as well.
The program writes no files and requires no downloaded source or root temporary script.
Its sole retained cross-J input is [J_A0004/verify.py](../Yin_J_A0004/verify.py), which supplies the appendix lists, relators and finite-quotient partition.
That file is loaded explicitly relative to this program, independently of the current working directory.
The mathematical justification is [C_A0105_v2](../../../claims/Yin_C_A0105_v2.md#statement).

The maintained implementation has completed all checks included in the default invocation:

- The 98 rules generated from the seven triangles have no conflicting left-hand sides.
  All 560 overlapping pairs among the \(14^3\) three-letter words join.
- Free substitution identifies the seven-triangle and two-generator presentations in both directions.
- Exact breadth-first balls of radii zero through eight have sizes \(1,5,17,53,161,467,1311,3637,9929\).
- The exact 32-by-28 appendix product partition equals J_A0004's 336 buckets, cell by cell.
- No nonempty row/column subrectangle without a unique product survives in the five ranges below.

| Radius pair | Pairs of maxima searched | States processed |
| --- | ---: | ---: |
| \((1,8)\) | 3,073 | 10,633 |
| \((2,7)\) | 10,011 | 107,980 |
| \((3,6)\) | 17,662 | 598,738 |
| \((4,4)\) | 6,894 | 188,790 |
| \((4,5)\) | 23,709 | 2,785,704 |

The pure partner search fixes maximal row and column indices and memoizes the required label sets separately within each such choice.
It uses no torsion or support-size filter.
The integer sorting key only determines a reproducible exploration order; it supplies no orderability hypothesis on the group.
The code returns a surviving rectangle if one exists and fails the exclusion assertion rather than reporting it as excluded.
The counts above are diagnostics of the completed exhaustive runs; soundness does not depend on their particular values.

Nesting and inversion imply unique products for every pair of subsets of \(B_r,B_s\) with \(r+s\le9\).
A single chosen pair can be tested using, for example,

~~~text
python -B mathematics/computations/programs/Yin_J_A0005/verify.py --pair 4 4
~~~

A one-pair invocation reruns the rewriting, ball and appendix checks but does not recheck the other radius pairs.
An additional chosen pair supplies evidence only after its search completes successfully.
The largest retained slice can be reproduced separately with `--pair 4 5`; it takes substantially longer than the \((4,4)\) slice.

The triangle input is from [Gardam, Warwick slide 12](../../../literature/pdf/Gar21c.pdf#page=12).
The two-generator presentation and appendix lists are those of [Mian–Siddique, arXiv v1, pp. 2 and 10](../../../literature/pdf/MS26b--arxiv-v1.pdf).
The verifier does not run Lean or import the source authors' search programs.
The termination, confluence, presentation and search arguments are given in the linked Claim; successful execution is not an independent mathematical review.

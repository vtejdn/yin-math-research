---
author: Yin
---
# Finite certificates for the seven collinear Gardam triples

The [verifier](verify.py) uses Python 3.10 or later, its standard library, and the exact normal-form code retained in [J_A0005/verify.py](../Yin_J_A0005/verify.py).
Run with assertions enabled:

~~~text
python -B mathematics/computations/programs/Yin_J_A0006/verify.py
~~~

Its cross-J input is loaded by an explicit path relative to this program, independently of the working directory.
No temporary script, downloaded original, external algebra package, coset enumerator or generated data file is needed.
It writes no files.
The [proof and precise scope](../../../claims/Yin_C_A0106_v2.md#statement) explain the mathematical deductions from the checks.

The maintained full run has completed for \(bdg,bcf,afg,acd,ceg,abe,def\).
For every triple it checks:

- Distinct endpoints for all nonbacktracking paths of length at most eleven from the left identity, giving 6,142 vertices.
- An explicit simple cycle of length 24, hence exact bipartite girth 24.
- A six-state permutation action satisfying both group relators and fixing the two ratio generators at the base state.
- Twelve explicit normal-form identities expressing the Schreier generators in those two ratios, proving the exact index six.
- A freely reduced length-sixteen relation in the two ratios.
- The twelve-by-seven integral boundary matrix of the verified Schreier cover and its Smith diagonal \(1,1,1,1,1,4,28\).

The resulting subgroup abelianization is \(C_4\oplus C_{28}\) in all seven cases.
The graph proof gives necessary right-support size \(126\) for a rectangle with no unique product, and \(189\) if it has any triple fiber.
These are necessary bounds, not examples attaining them or searches through all supports of those sizes.

The six-state tables, representatives, twelve Schreier words and two half-cycle paths are the retained short certificates.
Their exploratory searches are unnecessary for reproduction.
The verifier rebuilds the homology matrices from the tables and original relators; it does not trust a saved Smith-form result without integer reduction.
The exact normal form is reused from J5, whose finite overlap and presentation checks are rerun here.
The much larger J5 word-ball rectangle searches are not rerun.

A single retained case can be checked separately:

~~~text
python -B mathematics/computations/programs/Yin_J_A0006/verify.py --triple afg
~~~

That command covers only the selected triple.
The mathematical corollary for arbitrary nonzero coefficients supported on the seven positive generators and arbitrary right supports of size at most 125 combines these checks with C106v1 and the explicitly stated geometric infinite-order argument for two labels.
The finite program alone does not audit the external building or nonlinearity assertions.
No independent review is claimed by this development run.

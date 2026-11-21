---
author: Yin
---
# Independent review of the precision bound for trace-zero idempotents

An agent outside the development of C94 v1 inspected the entire proof and its necessary sources for Yin at 03:58 UTC on 21 November 2026.
The reviewer received the mathematical artifacts and scope without development discussions, author explanations or earlier findings about this proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0094_v1.md#statement) | Uniform bounds in the support, prime and precision, and the exact small-support cases. |
| [Whole finding](#whole-finding) | [Characteristic-zero obstruction](../../claims/Yin_C_A0094_v1.md#the-characteristic-zero-obstruction) | Range projection, faithful trace and vanishing of the idempotent. |
| [Whole finding](#whole-finding) | [Integral coefficient scheme](../../claims/Yin_C_A0094_v1.md#the-integral-coefficient-scheme) | The marked group table, certificate height, full divisibility and asymptotic consequence. |
| [Whole finding](#whole-finding) | [Small supports](../../claims/Yin_C_A0094_v1.md#the-exact-one--and-two-label-cases) | Exhaustive classification for at most two labels and all cyclic examples. |
| [Whole finding](#whole-finding) | [Defects](../../claims/Yin_C_A0094_v1.md#application-to-defects-of-approximate-one-sided-inverses) | Idempotence, zero identity coefficient and support bound for the defect modulo \(p^e\). |

## Whole finding

The whole argument proves \(e\log p\le H(k)\) uniformly for actual group tables with at most \(k\) distinct labels away from the identity.
For a complex idempotent \(F\), its orthogonal range projection \(P\) satisfies \(PF=F\) and \(FP=P\).
Thus the coefficient at the identity equals \(\tau(P)\), and faithfulness rules out a complex solution having a marked nonzero coefficient.
For an idempotent modulo \(p^e\), divisibility of every coefficient by \(p\) would give \(f=f^e\in p^e(\mathbb Z/p^e)[G]=0\).

The \(k+1\) coefficient and marking variables give at most \(k^2+k+1\) equations of degree at most two.
Only two ordered products can contribute the same off-diagonal quadratic monomial, so the logarithmic height is at most \(\log 2\).
The integral ideal consequently contains a nonzero integer of logarithmic height at most \(H(k)\), by the stated arithmetic Nullstellensatz with these parameters.
The review checked the coefficient-height convention, integer certificate, prefactor \(4n(n+1)d^n\) and logarithmic terms directly in the original theorem, whose proof was accepted as an external input. [Krick, Pardo and Sombra, arXiv v1, Theorem 1, p. 2](https://arxiv.org/pdf/math/9911094v1#page=2).
Evaluation with \(Y=x_j^{-1}\) gives divisibility by the full \(p^e\).
The bound \(H(k)=O(2^k k^3\log(k+2))\) gives (4) by taking logarithms when \(k\le(\log T)/\log 2\), and larger \(k\) already satisfies the claimed lower bound.

Reduction modulo \(p\) and the one-label obstruction force both coefficients of a two-label example to be units.
Group cancellation then gives \(h^2=g\) and \(g^2=h\), hence \(g\) has order three.
The identity coefficient \(2xy\) forces \(p^e=2\), and direct multiplication verifies the unique form in (3).
In the cyclic group of order \(p^e+1\), the counts of ordered nonidentity pairs are \(p^e\) at the identity and \(p^e-1\) elsewhere, giving each stated example, including the three-label example in characteristic three.
These examples have torsion, and the optimal support-dependent bound remains undetermined.

For \(D_e=1-B_eA\), the identity \(D_e^2-D_e=B_e(AB_e-1)A\) and cyclicity of the identity coefficient give both required congruences.
A nonzero reduction modulo \(p\) provides the marked unit away from the identity, and the remaining support is contained in \((\operatorname{supp}B_e)(\operatorname{supp}A)\).
These arguments allow the tables and coefficients to vary with precision.

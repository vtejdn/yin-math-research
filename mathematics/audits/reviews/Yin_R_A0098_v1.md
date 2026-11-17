---
author: Yin
---

# A summable schedule of weighted moments and two whole-group examples

At 2026-11-17T02:43 UTC an agent outside the development of Yin_C_A0062_v1 independently reviewed its fixed statement and three proof sections for Sheng Yin.
The reviewer had previously inspected the dyadic projection criterion and the trace input for the four-line groups.
The reviewer read the present argument and checked its new examples and external local-limit input without receiving development dialogue, author explanations or an earlier finding on the claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0062_v1.md#statement) | Existential and prescribed schedules, finite moment inputs, explicit spatial tail bound, sharp power-law thresholds and the groups and coefficients of the two examples. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0062_v1.md#argument) | Increment and error norms, one-sided convolution on each tail, endpoint multiplier, dyadic constants, spectral-mass asymptotics and summability. |
| [Whole-argument finding](#whole-argument-finding) | [Rational construction](../../claims/Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group) | The two noncommuting polynomials, positive comparisons, scalar subgroup recovery, range, kernel, exponential tails and independent row and column translations. |
| [Whole-argument finding](#whole-argument-finding) | [Generating walk](../../claims/Yin_C_A0062_v1.md#the-spectral-edge-of-the-generating-walk) | Local-limit hypotheses, normalization, moment-ratio argument, second exponent and the shared kernel and support conclusions. |
| [Whole-argument finding](#whole-argument-finding) | [Dyadic test](../../claims/Yin_C_A0057_v1.md#argument) | Finite fourth difference, contraction on Fourier coefficients and comparison to the weighted spatial moment of the projection. |
| [Whole-argument finding](#whole-argument-finding) | [Spatial integrality](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Integrality of the unnormalized trace from an exponent strictly above three on a good four-line group. |
| [Whole-argument finding](#whole-argument-finding) | [Inverse approximation](../../claims/Yin_C_A0058_v1.md#bounded-rational-inverses-have-exponential-tails) | Geometric norm approximation with linearly growing propagation yields an exponentially weighted Fourier square sum. |

## Whole-argument finding

The return part of each bracket is the squared trace-\(L^2\) norm of the difference of the two powers, including their matrix indices.
Forward telescoping to the \(L^2\) limit bounds each error by the sum of later increments.
After weighting by \(2^{\beta j/2}\), the shift by \(h\) has the summable factor \(2^{-\beta h/2}\), giving the same bound on every tail \(j\ge J\).
The reverse bound follows from the two successive errors.
For each endpoint moment the weighted coefficient multiplier is contractive, so replacing a power by the projection changes the square root of that moment by at most the current error.
These observations prove the fixed-schedule equivalence and allow a sufficiently accurate subsequence for the existential assertion.
Computing any one term uses only finite product comparisons and the lengths of their endpoints, whereas choosing a convergent schedule by this existence argument uses convergence to the projection.

For \(2^j\le r<2^{j+1}\) the fourth-difference weight at \(2^{-j}\) is at least \((1-e^{-1})^4\).
Each \(r\ge R\) therefore charges only an index \(j\ge\lfloor\log_2 R\rfloor\), and the two squared errors cost at most the factor \(2\) in (2).
The squared norm bound for forward telescoping gives exactly the stated denominator \((1-2^{-\beta/2})^2\).
For \(k_j=j+1\), finite propagation instead bounds the weighted endpoint term alone by a constant times \((j+1)^4 2^{-(4-\beta)j}\).
This explains why its summability by itself certifies no spatial decay.

The spectral mass away from zero gives the entire squared error.
Integrating the exponential upper envelope gives \(O(k^{-\alpha})\), and restricting to \(0<t\le1/(4k)\) gives a matching lower bound when the two-sided mass estimate holds.
Thus for a projection satisfying the spatial criterion, the weighted increment condition is sharp even for a prescribed irregular increasing schedule.
For a geometric schedule the boundary \(\kappa\alpha=\beta\) gives divergence.
An exponential spatial square moment also supplies the fourth moment needed for the displayed geometric-series remainder estimate.

The binary zero divisors exclude abelianness of the torsion-free group.
Distinct coefficients on all generators make the conjugation stabilizer of \(U\) central, giving \(UV\ne VU\) for the selected \(u\).
The positive comparison involving \(x=1-u\) is valid as a quadratic-form inequality without commuting the generating walk with \(u\).
Trace monotonicity for lower spectral cuts follows from trivial intersection with the complementary upper cut and the dimension inequality for projections.
The cyclic-shift distribution therefore gives the square-root mass law for \(Y\), with zero kernel and spectral accumulation at zero.
The nonzero coefficient at \(u\) and the affiliated inverse of \(1-u\) recover \(P\) inside any subgroup algebra containing \(Y\).
Taking a positive root and using the nonzero identity coefficient also handles the power and its translations.

The triangular row matrix \(T\) has the stated bounded right inverse.
Its multiplication on the left by \(\operatorname{diag}(1,Y^d)\) produces a dense nonclosed range, and comparison of \(A_dA_d^*\) with \(\operatorname{diag}(1,Y^{2d})\) gives the exponent \(1/(4d)\).
The kernel column \(W=(UV,-V,I)^t\) has the indicated order of the factors, and \(W^*W\ge I\) gives a bounded inverse with exponential Fourier square tails.
The polar isometry of \(W\) gives trace one for the projection.
The single generating entry \(U\) suffices for the translated support test on the input.
For the projection, the identity coefficient of \(D=p_{33}\) first places the translated conjugate of \(D\) in the subgroup algebra.
Multiplication by its inverse recovers the translate of \(V\) from \(p_{23}\), forcing the subgroup to contain a conjugate of every generator.
The translations here are independent multiplications by elements of \(G\) on the rows and columns.

The lazy walk is positive, symmetric, finitely supported, admissible and aperiodic on the fixed non-elementary hyperbolic group.
For \(z=P/\|P\|\), the all-time return estimate at the identity consequently gives \(m_k\asymp k^{-3/2}\) and \(m_{2k}/m_k\to2^{-3/2}\). [Gou14, Theorem 1.1, author preprint](../../literature/pdf/Gou14--arxiv-v1.pdf#page=2)
In particular the upper edge carries no atom.
The edge interval of width \(1/k\) has mass bounded above by a constant times \(m_k\), and that of width \(b/k\) has mass at least \(m_{2k}-e^{-b}m_k\).
Fixing \(b\) sufficiently large and interpolating by monotonicity gives two-sided mass of order \(t^{3/2}\).
The same Gram comparison now yields \(3/(4d)\) and leaves the kernel projection unchanged.
The first example has rational coefficients, while the second uses the spectral radius of the particular generating walk.

The argument supports both examples and the single-series criterion at the stated scopes.
No universal convergence schedule or spatial decay for arbitrary nonclosed-range kernels follows from the four-line pair counts.

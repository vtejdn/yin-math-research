---
author: Yin
---

# An ordinary affine pencil for the Brown measure of a scalar polynomial

<a id="statement"></a>
## The root measure of the cyclic pencil

Fix a scalar noncommutative polynomial \(P\) and let \(D=\max(1,\deg P)\), taking \(D=1\) for a constant, including zero.
There are an integer \(m\ge D\) and a single affine pencil
\[
 T(x)=A_0\otimes 1+\sum_{j=1}^d A_j\otimes x_j,\qquad A_j\in M_m(\mathbb C),
\]
with the following properties.
For every \(N\), every matrix tuple \(X\) of size \(N\), and every \(t\in\mathbb C\),
\[
 \det(tI_{mN}-T(X))=t^{(m-D)N}\det(t^D I_N-P(X)).
 \tag{1}
\]
An exponent zero denotes the constant polynomial one.
Let \(b\) be any bounded tuple in a finite tracial von Neumann algebra with normalized faithful normal trace \(\tau\).
For every \(t\ne0\), with \(\tau_m=\operatorname{tr}_m\otimes\tau\) normalized and \(\log 0=-\infty\),
\[
 \log\Delta_{\tau_m}(tI_m-T(b))
 =\frac{m-D}{m}\log|t|+\frac1m\log\Delta_\tau(t^D-P(b)).
 \tag{2}
\]

Write \(\mathcal R_D\nu\) for the probability measure obtained by spreading the mass at each \(w\) equally among the \(D\) roots of \(t^D=w\), counting multiplicities.
Write \(\mu\) for the normalized empirical eigenvalue measure in finite dimension and for the Brown measure with the indicated trace in the von Neumann algebra.
In both settings,
\[
 \mu_{T}=\left(1-\frac Dm\right)\delta_0+\frac Dm\,\mathcal R_D\mu_P .
 \tag{3}
\]
In particular \(\mu_T(\{0\})=1-D/m+(D/m)\mu_P(\{0\})\).
For every coupling in the [two-moment Wigner contract](../tasks/Yin_T_F0012_v3.md#contract), the events of full-sequence weak convergence to the free Brown measure for \(P(W)\) and for \(T(W)\) coincide.
The pencil uses the original matrices in every occurrence of their colors.

<a id="construction"></a>
## Rectangular factors with the same number of steps

When \(D=1\), take \(T=P\) and \(m=1\).
For \(D\ge2\), index the \(q\) nonzero monomials by \(a\), write their coefficients as \(c_a\), and pad each ordered word on the right with identities to length \(D\).
Write \(h_{a,j}\) for the variable or identity at its \(j\)-th position.
Set \(B_1=(c_a h_{a,1})_a\) as a row, \(B_D=(h_{a,D})_a\) as a column, and \(B_j=\operatorname{diag}_a(h_{a,j})\) for \(1<j<D\).
Their ordered product is \(P\), including its constant term.
Use \(D\) successive spaces of widths \(1,q,\ldots,q\), hence \(m=1+(D-1)q\).
In the block matrix \(T\), place \(B_j\) in position \((j,j+1)\) for \(j<D\) and \(B_D\) in position \((D,1)\), with all other blocks zero.
Every entry is affine in the original tuple.

<a id="argument"></a>
## Ordinary shifts and the free determinant

For \(t\ne0\), the pivot on the last \(D-1\) spaces of \(tI_m-T\) is upper triangular with diagonal \(tI\).
Its inverse is a finite triangular series, so the Schur complement on the first space is \(tI-t^{-(D-1)}B_1\cdots B_D\).
The finite determinant of the pivot contributes \(t^{(m-1)N}\).
The first-space determinant contributes \(t^{-(D-1)N}\det(t^D I_N-P(X))\), giving (1) everywhere by polynomial identity.
The same elimination in \(M_m(\mathbb C)\overline\otimes\mathcal M\) uses invertible unit triangular factors of Fuglede--Kadison determinant one.
Apply [bounded multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) and add the diagonal logarithms with weights equal to the normalized block widths.
The pivot contributes \((m-1)\log|t|/m\), and the scalar Schur block contributes \((\log\Delta_\tau(t^D-P(b))-(D-1)\log|t|)/m\).
This proves (2) also when the latter determinant vanishes.
The \(D=1\) identities are immediate.

The roots of (1) give (3) with algebraic multiplicities in finite dimension.
For a bounded free evaluation, the product of \(t-u\) over all roots \(u^D=w\) equals \(t^D-w\).
Thus the logarithmic potential of the right side of (3) agrees at every \(t\ne0\) with (2), by the potential formula for the Brown measure of \(P(b)\).
Both potentials are locally integrable on the entire plane.
Agreement off one point gives the same distributional Laplacian there and at zero, proving (3) on the whole plane.
This proves the stated zero-atom formula without evaluating a difference of infinite logarithms.

<a id="weak"></a>
## Equivalence of the full-sequence limits

Formula (3) makes both pencil laws invariant under multiplication by every \(D\)-th root of unity.
For any bounded continuous \(f\), the function \(w\mapsto D^{-1}\sum_{u^D=w}f(u)\) is bounded and continuous.
Local continuous branches give continuity away from zero, and every root has modulus \(|w|^{1/D}\) at the origin limit.
Consequently \(\nu\mapsto\mathcal R_D\nu\) preserves weak convergence.
Conversely pushing (3) forward by \(t\mapsto t^D\) gives \((1-D/m)\delta_0+(D/m)\mu_P\).
Applying these two continuous operations on each realization proves the equivalence on a single event for all bounded continuous real tests, with no choice of good dimensions or assumption on the coupling.

The earlier [word-chain identity](../ledger/Yin_L_F0061_v2.md#linearization-transfer) puts its parameter in one corner, and the [three-factor cyclic calculation](../ledger/Yin_L_F0063_v2.md#cyclic-global-area) treats an already factored product.
Here \(tI_m-T\) has an ordinary scalar shift on all coordinates for a single fixed pencil, and the root averaging recovers its entire law.
Full-sequence weak convergence for this family of ordinary pencils would therefore settle the scalar contract.
A pointwise determinant upper limit can be attained on different subsequences and leaves the full-sequence weak limit open, as the [alternating-shift example](../ledger/Yin_L_F0061_v2.md#brown-nonimplication) demonstrates.

<a id="example"></a>
## A constant and two words of different degrees

For \(P=1+x_1^2x_2+x_2x_1\), take \(B_1=(1,x_1,x_2)\), \(B_2=\operatorname{diag}(1,x_1,x_1)\) and \(B_3=(1,x_2,1)^{\mathsf T}\).
Their product keeps both copies of \(x_1\) in the cubic word and the order of the quadratic word.
Here \(D=3,m=7\), so (1) gives \(t^{4N}\det(t^3I_N-P(X))\).
The pencil law has the explicit summand \(4\delta_0/7\), and the remaining \(3/7\) of its mass is the three-root average of the scalar law.

## Current assessment
[Selected decision](#decision-cyclic-reviewed)

## Assessment history

### Decision cyclic-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:49 |
| status | open |
| reason | Block elimination and averaging over polynomial roots give a deterministic reduction for independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Ordinary cyclic pencil](#statement) | Finite and free laws, zero mass and pathwise equivalence under every coupling. |
| argument | [Elimination and Brown measure](#argument) | Rectangular factors, trace weights, infinite negative logarithms and the origin. |
| support | [Full-sequence equivalence](#weak) | Continuous forward and inverse operations on the pencil laws. |
| support | [Unequal word lengths](#example) | A repeated color, a lower-degree term and a constant. |

### Decision cyclic-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:53 |
| status | proved |
| reason | The ordinary-shift Schur identity yields the finite and free root measures and the exact coupling-wise weak convergence equivalence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed theorem](#statement) | The ordinary-shift Schur identity yields the finite and free root measures and the exact coupling-wise weak convergence equivalence. |
| argument | [Complete proof](#argument) | The stated parameter, normalization and coupling requirements. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0367_v1.md#cyclic-whole-proof) | Entire fixed statement and its exact scope. |

---
author: Yin
---

# Maximal linear density and the geometric criterion for a normal scalar vacuum

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

For a compactly supported Borel probability measure \(\mu\) on \(\mathbb C\), put
\[
 M_1\mu(z)=\sup_{r>0}\frac{\mu(B(z,r))}{r},\qquad
 G(\mu)=\int (M_1\mu)^2\,d\mu+
        \iiint \kappa(z,w,v)^2\,d\mu(z)d\mu(w)d\mu(v).
\]
Here \(\kappa\) is the reciprocal circumradius, zero on repeated or collinear triples.
Let \(Z\) be multiplication by the coordinate in the abelian tracial algebra \(L^\infty(\mu)\).
Its actual scalar conjugate variable means the vacuum adjoint of the represented outer derivation on \(\mathbb C[Z,Z^*]\) taking \(Z\) to \(1\otimes1\).
Such a vacuum \(\xi_\mu\) exists exactly when \(G(\mu)<\infty\).
There are absolute positive constants \(a,A\) such that whenever it exists,
\[
                   aG(\mu)\le\|\xi_\mu\|_2^2\le A G(\mu).                \tag{1}
\]
For the original scalar right slice \(E_0\), both \(\operatorname{Dom}\overline E_0\) and \(\operatorname{Dom} E_0^*\) then contain \(L^\infty(\mu)\).

For a finite tuple of bounded normal generators of a finite von Neumann algebra with faithful normal probability trace, let \(\mu_i\) denote the individual spectral laws.
On the represented mixed starred polynomial algebra let partial liberation at coordinate \(i\) be the prescription \(a\mapsto a\otimes1-1\otimes a\) on its marginal and zero on the omitted starred generators.
The full tuple satisfies actual starred ACSY exactly when, at every coordinate \(i\),

1. The marginal energy \(G(\mu_i)\) is finite.
2. The partial liberation prescription descends to the represented core and has an actual vacuum \(\eta_i\).
3. Its joint spectral measure \(\nu_{\eta_i}\) for left and right multiplication by \(Z_i=X_i\) satisfies \(I_i=\int_{z\ne w}|z-w|^{-2}\,d\nu_{\eta_i}(z,w)<\infty\).

In that case the actual joint vacuum at \(i\) has squared norm comparable to \(G(\mu_i)+I_i\) with absolute constants.
This characterizes existence of the starred derivations and their vacua for arbitrary correlations.
The mixed canonical bounded-vector domain problem for unrestricted normal tuples remains open.

## Argument

### Compression and maximal linear density

The coordinating agent proposed compressing the optimal-density scalar commutator and taking the maximal function of the square root of its density.
Suppose first that \(\mu\) has an actual scalar vacuum.
It is diffuse and the starred derivative on its represented marginal algebra is the divided difference. [Forced normal marginals](Yin_C_F0076_v1.md#statement)
The [one-coordinate column estimate](Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) bounds the scalar column cost \(c\) by \(12\|\xi_\mu\|_2\).
The [attained optimal-density commutator](Yin_C_F0211_v1.md#statement) gives \(d>0\) with \(\int d\,d\mu=1,\ d^{-1}\in L^1(\mu)\) and a bounded operator \(T\) of norm \(c\) on \(L^2(\mu)\) such that
\[
                       [T,Z]=|1\rangle\langle d^{-1/2}|.
\]
For any half-open square \(Q\) with sides parallel to the axes, center \(\lambda\), and side length \(\ell\), let \(P_Q\) be multiplication by \(1_Q\).
Compress the commutator to \(P_QL^2(\mu)\) and subtract the scalar \(\lambda\) from \(Z\).
The norm of its left side is at most \(2c\|(Z-\lambda)P_Q\|\le\sqrt2\,c\ell\).
The right side has norm \(\mu(Q)^{1/2}(\int_Qd^{-1}\,d\mu)^{1/2}\).
For a positive-mass square write \(\langle f\rangle_Q=\mu(Q)^{-1}\int_Q f\,d\mu\).
Jensen's inequality for \(t\mapsto t^{-2}\) applied to \(\sqrt d\) now gives
\[
       \frac{\mu(Q)}{\ell}
           \le\frac{\sqrt2\,c}{\sqrt{\langle d^{-1}\rangle_Q}}
           \le\sqrt2\,c\,\langle\sqrt d\rangle_Q .                      \tag{2}
\]
Also, if \(D\) is the support diameter and \(\lambda\) is any point of the support, the same uncompressed identity shows
\[
                      1\le\|d^{-1/2}\|_2\le2c D .                       \tag{3}
\]
The first inequality uses \(\int d\,d\mu=1\).
Diffuseness of a probability law ensures \(D>0\).

Set \(L=16D\).
In each real axis use the two families of dyadic half-open intervals at scales \(\ell_j=2^{-j}L,\ j\ge0\), with origin translated by \(0\) or \(L/3\).
For each choice of the two axis origins the squares on the plane form a nested filtration, giving four filtrations in all.
At any one scale the endpoint sets for the two translations have mutual distance \(\ell_j/3\), since \(2^j\) is congruent to \(1\) or \(2\) modulo \(3\).
If \(0<r\le D\), one can choose \(j\ge0\) with \(8r\le\ell_j<16r\).
Each coordinate projection of the closed ball \(\overline B(z,r)\) has length \(2r<\ell_j/3\) and therefore meets boundaries from at most one of the translations.
Choosing a translation in each axis whose boundaries are avoided places the ball in a single square of one of the four filtrations.
Consequently (2) bounds \(\mu(B(z,r))/r\) by \(16\sqrt2\,c\) times the largest of the four dyadic maximal functions of \(f=\sqrt d\) at \(z\).
The countably many zero-mass squares may be discarded for this almost-everywhere assertion.
At \(r>D\), use \(\mu(B(z,r))/r\le 1/D\le2c\) by (3).

For any of these filtrations let \(H_n f\) be the largest nonnegative conditional average up to scale \(n\).
Taking the first square along each nested chain whose average exceeds \(t\) gives disjoint squares covering \(\{H_n f>t\}\) and hence \(t\mu\{H_nf>t\}\le\int_{\{H_nf>t\}}f\,d\mu\).
Integration in \(t\) and Cauchy–Schwarz yield \(\|H_n f\|_2^2\le2\int fH_nf\,d\mu\le2\|f\|_2\|H_nf\|_2\).
This finite-scale maximal inequality passes to the supremum over all scales by monotone convergence.
Since \(\|f\|_2=1\), integrating the squared ball bound gives \(\int(M_1\mu)^2\,d\mu\le Cc^2\) with an absolute constant.
In particular the argument uses the same density at every location and scale, without a uniform linear-growth hypothesis on \(\mu\).

### Scalar and joint vacua

The [positive soft-kernel calculation](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) already bounds the total squared Menger curvature by \(6\|\xi_\mu\|_2^2\).
Together with (2) and the maximal estimate this gives \(G(\mu)\le C'\|\xi_\mu\|_2^2\).
Conversely, finite \(G(\mu)\) excludes atoms by the maximal-density term.
The [geometric scalar-core theorem](Yin_C_F0053_v1.md#maximal-density-cauchy-core-transfer), part A, gives the actual scalar vacuum with \(\|\xi_\mu\|_2^2\le4K_0G(\mu)\) and the two scalar bounded-vector domains.
Its Cauchy-transform input is [Tolsa and Verdera, Theorem 2](../audits/literature/TV06/Yin_U001.md#tv06-u001).
This proves (1) and the scalar criterion.

If the tuple has actual ACSY, the [normal recovery criterion](Yin_C_F0238_v1.md#statement) supplies the scalar vacuum of each marginal, its actual liberation vacuum and its finite inverse-gap energy.
Conversely the first condition gives diffuse laws and actual scalar vacua at every coordinate, so the remaining two conditions are exactly the other hypotheses of the same criterion on the original represented core.
Its norm identity \(\|\xi_i\|_2^2=\|\xi_{\mu_i}\|_2^2+I_i\) and (1) give the asserted comparison.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:56 |
| status | open |
| reason | Fix the compression estimate, scalar geometric equivalence and full mixed-vacuum criterion for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar actual vacuum exactly at finite curvature and square-integrable maximal linear density, quantitative norm comparison and the coordinatewise criterion on arbitrary correlated normal tuples. |
| argument | [Argument](#argument) | Local rank-one compression, maximal averages on four translated grids, the scalar criterion and the mixed inverse-gap criterion. |
| dependency | [Normal marginal formulas](Yin_C_F0076_v1.md#statement) | Diffuseness and the represented divided difference for an actual scalar vacuum. |
| dependency | [Scalar column bound](Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) | The scalar optimal column cost is at most twelve times the vacuum norm. |
| dependency | [Optimal commutator](Yin_C_F0211_v1.md#statement) | Attained normalized positive density, integrable reciprocal and exact bounded rank-one commutator in the scalar algebra. |
| dependency | [Vacuum-to-curvature bound](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Total squared Menger curvature bounded by six times the squared vacuum norm. |
| dependency | [Geometric scalar theorem](Yin_C_F0053_v1.md#maximal-density-cauchy-core-transfer) | Part A supplies the quantitative converse and both original scalar bounded-vector domains. |
| dependency | [Joint recovery](Yin_C_F0238_v1.md#statement) | Coordinatewise joint equivalence from scalar vacua, descended liberation with vacuum and finite inverse-gap energy, with its orthogonal norm identity. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:00 |
| status | proved |
| reason | Adopt the geometric equivalence for actual scalar conjugate variables and the resulting joint vacuum criterion after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar actual vacuum exactly at finite curvature and square-integrable maximal linear density, quantitative norm comparison and the coordinatewise criterion on arbitrary correlated normal tuples. |
| argument | [Argument](#argument) | Local rank-one compression, maximal averages on four translated grids, the scalar criterion and the mixed inverse-gap criterion. |
| dependency | [Normal marginal formulas](Yin_C_F0076_v1.md#statement) | Diffuseness and the represented divided difference for an actual scalar vacuum. |
| dependency | [Scalar column bound](Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) | The scalar optimal column cost is at most twelve times the vacuum norm. |
| dependency | [Optimal commutator](Yin_C_F0211_v1.md#statement) | Attained normalized positive density, integrable reciprocal and exact bounded rank-one commutator in the scalar algebra. |
| dependency | [Vacuum-to-curvature bound](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Total squared Menger curvature bounded by six times the squared vacuum norm. |
| dependency | [Geometric scalar theorem](Yin_C_F0053_v1.md#maximal-density-cauchy-core-transfer) | Part A supplies the quantitative converse and both original scalar bounded-vector domains. |
| dependency | [Joint recovery](Yin_C_F0238_v1.md#statement) | Coordinatewise joint equivalence from scalar vacua, descended liberation with vacuum and finite inverse-gap energy, with its orthogonal norm identity. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0264_v1.md#whole-proof-finding) | The optimal-density compression, four maximal estimates, scalar norm equivalence and both directions on the original mixed core. |

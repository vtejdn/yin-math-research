---
author: Yin
---

# A quadratic counterexample with three selfadjoint generators and bounded duals

This variant of the [selfadjoint sandwich example](Yin_C_F0012_v1.md#statement) belongs to the selfadjoint test branch of [bounded rational-closure conditions](../tasks/Yin_T_F0003_v2.md#contract).
It uses three selfadjoint generators instead of two, lowers the maximum degree in elementary free inputs from three to two, and replaces the triangular two-factor merge by one weighted right annihilation operator.
It does not settle whether a simpler two-selfadjoint-generator example exists.
Provenance: project deduction, with a contributing agent's check of the construction; no historical novelty claim is made.

## Current assessment
[Selected decision](#decision-quadratic-independently-reviewed)

## Exact construction and conclusions

<a id="statement"></a>

Let \(h\) have distribution \(d\mu(t)=3t^2\,dt\) on \((0,1)\), and let \(z\) be a standard circular element free from \(h\).
Thus \(z=(b_1+\mathrm i b_2)/\sqrt2\), where \(b_1,b_2\) are freely independent variance-one semicircular elements, also free from \(h\).
Set
\[
 M=W^*(h,z),\quad u=hz,\quad
 X=(h,Y_1,Y_2),\qquad
 Y_1=(u+u^*)/2,\quad Y_2=(u-u^*)/(2\mathrm i),
 \quad A=\mathbb C\langle h,Y_1,Y_2\rangle.
 \tag{1}
\]
All three generators are bounded selfadjoint, and \(W^*(X)=M\).
There are bounded operators \(D_h,D_1,D_2\) on all of \(H=L^2(M,\tau)\) satisfying
\[
 [X_j,D_i]=\delta_{ij}P_\Omega,
 \qquad
 \|D_h\|\le3\pi+4\sqrt3,\quad
 \|D_1\|,\|D_2\|\le2\sqrt3.
 \tag{2}
\]
Here \(X_h=h,X_1=Y_1,X_2=Y_2\), with \(i,j\in\{h,1,2\}\).
Nevertheless,
\[
 z=h^{-1}u\in\operatorname{Rat}_{L^0(M)}(A)\cap M,
 \qquad \operatorname{dist}(z,C^*(X))\ge1.
 \tag{3}
\]
There is also a positive witness with one scalar inverse:
\[
 f=z^*z=u^*(h^2)^{-1}u
 \in\operatorname{Rat}_{L^0(M)}(A)\cap M,
 \qquad \operatorname{dist}(f,C^*(X))\ge\tfrac12.
 \tag{4}
\]
The inverse and product in these formulas are affiliated operations.
For any ambient algebra \(B\), \(\operatorname{Rat}_B(A)\) means matrix rational closure, including all finite matrix sizes.
Since \(A\) is a *-algebra and matrices over \(C^*(X)\) are inverse closed in matrices over \(M\), (3)--(4) exclude both witnesses from \(\operatorname{Rat}_M(A)\).
Thus the bounded rational-closure equality fails under the full selfadjoint bounded-dual hypotheses.

## Complete proof

<a id="argument"></a>

### The tracial model

Put \(K=L^2((0,1),\mu)\) and use Hilbert space tensor products in
\[
 H=\bigoplus_{n\ge0}K\bar\otimes
       (\mathbb C^2\bar\otimes K)^{\bar\otimes n}.
 \tag{5}
\]
The grade-zero vacuum is \(1\in K\), and an element of \(L^\infty(\mu)\) acts on the first \(K\) factor.
Let \(\ell_j\) prepend \(1\otimes e_j\), for \(j=1,2\).
Its adjoint vanishes on grade zero; on a positive grade it contracts the first \(K\) factor against \(1\) and deletes the first colour if that colour is \(j\), giving zero otherwise.
The ranges of \(\ell_1,\ell_2\) are orthogonal.
Take
\[
 z=\ell_1+\ell_2^*.
 \tag{6}
\]
The orthonormal creation combinations \((\ell_1+\ell_2)/\sqrt2\) and \((-\mathrm i\ell_1+\mathrm i\ell_2)/\sqrt2\) show that \((z+z^*)/\sqrt2\) and \((z-z^*)/(\mathrm i\sqrt2)\) are a free variance-one semicircular pair, free from \(L^\infty(\mu)\).
In particular \(\|z\|\le2\) and \(\|z\Omega\|=\|z^*\Omega\|=1\).

This is the coloured version of the [standard tracial model in v1](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model).
The centred Wick-word calculation proves freeness, and the highest tensor grade in alternating products proves vacuum cyclicity.
Right multiplication by \(a\in L^\infty(\mu)\) acts on the last factor.
If \(r_j\) appends \(e_j\otimes1\), then right multiplication by \(z\) is \(r_1+r_2^*\).
The possible grade-zero left/right defects cancel, giving a commuting right action with cyclic vacuum.
Reversing the factors, conjugating functions and interchanging colours 1 and 2 gives the tracial conjugation; hence the vacuum state is faithful, normal and tracial on \(M\).
Thus (5) is its standard \(L^2\) space and the bounded operators \(\rho(a)\xi=\xi a\) are the actual right multiplications.
All subsequent estimates use this Hilbert norm.

The affiliated inverse \(q=h^{-1}\) has
\[
 \|q\|_2^2=\int_0^1 3\,dt=3,
 \qquad hq=1,\qquad
 \tau(1_{(0,\varepsilon]}(h))=\varepsilon^3.
 \tag{7}
\]

### A single bounded annihilation operator

Let \(K_q\) be zero on grade zero and on tensors whose last colour is 1.
On tensors whose last colour is 2, define
\[
 K_q(\xi_0\otimes e_{j_1}\otimes\xi_1\otimes\cdots
                    \otimes e_2\otimes\xi_n)
 =\langle q,\xi_n\rangle
        \xi_0\otimes e_{j_1}\otimes\cdots\otimes\xi_{n-1}.
 \tag{8}
\]
The inner product is linear in its second argument.
The last-factor functional has norm \(\sqrt3\), and different input grades have orthogonal output grades, so \(K_q\) is bounded on all of \(H\), with norm \(\sqrt3\).
It commutes with left \(h\), including grade one, where the first factor is retained.

On positive grades \(K_q\) commutes with both prefix creations.
On grade zero its creation defect is \([K_q,\ell_j]=\delta_{j2}|\Omega\rangle\langle q|\).
Both orders in \([K_q,\ell_j^*]\) vanish on grades zero and one, and contract distinct ends on higher grades.
Consequently
\[
 [K_q,h]=0,\quad [K_q,z]=0,\quad
 [K_q,z^*]=|\Omega\rangle\langle q|,
 \quad [K_q^*,z]=-|q\rangle\langle\Omega|.
 \tag{9}
\]
Define, temporarily in the operator-first convention,
\[
 E_u=-K_q^*,\qquad E_{u^*}=K_q.
\]
Then (7)--(9) give
\[
 [E_u,u]=[E_{u^*},u^*]=P_\Omega,
 \quad [E_u,u^*]=[E_{u^*},u]=0,
 \quad [E_u,h]=[E_{u^*},h]=0.
 \tag{10}
\]
Only the vector \(q\in L^2\), not an unbounded multiplier, is used in defining these duals.

### The scalar dual and bounded correction

The unnormalized finite-interval Hilbert transform with kernel \(1/(t-s)\) has norm at most \(\pi\) on unweighted \(L^2(0,1)\), with the normalization used in [v1's scalar construction](Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction).
With \(w(t)=3t^2\) and \(W\xi=\sqrt w\xi\), put
\[
 D_0=W^{-1}M_{\sqrt w}\,\mathcal T\,M_{\sqrt w}W.
\]
It is bounded on \(K\) with norm at most \(3\pi\).
On a dense space of smooth functions supported inside \((0,1)\), cancellation in the kernel gives \([D_0,h]=|1\rangle\langle1|\); boundedness extends the identity to \(K\).
Let \(\widehat D_h\) act by \(D_0\) on the last \(K\) factor of every grade.
First- and last-factor actions commute on positive grades, while the scalar identity applies on grade zero, so
\[
 [\widehat D_h,h]=P_\Omega,
 \qquad [\widehat D_h,z]=[\widehat D_h,z^*]=0.
 \tag{11}
\]
The creation and contraction identities include grades zero and one.

Put
\[
 E_h=\widehat D_h+K_q^*\rho(z)-\rho(z^*)K_q,
 \quad E_1=K_q-K_q^*,\quad
 E_2=-\mathrm i(K_q+K_q^*).
 \tag{12}
\]
Right multiplication commutes with all left generators, and traciality gives
\(P_\Omega\rho(z)=P_\Omega z\) and \(\rho(z^*)P_\Omega=z^*P_\Omega\).
Thus
\[
 [E_h,u]=P_\Omega z-P_\Omega\rho(z)=0,
 \qquad
 [E_h,u^*]=z^*P_\Omega-\rho(z^*)P_\Omega=0,
 \qquad [E_h,h]=P_\Omega.
\]
Taking the real and imaginary combinations in (10) gives \([E_i,Y_j]=\delta_{ij}P_\Omega\), and \([E_i,h]=0\).
Finally set \(D_h=-E_h,D_1=-E_1,D_2=-E_2\).
These satisfy the generator-first equations (2), and their stated norm bounds follow from \(\|K_q\|=\sqrt3\), \(\|z\|\le2\), and \(\|\widehat D_h\|\le3\pi\).

### Generation and rational membership

For \(\pi_\varepsilon=1_{[\varepsilon,1]}(h)\), the bounded functions \(h^{-1}\pi_\varepsilon\) belong to \(W^*(X)\), and
\[
 (h^{-1}\pi_\varepsilon)u=\pi_\varepsilon z\longrightarrow z
\]
strongly, with uniform norm bound two.
Hence \(W^*(X)=M\).
Since \(h\) has zero kernel, affiliated inversion gives \(h^{-1}u=z\) and \(u^*(h^2)^{-1}u=z^*z\), proving both rational membership assertions.

### Norm separation using right append isometries

Let \(\xi_\varepsilon=1_{(0,\varepsilon]}(h)\Omega/\varepsilon^{3/2}\), a unit vector in grade zero.
Define an isometry \(V_\varepsilon:H\to H\) by appending \(e_2\otimes\xi_\varepsilon\) on the right of each tensor.
It intertwines left \(h\) exactly.
The creation operators also intertwine exactly.
Only the grade-zero contraction of colour 2 produces a defect, so
\[
 zV_\varepsilon-V_\varepsilon z
       =|\xi_\varepsilon\rangle\langle\Omega|,
 \qquad z^*V_\varepsilon=V_\varepsilon z^*.
 \tag{13}
\]
It follows that
\[
 uV_\varepsilon-V_\varepsilon u
       =|h\xi_\varepsilon\rangle\langle\Omega|,
 \qquad u^*V_\varepsilon=V_\varepsilon u^*.
 \tag{14}
\]
The first defect has norm at most \(\varepsilon\).
The product rule and uniform norm bound \(\|V_\varepsilon\|=1\) now imply
\[
 \|aV_\varepsilon-V_\varepsilon a\|\longrightarrow0
 \quad\text{for every }a\in C^*(X)=C^*(h,u).
 \tag{15}
\]
The passage from polynomials to the C*-algebra uses the estimate \(\|aV-Va\|\le2\|a\|\).

Write \(Q_\varepsilon=V_\varepsilon V_\varepsilon^*\).
Its range is orthogonal to grade zero, so (13) gives
\[
 (1-Q_\varepsilon)zV_\varepsilon
       =|\xi_\varepsilon\rangle\langle\Omega|.
\]
For any \(a\in C^*(X)\), (15) implies
\[
 \|z-a\|\ge
 \|(1-Q_\varepsilon)(z-a)V_\varepsilon\|
 \ge1-\|aV_\varepsilon-V_\varepsilon a\|.
\]
This proves (3).

For the positive witness, (13) and \(z^*\xi_\varepsilon=V_\varepsilon\Omega\) give
\[
 fV_\varepsilon-V_\varepsilon f
       =z^*|\xi_\varepsilon\rangle\langle\Omega|
       =V_\varepsilon P_\Omega,
\]
whose norm is one.
For every \(a\in C^*(X)\),
\[
 1\le2\|f-a\|+\|aV_\varepsilon-V_\varepsilon a\|.
\]
Taking the limit proves (4).
Matrix inverse closure of the unital C*-subalgebra \(C^*(X)\subset M\) excludes every bounded matrix rational representation of either witness, independently of the displayed affiliated formulas.

## Comparison and remaining question

Each of \(Y_1,Y_2\) is a selfadjoint polynomial of degree two in the three elementary free inputs \(h,b_1,b_2\).
The dual uses one last-factor functional and its adjoint; no two-variable triangular kernel estimate is required.
The density can be \(3t^2\), since only \(h^{-1}\in L^2\) and bounded scalar density are needed here.
This is a simplification in degree and in the dual construction, with an explicit increase from two to three selfadjoint generators.
Deleting \(h\) does not prove a two-generator counterexample: the rational formulas for the witnesses use that generator, and their membership in the smaller affiliated rational closure has not been established.
The two-generator search and the general sufficient-condition Task therefore remain unresolved.

## Assessment history

### Decision quadratic-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-21T14:48 |
| status | open |
| reason | A complete explicit construction is retained for independent proof inspection, including the increase to three generators and the full matrix nonmembership argument. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact construction](#statement) | Three selfadjoint quadratic generators, whole-space bounded duals and two bounded rational witnesses. |

### Decision quadratic-independently-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-21T14:56 |
| status | proved |
| reason | Independent inspection verifies the complete construction, both norm-distance bounds and all matrix rational representations, with the increase to three selfadjoint generators explicitly retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact construction](#statement) | All three selfadjoint generators, bounded duals, generation, two bounded affiliated rational witnesses and matrix rational closure separation. |
| argument | [Complete proof](#argument) | The coloured tracial model, explicit bounded duals, right append isometries, both distances and the precise comparison. |
| support | [v1 model](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | The standard tracial model argument, with its two-colour extension proved in v3. |
| support | [Scalar transform](Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction) | The finite-interval Hilbert-transform normalization; the changed density, bound and correction are checked in v3. |
| review | [Independent complete inspection](../audits/reviews/Yin_R_F0056_v3.md#quadratic-selfadjoint-finding) | The entire exact statement and proof, including all whole-space and matrix-closure interfaces. |
| review | [Independent scope comparison](../audits/reviews/Yin_R_F0056_v3.md#branch-comparison-finding) | Degree and dual-construction simplification with three generators; no two-generator or general Task completion. |

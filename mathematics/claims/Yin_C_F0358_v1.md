---
author: Yin
---

# Counting real eigenvalues by the negative inertia of a polynomial symmetrizer

<a id="statement"></a>
## Weak Brown convergence from a positive free symmetrizer

Use the [fixed-law Wigner contract](../tasks/Yin_T_F0012_v3.md#contract), including complex strict upper entries with finite second moments, Hermitian symmetry, and arbitrary coupling across dimensions.
Let \(P,G=G^*\) denote a scalar noncommutative polynomial \(P\) and a selfadjoint scalar polynomial \(G\) in the Hermitian variables, with the polynomial identity \(PG=GP^*\).
Write \(p,g\) for their free semicircular evaluations and \(P_N,G_N\) for the finite evaluations.
Assume either of the following conditions.

1. The free metric satisfies \(g\ge\delta 1\) for some \(\delta>0\).
   Put \(h=g^{-1/2}p g^{1/2}\).
2. The polynomial has the form \(P=AB\) with \(A=A^*, B=B^*\), \(G=A\), and \(a=A(s)\ge0\) has zero kernel.
   Put \(h=a^{1/2}B(s)a^{1/2}\).

Then \(h\) is selfadjoint and the empirical eigenvalue law of \(P_N\) converges weakly almost surely to the spectral law of \(h\), which is the Brown measure of \(p\).
Both finite factors may share arbitrary inputs and the finite metric can be indefinite or singular.
The ordinary eigenvalue potentials converge almost surely locally in planar \(L^1\).
For each fixed scalar polynomial \(q\), the weak Brown conclusion also holds for \(q(P_N)\).

If in addition \(G_N>0\) eventually almost surely, the ordinary normalized log determinant of \(P_N-zI\) converges almost surely along the full sequence, locally uniformly for \(z\notin\mathbb R\).
Its value is \(\tau\log|p-z|\), and the ordinary determinant of an exact scalar linearization has the corresponding auxiliary trace normalization.
The additional finite positivity condition is used only for this pointwise conclusion.

<a id="argument"></a>
## Inertia bounds real roots with their algebraic multiplicities

Write \(n_-(D)\) for the number of strictly negative eigenvalues of a finite Hermitian matrix.
For each real \(t\), the polynomial \(F_t=(P-t)G\) is selfadjoint.
At any fixed matrix realization decompose the physical space into \(\operatorname{ran}G_N\oplus\ker G_N\), with \(G_N=\operatorname{diag}(D,0)\) and \(D\) invertible.
The identity \(P_NG_N=G_NP_N^*\) implies that \(P_N\) has zero lower-left block and that its upper-left block \(C\) satisfies \(CD=DC^*\).
On the range the restricted pencil is \((C-t)D\), whose determinant is \(\det(C-t)\det D\).
The other block of \(F_t\) is zero.
The conclusion also holds for an empty range with determinant one.

For real \(r<t\) outside the spectrum of \(P_N\), a change of \(n_-\) on the range can occur only at a real eigenvalue \(\lambda\) of \(C\).
By continuity of the ordered Hermitian eigenvalues its absolute jump is at most the nullity of \((C-\lambda)D\).
This nullity is at most the algebraic multiplicity of \(\lambda\) in \(C\), which in turn is bounded by its multiplicity in the block triangular \(P_N\).
Consequently
\[
 \#\{\text{eigenvalues of }P_N\text{ in }(r,t)\}
 \ \ge\ n_-(F_t(W))-n_-(F_r(W)).
\]
The count on the left is on the real line and includes algebraic multiplicities.

<a id="free-inertia"></a>
## Identification of the free limit

In the first case \(pg=gp^*\) gives \(h=h^*\) and \(p=g^{1/2}h g^{-1/2}\).
In the second case, with \(b=B(s)\), the [cyclic determinant identity](Yin_C_F0186_v4.md#argument) gives \(\Delta(ab-z)=\Delta(h-z)\) for \(z\ne0\) by exchanging the two factors \(a^{1/2}\) and \(a^{1/2}b\).
This follows also by unit triangular elimination in the two-by-two block matrix with diagonal blocks equal to one and off-diagonal blocks the two factors, scaling one by \(1/z\).
Equality of the locally integrable potentials off zero gives equality of their distributional Laplacians on the plane.
In the first case similarity gives the same conclusion at once.
Thus the spectral law \(\mu_h\) is the Brown measure of \(p\) in both cases.

At any real \(t\) with \(\mu_h(\{t\})=0\), \(F_t(s)=g^{1/2}(h-t)g^{1/2}\) is injective because each of its three factors is injective.
Its strictly negative spectral projection has trace \(\mu_h((-\infty,t))\).
For an invertible positive \(S\), congruence \(T\mapsto STS\) preserves the trace of the negative projection.
Indeed \(S^{-1}\operatorname{ran}1_{(-\infty,0)}(T)\) is a closed subspace of the same tracial dimension by polar decomposition and meets the nonnegative spectral subspace of \(STS\) only in zero.
Dimension comparison gives one inequality and congruence by \(S^{-1}\) gives the reverse.
For a noninvertible \(g\) take \(S=(g+\epsilon)^{1/2}\).
The congruences converge in norm as \(\epsilon\downarrow0\), and the limiting operator is injective, so the traces of their negative projections converge.

Choose a countable dense set of real endpoints avoiding atoms of \(\mu_h\) and of the expected empirical eigenvalue law of every \(P_N\).
Almost surely no finite spectrum meets any chosen endpoint.
The [finite-variance selfadjoint polynomial weak law](Yin_C_F0186_v4.md#finite-variance-weak) applied to all \(F_t\) at these endpoints gives
\(N^{-1}n_-(F_t(W))\to\mu_h((-\infty,t))\) on one event.
Hence the lower limit of the normalized number of real eigenvalues on each endpoint interval is at least its \(\mu_h\)-mass.
For any open subset of the plane, exhaust its intersection with the real line in \(\mu_h\)-mass by finite unions of disjoint such intervals.
The dense endpoints carry no atoms, so splitting an interval at an endpoint costs no limiting mass.
The open-set criterion for probability measures now gives the asserted weak convergence.

The [positive logarithmic tail and potential criterion](Yin_C_F0186_v4.md#remaining-defect) give the planar \(L^1_{\rm loc}\) assertion from weak convergence.
For \(q(P_N)\) use continuous mapping and the finite spectral mapping theorem.
For the free target, factor \(q(w)-z\) over the complex numbers and apply multiplicativity of the FK determinant to its factors, using the Brown potential of \(p\).
This identifies the free Brown measure with the pushforward of \(\mu_h\), also for a constant \(q\).

<a id="nonreal"></a>
## The pointwise conclusion when the finite metric is eventually positive

On this event the finite \(P_N\) are eventually similar to Hermitian matrices, so their spectra lie on the real line.
For nonreal \(z\) the function \(\lambda\mapsto\log|\lambda-z|\) is bounded below there.
The [almost-sure positive logarithmic tail](Yin_C_F0186_v4.md#log-statistics) controls the truncation at large real \(\lambda\), uniformly when \(z\) belongs to a compact set.
Weak convergence then gives the ordinary logarithmic limit at each such \(z\).
On a compact subset of either open half-plane the logarithms are uniformly Lipschitz in \(z\) by the positive distance to the real axis, and finite nets give local uniform convergence.
The free potential there equals the same spectral log integral (pointwise by similarity or cyclicity).
The [finite and free scalar linearization identities](../ledger/Yin_L_F0061_v2.md#linearization-transfer) give the determinant assertion for its pencil.

<a id="example"></a>
## A shared input at the edge of the positive spectrum

With three input variables take \(A=2+x,\ B=xy+yx+zyz\).
At free semicirculars \(2+s_x\) is positive and injective, and zero is its lower spectral edge.
The product therefore has the weak Brown limit under the full complex finite-variance Wigner contract, including arbitrary dependence across dimensions.
No bound on the sign or operator norm of \(2I+X_N\) is needed in the finite models.
The assertion leaves specified real-shift logarithmic losses for general indefinite finite metrics open.

## Current assessment
[Selected decision](#decision-inertia-reviewed)

## Assessment history

### Decision inertia-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:28 |
| status | open |
| reason | A count of real roots through the negative index of a Hermitian polynomial pencil covers a positive free metric and permits indefinite finite metrics. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Weak limits and pointwise consequence](#statement) | The two sufficiency conditions and the extra finite positivity hypothesis. |
| argument | [Finite root count](#argument) | Range compression and signed index variation with algebraic multiplicity. |
| support | [Free inertia and convergence](#free-inertia) | Singular injective free congruence and the weak limit. |
| support | [Nonreal ordinary logarithms](#nonreal) | Extra eventual finite positivity gives full-sequence locally uniform convergence. |
| support | [Degree-four example](#example) | Allowed shared colors and free positivity at the edge. |

### Decision inertia-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:30 |
| status | proved |
| reason | The finite inertia jumps and the free congruence identify the limiting measure of real eigenvalues, with full-sequence logarithms off the line if the finite metrics are eventually positive. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Symmetrized polynomial](#statement) | Two cases and the additional finite positivity hypothesis. |
| argument | [Complete root-count proof](#argument) | Range compression and algebraic multiplicities. |
| support | [Free limit](#free-inertia) | Tracial inertia, interval masses and cyclicity. |
| review | [Independent assessment](../audits/reviews/Yin_R_F0366_v1.md#inertia-whole-proof) | Full proof and comparison with the earlier thin-support result. |

---
author: Yin
---

# Spe26: Affine Determinant Proposal and Its Domain

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Primary author post](https://rolandspeicher.com/2026/09/09/a-story-of-the-determinant-of-operator-valued-semicircular-elements/), 2026-09-09, online statement.

Passages: Unnumbered generalization after the comparison of MS24 with Lehner’s formula.

Inspection: Coverage: the source statement was read; its printed domain is questioned by the explicit calculation below.


<a id="spe26-u001"></a>
## Spe26-U001: Displayed Proposal, Attribution and a Boundary Defect

Recorded 2026-09-13 after primary-source access on 2026-09-12.
Reader: research agent the affine-source reader.
Scope: the displayed affine determinant candidate and its Hilbert-Schmidt domain.
Coverage: the source statement was read; its printed domain is questioned by the explicit calculation below.
No source proof was supplied or accepted.
Bibliographic identity, public online-only status and access metadata are owned by the Spe26 entry.

### Source Statement and Inspection Boundary

The [primary author post](https://rolandspeicher.com/2026/09/09/a-story-of-the-determinant-of-operator-valued-semicircular-elements/) displays an unnumbered generalization after comparing MS24 with Lehner's formula.
It attributes both the proposal and a claimed proof to ChatGPT.
The inspected post provides no such proof or proof link.

For selfadjoint \(a,a_1,\ldots,a_n\in M_m(\mathbb C)\) and free standard semicircular \(s_j\), set
\[
 S=a\otimes1+\sum_j a_j\otimes s_j,\qquad
 \eta(x)=\sum_j a_jxa_j,\qquad
 \mathcal C_b(x)=bxb,\qquad
 \langle x,y\rangle_2=\operatorname{tr}_m(x^*y).
\]
The proposed determinant formula has right side
\[
 e^{-1/2}\inf_{\substack{b>0\\\mathcal C_b-\eta\succeq0}}
 \Delta_m(b)\exp\!\left[
 \frac12\langle a,(\mathcal C_b+\eta)^{-1}(a)\rangle_2\right].
                                                               \tag{S1}
\]
The source explicitly interprets \(\succeq0\) as positivity on the entire Hilbert-Schmidt space.
It prints an ordinary inverse and supplies no convention for a nontrivial kernel.
The finite-dimensional determinant is normalized as \(\Delta_m(b)=|\det b|^{1/m}\).

### Local Formulation Audit

Let \(m=2\), \(a_1=Z=\operatorname{diag}(1,-1)\), and \(b=I_2\).
Then \(\eta=\operatorname{Ad}Z\) acts as \(+I\) on diagonal matrices and \(-I\) on off-diagonal matrices.
Therefore
\[
 \mathcal C_b-\eta=I-\eta\succeq0,
 \qquad \ker(\mathcal C_b+\eta)
       =\{x:x\text{ is off-diagonal}\}\ne\{0\}.
\]
Taking \(a=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) shows that the objective in (S1) is undefined at an allowed trial point.
This is a defect in the printed formulation, not a counterexample to a suitably repaired determinant equality.

The strict-domain repair and its inverse-existence calculation were developed in [the search record](../../../ledger/Yin_L_F0029_v1.md#the-printed-domain-does-not-guarantee-the-printed-inverse).
The resulting global comparison, approximation and capacity reduction belong to [the project proof](../../../claims/Yin_C_F0124_v1.md), whose own review record controls their status.
They are not source theorems or an inspected reconstruction of an unseen ChatGPT proof.

### Use and Attribution

This unit supplies the provenance and exact formulation of a research candidate for [Yin_T_F0008](../../../tasks/Yin_T_F0008_v1.md#yin_t_f0008), together with the finite-dimensional obstruction above.
It supplies no accepted premise asserting the determinant equality.
The project's proof must remain self-contained relative to its actual mathematical dependencies, and must retain the source's role as the origin of the displayed proposal.
Neither historical priority beyond this located post nor any formal verification is asserted.

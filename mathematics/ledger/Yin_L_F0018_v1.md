---
author: Yin
---

<a id="bounded-linearization-recheck"></a>
# MSY23 Recheck: Bounded Outputs and Bounded Inverse Pencils

Date: 2026-09-10.
Author: the free-field algebra agent, responding to the user's request to search the previously audited MSY23 materials for the boundedness of a linear representation's matrix inverse.
The actual primary text on published pp. 8--9 and 21--25 was freshly read, including the proofs of Theorem 4.4 and Lemma 4.8.
This is a separate selected-source recheck; the [MSY23-U003](../audits/literature/MSY23/Yin_U003.md#msy23-u003) remains unchanged.

Current sufficient homes, 2026-10-21: [MSY23-U003 v2](../audits/literature/MSY23/Yin_U003.md#bounded-linearization-recheck) retains the exact source proof/domain analysis and its actual additional primary reading.
[C_F0012 Sections6-7](../claims/Yin_C_F0012_v1.md#6-exclusion-from-the-norm-closed-and-scalar-division-algebras) supply the complete accepted distance and minimal-state mathematics used below; the final matrix C*-inverse-closure step is retained here as its direct comparison consequence.
The note preserves this source-versus-example distinction and actual failed bounded-realization inference; no new C12 review or current adoption is performed.

## Source theorem and ambient-domain boundary

[MSY23-U003 v2](../audits/literature/MSY23/Yin_U003.md#additional-bounded-realization-source-recheck) retains the complete original analysis of Definition 4.2, Theorems 4.3–4.4, Definition 4.5, Proposition 2.3 and Lemma 4.8, with the actual primary-reading dates and limits.
A bounded inverse pencil is available in the source for rational closure evaluated in M.
Boundedness of an output evaluated in the affiliated algebra supplies a different premise; the following project example excludes that attempted inference, including every alternative bounded inverse pencil.

## The Existing Example Also Excludes Minimality and Alternative Pencils

The reviewed [Yin_C_F0012 construction](../claims/Yin_C_F0012_v1.md#yin_c_f0012) takes a positive $h$ with distribution $4t^3\,dt$ on $(0,1)$ and a standard semicircular $b$ free from $h$.
Set $Y=hbh$ and $X=1-h$.
The two coordinates are bounded selfadjoint generators and admit the explicitly bounded dual system constructed in that artifact.
Let $q=h^{-1}$ in $U$; it lies in $L^2$ but is unbounded.
The bounded affiliated rational output $b=qYq$ has the monic representation
\[
b=e_1^T
\underbrace{\begin{pmatrix}1-X&-Y\\0&1-X\end{pmatrix}}_{L(X,Y)}^{-1}
e_2,
\qquad
L(X,Y)^{-1}=\begin{pmatrix}q&b\\0&q\end{pmatrix}.
\tag{3}
\]
Its two-state realization is controllable and observable: with coefficient matrices $A_X=I_2$ and $A_Y=E_{12}$, the vectors $e_2,A_Ye_2=e_1$ span the state space, while $e_1^T,e_1^TA_Y=e_2^T$ span its dual.
Thus the inverse in (3) is unbounded even for this minimal monic realization, rather than because an unused block was appended.

The stronger obstruction is independent of a particular representation.
Yin_C_F0012 Section 6 proves
\[
\operatorname{dist}(b,C^*(h,Y))\ge1.
\tag{4}
\]
It uses small spectral unit vectors $\xi_\varepsilon$ for which $h\xi_\varepsilon$ and $Y\xi_\varepsilon$ tend to zero, while $\langle\xi_\varepsilon,b\xi_\varepsilon\rangle=0$ and $\|b\xi_\varepsilon\|=1$.
Every fixed polynomial acts asymptotically by its constant term on those vectors, yielding (4).
Since $C^*(X,Y)=C^*(h,Y)$, this is also exclusion in the monic coordinates.

If any polynomial pencil over $X,Y$, of any finite size, had a bounded inverse in $M_N(M)$, C*-algebra inverse closure would put that inverse in $M_N(C^*(X,Y))$.
Every scalar or polynomial compression of that inverse would belong to $C^*(X,Y)$.
Equation (4) therefore excludes every alternative bounded inverse-pencil representation of $b$.
This addresses the existence assertion, not only boundedness of the particular inverse displayed in (3).

## Verification Scope

The author of this note reread C_F0012 Sections 6--7 and reconstructed the displayed inverse, the two-state reachability/observability test, and the C*-matrix inverse-closure consequence.
The complete construction of its tracial model and bounded duals is consumed from the existing [whole-proof reviews](../audits/reviews/Yin_R_F0054_v1.md), rather than claimed as a new complete audit in this note.

The actual original C12 portion recheck is retained in [R_F0055](../audits/reviews/Yin_R_F0055_v5.md#bounded-linearization-c12-recheck), with its prior target-review context and limited fresh reconstruction explicit.

The actual original whole-note finding is retained in [R_F0055](../audits/reviews/Yin_R_F0055_v5.md#bounded-linearization-complete-note-finding), preserving its original primary readings and unknown initial context arrangement.

This record is an internal AI source and proof recheck, not external human peer review, formal verification, or a historical-priority assessment.

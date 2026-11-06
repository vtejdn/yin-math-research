---
author: Yin
---

<a id="you61-u001"></a>
# Complex symmetric and skew matrices under unitary congruence

The source is D. C. Youla, *A normal form for a matrix under the unitary congruence group*, Canadian Journal of Mathematics 13 (1961), pp. 694-704, in the [identified 11-page publication edition](readme.md#edition-1961).
The exact selected statements are introduction equations (1)-(3), printed p. 694 / PDF p. 1.
The source calls both normal forms classical; no earliest-priority claim is made here.
These established statements are accepted at the scopes below after direct statement and applicability checks.
The source's complete normal-form proof and references establishing the earlier classical results were not audited.
This unit is source inspection and notation conversion, not an independent project-proof review.

<a id="symmetric-congruence"></a>
## Equation (1): the complex symmetric form

Let S be any complex n-by-n matrix satisfying S^T=S, where T denotes the ordinary complex-linear transpose.
There is a unitary n-by-n matrix Q such that
\[
 Q^T S Q=\operatorname{diag}(s_1(S),\ldots,s_n(S)),
 \tag{Symmetric-congruence}
\]
where the diagonal entries are the nonnegative square roots of the eigenvalues of S^*S, hence the singular values of S.
Their decreasing order can be arranged by permuting the unitary columns.
No real, Hermitian, positive-definite or invertibility hypothesis is imposed on S.
Equation (1) and its accompanying singular-value description were read directly in the retained original for this input.
This reading is distinct from the earlier inspection of the skew equations (2)-(3); it does not enlarge that earlier inspection retrospectively.

Put V=conjugate(Q).
Then V is unitary and the same statement becomes
\[
 S=V\operatorname{diag}(s_1(S),\ldots,s_n(S))V^T.
\]
This follows by multiplying (Symmetric-congruence) on the left by conjugate(Q) and on the right by Q^*.
It is a notation conversion of the cited theorem, not an additional normal-form theorem.

<a id="symmetric-truncation"></a>
## Direct factorization and truncation consequences

For n>=2 and rank S<=2, multiply the first two columns of V by sqrt(s_1(S)),sqrt(s_2(S)) and pad by a zero column when necessary.
This gives U in M_(n,2)(C) with
\[
 S=UU^T,\qquad \|U\|^2=s_1(S)=\|S\|.
\]
For general S and n>=3, the same construction gives S_2=UU^T with rank S_2<=2, S_2^T=S_2, and
\[
 \|S_2\|\le\|S\|,\qquad \|S-S_2\|=s_3(S).
\]
Indeed the omitted diagonal terms have largest singular value s_3(S), and both V and V^T are unitary.
These are direct finite-dimensional consequences of the accepted symmetric form.
No random or measurable selection of V is asserted; a consuming uniform deterministic estimate can be conditioned on a random shift without selecting V measurably.
The [rank-two Wigner deduction](../../../claims/Yin_C_F0194_v9.md#symmetric-factorization) uses exactly this deterministic factorization and approximation.

<a id="skew-congruence"></a>
## Equations (2)-(3): the complex skew form

If A is any complex n-by-n matrix with A^T=-A, the source states that a unitary congruence puts A into blocks
\[
 \begin{pmatrix}0&\sigma_j\\-\sigma_j&0\end{pmatrix},
 \qquad \sigma_j>0,
\]
and zero blocks.
The positive block parameters are the positive square roots of the corresponding nonzero eigenvalues of A^*A, and the source explicitly gives rank A=2k for k positive blocks.
Thus positive singular values have even multiplicity; in even dimension the zero singular value also has even multiplicity.
These statements concern complex transpose-skew matrices, not only real skew matrices or Hermitian matrices.
Equations (2)-(3) and the paragraph identifying their singular values and rank were inspected in text and visually in the retained edition, as recorded in the existing source notes and [C_F0194_v7's source passage](../../../claims/Yin_C_F0194_v7.md#pairing-source).
The [complete antilinear pairing proof in C_F0194_v7](../../../claims/Yin_C_F0194_v7.md#singular-pairing) supplies that Claim's own mathematical proof; its source citation is classical attribution and does not import an unchecked source proof.
No inspection of the entire Youla article, its general-matrix extensions or associated references is claimed.

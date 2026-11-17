---
author: Yin
---

# Closed range and signed shell estimates from a cyclic minor

At 2026-11-17T04:30 UTC an agent outside the development of Yin_C_A0081_v1 independently reviewed the fixed statement and all three proof sections for Sheng Yin.
The reviewer checked the boundary result in the retained Boutonnet–Carderi preprint and read the cited signed first-return bounds.
No development dialogue, author explanation or prior finding on this claim was supplied.
At 2026-11-17T04:44 UTC the same reviewer independently checked the subsequently added two-row example against the established theorem and the free-subgroup row-product hypothesis.
The reviewer received the fixed example and its review scope and did not participate in its construction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0081_v1.md#statement) | The maximal cyclic and nonzero minor hypotheses, collected cosets, closed-range decision, same-kernel factorization, multiplicity exponent and signed shell estimate. |
| [Whole-argument finding](#whole-argument-finding) | [Boundary packets](../../claims/Yin_C_A0081_v1.md#spectral-packets-along-a-maximal-cyclic-subgroup) | Maximal amenability, disjoint fixed-point pairs, free high powers, phased averages and compression for a finite union of spectral arcs. |
| [Whole-argument finding](#whole-argument-finding) | [Coefficient lower bound](../../claims/Yin_C_A0081_v1.md#a-lower-bound-from-the-collected-coefficients) | Right cosets and row-Gram orientation, bounds on and off the spectral packets, the Laurent column-module basis and surjectivity of the residual matrix. |
| [Whole-argument finding](#whole-argument-finding) | [Signed shells](../../claims/Yin_C_A0081_v1.md#estimating-the-original-shell-sums) | Trace comparison, Smith invariant factors, the largest root order, exponential Fourier tails and squared shell error for the original powers. |
| [Whole-argument finding](#whole-argument-finding) | [Finite shell truncation](../../claims/Yin_C_A0076_v1.md#statement) | Allowed decay exponent, dyadic return difference, polynomial horizon and norm error on the exterior. |
| [Whole-argument finding](#whole-argument-finding) | [Signed means](../../claims/Yin_C_A0067_v1.md#statement) | Uniform factor four in the exterior coefficient norm of the limiting means, with the two probe phases and unnormalized trace. |
| [Whole-argument finding](#whole-argument-finding) | [Two-row example](../../claims/Yin_C_A0081_v1.md#a-two-row-example-with-full-row-product-support) | Collected module and its basis, the fourth-root spectral exponent, and generation of the ambient group by left differences in a single entry. |
| [Whole-argument finding](#whole-argument-finding) | [Free-subgroup row-product test](../../claims/Yin_C_A0082_v1.md#statement) | Required containment of the support of every collected row-Gram entry in one free subgroup. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line zero product](../../claims/Yin_C_A0051_v1.md#statement) | Nonfreeness of the four-line groups in the comparison. |

## Whole-argument finding

An amenable subgroup maximal among those containing \(H\) exists by the directed-union property.
It is virtually cyclic by the hyperbolic-group boundary result and thus cyclic in the torsion-free case, so maximality of \(H\) makes it equal to \(H\).
Lemma 2.2(iii) gives disjoint translated endpoint pairs for \(g\notin H\), and its proof gives north–south dynamics for an infinite-order element.
Disjoint neighborhoods of all four endpoints therefore give common high powers of the two generators to which ping-pong applies. [Boutonnet and Carderi, Lemma 2.2 and proof, p. 6](../../literature/pdf/BC15--arxiv-v2.pdf#page=6)

In the regular representation of the free subgroup, left translation by \(s^{-j}\) sends words without an initial \(s\)-syllable to disjoint sets for the distinct averaging indices.
The analogous calculation for \(v\) gives \(\|(I-P_v)V_N\|\le N^{-1/2}\) by adjunction.
Inserting \(P_s\le I-P_v\) and its complement yields the \(2/\sqrt N\) bound for \(U_N^*V_N\), uniformly in the two phases and on every right coset of the free subgroup.
A unit vector in a single arc differs from its phased average by at most the arithmetic mean of \(bj\delta\).
Summing this estimate over a disjoint partition subordinate to a fixed finite family of arcs and taking \(N\) large before \(\delta\) small gives \(\|E_\delta gE_\delta\|\to0\).
This justifies the operator-norm compression needed for each outside coefficient.

The product of two collected terms in the row Gram matrix has middle group element \(xy^{-1}\).
Its Laurent factors on the left and right keep it outside \(H\) unless \(Hx=Hy\), which verifies the orientation and the formula \(E_H(TT^*)=F_TF_T^*\).
Full row rank on the circle gives a uniform lower bound for this expectation.
Compressing the finitely many terms outside \(H\) to the arcs at the zeros of the selected minor leaves a lower bound there.
On their complement \(P(t)^*\) has a uniform lower singular-value bound, and \(\|P(t)^*\xi\|\le\|T^*\xi\|\) because its outputs form a subvector of the outputs of \(T^*\).
Combining the two estimates by the stated triangle inequality proves that \(T^*\) is bounded below, hence that \(T\) is onto.

The selected Laurent columns give the column module rank \(r\), so a basis over \(\mathbb C[t,t^{-1}]\) forms a square matrix \(D\) with nonzero determinant.
In that basis the collected columns span the whole free module, giving a Laurent right inverse for \(F_T\).
Reassembly on the original right-coset representatives preserves \(A=DT\) and leaves a nonzero cyclic minor in \(T\).
The preceding lower bound applies to \(T\), and \(D\) acts on copies of its torus multiplier, which is invertible almost everywhere.
It has dense range and zero kernel.
Consequently \(\operatorname{ran}A=\operatorname{ran}D\), \(\ker A=\ker T\), and closed range is equivalent to full row rank of \(F(z)=D(z)F_T(z)\) everywhere on the circle.
The dense final support has trace \(r\), giving nullity \(m-r\).

On a nonclosed input the two-sided bounds for \(TT^*\) compare \(AA^*\) with positive constants times \(DD^*\) in the correct order for trace-sublevel comparison.
The unimodular Smith multipliers and their inverses are bounded on the entire circle.
A diagonal invariant factor vanishing to order \(d_i>0\) contributes sublevel mass of order \(s^{1/(2d_i)}\) near that root.
Among the finitely many such roots the largest multiplicity gives the exponent \(1/(2d)\).
Polar decomposition transfers the positive part to the column Gram without counting its kernel atom, and the fixed scalar normalization only changes constants.
The exponent lies in the interval required by C76, and integration of the heat multiplier supplies its dyadic return-difference bound for the original matrix.

Geometric approximation of \((TT^*)^{-1}\) has linear propagation and geometric norm error, yielding an exponentially weighted square tail for the actual kernel projection through \(I-p=T^*(TT^*)^{-1}T\).
The polynomial weight can be absorbed by reducing the exponential rate.
Combining C67's coefficient-norm comparison with C76's original-matrix truncated arrays and squaring the exterior norm gives the stated exponential term and \(R^{-(\kappa\alpha-\beta)}\).
Row and column translations preserve the range and positive Gram spectrum up to unitaries, and bounded translations of the finitely many projection entries preserve exponential tails.
The argument applies under the specified cyclic-minor hypothesis and uses the actual coset comparisons and Laurent exponents to construct the factorization.

In the added example each collected column belongs to \((1-t)\mathbb C[t,t^{-1}]\oplus(1+t)^2\mathbb C[t,t^{-1}]\).
The third column gives \((1-t,(1+t)^2)^t\) in \(H\) and \((0,(1+t)^2)^t\) in an outside right coset.
Such a coset must occur since \(H\) is cyclic and \(G\) is non-elementary.
Their difference and the second of these vectors generate the displayed direct sum, verifying the diagonal choice of basis and full collected row rank after division even at \(t=1\).
The factors \(1-t\) and \((1+t)^2\) are coprime, so the Smith factors of \(D\) are a unit and their product up to units.
Their maximal unit-circle zero order is two at \(-1\), giving nonclosed range, positive spectral exponent \(1/4\) and the shell condition \(\kappa>4\beta\).

The \(21\) entry of \(AA^*\) is exactly \((1+t)^2V(1-t^{-1})\).
The identity representative contributes \(t^2+t-1-t^{-1}\).
For \(x\notin H\), equality of terms \(t^ixt^j=t^{i'}xt^{j'}\) forces \(t^{i-i'}=xt^{j'-j}x^{-1}\).
The disjoint fixed-point pairs exclude any nonidentity common power, so both exponents agree and all six terms from this representative are distinct.
Representatives of different double cosets have disjoint contributions.
Thus \(e,t\) and each representative \(x\) occur in the resulting support, as they also do in the input entry \((1+t)^2V\).
These elements generate \(G\), since every chosen generator belongs to some represented \(HxH\) or to \(H\).
Left differences of the support therefore generate \(G\), and a left and a right translation of one entry merely conjugate that difference group.
In \(AA^*\), independent column translations of \(A\) cancel, and row translations translate the two ends of the \(21\) entry.
For the specified four-line group no free subgroup can contain this row-product support, since the two nonzero characteristic-two factors have zero product, whereas a free group's bi-invariant order gives a unique least term in such a product.

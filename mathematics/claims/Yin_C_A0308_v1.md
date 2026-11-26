---
author: Yin
---

# All support-trace pairs of a two-label rank-one commutator sum

## Statement

Let \(H=\langle s,t\rangle\) be a nontrivial torsion-free group with regular scalar group-ring injectivity.
Use its regular right multiplications \(\rho_s,\rho_t\) on \(\ell^2(H)\).
For bounded operators \(T_s,T_t\) of ordinary complex rank at most two, consider only the cases when
\[
                F=[\rho_s,T_s]+[\rho_t,T_t]
\]
has ordinary rank one.
Write \((x,y)\) for the regular dimensions of the closed spans of the left translates of the range of \(F\) and the range of \(F^*\), respectively.
Let \(\mathcal D\) consist of all noninteger regular nullities of \(B+At-s(D+Ct)\) for complex two-square coefficients on these same marks.
Then \(\mathcal D\subset(0,1)\) and the complete set of attainable pairs is
\[
 \bigcup_{\delta\in\mathcal D}\left(
     (0,\delta]\times(0,1-\delta]\ \cup\
     (0,1-\delta]\times(0,\delta]\right).
\]
Both upper corners of each pair of rectangles are attained by bounded group von Neumann algebra vectors.
In particular the supremum of \(\min(x,y)\), with zero included for the empty case, equals the supremum of \(\min(\delta,1-\delta)\) for \(\delta\in\mathcal D\), with the same convention.

For every fixed marked group as above with a character of order 24 taking \(s,t\) to \(3,4\), there are \(\epsilon>0\) and a finite marked word neighborhood such that every such rank-one output there satisfies
\[
                            \min(x,y)\le1/2-\epsilon .
\]
Here the other marked groups in the neighborhood retain torsion-freeness, scalar injectivity and the same character degrees.
The input operators can be arbitrary bounded finite-rank operators with these two rank budgets.
For any marking with an abelian quotient of order 24, even without fixing its two degrees, the exactly complementary pair \((1/2,1/2)\) cannot occur.
These restrictions apply to this two-label part of the [rank-one criterion](Yin_C_A0157_v1.md#separating-the-ranges-and-excluding-rank-one).

## The increment and the smaller side

Under scalar injectivity the [two-label small-input exclusion](Yin_C_A0166_v2.md#statement) handles cyclic labels and any rank budget smaller than two on one side.
Use two occurrences of each label, allowing a zero tensor if necessary.
The [finite-rank pencil construction](Yin_C_A0167_v2.md#passing-from-a-commutator-sum-to-a-fractional-column-increment) then gives a four-column pencil \(L\), a constant column \(\alpha\), and an increment \(\gamma=\operatorname{rk}[L,\alpha]-\operatorname{rk}L\) satisfying
\[
                                  x\le\gamma\le1-y .
\]
Indeed for a rank-one tensor \(u\otimes v\) the two left-translation spans have the traces of the right support of \(u\) and the left support of \(v\).
The two inequalities follow by applying the cokernel projection of \(L\) to \(\alpha\) in that construction.
Both \(x,y\) are positive, so \(0<\gamma<1\).

Let \(L'\) be obtained by taking the target quotient by \(\mathbb C\alpha\).
One has \(\operatorname{rk}[L,\alpha]=1+\operatorname{rk}L'\).
Any noninteger rank of a pencil on the four occurrences belongs to \((3,4)\) and equals \(2+\operatorname{rk}K=4-\delta\) for a rectangle on the same labels, by the [four-column reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound).
The same linearization applied in the other direction puts every noninteger nullity of an individual rectangle in \((0,1)\).

If \(L\) has noninteger rank, its constant output span has dimension four.
The column \(\alpha\) lies there since otherwise its increment is one.
The quotient pencil on at most three rows has integer rank, so \(1+\operatorname{rk}L'=4\), giving \(\gamma=\delta\).
If \(L\) has integer rank, \(L'\) has noninteger rank \(4-\delta\) and \(\operatorname{rk}L-1<\operatorname{rk}L'<\operatorname{rk}L\).
As \(L\) has four columns this forces \(\operatorname{rk}L=4\) and \(\gamma=1-\delta\).
This proves containment in the stated union.

## Attaining every pair in the union

Start with a rectangle of noninteger nullity \(\delta\) and its four-row linearization \(L\) of rank \(4-\delta\).
For any nonzero constant column in its four-dimensional target, taking the quotient gives an integer rank between \(3-\delta\) and three, hence exactly three.
The increment is therefore \(\delta\).
Let \(E\) be the cokernel projection of \(L\), \(p\) the kernel projection of \(E\alpha\), and \(w=\alpha^*E\).
The [reverse pencil construction](Yin_C_A0167_v2.md#constructing-the-rank-one-sum-from-the-pencil) builds the two prescribed commutator inputs with output tensor \(-w\alpha\otimes p b\), where \(b\) is bounded and is a unit in the affiliated algebra.
The vectors are bounded; \(w\alpha=(E\alpha)^*E\alpha\) has rank \(\delta\), and \(pb\) has image support \(p\) of trace \(1-\delta\).
Thus the first upper corner occurs.
Taking the adjoint gives the opposite corner on the same ordered list: for a unitary \(U\), \([U,T]^*=[U,U^{-1}T^*U^{-1}]\), with the same ordinary rank bound on the input.

To obtain the entire rectangles, multiply a realized output tensor \(u\otimes v\) on its outside legs by a projection \(e\) in the left support of \(u\) and a projection \(f\) in the right support of \(v\).
The corresponding left multiplications on \(\ell^2(H)\) commute with every \(\rho_g\), so replacing each input by \(eT_j f\) produces \(eu\otimes vf\).
Its two support traces are exactly \(\tau(e),\tau(f)\) by dense range on the appropriate supports and polar decomposition.
The finite group von Neumann algebra here is diffuse: a minimal projection would have atomic central support and give a nonzero finite-dimensional factor summand, whose trace Hilbert space would be a finite-dimensional subrepresentation of the left regular action.
Translation by any infinite-order group element has no eigenvectors in the regular representation.
Thus no such summand exists.
In a diffuse finite von Neumann algebra every projection admits subprojections of every smaller trace, by successive subdivision or a diffuse abelian subalgebra in its corner.
This gives all positive pairs in the two rectangles and proves the supremum identity.

Finally apply the [coefficient-independent local gap](Yin_C_A0307_v1.md#statement) to every rectangle contributing to the union at the normalized marking.
For arbitrary degrees, \((1/2,1/2)\) would force \(\delta=1/2\) in the union, excluded by the [order-24 marking reduction](Yin_C_A0241_v1.md#statement) and the [exact half-kernel theorem](Yin_C_A0303_v1.md#statement).

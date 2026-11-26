---
author: Yin
---

# Substituting a single group element in the Gram compressions of the order-25 remainder

## Statement

Let \(R\in M_{14}(\mathbb CN)\) be the [order-25 companion remainder](Yin_C_A0222_v1.md#the-companion-over-the-actual-commutator-subgroup), and let \(J_0\le N\) contain all group elements in its support.
Assume that for every finite set of nonidentity elements of \(J_0*\langle x\rangle\), with \(x\) an infinite cyclic generator, there is a single \(w\in N\) such that the homomorphism fixing \(J_0\) and taking \(x\) to \(w\) leaves every member of the set nonidentity.
For \(X=R,R^*\), independently choose a column \(c_X\) and collect the other thirteen columns in \(F_X\).
There are fixed thirteen-word polynomial columns \(v_X(x)\) with complex vector coefficients and fixed positive three-by-three polynomial Gram matrices \(Q_X(x)\) as constructed below.
With the usual unnormalized matrix trace,
\[
            \inf_{w\in N}\bigl(\dim_N\ker Q_R(w)
                        +\dim_N\ker Q_{R^*}(w)\bigr)=0 .
\]
For the same choices approaching this infimum, the two-by-two Gram matrices of \(c_X,F_Xv_X(w)\) both have ranks tending to \(3/2\).
Each trial column uses thirteen fixed words in the same substituted element \(w\).
The three-column Gram matrix also uses the conjugating word \(w_1\) defined below.
Suppose the strictly positive values of the displayed sum are bounded away from zero, allowing the set of positive values to be empty.
Then there is one \(w\in N\) for which both \(Q_X(w)\) are affiliated units, both two-by-two Gram matrices have rank exactly \(3/2\), and both \(p_{\operatorname{im}R},p_{\ker R}\) belong to \(M_{14}(D_2(N))\).
Here \(D_2(N)\) denotes two layers of scalar inversion in the original regular affiliated algebra, and image projections use closed images.

There is also a weaker group condition with a consequence for the [unrestricted polynomial columns](Yin_C_A0232_v1.md#adding-one-monomial-in-the-original-group).
If \(J_0\cap\mathrm{FC}(N)=\{1\}\), where \(\mathrm{FC}(N)\) consists of elements having finite \(N\)-conjugacy classes, the center-valued rank of \(R\) is \((3/2)1\).
For either \(X\) the supremum of the positive scalar Schur ranks on columns using a total of at most \(k\) monomials in \(N\) is at least \(\tfrac12(1-(25/26)^k)\), including zero ranks when \(k=0\).
Finite simultaneous avoidance as above implies this weaker group condition.

## The two polynomial matrices and their free evaluations

For each \(X\), omit its subscript temporarily and write \(c,F\) for the chosen columns.
The scalar \(a=c^*c\) is an affiliated unit, \(P=ca^{-1}c^*\) is the orthogonal projection onto the closure of the image of \(c\), and \(B=(I-P)F\) is bounded of rank \(1/2\). [Bounded Gram computation](Yin_C_A0232_v1.md#the-bounded-schur-complement)
Let \(e\) be the initial projection of \(B\) and write \(\tau\) for the regular scalar trace.
Choose a complex unitary \(V_X\) for which all diagonal entries of \(V_X^*eV_X\) have scalar trace \(1/26\); diagonalization of \((\tau(e_{ij}))\) followed by Fourier conjugation does this.
These choices are independent of the substituted group element.
Choose once an infinite-order \(g\in J_0\), which exists by torsion-freeness and the noninteger rank of \(R\).
In \(J_0*\langle x\rangle\) set
\[
 w_0=xgx^{-1},\quad w_1=x^2gx^{-2},\quad
 v_X(x)=\frac{1}{\sqrt{13}}V_X\big(w_0^i g w_0^{-i}\big)_{i=1}^{13}
\]
with the final tuple arranged as a column.
For each substitution let \(W_X=Bv_X\), \(\sigma_X=W_X^*W_X\).
These are bounded operators in the first inverse layer since \(P=ca^{-1}c^*\).
The two-by-two polynomial Gram matrix of \(c,Fv_X\) has rank \(1+\operatorname{rk}\sigma_X\).

Define \(Q_X(x)\) to be the Gram matrix of the following three polynomial columns in two copies of the fourteen-coordinate output:
\[
     (c,0)^{\mathsf t},\qquad (0,c)^{\mathsf t},\qquad
     (Fv_X,(Fv_X)w_1^{-1})^{\mathsf t}.
\]
The first two columns have diagonal Gram matrix \(a I_2\).
Eliminating these two pivots subtracts their orthogonal output projections \(P\oplus P\), so the final positive scalar is
\[
           \sigma_X+w_1\sigma_Xw_1^{-1}.
\]
Consequently at every substitution,
\[
     \dim\ker Q_X
       =1-\operatorname{rk}(\sigma_X+w_1\sigma_Xw_1^{-1})
       \ \ge\ 1-2\operatorname{rk}\sigma_X\ \ge\ 0 .
\]
Indeed \(\operatorname{rk}\sigma_X\le\operatorname{rk}B=1/2\), and ranks are subadditive.

In the free product itself, \(J_0,\langle w_0\rangle,\langle w_1\rangle\) freely generate their free product by normal form.
The [finite free column calculation](Yin_C_A0232_v1.md#a-finite-column-attaining-the-rank) gives \(\operatorname{rk}\sigma_X=1/2\) over \(J_0*\langle w_0\rangle\).
The two scalar kernel projections in the last sum are free of trace \(1/2\), hence have zero intersection.
The sum is positive and injective, so \(Q_X(x)\) is injective in the free product for each \(X\). [Free projection and complementary scalar argument](Yin_C_A0232_v1.md#recovering-the-original-image-and-kernel-projections)

## Matching a finite trace moment in the original group

Write \(Q_X(x)=\sum_h C_{X,h}h\) in the free product with three-by-three complex coefficient matrices.
Choose a real \(C>0\) exceeding both finite sums \(\sum_h\|C_{X,h}\|\).
It bounds the operator norms of every \(Q_X(w)\) and of the free evaluations, since all group elements act unitarily.
For \(k\ge1\) the polynomial \(D_{X,k}(x)=(I_3-Q_X(x)/C)^k\) is a positive contraction at the free evaluation and at every group substitution.
This operator dominates the kernel projection of the corresponding \(Q_X\) by scalar functional calculus.
At the free evaluation its unnormalized trace decreases to zero because the kernel is zero.

Given \(\varepsilon>0\), choose \(k\) so that the sum of the two free traces is less than \(\varepsilon\).
Apply the avoidance hypothesis to the union of the nonidentity free words in the diagonal supports of both \(D_{X,k}(x)\).
For the resulting single \(w\), the identity coefficient of each diagonal entry is exactly the same in \(N\) as in the free product.
The two regular traces of the substituted moments therefore equal their free traces.
Together the inequalities give \(\dim_N\ker Q_R(w)+\dim_N\ker Q_{R^*}(w)<\varepsilon\).
The Schur rank bounds in the preceding section give the two simultaneous limits from below.

If positive total nullities have a lower bound \(\gamma>0\), choosing \(\varepsilon<\gamma\) forces both kernels to vanish at the same substitution.
This also holds immediately when every total nullity is zero.
For each \(X\), \(\operatorname{rk}\sigma_X=1/2\) and \(b=w_1\sigma_Xw_1^{-1}\) is a positive first-layer scalar of rank \(1/2\) with \(\sigma_X+b\) an affiliated unit.
Thus the [one-further-inverse formula](Yin_C_A0232_v1.md#recovering-the-original-image-and-kernel-projections) yields
\[
              p_{\operatorname{im}X}
                  =P+W_X(\sigma_X+b)^{-1}W_X^*
                        \ \in\ M_{14}(D_2(N)).
\]
For \(X=R^*\) its complement is the kernel projection of \(R\).
Without the positive-gap premise, the moment comparison supplies an infimum and can allow a sequence of strictly positive total nullities tending to zero.

## The condition on finite conjugacy classes

If a nonidentity \(h\in J_0\) has an \(N\)-conjugacy class of finite size \(l\), every \(w^{l!}\) centralizes \(h\) by the permutation action on that class.
The word \(x^{l!}h x^{-l!}h^{-1}\) is nonidentity in \(J_0*\langle x\rangle\) and becomes the identity at every substitution in \(N\).
This contradicts the stated avoidance property.

Now assume just \(J_0\cap\mathrm{FC}(N)=\{1\}\).
Every central bounded element of \(\mathcal N(N)\) has square-summable Fourier coefficients constant on \(N\)-conjugacy classes.
Its coefficients therefore vanish on every nonidentity group element of \(J_0\).
Writing \(Z_N\) for the normalized center-valued trace, this gives \(Z_N(y)=\tau(y)1\) first for \(y\in\mathbb CJ_0\), by pairing with all bounded central elements, and then for \(y\in\mathcal N(J_0)\) by \(L^2\)-density and contractivity of the trace-preserving conditional expectation onto the center.
The regular subgroup inclusion contains the support projections of \(R,B\) by spectral calculus.
Thus \(R\) has center-valued rank \((3/2)1\), and \(d=\sum_i Z_N(e_{ii})=(1/2)1\) for both choices of \(X\).
In the [one-monomial growth estimate](Yin_C_A0232_v1.md#adding-one-monomial-in-the-original-group), the current column center-valued rank \(r\) then satisfies \((d-r)(1-r)\ge(1/2-r)/2\) pointwise.
The same recurrence gives the displayed exponential estimate throughout \(N\), regardless of other finite conjugacy classes in \(N\).

## Assessment history

### Decision one-substitution-for-the-two-companion-projections

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:44 |
| status | proved |
| reason | Independent review verified the paired three-column Gram tests, common substitution, finite-conjugacy criterion and second-layer consequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The finite word condition, simultaneous approximation and the exact implication. |
| argument | [The two polynomial matrices and their free evaluations](#the-two-polynomial-matrices-and-their-free-evaluations) | Both free evaluations, positive Schur complements and the auxiliary conjugate. |
| argument | [Matching a finite trace moment in the original group](#matching-a-finite-trace-moment-in-the-original-group) | Finite moment support and one substitution for both zero-defect tests. |
| argument | [The condition on finite conjugacy classes](#the-condition-on-finite-conjugacy-classes) | Scalar center-valued trace on the coefficient subgroup and the separate rate. |
| review | [One substitution for the two companion projections](../audits/reviews/Yin_R_A0199_v1.md#one-substitution-for-the-two-companion-projections) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-one-substitution-for-the-two-companion-projections)

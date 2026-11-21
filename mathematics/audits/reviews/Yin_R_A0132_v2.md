---
author: Yin
---
# Independent review of the single-parameter coefficient transfer

On 2026-11-21 at 05:03 UTC, a separately assigned reviewer examined the complete statement and argument of Yin's C_A0096_v2.
The reviewer received the fixed claim and the scope of the inspection without participating in its development or receiving development discussions, author explanations or previous findings on v2.
The earlier v1 review was consulted for the inherited division-closure and alternation results.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0096_v2.md#statement) | The two direct-power bounds, exceptional set and degenerate cases, together with all four assertions under the square hypothesis. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0096_v2.md#argument) | All seven proof sections, including the right-module degree calculation, specialization at every parameter, rank-one updates and companion examples. |
| [Whole finding](#whole-finding) | [Affiliated alternation](../../claims/Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings) | Division-closure criterion, coordinate embeddings and the unit test at the actual dimension of the coefficient span. |
| [Whole finding](#whole-finding) | [Earlier finite-power bound](../../claims/Yin_C_A0096_v1.md#a-bound-for-the-direct-power-needed-by-a-prescribed-size) | Scope of the earlier bound for matrices with finitely many scalar coefficients. |
| [Whole finding](#whole-finding) | [Moment comparison](../../claims/Yin_C_A0097_v1.md#argument) | Numerical obstruction to deducing integrality of individual entries from the specified moments. |

## Whole finding

The proof establishes the rank formula (16) at every parameter, the bound of \(rh\) exceptional parameters and the four stated consequences of rational Atiyah on \(G^2\).

For the square test, the bounded transform \(cx\) satisfies \((cx)(cx)^*=xx^*(1+xx^*)^{-1}\leq1\).
If \(\Delta_x=0\), (5) equates two elementary tensors of Hilbert-space vectors, with \(c\delta_e\ne0\).
Applying a functional with value one at \(c\delta_e\) gives \((cx)\delta_e=\alpha c\delta_e\), and the separating identity vector and the affiliated inverse of \(c\) give \(x=\alpha I\).
For nonscalar \(x\), the division property on the square makes \(\Delta_x\) invertible.
For \(p=P_{\ker(x-\lambda)}\), both coordinate copies of \(x\) act as \(\lambda\) on \(p\otimes p\), so \(\Delta_x(p\otimes p)=0\) and \(\tau(p)^2=0\).
Polar decomposition in the finite algebra then makes \(x-\lambda\) a unit.
Factoring \(a+\lambda b=b(b^{-1}a+\lambda)\) for \(b\ne0\) gives (7), including the case of a scalar quotient.
Scalar factorization gives invertibility of each nonzero complex polynomial evaluated at a nonscalar \(x\), so localization is injective and elimination over its image gives the integer matrix rank in assertion 2.

For \(R=D[T]\), Euclidean elimination uses column entries in the form \(a=qf+r\) and row entries in the form \(b=fq'+r'\).
A nonzero remainder strictly lowers the pivot degree.
When all remainders vanish, clearing the column first leaves the pivot row unchanged, and clearing the row then preserves the zeros below the pivot.
Induction gives (9) with polynomial inverses, and passage to \(F=D(T)\) identifies the number of nonzero entries as \(r\).
As a right \(D\)-space, \(R/fR\) has basis the classes of \(1,T,\ldots,T^{\deg f-1}\), with the empty basis for a unit.
For any nonzero representative \(a\), the right Ore condition gives a nonzero common right multiple \(as=ft\), so the class of \(a\) is killed on the right by \(s\ne0\).
The free summand is torsion-free, which proves (11).

Over \(F\) select independent columns and independent coordinate rows on their span, giving the full-rank \(r\times r\) submatrix \(B\).
Writing \(\mathcal V=\operatorname{im}_F P\), a common right denominator shows that \((\mathcal V\cap R^m)/P R^n\) is precisely the torsion submodule.
The projected equality \(\pi x=\pi P y\) for \(y\in R^n\) forces \(x=P y\) since both vectors belong to \(\mathcal V\).
This proves the injection (13), and the column inclusion \(B R^r\subseteq(\pi P)R^n\) gives the surjection (14) in the stated direction.
Inside \(R_{\leq k+h}^r\), the kernel of the map to \(\operatorname{coker}B\) contains the \(r(k+1)\)-dimensional space \(B R_{\leq k}^r\).
Each truncated image has dimension at most \(rh\), and every finite independent set in the cokernel lies in one such image.
Together these estimates give \(\sum_i\deg f_i\leq rh\) even for a rectangular or rank-deficient \(P\).

Every coefficient list has a complex basis chosen among its original elements of \(D\).
For a nonzero value \(f_i(\lambda)\) the required arity is at most \(\deg f_i+1\leq rh+1\).
The coordinate inclusions preserve the group trace, so integrality on \(G^{rh+1}\) supplies the rational hypothesis at each arity used by the alternating tensor test.
Its external input is the division-closure criterion for torsion-free groups at \(F=\mathbb Q\), checked at the level of its hypotheses and statement. [Lück and Linnell, Theorem 2.3(3)](https://msp.org/akt/2018/3-1/akt-v3-n1-p02-s.pdf#page=11)
Thus each evaluated diagonal entry is a unit or zero, and even at singular parameters the polynomial changes of basis evaluate to invertible affiliated matrices.
A scalar Vandermonde inverse applies to the coefficients in the complex vector space \(U(G)\), giving at most \(\deg f_i\) distinct zeros for the \(i\)th diagonal polynomial.
Taking their union proves the claimed exceptional-set bound, and descent from the larger coordinate power uses \(r\leq\min(m,n)\).
If \(r=0\), injectivity of \(R\hookrightarrow F\) gives \(P=0\).
If \(h=0\), elimination uses only \(D\).
Under the asserted factorization certificate, the square test applies to each factor, and the ordered product of its values is zero or a unit at every \(\lambda\).

For the rank-one update put \(k=\operatorname{rank}_D A\) and \(s=q(\lambda)\).
The cases \(B=0\) and \(s=0\) give rank \(k\).
For \(s\ne0\), reducing \(A\) to an identity block also transforms the two factors of \(B=uv\), with complementary parts \(u_0,v_0\) as in (17).
When both complementary parts survive, eliminating the \(s u_1\) and \(s v_1\) blocks in (18) leaves rank \(k+1\).
When precisely one survives, the row or column elimination leaves a copy of \(I_k\), and the active matrix has only \(k\) columns or only \(k\) rows, respectively.
When neither survives, taking the Schur complements of \(I_k\) and \(1\) gives (19), with the order \(v_1u_1\) required over \(D\).
The square test on \(1+s v_1u_1\) then gives rank \(k-1\) or \(k\).
The reductions include rectangular matrices and empty complementary blocks, and use \(s\) only as a central scalar.

For the bounded monic companion, (21) identifies the two kernels by a module map whose squared norm on each vector is multiplied by \(\sum_{j=0}^{h-1}|\lambda|^{2j}>0\).
Rescaling gives an equivariant isometry, hence equality of unnormalized nullities.
The two eigenvalues of the displayed rational \(2\times2\) example are distinct, so the tensor products of matching eigenlines span the two-dimensional kernel of its tensor difference.
For a selfadjoint matrix the joint spectral measure on the two group coordinates is the product measure, whose mass on the diagonal is the sum of squared atom masses.
Four masses \(1/2\) give total mass two and squared sum one.
This last calculation tests the inference from those two integer quantities alone.
Whether the square hypothesis suffices for arbitrary matrix polynomials remains open here, as does the unrestricted question in the [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).

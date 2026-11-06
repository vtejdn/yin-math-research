---
author: Yin
---

# Remaining almost-sure controls for three Wigner factors

This continuing investigation concerns the real-input part of [F0012](../tasks/Yin_T_F0012_v3.md#contract).
The complete symmetric-carrier extension and its outer-polynomial and ordered-product deductions are now fixed in [the reviewed C_F0186_v7 theorem](../claims/Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed), with its [full argument](../claims/Yin_C_F0186_v7.md#argument).
The [reviewed nonsymmetric-carrier theorem](../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) now proves the three-real-factor logarithmic limit in probability and arbitrary-coupling upper-limit equality at every fixed parameter.
This Draft retains the stronger full-sequence almost-sure logarithmic and Brown questions, together with useful algebraic approaches to them.
The [complex symmetric shift theorem](../claims/Yin_C_F0188_v2.md#statement) and [arbitrary-complex-shift intermediate theorem](../claims/Yin_C_F0187_v2.md#statement) retain their exact accepted scopes.

<a id="candidate"></a>
## Fixed carrier finding and remaining question

The earlier symmetric-carrier theorem covers \(R=(x_1+Q)H\) when the entire carrier is reversal symmetric and has its displayed finite conditional-shift product certificate.
Examples include \(x_1x_2x_3x_2\) and \((x_1+Q)h(x_2+Q_2)\).
Its root-factorization argument also covers the zero-shift logarithmic determinant of any finite ordered product of the displayed classes.
Consequently the zero-shift determinant of \(R=x_1x_2x_3\) has the stronger almost-sure limit from that deduction.
The later nonsymmetric-carrier theorem covers its nonzero-shift logarithms in probability and their almost-sure upper limits; full-sequence almost-sure logarithmic and Brown convergence remain unresolved here.

## The actual nonsymmetric shift

For real symmetric inputs, \(H=W_2W_3\) is generally not symmetric, even though both factors are.
For \(z\ne0\), conditioning on \(W_2,W_3\) and using their polynomial invertibility events gives
\[
 W_1W_2W_3-zI
 =\bigl(W_1-z(W_2W_3)^{-1}\bigr)W_2W_3.
\]
The actual shift \(-z(W_2W_3)^{-1}\) is generally not complex symmetric, so C_F0188_v2 cannot be invoked.
The accepted intermediate estimate already applies to this independent arbitrary complex shift, and its product inequality supplies the growing intermediate range of the output.
What is missing in this approach is a summable polynomial least-singular-value floor, or a weaker estimate sufficient for the bottom negative-logarithmic contribution, for this actual product-inverse shift.
The statement is an unresolved interface rather than a universal arbitrary-shift conjecture or a necessary condition for every possible proof.

## Existing source boundary

The [retained ORSV15 inspection](../ledger/Yin_L_F0061_v1.md#two-wigner-factors-are-an-informative-benchmark) gives a two-real-Wigner product theorem with additional \(2+\tau\) moments and its precise conditional-symmetry mechanism.
It does not discharge this three-factor finite-variance interface.
The focused new search and its actual source-inspection limits are recorded below.
No claim that this exact interface is a publicly named open problem is made.

## Fixed cofactor controls

The [reviewed cofactor theorem](../claims/Yin_C_F0194_v1.md#decision-isolated-minor-reviewed) owns the complete symmetrized-adjugate identity, its exact failed row-to-kernel inference example, and the isolated-minor probability bound.
Its [fixed proof](../claims/Yin_C_F0194_v1.md#argument) supplies the rank-one factorization, complete nonsymmetric-offset profile adaptation, parameter order and summable arbitrary-coupling conclusion.
The first version controls only its explicitly isolated or exactly corank-one principal-minor branches.
The [reviewed second version](../claims/Yin_C_F0194_v2.md#statement) separately controls full corank at least two for arbitrary polynomially bounded complex offsets and [independent random shifts](../claims/Yin_C_F0194_v2.md#random-shift-statement).
Its [universal kernel anti-concentration](../claims/Yin_C_F0194_v2.md#kernel-anticoncentration), [measurable choices and shared-border calculation](../claims/Yin_C_F0194_v2.md#border-rank), [uniform truncated-law rank chain](../claims/Yin_C_F0194_v2.md#rank-chain), and [product reduction](../claims/Yin_C_F0194_v2.md#product-corank-reduction) are fully retained in that fixed argument.
The [rank-growth source attribution and inspection limits](../claims/Yin_C_F0194_v2.md#rank-growth-attribution) also remain there.
The identities below retain separate approaches to stronger full-product estimates without duplicating these fixed proofs.

## What the reviewed assembly leaves for the three-factor problem

For the original product, set F=-z(W_2W_3)^(-1) on the accepted polynomial norm and invertibility events for W_2,W_3, and set F=0 otherwise.
These events have arbitrarily prescribed polynomially small complements, and the extension stays independent of W_1.
The [reviewed arbitrary nonsymmetric-shift floor](../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed) applies to W_1+F and treats the actual low-matching tiny-ratio intersection through its internal-row and second-smallest estimates.
Its high-matching contribution is only O(sqrt(log(2+N)) N^(-1/18)), which is not summable as stated.
The complete propagation to the three-factor logarithmic probability limit and arbitrary-coupling limsup is retained in [the fixed carrier argument](../claims/Yin_C_F0186_v10.md#argument), with Q=0 and H=x_2x_3.
No vanishing mean probability of the unrestricted low-matching event is needed for that conclusion.
The continuing mechanisms below seek stronger estimates for the full-sequence almost-sure or planar question; a merely vanishing failure probability would reproduce an already resolved determinant subcase.
The [fixed method comparison](../ledger/Yin_L_F0066_v1.md#low-matching-structure) retains the diagonal-plus-hubs complement and the large-fiber obstruction to naive Riccati parametrization.

## A paired-cofactor identity for the complementary branch

This is a continuing algebraic lead, without an adopted small-value conclusion.
For an actual minor D put S=(D+D^T)/2 and K=(D-D^T)/2, and assume S is invertible.
With Q=sym adj D as in the fixed theorem, direct multiplication gives
\[
 T=D S^{-1}D^T=S-KS^{-1}K,\qquad TQ=(\det D)I.
\]
Indeed the fixed identity D^T Q=S adj D implies the second equality after multiplying by D S^{-1} on the left.
Expanding (S+K)S^{-1}(S-K) proves the first equality.
There is also an exact complex-symmetric block realization:
\[
 \mathcal B=\begin{pmatrix}S&-K\\K&-S\end{pmatrix},
 \qquad \mathcal B^T=\mathcal B.
\]
Its Schur complement about \(-S\) is \(S-KS^{-1}K=T\).
Writing \(y=S^{-1}Kq\), the equation \(Tq=(\det D)a\) becomes the coupled system
\[
 S q-Ky=(\det D)a,\qquad Kq-Sy=0.
\]
For \(D=X+F\), the random part of this block pencil is \(\operatorname{diag}(X,-X)\).
It consists of two coupled copies of the same Wigner matrix, so complex symmetry alone does not make it an iid Wigner matrix of size \(2N\) to which the scalar symmetric-shift floor applies.
Treating \(Ky\) as a free center when \(K\) has full rank retains a full-dimensional precision cost.
In the actual product-inverse setting the coefficients \(S,K\) also depend on the independent second and third Wigner inputs; exploiting that randomness would require a justified joint count rather than conditioning it away and then assuming a bounded-dimensional correction.
No such joint count is asserted here.
Thus, if a future inverse-concentration step supplies a structured vector q=Q a with a supported on a bounded set J, then
\[
 S q=K S^{-1}Kq+(\det D)a.
\]
Outside J, its right side lies in the fixed range of K.
The symmetric-part floor and polynomial norm events control the magnitude of this correction by a fixed power of dimension times the norm of q.
For bounded rank K, this suggests a finite-dimensional center parameter in a structured-vector row count.
The corresponding count and its exact inverse-theorem interface have not been supplied here.
For the actual product-inverse shift, K can have rank proportional to dimension, so the bounded-rank observation does not close that original case.
Indeed, for invertible real symmetric B,C and nonzero z, the skew part of F=-z(BC)^{-1} has the same rank as CB-BC, by multiplication with the invertible factors of \((BC)^{-T}((BC)^T-BC)(BC)^{-1}\).
Take B diagonal with distinct nonzero entries and C invertible real symmetric tridiagonal with every adjacent off-diagonal entry nonzero.
Their commutator is skew tridiagonal with nonzero adjacent entries, so it has rank N for even N and N-1 for odd N, as seen by its even-dimensional principal determinants.
The resulting polynomial nonidentity gives these ranks almost surely for two independent GOE inputs, with their own almost-sure invertibility.
Thus bounded skew rank fails even within an allowed Gaussian model of the original product.
A parameter grid for a full-dimensional correction can introduce leading entropy depending on the fine precision, which the current profile argument does not absorb.
The useful next test is whether the original product-inverse structure constrains this correction more strongly than its ambient rank suggests.

<a id="three-factor-middle"></a>
## The original three-factor middle range still has summable failures

For P_N=W_1W_2W_3-zI, use the independent shift F_N=-z(W_2W_3)^(-1) on the one-factor invertibility event and zero otherwise.
The [accepted one-factor floors](../claims/Yin_C_F0188_v2.md#statement), applied with zero shift and a probability exponent greater than two, make the inverse-event failures summable.
Apply [C_F0187_v2](../claims/Yin_C_F0187_v2.md#statement) to W_2,W_3 with zero shift and conditionally to W_1+F_N.
Its intermediate failures are summable as well.
On these events the exact factorization and [deterministic product inequality](../claims/Yin_C_F0186_v6.md#argument) give
\[
 a_k(P_N)\ge c(k/N)^3,\qquad C N^{3/4}\le k\le N,
\]
where a_k are increasing singular values and C is fixed.
To obtain this bound, distribute k+2 among three positive indices differing by at most one; for k>=6(ceil(N^(3/4))+1), each predecessor is at least k/6 and is in the intermediate range.
The product inequality is deterministic and does not require the three factors to be independent.
Thus this original three-factor middle bound is eventual almost surely under every coupling, even though the new least-value floor has only a vanishing main failure probability.
The complete finite-target and logarithmic passage is retained in [C_F0186_v10](../claims/Yin_C_F0186_v10.md#middle-and-free-log); this summable middle-range observation isolates the remaining bottom or planar obligation without duplicating that proof.

<a id="fresh-two-border-rewrite"></a>
## Keeping the second and third borders gives an exact rank-two update

The [reviewed many-index reduction](../claims/Yin_C_F0194_v3.md#polynomial-shift-consequence) identifies actual principal-minor cofactor events for \(W_1-z(W_2W_3)^{-1}\).
The subsequent probability floor already controls the needed low-matching intersection; the calculation here keeps additional randomness for possible stronger estimates.
The next calculation keeps random coordinates from the second and third factors instead of conditioning on both full factors.
It is a direct block calculation for the actual product order, not an assumption that the skew part has small rank.
No new probability or matching typicality assertion is made.

Fix an omitted index and place it first.
Write the second and third real symmetric factors as
\[
 B=W_2=\begin{pmatrix}b&x^T\\x&B_0\end{pmatrix},
 \qquad
 C=W_3=\begin{pmatrix}c&y^T\\y&C_0\end{pmatrix},
 \qquad m=N-1.
\]
Condition on \(B_0,C_0\), the first-factor principal block \(A_0=(W_1)_{\widehat i,\widehat i}\), and optionally the independent diagonal variables \(b,c\).
The vectors \(x,y\) remain independent, have independent coordinates with their respective fixed off-diagonal laws scaled by \(N^{-1/2}\), and are independent of all those conditioned blocks.
On the event that \(B_0,C_0\) are invertible put
\[
 E=B_0^{-1},\quad G=C_0^{-1},\quad
 u=Ex,\quad v=Gy,\quad
 s_B=b-x^TEx,\quad s_C=c-y^TGy.
\]
The transpose here is intentional: the factors and their inverses are real symmetric.
The full factors are invertible exactly when \(s_B,s_C\ne0\) on this event.
Set \(\beta=s_B^{-1}\), \(\alpha=s_C^{-1}\), and \(\ell=1+v^Tu\).
The inverse formulas, checked by direct block multiplication, are
\[
 B^{-1}=\begin{pmatrix}\beta&-\beta u^T\\-\beta u&E+\beta uu^T\end{pmatrix},
 \qquad
 C^{-1}=\begin{pmatrix}\alpha&-\alpha v^T\\-\alpha v&G+\alpha vv^T\end{pmatrix}.
\]
Therefore the actual principal block of the inverse product, in its correct order, is
\[
 (C^{-1}B^{-1})_{\widehat i,\widehat i}
 =GE+\beta Guu^T+\alpha vv^TE
       +\alpha\beta\ell\,vu^T.
 \tag{Fresh-product-block}
\]
The correction to \(GE=C_0^{-1}B_0^{-1}\) has rank at most two, since its columns lie in \(\operatorname{span}\{Gu,v\}\).
This is true even when the skew part of the full inverse product has rank proportional to dimension.

Define
\[
 D_0=A_0-zGE,\qquad
 U=\begin{pmatrix}Gu&v\end{pmatrix},\qquad
 V=\begin{pmatrix}u&Ev\end{pmatrix},\qquad
 R=\begin{pmatrix}\beta&0\\\alpha\beta\ell&\alpha\end{pmatrix}.
\]
Then the actual minor and the inverse two-by-two matrix satisfy
\[
 D_i=D_0-zURV^T,
 \qquad R^{-1}=\begin{pmatrix}s_B&0\\-\ell&s_C\end{pmatrix}.
 \tag{Fresh-rank-two}
\]
No inverse of \(D_0\) is used in this identity.
One-factor zero-shift floors apply to \(B,C,B_0,C_0\), with the harmless \(N\)-versus-\(N-1\) scaling adjustment, so their inverse-norm guards can have arbitrarily small polynomial failure probability.
These guards do not supply a lower bound for \(s_{\min}(D_0)\), which is another instance of the unresolved nonzero-shift product-inverse problem.
They do make all displayed background inverse coefficients polynomially bounded.
On those same guards, \(|\alpha|\le\|C^{-1}\|\) and \(|\beta|\le\|B^{-1}\|\), because these scalars are diagonal entries of the full inverses.
The guards involving the full factors depend on \(x,y\); they are retained as events rather than conditioning that would incorrectly preserve their independent border laws.

<a id="fresh-quartic-cofactors"></a>
## A denominator-free quartic matrix represents the actual matching graph

Form the augmented pencil
\[
 \mathcal K(x,y)=
 \begin{pmatrix}
 D_0&zU\\ V^T&R^{-1}
 \end{pmatrix}.
 \tag{Fresh-augmented}
\]
Its lower corner is invertible when \(s_Bs_C\ne0\), and taking that corner's Schur complement gives
\[
 \det\mathcal K=s_Bs_C\det D_i.
 \tag{Fresh-det}
\]
This formula does not require \(D_0\) or \(D_i\) to be invertible.
For \(1\le j,k\le m\), delete top-block row \(k\) and top-block column \(j\) from \(\mathcal K\), leaving both augmented rows and columns, and define
\[
 \mathcal A_{jk}(x,y)
 =(-1)^{j+k}\det\mathcal K^{(k\mid j)}(x,y).
\]
The same Schur-complement calculation gives, entrywise,
\[
 \mathcal A=s_Bs_C\operatorname{adj}D_i,
 \qquad \mathcal Q:=\operatorname{sym}\mathcal A
       =s_Bs_C\operatorname{sym}\operatorname{adj}D_i.
 \tag{Fresh-adj}
\]
It remains valid when the actual minor has corank one or its adjugate vanishes; an inverse formula for that minor is not invoked.

After the indicated principal blocks and \(b,c\) are fixed, every entry of \(\mathcal K\) is a polynomial in the \(2m\) real coordinates of \(x,y\).
The top-left entries have degree zero, the two top-right columns and two bottom-left rows have degree at most one, and the two-by-two lower corner has degree at most two.
For each determinant term, suppose that \(k\in\{0,1,2\}\) top rows select augmented columns.
Exactly \(k\) augmented rows must then select top-block columns; the remaining \(2-k\) augmented rows select augmented columns.
The total degree of that term is at most \(k+k+2(2-k)=4\).
The identical count applies to each \(\mathcal K^{(k\mid j)}\).
Thus \(\det\mathcal K\), all entries of \(\mathcal A\), and all entries of \(\mathcal Q\) have total border degree at most four, independently of \(N\).
No Gaussian substitution or changing-with-size entry law has been made; the normalization of the original fixed laws is incorporated in these polynomial coefficients.

On the actual invertibility guards, the scalar \(s_Bs_C\) is nonzero and cancels exactly from every normalized cofactor ratio:
\[
 \frac{|(\operatorname{sym}\operatorname{adj}D_i)_{jk}|}
      {\|\operatorname{adj}D_i\|_F}
 =\frac{|\mathcal Q_{jk}(x,y)|}{\|\mathcal A(x,y)\|_F},
 \qquad \operatorname{adj}D_i\ne0.
 \tag{Fresh-graph}
\]
Also \(\mathcal A=0\) if and only if the original adjugate is zero there.
Consequently the actual remaining guard can be restated exactly as a low-matching event for this quartic matrix in two still independent Wigner borders, together with the already explicit inverse and norm guards.
A small value of \(s_Bs_C\) creates no loss in (Fresh-graph), because it is a common scalar, rather than an entrywise comparison factor.

### Exact remaining obstruction after this change of exposure

The rank-two update alone does not transfer a matching from a background matrix to the actual adjugate.
Even for inverse matrices, a rank-one change can cancel every off-diagonal entry: for \(q\ge2\), let \(T_0=I_q+\mathbf1\mathbf1^T\) and \(T_1=I_q\).
Both are symmetric and invertible, \(T_1-T_0\) has rank one, and the complete nonzero off-diagonal graph of \(T_0\) disappears in \(T_1\).
Taking the inverses also yields a rank-one perturbation by direct multiplication of \((I_q+\mathbf1\mathbf1^T)^{-1}=I_q-\mathbf1\mathbf1^T/(q+1)\).
This is an obstruction to deterministic matching inheritance under low-rank updates, not an actual random-factor counterexample.

Likewise a nonzero quartic coefficient or generic nonzero edge is not a finite-radius typicality bound for atomic borders.
For example, the polynomial \(x_1^2-a^2\) vanishes at both points of a two-point law supported on \(\{-a,a\}\), despite being a nonzero polynomial.
No transfer from algebraic generic position to the law of \(x,y\) is justified by the bounded degree alone.
The specific coefficient relations in (Fresh-augmented), rather than an arbitrary quartic polynomial class, would have to give a quantitative random matching estimate.
No such estimate has been established in this calculation.
The concrete new interface is a uniform conditional bound on the low-matching event in (Fresh-graph), with the background blocks distributed as the actual independent principal Wigner blocks and with no inverse assumption on \(D_0\).
It retains two independent border vectors that are lost when conditioning on the full \(W_2,W_3\), while leaving their arithmetic and cofactor cancellations visible.

<a id="fresh-cubic-slopes"></a>
## The actual first-border linear coefficient is a cubic vector

The preceding construction also retains the linear part of the determinant in the exposed first-factor border.
Write \(W_1=\begin{pmatrix}a_1&w^T\\w&A_0\end{pmatrix}\), with the original normalized border \(w\in\mathbb R^m\).
The full inverse product has the rank-two representation
\[
 C^{-1}B^{-1}=\operatorname{diag}(0,GE)+U_*RV_*^T,
 \quad
 U_*=\begin{pmatrix}0&-1\\Gu&v\end{pmatrix},
 \quad
 V_*=\begin{pmatrix}-1&0\\u&Ev\end{pmatrix}.
\]
Accordingly the augmented full determinant is the determinant of
\[
 \mathcal L=
 \begin{pmatrix}
 a_1&w^T&0&-z\\
 w&D_0&zGu&zv\\
 -1&u^T&s_B&0\\
 0&v^TE&-\ell&s_C
 \end{pmatrix},
 \qquad \det\mathcal L=s_Bs_C\det M,
 \tag{Fresh-full-augmented}
\]
where \(M=W_1-zC^{-1}B^{-1}\).
Its principal minor deleting the first row and column is exactly \(\mathcal K\) from (Fresh-augmented).
Let \(T=\{1,\ldots,m\}\) index that minor's top block and let \(a,b\) index its two augmented positions, in this order.
These indices \(a,b\) are labels, distinct from the scalar diagonal values \(a_1,b,c\).
Cofactor expansion in the first row and column gives
\[
 \det\mathcal L
 =a_1\det\mathcal K-w^T\mathcal A w+\mathcal B^T w
                   -z(\operatorname{adj}\mathcal K)_{b,a},
\]
\[
 \mathcal B=(\operatorname{adj}\mathcal K)_{T,a}
          +z\bigl((\operatorname{adj}\mathcal K)_{b,T}\bigr)^T.
 \tag{Fresh-linear-coefficient}
\]
The sign and transpose orientation follow from expanding
\([w^T,0,-z](\operatorname{adj}\mathcal K)[w^T,-1,0]^T\).
Each entry of \(\mathcal B\) has total degree at most three in \(x,y\).
Indeed its first cofactor removes one augmented row, and its second removes one augmented column; the remaining determinant terms have degrees at most \(1+2=3\) or \(2+1=3\) by the same augmented-row-and-column count.
The final constant cofactor in the preceding display has degree at most two.
These degree bounds require no inverse of \(D_0\) or \(D_i\).

For comparison with the original exposed shifts, write \(M=\begin{pmatrix}a_1+F_{ii}&(w+f)^T\\w+g&D_i\end{pmatrix}\).
Direct multiplication of the inverse blocks gives
\[
 F_{ii}=-z\alpha\beta\ell,
 \qquad f=z(\alpha Ev+\alpha\beta\ell u),
 \qquad g=z(\beta Gu+\alpha\beta\ell v).
\]
Thus the original determinant's linear coefficient is \(-[\operatorname{adj}D_i\,g+(\operatorname{adj}D_i)^T f]\), and the exact normalization is
\[
 \mathcal B=-s_Bs_C
       [\operatorname{adj}D_i\,g+(\operatorname{adj}D_i)^T f].
 \tag{Fresh-linear-normalization}
\]
All three borders \(w,x,y\) still have their original within-dimension independence after conditioning only on the three principal blocks and diagonal entries.
The full-factor inverse guards remain events depending on \(x,y\), not conditioning that preserves their iid laws.

For a normalized Rademacher first border \(w_j=\varepsilon_j/\sqrt N\), its diagonal quadratic terms are constant and its unary coefficients before hub conditioning are \(\mathcal B_j/\sqrt N\).
After conditioning on a vertex cover \(I\) of the large off-diagonal edges, the exact unary coefficient for \(j\notin I\) is
\[
 \frac1{\sqrt N}
     \left(\mathcal B_j-2\sum_{k\in I}\mathcal Q_{jk}w_k\right).
 \tag{Fresh-covered-slope}
\]
For a general two-point first law supported on \(\{a_-,a_+\}\), put \(c_*=(a_-+a_+)/(2\sqrt N)\), \(d_*=(a_+-a_-)/(2\sqrt N)\), and write \(w_j=c_*+d_*\varepsilon_j\) with the original, possibly biased, independent signs.
With \(J=\{1,\ldots,m\}\setminus I\), the corresponding exact coefficient is
\[
 d_*\left(\mathcal B_j-2c_*\sum_{k\in J}\mathcal Q_{jk}
                  -2\sum_{k\in I}\mathcal Q_{jk}w_k\right).
\]
This is a coefficient identity, not an application of a fair-sign theorem to biased signs.
In particular even the Rademacher covered slope contains quartic hub corrections; the uncovered cubic vector alone is not the remaining unary guard.

<a id="projected-slope-pencil"></a>
## A one-parameter pencil occurs after removing two fixed directions

For this calculation only, assume \(D_0\) is invertible and write \(R_0=D_0^{-1}\).
No polynomial bound on this inverse is assumed.
Put
\[
 p=R_0Gu,\quad q=R_0v,\quad r=R_0^Tu,\quad s=R_0^TEv,
\]
\[
 c_y=s_C-zv^TER_0v,\qquad
 t_x=1+v^Tu+zv^TER_0Gu.
\]
A two-by-two Schur cofactor expansion of (Fresh-linear-coefficient) gives
\[
 \mathcal B=-z\det D_0
   \left[c_y p+t_x(q+r)
       +s\bigl(s_B-zu^TR_0Gu\bigr)\right].
 \tag{Fresh-cubic-factorization}
\]
For example, it follows by using the adjugate of
\[
 R^{-1}-zV^TR_0U
 =\begin{pmatrix}
 s_B-zu^TR_0Gu&-zu^TR_0v\\
 -\ell-zv^TER_0Gu&s_C-zv^TER_0v
 \end{pmatrix};
\]
the equality is a cofactor identity and does not assume invertibility of that two-by-two matrix or of \(D_i\).
Fix the background and \(y\), so \(q,s,c_y\) are fixed while \(t_x\) is an affine scalar function of the independent border \(x\).
Let \(\Pi\) be the complex orthogonal projection annihilating \(\operatorname{span}\{q,s\}\).
Then
\[
 \Pi\mathcal B=-z\det D_0\,
       \Pi(c_yR_0G+t_xR_0^T)E x.
 \tag{Fresh-projected-pencil}
\]
The loss of dimension in this projection is at most two.
This identifies a special one-scalar-parameter linear constraint behind small uncovered Rademacher slopes, rather than treating \(\mathcal B\) as a generic cubic vector.
The covered-slope correction in (Fresh-covered-slope) must still be retained in any application.

<a id="uniform-polynomial-pencil-bulk"></a>
## Uniform bulk for the polynomial pencil needs no inverse of the shifted background

The following development was obtained jointly by the responsible main agent and the assigned determinant agent.
It uses the accepted [finite-variance selfadjoint and Hermitized weak laws](../claims/Yin_C_F0186_v4.md#statement) and [polynomial rank-stability estimates](../claims/Yin_C_F0186_v4.md#rank-stability), rather than a new injectivity theorem for free rational functions.
For deterministic complex \(c,t\), direct multiplication gives
\[
 D_0(cR_0G+tR_0^T)D_0^T
       =(cG+tI)A_0-zGE(cG+tI).
\]
Multiplying further on the left by \(B_0C_0\) and on the right by \(C_0\) clears the unshifted inverses:
\[
 \begin{split}
 P_{c,t}(A_0,B_0,C_0)
 &:=B_0(cI+tC_0)A_0C_0-z(cI+tC_0)\\
 &=B_0C_0D_0(cR_0G+tR_0^T)D_0^TC_0.
 \end{split}
 \tag{Fresh-polynomial-pencil}
\]
The polynomial on the first line is defined even when \(D_0\) is singular.
The second identity is used only on the branch where \(R_0\) exists.

Let \(a,b,c_0\) be free variance-one semicircular elements corresponding to the independent principal blocks, and set
\[
 P_1=bac_0-zI,\qquad P_2=bc_0ac_0-zc_0.
\]
Their exact tracial Gram matrix is
\[
 \tau(P_1^*P_1)=\tau(P_2^*P_2)=1+|z|^2,
 \qquad \tau(P_1^*P_2)=0.
 \tag{Fresh-free-Gram}
\]
For the second norm, freeness first replaces the single \(b^2\) block in \(c_0ac_0b^2c_0ac_0\) by its trace one, and then
\(\tau(ac_0^2ac_0^2)=\tau(a^2)\tau(c_0^2)^2=1\).
The first norm is the analogous shorter calculation, and all terms linear in the single centered \(b\) have trace zero.
The remaining main cross term has odd total degree in \(c_0\) and changes sign under \(c_0\mapsto-c_0\), while the joint free law is unchanged, proving its zero trace.
Thus for every \(|c|^2+|t|^2=1\),
\[
 \|cP_1+tP_2\|_2^2=1+|z|^2=:g_z>0,
 \qquad \|cP_1+tP_2\|\le K_z
\]
with a fixed finite \(K_z\), since the semicircular norms equal two.
Taking \(\varepsilon_z=\sqrt{g_z/2}\) shows that the free singular law puts at least \(\delta_z=g_z/(2K_z^2)>0\) mass at singular values at least \(\varepsilon_z\), uniformly over that unit coefficient sphere.

This uniform positive fraction transfers to the finite principal blocks without higher entry moments or a growing precision net.
Fix an input spectral cutoff \(M>2\), and clip each of \(A_0,B_0,C_0\) spectrally to \([-M,M]\).
Their semicircular weak laws imply that each clipping changes rank by \(o(m)\) almost surely under every allowed cross-dimensional coupling.
The accepted polynomial rank bound makes the resulting change in \(P_{c,t}\) have rank \(o(m)\), uniformly in the unit coefficient pair, because the same finite list of words is used for all pairs.
On the clipped inputs, the polynomial pencil is operator-norm Lipschitz in \((c,t)\) with a fixed constant depending only on \(M,z\).
Choose one fixed finite net of the unit coefficient sphere whose mesh is small compared with \(\varepsilon_z\) divided by that constant.
At each point of this finite net, the accepted Hermitized weak convergence and the free bulk bound give at least \(\delta_zm/2\) singular values above \(\varepsilon_z/2\), eventually almost surely.
The rank comparison gives the same bound with a slightly smaller fraction for the clipped pencil, and the fixed Lipschitz estimate extends it to every unit pair, with threshold reduced again by a fixed factor.
Undoing the clipping loses only \(o(m)\) further singular values.
Hence fixed \(\delta'_z,\varepsilon'_z>0\) give
\[
 \inf_{|c|^2+|t|^2=1}
 \#\{j:s_j(P_{c,t}(A_0,B_0,C_0))\ge\varepsilon'_z\}
 \ge\delta'_z m
 \tag{Fresh-uniform-bulk}
\]
eventually almost surely, in particular outside a probability tending to zero.
The \(N^{-1/2}\) rather than \(m^{-1/2}\) normalization of these principal blocks differs by a scalar tending to one; after clipping its contribution is a vanishing uniform operator-norm perturbation and does not change this conclusion.
This proof uses singular-value counts and rank perturbations, not nonnormal eigenvalue stability.

On polynomial norm guards for \(A_0,B_0,C_0,E,G\), both multipliers \(B_0C_0D_0\) and \(D_0^TC_0\) in (Fresh-polynomial-pencil) have polynomial operator norm, whether or not \(R_0\) is well conditioned.
Singular-value product inequalities therefore transfer (Fresh-uniform-bulk) to a fixed positive fraction of singular values of \(cR_0G+tR_0^T\) bounded below by a fixed inverse power of \(N\), uniformly over unit \((c,t)\), on the branch \(D_0\) is invertible.
Right multiplication by \(E\) costs only the polynomial factor \(\|B_0\|\), and left multiplication by \(\Pi\) discards at most two singular directions.
Thus the projected coefficient pencil in (Fresh-projected-pencil) has a positive-dimensional singular bulk at polynomial scale after normalizing its scalar pair.
A generic bulk-degeneracy hypothesis for this actual pencil is not an additional missing premise.

### The relative normalization and covered slopes remain unresolved

Small unary slopes are measured relative to \(\|\mathcal A\|_F\), whereas (Fresh-projected-pencil) divides by \(z\det D_0\).
The displayed bulk result does not bound
\[
 \frac{\|\mathcal A\|_F}
      {|\det D_0|\sqrt{|c_y|^2+|t_x|^2}}
\]
by a fixed polynomial, nor exclude \((c_y,t_x)\) being simultaneously too small on the relevant event.
No inverse guard for \(D_0\) was proved or assumed to make that ratio harmless.
The exact singular \(D_0\) branch still has the denominator-free quartic and cubic cofactor identities, but the \(R_0\)-based projected-pencil argument is not formulated on that branch.
Furthermore the low-matching cover contributes \(2\mathcal Q_{J,I}w_I\), so a bound for the uncovered cubic vector alone is insufficient.
The scalar parameter \(t_x\) depends on \(x\); applying a fixed-parameter independent-coordinate distance bound would require a justified uniform argument, rather than conditioning on that parameter and retaining the iid law of \(x\).
These are genuine remaining interfaces after the uniform coefficient-bulk step, not counterexamples to the original determinant limits.

<a id="matching-threshold-tests"></a>
## A large polynomial shift delays the matching threshold but does not defeat every fine threshold

The [fixed finite-radius reduction](../claims/Yin_C_F0194_v3.md#statement) uses the off-diagonal graph with an edge \(ij\) when \(|Q_{ij}|\ge n^{-H}\|A\|_F\), where \(A=\operatorname{adj}D\ne0\), \(Q=(A+A^T)/2\), and \(i\ne j\).
Its [polynomial-shift consequence](../claims/Yin_C_F0194_v3.md#polynomial-shift-consequence) retains the mean probability of actual low-matching minors, rather than invoking continuous-model generic position.
A simple allowed atomic input tests the order in which its threshold exponent can be chosen.
The calculation below shows that a threshold exponent independent of the allowed polynomial shift size is impossible, but supplies no counterexample to a sufficiently fine exponent chosen after that size.
It is an elementary model calculation, not a proof of a general probabilistic matching guard.

Take an even \(n\), a real symmetric Rademacher matrix \(X_n\) with zero diagonal and independent strict upper entries in \(\{-1,1\}\), and the normalized matrix \(W_n=X_n/\sqrt n\).
All off-diagonal laws and the zero diagonal law are fixed and satisfy the original finite-second-moment and atomic permissions.
Deterministically \(\|W_n\|_F=\sqrt{n-1}\le\sqrt n\) and \(\|W_n\|\le\sqrt n\).
Let \(t=n^\gamma\) with fixed \(\gamma>2\), and first set \(D=tI_n+W_n\).
It is invertible for all sufficiently large \(n\), for every realization of the signs.
The resolvent expansion gives
\[
 D^{-1}=t^{-1}I_n-t^{-2}W_n+R_n,
 \qquad \|R_n\|\le\frac{\|W_n\|^2}{t^3(1-\|W_n\|/t)}
 \le\frac{2n}{t^3}.
\]
Moreover,
\[
 \|D^{-1}\|_F=\frac{\sqrt n}{t}
       \bigl(1+O(\sqrt n/t)\bigr).
\]
Since \(D=D^T\), one has \(Q=A=(\det D)D^{-1}\).
For every \(i\ne j\), the leading entry of \(D^{-1}\) has magnitude \(1/(t^2\sqrt n)\), and its error relative to that leading magnitude is at most \(2n^{3/2}/t=o(1)\), uniformly over all indices and all sign realizations.
The determinant cancels from the normalized cofactor ratio, yielding
\[
 \frac{|Q_{ij}|}{\|A\|_F}
 =\frac{1+o(1)}{tn}
 =n^{-\gamma-1}(1+o(1)),\qquad i\ne j,
 \tag{Diagonal-shift-threshold}
\]
with a uniform error.
Consequently the graph is empty for every fixed \(H<\gamma+1\), and complete for every fixed \(H>\gamma+1\), for all sufficiently large \(n\) and every realization.
In the latter regime its matching has size \(n/2\).
No conclusion at the equality \(H=\gamma+1\) is needed for this test.
For a size-\((N-1)\) principal minor of \(tI_N+W_N\), the same proof uses entries of magnitude \(N^{-1/2}\), inverse Frobenius norm \((1+o(1))\sqrt{N-1}/t\), and gives the same threshold transition in the original size \(N\).
Thus this is an actual-minor test, rather than a separately scaled model substituted into the cofactor question.

The same threshold delay occurs for a genuinely nonsymmetric offset.
Let \(J_n\) be the block diagonal matrix with blocks \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and put \(D=tJ_n+W_n\).
Then \(J_n^T=-J_n\), \(J_n^{-1}=-J_n\), and \(J_n\) is orthogonal.
Expanding about \(tJ_n\) gives
\[
 D^{-1}=-t^{-1}J_n-t^{-2}J_nW_nJ_n+\widetilde R_n,
 \qquad \|\widetilde R_n\|\le2n/t^3.
\]
The first term is skew, the second is symmetric, and \(J_nW_nJ_n\) is a signed permutation of the entries of \(W_n\).
For distinct indices its entries therefore still have magnitude \(n^{-1/2}\).
Also \(\|D^{-1}\|_F=(1+O(\sqrt n/t))\sqrt n/t\).
The identity \(Q=(\det D)\operatorname{sym}D^{-1}\) now gives exactly the same uniform asymptotic (Diagonal-shift-threshold), hence the same empty-versus-complete matching test.
This calculation keeps the actual symmetric Wigner dependence intact and does not use a Gaussian or continuous model.

For the raw convention \(D=tI_n+X_n\), or \(D=tJ_n+X_n\), use \(\|X_n\|\le n\) and error \(2n^2/t^3\) instead.
With \(\gamma>2\), the relative entry error still tends to zero and the ratio becomes
\[
 \frac{|Q_{ij}|}{\|A\|_F}
 =\frac{1+o(1)}{t\sqrt n}
 =n^{-\gamma-1/2}(1+o(1)),\qquad i\ne j.
 \tag{Raw-shift-threshold}
\]
The raw transition is therefore \(H=\gamma+1/2\).
Both tests are consistent with choosing a fine fixed \(H\) after the shift exponent \(\gamma\).
They rule out choosing a useful universal \(H\) independently of \(\gamma\), and show why polynomial cofactor noncancellation alone cannot specify that threshold.
No allowed shift causing low matching at every sufficiently fine fixed threshold has been constructed here.
Whether the actual product-inverse minors have growing matching at some appropriately chosen polynomial threshold remains unresolved.

## Bounded primary-source search and actual inspection limits

On 2026-11-05 the new question was searched under symmetric random matrices with arbitrary nonsymmetric deterministic perturbations, products of three Wigner matrices, and rank-two quadratic or product-of-two-linear-forms Littlewood--Offord concentration.
The queries repeatedly returned the symmetric-shift Nguyen theorem, the already inspected two-Wigner product benchmark, and general quadratic anticoncentration results.
The [Nguyen author-hosted 23-page preprint](https://people.math.osu.edu/nguyen.1261/cikk/singular-noLO.pdf), Theorem 1.3 on PDF p. 2 and its cofactor outline on pp. 4--8, was directly reread.
Its deterministic perturbation is symmetric, and its scalar iid arbitrary-matrix theorem in Theorem 1.1 is a different random input model.
The already retained published Ngu12 edition and theorem number remain distinguished in [its source notes](../audits/literature/Ngu12/readme.md).
An attempted web opening of ORSV15 arXiv:1403.6080v3 failed at that interface; its adequate existing retained inspection was reused rather than inferring a source change.

The publisher HTML of Matthew Kwan and Lisa Sauermann, [Resolution of the quadratic Littlewood--Offord problem](https://doi.org/10.1112/S0010437X25102789), was inspected at its abstract and introduction.
It gives quadratic point-anticoncentration in terms of robust dependence, not the finite-radius controlled-entropy near-kernel recovery needed above.
No theorem or proof from that source is adopted in this Draft, and no conclusion about absence of a suitable theorem elsewhere is asserted.
The search stopped after those scope checks because the direct adjugate and isolated-product calculations supplied the next discriminating local mechanism.


<a id="summable-arithmetic-probe"></a>
## Summable errors require additional arithmetic information: a bounded probe

This ordinary strategy investigation concerns the full-sequence, every-coupling [F0012 contract](../tasks/Yin_T_F0012_v3.md#contract), not a new accepted least-value theorem or an independent review.
The selected next short test retains the actual random coefficients in the two-original-border construction above and asks what arithmetic information its geometric estimates omit.
The direct planar resampling idea below remains a secondary exploratory lead.
The [existing comparison boundary](../ledger/Yin_L_F0063_v1.md) and [scalar smoothing and exact-truncation diagnosis](../ledger/Yin_L_F0065_v1.md) continue to apply.

### The every-coupling quantifier and the precise summability requirement

Fix an allowed tuple of entry laws, a fixed polynomial, and the resulting marginal law of the input tuple at each size.
Let \(\mu_N\) be its empirical eigenvalue measure and \(\mu\) the deterministic proposed Brown limit.
For a fixed bounded continuous real test function \(f\) and a fixed \(\varepsilon>0\), put
\[
 p_N(f,\varepsilon)
 =\mathbb P\left\{
 \left|\int f\,d\mu_N-\int f\,d\mu\right|>\varepsilon
 \right\}.
 \tag{Arithmetic-probe-macro-error}
\]
If \(\mu_N\) converges weakly to \(\mu\) almost surely under every permitted coupling across sizes, then
\[
 \sum_{N=1}^{\infty}p_N(f,\varepsilon)<\infty
 \quad\hbox{for every such fixed }f,\varepsilon.
 \tag{Arithmetic-probe-necessary-summability}
\]
Indeed, sample the whole input tuple independently for different sizes, preserving all required independence and fixed marginal laws within each size.
This is one of the permitted couplings.
If the displayed sum diverged, the deviation events would be independent and the second Borel--Cantelli lemma would make them occur infinitely often almost surely, contradicting convergence for that fixed \(f\).
Conversely, summability for rational positive \(\varepsilon\) on a fixed countable convergence-determining class of bounded continuous functions gives simultaneous convergence on that class under every coupling by the first Borel--Cantelli lemma, hence weak convergence to the fixed probability measure \(\mu\).
No independence across sizes is needed for this converse.
The probability-one convergence set may depend on the chosen coupling, as in the Task contract.

This argument concerns macroscopic test-function deviations, not arbitrary sufficient events in a proof.
In particular, nonsummable probabilities of singularity or a very small least singular value at one fixed \(z\) do not by themselves disprove Brown convergence.
Such events need not cause the deviation in (Arithmetic-probe-macro-error), and a single point has zero planar area.
The [accepted planar-defect equivalence](../claims/Yin_C_F0186_v4.md#statement) still allows a direct integrated argument that succeeds without a summable pointwise least-value floor.
Nor does a nonsummable upper bound show that the corresponding true probability is nonsummable.

### A unit-energy quartic with vanishing loads and a nonsummable atom

Let \(m\) be even and let \(\varepsilon_{a,j}\), \(1\le a\le4\), \(1\le j\le m\), be \(4m\) independent Rademacher variables.
Define the multilinear homogeneous quartic
\[
 F_m=m^{-2}\prod_{a=1}^{4}\left(\sum_{j=1}^{m}\varepsilon_{a,j}\right)
 =m^{-2}\sum_{j_1,j_2,j_3,j_4=1}^{m}
       \varepsilon_{1,j_1}\varepsilon_{2,j_2}
       \varepsilon_{3,j_3}\varepsilon_{4,j_4}.
 \tag{Arithmetic-probe-quartic}
\]
There are exactly \(m^4\) distinct four-coordinate monomials, each with coefficient \(m^{-2}\), and no lower-degree terms.
Distinct monomials are orthogonal in the Rademacher product law, so the formal fourth-layer energy and variance are
\[
 \sigma_4^2=\sum_{|S|=4}c_S^2=m^4m^{-4}=1,
 \qquad \mathbb EF_m=0,
 \qquad \mathbb EF_m^2=1.
\]
A fixed coordinate \((a,j)\) belongs to exactly \(m^3\) monomials.
Its coefficient-square load is therefore
\[
 L_{a,j}=\sum_{S\ni(a,j)}c_S^2=m^3m^{-4}=m^{-1},
 \qquad \tau_4=\max_{a,j}L_{a,j}/\sigma_4^2=m^{-1}.
\]
The coefficient hypergraph at its common coefficient scale \(m^{-2}\) has matching number exactly \(m\).
The \(m\) edges \(\{(1,j),(2,j),(3,j),(4,j)\}\) are disjoint, and no matching can have more than \(m\) edges because every edge uses one of the \(m\) coordinates in the first group.
Equivalently, multiplying by \(m^2\) gives matching number \(m\) at coefficient threshold one, while the normalized load is unchanged.
Thus neither a mismatch of coefficient scales nor repeated-coordinate collisions explains the following atom.

For one group the probability of a zero sum is
\[
 q_m=2^{-m}\binom{m}{m/2}
     =\sqrt{\frac{2}{\pi m}}\bigl(1+O(m^{-1})\bigr).
\]
Independence of the four groups and the product formula give the exact identity and asymptotic
\[
 \mathbb P(F_m=0)
 =1-(1-q_m)^4
 =4\sqrt{\frac{2}{\pi m}}+O(m^{-1}).
 \tag{Arithmetic-probe-atom}
\]
Consequently, for every nonnegative sequence \(h_m\), including arbitrarily small positive polynomial or exponential windows,
\[
 \mathbb P\{|F_m|\le h_m\}\ge\mathbb P(F_m=0)
 \asymp m^{-1/2}
\]
on the even sizes, whose sum diverges.
Writing the total number of independent coordinates as \(n=4m\) gives the same nonsummability on \(n\in8\mathbb N\).
This disproves a generic shortcut from unit formal quartic energy, vanishing maximum load and growing matching alone to summable pointwise small-ball errors.
It does not show that the actual Wigner cofactor polynomial has this distribution, refute a matrix least-value estimate using additional information, or establish a Brown-measure counterexample.
Even for a matrix realization, a separate argument would be needed to connect a pointwise atom to a macroscopic planar test-function deviation.

### Primary-source mechanism and actual inspection boundary

The bounded search on 2026-11-06 used terms concerning symmetric least singular values, quadratic small-ball estimates, normalized Schur complements and Wigner-polynomial Brown convergence.
The relevant primary source is Marcelo Campos, Matthew Jenssen, Marcus Michelen and Julian Sahasrabudhe, [The least singular value of a random symmetric matrix, arXiv:2203.06141v3, 23 October 2023](https://arxiv.org/abs/2203.06141v3).
Its [accessible original PDF](https://arxiv.org/pdf/2203.06141) identifies itself as v3 on its first page; the version-specific PDF URL failed at the access interface.
Theorem 1.1, PDF page 1, assumes independent identically distributed upper-triangular real entries with mean zero, variance one and a subgaussian law, and gives
\[
 \mathbb P\{s_{\min}(A_n)\le\varepsilon n^{-1/2}\}
 \le C\varepsilon+e^{-cn}.
\]
The inspected Theorems 1.4 and 1.5, PDF pages 6--7, exhibit arithmetic least-common-denominator hypotheses in approximate negative-correlation estimates.
Selected proof-outline passages on PDF pages 9--12 and the normalized quadratic Schur passage on PDF page 38 explain the role of joint numerator/denominator control.
This was statement and mechanism inspection, not full proof or appendix review.
No existing bibliography entry was located in the scoped local search, and no new accepted source input is created here.
The source neither supplies the nonsymmetric product-inverse shift nor removes the subgaussian hypothesis.

The proposed new information is arithmetic nonstructure of coefficients generated by the actual random minor, together with joint control of a small Schur numerator and its random graph normalization.
It is not another Euclidean energy or load estimate.
The source mechanism is a reason to test that distinction, not a theorem that already applies to the present quartic.
The search stopped at this applicability boundary rather than claiming absence of other suitable sources.

### First discriminating question on the actual two original borders

Start with the original three-factor product \(W_1W_2W_3-zI\), fixed \(z\in\mathbb C\setminus\mathbb R\), and fixed bounded real atomic entry laws, for example Rademacher off-diagonal laws.
This pilot lies within the original finite-second-moment permission and does not address all its laws.
Use the actual [two-border exposure](#fresh-two-border-rewrite) and [denominator-free quartic cofactor matrix](#fresh-quartic-cofactors), conditioning only on \(A_0,B_0,C_0\) and the independent diagonal entries \(b,c\).
The original vectors \(x,y\) retain their independent normalized coordinate laws, and
\[
 \mathcal A(x,y)=s_Bs_C\operatorname{adj}D_i,
 \qquad \mathcal Q(x,y)=\operatorname{sym}\mathcal A(x,y),
 \qquad
 \frac{|(\operatorname{sym}\operatorname{adj}D_i)_{jk}|}
      {\|\operatorname{adj}D_i\|_F}
 =\frac{|\mathcal Q_{jk}(x,y)|}{\|\mathcal A(x,y)\|_F}
\]
on the stated full-factor invertibility guards and nonzero-adjugate branch.
Those full-factor guards depend on \(x,y\) and remain events, not extra conditioning that silently preserves iid borders.
The denominator-free formulas remain the starting point on singular shifted backgrounds; no inverse bound for \(D_0\) is assumed.

The first short question is whether an independence-preserving decoupling of these actual degree-at-most-four entries yields many linear coefficient directions with no forced common low-complexity lattice structure, or whether the product-inverse identities force a collapse analogous to (Arithmetic-probe-quartic).
For the Rademacher pilot, reduce repeated sign powers before reading off formal multilinear coefficients.
Retain the original random background and fresh-border dependence when testing the resulting directions; an arbitrary deterministic background is not the intended claim.
A large matching or the existing uniform coefficient-bulk bound alone does not answer this arithmetic question.
A concrete forced collapse would reject this proposed transfer of the source mechanism, while absence of that collapse would only justify pursuing an actual probabilistic arithmetic estimate.
No such decoupling estimate, arithmetic count or summable exceptional-probability bound has been proved here.

The first unsupported bridge is a quantitative arithmetic nonstructure statement for these actual random directions, with a sufficiently small exceptional probability and a normalization compatible with the Schur numerator and graph denominator.
The earlier relative-normalization and covered-slope problems above remain visible; they are not removed by naming this bridge.
Passing the pilot would still leave the general finite-second-moment law, general matrix coefficients and planar or almost-everywhere parameter assembly to be proved.
In particular, exact-law truncation or rank-small replacement does not turn the cited subgaussian theorem into a finite-variance input.

### Secondary planar resampling lead

For a real \(f\in C_c^2(\mathbb C)\), the empirical statistic has the distributional representation
\[
 X_N(f)=\frac{1}{2\pi N}\int_{\mathbb C}
       \Delta f(z)\log|\det(P(W)-zI)|\,d^2z.
\]
Resampling one independent original upper-triangular row block, with its symmetric reflected entries, changes each fixed noncommutative polynomial by a rank bounded in terms of that polynomial.
Writing the output change as \(UV^*\), the determinant identity expresses the change of \(X_N(f)\) through the planar integral of
\[
 \log\left|\det\left(I+V^*(P(W)-zI)^{-1}U\right)\right|
\]
away from finitely many eigenvalues, with the locally integrable logarithmic interpretation across them.
The possible gain is cancellation in the \(\Delta f\)-weighted integral and the original fresh-row randomness, before replacing that integral by a worst-case resolvent norm.
The missing input is a sufficiently strong conditional influence or martingale-tail estimate to make macroscopic deviations summable.
Fixed rank alone supplies no spectral stability for nonnormal matrices.
This differs from the [old Gaussian-refresh route](../strategies/Yin_S_F0029.md): it seeks concentration under the unchanged original product law, without claiming a condition-number bound or removal of output noise.
No such influence estimate has been established here, so this remains a backup lead rather than the selected next arithmetic test.

The following ordinary strategy calculation makes one sufficient influence target explicit for the actual three-real-factor product.
It uses the accepted [BBLM05 fourth-moment replacement inequality](../audits/literature/BBLM05/Yin_U001.md#fourth-moment-resampling-bound), whose source statement and direct specialization were inspected without a review of the original proof.
For one of the \(3N\) independent upper-triangular input row blocks, let \(W^{(k)}\) replace exactly that block by an independent copy with its original law, including the required symmetric reflection.
Put
\[
 I_{k,N}(f):=X_N(f;W)-X_N(f;W^{(k)}).
\]
The statistic is real and bounded by \(\|f\|_\infty\), so the source's fourth-moment hypothesis holds even when the matrix entries have no fourth moment.
The source interface gives
\[
 \mathbb E|X_N(f)-\mathbb EX_N(f)|^4
 \le \frac{2304}{49}(3N)
             \sum_{k=1}^{3N}\mathbb E|I_{k,N}(f)|^4.
\]
Thus an actual original-law estimate
\[
 \sum_{k=1}^{3N}\mathbb E|I_{k,N}(f)|^4
       \le C_fN^{-2-\varepsilon_f},\qquad \varepsilon_f>0,
 \tag{Planar-fourth-influence-target}
\]
would give summable fixed-deviation probabilities by fourth-moment Markov, and almost-sure concentration under every cross-size coupling by first Borel--Cantelli.
This is an averaged unconditional target; no uniform conditional Lipschitz estimate is assumed.
It remains unproved for the actual Wigner product.

For this specific product, identification of the limiting means is already available as a short deduction from the [C186v10 fixed-parameter probability logarithms](../claims/Yin_C_F0186_v10.md#statement) and the [C186v4 expected planar square-integrability](../claims/Yin_C_F0186_v4.md#noncompact-planar).
For every compact disk K, pointwise-in-z probability convergence gives convergence in measure on probability space times K, by dominated convergence applied to the deviation probabilities.
The uniform bound \(\sup_N\mathbb E\|u_N\|_{L^2(K)}^2<\infty\) gives uniform integrability there; the deterministic free potential is also in local \(L^2\), by the same scalar logarithmic-kernel bound and compact support of its Brown measure.
Truncation at a fixed value followed by Cauchy--Schwarz on the tails therefore gives
\[
 \mathbb E\int_K|u_N(z)-u(z)|\,d^2z\longrightarrow0.
\]
The distributional Laplacian formula then yields \(\mathbb EX_N(f)\to\int f\,d\mu_{s_1s_2s_3}^{\mathrm{Br}}\).
This argument integrates the locally integrable potentials in z; it does not claim finite expectations of unregularized logarithms at every atomic parameter.
A version of (Planar-fourth-influence-target) for a countable convergence-determining smooth test family, together with the existing pathwise tightness, would consequently give the Brown conclusion for this product.
One fixed test or the bounded Rademacher pilot alone would not supply the full finite-variance or general-polynomial contract.

The proposed diagnostic is one fixed nonharmonic smooth radial test for the original Rademacher three-factor model, retaining the signed planar integral of the double-sample log determinant ratio.
Replacing a single original row block changes this product by rank at most two, and the common background normalization cancels in that ratio.
The [nilpotent and cyclic-shift example](../ledger/Yin_L_F0061_v2.md#brown-nonimplication) still gives an order-one change for a suitable such smooth test despite a rank-one perturbation and bounded norms.
Thus fixed rank, planar integration and smoothness alone do not prove the influence estimate; the actual random background must supply further information.
Taking a pointwise absolute value or a worst-case resolvent bound before integration would discard the proposed cancellation.


<a id="actual-cofactor-copy-difference"></a>
## An actual cofactor has an explicit two-copy bilinear coefficient matrix

This continues the [selected arithmetic probe](#summable-arithmetic-probe) by calculating a genuine entry of the augmented cofactor matrix, rather than a generic quartic.
It is ordinary proof development, with no new small-ball theorem or independent-review claim.
All transposes below are ordinary transposes, including for complex matrices; no conjugation enters these polynomial identities.

### Exact Schur formula for one cofactor

Use the original real-input [two-border exposure](#fresh-two-border-rewrite), with \(m=N-1\ge2\), \(E=B_0^{-1}\), \(G=C_0^{-1}\), and \(D_0=A_0-zGE\).
Condition only on these principal background blocks and the diagonal values \(b,c\), and assume \(E,G\) exist.
The parameter may be any fixed \(z\ne0\); in the intended probe it is fixed and nonreal.
For an index \(a\), let \(J_a:\mathbb C^m\to\mathbb C^{m-1}\) delete coordinate \(a\), retaining the other coordinates in increasing order.
Fix cofactor indices \(j,k\), and for the next formulas assume that
\[
 T=J_kD_0J_j^T
\]
is invertible.
This is an additional branch condition, not a consequence asserted from \(z\notin\mathbb R\).
No bound on \(\|T^{-1}\|\), or on an original input's operator norm, is assumed.
Put
\[
 Z=J_j^TT^{-1}J_k,
 \qquad \delta=(-1)^{j+k}\det T,
 \qquad R=zEZG,
\]
\[
 P=(I+R)E,
 \qquad Q=G(I+R),
 \qquad L=EG+ER^TG.
 \tag{Cofactor-probe-matrices}
\]
Here \(R\) is local notation for this coefficient matrix, not the two-by-two update matrix in (Fresh-rank-two).

Deleting top-block row \(k\) and column \(j\) in the augmented matrix \(\mathcal K\) gives top-left block \(T\).
Its two-by-two Schur complement is
\[
 \begin{pmatrix}
 b-x^TPx&-x^TRy\\
 -1-x^TLy&c-y^TQy
 \end{pmatrix}.
\]
For example, its lower-left correction is
\[
 -1-v^Tu-zv^TEZG u
 =-1-x^T(EG+zEGZ^TEG)y,
\]
where \(u=Ex\), \(v=Gy\), and \(ER^TG=zEGZ^TEG\).
The other three entries follow by the same block multiplication.
Taking the two-by-two determinant yields the actual entry
\[
 \mathcal A_{jk}(x,y)
 =\delta\left[(b-x^TPx)(c-y^TQy)
                -(x^TRy)(1+x^TLy)\right].
 \tag{Cofactor-probe-Schur}
\]
This augmented-cofactor identity holds for every \(x,y\) on the fixed \(T\)-invertible background branch.
Its identification with \(s_Bs_C(\operatorname{adj}D_i)_{jk}\) retains the earlier full-factor invertibility guards as events; those guards are not additional conditioning on the fresh borders.

### Complete multilinearization on the original Rademacher borders

Now take the second and third off-diagonal laws to be Rademacher, so that \(x=\varepsilon/\sqrt N\) and \(y=\eta/\sqrt N\), with independent fair sign vectors \(\varepsilon,\eta\).
Set \(P_s=(P+P^T)/2\) and \(Q_s=(Q+Q^T)/2\).
The sign polynomial \(\widehat f=\mathcal A_{jk}/\delta\) has only constant, pure quadratic, mixed bilinear and mixed quartic Walsh terms.
Writing \(a<b\) and \(c<d\) within their respective sign groups, its complete coefficient list is
\[
 \begin{aligned}
 c_{\varnothing}
 &=bc-\frac{c\operatorname{tr}P_s+b\operatorname{tr}Q_s}{N}
   +\frac{\operatorname{tr}P_s\operatorname{tr}Q_s
                  -\operatorname{tr}(RL^T)}{N^2},\\
 c_{\varepsilon_a\varepsilon_b}
 &=-\frac{2c(P_s)_{ab}}{N}
   +\frac{2(P_s)_{ab}\operatorname{tr}Q_s
                  -(RL^T+LR^T)_{ab}}{N^2},\\
 c_{\eta_c\eta_d}
 &=-\frac{2b(Q_s)_{cd}}{N}
   +\frac{2(Q_s)_{cd}\operatorname{tr}P_s
                  -(R^TL+L^TR)_{cd}}{N^2},\\
 c_{\varepsilon_a\eta_c}&=-\frac{R_{ac}}{N},\\
 c_{\varepsilon_a\varepsilon_b\eta_c\eta_d}
 &=\frac{1}{N^2}\left[
     4(P_s)_{ab}(Q_s)_{cd}
     -R_{ac}L_{bd}-R_{ad}L_{bc}
     -R_{bc}L_{ad}-R_{bd}L_{ac}\right].
 \end{aligned}
 \tag{Cofactor-probe-Walsh}
\]
All coefficients not listed are zero, and the coefficients of \(\mathcal A_{jk}\) are \(\delta\) times the displayed ones.
To verify the list, expand \(x^TP_sx\) as \(N^{-1}(\operatorname{tr}P_s+2\sum_{a<b}(P_s)_{ab}\varepsilon_a\varepsilon_b)\), do the same for \(y^TQ_sy\), and reduce the product \((x^TRy)(x^TLy)\) using \(\varepsilon_a^2=\eta_c^2=1\).
In the last product, equal indices in both groups give \(\operatorname{tr}(RL^T)\), equal indices in one group give the displayed pure quadratic corrections, and unequal indices in both groups give its four quartic contributions.
In particular, reducing a quartic square never produces a term odd in each sign group.

The odd-in-\(x\), odd-in-\(y\) projection therefore has the especially simple exact form
\[
 \frac{\mathcal A_{jk}(x,y)-\mathcal A_{jk}(-x,y)
       -\mathcal A_{jk}(x,-y)+\mathcal A_{jk}(-x,-y)}{4}
 =-\delta x^TRy.
 \tag{Cofactor-probe-odd-odd}
\]
Since \(Z\) has rank \(m-1\), this mixed-bilinear coefficient matrix has rank \(m-1\) when \(T,E,G\) are invertible and \(z\ne0\).
This is a statement about one cofactor, not about a selected homogeneous fourth layer or the symmetrized matching matrix.
The global sign-flip identity alone is not a small-ball probability estimate.

For this odd-odd layer only, the inverse can be removed:
\[
 \delta R
 =(-1)^{j+k}zEJ_j^T\operatorname{adj}(T)J_kG.
 \tag{Cofactor-probe-odd-odd-adjugate}
\]
Direct cofactor expansion gives (Cofactor-probe-odd-odd) with the right-hand side of (Cofactor-probe-odd-odd-adjugate) even when \(T\) is singular.
Equivalently, this layer identity is polynomial in the entries of \(T\) and agrees with that cofactor expansion on invertible \(T\).
Its rank conclusion does not extend unchanged to singular \(T\).
The formulas below involving products of \(R\) and \(L\) remain on the \(T\)-invertible branch: this single adjugate identity does not justify uncancelled expressions such as \(\delta RR\) at singular \(T\).

### Independent-copy difference and its conditional coefficient directions

Let \(x',y'\) be independent copies of the original normalized Rademacher borders, independent of \(x,y\) and of one another.
Set
\[
 s=x+x',\quad d=x-x',\qquad
 t=y+y',\quad e=y-y',
\]
and take the rectangular difference
\[
 \Delta\mathcal A_{jk}
 =\mathcal A_{jk}(x,y)-\mathcal A_{jk}(x',y)
  -\mathcal A_{jk}(x,y')+\mathcal A_{jk}(x',y').
\]
The pure \(x\), pure \(y\) and constant terms cancel.
For the product of quadratic forms,
\[
 (x^TP_sx-x'^TP_sx')(y^TQ_sy-y'^TQ_sy')
 =(d^TP_s s)(t^TQ_se).
\]
For \(h(x,y)=(x^TRy)(x^TLy)\), expanding \(x=(s+d)/2\), \(y=(t+e)/2\) gives
\[
 \begin{aligned}
 \Delta h=\frac14\bigl[
 &(s^TRt)(d^TLe)+(s^TRe)(d^TLt)\\
 &+(d^TRt)(s^TLe)+(d^TRe)(s^TLt)
 \bigr].
 \end{aligned}
\]
The mixed-bilinear term contributes \(-d^TRe\).
Consequently
\[
 \Delta\mathcal A_{jk}=\delta d^TM(s,t)e,
 \tag{Cofactor-probe-copy-difference}
\]
where
\[
 \begin{aligned}
 M(s,t)={}&-\left(1+\frac{s^TLt}{4}\right)R
            -\frac{s^TRt}{4}L
            +(P_s s)(Q_s t)^T\\
          &-\frac14(Rt)(s^TL)
            -\frac14(Lt)(s^TR).
 \end{aligned}
 \tag{Cofactor-probe-copy-matrix}
\]
Thus the exact coefficient matrix is a two-parameter pencil in the actual background matrices \(R,L\), plus three displayed rank-one matrices.
The scalar coefficients and those rank-one matrices depend on the common sums \(s,t\), not on the remaining difference signs after those sums have been conditioned on.

Define the random support sets
\[
 I=\{a:s_a=0\},\qquad J=\{c:t_c=0\}.
\]
For each coordinate, \(s_a\) takes values \(0,2/\sqrt N,-2/\sqrt N\) with probabilities \(1/2,1/4,1/4\).
Conditionally on \(s_a=0\), the difference \(d_a\) is an independent fair sign times \(2/\sqrt N\); when \(s_a\ne0\), it is zero.
The corresponding assertions hold for \(t_c,e_c\), independently across coordinates and between the two borders.
Hence, conditional on the full vectors \(s,t\),
\[
 d_I=\frac{2}{\sqrt N}\xi,
 \qquad e_J=\frac{2}{\sqrt N}\zeta,
 \qquad d_{I^c}=e_{J^c}=0,
\]
where \(\xi\in\{-1,1\}^I\), \(\zeta\in\{-1,1\}^J\) are independent fair sign vectors.
It follows that
\[
 \Delta\mathcal A_{jk}
 =\frac{4\delta}{N}\xi^TM_{I,J}(s,t)\zeta.
 \tag{Cofactor-probe-conditional-bilinear}
\]
After further conditioning on \(\zeta\), the actual remaining linear coefficient vector, before its common factor \(4\delta/N\), is
\[
 v(s,t,\zeta)=M_{I,J}(s,t)\zeta\in\mathbb C^I.
 \tag{Cofactor-probe-arithmetic-vector}
\]
This identifies the concrete vector whose real and imaginary coefficient directions would enter an arithmetic small-ball analysis; it is not an assertion that its least common denominator is large.
The support cardinalities are independent \(\operatorname{Bin}(m,1/2)\) variables, but large supports alone imply neither rank nor arithmetic regularity of the restricted coefficient matrix.

For completeness, this copy calculation also gives a precise conditional concentration reduction for fixed absolute windows.
For a fixed center \(u_0\in\mathbb C\) and \(h\ge0\), let
\[
 q=\mathbb P\{|\mathcal A_{jk}(x,y)-u_0|\le h
                  \mid A_0,B_0,C_0,b,c\}.
\]
Two applications of Cauchy--Schwarz show that \(q^4\) is at most the probability that all four corners \((x,y),(x',y),(x,y'),(x',y')\) belong to this same event.
On that intersection \(|\Delta\mathcal A_{jk}|\le4h\), so
\[
 q^4\le
 \mathbb E_{s,t}\,
 \mathbb P_{\xi,\zeta}\left\{
  |\xi^TM_{I,J}(s,t)\zeta|\le\frac{Nh}{|\delta|}
  \ \middle|\ s,t
 \right\}.
 \tag{Cofactor-probe-concentration-reduction}
\]
The background branch is fixed throughout this inequality, and \(\delta\ne0\) there.
This does not replace the random normalization \(\|\mathcal A(x,y)\|_F\) in (Fresh-graph) by a deterministic window, nor bound \(1/|\delta|\).
Such normalization and arithmetic estimates remain separate requirements for a least-value application.

### What is and is not forced to collapse

On the particular copy event \(s=t=0\), one has \(I=J=\{1,\ldots,m\}\), all three rank-one corrections vanish, and
\[
 M(0,0)=-R.
\]
Under the already stated invertibility and \(z\ne0\) hypotheses its rank is \(m-1\), and the vectors \(-R\zeta\), as \(\zeta\) ranges over all signs, span its \((m-1)\)-dimensional range.
This rules out a universal algebraic assertion that every copy realization of this single-cofactor construction forces all the remaining coefficient directions into a fixed-dimensional space.
However,
\[
 \mathbb P(s=t=0)=2^{-2m},
\]
so this check says nothing about typical copies, a quantitative lower bound on a restricted matrix, or a large arithmetic denominator.
It neither removes the nonsummable-error obstruction nor supplies a Brown convergence argument.

Finally, the actual graph uses \(\mathcal Q_{jk}=(\mathcal A_{jk}+\mathcal A_{kj})/2\), not a single off-diagonal cofactor.
If both corresponding background submatrices are invertible, use subscripts \((j,k)\) and \((k,j)\) for the matrices and scalars constructed above, with the same copies and common sums.
Its exact difference is
\[
 \Delta\mathcal Q_{jk}
 =d^T\left[\frac{\delta_{jk}M_{jk}(s,t)
                   +\delta_{kj}M_{kj}(s,t)}2\right]e.
 \tag{Cofactor-probe-symmetrization}
\]
Its odd-odd layer similarly involves \((\delta_{jk}R_{jk}+\delta_{kj}R_{kj})/2\).
These two contributions may cancel, so the rank \(m-1\) calculation for one cofactor is not a symmetrized matching bound.
The explicit half-sum in (Cofactor-probe-symmetrization), together with its random normalization, is the corresponding arithmetic object for that graph.
No typical-rank, arithmetic small-ball, singular-background quartic extension, or summable probability estimate for that half-sum is claimed here.


<a id="symmetrized-odd-odd-rank"></a>
## Exact rank of the symmetrized odd-odd coefficient and an allowed rare background

This ordinary continuation of the [actual cofactor calculation](#actual-cofactor-copy-difference) determines precisely how its mixed-bilinear coefficient behaves under symmetrization.
It supplies no typicality, normalized small-ball or Brown convergence theorem.
All transposes and ranks in the identities below are over the complex matrices with ordinary transpose.

### The actual symmetrized coefficient without separate cofactor-invertibility guards

Retain \(E=B_0^{-1}\), \(G=C_0^{-1}\), \(D_0=A_0-zGE\), and assume that \(D_0\) is invertible and \(z\ne0\).
Write
\[
 R_0=D_0^{-1},\qquad d_0=\det D_0,\qquad S_0=(R_0+R_0^T)/2.
\]
Fix \(j\ne k\), and put
\[
 a=(S_0)_{jk},\qquad H_{jk}=e_je_k^T+e_ke_j^T.
\]
The symbol \(R_0\) denotes the full background inverse, whereas \(R_{jk}\) in the preceding section denotes the coefficient matrix associated with a deleted cofactor.
The present calculation does not require either \(T_{jk}=J_kD_0J_j^T\) or \(T_{kj}=J_jD_0J_k^T\) to be invertible.

Define the matrix
\[
 \Omega_{jk}=(-1)^{j+k}J_j^T\operatorname{adj}(T_{jk})J_k.
\]
When \(T_{jk}\) is invertible it equals \(\delta_{jk}Z_{jk}\), and its adjugate definition retains the [previous odd-odd layer identity](#actual-cofactor-copy-difference) when that deleted matrix is singular.
For an arbitrary matrix perturbation \(U\), direct differentiation of the deleted determinant gives
\[
 \left.\frac{d}{dt}(\operatorname{adj}(D_0+tU))_{jk}\right|_{t=0}
 =\operatorname{tr}(\Omega_{jk}U).
\]
On the full-inverse branch, differentiation of \(\operatorname{adj}D=\det(D)D^{-1}\) instead gives
\[
 \begin{aligned}
 \left.\frac{d}{dt}(\operatorname{adj}(D_0+tU))_{jk}\right|_{t=0}
 &=d_0\left[(R_0)_{jk}\operatorname{tr}(R_0U)
                         -(R_0UR_0)_{jk}\right]\\
 &=\operatorname{tr}\left(
 d_0[(R_0)_{jk}R_0-R_0e_ke_j^TR_0]U\right).
 \end{aligned}
\]
Equality for every \(U\) proves
\[
 \Omega_{jk}=d_0[(R_0)_{jk}R_0-R_0e_ke_j^TR_0].
 \tag{Sym-odd-gradient}
\]
Consequently the odd-in-\(x\), odd-in-\(y\) component of the actual entry \(\mathcal Q_{jk}=(\mathcal A_{jk}+\mathcal A_{kj})/2\) is
\[
 \Pi_{\rm oo}\mathcal Q_{jk}(x,y)=-x^T\mathscr B_{jk}y,
\]
\[
 \begin{aligned}
 \mathscr B_{jk}
 &=\frac z2E(\Omega_{jk}+\Omega_{kj})G\\
 &=zd_0E\left[aR_0-\frac12R_0H_{jk}R_0\right]G.
 \end{aligned}
 \tag{Sym-odd-coefficient}
\]
Here \(\Pi_{\rm oo}f=[f(x,y)-f(-x,y)-f(x,-y)+f(-x,-y)]/4\), so this is an identity of the underlying polynomials, independent of a sign-law interpretation.
On normalized Rademacher borders its mixed-bilinear Walsh coefficient matrix is \(-\mathscr B_{jk}/N\).
The full inverse \(D_0^{-1}\) is still an explicit hypothesis; no singular-\(D_0\) rank classification is asserted.

### Complete rank classification for this layer

Since \(z,d_0,E,G,R_0\) are invertible scalar or matrix factors where appropriate,
\[
 \operatorname{rank}\mathscr B_{jk}
 =\operatorname{rank}\left(aI-\frac12H_{jk}R_0\right).
\]
If \(a=0\), the right-hand matrix has rank exactly two because \(j\ne k\), \(\operatorname{rank}H_{jk}=2\), and \(R_0\) is invertible.

Suppose now that \(a\ne0\).
Let \(U_2=(e_j,e_k)\), let \(J_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), and put
\[
 B_2=U_2^TR_0U_2
 =\begin{pmatrix}(R_0)_{jj}&(R_0)_{jk}\\
                  (R_0)_{kj}&(R_0)_{kk}\end{pmatrix}.
\]
Any vector in the kernel of \(K_a=aI-H_{jk}R_0/2\) belongs to \(\operatorname{range}U_2\), since its image under \(aI\) belongs to that range.
Writing the vector as \(U_2w\), its kernel equation becomes
\[
 \left(aI_2-\frac12J_2B_2\right)w=0.
\]
The trace of this unnormalized two-by-two matrix is \(a\), not one, because \(\operatorname{tr}(J_2B_2)=2a\).
Define
\[
 \Delta_{jk}=(R_0)_{jj}(R_0)_{kk}-(R_0)_{jk}(R_0)_{kj}.
\]
Its determinant is \(-\Delta_{jk}/4\).
Thus it is invertible if \(\Delta_{jk}\ne0\); if \(\Delta_{jk}=0\), its nonzero trace makes its kernel exactly one-dimensional.
Equivalently, \(\det K_a=-a^{m-2}\Delta_{jk}/4\).
This proves the exact classification
\[
 \operatorname{rank}\mathscr B_{jk}
 =\begin{cases}
 2,&a=0,\\
 m,&a\ne0\text{ and }\Delta_{jk}\ne0,\\
 m-1,&a\ne0\text{ and }\Delta_{jk}=0.
 \end{cases}
 \tag{Sym-odd-rank}
\]
In particular the whole odd-odd coefficient matrix does not vanish on this full-inverse branch, although its high-rank contributions can cancel down to rank two.

The quantitative issue is already visible in
\[
 \mathscr B_{jk}
 =zd_0a\,ER_0G
   -\frac{zd_0}{2}ER_0H_{jk}R_0G,
 \qquad
 d_0a=(\operatorname{sym}\operatorname{adj}D_0)_{jk}.
\]
The second term has rank at most two, while the scale multiplying the first term is exactly a background symmetrized cofactor edge.
Neither a nonzero edge nor the rank classification bounds that edge relative to \(\|\mathcal A(x,y)\|_F\), controls singular values of the coefficient matrix, or proves arithmetic nonstructure.
When that background edge is zero, the entire high-rank term disappears.
A rank-two remainder can itself have useful arithmetic properties, but none follows from its rank alone.

### A genuine fixed-law background with the high-rank cancellation

Take even \(m\ge4\), set \(N=m+1\), and use the same fixed raw law for every independent upper-triangular entry, including the diagonals, of each of the three real inputs:
\[
 \mathbb P(\xi=0)=\frac12,
 \qquad \mathbb P(\xi=\sqrt2)=\mathbb P(\xi=-\sqrt2)=\frac14.
\]
It is centered, has variance one and is bounded, so it satisfies the original finite-second-moment permission.
The matrices are normalized by the original \(N^{-1/2}\), not by \(m^{-1/2}\).
Put \(s=\sqrt{2/N}\) and define real symmetric matrices
\[
 H=\operatorname{diag}(1,-1,1,-1,\ldots),
 \qquad
 K=\operatorname{diag}\left(
 \begin{pmatrix}0&1\\1&0\end{pmatrix},\ldots,
 \begin{pmatrix}0&1\\1&0\end{pmatrix}\right).
\]
They satisfy \(H^2=K^2=I\) and \(HK=-KH\).
Consider the background event
\[
 A_0=0,\qquad B_0=sH,\qquad C_0=sK.
 \tag{Sym-odd-allowed-background}
\]
Every specified entry lies in the support of the corresponding original normalized law.
In particular \(\|B_0\|=\|C_0\|=s\), and every nonzero entry of these backgrounds has magnitude \(s\).
The fresh borders and omitted diagonal entries retain their original independent laws after this background event is fixed.
Full invertible second and third factors also have positive-probability completions, for example \(x=y=0\) and \(b=c=s\).

On this background,
\[
 E=s^{-1}H,\qquad G=s^{-1}K,
 \qquad D_0=-zs^{-2}KH,
 \qquad R_0=\frac{s^2}{z}KH.
\]
The matrix \(KH\) is real skew-symmetric, squares to \(-I\), and is invertible.
Thus the displayed identities hold for every nonzero \(z\), including the intended fixed nonreal parameter, and \(S_0=0\).
For a paired choice \(j=2r-1\), \(k=2r\), both \((R_0)_{jk}\) and \((R_0)_{kj}\) are nonzero.
Since \((\operatorname{adj}D_0)_{jk}=d_0(R_0)_{jk}\), both deleted matrices \(T_{jk},T_{kj}\) are invertible.
Each individual cofactor coefficient matrix from the preceding section therefore has rank \(m-1\), while their symmetrized coefficient has rank two by (Sym-odd-rank).
The restriction \(m\ge4\) makes this an actual decrease in rank; at \(m=2\) the individual rank would be one.

The remaining matrix is especially explicit.
Here
\[
 ER_0=-\frac{s}{z}K,
 \qquad R_0G=-\frac{s}{z}H,
\]
so for the paired indices
\[
 \mathscr B_{jk}
 =-\frac{d_0s^2}{2z}KH_{jk}H
 =-\frac{d_0s^2}{2z}(e_je_j^T-e_ke_k^T).
 \tag{Sym-odd-paired-coefficient}
\]
Accordingly
\[
 \Pi_{\rm oo}\mathcal Q_{jk}(x,y)
 =\frac{d_0s^2}{2z}(x_jy_j-x_ky_k).
\]
Only these two physical coordinates enter this particular odd-odd layer.
This does not say that the full \(\mathcal Q_{jk}\), its other Walsh layers, or the complete rectangular copy difference has the same two-coordinate support.
The background law contains a zero atom, so this example is not asserted to be a pure Rademacher background.

The probability and limitation of the example can be checked exactly.
For the \(m\)-dimensional principal blocks, the prescribed first block contributes probability \(2^{-m(m+1)/2}\).
The second block contributes \(2^{-2m-m(m-1)/2}\), from its \(m\) prescribed nonzero diagonals and zero off-diagonal entries.
The third contributes \(2^{-m-m-[m(m-1)/2-m/2]}\), from zero diagonals, \(m/2\) prescribed positive off-diagonal pairs and the remaining zero off-diagonal entries.
Independence of the three inputs gives total probability
\[
 2^{-(3m^2/2+3m)}.
\]
These probabilities are summable in \(m\).
The witness is therefore an allowed rare background defeating a deterministic inheritance of high rank from each individual cofactor to the symmetrized layer, even on the stated invertibility branch.
It does not establish typical cancellation, nonsummable errors, failure of a probabilistic matching estimate, or a counterexample to Brown convergence.
The remaining probabilistic work must control the actual background edge and the rank-two remainder, together with the graph normalization and the other sign layers, rather than invoke single-cofactor rank alone.


<a id="normalized-sym-odd-odd-energy"></a>
## Using normalized aggregate energy in the remaining arithmetic probe

The complete coefficient theorem and all necessary algebra are fixed in [C_F0194_v15](../claims/Yin_C_F0194_v15.md#statement), whose [proved decision](../claims/Yin_C_F0194_v15.md#decision-normalized-odd-odd-energy-reviewed) adopts independent whole-proof review.
Its [probability guards](../claims/Yin_C_F0194_v15.md#probability-guards) cover every omitted index simultaneously with arbitrary polynomial failure rates, using only real finite-second-moment inputs at each fixed \(z\ne0\).
The formal energy comparison permits unbounded original laws and a corank-one background and retains the realized border-dependent cofactor denominator.
Only the Rademacher second and third borders have the stated Walsh-energy interpretation; general real laws retain a formal monomial-coefficient conclusion.
The fixed proof supplies the actual border identities, aggregate lower bound, rank-two update cancellation and singular extension, so no duplicate proof is needed here.

This theorem removes the possibility that the entire symmetrized odd-odd coefficient layer is superpolynomially small relative to the actual denominator on those guards.
The guards' summability does not establish summable small-ball or bad-graph probabilities.
The next discriminating test remains arithmetic nonstructure of the actual symmetrized rectangular difference on typical independent-copy supports, using the [explicit copy construction](#actual-cofactor-copy-difference) only within its stated invertibility scope.
It must control the complete coefficient directions, possible cancellation with the other layers, and the realized graph normalization; the rank of one unsymmetrized cofactor is insufficient.

Aggregate energy alone does not provide many disjoint large output edges, small coordinate load, or arithmetic regularity of the restricted copy matrix.
The [unit-energy quartic obstruction](#summable-arithmetic-probe) continues to exclude a generic summable small-ball inference from energy, load or matching alone.
No summable least-value floor, planar-defect estimate or Brown convergence conclusion is obtained from this coefficient theorem.

<a id="joint-cofactor-conditional-atom"></a>
## Joint output still needs a typical-background or joint-numerator estimate

The [fixed joint-cofactor obstruction](../ledger/Yin_L_F0066_v6.md#joint-cofactor-formula) gives an original three-point-law background on which every actual off-diagonal output shares one scalar factor, with a [conditional atom of order \(N^{-1/2}\)](../ledger/Yin_L_F0066_v6.md#conditional-atom).
Its [realized denominator and polynomial guards](../ledger/Yin_L_F0066_v6.md#normalization-and-guards) are nondegenerate, and the aggregate formal odd-odd energy divided by that denominator is at least \(N/8\) on the atom.
The complete rectangular difference retains explicit shared scalar couplings, so replacing one output by the entire vector does not yield a uniform conditional summable estimate from these guards alone.
The background itself has probability exponentially small in \(N^2\), and the example is not a pure-Rademacher or typical-background failure.
The unresolved next step is a quantitative exclusion of harmful actual backgrounds or joint control with the small determinant numerator, at the [precise retained scope](../ledger/Yin_L_F0066_v6.md#scope-and-next-obligation).

<a id="joint-small-numerator-probe"></a>
## The remaining quantitative target is high-matching concentration

The [fixed branch comparison](../ledger/Yin_L_F0066_v7.md#accepted-branch-comparison) confirms that C_F0194_v5 already controls the low-matching tiny-ratio intersection with arbitrary polynomial error after conditioning on the full second and third inputs.
Its remaining error is the high-matching term \(\psi(\lfloor\sqrt N\rfloor)\), not a missing bound for the low-matching intersection.
The [complete numerator calculation](../ledger/Yin_L_F0066_v7.md#common-factor-full-numerator) excludes the L_F0066_v6 common-factor atom from the actual tiny-ratio event for every real first border and diagonal.
The [conditional exponential estimate](../ledger/Yin_L_F0066_v7.md#rare-background-exponential-bound) strengthens that exclusion on its rare bounded-law background without resolving typical high-matching concentration.

For the continuing bounded atomic real pilot, fix \(z\in\mathbb C\setminus\mathbb R\), put \(B=W_2,C=W_3\), and use
\[
 M=W_1-zC^{-1}B^{-1},\qquad MBC=W_1BC-zI_N.
\]
For a fixed requested \(B_*>1\), retain the \(B,C\)-measurable inverse guard \(\Lambda_N\) and the fixed exponents \(L,K,H\) selected in the cited branch comparison.
They satisfy
\[
 \mathbb P(\Lambda_N^c)\le CN^{-B_*},\qquad
 \|B^{-1}\|,\|C^{-1}\|\le N^L,
\]
with the norm guard \(\|M\|\le N^K\) failing with the same arbitrarily small polynomial order after the stated margins.
Let
\[
 D_i=M_{\widehat i,\widehat i},\qquad
 T_i=\operatorname{adj}D_i,\qquad
 Q_i=(T_i+T_i^T)/2.
\]
Only on \(T_i\ne0\), define \(R_i=|\det M|/\|T_i\|_F\).
Let \(\mathcal H_i(h,r)\) be the event that \(T_i\ne0\) and the graph with edges \(|(Q_i)_{jk}|\ge h\|T_i\|_F\), \(j\ne k\), has a matching of at least \(r\) edges.
The many-index threshold for \(s_{\min}(M)\le N^{-A}\) is \(R_i\le C_1N^{2K+1-A}\).
These interfaces keep the actual polynomial inverse-product shift and do not condition on the remaining first border.

### The next discriminating proposition must address high matching

The unresolved probability input is the arithmetic concentration of the actual full first-row polynomial on the high-matching branch.
To state it without hiding independence or lower-degree terms, condition on
\[
 \mathcal F_i=\sigma\!\left((W_1)_{\widehat i,\widehat i},
                  (W_1)_{ii},B,C\right).
\]
The first off-diagonal border remains \(\xi/\sqrt N\) with independent coordinates of the original first-input law.
Write its shifted row and column as \(\xi/\sqrt N+f_i\) and \(\xi/\sqrt N+g_i\), its shifted diagonal as \(\mu_i\), and retain \(T_i,Q_i\) defined above.
On \(T_i\ne0\), the exact normalized numerator is
\[
 \begin{aligned}
 Z_i(\xi)={}&
 \frac{\mu_i\det D_i-f_i^TT_i g_i}{\|T_i\|_F}
 -\frac{(T_i g_i+T_i^Tf_i)^T\xi}
              {\sqrt N\,\|T_i\|_F}
 -\frac{\xi^TQ_i\xi}{N\|T_i\|_F}.
 \end{aligned}
 \tag{Joint-probe-actual-quadratic}
\]
Thus \(Z_i=\det M/\|T_i\|_F\), and all coefficients, the center, the graph and its normalization are \(\mathcal F_i\)-measurable.
Define
\[
 \kappa_i(\tau)=
 \mathbb P_\xi\{|Z_i(\xi)|\le\tau\mid\mathcal F_i\}.
\]
An explicit sufficient next proposition for the bounded atomic pilot is the following, presently unproved:
for some fixed requested \(B_*>1\), choose \(T>0\), after the low-branch graph and polynomial guard exponents, such that
\[
 \frac1N\sum_{i=1}^N
 \mathbb P\left\{\Lambda_N\cap\mathcal H_i(N^{-H},\lfloor\sqrt N\rfloor),
                  \ \kappa_i(N^{-T})>N^{-B_*}\right\}
 \le C N^{-B_*}.
 \tag{Joint-probe-high-concentration-target}
\]
This would bound the corresponding averaged high-matching tiny-ratio probability by \((C+1)N^{-B_*}\), by splitting at the displayed conditional probability threshold.
Choosing the full least-value exponent \(A>T+2K+2\) then places the many-index event inside this window, while the [fixed low-matching bound](../ledger/Yin_L_F0066_v7.md#accepted-branch-comparison) handles its complement in matching.
The resulting summability would improve the fixed-parameter pilot; the general input-law, arbitrary-polynomial and planar assembly obligations would remain separate.

The accepted matching estimate only bounds \(\kappa_i\) by its nonsummable \(\psi(r)\) scale on every high-matching background.
A matching hypothesis alone cannot give (Joint-probe-high-concentration-target): the quadratic
\((\sum_{j=1}^{p}\varepsilon_j)(\sum_{j=1}^{p}\eta_j)\), with two independent even-sized sign groups, has matching number \(p\) and a zero atom of order \(p^{-1/2}\).
That elementary generic example is not asserted to be an actual Wigner cofactor.
It identifies why the next gain must use the distribution and arithmetic structure of the actual random coefficients, or the special actual center and normalization, rather than only increase matching size or repeat an aggregate-energy argument.
The fixed rare-background estimate does not supply that typical high-matching input.
No new external arithmetic theorem is adopted here; the retained [primary-source mechanism and its inspection limits](#summable-arithmetic-probe) still do not prove (Joint-probe-high-concentration-target) for this product-inverse model.

<a id="nonreal-center-corank-one-obstruction"></a>
## A nonreal parameter does not uniformly exclude a complete-numerator atom

The [fixed corank-one high-matching construction](../ledger/Yin_L_F0066_v9.md#actual-high-matching-background) has linear-size matching and a complete normalized numerator with a conditional zero atom of order \(N^{-1}\).
The [fixed-law realization and background probability](../ledger/Yin_L_F0066_v9.md#fixed-laws-and-background-probability) use bounded atomic off-diagonal laws and unbounded diagonal laws with every finite moment, with \(e^{-CN^3}\le\mathbb P(\Gamma_N)\le e^{-cN^2}\).
This defeats a uniform nonreal-center exclusion over all finite-variance backgrounds, but does not refute the bounded-diagonal pilot, the averaged high-concentration target or Brown convergence.
The retained finding is ordinary exploration and self-checking, not independent proof review.
The [raw-rank and two-point-law distinction](../ledger/Yin_L_F0066_v9.md#invertible-minor-and-sign-boundary) also prevents raw irreducibility from being substituted for concentration after sign-power reduction.

The [fixed scope and continuation boundary](../ledger/Yin_L_F0066_v9.md#scope-and-continuation) retains the precise limitations of this construction.
The subsequent [accepted-input comparison](../ledger/Yin_L_F0066_v10.md#isolated-background-upper-tail) shows that the existing isolated-minor theorem already controls this part of (Joint-probe-high-concentration-target) through background-averaged probabilities; it gives no uniform conditional bound on every background.

<a id="near-corank-one-normalization-and-existing-control"></a>
## The isolated high-matching subbranch is already controlled

The [fixed near-corank-one calculation](../ledger/Yin_L_F0066_v10.md#exact-normalized-product) retains the true center and gives
\[
 Z=\omega a\{\mu t_1-\ell(x)h(x)\}+E,\qquad
 |E|\le a(t_1/t_2)\|x+f\|\,\|x+g\|.
\]
The two affine forms use the same original fresh row, so they are not conditionally independent.
The [fresh-row ball and error comparison](../ledger/Yin_L_F0066_v10.md#fresh-row-ball-and-error) preserves the original finite-variance law and the actual normalization.

More decisively, [C194v1 already controls the isolated high-matching background upper tail](../ledger/Yin_L_F0066_v10.md#isolated-background-upper-tail), using its original unrestricted-in-matching scope and a conditional-expectation/Markov argument.
No full-matrix norm condition is inserted into the conditional probability.
Together with the accepted second-smallest floor, this controls the target's high-concentration contribution from actual minors with \(t_1(D_i)\le N^{-J}\) for a sufficiently large fixed \(J\), with arbitrarily small polynomial errors.
The [remaining high-matching target](../ledger/Yin_L_F0066_v10.md#remaining-polynomially-invertible-minors) is therefore the complete-quadratic concentration problem on polynomially invertible actual minors.
That remaining concentration, the general complex-law and polynomial extensions, and F0012 itself are unresolved.
The separate [independent whole-scope review R200v17](../audits/reviews/Yin_R_F0200_v17.md#near-corank-normalization-scope) checks this branch comparison and its accepted-source applications, without claiming a bound on the remaining branch.

<a id="invertible-minor-full-numerator-atom"></a>
## A uniformly invertible actual minor still permits a nonsummable conditional atom

The complete actual-model construction and fixed-law realization are retained in [L66v11](../ledger/Yin_L_F0066_v11.md#invertible-minor-full-numerator-atom).
On its explicitly realized high-matching backgrounds at \(z=i\), the minor satisfies \(t_1(D)>1\) and \(\|D^{-1}\|<1\), but the actual normalized complete numerator has conditional zero atom \(b_n^2\asymp N^{-1}\).
For every fixed \(\Theta>5/2\), this is exactly \(\kappa_1(N^{-\Theta})\) for sufficiently large sizes.
The [normalization and graph calculation](../ledger/Yin_L_F0066_v11.md#complete-atom-and-matching) retains the nonzero center \(\mu\det D\) and explains its exact cancellation on the original Rademacher row, despite full raw quadratic rank.

The [single fixed-law realization](../ledger/Yin_L_F0066_v11.md#fixed-laws-and-background-probability) has bounded off-diagonal laws and an unbounded centered diagonal law with all finite moments.
Its prescribed backgrounds have probability between \(e^{-CN^3}\) and \(e^{-cN^2}\).
Thus [the obstruction](../ledger/Yin_L_F0066_v11.md#scope-and-continuation) rules out a summable bound uniform over legal polynomially invertible high-matching backgrounds, while leaving the averaged target, the bounded-diagonal pilot and the full F0012 contract open.
The separate [independent whole-material review R200v19](../audits/reviews/Yin_R_F0200_v19.md#invertible-minor-atom-whole-material) checks the complete construction, original-law realization and stated limitations.

<a id="inverse-quadratic-coupled-background-obligation"></a>
## What inverse quadratic concentration supplies on the remaining actual minors

The complete source comparison and coupled reduction are fixed in [L66v12](../ledger/Yin_L_F0066_v12.md#inverse-quadratic-coupled-background-obligation).
Its [actual-law application](../ledger/Yin_L_F0066_v12.md#actual-complete-quadratic) retains the true center and linear terms through Ngu12a's quadratic concentration convention, with the raw radius \(N^{1-\Theta}\).
The [accepted symmetric-part guard](../ledger/Yin_L_F0066_v12.md#polynomial-row-combination-floor) and the remaining polynomial inverse bound exclude the small-row-combination alternative and give a low-entropy GAP vector.

The [exact resulting system](../ledger/Yin_L_F0066_v12.md#coupled-near-kernel-interface) concerns \(\mathcal T=DS^{-1}D^T=S-KS^{-1}K\), with \(S=\operatorname{sym}D\) and \(K=\operatorname{skew}D\).
It keeps \(Sv-Ku=0\) on every row and \(Su-Kv\) small outside only \(O(1)\) rows, with \(v=S^{-1}Ku\) polynomially bounded but not arithmetically controlled.
The two-block realization shares the same original Wigner minor, so the known independent-shift count does not apply.
The [sufficient probability obligation and exact averaging bridge](../ledger/Yin_L_F0066_v12.md#sufficient-mean-probability-obligation) remain unproved.
This is an ordinarily self-checked reduction and source comparison, not a completed background rarity theorem.

<a id="single-row-schur-coupled-count"></a>
## Single-row Schur exposure and the remaining profile count

The full single-row attempt and its exact limitation are retained in [L66v13](../ledger/Yin_L_F0066_v13.md#single-row-schur-coupled-count).
The [original-law exposure](../ledger/Yin_L_F0066_v13.md#single-row-conditioning) expresses the companion by one complex Schur parameter, while the [uniform half-rank bound](../ledger/Yin_L_F0066_v13.md#uniform-half-rank-bound) survives every value of that parameter and deletion of only \(O(1)\) equations.
The [fixed-candidate calculation](../ledger/Yin_L_F0066_v13.md#fixed-candidate-estimate) gives an exponential conditional bound by a polynomial scalar net and the original finite-second-moment projection estimate.
This is ordinary exploration and self-checking, not independent review or Claim adoption.

The [remaining counting boundary](../ledger/Yin_L_F0066_v13.md#entropy-and-average-boundary) is explicit: the available GAP family count is \(N^{C_*N+O_a(N^\varepsilon)}\), while the probability gain established for each fixed candidate is \(e^{-cN}\).
Families of size \(\exp(o(N))\) are controlled and would fit the [mean-background bridge](../ledger/Yin_L_F0066_v12.md#sufficient-mean-probability-obligation), but no such compression of the inverse-theorem output has been proved.
The unfinished continuation is a profile-sensitive probability count or candidate entropy reduction for the actual shared-row coupled system.
It must retain the original conditional row law and cannot multiply the existing one-row bounds across overlapping exposures or regard the companion as an independent center.
The full mean-background high-concentration target remains open.

<a id="multirow-schur-conditional-profile-obstruction"></a>
## Multirow exposure requires information beyond the relaxed conditional profile

The complete simultaneous Schur exposure and lawful conditional probability product are fixed in [L66v14](../ledger/Yin_L_F0066_v14.md#multirow-schur-conditional-profile-obstruction).
Its [coding-parameter obstruction](../ledger/Yin_L_F0066_v14.md#coding-parameter-obstruction) shows that conditioning on the companion statistic can determine an entire original sign row, even for a dense structured candidate whose ordinary concentration tends to zero.
Consequently the unrestricted conditional-profile census cannot supply the missing background probability gain.
This is an ordinary method-failure finding, not an actual coupled-background or F0012 counterexample.

Further work must retain the [actual Schur parameter relation, actual centers, or a joint row-pair estimate](../ledger/Yin_L_F0066_v14.md#remaining-actual-model-boundary) that the tested relaxation discarded.
The [fixed-candidate exponential bound](../ledger/Yin_L_F0066_v13.md#fixed-candidate-estimate) and its full-family entropy gap remain at their stated scope.
No gain from the actual B,C average or estimate for the full structured family has been established.

<a id="actual-center-random-graph-profile-test"></a>
## Actual-center random graphs and the remaining averaged progression tube

The complete center-operator lower bound, actual Schur equations and original-law random-graph representation are fixed in [L66v15](../ledger/Yin_L_F0066_v15.md#actual-center-random-graph-profile-test).
The [polynomial center floor](../ledger/Yin_L_F0066_v15.md#center-operator-polynomial-floor) leaves at most \(2r+e\) uncontrolled domain directions after e retained-row omissions.
Its [random graph](../ledger/Yin_L_F0066_v15.md#original-rectangle-random-graph) has only \(O(\log N)\) parameters, but its vector output depends on the same original rectangular block that supplies the probability.
The [short-row profile comparison](../ledger/Yin_L_F0066_v15.md#short-row-pair-scale-boundary) explains why neither a polynomial-in-N joint-concentration threshold nor an ordinary \(r^{-1/2}\) marginal factor reproduces C194v1's long-coordinate entropy cancellation.

The continuing probability obligation is the [feasible progression tube averaged over actual backgrounds](../ledger/Yin_L_F0066_v15.md#averaged-tube-and-mean-bridge), with all actual Schur, retained and exposed equations, the nonzero norm condition and the original bounded omission count preserved.
Its parameter and progression-descriptor choices cost \(\exp(o(N))\); a uniform fixed-choice exponential bound, or the stated averaged maximum bound for conditional original-rectangle probabilities, would feed into the existing mean-background bridge.
No such bound has been established.
The next discriminating step must exploit those actual equations or the distribution of the conditioned center operators to control the progression tube, rather than substitute a fixed-candidate estimate for a random graph or use rank alone.
This remains ordinary exploration with no independent review, full structured-family probability conclusion or counterexample to F0012.

<a id="two-column-long-profile-precision-test"></a>
## Two-column profiles and the remaining exact-companion low-product count

The complete original-law joint exposure and four-dimensional inverse-theorem comparison are fixed in [L66v16](../ledger/Yin_L_F0066_v16.md#two-column-long-profile-precision-test).
The [joint degenerate class](../ledger/Yin_L_F0066_v16.md#joint-degenerate-count) and [fixed high joint-product class](../ledger/Yin_L_F0066_v16.md#high-joint-product-count) admit simultaneous compression of u and v at their stated precision and omission scope.
The [two-precision comparison](../ledger/Yin_L_F0066_v16.md#two-precision-grid-obstruction) shows why the unrestricted fine companion grid does not close the low-product class by the accepted multiscale count.
The complete fixed exploration, including both subclass estimates and their limits, has the [independent whole-scope review R200v23](../audits/reviews/Yin_R_F0200_v23.md#joint-two-column-profile-whole-scope), which found no substantive gap under the stated inputs.
That review supplies no low-product probability bound, Claim adoption or F0012 completion.

That fixed trial leaves a probability count for low joint-product pairs with the original structured u and exact \(Sv=Ku\), avoiding the full norm-ball entropy for v.
The adopted exact-companion theorem below supplies this count for the actual three-factor background by preserving independent original coordinates after outside recovery.
Its use in the [mean-target contribution](../ledger/Yin_L_F0066_v16.md#mean-target-and-structure-boundary) is the separate complete-application question below.
The [actual \(\mathcal T^{-1}e_h\) construction](../ledger/Yin_L_F0066_v16.md#actual-unstructured-feasible-pair) prevents dropping the u-structure requirement altogether; it does not refute the structured target.

<a id="outside-equations-exact-companion-recovery"></a>
## Exact-companion recovery and its accepted three-factor application

The complete integrated theorem is fixed at [C194v21](../claims/Yin_C_F0194_v21.md#statement), with its [reviewed proved decision](../claims/Yin_C_F0194_v21.md#decision-structured-companion-reviewed).
Its statement concerns the actual real three-factor model, fixed nonreal z, B,C-measurable finite u-families with leading entropy independent of the fine precision, and the exact companion \(v=S^{-1}Ku\), on its stated polynomial guards.
It gives an arbitrary-power marginal pair bound uniformly in the outer index.
The source family remainder is \(o_a(n)\) for each fixed a and is uniform in B,C; the eventual dimension threshold may depend on that prescribed remainder.

The complete [argument](../claims/Yin_C_F0194_v21.md#argument) includes the actual commutator bulk, common outside identification, exact companion recovery, the transferred small-ball event on an original independent rectangle, and the full earlier degenerate/high-product proofs.
Its [parameter order](../claims/Yin_C_F0194_v21.md#parameter-order) fixes all coarse exponents and the family leading entropy before choosing the fine a.
The outside measurable reconstruction and both transfer inequalities retain the actual centers.
The full S norm is an event restriction, not a condition imposed on the unexposed rectangle.
The [independent whole-proof finding R200v24](../audits/reviews/Yin_R_F0200_v24.md#structured-companion-pair-whole-proof) covers the integrated statement and argument; R200v23 retains only its earlier L66v16 subclass scope.

<a id="ec-mean-application-continuation"></a>
### The complete conditional-numerator and Brown application

The [adopted C186v23 theorem](../claims/Yin_C_F0186_v23.md#decision-three-real-product-reviewed) contains the complete original-law application and later least-value, logarithmic and Brown deductions.
Its [source-to-pair argument](../claims/Yin_C_F0186_v23.md#inverse-quadratic-to-pair) supplies the complete quadratic reduction with arbitrary actual linears and center, the deterministic finite family and exact companion.
The [mean bridge](../claims/Yin_C_F0186_v23.md#candidate-count-application) keeps the exposed diagonal unrestricted and pays no Markov loss for the direct pair-event inclusion; the separate isolated-minor conversion retains its own loss and scale order.
The [independent whole-chain review R190v22](../audits/reviews/Yin_R_F0190_v22.md#three-real-product-whole-proof) checks these interfaces, all guard exceptions, exhaustive minor branches and the one-event planar conclusion.
Thus the actual three-real-factor Brown subclass is resolved, with fixed-parameter logarithmic limits asserted at nonreal z and zero.
The remaining allocation is propagation to an unresolved polynomial class, retaining the general complex-law and general-polynomial F0012 contract.

<a id="ordered-product-skew-bulk-propagation-test"></a>
## A conditional extension to every fixed ordered product

This ordinary comparison identifies another application of a general independent-shift companion count, if that extension of the accepted three-factor count is established.
It is not an application of C194v21's model-specific statement to a different shift.
Fix d at least three, original independent real finite-second-moment Wigner inputs, a fixed nonzero complex z, and set
\[
 R_N=W_2^{(N)}\cdots W_d^{(N)},\qquad
 P_N=W_1^{(N)}R_N,\qquad F_N=-zR_N^{-1}
\]
on the event that all factors are invertible.
The [accepted single-factor floor](../claims/Yin_C_F0188_v2.md#statement) gives this event and a polynomial bound on F_N with any prescribed polynomial failure power.
The original second-moment Frobenius bounds likewise give a polynomial upper bound on R_N with any prescribed polynomial failure power.

There is an exact identity
\[
 F_N-F_N^T=-zR_N^{-1}(R_N^T-R_N)(R_N^T)^{-1}.
\]
The formal polynomial \(T=x_d\cdots x_2-x_2\cdots x_d\) is nonzero because its two words are distinct.
In the [accepted Fock realization](../audits/literature/Miy26/Yin_U001.md#setting-and-hypotheses), the top-length components of T(s) applied to the vacuum are those two distinct word vectors, so \(\tau(T(s)^*T(s))>0\).
The [C186v4 expected weak law and row concentration](../claims/Yin_C_F0186_v4.md#row-concentration), applied to the fixed positive polynomial \(T^*T\) and a bounded-variation spectral test away from zero, therefore give a positive fraction of singular values of \(R_N^T-R_N\) bounded below by a fixed positive constant, outside an exponentially small event.
The identity and the polynomial upper norm of R_N transfer this to a positive fraction of polynomially bounded-below singular values of the actual skew part of F_N.
Any fixed number of principal deletions loses at most twice that number of singular directions.
This bulk calculation uses only z nonzero, not z nonreal.

The needed extension would count exact companion pairs for such an independent shift, with the same first-input-independent finite family, precision-independent leading entropy and polynomial guard intersection as C194v21.
If that extension is accepted, the [C186v23 complete source-to-pair and mean assembly](../claims/Yin_C_F0186_v23.md#inverse-quadratic-to-pair) has the same original first-input law, raw normalization, symmetric-part guards and arbitrary-shift isolated and low-matching interfaces in this model.
Those interfaces must be explicitly matched in a full new application before adopting its floor.
The exact factorization \(P_N-zI=(W_1^{(N)}+F_N)W_2^{(N)}\cdots W_d^{(N)}\) then supplies the proposed product floor.
The [existing fixed-product singular-value argument](../claims/Yin_C_F0186_v10.md#middle-and-free-log) would have summable failures here, since every carrier factor is an original single Wigner matrix; its profile is a constant times \((k/N)^d\) beyond O(N^(3/4)) bottom indices.
Thus an arbitrary-power floor would feed the same pathwise logarithmic and planar steps as C186v23, now at every fixed nonzero z; zero uses the separate factor floors directly.
The resulting all-parameter logarithms and Brown theorem remain a conditional continuation until the general count and the complete changed application have been checked and adopted.
The [earlier ordered-product theorem](../claims/Yin_C_F0186_v10.md#statement) already proves probability logarithms and every-coupling limsup, and retains that accepted scope throughout this test.

<a id="independent-polynomial-shift-propagation-test"></a>
## Propagation to an independent polynomial background

The complete argument is fixed in [C194v22](../claims/Yin_C_F0194_v22.md#statement), with its [corrected-chain adoption](../claims/Yin_C_F0194_v22.md#decision-skew-bulk-count-qualified-reviewed).
It gives a generic guarded count and a fully assembled least-value floor for \(x_1+Q(x_2,\ldots,x_d)\), with original real finite-second-moment Wigner inputs and arbitrary repetition of background variables.
Its own independent whole-proof finding and subsequent corrected-chain recheck support the uniform-shift proof, actual polynomial bulk and complete floor assembly.
The accepted [C194v21 decision](../claims/Yin_C_F0194_v21.md#decision-structured-companion-reviewed) and [C186v23 decision](../claims/Yin_C_F0186_v23.md#decision-three-real-product-reviewed) retain their exact three-factor scopes.
Their earlier reviews do not independently review this larger statement.

The generic count conditions on the entire background independent of the first input.
It retains a deterministic complex shift of polynomial norm, a linear number of polynomially large singular values of its algebraic skew part, the polynomial \(S,S^{-1},K\) guards, the exact companion \(v=S^{-1}Ku\), and a first-input-independent finite \(u\)-family with a precision-independent leading entropy exponent.
Only \(Su-Kv\) may omit a bounded number of rows.
C194v22 supplies the [common outside identification and recovery](../claims/Yin_C_F0194_v22.md#generic-identification), the complete degenerate/high/low profile count, and the [noncircular parameter order and original-law integration](../claims/Yin_C_F0194_v22.md#generic-parameter-order).
It does not apply the narrower C194v21 theorem statement to a new shift by notation alone.

For \(Q\in\mathbb C\langle x_2,\ldots,x_d\rangle\), reverse words without conjugating coefficients and set \(T=(Q-Q^{\mathrm{rev}})/2\).
The [polynomial dichotomy](../claims/Yin_C_F0194_v22.md#polynomial-skew-bulk) is exhaustive.
If \(T=0\), the full shift \(Q(W_2,\ldots,W_d)-zI\) is complex symmetric, and the accepted C188v2 theorem applies on its arbitrary-power polynomial norm guard.
If \(T\ne0\), its highest-degree Fock component is nonzero, so \(\tau(T(s)^*T(s))>0\).
C186v4 expected weak convergence and bounded-variation row concentration then give an exponential failure bound for a fixed positive singular bulk of the actual \(T(W)\).
A principal deletion loses at most two singular directions, and original second-moment norm guards control the finite word expansion of \(Q\).
This uses neither a Brown theorem for \(Q\) nor untruncated finite-matrix high trace moments.

The [complete additive-floor assembly](../claims/Yin_C_F0194_v22.md#additive-floor-assembly) checks the original full quadratic numerator, including both nonsymmetric border offsets, the random diagonal center and every linear term.
It retains the exact factor-\(N\) raw determinant-ratio scaling, arbitrary-power second-value and symmetric-part guards, isolated small minors, the source coefficient floor, rational candidate entropy, exact companion, low-matching inclusion and the many-index average without an \(N\) loss.
The generic count supplies a direct background concentration tail on the remaining invertible branch; the small-minor branch uses the isolated union and Markov's inequality.
The adopted [floor statement](../claims/Yin_C_F0194_v22.md#additive-floor-statement) is therefore, for every fixed \(z\in\mathbb C\) and \(b>0\), an exponent \(A\) with
\[
 \mathbb P\{s_{\min}(W_1+Q(W_2,\ldots,W_d)-zI)\le N^{-A}\}
       =O(N^{-b}).
\]
Every fixed real, nonreal and zero parameter is within that statement.
This scope follows from the whole generic exposure and guard proof, not merely from the fact that the skew part is independent of \(z\).
For example, \(x_1+x_2x_3x_2x_3\) has repeated background variables and fits the stated class.
There is no analogous exposure when every prospective first variable is repeated inside the background.

The separate [adopted C186v24 assembly](../claims/Yin_C_F0186_v24.md#decision-two-real-classes-reviewed) now supplies the logarithmic and Brown conclusions, using the summable C187v2 middle profile and C186v4 weak, positive-tail and planar controls.
Its [independent repaired whole-proof finding](../audits/reviews/Yin_R_F0190_v23.md#two-real-classes-repaired-whole-proof) covers both the complete consumer and the corrected upstream low-matching probability qualification.
C194v22 itself asserts only its count and floor scopes.
An outer-polynomial closure requires its own complete interface check.
The original F12 contract remains unchanged; repeated exposure of the distinguished input, general matrix-coefficient linearizations and the full arbitrary-polynomial real/complex problem remain outside these two classes.

<a id="two-sided-linear-exposure-profile-test"></a>
## A bounded test beyond a fresh independent additive exposure

This ordinary agent-S comparison for Yin considers the original real fixed-law finite-second-moment model with two independent inputs \(A=W_1^{(N)},B=W_2^{(N)}\), arbitrary cross-size coupling, and
\[
 P_N=AB+2BA,\qquad P(x,y)=xy+2yx.
\]
This development used no C186v24 review result; its comparison is with the exact two classes, now separately adopted, and supplies no extension of that theorem.
The polynomial is linear in each input, but each possible exposed variable occurs in two different positions.
The coefficient tensor of its \(x\)-linear part is \(1\otimes y+2y\otimes1\), of rank two in the bases \(1,y\).
Thus it is not a single displayed two-sided carrier \(L(y)(x+Q(y))R(y)\); the degree-two coefficient matrix likewise has rank two, excluding a single product of two scalar affine forms.
The same check applies after exchanging the inputs.
The inspected [carrier statements](../claims/Yin_C_F0186_v7.md#statement), [S32 frontier](../strategies/Yin_S_F0032.md#route), and the two exact C186v24 classes supply no such exposure certificate.
This comparison does not assert that every possible spectral identity has been classified.
The superficially similar choice \(xy+iyx\) would be a poor new test: multiplication by \(e^{-i\pi/4}\) makes it selfadjoint.
For every fixed \(z\), a scalar real witness \(3ab\ne z\) exists, so there is no forced odd-dimensional determinant-zero obstruction.
The [accepted GOE statement](../claims/Yin_C_F0186_v9.md#statement) already identifies the finite free target for this nonconstant polynomial and covers its Gaussian realization; that Gaussian convergence argument supplies no unchanged-law finite-variance estimate here.

The possible new information is a direct reconstruction using an original rectangular block of the other input, without an inverse of an internal \(A\)-minor.
For a fixed candidate \(u\), put \(v=Bu,t=Au\) and
\[
 r=(AB+2BA-zI)u=Av+2Bt-zu.
\]
Choose disjoint deterministic blocks \(R,T\) of size \(\lfloor N/8\rfloor\), let \(I=R\cup T\), and \(J=I^c\).
The [accepted original-real-vector distance mechanism](../claims/Yin_C_F0194_v3.md#linear-codimension), applied to the independent columns of \(B_{JI}\), gives \(s_{\min}(B_{JI})\ge N^{-1}\) outside \(Ce^{-cN}\).
Indeed each column has constant-order distance from the other columns after the \(N^{-1/2}\) normalization, since the remaining complex codimension is at least \(N/2\); the column-distance inequality loses at most \(\sqrt{|I|}\).
This event is common to every candidate.
An arbitrary-power polynomial guard for \(\|B\|\) follows from its original second moment.

Condition on the whole \(B\), \(A_{JJ}\), and \(A_{JI}\), leaving the original \(A_{II}\) unexposed.
For a candidate fixed before \(A\) is sampled, \(v,t_J,(Av)_J\) are then known.
Set
\[
 t_I^*=\tfrac12 B_{JI}^{\dagger}
       \bigl(zu_J-(Av)_J-2B_{JJ}t_J\bigr).
 \tag{Two-sided-outside-recovery}
\]
On \(\|r\|\le\varepsilon\), one has \(\|t_I-t_I^*\|\le\tfrac12N\varepsilon\).
The two remaining equations on \(I\) are
\[
 A_{II}u_I=t_I-A_{IJ}u_J,\qquad
 A_{II}v_I=zu_I-2B_{II}t_I-2B_{IJ}t_J-A_{IJ}v_J+r_I.
\]
Replacing \(t_I\) by its reconstruction changes their row tolerances by at most \(C N^{\gamma+1}\varepsilon\) on \(\|B\|\le N^\gamma\).
Their centers are fixed by the exposed outside and the candidate.
After exposing \(A_{RR},A_{TT}\), the original \(T\)-by-\(R\) rectangle remains independent, with paired fresh coefficient vectors \((u_j,(Bu)_j)\).
Its raw row tolerance has the additional factor \(\sqrt N\).
Consequently a prescribed finite family of size \(N^{C_*N+o(N)}\) can be counted on a block where the joint row concentration is at most \(N^{-D}\): the probability is at most \(N^{C_*N+o(N)-D|T|}\), apart from the common guards.
The reconstructed \(t_I^*\) requires no extra fine net.
This is a genuine new exposure identity for the two-sided map, but it does not count its high-concentration complement or all adaptive singular vectors.

Two short rejection tests prevent immediate promotion to a new floor.
First, the original single-row numerator is not the quadratic numerator used in C186v23.
With
\[
 A=\begin{pmatrix}a&x^T\\x&A_0\end{pmatrix},\qquad
 B=\begin{pmatrix}b&y^T\\y&B_0\end{pmatrix},
\]
its principal interior block is
\[
 A_0B_0+2B_0A_0-zI+xy^T+2yx^T,
\]
so it still depends on the fresh original row \(x\).
The determinant can genuinely have degree four: at size four, \(A(t)=t(E_{12}+E_{21})\) and \(B=E_{13}+E_{31}+E_{24}+E_{42}\) give \(\det(AB+2BA)=4t^4\).
This is an algebraic source-applicability witness, not a probability or Task counterexample.
The existing Wigner-plus-independent-shift cofactor average and quadratic inverse theorem cannot simply be applied to this interior.

Second, the independent image \(Bu\) need not lose its fine arithmetic structure.
For zero-diagonal Rademacher \(B\) and \(u=N^{-1/2}(1,\ldots,1)\), write \((Bu)_j=k_j/N\), with integers \(|k_j|\le N-1\).
For fresh independent Rademacher scalars \(\eta_j\), the pair
\[
 \left(\sum_j u_j\eta_j,\ \sum_j(Bu)_j\eta_j\right)
\]
takes at most \((N+1)(2N^2+1)\) values.
Its largest exact atom is therefore at least \(cN^{-3}\) for every such \(B\).
This does not say the near-kernel equations hold, but rules out eliminating all rich joint profiles by an arithmetic-smoothing claim about the independent background alone.
Diagonalizing \(B\) also supplies no original-law solution: an arbitrary orthogonal change does not preserve the independent coordinates of a non-Gaussian Wigner input.

The recommended first discriminating investigation is one legal, entropy-accounted joint-profile count for the complete relations \(Bu=v,\ Au=t,\ Av+2Bt-zu\approx0\), beginning with the actual rational-GAP family and precision-independent leading entropy in [C186v23](../claims/Yin_C_F0186_v23.md#inverse-quadratic-to-pair).
It must retain the centers in (Two-sided-outside-recovery) and the original \(B\)-relation while treating the rich profiles; replacing them by arbitrary centers, a free \(t\)-net, or an independent second copy of a reused rectangle is not the test.
A useful outcome is an explicit admissible exposure with negative net \(N\log N\) exponent uniformly as the approximation precision increases, or an explicit unavoidable precision-dependent entropy/coding loss analogous to the [earlier cyclic obstruction](../ledger/Yin_L_F0063_v2.md#free-net-entropy-loss).
The Rademacher model can first reject the bookkeeping, but success there would not supply the full fixed-law finite-variance statement.

The first unsupported implication back to F12/F14 is a lawful reduction from an adaptive near-kernel vector of this actual two-sided matrix to that predetermined finite family, or an all-vector count replacing that reduction.
The fresh-row quartic dependence above explains why the existing source-to-family module does not supply it.
Even a successful family count would still require that reduction, actual complete-minor/average estimates and a middle negative-logarithm bound; C187v2 cannot be applied directly to \(AB+2BA-zI\).
The [accepted general controls](../claims/Yin_C_F0186_v4.md#statement) would then supply the weak/positive-tail and planar parts, but do not supply those missing negative-tail inputs.
I recommend one bounded exposure-and-entropy test for this minimal two-sided class, rather than a main-route change or another carrier/outer closure.

<a id="two-sided-adaptive-fiber-test"></a>
## The tested one-sided adaptive fiber is identically feasible

The [fixed L66v17 test](../ledger/Yin_L_F0066_v17.md#two-sided-adaptive-fiber-test) completes the legal-exposure and precision-budget check for the proposal above at the original real finite-second-moment law.
After conditioning on all of \(B\), \(A_{JJ}\), \(A_{JI}\), \(A_{RR}\) and \(A_{TT}\), the original rectangle \(C=A_{TR}\) remains fresh, while the full exact outside fiber has complex dimension at least \(4m\), where \(|R|=|T|=m\).
Its two retained \(T\)-side relations impose only \(2m\) linear equations, so the relaxed adaptive existence event has probability one for every realization of \(C\), even at zero tolerance and with the retained polynomial companion bounds.
The [actual equations and dropped constraints](../ledger/Yin_L_F0066_v17.md#two-sided-relaxed-event-certain) make clear that these fake solutions need not solve the \(R\)-side equations and are not Task counterexamples.
The [precision budget](../ledger/Yin_L_F0066_v17.md#two-sided-precision-entropy) also has a positive leading loss for an unrestricted outside-fiber net; a fixed-family poor-profile estimate does not repair it.

A continuation must preserve the [full joint image and its center compatibility](../ledger/Yin_L_F0066_v17.md#two-sided-mirror-joint-map), or establish a genuine adaptive-to-structured reduction before discarding rows.
The outputs \((Cu_R,Cv_R,C^Tu_T,C^Tv_T)\) reuse the same entries, with real-linear rank \(m(k_R+k_T)-k_Rk_T\); they do not supply two independent row products.
No such new reduction or quantitative center-compatibility estimate is established here, and no least-value floor, middle negative-logarithm estimate or F12/F14 conclusion is added.

<a id="two-sided-actual-center-transversality-test"></a>
## Actual center constraints help locally, but leave a critical counting problem

The [fixed L66v18 calculation](../ledger/Yin_L_F0066_v18.md#two-sided-actual-center-transversality-test) now retains both sides of the original rectangle and all four actual real center quadrics.
Its [explicit background family](../ledger/Yin_L_F0066_v18.md#two-sided-transverse-and-degenerate-backgrounds) has a transverse member with Jacobian rank four and a degenerate member with rank three, together with a complete matrix realization and a fixed single-size original-law support check.
Thus the actual constraints can reduce candidate dimension, but full coefficient rank and the existing guards alone do not imply the required transversality; the support check supplies no asymptotic bad-event bound or Task counterexample.

The [complete precision budget](../ledger/Yin_L_F0066_v18.md#two-sided-transversality-entropy-interface) gains only one real precision power, or conditionally two in the complex case, before the unresolved coarse covering cost.
That gain does not absorb a remaining positive order-N exponent or exponential-in-N factor for any fixed fine exponent.
The first continuing interface is original-law quantitative control of the approximate outside tube and actual center strata together with an arithmetic or probabilistic gain that handles this critical counting cost.
No such joint count, nonreal transversality theorem, adaptive-to-structured reduction, principal-minor average or middle negative-logarithm estimate for this polynomial is established by the test.


<a id="all-center-joint-gap-and-companion-covariance"></a>
## All-center joint gap and its actual companion interface

The complete theorem is fixed in [C187v28](../claims/Yin_C_F0187_v28.md#statement), with its [proved decision](../claims/Yin_C_F0187_v28.md#decision-all-center-companion-reviewed) and [independent whole-proof finding](../audits/reviews/Yin_R_F0191_v28.md#all-center-companion-reviewed).
The [larger-center argument](../claims/Yin_C_F0187_v28.md#all-center-gap-high-centers) extends the accepted original real finite-second-moment joint gap to every real center using the existing tail-adapted compressed transfer.
The same event gives the [complex-vector and complex-center sum bound](../claims/Yin_C_F0187_v28.md#all-center-complex-extension), while the actual normalized companion graph has [Hermitian covariance](../claims/Yin_C_F0187_v28.md#companion-hermitian-covariance) bounded below at scale \(N^{-6K-1}\) under the specified polynomial norm and graph-error guards.
Its [common-minor and average interface](../claims/Yin_C_F0187_v28.md#companion-normalization-and-average) retains the original fresh-row law only for a candidate fixed from the minor before exposure.
The main joint-gap exception remains \(o(1)\), and Hermitian covariance supplies neither a six-dimensional real small-ball bound nor an adaptive-to-structured reduction.

The new usable input is this changed all-center and graph interface, not a replacement for the [critical double-sided entropy obstruction](../ledger/Yin_L_F0066_v18.md#two-sided-transversality-entropy-interface).
The next discriminating problem is the complete original-law normalized physical Schur expression below, whose numerator and graph normalization reuse the same fresh rows.
No corresponding probability bound, singular-minor treatment or middle negative-logarithm profile has been established.

<a id="two-sided-physical-schur-continuation"></a>
### Exact physical Schur expression retained for continuation

The following finite-dimensional identities were derived within this bounded exploration; they are ordinary calculations, not a reviewed small-ball theorem.
They retain information not contained in the covariance conclusion.
Write \(A=\begin{pmatrix}a&x^T\\x&A_0\end{pmatrix}\), \(B=\begin{pmatrix}b&y^T\\y&B_0\end{pmatrix}\), and delete all three auxiliary coordinates at this physical site from the [actual companion pencil in C187v28](../claims/Yin_C_F0187_v28.md#companion-use-boundary).
The remaining matrix \(Q=\mathcal L_0(z)\) is measurable in the two original physical minors and independent of the two original fresh rows \(x,y\).
Its border blocks, with row/column channels ordered as \((u,v,t)\), are
\[
 D_i=\begin{pmatrix}-z&a&2b\\b&-1&0\\a&0&-1\end{pmatrix},\quad
 R_i=\begin{pmatrix}0&x^T&2y^T\\y^T&0&0\\x^T&0&0\end{pmatrix},\quad
 C_i=\begin{pmatrix}0&x&2y\\y&0&0\\x&0&0\end{pmatrix}.
\]
Both border blocks reuse the same \(x,y\); no independent copy is introduced.
On the branch where \(M_0=A_0B_0+2B_0A_0-zI\) is invertible, put
\[
 G=M_0^{-1},\qquad r^T=x^TB_0+2y^TA_0,\qquad c=A_0y+2B_0x.
\]
Solving the last two block equations of \(Qw=f\) gives
\[
 Q^{-1}\begin{pmatrix}f_1\\f_2\\f_3\end{pmatrix}
 =\begin{pmatrix}
 G(f_1+A_0f_2+2B_0f_3)\\
 B_0G(f_1+A_0f_2+2B_0f_3)-f_2\\
 A_0G(f_1+A_0f_2+2B_0f_3)-f_3
 \end{pmatrix}.
\]
In particular \(Q\) is invertible exactly when \(M_0\) is invertible, and direct multiplication yields the complete Schur matrix
\[
 S_i=D_i-R_iQ^{-1}C_i
 =\begin{pmatrix}
 -z+3x^Ty-r^TGc&a-r^TGx&2b-2r^TGy\\
 b-y^TGc&-1-y^TGx&-2y^TGy\\
 a-x^TGc&-x^TGx&-1-2x^TGy
 \end{pmatrix}.
 \tag{Actual-two-sided-physical-Schur}
\]
Each entry is at most quadratic in \(x,y\), while its determinant can genuinely have degree six.
For the explicit size-three example \(a=b=0\), \(A_0=B_0=0_{2\times2}\), \(z=1\), \(x=t e_1\), \(y=t(e_1+e_2)\),
\[
 \det(AB+2BA-I_3)=(3t^2-1)(1-3t^2-2t^4),
\]
whose leading coefficient is \(-6t^6\).
This is an exact algebraic example, not a probability claim about a fixed original-law sequence.

The physical column block, projected orthogonally away from all other columns, has the following coordinates in an orthonormal basis of that complement:
\[
 F_i=\bigl(I_3+R_iQ^{-1}Q^{-*}R_i^*\bigr)^{-1/2}S_i.
 \tag{Actual-two-sided-block-distance}
\]
Indeed \([I_3,-R_iQ^{-1}]\) annihilates the other columns, and left multiplication by the displayed inverse square root makes its rows orthonormal.
For a unit approximate kernel of the full pencil with residual norm at most \(\varepsilon\), some physical three-vector has norm at least \(N^{-1/2}\).
If that corresponding \(Q\) is invertible, applying the projection gives \(s_{\min}(F_i)\le\sqrt N\,\varepsilon\).
This implication alone does not control the possibility that the selected minor is singular.
Also \(\det\mathcal L_N(z)=\det(AB+2BA-zI)\) and
\(s_{\min}(\mathcal L_N(z))\le s_{\min}(AB+2BA-zI)\), since \((u,Bu,Au)\) maps to \(((AB+2BA-zI)u,0,0)\) and has norm at least \(\|u\|\).

The random factor in (Actual-two-sided-block-distance) depends on the same original fresh rows as \(S_i\).
It cannot be frozen as an independent denominator for a linear fresh-row estimate.
The coefficient matrices \(E_{12}+E_{31}\) and \(2E_{13}+E_{21}\) of this pencil are not selfadjoint, and the pair of test directions \((e_1,e_1)\) annihilates both bilinear forms.
Thus neither the earlier selfadjoint positive-frame interface nor a full auxiliary frame can be imported by renaming the channels.
A complete original-law small-ball estimate for this normalized Schur object, singular-minor handling, an unconditional average and a middle singular-value estimate remain unproved.
All identities here follow by the displayed block elimination and the explicit determinant calculation; no numerical run or unretained program is necessary evidence.


<a id="two-sided-conditional-quartic-test"></a>
## One original row gives a quartic quotient with a remaining rank obligation

The complete bounded test is fixed in [L66v19](../ledger/Yin_L_F0066_v19.md#two-sided-conditional-quartic-test), as ordinary exploration with authoring checks, not a Claim adoption or independent review.
Its [legal one-row exposure](../ledger/Yin_L_F0066_v19.md#two-sided-legal-one-row-conditioning) leaves the original product row law and lowers the complete determinant from total degree six to conditional degree at most four.
The [same-row quotient and exterior-column formula](../ledger/Yin_L_F0066_v19.md#two-sided-quartic-denominator) preserve the random denominator and the exact rank-deficient branch even when the physical minor is singular.
The [distinct fourth-order Walsh example](../ledger/Yin_L_F0066_v19.md#two-sided-quartic-walsh-example) rules out a universal quadratic or cubic original-coordinate reduction, including at nonreal parameters.
The separate [high-corank background](../ledger/Yin_L_F0066_v19.md#two-sided-gap-with-singular-column-branch) shows that the current individual minor gap and norm conditions alone cannot give a vanishing uniform conditional bound; its fixed original-law realizations are summably rare and do not refute the Tasks.

The next concrete obligation is [original-law control of the full quartic pair and rank branch](../ledger/Yin_L_F0066_v19.md#two-sided-quartic-first-obligation), with the recorded polynomial normalization and index-union costs.
It requires additional quantitative background or coefficient information and control of the same fresh row in numerator and denominator; the accepted Hermitian covariance by itself supplies neither.
No complete small-ball bound, summable least-value floor, principal-minor average or middle negative-logarithm profile for this polynomial is established by the test.

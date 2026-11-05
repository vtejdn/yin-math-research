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

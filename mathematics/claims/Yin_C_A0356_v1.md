---
author: Yin
---

# Endpoint sums for a visible Schur remainder at a single regularization time

## Statement

Use the [simultaneous two-square block](Yin_C_A0344_v2.md#two-actual-inverses-and-the-formal-remainder) under the order-twenty half-kernel hypothesis.
Over the common sign subgroup \(N\) write \(R=\left(\begin{smallmatrix}D&E\\F&G\end{smallmatrix}\right)\), \(B=[D\ E]\), \(A=[F\ G]\).
The group-ring matrix \(R\) has regular rank two, \(D\) is an affiliated unit, and \(D(\psi)\) is invertible at every visible marking character \(\psi\), where \(r_\psi=\operatorname{rank} R(\psi)\ge3\).
Use coordinates selecting the [nonsummable second inverse](Yin_C_A0350_v1.md#selecting-and-approximating-one-actual-scalar-inverse), with the same invertible constant row and column changes on the indicated blocks of \(R\).
Here \(D\) denotes the transformed leading block, so that its actual bottom right inverse entry is the selected scalar.

There are finite group-ring residuals \(X_n\), built from the inverse approximation to \(D\) and the top row \(B\) at the same time \(n\), that are uniformly bounded in regular operator norm and tend to zero in regular \(L^2\).
Their values at every visible character tend to matrices of rank \(r_\psi-2\).
The normalized absolute coefficients of the chosen scalar inverse spread outside every moving set of bounded cardinality.
When the matrix inverse fails square integrability, the proportion of the incoming squared coefficient energy that survives collection in the product with \(D\) tends to zero.
For a particular proposed half kernel this gives lower bounds on the number of original endpoints carrying character mass and a test using finite group-return coefficients.
A second test compares the least coefficient energy permitted by the five character fibers with a polynomial moment minimum for the two-square positive matrix \(BB^*=DD^*+EE^*\).
In particular the half kernel requires
\[
                  \inf\sigma((BB^*)^{1/2})\le(\sqrt3-1)\|B\| .
\]
Both tests use the joint two-row block, including when the range of \(D\) is not closed.
The assumptions used below do not determine a violated finite inequality on every remaining marking.

## Bounded residuals built from the same-time inverse

Let \(U,V\) denote the constant two-coordinate selectors onto the upper and lower halves of the four input coordinates.
Choose positive \(L_D,L_B\) greater than the respective regular norms of \(D,B\) and their norms at all five marking characters.
Set
\[
 C_n=(I-D^*D/L_D^2)^n,\qquad
 Q_n=L_D^{-2}\sum_{j=0}^{n-1}(I-D^*D/L_D^2)^jD^*,\qquad
 H_n=(I-B^*B/L_B^2)^n .
\]
In the selected coordinates the bottom right entry of \(Q_n\) approximates the inverse of the second Schur pivot in measure and its \(\ell^1\) norm tends to infinity by the [scalar regularization proof](Yin_C_A0350_v1.md#selecting-and-approximating-one-actual-scalar-inverse), applied to this transformed block and its bottom right entry.
The nonzero character values of the pivots and nonsummability of this entry are unchanged premises of that selection.
No \(\ell^2\) convergence of the individual inverse entry is needed.

The orthogonal kernel projection \(P\) of \(R\) is also the kernel projection of \(B\): the kernels are nested and both have dimension two.
Thus \(AP=0\), \(P^2=P\), and \(H_n\to P\) strongly.
Define the two-by-four group-ring matrix
\[
 X_n=(G-FQ_n E)V H_n .
\]
Since \(B=DU+EV\), \(A=FU+GV\) and \(Q_nD=I-C_n\), one has the finite group-ring identity
\[
 X_n=A H_n-FQ_n B H_n-F C_n U H_n.                       \tag{1}
\]
It holds coefficient by coefficient after summing all signed products having the same original group endpoint.
We use the unnormalized regular matrix \(L^2\) norm and write \(\mathcal T_2=\operatorname{Tr}_2\otimes\tau_N\).
Put \(J_n=(I-BB^*/L_B^2)^n\).
The full row rank of \(B\) makes its polar partial isometry a unitary from the complement of \(P\) onto the two output coordinates.
Consequently \(\|H_n-P\|_2^2=\mathcal T_2(J_n^2)\) and \(\|BH_n\|_2^2=\mathcal T_2(BB^*J_n^2)\).
In the singular variable \(x\in[0,1]\) for \(D^*D/L_D^2\), \(1-(1-x)^n\le\min(nx,1)\), hence \(\|Q_n\|\le\sqrt n/L_D\).
Also \(\|BH_n\|\le L_B/\sqrt{2n+1}\), by maximizing \(x(1-x)^{2n}\).
Equation (1) gives a uniform regular operator bound and the finite estimate
\[
 \|X_n\|_2\le
 \|A\|\sqrt{\mathcal T_2(J_n^2)}
 +\frac{\|F\|\sqrt n}{L_D}\sqrt{\mathcal T_2(BB^*J_n^2)}
 +\|F\|\sqrt{\mathcal T_2(C_n^2)} .                         \tag{2}
\]
The first and third traces tend to zero by injectivity of \(BB^*\) and \(D^*D\).
The square of the \(n\)-dependent factor in the middle is the integral of \(L_B^2 n x(1-x)^{2n}\) against the finite spectral measure of \(BB^*/L_B^2\).
The integrand is bounded uniformly and tends to zero on the whole interval, including zero.
This proves \(L^2\) decay without an assumption on the rate.

At a visible \(\psi\), \(Q_n(\psi)\to D(\psi)^{-1}\), and \(H_n(\psi)\to p_\psi\), the orthogonal projection onto \(\ker B(\psi)\).
The selector \(V\) is an isomorphism from that kernel onto its last two coordinates, since its elements are exactly \((-D(\psi)^{-1}E(\psi)y,y)\).
Thus \(X_n(\psi)\to A(\psi)p_\psi\), of rank \(r_\psi-2\).
For every \(n\), the numerical identity on \(p_\psi\) gives
\[
 \|X_n(\psi)\|_{\rm op}\ge
 \|A(\psi)p_\psi\|_{\rm op}
 -\|F(\psi)\|_{\rm op}(1-\sigma_{\min}(D(\psi))^2/L_D^2)^n .
\]
For any fixed finite set \(S\subset N\), the contribution of its coefficients to \(X_n(\psi)\) has Hilbert--Schmidt norm at most \(\sqrt{|S|}\,\|X_n\|_2\).
The character sums outside \(S\) therefore converge to the same nonzero matrix \(A(\psi)p_\psi\).
If \(E_n\) contains the support of \(X_n\), Cauchy--Schwarz bounds the norm of this outside sum by \(\sqrt{|E_n\setminus S|}\,\|X_n\|_2\).
Together with (2) this tests finite original endpoint counts against finite heat moments of \(BB^*\) and \(D^*D\).
Operator norms on the right of (2) can be replaced by sums of coefficient norms when evaluating the test.

## The chosen second inverse on actual endpoints

Let \(Z_n=e_2^*Q_n e_2\) be one of the fixed scalar regularizations whose limit in measure is the [second pivot inverse outside \(\ell^1(N)\)](Yin_C_A0350_v1.md#selecting-and-approximating-one-actual-scalar-inverse).
The convolution norms \(m_n=\|Z_n\|_1\) tend to infinity.
The normalized scalars \(Z_n/m_n\) converge to zero in measure because \(Z_n\) has a fixed affiliated limit and \(m_n\to\infty\).
Their regular operator norms are at most one, so their regular \(L^2\) norms tend to zero by splitting the singular-value integral at an arbitrary positive threshold.
Thus, writing \(k_n=m_n^2/\|Z_n\|_2^2\) for large \(n\), we have \(k_n\to\infty\).
For any moving set of original group elements \(A_n\),
\[
  \sum_{g\in A_n}|Z_n(g)|/m_n\le\sqrt{|A_n|/k_n}.
\]
No sequence of sets with \(|A_n|=o(k_n)\) can carry a fixed fraction of the total variation of the chosen second inverse approximants.

The choice of \(L_D\) also dominates the five numerical norms at the characters of \(N_{\mathrm{ab}}=C_5\).
At each character the regularized matrix converges to the ordinary Moore--Penrose inverse of its evaluation, by singular value decomposition, even if that evaluation is singular.
Consequently the five signed sums of the coefficients of \(Z_n\) on the five residue classes stay bounded by finite Fourier inversion.
At a residue with divergent absolute mass along a subsequence, division by that absolute mass gives signed sum tending to zero.
At least one such residue exists, and this statement concerns already collected coefficients at distinct elements.

There is a separate identity for collisions at the very same group element.
With \(\|\cdot\|_{\mathrm{HS}}\) the numerical Hilbert--Schmidt norm, set
\[
 I_n=\sum_{h,g}\|D(g)Q_n(g^{-1}h)\|_{\mathrm{HS}}^2,\qquad
 O_n=\sum_h\Big\|\sum_gD(g)Q_n(g^{-1}h)\Big\|_{\mathrm{HS}}^2 .
\]
The positive numerical matrix \(A=\sum_g D(g)^*D(g)\) is invertible, since a vector in its kernel gives a constant kernel column of \(D\).
Hence \(I_n\ge\lambda_{\min}(A)\|Q_n\|_2^2\) with unnormalized matrix trace.
The exact identity \(D Q_n=I-(I-DD^*/L_D^2)^n\) gives \(O_n\le2\).
If at least one entry of \(D^{-1}\) fails to lie in \(L^2\), the squared \(L^2\) norm of \(Q_n\) increases to infinity by monotone convergence of the singular-value multipliers.
Thus \(O_n/I_n\to0\): after normalization by \(I_n\), the sum of all off-diagonal real cross terms tends to \(-1\).
If \(D^{-1}\in M_2(L^2)\), the same singular-value calculation gives \(Q_n\to D^{-1}\) in \(L^2\).
Nonsummability of the selected second inverse alone does not choose between these two cases.

## A finite comparison using all five characters

Let \(m\ge0\), \(F_m=\operatorname{supp}R\,(\{e\}\cup\operatorname{supp}(B^*B))^m\), and let \(\pi:N\to C_5\) be the common marked abelian quotient.
Count \(k_j=|F_m\cap\pi^{-1}(j)|\) for the five classes \(j\).
These are counts of distinct elements of \(N\), allowing any number of words at a given endpoint.
For every one of the five characters use \(p_\psi=\operatorname{proj}\ker B(\psi)\), also when \(\psi\) is not visible.
Define the finite quadratic minimum \(b_m\) over five numerical four-square matrices \(T_j\) by
\[
 \min\sum_{j:\,k_j>0}\frac{\|T_j\|_{\rm HS}^2}{k_j},\qquad
 T_j=0\ \ (k_j=0),\qquad
 \Big(\sum_j\psi(j)T_j\Big)p_\psi=R(\psi)p_\psi
       \quad\hbox{for all five }\psi .                            \tag{3}
\]
For a fixed choice of the class totals \(T_j\), the least possible sum of squared endpoint norms is exactly the objective in (3), attained by distributing each total equally over its class.
In particular (3) is the exact lower floor if only these five linear constraints and endpoint counts are imposed.
It is positive because a visible character has \(R(\psi)p_\psi\ne0\).

For every scalar polynomial \(f\) of degree at most \(m\) with \(f(0)=1\), the matrix \(S_f=Rf(B^*B)\) has support in \(F_m\) and \(S_f(\psi)p_\psi=R(\psi)p_\psi\).
Its class totals are feasible in (3), so \(\|S_f\|_2^2\ge b_m\), without using equality of the two regular kernels.
Under that equality \(RP=0\), and polar decomposition of the full row \(B\) gives
\[
 \|R f(B^*B)\|_2^2\le\|R\|^2\mathcal T_2\bigl(f(BB^*)^*f(BB^*)\bigr).
\]
Therefore
\[
 b_m\le\|R\|^2
 \min_{\deg f\le m,\ f(0)=1}\mathcal T_2\bigl(f(BB^*)^*f(BB^*)\bigr).       \tag{4}
\]
The polynomial minimum is the [Christoffel variational minimum](../audits/literature/Sim08/Yin_U001.md#christoffel-variational-principle) for the unnormalized trace spectral measure of \(BB^*\).
Its quadratic form uses only original group-ring returns through power \(2m\), including for singular numerical moment matrices.
Increasing the class counts to proved upper bounds weakens the left hand side and still gives a necessary test, as does replacing \(\|R\|\) by a proved upper bound.
A strict reversal of (4) at any one degree excludes the proposed half kernel.
The lower bound on \(\|S_f\|_2^2\) alone is already implied by the character evaluations and does not give that exclusion.

## A degree-one test on the eight group labels

Use the original marking assigning \(s,t\) degrees \(1,2\) modulo five and \(m_0=(st)^{-1}\) degree \(-3\).
The common sign kernel has this same cyclic quotient, with the identification fixed by restriction from the marking.
Let \(V_0=\{s^{\pm1}t^{\pm1},t^{\pm1}s^{\pm1}\}\).
Since every entry uses \(m_0 V_0\), we have \(F_1\subset m_0 V_0^3\).
Here \(V_0\) is symmetric so its cube contains \(V_0\).
Free reduction gives the following upper bounds for the numbers of distinct original endpoints in the five classes.
Lengths in the table are lengths of the reduced word before the common left translation.
\[
\begin{array}{c|rrrrr}
  &0&1&2&3&4\\ \hline
 2&2&2&0&2&2\\
 4&8&8&16&8&8\\
 6&56&56&64&56&56\\ \hline
 \text{total}&66&66&80&66&66
\end{array}
\]
For an explicit enumeration, represent \(s,t\) by the letters \(1,2\) and their inverses by \(-1,-2\).
Start with the set consisting of the empty list.
In each of three rounds append to each current list every pair \(a,b\in\{1,-1,2,-2\}\) with \(|a|\ne|b|\).
For each appended letter delete the last current letter if it is its negative, and append the letter otherwise.
Keep one copy of each resulting list after both appends.
The three set sizes are \(8,53,344\).
Count each final list \(w\) in column \((\sum w-3)\bmod5\).
This recurrence counts all distinct free endpoints and every actual relation preserves the column, so the individual bounds remain valid after taking the original group quotient.

Set \(H=BB^*\), \(h_1=\mathcal T_2(H)\), \(h_2=\mathcal T_2(H^2)>0\), \(c_\psi=\|R(\psi)p_\psi\|_{\mathrm{HS}}\).
For \(m=1\) the minimum on the right of (4), before multiplying by \(\|R\|^2\), is \(2-h_1^2/h_2\), by minimizing on \(f(x)=1+ux\).
For any feasible five class totals the individual character constraints give \(c_\psi^2\le344\sum_j\|T_j\|_{\mathrm{HS}}^2/k_j\) by weighted Cauchy--Schwarz, omitting empty classes.
Summing the squared character constraints and applying finite Fourier orthogonality bounds their sum by \(5\sum_j\|T_j\|_{\mathrm{HS}}^2\), at most \(400\) times the same objective.
In particular half nullity requires the following inequality involving only two positive moments:
\[
 \|R\|^2\left(2-\frac{h_1^2}{h_2}\right)
 \ \ge\ \max\left\{\frac{\max_\psi c_\psi^2}{344},
                    \frac{\sum_\psi c_\psi^2}{400}\right\}.        \tag{5}
\]
The coefficient sum \(\sum_g\|R(g)\|_{\mathrm{op}}\) can again replace the unknown regular norm as an upper bound.
Solving (3) using the five individual counts can strengthen (5).

## The singular gap of the full row

If \((BB^*)^{-1}\) belonged to \(M_2(\ell^1(N))\), then \(B^\dagger=B^*(BB^*)^{-1}\) would give \(R=RB^\dagger B\) in that convolution algebra.
Indeed \(I-B^\dagger B=P\) as affiliated operators and \(RP=0\), and the regular representation is faithful on \(\ell^1\).
Evaluation at a visible \(\psi\) would force \(\operatorname{rank}R(\psi)\le2\).
Thus the positive two-square inverse is not in \(M_2(\ell^1(N))\).
The same factorization excludes an entrywise summable \(B^\dagger\).

Write \(\beta=\|B\|\), \(\alpha=\inf\sigma((BB^*)^{1/2})\).
For \(0<\alpha<\beta\), the [Chebyshev residual](Yin_C_A0349_v1.md#the-size-of-a-positive-regular-gap) on \([\alpha^2,\beta^2]\) gives polynomials of degree at most \(n-1\) approximating \((BB^*)^{-1}\) in regular norm to within \(2\alpha^{-2}\theta^n\), \(\theta=(\beta-\alpha)/(\beta+\alpha)\).
The row entries have support in \(m_0 V_0\), where \(m_0=(st)^{-1}\) and \(V_0\) is the [symmetric eight-label set](Yin_C_A0350_v1.md#the-growth-of-the-eight-group-labels).
The differences of successive polynomials have support in the \(m_0\)-conjugate of its radius \(2n\) ball, with exponential growth rate at most \(\rho=3+2\sqrt3\) per unit radius.
Cauchy--Schwarz bounds their entrywise \(\ell^1\) norms by a constant times the square root of that ball size times \(\theta^n\).
If \(\rho\theta<1\), their summable differences give an entrywise \(\ell^1\) inverse, a contradiction.
Thus \(\alpha/\beta\le(\rho-1)/(\rho+1)=\sqrt3-1\).
If \(\alpha=\beta>0\) the inverse is constant and already excluded; \(\alpha=0\) satisfies the bound directly.
This joint-row test applies to \(DD^*+EE^*\) and does not require an \(\ell^1\) idempotent trace assumption.

## Assessment history

### Decision endpoints-and-the-joint-two-row-return-moments

| Field | Value |
| --- | --- |
| date | 2026-11-28T12:04 |
| status | proved |
| reason | A common kernel projection controls the same-time inverse residual. Five character constraints yield finite return inequalities and a singular gap obstruction for the full row. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Same-time regularization, scalar diffusion, and the full-row tests. |
| argument | [Bounded residuals built from the same-time inverse](#bounded-residuals-built-from-the-same-time-inverse) | Regular decay and visible rank at one common time. |
| argument | [The chosen second inverse on actual endpoints](#the-chosen-second-inverse-on-actual-endpoints) | Moving supports, residue sums and cancellation of same-endpoint products. |
| argument | [A finite comparison using all five characters](#a-finite-comparison-using-all-five-characters) | The character energy minimum and the regular two-row moment bound. |
| argument | [A degree-one test on the eight group labels](#a-degree-one-test-on-the-eight-group-labels) | The five original marking classes and the degree-one variance bound. |
| argument | [The singular gap of the full row](#the-singular-gap-of-the-full-row) | Convolution inversion and the positive full-row singular spectrum. |
| dependency | [Two actual inverses and the formal remainder](Yin_C_A0344_v2.md#two-actual-inverses-and-the-formal-remainder) | The actual zero remainder and the visible numerical rank excess. |
| dependency | [Selecting and approximating one actual scalar inverse](Yin_C_A0350_v1.md#selecting-and-approximating-one-actual-scalar-inverse) | Choice and regularization of a nonsummable second pivot inverse. |
| dependency | [The growth of the eight group labels](Yin_C_A0350_v1.md#the-growth-of-the-eight-group-labels) | Support of the compressed blocks and the original word growth bound. |
| dependency | [The size of a positive regular gap](Yin_C_A0349_v1.md#the-size-of-a-positive-regular-gap) | Chebyshev residual on an interval of positive singular squares. |
| dependency | [Christoffel variational principle](../audits/literature/Sim08/Yin_U001.md#sim08-u001) | The polynomial minimum at a specified point for a finite spectral measure. |
| review | [Endpoints and the joint two-row return moments](../audits/reviews/Yin_R_A0245_v1.md#endpoints-and-the-joint-two-row-return-moments) | Independent review of the complete fixed statement and proof at the indicated interfaces. |

## Current assessment

[Selected decision](#decision-endpoints-and-the-joint-two-row-return-moments)

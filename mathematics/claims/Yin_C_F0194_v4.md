---
author: Yin
---

# Unary oscillation in low-matching Wigner cofactor events

This version refines the low-matching branch of the [accepted many-index reduction](Yin_C_F0194_v3.md#decision-many-index-reviewed).
It retains the tiny determinant-ratio intersection and removes an additional branch with many oscillating unary terms.
The [independent complete review](../audits/reviews/Yin_R_F0200_v4.md#finding) checks this version's new proof and its exact input interfaces.
The original general finite-variance [Brown](../tasks/Yin_T_F0012_v3.md#contract), [matrix determinant](../tasks/Yin_T_F0013_v1.md#contract) and [scalar determinant](../tasks/Yin_T_F0014_v1.md#contract) contracts remain unresolved.

<a id="statement"></a>
## Complete model and assertions

Fix a real law xi with \(\mathbb E\xi=0\) and \(\mathbb E\xi^2=1\).
For each n, let W_n be real symmetric with independent strict-upper entries distributed as \(\xi/\sqrt n\), mirrored lower entries, and independent real diagonal entries independent of that off-diagonal family.
The diagonal laws can be arbitrary and vary with n unless a further assumption is stated.
Let F be an arbitrary deterministic complex n-by-n matrix and put \(M:=W_n+F\).
An independent random F is allowed by conditioning within this dimension.
All norms are operator or Euclidean unless marked by the unnormalized Frobenius subscript F.
All ranks are over C and \(\operatorname{sym}A:=(A+A^T)/2\) uses transpose.

For each i, delete row and column i to obtain \(D_i\), and put
\[
 A_i:=\operatorname{adj}D_i,\qquad Q_i:=\operatorname{sym}A_i.
\]
Use the constants \(a,\delta,c,C_0,C_1,c_*>0\) of C_F0194_v3.
For \(K\ge0\) and \(0\le\varepsilon\le a/(4\sqrt n)\), define
\[
 E_n(K,\varepsilon):=
 \{\|M\|\le n^K,\ \operatorname{rank}M\ge n-1,\
                         s_{\min}(M)\le\varepsilon\},
\]
\[
 \rho:=C_1n^{2K+1}\varepsilon,\qquad
 G_i(K,\varepsilon):=
       \{A_i\ne0,\ |\det M|/\|A_i\|_F\le\rho\}.
\]
The ratio is used only on \(A_i\ne0\).

For \(h>0\) and \(2\le r\le\lfloor(n-1)/2\rfloor\), let \(H_i(h,r)\) be the event that \(A_i\ne0\) and the graph on the retained n-1 indices with edges
\[
 |(Q_i)_{jk}|\ge h\|A_i\|_F,\qquad j\ne k,
\]
has a matching of at least r edges.
When \(A_i\ne0\) but \(H_i(h,r)\) fails, choose a maximal matching by a fixed greedy order on edges, and let \(S_i\) be its endpoint set.
Then \(|S_i|<2r\), and \(S_i\) covers every threshold edge.
Put \(T_i:=([n]\setminus\{i\})\setminus S_i\).
No graph or cover is assigned to \(A_i=0\).

Place index i first and write the border as
\[
 M=\begin{pmatrix}a_i&(x/\sqrt n+f_i)^T\\
                         x/\sqrt n+g_i&D_i\end{pmatrix},
\]
where x has independent raw coordinates of law xi, \(a_i:=M_{ii}\), and f_i,g_i are the deterministic complex row and column shifts.
They can differ.
Condition on \(D_i,a_i\), and, on the nonzero-adjugate low-matching branch, also on \(y:=x_{S_i}\).
For j in T_i define
\[
 q_{i,j}:=-\frac{(Q_i)_{jj}}n,\qquad
 l_{i,j}(y):=-\frac{(A_ig_i+A_i^Tf_i)_j}{\sqrt n}
                   -\frac2n\sum_{k\in S_i}(Q_i)_{jk}y_k.
\]
If the support of xi contains at least three points, set
\[
 w_{i,j}(y):=\max(|q_{i,j}|,|l_{i,j}(y)|).
\]
If it consists of exactly two distinct values u,v, set instead
\[
 w_{i,j}(y):=|l_{i,j}(y)+(u+v)q_{i,j}|.
\]
These cases exhaust the fixed variance-one law.
For a relative scale \(\lambda>0\), define
\[
 N_{i,\lambda}:=
 \#\{j\in T_i:w_{i,j}(x_{S_i})\ge\lambda\|A_i\|_F\}.
\]
This count is used only on its defined nonzero-adjugate low-matching branch.
All selected covers, counts and the events below are measurable in the actual matrix entries and F.

There are constants \(c_0,c_u,C>0\), depending only on xi, such that the following assertions hold.
Put
\[
 \chi(s):=e^{-c_us}+s^{-1/2},\qquad
 \psi(r):=e^{-c_*r}+\sqrt{\log(2+r)}\,r^{-1/9}.
\]

### Unary sums

For any finite independent family xi_j with this law and deterministic complex coefficients q_j,l_j, define \(Z_j:=q_j\xi_j^2+l_j\xi_j\).
Use \(w_j:=\max(|q_j|,|l_j|)\) for a law with at least three support points and \(w_j:=|l_j+(u+v)q_j|\) for a two-point law.
If at least \(s\ge2\) indices have \(w_j\ge t>0\), then
\[
 \sup_{z\in\mathbb C}
 \mathbb P\left\{\left|\sum_j Z_j-z\right|\le c_0t\right\}
 \le C\chi(s).
 \tag{Unary-sum-bound}
\]
The number of variables is any finite integer at least s.
No moment assumption is needed for this auxiliary assertion beyond the fixed law's stated nondegeneracy.

### Conditional low-matching bound

On the nonzero-adjugate low-matching branch, if \(N_{i,\lambda}\ge s\) and \(0\le\rho\le c_0\lambda/2\), then
\[
 \mathbb P\{|\det M|\le\rho\|A_i\|_F
                 \mid D_i,a_i,x_{S_i}\}
 \le C\chi(s)+C(h/\lambda)^2.
 \tag{Low-matching-unary}
\]
This conditional assertion holds wherever \(2\le s\le n-1\) and the indicated count condition holds, in the usual almost-everywhere sense for conditional laws.
If fewer than s indices remain in T_i, the count condition is empty.

For a law with at least three support points, the minor condition
\[
 \#\{j\in T_i:|(Q_i)_{jj}|\ge n\lambda\|A_i\|_F\}\ge s
 \tag{Large-diagonal-branch}
\]
implies the count condition for every x_{S_i}.
For a two-point law the effective coefficient above, including the factor u+v, is essential.
In the symmetric Rademacher case u+v=0 and every diagonal quadratic term is constant.

### Refined many-index average

For all sufficiently large n, every K and epsilon in the stated range, \(h,\lambda>0\), and integers
\[
 2\le r\le\lfloor(n-1)/2\rfloor,\qquad 2\le s\le n-1,
\]
if
\[
 C_1n^{2K+1}\varepsilon\le\min(c_*h/n,c_0\lambda/2),
\]
then
\[
 \begin{split}
 \mathbb P(E_n(K,\varepsilon))
 \le{}&C_0e^{-cn}
       +C\left[\psi(r)+\chi(s)+(h/\lambda)^2\right]\\
 &+\frac Cn\sum_{i=1}^n
 \mathbb P\{G_i(K,\varepsilon)\cap H_i(h,r)^c
                              \cap\{N_{i,\lambda}<s\}\}.
 \end{split}
 \tag{Refined-average-bound}
\]
The last event uses N only on its defined branch because G_i requires a nonzero adjugate.
The sufficiently large dimension may depend on K, as in C_F0194_v3.
All constants are uniform over the arbitrary complex shift and diagonal law in this norm-guarded assertion.
The entire bound holds after integrating any independent random shift.
No independence among minor events or between physical dimensions is assumed.

<a id="polynomial-shift-consequence"></a>
### Polynomial-shift consequence

Assume additionally that the diagonal entries of W_n are independent copies of \(\zeta/\sqrt n\), for a fixed real law zeta with finite second moment.
The law need not be centered.
For every \(\gamma,B>0\) there is \(K>0\), depending only on these fixed laws and exponents, with the following property.
Let F_n be independent of W_n and define
\[
 \Gamma_n:=\{\max_{j,k}|(F_n)_{jk}|\le n^\gamma\}.
\]
Choose fixed exponents \(H>L\ge0\) and \(A>H+2K+2\).
For all deterministic integer sequences
\[
 2\le r_n\le\lfloor(n-1)/2\rfloor,\qquad
 2\le s_n\le n-1,
\]
the matrices \(M_n:=W_n+F_n\) satisfy
\[
 \begin{split}
 \mathbb P\{s_{\min}(M_n)\le n^{-A}\}
 \le{}&C_Bn^{-B}+\mathbb P(\Gamma_n^c)\\
 &+C\left[\psi(r_n)+\chi(s_n)+n^{-2(H-L)}\right]\\
 &+\frac Cn\sum_i\mathbb P\left\{
 G_i(K,n^{-A})\cap H_i(n^{-H},r_n)^c
 \cap\{N_{i,n^{-L}}<s_n\}\cap\Gamma_n\right\}
 \end{split}
 \tag{Polynomial-refinement}
\]
for all sufficiently large n.
The counts in this formula use \(h=n^{-H}\).
Constants and the dimension threshold may depend on the laws and fixed exponents, but not on the law or realization of the independent shift.
The terminal mean is not shown to vanish.
If r_n and s_n tend to infinity and that mean and \(\mathbb P(\Gamma_n^c)\) tend to zero, the left side tends to zero.
No summability follows solely from these conditions.

### Conditional Rademacher obstruction

For every odd \(n=2q+1\), \(q\ge2\), there is a deterministic invertible minor D with
\[
 \|D\|=3,\qquad s_{\min}(D)=s_{\min}(\operatorname{sym}D)=1,
 \qquad \|Q\|_F/\|\operatorname{adj}D\|_F=1/\sqrt5,
\]
whose Q has full spectral rank and no off-diagonal edge at any positive threshold.
For a normalized independent Rademacher border with zero diagonal and shifts, the full matrix has norm less than four and exactly corank one, and its determinant ratio is zero with conditional probability one.
The explicit matrices and calculation appear in the proof.
This rejects a conditional bound based only on those minor norm, rank and diagonal scales.
It supplies neither an unconditional probability obstruction for actual Wigner minors nor a statement about the other omitted indices of that bordered matrix.

## Exact accepted inputs

[C_F0194_v3 statement](Yin_C_F0194_v3.md#statement) supplies its exact real normalized model, many-index constants, ratio and matching events, and uniform random-shift scope.
[C_F0194_v3 argument](Yin_C_F0194_v3.md#argument) supplies only its accepted pointwise many-index average, degree-two matching estimate, and polynomial norm/corank exception bounds.
Those inputs are reused at their actual scopes; none supplies a review of this version's new deduction.

[MNV16-U001](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) supplies Definition 1.5 and Theorem 1.6 in the 2016 Theory of Computing edition, PDF p. 3, with polynomial conventions on p. 2.
At degree one its second bound gives rank to the power -1/2 because \(\log1=0\).
The coefficients are real, the variables are independent fair signs, and the interval has length one with arbitrary center.
Its source proof and external dependencies are accepted without a new full audit.
The source does not directly state the complex unary-sum or conditional low-matching assertions proved below.

<a id="argument"></a>
## Complete unary and low-matching proof

<a id="unary-oscillation"></a>
### A finite-scale bound for independent unary sums

For the fixed real law xi, exactly one of the following two cases applies.

If its support contains at least three points, there are constants \(\kappa,p>0\) such that every \(q,l\in\mathbb C\) satisfies
\[
 \mathbb P\{|q(\xi^2-(\xi')^2)+l(\xi-\xi')|
       \ge \kappa\max(|q|,|l|)\}\ge p
 \tag{Three-point}
\]
whenever \((q,l)\ne(0,0)\), with xi' an independent copy.
Choose three distinct finite support points \(t_0,t_1,t_2\).
The matrix with rows
\[
 (t_1^2-t_0^2,t_1-t_0),\qquad
 (t_2^2-t_0^2,t_2-t_0)
\]
is invertible.
Its least singular value gives a uniform positive lower bound for at least one of the two polynomial differences when \(\max(|q|,|l|)=1\).
Choose small disjoint neighborhoods of the three points so this lower bound persists, uniformly over those normalized complex coefficients.
Each neighborhood has positive xi-probability.
The probability of the relevant ordered pair of neighborhoods is bounded below by their minimum probability product.
Scaling the coefficients proves (Three-point).
The matrix acts on complex coefficient pairs as well as real pairs; no nondegenerate covariance in a two-dimensional real plane is required.

If the law is supported on exactly two distinct real values u,v with respective probabilities \(\theta,1-\theta\), then
\[
 \xi^2=(u+v)\xi-uv\quad\text{almost surely},
\]
and
\[
 q\xi^2+l\xi=(l+(u+v)q)\xi-uvq.
 \tag{Two-point}
\]
Thus the effective coefficient is \(l+(u+v)q\).
The difference between two independent copies has modulus
\[
 |u-v|\,|l+(u+v)q|
\]
with probability \(2\theta(1-\theta)>0\).
For symmetric Rademacher inputs u+v=0, so the entire quadratic diagonal is constant.

Let \(Z_j:=q_j\xi_j^2+l_j\xi_j\) for independent copies xi_j and arbitrary deterministic complex coefficients.
Define
\[
 w_j:=
 \begin{cases}
 \max(|q_j|,|l_j|),&\text{if the support has at least three points},\\
 |l_j+(u+v)q_j|,&\text{if the support is }\{u,v\}.
 \end{cases}
\]
For \(s\ge2\), if at least s indices satisfy \(w_j\ge\lambda>0\), then
\[
 \sup_{z\in\mathbb C}
 \mathbb P\left\{\left|\sum_j Z_j-z\right|\le c_0\lambda\right\}
 \le C\left[e^{-cs}+s^{-1/2}\right]
 =:C\chi(s).
 \tag{Unary-sum}
\]
Here \(c_0,c,C>0\) depend only on xi and the fixed constants in the accepted MNV16 theorem.

For completeness, take independent copies \(Z_j^{(0)},Z_j^{(1)}\) and independent fair signs epsilon_j.
The variables
\[
 (Z_j^{(0)}+Z_j^{(1)})/2
 +(Z_j^{(0)}-Z_j^{(1)})\varepsilon_j/2
\]
have exactly the original independent laws.
The preceding oscillation estimate and an exponential indicator bound give at least cs sign coefficients of modulus at least c lambda, except with probability \(Ce^{-cs}\).
At least half of those coefficients have one common real or imaginary projection of modulus at least c lambda.
Conditioning on all copies leaves a real linear polynomial of independent fair signs.
After dividing by that coefficient scale, the projected disk of radius \(c_0\lambda\) lies in an interval of length strictly less than one when \(c_0\) is sufficiently small.
The second bound of MNV16 at degree one supplies the reciprocal square root of the actual rank.
That rank is at least a fixed multiple of s, and a larger constant handles the remaining bounded ranks and small s.
Integrating the copies proves (Unary-sum).
No moments are required by this unary-sum argument itself.

<a id="low-matching-decomposition"></a>
### Actual border decomposition on a low-matching minor

Fix i, condition on \(D:=D_i\) and the exposed diagonal a, and assume \(A:=\operatorname{adj}D\ne0\).
Let \(m:=n-1\), \(Q:=(A+A^T)/2\), and let the actual raw off-diagonal row be x with independent coordinates of law xi.
Write the row and column shifts as f,g, so
\[
 P(x):=\det M
 =a\det D-f^TAg-\frac{x^T(Ag+A^Tf)}{\sqrt n}
                      -\frac{x^TQx}{n}.
 \tag{Border}
\]
This uses transpose, not adjoint, and f,g may differ.

Suppose the graph \(|Q_{jk}|\ge h\|A\|_F\), \(j\ne k\), has no matching of size r.
Choose a maximal matching by a fixed finite greedy order and let S be its endpoints.
Then \(|S|<2r\), and S covers every threshold edge.
The choice is Borel in D.
Put \(T:=[m]\setminus S\).
Condition additionally on the actual values \(y:=x_S\).
For j in T define
\[
 q_j:=-Q_{jj}/n,\qquad
 l_j(y):=-\frac{(Ag+A^Tf)_j}{\sqrt n}
                    -\frac2n\sum_{k\in S}Q_{jk}y_k,
\]
and
\[
 b(y):=a\det D-f^TAg
 -\frac{y^T(Ag+A^Tf)_S}{\sqrt n}
 -\frac{y^TQ_{SS}y}{n}.
\]
The exact decomposition is
\[
 P(x)=b(y)+\sum_{j\in T}(q_jx_j^2+l_j(y)x_j)+R(x_T),
 \qquad
 R(x_T):=-\frac2n\sum_{\substack{j<k\\j,k\in T}}Q_{jk}x_jx_k.
 \tag{Core}
\]

Conditional on D,a,y, the variables x_T remain independent copies of xi.
This follows separately on each of the finitely many possible S selected from D.
It does not condition on a row-dependent choice of cover.

Distinct unordered pairs give orthogonal products \(x_jx_k\) in L2.
For pairs sharing one index, their product has expectation \(\mathbb E\xi^2(\mathbb E\xi)^2=0\); for disjoint pairs, independence and centering also give zero.
The diagonal second moments are \(\mathbb E(x_j^2x_k^2)=1\).
All these expectations exist with only finite second moments: a shared index has exponent two and every other index has exponent one.
Consequently
\[
 \mathbb E(|R|^2\mid D,a,y)
 =\frac4{n^2}\sum_{\substack{j<k\\j,k\in T}}|Q_{jk}|^2
 \le2h^2\|A\|_F^2.
 \tag{Remainder-L2}
\]
The constant has no dimension factor.
Neither a fourth moment nor a raw-entry cutoff is used.

<a id="conditional-unary-bound"></a>
### Conditional low-matching and tiny-ratio estimate

Use the appropriate effective weights w_j from (Unary-sum), with the coefficients q_j,l_j(y) in (Core).
For a relative scale \(\lambda>0\), define the measurable count
\[
 N_\lambda(D,y):=\#\{j\in T:w_j\ge\lambda\|A\|_F\}.
\]
In the two-point case this is explicitly the count of
\[
 \left|
 -\frac{(Ag+A^Tf)_j}{\sqrt n}
 -\frac2n\sum_{k\in S}Q_{jk}y_k
 -\frac{(u+v)Q_{jj}}n
 \right|\ge\lambda\|A\|_F.
 \tag{Effective-slope}
\]
In particular it retains every possible Rademacher cancellation.

If \(N_\lambda(D,y)\ge s\ge2\) and \(0\le\rho\le c_0\lambda/2\), then
\[
 \mathbb P\{|\det M|\le\rho\|A\|_F\mid D,a,y\}
 \le C\chi(s)+C(h/\lambda)^2.
 \tag{Conditional-unary}
\]
Indeed Chebyshev and (Remainder-L2) give
\[
 \mathbb P\{|R|>(c_0\lambda/2)\|A\|_F\mid D,a,y\}
 \le 8c_0^{-2}(h/\lambda)^2.
\]
On its complement the tiny determinant event puts the independent unary sum in a disk of radius at most \(c_0\lambda\|A\|_F\), centered at \(-b(y)\).
Apply (Unary-sum) at scale \(\lambda\|A\|_F\).
No independence between R and that sum is claimed or needed.

For a law with at least three support points, the sufficient condition
\[
 \#\{j\in T:|Q_{jj}|\ge n\lambda\|A\|_F\}\ge s
 \tag{Large-diagonal}
\]
implies \(N_\lambda(D,y)\ge s\) for every y.
Thus (Conditional-unary) genuinely removes this large-diagonal low-matching branch, regardless of all complex lower terms.
For a two-point law, replace it by the actual effective-slope count.
A claim based only on \(|Q_{jj}|\) would be false.

<a id="averaged-refinement"></a>
### Refinement of the accepted many-index probability reduction

Retain K,epsilon and the norm/rank event \(E_n(K,\varepsilon)\) from C_F0194_v3, and put \(\rho:=C_1n^{2K+1}\varepsilon\).
For each nonzero-adjugate low-matching minor choose S_i and define \(N_{i,\lambda}:=N_\lambda(D_i,x_{S_i})\).
No graph or ratio is assigned when \(A_i=0\); that case is already absent from \(G_i\).
If
\[
 \rho\le\min(c_*h/n,c_0\lambda/2),
\]
then, for \(r,s\ge2\),
\[
 \begin{split}
 \mathbb P(E_n(K,\varepsilon))
 \le{}&C_0e^{-cn}
 +C\left[\psi(r)+\chi(s)+(h/\lambda)^2\right]\\
 &+\frac Cn\sum_{i=1}^n
 \mathbb P\{G_i(K,\varepsilon)\cap H_i(h,r)^c
                            \cap\{N_{i,\lambda}<s\}\}.
 \end{split}
 \tag{Refined-average}
\]
In the last line the event includes \(A_i\ne0\) through G_i, so the partial definition of the count causes no ambiguity.
The matching part uses the accepted C_F0194_v3 conditional bound.
The low-matching part with a large unary count uses (Conditional-unary), integrated over D_i,a and x_{S_i}.
The remaining part is retained with its actual tiny-ratio intersection.
Finally use the accepted pointwise many-index average.
This uses no independence among minor events.

For the polynomial-shift model, restore the accepted norm and corank exceptions on Gamma_n.
Choose \(h=n^{-H}\), \(\lambda=n^{-L}\), fixed \(H>L\ge0\), and \(A>H+2K+2\).
The matching-radius inequality then implies the unary-radius inequality eventually.
For any allowed growing matching sizes r_n and unary counts s_n, the new error is
\[
 C\psi(r_n)+C\chi(s_n)+Cn^{-2(H-L)}.
\]
The terminal mean is
\[
 \frac Cn\sum_i\mathbb P\left\{
 G_i(K,n^{-A})\cap H_i(n^{-H},r_n)^c
 \cap\{N_{i,n^{-L}}<s_n\}\cap\Gamma_n\right\}.
\]
Add \(C_Bn^{-B}+\mathbb P(\Gamma_n^c)\).
This is a candidate quantitative improvement over the unconditioned low-matching mean.
It does not prove that its new terminal mean vanishes.

<a id="rademacher-conditional-obstruction"></a>
### A well-conditioned Rademacher obstruction to conditional diagonal reasoning

For every q>=1, put \(n:=2q+1\) and
\[
 B:=\begin{pmatrix}1&2\\-2&-1\end{pmatrix},
 \qquad D:=\operatorname{diag}(B,\ldots,B).
\]
Then \(\det B=3\), \(\|D\|=3\), \(s_{\min}(D)=1\), and \(\operatorname{sym}D\) is diagonal with entries alternating 1 and -1, so its least singular value is also one.
Its adjugate and symmetric adjugate are
\[
 A=3^qD^{-1},\qquad
 Q=3^{q-1}\operatorname{diag}(-1,1,\ldots,-1,1).
\]
Thus Q has full spectral rank and no off-diagonal matching edge, while
\[
 \|A\|_F=3^{q-1}\sqrt{10q},\qquad
 \|Q\|_F/\|A\|_F=1/\sqrt5.
\]
Let x have independent symmetric Rademacher coordinates and set
\[
 M(x):=\begin{pmatrix}0&x^T/\sqrt n\\x/\sqrt n&D\end{pmatrix}.
\]
The determinant is identically zero:
\[
 \det M(x)=-x^TQx/n
 =-\frac{3^{q-1}}n\sum_{\ell=1}^q
              (-x_{2\ell-1}^2+x_{2\ell}^2)=0.
\]
Since D is invertible, M(x) has exactly corank one.
Also \(\|M(x)\|\le3+\sqrt{(n-1)/n}<4\).
For the exposed top row all effective unary slopes vanish and every diagonal term is constant.
Hence tiny ratio and low matching occur with conditional probability one, despite fixed norm bounds, a well-conditioned invertible D, a well-conditioned symmetric part and a substantial full-rank Q.

This is a deterministic conditional-minor obstruction, not an unconditional probability counterexample for Wigner plus an independent shift.
It supplies no lower bound for the probability that an actual Wigner minor equals this D.
It also says nothing about matching or usable cofactors at the other omitted indices of M(x).
Therefore independent Wigner structure, interactions between omitted indices, or the particular product-inverse shift can still remove the terminal mean in (Refined-average).
A bound depending only on the displayed conditional norm, rank and diagonal scales cannot do so.

### Remaining question and actual scope

The new candidate bound handles many oscillating diagonal entries for laws with at least three support points and many effective linear coefficients for all laws.
Its remainder estimate uses precisely centering and second moments, without density, a fourth moment or a hidden cutoff.
The remaining task is to estimate the actual-minor terminal event with too few effective unary coefficients, retaining its tiny-ratio intersection, or find a useful interaction between different principal indices.
No full nonsymmetric-shift least-singular-value floor, matrix-coefficient-pencil theorem or completion of the original contracts is asserted.

## Current assessment
[Selected decision](#decision-unary-reviewed)

## Assessment history

### Decision unary-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T10:51 |
| status | open |
| reason | The complete unary-oscillation, conditional low-matching and refined many-index deductions are fixed for fresh independent review, with the terminal tiny-ratio and low-unary-count mean retained and no least-singular-value floor or original Task completion asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete unary and low-matching assertions](#statement) | Exact support-sensitive unary weights, complex independent unary sums, measurable low-matching cover conditioning, finite-second-moment remainder, refined average, independent random shifts, polynomial consequence and conditional Rademacher obstruction. |
| argument | [Complete candidate proof](#argument) | Three-point support matrix, exact two-point identity, sign representation and degree-one source bound, exact normalized bordered decomposition, pairwise L2 orthogonality, conditional estimate, refined average, polynomial norm/corank interfaces and full explicit counterexample. |
| dependency | [Accepted many-index statement](Yin_C_F0194_v3.md#statement) | Only its exact real normalized model, constants, pointwise-many-index probability consequence, degree-two matching theorem and uniform independent-shift scope. |
| dependency | [Accepted many-index argument](Yin_C_F0194_v3.md#argument) | Only the established pointwise cofactor average, normalized degree-two matching estimate and finite-second-moment polynomial norm/corank exception bounds; no earlier review is inherited for this new proof. |
| dependency | [Exact degree-one source input](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Definition 1.5 and Theorem 1.6 in the selected 2016 journal edition, degree one, real multilinear fair-sign polynomial and length-one intervals; its second bound specializes to rank to the power -1/2, with original source proof accepted externally. |

### Decision unary-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T10:59 |
| status | proved |
| reason | A fresh independent whole-proof review verifies the support-sensitive unary bound, finite-second-moment remainder, actual low-matching conditioning, refined average, polynomial-shift consequence and conditional Rademacher obstruction with all declared input interfaces. The remaining tiny-ratio, low-matching, low-unary-count mean is not estimated. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete unary and low-matching assertions](#statement) | Exact support-sensitive unary weights, complex independent unary sums, measurable low-matching cover conditioning, finite-second-moment remainder, refined average, independent random shifts, polynomial consequence and conditional Rademacher obstruction. |
| argument | [Complete candidate proof](#argument) | Three-point support matrix, exact two-point identity, sign representation and degree-one source bound, exact normalized bordered decomposition, pairwise L2 orthogonality, conditional estimate, refined average, polynomial norm/corank interfaces and full explicit counterexample. |
| dependency | [Accepted many-index statement](Yin_C_F0194_v3.md#statement) | Only its exact real normalized model, constants, pointwise-many-index probability consequence, degree-two matching theorem and uniform independent-shift scope. |
| dependency | [Accepted many-index argument](Yin_C_F0194_v3.md#argument) | Only the established pointwise cofactor average, normalized degree-two matching estimate and finite-second-moment polynomial norm/corank exception bounds; no earlier review is inherited for this new proof. |
| dependency | [Exact degree-one source input](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Definition 1.5 and Theorem 1.6 in the selected 2016 journal edition, degree one, real multilinear fair-sign polynomial and length-one intervals; its second bound specializes to rank to the power -1/2, with original source proof accepted externally. |
| review | [Independent unary and low-matching review](../audits/reviews/Yin_R_F0200_v4.md#finding) | Complete statement and argument, all three declared dependency interfaces, normalization, measurability, support cases and explicit conditional obstruction; no unresolved mathematical or source-applicability gap in this exact scope. |

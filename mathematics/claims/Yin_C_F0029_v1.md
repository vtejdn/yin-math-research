---
author: Yin
---

# Full affiliated criterion on dense left-module dual and adjoint test domains

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Duals on Dense Left-Module Domains

<a id="statement"></a>

<a id="yin_c_f0029"></a>
## Yin_C_F0029: A Full Affiliated Criterion on Dense Left Modules

Date: 2026-09-10.
Authorization: the user requested a further weakening of dual domains that supports the full main theorem, rather than only a polynomial-core implication.
Human author: Yin.
Proof development: another AI agent, developing the local-module proposal of root.
The good-window construction and general-left-module refinement were proposed by another AI agent and root and separately checked by the author.
The short projection-extraction and dense-restriction cancellation arguments were supplied by the author and separately checked within the team.
The strict noncommuting example was proposed by another AI agent and checked by root and the author.
These preliminary contributions are disclosed separately from the later complete-artifact review.
The [selected assessment](#current-assessment) records the mathematical and review assessments; no historical-priority, formal-verification, or external human-review claim is made.

This theorem proves the full affiliated finite-defect criterion on arbitrary dense left modules.
It needs neither all bounded vectors in the dual domains nor invariance under bounded right multipliers.
A left module containing the vacuum vector necessarily contains all of \(M\), so a strict weakening of that inclusion has a different domain geometry from an intermediate algebra containing the starred polynomial core.

## 1. Exact Hypotheses and Conclusions

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, let \(H=L^2(M,\tau)\), and set \(\Omega=1\), \(P=P_\Omega\).
Use the inner product linear in its second variable.
Write \(\lambda(a)\) and \(\rho(a)\) for bounded left and right multiplication by \(a\in M\), suppressing \(\lambda\) in products.
Let \(X=(X_1,\ldots,X_d)\) be a bounded normal tuple with \(M=W^*(X)\).

Let \(\mathcal E\subseteq H\) be a dense complex-linear left \(M\)-module:
\[
M\mathcal E\subseteq\mathcal E.
\tag{1}
\]
For each \(i\), let \(V_i\subseteq H\) be another dense complex-linear left \(M\)-module.
Suppose complex-linear operators \(D_{i,0}\), with domain exactly \(\mathcal E\), satisfy
\[
V_i\subseteq\operatorname{Dom}D_{i,0}^*,\qquad
D_{i,0}(X_jz)-X_jD_{i,0}z
=\delta_{ij}\langle\Omega,z\rangle\Omega
\quad(z\in\mathcal E).
\tag{2}
\]
Then \(D_{i,0}\) is closable; write \(D_i=\overline{D_{i,0}}\).

No inclusion \(\mathcal E\subseteq M\), vacuum-domain assumption, right invariance, projection exhaustion, adjoint-generator commutator bound, or infinity-to-\(L^2\) estimate is imposed.
The test modules \(V_i\) may differ and need not consist of bounded vectors.

Put
\[
U=U(M),\qquad
A=\mathbb C\langle X_1,\ldots,X_d\rangle,\qquad
F=\operatorname{Div}_U A.
\tag{3}
\]
Generator adjoints are not adjoined to \(A\) in this rationality conclusion.

Then:

1. \(\Delta(X)=d\), and the accepted MSY23 theorem identifies \(F\) with the embedded free skew field.
2. For every \(u\in U\), take any bounded fractions
   \[
   u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,\quad s,t\text{ regular}.
   \tag{4}
   \]
   Regular means invertible in \(U\), equivalently bounded injective with dense range on \(H\).
   The cleared defects
   \[
   T_i z=sD_{i,0}(bz)-aD_{i,0}(tz),\qquad z\in\mathcal E,
   \tag{5}
   \]
   are well-defined.
   One has \(u\in F\) if and only if all these defects have finite-dimensional range, for some, equivalently every, fraction pair (4).
   Every finite-rank defect has a unique bounded finite-rank extension to \(H\).
   Its finite numerical rank is independent of the fraction pair.
3. For bounded elements,
   \[
   F\cap M
   =\{f\in M:[D_{i,0},f]|_{\mathcal E}
       \text{ has finite rank for every }i\}.
   \tag{6}
   \]
   Equivalently, \(f\) preserves every full closed domain \(\operatorname{Dom}D_i\), and each \([D_i,f]\) there is the restriction of a bounded finite-rank operator.

Choosing \(\mathcal E=V_i=M\) recovers Yin_C_F0024.
Allowing arbitrary \(V_i\) with \(\mathcal E=M\) also covers the one-sided domain form recorded separately in Yin_C_F0030.
Section 8 gives a strictly smaller-domain example for a noncommuting tuple with \(d\geq2\).

## 2. Large Projections and Local Domains Are Automatic

### Projections Inside a Dense Left Module

Choose \(z_n\in\mathcal E\) with \(\|z_n-\Omega\|_2\to0\).
View \(z_n\in H\subset U\), take its affiliated polar decomposition \(z_n=v_n|z_n|\), and put
\[
e_n=1_{[1/2,\infty)}(|z_n|).
\tag{7}
\]
The bounded element
\[
a_n=e_n|z_n|^{-1}v_n^*\in M,\qquad \|a_n\|\leq2,
\]
where the inverse is taken only on the indicated spectral support, satisfies \(a_nz_n=e_n\).
Hence \(e_n\in\mathcal E\), and left invariance gives \(Me_n\subseteq\mathcal E\).

Write \(q_n=1-e_n\).
Since \(\|z_nq_n\|_2\leq\frac12\|q_n\|_2\), one has
\[
\|z_n-\Omega\|_2
\geq\|(z_n-\Omega)q_n\|_2
\geq\tfrac12\|q_n\|_2.
\]
Consequently
\[
\tau(1-e_n)\leq4\|z_n-\Omega\|_2^2\longrightarrow0.
\tag{8}
\]
The projections need not be increasing.
They converge strongly to \(1\), in both the left and right actions on \(H\): their \(L^2\) convergence and uniform boundedness first give strong convergence on bounded vectors and then on all of \(H\) by density.
Thus monotonicity or a pre-existing projection exhaustion is unnecessary.

### Windows with the Needed Right Products

For a bounded \(y\in M\), let \(l(y)\) and \(r(y)\) be its left and right support projections.
Finite tracial polar decomposition gives \(\tau(l(y))=\tau(r(y))\).
Define
\[
p_n=e_n\wedge
\bigwedge_{i=1}^d\bigl(1-l(X_i(1-e_n))\bigr).
\tag{9}
\]
Then \(p_n\leq e_n\) and
\[
p_nX_i(1-e_n)=0,\qquad
Mp_nX_i\subseteq Me_n\subseteq\mathcal E.
\tag{10}
\]
Moreover \(r(X_i(1-e_n))\leq1-e_n\), so
\[
\tau(1-p_n)
\leq\tau(1-e_n)+\sum_i\tau(l(X_i(1-e_n)))
\leq(d+1)\tau(1-e_n)\longrightarrow0.
\tag{11}
\]
Here the first bound is the standard finite-trace subadditivity for joins of projections.
Thus \(p_n\to1\) strongly, and the union of the spaces \(Mp_n\) is dense in \(H\).
Neither this union nor the family of windows needs to be increasing.

### Local Closed Graph and Weak Continuity

The dense adjoint test domain \(V_i\) makes \(D_{i,0}\) closable.
For fixed \(n\), \(Me_n\) is a Banach space in operator norm.
The map \(D_{i,0}:Me_n\to H\) has closed graph: operator-norm convergence of inputs implies \(L^2\) convergence, and the Hilbert closure agrees with \(D_{i,0}\) at every vector of \(Me_n\).
Hence there is a finite \(c_{i,n}\) with
\[
\|D_{i,0}z\|_2\leq c_{i,n}\|z\|
\quad(z\in Me_n).
\tag{12}
\]
No uniform bound in \(n\) and no adjoint estimate are asserted.

If \(z_\alpha,z\in Me_n\), \(z_\alpha\to z\) in \(L^2\), and \(\sup_\alpha\|z_\alpha\|<\infty\), then
\[
D_{i,0}z_\alpha\rightharpoonup D_{i,0}z.
\tag{13}
\]
Indeed, pair first against any vector in the dense domain of \(D_{i,0}^*\).
The adjoint identity gives convergence of these pairings, and (12) bounds the images uniformly, extending the convergence to all Hilbert test vectors.

On each window \(Mp_n\), define
\[
R_i=\rho(X_i),\qquad
K_nz=\sum_i\bigl(R_iD_{i,0}z-D_{i,0}(R_iz)\bigr),\qquad
C_n=K_n+P|_{Mp_n}.
\tag{14}
\]
Equation (10) makes every input of \(D_{i,0}\) legitimate.
Both \(z\) and \(zX_i\) lie in \(Me_n\), so (12) shows that \(C_n:Mp_n\to H\) is bounded from operator norm to Hilbert norm.

For an operator-norm-bounded net \(z_\alpha,z\in Mp_n\) converging in \(L^2\), both \(z_\alpha\) and \(z_\alpha X_i\) converge in \(L^2\) within \(Me_n\), with uniform operator-norm bounds.
Applying (13) separately to these inputs yields
\[
C_nz_\alpha\rightharpoonup C_nz.
\tag{15}
\]
This proof needs no closability of \(C_n\), no adjoint formula for \(C_n\), and no right invariance of any \(V_i\).
The local maps agree on their overlapping input domains because they are given by the same displayed formula, but no map on every vector of \(\mathcal E\) is required.

## 3. Maximal Delta on a Dense Left Module

Use the accepted finite-rank-cycle characterization at [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002):
\[
\Delta(X)=d
\quad\Longleftrightarrow\quad
\left[
\sum_i[T_i,X_i]=0,\ T_i\in\operatorname{FinRank}(H)
\ \Longrightarrow\ T_i=0\text{ for all }i
\right].
\tag{16}
\]
This left-multiplication form is equivalent to the source convention by conjugation and adjoints and applies to arbitrary bounded tuples.

Suppose such a cycle is given.
There is a bounded regular \(r\in M\) such that
\[
gr\in M\quad
\text{for every }g\in\sum_i\operatorname{Ran}T_i.
\tag{17}
\]
To see this, write a finite basis \(g_k=b_kt_k^{-1}\), with bounded \(b_k\) and bounded regular \(t_k\).
For two denominators, write the affiliated unit \(t_1^{-1}t_2=pq^{-1}\) with bounded regular \(p,q\), giving \(t_1p=t_2q\).
Induction gives a bounded regular common right multiple \(r=t_kc_k\), and then \(g_kr=b_kc_k\in M\).
These finite-tracial fraction facts are recorded in Yin_C_F0024 and its linked affiliated-operator source inputs.

Put \(Q=\rho(r)\), an injective bounded operator on \(H\).
For arbitrary \(c,\ell\in M\) and every \(n\), use the projections (7) to define
\[
S_i=\rho(c e_n)\,Q\,T_i\,\rho(\ell).
\tag{18}
\]
Each output is of the form \((gr)ce_n\in Me_n\subseteq\mathcal E\).
This multiplication order is essential: no arbitrary right multiplier is applied after a vector has only been placed in \(\mathcal E\).
All right multipliers commute with the left \(X_i\), so the \(S_i\) still satisfy the cycle identity.

Every \(D_{j,0}S_i\) is an everywhere-defined bounded finite-rank operator, obtained by applying \(D_{j,0}\) to a finite basis of \(\operatorname{Ran}S_i\subseteq\mathcal E\).
The same domain observation applies to \(D_{j,0}X_iS_i\) and \(D_{j,0}S_iX_i\), using left invariance of \(\mathcal E\).
Apply \(D_{j,0}\) to the cycle and use (2) to get
\[
0=\sum_i(D_{j,0}S_iX_i-D_{j,0}X_iS_i)
 =\sum_i[D_{j,0}S_i,X_i]-PS_j.
\tag{19}
\]
Only now take the ordinary trace, involving bounded finite-rank operators:
\[
0=\operatorname{Tr}(PS_j)
 =\langle e_nc^*,QT_j\ell\rangle.
\tag{20}
\]
Since \(e_n\to1\) strongly, varying \(n,c\) supplies a dense family of first test vectors.
Varying \(\ell\in M\) supplies an independently dense family of second test vectors.
Thus \(QT_j=0\), and injectivity of \(Q\) gives \(T_j=0\).
This proves \(\Delta(X)=d\).

The accepted [MSY23 free-field equivalence](../audits/literature/MSY23/Yin_U004.md#msy23-u004) identifies \(F\) with the embedded free skew field.
This argument uses neither normality nor an input \(D_{j,0}\Omega\).
It does not trace an uncontrolled unbounded product.

## 4. The Fundamental Identity Is Only Needed Locally

Traciality gives \([R_j,P]=[X_j,P]\).
On the fixed window \(Mp_n\), left multiplication by any \(X_j\) preserves the window, and (10) guarantees that the right products appearing in the commutator expansion lie in \(\mathcal E\).
Thus (2) gives
\[
[K_n,X_j]=[R_j,P]=[X_j,P],\qquad
[C_n,X_j]=0
\quad\text{on }Mp_n.
\tag{21}
\]
For example, the expansion of \([[R_i,D_{i,0}],X_j]z\) uses the dual relation at both \(z\) and \(zX_i\), and equals \([R_i,\delta_{ij}P]z\).
No right invariance of the whole domain is used.

Fix \(n,j\) and write \(x=X_j\).
The local bound in Section 2 makes
\[
\mathcal L(z)=\lambda(e^{zx^*})\,C_n\,\lambda(e^{-zx^*})
\tag{22}
\]
an entire function with values in the Banach space \(B((Mp_n,\|\cdot\|),H)\).
Left multiplication by every element of \(M\) preserves \(Mp_n\).
Equation (21) and convergence of exponential series imply that \(C_n\) intertwines exponentials of \(x\).
Normality therefore rewrites (22) as
\[
\mathcal L(z)
=\lambda(e^{zx^*-\bar z x})\,C_n\,
 \lambda(e^{-zx^*+\bar z x}).
\tag{23}
\]
Both exponentials are unitary.
Their left actions are isometries on \(H\) and on \(Mp_n\) in operator norm, so \(\|\mathcal L(z)\|\leq\|C_n\|\) uniformly.
Scalar Liouville, applied through all continuous linear functionals on this Banach space, makes \(\mathcal L\) constant.
Differentiating at zero gives \([C_n,x^*]=0\) on \(Mp_n\).

Hence \(C_n\) intertwines left multiplication by every starred polynomial.
For \(a\in M\), choose uniformly bounded starred polynomials \(a_\alpha\to a\) in \(L^2\), by Kaplansky density and norm approximation inside \(C^*(X)\).
For fixed \(z\in Mp_n\), the vectors \(a_\alpha z\) remain in that window, are uniformly bounded, and converge in \(L^2\) to \(az\).
Equation (15) gives \(C_n(a_\alpha z)\rightharpoonup C_n(az)\).
Meanwhile \(a_\alpha C_nz\to aC_nz\) in \(H\): uniformly bounded \(L^2\) convergence of multipliers is strong convergence on \(H\), by first testing bounded vectors and then using density.
Therefore
\[
C_n(az)=aC_nz
\quad(a\in M,\ z\in Mp_n).
\tag{24}
\]

The local identity (24) is sufficient.
There is no global expression \(D_{i,0}(zX_i)\) for arbitrary \(z\in\mathcal E\), and no value \(C_n\Omega\) is needed.

## 5. Closability and Dense-Restriction Cancellation

For any fractions (4), left invariance of \(\mathcal E\) makes the defects (5) well-defined.
For \(w\in V_i\) and \(z\in\mathcal E\),
\[
\langle w,T_i z\rangle
=\left\langle
b^*D_{i,0}^*(s^*w)-t^*D_{i,0}^*(a^*w),z
\right\rangle.
\tag{25}
\]
The adjoint inputs belong to \(V_i\) by its left \(M\)-module property.
Thus every defect is densely defined and closable.

**Finite-rank extension.**
A densely defined closable operator \(T\) with finite-dimensional range \(W\subset H\) has a unique bounded finite-rank extension.
For an orthonormal basis \(w_1,\ldots,w_r\) of \(W\), choose \(\eta_j\in\operatorname{Dom}T^*\) projecting orthogonally onto \(w_j\).
Such vectors exist because the projection of a dense linear subspace onto a finite-dimensional space is the entire space.
Then \(\langle w_j,Tz\rangle=\langle T^*\eta_j,z\rangle\) bounds each coordinate in the Hilbert norm.
The closure graph equals the graph of the resulting bounded operator, since the original domain is dense.

**Cancellation.**
Let \(T:\mathcal E\to H\) be closable and let \(y,y'\in M\) be regular.
If \(z\mapsto yT(y'z)\) has finite rank on \(\mathcal E\), then \(T\) has a bounded finite-rank extension.
Indeed \(y'\mathcal E\subseteq\mathcal E\) is dense in \(H\), because \(y'\) has dense range.
Injectivity of \(y\) makes \(T|_{y'\mathcal E}\) finite rank.
This restriction is closable, so its closure is a bounded finite-rank operator \(B\) on all of \(H\).
The graph of \(\overline T\) contains that whole-domain graph.
As \(\overline T\) is single-valued, it equals \(B\).

No infinity-to-\(L^2\) estimate, spectral cutoff, or graph-density assumption on \(y'\mathcal E\) is required for this cancellation.
Once \(T\) is bounded finite rank, multiplication by the injective \(y\) and composition with the dense-range \(y'\) preserve its finite numerical rank.
For the latter assertion, \(T(y'H)\) is a dense linear subspace of the finite-dimensional range \(T(H)\), hence equals it.

## 6. Fraction Independence and the Forward Implication

For two fraction pairs representing the same \(u\), common bounded regular left and right multiples give regular \(x,y,x',y'\in M\) with
\[
xs=ys_1,\qquad xa=ya_1,\qquad
tx'=t_1y',\qquad bx'=b_1y'.
\tag{26}
\]
The numerator equalities follow from equality of the affiliated fractions.
The required common multiples follow from the construction in Section 3 and its reversed version.

Every bounded multiplier preserves the input domain on the left.
Substitution into the two defects gives
\[
yT_i^{s_1,a_1,b_1,t_1}y'
=xT_i^{s,a,b,t}x'
\quad\text{on }\mathcal E.
\tag{27}
\]
If one defect has finite rank, cancellation proves the same for the other.
The numerical-rank observation proves equality of their finite ranks.

Let \(\mathcal R\) be the fraction-independent class of \(u\in U\) whose defects all have finite rank.
Constants and the \(X_j\) belong to it by (2), using coefficients \(s=t=1\).
Using the bounded coefficient \(1\) does not require the input vector \(\Omega\) to belong to \(\mathcal E\).

For sums, choose common denominators so that
\[
s=x_1s_1=x_2s_2,\quad a=x_1a_1+x_2a_2,\quad
t=t_1y_1=t_2y_2,\quad b=b_1y_1+b_2y_2.
\]
The resulting defect is \(\sum_{\ell=1}^2x_\ell T_{i,\ell}y_\ell\), hence finite rank.
Scalar multiplication has the same property.

For products \(u_\ell=s_\ell^{-1}a_\ell=b_\ell t_\ell^{-1}\), take bounded \(x,y,p,q\in M\), with \(x,q\) regular, satisfying
\[
xa_1=ys_2,\qquad t_1p=b_2q.
\tag{28}
\]
These are obtained from bounded fractions of \(a_1s_2^{-1}\) and \(t_1^{-1}b_2\); \(y,p\) need not be regular.
Then
\[
u_1u_2=(xs_1)^{-1}ya_2=b_1p(t_2q)^{-1}.
\]
Its defect equals
\[
x(s_1D_{i,0}b_1-a_1D_{i,0}t_1)p
+y(s_2D_{i,0}b_2-a_2D_{i,0}t_2)q
\quad\text{on }\mathcal E.
\tag{29}
\]
The middle terms cancel because their coefficients agree and their inputs are the identical vector \(t_1pz=b_2qz\in\mathcal E\).
Thus products remain in \(\mathcal R\).

If \(u=s^{-1}a=bt^{-1}\) is a unit of \(U\), then \(a,b\) are regular and \(u^{-1}=a^{-1}s=tb^{-1}\) has the negative of the original defect.
Therefore \(\mathcal R\) is an inverse-closed unital algebra containing \(A\), and
\[
F\subseteq\mathcal R.
\tag{30}
\]

## 7. Local Tensor Descent Gives the Reverse Implication

Suppose \(u\in\mathcal R\), and write \(T_i\) for the bounded finite-rank extensions of its defects.
For fractions (4), \(sb=at\).
Fix \(n\) and \(z\in Mp_n\).
Then \(zX_i\in\mathcal E\), so \(T_i(zX_i)\) agrees with the original defect evaluated at that input.
Also \(bz,tz\in Mp_n\), because the window is a left \(M\)-module.
Since right multiplication commutes with every bounded left coefficient, equations (14) and (24) give
\[
\begin{aligned}
\sum_i[R_i,T_i]z
&=sK_n(bz)-aK_n(tz)\\
&=sC_n(bz)-aC_n(tz)+(aPt-sPb)z\\
&=(aPt-sPb)z.
\end{aligned}
\tag{31}
\]
The two local \(C_n\) terms cancel as \((sb-at)C_nz\).
The first and last lines are bounded operators on \(H\).
Their equality holds on every \(Mp_n\), whose union is dense, so
\[
\sum_i[R_i,T_i]=aPt-sPb
\quad\text{on }H.
\tag{32}
\]

Let \(Jz=z^*\) and use the finite-tensor identification
\[
\Theta(g\otimes h)z=g\langle Jh,z\rangle,\qquad g,h\in H.
\]
It identifies the algebraic tensor product with finite-rank operators and satisfies
\[
[\rho(x),\Theta(g\otimes h)]
=\Theta(gx\otimes h-g\otimes xh).
\]
Writing \(T_i=\sum_\alpha\Theta(g_{i\alpha}\otimes h_{i\alpha})\), (32) becomes
\[
a\otimes t-s\otimes b
=\sum_{i,\alpha}
\bigl(g_{i\alpha}X_i\otimes h_{i\alpha}
      -g_{i\alpha}\otimes X_ih_{i\alpha}\bigr)
\tag{33}
\]
in \(H\otimes_{\mathbb C}H\), and hence in \(U\otimes_{\mathbb C}U\).
The latter passage is injective because \(H\hookrightarrow U\) is a complex-linear injection.

Pass to \(U\otimes_FU\).
Balancing kills the right-hand terms.
The invertible outer actions of \(s^{-1}\) and \(t^{-1}\) give
\[
u\otimes_F1=1\otimes_Fu.
\tag{34}
\]
If \(u\notin F\), then \(1,u\) are right-\(F\) linearly independent in \(U\): a relation \(a+ub=0\) with \(b\ne0\) gives \(u=-ab^{-1}\in F\).
Extend them to a right-\(F\) basis and choose a right-\(F\) linear map \(\phi:U\to F\) with \(\phi(1)=0\), \(\phi(u)=1\).
Applying \(\phi\otimes\mathrm{id}\) to (34) gives \(1=0\) in \(F\otimes_FU\cong U\), a contradiction.
Thus \(\mathcal R\subseteq F\), completing the full affiliated equivalence.

For bounded \(f\), take \(s=t=1\), \(a=b=f\), giving (6).
If its commutator has bounded finite-rank extension \(T_i\) and \(z\in\operatorname{Dom}D_i\), choose graph approximants \(z_n\in\mathcal E\).
Then \(fz_n\in\mathcal E\) and
\[
fz_n\to fz,\qquad
D_{i,0}(fz_n)=fD_{i,0}z_n+T_iz_n\to fD_iz+T_iz.
\]
Closedness gives \(fz\in\operatorname{Dom}D_i\) and \([D_i,f]z=T_iz\).
Conversely, the full closed-domain finite-rank condition restricts to the original commutator on \(\mathcal E\).
These are precisely the closures of the prescribed restrictions, not arbitrary larger closed extensions.

## 8. A Strict Noncommuting Example

Let \(d\geq2\), \(M=L(\mathbb F_d)\), and let \(U_1,\ldots,U_d\) be the canonical free Haar generators.
Use bounded duals \(B_i\) with \([B_i,U_j]=\delta_{ij}P\), supplied by the audited free-Haar construction in [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005).

Choose a positive measurable affiliated operator \(\eta\notin L^2(M)\).
For instance,
\[
\eta=1+|1-U_1|^{-\alpha},
\qquad \tfrac12\leq\alpha<1,
\tag{35}
\]
is finite almost everywhere in the Haar spectral model, belongs to \(L^1\), and does not belong to \(L^2\), because \(|1-e^{i\theta}|\) is comparable to \(|\theta|\) near zero.
The \(L^1\) property is optional.

Let \(T=\rho(\eta)\) be closed selfadjoint right multiplication by \(\eta\) on \(H\), and put
\[
h=(1+\eta^2)^{-1/2}\in M,\qquad
\mathcal E=V_i=Mh,\qquad
D_{i,0}=(B_i+T)|_{Mh}.
\tag{36}
\]
The element \(h\) is bounded regular, so \(Mh\) is an \(H\)-dense left \(M\)-module.
Both \(h\) and \(h\eta\) are bounded; hence \(Mh\subseteq\operatorname{Dom}T\).
Bounded perturbation gives
\[
(B_i+T)^*=B_i^*+T,\qquad
\operatorname{Dom}(B_i+T)=\operatorname{Dom}(B_i^*+T)=\operatorname{Dom}T.
\]
Thus the test-module adjoint inclusion holds.
The domain of right multiplication by \(\eta\) is invariant under bounded left multiplication, with \(T(az)=aTz\).
Consequently
\[
[D_{i,0},U_j]=[B_i,U_j]=\delta_{ij}P
\quad\text{on }Mh.
\]

The subspace \(Mh\) is a graph core for \(T\).
Selfadjoint spectral calculus makes
\[
\rho(h)=(1+T^2)^{-1/2}:H\longrightarrow\operatorname{Dom}T
\]
an onto isometry when the target has graph norm:
\[
\|\rho(h)y\|_2^2+\|T\rho(h)y\|_2^2=\|y\|_2^2.
\tag{37}
\]
Since \(M\) is dense in \(H\), its image \(Mh\) is graph dense.
Bounded perturbations preserve graph cores, so the actual closures and adjoints are
\[
D_i=B_i+T,\qquad D_{i,0}^*=D_i^*=B_i^*+T.
\tag{38}
\]

But \(\Omega\notin\operatorname{Dom}T\), because \(\eta\notin L^2\).
Thus neither the actual closed dual domains nor their adjoint domains contain all of \(M\).
The theorem nevertheless applies to this genuinely noncommuting tuple.
The additional unbounded right-multiplication terms cancel from every cleared defect:
\[
s((bz)\eta)-a((tz)\eta)=(sb-at)z\eta=0
\quad(z\in Mh).
\tag{39}
\]
All terms are legitimate \(H\) vectors because \(z\in Mh\subseteq\operatorname{Dom}T\) and the domain is left \(M\)-invariant.
No right-normalizer condition, averaging construction, or bounded similarity of \(hU_jh^{-1}\) is required.

This example proves strictness of the new domain assumptions.
It is not a counterexample to the polynomial-core criterion: the vacuum vector is omitted.
Any left \(M\)-module containing \(\Omega\) contains every \(a\Omega\), and hence all of \(M\).

For the simpler commutative projection-domain example, take one Haar generator and its bounded Fourier deletion dual \(B\), a real measurable \(\eta\notin L^2\), and \(\mathcal E=V_1=\bigcup_nM1_{\{|\eta|\leq n\}}\).
Bounded vector truncations show that this is a graph core for \(\rho(\eta)\).
Then \((B+\rho(\eta))|_{\mathcal E}\) satisfies the same hypotheses and again omits \(\Omega\).
Thus principal ideals and unions of projection ideals are convenient examples, not additional assumptions of the theorem.

## 9. Relation to Other Domains and Proof Inputs

Requiring both closed domains to contain \(C^*(X)\Omega\) does not genuinely weaken their inclusion of \(M\Omega\).
Closed graph on the Banach space \(C^*(X)\), in operator norm, supplies both infinity-to-\(L^2\) estimates.
Kaplansky bounded approximants and weak closedness of the Hilbert graphs then put every bounded vector of \(M\) in both domains, as in [Yin_C_F0027, Section 5](Yin_C_F0027_v1.md#yin_c_f0027).
Transfer of a generator identity also retains its stated initial domain and uses the corresponding graph/weak-continuity argument.

A norm-dense inverse-closed algebra does not acquire these operator-norm estimates merely by being complete in a stronger graph norm.
Yin_C_F0027's bounded-inversion argument remains valid at its own scope, but that completeness alone does not supply the full affiliated forward implication.
The present theorem uses left-module invariance for every bounded fraction coefficient and automatically available large bounded windows for the fundamental identity.

Accepted inputs are finite-tracial affiliated fractions and polar decomposition, the MSY23 finite-rank-cycle/free-field interfaces, Hilbert adjoints and closed graph, finite projection-trace inequalities, Kaplansky density, scalar Liouville, and the finite-tensor identification.
Their source-level inspection limits remain those of the linked audits.
Normality is used in the local Liouville argument, not in maximal Delta, cancellation, or the fraction algebra.
No bounded matrix inverse is inferred from boundedness of a scalar rational output.
The earlier Yin_C_F0012/Yin_C_F0014 obstructions and the unresolved general starred-polynomial-core forward question retain their original scopes.

Earlier unpromoted drafts imposed right-invariant projection or principal-ideal domains.
The final proof removes those requirements by extracting projections from any dense left module and using the local windows (9).
Its adjoint test modules likewise have no right-invariance requirement or operator-norm estimates.
This history does not alter the statement being proved.

The [original P1 review finding](../audits/reviews/Yin_R_F0018_v1.md#scope-and-independence) owns its P1 inspection scope and retains an unknown initial-context relationship.
It does not review the P2 assembly selected by the [current assessment](#decision-finding-owned-review).
The new architecture and strict example are mathematical deductions, not numerical experiments or proof-assistant verification.


## Argument: yin_c_f0029-p2


## Affiliated Rationality: Proofs Using the Shared Lemmas

Date: 2026-09-10.
Human author: Yin.
Proof development: root.
Authorization and original-artifact map: [approved extraction batch](../ledger/Yin_L_F0014_v1.md#authorization).
These are new proofs of the existing statements, not new claims or new theorem-role assignments.
The [proof-version map](../ledger/Yin_L_F0014_v1.md#proof-version-map) owns the selected version; the original complete arguments remain unchanged.
At creation these versions are candidates awaiting independent lemma and assembly reviews.

<a id="yin_c_f0029-p2"></a>
## Yin_C_F0029-P2: The Dense-Module Criterion

### Exact Statement Reference and Conventions

The authoritative statement is [Yin_C_F0029, Section 1](#yin_c_f0029).
Let \(M\) be finite tracial with faithful normal probability trace, \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
The inner product is linear in its second variable.
Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of \(M\).
Let \(E,V_i\subset H\) be dense complex-linear left \(M\)-modules, and let \(D_{i,0}:E\to H\) satisfy
\[
V_i\subseteq\operatorname{Dom}D_{i,0}^*,
\qquad [D_{i,0},X_j]z=\delta_{ij}Pz\quad(z\in E).
\]
Write \(D_i=\overline{D_{i,0}}\), \(U=U(M)\), \(A=\mathbb C\langle X\rangle\), and \(F=\operatorname{Div}_U A\).
No generator adjoints are adjoined to \(A\).
The hypotheses imply closability, and the closures here are exactly those of the specified restrictions.

We prove all three numbered conclusions of Yin_C_F0029: maximal Delta and free-field realization; the universal affiliated finite-defect criterion with numerical-rank independence; and the actual closed-domain bounded-element criterion.
The strict example is verified separately below.
No step assumes \(\Omega\in E\), right invariance of \(E\), or an operator-norm estimate on the whole of \(E\).
If the tuple is empty, \(M=W^*(\varnothing)=\mathbb C\), \(U=F=\mathbb C\), and the assertions are immediate with \(\Delta=0\) and no defects.
We therefore take \(d\geq1\) in the proof below.

### Direct Proof Dependencies and Their Interfaces

| Input | Use and supplied hypotheses |
| --- | --- |
| [Yin_C_F0031-P1](Yin_C_F0031_v1.md#yin_c_f0031-p1) | Dense adjoint tests make each cleared defect closable; finite range then gives a bounded finite-rank closure |
| [Yin_C_F0032-P1](Yin_C_F0032_v1.md#yin_c_f0032-p1) | The dense left module \(E\) supplies projections and local test spaces; each \(D_{i,0}\) is closable |
| [Yin_C_F0033-P1](Yin_C_F0033_v1.md#yin_c_f0033-p1) | Normality, generation and the dual relations supply the local module identity; the defects have bounded representatives from Yin_C_F0031 |
| [Yin_C_F0034-P1](Yin_C_F0034_v1.md#yin_c_f0034-p1) | The precise \(E,V_i,D_{i,0}\) assumptions hold, and generator defects are the rank-one \(P\) or zero |
| [Yin_C_F0035-P1](Yin_C_F0035_v1.md#yin_c_f0035-p1) | The accepted free-field interface, applied after maximal Delta is proved, makes \(F\subset U\) a same-unit division subring |
| [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Finite-rank-cycle characterization of \(\Delta(X)=d\) for a bounded tuple, with left/right conventions converted as in the audited unit |
| [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | The implication from maximal Delta to the embedded free field and the accepted finite-tracial affiliated foundation |

The finite-tensor identification is reconstructed in the proof below; elementary trace cyclicity is applied only to bounded finite-rank operators.
Finite-tracial left and right fractions and common regular multiples have the accepted source scope used in Yin_C_F0034.
The original Yin_C_F0029 proof is extraction provenance, not an input theorem.
Yin_C_F0024 and Yin_C_F0030 are not used to prove this version.

### 1. Maximal Delta Without Using the Rationality Conclusion

Suppose finite-rank bounded operators \(T_1,\ldots,T_d\) satisfy
\[
\sum_i[T_i,X_i]=0.
\]
By the accepted cycle characterization it suffices to prove that all \(T_i\) vanish.
Choose a finite basis \(g_k\) of their joint range and bounded fractions \(g_k=b_kt_k^{-1}\), with \(t_k\) regular.
A common bounded regular right multiple \(r=t_kc_k\) gives \(g_kr=b_kc_k\in M\).
For completeness, to combine two denominators, write the affiliated unit \(t_1^{-1}t_2=pq^{-1}\) with bounded regular \(p,q\).
Then \(t_1p=t_2q\); induction produces the required common multiple.
Put \(Q=\rho(r)\), an injective bounded operator on \(H\).

Take the projections \(e_n\) supplied by Yin_C_F0032, so \(Me_n\subset E\) and \(e_n\to1\) strongly.
For \(c,\ell\in M\), set
\[
S_i=\rho(c e_n)\,Q T_i\rho(\ell).
\]
Their ranges lie in \(Me_n\): the order of multiplication is \(g\mapsto gr\mapsto grce_n\).
All the added right multipliers commute with left \(X_i\), so \(\sum_i[S_i,X_i]=0\).
The operators \(D_{j,0}S_i\) are bounded finite rank, since a linear map on the finite-dimensional range of a bounded finite-rank operator gives a bounded composition.
The same reasoning applies to all domain compositions below, because \(ME\subset E\).
The dual relation gives
\[
0=\sum_i\bigl(D_{j,0}S_iX_i-D_{j,0}X_iS_i\bigr)
 =\sum_i[D_{j,0}S_i,X_i]-PS_j.
\]
Taking the ordinary finite-rank trace is now legitimate and yields
\[
0=\operatorname{Tr}(PS_j)
  =\langle\Omega,S_j\Omega\rangle
  =\langle e_nc^*,QT_j\ell\rangle.
\]
For fixed \(c,\ell\), let \(n\to\infty\).
Since \(c^*,\ell\) range over the dense space \(M\), this proves \(QT_j=0\), hence \(T_j=0\).
Thus \(\Delta(X)=d\).
MSY23-U004 now identifies \(F\) with the evaluated free skew field.
Neither normality nor a value of \(D_{j,0}\Omega\) was used in this step.

### 2. Defects, Fraction Independence and the Forward Direction

For any \(u\in U\), take bounded fractions \(u=s^{-1}a=bt^{-1}\), with \(s,t\) regular, and define on \(E\)
\[
T_i=sD_{i,0}b-aD_{i,0}t.
\]
Left invariance makes every term well-defined.
For \(v\in V_i\), the vectors \(s^*v,a^*v\) remain in \(V_i\), and
\[
\langle v,T_i z\rangle
=\left\langle
b^*D_{i,0}^*(s^*v)-t^*D_{i,0}^*(a^*v),z
\right\rangle.
\]
Consequently \(T_i\) is closable.
Yin_C_F0031 makes every finite-range \(T_i\) the restriction of its unique bounded finite-rank closure.

All hypotheses of Yin_C_F0034 hold for these maps and modules.
Hence the class \(\mathcal R\subset U\) of simultaneous finite-rank defects is independent of the chosen bounded fraction pairs, and each finite numerical rank is independent as well.
It is an inverse-closed unital algebra.
Using \(s=t=1\) for the bounded generators gives \([D_{i,0},X_j]=\delta_{ij}P\), so \(A\subset\mathcal R\).
Therefore \(F=\operatorname{Div}_U A\subseteq\mathcal R\).
This argument does not assume a bounded inverse pencil for a bounded rational scalar.

### 3. The Reverse Direction and the Tensor Equalizer

Let \(u\in\mathcal R\), and use \(T_i\) also for its bounded finite-rank defect representatives.
Since \(sb=at\), Yin_C_F0033 applies and gives the bounded Hilbert-operator identity
\[
\sum_i[\rho(X_i),T_i]=aPt-sPb.
\tag{P2-1}
\]
Its use is local before extension: for the projections \(p_n\) of Yin_C_F0032, \(Mp_n\subset Me_n\subset E\) and \((Mp_n)X_i\subset Me_n\).
Thus all terms are defined on these spaces, the local module map cancels using \(sb=at\), and boundedness extends the result to \(H\).
No right invariance of all of \(E\) is inserted.

Let \(Jz=z^*\).
The map
\[
\Theta(g\otimes h)z=g\langle Jh,z\rangle
\]
identifies \(H\otimes_{\mathbb C}H\) with finite-rank operators: the usual representation of a finite-rank operator by range vectors and continuous coordinate functionals gives surjectivity, and linear independence of a finite set of range vectors proves injectivity.
The appearance of \(J\) makes this identification bilinear with our inner-product convention.
Direct evaluation gives
\[
[\rho(x),\Theta(g\otimes h)]
=\Theta(gx\otimes h-g\otimes xh).
\]
Write \(T_i=\sum_\alpha\Theta(g_{i\alpha}\otimes h_{i\alpha})\).
Equation (P2-1) is precisely
\[
a\otimes t-s\otimes b
=\sum_{i,\alpha}
\bigl(g_{i\alpha}X_i\otimes h_{i\alpha}
      -g_{i\alpha}\otimes X_i h_{i\alpha}\bigr).
\tag{P2-2}
\]
The inclusion \(H\hookrightarrow U\) is complex-linear, so this equality also holds in \(U\otimes_{\mathbb C}U\).
Pass to \(U\otimes_F U\).
Every term on the right vanishes by balancing, since \(X_i\in F\).
The outer left action of \(s^{-1}\) on the first factor and right action of \(t^{-1}\) on the second are legitimate and give
\[
u\otimes_F1=1\otimes_Fu.
\]
Step 1 already established that \(F\subset U\) is a division subring with the same identity.
Yin_C_F0035 therefore gives \(u\in F\).
This proves \(\mathcal R=F\), without any dependence on Yin_C_F0029-P1's conclusion.

### 4. Bounded Elements and the Specified Closed Domains

For \(f\in M\), choose \(s=t=1\), \(a=b=f\), so the defect is \([D_{i,0},f]\) on \(E\).
The preceding equivalence proves the bounded-element equality in Yin_C_F0029.
If \(T_i\) is its bounded finite-rank representative and \(z\in\operatorname{Dom}D_i\), choose \(z_n\in E\) converging to \(z\) in the graph norm of \(D_i\).
Since \(fE\subset E\),
\[
fz_n\to fz,\qquad
D_{i,0}(fz_n)=fD_{i,0}z_n+T_i z_n\to fD_i z+T_i z.
\]
Closedness implies \(fz\in\operatorname{Dom}D_i\) and \([D_i,f]z=T_i z\).
Conversely, a full-domain bounded finite-rank commutator restricts to \(E\).
These statements concern precisely \(D_i=\overline{D_{i,0}}\), not arbitrary larger extensions.

### 5. Preserved Strict-Domain Example and Scope

The independently checked construction in Yin_C_F0029-P1 Section 8 is retained as an auxiliary example; its proof does not invoke the rationality conclusion.
Here is the complete interface needed by P2.
Take \(M=L(\mathbb F_d)\), \(d\ge2\), with free Haar generators \(U_j\) and bounded duals \(B_i\) supplied by [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005), with the audited sign convention \([B_i,U_j]=\delta_{ij}P\).
Set
\[
\eta=1+|1-U_1|^{-\alpha},\quad \tfrac12\le\alpha<1,\qquad
T=\rho(\eta),\quad h=(1+\eta^2)^{-1/2}.
\]
The Haar spectral model shows \(\eta\) is finite almost everywhere and not in \(L^2\), because \(|1-e^{i\theta}|\) is comparable to \(|\theta|\) near zero.
It is positive, and \(T\) is closed selfadjoint right multiplication.
The regular bounded \(h\) has dense-range right multiplication; \(h\eta\) is bounded.
Thus \(E=V_i=Mh\) is a dense left \(M\)-module inside \(\operatorname{Dom}T\).
Put \(D_{i,0}=(B_i+T)|_{Mh}\).
The domain of \(T\) is left \(M\)-invariant and \(T\) commutes there with left multipliers.
Bounded perturbation and restriction show \(Mh\subseteq\operatorname{Dom}D_{i,0}^*\), and the prescribed dual identities hold.

Spectral calculus makes \(\rho(h)=(1+T^2)^{-1/2}\) an onto isometry from \(H\) to \(\operatorname{Dom}T\) with graph norm.
Since \(M\) is dense in \(H\), \(Mh\) is a graph core.
Bounded perturbations preserve this property; hence \(D_i=B_i+T\) and \(D_i^*=B_i^*+T\), both with domain \(\operatorname{Dom}T\).
But \(\Omega\notin\operatorname{Dom}T\), so neither domain contains all bounded vectors.
The added right-multiplication terms cancel from every defect as \((sb-at)z\eta=0\).
This verifies strict domain reduction for a noncommuting tuple.
It does not supply a smaller unital core containing the vacuum: a left \(M\)-module containing \(\Omega\) contains \(M\).

The independent ancillary comparison in Yin_C_F0029-P1 Section 9 remains at its original scope and review; it is not needed for Steps 1-4.
No polynomial-only converse or equality \(\operatorname{Div}_U A\cap M=\operatorname{Div}_M A\) is asserted.


## Review Boundary

The selected proof graph uses the five extracted lemma proofs and the specified accepted source interfaces.
It has no dependency on a parent's conclusion through an extraction-origin link.
All original statements and complete proofs retain their actual inspected scope.
The new lemma and assembly reviews must identify the exact versions inspected before P2 is selected as current.
No manuscript compilation, formal verification, external human review or novelty certification is claimed.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0029-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0031_v1.md#decision-candidate-0002) | Dense adjoint tests and finite-range closability give bounded finite-rank cleared defects. |
| dependency | [Exact material](Yin_C_F0032_v1.md#decision-candidate-0002) | Dense left-module projections, local test spaces and closability. |
| dependency | [Exact material](Yin_C_F0033_v1.md#decision-candidate-0002) | Local module identity under normality, generation and bounded defects. |
| dependency | [Exact material](Yin_C_F0034_v1.md#decision-candidate-0002) | Fraction/tensor descent with the specified E, V_i, D_i and rank-one/zero generator defects. |
| dependency | [Exact material](Yin_C_F0035_v1.md#decision-candidate-0002) | Same-unit free-field division subring after maximal Delta. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:45 |
| status | proved |
| reason | Select the actual retained finding scopes and their known mathematical-development relationships, preserving status, authorized role, exact statement/proof/dependency selections and all historical decisions. No new mathematical review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0029-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact dependency](Yin_C_F0031_v1.md#decision-candidate-0002) | Dense adjoint tests and finite-range closability give bounded finite-rank cleared defects. |
| dependency | [Exact dependency](Yin_C_F0032_v1.md#decision-candidate-0002) | Dense left-module projections, local test spaces and closability. |
| dependency | [Exact dependency](Yin_C_F0033_v1.md#decision-candidate-0002) | Local module identity under normality, generation and bounded defects. |
| dependency | [Exact dependency](Yin_C_F0034_v1.md#decision-candidate-0002) | Fraction/tensor descent with the specified E, V_i, D_i and rank-one/zero generator defects. |
| dependency | [Exact dependency](Yin_C_F0035_v1.md#decision-candidate-0002) | Same-unit free-field division subring after maximal Delta. |
| review | [Retained finding](../audits/reviews/Yin_R_F0012_v1.md#criterion-assembly-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0012_v1.md).

Material covered by that review: [Exact material](Yin_C_F0024_v1.md#yin_c_f0024-p2), [Exact material](#yin_c_f0029-p2), [Exact material](Yin_C_F0030_v1.md#yin_c_f0030-p2) (together retain the original whole-source scope); [Exact material](Yin_C_F0029_v1.md).

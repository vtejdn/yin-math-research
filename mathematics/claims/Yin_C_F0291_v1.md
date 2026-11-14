---
author: Yin
---

# Weighted curvature rows for mixed canonical domains and the role of diffuseness

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

**Diffuse marginals.**
Let \(\mu\) be a compactly supported diffuse planar probability with support \(K\).
Write \(\kappa(x,y,z)\) for the reciprocal circumradius, with value zero on collinear or repeated triples, and define
\[
 g(z,w)=\int\kappa(z,w,s)^2\,d\mu(s),\qquad
 A(z)=\int g(z,w)\,d\mu(w).
\]
For every distinct \(z,w\in K\),
\[
            |z-w|g(z,w)\le 2\big(\sqrt{A(z)}+\sqrt{A(w)}\big).        \tag{1}
\]
In particular, a finite essential supremum of \(A\) implies both hypotheses of the [curvature row theorem](Yin_C_F0078_v2.md#statement).
At a coordinate \(Z\) of an arbitrary correlated normal tuple with actual starred conjugate variables, this single marginal condition gives both bounded-vector domains for the original generator-first canonical operator \(D=-\overline{(\mathrm{id}\otimes\tau)\delta_Z}\).
It gives the normal \(\mathsf A\)-to-\(\mathsf S\) implication on tuples that satisfy this condition at each coordinate.

For the same actual tuple write \(\xi=\delta_Z^*(1\otimes1)\), let \(\gamma\) be partial liberation at \(Z\), set \(\zeta=(i\gamma)^*(1\otimes1)=-i[Z^*,\xi]\), and let \(\nu_\xi,\nu_\zeta\) be the spectral measures on \(K^2\) of these two vectors for left and right multiplication by \(Z\).
Even when the curvature rows are unbounded, the spectral term satisfies
\[
         \int g^2\,d\nu_\zeta
         \le 8\int_{z\ne w}(A(z)+A(w))\,d\nu_\xi(z,w).                \tag{2}
\]
If the right side is finite, the spectral multiplier \(S_g\zeta\) exists in \(L^2(M,\tau)\).
Under finiteness of the right side of (2), define the curvature-weighted liberation derivation on starred generators by \(Z\mapsto i(z-w)g(z,w)\), \(Z^*\mapsto i(\bar z-\bar w)g(z,w)\), and zero on the omitted generators and their adjoints.
This prescription descends to the represented core and has actual vacuum \(S_g\zeta\).
For \(g\in L^2(\mu^2)\) it agrees with \(iI_g\gamma\), where \(I_g\) inserts the marginal tensor in the two coarse legs of the finite algebraic expansion of \(\gamma(p)\).

**A weighted curvature-row condition.**
For the actual tuple at \(Z\), suppose there exists a real Borel weight \(w_0\ge1\) in \(L^2(\mu)\) and a finite \(R\ge0\) with
\[
 \int g(z,v)w_0(v)\,d\mu(v)\le Rw_0(z)\quad(\mu\text{-almost everywhere}),
 \qquad
 K_\xi^2=\int_{z\ne v} w_0(z)^2w_0(v)^2\,d\nu_\xi(z,v)<\infty.         \tag{3}
\]
Then the original generator-first canonical operator \(D\) and its actual Hilbert adjoint both have domains containing \(M\Omega\), with the generator commutators on all these vectors.
All mixed starred words are allowed.
If each coordinate meets (3), the tuple satisfies \(\mathsf S\).
On an explicit correlated normal pair with \(\mu\) uniform on two perpendicular segments, (3) holds with an unbounded \(w_0\), while \(A\) is essentially unbounded.
There are also diffuse scalar marginals with actual normal conjugate variables that admit no finite positive weight satisfying the first inequality of (3).

**Three atomic sites.**
In the finite-marginal [Gram test (P14)](../drafts/Yin_D_F0002.md#angular-modes-of-the-three-point-curvature-form) take three planar sites \(z_i\), masses \(m_i\), and \(g_{ij}=\sum_{k\ne i,j}m_k\kappa(z_i,z_j,z_k)^2\) for \(i\ne j\).
The symmetric edge coefficients \(\alpha_{ij}\) and the single real triangle coefficient \(\lambda\) are required to satisfy
\[
     g_{ij}=(m_i+m_j)\alpha_{ij}+m_k\lambda
            \quad(\{i,j,k\}=\{1,2,3\}),\qquad
     \begin{pmatrix}\alpha_{ij}&\lambda\\ \lambda&\alpha_{ik}\end{pmatrix}
          \succeq0\quad(i=1,2,3).                                    \tag{4}
\]
There is no numerical constant uniformly bounding \(\max_{i<j}|z_i-z_j|^2\alpha_{ij}\) over configurations, even when the coefficients can be chosen separately for each configuration.
For the same family the scalar jump Laplacian \(L_g f(i)=\sum_{j\ne i}m_jg_{ij}(f(i)-f(j))\) on \(L^2(m)\) has an unbounded gap coefficient in its nonnegative square root.
More precisely, writing \((L_g^{1/2})_{ij}=-m_j b_{ij}\) in value coordinates for \(i\ne j\), one has \(\sup|z_1-z_2|b_{12}=\infty\) along the family.
These obstructions apply to a finite spectral model whose repeated triples contribute zero curvature.

## Argument

### Two triangles with a common edge

Fix four distinct planar points \(z,w,s,t\), put \(\ell=|z-w|\), and let \(d_z,d_w\) be the distances from \(z,w\) to the line through \(s,t\).
Use orthonormal coordinates with that line horizontal, and write \(\Delta_s=|\det(z-s,w-s)|\) and \(\Delta_t=|\det(z-t,w-t)|\).
Expansion of the first determinant along the vertical coordinates gives
\[
                 \Delta_s\le d_z|w-s|+d_w|z-s|.
\]
Writing the second determinant with one side \(z-w\) gives \(\Delta_t\le\ell\min(|z-t|,|w-t|)\).
The circumradius formula now yields
\[
 \begin{aligned}
 \ell\,\kappa(z,w,s)\kappa(z,w,t)
 &=\frac{4\Delta_s\Delta_t}
        {\ell |z-s|\,|w-s|\,|z-t|\,|w-t|}\\
 &\le \frac{4d_z}{|z-s|\,|z-t|}+\frac{4d_w}{|w-s|\,|w-t|}
 =2\big(\kappa(z,s,t)+\kappa(w,s,t)\big).
 \end{aligned}                                                        \tag{5}
\]
These determinant formulas include the case of a collinear triple.
For fixed \(z,w\), independent \(s,t\) of law \(\mu\) give four distinct points almost surely.
Taking \(L^2(\mu^2)\) norms on (5), independence gives \(\ell g(z,w)\) on the left and the triangle inequality gives (1).
When a row on the right is infinite the inequality still holds, since \(\kappa(z,w,s)\le2/\ell\).

Curvature extended by zero on repeated triples is lower semicontinuous, by continuity on all distinct triples and nonnegativity at repeated ones.
Fatou's lemma makes \(A\) lower semicontinuous.
Every relative open neighborhood of a support point has positive measure, so a finite essential bound \(a\) gives \(A(z)\le a\) for every \(z\in K\).
Equation (1) gives \(\sup_{z\ne w}|z-w|g(z,w)\le4\sqrt a\).
The [coordinate proof of the curvature row theorem](Yin_C_F0078_v2.md#the-original-canonical-operators) uses these two bounds only at the distinguished coordinate.
It gives the claimed domain conclusions with arbitrary correlations and arbitrary other marginal laws.

The [liberation commutator identity](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) gives \(d\nu_\zeta=|z-w|^2d\nu_\xi\), with zero diagonal mass for \(\nu_\zeta\).
Squaring (1) on distinct pairs proves (2).
Full actuality gives finite total squared Menger curvature \(\int A\,d\mu\) by the [scalar marginal criterion](Yin_C_F0255_v1.md#statement).
By (1), \(|z-v|^2g(z,v)^2\) is integrable against \(\mu^2\), as well as against \(\nu_\xi\) when the right side of (2) is finite.
Use the [positive polynomial approximants](Yin_C_F0078_v1.md#3-actual-polynomial-approximants-and-their-vacuum-vectors) \(q_j\), finite real symmetric marginal tensors with \(0\le q_j\le g+1\) and \(q_j\to g\) off the diagonal.
Their construction cuts off the continuous off-diagonal kernel near coincident points, then approximates it uniformly by polynomials with a vanishing positive error allowance.
Multiplication by either \(z-v\) or \(\bar z-\bar v\) gives dominated Hilbert-norm convergence in the coarse marginal space, using compactness to bound the gap times the constant error.
Every finite-core derivation \(iI_{q_j}\gamma\) therefore converges at the starred generators to the stated values, and by the outer product rule at every starred word.
Represented relations vanish for every \(j\), hence the limits give a derivation on the represented core.
The [marginal tensor adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) gives the actual vacuum \(S_{q_j}\zeta\), since row and column corrections cancel by symmetry.
Dominated convergence in \(L^2(\nu_\zeta)\), using (2), identifies the limiting vacuum with \(S_g\zeta\) by passing to each polynomial pairing.
When \(g\in L^2(\mu^2)\) the same domination gives \(q_j\to g\) in coarse Hilbert norm, so the limit is also the claimed inner insertion on each finite expansion.

### Weighted propagation along kernel compositions

Write \(w=w_0\), \(d=\operatorname{diam}K\), \(\rho=\max(1,R+\int w\,d\mu)\), and \(B=4\sqrt R+d\).
Represent the weight by a finite function on a conull set.
Since \(A\le Rw\) there, (1) and \(w\ge1\) give \(|z-v|(g(z,v)+1)\le B w(z)w(v)\) on distinct pairs of that set.
The right side of (2) is finite under (3), by \(A(z)+A(v)\le2R w(z)^2w(v)^2\).
For any of the finite approximants \(q=q_j\) above let \(T_q\) be its integral operator on \(L^2(\mu)\), and \(b_k\) the kernel of \(T_q^k\), \(k\ge1\).
The symmetric nonnegative kernel \(q\) satisfies \(T_qw\le\rho w\) almost everywhere.
It follows that \(\|T_q\|_{2\to2}\le\rho\).
Indeed, weighted Cauchy–Schwarz gives \(|T_q f|^2\le(T_q w)T_q(|f|^2/w)\), and integration using symmetry and \(T_q w\le\rho w\) once more gives the squared operator bound.
Induction now yields \(T_q^k1\le T_q^kw\le\rho^k w\).

Along each of the \(k\) edges of a path contributing to \(b_k(z,v)\), use its length times its kernel at that edge, and sum the \(k\) resulting majorants for \(|z-v|b_k(z,v)\).
On an edge from \(x\) to \(y\) the bound just proved replaces this factor by \(B w(x)w(y)\).
The two remaining path segments integrate independently from \(z\) and \(v\), giving \(T_q^{l-1}w(z)\) and \(T_q^{k-l}w(v)\) for edge \(l\).
Thus
\[
       \|\operatorname{row}(b_k)\|_2\le\rho^k\|w\|_2,\qquad
       |z-v|b_k(z,v)\le kB\rho^{k-1} w(z)w(v)
                      \quad(\mu^2\text{-almost everywhere}).           \tag{6}
\]
Each \(b_k\) is again a finite real symmetric marginal tensor.
The vacuum of \(i I_{b_k}\gamma\) is \(S_{b_k}\zeta\).
Its squared norm is the integral of \(|z-v|^2 b_k^2\) against \(\nu_\xi\) off the diagonal.
The [marginal adjoint graph](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) gives \(\nu_\zeta\ll\mu^2\).
Since \(d\nu_\zeta=|z-v|^2d\nu_\xi\), \(\nu_\xi\) restricted to distinct pairs is also absolutely continuous with respect to \(\mu^2\).
Consequently the second bound of (6) gives \(\|S_{b_k}\zeta\|_2\le kB\rho^{k-1}K_\xi\).

For a selfadjoint original polynomial \(a\) with \(\|a\|<1\) let \(u=a\pm i\sqrt{1-a^2}\).
Set \(E_b=(\mathrm{id}\otimes\tau)iI_b\gamma\) and \(v_k=\|E_{b_k}u\|_2\).
The [actual finite-kernel energy inequality (15)](Yin_C_F0078_v1.md#4-descending-finitely-many-energy-inequalities) yields
\[
              v_k^2\le 2\big(kB\rho^{k-1}K_\xi+\rho^k\|w\|_2\big)v_k+v_{2k}.
\]
Set \(s=2\rho\) and \(t_n=v_{2^n}/s^{2^n}\).
Since \(k/2^k\le1\), one has \(t_n^2\le C t_n+t_{n+1}\) with \(C=2(BK_\xi/\rho+\|w\|_2)\).
For this fixed \(q,u\), the sequence is bounded.
Indeed \(\|b_k\|_{L^2(\mu^2)}=\|T_q^k\|_{\rm HS}\le\rho^{k-1}\|q\|_{L^2(\mu^2)}\) by the operator norm estimate.
For fixed \(a\) each finite Leibniz term in \(\gamma(a)\) gives \(\|I_b\gamma(a)\|_2\le C_a\|b\|_{L^2(\mu^2)}\) after summation.
The differentiated binomial series at \(u\) has summable norm bounds by the derivative estimate for \(a^m\), namely \(m\|a\|^{m-1}\) times that bound at \(a\).
Thus \(v_k\le C_u\|b_k\|_{L^2(\mu^2)}\) for a fixed finite \(C_u\).
If some \(t_n>C+1\), the recurrence forces every subsequent term to grow by at least the fixed factor \(t_n-C>1\).
It follows that \(v_1\le s(C+1)\) uniformly in \(j\) and in these unitaries.

Let \(E_g\) be the right slice of the curvature-weighted liberation derivation constructed above.
The generator limits and finite Leibniz expansions at \(a\) give a uniform bound for the first derivatives at this fixed \(a\).
The same differentiated binomial series with summable bounds therefore gives \(E_{q_j}u\to E_g u\) in Hilbert norm and \(\|E_gu\|_2\le s(C+1)\).
For \(\delta_x,\delta_y\) the two real components of \(\delta_Z\) and its flip-adjoint companion, put \(V(u)^2=\sum_{l=x,y}\|(\mathrm{id}\otimes\tau)\delta_l u\|_2^2\).
The [original mixed energy (19)–(20)](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) gives
\[
               V(u)^2\le2\|\xi\|_2 V(u)+\tfrac12\|E_gu\|_2 .
\]
In that identity the middle trace of the summed defects \(A_x+A_y\) takes \(Z\) to \((z-v)g(z,v)/2\) and \(Z^*\) to \((\bar z-\bar v)g(z,v)/2\), and kills the omitted letters.
This derivation thus equals the Hilbert-valued limiting curvature derivation divided by \(2i\) on the original starred generators, then on words by the product rule.
The binomial series extends the equality to the displayed \(u\), giving the factor \(1/2\) in the norm bound.
Averaging the two unitary signs gives bounds for the slices of both real components on strict selfadjoint contractions.
Rescaling and splitting general core elements into real and imaginary parts gives operator-norm-to-Hilbert bounds for both canonical slices.
Indeed their linear combinations give the right slices for \(\delta_Z\) and its flip-adjoint companion, and evaluating the latter on \(p^*\) and taking the adjoint gives the left slice for \(\delta_Z\) on \(p\).
The [two-slice domain theorem](Yin_C_F0072_v1.md#statement) and the [original commutator passage](Yin_C_F0078_v2.md#the-original-canonical-operators) give both bounded-vector domains and the generator-first commutators as claimed.

### Actual marginals with unbounded rows

Let \(\mu\) be the equally weighted mixture of uniform arclength on \([0,1]\) and \(i[0,1]\).
Write \(x,y,t\) for radial distances on these two rays.
A triangle confined to one ray has zero curvature.
In any triangle using both rays its longest side is at least \(\max(x,y,t)\), by pairing a point of maximum radius with a point of the other ray.
Consequently \(\kappa\le2/\max(x,y,t)\), and integrating its square over \(t\in[0,1]\) gives \(g(z,v)\le8/\max(x,y)\) almost everywhere.
For \(0<\alpha<1/2\) take \(w(z)=|z|^{-\alpha}\) off the null origin.
Splitting the row integral at \(y=x\) gives \(T_gw\le8((1-\alpha)^{-1}+\alpha^{-1})w\), with \(w\in L^2(\mu)\).
To see the unbounded row take \(z=x>0,v=y>0\) with \(2x<y<1/2\) and a third point \(it\) with \(y<t<2y\).
Then \(\kappa(x,y,it)=2t/(\sqrt{x^2+t^2}\sqrt{y^2+t^2})\ge c/y\) with an absolute \(c>0\).
Integration in \(t\) and \(y\) gives \(A(x)\ge c'\log(1/(4x))\) for \(0<x<1/4\).

The measure has uniformly bounded maximal linear density since every ball of radius \(r\) intersects each segment in length at most \(2r\).
Its total curvature is finite by the bound on \(g\), since \(1/\max(x,y)\) is integrable on the unit square.
The [scalar geometric criterion](Yin_C_F0255_v1.md#statement) therefore gives an actual vacuum.
Take \(Z(z)=z\), a standard semicircular \(S\) free from it, and \(T=\operatorname{Re}Z+S\).
By the [commuting drift criterion](Yin_C_F0283_v1.md#the-liberation-vacuum-before-recovering-the-hidden-function), the pair \((Z,T)\) has actual starred conjugate variables, and its off-diagonal vacuum spectrum at \(Z\) has density \(|\operatorname{Re}z-\operatorname{Re}v|^2/|z-v|^2\le1\) relative to \(\mu^2\).
Indeed the liberation density is \(|\operatorname{Re}z-\operatorname{Re}v|^2\) there, and division by the squared gap recovers the off-diagonal spectrum.
Thus \(K_\xi\le\|w\|_2^2\).
The pair is correlated since the conditional expectation of \(T\) on \(W^*(Z)\) is the nonconstant \(\operatorname{Re}Z\).

For the converse limitation use the [actual shrinking-circle marginal](Yin_C_F0143_v1.md#argument) with radii \(r_n=2^{-n}\) and masses \(p_n\) proportional to \(2^{-3n/4}\).
On the product of circle \(n\) with itself, \(g\ge p_n/r_n^2\) almost everywhere by integrating curvature on the same circle.
If a positive finite-almost-everywhere \(w\) satisfied \(T_gw\le Rw\) for finite \(R\), its integral \(I_n\) over each circle would be finite, since \(T_gw\ge p_n I_n/r_n^2\) there.
Integration over that circle now gives \(R I_n\ge (p_n^2/r_n^2)I_n\).
Each \(I_n>0\), whereas \(p_n^2/r_n^2\to\infty\).
Thus no such weight exists, even though this actual scalar example has both full canonical domains.

### A small pair of atoms

Take an equilateral triangle of side one, with \(\kappa^2=c^2=3\), and set \(m_1=m_2=e,\ m_3=q=1-2e\), where \(0<e<1/3\).
Then \(g_{12}=qc^2\) and \(g_{13}=g_{23}=ec^2\).
The three edge equations force \(\alpha_{ij}=m_k(c^2-\lambda)/(m_i+m_j)\).
The positive matrix at vertex 3 has equal diagonals \(e(c^2-\lambda)/(1-e)\), so its eigenvalues imply \(\lambda\le e(c^2-\lambda)/(1-e)\), or \(\lambda\le e c^2\).
In particular
\[
    |z_1-z_2|^2\alpha_{12}
         \ge\frac{q(1-e)c^2}{2e}\longrightarrow\infty.
\]
Feasible choices exist at every fixed \(e\), for instance \(\lambda=0\) and the corresponding positive edge coefficients.
Also \(A(z_1)=A(z_2)=2e q c^2\) whereas \(|z_1-z_2|g_{12}=q c^2\).
Thus (1) itself can fail when \(\mu^2\) charges the coincident pair \(s=t\).

For the three-site jump Laplacian, the constant direction has eigenvalue zero, the direction \((1,-1,0)\) has eigenvalue \(3eqc^2\), and the remaining orthogonal direction \((q,q,-2e)\) has eigenvalue \(ec^2\), by substitution in the row formula.
The \((1,2)\) entry of the orthogonal projection onto the antisymmetric direction is \(-1/2\) in value coordinates.
The corresponding entry of the other nonconstant projection is \(q/2\), since the identity has entry zero there and the projection onto constants has entry \(e\).
The spectral theorem gives
\[
           b_{12}=\frac{c(\sqrt{3q}-q)}{2\sqrt e}.
\]
As \(e\downarrow0\), this diverges on an edge of fixed length one.
Actual normal conjugate variables force diffuse marginals, so the finite calculations concern the proposed certificates and leave the normal implication for unrestricted tuples unresolved. [Normal marginal diffuseness](Yin_C_F0076_v1.md#statement)

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:58 |
| status | open |
| reason | Fix the four-point and weighted curvature-row criteria, their actual diffuse examples and the finite-certificate obstructions for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Diffuse curvature and weighted-vacuum bounds, arbitrary mixed canonical domains under a weighted curvature-row condition, actual examples, and finite Gram and jump-square-root obstructions. |
| argument | [Argument](#argument) | Determinant estimates, weighted path propagation, energy recurrence, actual generator limits and mixed graphs, two diffuse examples and the three-site eigenspaces. |
| dependency | [Curvature row theorem](Yin_C_F0078_v2.md#statement) | The two original canonical domains when both marginal bounds hold. |
| dependency | [Original curvature energy](Yin_C_F0078_v1.md#argument) | Positive polynomial approximants, the finite-kernel row and vacuum recurrence, and the actual contracted mixed defect on analytic-core unitaries. |
| dependency | [Two-slice domain theorem](Yin_C_F0072_v1.md#statement) | Actual forward and adjoint bounded-vector domain conclusions from the two core bounds. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#statement) | The actual commutator vacuum and its joint spectral measure. |
| dependency | [Marginal tensor adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Actual adjoints for finite real symmetric liberation kernels and absolute continuity of the liberation spectral measure. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Finite total curvature for actual marginals and the scalar vacuum of the perpendicular segments. |
| dependency | [Commuting drift criterion](Yin_C_F0283_v1.md#statement) | Actual correlated pair on the segments and its explicit liberation spectral measure. |
| dependency | [Shrinking-circle obstruction](Yin_C_F0143_v1.md#statement) | Actual scalar law, both original domains and the within-circle lower bound. |
| dependency | [Normal diffuseness](Yin_C_F0076_v1.md#statement) | Exclusion of the finite atomic model as an actual normal conjugate-variable marginal. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T16:06 |
| status | proved |
| reason | Independent review verified the diffuse four-point bound, the weighted kernel iteration and both graph domains, including the examples and the finite three-site obstructions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Diffuse curvature and weighted-vacuum bounds, arbitrary mixed canonical domains under a weighted curvature-row condition, actual examples, and finite Gram and jump-square-root obstructions. |
| argument | [Argument](#argument) | Determinant estimates, weighted path propagation, energy recurrence, actual generator limits and mixed graphs, two diffuse examples and the three-site eigenspaces. |
| dependency | [Curvature row theorem](Yin_C_F0078_v2.md#statement) | The two original canonical domains when both marginal bounds hold. |
| dependency | [Original curvature energy](Yin_C_F0078_v1.md#argument) | Positive polynomial approximants, the finite-kernel row and vacuum recurrence, and the actual contracted mixed defect on analytic-core unitaries. |
| dependency | [Two-slice domain theorem](Yin_C_F0072_v1.md#statement) | Actual forward and adjoint bounded-vector domain conclusions from the two core bounds. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#statement) | The actual commutator vacuum and its joint spectral measure. |
| dependency | [Marginal tensor adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Actual adjoints for finite real symmetric liberation kernels and absolute continuity of the liberation spectral measure. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Finite total curvature for actual marginals and the scalar vacuum of the perpendicular segments. |
| dependency | [Commuting drift criterion](Yin_C_F0283_v1.md#statement) | Actual correlated pair on the segments and its explicit liberation spectral measure. |
| dependency | [Shrinking-circle obstruction](Yin_C_F0143_v1.md#statement) | Actual scalar law, both original domains and the within-circle lower bound. |
| dependency | [Normal diffuseness](Yin_C_F0076_v1.md#statement) | Exclusion of the finite atomic model as an actual normal conjugate-variable marginal. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0300_v1.md#finding) | Complete statement, all nine direct inputs and the limitations of the weighted sufficient condition. |

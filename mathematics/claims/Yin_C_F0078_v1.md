---
author: Yin
---
# Upper growth above dimension one restores normal canonical domains

Human author: Yin.
Root developed the curvature-kernel estimates, finite-composition application and normal-domain assembly.
The normal-branch agent checked the planar special-case constants and the proposed approximation interfaces while developing the separate row-kernel theorem C_F0077.
These are development contributions, not an independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \((M,\tau)\) be finite with faithful normal probability trace, \(H=L^2(M,\tau)\), \(\Omega=1\), and let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of \(M\).
Write \(\mathcal A=\mathbb C\langle X,X^*\rangle\) for the represented star algebra.
Suppose every marginal spectral probability \(\mu_i\), on \(K_i=\sigma(X_i)\), has constants \(C_i<\infty\) and \(1<\alpha_i<2\) such that
\[
 \mu_i(\overline B(z,r))\le C_i r^{\alpha_i}
 \quad(z\in K_i,\ r>0).                                      \tag{1}
\]
No freeness or other restriction on the joint law is imposed.

Suppose the full ACSY condition \(\mathsf A(X)\): there are outer derivations
\[
 \delta_i:\mathcal A\subset H\longrightarrow H\otimes_2H,\qquad
 \delta_i X_j=\delta_{ij}1\otimes1,\qquad
 \xi_i=\delta_i^*(1\otimes1)\in H
                                                               \tag{2}
\]
for the actual Hilbert adjoints.
Inner products are linear in the second variable.
Then
\[
 E_{i,0}=(\mathrm{id}\otimes\tau)\delta_i,\qquad
 D_i=-\overline{E_{i,0}}
\]
are well-defined closable canonical operators and
\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
 \qquad [X_j,D_i]|_{M\Omega}=\delta_{ij}P_\Omega|_{M\Omega}.
                                                               \tag{3}
\]
Thus \(\mathsf A(X)\Longrightarrow\mathsf S(X)\Longrightarrow\mathsf F(X)\) in this class.
Since normal \(\mathsf S\Longrightarrow\mathsf A\) is already known, \(\mathsf A\) and \(\mathsf S\) are equivalent under (1).
No converse from \(\mathsf F\) alone is asserted.

In particular the result applies when every \(\mu_i\) has a bounded planar Lebesgue density and compact support.
More generally, (1) includes singular planar measures with upper growth of exponent greater than one.
No sharpness claim for the exponent is made.

For this class the existing normal fraction-commutator rationality criterion applies to the specified canonical closures in (3), with its complete natural domains and its one-fraction/every-fraction conclusions.
Its comparison with any supplied strong system is exactly C_F0075 Part 4; it is not equality of arbitrary unclosed fraction operators on different domains.

## Argument

### 1. Reused interfaces and what remains to prove

The local reuse pass examined C_F0044's marginal curvature estimate, C_F0045's free lifting, C_F0051/C_F0052's marginal density transfers, C_F0055/C_F0056, and L_F0011.
Those results establish scalar or free cases and the actual mixed-energy interface, not the present correlated growth theorem.
A bounded external search for normal conjugate variables, bounded densities and liberation kernels did not supply an exact theorem at this scope.
No novelty claim follows from that search.

We use [C_F0076](Yin_C_F0076_v1.md#statement) for the unique normal phase, actual common tensor-leg graph approximation and coassociativity on \(\mathcal A\).
We use [C_F0063 Appendix A](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) for the real partial-liberation derivation and its actual vacuum.
The new [C_F0077](Yin_C_F0077_v1.md#statement) supplies its finite-kernel energy identity and its uniform-row-L2 contraction theorem.
That input is applied only to finite bounded kernels with uniform bounds; a singular curvature weight below need not itself be a coarse L2 vector.

The sum-of-real-components energy mechanism was previously retained in [L_F0011](../ledger/Yin_L_F0011_v1.md#3-exact-sum-of-components-identity).
Section 6 below reconstructs its actual-domain and normalization use with the C_F0076 graph input.
It is not treating the open estimate in that earlier material as proved.

Fix one coordinate, suppress its index, and write \(Z=X_i\), \(\mu=\mu_i\), \(K=K_i\), \(\alpha=\alpha_i\), \(C_\mu=C_i\), and \(D=\operatorname{diam}K\).
Growth makes \(\mu\) nonatomic and \(D>0\).

### 2. Curvature and elementary composition estimates

Let \(\mathfrak c(z,w,v)\) be Menger curvature, zero for collinear triples and with arbitrary values on repeated-point null sets.
It equals the reciprocal circumradius for a nondegenerate triangle.
Hence
\[
 \mathfrak c(z,w,v)^2
 \le\frac4{\max(|z-v|,|z-w|)^2}.
\]
Put, off the diagonal,
\[
 g(z,v)=\int\mathfrak c(z,w,v)^2\,d\mu(w),\qquad g(z,z)=0.
\]
This is a nonnegative real symmetric kernel.
For \(r=|z-v|\), split the integral into the radius-r disk and the annuli \(2^k r<|z-w|\le2^{k+1}r\).
Assumption (1) gives
\[
 g(z,v)\le A r^{-b_0},\quad b_0=2-\alpha\in(0,1),\quad
 A=4C_\mu\left(1+\frac{2^\alpha}{1-2^{\alpha-2}}\right).
                                                               \tag{4}
\]
Annuli outside the support contribute zero; extending the upper bound to their infinite geometric sum is harmless.
In particular \(|z-v|g(z,v)\) is bounded by \(AD^{1-b_0}\).
The same growth assumption and inward annuli give
\[
 \sup_{z\in K}\int |z-v|^{-a}\,d\mu(v)<\infty
 \quad(0<a<\alpha).                                            \tag{5}
\]

We need a finite number of composition estimates, not a bound on the unweighted Hilbert norm of g.
If \(0<a<\alpha\), and
\[
 b>\max(2a-\alpha,0),
\]
then
\[
 \int |z-w|^{-a}|w-v|^{-a}\,d\mu(w)
       \le L_{a,b}|z-v|^{-b}\quad(z\ne v),                       \tag{6}
\]
with a finite constant depending on the displayed parameters, \(C_\mu,D\).

Here is an elementary verification, including the borderline case.
Set \(r=|z-v|\).
On \(|w-z|<r/2\), the other factor is at most \((2/r)^a\), while inward annuli bound the first integral by a constant times \(r^{\alpha-a}\).
The analogous region near v has the same bound.
Where both distances are at least \(r/2\) and \(|w-z|\le2r\), use \(O(r^{-2a})\) and mass \(O(r^\alpha)\).
On the remaining outward annuli, the two distances are comparable and the bound is a constant times
\[
 \sum_{r\lesssim t\lesssim D}t^{\alpha-2a}.
\]
This is \(O(r^{\alpha-2a})\) if \(2a>\alpha\), \(O(1+\log(D/r))\) if \(2a=\alpha\), and \(O(1)\) if \(2a<\alpha\).
Each is bounded by a constant times \(r^{-b}\) for the stipulated strict b.
This proves (6) using only the growth bound.
No unverified Hardy--Littlewood--Sobolev theorem is invoked.

There are exponents
\[
 0<b_n\le b_0<1,\qquad b_N<\alpha/2
                                                               \tag{7}
\]
for some finite N, with \(b_{n+1}>\max(2b_n-\alpha,0)\) whenever a next step is needed.
Explicitly, if \(b_0<\alpha/2\), take N=0.
Otherwise put \(\varepsilon=(\alpha-b_0)/4>0\), subtract \(\varepsilon\) at each step and stop at the first exponent below \(\alpha/2\).
Before that step all exponents are at least \(\alpha/2>\varepsilon\), and \(b_n-\varepsilon>2b_n-\alpha\).

Define \(G=g+1\).
Off the diagonal it has an upper bound \(A_0|z-v|^{-b_0}\), since \(1\le D^{b_0}|z-v|^{-b_0}\).
Repeated use of (6) gives finite constants \(L_n\) with
\[
 0\le G^{\circ 2^n}(z,v)\le L_n|z-v|^{-b_n},\qquad 0\le n\le N.
                                                               \tag{8}
\]
Here composition means integration over successive middle variables.
Nonnegativity and (5) justify these integrals by Tonelli; the bounds prove off-diagonal finiteness.
Consequently:
\[
 \sup_z\int G^{\circ 2^n}(z,v)\,d\mu(v)\le A_n<\infty,\qquad
 \sup_{z\ne v}|z-v|G^{\circ 2^n}(z,v)\le B_n<\infty,             \tag{9}
\]
and at the final step
\[
 \sup_z\int |G^{\circ 2^N}(z,v)|^2\,d\mu(v)\le m_N^2<\infty.
                                                               \tag{10}
\]
The last assertion uses \(2b_N<\alpha\) in (5).
This is why any fixed \(\alpha>1\) suffices after finitely many compositions.

### 3. Actual polynomial approximants and their vacuum vectors

Let \(\gamma\) be partial liberation: \(\gamma(n)=n\otimes1-1\otimes n\) on the distinguished marginal algebra and zero at the other starred coordinates.
Under (2) the actual real derivation
\[
 \beta=\mathrm i\gamma
      =\mathrm i I_{Z\otimes1-1\otimes Z}\delta
\]
has vacuum
\[
 \zeta=\beta^*(1\otimes1)=-\mathrm i[Z^*,\xi]\in H              \tag{11}
\]
by C_F0063's actual tensor-adjoint computation.
The inner insertion commutes with both outer actions.
All these statements start on the original \(\mathcal A\).

The kernel g is continuous off the diagonal on \(K^2\).
For an off-diagonal convergent pair, the curvature integrand converges for all w except its two marginal-null exceptional points and is uniformly bounded by \(4/r^2\) with r bounded away from zero.
Dominated convergence proves the assertion.

Choose continuous radial cutoffs, equal to zero near the diagonal and tending to one at every positive separation.
Multiplying g by such a cutoff gives a continuous nonnegative symmetric function on \(K^2\).
Approximate it uniformly by real symmetric marginal polynomial tensors, with error \(\epsilon_j\downarrow0\), and then add the scalar \(\epsilon_j\).
Choose \(2\epsilon_j\le1\).
The resulting finite polynomial tensors q_j obey
\[
 0\le q_j\le g+1=G\quad\hbox{off the diagonal},\qquad
 q_j(z,v)\longrightarrow g(z,v)\quad(z\ne v).                  \tag{12}
\]
Stone--Weierstrass on the compact product, followed by pointwise-real and variable-swap symmetrization, provides these tensors.
Their diagonal values are finite but irrelevant to the nonatomic coarse product measure.

For a finite real symmetric marginal tensor q, the actual vacuum of \(\beta_q=\mathrm i I_q\gamma\) is \(S_q\zeta\), by C_F0077's marginal adjoint formula.
In terms of the joint left/right spectral calculus on H, (11) gives
\[
 \eta_q=S_q\zeta
       =-\mathrm i S_{(\bar z-\bar v)q(z,v)}\xi.                \tag{13}
\]
This formula concerns a bounded spectral multiplier for each finite q.
For \(q_{j,n}=q_j^{\circ 2^n}\), (8)--(9) give
\[
 \|\operatorname{row}(q_{j,n})\|_2\le A_n,\qquad
 \|\eta_{q_{j,n}}\|_2\le B_n\|\xi\|_2,                         \tag{14}
\]
uniformly in j.
The spectral bounds in (9) hold at all off-diagonal points of \(K^2\), not just coarse almost everywhere.
The gap multiplier is zero on the diagonal, even if the spectral measure of xi has a diagonal part.
Thus (13)--(14) do not assume that that measure is absolutely continuous with respect to \(\mu^2\).

All q_{j,n} are finite real symmetric polynomial kernels.
Equation (10) gives a uniform row-L2 bound at level N.
These are exact hypotheses of C_F0077; no assertion that g itself is coarse L2 is being made.

### 4. Descending finitely many energy inequalities

Fix an analytic-core unitary \(u=a+\mathrm i\sqrt{1-a^2}\), with \(a=a^*\in\mathcal A\) and \(\|a\|<1\).
Write \(E_q=(\mathrm{id}\otimes\tau)\beta_q\).
The exact finite-kernel energy calculation (B0c)--(B0e) of C_F0077 yields the slightly uncompressed form
\[
 \|E_qu\|_2^2
 \le2\{\|\eta_q\|_2+\|\operatorname{row}(q)\|_2\}\|E_qu\|_2
       +\|E_{q\circ q}u\|_2.                                  \tag{15}
\]
This uses \(|\tau(\operatorname{row}(q)u^*E_qu)|\le\|\operatorname{row}(q)\|_2\|E_qu\|_2\); it does not replace that row norm by a possibly nonuniform \(\|q\|_2\).

At level N, C_F0077's uniform-row theorem, (10), and (14) give a finite uniform bound \(U_N\) for \(\|E_{q_{j,N}}u\|_2\), independent of j and u.
Its constants also use the fixed \(\|\zeta\|_2\), and the Hilbert norms at level N are bounded by \(m_N\).
For n=N-1 down to 0, put
\[
 U_n=B_n\|\xi\|_2+A_n+
       \sqrt{(B_n\|\xi\|_2+A_n)^2+U_{n+1}}.
\]
Equations (14)--(15) prove \(\|E_{q_{j,n}}u\|_2\le U_n\).
Hence
\[
 \|E_{q_j}u\|_2\le U_0                                       \tag{16}
\]
uniformly for the original analytic-core unitaries.
If N=0, only the direct uniform-row step is needed.
No infinite singular-kernel iteration or unidentified higher adjoint domain is used.

### 5. The limiting weighted derivation on the original star core

Define its generator values by
\[
 \beta_g(Z)=\mathrm i(z-v)g(z,v),\quad
 \beta_g(Z^*)=\mathrm i(\bar z-\bar v)g(z,v),\quad
 \beta_g(X_j)=\beta_g(X_j^*)=0\ (j\ne i).
                                                               \tag{17}
\]
The first two are bounded marginal tensors by (4).
Equations (12) and (4) show that the actual derivations \(\beta_{q_j}\) converge in the coarse Hilbert space at every starred generator.
Their Leibniz expansions therefore converge at every fixed original word.
Since a represented zero is annihilated by every \(\beta_{q_j}\), these limits define a well-defined real outer derivation on \(\mathcal A\).
This defines \(\beta_g\) without applying an unbounded insertion to the entire coarse space, or requiring g in coarse L2.

Similarly (13) converges in H to
\[
 \eta_g=-\mathrm i S_{(\bar z-\bar v)g}\xi.
\]
The multiplier sequence is uniformly bounded, converges at every off-diagonal point, and vanishes on the diagonal.
Dominated joint spectral convergence proves the assertion for the actual vector xi, even if its spectral measure is singular.
Passing vacuum pairings to the limit gives the actual vacuum \(\beta_g^*(1\otimes1)=\eta_g\).

For each fixed analytic u, convergence of the first-derivative binomial series follows from generator convergence, the uniform bound for \(\beta_{q_j}(a)\), and the summable estimate \(k\|a\|^{k-1}\).
Thus (16) passes to
\[
 E_g=(\mathrm{id}\otimes\tau)\beta_g,\qquad \|E_gu\|_2\le U_0.
                                                               \tag{18}
\]
Averaging u and u*, scaling and splitting real/imaginary parts gives \(\|E_gp\|_2\le2U_0\|p\|\) on \(\mathcal A\).
Passing the finite actual adjoint pairings gives \(E_g^*p=p\eta_g-E_gp\) there, so both the original closure and actual adjoint have all bounded vectors in their domains.
For the normal conclusion below only (18) is needed.

### 6. The actual normal mixed energy and both canonical domains

Put \(\epsilon=\delta^\#\), where the coarse involution is flip-star, and let
\[
 \delta_x=(\delta+\epsilon)/2,\qquad
 \delta_y=(\delta-\epsilon)/(2\mathrm i).
\]
They are real and have actual selfadjoint vacua
\[
 \zeta_x=(\xi+\xi^*)/2,\qquad
 \zeta_y=\mathrm i(\xi-\xi^*)/2,\qquad
 \|\zeta_x\|_2^2+\|\zeta_y\|_2^2=\|\xi\|_2^2.
\]
Write \(T_a=(\mathrm{id}\otimes\tau)\delta_a\) on \(\mathcal A\).
Its actual core adjoint is \(T_a^*p=p\zeta_a-T_ap\).

The actual mixed-iterate domains supplied by C_F0076 justify the following calculation on every original core element.
More explicitly, its common uniformly spatially bounded algebraic tensor approximants to the phases also approximate \(\delta_a p\) in all required tensor-leg graphs.
Partial tracing them gives uniformly operator-norm-bounded polynomial approximants to \(T_ap\) in the required first-derivative graph.
Their products with each fixed L2 vacuum converge in H.
Closedness of the actual adjoint graph therefore puts \(T_ap\) in its actual adjoint domain and gives \(T_a^*(T_ap)=(T_ap)\zeta_a-T_a(T_ap)\).
This is the actual-domain mechanism already recorded in L_F0011; a maximal divided-difference domain is not substituted for the original closure.

Let \(A_a=(\delta_a\otimes1)\delta_a-(1\otimes\delta_a)\delta_a\).
Contracting this identity and using the vacuum on the second leg gives
\[
 T_a^2p=(\mathrm{id}\otimes\tau\otimes\tau)A_ap
                +\Theta(\delta_ap)\zeta_a.
\]
Pairing with p, using the preceding actual adjoint, and expanding \(\delta_a(p^*p)\) yields the real-energy identity.
Its analytic-unitary limit is
\[
 V(u)^2
 =2\operatorname{Re}\sum_{a=x,y}\langle T_au,u\zeta_a\rangle
  -\operatorname{Re}\langle
       (\mathrm{id}\otimes\tau\otimes\tau)(A_x+A_y)u,u\rangle,
 \quad V(u)^2=\|T_xu\|_2^2+\|T_yu\|_2^2.                     \tag{19}
\]
The limit uses only the final identity and the first-derivative series for the defects, which are outer derivations.
It asserts no new second-iterate domain at u.

For precision about the curvature coefficient, set
\[
 S=(\delta\otimes1)\epsilon+(\epsilon\otimes1)\delta
       -(1\otimes\delta)\epsilon-(1\otimes\epsilon)\delta.
\]
Algebraically \(A_x+A_y=S/2\).
The normal phase is \(k(z,v)=(\bar z-\bar v)/(z-v)\).
Its actual second divided differences from C_F0076 give
\[
 S(Z)(z,w,v)=(z-v)\mathfrak c(z,w,v)^2,\qquad
 S(Z^*)(z,w,v)=(\bar z-\bar v)\mathfrak c(z,w,v)^2.
\]
For example translate v to zero, put \(a=z,b=w,N_0=\bar a b-\bar b a\).
The first expression is
\[
 \frac{-N_0}{\bar a\bar b(a-b)}
 -\frac{-N_0}{b\bar a(\bar a-\bar b)}
 =\frac{-N_0^2}{\bar a|b|^2|a-b|^2}
 =a\,\mathfrak c(a,b,0)^2.
\]
The second is its conjugate.
The other starred generators are annihilated.
The actual mixed defect is an outer derivation, since its cross Leibniz terms cancel.
Tracing its middle leg preserves that property.
Equality on all generators and (17) therefore give on the whole core, and on their analytic power-series values,
\[
 (\mathrm{id}\otimes\tau\otimes\tau)(A_x+A_y)
                 =-\frac{\mathrm i}{2}E_g.                    \tag{20}
\]
All identifications in (20) use actual Hilbert vectors.
The separate singular kernel g need not itself be a Hilbert tensor.

By (18)--(20) and Cauchy--Schwarz,
\[
 V(u)^2\le2\|\xi\|_2 V(u)+U_0/2,
 \qquad
 V(u)\le\|\xi\|_2+\sqrt{\|\xi\|_2^2+U_0/2}.                    \tag{21}
\]
Both \(E_0=(\mathrm{id}\otimes\tau)\delta=T_x+\mathrm iT_y\) and \(F_0=(\mathrm{id}\otimes\tau)\epsilon=T_x-\mathrm iT_y\) therefore have uniform bounds on analytic u.
The same averaging/scaling/real-imaginary decomposition gives operator-norm-to-H bounds on the whole original \(\mathcal A\).
The actual core adjoint
\[
 E_0^*p=p\xi-F_0p
\]
is bounded from that operator norm into H as well.

For any \(a\in M\), uniformly bounded Kaplansky approximants from \(\mathcal A\) converge in H to a.
The two bounds and the weakly closed graphs of \(\overline{E_0}\) and \(E_0^*\) place a in both actual domains.
Passing the core generator commutator through those same graph limits gives \([\,\overline{E_{i,0}},X_j\,]=\delta_{ij}P\) on M.
Negation proves (3) for each coordinate.
This proves \(\mathsf A\Longrightarrow\mathsf S\).
The converse is the accepted normal statement in C_F0070 Part C.

### 7. Planar densities and the rationality comparison

If \(\mu\le L\,dA\) and has compact support of positive diameter D, choose any \(1<\alpha<2\).
For \(r\le D\), \(\mu(\overline B(z,r))\le\pi L r^2\le\pi L D^{2-\alpha}r^\alpha\); for \(r>D\), use \(1\le D^{-\alpha}r^\alpha\).
Taking the larger of these constants verifies (1).
No lower density bound is needed.

For \(F_X=\operatorname{Div}_{L^0(M)}\mathbb C\langle X\rangle\), C_F0068 Part C now applies to the canonical operator-first closures \(\overline{E_{i,0}}\).
Their restrictions to M have closure equal to the original canonical closure, since the original polynomial core is contained in M.
For every \(u\in L^0(M)\) and every bounded regular fraction quadruple \(Q=(s,a,b,t)\), \(u=s^{-1}a=bt^{-1}\), rationality is equivalent to bounded finite-rank extension of each literal fraction commutator on its entire natural domain.
The one-common-Q and every-Q conditions and numerical rank independence are those of that exact input.

The generator-first \(D_i=-\overline{E_{i,0}}\) simply negate those fraction operators.
Thus their finite-rank properties and ranks are identical; when identifying the boundary equation in C_F0068's operator-first convention, its representative is the negative of the generator-first fraction commutator.
The rational algebra remains the unstarred \(F_X\).

C_F0075 Part 4 compares these canonical operators with every supplied strong system on M and gives the same bounded finite-rank closure for each fixed Q when the full natural-domain finite-rank condition holds.
It does not assert equality of unclosed natural domains or equality of representatives belonging to different Q.
The general maximal-Delta boundary criterion and the specified fraction-commutator test therefore have the same applicability on this class, with these exact operator and fraction quantifiers.

## Scope and remaining question

The added upper-growth condition is substantive.
Neither the normal ACSY hypothesis nor finite total marginal curvature is asserted to imply (1).
The theorem leaves the unrestricted correlated-normal comparison open, including singular dimension-one cases not covered by other accepted classes.
It also makes no claim for arbitrary nonnormal tuples.

The new application uses a finite number of kernel compositions with uniform approximant bounds.
It does not assume the original curvature kernel is in coarse L2, interchange arbitrary unbounded tensor products, or infer an actual vacuum from a merely formal moment identity.
All new claims are retained here pending independent review.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:33 |
| status | open |
| reason | Complete candidate deriving correlated normal canonical full domains from upper growth of exponent greater than one, via finite curvature-kernel composition and actual target-core limits; independent review pending. |

Recorded authoring stage: proof draft.
Recorded review label: self-reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact growth and ACSY premises, both canonical domains, normal A/S equivalence, planar-density case and fraction-criterion scope. |
| argument | [Argument](#argument) | Seven sections: elementary growth/composition estimates, finite approximants, actual vacua, descending energy bounds, normal mixed-domain calculation and exact rationality application. |
| dependency | [Weighted liberation theorem](Yin_C_F0077_v1.md#statement) | Only actual finite symmetric kernel vacua, exact finite energy identity and the uniform-row-L2 theorem at the final finite-composition level. |
| dependency | [Actual normal phase graphs](Yin_C_F0076_v1.md#statement) | Unique phase and actual common bounded tensor-leg graph approximation, all mixed iterates and pure coassociativity. |
| dependency | [Actual liberation construction](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Original-core real partial liberation and the actual vacuum -i[Z*,xi]; no inverse-liberation bound is imported. |
| dependency | [Normal strong-to-ACSY interface](Yin_C_F0070_v1.md#statement) | Part C for the converse S-to-A; the universal Hilbert-Schmidt tensor convention for the displayed energy contractions. |
| dependency | [Normal fraction realization](Yin_C_F0068_v1.md#dual-specializations) | Part C with the proved operator-first canonical domains; whole natural domains, one/every fraction, rank and maximal-Delta criterion conventions. |
| dependency | [Canonical comparison](Yin_C_F0075_v1.md#statement) | Part 4 for every supplied strong system and each fixed complete fraction pair, with the stated limits on unclosed operators. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:45 |
| status | proved |
| reason | Adopt the complete proof after R_F0051 independently checked all growth exponents, finite composition estimates, actual original graph domains, both canonical domains and the exact fraction-criterion comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact growth and ACSY premises, both canonical domains, normal A/S equivalence, planar-density case and fraction-criterion scope. |
| argument | [Argument](#argument) | Seven sections: elementary growth/composition estimates, finite approximants, actual vacua, descending energy bounds, normal mixed-domain calculation and exact rationality application. |
| dependency | [Weighted liberation theorem](Yin_C_F0077_v1.md#statement) | Only actual finite symmetric kernel vacua, exact finite energy identity and the uniform-row-L2 theorem at the final finite-composition level. |
| dependency | [Actual normal phase graphs](Yin_C_F0076_v1.md#statement) | Unique phase and actual common bounded tensor-leg graph approximation, all mixed iterates and pure coassociativity. |
| dependency | [Actual liberation construction](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Original-core real partial liberation and the actual vacuum -i[Z*,xi]; no inverse-liberation bound is imported. |
| dependency | [Normal strong-to-ACSY interface](Yin_C_F0070_v1.md#statement) | Part C for the converse S-to-A; the universal Hilbert-Schmidt tensor convention for the displayed energy contractions. |
| dependency | [Normal fraction realization](Yin_C_F0068_v1.md#dual-specializations) | Part C with the proved operator-first canonical domains; whole natural domains, one/every fraction, rank and maximal-Delta criterion conventions. |
| dependency | [Canonical comparison](Yin_C_F0075_v1.md#statement) | Part 4 for every supplied strong system and each fixed complete fraction pair, with the stated limits on unclosed operators. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0051_v1.md#conclusion) | Entire statement and seven-section argument, with all six direct dependency scopes and full natural-domain/fraction quantifiers. |


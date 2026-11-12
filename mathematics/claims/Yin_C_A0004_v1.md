---
author: Yin
---
# Embedded decoration atoms and geometric coupling certificates

Date: 2026-11-11 (Asia/Hong_Kong).
This argument serves [S_A0006](../strategies/Yin_S_A0006.md) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
The main agent and two development helpers calculated the embedded-decoration model and its geometric extension for Yin.
Provenance: project deduction, using the already reviewed regular-transport certificate for the geometric application.
No new Atiyah group class or historical priority is claimed.

## Statement

Let \(G=\mathbb Z^2=\langle u,v\rangle\), let \(\tau\) be the canonical group trace, and set
\[
a=v+v^{-1},\qquad b=1-u,\qquad
H=\begin{pmatrix}a&b&b\\b^*&0&0\\b^*&0&0\end{pmatrix}.
\tag{1}
\]
Use \((z-H)^{-1}\), with \(z\in\mathbb C_+\), throughout.
Let \(P_e\) project onto the three coordinates at the identity group element, and define the complete one-cell Green matrix and its spectral-parameter first-return matrix by
\[
G_e(z)=P_e(z-H)^{-1}P_e,\qquad
\mathcal K_e(z)=zI_3-G_e(z)^{-1}.
\tag{2}
\]
The inverse in (2) acts on \(P_e\ell^2(G)^3\cong\mathbb C^3\).
This is the first-return convention specified in the argument below, rather than a scalar trace followed by inversion.

The following conclusions hold.

1. The complete Green matrix and first-return matrix are given by (5)--(8) below.
   The zero spectral projection is the constant matrix
   \[
   P_0=\begin{pmatrix}0&0&0\\0&1/2&-1/2\\0&-1/2&1/2\end{pmatrix}.
   \tag{3}
   \]
   Thus the unnormalized kernel dimension is \(1\), and the probability spectral law \(\mu_H\), defined using \(\operatorname{Tr}_3\otimes\tau\) divided by \(3\), has zero atom \(1/3\).
2. The complementary two-channel block has purely absolutely continuous spectral law, spectrum \([-4,4]\), and no zero eigenvector.
   Its unnormalized density satisfies (13), and the exact imaginary-axis asymptotics of the complete Green and first-return matrices are (11)--(12).
   In particular the continuous Green singularity is of order \(\eta^{-1/2}\), whereas the atom contributes \(1/(i\eta)\).
   The operator residues converge strongly to \(P_0\), but not in operator norm; their one-cell compressions do converge in matrix norm.
3. For any torsion-free discrete group, let \(D_\Gamma\colon\ell^2(G)^N\to\ell^2(G)^E\) be the finite regular-transport incidence operator from [C_A0003](Yin_C_A0003_v1.md#finite-graph-certificate), with no flat connected component.
   For every bounded selfadjoint \(A\in M_N(\mathcal N(G))\) and every real \(\lambda\), the block operator
   \[
   \mathcal H=\begin{pmatrix}A&D_\Gamma^*\\D_\Gamma&\lambda I_E\end{pmatrix}
   \tag{4}
   \]
   satisfies \(\ker(\mathcal H-\lambda)=0\oplus\ker D_\Gamma^*\) and has unnormalized atom \(E-N\) at \(\lambda\).
   For group-ring \(A\), this is an explicit sufficient condition within A0001, without a spectral-gap or commutation assumption.
   The extensions with flat components and the repeated-leaf specialization are stated and proved below.

## Current assessment

[Selected decision](#decision-reviewed-embedded-atoms)

## Assessment history

### Decision reviewed-embedded-atoms

| Field | Value |
| --- | --- |
| date | 2026-11-11T13:35 |
| status | proved |
| reason | Independent whole-argument inspection supports the complete matrix return calculation, embedded-atom boundary constants and geometric sufficient conditions, with the declared source and generality limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete model, spectral and boundary conclusions, incidence atom certificate and stated extensions. |
| argument | [Argument](#argument) | Exact transforms, justified endpoint limits, full trace normalization, bounded kernel calculations and geometric scope obstruction. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0017_v1.md#whole-artifact-finding) | Complete statement and argument, exact accepted input interfaces, source roles and restrictions. |
| dependency | [Regular-transport certificate](Yin_C_A0003_v1.md#finite-graph-certificate) | Exact incidence kernel dimension and actual-loop flatness criterion, proved in the selected tree-transport argument and independently reviewed there. |
| dependency | [Finite-trace support identities](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Exactly the finite-trace support identities recorded with Lemmas 5.1--5.5: equal traces of rectangular polar supports and the resulting kernel/cokernel dimension subtraction; no general integer-rank premise. |

## Argument

<a id="complete-resolvent"></a>
### Symmetric coordinates and the complete resolvent

Write the coordinate order as root, symmetric leaf, antisymmetric leaf, with the two leaf vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\).
The corresponding constant unitary \(U\) gives
\[
U^*HU=B\oplus0,\qquad
B=\begin{pmatrix}a&\sqrt2b\\\sqrt2b^*&0\end{pmatrix}.
\]
Under Fourier transformation put \(u=e^{i\theta}\), \(v=e^{i\phi}\), and
\[
a=2\cos\phi,\qquad c=2|b|^2=4-4\cos\theta,\qquad D=z^2-az-c.
\]
The variables \(a,c\) are independent with probability densities
\[
d\nu(a)=\frac{\mathbf1_{(-2,2)}(a)\,da}{\pi\sqrt{4-a^2}},\qquad
d\omega(c)=\frac{\mathbf1_{(0,8)}(c)\,dc}{\pi\sqrt{c(8-c)}}.
\]
The fiber resolvent, in the original coordinates, is exactly
\[
(z-H(\theta,\phi))^{-1}=
\begin{pmatrix}
z/D&b/D&b/D\\
\bar b/D&(z-a)/(2D)+1/(2z)&(z-a)/(2D)-1/(2z)\\
\bar b/D&(z-a)/(2D)-1/(2z)&(z-a)/(2D)+1/(2z)
\end{pmatrix}.
\tag{5}
\]
Define
\[
k(z)=\iint\frac{z}{D}\,d\nu\,d\omega,\qquad
j(z)=\iint\frac{z-a}{D}\,d\nu\,d\omega,\qquad
\ell(z)=\frac{zj(z)-1}{2\sqrt2},\qquad
\Delta(z)=k(z)j(z)-\ell(z)^2.
\]
The odd imaginary part of \(b=1-e^{i\theta}\) integrates to zero, and \(\operatorname{Re}b=c/4\).
Since \(zj-1=\iint c/D\), (5) yields
\[
U^*G_e(z)U=
\begin{pmatrix}k&\ell&0\\\ell&j&0\\0&0&1/z\end{pmatrix},\qquad
G_e(z)=\begin{pmatrix}
k&\ell/\sqrt2&\ell/\sqrt2\\
\ell/\sqrt2&(j+1/z)/2&(j-1/z)/2\\
\ell/\sqrt2&(j-1/z)/2&(j+1/z)/2
\end{pmatrix}.
\tag{6}
\]
For a one-dimensional integral with fixed branch convention, set
\(g_{\rm arc}(w)=\int(w-a)^{-1}d\nu(a)=1/\sqrt{w^2-4}\), analytic in \(\mathbb C_+\) and asymptotic to \(1/w\).
Because \(\gamma_c(z)=z-c/z\) belongs to \(\mathbb C_+\), the same functions are
\[
k(z)=\int g_{\rm arc}(\gamma_c(z))d\omega(c),\qquad
j(z)=\frac1z+\int\frac{c}{z^2}g_{\rm arc}(\gamma_c(z))d\omega(c).
\tag{7}
\]
These formulas are valid throughout \(\mathbb C_+\); no continuation of a return series outside its convergence disk is being assumed.

<a id="complete-first-return"></a>
### Which first-return matrix is being computed

For a bounded selfadjoint operator \(T\), an orthogonal projection \(P\), and \(Q=I-P\), use
\[
f_P(t)=PT(I-tQT)^{-1}P,\qquad
s_P(t)=P(I-tT)^{-1}P.
\]
The [GV17 convention and renewal identity](../ledger/Yin_L_A0017_v1.md#first-return-functions) give \(s_P(t)^{-1}=I_P-tf_P(t)\).
For \(z\in\mathbb C_+\), its spectral-parameter form, also obtained directly by a bounded block Schur complement, is
\[
\mathcal K_P(z)=f_P(1/z)
=PTP+PTQ(z-QTQ)^{-1}QTP
=zI_P-[P(z-T)^{-1}P]^{-1}.
\]
The middle resolvent acts on \(Q\mathcal H\).
Thus no inverse at a real spectral point is required.
For the finite cell \(P=P_e\), \(-\operatorname{Im}G_e(z)\) is positive definite: its quadratic form on a nonzero cell vector \(\xi\) is \((\operatorname{Im}z)\|(z-H)^{-1}\xi\|^2>0\).
Consequently \(G_e\) is invertible, \(\Delta\ne0\), and the complete answer is
\[
U^*\mathcal K_e(z)U=
\begin{pmatrix}
z-j/\Delta&\ell/\Delta&0\\
\ell/\Delta&z-k/\Delta&0\\
0&0&0
\end{pmatrix}.
\tag{8}
\]
Equations (6)--(8) include every off-diagonal cell return amplitude.

There are also useful, different projections onto all root sites or all leaf sites.
For the full root layer, the operator-valued function is \(f_{\rm root}(t)=a+2tbb^*\).
For the full two-leaf layer it is
\[
f_{\rm leaves}(t)
=t\,b^*(I-ta)^{-1}b\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{9}
\]
Initially these are power-series identities near \(t=0\), and their spectral forms extend for nonreal \(z\).
Equation (9) keeps the cross-leaf return terms and annihilates the antisymmetric leaf vector.
It remains valid without commutation of \(a\) and \(b\).
Taking an entrywise group trace in (9) is not the same operation as computing (8): compression and inversion do not commute.

<a id="embedded-atom"></a>
### The atom and the continuous complement

The fiber eigenvalues of \(B\) are
\[
\lambda_\pm(a,c)=\frac{a\pm\sqrt{a^2+4c}}2.
\]
For \(c>0\) they have opposite signs and are nonzero.
Since \(\omega(\{0\})=0\), \(\ker B=0\), and the zero projection of \(H\) is exactly (3).
The antisymmetric translates of \((0,1,-1)/\sqrt2\) are an orthonormal, finitely supported generating family for this kernel.
The root spectral measure has no part of this atom; each original leaf diagonal has atom \(1/2\), and the off-diagonal leaf residue is \(-1/2\).

For each fixed \(a\), the maps \(c\mapsto\lambda_\pm(a,c)\) are smooth with nonzero derivative on \((0,8)\).
The two pushforwards of the absolutely continuous measure \(\omega\), followed by integration in \(a\), are absolutely continuous.
This proves the assertion for the unnormalized spectral law \(\mu_B\) of total mass \(2\); positive matrix spectral measures are dominated by their scalar trace measure.
The ranges of the positive and negative branches, including their endpoints, are \([0,4]\) and \([-4,0]\).
Every neighborhood of a point in these ranges has a preimage of positive torus measure, including at the endpoints by continuity.
Thus the spectrum of \(B\) is exactly \([-4,4]\), and zero lies in its continuous spectrum.

The spectral theorem gives
\[
i\eta(i\eta-H)^{-1}\longrightarrow P_0\quad\hbox{strongly},\qquad
i\eta G_e(i\eta)\longrightarrow P_0\quad\hbox{in }M_3(\mathbb C).
\tag{10}
\]
The bounded spectral multipliers have modulus at most one and converge pointwise to the zero-eigenspace indicator, justifying the strong limit by dominated convergence.
On the complementary block their operator norm is exactly one for every \(\eta>0\), since \(0\in\sigma(B)\).
Hence the first limit in (10) is not operator-norm convergence.

<a id="boundary-asymptotics"></a>
### Exact boundary orders and constants

For \(\eta>0\), put
\[
K_\eta(c)=\sqrt{(c+\eta^2)^2+4\eta^2},\quad
A_\eta=\int\frac{d\omega(c)}{K_\eta(c)},\quad
J_\eta=\int\left(1-\frac{c}{K_\eta(c)}\right)d\omega(c).
\]
Averaging the arcsine variable in (7) gives exactly
\[
k(i\eta)=-i\eta A_\eta,\quad
j(i\eta)=-iJ_\eta/\eta,\quad
\ell(i\eta)=-(1-J_\eta)/(2\sqrt2).
\]
Define the positive constants
\[
\alpha=\frac{\Gamma(1/4)^2}{8\pi^{3/2}},\qquad
\beta=\frac{\Gamma(3/4)^2}{\pi^{3/2}},\qquad
d_0=\alpha\beta+\frac18=\frac{\pi+2}{8\pi}.
\]
Then, as \(\eta\downarrow0\),
\[
A_\eta\sim\alpha\eta^{-1/2},\qquad J_\eta\sim\beta\eta^{1/2},\qquad
U^*G_e(i\eta)U=
\begin{pmatrix}
-i\alpha\sqrt\eta(1+o(1))&-1/(2\sqrt2)+O(\sqrt\eta)&0\\
-1/(2\sqrt2)+O(\sqrt\eta)&-i\beta/\sqrt\eta(1+o(1))&0\\
0&0&1/(i\eta)
\end{pmatrix}.
\tag{11}
\]
In particular \(\Delta(i\eta)\to-d_0\), and (8) implies
\[
(U^*\mathcal K_e(i\eta)U)_{00}\sim-i\frac\beta{d_0}\eta^{-1/2},\qquad
(U^*\mathcal K_e(i\eta)U)_{ss}\sim-i\frac\alpha{d_0}\eta^{1/2},\qquad
(U^*\mathcal K_e(i\eta)U)_{0s}\longrightarrow\frac1{2\sqrt2d_0}.
\tag{12}
\]
The antisymmetric row and column in (8) vanish identically.

Here are convergent-integral justifications of the asymptotics, rather than a formal expansion at the singular endpoint.
In the part \(0<c<\delta<8\), substitute \(c=\eta t\).
After multiplication by \(\sqrt\eta\), the integrand for \(A_\eta\) converges to \((\pi\sqrt8)^{-1}t^{-1/2}/\sqrt{t^2+4}\).
The tail above \(t=M\) is bounded by a constant times \(M^{-1/2}\), uniformly for small \(\eta\); the part \(c\ge\delta\) becomes negligible.
For \(J_\eta/\sqrt\eta\), the limiting integrand is \((\pi\sqrt8)^{-1}t^{-1/2}(1-t/\sqrt{t^2+4})\).
For \(c\ge M\eta\) and \(\eta\le1\), rationalizing the difference gives
\[
0\le1-c/K_\eta(c)\le C\left(\frac{\eta^2}{c}+\frac{\eta^2}{c^2}\right).
\]
Its scaled tail on \([M\eta,\delta]\) is \(O(\eta M^{-1/2}+M^{-3/2})\), and the integrable endpoint near \(8\) contributes \(O(\eta^{3/2})\).
On bounded \(t\)-intervals the dominating function is a constant times \(t^{-1/2}\).
These estimates justify both limits.
The two remaining integrals evaluate to
\[
\frac1{\pi\sqrt8}\int_0^\infty\frac{t^{-1/2}}{\sqrt{t^2+4}}dt=\alpha,\qquad
\frac1{\pi\sqrt8}\int_0^\infty t^{-1/2}\left(1-\frac t{\sqrt{t^2+4}}\right)dt=\beta.
\]
For example, set \(t=2x\) in each integral and integrate the second by parts; the resulting beta integrals give the displayed gamma values.
The reflection identity \(\Gamma(1/4)\Gamma(3/4)=\pi\sqrt2\) gives \(\alpha\beta=1/(4\pi)\).

<a id="continuous-density"></a>
### Density accumulation and reciprocal slopes

For \(0<x<2\), the change of variable \(c=x(x-a)\) in the positive eigenvalue branch gives
\[
\rho_B(x)=\int_{-2}^{x}
\frac{2x-a}{\pi\sqrt{4-a^2}}\,
\frac{da}{\pi\sqrt{x(x-a)[8-x(x-a)]}}.
\]
The density is even by \((a,x)\mapsto(-a,-x)\).
Multiplying by \(\sqrt x\) and taking \(x\downarrow0\) yields
\[
\rho_B(x)\sim d\,|x|^{-1/2},\qquad
d=\frac1{\pi\sqrt8}\int_{-2}^{0}\sqrt{-a}\,d\nu(a)
=\frac{\Gamma(3/4)}{\pi^{3/2}\Gamma(1/4)}
=\frac\beta{\pi\sqrt2}.
\tag{13}
\]
To justify this limit, first restrict to \(-2<a<-\delta\), where the limiting integrand is dominated by a constant times \((a+2)^{-1/2}\).
For \(-\delta<a<x\), the rescaled integrand is bounded by a constant times \((2x-a)/\sqrt{x-a}\).
Its integral is \(O((x+\delta)^{3/2}+x\sqrt{x+\delta})\), which vanishes after first taking \(x\downarrow0\) and then \(\delta\downarrow0\).
The constant follows by \(-a=2\sin t\) and a beta integral.
Consequently
\[
\mu_H((-\varepsilon,\varepsilon))
=\frac13+\frac{4d}{3}\sqrt\varepsilon+o(\sqrt\varepsilon),\qquad
g_H(i\eta):=\frac13\operatorname{Tr}_3G_e(i\eta)
=\frac1{3i\eta}-\frac{i\beta}{3\sqrt\eta}+o(\eta^{-1/2}).
\tag{14}
\]
There is continuous spectrum on both sides arbitrarily close to the atom.

For the symmetric scalar channel, \(j(i\eta)\to\infty\) in magnitude while \(i\eta j(i\eta)\to0\).
Its reciprocal obeys \(j(i\eta)^{-1}\to0\), but \(j(i\eta)^{-1}/(i\eta)\sim1/(\beta\sqrt\eta)\to\infty\); it therefore has no atom.
For the normalized full scalar law, \(g_H(i\eta)^{-1}/(i\eta)\to3\), the reciprocal of the atom mass.
The root Green function \(k(i\eta)\to0\) instead, with \(k(i\eta)\sim-i\alpha\sqrt\eta\).
These are three different boundary behaviors inside the same operator.
Off-diagonal entries are essential to the matrix inverse in (8), since their nonzero limit contributes \(1/8\) to \(d_0\).

<a id="geometric-integer-certificate"></a>
### A geometric integer certificate without a spectral gap

For a bounded equivariant operator \(D\colon\ell^2(G)^N\to\ell^2(G)^E\), assume first that \(D\) is injective.
The equations for a vector \((x,y)\in\ker(\mathcal H-\lambda)\), with (4), are
\[
(A-\lambda)x+D^*y=0,\qquad Dx=0.
\]
Injectivity forces \(x=0\), and the other equation becomes \(D^*y=0\).
Polar decomposition identifies the support projections of \(D^*D\) and \(DD^*\), with equal unnormalized traces.
Their common trace is \(N\), whence \(\dim_G\ker D^*=E-N\).
This proves (4) under an independently certified injectivity hypothesis; no bounded inverse or closed range is used.

For the finite graph of [C_A0003](Yin_C_A0003_v1.md#finite-graph-certificate), the operator is
\[
(D_\Gamma x)_e=\sqrt{c_e}\bigl(x_i-\zeta_e\lambda_G(g_e)x_j\bigr),
\qquad e=(i,j),\ c_e>0,\ |\zeta_e|=1.
\]
That reviewed result proves \(\dim_G\ker D_\Gamma=f\), where \(f\) counts connected components with every actual closed-walk transport equal to the identity.
In a nonflat component, a nonidentity transport \(\eta\lambda_G(g)\) forces the common transported vector to vanish: either \(g\ne e\) has infinite order, or \(g=e\) and \(\eta\ne1\).
Thus one exhibited nonidentity loop transport in each component is a concrete certificate for \(f=0\), yielding the integer \(E-N\) in (4).
This uses actual group equality, not equality of unreduced formal words, and is not asserted to be an effective algorithm for arbitrary group presentations.
The base \(A\) can be arbitrary selfadjoint, can couple different graph components, and need not commute with any transport.
The arithmetic comes from the graph certificate and finite-trace rank subtraction, rather than from the analytic regularity of the complementary resolvent.

There are useful extensions when \(f\) is not zero.
If \(A=\lambda I_N\), then the two kernel equations decouple, giving atom \(E-N+2f\).
If \(A-\lambda I_N\ge0\) and \(\ker(A-\lambda)\cap\ker D_\Gamma=0\), taking the inner product of the first equation with \(x\) gives \(x=0\), and the atom is \(E-N+f\).
A concrete instance of the latter condition is a nonnegative diagonal scalar potential on the vertex coordinates, with at least one strictly positive entry in each flat component.
The tree-transport form of a flat section makes this intersection test explicit.
These are sufficient conditions with their stated restrictions, not a formula for arbitrary \(A\) on flat components.

<a id="repeated-leaf-extension"></a>
### Repeated leaves over noncommuting groups

Let \(G\) be any discrete group containing an infinite-order element \(u\), take \(b=1-\zeta u\) with \(|\zeta|=1\), any bounded selfadjoint \(a\in\mathcal N(G)\), and \(r\ge1\) identical leaf couplings.
The resulting \((r+1)\)-coordinate matrix splits by a constant leaf unitary into
\[
\begin{pmatrix}a&\sqrt r\,b\\\sqrt r\,b^*&0\end{pmatrix}\oplus0_{r-1}.
\]
Both \(b\) and \(b^*\) are injective: on every coset of \(\langle u\rangle\), an eigenvector of the corresponding bilateral shift would have constant modulus and cannot lie in \(\ell^2\) unless zero.
The two active-block equations consequently force both coordinates to vanish.
The zero projection is
\[
\operatorname{diag}\left(0,I_r-\frac1r\mathbf1\mathbf1^*\right),
\]
with unnormalized trace \(r-1\) and normalized atom \((r-1)/(r+1)\).
Neither commutation of \(a\) with \(u\) nor a positive lower bound for \(|b|\) is needed.
For the pilot (1), \(D=(b^*,b^*)^{\mathsf T}\) is also the incidence operator of two loops at one vertex, both labelled \(u^{-1}\); it has \(E-N=2-1=1\).
The explicit \(\eta^{-1/2}\) asymptotics in (11) belong to the specified \(\mathbb Z^2\) model, and are not asserted for this noncommuting extension.

<a id="noncompact-edge-modes"></a>
### The certificate need not come from compact modes

For \(G=F(u,v)\), take the two different loop transports
\[
D=\begin{pmatrix}1-u^{-1}\\1-v^{-1}\end{pmatrix}.
\]
The same geometric criterion gives \(\dim_G\ker D^*=2-1=1\).
Nevertheless \(\ker D^*\) contains no nonzero finitely supported vector.
Indeed, \(D^*=(1-u,1-v)\) is the signed divergence on oriented generator edges of the free-group Cayley tree, with a harmless choice of edge orientation.
A nonzero finitely supported flow has a finite nonempty edge support, which is a forest and has a leaf in one of its nonempty components.
At that leaf, the zero-divergence equation forces the unique supported incident coefficient to vanish, a contradiction.
Therefore the zero atom in (4), with this \(D\), is carried by noncompact \(\ell^2\) edge modes.
This separates the incidence index from finite-support localization hypotheses and is a structured free-group calibration, not a new group case.

<a id="scope-and-obstruction"></a>
### Scope, source roles and the remaining obstruction

The complete model calculation is a direct Fourier and block-resolvent computation prompted by the [decoration comparison](../ledger/Yin_L_A0017_v1.md#decoration-and-invisible-modes).
SA00 is a related model source, not an input asserting the variable-coupling result proved here.
The first-return definition and renewal relation use GV17, arXiv:1702.04032v2, Definition 2.2 and Theorem 2.5; the bounded form used here is also derived by the displayed Schur complement.
This is precise source attribution and a checked convention, not a claim to have audited the entire source proof.
The graph application uses the exact accepted finite-graph theorem and argument of [C_A0003](Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators), with its [independent review](../audits/reviews/Yin_R_A0007_v1.md#claim-finding).
The support-trace equality is the finite-von-Neumann-algebra foundation already accepted in that Claim and in [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
The Cauchy-residue interpretation reuses the [boundary formulas](../ledger/Yin_L_A0015_v1.md#boundary-residues-and-reciprocal-slopes), and (10) supplies the required direct limit here.

The nonflatness condition is substantial.
For one vertex and one identity-labelled loop of phase one, \(D_\Gamma=0\), and (4) becomes \(\operatorname{diag}(A,\lambda)\).
Its atom is \(1+\dim_G\ker(A-\lambda)\), so an unrestricted statement for flat channels immediately reintroduces an unknown kernel dimension.
For several such vertices it contains the arbitrary matrix problem.
Finite graph size and a formal Schur identity alone therefore provide no universal integer certificate.

The next geometric problem is to identify further structured couplings whose kernel or cokernel has an independent transport or local-mode certificate, and to verify that arbitrary-matrix reductions preserve such structure before claiming broader coverage.
The present certificate already tolerates continuous spectrum accumulating at the atom, while the general A0001 contract remains unresolved.

---
author: Yin
---
# Signed edge potentials, Schur atoms and height certificates

Date: 2026-11-11 (Asia/Hong_Kong).
This variant serves [S_A0006](../strategies/Yin_S_A0006.md) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
It replaces the zero edge block of [C_A0004_v2](../claims/Yin_C_A0004_v2.md#statement) by an invertible signed scalar block.
The preceding variant and its reviewed conclusions retain their exact scope.
Provenance: project deduction, with two development helpers for the lattice and free-tree calculations, and a source-checked ordered-quotient criterion identified below.
No historical priority or new Atiyah group class is asserted.

## Statement

For \(G=\mathbb Z^2=\langle u,v\rangle\) or \(F(u,v)\), put
\[
U=u+u^{-1},\quad V=v+v^{-1},\quad b_1=1-u,\quad b_2=1-v,
\quad D=(b_1^*,b_2^*)^{\mathsf T},\quad J=\operatorname{diag}(1,-1),
\qquad H_e=\begin{pmatrix}V&D^*\\D&eJ\end{pmatrix},\quad e\in\mathbb R\setminus\{0\}.
\tag{1}
\]
Use the canonical group trace and unnormalized matrix traces unless divided by three.
Write \(G_e(z)=P_{\mathrm{id}}(z-H_e)^{-1}P_{\mathrm{id}}\), \(g_e=\operatorname{Tr}_3G_e/3\), and \(K_e=zI_3-G_e^{-1}\), with the same first-return convention as v2.
The subscript \(e\) in this variant denotes the real perturbation parameter, not a group element.

1. The zero-kernel Schur operator is
   \[
   S_e=\frac{T_e}{e},\qquad T_e=U+(e-1)V.
   \tag{2}
   \]
   Both models have zero kernel and no zero atom for every \(e\ne0\), although zero is a continuous-spectrum interior point.
   In fact neither model has any spectral atom.
2. Their complete cell Green matrices are (6) and (14).
   On the lattice, every \(e\ne0,2\) has a finite positive zero density and finite invertible cell Green boundary (8)--(9).
   At \(e=2\) the density is logarithmically divergent, with the complete matrix and first-return limits (10)--(12).
   On the free group the zero density is finite and strictly positive for every \(e\ne0\), with the explicit physical branch and full boundary (16)--(18).
3. For fixed nonzero \(e\), the full operator residues converge strongly to zero but have norm one for every positive imaginary parameter.
   The limits as \(e\to0\) and as the imaginary spectral parameter tends to zero do not commute.
4. The general invertible-edge Schur reduction, height-layer injectivity certificate and ordered-quotient source criterion below control structured kernels beyond \(DC_0D^*\) perturbations.
   Infinite collective holonomy alone does not retain the preceding integer index after this perturbation: the stated \(C_2*C_3\) example has a nonzero nonintegral kernel dimension.
   That last example has torsion and is not a counterexample to A0001.

## Current assessment

[Selected decision](#decision-reviewed-signed-edges)

## Assessment history

### Decision reviewed-signed-edges

| Field | Value |
| --- | --- |
| date | 2026-11-11T14:37 |
| status | proved |
| reason | Independent whole-argument inspection supports the signed-edge Schur reduction, both complete matrix calculations and all boundary limits, the height and ordered-quotient certificates, and the torsion obstruction within their stated hypotheses and source limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete four-part statement for both groups and every real nonzero parameter, with the separately stated structured extensions and torsion-free-contract boundary. |
| argument | [Argument](#argument) | Formulas (1)--(23), the complete physical-branch and critical-boundary derivations, all-atom exclusions, general projection and height arguments, and the torsion-free indicable scalar application. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0017_v3.md#whole-artifact-finding) | Exact complete statement and argument, including all sensitive subsection bindings, the final indicable application and source-attribution additions. |
| dependency | [Preceding incidence model](Yin_C_A0004_v2.md#statement) | Unchanged first-return convention, unperturbed kernel dimension and atom, and regular-transport injectivity; the collective-holonomy subsection supplies the old index in the torsion example. |
| dependency | [Tree and lattice transforms](../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms) | Accepted isotropic transforms and elliptic modulus normalization; the weighted pencil, matrix boundary and physical-branch arguments are proved here. |
| dependency | [Finite-trace support identities](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Rectangular polar-support trace equality and dimension subtraction, without integer-rank assumptions for arbitrary group-ring matrices. |

Additional direct source inputs are [Lin92 Theorem 4, pp. 50--51](https://math.uchicago.edu/~shmuel/L%5E2%20cohomology%20readings/Linnell,%20zerol2.pdf), [DLMF 19.12.1](https://dlmf.nist.gov/19.12.E1) and [DLMF 18.40.6](https://dlmf.nist.gov/18.40.E6).
They are accepted at the exact statement, convention and applicability scopes identified in the argument and independent review; their historical source derivations were not re-audited.
Lin92 supplies only the scalar ordered-quotient theorem, DLMF 19.12.1 supplies the complementary-modulus endpoint series, and DLMF 18.40.6 supplies the boundary-value formula applied to locally smooth weighted coarea densities.

## Argument

<a id="zero-schur-and-projection"></a>
### Zero Schur reduction and the complete kernel

More generally let \(A=A^*\in M_N(\mathcal N(G))\), let \(B=B^*\in M_E(\mathcal N(G))\) be boundedly invertible, and let \(D\in M_{E,N}(\mathcal N(G))\).
For \(\mathcal H=\begin{pmatrix}A&D^*\\D&B\end{pmatrix}\), the lower equation gives \(y=-B^{-1}Dx\), so
\[
\ker\mathcal H=\{(x,-B^{-1}Dx):x\in\ker S\},\qquad S=A-D^*B^{-1}D.
\tag{3}
\]
This is a bounded equivariant isomorphism with bounded inverse given by root-coordinate restriction.
If \(p=1_{\{0\}}(S)\) and \(W=(I_N,-B^{-1}D)^{\mathsf T}\), its exact orthogonal projection is
\[
P_{\ker\mathcal H}=Wp\,[pW^*Wp]^{-1}_{p}\,pW^*,\qquad
\dim_G\ker\mathcal H=\dim_G\ker S.
\tag{4}
\]
The inverse is on the \(p\)-corner, where \(pW^*Wp\ge p\); the zero corner gives zero.
Rectangular polar decomposition proves the dimension equality and avoids confusing an invertible congruence with a unitary equivalence of projections.
For (1), \(D^*JD=(2-U)-(2-V)=V-U\), proving (2).

The injectivity of \(D\) therefore no longer fixes the kernel to its cokernel.
In both current groups the old cokernel is nonzero, while \(eJ\) is invertible.
Consequently \(eJ\) cannot equal \(DC_0D^*\) for a bounded \(C_0\), since every latter operator annihilates \(\ker D^*\).

For \(z\in\mathbb C_+\), set \(d_1=z-e,d_2=z+e\), \(B_z=\operatorname{diag}(d_1,d_2)\), and
\[
F(z)=z-V-D^*B_z^{-1}D,\qquad R(z)=F(z)^{-1}.
\]
The imaginary part is
\(\operatorname{Im}F(z)=\eta[I+(2-U)/|d_1|^2+(2-V)/|d_2|^2]\ge\eta I\).
The same lower bound for the adjoint yields surjectivity.
The complete noncommuting block inverse is
\[
(z-H_e)^{-1}=
\begin{pmatrix}
R&RD^*B_z^{-1}\\
B_z^{-1}DR&B_z^{-1}+B_z^{-1}DRD^*B_z^{-1}
\end{pmatrix}.
\tag{5}
\]

<a id="lattice-matrices-and-regular-boundary"></a>
### Lattice matrices and regular zero boundary

Use \(U=2\cos\theta,V=2\cos\phi,x=2-U,y=2-V\), with independent uniform angles.
Here \(R_z=[z-V-x/d_1-y/d_2]^{-1}\) is a scalar Fourier multiplier.
Averaging the odd sine terms separately gives
\[
G_{e,Z}(z)=\begin{pmatrix}
\mathbb ER_z&\mathbb E(xR_z)/(2d_1)&\mathbb E(yR_z)/(2d_2)\\
\mathbb E(xR_z)/(2d_1)&d_1^{-1}+\mathbb E(xR_z)/d_1^2&\mathbb E(xyR_z)/(4d_1d_2)\\
\mathbb E(yR_z)/(2d_2)&\mathbb E(xyR_z)/(4d_1d_2)&d_2^{-1}+\mathbb E(yR_z)/d_2^2
\end{pmatrix}.
\tag{6}
\]
This and \(K_e=zI-G_e^{-1}\) determine the complete return matrix by explicit integrals.

For fixed \(\phi\), \(T_e=0\) has at most two \(\theta\) solutions, hence its Haar measure is zero.
Thus (3) proves \(\ker H_e=0\).
The characteristic polynomial is
\[
p(z;U,V)=z^3-(e^2+4)z+(z+e)U+[-z^2+z+e(e-1)]V.
\tag{7}
\]
For each fixed real \(\lambda\ne-e\), its coefficient of \(U\) is nonzero; at \(\lambda=-e\) it equals \(2e(2-V)\).
Fubini therefore excludes every spectral atom.

Put \(c=e-1,A_c=|c|\), and let \(I_0=\mathbb E\delta(T_e)\), \(I_{xy}=\mathbb E[xy\delta(T_e)]\), with delta notation denoting coarea density.
For \(e\ne0,2\), zero is a regular value of \(T_e\), since simultaneous vanishing of its derivatives on its zero set would require \(|c|=1\); when \(c=0\), the nonzero \(\theta\) derivative suffices.
Conditioning on \(\phi\) gives
\[
\mathbb E_\theta\delta(2\cos\theta+2c\cos\phi)
=\frac{\mathbf1_{|c\cos\phi|<1}}{2\pi\sqrt{1-c^2\cos^2\phi}}.
\]
For \(|c|<1\), direct integration, and for \(|c|>1\), exchange of variables followed by scaling, yield
\[
I_0=\frac{K(k)}{\pi^2\max(1,A_c)},\qquad
k=\frac{\min(1,A_c)}{\max(1,A_c)},\qquad
\rho_{e,Z}(0)=\frac{e^2+4}{3|e|}I_0>0.
\tag{8}
\]
Here \(K\) is the complete elliptic integral with modulus \(k\), and \(\rho_{e,Z}\) is the normalized probability density.
For \(c=0\), \(k=0\) and \(I_0=1/(2\pi)\).
The density is smooth near zero.
Indeed a zero fiber eigenvector is \(w=(1,-b_1^*/e,b_2^*/e)^{\mathsf T}\), its zero eigenvalue is simple because the edge block is invertible, and near its zero set
\(\lambda=eT_e/(e^2+x+y)+O(T_e^2)\).
The coarea formula and \((U,V)\mapsto(-U,-V)\) give
\(\mathbb E[x\delta(T_e)]=\mathbb E[y\delta(T_e)]=2I_0\), proving (8).

Define the unnormalized cell density matrix
\[
\mathcal D_Z=|e|\begin{pmatrix}
I_0&-I_0/e&I_0/e\\
-I_0/e&2I_0/e^2&-I_{xy}/(4e^2)\\
I_0/e&-I_{xy}/(4e^2)&2I_0/e^2
\end{pmatrix}.
\]
It equals \(|e|\mathbb E[ww^*\delta(T_e)]\) and is positive definite.
To see strictness, choose an open zero-curve piece where both sine coordinates are nonzero, and change their signs separately.
A constant vector orthogonal to every \(w\) on those pieces must have both edge coordinates zero and then root coordinate zero.

For the principal values \(A_u=\operatorname{PV}\mathbb E(U/T_e)\), \(A_v=\operatorname{PV}\mathbb E(V/T_e)\), conditioning on the larger arcsine variable gives
\[
(A_u,A_v)=\begin{cases}(1,0),&0<e<2,\\(0,(e-1)^{-1}),&e<0\text{ or }e>2.\end{cases}
\]
The underlying identity is that the principal-value Cauchy transform of \(2\cos\theta\) has zero real part in \((-2,2)\), which also follows from its elementary square-root transform.
The full boundary is
\[
G_{e,Z}(0+i0)=
\begin{pmatrix}
0&-A_u/2&A_v/2\\
-A_u/2&(A_u-1)/e&-(A_u+A_v)/(2e)\\
A_v/2&-(A_u+A_v)/(2e)&(1+A_v)/e
\end{pmatrix}-i\pi\mathcal D_Z.
\tag{9}
\]
For example, \(\operatorname{PV}\mathbb E(1/T_e)=\operatorname{PV}\mathbb E(UV/T_e)=0\), so \(\operatorname{PV}\mathbb E(xy/T_e)=-2(A_u+A_v)\); substitution in (6) proves the cross term as well as the diagonals.
Smooth coarea densities and the scalar [Sokhotski boundary formula, DLMF 18.40.6](https://dlmf.nist.gov/18.40.E6), justify the limits, also with these bounded Fourier weights.
That directly checked formula fixes the principal-value term and the sign \(-i\pi\) for the convention \((z-t)^{-1}\); its source proof was not re-audited.
The strict density positivity makes (9) invertible; hence \(K_{e,Z}(i\eta)\to-G_{e,Z}(0+i0)^{-1}\).
In particular \(g_{e,Z}(0+i0)=(A_u+A_v)/(3e)-i\pi\rho_{e,Z}(0)\), and \(\mu_{e,Z}((-\delta,\delta))=2\rho_{e,Z}(0)\delta+O(\delta^2)\).

<a id="lattice-critical-boundary"></a>
### Lattice critical parameter and complete logarithmic boundary

The only nonzero critical parameter is \(e=2\), where \(T=U+V\) has two zero saddles, at \((0,\pi)\) and \((\pi,0)\).
The preceding zero-eigenvalue relation has \(\lambda=T/4+O(T^2)\) at either saddle.
The elementary local saddle integral, or the [exact square-lattice density](../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms), gives
\[
\rho_{2,Z}(s)=\frac2{3\pi^2}\log\frac1{|s|}+O(1),\qquad
\mu_{2,Z}((-\delta,\delta))=\frac4{3\pi^2}\delta\log\frac1\delta+O(\delta).
\tag{10}
\]
For a direct check of the full boundary constants, factor (7) as
\[
p(z)=(z+2)[U+(1-\kappa(z))V-\omega(z)],\quad
\kappa(z)=\frac{z^2}{z+2},\quad \omega(z)=\frac{8z-z^3}{z+2}.
\]
Then \(R_z=(2-z)\widetilde R_z\), where \(\widetilde R_z=[\omega-U-(1-\kappa)V]^{-1}\).
On \(z=i\eta\), \(\omega=4i\eta+O(\eta^2)\), \(\kappa=O(\eta^2)\).
Comparison with \((4i\eta-T)^{-1}\) has uniformly comparable denominators and weighted expectation error at most
\(C\eta^2\mathbb E(T^2+16\eta^2)^{-1}=O(\eta\log(1/\eta))\), for every bounded multiplier used in (6).
The [accepted lattice transform](../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms) and [DLMF 19.12.1](https://dlmf.nist.gov/19.12.E1) give
\(g_T(4i\eta)=-i\log(4/\eta)/(2\pi)+o(1)\).
Symmetry and \(\mathbb E[T(4i\eta-T)^{-1}]=4i\eta g_T(4i\eta)-1\) imply
\(\mathbb E[U\widetilde R_z]=\mathbb E[V\widetilde R_z]=-1/2+o(1)\).
Thus \(\mathbb E(xR_z)=\mathbb E(yR_z)=4g_T(4i\eta)+1+o(1)\).
For the remaining entry, direct arcsine integration gives \(\mathbb E[xy\delta(T)]=4/\pi^2\), while \(xy=4-2T+UV\) and parity give \(\operatorname{PV}\mathbb E(xy/T)=-2\).
Consequently \(\mathbb E(xyR_z)\to4-8i/\pi\).

Let
\[
B_0=\begin{pmatrix}1&-1/2&1/2\\-1/2&1/2&0\\1/2&0&1/2\end{pmatrix},\qquad
J_0=\begin{pmatrix}0&-1/4&1/4\\-1/4&-1/4&-1/4+i/(2\pi)\\1/4&-1/4+i/(2\pi)&3/4\end{pmatrix}.
\]
Substitution in (6) yields
\[
G_{2,Z}(i\eta)=-\frac{i}{\pi}\log(4/\eta)B_0+J_0+o(1),\qquad
g_{2,Z}(i\eta)=\frac16-\frac{2i}{3\pi}\log(4/\eta)+o(1).
\tag{11}
\]
The nullspace of \(B_0\) is spanned by \(n=(1,1,-1)^{\mathsf T}\), and \(n^*J_0n=-i/\pi\).
Schur inversion along this line and its orthogonal complement therefore gives
\[
G_{2,Z}(i\eta)^{-1}\longrightarrow i\pi nn^*,\qquad
K_{2,Z}(i\eta)\longrightarrow-i\pi nn^*.
\tag{12}
\]
The logarithmic Green divergence supplies no zero residue and no first-return pole.

<a id="free-cavities-and-physical-branch"></a>
### Free-tree full matrices and physical boundary branch

In (5) write
\[
F(z)=w-pU-qV,\quad
w=z-2/d_1-2/d_2,\quad p=-1/d_1,\quad q=1-1/d_2.
\]
On each deleted-edge subtree the imaginary-part estimate for \(F\) remains valid: the separate \(U,V\) compressions have norm at most two.
Thus the actual analytic cavity functions satisfy
\[
h_u=(w-p^2h_u-2q^2h_v)^{-1},\quad
h_v=(w-2p^2h_u-q^2h_v)^{-1},\quad
g=(w-2p^2h_u-2q^2h_v)^{-1}.
\tag{13}
\]
These are analytic squares, not absolute squares.
Set \(x_F=ph_u,y_F=qh_v\).
The coefficient of \(F^{-1}\) at a reduced word containing \(n_u,n_v\) generator letters is \(g x_F^{n_u}y_F^{n_v}\), by successive tree Schur elimination along its unique path.
Hence (5) gives
\[
G_{e,F}(z)=\begin{pmatrix}
g&g(1-x_F)/d_1&g(1-y_F)/d_2\\
g(1-x_F)/d_1&d_1^{-1}+2g(1-x_F)/d_1^2&g(1-x_F)(1-y_F)/(d_1d_2)\\
g(1-y_F)/d_2&g(1-x_F)(1-y_F)/(d_1d_2)&d_2^{-1}+2g(1-y_F)/d_2^2
\end{pmatrix}.
\tag{14}
\]

With \(c=e-1\), define
\[
r=c^2-1+\sqrt{c^4-c^2+1},\quad a=(1+2r)^{-1/2},\quad
b=\begin{cases}ra/c^2,&c\ne0,\\1/2,&c=0,\end{cases}\quad
\gamma(c)=\frac{\sqrt{1+2r}}{2(1+r)}.
\tag{15}
\]
The physical limits are
\[
h_u(0+i0)=-i|e|a,\qquad h_v(0+i0)=-i|e|b,\qquad
g(0+i0)=-i|e|\gamma(c).
\tag{16}
\]
Here is a direct branch justification, rather than selection by formal algebra alone.
When \(c\ne0\), the two equations force \(h_u,h_v\) to stay bounded and bounded away from zero as \(z=i\eta\to0\).
If one diverged, either the other remains bounded, contradicting its own quadratic term, or both diverge and the two independent leading linear combinations in (13) cannot both vanish.
If one tended to zero, its reciprocal equation would force the other to diverge.
Every cluster pair is therefore a nonzero finite solution at \(w=0,p=1/e,q=c/e\).
For \(r_*=q^2h_v/(p^2h_u)\), these equations become
\[
r_*^2+2(1-c^2)r_*-c^2=0,\qquad
h_u^2=-\frac1{p^2(1+2r_*)}.
\]
The positive root is (15), and nonpositive imaginary parts select (16) from its two imaginary pairs.
The negative root \(r_-=c^2-1-\sqrt{c^4-c^2+1}\in(-2,-1/2)\) yields two real pairs.
At every such solution the cavity Jacobian determinant is \(4p^2q^2(1+r_*+r_*^{-1})\ne0\).
Convergence to a real pair would thus force a local holomorphic branch with \(-\operatorname{Im}h_j(i\eta)=O(\eta)\).
The resolvent identity \(-\operatorname{Im}F_{\rm sub}^{-1}=F_{\rm sub}^{-*}(\operatorname{Im}F_{\rm sub})F_{\rm sub}^{-1}\), together with \(\operatorname{Im}F_{\rm sub}\ge\eta I\), would give a uniformly square-summable cavity Green column.
But for a real pair
\[
|ph_u|^2=-\frac1{1+2r_-},\qquad |qh_v|^2=-\frac{r_-}{r_-+2}.
\]
The first is at least one when \(c^2\ge1\), and the second is at least one when \(c^2\le1\).
The corresponding repeated-generator ray then has limiting column coefficients \(h_j(t_jh_j)^n\) that are not square summable, contradicting Fatou's lemma and the uniform bound.
Continuity and the finite set of possible cluster pairs preclude oscillation between them, proving the physical limit.
For \(e=1\), \(q(z)=O(z)\) and \(|h_v(i\eta)|\le1/\eta\), so \(q^2h_v=O(\eta)\); the first equation gives \(h_u\to-i\), and the second gives \(h_v\to-i/2\).
The Jacobian is nonsingular there as well.
The implicit function theorem now supplies a holomorphic continuation of the upper boundary branch near zero for every fixed nonzero \(e\).
This does not mean that the full operator resolvent continues across its real spectrum; the lower boundary branch is different.

<a id="free-density-and-residues"></a>
### Free density, complete boundary and residue limits

Put \(\rho=|e|\gamma(c)\), \(X=\operatorname{sgn}(e)a\), \(Y=\operatorname{sgn}(e)cb\).
Substituting \(x_F=-iX,y_F=-iY,g=-i\rho\) and \(d_1=-e,d_2=e\) in (14) gives the complete finite boundary.
Its imaginary part is particularly useful:
\[
-\frac1\pi\operatorname{Im}G_{e,F}(0+i0)
=\frac\rho\pi\begin{pmatrix}
1&-1/e&1/e\\-1/e&2/e^2&(XY-1)/e^2\\1/e&(XY-1)/e^2&2/e^2
\end{pmatrix}>0.
\tag{17}
\]
After diagonal scaling, its root Schur complement is \(\begin{pmatrix}1&XY\\XY&1\end{pmatrix}\).
For \(c\ne0\), \((XY)^2=r/[(r+2)(1+2r)]\le1/9\), since the denominator minus \(9r\) is \(2(r-1)^2\); for \(c=0\), \(XY=0\).
This proves strict positivity, invertibility of the Green boundary and a finite first-return limit \(-G_{e,F}(0+i0)^{-1}\).
All cell measures have analytic densities near zero, and the normalized scalar quantities are
\[
g_{e,F}(0+i0)=\frac{2\rho(X+Y)}{3e^2}-\frac{i\rho}{3}(1+4/e^2),\qquad
\rho_{e,F}(0)=\frac{e^2+4}{3\pi|e|}\gamma(e-1)>0.
\tag{18}
\]
The atom is zero by the finite boundary and faithfulness of the canonical trace.
In particular \(g_{1,F}(0+i0)=1/3-5i/6\) and \(g_{2,F}(0+i0)=1/6-i/\sqrt3\).
Thus the single-generator degeneration at \(e=1\) is regular in both models, while the lattice logarithmic singularity at \(e=2\) has no free counterpart.
The small-window probability is \(2\rho_{e,F}(0)\delta+O(\delta^2)\).

In both groups positive zero density, including the critical logarithm, puts zero in the continuous spectrum and implies
\[
i\eta(i\eta-H_e)^{-1}\longrightarrow0\ \text{strongly},\qquad
\|i\eta(i\eta-H_e)^{-1}\|=1\quad(\eta>0).
\tag{19}
\]
The finite-cell residues are \(O(\eta)\), except for the lattice \(e=2\), where they are \(O(\eta\log(1/\eta))\).
For small \(e\ne0\), (8), the elliptic endpoint expansion, and (18) give
\[
\rho_{e,Z}(0)\sim\frac{2}{3\pi^2|e|}\log\frac1{|e|},\qquad
\rho_{e,F}(0)\sim\frac{\sqrt3}{3\pi|e|}.
\tag{20}
\]
There is no uniform bounded-density assertion as \(e\to0\).
Although \(\|H_e-H_0\|=|e|\) implies weak convergence of the spectral laws, the [v2 zero atom](../claims/Yin_C_A0004_v2.md#statement) has mass \(1/3\).
Thus \(\lim_{e\to0}\lim_{\eta\downarrow0}i\eta g_e(i\eta)=0\), whereas reversing these limits gives \(1/3\).

<a id="height-layer-certificate"></a>
### A height-layer certificate beyond the protected edge form

Suppose a discrete group admits an epimorphism \(\varphi:G\to\mathbb Z\), write \(N=\ker\varphi\), and choose \(t\in G\) with \(\varphi(t)=1\).
Decompose \(\ell^2(G)^d=\bigoplus_{n\in\mathbb Z}\ell^2(t^nN)^d\), identifying each layer with \(\ell^2(N)^d\).
Let \(T\in M_d(\mathcal N(G))\) have finite height bandwidth and act in these coordinates as
\[
(Tf)_n=\sum_{j=p}^{q}A_{n,j}f_{n+j},\qquad q>p,
\tag{21}
\]
where all \(A_{n,j}\in M_d(\mathcal N(N))\) are bounded and the outer coefficients \(A_{n,q}\) are boundedly invertible.
Uniform bounds on their inverses are not needed for the following finite-interval argument.
Then \(T\) is injective.
Indeed, the equation at layer \(n-p\) expresses \(f_{n+q-p}\) from the preceding \(q-p\) layers.
For any interval of length \(m\ge q-p\), restrictions of global kernel vectors lie in the graph of a bounded \(\mathcal N(N)\)-linear map from the first \(q-p\) layers to the rest.
This graph is closed and has \(N\)-dimension \(d(q-p)\), by its bounded inverse coordinate restriction and polar decomposition.
Let \(P\) be the global kernel projection and \(\chi_m\) the interval cut.
The positive contraction \(\chi_mP\chi_m\) has range in that graph, so
\[
m(\operatorname{Tr}_d\otimes\tau_G)(P)
=(\operatorname{Tr}_{md}\otimes\tau_N)(\chi_mP\chi_m)
\le d(q-p).
\tag{22}
\]
The equality follows because every layer diagonal trace is the sum of the diagonal matrix coefficients of \(P\) at \(\delta_{t^n}\), equal to those at the identity by right-translation equivariance.
Letting \(m\to\infty\) and using trace faithfulness proves injectivity.
For zero bandwidth, invertibility of the sole coefficient proves the same conclusion directly.
This argument uses no amenability of \(G\) or \(N\), no ordering of \(N\), and no integer-rank hypothesis for its group algebra.

In particular, if \(\varphi(u)=1\) and \(\varphi(v)=0\), the equation \(T_ef=0\) is a two-step recurrence with unit outer coefficients; hence (22) gives its zero kernel for every real \(e\), including the present \(e\ne0\) Schur problem.
This proves zero-atom exclusion for a class of structured operators on groups that need not themselves be free or abelian.
It is not a theorem about all matrices over those groups.

For either current group, the same height argument applies to the real Schur operator at every \(\lambda\ne\pm e\), whose \(U\) coefficient is nonzero.
At \(\lambda=e\), the first edge equation gives \(b_1^*x=0\), hence \(x=0\), then the second edge coordinate vanishes and \(b_1y_1=0\).
At \(\lambda=-e\), interchange the two edges.
Both \(u,v\) have infinite order, so their difference operators are injective by the accepted regular-transport argument.
This proves the asserted absence of all atoms on the free group as well.

<a id="ordered-quotient-source"></a>
### Ordered-quotient input and its exact scope

The scalar height conclusion is covered by a more general established theorem.
Linnell, *Zero divisors and \(L^2(G)\)*, C. R. Acad. Sci. Paris, Series I, 315 (1992), 49--53, Theorem 4 on printed pp. 50--51, was checked directly in the [journal scan](https://math.uchicago.edu/~shmuel/L%5E2%20cohomology%20readings/Linnell,%20zerol2.pdf), including the actual images at the page break.
For a normal subgroup \(N\lhd G\) with right-orderable quotient and transversal \(\mathcal T\), it treats \(\alpha=\sum_{t\in\mathcal T}\alpha_t t\in\ell^2(G)\), \(\alpha_t\in\ell^2(N)\).
If the quotient support has a least term \(t_0\) and \(\alpha_{t_0}\phi\ne0\) for every nonzero \(\phi\in\mathcal N(N)\), it concludes \(\alpha\beta\ne0\) for every nonzero \(\beta\in\ell^2(G)\).
For a finite group-ring scalar with a unique extreme support element under a map to \(\mathbb Z\), that coefficient is a nonzero scalar times a group unit, so the premise holds without any zero-divisor conjecture for \(N\).
This supplies an additional sufficient scalar criterion for the Schur operator in (3), and permits right-orderable quotients beyond \(\mathbb Z\).
The statement and applicability were inspected; the full historical proof was not re-audited.
The matrix-valued finite-layer argument (21)--(22) is supplied directly here and is not attributed to the scalar source theorem.

There is a broader scalar application within torsion-free groups.
Suppose the subgroup \(H=\langle u,v\rangle\) is torsion free and admits a nonzero homomorphism to \(\mathbb Z\).
Then \(T_e\) is injective for every \(e\ne0\), even when the homomorphism cannot assign heights one and zero to the chosen generators.
For \(c=e-1=0\), this follows directly from injectivity of \(u+u^{-1}\) for an infinite-order \(u\), or its value \(2I\) when \(u=1\).
For \(c\ne0\), choose a least-height term among \(u^{\pm1},v^{\pm1}\).
If their absolute heights differ, this term has a single nonzero scalar-unit coefficient.
If the absolute heights agree, they are both nonzero and the least coefficient, after factoring a group unit, is \(1+ch\) for an actual element \(h\) of the height kernel.
It is boundedly invertible when \(|c|\ne1\), by a geometric series after factoring the larger term.
The only remaining allowed real value is \(c=1\), since \(c=-1\) would mean \(e=0\).
If \(h=1\), the coefficient is \(2I\); otherwise \(h\) has infinite order, and \(1+h\) is injective by the regular-shift argument.
Thus the least coefficient always meets Lin92 Theorem 4's exact hypothesis.
Applying that theorem over \(H\), and then decomposing \(\ell^2(G)\) into right \(H\)-cosets when needed, proves the assertion.
This conclusion concerns the displayed two-generator scalar family, not all matrices over an indicable group.

The source search was prompted by the needed implication from an invertible extreme height coefficient to analytic kernel exclusion.
Existing A-series material supplied cyclic-quotient algebraic examples and finite-trace foundations, but not this exact retained criterion.
Searches for analytic zero divisors, cyclic quotients and leading coefficients led through Linnell's Durham survey to the 1992 primary theorem.
The checked primary statement settles the scalar attribution and applicability question; no claim of a new or earliest criterion is made.

<a id="holonomy-obstruction"></a>
### Why infinite collective holonomy no longer fixes the atom

There is a direct obstruction even to extending the v2 torsion-allowing holonomy certificate unchanged.
Take the infinite group \(G=C_2*C_3=\langle u,v\mid u^2=v^3=1\rangle\), and \(e=3\).
Its actual loop labels generate an infinite subgroup, so the [v2 collective-holonomy criterion](../claims/Yin_C_A0004_v2.md#collective-holonomy-condition) makes \(D\) injective and gives unperturbed zero-kernel dimension one.
Set \(p=(1+u)/2\), \(r=(1+v+v^2)/3\).
These are projections with traces \(1/2,1/3\), and \(V=3r-I\).
Now \(T_3=2u+2V\).
If \(T_3f=0\), then \(uf=-Vf\); taking squared norms and using \(V^2=I+3r\) gives \(rf=0\), and then \(uf=f\).
The converse holds, so
\[
\ker T_3=\operatorname{ran}p\cap\ker r,\qquad
\frac16\le\dim_G\ker T_3\le\frac12.
\tag{23}
\]
The lower bound follows by applying finite-trace rank subtraction to \(rp\) on \(\operatorname{ran}p\): its image dimension is at most \(\tau(r)=1/3\).
The upper bound is \(\tau(p)=1/2\).
By (4), \(\dim_G\ker H_3\) belongs to the same strictly positive nonintegral interval, and the normalized zero atom lies in \([1/18,1/6]\).
No exact value or free-convolution atom theorem is needed for this obstruction.
It shows that infinitude of the loop subgroup cannot by itself preserve an integer kernel dimension after the signed perturbation.
The group has torsion, so this is not an Atiyah counterexample under A0001 and supplies no negative conclusion for torsion-free groups lacking a height certificate.

## Scope and next obstruction

The two comparison groups retain integer kernel dimension zero, but the former integer one is not stable under any nonzero signed edge potential of (1).
The new arithmetic control comes from the Schur operator's actual height or quotient structure, or from direct Fourier/tree analysis, rather than from the old incidence cokernel.
Neither the Schur identity alone nor the trace of an unknown scalar kernel proves integrality.
The next question is which rank-deficient extreme coefficients, or relation systems without a usable ordered quotient, admit an independent finite-layer or transport certificate after Schur elimination.
Any such extension must identify its actual input geometry and cannot assume the unknown integer nullity of the residual operator.

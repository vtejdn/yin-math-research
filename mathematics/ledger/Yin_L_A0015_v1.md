---
author: Yin
---
# Cauchy boundary residues and probability strategies for Atiyah integrality

Date: 2026-11-11 (Asia/Hong_Kong).
This exploration develops the exact atom formulation in [L_A0012](Yin_L_A0012_v1.md) for the complete complex-coefficient contract of [A0001](../tasks/Yin_T_A0001_v1.md#contract).
The main agent and two development helpers checked the direct spectral calculations, compared probability mechanisms and retained their limitations.
These are reformulations, source applications and strategy tests, not a proof of the conjecture or a claim of novelty for standard transform identities.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0015_v1.md#whole-artifact-finding) covers formulas (1)--(21), their equivalences and stated limits at its recorded accepted-foundation scope.

## Setting and source scope

Fix a discrete group \(G\), let \(M=\mathcal N(G)\), and write
\[
\tau_n=\operatorname{tr}_n\otimes\tau_G,\qquad
\operatorname{tr}_n(I_n)=1,\qquad
\nu_n=n\tau_n.
\]
For a bounded selfadjoint \(H\in M_n(M)\), let \(\mu_H\) be its probability law and set
\[
g_H(z)=\tau_n((zI-H)^{-1})
       =\int_{\mathbb R}\frac{d\mu_H(x)}{z-x},
\qquad F_H(z)=g_H(z)^{-1},\quad z\in\mathbb C^+.
\]
Thus \(g_H\) has negative imaginary part.
The function \(F_H\) is a scalar reciprocal, not the inverse of an operator-valued Cauchy transform.

The group-matrix atom equivalence, the all-size selfadjoint affine reduction and the actual affiliated rational closure \(R_G\) are used at the precise scope of [L_A0012](Yin_L_A0012_v1.md#matrix-atoms-an-exact-formulation-without-rational-inverses).
No scalar-polynomial substitute for all matrix sizes is assumed.
The equivalences below hold for a fixed group; A0001 asks them for every torsion-free group.

The [BBL21 interface](../audits/literature/BBL21/Yin_U001.md#cauchy-boundary-recovery) records the matching arXiv v2 Lemmas 2.1 and 2.3.
These source statements supply attribution and their operator-valued extensions; the scalar residue calculations below are direct.
The [Bia97 source notes](../audits/literature/Bia97/readme.md) supply Section 3, Lemma 2 and Corollary 3, printed pp. 708--711, for the free-heat calculation.
The [MSY23 entropy interface](../audits/literature/MSY23/Yin_U005.md#section-61-how-entropy-supplies-maximal-delta) supplies the one-variable entropy-dimension formula.
Their analytic foundations remain accepted external inputs, not newly audited proofs.

## Boundary residues and reciprocal slopes

For any probability measure \(\mu\) and \(a\in\mathbb R\),
\[
m_\mu(a):=\mu(\{a\})
=\angle\lim_{z\to a}(z-a)g_\mu(z)
=\lim_{\eta\downarrow0}i\eta g_\mu(a+i\eta)
=\lim_{\eta\downarrow0}-\eta\operatorname{Im}g_\mu(a+i\eta).
\tag{1}
\]
The angular limit is taken inside each fixed cone
\(\lvert\operatorname{Re}z-a\rvert\le C\operatorname{Im}z\).
Indeed, \((z-a)/(z-x)\) converges pointwise to \(1_{\{a\}}(x)\) and is bounded in modulus by \(\sqrt{1+C^2}\).
Dominated convergence proves the first equality, and the vertical imaginary-part formula is
\[
-\eta\operatorname{Im}g_\mu(a+i\eta)
=\int\frac{\eta^2}{(a-x)^2+\eta^2}\,d\mu(x).
\tag{2}
\]

Consequently the full integer matrix-kernel property is equivalent to
\[
n\angle\lim_{z\to a}(z-a)g_H(z)\in\{0,1,\ldots,n\}
\tag{3}
\]
for every finite \(n\), every \(H=H^*\in M_n(\mathbb CG)\) and every real \(a\).
The converse uses \(H=A^*A\) at zero for each rectangular matrix \(A\); the forward implication applies the property to \(H-aI\).
The selfadjoint affine tests in L_A0012 suffice, with their actual enlarged size and integer trace corrections.

Since \(g_\mu\) never vanishes on \(\mathbb C^+\),
\[
\frac{F_\mu(z)}{z-a}=\frac1{(z-a)g_\mu(z)}.
\tag{4}
\]
If \(m_\mu(a)>0\), the ratio has finite angular limit \(1/m_\mu(a)\) and \(F_\mu(z)\to0\).
If \(m_\mu(a)=0\), the modulus of this ratio tends to infinity.
There need not be a positive-real infinite limit in the latter case.
Thus (3) is also equivalent to every finite ratio limit belonging to
\[
\{n/k:1\le k\le n\},
\tag{5}
\]
with the infinite-modulus alternative otherwise.

A finite Julia--Caratheodory derivative detects an atom only together with boundary value \(F_\mu(a)=0\).
For \(\mu=\delta_1\) at \(a=0\), one has \(F(z)=z-1\) and
\(\operatorname{Im}F(i\eta)/\eta=1\), but there is no atom at zero.
Conversely, the arcsine law on \([-1,1]\) has
\(F(z)=\sqrt{z^2-1}\), chosen asymptotic to \(z\) at infinity.
At \(a=1\), its boundary value is zero, its ratio in (4) has infinite modulus and there is no atom.

The residue in (1) is a boundary residue.
An atom may coexist with continuous spectral mass in every neighborhood, so a meromorphic continuation or an isolated Laurent pole is not implied.

## Finite atomic part and a uniform remainder

A finite positive measure \(\rho\) is atomless if and only if
\[
\lim_{\eta\downarrow0}\sup_{x\in\mathbb R}
       \eta|g_\rho(x+i\eta)|=0.
\tag{6}
\]
For a proof, put \(M_\rho=\rho(\mathbb R)\).
For every \(\delta>0\),
\[
Q_\eta(x):=-\eta\operatorname{Im}g_\rho(x+i\eta)
\le \rho([x-\delta,x+\delta])
       +M_\rho\eta^2/\delta^2,
\qquad
\eta^2|g_\rho(x+i\eta)|^2\le M_\rho Q_\eta(x).
\]
For a finite atomless measure,
\(\sup_x\rho([x-\delta,x+\delta])\to0\).
Otherwise intervals of shrinking lengths and uniformly positive mass have, by tightness, a subsequence of bounded centers converging to a positive-mass point.
First letting \(\eta\to0\), then \(\delta\to0\), proves (6).
The converse follows from (1) at any atom.

The integer matrix-kernel property is therefore also equivalent to the following decomposition for every tested \(H\):
\[
g_H(z)=\sum_{j=1}^{r}\frac{k_j}{n(z-\lambda_j)}
       +g_{\rho_H}(z),\qquad
k_j\in\mathbb Z_{>0},\quad
\sum_j k_j\le n,
\tag{7}
\]
where the \(\lambda_j\) are distinct real numbers and \(\rho_H\) is a finite positive measure satisfying (6).
In particular \(r\le n\).
The forward direction removes all atoms, each of which has mass at least \(1/n\).
The reverse direction uses (6) to show that the listed masses are exactly all the atoms.
This is a decomposition of the transform on the upper half-plane, not analytic continuation across the continuous spectrum.
The estimate is for each fixed measure and supplies no rate uniform over groups, coefficients or matrices.

## Positive resolvents and the bounded rational endpoint

For \(A\in M_{m,n}(\mathbb CG)\), put \(K=A^*A\).
Spectral calculus gives
\[
s_A(\varepsilon)
=\tau_n\bigl(\varepsilon(K+\varepsilon I)^{-1}\bigr)
=-\varepsilon g_K(-\varepsilon)
\longrightarrow\mu_K(\{0\})
=\nu_n(p_{\ker A})/n.
\tag{8}
\]
The values decrease as \(\varepsilon\downarrow0\).
The transform on the negative real axis is defined by the same integral, outside the spectrum.
Requiring the limits in (8) to lie in \(\{0,1/n,\ldots,1\}\) is another full equivalence.

For the actual affiliated rational closure, set
\[
q_r=(1+r^*r)^{-1}\in R_G\cap M,\qquad r\in R_G.
\]
L_A0012 proves \(1_{\{1\}}(q_r)=p_{\ker r}\) and the equivalence of A0001 with division of \(R_G\).
Hence the property is equivalent to the single-endpoint tests
\[
r\ne0
\quad\Longrightarrow\quad
\lim_{\eta\downarrow0}i\eta g_{q_r}(1+i\eta)=0.
\tag{9}
\]
Equivalently, the corresponding reciprocal ratio has infinite modulus.
Intermediate affiliated inverses are still permitted and must actually exist.
The test excludes an atom at \(1\), not every atom of \(q_r\): \(r=1\) gives \(q_r=\tfrac12 1\).

## Schur complements and boundary energy

Represent a bounded selfadjoint variable cyclically with unit cyclic vector \(\Omega\) and its prescribed scalar law.
Relative to \(\mathbb C\Omega\oplus\Omega^\perp\), write
\[
H=\begin{pmatrix}a&v^*\\v&D\end{pmatrix},
\qquad
\sigma(B)=\langle1_B(D)v,v\rangle.
\]
The scalar \(a\) is real, \(D\) is bounded selfadjoint, and \(\sigma\) is a finite positive measure.
The Schur-complement identity gives
\[
F_H(z)=z-a-\int\frac{d\sigma(t)}{z-t}.
\tag{10}
\]
For a real \(\lambda\), let
\[
E_\lambda=\int\frac{d\sigma(t)}{(\lambda-t)^2}.
\]
When \(E_\lambda<\infty\), the integral
\(J_\lambda=\int(\lambda-t)^{-1}\,d\sigma(t)\) is absolutely convergent by Cauchy--Schwarz.
Then
\[
\mu_H(\{\lambda\})>0
\iff
E_\lambda<\infty\ \text{and}\ \lambda-a-J_\lambda=0,
\qquad
\mu_H(\{\lambda\})=\frac1{1+E_\lambda}.
\tag{11}
\]

To verify (11) without a boundary differentiability assumption, solve the eigenvector equations with first coordinate one.
Finite \(E_\lambda\) is exactly the condition that
\(w=(\lambda-D)^{-1}v\), with zero component on \(\ker(\lambda-D)\), exists as a vector.
It has squared norm \(E_\lambda\).
The first eigenvector equation is \(a+\langle w,v\rangle=\lambda\), which is the stated balance equation.
Conversely an eigenvector having nonzero overlap with \(\Omega\) yields this vector after normalization and proves finiteness of \(E_\lambda\).
Cyclicity rules out eigenvectors orthogonal to \(\Omega\), and the normalized projection mass is \(1/(1+\|w\|^2)\).

For an \(n\)-square tested group-ring law, the exact arithmetic target at these balanced finite-energy points is
\[
E_\lambda\in\{n/k-1:1\le k\le n\}.
\tag{12}
\]
Generic positivity does not enforce this set.
For example \(\alpha\delta_0+(1-\alpha)\delta_1\) has
\(E_0=(1-\alpha)/\alpha\), for every \(0<\alpha<1\).
A recursion strategy must obtain additional constraints from actual labelled group paths or another structural input.
The compressed operator \(D\) is generally not a group-ring convolution operator, so the desired Atiyah property cannot simply be applied to it.
For a normalized matrix trace, the cyclic representation in this argument is the representation of that scalar law, not a single arbitrarily chosen diagonal entry of the original matrix resolvent.

## Free heat and entropy observables

Let \(\sigma_t\) be the centered semicircle law of variance \(t>0\), and let \(\rho_t\) be the density of \(\mu\boxplus\sigma_t\).
Use the Bia97 boundary functions
\[
v_t(x)=\inf\left\{v\ge0:
 \int\frac{d\mu(y)}{(x-y)^2+v^2}\le\frac1t\right\},
\qquad
\psi_t(x)=x+t\int\frac{x-y}{(x-y)^2+v_t(x)^2}\,d\mu(y).
\]
The checked source gives
\(\rho_t(\psi_t(x))=v_t(x)/(\pi t)\) and the homeomorphism \(\psi_t\).
At zero height, the finite threshold integral makes the displayed real integral well defined.
It follows directly that
\[
\mu(\{x\})
=\lim_{t\downarrow0}\frac{v_t(x)^2}{t}
=\pi^2\lim_{t\downarrow0}t\,\rho_t(\psi_t(x))^2.
\tag{13}
\]
Indeed \(0\le v_t(x)\le\sqrt t\), and whenever the height is positive,
\[
v_t(x)^2/t
=\int\frac{v_t(x)^2}{(x-y)^2+v_t(x)^2}\,d\mu(y).
\]
Dominated convergence gives the atom along positive-height subsequences.
A positive atom forces positive height for every \(t\); if there is no atom, zero-height subsequences have the same zero limit.

For \(\mu=\mu_H\), requiring \(n\) times (13) to be an integer is exactly (3).
An operator realization adjoins a scalar semicircular element free from the whole normalized tracial algebra \(M_n(M)\).
Unspecified entrywise matrix noise need not realize this scalar convolution.
The coordinate \(\psi_t(x)\) is essential to the stated formula; no replacement by a fixed spatial coordinate is asserted.

The accepted one-variable entropy formula gives
\[
\delta^*(h)=1-\sum_x\mu_h(\{x\})^2
\]
for bounded selfadjoint \(h\).
It equals one precisely for atomless laws and zero precisely for a Dirac law.
For the latter assertion, the nonnegative atom masses have total at most one, and their squares sum to one only for a single mass one.
Combining with L_A0012, the Atiyah property is equivalent to
\[
\delta^*(h)\in\{0,1\}
\quad\text{for every bounded selfadjoint }h\in R_G,
\tag{14}
\]
or to \(\delta^*(h)=1\) for every actually nonscalar such \(h\).
It is enough to impose the binary condition on all \(q_r\).
A partial kernel would give \(q_r\) an atom of mass strictly between zero and one, forcing \(0<\delta^*(q_r)<1\).
One must not require \(\delta^*(q_r)=1\) for all nonzero \(r\), because \(q_1\) is scalar.

These observables suggest estimates of order \(o(t^{-1/2})\) for the transported density of a nonscalar bounded rational observable.
Any independently proved bound \(C_{h,x}t^{-\beta_{h,x}}\) with \(\beta_{h,x}<1/2\) would suffice, but is stronger than the exact target.
Free smoothing itself gives no arithmetic restriction: (13) recovers every \(\alpha\) from \(\alpha\delta_0+(1-\alpha)\delta_1\).
The [MSW17 algebraic-freeness interface](../audits/literature/MSW17/Yin_U001.md) also prevents importing ordinary full-tuple conjugate variables in the presence of actual polynomial relations.
Already the real and imaginary parts of one Haar unitary satisfy \(X^2+Y^2=1\).
A relation-compatible derivative estimate for scalar rational observables remains missing.

## Logarithmic slopes and return amplitudes

For bounded positive \(K\), define the regularized unnormalized logarithmic determinant
\[
L_K(\varepsilon)=\nu_n(\log(K+\varepsilon I)).
\]
Differentiating bounded functional calculus at each positive \(\varepsilon\) and using (8) gives
\[
\varepsilon L_K'(\varepsilon)=
\nu_n\bigl(\varepsilon(K+\varepsilon I)^{-1}\bigr)
\longrightarrow\nu_n(p_{\ker K}),
\qquad
\frac{L_K(\varepsilon)}{\log\varepsilon}
\longrightarrow\nu_n(p_{\ker K}).
\tag{15}
\]
For the second limit, integrate
\(\log(x+\varepsilon)/\log\varepsilon\) against the finite spectral measure.
On its bounded support this quotient is uniformly bounded for sufficiently small \(\varepsilon\), tends to one at zero and tends to zero elsewhere.
No determinant-class hypothesis on the nonzero spectrum is needed.

Thus integer logarithmic slope for every \(K=A^*A\) is equivalent to A0001.
Vanishing determinant alone is not equivalent to a kernel.
For example, the atomless probability measure
\(1_{(0,e^{-1}]}(x)\,dx/[x(\log x)^2]\) has logarithmic integral minus infinity.

Choose \(c>0\) with \(c\ge\|K\|\) and put \(B=I-K/c\), a positive contraction.
Then
\[
\tau_n(B^j)\longrightarrow\mu_B(\{1\})
=\nu_n(p_{\ker K})/n,
\qquad
(1-t)\tau_n((I-tB)^{-1})\longrightarrow\mu_B(\{1\})
\quad(t\uparrow1).
\tag{16}
\]
Both follow by dominated convergence.
The coefficients of \(\tau_n(B^j)\) are weighted returns of labelled group words.
For general complex group-ring matrices they are return amplitudes, not transition probabilities of an ordinary Markov chain.

Near \(t=0\), define
\[
D_B(t)=\exp\left(-\sum_{j\ge1}
              \nu_n(B^j)\frac{t^j}{j}\right).
\]
For \(0\le t<1\), its positive continuation is
\(\exp(\nu_n(\log(I-tB)))\), and
\[
-\lim_{t\uparrow1}(1-t)\frac{D_B'(t)}{D_B(t)}
=\lim_{t\uparrow1}\frac{\log D_B(t)}{\log(1-t)}
=\nu_n(p_{\ker K}).
\tag{17}
\]
The first identity follows by differentiating and applying dominated convergence to \((1-t)x/(1-tx)\).
The second follows as in (15).
This exposes the same atom as a local logarithmic exponent of a series whose coefficients remember returns.

## Torsion-free cycle arithmetic and its obstruction

A primary-source search on 2026-11-11 for return-word determinant integrality found [Kontsevich, Noncommutative identities, arXiv:1109.2469v1, Section 1, Step 1](https://arxiv.org/html/1109.2469v1).
That step explicitly extends its scalar Euler-product argument to arbitrary torsion-free groups.
The [Kassel--Reutenauer paper, arXiv:1303.3481v5](https://arxiv.org/html/1303.3481v5), Definition 2.1, Proposition 2.2, Corollary 2.3 and the matrix-word construction in Section 4, provides the corresponding cyclic-series framework.
These passages were checked directly; their separate algebraicity theorems concern free groups and are not imported for arbitrary torsion-free groups.
Bibliographic identities are retained under Kon11 and KR14.

Here is the explicit matrix specialization needed for this strategy.
For \(A\in M_n(\mathbb CG)\), give each nonzero term in entry \(A_{ij}\) a letter \(e=(i,j,g)\) with weight \(c_e\).
An admissible cyclic word is a closed index path with group-label product equal to the identity.
Its rotations are again admissible.
If a power of a word is admissible, its index path already closes and its label \(g\) satisfies \(g^r=e\); torsion-freeness forces \(g=e\).
Thus admissibility is also closed under taking primitive roots.
For each primitive cyclic class \([\gamma]\), put \(w_\gamma=\prod_{e\in\gamma}c_e\).
Counting its \(|\gamma|\) distinct rotations in every positive power gives the formal identity
\[
D_A(t):=\exp\left(-\sum_{j\ge1}
                 \nu_n(A^j)\frac{t^j}{j}\right)
=\prod_{[\gamma]\ {\rm primitive,\ admissible}}
        (1-w_\gamma t^{|\gamma|}).
\tag{18}
\]
There are finitely many letters, so every coefficient involves finitely many factors.
In particular \(D_A\in\mathbb Z[[t]]\) for \(A\in M_n(\mathbb ZG)\).
Keeping all weights independent gives coefficients in \(\mathbb Z[c_e]\), and specialization preserves the identity for arbitrary complex coefficients.
This supplies actual torsion-free information; it is not a consequence of Herglotz positivity.

However, neither integer coefficients nor algebraicity suffices to quantize a boundary atom.
For the probability law
\[
\mu=\tfrac12\delta_0+\tfrac12\delta_4
\]
one has
\[
g_\mu(z)=\frac1{2z}+\frac1{2(z-4)},\qquad
D_\mu(t):=\exp\left(\int\log(1-tx)\,d\mu(x)\right)
=\sqrt{1-4t}
=1-2\sum_{j\ge1}C_{j-1}t^j\in\mathbb Z[[t]],
\tag{19}
\]
where \(C_j=\frac1{j+1}\binom{2j}{j}\).
Its Cauchy transform is rational, its determinant series is algebraic with integer coefficients, but its atom at four has mass \(1/2\).
This is a counterexample to a generic analytic-arithmetic implication, not a group-ring counterexample to A0001.
A successful use of (18) must retain additional labelled-word or multivariate structure and connect it to the local exponents in (17).
Algebraicity can allow fractional Puiseux exponents, and a one-variable integer series does not retain all of the canonical group trace.

The new arithmetic route should first test which part of the primitive-word structure excludes the fractional behavior in (19), including under coefficient specialization.
An integer-coefficient argument alone leaves an additional bridge to the Task's arbitrary complex coefficients.
The multivariate identity keeps those coefficients visible, but does not solve the analytic specialization problem.

## A geometric index mechanism beyond algebraicity

There is a concrete source model where extra geometry does quantize the total residue.
Use a connected finite leafless multigraph \(K\), strictly positive real symmetric edge weights, real vertex potentials and the lifted Jacobi operator on its universal covering tree.
Let \(p=|V(K)|\), let \(\mu_v\) be the law at a lift of \(v\), and put \(\mu=p^{-1}\sum_v\mu_v\).
The Aomoto index theorem, checked in [BGVM20, Theorem 3.1](https://arxiv.org/html/2008.03318v2), gives
\[
p\mu(\{\lambda\})
=\operatorname{cc}(X_\lambda)-|\partial X_\lambda|\in\mathbb Z,
\qquad X_\lambda=\{v:\mu_v(\{\lambda\})>0\}.
\tag{20}
\]
Here the induced \(X_\lambda\) is a forest and \(\partial X_\lambda\) consists of its neighboring vertices outside the set.
This is a finite combinatorial index, not a conclusion from algebraicity alone.

[BBGSS23, Sections 1--2](https://arxiv.org/html/2309.00437v1) explicitly impose the positive-weight hypotheses above and give a finite vertex-edge product for the exponential logarithmic potential.
Its factors have integer exponents.
Section 4 sketches the resulting index proof only for isolated eigenvalues and explicitly leaves the additional Puiseux analysis at embedded eigenvalues to further work.
For the general index statement, the accepted input here is BGVM20 rather than that sketch.
Only the stated interfaces were checked; the source proofs were not independently audited in full.

The free deck group and \(p\) vertex representatives identify this law with the normalized trace of a \(p\)-square matrix over that free group's complex group ring.
Thus (20) supplies an actual residue-counting mechanism in a known Atiyah setting.
It does not represent an arbitrary group's operator on the universal tree without changing its law.

An elementary relation test makes that loss explicit.
For \(A=u+u^{-1}+v+v^{-1}\), the free-group canonical trace satisfies \(\tau(A^4)=28\): a four-step returning walk on the four-regular tree has distance pattern up-down-up-down in \(16\) ways, or up-up-down-down in \(12\) ways.
After imposing \([u,v]=e\), the \(\mathbb Z^2\) trace is \(36\): there are \(6+6\) pure-direction words and \(24\) words using each of \(u,u^{-1},v,v^{-1}\) once.
The second moments agree and odd moments vanish, so the corresponding determinant germs satisfy
\[
\log D_{\mathbb Z^2}(t)-\log D_{F_2}(t)
=-2t^4+O(t^6).
\tag{21}
\]
This calculates a relation correction at the first affected order, not an atom defect or a new Atiyah case.
A graph-index strategy must account for such corrections before taking a boundary residue.

## Strategy consequences and limits

The exact residue tests improve the formulation without supplying the missing arithmetic.
The Schur-energy description isolates a possible recursion mechanism, but a finite equation or generic positivity alone allows arbitrary atom masses.
The geometric index in (20) supplies a genuine additional mechanism for [S_A0006](../strategies/Yin_S_A0006.md) in the universal-tree setting, with a relation-compatible extension still missing.
The free-heat and entropy identities are additional exact observables and an analytic exploratory branch, with the relation-compatible estimate still absent.
They do not by themselves supersede [S_A0005](../strategies/Yin_S_A0005.md).

The return-word product contributes an independent combinatorial input and supports [S_A0007](../strategies/Yin_S_A0007.md), a distinct proposed route toward local-exponent rigidity.
Its unresolved bridge is precisely the passage from labelled cyclic structure to integer boundary exponents, beyond the false implication tested in (19).
The weak-convergence and near-zero issues in [S_A0003](../strategies/Yin_S_A0003.md) remain separate; exact return identities do not automatically provide atom convergence from approximating laws.
No new group class, universal recursion, rate estimate or solution of A0001 is established.

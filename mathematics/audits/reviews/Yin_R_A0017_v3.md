---
author: Yin
---
# Independent review of signed edge potentials and height certificates

Review act: 2026-11-11T14:34, in UTC, for Yin.
The exact target is the complete 2026-11-11 working revision of [C_A0004_v3](../../claims/Yin_C_A0004_v3.md#statement) and its [argument](../../claims/Yin_C_A0004_v3.md#argument), including formulas (1)--(23), the torsion-free indicable scalar application in the ordered-quotient subsection, and the final scope restrictions.
The saved target after its inline-math delimiter maintenance was read in full, and the subsequently added DLMF boundary-formula attribution was checked before finalizing this finding.
This is new independent evidence for the signed-edge variant in the existing review family.
The [preceding review](Yin_R_A0017_v2.md#whole-artifact-finding) retains its exact v2 target and conclusions.

## Arrangement and accepted inputs

A separately organized reviewing agent outside substantive proof development performed the whole-argument inspection.
Its initial context supplied the fixed target locator, scope, governing instructions, human identity and administrative work-start metadata.
It supplied no proof-development dialogue, draft, mathematical development summary, helper answer or previous verdict about the target.
The reviewer first enumerated its obligations and formed initial findings from the complete fixed target, then consulted prior reviews only for the unchanged inputs identified below.
A notice of the added indicable scalar application identified its location; the reviewer read and checked the actual paragraph directly.
The reviewer supplied no substantive proof repair and read no development draft or developer-helper conversation.

The [v2 statement](../../claims/Yin_C_A0004_v2.md#statement), [collective-holonomy argument](../../claims/Yin_C_A0004_v2.md#collective-holonomy-condition) and [v2 independent finding](Yin_R_A0017_v2.md#whole-artifact-finding) are accepted only for the first-return convention, unperturbed kernel dimension and atom, regular-transport injectivity, and the infinite-holonomy example used here.
Their applicability was checked against the actual incidence column and the unchanged \(e=0\) operator.
No v2 density, spectral gap or perturbation conclusion is transferred to the present signed edge block.
The [isotropic tree and square-lattice formulas](../../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms) and their [independent review](Yin_R_A0016_v1.md#whole-artifact-finding) are reused only at their exact transform and modulus-normalization interfaces.
The finite-trace support facts already used in v2 are applied through rectangular polar decomposition; no integer-rank theorem for an arbitrary group-ring matrix is assumed.
These inputs form no cycle through the new variant.

## Whole-artifact finding

No substantive mathematical gap was found in the complete statement and argument under their stated hypotheses.
The checks below cover both models for every real \(e\ne0\), including the separate \(e=1\) and \(e=2\) cases, the complete matrix constants, all spectral-atom exclusions, the generalized layer certificate, the primary-source interface, and the torsion obstruction.
This is mathematical agent review, without numerical experiments or proof-assistant verification.

### Schur reduction, projection and full inverses

Solving the lower kernel equation gives exactly (3), with a bounded equivariant graph map and bounded inverse on its range.
The positive operator \(pW^*Wp\) is bounded below by the identity of its corner, so the displayed corner inverse exists and (4) is the orthogonal projection, including the zero-corner case.
The polar decomposition of \(Wp\) identifies its initial support with \(p\), proving the stated unnormalized dimension equality.
The multiplication \(D^*JD=V-U\) then gives \(S_e=T_e/e\) with the correct sign.
The old cokernel has dimension one, so an invertible \(eJ\) cannot annihilate it as every bounded \(DC_0D^*\) does.

For the resolvent pencil, the imaginary-part estimate follows from the signs of \((z-e)^{-1}\) and \((z+e)^{-1}\), with \(2-U\) and \(2-V\) positive.
The estimate for the adjoint eliminates the cokernel and supplies a bounded inverse throughout the upper half-plane.
Direct block multiplication verifies (5) in its stated noncommuting order.
The finite-cell Green matrix also has strictly negative imaginary part on every nonzero cell vector, so its inverse and the first-return convention are well defined there.

### Lattice matrices, regular parameters and all atoms

Independent sign changes of the two sine coordinates give every entry of (6), including the factor \(1/4\) in the edge cross term.
Expansion of the fiber determinant gives (7).
For \(\lambda\ne-e\), the nonzero coefficient of \(U\) leaves a zero-measure set of \(\theta\) at each fixed \(\phi\).
At \(\lambda=-e\), the remaining expression is \(2e(2-V)\), whose zero set also has Haar measure zero.
Thus this argument excludes every lattice atom, including the edge parameters.

The zero level of \(T_e\) is regular precisely at the permitted parameters other than \(e=2\), with \(c=0\) covered by its nonvanishing \(\theta\) derivative.
Conditioning on one arcsine coordinate gives the stated delta density.
Exchanging the two coordinates and scaling when \(|c|>1\) gives (8) with modulus \(\min(1,|c|)/\max(1,|c|)\), not its square.
The zero fiber is simple because its edge block is invertible.
The eigenvalue derivative is \(e/(e^2+x+y)\), so the spectral density matrix is exactly \(|e|\mathbb E[ww^*\delta(T_e)]\).
This accounts for both the absolute value of \(e\) and the normalization by three in the scalar density.
Simultaneous sign reversal of \(U,V\) gives the two first weighted delta moments \(2I_0\).
Separate sine sign changes on a regular zero-curve piece force every constant annihilating vector to vanish, proving strict matrix positivity for all these parameters.

The elementary arcsine Cauchy transform gives \((A_u,A_v)=(1,0)\) for \(|c|<1\), including \(c=0\), and \((0,1/c)\) for \(|c|>1\).
Parity gives the zero principal values of \(1/T_e\) and \(UV/T_e\).
Substitution of the remaining weighted principal values in (6) yields every real entry of (9), including its edge cross entry.
Regular coarea densities justify the weighted boundary limits and smoothness near zero.
Strict negativity of the boundary imaginary part proves invertibility and the finite first-return limit.
Taking the trace gives the displayed scalar boundary and small-window probability, with the unnormalized cell trace divided by three only at that last stage.

### Critical lattice constants and inverse limit

At \(e=2\), the two saddles and the derivative \(\lambda=T/4+O(T^2)\) give exactly the logarithmic coefficients in (10).
The factorization using \(\kappa\) and \(\omega\) follows by direct expansion of (7), and \(R_z=(2-z)\widetilde R_z\) has the stated sign.
On \(z=i\eta\), both comparison denominators are bounded below by a constant times \((T^2+\eta^2)^{1/2}\).
The \(O(\eta^2)\) perturbation therefore gives the claimed \(O(\eta\log(1/\eta))\) weighted expectation error.
The isotropic lattice transform and its elliptic endpoint expansion give \(g_T(4i\eta)=-i\log(4/\eta)/(2\pi)+o(1)\), fixing both the constant inside the logarithm and its sign.

Symmetry gives the two weighted \(U,V\) limits \(-1/2\).
On \(T=0\), \(xy=4\sin^2\phi\), so direct conditional arcsine integration gives \(\mathbb E[xy\delta(T)]=4/\pi^2\).
The weight vanishes quadratically at the saddles, making its density continuous there and permitting the finite weighted boundary limit.
Parity and \(xy=4-2T+UV\) give the principal value \(-2\).
The resulting limit of \(\mathbb E(xyR_z)\) is \(4-8i/\pi\), including the nonzero imaginary constant needed in \(J_0\).
Substituting these quantities in (6) gives all entries of \(B_0,J_0\) and both terms of (11).

The kernel of \(B_0\) is exactly the line spanned by \(n=(1,1,-1)^{\mathsf T}\), and direct multiplication gives \(n^*J_0n=-i/\pi\).
Schur inversion on that line and its orthogonal complement gives \(G^{-1}\to nn^*/(n^*J_0n)=i\pi nn^*\), with no missing normalization by \(\|n\|^2\).
This proves (12) and excludes a first-return pole despite the logarithmic Green divergence.

### Free-tree matrix and physical branch

The compressed \(U,V\) operators still have norm at most two, so the same dissipative-pencil estimate defines actual cavity resolvents throughout the upper half-plane.
The two deleted-edge types have the multiplicities in (13).
Both orientations carry the same analytic coefficient, explaining the squares \(p^2,q^2\).
Successive elimination along a reduced-word path gives the product \(gx_F^{n_u}y_F^{n_v}\).
The coefficients at words of lengths zero, one and two then give every entry of (14), including its unequal edge parameters and cross term.

For \(c\ne0\), an unbounded cavity cluster contradicts either one reciprocal equation or the invertible system of two leading linear combinations when both entries are unbounded.
A vanishing cluster entry would force the other to be unbounded.
Thus every cluster pair is finite and nonzero.
Eliminating its ratio gives the displayed quadratic for \(r_*\) and the displayed value of \(h_u^2\).
The positive root has the two imaginary solutions, of which only the negative-imaginary one is dissipative.
Its value gives (15)--(16), including the factors \(|e|\).

The negative root belongs to \((-2,-1/2)\) and gives real pairs.
The derivative of the reciprocal equations has determinant \(4p^2q^2(1+r_*+r_*^{-1})\), which is nonzero at every such pair.
A real cluster would therefore lie on a local holomorphic branch whose imaginary diagonal is \(O(\eta)\).
The resolvent identity then bounds the squared norm of its Green column uniformly by \(-\operatorname{Im}h_j/\eta\).
At the real pair, the \(u\)-ray factor has squared modulus at least one for \(c^2\ge1\), and the \(v\)-ray factor has squared modulus at least one for \(c^2\le1\).
The corresponding forward ray exists in that cavity subtree.
Its pointwise limiting column is not square summable, contradicting the uniform bound by Fatou's lemma, including \(c^2=1\).
Continuity and the finite possible cluster set then force the physical limit rather than merely producing a candidate algebraic solution.

At \(e=1\), \(q^2h_v=O(\eta)\) follows from the actual resolvent norm bound, and the remaining quadratic forces \(h_u\to-i\).
The other equation gives \(h_v\to-i/2\).
The limiting Jacobian is nonsingular in this case as well as on the positive-root branch for \(c\ne0\).
The resulting holomorphic continuation is that of the upper scalar boundary functions; it is correctly distinguished from continuation of the full operator resolvent across its spectrum.

### Free density, residues and perturbation limit

Substitution into (14) yields the complete finite boundary and exactly the imaginary matrix in (17).
After diagonal scaling, its root Schur complement has off-diagonal entry \(XY\).
The identity \((XY)^2=r/[(r+2)(1+2r)]\le1/9\) follows from the ratio equation and \(2(r-1)^2\ge0\); at \(c=0\), the product is zero.
Thus the boundary is strictly dissipative and invertible for every real \(e\ne0\).
The analytic upper boundary branch gives analytic cell densities on a neighborhood of zero, with no singular measure there.
The trace gives both parts of (18), including \(g_{1,F}=1/3-5i/6\) and \(g_{2,F}=1/6-i/\sqrt3\).

The positive densities give a spectral interval through zero in both models, with the lattice logarithm treated separately.
The spectral multiplier \(i\eta/(i\eta-\lambda)\) is bounded by one and converges pointwise to the zero-eigenvalue indicator.
Since that projection vanishes, the spectral theorem gives strong convergence to zero in (19).
Since zero remains in the spectrum, its operator norm is one for every \(\eta>0\).
The finite matrix expansions give the two asserted cell-residue rates.
The elliptic endpoint behavior at \(|e-1|\to1\) and \(\gamma(-1)=\sqrt3/4\) give both constants in (20), from either permitted side of \(e=0\).
Norm convergence of \(H_e\) to the exact v2 operator gives convergence of the fixed-\(\eta\) resolvents, while the accepted v2 atom has mass \(1/3\).
This proves the two different iterated scalar residue limits without asserting a uniform density bound.

### Height layers and exclusion of the remaining free atoms

The coordinates on \(t^nN\) identify right \(N\)-translation consistently across layers, so the coefficient operators and the finite graph maps are equivariant for the same right action.
The equation at layer \(n-p\) solves for the next unknown using \(A_{n-p,q}^{-1}\).
Iterating only finitely many times makes a bounded map from the first \(q-p\) layers into the rest of any finite interval.
No uniform inverse bound in \(n\) or in the interval length is needed.
Its graph has dimension \(d(q-p)\) by coordinate restriction and polar decomposition.
The range of the positive contraction \(\chi_mP\chi_m\) lies in this closed graph, so its trace is bounded by that dimension.
Every layer diagonal has the same trace as the identity layer by right-translation equivariance of the global kernel projection.
This proves (22); division by \(m\) and faithfulness prove injectivity.
The sole-coefficient case proves the zero-bandwidth assertion separately.
No amenability, ordering of \(N\), or group-ring rank-integrality premise enters this argument.

For the two current groups, the height choice \(\varphi(u)=1,\varphi(v)=0\) gives nonzero unit extreme coefficients for \(T_e\) and for each real Schur pencil with \(\lambda\ne\pm e\).
At \(\lambda=e\), the first edge equation forces the root vector to vanish by the infinite-order shift argument, then forces the second edge coordinate to vanish and finally the first edge coordinate to vanish.
At \(\lambda=-e\), the same argument uses the other generator.
These cases cover all real spectral parameters and prove the full free-model atomlessness asserted in the statement.

### Ordered-quotient source and the indicable scalar application

The reviewer inspected the actual local journal page images of Linnell, *Zero divisors and \(L^2(G)\)*, C. R. Acad. Sci. Paris, Series I, 315 (1992), 49--53, at printed pages 50--51.
Theorem 4 starts on page 50 and concludes on page 51 of the [primary scan](https://math.uchicago.edu/~shmuel/L%5E2%20cohomology%20readings/Linnell,%20zerol2.pdf).
It has exactly the stated normal-subgroup, right-orderable-quotient and least-support conditions.
Its least coefficient is tested against every nonzero element of the subgroup von Neumann algebra, and its conclusion concerns every nonzero vector of the full group \(\ell^2\) space.
The target's scalar-unit specialization meets that premise directly.
This is an accepted statement-and-applicability input; the complete historical proof was not re-audited.
The source is not used as a matrix-valued theorem.

For the added application, a nonzero map from \(H=\langle u,v\rangle\) to \(\mathbb Z\) has nonzero height on at least one of its two generators.
When the absolute heights differ, including the case that exactly one is zero, the least supported term is unique and has nonzero scalar-unit coefficient.
When they agree, both are nonzero, and the two least terms factor to \(1+ch\) in the height kernel, up to a group unit.
For \(|c|\ne1\), the geometric inverse exists, factoring the larger term when necessary.
The excluded value \(e=0\) removes \(c=-1\); for the remaining unit-modulus case \(c=1\), the coefficient is either \(2I\) or an injective \(1+h\) with \(h\) of infinite order by torsion-freeness.
Injectivity on \(\ell^2\) implies the precise coefficient premise on the von Neumann algebra vectors used in Theorem 4.
For \(c=0\), the stated infinite-order shift argument for \(u+u^{-1}\), or the value \(2I\) when \(u=1\), handles the discarded generator directly.
Left convolution preserves each right coset \(Ht\), so the conclusion transfers from \(H\) to the ambient group.
This checks the entire added scalar application, without any inference about arbitrary matrices over an indicable group.

### Torsion obstruction and scope

For \(C_2*C_3\), the two actual labels generate an infinite group, so the accepted collective-holonomy criterion gives the old incidence kernel dimension one.
The elements \(p,r\) are the subgroup-averaging projections with the stated traces, and \(V=3r-I\) gives \(V^2=I+3r\).
The equation \(uf=-Vf\), compared in squared norm, forces \(rf=0\), then \(uf=f\); the converse also holds.
Thus (23) identifies the exact kernel, rather than merely an included subspace.
Rank subtraction for \(rp\) gives the lower bound \(1/2-1/3=1/6\), and containment in the range of \(p\) gives the upper bound \(1/2\).
The whole interval is positive and excludes every integer.
Schur dimension equality and division by three give the claimed perturbed dimension and atom interval.
No exact free-product atom calculation is required.
The group has torsion, so this is only an obstruction to preserving the prior holonomy certificate, not a counterexample to the [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).

## Source and conclusion limits

The reviewer also directly checked [DLMF 19.12.1 and the value following 19.12.3](https://dlmf.nist.gov/19.12): the convergent complementary-modulus series uses the principal logarithm and \(d(0)=2\log2\).
That precise endpoint input, together with the accepted isotropic transform, suffices for the logarithmic constants and the small-\(e\) density asymptotic.
The reviewer directly checked the subsequently cited [DLMF 18.40.6](https://dlmf.nist.gov/18.40.E6), including its principal-value term and negative imaginary jump for the \((z-t)^{-1}\) convention.
The locally smooth weighted coarea densities meet the boundary-formula hypotheses; signed or complex matrix weights are handled by linearity.
These DLMF source derivations were not audited.
The earlier independent reviews are reused only for the explicitly identified unchanged inputs; their findings are not relabelled as reviews of v3.

The current argument proves the two complete model calculations and its stated structured kernel criteria.
It does not prove integrality for arbitrary group-ring matrices, characterize groups without a usable quotient, compute an exact torsion-example atom, or establish a new Atiyah group class.
No unresolved source-applicability issue was found within the stated scope.
The target's mathematical assessment and any Task lifecycle decision remain separate acts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0004_v3.md#statement) | Exact four-part statement, all hypotheses, real nonzero parameters, trace conventions, complete matrix models, atom exclusions, residue limits and stated structured extensions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0004_v3.md#argument) | Complete current argument, formulas (1)--(23), all intervening derivations, source interfaces, indicable scalar application and final limitations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Critical lattice boundary](../../claims/Yin_C_A0004_v3.md#lattice-critical-boundary) | Complete \(e=2\) matrix constants, logarithmic normalization, weighted cross-entry limit and rank-one inverse and first-return limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Free physical branch](../../claims/Yin_C_A0004_v3.md#free-cavities-and-physical-branch) | Actual cavity inverses, full matrix coefficients, all algebraic cluster pairs, exclusion of real branches, \(e=1\) degeneration and local upper-branch continuation. |
| [Whole-artifact finding](#whole-artifact-finding) | [Height-layer certificate](../../claims/Yin_C_A0004_v3.md#height-layer-certificate) | General finite-band matrix argument, no uniform inverse-bound assumption, exact compressed-trace estimate and all-atom application including both edge parameters. |
| [Whole-artifact finding](#whole-artifact-finding) | [Ordered quotient and indicable application](../../claims/Yin_C_A0004_v3.md#ordered-quotient-source) | Lin92 Theorem 4 statement and applicability only; unique extreme coefficient, complete torsion-free two-generator indicable scalar application, and its matrix and source-proof limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Holonomy obstruction](../../claims/Yin_C_A0004_v3.md#holonomy-obstruction) | Exact \(C_2*C_3\) kernel identification, positive nonintegral dimension interval, normalized atom interval and torsion-free-contract exclusion. |

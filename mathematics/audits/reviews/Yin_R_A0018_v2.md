---
author: Yin
---
# Independent review of infinite commuting projection orbits

Review time: 2026-11-11T15:33.
Human record author: Yin.
The exact target is the saved 2026-11-11 revision of [C_A0005_v2](../../claims/Yin_C_A0005_v2.md#statement) and its complete [argument](../../claims/Yin_C_A0005_v2.md#argument), including formulas (1)--(18), the corrected additive formula (10), the finite Boolean orbit and augmentation rigidity subsections and all realization and source qualifications.
This is new evidence for the infinite-orbit continuation in the same review family as R_A0018_v1; it does not replace that earlier review's different input scope.

## Arrangement and inputs

An agent outside substantive proof development performed this whole-artifact inspection.
The reviewer received the fixed candidate, the named direct dependency and original-source locations, the review assignment, and administrative framework, operator and execution facts.
No development draft, proof-generation dialogue, mathematical development summary, proposing-agent explanation or previous review conclusion was supplied or consulted before the initial findings.
The reviewer enumerated the obligations from the exact statement, checked the complete argument and then directly read the [v1 projection-middle subsection](../../claims/Yin_C_A0005_v1.md#projection-middle-and-finite-orbits) and the relevant original LNW08 passages.
No earlier R finding was relied on.

During this inspection the reviewer reported a missing plus sign in formula (10), with the countercheck described below, without editing the Claim.
The authoring agent restored that symbol to match the two orthogonal summands already stated in the original prose, and the reviewer checked the saved correction and its existing argument.
The reviewer supplied no new substantive construction or replacement proof.
The finite Boolean orbit and augmentation rigidity subsections and the corresponding statement sentences were subsequently supplied only as saved additions to the fixed candidate, without their development context.
The reviewer independently checked those additions and their affected statement and continuation interfaces, together with the complete candidate already inspected, before recording this finding.
These are the actual input and recheck conditions underlying the independent relationship, not a claim that the original missing-symbol display was correct.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#finding-infinite-orbit) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#finding-infinite-orbit) | [C_A0005_v2 statement](../../claims/Yin_C_A0005_v2.md#statement) | All hypotheses and conclusions, including arbitrary commuting translates, unnormalized trace, infinite-component exhaustion, exact atoms and truncation, actual projections, realization restrictions, the abelian matrix-family bound and adjacent-commutation rigidity. |
| [Whole-artifact finding](#finding-infinite-orbit) | [C_A0005_v2 argument](../../claims/Yin_C_A0005_v2.md#argument) | Complete saved argument, formulas (1)--(18), corrected additive (10), all boundary and limit steps, conditional constructions, augmentation rigidity and actual source-use interfaces. |
| [Whole-artifact finding](#finding-infinite-orbit) | [Finite Boolean orbit argument](../../claims/Yin_C_A0005_v2.md#a-trace-lower-bound-forces-a-finite-boolean-orbit) | The uniform trace lower bound on every nonzero finite Boolean product, maximal partition proof, transport periodicity, torsion-free abelian group-ring matrix application and individual-trace counterexample. |
| [Whole-artifact finding](#finding-infinite-orbit) | [Augmentation rigidity argument](../../claims/Yin_C_A0005_v2.md#augmentation-rigidity-for-abelian-group-ring-matrix-projections) | Adjacent commutation under entrywise group-automorphism transport, zero-augmentation difference projections, fixedness, injective residual and the actual kernel projection, integer trace and normalization in (18). |
| [Whole-artifact finding](#finding-infinite-orbit) | [C_A0005_v1 projection-middle interface](../../claims/Yin_C_A0005_v1.md#projection-middle-and-finite-orbits) | The bounded projection-middle kernel isomorphism at zero potential and the finite-path module interface used by v2; no whole-v1 review or reliance on its general affiliated-operator reduction. |

## Obligations and decisive checks

### The complete component decomposition

The required partition must account for every retained site, not merely exhibit some orthogonal finite paths.
With \(p_j=\sigma^{-j}(p)\), the translate \(\sigma^j(e_\ell)\) has retained interval \([-j,\ell-1-j]\) and deleted neighbors \(-j-1,\ell-j\).
Two different intervals containing zero impose incompatible retained/deleted conditions at a boundary, so these projections are pairwise orthogonal and lie below \(p\).
Trace invariance gives the same mass \(\tau(e_\ell)\) to each of the \(\ell\) positions.
Both exterior inequalities in (7) have the correct orientation.

For a right-infinite start, every positive translate requires site \(-1\) to be retained, whereas the unshifted start deletes it.
Translation then proves pairwise orthogonality of all its translates.
Their equal traces and the finite total trace force that trace to vanish, and faithfulness forces the projection itself to vanish.
The reversed argument handles left-infinite starts; the countable family of their translates exhausts the half-infinite possibilities.
The remaining full-line event is exactly \(p_\infty\).
The countable commuting spectral partition therefore proves strong equality in (3), and normality gives its trace equality.
This step requires neither probabilistic independence nor ergodicity nor a finite orbit.

### Path modules, residual nullity and the full kernel

For \(x_j\in e_\ell\ell^2(G)\), the vectors \(t^jx_j\) lie in the stated orthogonal ranges, and the displayed \(U_\ell\) is a surjective equivariant isometry.
Compression kills precisely the two exterior terms in (7), while the interior terms have coefficient one.
Thus the claimed reduction to \(J_\ell\) in (8) is exact, including paths of length one.
The sine eigenvectors give all \(\ell\) eigenvalues, and zero occurs once precisely for odd \(\ell\).
Each such direction is one copy of the \(e_\ell\)-module, with trace \(\tau(e_\ell)\), not a normalized corner trace.

The shift fixes \(p_\infty\), so the all-open corner reduces \(T\).
On the full group Hilbert space, left translation by the infinite-order element \(t\) splits into bilateral-shift representations over the right cosets of \(\langle t\rangle\).
Fourier transformation gives multiplier \(2\cos x\), whose zero set has Haar measure zero.
Thus \(T\), and hence its all-open reducing restriction, is injective.
There is no omitted zero mode at infinity.

The equations for \(H_p(x,y)=0\) give \(x=px\), \(pTx=0\) and \((1-p)y=-(1-p)Tx\).
Consequently the proposed graph map from \(\ker(R|_p)\oplus p\ell^2(G)\) is bounded, injective and surjective, with inverse given by the first coordinate and the \(p\)-part of the second coordinate.
This directly verifies the v1 bounded interface at zero potential and proves the dimension identity in (4).
There is no domain replacement involving unbounded affiliated operators.

The trace identity (3) controls the omitted odd lengths by \(\ell/(L+1)\), proving (5) for every integer \(L\ge0\).
The identity \(\sum_{\ell\ge1}e_\ell=p(1-p_{-1})\) follows by excluding the zero right-infinite start.
It yields \(\sum_{\ell\text{ odd}}\tau(e_\ell)\le1-\tau(p)\) and the stated upper bound one on unnormalized nullity.
At \(p=0\), both coordinates are forced to vanish; at \(p=1\), injectivity of \(T\) leaves exactly the free lower coordinate.
These give nullities zero and one and check the two-coordinate factor \(1/2\).

### The actual projections and spectral limits

For odd \(\ell=2m+1\), the translated ranges make \(V_\ell^*V_\ell=e_\ell\), and its alternating even-site coefficients are the normalized zero eigenvector of \(J_\ell\).
The orthogonal strong sum in (9) is therefore exactly the residual kernel projection \(k_R\).
The full graph ranges need not be orthogonal across paths, since deleted boundary coordinates can be shared.
The use of the single global Gram inverse in (10) is necessary and correct.

The first inspected display of (10) omitted the plus sign after \(\operatorname{diag}(0,p)\).
Read literally as multiplication, it vanished because \(\operatorname{diag}(0,p)W=0\), contradicting the already checked case \(p=1\).
The saved display now adds that free-coordinate projection to the graph projection, consistently with the unchanged surrounding argument.
On the \(k_R\)-corner, \(k_RW^*Wk_R\ge k_R\), so its inverse and inverse square root are bounded there.
The operator \(Wk_R[k_RW^*Wk_R]^{-1/2}_{k_R}\) has initial projection \(k_R\) and final projection equal to the second term of (10).
That final range is orthogonal to the free lower \(p\)-module, so their sum is precisely the full kernel projection and its trace is \(\tau(p)+\tau(k_R)\).
The convention for \(k_R=0\) is consistent.
This recheck resolves the displayed-symbol defect at its actual scope.

For the all-open component, the zero nonconstant Fourier coefficients \(\tau(p_\infty t^n)=0\) follow from nonzero height and \(p_\infty\in\mathcal N(N)\).
Hence the \(p_\infty\)-weighted unitary spectral measure is its trace times Haar measure, whose pushforward under \(2\cos x\) is the stated arcsine component.
The path block spectra and their unnormalized module weights give all remaining terms in (11).
The total mass is exactly \(\tau(p)\), and the resolvent series is absolutely controlled by that mass divided by \(|\operatorname{Im}z|\).
The branch \(\sqrt{z^2-4}\sim z\) gives the correct Cauchy transform on both half-planes.
Finally, \(|i\eta/(i\eta-x)|\le1\) and its pointwise limit is the indicator of zero, so dominated convergence proves the claimed residue without exchanging an uncontrolled path-length limit.
Neither the continuous all-open spectrum nor accumulation of nonzero path eigenvalues contributes an extra atom.
The candidate correctly restricts the complete law (11) to \(R|_p\) and transfers only the established zero atom to \(H_p\).

### Realizations and exact algebraic restrictions

The restricted wreath product \(\mathbb Z\wr\mathbb Z\) is torsion free by the height homomorphism and the torsion-free base.
Product Haar measure gives independent translated arc projections and the exact weights \((1-\theta)^2\theta^\ell\).
Their distinctness follows from the strictly positive mixed trace \(\theta(1-\theta)\).
The all-open event has zero mass, and summing the odd geometric series gives (6) and (12), including both numerical examples.

A scalar finite-support projection over a torsion-free abelian coefficient group lies in a finite-rank free abelian subgroup algebra.
Its continuous idempotent Fourier function on the connected finite torus is constant zero or one.
The Fourier-support argument proves \(\mathbb CG\cap\mathcal N(N)=\mathbb CN\), so enlarging the ambient group does not put the measurable arc projection or its coupling in the group ring.
The finite-lamp comparison uses an actual averaging projection of trace \(1/|F|\); distinct lamp copies supply the same product-trace calculation and give (14).
Those ambient groups have torsion, so this example is outside the A0001 contract.

The hypothetical nontrivial scalar projection in \(\mathbb CK\), for torsion-free \(K\), would have trace strictly between zero and one by faithfulness.
Different lamp copies in \(K\wr\mathbb Z\) commute even if \(K\) itself is nonabelian, their traces factor, and the height argument still proves torsion freeness.
Thus the conditional construction is valid; it does not assert that its premise is attainable.
The converse requirement of a scalar group-ring projection in the specified model follows from (13).
For actual matrix projections over torsion-free abelian \(N\), continuous rank on a finite connected torus is constant and has integer integral.
Kernel and spectral projections of a group-ring matrix need not themselves belong to that group ring, so the candidate correctly refuses to transfer this conclusion to them without further input.

### Uniform trace bounds and finite Boolean families

For each finite commuting subfamily, the Boolean products (15) are orthogonal projections summing to one.
The uniform positive lower bound limits their nonzero number to \(\lfloor D/\delta\rfloor\).
The attainable numbers are bounded integers, so one finite subfamily attains their maximum \(m\).
Adjoining any other member cannot split a nonzero atom into two nonzero pieces: both would meet the same trace hypothesis, and the number of atoms would increase.
It follows that every member is a sum of the same \(m\) atoms, proving (16), including arbitrary infinite indexing of the original family.
For a full transport orbit, the automorphism preserves this generated finite Boolean algebra and permutes its minimal atoms, which proves periodicity.

Every finite Boolean product of commuting projections in \(M_d(\mathbb CN)\), for torsion-free abelian \(N\), is again a finite-support projection matrix.
Its entries collectively involve only a finitely generated free abelian subgroup, so the previously checked connected-torus rank argument makes its nonzero trace a positive integer.
Thus \(D=d\) and \(\delta=1\) are justified for all the necessary intersections, giving the asserted bound \(2^d\) without assuming the general Atiyah statement.
The scope remains torsion-free abelian \(N\), as in the statement's preceding scalar exclusion.
For the Bernoulli example at \(\theta=1/2\), each \(Q_j\) has trace one, but a product at \(r\) distinct sites has two diagonal contributions of trace \(2^{-r}\), proving (17).
These are infinitely many distinct commuting projections in the von Neumann algebra, and their intersections have no uniform positive trace lower bound.
The example therefore establishes exactly the claimed insufficiency of individual integer traces.

### Augmentation rigidity and the enlarged matrix model

For entrywise transport by a group automorphism, augmentation satisfies \(\varepsilon\circ\sigma=\varepsilon\) and is a unital star homomorphism on the group ring \(\mathbb CN\).
Adjacent commutation makes \(E:=P(I_d-\sigma(P))\) a selfadjoint group-ring matrix projection.
Its augmentation is zero because \(\varepsilon(P)\) is itself a projection and equals \(\varepsilon(\sigma(P))\).
The finite support of \(E\) is contained in a finitely generated free abelian subgroup.
Its Fourier transform is a continuous projection matrix of constant rank on that subgroup's connected dual torus, and the rank at the trivial character is zero.
Therefore \(E=0\).
The reversed difference \((I_d-P)\sigma(P)\) has the same properties and vanishes as well, giving \(P=P\sigma(P)=\sigma(P)\).
This proves fixedness from adjacent commutation alone, without assuming commutation of all translates or invoking the general Atiyah conjecture.

Fixedness implies that \(P\) commutes with \(tI_d\), so its corner reduces \((t+t^{-1})I_d\).
The bilateral-shift injectivity argument already checked applies to all \(d\) coordinates and hence to this reducing corner.
The kernel equations then force the first \(d\) coordinates to vanish and leave exactly the lower \(P\)-module.
Thus the actual projection is \(\operatorname{diag}(0,P)\), as in (18).
Constant rank for \(P\) identifies its unnormalized trace with \(\operatorname{rank}_{\mathbb C}\varepsilon(P)\), an integer from zero to \(d\), and the probability atom requires division by \(2d\).
The stated exclusion of an extra unrelated unitary conjugation in the matrix coordinates is justified: such a transport need not preserve the augmentation matrix, so the zero-augmentation difference argument is not supplied for it.
The final continuation boundary correctly keeps nonabelian coefficient groups and projections outside the group ring distinct from this established abelian rigidity result.

## Source interfaces and remaining limits

The reviewer directly inspected the locally held original [LNW08 arXiv v2, Theorem 1.5](../../literature/pdf/LNW08/arxiv-v2.html#S1.E5), including its relation between the finite-lamp Plancherel law and the expected absorbing-cluster spectral measure.
The reviewer also inspected [Section 2B](../../literature/pdf/LNW08/arxiv-v2.html#S2.SS2), including the finite-cluster projection definition, orthogonality statement and boundary intertwining, and [Section 4A](../../literature/pdf/LNW08/arxiv-v2.html#S4.SS1), including the arbitrary-parameter projection on \(\mathbb Z\), its interval-indicator Fourier transform and the loss of finite-support eigenfunctions.
The original [Section 2D](../../literature/pdf/LNW08/arxiv-v2.html#S2.SS4) uses torsion freeness of the base group, which does not remove torsion from a finite lamp group in the wreath product.
These passages support the candidate's actual comparison and attribution statements.
The source uses a probability-normalized walk and a full-space law, whereas the candidate proves its adjacency normalization and \(p\)-corner law directly; no equality of these differently normalized measures is imported.
The two-coordinate graph formula and the arbitrary commuting-orbit exhaustion are checked through the local proof rather than asserted as consequences of the paper.
The arbitrary-parameter lamp construction is correctly identified as prior literature.

This inspection does not constitute a complete audit of LNW08's proofs or a historical-priority search.
The source comparisons introduce no unverified necessary theorem premise into the self-contained local path argument.
Standard spectral calculus, faithful normal trace properties, Fourier transformation for abelian groups and bounded equivariant dimension invariance are used at their ordinary foundational scope, without re-proving their general theories.
The non-projection singular-middle theory, noncommuting transport and finite-section generalities in C_A0005_v1 are outside this finding except for the precise bounded interface bound above.
There is no proof-assistant certification or claim of the general A0001 conclusion.

## Finding infinite orbit

The complete saved statement and argument of C_A0005_v2, including the corrected additive (10), the finite Boolean orbit criterion and augmentation rigidity through (18), are supported by this independent inspection.
No unresolved mathematical gap remains in those stated conclusions or their actual source-use interfaces.
The initial missing-symbol display was false and has been rechecked only in its saved corrected form, as explained above.
The existence of a nontrivial scalar group-ring projection for a general torsion-free coefficient group remains a conditional realization premise, not an established example and not a gap in the proved implication.
Arbitrary spectral projections remain outside the finite-support projection argument.
This finding supplies review evidence for the exact candidate and does not itself select a C assessment, complete A0001 or assert integrality for arbitrary torsion-free group-ring matrices.

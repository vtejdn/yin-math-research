---
author: Yin
---
# Finite-kernel window compatibility: independent whole-proof review

Date of the review act: 2026-11-12T14:29.
The human record author is Yin.
The inspected artifact is the 12 November 2026 working revision of [C14 v4](../../claims/Yin_C_A0014_v4.md), including its explicit finite matrix with rows in \(SF\), columns in \(F\), and entries \(a(yx^{-1})\).

This is an independent whole-proof inspection by a separately organized reviewing agent outside substantive proof development.
The reviewer received the fixed artifact, necessary direct dependencies, review instructions and execution metadata.
No exploration draft, proof-generation dialogue, author explanation, proposed repair or earlier R finding was supplied or consulted.
The only subsequent artifact clarification identified the saved finite-matrix setup addition, which was read in the artifact.
The reviewer did not develop or edit the argument.
Obligations were reconstructed from the statement and checked against the complete argument before this finding was recorded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument) | [C14 v4 statement](../../claims/Yin_C_A0014_v4.md#statement) | Every displayed assertion (1)–(16), all quantifiers and group hypotheses, the actual tied convolution coefficients, and the stated limitations. |
| [Whole-argument finding](#whole-argument) | [C14 v4 argument](../../claims/Yin_C_A0014_v4.md#argument) | The complete coefficient-map, window-compatibility, row-witness, cut-energy, trace-limit and solid-norm arguments, including auxiliary equations (17)–(22). |
| [Whole-argument finding](#whole-argument) | [C14 v4 scope](../../claims/Yin_C_A0014_v4.md#scope-and-remaining-structural-input) | No independent correlation upper bound, no uniform kernel approximation, no new group-class theorem and no completion of the general amenable problem. |
| [Whole-argument finding](#whole-argument) | [C14 v3 finite-kernel interface](../../claims/Yin_C_A0014_v3.md#finite-window-kernel-correlation-criterion) | Basis-independent finite average, \(0\le b_F\le p\), exact kernel membership and the torsion-free amenable norm failure. |
| [Whole-argument finding](#whole-argument) | [C14 v3 positivity proof](../../claims/Yin_C_A0014_v3.md#positivity-finite-propagation-and-the-exact-kernel-average) | Coefficient orientation, Bessel normalization and the trace and kernel-support identities actually reused. |
| [Whole-argument finding](#whole-argument) | [C14 v3 norm obstruction](../../claims/Yin_C_A0014_v3.md#correlation-bounds-and-their-precise-force) | The concluding spectral-gap argument proving \(\|p-b_F\|=1\); no new review of the separate global-filter assertions is claimed. |
| [Whole-argument finding](#whole-argument) | [C1 v2 localization statement](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization) | Scalar group-ring specialization with no auxiliary state: boundary deficit and complete finite-support kernel density. |
| [Whole-argument finding](#whole-argument) | [C1 v2 localization proof](../../claims/Yin_C_A0001_v2.md#proof-of-complete-rational-kernel-localization) | Local projection dimensions and faithful-trace argument establishing the reused density conclusion. |
| [Whole-argument finding](#whole-argument) | [C1 v1 finite matrix estimate](../../claims/Yin_C_A0001_v1.md#matrix-boundary-estimate) | Supporting check of the one-column finite-propagation bound and its inner-boundary constant. |
| [Whole-argument finding](#whole-argument) | [BCM04 assembly trace](../literature/BCM04/Yin_U001.md#assembly-trace) | Theorem 6.3 and Definition 3.5 in the recorded author edition, and their scalar projectionlessness specialization together with HK97. |
| [Whole-argument finding](#whole-argument) | [HK97 amenable assembly](../literature/HK97/Yin_U001.md#amenable-assembly) | Corollary 1.3 for countable amenable groups, accepted at the source unit's statement-and-applicability depth. |
| [Whole-argument finding](#whole-argument) | [Nic08 related mechanism](../literature/Nic08/Yin_U001.md#nic08-u001) | Attribution and hypothesis distinction for the final arXiv v2 Proposition 8.7; this source is related context, not a logical premise of the local moment proof. |

<a id="whole-argument"></a>
## Whole-argument finding

The complete statement and argument are mathematically correct at their explicit scopes.
No gap requiring repair was found.
The following checks give the decisive evidence for this conclusion.

### Coefficient map, normalization and window geometry

The row-operator formula for \(\Phi_F\) has the displacement \(yx^{-1}\), so its complete positivity and its value \(1\) on the finite identity are correct.
For \(T_F:=P_FpP_F\), the containment of the finite kernel gives \(T_FQ_F=Q_FT_F=Q_F\).
Consequently \(T_F-Q_F\) is a positive contraction with ordinary trace \(|F|\delta_F\), and the entrywise Cauchy--Schwarz estimate gives precisely \(\sqrt{|F|\delta_F}\).
It does not give \(\sqrt{\delta_F}\).
The positive-trace coefficient estimate applies separately to \(r_F-b_F\) and to \(p-b_F\).
All the orders and coefficient estimates in (2) follow.

The direct scalar specialization of the finite-propagation estimate has boundary coefficient one.
The right-invariant metric and left multiplication by the support of \(a\) give exactly the displayed inner boundary.
Amenability is needed to make this defect small along a Følner sequence; no inverse-propagation assumption enters.

Right translation sends a kernel vector to \(\xi\lambda_z\), and cancellation of \(\lambda_z\lambda_z^*\) proves the invariance of its convolution square.
For nested windows, zero extension makes the smaller kernel projection dominated by the larger one.
For disjoint windows, the sum of the smaller projections is a projection, so its difference from \(Q_E\) has rank \(d\) and Hilbert--Schmidt norm \(\sqrt d\).
This verifies (4)–(6), including \(ac=0\), the trace normalization and the unnormalized error.
The intersection and dimension identities in (7) require no orthogonality for overlaps.
The conditional tiling estimate (18) retains its factor \(\sqrt{|E|\delta_F}\).
No existence of a tiling is inferred.

### Strong sums and the fixed-row estimate

For each coordinate, exactly \(|E|\) right translates \(Ez\) contain it.
The positive partial sums of \(Q_{Ez}\) are bounded by the corresponding coordinate-projection sums.
Their matrix entries are the sums over \(t\in E\) with \(gt\in E\), with \(g=yx^{-1}\), which proves the second strong identity in (19) with the same coefficient convention.

For a row input coordinate, the output support lies in \(Tx\).
The projection \(R_z:=P_{Ez}-Q_{Ez}\) kills that output when the whole support lies inside \(Ez\), because it is an exact kernel vector, and also when it lies outside.
Thus the domain restriction to \(D_z\) is valid for every column of the row.
The compressed positive operator is bounded by \(\|B\|^2(P_{D_z}\otimes I_m)\); summing uses exactly \(d_E(T)\) translates through each coordinate.
This verifies both estimates in (8), with no missing factor \(m\).
The finite union of left-translate symmetric differences proves that \(d_E(T)/|E|\) tends to zero.

Density in the operator-norm closure of the algebraic right annihilator gives the stated left approximate identity on \(J\).
It supplies neither equality with the whole analytic annihilator nor uniform approximation of the full von Neumann kernel.
The reused norm-failure proof applies only with torsion-free amenability and \(0<\alpha<1\), exactly as stated.

### Cut energy, the half-unit obstruction and traces

The coordinate-overlap count yields the Schur multiplier (20).
For positive inputs its partial sums are strongly bounded, and linear decomposition extends it to every bounded input.
Expansion of the commutator squares gives (11) with normalization \(1/|W|\).
Writing the energy in the two diagonal corners of \(Q\) proves positivity and contractivity.
Subtracting \((Q-r)^2\), where \(r:=\mathsf M_W(Q)\), leaves \(r-r^2\ge0\), which verifies the remaining inequality.

For a nontrivial \(p\), an energy norm \(c<1/2\) forces the upper diagonal corner of \(r-1/2\) to be at least \(d:=1/2-c>0\), and the lower one to be at most \(-d\).
The Schur complement subtracts a positive operator from the lower corner, so both the upper corner and that complement are boundedly invertible.
The two nonzero corners also ensure spectral values on both sides of \(1/2\).
Spectral permanence and continuous functional calculus would therefore give a nontrivial projection in the reduced group algebra.
The BCM04/HK97 interface rules this out for the present finitely generated torsion-free amenable group.
The comparison \(r=I/2\) verifies sharpness of this general positive-contraction threshold.

An increasing finite exhaustion makes the union of its finite kernels equal to the entire algebraic kernel, so complete kernel density implies \(Q_{E_j}\to p\) strongly.
For fixed finite \(W\), each multiplier output column has finite support and the multiplier is uniformly bounded.
This proves its strong continuity on bounded sets, and hence strong convergence of the energy operators.
Operator-norm lower semicontinuity gives the stated liminf lower bound.
No Følner hypothesis on the exhaustion is used in (12).

The finite trace expansion in (22) has factor two.
Replacing \(Q_E\) by \(P_EpP_E\) changes each normalized weighted squared-entry sum by at most \(2\sqrt{\delta_E}\), before that factor two.
The resulting sum contains \(\phi_E(g)(1-\phi_W(g))|p(g)|^2\).
The summable majorant \(|p(g)|^2\), whose sum is \(\alpha\), justifies both successive dominated-convergence arguments in (13).
The eigenvalue-count estimate controls the proportion of directions above a fixed threshold and gives no operator-norm upper bound.

### Solid convolution norms and source boundaries

For self-adjoint \(b\), the coefficientwise modulus is symmetric, so its convolution operator is self-adjoint.
Amenability and normalized Følner vectors give its regular norm exactly \(\|b\|_1\).
Faithfulness of the finite trace gives the even-moment formula, without requiring completeness of \(N\), a triangle inequality for \(N\), or spectral invariance of any completion.
Iterated multiplication and the continuous identity-coefficient estimate produce \(C_0M^{2n-1}N(|b|)^{2n}\).
Taking \(2n\)-th roots removes \(C_0\), leaves the factor \(M\), and the modulus inequality supplies \(K\).
Thus the constant in (15) is \(MK\).
The reciprocal-pair argument for positive submultiplicative weights proves (16), including self-inverse group elements.

The Nic08 unit and its edition record identify the related final-v2 unconditional-completion argument and retain its spectral-equivalence premise.
C14 v4 does not attribute the continuous-identity-coefficient hypothesis or the local moment proof to Proposition 8.7.
No source-priority claim or unverified novelty claim is needed for the present result.
This review inspected the retained source-unit evidence and its applicability, not the original Nic08 PDF anew.
The BCM04 and HK97 assembly theorems are likewise accepted established inputs at the recorded statement-and-applicability scope; their substantial original proofs were not independently re-audited.

## Verdict and limits

This finding supports acceptance of the whole C14 v4 statement and argument, including its exact scope section, as independently reviewed mathematics.
It gives no independent general upper bound on \(\mathcal C_F\) and no cut-energy upper bound strictly below \(1/2\).
The latter remains an unresolved sufficient condition.
The fixed-witness norm convergence and the normalized trace estimates cannot be promoted to uniform control of the entire analytic kernel.
No new torsion-free amenable group class, scalar domain theorem or full Atiyah conclusion is proved.
This is not a review selecting or certifying Task completion.

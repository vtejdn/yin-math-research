---
author: Yin
---
# Independent review of Borel corners and two-sided unitary changes

## Whole-proof finding

At 2026-11-13T16:37 UTC a separately assigned agent completed an initial independent review of the [statement](../../claims/Yin_C_F0226_v1.md#statement) and [argument](../../claims/Yin_C_F0226_v1.md#argument) fixed by the [16:33 candidate](../../claims/Yin_C_F0226_v1.md#decision-candidate).
The reviewer had worked on other normal-tuple column and conditional covariance questions using the known normal phase and omitted-algebra graph, and knew that two-sided unitary transformations were under consideration.
The reviewer did not develop this candidate, receive its substantive exploration dialogue or proof summary, or consult its development notes, author explanations or earlier findings about this proof before forming the judgment.
The fixed proof, its direct mathematical inputs and the Task conventions supplied the basis of the review.
All conclusions hold at their stated scopes.

### Compressed Borel tests and the projection gap

Positivity and domination of \(\mu_e(B)=\tau(e1_B(X))\) follow by cycling to the positive compression by \(1_B(X)\).
For a marginal polynomial, the normal phase and the outer product rule give its divided difference off the product-null diagonal.
The omitted-algebra actions put the compressed polynomial in the closed graph with derivative \(e\,\delta P\,d\).
The tested \(\ell\) is a finite sum of actual adjoint-domain tensors.
Cycling \(e,d\) separately against the marginal multipliers in their respective legs produces \(\mu_e\otimes\mu_d\) in that order.
Conjugation of the factor \(\bar z-\bar w\) in the first argument of the Hilbert pairing supplies \(z-w\), exactly canceling the denominator.
The compressed Hilbert input and both one-variable integrals against these dominated measures converge under scalar \(L^2(\mu)\) approximation of \(F\).
This verifies the inequality even when \(F(X)\) belongs to no specified derivation domain, and the zero-projection cases give zero on both sides.
For positive masses, vanishing of all polynomial tensor tests gives equality of \(F(z)\) and \(F(w)\) on the full measure product.
Two independent variables equal almost everywhere must share a constant value, and the complementary measures sum to \(\mu\).
A nontrivial omitted commutant inside \(N\) for a given nontrivial marginal subalgebra would have a nonscalar projection and hence contradict this complementary test.

For projections with diagonal traces bounded away from both endpoints, weak-star compactness of the densities preserves both limiting masses.
Each term of the difference pairing factors into two integrals of bounded functions, so weak-star convergence controls those products for the original measurable \(F\), without needing convergence on arbitrary test functions on a product space.
Were the corners to tend to zero, the same Fubini conclusion would make \(F\) constant on the sum of the two limit measures.
This proves positivity for a fixed trace window.
For the sequence conclusion, \(L_a-R_a\) is normal on \(L^2(M)\) because \(a\) is normal and the left and right actions commute with each other's adjoints.
Hence commuting asymptotically with \(a\) also controls the adjoint and controls both selfadjoint parts of the tested element.
Traciality splits the centered squared norm into the two real variances.
A positive variance limit of bounded selfadjoint laws retains two separated support points.
Choosing a nonatom strictly between them and approximating its spectral indicator by continuous functions with a transition region of arbitrarily small limiting mass yields a sequence of projections of intermediate trace whose commutators tend to zero.
Their one-sided corners would then tend to zero, a contradiction.
These steps prove an assertion for each fixed nonscalar \(a\) and cover arbitrary fixed uniform bounds by scaling.

### Actual twist and the two cost comparisons

Both tuples generate the same von Neumann algebra, since \(U,V\) belong to the unchanged omitted algebra.
In the larger algebra with coefficients in \(N\), bounded strong-star approximation of each omitted coefficient gives graph approximation of every fixed word, since the differentiated factors are fixed coarse vectors.
On this common extension \(a\otimes b\mapsto aU^*\otimes V^*b\) is a coarse bimodule unitary and sends \(\delta(UXV)=U\otimes V\) to the unit tensor.
The two trace cycles and the equality \(\bar\delta(U^*aV^*)=U^*(\bar\delta a)V^*\) give the actual adjoint vacuum \(U\xi V\) on the new dense represented core.
This argument applies to the distinguished coordinate independently of target normality.

On either represented algebra the central-summand theorem supplies an optimal ultraweak-to-weak continuous bounded dual whenever its cost is finite.
Homogeneous bounded-map Fuglede at each omitted normal coordinate gives commutation with the omitted adjoints.
Normality then gives left \(N\)-linearity on bounded inputs by ultraweak density.
For \(E'(a)=E(aV^*)U^*\), the old commutator evaluated on \(VaV^*\) yields the old trace \(\tau(a)\) and the correct output factor of \(U\) on the left.
The input and output twists are surjective isometries.
The inverse construction exchanges the source and target roles without needing equality of their norm-closed star algebras, so the costs agree, including the case \(+\infty\).
The singular projections of \(U(X-U^*bV^*)V\) are conjugated on the input by \(V^*\) and on the output by \(U\).
The transformation permutes all omitted shifts and preserves common-family orthogonality and each trace.

The quotient defining the canonical slice cost has a represented column norm at the input.
To check its passage to bounded inputs, fix a finite column and apply Kaplansky in a matrix algebra, then compress to the first column and approximate each of its entries in operator norm by polynomials.
Weak compactness in the finite direct sum and the weakly closed graphs of the individual closed slices preserve the same upper bound.
Closability here follows coordinatewise from the adjoint calculation on a dense core.
The common enlarged algebra lies in the graph domain with the sliced derivative given by the bounded approximation above.
Its twisted slice is \(E_0(aV^*)U^*\), preserving the right-column input norm and output Hilbert norm.
For the reverse direction, the marginal projection of the transported derivation at normal \(Y\) has its own actual adjoint vacuum, so the single-generator theorem makes the \(Y\)-marginal diffuse.
All omitted marginals retain their original diffuseness.
The normal-coordinate commutation relation now uniquely determines each starred value of the distinguished derivation, since left and right spectral difference has zero kernel on the coarse tensor product.
Thus inverse transport compares the actual canonical slices on both original cores while assuming an adjoint vacuum only for the one transported coordinate.
Under adjoint orientation the roles of the two twisting factors become \(V^*,U^*\) and the same checks apply.

Finally \(YY^*=U|X|^2U^*\) and \(Y^*Y=V^*|X|^2V\).
Unitary invariance converts their difference in \(L^2\) exactly to the commutator of \(VU\) with \(|X|^2\).
For nonscalar modulus, the fixed Borel rigidity forces exact scalar phase in the normal case and convergence to the trace phase in the approximately normal case, since the unitaries have \(L^2\)-norm one.
Constant modulus is nonzero by diffuse marginal law, and scaling makes \(X\) unitary.
Translation leaves the core and normalized derivation unchanged.
The review does not establish actual vacua for the other target coordinates after general measurable twists, or solve the arbitrary correlated normal-tuple implication.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0226_v1.md#statement) | Borel tests, scalar commutants, fixed trace-window and sequence gaps, distinguished-coordinate transport, and exact and approximate normality. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0226_v1.md#argument) | Trace pairing, marginal approximation, weak-star product limits, spectral cuts, both unitary changes, and measurable graph and norm extensions. |
| [Whole-proof finding](#whole-proof-finding) | [Marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, the marginal divided difference, unique forced starred values, closability and adjoint orientation. |
| [Whole-proof finding](#whole-proof-finding) | [Omitted-coordinate action](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Closed graph killed on the omitted algebra and invariant under both outer omitted actions. |
| [Whole-proof finding](#whole-proof-finding) | [Core adjoint tensors](../../claims/Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Product-rule inclusion of finite core tensors in the actual adjoint domain. |
| [Whole-proof finding](#whole-proof-finding) | [Central-summand transfer](../../claims/Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Existence of a normal optimal bounded witness separately for the source and target, including nonnormal distinguished generator. |
| [Whole-proof finding](#whole-proof-finding) | [Homogeneous Fuglede](../../claims/Yin_C_F0070_v1.md#statement-and-interfaces) | A bounded map from the operator-norm algebra into the Hilbert space commuting with an omitted normal generator also commutes with its adjoint. |
| [Whole-proof finding](#whole-proof-finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong approximation of omitted coefficients, including strong-star approximation by the selfadjoint matrix trick, and finite matrix-column approximation. |
| [Whole-proof finding](#whole-proof-finding) | [Slice closability](../literature/ACSY24/Yin_U001.md#acsy24-u001) | The individual core adjoint identity yields a closable right slice for each transported distinguished derivation. |
| [Whole-proof finding](#whole-proof-finding) | [Singular projections](../../claims/Yin_C_F0211_v1.md#statement) | Singular projection test at omitted shifts, with traces and orthogonality transported by the explicit unitaries. |
| [Whole-proof finding](#whole-proof-finding) | [Task definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | One actual outer derivation on the represented full star core, Hilbert adjoint vacuum and the bounded-vector commutator conventions. |

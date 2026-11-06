---
author: Yin
---

# Coefficient-class propagation after the three-channel determinant theorem

This bounded strategic comparison was developed for Yin on 2026-11-06 by an assigned strategy agent and the responsible research agent.
It is ordinary exploration and source-interface checking, not an independent mathematical review or a new determinant theorem.
The [two-channel theorem](../claims/Yin_C_F0186_v20.md#decision-finite-variance-two-channel-reviewed) and now [adopted three-channel theorem](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed) retain their exact fixed-model scopes.
The latter uses the [adopted middle input](../claims/Yin_C_F0187_v25.md#decision-three-channel-middle-reviewed) and [adopted floor](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed).
Neither completes the original arbitrary-coefficient [F0013 contract](../tasks/Yin_T_F0013_v1.md#contract) or arbitrary-polynomial [F0014 contract](../tasks/Yin_T_F0014_v1.md#contract).

The recommendation is to test a coefficient class for which the combined Gram is automatic, using the existing positive-frame middle theorem.
A secondary lead is a fixed congruence reduction of pencils with one definite original noise coefficient, followed by an auxiliary observation problem.
Neither proposal calls for another fixed four-channel path example.
The earlier [moment, smoothing and coefficient-product comparison](Yin_L_F0063_v1.md) and [cyclic entropy comparison](Yin_L_F0063_v2.md) remain relevant rejection tests.

<a id="special-coefficient-interfaces"></a>
## Which parts of the completed argument depend on its coefficients

For the path pencil, the coefficient \(I\) permits the component residual to be written as
\[
 CV+DVT+VK-\lambda V,
 \qquad T=\operatorname{diag}(0,1,\sqrt2).
\]
It also permits the final [physical rectangle argument](../claims/Yin_C_F0194_v16.md#three-column-graph) to condition on the entire second input and apply the original scalar rectangular theorem in the first input.
This last use of identity noise is separate from the formal coefficient argument.

The two distinct observations of an auxiliary direction \(a\) are \(a\) and \(Ta\).
Separated slopes give a quantitative lower bound for their smaller singular value away from the coordinate axes.
With three channels, the orthogonal complement of their span is one-dimensional on that branch.
The invisible part of a retained-kernel vector is therefore \(b\otimes h\), and the [scalar joint gap](../claims/Yin_C_F0187_v25.md#rank-one-residual) excludes its approximate residual.
For more channels, two observations can leave an invisible auxiliary space of dimension greater than one, so the same scalar argument does not extend merely by changing constants.

The path entries of \(K\) give the endpoint recursions and the central relation \(u_1+u_3=-(C+D)u_2\) in [the coordinate observation argument](../claims/Yin_C_F0187_v25.md#coordinate-observation-graphs).
These relations both control coordinates and keep the imposed boundary conditions within the retained kernel's dimension budget.
A connected arbitrary graph does not supply those exact recursions without further work.
Likewise, the finite and free cubic identities use the displayed constant pivots, not a theorem that every coefficient tuple admits the same scalar reduction.

The [finite-channel noncancellation theorem](../claims/Yin_C_F0187_v16.md#statement), [high-rank tensor theorem](../claims/Yin_C_F0187_v18.md#statement), and [three-channel all-scale raw theorem](../claims/Yin_C_F0187_v23.md#statement) already abstract several algebraic steps from the path.
Their geometric and physical coefficient-transfer hypotheses must still be matched at the new original model.
The completed probability bridge cannot be transferred solely because these raw tensor inputs apply.

<a id="positive-frame-candidate"></a>
## First candidate: finish the positive-frame coefficient class

### Exact starting scope and a whole-space Gram supplied by the original coefficients

Begin with fixed real symmetric matrices \(A_0,A_1,\ldots,A_d\in M_m(\mathbb R)\), original independent real finite-second-moment Wigner inputs \(W_j^{(N)}\), and
\[
 L_N:=A_0\otimes I_N+\sum_{j=1}^d A_j\otimes W_j^{(N)}.
\]
For input \(j\), each strict upper entry is an independent copy of \(\xi_j/\sqrt N\), where \(\xi_j\) is fixed, real, centered and has variance one.
Each input has its own fixed centered real diagonal law with finite second moment and the same normalization.
All upper-triangular coordinates and inputs are independent within each size, while cross-size coupling is arbitrary.
Keep the exact coefficient condition of [C187v3](../claims/Yin_C_F0187_v3.md#statement):
\[
 \chi_A:=\inf_{\substack{u,v\in\mathbb C^m\\\|u\|=\|v\|=1}}
               \sum_{j=1}^d|u^*A_jv|^2>0.
 \tag{Positive-frame-condition}
\]
The infimum is over complex directions, even in this proposed real-input application.
Replacing it by an infimum over real directions is not an invocation of that fixed theorem.
The real symmetric restriction here is needed for the direct signed selfadjoint inverse argument, not for the already proved middle theorem, whose coefficient and entry-law scope is broader.

For a physical minor with \(n\) retained positions, let \(\mathcal H:=\mathbb R^m\otimes\mathbb R^n\) and \(\mathcal E:=\bigoplus_{j=1}^d\mathbb R^n\).
Write a vector \(h\in\mathcal H\) as physical vectors \(h_i\in\mathbb R^m\).
For \(1\le a\le m\), define the actual noise maps by
\[
 (U_a h)_{j,i}:=e_a^T A_jh_i,\qquad
 G(h)_{ab}:=\langle U_ah,U_bh\rangle.
\]
The same formulas can be complexified solely to check the conjugations.
With the usual inner product conjugate-linear in its first argument,
\[
 \begin{aligned}
 z^*G(h)z
 &=\left\|\sum_{a=1}^m z_aU_ah\right\|^2\\
 &=\sum_{j=1}^d\sum_{i=1}^n|z^TA_jh_i|^2\\
 &=\sum_{j=1}^d\sum_{i=1}^n|(\overline z)^*A_jh_i|^2
 \ge\chi_A\|z\|^2\|h\|^2.
 \end{aligned}
 \tag{Whole-space-positive-frame-Gram}
\]
For nonzero \(z\), the last step applies (Positive-frame-condition) with \(u=\overline z/\|z\|\) and \(v=h_i/\|h_i\|\), omitting zero physical components; the zero direction is immediate.
Thus \(G(h)\succeq\chi_A\|h\|^2I_m\) on the entire physical space.
Also
\[
 \sum_{a=1}^m\|U_ah\|^2
 =\sum_{j=1}^d\|(A_j\otimes I_n)h\|^2
 \le\Lambda\|h\|^2,\qquad
 \Lambda:=\sum_{j=1}^d\|A_j\|^2.
 \tag{Whole-space-stack-bound}
\]
This deduction uses the original coefficients and no event, low-energy cutoff, identity noise direction, diagonal slope representation or path coupling.

The actual fresh border agrees with these maps.
For the \(d\) independent real border vectors \(x_j\in\mathbb R^n\), retaining their original \(N^{-1/2}\) normalization, put
\[
 x:=(x_1,\ldots,x_d)\in\mathcal E,\qquad
 R(x)e_a:=\sum_{j=1}^d(A_je_a)\otimes x_j.
\]
Since \(A_j=A_j^T\), one has \(R(x)e_a=U_a^*x\).
For an actual real symmetric inverse \(Z=M^{-1}\), the quadratic Schur block is therefore exactly
\[
 [\,\langle U_a^*x,ZU_b^*x\rangle\,]_{a,b=1}^m
 =R(x)^TZR(x).
 \tag{Original-border-map-match}
\]
No mixed input is conditioned on and none of the \(d\) original rows is replaced by a synthetic independent law.
For nonsymmetric coefficients or complex original rows, this real signed-map identification is not automatically available.

### What already follows, and what is genuinely left

For every fixed auxiliary size \(m\), [C187v3](../claims/Yin_C_F0187_v3.md#statement) already gives the middle profile \(s_{mN-j}(L_N)\ge c j/(mN)\) beyond \(4m\lceil N^{3/4}\rceil\), with summable failure.
It also gives a finite free logarithm and middle negative-logarithmic control.
These inputs retain their full stated complex-law and arbitrary-coefficient scope under \(\chi_A>0\).
For the proposed real symmetric subfamily, any separate polynomial least-value floor in probability would remove the bottom contribution at order \(O(N^{-1/4}\log N)\).
The [accepted finite-variance weak and positive-logarithmic controls](../claims/Yin_C_F0186_v4.md#statement), followed by the clipping and [marginal limsup criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion), would then complete the determinant conclusion for that whole subfamily.
No new middle proof is needed for it.

At \(m=3\), (Whole-space-positive-frame-Gram), (Whole-space-stack-bound), and (Original-border-map-match) satisfy exactly the full-space hypotheses of [C187v23](../claims/Yin_C_F0187_v23.md#statement).
For every selfadjoint \(Z\), its raw degree-six tensor therefore satisfies
\[
 \|\mathscr T_6(Z)\|_F\ge c(\chi_A,\Lambda)q_1q_2q_3,
 \qquad q_1\ge q_2\ge q_3>0,
 \tag{Positive-frame-raw-sixth}
\]
at the source's arithmetic-average symmetric tensor convention.
Here \(q_i\) are the singular values of \(Z\).
This is a direct fixed-source application for arbitrary real symmetric coefficient tuples satisfying \(\chi_A>0\), not a new path example.
Unlike the earlier path application, the full-space Gram is actually valid on the complete inverse support.
The raw substitution \(x_{j,i}=\xi_{j,i}/\sqrt N\) multiplies the degree-six tensor by \(N^{-3}\).
It does not by itself identify the complete degree-six Walsh coefficients after repeated variables have been reduced.

The raw product scale already controls the graph-area scale on a suitable Frobenius event.
For an invertible \(3n\)-by-\(3n\) actual minor with \(n=N-O(1)\), a fixed guard \(\|M\|_F^2\le B N\) gives
\[
 q_3^{-2}=s_{3n-2}(M)^2
 \le\frac{\|M\|_F^2}{3n-2}\le C_B,
 \tag{Third-inverse-value-from-Frobenius}
\]
where singular values of \(M\) are decreasing.
Indeed its first \(3n-2\) values are at least \(s_{3n-2}(M)\).
Such a guard has probability tending to one for the original fixed finite-second-moment inputs, by their squared-entry weak law and the fixed coefficient norm bounds.
A deterministic vanishing parent shift preserves this guard.
Thus \(q_3\ge c_B>0\); no divergence \(q_3\to\infty\) is required for the following comparison.

For any real \(3n\)-by-three boundary matrix \(\mathcal B\) with \(\|\mathcal B\|\le B_0\),
\[
 \sqrt{\det(I_3+\mathcal B^TZ^2\mathcal B)}
 \le\prod_{r=1}^3\sqrt{1+B_0^2q_r^2}
 \le C_{B,B_0}q_1q_2q_3.
 \tag{Positive-frame-raw-area-scale}
\]
The first inequality is the elementary singular-value compression bound.
Consequently raw sixth energy at its natural \(N^{-3}\) normalization is already on a sufficient bounded-boundary graph scale.
The first unresolved implication is from that raw tensor to surviving complete Walsh coefficients with adequate physical-group loads for actual minors.
It is not another raw nonvanishing theorem or another free integrability calculation.

For \(m>3\), the existing arbitrary-channel [comparable-rank theorem](../claims/Yin_C_F0187_v16.md#statement) and [high-rank theorem](../claims/Yin_C_F0187_v18.md#statement) apply at their stated interfaces after the same map identification and, when needed, a fixed change of the domain metric.
A complete all-scale mixed-rank conclusion for arbitrary \(m\) is not supplied by the three-channel C187v23.
That is an additional algebraic extension if the coefficient-class physical test succeeds.
The initial test should use the entire \(m=3,\chi_A>0\) class, not one chosen coefficient tuple.

<a id="positive-frame-physical-boundary"></a>
### The physical transfer must have a branch that permits a free gap

The path proof's vanishing complete-inverse physical diagonal energy cannot be assumed for every positive-frame model.
For a direct discriminating example, choose the real symmetric matrix-unit basis as the noise coefficients and set \(A_0:=M_0I_m\), with \(M_0\) a sufficiently large fixed constant.
This noise family satisfies (Positive-frame-condition).
Indeed, if \(u^*Av=0\) for every real symmetric matrix \(A\), the diagonal units give \(\overline u_iv_i=0\).
Choose \(i\) with \(u_i\ne0\); then \(v_i=0\), and the symmetric off-diagonal units give \(\overline u_iv_j=0\) for every \(j\), contradicting \(v\ne0\).
Compactness gives a positive frame constant.

Take fixed bounded centered variance-one real off-diagonal laws and bounded real diagonals, which are permitted original finite-second-moment laws.
The [bounded-input norm argument](../claims/Yin_C_F0187_v4.md#spectral-residual-spread), applied to the fixed finite number of inputs, bounds all their norms by one fixed constant outside exponentially small probability.
Choose \(M_0\) large enough that, on this event, the noise part \(E\) of every required actual principal minor satisfies \(\|E\|\le M_0/4\).
Then
\[
 Z=(M_0I+E)^{-1}=M_0^{-1}I+F,\qquad
 \|F\|\le(3M_0)^{-1}.
\]
For physical block projections \(P_i\), it follows that
\[
 \mathcal D(Z):=\sum_i\|P_iZP_i\|_F^2
 \ge\frac{4mn}{9M_0^2},\qquad
 \|Z\|_F^2\le\frac{16mn}{9M_0^2},
 \qquad
 \frac{\mathcal D(Z)}{\|Z\|_F^2}\ge\frac14.
 \tag{Positive-frame-gapped-diagonal-obstruction}
\]
This is an actual positive-frame model, so imposing \(\mathcal D(Z)=o(\|Z\|_F^2)\) uniformly on the whole class would exclude valid cases.
In this example the parent itself is safely invertible on the same event, so the conclusion is not a determinant obstruction.
It shows that the physical proof should split off a directly controlled branch or preserve the complete Schur numerator rather than require the path's inverse spread on every minor.

The first discriminating task is therefore to determine a sufficient physical coefficient or complete-numerator alternative for actual minors throughout the \(m=3,\chi_A>0\) class.
On a branch where suitable head/residual physical collision controls hold, one can test the fixed-coefficient extension of [C187v24's collision and load mechanism](../claims/Yin_C_F0187_v24.md#argument).
On the complementary branch, one must justify direct exclusion of the tiny normalized Schur numerator or retain enough lower-degree structure to control it.
The displayed gapped model is a compulsory check on any proposed universal spread premise.
The [arbitrary-minor counterexample](Yin_L_F0059_v1.md#schur-findings) remains a separate warning against discarding the actual pencil relation.
No such branch alternative has been proved in this comparison.

Even a successful raw-to-physical coefficient test would leave the following probability interfaces to establish or check for the new coefficient class:

- A physical small-support delocalization or rectangular lower bound for \(\sum_jA_j\otimes W_j\), with the necessary deterministic offsets and actual conditioning.
  C194v16 conditions on its second input and uses identity noise in scalar channel rectangles; this step is not available merely by replacing two original rows with \(d\) rows.
  The positive frame suggests a block covariance route, but the required uniform physical-support estimate has not been supplied here.
- The fixed-\(d\) original-law copy construction, its full-support row-ball control, and the degree-six matching/load conversion.
  The \(d\) fresh rows are independent under actual-minor conditioning, but C194v16's proved two-law statement is not a theorem for all fixed \(d\).
  Its finite-degree mechanisms are potential inputs to a new explicit extension.
- The three-column graph-distance and many-index averaging argument with those new physical and conditional inputs, including the chosen parent norm guard, averaged bad-minor probabilities, common shift and return to the unshifted matrix.
  The fixed three-column algebra survives, while the new probability hypotheses still require proof.

These distinctions prevent promoting a formal tensor lower bound into an original-model floor.
A valid conclusion would give an entire coefficient class with no identity direction or path structure.
It would be genuine F0013 progress.
Usual scalar polynomial linearizations need not have \(\chi_A>0\), so it would not automatically solve F0014 or the remaining zero-frame part of F0013.
Fixed symmetrizable pencils may be added only after checking the actual constant left multiplier makes all coefficients, including \(A_0\), real symmetric; the normalized finite and free logarithms then change by the same fixed determinant constant.
No arbitrary pencil is claimed to admit such a multiplier.

<a id="definite-direction-candidate"></a>
## Second candidate: congruence normal form and the invisible auxiliary space

A different structural enlargement begins with two original real inputs and real symmetric coefficients \(A_0,A_1,A_2\), where one original noise coefficient is positive definite.
For \(A_1>0\), a fixed congruence and orthogonal diagonalization give a real invertible \(S\) with
\[
 S^TA_1S=I,\qquad
 T:=S^TA_2S\ \text{diagonal},\qquad
 K:=S^TA_0S,
\]
and
\[
 \widetilde L_N:=(S^T\otimes I_N)L_N(S\otimes I_N)
 =I\otimes C_N+T\otimes D_N+K\otimes I_N.
 \tag{Definite-original-direction-normal-form}
\]
The original independent matrices and entry laws have not changed.
The finite normalized logarithm changes by \(2m^{-1}\log|\det S|\), and the bounded free logarithm changes by exactly the same constant under the accepted FK interface.
The [fixed symmetrizer comparison](Yin_L_F0059_v1.md#symmetrizer) is a nearby precedent, but its Gaussian scalar trace shift is unavailable for general atomic laws.
This proposal instead keeps the original rows and seeks a coefficient-class geometric theorem.
A positive combination of several noise coefficients is not substituted for one original positive coefficient without accounting for the resulting dependence between mixed inputs; the [mixed-factor coding example](../drafts/Yin_D_F0010.md#mixed-factor-coding-obstruction) forbids assuming independent residual noise after that mixing.

Common reducing subspaces of the symmetric pair \(T,K\) yield an exact auxiliary block diagonal decomposition and the corresponding finite/free determinant factorization.
Scalar blocks reduce to the accepted scalar affine scope of [C186v11](../claims/Yin_C_F0186_v11.md#statement).
This preprocessing is exact, but irreducibility of a remaining block does not imply a positive coefficient frame or the missing physical estimate.

For a real component matrix \(V\), the original residual is
\[
 CV+DVT+VK-\lambda V.
\]
If a unit auxiliary direction \(a\) is exactly invisible to the two original rows, then \(Va=VTa=0\).
For an exact mode, multiplying the residual by \(a\) gives \(VKa=0\).
More generally, if \(V\) annihilates an auxiliary subspace \(F\), then
\[
 b\in F,\quad Tb\in F\quad\Longrightarrow\quad Kb\in\ker V.
 \tag{Auxiliary-relation-propagation}
\]
Starting with \(F_0:=\operatorname{span}\{a,Ta\}\), this gives the finite-dimensional recurrence
\[
 F_{r+1}:=F_r+K\{b\in F_r:Tb\in F_r\}\subseteq\ker V.
 \tag{Auxiliary-relation-closure}
\]
If this closure reaches the whole auxiliary space, an exact nonzero invisible mode is impossible.
This is an algebraic implication from the original equation, not independent noise associated with products of coefficients.

The closure may stop at a proper subspace without establishing a common reducing subspace of \(T,K\).
No general rank criterion or quantitative lower bound for all directions is asserted here.
In the completed three-channel path model with its distinct slopes, a noncoordinate direction leaves a one-dimensional invisible complement, which the accepted scalar joint gap can control.
For general \(m\), a stopped relation space can leave a multi-dimensional physical component system.
The first new bridge is a quantitative original-law exclusion of those systems, or an explicit coefficient obstruction to it; a scalar joint eigenvector gap alone does not supply that statement.

A discriminating investigation would classify the stopped spaces of (Auxiliary-relation-closure) for an arbitrary fixed symmetric pair, then identify the exact random equations left on each quotient.
It should test whether they reduce to the existing large-block scalar joint gap or require a matrix-valued joint-gap estimate.
Any proposed quantitative result must be tested both on bounded-energy approximate modes and on the actual growing-deletion retained-row kernel.
The [Frobenius-only retained-kernel obstruction](Yin_L_F0066_v8.md#three-channel-middle-frobenius-obstruction) rules out silently replacing the latter by a low spectral subspace.
Repeated slopes and arbitrary \(K\) remain part of this classification; merely appending a path vertex does not test it.

Success would cover arbitrary auxiliary dimensions and a genuine class of definite-direction selfadjoint pencils, rather than a fixed tuple.
It would still not reach general nonselfadjoint coefficients or arbitrary scalar polynomial linearizations.
In particular the universal selfadjoint Hermitization of a general pencil has noise coefficients
\[
 \begin{pmatrix}0&A_j\\A_j^*&0\end{pmatrix}.
\]
Every real linear combination has the same off-diagonal grading, so a nonzero positive definite combination is impossible.
It also has zero coefficient frame, since two vectors supported in the same grading sector annihilate every such bilinear form.
Thus neither of the proposed coefficient-class hypotheses follows from universal Hermitization.

<a id="comparison-and-first-allocation"></a>
## Comparison, source boundary and allocation recommendation

The positive-frame candidate uses information absent from the path coefficients: a whole-space combined Gram that follows directly from the original coefficient frame.
At auxiliary size three, this supplies the auxiliary combined-Gram and mixed-rank raw noncancellation inputs directly, while the existing positive-frame middle theorem removes the new middle proof.
The remaining physical and original-law probability interfaces are explicit above.
This is the more concrete next allocation.

The definite-direction candidate uses an exact class reduction and an auxiliary relation-space test.
Its remaining multi-dimensional invisibility problem is less developed and may contain a substantial part of the original geometric difficulty.
Retain it as a secondary lead until the quotient equations yield a specific new estimate or obstruction.
Neither candidate justifies an unbounded succession of fixed path examples.

The comparison reuses the accepted fixed results and the actual source-inspection boundaries in [L63v1](Yin_L_F0063_v1.md) and [L63v2](Yin_L_F0063_v2.md#source-inspection-boundary).
No new external original was inspected for this record and no new external theorem is adopted.
The prior Gaussian, Kronecker, product-linearization and arithmetic comparisons do not establish theorem absence for these proposed classes.
The source attribution of the accepted tensor and concentration inputs remains at their fixed responsible materials.

The arbitrary-coupling target still needs vanishing lower-deviation probability along a suitable deterministic subsequence, not merely a positive probability of a good determinant.
Products of coefficient matrices still do not create fresh independent noise in the original pencil.
The cyclic full-numerator and entropy failures likewise rule out substituting aggregate energy or a rectangle-dependent net for the missing probability estimate.
These retained tests motivate the proposed physical coefficient/full-numerator distinction; they do not prove it.

This record preserves the conditional deductions, the actual gapped-model obstruction to an overstrong spread premise, and two research candidates.
It makes no new C assessment, R finding, strategy selection or Task-completion decision.

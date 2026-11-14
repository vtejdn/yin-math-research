---
author: Yin
---

# Full dual domains and cutoff divergence on projections of any prescribed trace

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(M\) be a diffuse finite von Neumann algebra with faithful normal probability trace \(\tau\), \(H=L^2(M,\tau)\), and \(\mathcal P_t=\{e=e^*=e^2\in M:\tau(e)=t\}\) with its \(L^2\) metric, \(0<t<1\).
Let \(T:H\supset\operatorname{Dom}T\to H'\) be a closed linear operator into a Hilbert space with \(1\in\operatorname{Dom}T\).
Either \(M\subseteq\operatorname{Dom}T\) and \(T\) is operator-norm-to-Hilbert bounded there, or on **every** \(\mathcal P_t\) its domain is a meagre countable union of closed sets.
In the second case the projections outside the domain form a dense \(G_\delta\) on each \(\mathcal P_t\).
For a countable collection of deficient operators this last assertion holds simultaneously for all of them.

For \(T1=0\), put \(B_t=\sup_{e\in\mathcal P_t}\|Te\|\) and \(B_{\rm all}=\sup_{e=e^*=e^2}\|Te\|\), assigning infinite norm outside the domain.
With \(m=\min(t,1-t)\),
\[
       B_t\le B_{\rm all}\le D_t B_t,\qquad
       D_t=\max\{(1-m)^{-1},(2m)^{-1}\}.                                \tag{1}
\]
The constant \(D_t\) is sharp even for bounded scalar-valued maps on a diffuse abelian algebra.
Finite \(B_t\) gives \(\|T|_M\|_{\infty\to H'}\le4D_tB_t\).

Now let \(X\) be a bounded normal generating tuple with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix its distinguished coordinate \(Z\) with derivation \(\delta\), write \(S_0=(\mathrm{id}\otimes\tau)\delta\) on the original core \(P\), and put \(a=\sup_{p\in P,\ \|p\|\le1}\|S_0p\|_2\).
For **any** prescribed positive sequence \(r_n\to0\), take the canonical regularized slices
\[
   S_n=(\mathrm{id}\otimes\tau)\,I_{\,|z-w|^2/(|z-w|^2+r_n^2)}\,\delta .
\]
Here \(I\) is inner spectral multiplication for \(Z\) on the coarse bimodule.
Each \(S_n\) below denotes its normal bounded extension to \(M\).
For any \(t\in(0,1)\) one has
\[
 a\le4D_t\sup_{e\in\mathcal P_t,\,n}\|S_n e\|_2,\qquad
 \sup_{e\in\mathcal P_t,\,n}\|S_n e\|_2\le3a\quad(a<\infty).             \tag{2}
\]
If \(a=\infty\), there is a dense \(G_\delta\) of \(e\in\mathcal P_t\) satisfying **both**
\[
       e\notin\operatorname{Dom}\overline{S_0},\qquad
                           \limsup_n\|S_ne\|_2=\infty .                  \tag{3}
\]
In particular a nonmeagre subset of even one trace layer on which the individual sequences are pointwise bounded suffices for the entire distinguished forward domain.
Testing the right slices in both orientations gives the complete canonical dual and adjoint domains by the [normal domain comparison](Yin_C_F0075_v1.md#statement).
For a failed actual adjoint domain the same dense category statement for domain omission applies directly to \(T=S_0^*\), whose value at \(1\) is the vacuum.
For \(d\ge3\), an infinite distinguished original column cost gives (3) without enlarging the tuple by [the single-input comparison](Yin_C_F0276_v1.md#statement).
This does not decide the boundedness of the cutoff sequences for all actual tuples.

## Argument

### A bounded patch in a fixed trace layer

Diffuseness permits taking a subprojection of any prescribed trace between zero and the trace of a given projection.
Indeed every nonzero projection has a nonzero subprojection of arbitrarily small trace, by successively splitting and retaining the smaller nonzero piece.
A maximal subprojection of trace at most a prescribed amount exists by taking suprema of chains and normality of the trace.
The preceding small-piece property shows that its trace must be the prescribed amount.
Repeated dyadic splits thus supply, in any nonzero corner with normalized trace, a copy of the Lebesgue probability algebra with its unit.
For \(0\le v\le1\), translate an interval of length \(v\) on its unit circle by the mesh \(j/l,\ 0\le j<l\).
These \(l\) projections all have normalized trace \(v\), and their average is within \(1/l\) of \(v\) times the corner unit in operator norm, by counting mesh points.

The trace layer is a complete metric space.
An \(L^2\)-Cauchy sequence of projections has an \(L^2\) limit in the operator unit ball by weak-star compactness, identified by its pairings with bounded vectors.
The involution and trace pass to the limit, and the squares converge in \(L^2\) by the uniform operator bound, so the limit is in the layer.
The sets \(\{e\in\mathcal P_t:e\in\operatorname{Dom}T,\ \|Te\|\le K\}\) are closed by weak compactness of bounded output balls and weak closedness of the graph.
These assertions also hold for their intersections over a countable family of operators with a shared bound.

Suppose \(\|Te\|\le K\) throughout a nonempty ball of radius \(\epsilon>0\) about \(e_0\in\mathcal P_t\), with inclusion in the domain understood.
Take any two projections \(p,q\) of trace \(s\le s_0=\min(t/2,1-t,\epsilon^2/8)\).
Since \(\tau(p\vee q)\le2s\), there is a projection \(f\le e_0\wedge(1-(p\vee q))\) of trace \(t-2s\).
Indeed \(\tau(e_0\wedge(1-(p\vee q)))\ge t-2s\).
The projection dimension inequality used here follows from polar decomposition of \((1-q)p\), whose initial and final supports are \(p-(p\wedge q)\) and \((p\vee q)-q\), respectively.
Extend \(f\) inside \(1-(p\vee q)\) to \(b\) of trace \(t-s\), possible since \(1-2s\ge t-s\).
Both \(b+p\) and \(b+q\) have trace \(t\) and overlap \(e_0\) on \(f\), giving distance at most \(2\sqrt s<\epsilon\).
Subtracting shows that \(p-q\in\operatorname{Dom}T\) with \(\|T(p-q)\|\le2K\).
Vary \(q\) over the circle intervals in the unit corner of \(M\) and average.
Their averages converge to \(s1\), and bounded outputs have a weak cluster point, so the closed graph gives
\[
                    \|T(p-s1)\|\le2K .
\]
Split any projection into \(l=\lceil1/s_0\rceil\) projections of equal trace to obtain
\(\|T(p-\tau(p)1)\|\le 2lK\) for every projection.
In particular all projections lie in the domain and their images have norm at most \(2lK+\|T1\|\).
A positive contraction is the operator-norm limit of averages of its spectral threshold projections, by a uniform mesh in \([0,1]\).
Using weak graph closure again, then writing a general contraction as the sum of the positive and negative parts of its real and imaginary parts with the appropriate signs, gives \(M\subseteq\operatorname{Dom}T\) and boundedness there.
Every bound is uniform for a family satisfying the same patch bound and bounded values at \(1\).
Conversely, if \(M\subseteq\operatorname{Dom}T\), the closed graph theorem on the Banach space \(M\) gives boundedness there.
If full inclusion fails, all closed sublevels on every trace layer have empty interior, giving the assertions by the Baire category theorem.
Countable intersections of dense \(G_\delta\) subsets remain dense on these complete spaces.

### The sharp comparison between one trace layer and all projections

Assume \(T1=0\) and \(B_t<\infty\), hence \(T|_M\) is bounded by the patch argument.
Complementing projections gives \(B_m=B_t\).
For a projection \(p\) of trace \(s\le m\), average trace-\(m\) projections containing it, by adding circle intervals in its complement of normalized trace \((m-s)/(1-s)\).
The average tends to \(p+(m-s)(1-p)/(1-s)\).
Its image has norm at most \(B_m\), giving \(\|Tp\|\le (1-s)B_m/(1-m)\).
For \(s\ge m\) average subprojections of trace \(m\) in \(p\) to get \(\|Tp\|\le(s/m)B_m\).
For \(m\le s\le1-m\) apply the latter inequality also to \(1-p\), obtaining \(\|Tp\|\le\min(s,1-s)B_m/m\).
The other values follow by the first inequality and complementation.
This proves (1) and the bound for all contractions follows by the spectral approximation already given.

In a Lebesgue probability algebra a functional with density equal to \(1\) on one half and \(-1\) on the other has \(B_{\rm all}=1/2\), \(B_m=m\).
For a set \(A\) of mass \(0<s<m\) take the density \(1_A/s-1\).
Here \(B_{\rm all}=1-s\) and \(B_m=1-m\), by maximizing and minimizing the overlap of a set of mass \(m\) with \(A\).
Let \(s\downarrow0\).
Both families are bounded functionals on the Hilbert space for each fixed choice and both vanish at \(1\).
They give the two lower bounds on the possible constant, including \(m=1/2\).

### Canonical cutoffs on the original algebra

The generated algebra in this application is diffuse.
For \(d=1\) this follows from the [diffuse normal marginal](Yin_C_F0076_v1.md#statement).
For \(d\ge2\) it is a factor by [two-coordinate rigidity](Yin_C_F0202_v1.md#statement) and contains a diffuse marginal, excluding a finite matrix factor.
Equivalently, in any finite algebra containing a diffuse unital abelian subalgebra, a minimal projection would generate a type I finite matrix central summand, on which the restricted normal representation of the diffuse abelian algebra would give a normal character on a nonatomic law.

The [liberation cutoff theorem](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) gives finite column and hence single-input cost for each \(S_n\), and \(S_n p\to S_0p\) in \(H\) for each original polynomial.
Each suppressed derivation is closable and has an actual vacuum by the [soft adjoint theorem](Yin_C_F0081_v1.md#statement), with its parameter \(r_n^2\).
Its sliced core has a dense adjoint domain by [the actual adjoint theorem](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
The normal-summand proof in [C_F0276](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) thus gives a normal extension of the same single-input norm, independently of the value at the distinguished generator.
These maps take \(1\) to zero.
On bounded sets they are \(L^2\)-to-weak continuous, since bounded \(L^2\) convergence implies ultraweak convergence.
Their norm sublevels on \(\mathcal P_t\) are therefore closed.
The averaging and patch bounds above work for this family of normal maps even if no closed Hilbert operator is chosen to represent their extensions: all inputs in the averages stay uniformly bounded and all the limits in the patch argument are operator-norm or bounded \(L^2\) limits.

For \(a<\infty\), the [single-input separated multiplier bound](Yin_C_F0237_v1.md#two-slice-identities-and-the-different-component-terms) gives a bound \(2a\) for the right slice after applying \(I_{v\otimes w}\) to \(\delta\), for spectral unitaries \(v,w\) in the marginal C*-algebra.
Indeed its value at \(p\) is \(S_0(pw)v-pS_0(w)v\), using norm-continuous extensions when \(w\) is a norm limit of core polynomials.
The symbol \(r_n^2/(|z-w|^2+r_n^2)\) is a probability average of these products by the Gaussian Fourier formula in the cutoff theorem.
Subtract this suppression from the original slice to obtain \(\|S_n\|_{M\to H}\le3a\) independently of \(n\).
Conversely if \(B=\sup_{e\in\mathcal P_t,n}\|S_ne\|_2<\infty\), the sharp comparison and spectral approximation give \(\|S_n\|\le4D_t B\), and the core limit gives \(a\le4D_t B\).
This proves (2).
If merely a nonempty patch has a common bound for all \(n\), the uniform patch argument still gives \(\sup_n\|S_n\|<\infty\).
Thus when \(a=\infty\), every closed sublevel of \(e\mapsto\sup_n\|S_n e\|_2\) has empty relative interior, and countably many such sublevels contain every point with finite supremum.
Their complement is a dense \(G_\delta\) where the limsup is infinite since each map is finite.

Finally \(a<\infty\) puts every bounded input in the domain of \(\overline{S_0}\) by bounded strong approximation from the polynomial core and weak graph closure.
Full inclusion implies \(a<\infty\) by the closed graph theorem.
When \(a=\infty\), intersect the dense \(G_\delta\) for this missing domain with the one just obtained for the cutoffs to get (3).
The cited normal domain comparison identifies the existential bare system with the forward canonical domains and the strong system with both bare orientations, including the generator-first sign and both canonical domains.
The adjoint statement uses its own graph directly and makes no assumption that the polynomial core is a core for the adjoint.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:55 |
| status | open |
| reason | Fix the fixed-trace domain dichotomy, sharp layer comparison and generic divergence of the canonical cutoffs on each trace layer for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Projection-domain category, optimal shell constant and simultaneous domain and cutoff failure for the normal converse. |
| argument | [Argument](#argument) | Local trace-preserving changes, convex averages of fixed-trace projections, sharp examples, and normal regularization with core convergence. |
| dependency | [Normal marginal](Yin_C_F0076_v1.md#statement) | Diffuseness and existence of actual starred derivatives in the tuple application. |
| dependency | [Factoriality](Yin_C_F0202_v1.md#statement) | Scalar center when the tuple has two or more coordinates. |
| dependency | [Cutoff and Fourier formulas](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Fixed-radius boundedness, convergence on each core input and probability Fourier representation of the suppressed symbol. |
| dependency | [Suppressed actual vacuum](Yin_C_F0081_v1.md#statement) | Actual adjoint vacuum at every positive cutoff. |
| dependency | [Actual slice adjoint](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Dense adjoint of the original and suppressed right slices and the adjoint value at the vacuum. |
| dependency | [Original single-input reduction](Yin_C_F0276_v1.md#statement) | Normal extension proof for a bounded slice with dense Hilbert adjoint and comparison with original columns in dimension at least three. |
| dependency | [Single-input multiplier estimate](Yin_C_F0237_v1.md#two-slice-identities-and-the-different-component-terms) | Right slice after a separated spectral multiplier, applied before a Fourier probability average. |
| dependency | [Normal domains](Yin_C_F0075_v1.md#statement) | Bare orientations, strong domain comparison and the original canonical operators under the strong condition. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:00 |
| status | proved |
| reason | The independent finding verifies the fixed-trace dichotomy, sharp universal comparison and generic failure of the original domain and cutoff sequences. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Projection-domain category, optimal shell constant and simultaneous domain and cutoff failure for the normal converse. |
| argument | [Argument](#argument) | Local trace-preserving changes, convex averages of fixed-trace projections, sharp examples, and normal regularization with core convergence. |
| dependency | [Normal marginal](Yin_C_F0076_v1.md#statement) | Diffuseness and existence of actual starred derivatives in the tuple application. |
| dependency | [Factoriality](Yin_C_F0202_v1.md#statement) | Scalar center when the tuple has two or more coordinates. |
| dependency | [Cutoff and Fourier formulas](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Fixed-radius boundedness, convergence on each core input and probability Fourier representation of the suppressed symbol. |
| dependency | [Suppressed actual vacuum](Yin_C_F0081_v1.md#statement) | Actual adjoint vacuum at every positive cutoff. |
| dependency | [Actual slice adjoint](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Dense adjoint of the original and suppressed right slices and the adjoint value at the vacuum. |
| dependency | [Original single-input reduction](Yin_C_F0276_v1.md#statement) | Normal extension proof for a bounded slice with dense Hilbert adjoint and comparison with original columns in dimension at least three. |
| dependency | [Single-input multiplier estimate](Yin_C_F0237_v1.md#two-slice-identities-and-the-different-component-terms) | Right slice after a separated spectral multiplier, applied before a Fourier probability average. |
| dependency | [Normal domains](Yin_C_F0075_v1.md#statement) | Bare orientations, strong domain comparison and the original canonical operators under the strong condition. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0291_v1.md#finding) | All eight direct interfaces, diffuse corners, sharp scalar examples, the suppressed adjoint domain and the dense category assertions. |

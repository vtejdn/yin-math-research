---
author: Yin
---
# Independent review of central support and three translates

Review performed at 2026-11-11T19:30 UTC for Yin.
The inspected fixed artifact is [C_A0009_v5](../../claims/Yin_C_A0009_v5.md), including its complete statement, argument, conditional trace inequality, adjoint transfer and remaining-case discussion.
This is distinct independent evidence in the existing R_A0028 topic family.
The preceding physical versions retain their own targets and findings.

## Review arrangement and inputs

The reviewer was outside substantive proof development and received the fixed candidate, its assignment, applicable rules and operational metadata.
No development drafts, mathematical summary, proof-generation dialogue or author explanation was supplied or consulted.
Initial findings were formed from the complete candidate and the necessary fixed mathematical inputs before reading any previous review conclusion.
Only afterward was [R_A0028_v3](Yin_R_A0028_v3.md#whole-artifact-finding) inspected to confirm the accepted scope of C_A0009_v4, which is used only for the final residual-case deduction and the retained universal bound.
That earlier finding is reused at its recorded scope; its finite enumeration and external-source checks were not repeated here.

The new compression, finite root projections, trigonometric signs, synthesis matrix, trace estimates, transfers and middle-case identities were rederived directly.
The accepted analytic foundations are bounded spectral calculus in a finite von Neumann algebra, the normal faithful group trace, polar decomposition with unnormalized matrix traces, and the orthogonal decomposition of the regular representation over subgroup cosets.
Their particular uses were checked below without re-auditing these general foundations.
No numerical experiment, assumed fiber decomposition or formal verification supplies the verdict.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact statement](../../claims/Yin_C_A0009_v5.md#statement) | Both common-power bounds of 1/6, central support and conditional trace scope, and the residual-case deduction under kernel dimension at least 1/4. |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete argument](../../claims/Yin_C_A0009_v5.md#argument) | The whole fixed proof, including actual-group hypotheses, bounded cuts, all root weights and exceptional sets, Gram identity, trace normalization, both transfers, middle-case limitation and generic-rank nonapplication. |
| [Whole-artifact finding](#whole-artifact-finding) | [Cyclic regular spectral law](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | Infinite-order regular shifts, Haar spectral measure, vanishing singleton projections and subgroup-coset applicability; no other rational-closure claim is used. |
| [Whole-artifact finding](#whole-artifact-finding) | [Bounded three-term compression](../../claims/Yin_C_A0009_v2.md#the-exact-compression-imposed-by-a-three-term-kernel) | The norm-square identity for a kernel projection; rederived directly for the candidate without commutation between the projection and a generator. |
| [Whole-artifact finding](#whole-artifact-finding) | [Polar-decomposition dimension interface](../../claims/Yin_C_A0009_v3.md#the-first-translate-configuration-closes-at-two-copies) | Equality between the unnormalized domain trace and closed-range trace for an injective bounded synthesis map; the current three-column argument is checked independently. |
| [Whole-artifact finding](#whole-artifact-finding) | [Accepted finite-cycle statement](../../claims/Yin_C_A0009_v4.md#statement) | Reused strict universal bound 8/29 and necessary configuration at kernel dimension at least 1/4, with exact moments and negative-class restrictions; not an input to the two new 1/6 bounds. |
| [Whole-artifact finding](#whole-artifact-finding) | [Common-power classification](../../claims/Yin_C_A0009_v4.md#all-positive-eight-cycle-classes) | Applicability of the three actual relations, mutual exclusion, no true negative class and moment vector (3,15,87,551) in the stated hypothetical range. |
| [Whole-artifact finding](#whole-artifact-finding) | [Existing whole-artifact review](Yin_R_A0028_v3.md#whole-artifact-finding) | Reused independent evidence for the unchanged C_A0009_v4 statement and classification; read only after initial findings, without claiming a new reproduction of its enumeration or source audits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Generic Laurent-rank hypotheses](../../claims/Yin_C_A0012_v2.md#exact-generic-rank-for-rectangular-laurent-matrices) | Comparison only: the specified finite Laurent expression and actual coefficient-algebra tensor product are required and have not been supplied for this central extension. |
| [Whole-artifact finding](#whole-artifact-finding) | [Original Task contract](../../tasks/Yin_T_A0001_v1.md#contract) | Scope comparison only: these scalar conditional bounds do not settle arbitrary finite complex group-ring matrix integrality. |

## Whole-artifact finding

The complete fixed argument supports the two bounds and the stronger central trace inequality stated in C_A0009_v5.
No unresolved mathematical gap or necessary new source-attribution correction was found in this inspected scope.
The proof places the kernel inside the indicated half-circle and bounds its trace on every central measurable subset; it does not assert that the kernel is nonzero anywhere on that half-circle.
The final exclusion of two common-power alternatives is valid using the unchanged accepted C_A0009_v4 result at its exact scope.
The middle relation, scalar injectivity and the full all-matrix Task remain unresolved.

### Actual group, center and domains

Let \(H:=\langle a,b\rangle\) and \(M:=\mathcal N(H)\).
Left convolution on every right coset \(Ht\) is a copy of the operator on \(\ell^2(H)\), and the trace at the ambient identity is the trace of the \(H\)-kernel projection.
Thus reduction to \(H\) and restoration to any ambient group preserve the stated dimension even when the ambient group is uncountable.

For \(b^2=a^3=z\), the element \(z\) commutes with both generators, hence its bounded Borel functions lie in the center of \(M\) and commute with \(p:=P_{\ker T}\).
Centrality in the ambient group is neither available nor needed.
If \(a=e\), then \(b^2=e\) forces \(b=e\) and \(T=1\).
Otherwise \(a\) and \(z\) have infinite order.
Their regular spectral law supplies the normalized Haar measure of \(z\), so every singleton spectral projection is zero by faithfulness.

From \(bp=(1+a)p\), the norm-square identity gives \(pap+pa^*p=-p\).
Writing \(A:=pap\), compression of \(b^*=z^{-1}b\) gives \(p+A^*=z^{-1}(p+A)\).
The first identity changes the left side to \(-A\), yielding \((1+z)A=-p\) with the stated sign.
On \(f_N\), the inverse of \(1+z\) is bounded and central, so \(Af_N=-(1+z)^{-1}pf_N\) is an ordinary bounded identity.
The \(f_N\) increase to one because the projection at \(z=-1\) vanishes.
The argument never applies this inverse to an arbitrary vector outside its domain.
The affiliated reformulation is dispensable for all subsequent inferences.

### Finite projections and exact signs

For each \(k\), the unitary \(\lambda_k^{-1}a\) has cube one, so its finite average \(E_k\) is a selfadjoint projection.
The three central root ratios are the distinct cube roots of unity, which proves orthogonality, the sum-one identity and \(aE_k=\lambda_kE_k\) directly inside \(M\).
No fiber representation is needed.

The relation \(a^2=za^*\) gives \(pa^2pf_N=z\overline{c(z)}pf_N\).
Compressing the three-term formula for \(E_k\) therefore gives
\[
 pE_kpf_N
 =\frac{1+\lambda_k^{-1}c+\lambda_k\overline c}{3}\,pf_N
 =t_kpf_N.
\]
This verifies the conjugates and the order of every factor without assuming that \(p\) commutes with \(a\) or with \(E_k\).

On \(-\pi<\theta<\pi\),
\[
 c(e^{i\theta})=-\frac{e^{-i\theta/2}}{2\cos(\theta/2)},
\]
which gives the angle \(5\theta/6+2\pi k/3\) and the minus sign in formula (8).
Applying the cosine-difference identity yields exactly the three sine products in (9).
For \(0<\theta<\pi\), both sine factors of \(t_0\) and \(t_1\) are positive.
The second sine factor of \(t_2\) is positive, and its first factor has the sign of \(\pi/2-\theta\).
Reflection preserves \(t_0\) and exchanges \(t_1,t_2\), proving the stated negative-angle conclusions.

At zero the weights are \((0,1/2,1/2)\), while at the two half-circle endpoints the indicated other weight is zero.
Together with the branch endpoint, these are all exceptional spectral sets used by the proof, and each has zero projection.
On a cut where \(t_k\le-\varepsilon\), positivity of \(pE_kp\) and the central identity force \(pf_N\) to vanish.
A countable union over positive rational \(\varepsilon\) and integer \(N\) eliminates every negative-weight region.
Thus \(p=e_Ip\) for \(I:=(-\pi/2,\pi/2)\), with \(\tau(e_I)=1/2\).
On this support the rational coefficient is bounded because \(|1+z|\ge\sqrt2\).

### Gram matrix and all central trace cuts

The row \(F\) in (12) is bounded and its Gram matrix has entries \(pa^{j-i}p\), with row index \(i\) and column index \(j\).
For the stated \(V\), the finite-root sums make \(V\) unitary.
The \((i,j)\) entry of the right side of (13) is
\[
 \sum_{k=0}^2\lambda_k^{j-i}t_kp=pa^{j-i}p,
\]
including the negative powers by adjoints.
This checks all entries and the factor three.

On \(pg_N\ell^2(H)\) in each of the three columns, the Gram operator is bounded below by \(3/N\) times the domain projection.
The restricted row is therefore injective, with initial support \(\operatorname{diag}(pg_N,pg_N,pg_N)\) and final support at most \(g_N\).
Polar decomposition equates the unnormalized matrix trace of the initial support with the trace of the final support.
This gives \(3\tau(pg_N)\le\tau(g_N)\), with no missing normalization factor.

The \(g_N\) increase to \(e_I\) after the already vanishing singleton projections are removed.
Normality of the trace gives \(3\tau(p)\le1/2\).
Intersecting every \(g_N\) with an arbitrary \(e_E\) gives, by the same reasoning,
\[
 3\tau(pe_E)\le\tau(e_{E\cap I})=\frac{|E\cap I|}{2\pi}.
\]
Neither passage requires a positive uniform lower bound for the weights on all of \(I\), or a measurable family of factor representations.

### Adjoint transfer and the remaining relation

For \((ba^2)^2=a^3\), putting \(w:=ba^2\) preserves the actual generated subgroup and gives \(w^2=a^3=z\).
The earlier argument applies directly to \(Q:=1+a-w\) in that group.
The equality
\[
 Ta^2=a^2+a^3-w=zQ^*
\]
uses \(za^*=a^2\) and \(zw^*=w\), so every term and adjoint is correct.
The kernel projection of \(Ta^2\) is \(a^{-2}p_Ta^2\); its trace agrees with that of \(p_T\) on every central cut.
Left multiplication by the unitary \(z\) changes no kernel, and polar decomposition in each finite central corner equates the kernel traces of \(Q\) and \(Q^*\).
This proves (18).
Trace faithfulness then transfers the support statement as well as the numerical and measure inequalities.

For the middle relation, \(w:=ba\) gives \(S:=Ta=a+a^2-w\) and \(S^*=z^{-1}S\).
Centrality of \(z\) makes \(S\) a bounded normal operator, and the chosen central square root makes \(\zeta^{-1}S\) selfadjoint.
If \(r:=P_{\ker S}\) and \(C:=rar\), the norm square of \(wr=(a+a^2)r\) gives \(C+C^*=-r\), while \(a^2=za^*\) gives \(rwr=C+zC^*\).
Taking the adjoint produces \(C^*+z^{-1}C=z^{-1}C+C^*\), a tautology.
Thus this calculation does not pin \(C\), and it establishes no counterpart of the half-circle support bound.

The comparison with C_A0012_v2 is accurate: its rank theorem concerns a specified finite bounded-coefficient Laurent expression in an actual von Neumann tensor product.
Centrality of a group element alone supplies neither that representation nor the theorem's evaluation interface.
The candidate makes no generic-rank inference for the unsupplied representation.

### Dependency use, source scope and original objective

The cyclic spectral input is used only for actual infinite-order regular group elements.
The compression and polar-decomposition interfaces match their fixed predecessors and were rechecked directly at the points needed here.
The new bounds use no finite-cycle classification, ordered quotient or inheritance theorem.

C_A0009_v4 is an accepted input for the final residual-case deduction, with its fixed independent coverage in R_A0028_v3.
Its hypothesis \(\delta\ge1/4\) gives exactly one of the three common-power relations, no true negative class and moments \((3,15,87,551)\).
Since \(1/6<1/4\), the two newly proved bounds exclude precisely \(j=0,2\) from that range.
The remaining \(j=1\) alternative retains those exact restrictions and is only a necessary hypothetical configuration.
The earlier universal strict bound remains \(\delta<8/29\).

No new external theorem or historical priority claim is introduced in the new proof.
The existing finite-cycle result retains its earlier recorded source-verification boundary, including its established Lin92 input; this review does not claim another inspection of that primary theorem.
No additional necessary source correction was identified for the elementary identities and accepted analytic foundations used here.
This is an independent review of the new whole argument with explicitly reused accepted dependency evidence, not a literature-wide novelty search or a new audit of every predecessor proof.
The unchanged Task still asks for integer kernel dimensions for all finite complex group-ring matrices, and the inspected scalar conditional bounds do not meet that completion criterion.

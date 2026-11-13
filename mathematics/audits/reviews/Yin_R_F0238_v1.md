---
author: Yin
---
# Independent review of the unconditioned singular law under omitted shifts

## Whole-proof finding

At 2026-11-13T16:43 UTC a separately assigned agent completed independent review of the [statement](../../claims/Yin_C_F0229_v1.md#statement) and [argument](../../claims/Yin_C_F0229_v1.md#argument) of the [16:42 candidate](../../claims/Yin_C_F0229_v1.md#decision-candidate).
The reviewer had investigated other normal-tuple questions, including inverse bounds for the conditional variance of a shifted coordinate, and knew that the unconditional distribution was of interest.
The reviewer did not participate in this resolvent and polar-phase proof, receive its development discussion or mathematical summary, or consult development drafts, author explanations or previous conclusions on this candidate before reaching the mathematical finding.
The reviewer checked all three directly declared inputs at their used scopes.
During review the author corrected internal equation references to the differentiated identity (3) and its real scalar inequality (4).
The corrected references were read back, and the mathematical displays and their uses agree.
The proof establishes the full fixed statement, uniformly over bounded \(b\) in the omitted algebra.

### Closed graph, the real estimate, and absence of a kernel

The actual closed derivation kills \(b,b^*\) by the omitted-coordinate graph theorem.
The surviving starred value of \(T=X_i-b\) is the marginal phase of \(X_i\), which is unitary for the marginal product law, regardless of the normality of \(b\).
Bounded strong-star approximation of \(b\) is available by Kaplansky, also by applying its selfadjoint version to the matrix with entries \(b,b^*\) off the diagonal.
Polynomial approximation of the bounded omitted coefficients therefore gives graph convergence for every fixed word in \(T,T^*\).
For \(s>0\) the resolvent Neumann series for \(R=(T^*T+s)^{-1}\) has derivative terms bounded by a fixed multiple of \(nq^{n-1}\), \(q<1\).
Both differentiated factors in \(W=TR\) thus belong to the graph with the required Leibniz evaluation.
In outer notation its derivative is
\[
  (1-TRT^*)(\bar\delta T)R -TR(\bar\delta T^*)TR .
\]
Here \(1-TRT^*=s(TT^*+s)^{-1}\); the second term has \(W\) on both sides of \(\bar\delta T^*\), giving exactly the multiplier and sign in (3).
Pairing this graph value with the actual adjoint vacuum is legitimate.
The distribution of the modulus of \(W\) is obtained by \(v\mapsto v/(v^2+s)\) from the modulus of \(T\), also before injectivity since this function vanishes at zero.
The two moduli of \(T\) have identical tracial laws by polar equivalence of their supports, with equal deficits at zero.
The trace norm of \(W\otimes W^{\rm op}\) is the square of \(\tau(|W|)\), since the opposite leg has the other modulus with the same trace.
Using the unitary phase and bounding only the trace of this product gives (4), preserving the sign of the vacuum pairing.
After multiplication by \(s\), the first scalar integral squared tends to the squared kernel mass, \(s|\langle\xi,W\rangle|\le\|\xi\|_2\sqrt s/2\), and the other term tends to zero by bounded convergence for \(\sqrt s\,v/(v^2+s)\).
Faithfulness therefore gives zero kernel for both \(T\) and \(T^*\), so the polar operator \(U\) is unitary.

### Arctangent primitive, constants and fractional inverse moments

Writing \(t=\sqrt s\), expansion of (4) at each \(t\) gives the signed kernel \((t^2-vw)/((t^2+v^2)(t^2+w^2))\).
Direct differentiation of \(\arctan(v/t)\) gives \(-v/(t^2+v^2)\), hence the signed kernel is minus the derivative of the displayed arctangent divided difference, including the continuous diagonal primitive \(t/(t^2+v^2)\).
Integration in \(dt\) on a finite interval away from zero is valid termwise by uniform boundedness there.
The integrated \(W\) term is \(U\) times a positive spectral multiplier bounded by \(\pi/2\) before normalization, using the scalar integral of \(v/(v^2+t^2)\).
This controls the signed vacuum integral uniformly in both endpoints, without integrating its pointwise absolute value.
At the upper endpoint the divided difference is at most \(1/R\).
At lower endpoint \(r\) and \(v,w\in[0,r]\) it is at least \(1/(2r)\), since this is the minimum derivative of \(\arctan(v/r)\) on the interval.
The two normalization factors thus give exactly \(\mu([0,r])^2\le\pi r\|\xi\|_2\).
Writing \(C=\pi\|\xi\|_2>0\), the tail integration against \(\min(1,\sqrt{Cr})\) on the two sides of \(r=C^{-1}\) gives \(a C^a/(1/2-a)+C^a=C^a/(1-2a)\).
Neither the cutoff \(\|T\|\) used in the individual graph construction nor \(\|b\|\) appears in this final bound.

### Exact integrated phase defect and endpoints

Let \(g=g_t(P)\), and use the product trace on \(M\bar\otimes M^{\rm op}\).
Since \(W=Ug\), the factorization in this algebra is
\[
    W\otimes W^{\rm op}
      =(U\otimes1)(g\otimes g^{\rm op})(1\otimes U^{\rm op}).
\]
Moving \(U\otimes1\) around the trace puts the other factors in the declared order \((1\otimes U^{\rm op})k(U\otimes1)\).
Conditional expectation against the two spectral legs of \(P\) gives the stated measurable \(m\) on \(\mu^2\).
That product of unitaries has operator norm one, hence \(|m|\le1\).
The real trace identity has a signed scalar part and the additional nonnegative integrand \(g_t(v)g_t(w)(1-\mathrm{Re}\,m(v,w))\).
The scalar part integrates to \(J(\lambda)-J(R)\).
For \(v,w>0\), partial fractions give the normalized integral of \(g_t(v)g_t(w)\) over \(t>0\) as \(1/(v+w)\); at \(v=w\) the answer is \(1/(2v)\).
The kernel-free conclusion makes these formulas sufficient on the whole product measure.
First let \(R\uparrow\infty\) at fixed \(\lambda>0\), using \(J(R)\le 2/(\pi R)\).
The nonnegative integral then increases as \(\lambda\downarrow0\) and stays bounded by \(\|\xi\|_2\), since \(J(\lambda)\ge0\) and the normalized integrated vector has Hilbert norm at most one.
That vector tends in \(L^2\) to \(U\) by spectral bounded convergence.
The exact equality thus gives a finite limit of \(J(\lambda)\) and the asserted polar identity, without assuming monotonicity of \(J\) or an inverse moment at the endpoint \(a=1/2\).
The mass bound does not decide the stronger summed column obstruction or the general normal-tuple implication.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0229_v1.md#statement) | All bounded omitted shifts, both null kernels and equal singular laws, uniform mass and fractional moment bounds, exact integrated phase defect. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0229_v1.md#argument) | Graph resolvent identity, signed and positive terms, finite-interval arctangent integration, endpoint limits, constants and opposite-algebra factors. |
| [Whole-proof finding](#whole-proof-finding) | [Normal marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Item 1, closability and unitary starred-coordinate value in the abelian marginal tensor algebra. |
| [Whole-proof finding](#whole-proof-finding) | [Omitted-coordinate graph action](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Closed graph contains all elements and adjoints of the omitted von Neumann algebra with zero derivative. |
| [Whole-proof finding](#whole-proof-finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strong-star approximation by omitted star polynomials, using the selfadjoint matrix version and norm density. |
| [Whole-proof finding](#whole-proof-finding) | [Task conventions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual represented Hilbert adjoint at the vacuum, outer multiplication and coordinate normalization. |
| [Whole-proof finding](#whole-proof-finding) | [Singular projection comparison](../../claims/Yin_C_F0211_v1.md#statement) | The summed cubed-mass bound with squared radii used only to delimit the consequence of the new one-shift estimate. |

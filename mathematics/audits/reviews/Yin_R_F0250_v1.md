---
author: Yin
---
# Gaussian column bounds and the two-segment Schur obstruction

On 2026-11-14T10:25 UTC an agent for Yin independently inspected the whole [C_F0241 v1 candidate](../../claims/Yin_C_F0241_v1.md#decision-candidate).
The reviewer took no part in proof development and received the fixed proof and its direct inputs without substantive development discussion, exploration notes, separate author explanations or previous review findings.

## Finding

The argument establishes all three items for the intrinsic row-bounded Gaussian model.
In particular, the corner example has finite column bounds in both orientations even though the inverse divided difference has unbounded Schur norm on opposite half-intervals.

**Enlargement and column bounds.**
The enlarged matrix has positive part \(G\oplus I_2\), so the inverse-square trace increases by two and the two identity blocks cancel from the covariance difference.
The Gaussian criterion therefore supplies a closed canonical slice containing every bounded input in the enlarged intrinsic algebra, even when \(A\) is rectangular.
Its restriction from that algebra with the operator norm to \(L^2\) has closed graph because operator-norm convergence implies \(L^2\) convergence.
The forced marginal phase and the normalized unstarred generator values restrict to the original ones under the coarse-space embedding, so Leibniz gives agreement on every old starred word.
Left multiplication by either added field commutes with the slice on the enlarged core and carries each graph approximant to another graph approximant.
The semicircular distribution function is continuous and carries semicircular law to uniform law on \([0,1]\).
Operator-norm approximation of its circle-valued exponential therefore gives the same commutation for the resulting Haar unitaries and their conjugate words on bounded inputs.
The free-column estimate applies within the generated free product and gives \(\|\sum u_jb_j\|\le 2\|\sum b_j^*b_j\|^{1/2}\).
The conditional expectation of \(u_j^*u_k\) onto the old algebra is \(\delta_{jk}1\), so bounded approximation of each \(E_i b_j\) gives the claimed sum of squared slice norms.
For the adjoint tuple the flip-adjoint derivation has the normalized values on \(X_j^*\) and has actual vacuum \(\xi_i^*\).
The new marginal is \(\bar z\), whose law is still diffuse, and conjugating the base parameters preserves the Gaussian row-bound hypothesis.
This allows the same enlargement and column estimate in that orientation.

**Relabelling and the corner vacuum.**
The Borel inverse on conull sets identifies \(L^\infty\) of the two spectral laws and their one-edge \(L^2\) spaces by composition, first on separated functions and then by density.
This preserves each field, full row rank and the inverse trace integral.
Product-measure substitution changes only the endpoint distance in the second integral and preserves the order \(P^{-1}Q-PQ^{-1}\), including conjugation of \(G(w,v)\).
The new law is bounded and diffuse, so its diagonal is null and the matrix criterion applies with its actual scalar vacuum hypothesis.
The two Lipschitz bounds give exactly the reciprocal-square comparison factors.
For \(h(s)=s+ia|s|\) and \(0<s<1\), the Cauchy integral splits into the difference of the two truncated logarithms divided by \(2(1+ia)\) and an opposite-half term bounded by \(\tfrac12\log((1+s)/s)\).
The logarithms at \(s=0,1\) have integrable squares, and reflection gives the controls on the negative half.
Dominated convergence gives an \(L^2\) limit \(C\).
The divided difference of any starred polynomial is bounded on the two segments, so symmetric truncation gives its vacuum pairing \(2\int f(h(s))C(s)\,d\mu(s)\).
With the inner product linear in the second variable this is the actual adjoint vector \(2\overline C\).
Here \(1/2\le b\le 3/2\) and \(|Q-P|=|s-v|/4\), giving an integrable covariance quotient since \(|h(s)-h(v)|\ge |s-v|\).
The one-edge formula gives \(\mathbb E_N T_b^2(s)=(1+s/4)^2+1/48\), using \(\int t^2\,d\mu(t)=1/3\).
Freeness would give the constant \(\tau(T_b^2)1\), so the example is correlated.

**Schur norm.**
At the geometric sample points, division by the larger magnitude shows that the two triangular constants differ by \(2ia/(1+a^2)\), with entrywise errors bounded by \(C_a4^{-|i-j|}\) off the diagonal.
The Fourier coefficients of \(i(\pi-\theta)\) give \(1/m\) for \(m\ne0\) and zero for \(m=0\), proving the uniform input bound \(\|D\|\le\pi\).
The constant unit vector detects the triangular difference times \(H_{n-1}-(n-1)/n\), with error bounded independently of \(n\) by \(2C_a\sum_{d\ge1}4^{-d}/d\).
At each fixed \(n\), compression to normalized indicators of disjoint intervals gives rectangle averages of \(k\) times \(D_{ij}\), with input norm exactly \(\|D\|\).
Continuity at the sampled opposite-sign pairs lets these compressions approach the tested matrix in operator norm.
Hence the logarithmic divergence holds for the measurable multiplier and excludes a projectively summable expansion, which would bound the multiplier by the sum of the products of the two supremum norms.
Kwapień and Pełczyński state the logarithmic operator-norm growth of the main triangle projection and its Hilbert matrix test in the introduction on printed p. 43, using an antidiagonal convention equivalent by reversal of columns.
The candidate derives the needed lower bound directly. [Original article, p. 43](https://matwbn.icm.edu.pl/ksiazki/sm/sm34/sm3414.pdf#page=1)

The review checked the four fixed mathematical inputs at their invoked statements and interfaces, without recursively reviewing their full proofs.
The Gaussian hypothesis is essential to the enlargement used here, and the finding does not decide the unrestricted normal-tuple question.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0241_v1.md#statement) | All three items, both orientations and the intrinsic rectangular-noise case. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0241_v1.md#argument) | Whole Gaussian enlargement, measure substitution, scalar vacuum, correlation and discrete-to-diffuse Schur test. |
| [Finding](#finding) | [ACSY and strong-domain definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred algebra, actual vacuum adjoint, and domains on bounded vectors. |
| [Finding](#finding) | [Gaussian matrix theorem](../../claims/Yin_C_F0209_v1.md#statement) | Equivalence with the covariance integrals and actual canonical full domains in the enlarged and relabelled intrinsic systems. |
| [Finding](#finding) | [Forced phase and companion](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 for restriction on the old core and the normalized adjoint orientation. |
| [Finding](#finding) | [Haar column estimate](../../claims/Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Free-product operator norm and Hilbert orthogonality on finite columns. |
| [Finding](#finding) | [One-edge Gaussian action](../../claims/Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Coordinate identification by the vacuum vector and the conditional second moment. |

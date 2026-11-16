---
author: Yin
---

# Review of the operator-norm neighborhood of a free semicircular pair

## Finding

At 2026-11-16T17:19 UTC a separately assigned agent for Yin independently reviewed the whole C_F0317 v1 candidate fixed at 17:17 UTC.
The reviewer did not develop the argument and received the fixed mathematical inputs without development dialogue, author explanations, exploration notes or prior findings on this candidate.
Conditional on failure of the universal normal implication, the proof gives both infinite slice costs, the simultaneous approximation (1), the marginal tail constraint and the exact coupling (2).

The real two-interval noise has bounded maximal linear density and zero curvature, hence an actual scalar vacuum.
For \(\lambda<1/2\) one continuous sign function works on the spectra of both \(v\) and \(v+\lambda J\).
Uniform polynomial approximation and the uniform norm bound give convergence of the signs in operator norm.
Simultaneous negation implies \(\mathbb E_Bs=bJ\), and freeness gives \(\tau(Js_0)=0\).
Equality in \(\tau(s_0Y)\le\tau(|Y|)\) would force \(1-\operatorname{Re}(s_0s)=0\) by faithfulness and invertibility of \(|Y|\).
A unitary with real part one is the identity, so this would imply \(s=s_0\) and \([s_0,J]=0\).
Freeness gives \(\|[s_0,J]\|_2^2=2\).
The resulting strict inequality and \(\tau(sv)\le\tau(|v|)\) imply \(b>0\), while norm convergence of the signs gives \(b\to0\).
The two reduced-word projection estimates used in the conditional compression theorem require freeness alone of the noise factor.
Applied to \(s-bJ\), whose norm is at most two, they give the stated \(4\sqrt{\tau(e)}/b\) operator norm error.

The noncrossing pairing recursion for a standard semicircular identifies its conjugate variable with itself, also on adjoining a free centered symmetry with derivative zero.
The actual vacuum in diagonal block \(n\) has entry \(t_n\zeta_n/\alpha_n\).
The other blocks therefore have combined squared norm \(\sum_{n\ge1}4^{-n}/L^2\), while replacing \((1-t)A\) by \(A\) in the main block costs at most \(t\) in the common Hilbert norm.
Since \(\|W_n\|<3\) when \(d<1\), the contribution from \(W\) on the tail is at most \(3\sqrt t\).
The gaps to the main interval and from disk \(n\) to any disk \(k>n\) are bounded below by an absolute multiple of \(d2^{-n}\).
Summing the ordered coarse-block masses against the inverse squared gaps gives the bound by \(C'd^{-2}\sum_n4^n t_n\).
Thus the inner correction costs at most \(2\|K\|_2\) in vacuum norm and has the same bound on the tensor \(D_0J\).
The base-tensor insertion at the free noise cancels the derivative of \(Y\) with added vacuum norm at most \(\lambda\|g_v\|_2\|D_0J\|_2\).
Norm approximation on the spectral gap puts the killed sign in the graph.
Restriction and orthogonal projection give (4) since \(W\) belongs to the generated algebra.

Each individual disk can be isolated by a smooth cut in the real spectral variable, including when the disks accumulate at the main endpoint.
The norm and graph approximants, after the two inner cuts, give the original distinguished derivative scaled by \(\alpha_n\) on \(Z_n\) and zero on the new coefficient \(b^{-1}e_nse_n\).
The latter differs from \(J_n\) by less than the predetermined tolerance.
The old trace agrees with the normalized ambient corner trace, so each test has norm at most two and the stated lower bound on the normalized slice.
The inequality for a finite global cost \(a\) then yields \(4a\ge 2^{n-1}/L\) at every \(n\).
The sign involution and the even-algebra result produce vacua \(\xi,s\xi s\) and infinite equal costs for the pair in its own generated algebra.
The bare-dual implication applies to this fully actual normal pair.

On the main block the quantile parameter has the uniform law on \([0,1-t]\), while on every tail block its law is uniform on \([1-t,1]\).
The mixture with weights \(1-t,t\) gives the uniform probability and hence an exactly standard semicircular \(T_0\).
The quantile is uniformly continuous even at the endpoints.
On each tail block \(\|W_n-2\|\le d\) and \(\|T_0-2\|\le2-Q(1-t)\), so taking the supremum over all blocks gives (5) in operator norm.
Alternating centered words for \(T_0\) and \(s_0T_0s_0\) reduce to centered free words for \(R\) and \(W^*(s_0)\), proving freeness in the same extension.
The conjugation error for the second operator is bounded by \(2\|T_0\|\|s-s_0\|=4\|s-s_0\|\) in addition to (5).
The common \(L^2\) vacuum comparison follows from (4), since \(\|\xi_j-W_j\|_2=\|\xi-W\|_2\) for both \(j\).

For the coupling, \(a=s-bJ\) satisfies \(\mathbb E_Ra=0\) and \(\mathbb E_Ra^2=(1-b^2)1\).
For \(f\in W^*(W)\), sign symmetry gives \(\mathbb E_B(f-\tau(f))=0\).
Between two reduced words containing noise, the \(R\)-coefficient formed from \(f-\tau(f)\) and the adjacent \(B\)-letters still has zero expectation onto \(B\).
Its vanishing scalar trace keeps the neighboring centered noise letters separated.
Separate normality in each word therefore gives \(\mathbb E_R(a(f-\tau(f))a)=0\).
The remaining terms give exactly the mixture (2), where the second probability is represented jointly by the commuting left and right spectral actions on the trace vector.
The parameters can be chosen in the prescribed order because every constraint on \(t_n>0\), after fixing \(\lambda,d,L\) and the witnesses, is an upper bound.
Reducing a summable majorant for \(4^nt_n\) makes both Hilbert and operator errors in (1) simultaneously small and achieves \(t<\varepsilon\).
The review checked the twelve direct dependency interfaces below.
The existence of a counterexample to the universal normal implication remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0317_v1.md#decision-candidate) | Whole fixed 17:17 UTC decision concerning the conditional construction and its quantitative restrictions. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0317_v1.md#statement) | Conditional actual exchange pair, deficient domains, common operator-norm coupling, Hilbert vacuum error, endpoint tail and independent component of the spectral coupling. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0317_v1.md#argument) | Entire proof including strict sign regression, graph and vacuum estimates, parameter order, exact reference law and rectangular spectral law. |
| [Finding](#finding) | [Scalar vacuum criterion](../../claims/Yin_C_F0255_v1.md#statement) | Finite density and zero curvature for the gapped scalar noise. |
| [Finding](#finding) | [Conditional compression](../../claims/Yin_C_F0313_v1.md#compression-of-a-free-perturbation) | The reduced-word proof for a free noise algebra and the norm bound on the centered perturbation in a small block. |
| [Finding](#finding) | [Sign and exchange models](../../claims/Yin_C_F0311_v1.md#statement) | Finite witnesses, even-algebra vacuum, equivariance and failure of both cost bounds in the resulting pair. |
| [Finding](#finding) | [Semicircular moments](../literature/NS06/Yin_U004.md#ns06-u004) | The noncrossing pairing formula identifying the standard semicircular vacuum. |
| [Finding](#finding) | [Free vacuum extension](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Preservation of the semicircular vacuum when the free symmetry is killed. |
| [Finding](#finding) | [Finite witnesses](../../claims/Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Norm stability of each fixed witness and its normalized differentiated expression for close coefficients. |
| [Finding](#finding) | [Direct-sum derivation](../../claims/Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Weighted vacua and the off-diagonal inner derivation on separately generated spectral blocks. |
| [Finding](#finding) | [Free extension of the base](../../claims/Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) | Extension of the base derivation across the free selfadjoint noise while preserving its vacuum. |
| [Finding](#finding) | [Base tensor insertion](../../claims/Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Scaled norm of the actual vacuum for the insertion of \(-\lambda D_0J\) at \(v\). |
| [Finding](#finding) | [Graph restriction](../../claims/Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) | Spectral gap functional calculus, intrinsic derivative on the generated core and orthogonal projection of the vacuum. |
| [Finding](#finding) | [Intrinsic comparison](../../claims/Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) | Separated spectral cuts and the normalized corner slice estimate under a hypothetical finite global cost. |
| [Finding](#finding) | [Bare dual obstruction](../../claims/Yin_C_F0070_v1.md#statement) | Boundedness of the original core right slice if the normal pair admits a bare full-domain dual system. |

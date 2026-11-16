---
author: Yin
---

# Review of negative liberation forms on restricted circular curvature kernels

An independent reviewer checked the complete argument of the [fixed candidate](../../claims/Yin_C_F0302_v1.md#decision-candidate) at 2026-11-16T16:00 UTC.
The reviewer had no role in developing it and received its fixed text and dependency locators without development dialogue, exploration notes, author explanations or earlier findings on this candidate.

## Finding

The proof establishes the stated lower bound for a single correlated pair and for both sequences of test unitaries, with a positive constant independent of \(n\).
The upper bound \(2J\) for the unnormalized negative form holds for all positive powers and all the stated subkernels.

The circle law has normalizing constant \(c_0=1/6\), bounded maximal linear density by the chord-length estimate for arcs, and squared curvature one off the null diagonals.
Here \(1/2\le\rho\le1\), and \(\rho=1\) occurs only at the null point \(1\).
The cancellation \(d\mu/(1-\rho^2)=32c_0\,dm/(1+\rho)\) gives finite \(I\), and Lipschitz continuity in chordal distance gives \(J\le\operatorname{Lip}(h)^2 I^2\).
These are the hypotheses of the scalar and coupling criteria.
The coupling generates the free product, has nonconstant conditional mean, and supplies the actual conjugate variables, the strong duals and the exact squared norm difference \(2J\) at \(Z\).
This difference is the inverse-gap energy by the [normal recovery identity](../../claims/Yin_C_F0238_v1.md#statement), also used in the coupling theorem.
Actuality also supplies the descended partial liberation and its vacuum, as required for the graph argument.

At a radial parameter below one, every term containing the free Haar unitary in a product of positive coupling expansions has positive rotation degree.
The \(N\)-valued expectation therefore retains exactly the product of base coefficients and conditional means, including with intervening base letters.
Strong-star convergence with common unitary bounds passes every fixed word to the endpoint in \(L^2\).
At a cut \(p=l v_0 b\), tracing its two inner insertions pairs the conditional suffix factors with \(1-\overline{v_0(z)}v_0(v)\).
For \(W^m\) the additional suffix phase is \(z\bar v\), which gives \(-d(z,v)t^j\) for \(1\le j\le m\).
For \(W^{-m}\) the suffix phase is one, which gives \(d(z,v)t^j\) for \(0\le j<m\).
These computations give both geometric sums and their signs.
The inequalities \(2td\le|h(z)-h(v)|^2\), \((1-t)^2-(1-\rho(z)^2)(1-\rho(v)^2)=(\rho(z)-\rho(v))^2\), and \(|z-v|^2\le4\) give the pointwise majorant by twice the coupling integrand for the positive powers.

The extreme angular gap of a restricted triple lies in \([2\delta,2.2\delta]\), hence its chord diameter lies in the stated shell for all large \(n\).
Each arc has positive marginal mass, so the integral of the endpoint kernel is \(2\mu(E_n)\mu(F_n)\mu(H_n)>0\).
For all large \(n\), each endpoint satisfies \(1/(64n)\le1-\rho\le1/(16n)\), by \(|1-e^{ix}|/|x|\to1\).
Consequently \(1/(64n)\le1-t\le1/(8n)\) and \(7/8\le t^n\le e^{-1/64}\) uniformly.
Since \(d(z,v)\) is comparable to \(\delta^2\), the first geometric sum has negative magnitude at least a fixed multiple of \(\sqrt n\).

For the analytic test, re-expansion at the two first-order positive modes gives differences of squared coefficients \(\varepsilon^3/2\) and \(-\varepsilon^3/4\) to cubic order.
Parseval bounds the combined energy of all remaining nonzero modes by \(O(\varepsilon^4)\), uniformly under weights between zero and one.
The cubic expression therefore has weighted leading term \(\varepsilon^3(1-s)^2/4\).
With \(s=t^n\le e^{-1/64}\), first choosing \(\varepsilon>0\) small fixes a strictly positive lower bound and ensures \(2\varepsilon<1\).
Then the subtracted term is at most \(1-t\) by unimodularity and tends uniformly to zero.
The Fourier sums converge in the actual liberation graph uniformly in phase for each fixed \(n\), since the derivative bounds grow at most linearly in the Fourier index.
The strict contraction also gives graph convergence of the binomial series at the same vector, and closability identifies the derivatives.
Averaging in phase eliminates all unequal Fourier indices, without requiring orthogonality of powers of \(W\).
Some phase therefore attains at least the claimed integrated negative magnitude.
Taking the smaller of the two positive constants covers both test classes.

The fixed dependency theorems were used at their stated scopes.
The result concerns the ratio to the mass on these cuts and leaves the general normal-tuple implication open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0302_v1.md#decision-candidate) | The selected construction and its three declared mathematical inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0302_v1.md#statement) | Both test classes, one actual correlated pair, positive localized kernel mass and the \(2J\) bound on powers. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0302_v1.md#argument) | Complete proof from coupling and suffix signs through the fixed shell, graph calculus and phase average. |
| [Finding](#finding) | [Coupling](../../claims/Yin_C_F0290_v1.md#statement) | Defect integrability, exact vacuum norm, generation, actuality and strong duals. |
| [Finding](#finding) | [Endpoint construction](../../claims/Yin_C_F0290_v1.md#unitarity-generation-and-conditional-law-at-the-endpoint) | Rotations, norm expansion below the endpoint and bounded strong-star convergence at the endpoint. |
| [Finding](#finding) | [Scalar criterion](../../claims/Yin_C_F0255_v1.md#statement) | Finite marginal density and curvature energies, and actual liberation from the joint condition. |
| [Finding](#finding) | [Liberation graph](../../claims/Yin_C_F0077_v1.md#statement) | Graph closability for the actual real partial liberation, applied to the two unitary approximations. |
| [Finding](#finding) | [Normal recovery](../../claims/Yin_C_F0238_v1.md#statement) | Identification of the joint-minus-marginal squared vacuum norm with the inverse-gap energy. |

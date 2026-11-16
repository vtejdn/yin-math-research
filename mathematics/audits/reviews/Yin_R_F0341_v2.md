---
author: Yin
---

# The dihedral rotation law and the original relative derivation

## Finding

Review time (UTC) 2026-11-16T19:10.
I reviewed the complete C_F0334 v2 candidate dated 2026-11-16T19:08, both directions of its new criterion, its seven declared dependency interfaces and its use of the separately retained v1.
I was outside development of both versions of C_F0334 and received no development dialogue, author explanation or previous finding on v2.
I previously developed the separate C_F0320 result used for the scalar angular identity and checked that interface again here.
The v1 assessment already refers to the earlier R_F0341 v1 finding; the new necessity and sufficiency below were checked from v2 and its fixed mathematical inputs.
The three conditions are necessary and sufficient, including at Haar law and when the sign function has infinite secant energy.

In the sign algebra \(a v a=v^{-1}\), so every reduced word is \(v^k\) or \(v^k a\).
A word of the latter kind is conjugate to \(a\) or \(s\), hence has zero trace.
It follows that the two Laurent spans, with and without the terminal reflection, are orthogonal.
Negating both signs fixes the trace on all words and extends in the faithful trace representation to an involution.
It fixes the Laurent subspace pointwise and changes sign on the other subspace.
For an existing relative derivation, v1 locates the liberation vacuum in \(L^2(N)\), and the restriction to the sign core has the same vacuum.
Equivariance then puts that vector in \(L^2(W^*(v))\).
Conjugating by \(a\) makes the rotation law invariant under inversion.
If \(p\) is an eigenprojection of \(v\) at \(\lambda_0\), the kernel identity for the restricted closable derivation gives \(p\cdot\gamma v\cdot p=0\).
The trace product of its \(a\otimes s\) term is zero by the reflection orthogonality, and its \(-1\otimes v\) term gives \(-\lambda_0\tau(p)^2\).
This excludes every atom, including either real endpoint.

For positive powers the rotation cuts give the negative of \(\sum_{k=0}^{n-1}m_km_{n-k}\), and for \(v^{-n}\) they give the sum of \(m_{-(k+1)}m_{-(n-k-1)}\) over the same indices.
Both are the negatives of the double traces of the scalar derivation with \(\mathcal L v=1\otimes v\).
Subtraction of \(f(z)/z\) from \(d_f(z,w)\) gives exactly \(w d_{f/v}(z,w)\), so the representing vector of the scalar divided difference is \((1-\eta)v\) in the inner product linear in the second argument.
The actual scalar circle identity now gives the \(L^3(m)\) density and \(\|\eta\|_2^2=(\int\rho^3\,dm-1)/3\).
By strict convexity the zero-gradient case is exactly Haar.
For a nonzero gradient, the v1 off-sign spectral measure and finite inverse-gap energy force \(J<\infty\).

Starting with the scalar conditions, \(G=P_-\rho-P_+\rho\) lies in \(L^2(\rho\,dm)\) by the \(L^3(m)\) circle projection estimate and Hölder.
For \(n>0\), the negative-mode term in \(\int v^n G\rho\,dm\) sums \(m_jm_{n-j}\) for \(j\ge1\), and the positive-mode term cancels precisely the \(j>n\) tail.
The products are summable for each fixed \(n\) by the square summability of the density's Fourier coefficients.
Since \(G\) is purely imaginary, complex conjugation gives the opposite sign at negative powers, and the two terms also cancel at zero.
Thus \(H=G^*\) has the actual angular vacuum pairing, and the same \(f/v\) calculation gives \(\xi_v=(1+H)v\).
Diffuse \(\lambda\) ensures that the two orthogonal normal-form summands contain no nonzero null Laurent polynomial.
The formal sign derivation respects the two involution relations, so this proves that it is represented on \(N_0\).
Its vacuum is \(-H\) on the rotation words by the cuts and on the reflection words by parity.
Consequently the complementary derivation \(\operatorname{ad}-\Gamma_N\) kills \(B\) and has vacuum \(H\).

For the extension by zero on \(A\), the prescriptions agree on their common base, and \(B\)-centering leaves \(N_0\) invariant.
A reduced word with a centered \(A\)-letter is orthogonal to \(N\).
For each nonzero cut of such a word, the part ending or beginning next to the cut in a centered \(A\)-letter has zero \(N\)-expectation.
The two tensor legs from differentiating the cut lie in \(N_0\), so at least one scalar trace vanishes.
Also \(\mathbb E_B H=0\) by centering and reflection orthogonality.
These facts verify the pairing on mixed words, pure \(A\)-words and the amalgamating algebra, while the sign-core pairing supplies the remaining words.
On a formal null relation \(x\), the pairing at \(p^*xq^*\) tests the derivative of \(x\) against the tensor of the represented \(p,q\), since the terms containing \(x\) as an undifferentiated factor vanish.
Density of these tensors proves descent.
Subtracting from \(\operatorname{ad}\) therefore constructs the original partial liberation with vacuum \(-H\), before constructing the normalized derivative.

The compressed sign-core pairing forces \(e_\pm H e_\pm=0\), and the two cross blocks have equal squared norms by skew-adjointness.
Amalgamated freeness now gives the opposite-sign spectral density \(2\|H\|_2^2\) relative to \(\mu^2\) on each of the two cross rectangles.
Since the squared sign difference there is four, the inverse-gap integral is \(\|H\|_2^2 J/2\) at non-Haar law.
At Haar law the integral of the zero spectral measure is zero irrespective of \(J\).
The diffuse coarse spectral gap is injective, and the represented liberation identifies the normalized derivative on core words.
In the reconstruction its soft inverse-gap term converges in norm off the diagonal and the scalar adjoint correction tends weakly to \(\xi_\mu\) on the diagonal.
This gives the actual vacuum on all represented words and its squared norm, with cubic coefficient \(1/6\).
The v1 estimates and the two original domains therefore apply on exactly the class characterized in v2, including free conjugation by an arbitrary unitary free from \(A\) under the stated conditions.
The estimate for nonzero gradient retains the \(1+\|\eta\|_2\) factor in front of \(\sqrt J\); the criterion alone supplies no absolute normalized bound as nonzero \(\eta\) tends to zero.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0334_v2.md#decision-candidate) | Complete 2026-11-16T19:08 v2 candidate and all seven declared direct interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0334_v2.md#statement) | Three-way scalar condition, actual skew liberation and divided-difference vacua, cubic coefficient, Haar boundary and inherited domain bounds. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0334_v2.md#argument) | Both directions, rotation and reflection words, atom exclusion, moment identities, amalgamated extension, represented descent and orthogonal reconstruction. |
| [Finding](#finding) | [Retained v1 decision](../../claims/Yin_C_F0334_v1.md#decision-reviewed) | Earlier domain theorem under assumed actuality and its existing evidence remain attached to v1. |
| [Finding](#finding) | [Two-point restriction](../../claims/Yin_C_F0334_v1.md#locating-the-liberation-vector-in-the-two-symmetry-algebra) | Sign-core restriction, vanishing same-sign compressions and calculation of the two cross spectral measures. |
| [Finding](#finding) | [Original domain theorem](../../claims/Yin_C_F0334_v1.md#statement) | Both orientations under actuality, the Haar exception to finite \(J\), and relative domain and commutator consequences. |
| [Finding](#finding) | [Free conjugation instance](../../claims/Yin_C_F0334_v1.md#the-opposite-sign-term-and-the-zero-vacuum-boundary) | Amalgamation over \(W^*(a)\) for the indicated free-unitary realization and the free zero-gradient estimate. |
| [Finding](#finding) | [Kernel projection identity](../../claims/Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the derivative of a normal rotation minus a scalar to the putative eigenprojection on both legs. |
| [Finding](#finding) | [Circle angular identity](../../claims/Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) | Actual scalar circle law, signed Fourier functional, \(L^3\) bounds and normalized cubic angular energy. |
| [Finding](#finding) | [Divided-difference descent](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Faithful descent from the actual liberation by the diffuse inner gap. |
| [Finding](#finding) | [Actual adjoint reconstruction](../../claims/Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Weak marginal correction, norm-convergent off-diagonal term and orthogonal squared norm on the original core. |
| [Finding](#finding) | [Relative sign interface](../../claims/Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Normalized distinguished derivative with a killed selfadjoint sign, allowing its atomic law. |

---
author: Yin
---
# Whole-proof self-review of radial univalent dual costs

## Whole-proof finding

At 2026-11-13T16:08 UTC the check_defect agent for Yin reviewed all four assertions of the [fixed candidate](../../claims/Yin_C_F0224_v1.md#statement) dated 2026-11-13T16:04, its complete [argument](../../claims/Yin_C_F0224_v1.md#argument), and the eight declared direct inputs.
All four assertions hold at their stated scopes.
The receiving agent had developed the preliminary Koebe coefficient factorization and its norm, and had seen development of the radial endpoint and power lower bound before receiving the fixed claim.
The review used the fixed claim and necessary mathematical sources, without consulting development notes or prior findings about this candidate during the check.
The relationship for the complete finding is therefore self-review.
The following checks concern the project proof and actual applicability of its inputs.
The underlying classical Grunsky, growth, Runge, strong Haagerup and shifted-circular theorems were used at statement level.

### Coefficient matrix and radial endpoint

For \(F(\zeta)=1/f(1/\zeta)\), the exterior difference ratio at \((1/z,1/w)\) is \(d(z)d(w)/g(z,w)\), where \(d=z/f\) with removable value \(1\) at zero.
The classical exterior logarithm has negative Grunsky coefficients, so solving for \(g\) gives the positive exponential in C_F0224.
The contraction bound on \((\sqrt{mn}\,b_{mn})\) holds for exterior univalence alone. [Krushkal, §1.3, (6)–(8) and the matrix statement following (10)](https://www.intechopen.com/chapters/72257)
The exponential vectors over \(v(z)\) have exactly the Hardy Gram kernel, making their map from the span of the coefficient vectors well defined, isometric and extendible by density.
Their vacuum components account for index zero.
The second-quantized contraction preserves each symmetric tensor power and its norm is at most one on their Hilbert sum.
With the scalar product linear in the second variable, testing at \(e(\bar z),e(w)\) reads off the bilinear Taylor coefficients.
Multiplication by \(d(z)d(w)\) therefore uses a transpose on the right, with the same norm as the multiplier even for complex coefficients.
The lower growth theorem gives \(|d|\le4\), including the removable value, and hence the two multiplier norms give \(16\). [Belyaev, Theorem 3.2.11, pp. 42–43, course-copy PDF](https://www.math.stonybrook.edu/~bishop/classes/math627.S25/Beliaev_notes.pdf)
For Koebe the limiting operator equals \(QQ^*\) with \(Q=(I-S)^2\).
The alternating unit vectors approximate the eigenvalue \(-1\) of \(S\), giving \(\|Q\|=4\) and equality \(16\).

For each fixed \(t<1\), the inverse of \(f_t\) is holomorphic on the image of a disk strictly larger than the closed disk used for approximation.
The compact image of that closed disk has connected complement, so C_F0218 applies through the precise Runge interface.
Both norm approximations give \(C^*(1,Z_t)=C^*(1,c)\), and the derivative normalization at zero makes its attained vacuum \(c\).
Because the indices of \(J_-\) are vectors \((c^*)^n\Omega\), its analysis coefficients on \(a\in M\) are \(\tau(c^n a)\).
The radial coefficient matrix \(W_tA_fW_t\) converges strongly on all of \(\ell^2\) since \(A_f\) is bounded and \(W_t\) are contractions converging strongly to the identity.

Conjugation by the gauge unitaries introduces the phase \(e^{in\theta}\) in \(\tau(c^n\alpha_{-\theta}(a))\) and \(e^{im\theta}\) in the output.
The factor \(e^{i\theta}\) in the definition of \(D_\theta\) cancels the \(e^{-i\theta}\) from the distinguished left generator.
Each integrand on a fixed input is Hilbert-norm continuous, so its Poisson average gives the required bounded map with coefficient weight \(t^{m+n}\).
The input coefficient list for a core word is finite by gauge degree.
At a strict radius the analytic power series converge with geometric coefficient decay even after the polynomial growth of \(\|c^k\|\) and the number of cuts of a power.
Thus the divided-difference product gives exactly \(P_\Omega\) on \(B\).
The central-summand transfer produces the required \(M\to H\) witness and permits an unrestricted value at the unit.
Applying the same argument at \(s/t\) proves monotonicity.
In the other direction product weak compactness on the separate Hilbert balls for \(a\in B\) gives a single linear endpoint map if the norms stay bounded.
Strong convergence of the kernels tests its commutator pointwise.
The infinite-cost case follows from the same implication, and these steps give equality of the two costs without ever evaluating \(f(c)\).

### The Koebe Hilbert cost

The two circular intertwinings are \(L_cJ_+=J_+S\) and \(J_-^*L_c=S^*J_-^*\), giving exactly the shifts shown on either side of \(D_t\) in \(M_{k,t}\).
At \(t=1\) each summand has the common approximate eigenvalue \((-1)^{k-1}\) on the alternating vectors, giving the claimed \(16k\) after the two outer factors.
For \(N=2k\), moving both shifts to the test vectors leaves at least \(N-\max(j,k-1-j)\) common coordinates and every diagonal entry there is at least \(t^{2(N-1)}\).
Each shift from either quadratic factor changes the sign of a surviving scalar product and the sign of that term's coefficient simultaneously.
Dropping all the extra terms gives the stated lower bound \((k/2)t^{4k}\).
The strong Haagerup bound applies to one homogeneous power of a unit-variance circular and gives \(\|c^k\|_\infty\le C_{\rm circ}\sqrt k\).
For \(k=\lfloor1/(-\log t)\rfloor\) near one, \(t^{4k}\ge e^{-4}\) and \(k\asymp(1-t)^{-1}\).
Using Hilbert commutators at this step proves the lower rate for \(\beta_H\).

For the upper rate \(Q_n\) has initial words ending in \(uv^n\), so the initial projections are pairwise orthogonal while its image consists of all words ending in \(u^n\).
Testing the sum of its weighted range projections on \(u^N\) gives \(\|T_t\|^2=(1-t^4)^{-1}\).
The boundary commutators of the two different circular letters vanish, leaving only \([r_u^*,\ell(u)]=P_\Omega\).
This gives \([T_t,L_c]=J_+D_tJ_-^*\), and multiplying by \((I-tL_c)^2\) on each side gives respectively \(P_t\) and \(P_t^*\) in coefficient coordinates.
The strict-radius series calculation yields the correct operator-first dual on all \(H\), proving the matching upper rate.

### Analytic commutators with bounded inputs

For real \(\lambda>1\), the shifted circular calculation uses the positive variable \(X=(\lambda-c)(\lambda-c)^*\) and Cauchy transform \(G(-s)=-h(s)\).
Its rational inverse is \([1+(\lambda^2-1)w]/[w(1-w)^2]\).
Substituting \(w=-h\) gives the polynomial equation in the claim with a minus on the \((\lambda^2-1)h\) term.
It extends down the positive \(s\)-axis by real analyticity of the resolvent trace. [Haagerup, Kemp and Speicher, arXiv version 1, Theorem 2.2 and (2.11)](https://arxiv.org/pdf/0811.3125v1)
Positivity then gives \(h(s)^3\le1/s\), while the elementary positive resolvent bound gives \(h(s)\le1/s\).
Integrating \(s^{-1/2}h(s)\) gives the constants \(6\) and \(2\) below and above \(s=1\).
Circular rotation, the trace norm and the small-\(|w|\) power series prove the stated uniform \(16/\pi\) bound on the analytic moment function of bounded \(a\).

The recurrence for \(M_{k,1}\) follows by multiplying on the left by \(S+S^*\) and canceling \(S^*S\).
It includes the boundary term for \(j=0\) and yields \(\sin(k\theta)/\sin\theta\) under the sine transform.
For complex coefficients the sine transform of a Taylor vector uses the difference of the two boundary evaluations at opposite angles, with no conjugation of the coefficients.
The distinct spaces \(u^j V_-\) are orthogonal, and the two approximate eigenvectors of \(S^*\) give the required two sums of squared tail values at \(1,-1\).
Expansion of \(\sin(k\theta)/\sin\theta\) selects \(k\ge |l|+1\) with \(k-|l|-1\) even at Fourier index \(l\).
This gives precisely the average of \(h_{|l|+1}(1),h_{|l|+1}(-1)\), including index zero.
Each positive tail index is used at most twice in Parseval, giving \(\|d_p\|_{L^2(d\theta/2\pi)}\le\sqrt2\|p(c)\|\).
The sine-transform normalization on \((0,\pi)\) then yields the factor \(2\) for \(M_{p,1}:H^\infty\to H^2\).
On the basis vector \(e_n\), the surviving term \(S^jV_\theta(S^*)^{k-1-j}\) contributes \(e^{i(n-k+1+j)\theta}\).
Splitting the rotations as in the claim gives that identical phase, including the scalar absorbed into \(p_\theta\).
Poisson averaging therefore preserves the polynomial estimate at every radius.
Finally \(S^*:H^\infty\to H^\infty\) has norm at most \(2\) by the disk maximum principle, and the two outside factors have respective bounds \(4,9\) in their stated spaces.
This establishes a common constant for the analytic commutator estimate on bounded inputs.
The lower growth of the whole-Hilbert-space dual cost does not decide whether the bounded-input dual costs for Koebe stay bounded, as recorded in the statement.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0224_v1.md#statement) | All four assertions, optimal kernel constant, precise normed domains, radial endpoint and remaining Koebe bounded-input question. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0224_v1.md#argument) | Grunsky exponential compression, Poisson averaging and bidual limit, matching Koebe Hilbert bounds, shifted circular resolvent and all analytic polynomial commutators. |
| [Whole-proof finding](#whole-proof-finding) | [Univalent circular changes](../../claims/Yin_C_F0218_v1.md#statement) | Radial hypotheses, norm approximation and generation, fixed-law Hilbert dual, normalized minimizing vacuum and forced kernel on bounded inputs. |
| [Whole-proof finding](#whole-proof-finding) | [Analytic commutator series](../../claims/Yin_C_F0218_v1.md#convergent-power-series-and-simultaneous-commutators) | Circular Fock pairings and power growth, and norm convergence of the divided-difference product at each strict radius. |
| [Whole-proof finding](#whole-proof-finding) | [Central-summand transfer](../../claims/Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Transfer from the represented unital norm algebra to the von Neumann algebra preserving the norm bound and generator identity. |
| [Whole-proof finding](#whole-proof-finding) | [Polynomial Runge theorem](../literature/GW25/Yin_U001.md#gw25-u001) | Connected complement and holomorphy of the inverse near the image of the smaller closed disk. |
| [Whole-proof finding](#whole-proof-finding) | [Strong Haagerup inequality](../literature/KS07/Yin_U001.md#ks07-u001) | Distribution-dependent factor times the square root of the degree for the norm-one-in-\(L^2\) circular powers. |
| [Whole-proof finding](#whole-proof-finding) | [Exterior Grunsky input](../../claims/Yin_C_F0224_v1.md#exterior-grunsky-input) | Exterior normalization, logarithm sign, unweighted finite input sequences and contractivity of the square-root-weighted matrix. |
| [Whole-proof finding](#whole-proof-finding) | [Disk growth input](../../claims/Yin_C_F0224_v1.md#disk-growth-input) | Normalized univalent growth lower bound and \(H^\infty\) norm of \(z/f(z)\). |
| [Whole-proof finding](#whole-proof-finding) | [Shifted circular input](../../claims/Yin_C_F0224_v1.md#shifted-circular-input) | Unit circular variance, real shift above the spectral radius, orientation of the square and the local inverse of the scalar Cauchy transform. |

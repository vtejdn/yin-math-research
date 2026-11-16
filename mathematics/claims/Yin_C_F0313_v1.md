---
author: Yin
---

# A single exchange-symmetric normal pair from unbounded projection tests

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

The [universal normal implication](../tasks/Yin_T_F0011_v1.md#contract) fails if and only if there is one pair of bounded normal generators \(Z_0,Z_1\) with full actual starred conjugate variables, exchanged by a trace-preserving involutive automorphism of their generated algebra, for which both original right slices have infinite cost on the operator-norm unit ball of the represented starred polynomial core.
Such a pair has no bare full-domain dual system.
Equivalently, the universal implication holds if every single [sign-symmetric projection model](Yin_C_F0311_v1.md#statement) has finite distinguished slice cost, with an arbitrary model-dependent bound.
If it fails, one such projection model has infinite cost.
All these assertions are existential equivalences.
The finiteness of the universal constant remains open.

The construction also gives an operator-norm estimate for the effect of replacing a symmetry by the sign of its free semicircular perturbation on small corners.
Let \(J=J^*=J^{-1}\) be centered in a finite tracial algebra \(R\) with faithful probability trace, let \(S\) be a standard semicircular free from \(R\), and set \(B=W^*(J)\).
If \(e\in R\) is a projection with \(\mathbb E_B e=t1\), then every \(d\in W^*(J,S)\) satisfies
\[
    \|e(d-\mathbb E_Bd)e\|\le 2\sqrt t\,\|d-\mathbb E_Bd\| .                  \tag{1}
\]
For one fixed sufficiently small \(\epsilon>0\), \(J'=\operatorname{sgn}(J+\epsilon S)\) satisfies \(\mathbb E_B J'=bJ\) with a real \(b>1/2\) independent of \(R\).
Consequently \(b^{-1}eJ'e\) approximates \(eJe\) to within \(8\sqrt t\) in operator norm.
This correction of the conditional mean allows one fixed noise level for countably many prescribed mixed tests.

## Argument

### Compression of a free perturbation

Use the [free-product Hilbert decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) for \(R*W^*(S)\).
The space is the orthogonal sum of \(L^2(R)\) and \(L^2(R)\otimes K\), where \(K\) is the sum of all reduced tensor spaces beginning with a centered noise letter.
The first factor in the latter summand is the optional \(R\)-letter preceding that noise.
Left multiplication by \(R\) acts by its usual representation on the first factor.
Let \(Q\) project onto \(L^2(B)\otimes K\).
The hypothesis on \(e\) gives \(QeQ=tQ\), by pairing \(eb_1\) against \(b_2\) for \(b_1,b_2\in B\).
In particular \(\|eQ\|\le\sqrt t\).

Write \(d_0=d-\mathbb E_Bd\).
Then \((1-Q)d_0(1-Q)=0\).
To see this, first take a reduced word in \(B,W^*(S)\) containing a centered noise letter.
On \(L^2(R)\) its output starts with an optional \(B\)-letter followed by a noise letter, including when a scalar is removed from the rightmost \(R\)-product.
On \((L^2(R)\ominus L^2(B))\otimes K\) its last optional \(B\)-factor multiplies the initial \(R\)-factor of the input to an element orthogonal to \(B\).
This factor is centered, so no cancellation of the adjacent noise letters can occur.
Both outputs belong to \(QH\), where \(H=L^2(R*W^*(S))\).
The argument first applies to bounded reduced tensors and extends by density.
Centered reduced words span a weakly dense subspace of the kernel of \(\mathbb E_B\) in \(W^*(J,S)\), by the free-product decomposition and normality of the expectation.
The compressed identity passes to this closure.
In \(ed_0e=eQd_0e+e(1-Q)d_0Qe\) each term now has norm at most \(\sqrt t\,\|d_0\|\), proving (1).

The tracial law of \(J,S\) depends only on the centered symmetry and standard semicircular laws.
It is invariant under simultaneous negation, so \(\mathbb E_BJ'\) is a real multiple of \(J\).
For sufficiently small fixed positive \(\epsilon\), \(J+\epsilon S\) has a spectral gap about zero and \(\|J'-J\|<1/2\).
Indeed the spectra remain in two disjoint neighborhoods of \(-1,1\), and one fixed continuous function equal to the sign on these neighborhoods is norm continuous in the selfadjoint input by uniform polynomial approximation.
The estimate is uniform over the realizations by their common faithful law, or by the same polynomial approximation with \(\|S\|=2\).
Thus \(b>1/2\), \(\|J'-bJ\|\le2\), and (1) proves the asserted bound.
The proof of (1) uses the full operator norm, which will allow arbitrary fixed word lengths below.

### Choosing the corners before introducing the common noise

Assume the universal implication fails.
The [finite sign-symmetric transfer](Yin_C_F0311_v1.md#statement) gives, for each \(n\ge1\), a sign-symmetric relative model \(R_n=W^*(Z_n,J_n)\), where \(J_n=2P_n-1\) is a centered symmetry.
Taking a positive rescaling of the distinguished generator makes \(\|Z_n\|\le1\) and preserves the slice-to-vacuum ratios.
Write \(D_n\) and \(\zeta_n\) for the normalized derivation and its actual vacuum.
Fix a starred polynomial contraction \(p_n(Z_n,J_n)\) with right slice norm \(b_n>4^n\|\zeta_n\|_2\).
The vacuum norm is positive by testing at \(Z_n\).
There is a tolerance \(h_n>0\) such that replacing \(J_n\) in this fixed expression by a selfadjoint element within \(h_n\) in a larger tracial algebra gives polynomial norm at most two and formal right slice norm at least \(b_n/2\).
In the formal derivative only the distinguished letters are marked, with the same unit tensor and the original marginal phase as their values.
This continuity follows by telescoping the finitely many words, in operator norm for the polynomial and coarse norm for each derivative with its bounded outer factors. [Finite witness comparison](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses)

Choose \(t_n>0\) so small that \(8\sqrt{t_n}\le h_n\), \(t_n\le2^{-4n-4}\), and \(\alpha_n=2^nt_n^{3/2}\|\zeta_n\|_2\le 2^{-n-4}\).
In the direct product \(R\) with trace weights \(t_n\) place \(Z=2^{-n}+\alpha_n Z_n\) on the \(n\)-th summand and take \(J=(J_n)\).
Use the remaining mass for one copy of the first input model with \(Z=2+Z_1/8\) and its centered symmetry.
All summands admit involutions fixing their distinguished generator and negating their symmetry.
Their product defines the same involution on \(R\).
The spectral projections \(e_n\) of the separated disks are precisely the summand units, so \(W^*(Z,J)=R\).
Since each \(J_n\) is centered, \(\mathbb E_B e_n=t_n1\) for \(B=W^*(J)\).

Apply the [direct-sum derivation](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) to \(Z,J\).
On a diagonal block it is \(D_n/\alpha_n\), and on distinct coarse blocks it is inner with kernel \(1/(z-v)\).
The sum of the squared diagonal vacuum norms off the auxiliary block is \(\sum_n t_n^3\|\zeta_n\|_2^2/\alpha_n^2=\sum_n4^{-n}\).
The gap and mass estimates make the inner kernel square integrable.
In the auxiliary block the fixed scaled distinguished vacuum is finite and the derivative kills its coefficient as well.
This gives a global actual vacuum, the unit value at \(Z\), its marginal phase at \(Z^*\), and a finite coarse tensor \(D_0J\) from the distinct-block correction.

Adjoin \(S\) freely, extend \(D_0\) by zero there, and insert the fixed base tensor \(-D_0J/\epsilon\) in the free difference quotient at \(S\).
The [free-noise vacuum calculation](Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) gives an actual vacuum for the resulting derivation, whose squared norm is at most the former squared vacuum norm plus \(\|D_0J\|_2^2/\epsilon^2\).
The derivation kills \(Y=J+\epsilon S\) and preserves its old values at \(Z,Z^*\).
The sign \(J'\) is a norm limit of polynomials in \(Y\) with zero derivatives because of the spectral gap.
The actual vacuum gives graph closability; norm convergence and bounded multiplication on coarse tensors allow adjoining \(J'\) on every needed word. [Spectral cut and restriction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator)
On the represented starred polynomials in \(M=W^*(Z,J')\), the generator values are intrinsic and projection of the ambient vacuum gives the actual vacuum there.
The simultaneous negation of \(J,S\) fixes \(Z\), extends to the tracial free product, and sends \(J'\) to \(-J'\).
Thus \(M\) is a single sign-symmetric projection model with coefficient \((1+J')/2\).

### Detecting the bad polynomials after taking the sign

The spectral projections \(e_n\) are limits in norm and derivation graph of starred polynomials in \(Z\).
For each fixed \(n\) choose a smooth function of the real part of \(Z\) constant at the correct values on neighborhoods of the separated real spectral intervals.
Approximation in \(C^1\) gives the cut and its divided difference \((e_n(z)-e_n(v))/(z-v)\) on the marginal.
Insert \(e_n\) on both inner tensor legs of the distinguished derivative, writing \(\theta_n=I_{e_n\otimes e_n}\delta\).
The [corner calculation](Yin_C_F0308_v1.md#direct-comparison-of-the-original-and-compressed-slices) applies to this graph extension.
In particular \(\theta_n e_n=\theta_n J'=0\).
In the normalized corner, \(\alpha_n\theta_n\) sends \((e_nZ-2^{-n}e_n)/\alpha_n=Z_n\) to the unit tensor and sends its adjoint to the old phase.

The actual target coefficient \(H_n=b^{-1}e_nJ'e_n\) therefore has derivative zero for \(\theta_n\).
By (1) it differs from \(J_n\) in the ambient normalized corner by at most \(8\sqrt{t_n}\).
Compute in that corner using its probability trace, which restricts to the original trace on \(R_n\).
Thus \(x_n=p_n(Z_n,H_n)\) has norm at most two and its right slice for \(\alpha_n\theta_n\) has norm at least \(b_n/2\) by the chosen tolerance.
The resulting \(x_n\) and \(\theta_n x_n\) are intrinsic to the target corner, with unit \(e_n\).

If the distinguished slice had finite cost \(a\) on core contractions, its bound would pass to each of the above simultaneous norm and graph limits.
For every such \(x=e_nxe_n\) the corner calculation gives
\[
   t_n^{3/2}\|(\mathrm{id}\otimes\tau_{e_n})\theta_n x\|_{2,\tau_{e_n}}
                     \le 2a\|x\|.
\]
Indeed the unnormalized slice after inner insertion equals \((E(xe_n)-xE(e_n))e_n\).
Applying this to \(x_n\) would give \(4a\ge t_n^{3/2}b_n/(2\alpha_n)>2^{n-1}\) for all \(n\).
Hence the cost in this single sign-symmetric projection model is infinite.

The [even-algebra identity](Yin_C_F0311_v1.md#statement) now gives two fully actual normal coordinates \(Z,J'ZJ'\) in the fixed algebra of the sign involution, exchanged by conjugation by \(J'\).
Their right slice costs agree.
If either were finite, the parity decomposition would bound the original projection model's cost by \(\sqrt2\) times that finite cost.
Both are thus infinite, which [excludes a bare system](Yin_C_F0070_v1.md#statement).
Conversely the existence of such an actual pair contradicts the universal implication, and a model with infinite sign-symmetric cost gives such a pair by the same even-algebra identity.
This proves the stated qualitative equivalences.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:47 |
| status | open |
| reason | Fix the single-law assembly, conditional compression estimate and exchange-symmetric separator equivalence for complete independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One sign-symmetric projection model and one fully actual exchange-symmetric normal pair under failure of the universal implication, and quantitative compression of fixed free noise. |
| argument | [Argument](#argument) | Reduced-word projections, conditional mean of the sign, mass choices, actual vacuum, intrinsic corner estimates and both coordinate costs. |
| dependency | [Free Hilbert decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Reduced-word representation used to prove the small-corner estimate. |
| dependency | [Sign and exchange models](Yin_C_F0311_v1.md#statement) | Finite sign-symmetric witnesses from failure and the two even-algebra coordinates with their cost comparison. |
| dependency | [Continuity of a finite witness](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Telescoping estimate under perturbation in a larger corner. |
| dependency | [Direct sum before smoothing](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Trace weights, separated spectra, mixed inner kernel and summability of the ambient vacuum. |
| dependency | [Noise insertion](Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) | Actual vacuum on the free extension and at insertion of an arbitrary base tensor. |
| dependency | [Spectral cut and restriction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) | Adding a zero-derivative norm limit and restricting the represented derivative and vacuum. |
| dependency | [Corner comparison](Yin_C_F0308_v1.md#direct-comparison-of-the-original-and-compressed-slices) | Norm and graph convergence of separated cuts, inner insertion and twice the global operator-to-Hilbert cost. |
| dependency | [Bare duals and slice cost](Yin_C_F0070_v1.md#statement) | Exclusion of every bare full-domain system at infinite cost for a normal pair. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:51 |
| status | proved |
| reason | Adopt the free compression estimate and the single exchange-symmetric pair criterion after independent review and adoption of the finite transfer. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One sign-symmetric projection model and one fully actual exchange-symmetric normal pair under failure of the universal implication, and quantitative compression of fixed free noise. |
| argument | [Argument](#argument) | Reduced-word projections, conditional mean of the sign, mass choices, actual vacuum, intrinsic corner estimates and both coordinate costs. |
| dependency | [Free Hilbert decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Reduced-word representation used to prove the small-corner estimate. |
| dependency | [Sign and exchange models](Yin_C_F0311_v1.md#statement) | Finite sign-symmetric witnesses from failure and the two even-algebra coordinates with their cost comparison. |
| dependency | [Continuity of a finite witness](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Telescoping estimate under perturbation in a larger corner. |
| dependency | [Direct sum before smoothing](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Trace weights, separated spectra, mixed inner kernel and summability of the ambient vacuum. |
| dependency | [Noise insertion](Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) | Actual vacuum on the free extension and at insertion of an arbitrary base tensor. |
| dependency | [Spectral cut and restriction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) | Adding a zero-derivative norm limit and restricting the represented derivative and vacuum. |
| dependency | [Corner comparison](Yin_C_F0308_v1.md#direct-comparison-of-the-original-and-compressed-slices) | Norm and graph convergence of separated cuts, inner insertion and twice the global operator-to-Hilbert cost. |
| dependency | [Bare duals and slice cost](Yin_C_F0070_v1.md#statement) | Exclusion of every bare full-domain system at infinite cost for a normal pair. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0321_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

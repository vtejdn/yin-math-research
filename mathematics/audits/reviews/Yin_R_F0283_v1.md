---
author: Yin
---

# Review of local secant spread for a regularly varying singular law

## Finding

At 2026-11-14T14:06 UTC an agent outside proof development independently checked the whole [C_F0274 v1 candidate](../../claims/Yin_C_F0274_v1.md#decision-candidate) dated 2026-11-14T14:03 and the five dependency interfaces bound below.
The reviewer received the fixed candidate without its development dialogue or exploration notes and consulted the earlier distinct finding on the local secant theorem used as an input.
The angular bound and the restrictions on the variation index follow with the stated quantifiers.

For each \(t>0\), the rescaled law of \(P/s\), divided by \(F(s)\), has mass tending to \(t^\alpha\) on \([0,t]\).
On any bounded interval, step approximations therefore give convergence against continuous functions, with the mass near zero controlled by \(t^\alpha\) as \(t\downarrow0\).
Iteration of the two doubling bounds up to the first \(n\) with \(2^n s\in[s_*/2,s_*]\) gives both power bounds because \(F(s_*/2)>0\).
For \(j\ge n\), the upper doubling estimate through \(n\) gives \(2^{(\alpha+\gamma)j}F(s)\ge F(s_*/2)\), so the fixed multiplicative constant \(1/F(s_*/2)\) controls \(F(2^j s)\) even beyond the doubling range.
The mass of each kernel on \(2^j<t\le2^{j+1}\), relative to \(F(s)\), is at most \(K_\gamma 2^{\alpha+\gamma}2^{-j(1-\alpha-\gamma)}\).
The resulting geometric tail tends to zero uniformly in \(s\).
Under \(x=t^2\), the Mellin exponents for \(H\) and \(A\) are respectively \(\alpha/2\) and \((1+\alpha)/2\), both strictly between zero and one.
Their common prefactor is \(\pi\alpha/2\), so \(A/H\to B=\tan(\pi\alpha/2)>0\) for every sequence of radii decreasing to zero.

Apply the two-resolvent theorem to the singleton family \(\{b\}\).
The integral on \([1,\infty)\) is bounded by \(1/2\), so divergence in the candidate supplies precisely the required divergent integral.
On any sequence selected by that theorem the two unit-tensor errors tend to zero, and they continue to vanish on every subsequence converging to a common point.
For the complement projection of any open neighborhood of that point, concentration of the two positive states controls both truncated \(a_s\) legs by \(2^m h_s\) before and after polar conjugation.
The common trace bound on the discarded tails, divided by \(H\), tends to zero as \(m\to\infty\) by the geometric estimate and the positive limit of \(H/F\).
The trace Cauchy–Schwarz inequality then localizes the total variation of \(G\).
Using the local phase comparison on the finite-scale measures and a subsequential limit \(q\) of \(G(1)\), the two unit tests give \(1\le\operatorname{Re}(\lambda q^2)+\epsilon B^2\) and \(\lvert\lambda q+\bar q\rvert\le\epsilon B\) for every \(\epsilon>e(z_0)\) and an optimal phase center \(\lambda\).
In particular \(\operatorname{Re}(\lambda q^2)\le(\operatorname{Re}(\sqrt\lambda q))^2\le\epsilon^2B^2/4\).
Taking \(\epsilon\downarrow e(z_0)\) and the positive square root gives \(e(z_0)\ge 2(\sqrt{1+B^{-2}}-1)=2(\csc(\pi\alpha/2)-1)\).
This uses the vanishing errors of the selected sequence also at the critical index when the slowly varying factor tends to zero.

Existence of at least one such point and the chord distance bound \(e\le2\) force \(\sin(\pi\alpha/2)\ge1/2\), hence \(\alpha\ge1/3\).
Independently of divergence, the lower power bound conflicts with \(F(s)^2\le\pi s\|\xi_i\|_2\) whenever \(\alpha+\gamma<1/2\).
For \(\alpha>2/3\) one can choose \(\alpha-\gamma>2/3\), making the power in the upper comparison for the cubic integrand strictly greater than \(-1\).
For \(\alpha<2/3\) one can choose \(\alpha+\gamma<2/3\), making the power in the lower comparison strictly less than \(-1\).
At equality the exact integral is \(\int_0^1 L(s)^3\,ds/s\), and the displayed logarithmic example diverges by the substitution \(u=\log(e/s)\).
The example gives a scalar distribution near zero and makes no existence claim for an omitted shift.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0274_v1.md#decision-candidate) | Fixed decision dated 2026-11-14T14:03 including all five declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0274_v1.md#statement) | Fixed shift, every common point on a theorem-selected sequence, the angular bound and all three index regimes. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0274_v1.md#argument) | Compact convergence, uniform dyadic tail, both Mellin constants, variation localization, two traces and the endpoint integral. |
| [Finding](#finding) | [Singular-mass estimate](../../claims/Yin_C_F0229_v1.md#statement) | Zero kernel and the square-root mass estimate at the fixed omitted shift, independently of cubic divergence. |
| [Finding](#finding) | [Two-resolvent theorem](../../claims/Yin_C_F0269_v1.md#statement) | The singleton family gives a selected sequence and a common point for its left and right marginal probabilities. |
| [Finding](#finding) | [Mellin integral](../../claims/Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | The positive half-line integral at exponents \(\alpha/2\) and \((1+\alpha)/2\). |
| [Finding](#finding) | [Variation localization](../../claims/Yin_C_F0273_v1.md#concentration-of-the-complex-measures-in-total-variation-away-from-the-point) | Uniform normalized dyadic tails and both positive limits imply concentration of the complex variation. |
| [Finding](#finding) | [Local trace constraints](../../claims/Yin_C_F0273_v1.md#the-two-scalar-trace-inequalities-in-a-local-cone) | Vanishing unit-test errors along the selected sequence and both phase inequalities for the limiting ratio \(B\). |

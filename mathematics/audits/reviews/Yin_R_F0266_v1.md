---
author: Yin
---

# Exact column costs under bilipschitz relabelling and their Lipschitz variations

On 2026-11-14T12:19 UTC, a separate agent reviewed the complete [candidate proof for Yin](../../claims/Yin_C_F0257_v1.md#decision-candidate).
The reviewer took no part in developing the proof and received the fixed claim and its dependency locators without proof-development dialogue, author explanations or prior findings on this candidate.

## Whole-proof finding

The hypotheses give diffuse laws, closable coordinate derivations and the forced starred values on both represented cores, since the whole-plane bilipschitz relabelling preserves actual starred ACSY.
On the distinguished letters the old derivative gives the divided differences of \(\phi\) and \(\overline{\phi}\).
Multiplication by \(K_\phi\) converts these to \(1\) and the new starred phase, respectively.
The inner calculus commutes with both outer actions, so the identity extends to all mixed words.
I checked that the graph approximation used here is available before applying any estimate on sliced columns.
In the cutoff step the limiting squared column modulus has spectrum in \([0,1]\), where the cutoff is constant on a neighborhood, so its outer divided difference vanishes there.
Uniform first-derivative polynomial approximation therefore preserves graph convergence while restoring the input column norm up to \(1+\varepsilon\).
Every bounded Borel insertion and the slice are continuous on the resulting Hilbert-space derivatives.
Reversing the approximation uses \(K_{\phi^{-1}}(\phi(z),\phi(w))K_\phi(z,w)=1\) off the diagonal and the vanishing of the diagonal coarse spectral projection.
The two extended inequalities establish (1) even when a cost is infinite.

For \(F(f)=\mathfrak c_{Y_f}(1)\), (1) takes the supremum over a fixed set of original columns, with continuous output norm for each column.
Each sublevel set is relatively closed, and applying Baire inside an arbitrary nonempty open subset of finiteness gives an open ball with a common bound \(B\).
At a center \(f_0\) of local boundedness, write \(\phi_0=\mathrm{id}+f_0\) and \(h=g\circ\phi_0\).
For all unit Lipschitz tests, \(\|h\|_{\rm Lip}\le 1+\|f_0\|_{\rm Lip}\) and \(|1+Df_0|\ge1-\|f_0\|_{\rm Lip}\), so one positive radius works for the complex Cauchy integral in every direction.
The coefficient of order \(m\) is the original insertion of \((-1)^m K_{\phi_0}((Dg)\circ(\phi_0,\phi_0))^m\).
Taking the Hilbert column norm and applying (1) gives (2) with \(BR^{-m}\).
If the first-order supremum is infinite at every center of an open subset, local application of the same argument forces some infinite original right column cost there.
The selected enlargement theorem applies to that actual tuple at the same coordinate.

For each fixed tested column, the variation of its joint spectral measure is bounded by the product of the Hilbert norms of the two columns, by orthogonality of projections on disjoint sets.
The product law dominates this measure and assigns zero mass to the diagonal.
The two truncated push-forwards have compact support and equal total mass.
Their difference pairs with a unit Lipschitz test as the integral of the truncated divided difference, in the stated order of the variables.
The error against the full integral is at most \(|\beta_{p,q}|\{0<|z-w|\le\epsilon\}\), uniformly over tests for each fixed pair \(p,q\).
This proves convergence in the specified completion and identifies the norm of the limit before taking the supremum over column pairs.
With the inner product linear in the second variable, \(C^*q_j=q_j\otimes1\) yields exactly the integral in the tested Hilbert pairing, and Hilbert duality gives (4).

The whole argument supports the stated extended-real identity, necessary variation estimates, conditional obstruction and dual-norm formula.
The existence of an actual tuple exhibiting the open-set obstruction remains unresolved by this claim.
I used the five selected dependencies at the interfaces below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0257_v1.md#statement) | All three assertions for the actual represented cores, including extended values and the local conditional obstruction. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0257_v1.md#argument) | Forward and inverse transfer, local category and Cauchy estimates, and convergence and duality for actual tested columns. |
| [Whole-proof finding](#whole-proof-finding) | [Planar invariance](../../claims/Yin_C_F0256_v1.md#statement) | Actual ACSY under a single plane bilipschitz change with identity on the other coordinates. |
| [Whole-proof finding](#whole-proof-finding) | [Mixed-core approximation](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Bounded graph approximants for mixed words and the cutoff restoring the finite column norm in either direction. |
| [Whole-proof finding](#whole-proof-finding) | [Starred normal derivatives](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, closability, the distinguished starred phase and zero derivatives of omitted starred letters. |
| [Whole-proof finding](#whole-proof-finding) | [Coarse measure class](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination for the inner joint spectral calculus and its diagonal projection. |
| [Whole-proof finding](#whole-proof-finding) | [Two-Haar enlargement](../../claims/Yin_C_F0208_v1.md#statement) | Infinite original right column cost implies absence of a bare full-domain dual system on the actual enlargement. |

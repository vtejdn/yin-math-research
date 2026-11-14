---
author: Yin
---

# Schur multipliers on products of measure spaces

<a id="ap25-u001"></a>
## Measurable Schur factorization

Section 4 of the [inspected preprint](readme.md) uses \(\sigma\)-finite spaces \((S,\mu),(T,\nu)\).
For each \(h\in L^2(\mu\otimes\nu)\), let \(I_h:L^2(\nu)\to L^2(\mu)\) have integral kernel \(h\), with integration in the second variable against \(\nu\).
A measurable symbol \(\Phi\) is a Schur multiplier for \((\mu,\nu)\) if \(I_h\) of trace class always gives \(I_{\Phi h}\) of trace class.
The norm is the optimal constant in \(\|I_{\Phi h}\|_1\le C\|I_h\|_1\).
The equivalent operator-norm test applies to all Hilbert–Schmidt kernels \(h\), with the same optimal constant (p. 7, equation (4.1) and its dual formulation).

For \(\Phi\in L^\infty(\mu\otimes\nu)\) of Schur norm at most one, Theorem 4.2(i), (iii), p. 8, supplies measurable bounded functions \(\varphi_n,\psi_n\) such that
\[
 \Phi(s,t)=\sum_{n\ge1}\varphi_n(s)\psi_n(t)
 \quad(\mu\otimes\nu\text{-a.e.}),\qquad
 \sum_n|\varphi_n|^2\le1\quad(\mu\text{-a.e.}),\qquad
 \sum_n|\psi_n|^2\le1\quad(\nu\text{-a.e.}).
\]
The converse holds with the same bound.
For a positive real bound \(B\), apply the unit-ball statement to \(\Phi/B\) and multiply both sequences by \(\sqrt B\).
This scaling uses exactly the theorem as printed, which quantifies over positive integer bounds and includes one.
The two pointwise square-sum bounds ensure absolute convergence of the series outside the two marginal exceptional sets.
Its equality to the given symbol holds almost everywhere for the product measure, so any use for a different spectral measure needs its own justification.

The definition, equivalence, envelope normalization and the proof's reference to Theorem 6.1 and Lemma 4.3 were inspected on 2026-11-14.
Theorem 4.2 is accepted as an established input for these measure-space bounds.
The full proofs of the approximation lemmas and the theorem for projection-valued spectral measures were outside this inspection.

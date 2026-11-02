---
author: Yin
---

# KM26: q-Circular Homogeneous Norm Interface

Inspected edition and source notes: [arXiv v2](readme.md).

<a id="km26-u001"></a>
## KM26-U001: Strong Haagerup and Actual q-Fock Norm

Date: 2026-09-11.
Readers: the group-theoretic research agent and independent reviewer the polynomial-core research agent.
Source: [arXiv:2409.03177v2](https://arxiv.org/html/2409.03177v2), Theorem 1.2, Section 2 setup and Lemma 2.3.
Consumer: Yin_T_F0006 and its q-coefficient argument (original material now separated into [Yin_C_F0097_v1](../../../claims/Yin_C_F0097_v1.md), [Yin_C_F0098_v1](../../../claims/Yin_C_F0098_v1.md), [Yin_L_F0024_v1](../../../ledger/Yin_L_F0024_v1.md)).

For the canonical finite q-circular family c and -1<q<1, every holomorphic homogeneous polynomial of degree n satisfies
\[
\|P_n(c)\|\le A(|q|)\sqrt{n+1}\|P_n(c)\|_2,
\]
with A independent of the number of variables.
The statement and normalizations were checked and accepted; the full source proof was not audited.

In the chosen Fock convention c_i=ell_q(e_i)+ell_q(f_i)* for orthonormal e_i,f_i, c_w Omega=e_w.
Degree-n energy is computed using the positive q-symmetrizer P_q^{(n)}=sum_pi q^{inv(pi)} U_pi.
Raw word tensors are not an orthonormal basis.
Different degrees remain orthogonal.

Only holomorphic scalar-coefficient estimates are used.
A finitely sized matrix can be controlled entrywise; this does not import the operator-coefficient generalization mentioned as future work in the source.

### Uniform concatenation interface checked on 2026-09-11

The coordinating agent independently reread Lemma 2.3 in the same primary version.
It gives, for every split n+m,
\[
P_q^{(n+m)}\le C_{|q|}\bigl(P_q^{(n)}\otimes P_q^{(m)}\bigr),
\qquad C_{|q|}=\prod_{k\ge1}(1-|q|^k)^{-1}.
\]
Thus literal concatenation from the Hilbert tensor product of the two deformed homogeneous spaces has norm at most the square root of this constant, uniformly in both degrees.
This is the forward inequality, not a uniform reverse inequality for arbitrary splits.
The same formula appears as equation (3) on printed p. 5 of [Nou04](https://arxiv.org/pdf/math/0605789); the proof of its Lemma 1 on p. 6 separately supplies the uniform one-factor reverse inequality already used in [MS23-U001](../MS23/Yin_U001.md#ms23-u001).
Here Nou's nonnegative deformation bound is specialized to absolute q.
The exact statements and their use were checked; the foundational symmetrizer proofs were not newly audited in full.

This input is used by the [complete state-energy argument](../../../claims/Yin_C_F0101_v1.md).
Its [original review account](../../reviews/Yin_R_F0111_v1.md#original-f0062-account) retains an unknown initial-context relationship, while the current Claim decision selects the later [isolated finding](../../reviews/Yin_R_F0111_v1.md#current-isolated-finding) at its actual eight-section scope.
That argument is a project deduction; neither geometric decay of recognizable state energies nor scalar rational reconstruction is asserted as a theorem of KM26.

The finite-state decay, padding and bounded-inverse conclusions in the consuming ledger are project deductions, checked in [the original proof account](../../reviews/Yin_R_F0109_v1.md#original-f0059-account) at its unknown initial-context relationship; they are not claims made by this source theorem.
The later isolated C_F0097 finding in that R has a different target and supplies no new whole-ledger review.

<a id="strong-convergence-comparison"></a>
## Miy23: Scope Comparison, Not a Proof Dependency

Source: [arXiv:2306.16679v1](https://arxiv.org/html/2306.16679v1), Theorem 1.1 and Corollary 3.3.
Polynomial norms vary continuously with q inside (-1,1), and spectra of selfadjoint polynomials vary in Hausdorff distance.
Selected statements and the moment/Haagerup mechanism were inspected, not the full proof.
These results do not give bounded rational reconstructions and are not premises of the new coefficient deductions.
Miy23 is distinct from the existing MS23 dual/conjugate-system source.

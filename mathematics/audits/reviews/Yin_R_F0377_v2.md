---
author: Yin
---

# Review of the commutator-cubic physical residue detector

## Arrangement and fixed scope

This independent review was performed at 2026-11-19T16:22 UTC by a separately assigned agent outside development of the four-channel argument.
The reviewer received the fixed [L70v4](../../ledger/Yin_L_F0070_v4.md), its requested scope and the applicable rules, without its development dialogue or author explanations.
The review covers its complete bounded algebraic argument, including the stated dimensional and probabilistic limitations.
The earlier [three-channel and covariance review](Yin_R_F0377_v1.md) retains its distinct fixed inputs and findings.
No earlier finding is being extended automatically to this new calculation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Commutator-cubic detector](#commutator-cubic-detector) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Commutator-cubic detector](#commutator-cubic-detector) | [Four-channel realization](../../ledger/Yin_L_F0070_v4.md#cyclic) | The exact determinant identity, structural zero factor and commuting specialization. |
| [Commutator-cubic detector](#commutator-cubic-detector) | [Symmetric witness](../../ledger/Yin_L_F0070_v4.md#witness) | Spectrum, eigenvectors, projector normalization, antisymmetric partial trace and determinant of the detector. |
| [Commutator-cubic detector](#commutator-cubic-detector) | [Actual Schur observation](../../ledger/Yin_L_F0070_v4.md#schur) | Quadratic transpose symmetry, zero diagonal, scalar quotient, residue sign, node collisions including conjugates, and formal coefficient-image membership. |
| [Commutator-cubic detector](#commutator-cubic-detector) | [Remaining requirements](../../ledger/Yin_L_F0070_v4.md#remaining) | The numerical dimension surplus and its expressly limited probabilistic implications. |
| [Commutator-cubic detector](#commutator-cubic-detector) | [Joint quotient interface](../../claims/Yin_C_F0363_v4.md#quotient) | Only the finite-dimensional annihilator argument and conjugate-node realification used by this algebraic construction. |

<a id="commutator-cubic-detector"></a>
## Finding

No gap was found in the bounded algebraic argument.
The four-channel realization has a triangular pivot on channels two through four with diagonal \(zI\).
The product of its off-diagonal blocks in the Schur complement is \(z^{-2}(XYX-YX^2)\).
Its determinant is therefore \(z^{3N}z^{-2N}\det(z^3I-P)=z^N\det(z^3I-P)\), first for \(z\ne0\) and then everywhere by polynomial identity.
The structural factor supplies at least \(N\) zero eigenvalues, with any additional zero multiplicity governed by \(P\).
At a commuting scalar evaluation \(P=0\), the characteristic polynomial is exactly \(z^4\).

At the displayed symmetric witness, \(P=-2Y\) has eigenvalues \(1,-1\), giving \(z^2(z^6-1)\).
The eigenvalue \(1\) is simple.
The identities \(Xu=v\), \(Xv=u\), \(Yu=-u/2\), and \(Yv=v/2\) verify both \(Qr=r\) and \(lQ=l\).
The normalization is \(lr=2+1+1+2=6\).
Using \(\operatorname{Tr}(Kr_al_b)=l_bKr_a\), together with \(Ku=-v\) and \(Kv=u\), gives every displayed entry of \(F\).
Direct multiplication then gives the stated upper triangular \(D=BFA-AFB\); its four diagonal entries are \(1/3\), so \(\det D=1/81\).

The physical test is legal for the actual Schur quadratic coefficient.
Since \(K^{\mathsf T}=-K\), the two-color matrix \(H\) is transpose-symmetric and has zero diagonal.
Thus its trace pairing is unchanged by transpose symmetrization and kills diagonal-square contributions.
Block multiplication yields (4), including the difference sign and without an extra factor of two.
The same pairing kills physical scalar blocks because \(\operatorname{Tr}K=0\).
Ordinary transpose reverses physical products without conjugating the spectral node, and the substitution by symmetric \(X,Y\) respects this operation.

At \(t=z\), the \(1\)-eigenspace of \(Q\) contributes residue \(-P_1\), and the other eigenspaces are regular.
Consequently minus the residue of the tested Schur kernel is exactly \(D\).
The nonzero spectrum of \(Q\) is \(\mu_6\); hence another node \(w\) can have a pole at \(t=z\) exactly when \(w/z\in\mu_6\).
For the complete finite list, including conjugates, the collision equations are proper real algebraic conditions.
They exclude a null set in the planar product of the original node parameters, including the exceptional rays where a node collides with its own conjugate.

A formal rational identity among the symmetrized kernels remains an identity after the symmetric matrix substitution wherever the expressions are defined, and hence as a meromorphic identity in \(t\).
Taking the isolated residue annihilates its scalar part and all other nodes.
Its remaining coefficient pairs with \(D\).
Finite-dimensional annihilator duality therefore puts the node-supported matrix \(D\) in the joint coefficient image modulo scalar physical kernels.
Including the conjugate kernels gives the equivalent real-and-imaginary basis statement.
This argument concerns formal kernels; accidental dependencies at a fixed numerical old block are outside its conclusion.

The four-by-four detector has full rank, so choosing all four auxiliary rows and columns gives the stated numerical inequality \(4+4>4\).
It does not construct eight independent physical random directions or verify their conditional spread.
The old-block covariance and oversampling results and the conditional LCD alternative are named only as possible interfaces; this review does not adopt their hypotheses for the commutator cubic.
The initial principal trim, physical projected spread, original-sign polarization and subsequent restoration estimate remain unproved here.
In particular the finding establishes no summable smallest-singular-value bound, integrated terminal logarithmic estimate or Brown-convergence theorem.

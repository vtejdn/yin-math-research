---
author: Yin
---
# CN25: approximate Jacobian relations and uniform derivation domains

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [CN25 arXiv v2](../../../literature/pdf/CN25--arxiv-v2.pdf), arXiv:2201.00062v2, 4 January 2022, 22 pages.
Published identity: Indiana University Mathematics Journal 74(4) (2025), 883--918.

Passages: Sections 1.2--1.3, pp.3--5; Lemma 3.1 and Theorem 3.2, pp.10--11; Theorem 3.6, p.12; Proposition 6.8 and Theorem 6.9, pp.20--22.
Printed and PDF page numbers agree.

Inspection: 2026-10-15: exact statements and displayed proof mechanisms read at these scopes.
Approximate-relation pairing and the local module/topology distinction were checked.
The Dirichlet-form inputs from DL92, Sau89 and Cip08, and the general dimension foundations, were not independently re-audited.
These passages are accepted as established source interfaces with those boundaries.


<a id="cn25-u001"></a>
## Approximate relations require actual limits

Lemma 3.1 assumes a net of polynomial vectors whose evaluated values tend weakly to zero in L2 and whose **entire evaluated Jacobians** tend weakly in the indicated Hilbert tensor matrix space.
Every actual vacuum derivation is orthogonal to the resulting derivative module.
The proof pairs the derivative values against algebraic tensors in its actual adjoint domain, then passes to the weak limit.
Theorem 3.2 specializes to a bounded limiting Jacobian and bounds free Stein dimension by its kernel dimension.

An ambient presentation with fewer variables supplies neither the required polynomial net nor these graph limits.
Theorem 3.6 additionally assumes full Stein dimension for its starting tuple and actual membership of the adjoined elements in the closed full-gradient domain.
It is not an unrestricted subalgebra monotonicity or target-to-reference extension theorem.

## Actual derivations versus their closure

Lemma 1.1 makes all derivations into a Hilbert space via generator values, while the free Stein dimension uses the closure of the actual-vacuum subspace.
Section 1.3 explicitly limits the algebraic module action on that actual subspace.
Consequently dimensions or module closure do not decide a prescribed affine slice of the actual adjoint domain.

Proposition 6.8 defines a larger algebra by simultaneous membership in the actual closures of delta together with its real companion and a uniform bound for ||delta(y)||/||delta||_X over all actual-vacuum derivations.
It proves Lipschitz functional-calculus and weak closedness properties at that uniform bound.
Theorem 6.9 preserves the dimension for that particular algebra.
Membership and the uniform bound are premises; weak density alone does not put h or S_j into this algebra for C_F0147.

The separate target-only functional criterion in [D_F0005](../../../drafts/Yin_D_F0005.md#an-exact-target-only-functional-reduction) uses the source's actual-versus-closed distinction.
The new resolvent proof is fixed at [C_F0148's argument](../../../claims/Yin_C_F0148_v1.md#argument); it does not assume the full-Jacobian convergence required by Lemma 3.1, or invoke the uniform Dirichlet algebra without its premises.

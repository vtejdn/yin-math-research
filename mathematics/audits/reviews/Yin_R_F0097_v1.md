---
author: Yin
---

# Independent internal review: finite free square-zero positive support

Review completed: 2026-09-16.
Human record author: Yin.
Reviewer: separately organized Codex research subagent the reviewing agent.
Proof developed by another AI agent, then transcribed and edited by the coordinator.

Reviewed Claim: [Yin_C_F0116_v1](../../claims/Yin_C_F0116_v1.md#decision-candidate-0001).
Complete reviewed statement and supporting proof: [Yin_C_F0116_v1.md](../../claims/Yin_C_F0116_v1.md#finite-free-square-zero-positive-support), introductory statement and Sections 1--6.
Consumer context: [Yin_T_F0007_v1](../../tasks/Yin_T_F0007_v1.md#decision-candidate-0001).

**Verdict: pass for both conclusions for every finite integer m>=1.**
In the specified reduced free product of m normalized-trace M2 factors, every bounded element of the affiliated scalar division closure of `A=C<x_1,...,x_m>`, with `x_i=e12^(i)`, has positive-word Fourier support and belongs to the bounded scalar division closure of the same A.
Unbounded intermediate affiliated inverses are included.
No conclusion about arbitrary proper non-star or diffuse inputs is accepted.

## 1. Review arrangement and fixed inputs

The reviewer did not invent, develop or write the terminal-block construction or its affiliated-closure proof.
The reviewer had independently reviewed the earlier C_F0113 conditional reconstruction and was familiar with the same C_F0106/DR97 interface.
The coordinator first supplied the author's proposed core mechanism; the reviewer independently checked the local matrices, boundary commutations, actual affiliated domains and trace ordering, reporting provisional findings before receiving the fixed full proof.
Those checks were communicated to the coordinator and author; no correction or additional hypothesis was requested.
The present review then read and checked the complete fixed proof, including its finite-m reconstruction and scope.
This is separately organized internal AI review with disclosed prior subject familiarity and shared context, not blind review or external human review.

The **only necessary direct Claim dependency** is [Yin_C_F0106_v1](../../claims/Yin_C_F0106_v1.md#decision-candidate-0002).
Its actual finite-factor residual and state construction is used; its full-star scalar closure conclusion alone would not imply the present non-star conclusion.
The reviewer inspected the [Claim proof](../../claims/Yin_C_F0106_v1.md).
Its accepted prior review supplies the dependency trust boundary, and the specific Sections 4--7 interfaces were rechecked directly here.

C_F0113 is the earlier three-factor conditional proof-method precedent, not a premise enlarged to m factors.
C_F0112 is an earlier independent two-factor result used for comparison.
The present proof directly supplies the m=2 instance and proves the single-factor input equality, so neither Claim is needed as an additional logical dependency for its conclusion.

The two retained external interfaces are:

- [FK86 affiliated-algebra foundation](../literature/FK86/Yin_U001.md#measure-topology-interface): finite-trace affiliated operators form the algebra whose sums and products are closures of the initial densely defined operator operations.
  The existing audit records primary parsed-text inspection of Sections 1.2, 1.4--1.5, printed pp. 271--272 / PDF pp. 4--5, with foundational statements and applicability accepted, not their original proofs re-audited.
- [DR97-U004, Lemma 11](../literature/DR97/Yin_U004.md#dr97-u004): norm-decaying powers of a matrix over a unital Banach algebra permit inversion of I minus that matrix using bounded scalar inverses of expressions in its entries.
  The existing source audit reconstructs and independently cross-checks its local proof, including corrected Schur formulas, against the published source, printed pp. 619--621 / PDF pp. 7--9.

The existing AP18 interface fixes the affiliation/domain convention.
The review consumes the recorded foundational interfaces and checks the new application; no fresh source acquisition, source-page rendering or whole-paper audit is claimed.
The group-specific DR97 realization theorem is not being applied to matrix units.
C_F0106's own transitive finite-residual and homogeneous-estimate inputs remain within its accepted scope.

## 2. Local matrices and every commutation boundary

For normalized trace, the displayed `z_+, z_-, z_0` are an orthonormal centered basis.
Direct multiplication gives `d(z_+)=0`, `d(z_-)=-sqrt(2)z_0`, and `d(z_0)=sqrt(2)z_+`.
Thus d has norm exactly sqrt(2), centered kernel `Cz_+`, and no scalar output.

In the reduced free-product Hilbert decomposition, fixing a reduced prefix ending outside factor i gives one orthogonal three-dimensional terminal-i block.
T_i acts there by this same matrix and annihilates the complementary basis vectors.
There are no terms landing in another block.
The operator is consequently bounded of norm sqrt(2), and its kernel is exactly the absence of the two forbidden terminal-i coefficients.
This is an exact kernel description, not merely an inclusion of positive words.

The commutation check must include more than disjoint first and last blocks.
On the vacuum, a generator is either outside terminal factor i or lies in the local kernel.
On a one-block vector a in factor i, the same-factor computation gives both orders as `x_i a x_i`.
Subtracting the scalar part of `x_i a` does not affect d; the other order has no hidden scalar component since `tau(x_i a x_i)=tau(a x_i^2)=0`.
A different generator prefixes a block and leaves the local terminal action unchanged.
For a one-block vector from another factor, both orders are zero even when the left product creates a vacuum term.

For at least two blocks, left multiplication changes or removes only the first block.
In the only short boundary, deleting that first block leaves the original terminal block, whose d-image remains centered.
The two orders therefore give exactly the two terms displayed in Section 2, without an additional deletion or scalar contraction at the right.
Longer words introduce no new boundary.
These calculations exhaust the basis, and boundedness extends the commutation identities to all H.

## 3. Extracting forbidden letters in arbitrary positions

The argument uses full commutation of f with T_i, not just `T_i f Omega=0`.
For a reduced word `v z_(i,t) s` with a forbidden t, the adjoint suffix s* ends outside factor i.
Thus `T_i(s* Omega)=0`, including the empty suffix.
Commutation implies `f s* Omega` lies in the exact kernel identified above; its coefficient at `v z_(i,t)` is zero.

The coefficient identity has the correct order:

`tau((v z_(i,t))* f s*) = tau(s* (v z_(i,t))* f) = tau((v z_(i,t) s)* f)`.

All factors here are bounded, so tracial cyclicity is legitimate.
Each forbidden letter of any reduced basis word can be selected in this manner.
Hence every word with a forbidden letter has zero coefficient.
The remaining basis vectors are precisely the vacuum and the reduced products of `sqrt(2)x_i`; their closed span is H_+.
No total-degree substitute or assumed inverse-invariance of H_+ is involved.

## 4. Closed affiliated operations, including unbounded inverses

Fix a bounded T.
For two affiliated operators satisfying the specified one-sided domain invariance and literal commutation, their initial sum domain is T-invariant.
Their actual composition domain is T-invariant as well: if `xi in Dom b` and `b xi in Dom a`, then `T xi in Dom b` and `b T xi=T b xi in Dom a`.
Thus both initial operations commute on exactly their legal domains.

The finite-trace affiliated-algebra foundation makes these initial domains dense and their operations closable, with closures equal to the affiliated sum and product.
If `(xi_n,c xi_n)` converges to `(xi,eta)` in the graph of either initial operation c, boundedness of T makes `(T xi_n,T c xi_n)` converge to `(T xi,T eta)`.
These are still points of the initial graph.
Its closure therefore contains the latter point.
This proves invariance and commutation for the actual closed sum/product, without requiring either graph convergence of a and b separately or invariance of a merely formal domain.

For an affiliated algebra unit a, its kernel and cokernel projections vanish by multiplication with the algebraic inverse; the displayed projection arguments are valid affiliated identities.
Equivalently, the polar decomposition has full initial and final support.
Its actual closed inverse is the ordinary operator inverse with domain Ran(a): spectral calculus for its positive part verifies this equality, even if the range is not closed.
Since `T a xi=a T xi`, the range is T-invariant, and the calculation in (9) proves commutation with this actual inverse on its entire domain.
No commutation with T* or selfadjointness of T is needed.

The class E_T is thus a unital scalar-division-closed subalgebra of L0(M).
Every generator belongs to every E_(T_i), so the entire affiliated scalar division closure belongs to their intersection.
For its bounded outputs the actual domain is all H, giving the full commutation required in Section 3.
This establishes positive support even for rational evaluations with unbounded intermediate inverses.

## 5. Finite-m state construction and reconstruction in the original A

C_F0106 covers any fixed finite number of finite-dimensional tracial factors, including m=1.
For the full star algebra B, the inclusion `A subset B` puts the bounded f within that proof's hypothesis.
Its Section 4 first gives finite-rank auxiliary commutators.
Section 5 extends Fourier coefficients by zero on **all nonreduced words of the full free monoid**, obtains a finite residual space and selects a reachable and observable minimal realization.
Its coefficient-shift identity gives square-summability of every state entry and, crucially, actual same-factor matrix zero products.
Thus it supplies more than a realization valid only on admissible paths.

C_F0106 Section 7 uses its positive matrix energy to obtain exponential state-energy decay.
Same-factor zero products eliminate every nonreduced term before factor multiplication can shorten a word.
Its homogeneous estimate then gives actual matrix operator-norm decay `V^k -> 0`.
This precedes the positive `B*B` scalar-pivot construction.
The norm-convergent geometric inverse, coefficient identity and faithfulness of the trace identify `lambda(I-V)^(-1)gamma` with f, independently of that later star-algebra reconstruction.
This is exactly the portion required here.
Zero or constant series are immediate cases of the conclusion and require no nontrivial state construction.

The Pauli-to-`z_+,z_-,z_0` basis change is unitary within each factor.
Fourier coefficients therefore transform with conjugate U, as stated.
Since each transition family linearly spans the other factor by factor, reachability, observability and same-factor zero products are all preserved.
The sum of the transformed matrices tensored with the transformed letters equals the **same bounded operator V**, by `sum_t conjugate(U_ts)U_tr=delta_sr`.

The newly proved support assertion annihilates scalar coefficients containing a forbidden letter on every reduced word; the state zero products handle every nonreduced word.
Thus the rows `lambda mu'(p)` and columns `mu'(q)gamma` annihilate the middle forbidden matrix for all p,q in the full monoid.
Their spanning properties force that matrix itself to vanish.
The surviving pencil has entries in the original non-star A and retains its previously proved norm decay.
No inference from scalar-output cancellation without minimality is used.

Finally DR97 Lemma 11 applies to this actual pencil in M_N(M).
A sufficiently small power V^q has entries below `1/(2N)`.
Scalar Schur elimination of `I-V^q` gives successive entry bounds `r_k=1/(2N-k)<1`, so every scalar pivot has a bounded inverse in M.
The resulting expressions use only entries of V and ring operations.
Multiplication by `I+V+...+V^(q-1)` then gives the entries of `(I-V)^(-1)` in `Div_M A`.
This avoids C_F0106's `B*B` step and adds neither adjoints nor unbounded inverses to the reconstruction.
Multiplying by the scalar state row and column proves f belongs to R.
The reverse inclusion holds since every bounded scalar inverse is also its affiliated inverse.

## 6. Accepted scope and remaining Task boundary

Both stated conclusions are proved for every finite m>=1 with normalized M2 factors and these specified matrix units.
The one-factor input equality follows directly from `(a+b x)^(-1)=a^(-1)-b a^(-2)x` when a is nonzero; when a=0 the element is not invertible.
The three-factor and higher finite-factor cases consequently give proper non-star input examples within the binary Task by grouping already treated factors.
This does not require assuming the general binary permanence statement to prove the present theorem.

The earlier positive-support gap for this particular family is resolved by Sections 1--4, and the conditional realization then gives the full bounded-intersection equality for the family.
General T_F0007, arbitrary proper non-star input algebras and diffuse factors remain outside the theorem.
No proof-assistant check, numerical experiment, novelty determination, external human review or full Task completion is asserted.
This review changed only its own audit file, not the proof, canonical records, Task or indexes.

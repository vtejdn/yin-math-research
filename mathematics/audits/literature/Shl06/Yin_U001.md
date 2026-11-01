---
author: Yin
---

# Shl06: Unbounded Dual Systems and the Conjugate Interface

## Shl06-U001

Source: [retained Abel Symposium preprint](../../../literature/pdf/Shl06--abel-preprint.pdf), Sections 1.1--1.2, Theorem 1 and Corollary 2, pp. 2--4.
Review: 2026-10-10, direct AI reading and self-reviewed reconstruction for Yin; no independent reviewer.

### Precise setting and terminology

Let M be a finite von Neumann algebra with faithful normal tracial state, H=L2(M), Omega=1, P the projection onto C Omega, and X a finite selfadjoint generating tuple.
Put A=C<X>.
Inner products here are linear in the second argument, and HS has inner product Tr(S* T).
This fixes the convention for every formula below rather than copying inconsistent printed adjoint formulas.

For a tuple T of Hilbert--Schmidt operators, Theorem 1 presupposes a **well-defined derivation** delta:A -> HS satisfying delta(Xj)=Tj.
Arbitrary prescribed T need not descend through algebraic relations among X.
For example X1=0 forces T1=0.
The introductory prescription on generators is not permission to omit this compatibility requirement.

<a id="shl06-normalized-dual-construction"></a>
The source uses **dual system**, **dual systems of unbounded operators**, and **closable unbounded operator**.
Its Theorem 1 imposes Y Omega=0 and Omega in Dom Y*.
It does not name this a canonical dual system.
MS23 Definition 2.4 explicitly calls the corresponding tuple a **normalized dual system**, explaining that normalization means vacuum annihilation in addition to the older dual-system requirements.

Here unbounded is the unbounded-operator framework, not a requirement that the operator have infinite norm; bounded cases remain allowed.
A tuple is dual to X.
Conjugate variables establish existence/closability and give its adjoint vacuum values; it is misleading to call it a dual system *of the conjugate variables*.

### Theorem 1: corrected full proof

The equivalence is P in Dom delta* if and only if there is a densely defined closable Y containing A Omega in its domain, annihilating Omega, satisfying [Y,Xj]=Tj on A Omega, with Omega in Dom Y*.
It is enough to choose exactly the polynomial domain and then take its closure.

Suppose first Y exists.
Leibniz expansion gives [Y,p]=delta(p) on A Omega, and therefore

\[
 \langle P,\delta(p)\rangle_{HS}
 =\langle\Omega,Y(p\Omega)\rangle
 =\langle Y^*\Omega,p\Omega\rangle.
\]

Consequently P is in Dom delta* and xi=delta*(P)=Y* Omega.

Conversely, put xi=delta*(P) and define Y0(p Omega)=delta(p)Omega.
Faithfulness of the trace and well-definedness of delta make this a well-defined densely defined operator.
The derivation identity gives Y0 Omega=0 and [Y0,Xj]=Tj on the polynomial domain.
For q in A set

\[
 Z(q\Omega)=q\xi-\delta(q^*)^*\Omega.
\]

For p,q in A, use the adjoint relation for delta on q* p and expand delta(q* p)=delta(q*)p+q*delta(p).
It gives

\[
 \langle p\Omega,q\xi\rangle
 =\langle\delta(q^*)p\Omega,\Omega\rangle
  +\langle\delta(p)\Omega,q\Omega\rangle.
\]

The first term is exactly <p Omega,delta(q*)* Omega>.
Hence <Y0 p Omega,q Omega>=<p Omega,Z q Omega>.
Thus A Omega is contained in Dom Y0*, Y0* q Omega=Z q Omega, and Y0 is closable.
Its closed extension D=closure(Y0) has the same adjoint and is fixed by choosing the polynomial-domain closure.
Any other normalized implementer agrees on A Omega, but may have a different larger domain; uniqueness on the polynomial domain is not uniqueness of all closed extensions.

### Literal-source corrections

The displayed definition of Y* on p. 3 omits multiplication by q before xi.
The printed expression -delta(q*)* Omega+xi sends q=0 to xi, so it cannot be a linear operator when xi is nonzero.
The correct expression above passes this immediate check.
This omission is visible in the PDF, not an extraction artifact.

The same page prints (Y-JY*J)Omega=JY*Omega although Y Omega=0, an algebraically inconsistent sign.
It also prints a minus in Y(q Omega)=[Y,q]Omega-qY Omega and inconsistent commutator signs in the final verification.
The complete calculation above avoids these mistakes.
With a normalized dual, the resulting relation is xi=Y0* Omega.
Theorem 1 itself is supported under the well-defined derivation hypothesis.

### Free difference quotient specialization

For delta_i(p)=sum a P b when partial_i p=sum a tensor b, one has

\[
 D_i^0(p\Omega)=(\mathrm{id}\otimes\tau)(\partial_i p)\Omega,
 \quad (D_i^0)^*(p\Omega)=p\xi_i-D_i^0(p\Omega),
 \quad (D_i^0)^*\Omega=\xi_i.
\]

The second formula uses selfadjoint X and the star/flip relation for the free difference quotient.
It includes the necessary p xi_i term missing from the source's general adjoint formula.
MS23 Definition 2.4/Theorem 2.5 is the terminology/conjugate-system interface; Shl06 Theorem 1 is the earlier general derivation result.

This theorem does NOT establish M Omega contained in Dom D_i intersect Dom D_i*, boundedness of D_i, or a rationality criterion.
A bounded-vector domain property requires separate estimates, such as those in Dab10.
No Claim assessment changes are required by this source correction.

### Corollary 2 and the essential-skew-adjointness limit

On A Omega the operator B_i=(D_i^0-(D_i^0)*|A Omega)/2 is skew-symmetric and [B_i,Xj]=delta_ij P.
A densely defined skew-symmetric operator is closable.
Conversely, for a skew-symmetric implementer B with polynomial domain, Omega belongs to Dom B*, and direct tracial calculation yields the conjugate vector B*Omega-JB Omega.
The printed p. 4 formula has incompatible signs under the convention fixed above.

The source calls the implementers **essentially anti-symmetric**.
Its construction proves skew-symmetry and closability; it does not prove that the closure is skew-adjoint (which would require an additional domain/maximality argument).
Therefore the existence equivalence with *closable skew-symmetric* implementers is checked, while an interpretation as *essentially skew-adjoint* remains Questioned.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Shl06, nine-page Abel Symposium preprint.

Passages: Sections 1.1--1.2, Theorem 1, Corollary 2; pp. 2--4. MS23 Definition 2.4 and Theorem 2.5 supply the explicit normalized-system name.

Inspection: 2026-10-10: complete reading, p. 3 and p. 4 visual checks, both Theorem 1 implications reconstructed in one inner-product convention, adjoint omission tested at q=0, polynomial specialization checked. Core equivalence audited within stated scope; essential skew-adjointness not established. arXiv v1 has the same p. 3 defects; no publisher-version collation, formal verification or independent review.

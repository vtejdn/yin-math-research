---
author: Yin
---

# Full matrix units from a rational regular rank in a free cyclic extension

## Statement

Let \(G\) be torsion-free and let \(X\in M_{n,m}(D_j(G))\), using the [scalar inverse layers](Yin_C_A0239_v1.md#statement).
Suppose its unnormalized regular rank is \(\rho=p/q\) in lowest terms, \(q>1\).
Choose \(1\le k<q\) with \(kp\equiv1\bmod q\) and set \(b=\lfloor k\rho\rfloor\).
Then \(D_{j+b+1}(G*\mathbb Z)\) contains algebraic matrix units for a unital copy of \(M_q(\mathbb C)\).
In particular its unit splits into \(q\) mutually isomorphic projective summands, each of regular dimension \(1/q\).
The diagonal idempotents of this system need not be selfadjoint.
For a scalar first Schur complement of rank \(1/q\) this gives the matrix units in the second inverse layer for every \(q>1\).

For each fixed integer \(d>1\) the following three existence statements are equivalent, allowing the torsion-free group to vary.

1. A finite complex group-ring matrix has nonintegral rational regular rank with reduced denominator divisible by \(d\).
2. For some finite \(i\), the scalar ring \(D_i\) contains a unital copy of \(M_d(\mathbb C)\).
3. The unit class belongs to \(dK_0(D_\infty)\), where \(D_\infty=\bigcup_iD_i\) is the actual division closure.

From the first statement the second is realized in the free cyclic extension of the original group.
From the third statement one obtains a finite group-ring matrix in that same group with rank \(a+1/d\) for a nonnegative integer \(a\).
The equivalence concerns rational ranks.
For an irrational \(\rho\), the same compression below realizes every fractional part \(\{k\rho\}\), \(k\ge1\), as the rank of a positive scalar in a finite inverse layer of one fixed \(G*\mathbb Z\); these ranks are dense in \([0,1]\).

## Two nested column compressions

More generally take any positive integer \(k\) for which \(k\rho\) is not an integer, put \(b=\lfloor k\rho\rfloor\), and form \(Z=I_k\otimes X\).
Fix a subgroup \(K\le G\) supporting an inverse expression for \(X\), choose an infinite-order \(h\in K\), and write \(H=G*\langle x\rangle\).
Such \(h\) exists because a constant matrix has integer rank.
Inside \(H\), the group \(K\) and the cyclic groups on \(w=xhx^{-1}\) and \(v=x^2hx^{-2}\) generate their free product by normal form.
Use \(w\) for the compression and reserve \(v\) for the final matrix units.

Let \(l=km\) and let \(E\) be the initial projection of \(Z\), of unnormalized trace \(k\rho\).
Use the [trace balancing and Fourier columns](Yin_C_A0239_v1.md#the-finite-frame-in-the-free-product) on these \(l\) coordinates, now with normalized trace \(k\rho/l\) for \(E\).
This gives a single \(l\)-by-\(l\) group-ring unitary over \(K*\langle w\rangle\) of the form \(U\operatorname{diag}(w^ihw^{-i})F_l\), with \(U\) the constant balancing unitary and \(F_l\) the normalized Fourier matrix.
For \(s=b,b+1\), let \(V_s\) consist of its first \(s\) columns.
In particular \(b+1\le l\).
For \(0<s<l\) its range projection is free from \(E\) under the normalized scalar matrix trace.
Indeed after conjugating by \(U\), the centered range projection has zero diagonal because the retained \(s\) columns of \(F_l\) all have constant modulus.
Splitting the centered entries of the old projection into scalar and centered parts gives exactly the reduced-word expansion in the finite frame proof, which allows distinct traces \(s/l,k\rho/l\).
The [free intersection formula](../audits/literature/CK14/Yin_U001.md#ck14-u001) gives
\[
               \operatorname{rk}(ZV_s)=\min(s,k\rho).
\]
At \(s=0,l\) this follows from the empty frame or the full unitary.

The positive \((b+1)\)-square matrix \((ZV_{b+1})^*ZV_{b+1}\) thus has rank \(k\rho\), and its leading \(b\)-square principal block has full rank \(b\).
For \(b>0\), the leading block has an affiliated inverse with entries in \(D_{j+b}(K*\langle w\rangle)\) by [positive scalar elimination](Yin_C_A0239_v1.md#inner-rank-and-the-unit-class).
The scalar Schur complement \(T\) is positive of rank \(k\rho-b\) by triangular congruence, with entries in the same layer.
For \(b=0\) take the single Gram entry as \(T\) in \(D_j\).
This gives the asserted irrational conclusion by density of the fractional parts of the positive multiples of an irrational number.

## Splitting the identity into equivalent summands

For \(kp\equiv1\bmod q\) the preceding \(T\) has rank \(1/q\).
Apply the [one-column frame for a rational scalar](Yin_C_A0239_v1.md#inner-rank-and-the-unit-class) to \(T\) over \((K*\langle w\rangle)*\langle v\rangle\), still inside \(H\).
It gives a \(q\)-by-one column \(W\), a row \(Y\), and the nonzero scalar image projection \(P\) of \(T\), all over \(R=D_{j+b+1}(H)\), such that
\[
                   YW=1,\qquad WY=P I_q .
\]
For the standard complex matrix units \(e_{ij}\) of size \(q\) define \(f_{ij}=Y(Pe_{ij})W\in R\).
Since \(WY=PI_q\), these satisfy \(f_{ij}f_{kl}=\delta_{jk}f_{il}\) and \(\sum_i f_{ii}=1\).
They give a unital homomorphism from \(M_q(\mathbb C)\), injective by simplicity.
All \(q\) diagonal right ideals have equal regular dimension by the off-diagonal isomorphisms, hence dimension \(1/q\).
This strengthens stable divisibility of the algebraic unit class to an actual matrix algebra after the stated number of inversions.

## Recovering a group-ring rank from the unit class

If \(d\mid q\), the unital embedding of \(M_d(\mathbb C)\) into \(M_q(\mathbb C)\) given by tensoring with \(I_{q/d}\) proves the first implication.
A unital system of \(d\)-square matrix units splits the right regular module into \(d\) isomorphic summands.
Extension of scalars to \(D_\infty\) therefore gives the third statement.

Conversely write \([1]=d([E]-[F])\), with finitely generated projectives represented by idempotents \(e\in M_a(D_\infty)\) and \(f\in M_c(D_\infty)\).
Apply extension of scalars to the affiliated algebra followed by regular dimension, an additive homomorphism on projective classes since split sums and isomorphisms are preserved.
It gives \(\operatorname{rk}e-\operatorname{rk}f=1/d\).
The matrix \(B=e\oplus(I_c-f)\) therefore has rank \(c+1/d\).
All its entries belong to one finite scalar inverse layer since only finitely many expressions occur.
The [polynomial block presentation](Yin_C_A0239_v1.md#the-exact-original-infimum) writes \(B=D-CA^{-1}B_0\) with polynomial blocks and an affiliated-unit square \(A\) of size \(u\).
The polynomial matrix with rows \((A,B_0)\) and \((C,D)\) has rank \(u+c+1/d\) by elimination.
It has precisely the desired reduced denominator.
The argument uses projective classes without any exactness premise for nonsplit sequences.

## Assessment history

### Decision matrix-units-for-a-prescribed-denominator

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:04 |
| status | proved |
| reason | Whole-proof inspection verified the nested compression, construction of unital matrix units, finite depth and the same-group converse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The finite layer for full matrix units, the three existential conditions and the irrational conclusion. |
| argument | [Two nested column compressions](#two-nested-column-compressions) | The two ranks within one Fourier frame, the scalar Schur complement and its depth. |
| argument | [Splitting the identity into equivalent summands](#splitting-the-identity-into-equivalent-summands) | Two free directions in the same cyclic extension and the unital algebraic matrix units. |
| argument | [Recovering a group-ring rank from the unit class](#recovering-a-group-ring-rank-from-the-unit-class) | The exact denominator in the group giving the K-theory divisibility. |
| review | [Matrix units for a prescribed denominator](../audits/reviews/Yin_R_A0200_v1.md#matrix-units-for-a-prescribed-denominator) | Independent review of the fixed proof. |
| review | [Independent verification of the four results](../audits/reviews/Yin_R_A0200_v1.md#independent-verification-of-the-four-results) | Separate whole-proof review of the four fixed statements. |

## Current assessment

[Selected decision](#decision-matrix-units-for-a-prescribed-denominator)

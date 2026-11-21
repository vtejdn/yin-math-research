---
author: Yin
---
# Rank denominators after a finite extension of rational coefficients

## Whole finding

At 2026-11-21 05:22 UTC an agent outside the development of C104 independently reviewed its full [statement](../../claims/Yin_C_A0104_v1.md#statement) and [argument](../../claims/Yin_C_A0104_v1.md#argument) for Yin.
The reviewer received the fixed Claim and the requested points of scrutiny, without development dialogue, author explanations or a prior verdict on C104.
The proof establishes the stated denominator bound for any number field and the divisibility assertion for a Galois number field.

Rational integrality on \(G^j\) passes to every coordinate subgroup \(G^t\), and the rational division closure of each is a division ring by [Lück and Linnell, Theorem 2.3(1),(3)](https://arxiv.org/pdf/1602.06906v3#page=10).
I checked the hypotheses of that theorem and the [coordinate embeddings](../../claims/Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings).
For a nonscalar \(x\in D\), the [square test](../../claims/Yin_C_A0096_v2.md#the-square-test-for-a-scalar-affiliated-element) makes each \(x-\lambda\) a unit in \(U(G)\).
Factoring an annihilating rational polynomial over \(\mathbb C\) rules out algebraic nonscalars.
Consequently any element of \(Z(D)\) algebraic over \(k=D\cap\overline{\mathbb Q}\) lies in \(k\), by transitivity of algebraicity.
Every monic factor over \(Z(D)\) of the minimal polynomial of a primitive element of \(kK/k\) has coefficients algebraic over \(k\), since they are symmetric expressions in a subset of its roots.
This proves \(Z(D)\otimes_k kK\) is a field even if \(k/\mathbb Q\) is infinite.

For any division ring \(D_0\) with center \(Z_0\) and any finite field extension \(W/Z_0\), the minimal-length argument in the Claim makes a nonzero ideal of \(D_0\otimes_{Z_0} W\) contain a unit.
Indeed, after normalizing the first coefficient to one, every commutator with \(d\otimes1\) loses that coefficient, so minimality and independence of the \(W\)-entries force the other coefficients into \(Z_0\).
The resulting central tensor is \(1\otimes w\) with \(w\ne0\).
Right ideals are right \(D_0\)-subspaces of a space of dimension \([W:Z_0]\), giving the Artinian condition independently of \([D_0:Z_0]\).
Applying this with \(D_0=D\) and \(W=Z(D)\otimes_k kK\) shows that evaluation has zero kernel by simplicity and has image \(DK\), since the \(k\)-span of \(K\) is a finite-dimensional domain and hence equals \(kK\).
The hypotheses of Artin–Wedderburn therefore hold.

Write \(E=M_s(V)\) in the resulting coordinates and \(U=U(G)\).
The right modules \(e_{aa}U\) of its diagonal units have equal dimension by multiplication by \(e_{ab}\), and sum directly to \(U\), so each has dimension \(1/s\).
For a rectangular matrix over \(E\), elimination on its expanded \(V\)-matrix reduces its image to the sum of one such module per pivot.
The row and column operations assemble into invertible block matrices over \(E\), hence preserve the dimension of the image after passage to \(U\).
This gives the unnormalized regular rank also for \(K[G]\), including when the idempotents in \(U\) are not projections.

In \(E_j=D_jK\), matrix units from different coordinates commute.
Their products satisfy all matrix-unit identities with diagonal sum one.
For the resulting \(N=s^j\) indices, left multiplication gives \(N\) isomorphic summands \(e_{aa}E_j\) of the right \(D_j\)-space \(E_j\).
Its dimension is positive and at most \([K:\mathbb Q]\), since a rational basis of \(K\) spans it over \(D_j\).
This yields the bound also for a nonnormal \(K\).

Set \(k'=K\cap D\) in the scalar copy inside \(U\).
In the Galois case, the primitive-element polynomial for \(K/k'\) is separable over the center of \(D_j\), so the Chinese remainder theorem and the preceding simplicity argument make \(B=D_j\otimes_{k'}K\) a finite product of simple rings.
For a primitive element \(\theta\), the matrix \((\sigma(\theta)^i)_{\sigma,\,0\le i<[K:k']}\) is invertible over the central complex scalars.
It recovers all coefficients \(d_i\in D_j\) from the evaluations of \(\sum_i d_i\otimes\theta^i\) in \(U(G^j)\).
Every simple factor \(eB\) therefore survives in some \(\pi_\sigma\), and \(\sigma(K)=K\) makes the image of every \(\pi_\sigma\) precisely \(E_j\).
The restriction to \(eB\) is an isomorphism onto \(\pi_\sigma(e)E_j\) that intertwines right multiplication by \(d\otimes1\) with right multiplication by \(d\).
Projecting the \(N\)-by-\(N\) matrix units onto this nonzero factor again gives diagonal sum equal to its identity and off-diagonal right-module isomorphisms.
Thus \(N\) divides the right \(D_j\)-dimension of every \(eB\), and their sum is \([K:k']\).
This proves the asserted divisibility without comparing individual matrix ranks under field automorphisms.

When \([K:k']\) is free of nontrivial \(j\)-th powers, divisibility forces \(s=1\).
In particular a squarefree Galois degree over \(\mathbb Q\) suffices when \(j=2\), since \([K:k']\) divides that degree.
The conclusion also gives integral kernel dimension by subtracting the rank from the number of columns.
The rational-power hypothesis and the coefficient restriction delimit this contribution to the [original complex-coefficient question](../../tasks/Yin_T_A0001_v1.md#contract).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0104_v1.md#statement) | Rational group-power hypothesis, simple Artinian scalar extension, denominator bound, Galois divisibility and integrality consequences. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0104_v1.md#argument) | Relative algebraic closure, simplicity, tracial ranks, commuting matrix units and right dimensions of the surviving Galois factors. |
| [Whole finding](#whole-finding) | [Coordinate embeddings](../../claims/Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings) | Subgroup restriction and commuting embeddings of the rational division closures in the affiliated product algebra. |
| [Whole finding](#whole-finding) | [Square test](../../claims/Yin_C_A0096_v2.md#the-square-test-for-a-scalar-affiliated-element) | A nonscalar rational affiliated element has no complex eigenvalue and all its scalar translates are units. |

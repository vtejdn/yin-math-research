---
author: Yin
---

# Alternating subgroup products bound the nullity of the nine-monomial matrix

## Statement

Consider a three-square monomial group-ring matrix whose coefficient moduli can be made equal to one by positive scalar row and column scalings.
Use the [first-row and first-column normalization](Yin_C_A0266_v3.md#the-only-three-row-pattern-left) to give it the form
\[
 H=\begin{pmatrix}
  1&1&1\\1&\lambda u&\mu v\\1&\sigma w&\theta z
 \end{pmatrix},\qquad
          |\lambda|=|\mu|=|\sigma|=|\theta|=1 .
\]
Let \(J_1=\langle u,v\rangle\) and \(J_2=\langle w,z\rangle\).
Assume \(u,v\) freely generate \(J_1\) and \(w,z\) freely generate \(J_2\).
For noninteger critical inputs under scalar injectivity these two free-pair conditions follow from the [two-row face test](Yin_C_A0273_v1.md#the-two-row-and-two-column-subgroups).

Let \(n\ge1\) be an integer.
Suppose that no product of \(2j\) alternating nonidentity elements of \(J_1,J_2\) equals the identity in the actual group for \(1\le j\le n\).
Then its regular nullity with the unnormalized matrix trace satisfies
\[
                           \dim_G\ker H\le\frac{1}{n+1}.
\]
For a choice of common first row, \(n=1\) requires just \(J_1\cap J_2=\{1\}\).
If also no alternating four-term product of nonidentity elements equals the identity, nullity is at most \(1/3\).
The assertion only restricts syllable length; the individual elements can be arbitrary words in their respective subgroups.
The same estimates apply after permuting the rows or taking the adjoint and renormalizing.

There is a version at length two with arbitrary nonzero moduli on the second and third rows.
Inside the two-dimensional constant kernel of the first row, take the projections \(P,Q\) onto the kernels of the second and third rows restricted to that space.
Let \(\overline P,\overline Q\) be their matrices of scalar group traces in any constant orthonormal basis there.
If \(J_1\cap J_2=\{1\}\), one has
\[
      \dim_G\ker H \le \operatorname{tr}_2(\overline P\,\overline Q).
\]
In particular the \(1/2\) bound at \(n=1\) only needs one of these two rows to have unit moduli in the normalized matrix.

## The scalar coefficient of each row projection

Let \(W=\{c\in\mathbb C^3:\sum c_i=0\}\), and identify \(W\otimes\ell^2(G)\) with two regular coordinates by a constant isometry.
The second-row projection \(P\) belongs to the two-square algebra over \(\mathcal N(J_1)\) there, and \(Q\) belongs to that over \(\mathcal N(J_2)\).
Both have unnormalized trace one.
Indeed in independent coordinates on \(W\) the second row is \((\lambda u-1,\mu v-1)\); its first entry is an affiliated unit by the bilateral shift of \(u\), giving row rank one.
The same reasoning applies to the third row at arbitrary nonzero moduli.
The kernel of \(H\) in these coordinates is the meet \(P\wedge Q\).

For a row of unit moduli, its trace matrix on \(W\) is exactly \(I_W/2\).
For the second row, twisting by a circle character of the free group on \(u,v\) removes the two phases and preserves its projection's entrywise traces.
Given any permutation of \(1,u,v\), normalize its first term by left multiplication by the inverse of that term.
The other two group elements are again a free basis of \(J_1\): interchanging \(u,v\), or passing to \(u^{-1},u^{-1}v\) on moving \(u\) to the first position, are invertible free basis changes; the same holds with \(u,v\) exchanged.
The induced automorphism preserves the canonical trace.
Thus permuting the three input coordinates preserves the trace matrix of the row-kernel projection inside the first-row kernel, since the first row is itself permutation invariant.
Extended by zero on \(W^\perp\), this trace matrix commutes with all coordinate permutations, so has one common diagonal entry and one common off-diagonal entry.
It is scalar on \(W\), and its trace one gives the value \(I_W/2\).

For arbitrary moduli and trivial subgroup intersection, the trace of any product \(ab\), \(a\in\mathcal N(J_1), b\in\mathcal N(J_2)\), equals \(\tau(a)\tau(b)\) by the group Fourier support and tracial Cauchy-Schwarz approximation.
Thus the unnormalized trace of \(PQ\) equals \(\operatorname{tr}_2(\overline P\,\overline Q)\).
The compression \(PQP\) dominates the meet, proving the length-two bound.
If either trace matrix is \(I_W/2\), the right side is \(1/2\).

## The moments up to the prescribed syllable length

Return to unit moduli on both rows and put \(U=2P-I_W,\ V=2Q-I_W\).
These are selfadjoint unitaries, and every entry has zero identity Fourier coefficient by the scalar calculation.
For \(1\le j\le n\) the normalized matrix trace of \((UV)^j\) is zero.
Indeed approximate \(U,V\) separately in their two-square subgroup algebras by uniformly bounded matrices of finite group-ring sums in the trace \(L^2\)-norm.
Kaplansky density in the reduced group \(C^*\)-algebra followed by norm approximation by group-ring matrices gives these approximants.
Subtract their matrices of identity coefficients, which tend to zero, to restore exact centering with a uniform bound.
For finite sums, each diagonal term in the matrix product is a linear combination of group elements that are products of \(2j\) alternating nonidentity letters from the two subgroups.
The syllable hypothesis makes each term have trace zero.
For the bounded limits, telescoping the \(2j\) factors and applying tracial Cauchy-Schwarz proves the same trace identity.
Negative moments through order \(n\) vanish by adjoints.

Write \(\delta\) for the unnormalized trace of \(P\wedge Q\).
The complementary meet \((I_W-P)\wedge(I_W-Q)\) also has trace \(\delta\), because the ambient unnormalized trace is two and both projections have trace one.
Both meets are fixed by \(UV\) and they are orthogonal.
Hence the trace of the fixed projection of \(UV\) is at least \(\delta\) when using the normalized two-square trace.
The positive operator
\[
               \frac{1}{(n+1)^2}
                   \left(\sum_{j=0}^n (UV)^j\right)^*
                   \left(\sum_{j=0}^n (UV)^j\right)
\]
acts as the identity on that projection.
Its normalized trace is \(1/(n+1)\) by the vanishing moments, and spectral calculus gives the desired estimate.

## Assessment history

### Decision truncated-moments-for-two-row-subgroups

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | Alternating moment vanishing and the equal complementary traces give the stated nullity bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [The scalar coefficient of each row projection](#the-scalar-coefficient-of-each-row-projection) | The action of all three coordinate permutations and the arbitrary-modulus trace bound. |
| argument | [The moments up to the prescribed syllable length](#the-moments-up-to-the-prescribed-syllable-length) | Finite-support approximation, complementary meets and the positive polynomial. |
| review | [Truncated moments for two row subgroups](../audits/reviews/Yin_R_A0209_v1.md#truncated-moments-for-two-row-subgroups) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-truncated-moments-for-two-row-subgroups)

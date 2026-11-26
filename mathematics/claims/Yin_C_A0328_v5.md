---
author: Yin
---

# A nonabelian solvable image gives a uniform gap at cyclic order sixteen with degrees one and six

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity, and suppose it has a cyclic quotient of order sixteen in which \(s,t\) have degrees \(1,6\).
If \(H'\ne H''\), every complex two-square rectangle \(K=B+At-s(D+Ct)\) of noninteger regular rank satisfies
\[
                          \dim_H\ker K\le 99/200 .
\]
The coordinate trace is unnormalized.
In particular a half kernel at this marking forces \(H_{\rm ab}=C_{16}\) and \(H'\) perfect, so every solvable image factors through that cyclic quotient.
Indeed \(H'\ne H''\) is equivalent to the existence of a nonabelian solvable image, using the actual quotient \(H/H''\) in one direction and preservation of perfectness under homomorphisms in the other.
The [two-label support-trace characterization](Yin_C_A0308_v1.md#statement) then gives the same \(99/200\) bound on the smaller support trace of a rank-one commutator output with ordinary input ranks at most two.
The perfect-commutator case remains open.

## Reduction at a fractional nullity above the threshold

Write \(\delta=\dim_H\ker K\) and suppose \(\delta>99/200\) is noninteger.
Scalar injectivity gives \(0<\delta<1\).
The [abelian short-vector estimate](Yin_C_A0198_v1.md#the-lattice-of-all-finite-characters) gives \(\delta\le2\sqrt{2/N}<99/200\) for a finite abelian quotient of order \(N\ge33\); the lifted integer maximum rank is necessarily two.
An infinite abelianization also gives such a quotient.
If the abelianization has order 32, the [boundary-order comparison](Yin_C_A0198_v1.md#the-two-boundary-orders) gives a lift with either \(4d<m\) or \(4d=m\) and both weights nonzero, where \(m\mid32\) is its exponent and \(d\) its width.
In the first case \(\delta\le2d/m\le1/2-1/m\) by integrality of \(4d,m\) and divisibility of \(m\) by sixteen in the present marking.
The [one-unit endpoint bound](Yin_C_A0197_v1.md#a-common-deficit-at-the-roots-of-unity) gives this last inequality also in the second case.
It follows that \(H_{\rm ab}=C_{16}\), since any proper finite cover has order at least 32.

Here are the exact quantitative interfaces needed from the previous reductions.
The [unequal column degrees and dihedral test](Yin_C_A0328_v1.md#statement) give \(B,C\) invertible, at least one of \(A,D\) invertible, and no nonabelian marked dihedral quotient: their largest threshold is \(11/24<99/200\).
The assembly is invertible by the four-column reduction, and neither \(A\) nor \(D\) is zero by the constant point correspondence argument in the [sixteenth-root rank estimate](Yin_C_A0328_v4.md#statement).
Since \(H_{\rm ab}=C_{16}\), every nonabelian dihedral quotient would have odd rotation order, with \(s\) a reflection and \(t\) generating rotations.
Thus [the splitting and sign-quotient proof](Yin_C_A0328_v1.md#two-dimensional-twists-and-the-sign-quotient) applies: \(M=H'/H''\) is finite of odd order and \(H/H''=M\rtimes C_{16}\), with marks \((0,s),(u,s^6)\), \(u\) a cyclic module generator.
In particular \(S=\operatorname{Ad}_s\) satisfies \(\Phi_4(S)\Phi_8(S)\Phi_{16}(S)=0\).

For \(M_\ell=M/\Phi_\ell(S)M\) at \(\ell=4,8,16\) the [half-turn approximation](Yin_C_A0328_v2.md#approximating-a-half-turn-by-an-actual-character) gives \(\delta\le3/8\) if \(|M_\ell|>(2\ell)^{\ell/2}\).
The [small fourth-root test](Yin_C_A0328_v2.md#all-small-fourth-root-modules) then gives \(\delta\le17/40\) if \(M_4\ne0\).
The [eighth-root estimates](Yin_C_A0328_v3.md#both-possible-missing-corners-at-the-remaining-178-markings) give \(\delta\le11/24\) if \(M_8\ne0\).
All these bounds require only the marked split quotient and the corner ranks already obtained, so neither application assumes that \(\delta\) is one half.
Thus \(M_4=M_8=0\); both corresponding endomorphisms of the finite group \(M\) are invertible.
Consequently \(S^8=-I,\ M=M_{16}\) and \(|M|\le2^{40}\).

If \(M\ne0\), take a prime divisor \(p\) and a simple \(\mathbb F_p[S]\)-quotient of \(M/pM\).
It is \(E=\mathbb F_p(\alpha)\), where \(\alpha\) represents the inverse action and is a primitive sixteenth root; \(p\) is odd, \(f=[E:\mathbb F_p]=\operatorname{ord}_{16}(p)\), and \(p^f\le2^{40}\).
The full split quotient gives a marked affine action on \(E\) with a nonzero second translation.
We next bound \(\delta\) for every such marked factor.

## A uniform large-prime estimate and the precise finite range

For \(p>49152\) apply the [cycle norm and local perturbation proof](Yin_C_A0328_v4.md#cycle-values-and-a-short-line-of-actual-characters), choosing in its eight-dimensional lattice the open \(\ell^1\)-ball of radius \(49/100\).
Its volume is \((49/50)^8/8!>1/p\) since \(49152\cdot49^8>8!\cdot50^8\).
Two points give a nonzero lattice vector of norm less than \(49/50\), whose reduction is a nonzero multiple of the selected character.
The total absolute weight over the sixteen coordinates is therefore less than \(2p(49/50)\).
All nonzero norm and hyperplane conditions already hold for \(p>40320\).
The [at-most-four local changes](Yin_C_A0328_v4.md#the-two-possible-reversal-counts) cost at most four units of rank since the possibly singular two-square corner has rank one.
Thus \(16p\delta<4p+2\cdot2p(49/50)\), giving \(\delta<99/200\).

It remains to check \(p\le49152\) and \(p^f\le2^{40}\).
The [native integer verifier](../computations/programs/Yin_J_A0010/verify_sixteenth_remainder.mjs) sieves all such odd primes and constructs all monic marked irreducible factors of \(X^8+1\).
It encodes a factor by the coefficients \(u_j\) in \(X^f=\sum_{j<f}u_jX^j\).
For every prime the program checks divisibility into \(X^8+1\), distinctness, and exactly \(8/f\) factors when the size condition holds, and zero otherwise.
This certifies irreducibility and completeness since every root is primitive of order sixteen and every Frobenius orbit has length \(f\).
For clarity, the construction uses the following cases, with congruences on \(p\) modulo sixteen.

* At \(p\equiv1\) take all odd powers of a primitive sixteenth root of the prime field.
* At \(p\equiv9\) the factors are \(X^2-d\) for the four primitive eighth roots \(d\).
* At \(p\equiv7,15\) let \(b=-1,1\), respectively.
  The quadratics are \(X^2-aX+b\) with \((a^2-2b)^2=2\), since the conjugate of a root \(\alpha\) is \(b/\alpha\).
* In degree four one only needs \(p\le1024\).
  At \(p\equiv3,11\) the factors are \(X^4-aX^2-1\), \(a^2=-2\), using the roots \(\alpha,-\alpha,\alpha^3,-\alpha^3\).
  At \(p\equiv5,13\) take \(X^4-d,\ d^2=-1\).

The resulting counts of marked factors of degrees \(1,2,4\) are \(5000,7512,180\), respectively.

## The 12692 finite certificates with a possible singular corner

The coefficients \(u_j\) give the recurrence \(e_{i+f}=\sum_{j<f}u_j e_{i+j}\) modulo \(p\).
Any \(f\) initial coordinates are available from a linear functional on the power basis of \(E\), so the sixteen resulting coordinates are values of a single genuine character on \(\alpha^i\).
They satisfy \(e_{i+8}=-e_i\).
As in [the cyclic induced representation](Yin_C_A0328_v3.md#the-complete-interval-test-in-eight-coordinates), at every \(z^{16p}=1\) there are edges \(i\to i+1,\ i\to i+6\) carrying the original translations \(s,t\) and respective scalar exponents \(ap,b_i\) with
\[
                            b_i\equiv6ap+16e_i\bmod16p .
\]
These are the tensor of the cyclic character at \(z^p\) and the affine representation at \(z^{16}\).
The translation generator and cyclic shift are absorbed in the functional by a nonzero field multiplier.
The verifier takes centered representatives of the \(b_i\), allowing one extra period of either sign at site zero.

For a fixed choice let \(L,U\) be the minimum and maximum costs of the 2912 pairs of matching edge sets.
They are recovered from \(m_i-m_{i-1}=n_{i-6}-n_i\) as in the [circulation enumeration](Yin_C_A0328_v4.md#the-two-possible-reversal-counts).
The verifier checks a unique minimizing edge set pair; its complement is the unique maximizing pair, with \(U+L\) the cost of all edges.
Let \(q\) be the smaller number of straight-through sites using just the first or just the second edges in that minimum.
This is the smaller of the two possible counts at which the missing corner would be required when using the minimum or the maximum.
For each marked factor the retained witness satisfies the integer inequality
\[
                         25\big(2(U-L)+16p q\big)\le198(16p).
\]

Choose the end needing at most \(q\) local replacements, depending on whether \(A\) or \(D\) is singular.
Its one-input sites use precisely the indicated matched corners, while its two-input sites use the full assembly up to translations and permutations.
For example an \(A\) singleton has its second edge entering and its first edge absent on exit, and the single-input and single-output counts then force the two second edges to be used and both first edges absent.
The analogous \(D\) case has both first edges used and both second edges absent.
Replacing the deficient corner by an invertible rank-one perturbation at just the needed sites thus gives an injective endpoint by the [unique matched edge sets](Yin_C_A0293_v1.md#invertibility-when-the-extremum-has-unique-edge-sets).
As in the [local perturbation bound](Yin_C_A0328_v4.md#full-rank-of-the-modified-endpoint), its cost at each true root is at most \(q\) units of rank.
Consequently
\[
                        16(16p)\delta\le 2(U-L)+16p q ,
\]
giving \(\delta\le99/200\).

For 12690 factors the verifier finds a witness on one of the first twenty nonzero multiples, restricted to multipliers below \(p\), of the functional with initial values \((1,\ldots,f)\bmod p\).
It tests \(a=0,1,2,3,5\) and the three choices of the extra period at zero.
The remaining factor at \(p=3\) is \(X^4-2X^2-1\); the initial values \((0,1,1,0)\) and \(a=1\) give spread 176 and \(q=0\).
The remaining factor at \(p=13\) is \(X^4-5\); the initial values \((9,1,0,0)\) and \(a=2\) give spread 720 and \(q=0\).
Neither needs an extra period.
The optional witness output supplies the individual finite parameters, costs and repair count for every marked factor.
All finite and infinite prime cases contradict \(\delta>99/200\) when \(M\ne0\).
This proves the gap and the perfectness assertion at a half kernel.

## Assessment history

### Decision the-full-solvable-image-gap-at-order-sixteen

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:52 |
| status | proved |
| reason | The large-prime volume margin and the complete finite certificates give a uniform bound of ninety-nine two-hundredths in the nonperfect case. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The uniform group and commutator support bounds. |
| argument | [Reduction at a fractional nullity above the threshold](#reduction-at-a-fractional-nullity-above-the-threshold) | The larger abelianization and earlier quantitative reductions. |
| argument | [A uniform large-prime estimate and the precise finite range](#a-uniform-large-prime-estimate-and-the-precise-finite-range) | The volume margin and complete cyclotomic factors. |
| argument | [The 12692 finite certificates with a possible singular corner](#the-12692-finite-certificates-with-a-possible-singular-corner) | The actual phase estimates and the individual finite witnesses. |
| dependency | [Large-prime rank bound](Yin_C_A0328_v4.md#statement) | The preceding large-prime theorem and its finite cycle computation. |
| review | [Large primes and singular sites at order sixteen](../audits/reviews/Yin_R_A0231_v1.md#large-primes-and-singular-sites-at-order-sixteen) | Independent review of the preceding argument. |
| review | [The full solvable-image gap at order sixteen](../audits/reviews/Yin_R_A0231_v1.md#the-full-solvable-image-gap-at-order-sixteen) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-full-solvable-image-gap-at-order-sixteen)

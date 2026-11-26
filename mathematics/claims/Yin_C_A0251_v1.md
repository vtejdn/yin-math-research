---
author: Yin
---

# Four remaining prime divisors of the commutator abelianization at order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity.
Suppose there is a four-site matrix of regular rank \(3/2\) and an abelian quotient of order 24.
Use the [normalized marking](Yin_C_A0241_v1.md#statement) of \(H_{\rm ab}=C_{24}\), the commutator abelianization \(M=H'/H''\), \(S=\operatorname{Ad}_{ts^{-1}}\) on \(M\), and \(M_r=M/\Phi_r(S)M\).
Then \(M_3\) is trivial or the additive group of \(\mathbb F_4\), and \(|M_{24}|\) divides either 64 or 25.
Consequently
\[
 |M|\le159744,\qquad p\mid |M|\ \Longrightarrow\ p\in\{2,3,5,13\}
 \quad\text{for every prime }p.
\]
The bounds leave open the half-rank problem at this marking.

## The three-cycle bound on the whole integral quotient

Let \(L(y)=(Ay+B)(Cy+D)^{-1}\) be the rational transfer.
The denominators and numerators have nonmonomial determinants, and at least one of \(C,D\) is invertible, by the [four-step spectral idempotent argument](Yin_C_A0245_v1.md#two-fourier-blocks-of-the-rational-transfer).
On \(M_3\) the map \(1-S^4=1-S\) is invertible.
The [pure rotation construction](Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group) therefore already applies on \(M_3\) itself.
In its metabelian quotient \(t\) is the fourth power of the chosen cyclic generator and \(s\) has degree three with translation part generating \(M_3\) as a module.
Use three auxiliary channels and the associated genuine characters.
As in the [three-block calculation](Yin_C_A0245_v1.md#a-coefficient-with-three-ordered-factors), the four-step identity after removing its rightmost invertible block equates a finite character sum to a constant matrix.
For a path \((i_1,i_2,i_3,i_4)\) its frequency, up to sign, is \((\sum_j S^{-i_j})v\) for a cyclic generator \(v\).
The transition \(i\mapsto i+4k-3\) carries \(s^{-1}E_k(t)\), where \(E_k\) is the \(k\)-th Fourier component of \(L\) under rotation by a cube root of unity.

If \(D\) is invertible, \(E_1\) is a rational unit and \(E_0\ne0\), since \(E_0(0)=BD^{-1}\ne0\).
For invertible \(C\) the reversed rational function gives the same statements for \(E_2\) and for \(E_0\) at infinity, using \(AC^{-1}\ne0\).
Choose the path \((0,1,1,2)\) in the first case and \((0,2,2,1)\) in the second.
The nonzero middle block is between two affiliated units in either path.
Their product is nonzero.
The path frequency must therefore be zero or equal to that of another path between the same endpoints.
Each middle index has three possibilities.
The [integer verifier](../computations/programs/Yin_J_A0010/verify_small_collisions.py) obtains absolute norm \(1,3,9\) or \(12\) for the selected frequency polynomial and its differences from those of the other eight paths in \(\mathbb Z[X]/\Phi_3\).
Since \(v\) generates \(M_3\), the [integral norm divisibility argument](Yin_C_A0241_v1.md#the-norm-of-the-resulting-relation) shows that \(|M_3|\) divides one of these integers.
It also divides one of \(1,4,7,16\) by the earlier four-term bound.
Hence it divides four.
Modulo two \(\Phi_3=X^2+X+1\) is irreducible, excluding a one-dimensional quotient \(M_3/2M_3\).
This gives the claimed abelian group alternatives.

## Frequency comparison on the twenty-fourth simple factors

By the [order-24 bound](Yin_C_A0241_v1.md#statement) it is enough to remove characteristics \(7,73,97,193\) among the possible prime divisors of \(M_{24}\).
A prime divisor \(p\) supplies a simple quotient of \(M_{24}/pM_{24}\).
At these primes \(p\nmid24\), so this quotient is the additive field \(\mathbb F_p(\alpha)\) with \(S\) acting by a primitive twenty-fourth root \(\alpha\).
Use the same pure rotation construction in 24 channels: \(1-S^4\) is an automorphism and the orbit frequency is evaluated at a nonzero generator of this field module.
Now \(P^4\) has six-cycles, so the six transitions carry \(s^{-1}E_k(t)\) for the Fourier classes of \(L\) modulo six.

Suppose first that \(D\) is invertible and put \(T=D^{-1}C,\ V=A-BD^{-1}C\).
The expansion \(L(y)=BD^{-1}+Vy(I+yT)^{-1}D^{-1}\) gives for \(1\le k\le5\)
\[
              E_k(y)=(-1)^{k-1}Vy^kT^{k-1}(I-y^6T^6)^{-1}D^{-1}.
\]
Here \(V\) is invertible.
Also \(T\) has a nonzero eigenvalue, since otherwise \(\det(Cy+D)=\det D\) would be a monomial.
Thus \(E_1(t)\) is an affiliated unit and the other four displayed blocks are nonzero.
If \(C\) is invertible, apply the same argument to \(L(y^{-1})\): \(E_5(t)\) is then a unit and the other four are nonzero.
This uses only cyclic rational evaluation at the infinite-order \(t\).

Start at \(i_1=0\).
Choose three transitions \(i_{j+1}=i_j+4k_j-3\bmod24\) with \(k_j\in\{1,\ldots,5\}\), at least two indices equal to the available unit block \(1\) or \(5\).
The chosen ordered product is nonzero as it contains two units and one nonzero block.
For fixed endpoints each of the two middle indices ranges over six positions in its residue class modulo four.
The [exact marking check](../computations/programs/Yin_J_A0010/readme.md#three-step-frequencies-at-orders-three-and-twenty-four) finds a triple for which \(\sum_j\alpha^{-i_j}\ne0\) and its value differs from those of all 35 other middle choices.
It verifies both choices of unit block on each irreducible factor: four quadratics at \(7\), and eight linear factors at each of \(73,97,193\).
Polynomial multiplication recovers all of \(\Phi_{24}\bmod p\), and the checked degrees are the Frobenius orders.
A nonzero isolated coefficient contradicts the identity on the full dual of the simple quotient.
This excludes these four primes for every permissible marking.

At \(p=5\) all four quadratic factors instead fail this isolation test even if \(k_j=0\) is allowed and the unit-block restriction is removed.
The enumerated initial index zero suffices for that statement because translating every index multiplies all frequencies by the same unit.
This failure leaves the characteristic open.
Removing the four excluded primes from the earlier divisibility list makes \(|M_{24}|\) a divisor of \(64\) or \(25\).
Finally, the [bounds on \(M_2,M_4\)](Yin_C_A0249_v1.md#statement), the vanishing of \(M_8\), and the [sixth and twelfth quotient bounds and partial-product filtration](Yin_C_A0245_v1.md#the-integral-orders-and-the-finite-commutator-abelianization) give \(3\cdot4\cdot13\cdot4\cdot1\cdot4\cdot64=159744\) and the stated prime support.

## Assessment history

### Decision the-remaining-primes-and-path-frequencies

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:32 |
| status | proved |
| reason | Independent whole-proof inspection verified the stated bounds, hypotheses and argument at the indicated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The reduced third quotient and the four possible prime divisors of the full module. |
| argument | [The three-cycle bound on the whole integral quotient](#the-three-cycle-bound-on-the-whole-integral-quotient) | Both nonzero triple products and their nine possible comparisons. |
| argument | [Frequency comparison on the twenty-fourth simple factors](#frequency-comparison-on-the-twenty-fourth-simple-factors) | All primitive factors, unit blocks and the final filtration bound. |
| review | [The remaining primes and path frequencies](../audits/reviews/Yin_R_A0202_v1.md#the-remaining-primes-and-path-frequencies) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-remaining-primes-and-path-frequencies)

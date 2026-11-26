---
author: Yin
---

# Comparing the two squares of the order-four transfer at cyclic order twenty-four

## Statement

Suppose \(H=\langle s,t\rangle\) is torsion-free with regular group-ring scalar injectivity, has an abelian quotient of order 24, and admits a two-by-two four-site matrix of regular rank \(3/2\).
Use the [normalized marking](Yin_C_A0241_v1.md#statement) \(H_{\rm ab}=C_{24}\) with degrees \(3,4\).
Write \(M=H'/H''\), \(S=\operatorname{Ad}_{ts^{-1}}\) on \(M\), and \(M_r=M/\Phi_r(S)M\).
Then
\[
                 M_3=M_{12}=M_{24}=0,\qquad
                 |M|\mid |M_2|\,|M_4|\,|M_6|,\qquad |M|\le117 .
\]
In particular \(M\) is of odd order, with prime divisors among \(3,5,13\).
The result excludes all four primitive twenty-fourth cyclotomic markings in characteristic five.
It still allows a fifth-order contribution at the fourth cyclotomic quotient.

## A two-step coefficient on each side

By the [four-step identity](Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group), \(J=(s^{-1}I_2)L(t)\) satisfies \(J^4=I_2\), where \(L(y)=(Ay+B)(Cy+D)^{-1}\).
Use the pure rotation representations from that calculation on the whole cyclic module \(M_3\), or on a simple quotient of \(M_{24}\) in characteristic five.
On \(r=3\) or 24 channels the cyclic generator acts as the forward permutation \(P\), the image of \(t\) is \(P^4\), and the phase on a translation at channel \(i\) is a character evaluated on \(S^{-i}\) of that translation.
In both cases the necessary \(1-S^4\) is invertible.
In the normal form of the inverse \(s\)-translation, the fixed factor \(v\) in the character is a cyclic generator of the chosen module.

For every character \(\psi\) of that module the absorbed transfer is \(T_\psi=\Delta_\psi W\) with
\[
       (\Delta_\psi)_{ii}=\psi(-S^{-i}v)I_2,\qquad
       W=(P^{-3}\otimes s^{-1})\,L(P^4\otimes t).
\]
The affiliated matrix \(W\) is independent of \(\psi\) and invertible.
Since \(T_\psi^4=I\), one has the identity
\[
                 \Delta_\psi W\Delta_\psi W
                    = W^{-1}\Delta_\psi^{-1}W^{-1}\Delta_\psi^{-1}.
\]
All inverses here are in the actual regular affiliated algebra; in particular the cyclic rational denominators are evaluated on finitely many rotations of the infinite-order \(t\).

Fix input 0 and output \(h\).
A forward path through \(j\) contributes the character of \(-(S^{-h}+S^{-j})v\), with coefficient \(W_{h,j}W_{j,0}\).
A reverse path through \(l\) contributes the character of \((1+S^{-l})v\).
On the reverse side \(W^{-1}=L(P^4\otimes t)^{-1}(P^3\otimes s)\), so \(l\equiv3\bmod\gcd(4,r)\).
The forward indices satisfy \(j\equiv-3\bmod\gcd(4,r)\).
Comparing characters on the whole dual is legitimate for these finite sums with coefficients in a complex vector space of affiliated matrices.
If the chosen forward coefficient is nonzero, then either its frequency agrees with that of another forward path, or for some reverse index \(l\) one has
\[
                         (1+S^{-j}+S^{-h}+S^{-l})v=0 .
\]

Let \(E_k(t)\) denote the Fourier block of \(L(t)\) for index \(k\) modulo the order of \(P^4\).
A forward step \(i\mapsto i+4k-3\) carries \(s^{-1}E_k(t)\).
If \(D\) is invertible then \(E_1(t)\) is an affiliated unit; if \(C\) is invertible its inverse-parameter counterpart \(E_{-1}(t)\) is an affiliated unit.
These alternatives follow from the [three-cycle calculation](Yin_C_A0245_v1.md#two-fourier-blocks-of-the-rational-transfer) and [six-cycle formula](Yin_C_A0251_v1.md#frequency-comparison-on-the-twenty-fourth-simple-factors), respectively at the two cycle lengths.
At least one of \(C,D\) is invertible in the putative half-rank input.
We use two consecutive steps of an available unit block, so the forward coefficient is itself an affiliated unit.

## Eliminating the third cyclotomic quotient

Suppose \(M_3\ne0\).
By the [three-cycle bound](Yin_C_A0251_v1.md#the-three-cycle-bound-on-the-whole-integral-quotient) it is additively \(\mathbb F_4\), with \(S\) acting by a primitive cube root.
At \(r=3\) the two-step path is \(0,1,2\) for the forward unit block or \(0,2,1\) for the inverse-parameter unit block.
Its frequency differs from each other forward frequency since the three orbit elements \(S^{-j}v\) are distinct.
Moreover \(1+S^{-j}+S^{-h}=0\) as an endomorphism, because the three indices \(0,j,h\) are \(0,1,2\) in some order.
Thus each possible reverse comparison leaves the nonzero element \(S^{-l}v\).
This contradicts the character identity, proving \(M_3=0\).

The finite group \(M\) has \(S^{24}=I\) and \(S-I\) invertible.
On \(M/2M\) the polynomial \(X^{24}-1\) is \((X-1)^8\Phi_3(X)^8\), while \(\Phi_3(S)\) is surjective because \(M_3=0\).
Surjectivity on this quotient makes both \(S-I\) and \(\Phi_3(S)\) invertible there.
Their product cannot have zero eighth power on a nonzero module.
Hence \(M/2M=0\), so \(M\) has odd order.

## The four quadratic factors in characteristic five

If \(M_{24}\ne0\), the [previous divisor bound](Yin_C_A0251_v1.md#statement) and oddness now force its order to divide 25.
A simple quotient in characteristic five identifies with \(\mathbb F_{25}\) on which \(S\) acts by a primitive twenty-fourth root \(\alpha\); all primitive roots have Frobenius degree two.
Let \(b=1\) for the unit block \(E_1\) and \(b=17\) for \(E_5\).
Two successive transitions use the path \(0,b,2b\bmod24\).
Indeed \(4\cdot1-3=1\) and \(4\cdot5-3=17\).
All possible forward middle indices give different frequencies, since the powers of \(\alpha\) at distinct indices modulo 24 are distinct and \(v\ne0\).

Set \(a=\alpha^{-b}\), another primitive twenty-fourth root, with \(b\equiv1\bmod4\).
The reverse comparison would require
\[
                        -(1+a+a^2)\in a^3\langle a^4\rangle ,
\]
since \(l\equiv3\bmod4\) and \(\alpha^{-l}\) lies in the indicated coset.
Put \(u=a^6=\operatorname{Nm}_{\mathbb F_{25}/\mathbb F_5}(a)\), \(y=a+a^5\).
The element \(u\) has order four, so \(u^2=-1\).
Every element of \(\langle a^4\rangle\) has norm one.
Taking norms in the displayed condition and using \(\operatorname{Nm}(-1)=1\) therefore gives
\[
       y^2+(1+u)y+1-u+u^2
         =\operatorname{Nm}(1+a+a^2)=u^3 .
\]
Expansion against the conjugate \(a^5\) gives the first identity.
Using \(u^2=-1\) leaves \(y(y+1+u)=0\).
If \(y=0\), then \(a^5=-a\), so \(a^4=-1\), impossible since \(a^4\) has order six.
If \(y=-1-u\), the polynomial of \(a\) over \(\mathbb F_5\) is \(X^2+(1+u)X+u=(X+1)(X+u)\), contradicting its degree two.
This excludes every reverse comparison.
The nonzero forward coefficient again contradicts the identity; hence \(M_{24}=0\).

Finally \(M_{12}\) was known to be a 2-group and \(M_8=0\).
By oddness and [the bounds for \(M_6,M_{12}\)](Yin_C_A0245_v1.md#statement), \(M_{12}=0\) and \(|M_6|\le3\).
The [bounds for \(M_2,M_4\)](Yin_C_A0249_v1.md#statement) and the partial-product filtration of \(M\) give the divisibility in the statement and \(|M|\le3\cdot13\cdot3=117\).

## Assessment history

### Decision the-order-four-transfer-compared-with-its-inverse

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:10 |
| status | proved |
| reason | Independent proof inspection verified the frequency signs, cyclotomic eliminations, integral divisibility and finite-field contradiction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Odd order, the vanishing quotients and the bound 117. |
| argument | [A two-step coefficient on each side](#a-two-step-coefficient-on-each-side) | Forward and reverse frequencies and the unit two-step path. |
| argument | [Eliminating the third cyclotomic quotient](#eliminating-the-third-cyclotomic-quotient) | All possible collisions and the resulting vanishing of the binary part of the full module. |
| argument | [The four quadratic factors in characteristic five](#the-four-quadratic-factors-in-characteristic-five) | The finite-field norm and exclusion of every primitive marking. |
| review | [The order-four transfer compared with its inverse](../audits/reviews/Yin_R_A0205_v1.md#the-order-four-transfer-compared-with-its-inverse) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-order-four-transfer-compared-with-its-inverse)

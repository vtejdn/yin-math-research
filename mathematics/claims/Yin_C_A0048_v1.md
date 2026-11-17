---
author: Yin
---
# How a cyclic tower constrains the two surviving four-class masks

## Statement

Let \(G\) be a group, and let \(a,b\in\mathbb F_2[G]\) be nonzero finite sums with \(ab=0\).
Suppose a homomorphism \(\chi:G\to C_7\) gives four odd classes on each factor, as in the [exceptional quotient table](../ledger/Yin_L_A0046_v1.md#complete-fibers-with-arbitrary-positive-odd-multiplicities).
No restriction is needed on the branches of the two supports with even cardinalities.
If \(\chi\) lifts along reduction to \(G\to C_{7^k}\), then
\[
       |\operatorname{supp}a|\,|\operatorname{supp}b|
                             \ \ge\ 16\cdot 7^{\,k-1}.                   \tag{1}
\]
The cardinalities on the left count distinct surviving group labels.
In particular the specified character cannot lift to an integral character.
If \(G\) is finitely generated it must be nonzero on the \(7\)-primary torsion of \(G_{\mathrm{ab}}\).
For any supplied finite presentation and character, every fixed-depth lifting assumption in (1) can be tested by linear congruences.

There is also a test in an individual color one seeks to erase.
At any attainable lift, an odd number of vertex occurrences in a refined class above that color rules out its erasure in the actual group.
The growth test below applies at every level simultaneously and distinguishes the two primitive Fourier orbits at that level.
It gives a stronger factor of nine at a level where both factors vanish on exactly one of the two opposite primitive orbits.
The unconditional factor seven in (1) is sharp for zero products in the finite cyclic quotient itself.

## Primitive roots and the branching bound

For \(1\le j\le k\) let \(a_j,b_j\in\mathbb F_2[C_{7^j}]\) be the projected factors.
Their supports count the odd classes among the multiplicities of the original labels.
Further reduction to level one is nonzero on both, and \(a_jb_j=0\).
Realize this ring as \(\mathbb F_2[X]/(X^{7^j}-1)\).

Put \(m=7^{j-1}\).
The order of 2 modulo \(7^j\) is \(3m\).
Indeed its order modulo seven is three, \(2^3-1=7\), and if \(7\mid u\), expansion of \((1+u)^7-1\) increases its \(7\)-adic valuation by exactly one.
Raising \(1+u\) to an exponent coprime to seven preserves that valuation.
Thus the primitive \(7^j\)-th roots over \(\mathbb F_2\) split into two Frobenius orbits of size \(3m\).
For a primitive root \(\zeta\) put \(\omega=\zeta^m\).
Then \(\mathbb F_2(\omega)=\mathbb F_8\) and \(\zeta\) has degree \(m\) over this subfield.
The two primitive orbits project under the \(m\)-th power map onto the two distinct cubic orbits for seventh roots: the fibers of each cubic orbit together have exactly \(3m\) elements.

Write either factor \(u_j\) uniquely in the form
\[
            u_j(X)=\sum_{s=0}^{m-1}X^s P_s(X^m),\qquad \deg P_s<7.
\]
Its coefficient in class \(s\) at level \(j-1\) is \(P_s(1)\).
If \(u_j(\zeta)=0\), independence of \(1,\zeta,\ldots,\zeta^{m-1}\) over \(\mathbb F_8\) implies \(P_s(\omega)=0\) for every \(s\).
An odd parent has \(P_s(1)=1\), so \(P_s\) has odd weight.
One term cannot vanish at a seventh root.
An odd parent therefore has at least three odd children when \(u_j\) vanishes on one primitive orbit.
If it vanishes on both, \(P_s\) is divisible by both coprime cubic factors of \(1+Y+\cdots+Y^6\).
Since it has degree at most six and is nonzero, it must be exactly this polynomial and all seven children are odd.
With neither orbit killed, an odd parent still has at least one odd child.

At each level \(j\ge2\) every primitive orbit is killed by at least one factor because \(a_jb_j=0\) and evaluation takes values in a field.
Denote the two numbers of killed orbits by \(e_a,e_b\in\{0,1,2\}\), so \(e_a+e_b\ge2\).
Each side's support grows over its odd parents by at least \(d(e)\), with \(d(0)=1,d(1)=3,d(2)=7\).
The product of the two growth factors is at least seven, and is nine if \(e_a=e_b=1\).
Even parents can only contribute additional surviving children.
The initial support product is sixteen and the original supports dominate the final projected ones, proving (1).
An integral lift would give lifts of every depth.
In a finitely generated abelian group, a mod-seven character vanishing on the torsion subgroup lifts integrally by choosing lifts on a free basis.
Only its \(7\)-primary torsion can contribute to a map to \(C_7\), proving the torsion assertion.

## Application to labels and its limit

For a supplied Ope26f matching tuple, impose the signed fundamental-loop equations on the letter values modulo \(7^k\), with their given values prescribed modulo seven.
These are exactly the relations of the abelianized graph presentation used in the [spanning forest test](Yin_C_A0043_v1.md#what-a-supplied-matching-instance-would-determine).
Each solution permits transporting the vertices to the refined classes, reversing the second factor's path labels.
If all original group labels in a color have even multiplicity, their counts remain even in every refined class above it, because equal group elements have equal images.
An odd refined class proves non-erasure and needs no decision of equality of two arbitrary group words.
Even when all refined counts in the color are even, some original group labels might still survive.
For a tuple with \(n\) vertices per side, the two original support sizes are at most \(n\); hence \(16\cdot 7^{k-1}>n^2\) and a verified lift to depth \(k\) exclude the desired two parity masks outright.

For the sharp quotient calculation, in \(C_{7^k}\) let \(N\) be the kernel of reduction to \(C_7\) and let \(T_N=\sum_{h\in N}h\).
For \(D=\{0,1,2,4\}\) take arbitrary representatives of \(D,-D\) in \(C_{7^k}\) and their indicator sums \(u,v\).
The product \((T_N u)v\) vanishes over \(\mathbb F_2\): translation of \(T_N\) depends only on the residue modulo seven, and the product counts of \(D,-D\) are \(4,2,2,2,2,2,2\).
The two supports have sizes \(4\cdot7^{k-1}\) and four, and the odd order of \(N\) preserves both parity masks under reduction.
Thus the bound on finite quotient data alone allows the pattern at any prescribed finite depth when enough labels are available.
This finite example does not impose equalities of labels in an Ope26f group.

## Assessment history

### Decision cyclic-tower-support-bound

| Field | Value |
| --- | --- |
| date | 2026-11-17T08:44 |
| status | proved |
| reason | The review checked the primitive-root branching factors, sharpness, the abelianization test and its limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Growth of odd fibers along a seven-power tower and the resulting restriction on lifting the cyclic character. |
| argument | [Proof](#primitive-roots-and-the-branching-bound) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0079_v1.md#whole-argument-finding) | Review of the entire argument with its stated dependencies. |

## Current assessment

[Selected decision](#decision-cyclic-tower-support-bound)

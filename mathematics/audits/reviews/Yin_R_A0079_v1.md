---
author: Yin
---

# Growth of odd support classes in a tower of cyclic quotients

A separate reviewing agent checked fixed C_A0048_v1 for Yin on 2026-11-17T00:33 UTC.
The reviewer had checked the earlier seven-color arithmetic classification and its explicit quotient fibers but did not develop the tower argument.
No C_A0048 development discussion, author explanation or prior verdict was received or consulted before this inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0048_v1.md#statement) | Product growth from the four odd classes, integral-lift obstruction, abelianization condition and refined-color non-erasure. |
| [Whole-argument finding](#whole-argument-finding) | [Primitive roots and branching](../../claims/Yin_C_A0048_v1.md#primitive-roots-and-the-branching-bound) | Order of two, Frobenius orbits, coefficient independence and both the unconditional and split-orbit growth factors. |
| [Whole-argument finding](#whole-argument-finding) | [Application and sharpness](../../claims/Yin_C_A0048_v1.md#application-to-labels-and-its-limit) | Word-congruence test, support and occurrence parity, size cutoff and the finite quotient attaining equality. |
| [Whole-argument finding](#whole-argument-finding) | [Seven-fiber table](../../ledger/Yin_L_A0046_v1.md#complete-fibers-with-arbitrary-positive-odd-multiplicities) | Four odd labels per side initially and explicit product counts of \(D,-D\) for sharpness. |
| [Whole-argument finding](#whole-argument-finding) | [Matching presentation test](../../claims/Yin_C_A0043_v1.md#what-a-supplied-matching-instance-would-determine) | Abelianized fundamental loops and quotient colors of path labels for an actual tuple. |

## Whole-argument finding

Since \(\operatorname{ord}_{7}(2)=3\) and \(v_7(2^3-1)=1\), expanding successive seventh powers gives \(\operatorname{ord}_{7^j}(2)=3\cdot7^{j-1}\).
There are \(6\cdot7^{j-1}\) primitive roots, forming exactly two Frobenius orbits.
For \(m=7^{j-1}\) each orbit maps under the \(m\)-th power to the corresponding orbit at order seven.
The \(m\) lifts of each primitive seventh root all have order \(7^j\), so each cubic orbit has exactly \(3m\) such lifts.
For \(\omega=\zeta^m\), the degree ratio over \(\mathbb F_2(\omega)\) is \(m\), and the first \(m\) powers of \(\zeta\) are a basis.

Writing the coefficient array in residue columns \(s+mi\), evaluation at \(\zeta\) therefore forces each seven-entry column polynomial to vanish at \(\omega\) independently when the whole factor kills this orbit.
Evaluation of that column at one gives its parent parity under reduction modulo \(m\).
An odd column vanishing at one cubic orbit has weight at least three.
If it vanishes at both, it is the unique nonzero multiple of the product of the two cubics of degree at most six, namely \(1+X+\cdots+X^6\).
These facts give the three lower bounds \(1,3,7\).
Vanishing of the product at each primitive orbit requires at least one factor to kill it.
An assignment of one orbit to each factor gives a product growth factor at least nine; if one factor kills both, the bound is at least seven.
The disjoint child sets above the odd parent classes already give these lower bounds, and even parent classes can only add support.

Induction from the known level-one product cardinality \(16\) gives \(16\cdot7^{k-1}\).
Each odd projected class has at least one distinct original support element, so the inequality also holds for the original finite supports.
An integral character lift contradicts these bounds at unbounded depth.
For a finitely generated abelianization, vanishing on its \(7\)-primary torsion would give vanishing on the whole torsion subgroup and allow integral lifts of the values on a free basis, proving the stated implication.
Congruences on a supplied finite presentation characterize lifts at each fixed depth.
An odd refined occurrence class forces a surviving original label because every group-label equality refines to a single class at the higher level.
Even refined counts alone do not establish erasure.

In the cyclic sharpness example the \(N\)-translate of each representative fills a disjoint coset of size \(7^{k-1}\), and reducing its parity to level one retains the original label because that size is odd.
The other factor has exactly four support positions.
For the product, multiplication by \(T_N\) sends every term in a given level-one class to the same coset sum and the seven printed multiplicities are even.
This proves vanishing at every depth and attains the bound there.
Direct binary convolution at orders \(7,49,343\) also gives zero with respective support sizes \((4,4),(28,4),(196,4)\).
The finite cyclic groups only establish sharpness of the quotient bound, and no implication about actual vertex equalities or a torsion-free counterexample is drawn.
The proof supports all stated conclusions.

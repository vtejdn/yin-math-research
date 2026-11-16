---
author: Yin
---
# A cubic obstruction to cancellation in a three-representation product fiber

## Statement

Let \(A,B\) be finite nonempty subsets of a group. Work over the complex numbers with **nonzero** coefficients on every point of \(A,B\).
Write \(v_{xy}=e_x+e_y\) in the integer lattice on the disjoint union of row and column labels.
For each element with exactly two representations \(xy=x'y'\) choose either orientation and include \(v_{xy}-v_{x'y'}\) as a generator of \(L_2\).
Write \(S=(L_2\otimes\mathbb Q)\cap\mathbb Z^{A\sqcup B}\).

Consider one actual product with exactly three representations and corresponding vectors \(v_0,v_1,v_2\). Suppose \(v_1-v_0,v_2-v_0\in S\).
If the group-ring product vanishes, the order of **each** \(v_i-v_j,\ i\ne j\), in the finite group \(S/L_2\) is divisible by three.
In particular, a single such triple rules out all complex zero products on these supports if \(3\nmid[S:L_2]\).
This applies to arbitrary lengths of the four Laurent rows and columns in the [four-coset setting](Yin_C_A0020_v1.md#statement); the triples count actual group-element products.

For a fiber of any odd cardinality, suppose all within-fiber differences lie in \(S\) and their images in \(S/L_2\) have orders that are powers of two, allowing order one.
Then no complex coefficient choice with these supports gives zero product.

If every actual fiber has two or three representations and every triple satisfies the saturation hypothesis above, a finite system of integral congruences below decides the existence of a zero product on those supports.

## Argument

A coefficient choice is a character \(z:\mathbb Z^{A\sqcup B}\to\mathbb C^\times\) with \(z(v_{xy})=a_x b_y\).
A two-term fiber equation forces \(z(d)=-1\) on its chosen difference \(d\).
Thus \(z(L_2)\subseteq\{1,-1\}\).
For \(d\in S\) of order \(m\) modulo \(L_2\), one has \(z(d)^{2m}=1\). In particular \(|z(d)|=1\).

Dividing the three-term equation by its first term gives \(1+\xi+\eta=0\) with \(|\xi|=|\eta|=1\).
Then \(|1+\xi|=1\) gives \(\Re\xi=-1/2\), so \(\xi,\eta\) are the two distinct primitive cube roots of unity.
Their ratio is also a primitive cube root.
Hence \(3\mid 2m\) for each within-triple difference, proving the first assertion.

In the odd fiber of the second assertion, divide by one term.
All resulting terms are powers of a common primitive \(2^s\)-th root, taking \(s\ge1\).
Writing a sum of these powers as a polynomial \(F\) with nonnegative integer coefficients gives \(F(1)\) equal to the odd number of terms, counting repetitions.
If the sum vanished, the monic cyclotomic polynomial \(X^{2^{s-1}}+1\) would divide \(F\) in \(\mathbb Z[X]\), making \(F(1)\) even.

For the last assertion, take \(\zeta=\exp(\pi\mathrm i/3)\).
Attach exponent \(3\bmod6\) to each oriented two-term difference.
In each triple choose either permutation of \(2,4\bmod6\) for the exponents on \(v_1-v_0,v_2-v_0\).
For a given assignment write \(d_i\) for these differences and \(c_i\) for their exponents.
It is feasible precisely when
\[
     \sum_i n_i d_i=0,\quad n_i\in\mathbb Z
          \quad\Longrightarrow\quad \sum_i n_i c_i=0\pmod6 .
\]
It suffices to test an integer basis of the relation lattice for each of the finitely many assignments.
Necessity follows from the ratios just computed.
Under this congruence condition \(d_i\mapsto\zeta^{c_i}\) defines a character of the difference sublattice.
Smith normal form extends it to the ambient lattice by taking the indicated roots in \(\mathbb C^\times\), and permits all values to be roots of unity.
This extension solves every two- and three-term equation.
For a specific passing table its multipliers still require a separate regular-rank calculation. For a triple whose differences are outside \(S\), its coefficient triangle can have unequal side lengths and the cubic test need not apply.

## Assessment history

### Decision cubic-fibers

| Field | Value |
| --- | --- |
| date | 2026-11-17T00:10 |
| status | proved |
| reason | Independent review verifies the root orders, odd-fiber obstruction and both directions of the finite feasibility test. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Saturated triple differences, odd fibers and the mixed two- and three-term test with its hypotheses. |
| argument | [Proof](#argument) | Ratio, cyclotomic and lattice extension arguments. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0056_v1.md#whole-argument-finding) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-cubic-fibers)

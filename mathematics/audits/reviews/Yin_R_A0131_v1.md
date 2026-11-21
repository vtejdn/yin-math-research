---
author: Yin
---
# Independent review of the normality criterion for the complex group algebra

On 2026-11-21 at 04:10 UTC, a separately assigned reviewer completed an independent inspection of Yin's fixed C_A0095_v1 statement and proof, including the final argument on extreme support layers.
The reviewer received the claim, its source locator and the scope of review without proof-development discussions, author explanations or prior review conclusions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0095_v1.md#statement) | Matrix nilpotence, four scalar conditions for each fixed torsion-free group, and the extreme-layer assertions. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0095_v1.md#argument) | Entire proof, including descent to the original complex coefficients, scalar equivalences, fixed-lift comparison and support reduction. |
| [Whole finding](#whole-finding) | [Extreme layers](../../claims/Yin_C_A0095_v1.md#testing-the-extreme-layers-of-one-element) | Highest-degree component, conjugation of the lowest layer and exclusion at minimum support cardinality in the same group. |

## Whole finding

The proof establishes all of the stated assertions.
Over the integral group ring every surviving term in the differentiated product differentiates each factor exactly once and preserves the factor order.
The resulting factorial bound eventually falls below the norm of every nonzero integral matrix, since some column evaluated on the identity basis vector has a nonzero integer coordinate.
Kleinecke's paper gives the factorial identity in (2) on p. 535 and its Banach algebra norm estimate on p. 536.
The integral lower bound supplies the extra step to exact nilpotence. [Kleinecke, *On operator commutators*](https://doi.org/10.1090/S0002-9939-1957-0087914-4)

The finitely many original coefficients generate a finite extension \(K\) of a rational function field \(k\).
Multiplication on the \(k\)-vector space \(K\) embeds each coefficient faithfully as a matrix over \(k\).
One polynomial clears all denominators in both images, and distinct monomials remain distinct in the central free abelian group used in the integral proof.
The double commutator scales by \(q^3\), the first commutator by \(q^2\), and the scalar \(q^{2m}\) is invertible on returning to the rational function field.
This verifies nilpotence in the original matrix algebra for the actual complex coefficients.

On a finite-dimensional orbit with a nonzero eigenvalue \(\lambda\), every nonzero power of a corresponding eigenvector has commutator eigenvalue \(m\lambda\), bounded in modulus by \(2\|D\|\).
If all eigenvalues vanish and \([D,X]\ne0\), the last nonzero iterate is a nonzero commutator killed by the next derivation, so the matrix result applies.
For \(X=D^*\), the triple identity bounds the orbit dimension by three.
Conversely, a highest nonzero power of a nonzero nilpotent gives a square-zero \(V\), and each term of \(\partial_V^3(V^*)\) vanishes.
The faithful regular representation detects \(V\ne0\), and normality would force \(\|V\|^2=\|V^2\|=0\).

For the fixed-group implication the reviewer accepts Connell's Theorem 8 after checking its statement and definition of a prime group on p. 675.
The field \(\mathbb C\) is prime and a torsion-free group has no nontrivial finite normal subgroup.
Consequently, for nonzero \(\alpha,\beta\) with \(\alpha\beta=0\), primeness gives \(\beta\mathbb C[G]\alpha\ne0\).
Linearity then gives a single \(g\in G\) for which \(\beta g\alpha\) is nonzero and square-zero.
Connell's original proof lay outside the scope of the source inspection. [Connell, *On the Group Ring*, p. 675](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/29E2EC3F9179FB3C6225A26EC88CBB77/S0008414X00029849a.pdf/on-the-group-ring.pdf#page=26)

In the supplementary universal construction, distinct support pairs give distinct words \(bza\) in the free product, including pairs with an identity factor, and the free product remains torsion-free.
For the comparison with the integer fixed-lift argument, the noncommuting finite orbit supplies a nonzero nilpotent.
The specified annihilated element \(A\) and prescribed nonzero reduction \((-1)^k c\) come from the separate identity in the [fixed-lift test](../../claims/Yin_C_A0039_v3.md#a-finite-adjoint-orbit-test-for-an-exact-annihilator).

The degree \(3h-l\) forces all three unstarred factors into the highest layer and the starred factor into the adjoint of the lowest, even when distinct support products coincide within that degree.
For a single top label \(u\), right multiplication by \(u\) commutes with \(\operatorname{Ad}u\), yielding the stated third power of \(\operatorname{Ad}u-I\).
Unitarity of conjugation gives the same kernel for its difference from the identity and for the cube of that difference.
It follows that \(u\) and \(u^{-1}\) commute with \(Q\) and \(Q^*\).
When the two layers exhaust the support, deletion of the top term therefore preserves both \([D,D^*]\) and \(\partial_D^3(D^*)\).
Any resulting nonnormal witness has exactly one fewer support label in the same group.
The character only needs to be defined on the subgroup generated by \(\operatorname{supp}D\).
The [A0002 contract](../../tasks/Yin_T_A0002_v1.md#contract) still requires a decision for arbitrary finite supports in every torsion-free group.

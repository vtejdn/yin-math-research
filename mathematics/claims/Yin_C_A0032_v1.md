---
author: Yin
---
# Eliminating a whole factor from the coefficient equations of a zero product

## Statement

Let \(A,B\) be nonempty finite subsets of a group \(G\), and prescribe nonzero complex coefficients on all their elements.
For \(v=(v_y)_{y\in B}\in(\mathbb C^\times)^B\), form the matrix \(M(v)\) with rows indexed by \(w\in AB\) and columns by \(x\in A\), with
\[
       M(v)_{w,x}=
          \begin{cases}
             v_{x^{-1}w},&x^{-1}w\in B,\\
             0,&\text{otherwise}.
          \end{cases}
\]
This uses the original group-product fibers even when their cardinalities are three or larger.

There are coefficients \(u_x\ne0\) on all of \(A\) with \((\sum_x u_x x)(\sum_y v_y y)=0\) exactly when deleting any single column of \(M(v)\) preserves its rank.
This gives a finite choice of strata, specified below by vanishing minors and a product of nonvanishing pivot minors.
All further equations on a stratum have only the \(B\)-side variables.
The integer coefficients in a minor count signed matchings with the same multiset of column labels from \(B\).
Two-term minors consequently impose character equations even in a table having no two-term product fiber.
An incompatible integral relation among their prescribed values, or a nonzero monomial among the required vanishing minors, excludes the stratum.

For any surviving branch of those character equations, form the Laurent polynomials obtained from **all** required vanishing minors by the substitution below.
Suppose their individual within-polynomial exponent differences span at most two rational directions together in the remaining lattice.
Then exact feasibility of this branch, including the pivot conditions, is decided by one-variable gcds, two-variable polynomial gcds and elimination in one variable.
The original coefficient torus can have arbitrarily many more directions.
The pivot polynomials place no restriction on the dimension used in this hypothesis.
Testing all branches with this property decides the original support problem if every remaining branch is covered.
The construction also works with \(A\) and \(B\) interchanged on passing to the opposite group.

## Full support and rank strata

For fixed \(v\), the coefficient vector of the group-ring product is \(M(v)u\).
Its kernel contains a vector with nonzero \(x\)-coordinate precisely when column \(x\) belongs to the span of the other columns.
If this holds for every \(x\), no individual coordinate hyperplane contains the kernel.
A finite union of proper linear subspaces of a complex vector space is still proper: the product of their nonzero defining linear forms is a nonzero polynomial.
Thus a single kernel vector can be chosen with every coordinate nonzero.
The converse follows from the same column relation.

The matrix is nonzero on the coefficient torus.
For a solution its rank \(t\) must lie between one and \(|A|-1\).
For each \(t\) in this range require all its \((t+1)\)-minors to vanish.
For each deleted column choose one \(t\)-minor of the remaining matrix and require that minor to be nonzero.
Take all the finitely many possible choices, omitting a choice if some required pivot is identically zero.
Write \(H\) for the product of the chosen pivots, so their common condition is \(H(v)\ne0\).
This describes exactly the possible \(v\), since the chosen pivots give rank at least \(t\) after each deletion and the larger minors bound the rank before any deletion.
For \(|A|=1\) the absence of an admissible rank reflects the invertibility of the single group monomial.

For a minor, order its input columns and output rows.
Its nonzero determinant terms correspond to perfect matchings between these two sets allowed by the multiplication table.
Each edge \((w,x)\) contributes the label \(x^{-1}w\in B\).
For each multiset of labels sum the signs of its matchings before treating the determinant as a Laurent polynomial.
For example, if two required minors are \(a_0 v^\lambda+a_1 v^\mu\) and \(b_0v^{\lambda+\eta}+b_1v^{\mu+\eta}\), with \(\mu\ne\lambda\) and all four displayed coefficients nonzero, then \(a_0b_1-a_1b_0\ne0\) excludes the stratum.
This test concerns the combined coefficient equations through their minors, regardless of whether any single fiber determines a ratio.

## Character equations from minors

Discard identically vanishing required equations and reject any nonzero monomial required to vanish.
For every binomial required to vanish write \(v^{d_j}=q_j\), where \(d_j\in\mathbb Z^B\) is a difference of its exponents and \(q_j\in\mathbb Q^\times\) is the signed ratio from its two nonzero integer coefficients.
The assignment extends to a character on \(L:=\sum_j\mathbb Z d_j\) precisely when \(\prod_j q_j^{n_j}=1\) for every relation \(\sum_j n_j d_j=0\).
An integer basis of the relations suffices.
Let \(S=\operatorname{sat}(L)\) in \(\mathbb Z^B\).
Smith normal form yields the finite list of extensions \(\rho:S\to\mathbb C^\times\) of the prescribed character by taking all required roots of the \(q_j\) and their products.
All branch values are algebraic, including when some binomial coefficients have unequal absolute values.
If there are no binomials, take \(S=0\) and the single empty assignment.

Split \(\mathbb Z^B=S\oplus N\).
On a fixed branch, replace each monomial with exponent \(s+n\) by \(\rho(s)T^n\), with \(T\in\operatorname{Hom}(N,\mathbb C^\times)\).
Apply the substitution to \(H\) and to every required equation, combining terms at equal exponents and again handling identically zero equations and nonzero monomials.
An identically zero \(H\) rejects the branch.
For each remaining required equation separately divide by any one of its monomials, which is nonzero everywhere in the torus.
Let \(D\subset N\) be the saturation of the subgroup spanned by the exponent differences in these equations.
Put \(d=\operatorname{rank}D\) and split \(N=D\oplus N'\).
The equations now concern only \(t\in\operatorname{Hom}(D,\mathbb C^\times)\).
Write the pivot product, after the same substitution, as
\[
               H(t,U)=\sum_{\gamma\in N'} H_\gamma(t)\,U^\gamma .
\]
For fixed \(t\), some \(U\in\operatorname{Hom}(N',\mathbb C^\times)\) keeps all pivots nonzero precisely when at least one \(H_\gamma(t)\ne0\).
Indeed a nonzero Laurent polynomial over an infinite field cannot vanish on the entire torus.
This proves why exponent directions occurring only in pivot requirements need not be counted.
The remaining equations and all \(H_\gamma\) have algebraic coefficients.

## Curves and isolated solutions in two variables

For \(d=0\) evaluate the constant conditions.
For \(d=1\), clear powers of the variable in the nonzero Laurent equations, and compute their gcd.
Check its nonzero roots against the inequalities \(H_\gamma(t)\ne0\) for at least one \(\gamma\).
When all required equations are identically zero, the pivot check is just whether \(H\) is a nonzero Laurent polynomial.
These tests are in the coefficient space of the projected factor, whereas the [one-direction fiber test](Yin_C_A0026_v1.md#exact-test-with-one-remaining-direction) applies to the row and column character equations jointly.

Take \(d=2\) and choose torus coordinates \(X,Y\).
Multiplying each polynomial by a Laurent monomial, arrange that all nonzero equations \(P_i(X,Y)\) and all nonzero \(H_\gamma(X,Y)\) are ordinary polynomials, with factors \(X,Y\) removed.
All calculations below take place on \(X Y\ne0\), and can be performed over the algebraic closure of the coefficient number field.
If there are nonzero equations, take their gcd \(C\).
Every common nonmonomial irreducible factor \(c\) of the equations gives a feasible point on its curve exactly when at least one \(H_\gamma\) is not divisible by \(c\).
Indeed \(c\) is distinct from \(X,Y\), and its irreducible curve meets the torus in a dense open set.
A polynomial not divisible by \(c\) is nonzero on a nonempty open subset there.
Equivalently, when \(c\) depends on \(Y\) and is not a vertical line, one may choose \(X\ne0\) away from the finitely many exceptional leading coefficients, constant terms and resultant zeros of \(c\) and that \(H_\gamma\), then take a root of \(c(X,Y)\).
For a vertical line \(X=x\), the same test reduces to checking that \(H_\gamma(x,Y)\) is a nonzero polynomial and choosing \(Y\ne0\) outside its zeros.

For solutions outside the common curve set, use \(Q_i=P_i/C\), which have gcd one.
The common zeros of the \(P_i\) consist of the curves just considered together with the common zeros of all \(Q_i\).
A nonzero constant \(Q_i\) leaves no points in this latter set.
Otherwise take any nonconstant \(R=Q_i\) and choose an integer linear combination \(T\) of the \(Q_j\) coprime to \(R\).
To see existence, for each of the finitely many irreducible factors of \(R\), at least one \(Q_j\) is nonzero modulo that factor.
Thus \(T=\sum_j n^{j-1}Q_j\), with the \(Q_j\) indexed from one, works outside a finite list of integers \(n\).
A gcd computation checks a chosen \(n\).
If both \(R,T\) are independent of \(Y\), their coprimality excludes a common point.
Otherwise \(\operatorname{Res}_Y(R,T)\) is a nonzero polynomial in \(X\), since \(R,T\) have no common positive-degree factor over \(\overline{\mathbb Q}(X)\).
Every common affine point supplies a root of this resultant, including points at which leading coefficients specialize to zero.
For instance this necessity follows from the Sylvester polynomial identity expressing the resultant as a polynomial combination of \(R,T\).
The same necessity holds if one of them is constant in \(Y\), when the resultant is a power of that polynomial in \(X\).
For each nonzero root \(x\), substitute into **all** \(Q_i\).
They cannot all vanish identically in \(Y\), since that would give the common factor \(X-x\).
Take the gcd of the nonzero \(Q_i(x,Y)\), check all its nonzero roots \(y\), and verify \(H_\gamma(x,y)\ne0\) for at least one \(\gamma\).
Every accepted point satisfies the coefficient equations, and the resultant argument includes every isolated point.
This last specialized check removes any extraneous roots caused by a degree drop.

For each passing branch, a choice of the unused torus coordinates gives the full vector \(v\), and a full-support kernel vector of \(M(v)\) recovers \(u\).
A branch rejected at some smaller subsystem cannot be restored by imposing the remaining coefficient equations.
Branches whose required minor differences still have rank above two can require higher-dimensional analysis.
The tests concern the existence of coefficients on fixed supports, and a passing point still requires its own regular-rank calculation for [A0001](../tasks/Yin_T_A0001_v1.md#contract).

## Assessment history

### Decision factor-elimination

| Field | Value |
| --- | --- |
| date | 2026-11-17T01:29 |
| status | proved |
| reason | The independent review covers the full statement and argument at their stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Elimination on the exact support torus and complete feasibility when the remaining exponent differences span at most two directions. |
| argument | [Proof](#full-support-and-rank-strata) | The complete argument and its conditions of applicability. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0063_v1.md#whole-argument-finding) | Independent review of the exact statement and proof. |

## Current assessment

[Selected decision](#decision-factor-elimination)

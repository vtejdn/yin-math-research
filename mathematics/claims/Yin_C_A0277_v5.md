---
author: Yin
---

# An effective finite word test for the nine-monomial half-kernel

## Statement

Let \(K\ge1\) be a rational number.
There is a terminating algorithm returning an integer \(R\ge1\) and a positive rational number \(\epsilon\) for the following test.
Use the three rows
\[
       (1,1,1),\qquad (1,\lambda u,\mu v),\qquad (1,\sigma w,\theta z)
\]
over any discrete group.
Suppose the four nonzero coefficient moduli lie in \([1/K,K]\), \(u,v\) freely generate their subgroup, and \(w,z\) freely generate theirs.
If there is no common nonidentity element of the two radius-\(R\) word balls in the indicated bases, then the unnormalized regular nullity is at most \(1/2-\epsilon\).
This makes the [compact-coefficient common-word bound](Yin_C_A0277_v4.md#common-words-at-bounded-coefficient-ratios) effective.
It computes a uniform radius and gap from \(K\); application to a particular presentation requires establishing its finite word tests there.
No running-time bound is asserted.

## Finite relation patterns and polynomial moments

Use the free group \(F\) on the four formal labels and let \(B_L\) be its finite ball of freely reduced words of length at most \(L\).
Use integers \(L\ge4\).
Put \(k_L=\lfloor L/2\rfloor\).
Enumerate subsets \(D\subseteq B_L\) and keep precisely the patterns passing the following finite checks, using free reduction for every product.

* The identity belongs to \(D\), and so does the inverse of each member.
* If \(g,h\in D\) and \(gh\in B_L\), then \(gh\in D\).
  If \(g\in D\) and \(xgx^{-1}\in B_L\) for a generator or inverse generator \(x\), then \(xgx^{-1}\in D\).
* No nonidentity word entirely in either one of the two free pairs belongs to \(D\).
  For any nonidentity word \(a\) in the first pair and \(b\) in the second, both of length at most \(k_L\), require \(ab^{-1}\notin D\).
  These last words have length at most \(L\).

Realized patterns of true relations in such marked groups pass these tests when their radius-\(k_L\) balls have trivial intersection.
The enumeration also permits patterns that may not extend to any marked group.

Let \(H\) denote the displayed formal matrix and take the rational constant \(C=9K^2\).
Its evaluations have \(\|H\|^2\le C\) by the three row and column bounds on entry norms.
For \(1\le m\le k_L\) sum the diagonal entries of \((I-H^*H/C)^m\) formally over \(\mathbb CF\).
Regard coefficient conjugation as sign change on the imaginary coordinate of each of the four complex variables.
Let \(t_{D,m}\) be the real part of the sum of its coefficients indexed by \(D\).
Every term word has length at most \(2m\), so the pattern covers all terms.
These are explicit rational polynomials in eight real variables.
For actual group relations they are exactly the matrix traces of these powers.

For every retained \(D\) consider the simultaneous real polynomial conditions
\[
 \frac1{K^2}\le |c|^2\le K^2\quad(c=\lambda,\mu,\sigma,\theta),
 \qquad t_{D,m}\ge \frac12-\frac1L\quad(1\le m\le k_L).
\]
Enumerate pairs \((L,j)\), \(j\ge1\), in increasing order of \(L+j\).
At such a pair partition the box \([-K,K]^8\) into boxes by dividing each interval into \(2^j\) equal pieces.
For each retained pattern and each box evaluate the rational polynomials of its inequalities, written as \(f\ge0\), by interval arithmetic with exact rational endpoints.
If for every pattern every box has at least one such upper endpoint strictly negative, return \(R=k_L\) and \(\epsilon=1/L\).
Every coefficient tuple in the annulus lies in at least one tested box.
In a tested group, every power is a positive contraction with trace at least the kernel dimension.
Hence the returned values have the claimed property.

## Why the search terminates

First suppose that for every \(L\) one could select a retained pattern and a coefficient vector in the compact annulus with all the indicated moment inequalities.
Take a subsequence along which the coefficients converge and membership eventually stabilizes for every free word as the balls exhaust \(F\).
The eventual members form a normal subgroup \(N\triangleleft F\): each test for the identity, inverse, product and generator conjugation of any fixed words is imposed for all sufficiently large \(L\).
Both pairs in \(F/N\) are free by the third check.
They have trivial intersection since fixed nonidentity words in its two factors are eventually covered by the radius test.

For each fixed \(m\), membership of every word in its finite expansion stabilizes.
Its trace at the limit coefficients in \(F/N\) is consequently at least \(1/2\), on taking \(L\to\infty\).
By spectral calculus these traces decrease to the regular nullity in the limit group.
That nullity would be at least \(1/2\), contrary to the [strict arbitrary-modulus result](Yin_C_A0277_v4.md#the-two-orders-of-a-group-product).
Thus at some fixed \(L\) all the finitely many systems are infeasible.
For a given infeasible system the minimum of its left-hand sides \(f\) is a strictly negative continuous function throughout the compact box \([-K,K]^8\), so it has a strictly negative maximum.
For this finite list of polynomial expressions the widths of their rational interval evaluations tend uniformly to zero with the box mesh, by finite addition and multiplication on bounded intervals.
Consequently every sufficiently fine box is excluded by at least one strict upper bound.
A single fine mesh works for every pattern at this fixed \(L\), and the enumeration reaches that pair.
This proves termination even with the unrealizable finite patterns admitted in the search.

## Assessment history

### Decision effective-local-tests-on-bounded-ranges-of-moduli

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | The finite interval search and the compactness argument prove existence of an effective radius and gap for every rational modulus bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The computability statement and its inputs. |
| argument | [Finite relation patterns and polynomial moments](#finite-relation-patterns-and-polynomial-moments) | Local relation masks, polynomial trace bounds and interval certification. |
| argument | [Why the search terminates](#why-the-search-terminates) | Compactness of limit presentations and termination of the joint search. |
| review | [Effective local tests on bounded ranges of moduli](../audits/reviews/Yin_R_A0213_v1.md#effective-local-tests-on-bounded-ranges-of-moduli) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-effective-local-tests-on-bounded-ranges-of-moduli)

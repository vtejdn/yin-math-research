---
author: Yin
---

# The central quotient in the common-power branch at order twenty-four

## Statement

Under the [order-24 common-power hypotheses](Yin_C_A0258_v1.md#statement), write \(F=\langle t_0,t_1\rangle\) for the normal subgroup of index four, \(h=t_0^k=t_1^{\pm k}\) for the common infinite central power, and \(Q=F/\langle h\rangle\).
A half-rank rectangle requires all the following conditions.

1. The group \(Q\) lies outside Linnell's class \(\mathcal C\).
   In particular a virtually free-by-cyclic or virtually closed orientable surface group as \(Q\) excludes the rectangle.
2. The class of the central extension \(1\to\langle h\rangle\to F\to Q\to1\) is nonzero in \(H^2(Q;\mathbb Q)\) and remains nonzero on every finite-index subgroup of \(Q\).
   Thus \(H_2(Q';\mathbb Q)\ne0\) for every finite-index \(Q'\le Q\).
3. Every finite subgroup of \(Q\) is cyclic and is centralized by its normalizer in \(Q\).
   For a subgroup of order \(m\) its full inverse image is infinite cyclic, with \(\langle h\rangle\) the subgroup of index \(m\).

The first statement uses the group class of [Linnell's Theorem 1.5](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems).
The other two use the actual central extension and finite abelianization of \(F\).
The conclusions leave open quotients with a nondisappearing rational extension class outside the specified class.

## Lifting Linnell's class through a central cyclic extension

Let \(\mathcal B\) consist of groups all of whose central extensions by an infinite cyclic group are in \(\mathcal C\).
Free groups belong to \(\mathcal B\): lifting a free basis splits such an extension, and the resulting direct product of the free group and the cyclic kernel lies in \(\mathcal C\) by extension with cyclic quotient.
A directed union of groups in \(\mathcal B\) belongs to \(\mathcal B\), since the preimages form a directed union of central extensions by the same kernel.
If \(N\) is normal in \(B\), \(N\in\mathcal B\), and \(B/N\) is elementary amenable, the preimage of \(N\) in each central cyclic extension of \(B\) lies in \(\mathcal C\), with quotient \(B/N\).
Closure of \(\mathcal C\) under these extensions gives \(B\in\mathcal B\).
By the defining minimality of \(\mathcal C\), one has \(\mathcal C\subseteq\mathcal B\).

If \(Q\in\mathcal C\), it follows that \(F\in\mathcal C\), and the extension by \(H/F=C_4\) gives \(H\in\mathcal C\).
The torsion-free case of Linnell's theorem gives integer regular ranks for every finite complex group-ring matrix over \(H\), excluding regular rank \(3/2\).
For clarity \(\mathcal C\) is subgroup-closed: the collection of groups all of whose subgroups are in \(\mathcal C\) contains free groups by the subgroup theorem for free groups, and is closed under directed unions and extensions with elementary amenable quotient by intersecting with the normal subgroup.
It thus contains \(\mathcal C\).
A group virtually in \(\mathcal C\) belongs to \(\mathcal C\) by taking the normal core and extending by the finite quotient.
A free-by-cyclic group is in the class by definition.
A closed orientable surface group of genus at least one maps onto \(\mathbb Z\) with free kernel: cutting along a nonseparating curve gives the infinite cyclic cover as an increasing chain of compact surfaces with boundary, or equivalently an open orientable surface with free fundamental group.
The sphere gives the trivial group.
This proves the examples in the statement.

## The rational class on finite-index subgroups

For a finite-index subgroup \(Q'\le Q\) write \(E\le F\) for its full preimage and choose a section \(s:Q'\to E\) with \(s(1)=1\).
The integers \(\ell(a,b)\) given by \(s(a)s(b)=h^{\ell(a,b)}s(ab)\) form the cocycle of the restricted extension.
If its rational class is zero, there is a map \(u:Q'\to\mathbb Q\) with \(\ell(a,b)=u(a)+u(b)-u(ab)\).
The formula \(h^n s(a)\mapsto n+u(a)\) is then a homomorphism \(E\to\mathbb Q\) taking \(h\) to one.
Let \(t_i\) represent the right cosets \(Et_i\) in \(F\) and, for \(f\in F\), write \(t_i f=e_{i,f}t_{\pi_f(i)}\) with \(e_{i,f}\in E\).
The sum of the values of this homomorphism on all \(e_{i,f}\) is a homomorphism \(F\to\mathbb Q\), by the coset permutation rule.
Since \(h\) is central in \(F\), this sum is \([F:E]\) on \(h\), contradicting [finite abelianization of \(F\)](Yin_C_A0252_v1.md#the-promislow-group-and-the-index-four-subgroup).
Thus the rational class is nonzero on every \(Q'\).
Over the field \(\mathbb Q\) degree-two cohomology with trivial rational coefficients is the vector-space dual of rational degree-two homology, by applying the exact vector-space dual functor to rational chains.
This gives the stated homological exclusion.

## The normalizer of finite torsion

Let \(D\le Q\) be finite of order \(m\), and let \(K\le F\) be its preimage.
The center of \(K\) contains \(\langle h\rangle\) with index \(m\) in \(K\).
Transfer from \(K\) into the subgroup \(\langle h\rangle\), computed by the same coset formula with the integer exponent map, is a homomorphism taking \(h\) to \(m\).
Its kernel injects into \(D\) because it intersects \(\langle h\rangle\) trivially, so it is finite and hence trivial by torsion-freeness.
It follows that \(K\) embeds in \(\mathbb Z\) and is infinite cyclic, with \(D\) cyclic of order \(m\).
Any element of the normalizer of \(D\) in \(Q\) lifts to an element of \(F\) normalizing \(K\).
Conjugation on this infinite cyclic preimage fixes the nonidentity element \(h\), so it is the identity and induces the identity on \(D\).

## Assessment history

### Decision restrictions-on-the-central-quotient

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:10 |
| status | proved |
| reason | Whole-proof review verified the lifting, cohomological and finite-normalizer restrictions and their use in the marked half-rank case. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The group-class, rational homology and finite-normalizer exclusions. |
| argument | [Lifting Linnell's class through a central cyclic extension](#lifting-linnells-class-through-a-central-cyclic-extension) | The class closure, finite extension and virtually surface examples. |
| argument | [The rational class on finite-index subgroups](#the-rational-class-on-finite-index-subgroups) | The cocycle sign, transfer of a central power and degree-two homology. |
| argument | [The normalizer of finite torsion](#the-normalizer-of-finite-torsion) | The cyclic finite preimage calculation and trivial action by the normalizer. |
| review | [Restrictions on the central quotient](../audits/reviews/Yin_R_A0205_v1.md#restrictions-on-the-central-quotient) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-restrictions-on-the-central-quotient)

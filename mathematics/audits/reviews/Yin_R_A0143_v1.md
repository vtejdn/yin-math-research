---
author: Yin
---
# Outermost coefficients in Gardam's group

## Whole finding

At 2026-11-21T06:14 UTC an agent outside the development of C_A0106_v1 independently reviewed its [statement](../../claims/Yin_C_A0106_v1.md#statement) and [complete argument](../../claims/Yin_C_A0106_v1.md#argument) for Yin.
The reviewer received the fixed inputs and scope without the development discussion or a previous finding on this claim.
The proof establishes finite-support injectivity over every field under (1), the stated scalar unique-product criterion for every nonempty finite right support, and the complex outer-sphere identity and estimate.

The group and word metric enter through two parts of [C_A0105_v2](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
Eliminating \(c,f,g,d,e\) by the five specified triangle relations expresses them in \(a,b\), and independent free reduction of all seven substituted relators gave five identities, \(R_1\) for \(add\), and \(bR_2b^{-1}\) for \(eeg\).
This gives inverse presentation maps since they fix \(a,b\), which generate both groups.
For the [rewriting rules](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system), the reviewer regenerated the two-letter rules from the seven cyclic triples and independently joined all 560 overlaps of the 98 rules by reducing at the rightmost available position.
All rules hold in the group, and their equalities give the presentation since they include inverse cancellations and reduce every triangle to the identity.
The lexicographic decrease of length and the number of negative-before-positive pairs gives termination, so the joins suffice for confluence.
Since every representative reduces to the same normal word without increasing its length, this word is shortest for the seven generators and their inverses.
The two-generator ball sizes and bounded unique-product calculations of C_A0105_v2 are outside the dependency used here.

Let \(B\ne 0\) have finite support with maximum length \(h\), including the case \(h=0\).
If a product of two support elements has length \(m+h\), both factors attain their respective maximal lengths by subadditivity.
Their normal words are irreducible separately, and the final letter of the first is positive.
The only possible reduction across their join shortens the word by cancellation or a positive-positive triangle rule.
Such a join cannot attain \(m+h\).
Conversely an eligible join is irreducible because all left sides have length two, hence gives a normal word of length \(m+h\).
The length-\(m\) prefix and the remaining suffix recover the two factors uniquely, including the empty suffix.
Thus a word from an eligible pair has coefficient exactly \(A_xb_w\), even when this vector is zero.
For each maximal occupied \(w\), the common-kernel hypothesis for its first symbol guarantees at least one eligible \(x\) with \(A_x b_w\ne0\).
This argument allows every \(d,n\ge1\) and every smaller-length coefficient of \(A\).

Reading the ordered adjacent pairs cyclically in the seven triangles gives the predecessor sets for \(a,\ldots,g\), respectively, as \(bdg,bcf,afg,acd,ceg,abe,def\), with each string denoting its set of letters.
If the terminal set is contained in none of these triples, each positive initial letter admits a terminal.
Because the triples cover the alphabet, such a terminal set contains at least two different letters, and at least one avoids cancellation at each inverse initial letter.
Every terminal is eligible for the empty input word.
For scalar \(A\), its coefficient at every occupied word is nonzero.
Thus for each maximal \(w\) of any nonempty finite right support, at least one of its products has precisely one representation in the entire support rectangle.
Taking \(m=1\) gives both generator examples, and shorter terms cannot affect the argument.

Over \(\mathbb C\), summing \(\|A_xb_w\|_2^2\) over the eligible pairs counts each represented outer-sphere word exactly once.
All remaining coefficients on that sphere vanish, which gives the asserted Gram-matrix identity.
For each of the fifteen initial symbols, including the empty symbol, \(\ker G_j=\bigcap_{x\in T_j}\ker A_x\) by the same sum-of-squares identity on a single vector.
Under (1) the least of the fifteen smallest eigenvalues is therefore positive for the fixed \(A\), independently of \(B\) and \(h\).
The right side estimates the top sphere of the finite input, so this proof leaves the general \(\ell^2\)-kernel dimension open.

In [CM94, §6, p. 374, (6.1)](../../literature/pdf/CM94.pdf#page=30), the authors give the unique positive-then-inverse right normal form for their triangle-presentation groups and identify its length with shortest-path length.
Immediately before (6.1) they credit Proposition 3.2 of reference [2], listed on [p. 382](../../literature/pdf/CM94.pdf#page=38) as the paper by Cartwright, Mantero, Steger and Zappa.
C_A0106_v1 cites (6.1) for this normal-form convention and derives its group-specific prerequisites from C_A0105_v2.
The outer-sphere formula and support conclusions have their own proof above.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0106_v1.md#statement) | All matrix dimensions and fields under (1), scalar terminal criterion with arbitrary finite right support, and complex estimate for finite inputs. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0106_v1.md#argument) | Seven-generator metric, classification and uniqueness of all outer pairs, predecessor sets, coefficient formula and uniformity in the input radius. |
| [Whole finding](#whole-finding) | [Presentation](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation) | Elimination and both presentation maps for the group used in C_A0106_v1. |
| [Whole finding](#whole-finding) | [Rewriting system](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) | Validity, termination, confluence, equality in the group and the resulting shortest seven-generator words. |

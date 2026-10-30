---
author: Yin
---

<a id="ms23-u002"></a>
# MS23-U002: The Multi-Variable Dual and Its Crossing Rule

- Source: [MS23](../../../literature/pdf/MS23.pdf), the user's 36-page published article.
- Locator: Section 4, Example 4.1, Remark 4.2, Examples 4.3-4.4 and Proposition 4.5, printed/PDF pp. 14-21; the transition to Theorem 4.6 on pp. 21-22.
- Record: 2026-09-09, the combinatorial agent, direct source reading and independent reconstruction of the source proof.
This is a source audit, not an independent review of this audit artifact unless a later reviewer is explicitly recorded.
- Kind and state: combinatorial operator construction and full local proof; audited within the scope below.
The finite computation is supplementary.

## Statement, Domain and Order Conventions

Let $d<\infty$, $-1<q<1$, and let $e_1,\ldots,e_d$ be the specified orthonormal real basis, complexified for the q-Fock space $\mathcal F_q$.
Write $\Omega=e_0$, $\mathcal F_{\mathrm{alg}}=\bigoplus_{n\ge0}^{\mathrm{alg}}H^{\otimes n}$, and $A_j$ for the left q-Gaussian.
The source denotes the annihilation operator by $l_j$, so

\[
A_j e_{j_n\cdots j_1}
=e_{j j_n\cdots j_1}
+\sum_{a=1}^n q^{n-a}\delta_{j,j_a}
e_{j_n\cdots\widehat{j_a}\cdots j_1}.
\]

The word is displayed in decreasing position order: vertex 1 labels its rightmost letter.
The commutator is $[D,A]=DA-AD$.
The normalized algebraic dual is uniquely specified recursively by

\[
D_i\Omega=0,\qquad
D_i e_{jw}=A_jD_i e_w+\delta_{ij}P_\Omega e_w-D_i l_j e_w.
\tag{1}
\]

Both terms on the right involving $D_i$ concern strictly shorter words.
Strict positivity of the finite-degree q-Gram matrices for $-1<q<1$ makes the word tensors linearly independent.
Thus (1) defines a densely defined linear operator on the whole algebraic Fock space.
The source's use of "unbounded operators" here is domain terminology: Proposition 4.5 does not prove that their operator norms are infinite, or that they extend boundedly.

The proposition gives a closed expression for (1), and proves

\[
[D_i,A_j]=\delta_{ij}P_\Omega
\quad\text{on }\mathcal F_{\mathrm{alg}}.
\tag{2}
\]

All products in (2) are defined because $D_i$ and $A_j$ preserve $\mathcal F_{\mathrm{alg}}$.
No closure, adjoint-vacuum domain or bounded extension is used in this unit's proof.

## The Partition Set and an Explicit Crossing Formula

For $n\ge1$, a partition $\pi\in B(n+1)$ of vertices $0,1,\ldots,n$ is equivalent to the following data:

1. Choose a pivot $k=\pi(0)$ with $1\le k\le\lfloor(n+1)/2\rfloor$, and pair 0 with $k$.
2. For every $a=1,\ldots,k-1$, choose a distinct partner $p_a\in\{k+1,\ldots,n\}$ and form the pair $(a,p_a)$.
3. All remaining vertices above $k$ are singletons.
There are $n-2k+1$ of them.
There are no singleton vertices at or below $k$.

The notation $\pi(0)$ means the partner of 0, not a block label or the number of pairs.
Let $s(\pi)$ denote the singleton set.
For $j_0=i$, set

\[
\delta_{p(\pi)}=
\delta_{i,j_k}\prod_{a=1}^{k-1}\delta_{j_a,j_{p_a}},
\qquad
e_{s(\pi)}=e_{j_{s_r}\cdots j_{s_1}}
\quad(s_r>\cdots>s_1).
\]

An empty output is $\Omega$, and the empty product is 1.
Only pair blocks contribute delta factors.

The source draws the $(0,k)$ pair at height 1 and $(a,p_a)$ at height $a+1$; singletons extend vertically to the top.
Intersections of these prescribed polygonal paths are counted, including two intersections between suitably nested pairs.
This is not the usual crossing statistic on pair partitions.

The drawing rule has the following convenient exact translation, reconstructed in this audit:

\[
\boxed{\operatorname{cross}(\pi)
=\sum_{a=1}^{k-1}(p_a-k)
+\operatorname{inv}(p_1,\ldots,p_{k-1}).}
\tag{3}
\]

Here $\operatorname{inv}(p)=\#\{a<b:p_a>p_b\}$.
To verify (3) directly from the drawing, each horizontal segment crosses the vertical segments belonging to higher pairs and to singletons.
The total is

\[
\frac{k(k-1)}2+
\sum_{a=1}^{k-1}
\left(\#\{b>a:p_b<p_a\}+\#\{s\in s(\pi):s<p_a\}\right).
\]

The parenthesis equals $p_a-k-1-\#\{b<a:p_b<p_a\}$.
Summing and replacing the number of noninversions by $\binom{k-1}{2}-\operatorname{inv}(p)$ gives (3).
This is a local notation conversion of the source's drawing, not an additional theorem about q-Gaussian boundedness.

With these conventions, Proposition 4.5 states

\[
\boxed{D_i e_{j_n\cdots j_1}
=\sum_{\pi\in B(n+1)}
(-1)^{\pi(0)-1}q^{\operatorname{cross}(\pi)}
\delta_{p(\pi)}e_{s(\pi)}.}
\tag{4}
\]

The sign depends on the pivot, not on the crossing count.
At $q=0$ only $k=1$ remains, and (4) deletes a matching terminal letter, as for the free right annihilator.

## Examples and the Source's Combinatorial Pattern

The first nontrivial correction occurs in degree three:

\[
D_i e_{j_3j_2j_1}
=\delta_{i,j_1}e_{j_3j_2}
-q\delta_{i,j_2}\delta_{j_3,j_1}\Omega.
\]

In degree four the two correction terms correspond to $k=2$, $p_1=3,4$:

\[
D_i e_{j_4j_3j_2j_1}
=\delta_{i,j_1}e_{j_4j_3j_2}
-\delta_{i,j_2}
\left(q\delta_{j_3,j_1}e_{j_4}
+q^2\delta_{j_4,j_1}e_{j_3}\right).
\]

For the degree-five full pairing $(0,3),(1,5),(2,4)$, (3) gives $2+1+1=4$.
The usual pair-crossing statistic would give 2 and therefore the wrong coefficient.
The other full pairing $(0,3),(1,4),(2,5)$ has exponent $1+2=3$.
Both have positive sign.
The degree-six examples $(p_1,p_2)=(6,5),(6,4),(5,4)$ have exponents $6,5,4$ and the respective surviving letters at vertices $4,5,6$.
These reproduce all four drawings of Example 4.4 and the corresponding terms of Example 4.1.

Only odd degrees can contribute a vacuum component.
For $n=2m-1$, a full pairing necessarily has $k=m$, and its high partners permute $m+1,\ldots,2m-1$.
Consequently,

\[
\operatorname{cross}(\pi)=\frac{m(m-1)}2+\operatorname{inv}(p),
\qquad (-1)^{\pi(0)-1}=(-1)^{m-1}.
\tag{5}
\]

The compulsory quadratic exponent in (5) is the source of the strong q-decay exploited in Theorem 4.6.
Formula (5) alone does not control the norm of the full operator $D_i$: it concerns its vacuum matrix coefficient.

## Reconstruction of the Whole Proposition 4.5 Proof

The vacuum gives $D_i A_j\Omega=\delta_{ij}\Omega$ and $A_jD_i\Omega=0$.
Fix a nonempty input $e_{j_n\cdots j_1}$ and set the next left letter to $j_{n+1}$.
Expand $A_{j_{n+1}}D_i$ using (4).
Its creation terms prepend $j_{n+1}$ to the singleton output.
Its annihilation terms select one singleton $s_a$ and carry an additional factor $q^{r-a}\delta_{j_{n+1},j_{s_a}}$, where $s_r>\cdots>s_1$ and $r=|s(\sigma)|$.

Expand $D_i A_{j_{n+1}}$ as

\[
D_i e_{j_{n+1}j_n\cdots j_1}
+\sum_{l=1}^n q^{n-l}\delta_{j_{n+1},j_l}
D_i e_{j_n\cdots\widehat{j_l}\cdots j_1}.
\tag{6}
\]

The partitions in the last sum act on the remaining $n-1$ letters, in order-preserving compressed coordinates.
This relabeling is essential when comparing $l$ with the pivot.

### First Cancellation: Removing a Singleton

Take a partition $\sigma\in B(n+1)$ and the singleton $l=s_a$ selected by an annihilation term of $A_{j_{n+1}}D_i$.
Delete that singleton and compress the remaining labels to obtain $\pi\in B(n)$.
Since every singleton lies above the pivot, $\pi(0)=\sigma(0)$, so the signs agree.
The delta factors and output word are unchanged apart from the selected singleton and the common new delta.

The deleted singleton crosses exactly the pair paths whose high partner is larger than $l$.
Equivalently, (3) changes by the number of those partners:

\[
\operatorname{cross}(\sigma)-\operatorname{cross}(\pi)
=(n-l)-(r-a).
\]

Therefore the two exponents match:

\[
\operatorname{cross}(\pi)+n-l
=\operatorname{cross}(\sigma)+r-a.
\tag{7}
\]

This is a bijection between all annihilation terms on $A_{j_{n+1}}D_i$ and the terms of the second part of (6) for which $l>\pi(0)$, with $\pi(0)$ measured in the compressed coordinates.
The inverse inserts $l$ as a singleton.
Thus these terms cancel in the commutator, with identical signs, deltas, exponents and singleton order.

### Remaining Terms: Inserting a Pair

For a remaining term in (6), write $k=\pi(0)$ and $l\le k$.
Insert vertex $l$, add the new largest vertex $n+1$, and pair them.
The resulting partition $\pi'\in B(n+2)$ has pivot $k+1$.
All old high partners increase by one.
The new partner $n+1$ is inserted at position $l$ in the low-endpoint partner list.

In (3), the sum of partner offsets increases by $n-k$.
The new maximal partner creates $k-l$ inversions with the partners after it.
Hence

\[
\operatorname{cross}(\pi')-\operatorname{cross}(\pi)
=(n-k)+(k-l)=n-l.
\tag{8}
\]

The sign changes exactly as required when the remaining terms are subtracted from (6):

\[
-(-1)^{k-1}=(-1)^k=(-1)^{\pi'(0)-1}.
\]

The new pair adds precisely $\delta_{j_{n+1},j_l}$.
Its endpoints never become output singletons, so the output word is unchanged.
This gives a bijection to all partitions in $B(n+2)$ whose largest vertex is paired.

Meanwhile the creation terms from $A_{j_{n+1}}D_i$ are exactly the partitions in $B(n+2)$ with the largest vertex singleton.
Adding that leftmost singleton creates no crossing and prepends exactly the new letter.
The two disjoint classes exhaust $B(n+2)$ and reconstruct $D_i e_{j_{n+1}\cdots j_1}$.
Thus (6) equals $A_{j_{n+1}}D_i$ on nonempty words, proving (2).

This verifies the complete induction/classification argument, not only its low-degree consequences.
The published pp. 19-21 examples and their displayed exponents agree with (7)-(8); in particular the pair-insertion example changes crossing number from 7 to 13 with $n=8$, $l=2$.

## Boundary Cases, Dependencies and Research Interface

- At $q=1$ and $d\ge2$, the symmetric Fock quotient identifies $e_1\otimes e_2-e_2\otimes e_1$ with zero, whereas the formula for $D_1$ sends it to $-e_2$.
At $q=-1$, the antisymmetric quotient identifies $e_1\otimes e_1$ with zero, whereas $D_1$ sends it to $e_1$.
Therefore the algebraic formula does not descend to these endpoint Hilbert-space quotients.
This confirms Remark 4.2 and its one-variable endpoint dependency.
It does not forbid a different formulation with different relations or domains.
- The needed analytic input here is the strictly positive q-inner product and density of the algebraic Fock space for $-1<q<1$, introduced in Section 2.
The crossing proof itself is a finite algebraic identity, polynomial in q, and imports no crossing theorem from the source's cited reference [1].
That citation is an analogy, not a required dependency of Proposition 4.5.
- Theorem 4.6 must separately show $\Omega\in\operatorname{Dom}(D_i^*)$ before this becomes a normalized dual system in the source's stronger analytic definition.
Section 5 must separately establish the regularity of the conjugate variables.
Neither follows from (2) alone.
- This supplies the exact combinatorial operator behind the [q-Gaussian route](../../../strategies/Yin_S_F0008.md).
It refines the degree-three diagnostic already used in [Yin_C_F0020](../../../claims/Yin_C_F0020_v1.md#yin_c_f0020), without changing that claim's bounded-dual parameter range.
- Proposition 4.5 does not establish boundedness of these normalized $D_i$ on the entire q-Fock space for all q, nor a finite-state structure for general rational q-Wick coefficients.
Its paired contractions explain why a direct terminal-letter deletion argument from the free case is insufficient.

## Verification Facts and Computation

The complete pp. 14-21 passage was read in extracted text, and rendered pp. 15-17 and 19-21 were inspected directly to verify the partition geometry, superscripts, signs, indices and examples.
The source statement, domain, all cases of the proof and both exponent identities have been reconstructed above.
No mathematical error was found in Proposition 4.5 within this scope.
The order-preserving relabeling and the nonstandard crossing statistic are essential interpretation points, rather than source corrections.

The independent standard-library [exact check](../../../computations/programs/Yin_J_F0003/main.py), with its [execution record](../../../computations/programs/Yin_J_F0003/readme.md#question-and-scope), compares three separately implemented objects: the prescribed drawing, the explicit statistic (3), and the dual recursively forced by (1).
It also tests the actual commutator directly.
On 2026-09-09 the executed checks passed:

- 512 partitions through $n=10$, comparing geometric and explicit crossing numbers;
- 1,257 singleton-deletion and 1,978 pair-insertion exponent identities;
- 4,301 dual-formula comparisons and 11,881 direct commutator identities, over two-letter words through length 8 and three-letter words through length 6;
- the wrong usual-crossing rule as a negative control and both endpoint quotient obstructions.

Arithmetic is exact in $\mathbb Z[q]$ and intermediate word supports are not truncated.
These finite checks neither replace the universal proof above nor certify q-Fock norm estimates, convergence, operator boundedness, or formal proof-assistant verification.
No author erratum search or comparison with another edition was performed by this unit's author; any source-level version search must be recorded separately.

## Revisions and Downstream Effects

Initial full unit, 2026-09-09.
It supplies the audited combinatorial input to the adjoint-vacuum estimate and subsequent conjugate-variable formulas, and makes explicit the normalization and domain limits of its use in Yin_C_F0020/Yin_S_F0008.
No project claim is promoted to all-q bounded duals by this audit.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | MS23, the supplied 36-page published article, Advances in Mathematics 413 (2023), 108834; printed and one-based PDF pages agree. The earlier 30-page arXiv reading and external source editions retain their separate recorded scopes. |
| source-locator | Section 4, Example 4.1, Remark 4.2, Examples 4.3-4.4 and Proposition 4.5, printed/PDF pp. 14-21; transition to Theorem 4.6 on pp. 21-22. |
| inspection | 2026-09-09: full local algebraic/combinatorial reconstruction of the multi-variable dual and crossing rule, with supplementary exact finite checks. Source-proof reconstruction is distinct from independent artifact review, which is separately recorded. The finite checks do not establish Hilbert-space norm estimates, convergence, boundedness or formal verification; no separate errata or edition comparison was claimed by this unit author. |

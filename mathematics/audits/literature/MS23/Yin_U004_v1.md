---
author: Yin
---

<a id="ms23-u004"></a>
# MS23-U004: Wick Difference Quotients and Lipschitz Conjugates

- Source: [MS23](../../../literature/pdf/MS23.pdf), 36-page published article in Advances in Mathematics 413 (2023), 108834.
- Locator: Section 5 opening, Proposition 5.1, Example 5.2, and Corollary 5.3, printed/PDF pp. 26-31.
Remark 5.4 is outside this unit.
- Record: 2026-09-09, the estimate agent; complete local induction and analytic estimate reconstructed, source formulas and diagrams visually checked, supplementary exact computation executed.
This reconstruction is self-reviewed; the fresh2026-10-21 independent full local proof review is recorded separately in the [source index](readme.md#goal-completion-review).
- Coverage: `Audited within scope`, with the explicit foundational and homogeneous Haagerup inputs retained.
No formal verification is claimed.

## Setting and the Precise Conclusions

Fix finite $d\ge1$, $q\in(-1,1)$, and the canonical q-Gaussian tuple $A=(A_1,\ldots,A_d)$ in $M=\Gamma_q(\mathbb R^d)$ with faithful vacuum trace.
Let $e_{j_n\cdots j_1}$ be the q-Fock word vector and $W(e_{j_n\cdots j_1})$ its Wick polynomial.
The source identifies these two notationally; all derivatives below are derivatives of Wick **polynomials**, not of raw tensor vectors independently of this identification.

The algebraic free difference quotient is
\[
\partial_i:\mathbb C\langle A\rangle\longrightarrow
\mathbb C\langle A\rangle\odot\mathbb C\langle A\rangle,
\quad \partial_i A_j=\delta_{ij}1\otimes1,
\]
with bimodule convention $a\cdot(u\otimes v)\cdot b=au\otimes vb$.
The generators are algebraically free.
Existence of the conjugate system implies closability as an operator $L^2(M)\to L^2(M)\otimes L^2(M)$; write its closure as $\overline\partial_i$.

Proposition 5.1 gives a finite crossing-partition expression for $\partial_iW(e_w)$.
Corollary 5.3 asserts, for every $i,j$,
\[
\boxed{\xi_i\in\operatorname{dom}(\overline\partial_j),\qquad
       \overline\partial_j\xi_i\in M\ \overline\otimes\ M.}
\tag{1}
\]
Here $\xi_i$ is the bounded conjugate variable from [MS23-U003](Yin_U003_v1.md#ms23-u003), identified with its $L^2$ vector.
The spatial tensor product is represented on $H_q\otimes H_q$, and the trace on it is $\tau\otimes\tau$.
Statement (1) is the source's Lipschitz-conjugate condition, not boundedness of the operators $D_i$ or of $\partial_j$ on all of $L^2(M)$.

## The Partition Family and Its Crossing Statistic

Place vertices $n>\cdots>1>0$ on a horizontal line and assign colors $j_k$, including $j_0=i$.
A partition $\pi\in C(n+1)$ has blocks of size one or two and satisfies the following rules:

1. Vertex $0$ is paired with a distinguished pivot $k\in\{1,\ldots,n\}$, and this pair has height one.
2. Each vertex $l\in\{1,\ldots,k-1\}$ is either a singleton or paired with one vertex strictly larger than $k$; such a pair has height $l+1$.
3. All other unpaired vertices are singletons.
Draw each pair as a rectangular arch at its assigned height and each singleton as a vertical line extending above the arches.

Write $p(\pi)$ for all pairs, including $(0,k)$; $s_l(\pi)$ and $s_r(\pi)$ for the singleton vertices respectively larger and smaller than $k$, each read in descending order; and $\delta_{p(\pi)}=\prod_{(a,b)\in p(\pi)}\delta_{j_a,j_b}$.
The statistic $\operatorname{cross}(\pi)$ counts all transverse intersections in this specific drawing.
It is not the usual single-crossing count of arbitrarily drawn semicircular pairings: nesting can produce two intersections because pair heights are fixed.

An explicit way to reconstruct the drawing count is useful.
For pairs $(a,b)$ and $(c,e)$, written with $a<b$, $c<e$, and $a<c$, their contribution is
\[
\mathbf1_{a<c<b}+\mathbf1_{a<e<b}.
\]
A singleton $s$ contributes one crossing with $(a,b)$ exactly when $a<s<b$.
Summing these contributions gives the source's rectangular statistic.
This interpretation was compared directly with the drawings on pp. 28-30.

Set $N(\pi)=\operatorname{cross}(\pi)-|s_r(\pi)|$.
Its nonnegativity, needed in Corollary 5.3, follows directly: the bottom arc $(0,k)$ crosses every vertical string based at $1,\ldots,k-1$, contributing $k-1$.
Among these vertices, $|s_r(\pi)|$ are singletons and the others start additional pairs.
Hence
\[
N(\pi)\ge k-1-|s_r(\pi)|=|p(\pi)|-1\ge0.
\tag{2}
\]
Consequently $|q^{N(\pi)}|\le1$ for all $|q|<1$, including negative $q$; at $q=0$, powers with exponent zero mean one.

## Proposition 5.1 and Its Complete Induction

With the preceding conventions, the claimed identity is
\[
\boxed{\displaystyle
\partial_i W(e_{j_n\cdots j_1})
=\sum_{\pi\in C(n+1)}
(-1)^{|p(\pi)|-1}q^{N(\pi)}\delta_{p(\pi)}
W(e_{s_l(\pi)})\otimes W(e_{s_r(\pi)}).}
\tag{3}
\]
Empty singleton lists give $1$.
The degree-one case is $\delta_{i,j_1}1\otimes1$.
The empty-word derivative is zero and can be added with an empty partition sum.

The induction uses the correct Wick recurrence
\[
W(e_{j_{n+1}\cdots j_1})
=A_{j_{n+1}}W(e_{j_n\cdots j_1})
-\sum_{h=1}^n q^{n-h}\delta_{j_{n+1},j_h}
 W(e_{j_n\cdots\widehat{j_h}\cdots j_1}).
\tag{4}
\]
The factor $\delta_{j_{n+1},j_h}$ is printed correctly in the proof on p. 27 but is missing from the introductory display on p. 6.
It is necessary already for a degree-two word with distinct colors.
No proof here uses the incorrect p. 6 display.

Differentiate (4).
The resulting terms are the leading term $\delta_{i,j_{n+1}}1\otimes W(e_{j_n\cdots j_1})$, the left action $(A_{j_{n+1}}\otimes1)\partial_iW(e_{j_n\cdots j_1})$, and the negative sum of shorter-word derivatives.
Expand the left action by the q-creation/annihilation formula and classify all terms as follows.

**The leading term.**
It is the partition with distinguished pair $(0,n+1)$ and all other vertices right singletons.
Its crossing count is $n$, its number of right singletons is $n$, its exponent is zero, and its sign is positive.

**The left-creation terms.**
For each partition of the old word, append the new vertex $n+1$ as a left singleton.
It lies outside every old arch, so all crossing counts, right-singleton counts, colors, and signs remain unchanged.
This accounts exactly for partitions of the new word where $n+1$ is a singleton.

**Cancellation of a left-annihilation term.**
Suppose the left action contracts $j_{n+1}$ with the left singleton $h=s_l(\pi)_r$, where the singleton list is $s_l(\pi)_{|s_l|}>\cdots>s_l(\pi)_1$.
Its q-power is
\[
N(\pi)+|s_l(\pi)|-r.
\]
Delete that singleton and call the resulting partition $\sigma$.
The line based at $h$ crosses exactly as many arches as there are paired left endpoints strictly above $h$.
There are $n-h$ vertices above it and $|s_l(\pi)|-r$ of these are left singletons.
Thus
\[
\operatorname{cross}(\pi)-\operatorname{cross}(\sigma)
=n-h-(|s_l(\pi)|-r).
\tag{5}
\]
Deletion preserves both the pair count and the right-singleton count.
Therefore this left-annihilation term has exactly the same q-power, color constraint, and tensor factor as the corresponding shorter-word derivative in the negative sum of (4), and the opposite sign.
They cancel bijectively.

**The remaining shorter-word terms.**
Retain physical vertex labels before renumbering.
Such a term has a removed position $h$ strictly to the right of its retained pivot.
Add the pair $(h,n+1)$.
This yields a permitted partition of the new word with $n+1$ paired, distinct from the distinguished pair.
The extra pair increases $|p|$ by one, giving exactly the minus sign in (4), and leaves the right-singleton count unchanged.
In the rectangular drawing its insertion adds $n-h$ crossings: each retained intermediate vertex contributes one endpoint or singleton intersection, with a pair having two intermediate endpoints contributing twice.
Consequently
\[
\operatorname{cross}(\sigma')-\operatorname{cross}(\sigma)=n-h,
\qquad N(\sigma')=N(\sigma)+n-h.
\tag{6}
\]
This is the contraction coefficient from (4).
Every partition with $n+1$ paired to a nondistinguished vertex is obtained uniquely in this way by deleting that pair.

The three surviving classes exhaust $C(n+2)$, proving (3) for all degrees.
On pp. 28-29 the source writes the remaining-index condition as $h\le\sigma(0)$; this uses the **renumbered shorter word**.
In the original retained labels the strict condition is $h<\text{pivot}$.
Confusing these label systems creates an apparent missing or extra pivot case.
The diagrams and arithmetic examples were checked with the correct relabeling; no contradictory case remains.

## Example 5.2 and an Independent Exact Check

At degree three, (3) gives
\[
\begin{aligned}
\partial_i W(e_{abc})={}&
\delta_{i,a}1\otimes W(e_{bc})
+\delta_{i,b}W(e_a)\otimes W(e_c)
+\delta_{i,c}W(e_{ab})\otimes1\\
&-q\delta_{i,b}\delta_{a,c}1\otimes1.
\end{aligned}
\tag{7}
\]
It agrees with direct differentiation of $W(e_{abc})=A_aA_bA_c-\delta_{b,c}A_a-q\delta_{a,c}A_b-\delta_{a,b}A_c$.
At $q=0$, (2) makes every partition with additional pairs vanish, and (3) reduces to the usual free Wick deconcatenation formula.

The durable [exact checker](../../../computations/programs/Yin_J_F0004/main.py) independently compares the complete polynomial-recurrence/Leibniz calculation with the rectangular-partition calculation for all binary words of lengths 1-6, both derivatives, and $q=0,2/7,-1/3$.
All 756 exact rational identities passed.
The [computation account](../../../computations/programs/Yin_J_F0004/readme.md#question-and-scope) gives the exact finite inputs, reproduction command, observed comparisons and precise limitations.
This finite evidence checks signs, color constraints, tensor order, and crossing counts; the all-degree conclusion rests on the induction above.

## Corollary 5.3: The Derivative Series Bound

Use the constants from [MS23-U003](Yin_U003_v1.md#ms23-u003): $t=|q|$, $c=w(q)^{-1/2}$, $C_t=\prod_{k\ge1}(1-t^k)^{-1}$, and $[n]_t!=\prod_{k=1}^n[k]_t$.
For $|w|=m$, put
\[
\eta_{i,w}=r_{iw}^*e_w\in H^{\otimes(2m+1)}.
\]
Write $\eta_{i,w}=\sum_{|v|=2m+1}\alpha_v e_v$.
Raw word vectors are not orthonormal, so these coefficients cannot be bounded by treating them as q-inner products with $e_v$.
Instead the free deletion operators extract them exactly:
\[
\alpha_v\Omega=r_v\eta_{i,w},\qquad
|\alpha_v|\le c^{2m+1}c^{m+1}\sqrt{[m]_t!}
=c^{3m+2}\sqrt{[m]_t!}.
\tag{8}
\]
This explains the inverse power $w(q)^{-(3m+2)/2}$ on p. 30.

For a raw word $v$ of length $2m+1$, (2), (3), and the homogeneous Haagerup inequality imply
\[
\begin{aligned}
\|\partial_jW(e_v)\|
&\le\sum_{\pi\in C(2m+2)}
\|W(e_{s_l(\pi)})\|\,\|W(e_{s_r(\pi)})\|\\
&\le C_t^3(2m+1)^2[2m]_t!\,|C(2m+2)|\\
&\le C_t^3(2m+1)^2[2m]_t!(2m+2)!.
\end{aligned}
\tag{9}
\]
Both singleton lengths are at most $2m$.
Thus each Haagerup degree factor is at most $2m+1$, and the product of their Hilbert word norms is at most $[2m]_t!$.
The last combinatorial bound embeds every singleton/pair partition in the symmetric group as an involution; the source's constrained family is a subset.
These estimates intentionally ignore cancellations and are uniform in the word colors.

There are $d^{2m+1}$ possible words $v$ in (8) and $d^m$ words $w$.
Combining (8)-(9), the derivative series is absolutely bounded by
\[
\begin{aligned}
&\sum_{m\ge0}\sum_{|w|=m}
t^{m(m+1)/2}\|\partial_jW(\eta_{i,w})\|\\
&\quad\le dC_t^3c^2\sum_{m\ge0}
t^{m(m+1)/2}(2m+1)^2(2m+2)!
(dc)^{3m}\sqrt{[m]_t!}\,[2m]_t!.
\end{aligned}
\tag{10}
\]
This is the source's p. 31 constant $dC_t^3/w(q)$ and factor $(d/\sqrt{w(q)})^{3m}$, visually checked in the published PDF.
An extraction rendering the latter as $(d\sqrt{w(q)})^{3m}$ must not be used.

For $0<t<1$, the ratio of consecutive summands in (10) is
\[
t^{m+1}(dc)^3
\left(\frac{2m+3}{2m+1}\right)^2
(2m+4)(2m+3)\sqrt{[m+1]_t}\,[2m+1]_t[2m+2]_t,
\tag{11}
\]
which tends to zero: q-integers are bounded for fixed $t<1$, and $t^{m+1}m^2\to0$.
Thus the quadratic crossing decay dominates both the dimension counts and the ordinary factorial in (10), for every fixed finite $d$ and every $q\in(-1,1)$.
At $q=0$, the original series has only $m=0$ and gives the usual semicircular identity $\partial_j\xi_i=\delta_{ij}1\otimes1$.

## The Graph-Closure Step

Let $\xi_i^{(N)}$ be the finite sum of the Wick-operator series in U003 over $m\le N$.
Each is a polynomial.
U003 proves $\xi_i^{(N)}\to\xi_i$ in operator norm and hence in $L^2(M)$.
Estimate (10) proves that $\partial_j\xi_i^{(N)}$ converges in the spatial operator norm to some $T_{ji}\in M\overline\otimes M$; it consequently converges in $L^2(M\overline\otimes M,\tau\otimes\tau)$ as well.
The latter Hilbert space is the target $L^2(M)\otimes L^2(M)$ of the difference quotient.

By closability, the limit pair $(\xi_i,T_{ji})$ belongs to the graph of $\overline\partial_j$.
Therefore (1) follows with
\[
\overline\partial_j\xi_i
=\sum_{m\ge0}(-1)^m q^{m(m+1)/2}
             \sum_{|w|=m}\partial_jW(r_{iw}^*e_w),
\]
where convergence is in the stated operator norm.
This supplies the graph-domain justification compressed into the final sentence of Corollary 5.3.
No interchange of an unbounded derivative with an infinite sum is assumed before checking convergence in both graph components.

## Dependencies and Verification Boundaries

The polynomial recurrence, algebraic freeness, trace representation, and derivative closability interface belong to [MS23-U001](Yin_U001_v1.md#ms23-u001).
The algebraic dual construction and its conventions belong to [MS23-U002](Yin_U002_v1.md#ms23-u002), but the derivative induction above is reproduced directly rather than inferred merely from analogy.
The conjugate series and free-deletion norm bounds are supplied by [MS23-U003](Yin_U003_v1.md#ms23-u003).

The homogeneous Haagerup theorem is the established input cited as Bozejko 1999 Proposition 2.1 and directly accepted in the precise form needed from [Dab14-U001](../Dab14/Yin_U001_v1.md#dab14-u001).
Its original proof is outside this source-unit review.
The known closability theorem is also retained with the scope described in U001; its applicability follows from the now-proved conjugate-system existence.
No unverified assumption about dual-operator boundedness enters this chain.

All pp. 26-31 passages in the assigned scope were read.
Rendered pp. 26, 28, 29, 30, and 31 were inspected for the family definition, crossings, relabeling diagrams, and estimates.
The all-degree proof, nonnegative exponent, coefficient extraction, ratio test, and graph closure were reconstructed; the exact finite checks were actually executed and recorded.
No separate errata search or formal proof-assistant verification is claimed in this unit.

## Corrections and Research Interface

The explicit repair is the missing Kronecker delta in the p. 6 Wick recurrence; p. 27 already has the correct formula.
The other clarifications are proof expansions: use the rectangular crossing statistic; keep the original-versus-renumbered pivot distinction on pp. 28-29; retain the inverse $w(q)$ powers in text extraction; and establish the closed-derivative domain by graph convergence.
With these clarifications, no unresolved gap remains in Proposition 5.1 or Corollary 5.3 under their stated hypotheses and retained external inputs.

For [Yin_S_F0008](../../../strategies/Yin_S_F0008.md#s_f0008) and [Yin_C_F0020](../../../claims/Yin_C_F0020_v1.md#yin_c_f0020), the result supplies a precise combinatorial law for q-Wick derivatives and an all-$q$ analytic decay mechanism for the particular conjugate-variable series.
It does not assert finite state dimension or exponential coefficient decay for arbitrary affiliated rational functions.
It also does not construct an all-$q$ bounded simultaneous dual system.
The full derivative formula already exhibits the additional $q$-contractions that distinguish it from free deconcatenation; extracting an arbitrary-rational-function strategy remains a separate research obligation.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | MS23, the supplied 36-page published article, Advances in Mathematics 413 (2023), 108834; printed and one-based PDF pages agree. The earlier 30-page arXiv reading and external source editions retain their separate recorded scopes. |
| source-locator | Section 5 opening, Proposition 5.1, Example 5.2 and Corollary 5.3, printed/PDF pp. 26-31; Remark 5.4 is outside this unit. |
| inspection | 2026-09-09: complete partition induction, Wick derivatives, Lipschitz estimates and graph-domain passage reconstructed and self-reviewed, with supplementary exact computation; separate reviews are recorded in the source home. Foundations and homogeneous Haagerup inputs retain their limits. This unit does not itself establish arbitrary-rational finite residual rank or an all-q bounded simultaneous dual system. |


## Current project proof review

The fresh2026-10-21 [independent finding](../../reviews/Yin_R_F0060_v1.md#ms23-u004-isolated-finding) covers the complete all-degree induction, every coefficient/norm/count/ratio estimate and the graph-limit chain.
It checks fixed local mathematics at the retained accepted-source depth; it performs no new primary-page inspection or finite execution and certifies no old reviewer isolation or date.
The [later old-findings comparison](../../reviews/Yin_R_F0060_v1.md#ms23-old-findings-comparison) preserves the original negative interface findings and distinguishes their historical evidence from this current proof review.

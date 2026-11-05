---
author: Yin
---

# Coupling classification for reduced determinants of uniform permutations

This argument addresses the complete [F0016 contract](../tasks/Yin_T_F0016_v1.md#contract).
It extends the [existing cycle-product analysis](../ledger/Yin_L_F0062_v1.md#reduced-determinants) beyond its arithmetic positive cases.
The deduction was developed on 2026-11-05 and has [independent whole-contract review](../audits/reviews/Yin_R_F0194_v1.md#finding-whole-contract).

## Statement

Let p be a fixed nonzero complex Laurent polynomial, let pi_N be uniform on S_N, and let P_N be its permutation matrix.
Use exact-zero removal with original-dimension normalization, and write
\[
 b_N(p)=\log\Delta_N^+(p(P_N)),\qquad
 c(p)=\int_{\mathbb T}\log|p(z)|\,dm(z).
\]
The four universal assertions have the following answers.

| Coupling | Full almost-sure limit to c(p), for every p | Almost-sure upper-limit equality, for every p |
| --- | --- | --- |
| Arbitrary uniform marginals | False | False |
| Independent dimensions | False | True |

More precisely, the following statements hold.

1. Every coupling satisfies \(\limsup_N b_N(p)\le c(p)\) almost surely.
2. Independent dimensions satisfy \(\limsup_N b_N(p)=c(p)\) almost surely for every fixed p.
3. There is a fixed irrational unit-circle root alpha such that, for p(z)=z-alpha and independent dimensions, \(\liminf_N b_N(p)=-\infty\) almost surely, whereas c(p)=0 and the upper limit is zero.
4. There are two fixed irrational unit-circle roots alpha_1,alpha_2 and a coupling with uniform marginals such that, for p(z)=(z-alpha_1)(z-alpha_2), \(b_N(p)\le-1\) eventually almost surely, whereas c(p)=0.

Every finite matrix in either counterexample is invertible.
The event is allowed to depend on the fixed polynomial and coupling.

## Inputs and source scope

The [retained cycle analysis](../ledger/Yin_L_F0062_v1.md#permutation-positive-cases) supplies the cycle convention and arbitrary-coupling cycle-count estimate.
The [FK--Mahler interface](../audits/literature/Den09/Yin_U001.md#mahler-measure) identifies c(p) with the free target.
All further cycle estimates used here are also derived directly below.
No arithmetic lower bound for an arbitrary irrational angle is assumed.

A bounded search on 2026-11-05 used “random permutation characteristic polynomial Liouville irrational angle almost sure determinant” and “random permutation logarithm characteristic polynomial arbitrary irrational convergence probability n”.
The inspected [Cook--Zeitouni abstract, arXiv:1806.07549v1](https://arxiv.org/abs/1806.07549v1) concerns the maximum characteristic polynomial and Diophantine sensitivity; it is related context, not a theorem used here.
The existing Zei13 inspection supplies the cycle formula and its finite-type boundary.
The recurrence observation below is standard: [Tao's 254A Lecture 3, Theorem 2 and equation (4)](https://terrytao.wordpress.com/2008/01/13/254a-lecture-3-minimal-dynamical-systems-recurrence-and-the-stone-cech-compactification/) states bounded gaps for simultaneous torus returns.
That original HTML statement and its application were inspected under [the Tao08 source scope](../audits/literature/Tao08/readme.md), and a direct compactness proof is included below.
This search establishes neither novelty nor absence of earlier versions of this classification.

## Argument

### Reduced cycle products

Factor
\[
 p(z)=a z^h\prod_{j=1}^d(z-\alpha_j),\qquad a\ne0,
\]
with nonzero roots counted with multiplicity; monomials have d=0.
Let Z be the finite set of roots of p that are roots of unity, let mu_k be the set of k-th roots of unity, and put
\[
 E_k=Z\cap\mu_k,\qquad
 B_k(p)=\sum_{\zeta\in\mu_k\setminus E_k}\log|p(\zeta)|.
\]
An empty sum is zero.
If C_k(pi_N) counts k-cycles, block diagonalization gives
\[
 N b_N(p)=\sum_{k=1}^N C_k(\pi_N)B_k(p).
 \tag{1}
\]
Deletion is performed for the whole polynomial, without asserting multiplicativity of reduced determinants with different zero sets.
The coefficient contributes (k-|E_k|)log|a|, and the Laurent monomial contributes zero.
If alpha_j is not in E_k, its contribution is
\[
 \log|\alpha_j^k-1|-\sum_{\zeta\in E_k}\log|\zeta-\alpha_j|.
 \tag{2}
\]
If alpha_j is in E_k, differentiation of z^k-1 instead gives
\[
 \log k-\sum_{\zeta\in E_k\setminus\{\alpha_j\}}\log|\zeta-\alpha_j|.
 \tag{3}
\]
The finite deleted-location sums in (2)--(3) involve fixed nonzero distances, and multiplicities repeat these contributions.
Off-circle roots satisfy log|alpha_j^k-1|=k log^+|alpha_j|+O_p(1).
A root of unity not in E_k has a nonzero power in a fixed finite set.
Irrational unit-circle roots have the upper bound log|alpha_j^k-1|<=log 2.
Therefore, for a fixed C_p and every k>=1,
\[
 B_k(p)\le k c(p)+C_p\log(k+1),\qquad
 c(p)=\log|a|+\sum_j\log^+|\alpha_j|.
 \tag{4}
\]
If every irrational unit-circle root satisfies |1-alpha_j^k|>=delta>0, the same identities give
\[
 |B_k(p)-k c(p)|\le C_{p,\delta}\log(k+1).
 \tag{5}
\]
The constants include small k and possible empty products.

### Cycle count and the universal upper bound

Insertion of the last symbol gives
\[
 \mathbb E t^{K_N}=\frac{t(t+1)\cdots(t+N-1)}{N!},\qquad K_N=\sum_k C_k(\pi_N).
\]
Thus E 2^{K_N}=N+1, and
\[
 \mathbb P\{K_N>6\log(N+1)\}\le(N+1)^{1-6\log2}.
\]
This is summable, so first Borel--Cantelli yields K_N=O(log(N+1)) almost surely under every coupling.
Equations (1) and (4), with sum k C_k=N, imply
\[
 b_N(p)\le c(p)+C_p K_N\log(N+1)/N.
 \tag{6}
\]
This proves the universal upper bound.

### Independent upper-limit equality

List the distinct irrational unit-circle roots as beta_1,...,beta_s.
If s=0 take G to be all positive integers.
Otherwise put g=(beta_1,...,beta_s) in a torus.
Since no beta_j is 1, a sufficiently small neighborhood of g has all coordinates at distance at least some delta>0 from 1.
The integers n with g^n sufficiently close to the identity have bounded gaps.
Indeed, take a finite epsilon-net for the compact closure of {g^n:n in Z}, with net points g^{j_1},...,g^{j_t} in the orbit.
For every integer n, distance(g^n,g^{j_i})<epsilon for some i, hence distance(g^{n-j_i},1)<epsilon by translation invariance.
The finite range of the j_i bounds the gaps in return times.
Translating by 1 gives a set G of positive integers with bounded gaps and
\[
 |1-\beta_j^N|\ge\delta\quad(N\in G,\ 1\le j\le s).
 \tag{7}
\]
In particular sum_{N in G}1/N diverges.
A uniform permutation is one N-cycle with probability 1/N.
Under independence across dimensions these events for N in G are independent, so second Borel--Cantelli gives infinitely many almost surely.
At those dimensions b_N(p)=B_N(p)/N, which tends to c(p) by (5) and (7).
Together with (6) this proves the independent upper-limit equality.
Convergence in probability is not asserted or needed.

### Explicit alternating irrational resonances

For positive integers q put
\[
 T(q)=\lceil2q\exp(q^2)\rceil.
\]
Set Q_1=2, Q_2=8 and, for n>=1, set
\[
 Q_{n+2}=Q_{n+1}\left\lceil\exp(10T(Q_{n+1}))\right\rceil.
 \tag{8}
\]
Every Q_n divides Q_{n+1}, and successive terms grow by more than a factor of three.
Define
\[
 \theta_1=\sum_{k\ge1}Q_{2k-1}^{-1},\qquad
 \theta_2=\sum_{k\ge1}Q_{2k}^{-1},\qquad
 \alpha_i=\exp(2\pi i\theta_i).
 \tag{9}
\]
For n of the corresponding parity, the partial sum through 1/Q_n is an integer divided by Q_n, and its strictly positive tail is at most 2/Q_{n+2}.
If theta_i=a/b were rational, its positive difference from that partial sum would be at least 1/(bQ_n), contradicting the tail bound for arbitrarily large n of that parity.
Both theta_i are therefore irrational.
Using |exp(2 pi i x)-1|<=2 pi distance(x,Z), we obtain
\[
 |1-\alpha_i^{Q_n}|\le\frac{4\pi Q_n}{Q_{n+2}}
 \le\exp(-8T(Q_{n+1})).
 \tag{10}
\]
The last inequality follows from (8), Q_n<Q_{n+1} and 4pi<=exp(2T(Q_{n+1})).
The resonances are nonzero because the angles are irrational.

### Independent full-limit counterexample

Take p_1(z)=z-alpha_1, so c(p_1)=0.
For each odd n put q=Q_n and use the q dimensions q<=N<2q.
At any such dimension a permutation has at most one q-cycle and has one with probability 1/q.
Indeed, choosing its q symbols, cyclic order and remaining permutation gives expected q-cycle count binomial(N,q)(q-1)!(N-q)!/N!=1/q.
The block-event probability under independent dimensions is
\[
 1-(1-1/q)^q\ge1-e^{-1}.
\]
Successive odd-n blocks are disjoint, so the independent block events occur infinitely often almost surely.
At any selected dimension having a q-cycle, (10) gives log|1-alpha_1^q|<=-q^2.
Every other cycle contributes at most log 2, hence
\[
 b_N(p_1)\le-\frac{q^2}{N}+\frac{K_N\log2}{N}
 \le-\frac q2+\frac{K_N\log2}{N}.
\]
The cycle-count bound proves liminf b_N(p_1)=-infinity almost surely.
The independent upper-limit theorem gives limsup b_N(p_1)=0.
Thus the full-limit assertion fails in both universal coupling regimes.

### Arbitrary-coupling upper-limit counterexample

Take p_2(z)=(z-alpha_1)(z-alpha_2), so c(p_2)=0.
For N>=T(Q_1), choose the unique n with T(Q_n)<=N<T(Q_{n+1}), put q=Q_n, and choose i by the parity of n.
Define
\[
 M_N=\sum_{1\le t\le\lfloor N/(2q)\rfloor}C_{tq}(\pi_N),\qquad A_N=\{M_N>0\}.
\]
Counting ordered disjoint cycles gives E C_l=1/l, E(C_l C_h)=1/(lh) when l!=h and l+h<=N, and E(C_l(C_l-1))=1/l^2 when 2l<=N.
These formulas follow by selecting the disjoint symbol sets, cyclic orders and an arbitrary remaining permutation, and cancelling factorials against N!.
All lengths used in M_N are at most N/2, so
\[
 \mu_N:=\mathbb E M_N=\frac1q H_{\lfloor N/(2q)\rfloor},\qquad
 \mathbb E M_N^2=\mu_N^2+\mu_N.
\]
The estimate H_floor(x)>=log x for x>=1 and N>=2q exp(q^2) imply mu_N>=q.
Cauchy--Schwarz applied to M_N 1_{A_N} gives
\[
 a_N:=\mathbb P(A_N)\ge\frac{\mu_N}{1+\mu_N}\ge\frac q{q+1}\longrightarrow1.
 \tag{11}
\]
On A_N a cycle has length l=tq<=N/2.
Since |1-w^t|<=t|1-w| for |w|=1, (10) yields
\[
 \log|1-\alpha_i^l|\le\log t-8T(Q_{n+1})
 \le-7T(Q_{n+1})\le-7N.
\]
Every remaining root factor is at most 2, and the total number of factors is 2K_N<=2N.
Therefore, on A_N,
\[
 b_N(p_2)\le-7+2\log2<-1.
 \tag{12}
\]

For an explicit lawful coupling, take a single V uniform on (0,1).
If 0<a_N<1, sample pi_N uniformly conditional on A_N when V<=a_N, and uniformly conditional on its complement otherwise, using additional independent variables for these finite conditional samples.
When a_N=1 sample uniformly from A_N; handle the finitely many earlier dimensions unconditionally.
The mixture weights a_N and 1-a_N make each marginal exactly uniform on S_N.
Since a_N tends to one, almost every V<1 is eventually below every a_N.
Thus A_N holds eventually almost surely in this coupling, and (12) gives limsup b_N(p_2)<=-1<0=c(p_2).
Neither alpha_i is a root of unity, so p_2(P_N) is always invertible.
This proves all four conclusions.

## Current assessment

[Selected decision](#decision-classification-reviewed)

## Assessment history

### Decision classification-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:24 |
| status | open |
| reason | A complete candidate classifies all four coupling assertions; mathematical review and whole-contract adoption remain pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Four coupling assertions](#statement) | Exact reduced convention, all fixed nonzero complex Laurent polynomials and both cross-size coupling regimes. |
| argument | [Cycle and coupling argument](#argument) | Universal upper bound, independent upper-limit equality, fixed independent full-limit counterexample and fixed arbitrary-coupling upper-limit counterexample. |

### Decision classification-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:29 |
| status | proved |
| reason | Independent review checked the complete fixed argument and all four assertions against the original F0016 contract, including exact-zero removal and both coupling laws. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Four coupling assertions](#statement) | Exact reduced convention, every fixed nonzero complex Laurent polynomial, both assertions and both cross-size coupling regimes. |
| argument | [Complete argument](#argument) | Whole reduced cycle calculation, universal bound, independent positive theorem and both fixed counterexamples. |
| dependency | [Mahler and FK target](../audits/literature/Den09/Yin_U001.md#den09-u001) | Finite logarithmic integral, Jensen root formula and the normalized free target, using only the recorded Mahler, FK and Fourier interfaces of this exact unit. |
| review | [Independent whole-contract finding](../audits/reviews/Yin_R_F0194_v1.md#finding-whole-contract) | Complete statement, argument, source interfaces, counterexample laws and comparison with the unchanged Task contract; no unresolved gap found. |

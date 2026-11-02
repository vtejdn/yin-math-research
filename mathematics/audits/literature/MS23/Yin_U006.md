---
author: Yin
---

# MS23: The One-Variable Model

<a id="ms23-u006"></a>
## MS23-U006: Recursion, q-Falling Factorials and the Vacuum Adjoint

Source: [MS23 published PDF](../../../literature/pdf/MS23.pdf), Section 3, pp. 10-14.
Date: 2026-09-09.
Reconstruction: the coordinating agent; the [original complete one-variable review](../../reviews/Yin_R_F0104_v1.md#ms23-u002-original-finding) retains its unknown initial-context relationship and exact scope.
All statements and local proof steps of Proposition 3.3 and Corollary 3.4 are reconstructed below.
Remark 3.5 is a supplementary comparison with explicit retained orthogonal-polynomial inputs.

### Exact statement

For one generator write e_n=e^(tensor n), e_0=Omega.
Then ||e_n||_q^2=[n]_q!, with [n]_q=(1-q^n)/(1-q), and

\[
Ae_n=e_{n+1}+[n]_q e_{n-1}.
\]

Normalization and [D,A]=P_Omega force

\[
De_0=0,\quad De_1=e_0,\quad
De_{n+1}=ADe_n-[n]_qDe_{n-1}\quad(n\ge1).
\tag{1}
\]

Define P_q(a,b)=product_{j=0}^{b-1}[a-j]_q for b>=0, with empty product one.
On the valid range a>=b this is [a]_q!/[a-b]_q!.
Proposition 3.3 states

\[
De_n=\sum_{k=1}^{\lceil n/2\rceil}
(-1)^{k-1}q^{k(k-1)/2}P_q(n-k,k-1)e_{n-2k+1}.
\tag{2}
\]

This is an algebraic finite sum on F_alg and so defines a densely defined operator for -1<q<1.
The q=0 specialization is right deletion.
At q=-1 the quotient sends e_2 to zero but the recursion requires De_2=e_1, so the endpoint cannot be included.
The source's exclusion is necessary, not a norm-estimate artifact.

### Full coefficient induction, including boundaries

Let c_(n,k) be the coefficient in (2), setting it to zero outside its valid degree range.
Formula (1) is equivalent to

\[
c_{n+1,k}=c_{n,k}+[n-2k+3]_q c_{n,k-1}-[n]_q c_{n-1,k-1}.
\tag{3}
\]

For k=1 the coefficient is one.
For k>=2 and n>=2k-2, factor the two falling products in the last two terms to obtain

\[
[n-2k+3]_qP_q(n-k+1,k-2)-[n]_qP_q(n-k,k-2)
=-q^{n-k+1}[k-1]_qP_q(n-k,k-2).
\]

Meanwhile

\[
P_q(n-k+1,k-1)-P_q(n-k,k-1)
=q^{n-2k+2}[k-1]_qP_q(n-k,k-2).
\]

Multiplying these identities by the respective signs and powers in (2) proves (3), since their exponents differ exactly by k-1.
At the new lowest-degree term n=2k-2, the extended product representing c_(n,k) contains [0]_q and vanishes; the same identities still apply.
Outside these ranges every contributing coefficient is zero.
This supplies a uniform induction and avoids the source's intermediate appearances of formally negative falling-product lengths.
The base cases n=0,1 finish the proof.

**Source correction, Example 3.1, p. 11:** the displayed e_3 coefficient of De_6 is missing its linear q term inside the parentheses.
The corrected identity is

\[
De_6=e_5-q(1+q+q^2+q^3)e_3
+q^3(1+q)(1+q+q^2)e_1.
\]

The printed Proposition 3.3 formula and the defining recursion agree with this correction.
The exact [computation record](../../../computations/programs/Yin_J_F0003/readme.md#question-and-scope) supplements the induction; finite agreement is not used to establish (2).

### Corollary 3.4: the vacuum coefficient defines an L2 functional

Only odd input degrees contribute to <De_n,Omega>:

\[
\langle De_{2m-1},\Omega\rangle_q
=(-1)^{m-1}q^{m(m-1)/2}[m-1]_q!.
\]

Since the e_n are orthogonal rather than normalized, the representing vector is

\[
\xi=D^*\Omega
=\sum_{m\ge1}(-1)^{m-1}q^{m(m-1)/2}
\frac{[m-1]_q!}{[2m-1]_q!}e_{2m-1}.
\tag{4}
\]

Its squared norm is

\[
\sum_{m\ge1}|q|^{m(m-1)}\frac{([m-1]_q!)^2}{[2m-1]_q!}.
\tag{5}
\]

For 0<|q|<1, the ratio of successive nonnegative summands is |q|^(2m)[m]_q^2/([2m]_q[2m+1]_q), which tends to zero.
At q=0 only m=1 survives.
Cauchy-Schwarz in the orthogonal basis now proves the required boundedness of the vacuum functional on all finite vectors; thus Omega is actually in dom(D*), rather than merely a formal notation.
[U001](Yin_U001.md#ms23-u001) identifies xi as the conjugate variable and proves closability.

The source observes that the scalar series of numbers in (5) also converges at q=1, where the ratio tends to 1/4.
This observation alone does not extend the paper's bounded-generator q-Fock theorem to the bosonic endpoint.
No q=-1 endpoint or whole-operator norm bound for D follows from (5).

### Remark 3.5: a consistency comparison, not a premise of the main theorem

Use the monic Chebyshev normalization U_0=1, U_1=x, U_(n+1)=xU_n-U_(n-1), C_1=x and C_n=U_n-U_(n-2) for n>=2.
The q-Hermite connection stated on p. 13 is

\[
U_n(x\sqrt{1-q})
=\sum_{k=0}^{\lfloor n/2\rfloor}(-1)^k q^{k(k+1)/2}
{n-k\brack k}_q(1-q)^{(n-2k)/2}H_{n-2k}(x|q).
\tag{6}
\]

The source retains its orthogonal-polynomial reference [8], Lemma 5.57.
The finite connection is also checkable by substituting the two three-term recurrences and the q-binomial identity; no interchange of infinite sums is involved in (6).
Its vacuum coefficient gives tau(U_(2n)(A sqrt(1-q)))=(-1)^n q^(n(n+1)/2), with odd moments zero.

The general Chebyshev conjugate formula quoted from MS17, Exercise 8.12, then gives

\[
\sqrt{1-q}\sum_{n\ge0}(-1)^nq^{n(n+1)/2}
C_{2n+1}(A\sqrt{1-q}).
\tag{7}
\]

This quoted general formula is retained as an optional external comparison, not independently proved here or needed by (1)-(5).
Its application has no convergence problem: the spectrum of A sqrt(1-q) is [-2,2] by [BKS97-U001](../BKS97/Yin_U001.md#bks97-u001), the corresponding first-kind Chebyshev polynomials have uniform bound two, and the q powers are summable.
The factor sqrt(1-q) follows from the inverse scaling of a conjugate variable.

Expanding (7) with (6) is absolutely legitimate: for fixed |q|<1 the absolute q-binomial coefficients are uniformly bounded by convergent-product constants, the Wick norms grow at most exponentially in degree times a linear factor, and the outer q^(n(n+1)/2) defeats those factors and the finite number of inner terms.
Uniqueness of the conjugate variable forces the resulting coefficient of e_(2m+1) to equal (4).
This proves the source's otherwise unexplained final q-series identity **conditional on its explicitly retained general Chebyshev formula**; it is not an additional dependency of Corollary 3.4.

### Verification scope

All pp. 10-14 were text-read and the recursive displays, q-factorials, conjugate coefficients and Chebyshev comparison were visually inspected.
The uniform all-n coefficient proof above repairs the induction's boundary notation; the isolated De_6 example is corrected.
The main one-variable result has no unresolved local proof gap.
The optional orthogonal-polynomial comparison retains its stated external identities and is not a whole-book review of either source.

## Source and inspection

Source edition: MS23, the supplied 36-page published article, Advances in Mathematics 413 (2023), 108834; printed and one-based PDF pages agree.
The earlier 30-page arXiv reading and external source editions retain their separate recorded scopes.

Passages: Section 3, Proposition 3.3, Corollary 3.4 and the supplementary Remark 3.5 comparison, printed/PDF pp. 10-14.

Inspection: 2026-09-09: the main one-variable recursion, closed formula and conjugate series were reconstructed with all-n and endpoint corrections; separate review is recorded in the source home.
The optional q-series/Chebyshev comparison remains conditional on its explicitly retained general formula and is not a dependency of Corollary 3.4 or a whole-book audit.

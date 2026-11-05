---
author: Yin
---

# Random diagonal quantiles and all-dimension purely imaginary Wigner floors

This is a project deduction, with no novelty or priority claim.
It extends the [reviewed seventh-version package](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) by proving that its purely imaginary symmetric-quantile guard has exponentially small failure when the independent real diagonal law is nonconstant.
The [current decision](#decision-random-diagonal-reviewed) adopts this scope after independent whole-proof review; the earlier physical versions retain their adopted results and actual review limits.
The quantile lemma is proved here by finite-dimensional singular-subspace comparisons and a bounded independent-variable calculation.
The only adopted probability-floor input is the exact guarded theorem in C_F0194_v7; its complete proof is reused rather than duplicated.

<a id="statement"></a>
## Exact assertions and boundaries

Singular values are in decreasing order.
For N sufficiently large put
\[
 r_N=\lfloor\sqrt N\rfloor,\qquad
 k_N=4r_N+3\le N,\qquad
 \ell_N=k_N-2=4r_N+1\le N-1.
\]
Let zeta be any fixed nonconstant real random variable, and let zeta_1,...,zeta_N be independent copies.
No global moment assumption on zeta is required for the following quantile assertion.
For any deterministic complex N-by-N matrix G put
\[
 S_N=G+N^{-1/2}\operatorname{diag}(\zeta_1,\ldots,\zeta_N),
 \qquad S_{N,-i}=S_N[[N]\setminus\{i\}].
\]
There are c0,c,C>0 and N0, depending only on the fixed law, such that
\[
 \sup_{G\in M_N(\mathbb C)}
 P\left\{s_{k_N}(S_N)<c_0N^{-1/2}
       \ \text{or}\ \min_{1\le i\le N}s_{\ell_N}(S_{N,-i})<c_0N^{-1/2}\right\}
 \le C e^{-cN},\qquad N\ge N_0.
 \tag{Diagonal-quantile}
\]
There is no symmetry or magnitude restriction on G.
The same bound holds for an arbitrary random G_N independent of the entire diagonal vector, by conditioning within each dimension.
The elementary perturbation, low-rank and principal-compression inequalities and bounded-variable estimate proved below are included at their displayed scopes.

For the least-value application, fix a real law eta with E eta=0 and E eta^2=1, and a nonconstant real law zeta with finite second moment.
The latter need not be centered.
Let W_N be Hermitian with independent strict upper entries i eta_jk/sqrt(N), conjugate lower entries, and independent diagonal entries zeta_j/sqrt(N), with the two families independent.
The laws are fixed with dimension.
For every gamma,B>0 there are fixed A,C_B,C,N0, depending only on the two laws,gamma,B, such that
\[
 \sup_{\max_{j,k}|F_{jk}|\le N^\gamma}
 P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Pure-imaginary-nonconstant-diagonal-floor}
\]
Here F may be any deterministic complex matrix, with no symmetry restriction and no parity restriction on N.
For F_N independent of the whole W_N, define Gamma_N={max|F_N,jk|<=N^gamma}.
The same right side bounds P(s_min(W_N+F_N)<=N^(-A),Gamma_N); add P(Gamma_N^c) for the unguarded probability.
All constants are uniform over the displayed shift class, and arbitrary coupling between dimensions is allowed.

More precisely, for D_i=(W_N+F)[[N] minus {i}], the exact guard used in C_F0194_v7 at L0=1 is
\[
 \Sigma_N(F,1)=\bigcap_{i=1}^N
       \{s_{\ell_N}(\operatorname{sym}D_i)\ge N^{-1}\},
 \qquad\operatorname{sym}D=(D+D^T)/2.
\]
The new argument gives P(Sigma_N(F,1)^c)<=C exp(-cN) uniformly over every deterministic complex F, without an entry bound, and over every independent random F_N.
It does not condition on this guard or assume it is independent of the noise.

For a constant diagonal law zeta=a, the uniform quantile assertion fails after choosing G=-aI/sqrt(N).
In the Wigner application the same deterministic shift cancels that diagonal, and every odd-dimensional realization is transpose-skew and singular.
Under the Tasks' centered-diagonal convention, the excluded constant law is exactly the identically zero law.
The preceding purely imaginary guarded and even-skew results retain their own scopes at C_F0194_v7.
The new floor error is not claimed summable, and no general matrix-coefficient determinant assertion, polynomial determinant transfer, Brown-measure conclusion or original Task completion is part of this statement.

<a id="argument"></a>
## Complete proof and exact adopted input

The [accepted seventh-version decision](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) supplies only its [purely imaginary quantile-guarded floor](Yin_C_F0194_v7.md#quantile-guard-floor), with its actual law hypotheses, independent-random-shift form and recorded source/review limits.
The argument below discharges that guard through a new uniform diagonal estimate.
All singular-subspace and bounded-variable calculations used in that estimate are provided here; no additional external probability theorem is invoked.
The earlier constant-diagonal skew obstruction is also verified directly below at the present shifted scope.

<a id="quantile-proof"></a>
## Random-diagonal quantile proof

### Elementary singular-direction facts

For a square matrix A, s_j(A) is the largest a for which some j-dimensional complex subspace E has ||Ax||>=a||x|| for every x in E.
Indeed the span of the first j right singular vectors achieves a=s_j(A); every j-dimensional subspace meets the span of the last n-j+1 right singular vectors, which gives the reverse bound.
This also applies to a subspace of larger dimension by restricting it to dimension j.
The following comparisons are direct consequences of this description.

If ||E||<=e, then s_j(A+E)>=s_j(A)-e, by the triangle inequality on a top j-dimensional singular subspace of A.
If Q has rank at most r and B has at least t singular values at least a, intersect its t-dimensional good subspace with ker Q.
The intersection has dimension at least t-r, and (B+Q)x=Bx there, so s_(t-r)(B+Q)>=a whenever t>r.
If A_I is a principal compression, a good input subspace for A_I lifts by zero extension to one for A, because deleting output coordinates can only decrease the norm.
Thus s_j(A)>=s_j(A_I) whenever the right side is defined.
Finally let E be a k-dimensional good subspace for A and fix a coordinate i.
Impose x_i=0 and (Ax)_i=0 on E; these are two complex linear equations, so their common solution space has dimension at least k-2.
Deleting coordinate i identifies that space isometrically with a subspace on which A_-i has exactly the same action norm.
Hence s_(k-2)(A_-i)>=s_k(A) for k>=3, simultaneously for every i as a deterministic implication.

### A bounded independent-variable estimate

Put a0=1-e^(-1)-1/2>0.
If Y_1,...,Y_m are independent, 0<=Y_j<=L and E Y_j>=mu>0, then
\[
 P\left\{\sum_jY_j\le\frac{\mu m}{2}\right\}
 \le\exp(-a_0\mu m/L).
\]
For 0<=y<=L, convexity gives e^(-y/L)<=1-(1-e^(-1))y/L.
Independence and 1-t<=e^(-t) bound the expectation of exp(-sum Y_j/L) by exp(-(1-e^(-1))mu m/L).
Markov's inequality on the displayed lower-tail event adds the factor exp(mu m/(2L)), proving the claim.
This is the only concentration calculation used in the quantile argument.

### Bounded truncation with positive conditional variance

Choose two disjoint bounded intervals, separated by a positive distance, each of positive zeta probability.
They exist because the real law is not constant.
Choose M>=1 with both intervals inside [-M,M], and set
\[
 q=P(|\zeta|\le M)>0,\qquad
 v=\operatorname{Var}(\zeta\mid |\zeta|\le M)>0.
\]
The conditional variance is positive because both separated intervals retain positive conditional mass, and v<=M^2.
Let I={j:|zeta_j|<=M} and m=|I|.
The preceding estimate applied to independent membership indicators gives P(m<qN/2)<=exp(-a0 qN).
Conditional on any membership set I of positive probability, its retained zeta_j remain independent with the bounded conditional law.
Write G_I=G[I,I] and S_I=S_N[I,I], using the inherited coordinate order.
For deterministic G the compression G_I is fixed after this conditioning.
In the remaining conditional argument retain only m>=qN/2; the smaller membership sets are included in the preceding failure bound.

### Large deterministic directions or bounded Frobenius mass

Take the singular-value decomposition of G_I and split G_I=G_big+G_small, retaining exactly the singular values strictly greater than 2M/sqrt(N) in G_big.
Write r=rank G_big, so ||G_small||<=2M/sqrt(N).
This splitting can be defined by the spectral projection of G_I*G_I above 4M^2/N and is measurable even at repeated singular values.

If r>=k_N, boundedness of the retained diagonal and the first comparison give
\[
 s_{k_N}(S_I)\ge s_{k_N}(G_I)-M/\sqrt N>M/\sqrt N.
\]
Suppose instead r<k_N, and put B=G_small+diag(zeta_j:j in I)/sqrt(N).
Then ||B||<=3M/sqrt(N).
For each j in I let X_j=|sqrt(N)(G_small)_jj+zeta_j|^2.
Conditional on I, these variables are independent, lie in [0,9M^2], and have expectations at least v, because for every complex w,
\[
 E|w+\zeta|^2
 =\operatorname{Var}(\zeta)+|w+E\zeta|^2\ge\operatorname{Var}(\zeta)
\]
under the bounded conditional law.
The independent-variable estimate gives, outside probability exp(-a0 v m/(9M^2)),
\[
 \|B\|_F^2\ge\frac1N\sum_{j\in I}X_j\ge\frac{vm}{2N}.
\]

Put c0=sqrt(v)/2 and let t be the number of singular values of B at least c0/sqrt(N).
The operator bound and the remaining singular-value upper bounds imply
\[
 \frac{vm}{2N}\le\|B\|_F^2
 \le\frac{9M^2t}{N}+\frac{v(m-t)}{4N}
 \le\frac{9M^2t}{N}+\frac{vm}{4N}.
\]
Thus t>=delta m, where delta=v/(36M^2)>0.
Choose N0 so that m>=qN/2 implies delta m>=2k_N and k_N<=m, for every N>=N0.
Since r<k_N, the rank comparison applied to S_I=B+G_big leaves at least k_N good directions and gives s_(k_N)(S_I)>=c0/sqrt(N).
The large-r branch has the same bound because c0<=M/2.

The conditional failure bound is uniform over I and G, and m>=qN/2 makes it at most exp(-a0 v q N/(18M^2)).
Adding the membership failure proves the asserted exponential probability with, for example, C=2 and c=min(a0 q,a0 v q/(18M^2)).
Principal compression transfers the bound to S_N itself, and the two-coordinate-constraint comparison transfers it simultaneously to every S_(N,-i) at index ell_N.
No union over the deleted coordinates is needed.
For an independent random G, integrate the uniform deterministic estimate conditional on G; no bound on that random G is required.

<a id="pure-imaginary-application"></a>
## Application to a purely imaginary Wigner input

Let W_N have independent upper entries i eta_jk/sqrt(N), conjugate lower entries, and independent real diagonal entries zeta_j/sqrt(N), with the two families independent.
The real eta law is fixed, centered and variance one; zeta is fixed, nonconstant and has finite second moment, without a centering requirement.
For deterministic complex F, sym(W_N+F)=sym F+diag(zeta_j)/sqrt(N).
The preceding quantile theorem applies with G=sym F, and its simultaneous principal-compression bound implies the exact C_F0194_v7 guard with L0=1 once c0/sqrt(N)>=N^(-1).
Its failure is at most C exp(-cN), uniformly over all F, with no entry bound needed for this guard assertion.

Now impose max|F_jk|<=N^gamma to apply the [accepted guarded probability floor](Yin_C_F0194_v7.md#quantile-guard-floor) with L0=1.
For every gamma,B>0 some fixed A,C_B,C,N0 give
\[
 \sup_{\max|F_{jk}|\le N^\gamma}
 P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}N^{-1/18}.
\]
The exponential guard failure has been absorbed into the arbitrary-power term by changing its constant and dimension threshold.
This is an all-dimension probability floor with no parity restriction.
It does not make the matching error summable.

For F_N independent of the whole W_N, the quantile assertion follows by conditioning on F_N because sym F_N is independent of the entire diagonal family.
Define Gamma_N={max|F_N,jk|<=N^gamma}.
The same probability bound holds for the least-value event intersected with Gamma_N, and adding P(Gamma_N^c) gives the unguarded bound.
Only F_N is conditioned on; the symmetric-quantile event may be correlated with W_N and is handled by set inclusion.
No independence between dimensions is required.

<a id="constant-diagonal-boundary"></a>
## Noncentered and constant-law boundaries

The quantile proof uses positive conditional variance, so a nonzero mean creates no obstruction and is absorbed by the arbitrary complex center in each squared diagonal term.
For a constant law zeta=a, however, choosing G=-aI/sqrt(N) makes S_N zero, disproving any uniform positive quantile conclusion of this kind.
In the Wigner application the deterministic shift F=-aI/sqrt(N) cancels that diagonal and leaves a transpose-skew matrix.
For odd N its determinant is zero because det A=det A^T=det(-A)=-det A.
This shift satisfies any fixed positive polynomial entry bound for all sufficiently large N.
Therefore nonconstancy cannot be removed from the all-dimension arbitrary-shift floor, even when a is nonzero.
Under the Tasks' centered-diagonal convention, the excluded constant law is exactly the identically zero law.
The accepted even-skew result and the general guarded result remain available for that boundary under their own hypotheses.
This deduction supplies neither the matrix-coefficient determinant assertion nor the full-sequence Brown-measure assertion of the original Tasks.

## Current assessment
[Selected decision](#decision-random-diagonal-reviewed)

## Assessment history

### Decision random-diagonal-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T13:49 |
| status | open |
| reason | A complete candidate proves an exponential random-diagonal singular quantile for arbitrary complex shifts and uses the accepted seventh-version guarded floor to obtain an all-dimension purely imaginary least-value estimate for nonconstant finite-second-moment real diagonals. Independent review remains to be performed; no original Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Random-diagonal and purely imaginary assertions](#statement) | Exact exponential quantile, simultaneous principal compressions, elementary auxiliary comparisons, independent random G, nonconstant-diagonal all-dimension floor, random-shift guard, noncentered and constant-law boundaries. |
| argument | [Complete new proof](#argument) | Bounded conditional variance, elementary exponential estimate, deterministic singular split, Frobenius count, rank/compression comparisons, and the exact guarded-floor application and boundaries. |
| dependency | [Accepted purely imaginary guarded floor](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) | Only the exact purely imaginary symmetric-quantile guarded floor at L0=1 and its independent-random-shift form, with unchanged source and proof-inspection limits; the new diagonal guard is established here. |

### Decision random-diagonal-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T13:59 |
| status | proved |
| reason | Independent whole-proof review supports the uniform exponential random-diagonal quantile, all simultaneous principal-compression and independent-random-shift conclusions, and the all-dimension purely imaginary floor under a nonconstant finite-second-moment diagonal law. The sole accepted guarded-floor input is resolved at its exact scope; constant-diagonal, nonsummability and original Task boundaries remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Random-diagonal and purely imaginary assertions](#statement) | Exact exponential quantile, simultaneous principal compressions, elementary auxiliary comparisons, independent random G, nonconstant-diagonal all-dimension floor, random-shift guard, noncentered and constant-law boundaries. |
| argument | [Complete new proof](#argument) | Bounded conditional variance, elementary exponential estimate, deterministic singular split, Frobenius count, rank/compression comparisons, and the exact guarded-floor application and boundaries. |
| dependency | [Accepted purely imaginary guarded floor](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) | Only the exact purely imaginary symmetric-quantile guarded floor at L0=1 and its independent-random-shift form, with unchanged source and proof-inspection limits; the new diagonal guard is established here. |
| review | [Independent random-diagonal whole-proof finding](../audits/reviews/Yin_R_F0200_v8.md#random-diagonal-whole-proof) | Entire exact statement and proof, elementary auxiliary assertions, bounded conditional-law and singular split, Frobenius count, sole guarded-floor interface, random-shift conditions and constant-law boundary; no unresolved mathematical gap in this scope. |

---
author: Yin
---

# Which higher product-fiber moments test spatial decay without forcing closed range?

## Statement

Fix a pattern-free torsion-free four-line group \(G\) with its rose word length, and a finite group-ring matrix \(A\) with \(m\) columns.
Write \(B=A^*A/M\), choosing \(M>\|A\|^2\), \(Q_k=(I-B)^k\), and \(p=1_{\{0\}}(B)\).
Use the canonical group trace and the unnormalized matrix trace.
For \(s\ge0\) form the endpoint-weighted paired-word sum
\[
 F_k(s)=\sum_{g}e^{-s|g|}\|\widehat Q_k(g)\|_{\rm HS}^2,\qquad
 D_k(s)=\sum_{h=0}^4(-1)^h\binom4h F_k(hs).
\]
Each \(F_k\) groups the two length-\(k\) matrix products by their common endpoint in the original group.
The coefficients of the two words, including their internal matrix indices and complex phases, enter before squaring.
For \(3<\beta<4\) the following hold.

1. The weighted square sum \(\sum_g (1+|g|)^\beta\|\widehat p(g)\|_{\rm HS}^2\) is finite if and only if
   \[
          \sum_{j\ge0}2^{\beta j}\lim_{k\to\infty}D_k(2^{-j})<\infty .
   \]
   This would imply an integral kernel trace by the [spatial criterion](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace). Existence of such a \(\beta\) is equivalent to finiteness at some exponent strictly above three.
2. Requiring \(\liminf_{k\to\infty}\sum_{j\ge0}2^{\beta j}D_k(2^{-j})<\infty\) is equivalent to \(A\) having closed range.
   For every matrix with nonclosed range the inner weighted sums in this second test tend to infinity, even if the projection in item 1 has exponential spatial decay.
3. On each of these groups, the finite rectangular matrices \(A=(1-g)(1,V)\), with \(g\) of infinite order and \(V\) any finite group-ring element, have nonclosed range and an exponentially localized kernel projection.
   For these matrices the first test follows from finite-radius product estimates on \(1+VV^*\) after removing the injective left factor.
   No commutation between \(g\) and \(V\) is required.

## Argument

Expanding the fourth finite difference gives
\[
             D_k(s)=\sum_g(1-e^{-s|g|})^4\|\widehat Q_k(g)\|_{\rm HS}^2\ge0 .
\]
In particular \(F_k(0)\) is an ordinary return moment, whereas positive \(s\) also retains the distance of a shared endpoint.
For fixed \(k\) these are finite sums, since powers of a finite group-ring matrix have finite propagation.
For fixed \(s\), \(Q_k\to p\) in trace \(L^2\) by bounded spectral convergence.
The multiplier on Fourier coefficients in the last display is bounded by one, so \(D_k(s)\) tends to the same expression with \(p\) in place of \(Q_k\).
For every integer \(r\ge1\),
\[
 c_\beta r^\beta\le \sum_{j\ge0}2^{\beta j}(1-e^{-2^{-j}r})^4
                         \le C_\beta r^\beta .
\]
The term \(j=\lfloor\log_2 r\rfloor\) gives the lower bound.
For the upper bound sum \(2^{\beta j}\) through that index and use \(r^4 2^{(\beta-4)j}\) on the remaining indices.
The term at \(r=0\) vanishes and the unweighted \(L^2\) norm of a matrix projection is finite.
Summing the nonnegative terms proves item 1, including cases of infinite weighted mass.
The same comparison at finite \(k\) identifies the sum in item 2 with the positive-radius weighted mass of \(Q_k\), up to constants independent of \(k\).

## Interchanging the scales forces a spectral gap

If item 2's liminf is finite, choose a subsequence of \(Q_k\) bounded in the weighted square norm of exponent \(\beta\), adding the bounded coefficient at the identity.
For any finitely supported matrix \(T\), rapid decay on the [actual hyperbolic group](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) gives
\[
 \Big\|\sum_{|g|\ge2^J}\widehat T(g)\lambda_g\Big\|
 \le C\sum_{j\ge J}2^{3j/2}
        \Big(\sum_{2^j\le |g|<2^{j+1}}\|\widehat T(g)\|_{\rm HS}^2\Big)^{1/2}
 \le C_\beta\,2^{-(\beta-3)J/2}\|T\|_{\ell^2_\beta}.
\]
Here the square of \(\|T\|_{\ell^2_\beta}\) uses the weight \((1+|g|)^\beta\).
The subsequence therefore has uniformly small tails in operator norm.
On each fixed ball its coefficients converge, since \(Q_k\to p\) in \(L^2\).
Combining these two estimates makes the subsequence norm Cauchy, and its norm limit must equal \(p\).
If positive spectrum of \(B\) accumulates at zero, the operator norm of \(Q_k-p\) equals one for every \(k\), by the spectral theorem on the complement of the kernel.
This excludes nonclosed range.
Conversely, closed range gives \(\|Q_k-p\|\le\theta^k\) for some \(0\le\theta<1\).
If the support of \(I-B\) lies in the radius-\(w\) ball, with \(w\ge1\), that of \(Q_k\) lies in the radius-\(kw\) ball.
Consequently the \(\ell^2\) coefficient tail of \(p\) outside that ball is \(O(\theta^k)\), so \(p\) has every polynomially weighted square sum finite.
Inside that ball the weighted square norm of \(Q_k-p\) is bounded by \(O((1+kw)^\beta\theta^{2k})\) after squaring.
Outside it \(Q_k\) is zero.
This bounds the full weighted masses of \(Q_k\), proving the equivalence and divergence assertion of item 2.

## Nonclosed range with exponential decay after canceling an injective factor

Put \(T=(1,V)\).
It maps onto \(\ell^2(G)\), while left convolution by \(1-g\) is injective with nonclosed range, as seen on the infinite cyclic cosets by the shift representation.
Thus \(A\) has the same kernel as \(T\) and the same range as \(1-g\).
For its projection use
\[
                 p= I_2-T^*(1+VV^*)^{-1}T .
\]
The row Gram matrix \(1+VV^*\) has spectrum in \([1,1+\|V\|_1^2]\).
Choosing \(J>1+\|V\|_1^2\), the geometric sums \(J^{-1}\sum_{j=0}^{k-1}(1-(1+VV^*)/J)^j\) approximate its inverse with error \(O((1-1/J)^k)\) in operator norm.
Their propagation grows at most linearly with \(k\), and multiplying by the fixed \(T^*,T\) preserves both estimates up to constants.
It follows that the \(\ell^2\) coefficient tails of \(p\) decay exponentially in word radius, and hence the higher endpoint moments in item 1 meet the criterion in this family.
The trace of \(p\) is one, also obtained from the surjective row \(T\).
The stronger raw-power bound in item 2 still fails for \(A\).
The case \(A=0\) in the first two items is immediate from \(Q_k=p=I\).

For a general four-line input the earlier [two-factor fiber estimate](Yin_C_A0049_v1.md#statement) concerns the specified vertex-label lists.
It provides no bound, uniform in word order on a fixed group, for the limits \(D_k(2^{-j})\) in item 1.
The criterion specifies both the required location-sensitive moment and the order of limits that allows a genuinely nonclosed range.

## Assessment history

### Decision ordered-endpoint-moments

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:24 |
| status | proved |
| reason | The review checked the scale sum, the closed-range equivalence and the explicit nonclosed-range family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two orders of limits for weighted endpoint moments and exponential decay after removing an injective factor. |
| argument | [Proof](#argument) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0093_v1.md#whole-argument-finding) | Independent review of the statement, proof and its direct inputs at the indicated scope. |

## Current assessment

[Selected decision](#decision-ordered-endpoint-moments)

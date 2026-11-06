---
author: Yin
---

# A mixed-moment obstruction to a free transpose-pair replacement

This comparison concerns a possible transpose-polynomial route toward the unresolved general scalar-polynomial question in [F0014](../tasks/Yin_T_F0014_v1.md#contract).
It gives a complete exact calculation and probability limit for one fixed bounded complex Hermitian Wigner law.
It is an ordinary proof-development finding, not an independent project review, a novelty claim or a counterexample to the determinant Task.
The [second version's complex-orientation and diagonal-floor boundaries](Yin_L_F0066_v2.md) and the [first version's real cofactor comparison](Yin_L_F0066_v1.md) remain at their own fixed scopes.
In particular the second version's [two-coordinate mixed-orientation cancellation](Yin_L_F0066_v2.md#mixed-orientation-cancellation) and the present asymptotic mixed-trace calculation are distinct evidence, even though they use the same phase c.

Write tr_N=N^(-1)Tr for the normalized trace, use ordinary complex-linear transpose T, and use * only for conjugate transpose.
The sole reused project theorem is the one-input marginal weak semicircular law at the [accepted C_F0186_v4 decision](../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed).
The mixed-moment expectation, variance bound and failure of a free-pair replacement are proved directly below; no joint W,W^T limit theorem is assumed or cited as an input.

<a id="transpose-joint-counterexample"></a>
## The actual pair W,W^T need not have a free semicircular joint limit

Let c=(1+i)/sqrt(2), take independent real Rademacher signs epsilon_ab above the diagonal, and set W_ab=c epsilon_ab/sqrt(N) for a<b, W_ba=conjugate(W_ab), with zero diagonal.
This is an original fixed-law complex Hermitian Wigner input.
Both W and W^T separately have standard semicircular weak limits by the [accepted one-input law](../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed); for W^T the fixed upper law is conjugate(c) epsilon, so the same finite-second-moment hypotheses apply.
Nevertheless
\[
 \operatorname{tr}_N(WW^T)=0
\]
identically: each unordered edge contributes c^2+conjugate(c)^2=i-i=0, and the diagonal is zero.
Their individual normalized traces also vanish identically.

Write X_N=tr_N(W W^T W W^T).
A direct four-step closed-walk expansion gives the exact formula
\[
 \mathbb E X_N=-\frac{(N-1)(2N-1)}{3N^2}
       \longrightarrow-\frac23.
 \tag{Transpose-fourth-moment}
\]
Here are all contributions, including their normalization.
Each term has factor N^(-3), and expectation can be nonzero only when every unordered Rademacher edge occurs an even number of times.
With three distinct vertices, the two possible walk patterns are (a,b,a,d,a) and (a,b,c,b,a).
For a chosen center a in the first pattern the phase is -sgn(b-a)sgn(d-a), with b,d distinct and different from a; the second pattern has the same sum after relabeling its center.
The signed sum for one pattern is
\[
 -\sum_{a=1}^N\left[(N+1-2a)^2-(N-1)\right]
 =-\frac{N(N-1)(N-2)}3.
\]
Both patterns therefore contribute -2(N-1)(N-2)/(3N^2).
The only remaining nonzero pattern uses two vertices, (a,b,a,b,a), and its phase is c^4 or conjugate(c)^4, both equal to -1.
Its N(N-1) choices contribute -(N-1)/N^2.
A walk with a loop vanishes, and a four-vertex walk has unpaired edges and zero expectation, proving the exact formula.

Moreover Var(X_N):=E|X_N-E X_N|^2=O(N^(-1)).
To verify this bound, expand the covariance of two normalized four-step trace sums, using conjugation for the second sum if necessary.
If the two closed walks have disjoint unordered-edge sets, independence makes their covariance zero.
For a nonzero remaining covariance, their union is connected because they share an edge, and each contributing expectation has every edge appearing at least twice among the eight traversals.
Consequently the union has at most four distinct edges and at most five vertices.
There are finitely many equality patterns, each with at most O(N^5) indexings and bounded phase/amplitude contribution, while the two trace normalizations contribute N^(-6).
This gives the claimed O(N^(-1)) bound and hence X_N tends to -2/3 in probability.

For two centered freely independent variables, the alternating mixed fourth moment is zero by the definition of freeness.
Thus this pair cannot converge jointly to freely independent standard semicircular variables, even though the second cross moment is zero and both marginal laws are semicircular.
This is a genuine asymptotic obstruction to that replacement, not a counterexample to the original determinant Task.
Any future transpose-polynomial weak-limit route must keep the actual orientation correlations and prove its own joint limit and nonvanishing mechanism.

<a id="comparison-scope"></a>
## Consequence and exact comparison limit

The calculation applies to the dependent pair built from the same unordered-edge signs, not to a second independent Wigner matrix.
It proves that matching both marginal semicircular laws and the second cross moment does not justify the freely independent joint model.
No complete description or existence theorem for the actual joint limiting distribution is claimed here.
A valid transpose-polynomial approach would need that actual distribution and a justified nonvanishing argument for the transpose-dependent polynomial.
The previously settled fixed-transpose-sign setting is different: it has the exact finite-dimensional identity W^T=+/- W, whereas this phase-line example has neither sign identity.
The example also supplies no failure of the probability floors already proved for nonzero real-part laws, and no determinant or Brown-measure conclusion follows merely from its mixed fourth moment.

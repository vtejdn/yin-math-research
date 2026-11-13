---
author: Yin
---

# Koehler–Sohn small-ball estimate for vector sums with short columns

<a id="ks26-u001"></a>
## Proposition 2.4

In the [inspected arXiv v1 edition](readme.md#arxiv-v1), Proposition 2.4 appears on printed and PDF page 14.
Let independent real random variables \(X_i\) have mean zero and variance one, and assume a fixed \(M\) satisfies \(\inf_i\mathbb E[X_i^2\mathbf1_{|X_i|\le M}]\ge1/2\).
For deterministic vectors \(v_i\in\mathbb R^m\), suppose \(\sum_i v_iv_i^T\succeq I_m\) and \(\max_i\|v_i\|\le d\).
With a constant \(C=C(M)\), every \(t\ge C d\) satisfies
\[
 \sup_{x\in\mathbb R^m}\mathbb P\!\left\{\left\|\sum_i v_i X_i-x\right\|\le t\sqrt m\right\}\le (Ct)^m.
\]
Each fixed centered unit-variance real entry law admits such an \(M\) by monotone convergence.
The Euclidean norm of the full vector and the factor \(\sqrt m\) in the radius are essential to the scale conversion.
In a real singular subspace of an original-entry linear map whose singular values are at least \(a/\sqrt N\), multiplying the projected columns by \(\sqrt N/a\) gives the required covariance inequality.
An original column norm of order \(1/N\) then permits \(t\) of order \(1/\sqrt N\), including for atomic laws.
The uniformity in the target also permits conditioning on independent discarded coordinates and absorbing them into the translation.
Coefficient selection and conditioning must preserve independence of the real multipliers.

Direct inspection covered the complete statement on rendered page 14, the title and supplied contents on rendered pages 1–2, and the discussion of the lower scale on page 15.
The proof organization in §3.3 was consulted for the Gaussian regularization and Brascamp–Lieb mechanism.
The proposition is accepted at statement and applicability depth, and the source proof and its cited dependencies retain their external proof status.

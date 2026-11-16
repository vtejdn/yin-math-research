---
author: Yin
---

# Indicator testing for a nonhomogeneous vertical square function

## LM17-U001

The inspected [arXiv edition](readme.md#yin-edition) gives the hypotheses in Section 1, p. 1, (1.1)–(1.2), and the local theorem and its global estimate on p. 2, Theorem 1.3 and (1.4).
This unit records the theorem statement and checks the indicator specialization.

<a id="indicator-testing"></a>
### Local tests and the global vertical estimate

Let \(\sigma\) be a Borel measure on \(\mathbb R^n\) with \(\sigma(B(x,t))\le C_0t^m\) for all \(x\in\mathbb R^n,\ t>0\), with \(m>0\).
For \(\theta_t f(x)=\int s_t(x,y)f(y)\,d\sigma(y)\), the source requires some \(\alpha>0\) and a uniform constant \(C_K\) such that
\[
 |s_t(x,y)|\le C_K\frac{t^\alpha}{(t+|x-y|)^{m+\alpha}},
 \qquad
 |s_t(x,y)-s_t(x,y')|\le C_K\frac{|y-y'|^\alpha}{(t+|x-y|)^{m+\alpha}}
 \quad\text{if }|y-y'|<t/2.
\]
Only the second kernel variable enters this continuity test.
The vertical square norm is the \(L^2(dt/t)\) norm of \(t\mapsto\theta_t f(x)\), followed by \(L^2(d\sigma(x))\) for its global estimate.

Theorem 1.3 takes one test \(b_Q\) for each cube, supported in \(Q\), with average one on each positive-measure \(Q\), squared \(L^2(\sigma)\) norm at most \(C_1\sigma(Q)\), and
\[
  \int_Q\int_0^{\ell(Q)}|\theta_t b_Q(x)|^2\,\frac{dt}{t}\,d\sigma(x)
       \le C_2\sigma(Q).
\]
The estimates are uniform over cubes.
It concludes that \(\int_{\mathbb R^n}\int_0^\infty|\theta_t f(x)|^2\,dt/t\,d\sigma(x)\le C\|f\|_{L^2(\sigma)}^2\) for all \(f\in L^2(\sigma)\).
At \(b_Q=\mathbf1_Q\), the support and average conditions hold and the squared norm equals \(\sigma(Q)\).
Thus the local square estimate for those indicators suffices, with zero-measure cubes contributing zero.
The application must supply the growth, kernel and testing constants for its chosen measure and operator, uniformly if applied to a family.
The global \(L^2\) conclusion is an established source input here.

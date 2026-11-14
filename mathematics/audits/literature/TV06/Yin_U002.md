---
author: Yin
---

# The exact Cauchy energy and the arclength normalization

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Xavier Tolsa and Joan Verdera, *May the Cauchy transform of a non-trivial finite measure vanish on the support of the measure?*, Ann. Acad. Sci. Fenn. Math. 31 (2006), 479–494. [Published edition](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf) and [authors' version](https://mat.uab.cat/~xtolsa/xv2.pdf). |
| source-locator | Published Theorem 2, equation (1), and preceding principal-value and density discussion, printed p.481. The authors' version has the density conventions and Theorem 2 on pp.2–3 and the localization, Lemma 8, equations (9)–(10), and the arclength computation on pp.8–10. |
| inspection | 2026-11-14. The research agent for Yin read the selected theorem and the indicated normalization and proof passages in the two editions while deriving the scalar weighted estimates. |

<a id="tv06-u002"></a>
## Exact identity

For a positive finite planar Radon measure \(\lambda\), write \(C_\epsilon\lambda(z)=\int_{|w-z|>\epsilon}(z-w)^{-1}d\lambda(w)\).
Let \(c^2(\lambda)\) be the integral of squared reciprocal circumradius over all ordered triples, with zero on collinear or repeated triples.
Assume \(c^2(\lambda)<\infty\) and \(M_1\lambda(z)=\sup_{r>0}\lambda(B(z,r))/r\) belongs to \(L^2(\lambda)\).
Then the principal value \(C\lambda\) exists \(\lambda\)-almost everywhere, the ordinary one-dimensional arclength density \(\theta_\lambda(z)=\lim_{r\downarrow0}\lambda(B(z,r))/(2r)\) exists almost everywhere, and
\[
 \|C\lambda\|_{L^2(\lambda)}^2
 =\lim_{\epsilon\downarrow0}\|C_\epsilon\lambda\|_{L^2(\lambda)}^2
 =\frac{\pi^2}{3}\int\theta_\lambda^2\,d\lambda+\frac16c^2(\lambda).
\]

The normalization of the density matters here.
On p.2 the authors' version writes the ball mass divided by \(r\) and then identifies the limit with the density with respect to arclength.
For \(\lambda=g\,ds\) on a line these quantities are \(2g\) and \(g\), respectively.
Lemma 8, equation (9), evaluates the near-diagonal contribution on a Lipschitz graph as \((\pi^2/3)g^2\) with \(g=d\lambda/d\mathcal H^1\).
In its flat calculation \(ds\) is ordinary Lebesgue measure, and equation (10) gives \(4\int_0^1\log(1+t)\,dt/t=\pi^2/3\).
The preceding localization reduces the positive-density part to those graphs and the zero-density part has zero near-diagonal contribution.
Thus the density in the displayed identity is mass divided by \(2r\), or equivalently one uses coefficient \(\pi^2/12\) with mass divided by \(r\).
The curvature coefficient is independent of this convention.

The equality of norms and almost-everywhere convergence also give strong convergence \(C_\epsilon\lambda\to C\lambda\) in \(L^2(\lambda)\).
Indeed bounded \(L^2\) norms and convergence in measure on the finite measure space give weak \(L^2\) convergence by testing first against bounded functions and using uniform integrability in \(L^1\).
Convergence of the norms gives the strong limit.

This inspection accepts the principal-value, rectifiability and norm-limit theorem as a published result.
It checks the exact coefficients against the local proof on the graph and the flat normalization.
The graph reduction and its external rectifiability theorems have not undergone a separate whole-proof audit here.
The earlier [source unit](Yin_U001.md#tv06-u001) uses only a maximal-density bound with an unspecified absolute constant.

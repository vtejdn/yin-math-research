---
author: Yin
---

# Distance to a fixed subspace through its least common denominator

<a id="rv09-u001"></a>
## Source and inspection

The input is [Theorem 4.2](../../../literature/pdf/RV09/arxiv-v4.html#S4.Thmtheorem2) in Section 4 of [arXiv v4](readme.md#arxiv-v4).
The definitions, theorem, and projection calculation in its proof were read directly online and compared with the [earlier author PDF](readme.md#author-2008).
The theorem is accepted at statement and applicability depth, with the local rescaling correction below.
The complete source proof and its external inputs were not independently audited.

<a id="concentration-and-lcd"></a>
## Definitions and conventions

[Definition 3.1](../../../literature/pdf/RV09/arxiv-v4.html#S3.Thmtheorem1) uses closed Euclidean balls:
\[
 \mathcal L(S,t)=\sup_{v\in\mathbb R^m}\Pr\{\|S-v\|_2\le t\},\qquad t>0.
\]
For a nonzero real subspace \(E\subset\mathbb R^N\), [Section 4](../../../literature/pdf/RV09/arxiv-v4.html#S4.Ex4) defines, for \(\alpha>0\) and \(0<\gamma<1\),
\[
 \operatorname{LCD}_{\alpha,\gamma}(E)
 =\inf\{\|\theta\|_2:\theta\in E,
    \operatorname{dist}(\theta,\mathbb Z^N)
       <\min(\gamma\|\theta\|_2,\alpha)\}.
\]
The strict inequality excludes \(\theta=0\); an empty infimum is interpreted as \(+\infty\).
The source's subgaussian parameter is a bound \(B\) in \(\Pr(|\xi|>t)\le2e^{-t^2/B^2}\) for all \(t>0\), as in Section 1.1.

<a id="distance-to-subspace"></a>
## Theorem 4.2

Let \(X\in\mathbb R^N\) have iid centered subgaussian coordinates of variance one, and let \(H\) be a fixed subspace of dimension \(N-m\), where \(1\le m<N\).
For every \(v\in\mathbb R^N\), \(\alpha>0\), \(\gamma\in(0,1)\), and
\[
 \varepsilon\ge\frac{\sqrt m}{\operatorname{LCD}_{\alpha,\gamma}(H^\perp)},
\]
the source gives
\[
 \Pr\{\operatorname{dist}(X,H+v)<\varepsilon\sqrt m\}
 \le (C\varepsilon/\gamma)^m+C^m e^{-c\alpha^2},
\]
with \(C,c>0\) depending only on the coordinate subgaussian parameter.

<a id="scaling-and-scope"></a>
## Scaling and conditional use

The first proof paragraph writes \(\xi_k/2\) after establishing \(\mathcal L(\xi_k,1/2)\le1-b\).
The appropriate rescaling is \(2\xi_k\), because \(\mathcal L(2\xi_k,1)=\mathcal L(\xi_k,1/2)\).
With the same projected coefficient vectors, apply Theorem 3.3 to twice the projected sum at radius \(2\varepsilon\sqrt m\).
Its threshold is satisfied by the displayed hypothesis; the factor two is absorbed in \(C\).
This checks that rescaling step, not the full proof of Theorem 3.3.

Fair signs meet the coordinate assumptions.
A conditional application requires that, after fixing the history, the tested coordinates still have the indicated iid law and that \(H,v\) are fixed by that history.
The constants remain uniform when the coordinate law is unchanged.
A closed-distance event may be enclosed in a strictly larger open ball; this changes the radius and constants.
Complex statistics require an explicitly chosen real representation.
Whitening a coefficient map, proving its LCD lower bound, and handling symmetric-edge reuse are obligations of the consuming argument.
Theorem 4.2 itself supplies neither those facts nor a Wigner-polynomial least-singular-value bound.

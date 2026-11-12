---
author: Yin
---

# KU14: finite propagation and invariant translation approximation

<a id="ku14-u001"></a>
## Source and inspection scope

The inspected [arXiv v1 original](readme.md#arxiv-v1) is Katsura and Uuye's *On the invariant uniform Roe algebra*.
The scope is Section 1 on printed/PDF p. 1, from the regular-representation conventions through Definition 1.1 and the following amenable-group sentence.
The complete original was obtained, but no whole-paper mathematical review was performed.

<a id="uniform-roe-algebra"></a>
## Finite propagation and the uniform Roe algebra

Let \(G\) be a countable discrete group, with coordinate basis \((\delta_x)_{x\in G}\) for \(\ell^2(G)\).
Use \(\lambda_g\delta_x=\delta_{gx}\) and \(\rho_g\delta_x=\delta_{xg^{-1}}\).
A bounded operator \(A\), indexed here by output row \(x\) and input column \(y\), has finite propagation, called finite width in the source, when
\[
\{xy^{-1}:\langle A\delta_y,\delta_x\rangle\ne0\}
\]
is finite.
The uniform Roe algebra \(C_u^*(G)\) is the operator-norm closure of those operators.
The source's finite-width matrix convention is the same finite-relative-support condition; the displayed row/column indexing is made explicit here.
In a finitely generated group this is finite propagation for the right-invariant word metric.
Position-dependent coefficients are allowed.

The group von Neumann algebra satisfies \(\mathcal N(G)=\rho(G)'\).
The right-conjugation fixed-point algebra is therefore
\[
C_u^*(G)^G=C_u^*(G)\cap\mathcal N(G).
\]
These definitions and the stated equality were checked directly in the indicated introduction passage.

<a id="itap"></a>
## Invariant translation approximation property and amenable scope

Definition 1.1 calls
\[
C_r^*(G)=C_u^*(G)^G
\]
the invariant translation approximation property, abbreviated ITAP.
Here \(C_r^*(G)\) is the source's \(C_\lambda^*(G)\).
The next paragraph explicitly states that amenable groups have ITAP and attributes that assertion to Roe's book, with the definition referring to Section 11.5.3.
That attribution is recorded as the source's statement; Roe's book was not inspected here.

The local amenable application uses the displayed identity for countable groups and may separately prove its needed direction by invariant-mean averaging.
This source inspection does not establish that a group-ring kernel projection lies in \(C_u^*(G)\), does not supply an approximation error or a kernel dimension formula, and does not claim ITAP for all groups.
The later tensor and slice-map results of KU14 are not inputs at this inspection scope.

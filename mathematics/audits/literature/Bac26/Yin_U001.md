---
author: Yin
---

# Bac26: the domain assumption in linear sofic representation uniqueness

<a id="bac26-u001"></a>
## Source and inspection

The inspected source is [arXiv v3](readme.md#arxiv-v3), whose terminology is linear sofic representations.
On 2026-11-12 the actual v3 Theorems 1.1 and 1.2 on pp. 1–2, Section 2.2 on p. 3, Definition 3.2 and Proposition 3.3 on p. 5, and Theorem 6.4 on pp. 11–12 were checked.
This is a statement, definition-interface and applicability check; the uniqueness, monotiling and stability proofs were not fully audited.
No inspection of an earlier version is substituted for these v3 locators.

<a id="domain-hypothesis"></a>
## Exact hypotheses and limitation

Theorem 1.1 states uniqueness up to conjugacy of linear sofic representations for a finitely generated amenable \(K\)-algebra \(A\) without zero divisors, over an arbitrary field \(K\).
Theorem 1.2 specializes the weak-stability conclusion to a torsion-free amenable group \(G\), but separately assumes that \(KG\) has no zero divisors.
The general Theorem 6.4 likewise begins with an amenable \(K\)-algebra without zero divisors; its group-ring part concludes weak stability if and only if the group is residually finite under those hypotheses.
The global finite-generation convention is stated at the start of Section 2 on p. 2.

The normalized finite matrix rank is \(\operatorname{rk}(B)=\operatorname{rank}_K(B)/n\) for \(B\in M_n(K)\).
Definition 3.2 includes the bound \(\operatorname{rk}(\phi(a))\geq1-1/d\) simultaneously for every nonzero element of the specified finite-dimensional degree subspace.
Proposition 3.3 identifies linear sofic representations with sequences that eventually satisfy each such approximation condition.
Thus they in particular require asymptotic rank one for every nonzero fixed algebra element; ordinary injectivity into a matrix rank ultraproduct only requires positive rank for such elements.

Section 2.2 on p. 3 explicitly explains the obstruction: if \(ab=0\) with \(a,b\ne0\), an injective rank-ultraproduct representation cannot give rank one to both elements; at least one of their ranks is at most \(1/2\).
Consequently the existence and uniqueness theorem cannot be invoked to establish the absence of zero divisors from amenability alone.
Using its maximally separating approximation hypothesis to infer scalar full rank would already assume the missing conclusion in the representation input.
The source is useful for comparing approximation methods once the domain hypothesis is available, and supplies no new resolution of that hypothesis in the passages inspected here.

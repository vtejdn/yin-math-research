---
author: Yin
---

# Single group translations and the positive-nullity test for a Schur kernel

## Statement

Let \(K\le G\) be discrete groups and let \(P\in\mathcal N(K)\) be an orthogonal projection with canonical trace \(1/2\).
For \(g\in G\) write
\[
       d(g)=\dim_G(P\ell^2(G)\cap g^{-1}P\ell^2(G)).
\]
Suppose that for every finite set of nonidentity elements of \(K*\langle x\rangle\), where \(x\) generates an infinite cyclic group, there is a single substitution \(x\mapsto g\in G\), fixing \(K\), that keeps all of them nonidentity.
Then \(\inf_{g\in G}d(g)=0\), even though the allowed multipliers here are individual group elements.

Quantitatively, for each \(m\ge1\) and finite group-ring contraction \(b\in\mathbb CK\) with \(\|P-b\|_2\le\epsilon\), one can take as the finite set all nonidentity group elements occurring in the expansion of \((b x^{-1} b x)^m\) over \(K*\langle x\rangle\).
Every substitution avoiding this set satisfies
\[
                   d(g)\le \frac12\,\binom{2m}{m}4^{-m}+4m\epsilon .
\]
Here \(\|\cdot\|_2\) is the norm from the canonical trace.

In particular suppose \(P\) is the kernel projection of a first Schur scalar \(S=d-ca^{-1}b_0\) of a two-by-two matrix over \(\mathbb CK\) with affiliated-unit pivot.
If the strictly positive kernel dimensions of the associated positive three-by-three matrices with a single group element as multiplier have a uniform positive lower bound, then \(P\in D_2(G)\) and \(D_2(G)\) contains matrix units of a unital copy of \(M_2(\mathbb C)\) with first diagonal unit \(P\).
Otherwise, when every such matrix has positive nullity, their nullities can tend to zero while the number of group terms in their defining formulas stays bounded.
In particular the single-element infimum result applies to every half-trace projection on a countable torsion-free acylindrically hyperbolic \(G\).
It does not assert that an arbitrary such projection is the kernel of a group-ring Schur scalar.

## The free half-projection moment

Use the regular inclusion \(\mathcal N(K)\subset\mathcal N(K*\langle x\rangle)\).
There \(P\) and \(Q=x^{-1}Px\) are freely independent by the normal form of the free product.
Write \(U=2P-I,\ V=2Q-I,\ W=UV\).
The symmetries \(U,V\) are centered, and every nonzero power of \(W\) has trace zero by freeness.
Also \(\tau(UW^j)=0\) for every integer \(j\), since it reduces to a nonempty alternating product of centered symmetries.
The operator \(W+W^*\) commutes with \(P\), and
\[
                 PQP=P(2+W+W^*)/4 .
\]
Consequently the trace of \((PQP)^m\) is one half the constant Laurent coefficient of \((2+z+z^{-1})^m/4^m\), which equals \(\binom{2m}{m}/(2\cdot4^m)\).
It tends to zero, for instance by integrating \(((1+\cos\theta)/2)^m\) over the circle and using dominated convergence.
This computes the moment for arbitrary \(P\) of trace one half, without a closed-range or center-balance hypothesis.

## Transferring the moment by finitely many word tests

For \(Q_g=g^{-1}Pg\), both \(P\) and \(Q_g\) act as the identity on their common range, so the trace of the positive contraction \((PQ_gP)^m\) is at least \(d(g)\).
Cyclicity and \(P^2=P\) identify that trace with \(\tau((P g^{-1}P g)^m)\).
Replacing the \(2m\) occurrences of \(P\) there by \(b\) changes the trace by at most \(2m\epsilon\), by telescoping and tracial Cauchy-Schwarz with all other factors contractions.
The identical estimate holds at the free generator \(x\).
Under a substitution avoiding the indicated finite set, the identity coefficient of \((b g^{-1} b g)^m\) equals the one at \(x\), since no nonidentity term becomes the identity.
This proves the quantitative claim.

Contractions in \(\mathbb CK\) approximate \(P\) arbitrarily well in \(\|\cdot\|_2\).
Indeed the unit ball of the reduced group \(C^*\)-algebra is strongly dense in the unit ball of the von Neumann algebra by Kaplansky density.
Evaluation at the identity vector gives the required \(L^2\) approximation, and operator-norm group-ring approximation followed by scalar rescaling restores the contraction bound.
For any desired error choose \(m\) first to make the computed moment small and then choose \(\epsilon\) sufficiently small.
Finite word avoidance now gives the infimum statement.

For a countable group with no nontrivial mixed identity the necessary simultaneous avoidance follows from [Hull and Osin, Proposition 5.3](../literature/pdf/HO16--arxiv-v1.pdf#page=26).
Indeed failure for a finite family would be a universal disjunction of word equations with constants in the group, true there and false at \(x\) in its free product.
For countable acylindrically hyperbolic groups with trivial finite radical, [their Corollary 5.10](../literature/pdf/HO16--arxiv-v1.pdf#page=30) supplies the absence of nontrivial mixed identities.
Torsion-freeness in the stated application ensures that the finite radical is trivial.
For a subgroup \(K\le G\), the inclusion \(K*\langle x\rangle\hookrightarrow G*\langle x\rangle\) respects nontriviality, so the condition for \(G\) implies the relative condition used above.

## The three-by-three test and its exact alternative

For the stated Schur kernel put
\[
       L_g=\begin{pmatrix}a&0&b_0\\ c&0&d\\0&a&b_0g\\0&c&dg\end{pmatrix}.
\]
Projection onto the last coordinate identifies its affiliated kernel with the solutions of \(S\xi=Sg\xi=0\), hence \(\dim_G\ker(L_g^*L_g)=d(g)\) by the [original group-ring linearization](Yin_C_A0125_v2.md#group-ring-witnesses-and-the-exact-projection).
The entries of \(L_g\) use only translates of the fixed original coefficients.
If all strictly positive \(d(g)\) are bounded below, some \(d(g)\) must therefore vanish.
The [single-inverse matrix-unit construction](Yin_C_A0125_v2.md#algebraic-matrix-units-from-a-single-inverse) then applies to this \(g\) with only the scalar trace-one-half hypothesis, giving the original-group conclusion.
If none vanishes, choose successive values with arbitrarily small strictly positive nullity.
A bound on the number of group terms allows their locations to vary with \(g\).

## Why a factor trace alone does not give single-element mixing

Let \(G=(\bigoplus_{\mathbb Z}\mathbb Z)\rtimes\mathbb Z\) with the integer shift on the lamp coordinates.
This is torsion-free, and all nonidentity conjugacy classes are infinite.
Indeed a nonzero finite lamp configuration has infinitely many distinct shifts, while conjugating an element of nonzero shift by integer multiples of a single lamp changes its lamp component by distinct configurations.
Let \(P\) be the spectral projection of the lamp unitary at position zero for a semicircle.
Its trace is one half, and in the group von Neumann algebra of the lamps the coordinate functions have the independent circle Haar law.
Conjugating by a group element of shift \(j\) moves this projection to the lamp at position \(j\) or \(-j\), according to the conjugation convention.
Thus \(d(g)=1/2\) for zero shift and \(d(g)=1/4\) otherwise.
This example concerns a bounded projection and the restriction to single group elements.
The earlier [finite-sum approximation](Yin_C_A0125_v2.md#reduction-of-the-defect-with-one-more-group-element) still applies in the factor and concerns a larger family of multipliers.

## Assessment history

### Decision single-translations-of-a-half-trace-kernel

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:44 |
| status | proved |
| reason | Independent review verified the moment formula, finite-word comparison and the exact alternative for the original Schur projection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One group element per mixer and the exact alternative for an original Schur kernel. |
| argument | [The free half-projection moment](#the-free-half-projection-moment) | The normalized central binomial moment. |
| argument | [Transferring the moment by finitely many word tests](#transferring-the-moment-by-finitely-many-word-tests) | Two finite-support approximation errors and simultaneous word avoidance. |
| argument | [The three-by-three test and its exact alternative](#the-three-by-three-test-and-its-exact-alternative) | The original group-ring Gram matrices and their positive-nullity gap. |
| argument | [Why a factor trace alone does not give single-element mixing](#why-a-factor-trace-alone-does-not-give-single-element-mixing) | The semicircle lamp projection in a torsion-free group with infinite conjugacy classes. |
| review | [Single translations of a half-trace kernel](../audits/reviews/Yin_R_A0199_v1.md#single-translations-of-a-half-trace-kernel) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-single-translations-of-a-half-trace-kernel)

---
author: Yin
---
# Unitary regularization and liberation Fisher information

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Voi99-U004

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published edition of Voi99. |
| source-locator | Sections 8–9, printed pp.128–141, PDF pp.28–41. |
| inspection | 2026-10-18, authoring agent for Yin. All statements and proofs were read; derivation identities, adjoint pairings, the Hilbert-transform computation, norm identities, projection arguments and extended-value cases were checked. Printed pp.129–131 and 140 were visually inspected. The signed-vector corrections and corrected hypotheses are recorded explicitly. |

## Unitary derivation and Fisher information

For a unitary \(U\) and a unital \(*\)-algebra \(B\) algebraically free from its Laurent-polynomial algebra, Section 8 introduces
\[
 d_{U:B}:B[U,U^{-1}]\longrightarrow
 B[U,U^{-1}]\otimes_{\mathbb C}B[U,U^{-1}],
 \quad d_{U:B}|_B=0,\quad d_{U:B}U=1\otimes U.
\]
Consequently \(d_{U:B}U^{-1}=-U^{-1}\otimes1\).
For this represented derivation, \(U\) must satisfy no nonzero Laurent-polynomial relation; infinite spectrum suffices.
The source's phrase “infinite order” is insufficient if interpreted only as infinite multiplicative group order: a unitary with two eigenvalues, one of infinite order on the circle, provides a counterexample to that interpretation.

Definition 8.9 sets
\[
 F(U)=\|d_{U:\mathbb C}^*(1\otimes1)\|_2^2
\]
when the actual adjoint vector exists, and \(F(U)=+\infty\) otherwise.
This depends only on the distribution of \(U\), so the source also writes \(F(\mu)\) and \(F(p)\).
Haar measure on \(\mathbb T\) is normalized to have mass one.

If the law has density \(p\in L^3(\mathbb T)\), the Hilbert-transform argument proves existence of the adjoint vector.
With the transform as actually printed in 8.7,
\[
 (H_\varepsilon p)(e^{\mathrm i\theta_1})
 =-\frac1{2\pi}\int_{\varepsilon<|\theta|\le\pi}
       p(e^{\mathrm i(\theta_1-\theta)})\cot(\theta/2)\,d\theta,
 \qquad Hp=\lim_{\varepsilon\downarrow0}H_\varepsilon p,
\]
the corrected signed formula is
\[
 d_{U:\mathbb C}^*(1\otimes1)=-\mathrm i(Hp)(U).
\]
The norm formulas in Corollary 8.8 are unaffected by this sign:
\[
 F(p)=\int p(Hp)^2\,d\lambda
     =\frac13\left(\int p^3\,d\lambda-1\right).
\]
The \(L^\infty\) norm of the adjoint vector is the essential supremum of \(Hp\) on the support \(\{p>0\}\).
The \(L^3\)-boundedness/convergence of the circle Hilbert transform is an accepted classical external input, not re-proved here.
Hölder's inequality gives \(Hp\in L^2(p\,d\lambda)\).
The cubic identity follows by taking the constant coefficient of the cube of the analytic Herglotz boundary function; changing the sign of its imaginary part leaves its real cubic identity unchanged.

<a id="unitary-sign-check"></a>
## Direct sign check and its effect on regularization

The restriction identity in the unnumbered Proposition between 8.1 and 8.3 is
\[
 d_{U:B}|_{\operatorname{Alg}(B,UBU^*)}=-\delta_{UBU^*:B}.
\]
Corollary 8.3 correctly gives, for \(h=d_{U:B}^*(1\otimes1)\),
\[
 j(UBU^*:B)=-E_{W^*(B,UBU^*)}(h^*).
\]
The unitary derivation is anti-real, so \(h^*=-h\).
Consequently this is \(+E_{W^*(B,UBU^*)}h\).
The minus signs before \(d_{U:\mathbb C}^*(1\otimes1)\) in Corollaries 8.5–8.6 do not follow from 8.3–8.4 and must be changed to plus under the source's stated adjoint convention.

A first Fourier mode checks the independent sign error in Proposition 8.7.
Choose \(0<a<1/2\) and \(p(e^{\mathrm i\theta})=1+2a\cos\theta\).
Then \(\tau(U)=a\), \(\tau(U^2)=0\), and the printed Hilbert transform is \(Hp=-2a\sin\theta\).
The printed candidate \(h=\mathrm iHp(U)=a(U^*-U)\) gives
\[
 \tau(h^*U)=-a,
\]
whereas actual adjunction requires
\[
 \tau(h^*U)=(\tau\otimes\tau)(d_UU)=\tau(U)=a.
\]
Thus \(h=-\mathrm iHp(U)\) has the required sign.
The passage from the displayed cotangent identity to the next integral on p.131 changes a minus sign to a plus; this is also visible in the page image.
These two signed-vector errors can cancel when the printed formulas are combined, but the individual adjoint and gradient formulas must be corrected separately.
Squared norms and the finiteness estimates below are insensitive to those signs.

The source's regularization mechanism is otherwise as follows.
Free extension of constants gives \(d_{U:B}^*1=d_{U:\mathbb C}^*1\).
Conditional expectation gives the gradient after conjugation.
When \(B\) contains a diffuse abelian algebra and \(\tau(U)\ne0\), Proposition 2.5 removes the conditional expectation onto \(W^*(B,UBU^*)\).
For arbitrary \(A,B\), enlargement by a free diffuse algebra and compression gives the corresponding conditional-gradient formula.
The bounds in 8.10 follow from the Brownian density bounds and the cubic expression for \(F\): \(F(U(t))=O(t^{-1})\) near zero and has an exponential tail.

## Liberation Fisher information

For unital \(*\)-subalgebras \(A_1,\ldots,A_n,B\subseteq M\), Definition 9.1 sets
\[
 \varphi^*(A_1;\ldots;A_n:B)
 =\sum_{k=1}^n
 \bigl\|j(A_k:A_1\vee\cdots\vee\widehat A_k\vee\cdots\vee A_n\vee B)\bigr\|_2^2.
\]
An absent gradient or an infinite \(L^2\) norm gives \(+\infty\).
Here \(\vee\) denotes the generated algebra, with von Neumann closure where needed for \(L^2\).
The abbreviation \(\varphi^*(A_1;\ldots;A_n)\) means \(B=\mathbb C1\).
The source also calls this infinitesimal liberation information.
For two algebras its punctuation matters:
\[
 \varphi^*(A;B)=2\varphi^*(A:B)=2\varphi^*(B:A).
\]

## Checked result groups

| Passage | Content and proof mechanism checked |
| --- | --- |
| 9.2 | Restriction decreases the squared norm by conditional expectation; taking von Neumann closures does not change it. Grouping coordinates gives the stated sums and superadditivity inequalities. The entropy derivative interpretation in 9.2(a) remains heuristic. |
| 9.3 | Under the stated \(B\)-amalgamated freeness, gradients for disjoint groups retain their smaller constant algebras. Orthogonality of their centered \(L^2\) components gives additivity. Vanishing of the total information is equivalent to scalar freeness of \(A_1,\ldots,A_n,B\), using 5.17. |
| 9.4 | If \(A_1\vee\cdots\vee A_n\vee B,U_1,\ldots,U_n,U\) are jointly free, conjugation gives \(\varphi^*(U_1A_1U_1^*;\ldots;U_nA_nU_n^*:B)\le\sum_kF(U_k)\). A common diffuse abelian subalgebra and \(\tau(U_k)\ne0\) give equality. Two Markovian conditional-expectation contractions prove monotonicity under the other stated conjugations. |
| 9.6 | Strong convergence of the conditional projections and the word formula give lower semicontinuity. Uniform \(L^2\) bounds are needed only along a subsequence realizing the finite liminf. |
| 9.7 | Pointwise convergence of trace laws on the full free product gives lower semicontinuity through a bounded functional on its GNS quotient. The inequality annihilates the null space, so the limiting vector is well-defined. |
| 9.8 | For a freely Markovian triple, \(\varphi^*(A:C)^{-1}\ge\varphi^*(A:B)^{-1}+\varphi^*(B:C)^{-1}\). Orthogonal components of the two gradients and Cauchy–Schwarz give the finite nonzero case; zero and infinite values are handled by contraction and \(0^{-1}=+\infty,\ (+\infty)^{-1}=0\). |
| 9.9 | Apply 9.8 to \(UAU^*,A,B\), and use \(\varphi^*(UAU^*:A)\le F(U)\). The source proof prints \(\ge F(U)\), the opposite of both 9.4 and the inequality needed after reciprocation. |
| 9.10 | The liberated Fisher information is decreasing, right-continuous and finite at positive time when the Brownian motions are free from the joint algebra \(A_1\vee\cdots\vee A_n\vee B\). Independent increments give monotonicity; 9.7 gives right continuity; 9.4 and 8.10 give finiteness. |

The printed hypothesis of 9.10 omits \(B\) from its freeness requirement, although its conclusion is relative to \(B\).
Its first displayed conjugate also omits a star.
The checked formulation uses the joint-algebra freeness hypothesis of 9.4 and \(U_k(t)A_kU_k(t)^*\) for every coordinate.
No assertion is made for an arbitrary \(B\) correlated with the Brownian motions.

## Assessment and dependencies

The norm and information conclusions above are supported after the explicit sign, inequality and hypothesis corrections.
This is not a certification of the signed formulas as printed.
The dependencies are the inspected gradient/Markovian mechanisms in [Voi99-U002](Yin_U002.md#voi99-u002) and [Voi99-U003](Yin_U003.md#voi99-u003), plus classical Hilbert-transform theory and the free Brownian inputs identified there.
No full-\(M\Omega\) domain assertion for implementing operators is proved in this section.

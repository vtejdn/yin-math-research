---
author: Yin
---
# A skew polynomial representation and separating two-group quotients for the type kernel

## Statement

Use the seven-triangle presentation of Gardam's group \(\Gamma\) identified with its two-generator presentation in [C105 v2](Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
Let \(d:\Gamma\to C_3\) send each positive triangle generator \(a,\ldots,g\) to \(1\).
There is a homomorphism \(\psi:\Gamma\to C_7\) taking these generators, in that order, to
\[
                      6,\ 1,\ 0,\ 4,\ 2,\ 5,\ 3 .
\]
There is a separating descending sequence of finite quotient groups of \(\Gamma\), each an extension of \(C_3\) by a finite \(2\)-group, with the induced map to \(C_3\) equal to \(d\).
In particular \(\ker d\) and all its subgroups are residually finite \(2\)-groups.

More explicitly, set \(E=\mathbb F_2[\theta]/(\theta^3+\theta+1)\), \(\sigma(c)=c^2\), and let \(D\) be the division ring of fractions of \(E[X;\sigma]\), with \(Xc=c^2X\).
Its center is \(K=\mathbb F_2(s)\), where \(s=X^3\).
Writing \(c_p=\theta^{3\psi(p)}\) for the seven positive letters, a faithful representation is
\[
                   \Gamma\longrightarrow D^\times/K^\times,\qquad
                      p\longmapsto [X+c_p].
                                                        \tag{1}
\]
For \(h\in\ker d\) represented by any signed word \(w\), let \(e(w)\) denote its total signed exponent, an integer divisible by three, and \(f_w\) the corresponding ordered product of \(X+c_p\) and their inverses.
The map \(h\mapsto f_w/(1+s)^{e(w)/3}\) is also a faithful representation into \(D^\times\) itself.
The [cyclic change of generators](../ledger/Yin_L_A0068_v1.md) identifies a second proof of residual \(2\)-finiteness using the published upper triangular representation of the cyclic triangle group.

## Argument

### The skew division ring and the triangular products

The ring \(E[X;\sigma]\) has no zero divisors by the leading-term product.
Inverting the nonzero central polynomials in \(\mathbb F_2[s]\) gives a domain of dimension nine over \(K\), with basis \(\theta^iX^j\), \(0\le i,j<3\).
Indeed \(E[X;\sigma]\) is free on this basis over \(\mathbb F_2[s]\), by uniqueness of the coefficients of powers of \(X\).
A finite-dimensional domain over a central field is a division ring, so this central localization is \(D\).
Commuting with \(E\) forces the coefficients of \(X\) and \(X^2\) in the \(E(s)\)-coordinate form to vanish, and commuting with \(X\) then forces the remaining coefficient to belong to \(E(s)^\sigma=\mathbb F_2(s)\).
The last equality follows by writing \(E(s)\) on an \(\mathbb F_2\)-basis of \(E\) and extending the fixed-space equations to \(\mathbb F_2(s)\).

The sum of the displayed \(\psi\)-labels vanishes modulo seven in every triangle, so these labels define the claimed homomorphism.
Its threefold multiples are \(4,3,0,5,6,1,2\).
For each relator \(pqr\), \(c_pc_qc_r=1\) and \(c_p+c_q^2=c_r^4\).
For direct verification the exponents of these last three terms in the order \(c_p,c_q^2,c_r^4\) are
\[
\begin{array}{c|rrrrrrr}
pqr&acb&add&afg&bbf&cef&cdg&eeg\\\hline
(\log_\theta c_p,\log_\theta c_q^2,\log_\theta c_r^4)
 &(4,0,5)&(4,3,6)&(4,2,1)&(3,6,4)&(0,5,4)&(0,3,1)&(6,5,1).
\end{array}
\]
These sums in \(E\) use \(\theta^3=\theta+1\).
Ordinary skew multiplication gives
\[
 (X+c_p)(X+c_q)(X+c_r)
 =X^3+(c_p+c_q^2+c_r^4)X^2+
 \big((c_p+c_q^2)c_r^2+c_pc_q\big)X+c_pc_qc_r=X^3+1 .
\]
The coefficient of \(X\) vanishes since \(c_r^6=c_r^{-1}=c_pc_q\).
The same central product holds for the cyclic shifts by conjugation in \(D^\times\).
This proves that (1) is a homomorphism.
For the lift on \(\ker d\), insertion of a conjugate of a relator or of its inverse multiplies \(f_w\) by \((1+s)^{\pm1}\) and changes \(e(w)\) by \(\pm3\).
Free cancellations preserve both quantities.
The displayed lift is therefore independent of the word and multiplicative.

### Detecting a nonempty normal word at \(s=1\)

Evaluate skew polynomials as \(\mathbb F_2\)-linear maps on \(E\) by sending constants to multiplication and \(X\) to the Frobenius map \(t\mapsto t^2\).
This respects \(Xc=c^2X\) and sends \(s\) to the identity.
Let \(L_p(t)=t^2+c_pt\).
Its kernel is \(\{0,c_p\}\), so it has rank two on the three-dimensional space \(E\).
The seven kernels are all the lines, since the \(c_p\)'s are distinct and exhaust \(E^\times\).
For fixed \(q\), \(L_pL_q\) has rank one exactly when \(\ker L_p\subset\operatorname{im}L_q\), which occurs for three choices of \(p\).
Each of the three predecessor letters \(p\) such that \(pqr\) is a cyclic triangle has this property because \(L_pL_qL_r=0\) and \(L_r\) has rank two.
The [predecessor table](Yin_C_A0106_v1.md#argument) therefore identifies exactly the rank-one pairs.
All other pairs have rank two.

For an inverse letter use the polynomial \(Y_p=(1+s)(X+c_p)^{-1}\), equal to the product of the other two factors in any cyclic triangle beginning with \(p\).
Let \(M_p\) denote its evaluation.
This product has rank one by the preceding pair test, and \(M_p L_p=L_p M_p=0\).
Consequently \(\operatorname{im}M_p=\ker L_p\) and \(\ker M_p=\operatorname{im}L_p\).
The product \(M_p M_q\) vanishes exactly when \(L_qL_p\) has rank one.

Use the positive-then-negative irreducible normal word in [C105 v2](Yin_C_A0105_v2.md#a-finite-complete-rewriting-system).
In a purely positive run each adjacent pair is outside the triangle list.
Its entire product has rank two and kernel equal to the kernel of the last letter, by induction on the number of factors using the pair test.
In a purely negative run every adjacent pair has nonzero product under the \(M_p\)'s.
Since these maps have rank one, their composite has rank one and image equal to the image of its first factor, by composing from the right.
At a mixed join \(p q^{-1}\), irreducibility requires \(p\ne q\).
The image line of the negative run is \(\ker L_q\), distinct from the kernel \(\ker L_p\) of the positive run, so the mixed product has rank one.

Replacing inverse letters by \(Y_p\) multiplies the representative by a central power of \(1+s\) and gives a skew polynomial.
For every nonempty normal word this polynomial evaluates to rank one or two.
If the represented projective element were trivial, the polynomial would belong to \(K\cap E[X;\sigma]=\mathbb F_2[s]\), by the coefficient and center calculations above.
Its evaluation would have rank zero or three.
This contradiction proves faithfulness of (1) and of its lift on \(\ker d\).

### Explicit separating quotients

Put \(T=X^{-1}\).
The skew Laurent series division ring \(E((T;\sigma^{-1}))\) contains \(D\): nonzero series with a lowest exponent have inverses by recursion, and the inclusion of skew polynomials consequently extends through the central localization.
In its power series ring put \(U_m=1+T^m E[[T;\sigma^{-1}]]\) for \(m\ge1\).
The \(U_m\) are normal in \(U_1\), stable under conjugation by \(X\), and intersect in the identity.
Each quotient \(U_m/U_{m+1}\) is the additive group of \(E\), by its first coefficient, so every \(U_1/U_m\) is a finite \(2\)-group.
Conjugation by \(X\) acts with order dividing three, since \(X^3\) is central.
Use this action in \(U_1\rtimes C_3\), writing \(\tau\) for the generator of \(C_3\).

There is a central series \(b\in1+T^3\mathbb F_2[[T^3]]\) with \(b^3=1+T^3\).
Indeed the coefficient of each successive power of \(T^3\) in the cube is the sum of three times the unknown coefficient and terms already known.
Three is a unit in \(\mathbb F_2\), which gives a unique recursion.
Send the letter \(p\) to
\[
                      b^{-1}(1+c_pT)\tau .
\]
In a product of three such letters, the conjugations on \(U_1\) are the same as in the product \(\prod (1+c_pT)X=\prod (X+c_p)\).
For a triangle, the \(U_1\)-part before dividing by \(b^3\) is therefore \((1+s)X^{-3}=1+T^3\).
This verifies all seven relations.
The map from the semidirect product to the multiplicative group of the Laurent series division ring modulo its center, \((u,\tau^i)\mapsto[uX^i]\), sends the new representation to (1) in the larger projective group.
An element of \(D\) that becomes central in that larger ring already commutes with \(D\) and hence lies in \(K\).
Faithfulness of (1) proves faithfulness of this semidirect-product representation.
Its projections to \((U_1/U_m)\rtimes C_3\) separate all distinct group elements and have descending kernels.
The projection of \(\Gamma\) to the last \(C_3\) is its type \(d\), so each finite image has a normal \(2\)-subgroup with quotient \(C_3\), as claimed.

## Assessment history

### Decision skew-triangle-model

| Field | Value |
| --- | --- |
| date | 2026-11-21T07:15 |
| status | proved |
| reason | An independent verification checks the division ring, every normal word, both representations and separation by finite quotients. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Faithful skew polynomial model, a lift of the type kernel and separating finite two-group extensions over the type quotient. |
| argument | [Proof](#argument) | Central products, reduction to linear maps over the field of eight elements, a normal form and the Laurent series congruence quotients. |
| review | [Whole finding](../audits/reviews/Yin_R_A0145_v1.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Group word problem](Yin_C_A0105_v2.md#decision-exact-balls) | The equivalent presentation and its complete positive-then-negative normal form. |
| dependency | [Predecessor sets](Yin_C_A0106_v1.md#decision-outer-layer) | The exact admissible positive pairs of triangle generators. |

## Current assessment

[Selected decision](#decision-skew-triangle-model)

---
author: Yin
---
# Faithfulness of the skew polynomial model for Gardam's group

## Whole finding

At 2026-11-21T07:09 UTC an agent outside the development of C_A0108_v1 independently reviewed its [statement](../../claims/Yin_C_A0108_v1.md#statement) and [argument](../../claims/Yin_C_A0108_v1.md#argument) for Yin.
The reviewer received the fixed claim and the review assignment without its development dialogue, exploration notes, author explanations or an earlier finding on this claim.
An adjacent review of C_A0107_v1 mentioned the presentation identification.
The reviewer checked that identification and the rewriting dependencies directly, and constructed a separate finite-state verification of the faithfulness argument.

### Relations and the central factor

In alphabetical order, substitution of \(a,b,a^{-1}b^{-1},ba^2b^{-2},bab^2,b^{-2},b^2a^{-1}\) for the seven generators leaves five empty reduced relators and sends \(add,eeg\) to \(R_1,bR_2b^{-1}\), respectively.
Conversely the five eliminating relations imply those substitutions in the triangle group, giving inverse presentation maps.
The proposed labels sum to zero modulo seven on each relator and the label of \(b\) generates \(C_7\). [Presentation identification](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).

The degree-three polynomial defining \(E\) has no root in \(\mathbb F_2\).
The powers of \(X\), grouped by degree modulo three, give the stated free basis over \(\mathbb F_2[s]\).
The leading term of a product is nonzero, so the central localization is a domain.
Left and right multiplication by any nonzero element are injective endomorphisms of a nine-dimensional \(K\)-space, hence surjective.
In the coordinates \(u_0+u_1X+u_2X^2\), with \(u_i\in E(s)\), commutation with \(\theta\) forces \(u_1=u_2=0\), as the three conjugates of \(\theta\) are distinct.
Commutation with \(X\) then gives the Frobenius fixed space \(\mathbb F_2(s)\), since the fixed-space linear system on \(E\) retains its rank over \(\mathbb F_2(s)\).
In particular a central skew polynomial has coefficients in \(\mathbb F_2\) and powers of \(X\) divisible by three.

I encoded \(1,\theta,\theta^2\) by the binary digits of an integer in increasing place order.
Multiplication modulo \(\theta^3+\theta+1\) gave \((c_a,\ldots,c_g)=(6,3,1,7,5,2,4)\) in these coordinates.
Independently multiplying the factors in each of the 21 cyclic triangles by the rule \((uX^i)(vX^j)=uv^{2^i}X^{i+j}\) gave the coefficients \((1,0,0,1)\) in every case.
The central relator value \(1+s\) therefore defines the projective representation.
Each relator insertion changes the signed exponent by three and supplies one factor of \(1+s\), with reciprocal changes for an inverse insertion.
The signed exponent adds on concatenation and is divisible by three on \(\ker d\), so the claimed normalization defines a multiplicative lift there.

### Detecting all normal words

I regenerated the two-letter rules from the seven cyclic boundary families.
For each of the 42 inverse-positive pairs of distinct indices the two triangles have a unique common terminal letter, giving the length-preserving interchange.
The length and inversion count decrease lexicographically.
Among the 98 rules, the two reductions in each of the 560 overlapping triples joined by repeated leftmost reduction.
Disjoint reductions commute.
All the rule equalities hold in the triangle group, and they imply each triangle relator and both inverse cancellations.
This verifies the normal-form input. [Rewriting system](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system).

At \(s=1\), I tabulated the eight values of \(L_p(t)=t^2+c_pt\) and composed these maps.
The rank-one predecessors of \(a,\ldots,g\) were \(bdg,bcf,afg,acd,ceg,abe,def\), exactly the cyclic predecessor sets. [Predecessor table](../../claims/Yin_C_A0106_v1.md#argument).
For each \(p\), every cyclic triangle \(pqr\) gives the same \(M_p=L_qL_r\) since its skew polynomial is \((1+s)(X+c_p)^{-1}\).
The two zero composites with \(L_p\) identify \(\operatorname{im}M_p=\ker L_p\) and \(\ker M_p=\operatorname{im}L_p\) by their dimensions.
Appending a permitted positive factor \(L_q\) preserves rank two because its image misses the previous kernel line except at zero, and gives \(\ker L_q\) as the new kernel.
In a negative run each adjacent composite is nonzero since the reversed positive pair is outside the triangle list.
Induction from the right gives the image line of its first factor.
At a mixed join the two indices differ, so the distinct image and kernel lines give rank one.

As a separate check over words of *all* lengths, I enumerated states \((\ell,A)\) consisting of the last signed letter and the table of the composite linear map on the eight elements of \(E\).
Starting from the fourteen one-letter states, I appended each letter \(q\) for which \(\ell q\) admits no rule, forming \((q,A\circ L_q)\) for a positive letter and using \(M_p\) for \(q=p^{-1}\).
Iteration until no new states appeared gave 49 states of rank one and 294 of rank two.
Every nonempty irreducible word reaches a state by induction on its length, and every transition extends an irreducible word because the rule left sides have length two.
Thus no such word evaluates to a scalar map after its inverse letters are cleared by central factors.
Every polynomial in \(\mathbb F_2[s]\) evaluates to zero or the identity at \(s=1\).
This distinguishes every nonempty normal word from the projective identity and proves faithfulness of both the projective representation and the normalized lift.

### The finite quotient sequence

The substitution \(T=X^{-1}\) gives \(Tc=\sigma^{-1}(c)T=c^4T\) on \(E\).
In the skew Laurent series ring the lowest coefficient of a product is a product of nonzero field elements after a Frobenius twist.
Factoring off the lowest monomial leaves a unit of the form \(1+O(T)\), invertible by a geometric series.
This provides an injective extension through the central localization.
The filtration by order in \(T\) is two-sided and preserved by conjugation by \(X\).
Modulo \(T^{m+1}\), the degree-\(m\) coefficients add under multiplication in \(U_m\), since \(2m\ge m+1\).
Every value in \(E\) occurs, giving \(|U_1/U_m|=8^{m-1}\), and the first nonconstant nonzero coefficient of a nonidentity element of \(U_1\) distinguishes it in some quotient.

Write \(z=T^3\).
For \(b=1+\sum_{j\ge1}b_jz^j\) the coefficient of \(z^j\) in \(b^3\) is \(3b_j\) plus a polynomial in earlier coefficients.
This gives the required unique central cube root of \(1+z\).
Conjugation by \(X\) has cube the identity, so sending \(\tau\) to the projective class of \(X\) respects the semidirect-product relations.
For a triangle the unnormalized product of the three power-series coordinates is \((1+s)X^{-3}=1+z\), and the three factors of \(b^{-1}\) cancel it.
In the projective group the image of each resulting generator is \([X+c_p]\), since \(b\) is central.
If an element of \(D^\times\) is central in the Laurent series ring, it commutes with every element of \(D\) and belongs to \(K^\times\).
Thus an element in the kernel of the semidirect-product representation also lies in the kernel of the faithful projective representation and is the identity.
Taking its finite images produces nested kernels with trivial intersection.
The type projection is surjective at every level, with kernel a subgroup of \(U_1/U_m\).
Restriction of the same maps separates every subgroup of \(\ker d\) by finite \(2\)-groups.
This completes the independent review of all conclusions in C_A0108_v1.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0108_v1.md#statement) | The seven labels, the center and both faithful representations, the nested separating finite images over the specified type map, and residual finite \(2\)-group separation for every subgroup of its kernel. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0108_v1.md#argument) | Central localization, triangular products, integral normalization on the type kernel, rank detection of all nonempty normal words, skew Laurent series and the finite quotients. |
| [Whole finding](#whole-finding) | [Presentation identification](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation) | Both presentation maps for the group in this claim. |
| [Whole finding](#whole-finding) | [Rewriting system](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) | The two-letter rules, termination, joining and the resulting normal words. |
| [Whole finding](#whole-finding) | [Predecessor table](../../claims/Yin_C_A0106_v1.md#argument) | The seven predecessor sets used for the ranks of the evaluated pairs. |

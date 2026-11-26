---
author: Yin
---

# A scalar idempotent for the original Schur kernel at the order-24 marking

## Statement

Suppose a torsion-free scalar-injective group \(H=\langle s,t\rangle\), with the normalized order-24 marks \(3,4\), supports a four-site matrix
\[
           K=B+At-s(D+Ct)
\]
of regular rank \(3/2\).
Write \(U=U(H)\) for the regular affiliated algebra and \(D_j(H)\) for the scalar inverse layers starting with \(D_0(H)=\mathbb CH\).
Choose any nonzero entry as pivot and permute rows and columns so that the resulting matrix is \(\left(\begin{smallmatrix}a&b\\ c&d\end{smallmatrix}\right)\).
Let \(\sigma=d-ca^{-1}b\) be the actual first Schur complement.
There is a scalar algebraic idempotent \(h\in D_1(H)\) with affiliated image exactly \(\ker\sigma\), of von Neumann dimension \(1/2\).
The orthogonal projection onto that kernel is in \(D_2(H)\).
For this particular kernel the two assertions hold inside the original group, including the remaining case of a perfect commutator subgroup.
They do not assume a spectral gap.

More precisely the expression for \(h\) uses just the two scalar inverses of \(a\) and \(\det(Ct+D)\) over the group ring.
No nonzero group-ring scalars \(u,v\) can satisfy \(uhv\in\mathbb CH\).
The orthogonal projection can be obtained with one further scalar inverse after adjoining adjoints in the first layer.
These statements distinguish the algebraic idempotent, which can be unbounded, from its orthogonal range projection.

For each \(\omega^4=1\), let \(K_\omega=B+At-\omega s(D+Ct)\); choose the corresponding pivot entry after the same permutations.
The resulting four scalar idempotents \(h_\omega\), with \(h_1=h\), satisfy
\[
                 \sum_{\omega^4=1}[h_\omega]=2[1]
                           \quad\text{in } K_0(D_1(H)).
\]
They are the orbit of \(h\) under the four actual character twists fixing \(t\) and multiplying \(s\) by \(\omega\).
In particular an invariant homomorphism \(K_0(D_1(H))\to\mathbb Z\) taking an odd value on the unit excludes the half kernel.
The direct sum of the four phase matrices \(K_\omega\) has inner rank exactly six over \(D_1(H)\).
This last factorization concerns all four phase matrices together.

## Resolving the finite-order transfer

Let \(Q=Ct+D\) and \(V=(s^{-1}I_2)(At+B)Q^{-1}\).
The entries of \(Q\) commute and \(\det(Ct+D)\) is a nonzero polynomial in the infinite-order element \(t\), so the usual adjugate formula supplies \(Q^{-1}\).
The [order-four transfer equality](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) gives \(V^4=I_2\) over \(U\), with all four eigenspaces of regular dimension \(1/2\).
The scalar character twists act on \(U\) by trace-preserving automorphisms and preserve each actual inverse layer.
Define
\[
             e_\omega=\frac14\sum_{j=0}^3\omega^{-j}V^j,\qquad
             E_\omega=Q^{-1}e_\omega Q .
\]
Finite polynomial interpolation gives complementary idempotents \(e_\omega\) summing to \(I_2\).
On its image \(V\) acts by \(\omega\); on the other images \(V-\omega I_2\) acts by nonzero scalars.
Since \(K_\omega=(sI_2)(V-\omega I_2)Q\), the affiliated image of \(E_\omega\) is exactly \(\ker K_\omega\).
All entries of these idempotents use only \(\det(Ct+D)^{-1}\) as a new scalar inverse.
The character taking \(s\) to \(\omega s\) and fixing \(t\) sends \(e_1\) to \(e_\omega\) and \(E_1\) to \(E_\omega\).
If the pivot uses column permutations, conjugate all \(E_\omega\) by the corresponding constant change of coordinates; row permutations preserve the kernel.

## Recovering the scalar idempotent from the Schur coordinate

Write \(a_\omega,b_\omega,c_\omega,d_\omega\) for the entries of the permuted phase matrix and \(\sigma_\omega=d_\omega-c_\omega a_\omega^{-1}b_\omega\).
The character relation makes all chosen \(a_\omega\) nonzero group-ring scalars, hence affiliated units by hypothesis.
Put
\[
       \theta_\omega=\binom{-a_\omega^{-1}b_\omega}{1},\qquad
       \pi=(0,1),\qquad h_\omega=\pi E_\omega\theta_\omega .
\]
In right affiliated modules the two row equations identify the kernel of the permuted \(K_\omega\) with \(\theta_\omega\ker\sigma_\omega\), with inverse \(\pi\).
Thus \(h_\omega\) takes values in \(\ker\sigma_\omega\) and acts as the identity there.
It is the required idempotent, with its two specified denominators and affiliated rank \(1/2\).
Multiplication on either side by a nonzero group-ring scalar preserves that rank, whereas every group-ring scalar has rank zero or one.

For the orthogonal projection set \(h=h_1\) and define
\[
       G_h=hh^*+(1-h^*)(1-h),\qquad p=hh^*G_h^{-1}.
\]
Both terms of \(G_h\) are positive affiliated scalars.
The support of \(hh^*\) is the image projection of \(h\).
The support of \((1-h^*)(1-h)\) is the initial projection of \(1-h\), the orthogonal complement of \(\ker(1-h)=\operatorname{im}h\).
Thus \(G_h\) is an affiliated unit, and \(p\) is the identity on the first support and zero on the second.
It is the orthogonal kernel projection of \(\sigma\) and lies in \(D_2(H)\) since the first layer is closed under adjoints.
This uses the finite-order transfer for this input, whereas the [free cyclic construction](Yin_C_A0124_v1.md#statement) applies to arbitrary rational scalar ranks in an enlarged group.

## The phase orbit and a six-coordinate factorization

Let \(R=D_1(H)\).
The maps \(\pi,\theta_\omega\) identify the right projective modules \(E_\omega R^2\) and \(h_\omega R\).
Indeed \(\pi E_\omega\) takes its values in the latter, \(\theta_\omega h_\omega\) in the former, and the two restrictions are inverse: the identities hold in \(U\) by the Schur coordinate argument and all their entries belong to \(R\).
Since the conjugated \(E_\omega\) still split the identity, their projective classes sum to \(2[1]\).
The same constant row and column permutations were used at each phase, so \(h_\omega\) is the actual character translate of \(h\).
An invariant integer-valued homomorphism would send the left side of the formula to a multiple of four, proving the stated odd-value obstruction.

Over \(R\), the image of \(V-\omega I_2\) is \(\bigoplus_{\nu\ne\omega} e_\nu R^2\), since its nonzero scalar eigenvalues on those summands can already be inverted over \(\mathbb C\).
The outer factors \(sI_2,Q\) in \(K_\omega\) are units over \(R\).
Consequently the image module for \(\bigoplus_{\omega^4=1}K_\omega\) is isomorphic to three copies of \(\bigoplus_\nu e_\nu R^2=R^2\).
An isomorphism of the image with \(R^6\), followed by its inclusion, gives a factorization through six coordinates.
The regular rank of the direct sum is six, so no smaller factorization over \(R\) exists.

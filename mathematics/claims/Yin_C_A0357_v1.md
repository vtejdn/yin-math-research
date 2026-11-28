---
author: Yin
---

# Character rank excess and cancellation of a second inverse in the full \((2,3,11)\) triangle lift

## Statement

Let \(\Gamma\) be the full inverse image of the orientation-preserving hyperbolic triangle group of orders \(2,3,11\) in the universal cover of \(\operatorname{PSL}_2(\mathbb R)\).
This torsion-free two-generator group has abelianization \(C_5\), perfect commutator subgroup and integer regular nullity for every complex group-ring matrix.
There are four-square group-ring matrices of regular rank two for which the trivial character gives rank three and four, respectively.
In both cases the kernel has an affiliated basis with a constant left inverse and an orthogonal projection satisfying the original matrix kernel equation.
In the rank-four example every compression by a nonzero constant row and column repeated on the two positions is an affiliated unit matrix whose inverse lies outside \(M_2(\ell^1(\Gamma))\).

In the rank-four example a two-square pivot block can be chosen so that the inverse of the second Schur pivot is \((1+x)^{-1}\), where \(x\) is an infinite-order generator surjecting onto \(C_5\).
Here the sign on one row block is normalized by a constant coordinate change. For its finite-support regularizations specified below, the total absolute coefficient mass is \(n4^{-n}\binom{2n}{n}\).
On each of the five cosets of the commutator subgroup the absolute mass is one fifth of this amount up to a bounded error, whereas the signed coefficient sum on each coset stays bounded.
Both scalar pivot values are nonzero at all five characters.
In the rank-three example a constant change of coordinates makes the first pivot \(2+x\) invertible in \(\ell^1(\Gamma)\) and the second pivot \(1-(2+x)^{-1}\).
Its inverse \(1+(1+x)^{-1}\) is unbounded in the regular representation.
The trivial character can be replaced by any prescribed one of the five marking characters by a unitary character twist.

Thus the numerical rank excess, an inverse outside \(\ell^1\), divergent absolute mass with cancellation inside the individual abelianization cosets, and the kernel projection identities coexist in a group satisfying the complex strong Atiyah conjecture.
The matrices here are built from relators of \(\Gamma\).
The [commutator on the actual common sign subgroup](Yin_C_A0344_v2.md#statement) in the order-twenty half-kernel problem has additional constraints from its two involutions and the simultaneous compressions.

## The central generator and the perfect index-five subgroup

The [full lift presentation and torsion-freeness](Yin_C_A0194_v1.md#an-explicit-perfect-marking) give generators \(x,y,w\) with \(x^2=y^3=w^{11}=xyw=z\), where \(z\) is central of infinite order.
Eliminating \(w=z(xy)^{-1}\) gives \((xy)^{11}=z^{10}=x^{20}\).
Conversely \(x^2=y^3\) implies that their common value commutes with both \(x\) and \(y\).
The presentation on \(x,y\) therefore has relators
\[
             r_1=x^2y^{-3},\qquad r_2=(xy)^{11}x^{-20}.
\]
Their exponent rows are \((2,-3)\) and \((-9,11)\), with determinant \(-5\).
The abelianization has order five, and the assignment \(x\mapsto1,\ y\mapsto4\) in \(\mathbb Z/5\mathbb Z\) identifies it.
Here \(z=x^2\) maps to \(2\).

The subgroup \(H_{11}=\langle xz^2,yz^{-2}\rangle\) is perfect by the [two-generator lift calculation](Yin_C_A0194_v1.md#an-explicit-perfect-marking).
Both displayed generators have trivial image in the abelianization.
Since \(z\) is central and \(\Gamma=H_{11}\langle z\rangle\), \(H_{11}\) is normal with cyclic quotient.
Moreover \((xz^2)^2=z^5\) belongs to \(H_{11}\), so the quotient has order at most five.
The abelianization makes its order at least five.
It follows that \(\Gamma'=H_{11}\) is perfect.
The [surface-subgroup argument](../ledger/Yin_L_A0082_v1.md#the-surface-subgroup-and-its-central-extension) puts \(H_{11}\) in Linnell's class \(\mathcal C\).
Closure under finite-quotient extensions puts \(\Gamma\) in that class, and [Linnell's theorem](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) gives the asserted complex integrality.

## The relator rows and two pivot choices

To make the individual fiber compressions explicit, use the equivalent second relator \(\mu^{11}x^{-2}\) in place of \(r_2\), where \(\mu=y^{-1}x=w\) because \(xyw=x^2\).
Its exponent row is \((9,-11)\).
Define a Fox row \(D(u)\) by \(D(x)=(1,0),\,D(y)=(0,1)\), \(D(uv)=D(u)+uD(v)\) and \(D(u^{-1})=-u^{-1}D(u)\), with word coefficients evaluated in \(\Gamma\).
Writing \(v=(x-1,y-1)^{\mathsf T}\), induction gives \(D(u)v=u-1\).
Let \(B\) have rows \(D(r_1),D(\mu^{11}x^{-2})\).
The recurrence defining these rows and the identities \(x^2=y^3=\mu^{11}\) give
\[
 B=\begin{pmatrix}a&u\\h-a&-h\end{pmatrix},\quad
 a=1+x,\quad u=-(1+y+y^2),\quad h=\sum_{k=0}^{10}\mu^k y^{-1}.
\]
Thus \(Bv=0\) and the augmentation of \(B\) is the exponent matrix of determinant \(5\).
The elements \(x-1\) and \(a\) are affiliated units, by the bilateral shift representation of \(\langle x\rangle\).
Thus \(v\) generates a one-dimensional right module over the regular affiliated algebra, and the nonzero pivot \(a\) gives regular rank at least one.
It follows that \(B\) has rank one and its affiliated kernel is exactly the module generated by \(v\).
The column \(v(x-1)^{-1}\) has the constant left inverse \((1,0)\).
The matrix \(v(v^*v)^{-1}v^*\) is a selfadjoint idempotent in the affiliated algebra whose image is this kernel, hence is the bounded orthogonal kernel projection.
At every nontrivial scalar character \(\psi\) the vector \(\psi(v)\ne0\), while \(\psi(a)\ne0\) at every character since \(-1\notin\mu_5\).
Thus the trivial character sees rank two and each other character sees rank one.

Take \(R_3=\operatorname{diag}(1,B,0)\) and \(R_4=B\oplus(-B)\).
These matrices have regular rank two and trivial-character ranks three and four.
Their kernels are direct sums of the preceding kernel and the corresponding coordinate spaces.
The scalar functions \(a,u,h\) are linearly independent in \(\mathbb C\Gamma\).
The images of \(x,y\) in the triangle quotient have orders two and three, so \(a,u\) are independent.
Their combined group support has at most four elements, while the eleven terms of \(h\) are distinct because \(\mu^{11}=z\) has infinite order.
For nonzero constant row \((p,q)\) and column \((r,s)^{\mathsf T}\) their compression of \(B\) has coefficients \(((p-q)r,\ ps,\ q(r-s))\) on \(a,u,h\).
If \(p=0\), equality of all three coefficients to zero would give \(r=s=0\).
If \(p\ne0\), it would give \(s=0\), then \(r\ne0\), then \(q=0\) and finally \(pr=0\).
Thus the compression is a nonzero group-ring scalar and is an affiliated unit by scalar integrality.
Write \(l\) for this compressed scalar.
If its augmentation vanishes, an \(\ell^1\) inverse would contradict augmentation of \(ll^{-1}=1\).
If its augmentation is nonzero, complete the chosen row and column to constant bases putting \(l\) in the first pivot position of \(B\).
The remaining scalar Schur complement vanishes in the affiliated algebra since \(B\) has rank one.
If \(l^{-1}\in\ell^1(\Gamma)\), the same identity holds in the faithfully represented convolution algebra, so augmenting gives a zero Schur complement of the invertible augmented matrix, a contradiction.
Repeating these row and column vectors on the two positions gives a two-square compression of \(R_4\) whose diagonal entries are this unit and its negative.
Also \(R_4\) anticommutes with each constant swap \(\left(\begin{smallmatrix}0&\lambda I\\ \lambda^{-1} I&0\end{smallmatrix}\right)\) for \(\lambda\ne0\).
Multiplying the second output block by \(-I\) and permuting the copies' first coordinates to the front in \(R_4\) produces the leading block \(\operatorname{diag}(a,a)\); its second pivot has inverse \(a^{-1}\).
For \(R_3\) the leading block is \(\operatorname{diag}(1,a)\).
Multiply its two sides by the constant matrix \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\) and its transpose, extending by identity on the other coordinates.
The new leading block is \(\left(\begin{smallmatrix}1+a&1\\1&1\end{smallmatrix}\right)\), with first pivot \(2+x\) and second pivot \(b=1-(2+x)^{-1}\).
The geometric series for \((2+x)^{-1}\) converges absolutely, and \(b^{-1}=1+a^{-1}\) is unbounded since the Haar spectrum of \(x\) contains \(-1\).
The regular ranks and formal numerical ranks are preserved by those invertible changes.
The rational expression for \(b\) and both of its pivot values are defined and nonzero at all five characters.
An invertible constant change of domain transports the affiliated kernel basis and its constant left inverse, and the orthogonal projection is obtained from the transported basis by its Gram inverse.
For any chosen character \(\chi\), multiplying each group coefficient at \(g\) by \(\overline{\chi(g)}\) is a trace-preserving automorphism implemented by multiplication by \(\overline{\chi}\) on the group basis.
It moves the augmented rank excess to \(\chi\).

## Collecting the regularizing products by their actual endpoint

For the unsheared \(R_4\) block the lower diagonal entry of the inverse regularization at \(L=2=\|a\|\) is
\[
 q_n=\tfrac14\sum_{j=0}^{n-1}T^j(1+x^{-1}),\qquad
 T=1-\tfrac14(1+x^{-1})(1+x)=\tfrac14(2-x-x^{-1}).
\]
The endpoint \(L=\|a\|\) is admissible here since \(0\le T\le1\) and its regular spectral projection at one is zero.
Thus \((1+x)q_n=1-T^n\), and \(q_n\) converges in measure to \(a^{-1}\) by scalar Fourier calculus.
All these products lie in the group ring of the infinite cyclic subgroup \(\langle x\rangle\).
Apply \(x\mapsto-x\) in this Laurent ring and denote the image of \(q_n\) by \(q'_n\).
The coefficient of \(x^k\) in the resulting \(j\)-th power of \(T\) is
\[
         p_j(k)=4^{-j}\binom{2j}{j+k},
\]
with the binomial zero outside \([-j,j]\), by expanding \(4^{-j}x^{-j}(1+x)^{2j}\).
Consequently
\[
        [x^k]q_n=\tfrac{(-1)^k}{4}\sum_{j=0}^{n-1}\bigl(p_j(k)-p_j(k+1)\bigr).
\]
For \(k\ge0\) every summand before the alternating factor is nonnegative and for \(k<0\) every such summand is nonpositive.
Thus the signed collisions within each time step are exactly accounted for and collection across times causes no further loss in absolute mass.
Telescoping over \(k\) gives \(\|q_n\|_1=\frac12\sum_{j=0}^{n-1}p_j(0)=n4^{-n}\binom{2n}{n}\).
The last identity follows by induction from \(p_{j+1}(0)/p_j(0)=(2j+1)/(2j+2)\).
Stirling's formula gives \(\|q_n\|_1\sim\sqrt{n/\pi}\).

Let \(S_n\) have probabilities \(p_n(k)\).
The equality \((1-x)q'_n=1-\sum_k p_n(k)x^k\) and finite support show that its coefficient at \(k\ge0\) is \(\mathbb P(S_n>k)\) and its coefficient at \(k<0\) is \(-\mathbb P(S_n\le k)\).
Conditioning on the value of \(S_n\) counts an interval of \(|S_n|\) consecutive integers in the absolute coefficient sum.
Each residue modulo five occurs \(|S_n|/5\) times up to an error at most one on that interval.
As \(x\) generates the abelianization, on every commutator coset the absolute mass of \(q_n\) differs from \(\|q_n\|_1/5\) by at most one.
For any fifth root \(\zeta\),
\[
 q_n(\zeta)=\frac{1-(1-|1+\zeta|^2/4)^n}{1+\zeta}\longrightarrow \frac1{1+\zeta}.
\]
Inverting the five-point Fourier transform shows that the signed coefficient sum on each commutator coset converges.
These exact endpoint counts concern \(q_n\) for \(\operatorname{diag}(a,a)\).
The sheared block gives a separate example of a genuine second rational pivot; no coefficient growth rate for its matrix regularization is asserted.

## Assessment history

### Decision the-triangle-lift-and-the-cyclic-regularization

| Field | Value |
| --- | --- |
| date | 2026-11-28T12:04 |
| status | proved |
| reason | Fox rows in the full triangle lift realize both visible rank excesses with integral regular ranks. The cyclic regularization has explicitly computable absolute and signed mass in every class. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rank-three and rank-four calibrations, scalar pivot inverses and fiber masses. |
| argument | [The central generator and the perfect index-five subgroup](#the-central-generator-and-the-perfect-index-five-subgroup) | The full lift, perfect derived group and complex Atiyah integrality. |
| argument | [The relator rows and two pivot choices](#the-relator-rows-and-two-pivot-choices) | Actual and numerical ranks, compressions, kernel projections and both pivot choices. |
| argument | [Collecting the regularizing products by their actual endpoint](#collecting-the-regularizing-products-by-their-actual-endpoint) | Coefficient cancellation, the total mass and all five residue classes. |
| dependency | [An explicit perfect marking](Yin_C_A0194_v1.md#an-explicit-perfect-marking) | The perfect subgroup and torsion-freeness of the full triangle lift. |
| dependency | [The surface subgroup and its central extension](../ledger/Yin_L_A0082_v1.md#the-surface-subgroup-and-its-central-extension) | Membership of the perfect subgroup in Linnell's class. |
| dependency | [Group class and exact theorems](../audits/literature/Lin93/Yin_U001.md#lin93-u001) | Complex integrality for a torsion-free group in the indicated class. |
| review | [The triangle lift and the cyclic regularization](../audits/reviews/Yin_R_A0245_v1.md#the-triangle-lift-and-the-cyclic-regularization) | Independent review of the complete fixed statement and proof at the indicated interfaces. |

## Current assessment

[Selected decision](#decision-the-triangle-lift-and-the-cyclic-regularization)

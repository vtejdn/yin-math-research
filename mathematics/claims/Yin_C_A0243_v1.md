---
author: Yin
---

# Traceless finite-rank matrices in the range of the commutator sum

## Statement

Let \(G\) have a finite generating list \(S\), let \(H=\ell^2(G)=L^2(\mathcal N(G),\tau)\), and write \(U\) for the affiliated algebra.
For \(g\in S\) let \(\rho_g\) denote right multiplication, and put \(\partial(T)=\sum_{g\in S}[\rho_g,T_g]\) for tuples of bounded operators of finite ordinary rank.
Fix \(q\ge2\).
Consider bounded group von Neumann algebra elements \(x_i,y_i\), regarded as vectors in \(H\), with the following properties.

* There are orthogonal projections \(p_i\) summing to \(1\) such that the closed spans of the left group translates of \(x_i\) and of \(y_i\) both equal \(Hp_i\), for \(1\le i\le q\).
* The vectors satisfy \(\tau(y_j^*x_i)=\delta_{ij}\). Write \(E_{ij}h=x_i\tau(y_j^*h)\) and let \(\mathcal B\) be their complex span.
* The intersection \(\mathcal B\cap\operatorname{im}\partial\) consists exactly of the matrices \(\sum a_{ij}E_{ij}\) with \(\sum_i a_{ii}=0\).

Such vectors exist exactly when the actual \(*\)-regular closure of \(\mathbb CG\) in \(U\) contains a unital copy of \(M_q(\mathbb C)\).
In every such system \(\tau(p_i)=1/q\), and \(\mathcal B\) is an algebra of ordinary finite-rank operators with matrix units \(E_{ij}\).
Its identity has ordinary rank \(q\).
The vectors \(x_i\) are mutually orthogonal, as are the \(y_i\), and the two families can differ.

There are finite-depth versions for the [scalar inverse layers](Yin_C_A0239_v1.md#statement).
From algebraic matrix units in \(D_l(G)\) one may take the \(p_i\) in \(D_{l+1}(G)\), and the \(x_i,y_i\) in \(\mathcal N(G)\cap D_{l+2}(G)\).
Each traceless matrix in \(\mathcal B\) then has a tuple of witnesses whose finite-rank tensors have both factors in this last bounded space.
Conversely, if just the \(x_i\) of such a system belong to \(D_k(G)\), the same group has unital algebraic matrix units in \(D_{k+1}(G)\).
Thus for a reduced nonintegral rational rank \(\rho=p/q\) over \(D_j(G)\) of a finitely generated torsion-free group, the [free extension construction](Yin_C_A0242_v1.md#statement) gives these simultaneous bounded witnesses on any finite marking of \(G*\mathbb Z\) in layer \(j+\lfloor n\rho\rfloor+3\), where \(1\le n<q\) and \(np\equiv1\bmod q\).

## Making the diagonal projections orthogonal

Let \(f_{ij}\) be unital algebraic matrix units and put \(h_m=\sum_{i\le m} f_{ii}\), with \(h_0=0\).
For any affiliated idempotent \(h\) the orthogonal projection onto \(hU\) is
\[
 P(h)=hh^*\big(1-(h-h^*)^2\big)^{-1}.
\]
Indeed the denominator is the sum of \(hh^*\) and \((1-h^*)(1-h)\), whose support modules are \(hU\) and its orthogonal complement.
It is also \(1+(h-h^*)^*(h-h^*)\), hence is an affiliated unit.
Multiplication by its inverse yields the identity on the first support and zero on the second.
In particular \(P_m=P(h_m)\) costs at most one layer above the original matrix units.
The flag \(h_mU\) is increasing, so \(p_i=P_i-P_{i-1}\) form an orthogonal partition.

Projection by \(p_i\) identifies \(f_{ii}U\) with \(p_iU\), with inverse given there by \(f_{ii}\).
Indeed \(h_iU=h_{i-1}U\oplus f_{ii}U\), \(f_{ii}\) kills \(h_{i-1}U\), and \(p_i\) sends each vector in \(h_iU\) to itself modulo \(h_{i-1}U\).
Thus \(a=\sum_i p_i f_{ii}\) has inverse \(\sum_i f_{ii}p_i\).
After conjugating by \(a\), the matrix units \(g_{ij}=a f_{ij}a^{-1}\) have \(g_{ii}=p_i\), and \(g_{ij}=p_i g_{ij}p_j\).
The \(p_i\) all have trace \(1/q\) by their module isomorphisms.
These operations use only \(D_{l+1}\) when \(f_{ij}\in D_l\), and stay in the regular closure when starting there.

## Simultaneous bounded witnesses on one marking

Write \(A=\mathbb CG\).
For any traceless scalar matrix \((a_{ij})\) the tensor
\[
             \sum_{i,j}a_{ij}g_{1i}\otimes g_{j1}
\]
vanishes in \(U\otimes_A U\).
Indeed each element of the regular closure can be moved across this balanced tensor product by the [equalizer theorem](Yin_C_A0131_v1.md#the-equalizer-in-the-affiliated-ring), and \(g_{1i}g_{j1}=\delta_{ij}p_1\).
In the complex tensor product the displayed tensor is consequently a finite sum of balances \(\Psi_g(u,v)=ug\otimes v-u\otimes gv\), \(g\in S\), by [word expansion](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank).

When \(g_{ij}\in D_{l+1}\), all factors \(u,v\) can be chosen in \(D_{l+1}\).
To see this, expand \(\delta(z)=z\otimes1-1\otimes z\) from any inverse expression, using outer bimodule multiplication, the product rule and \(\delta(z^{-1})=-z^{-1}\delta(z)z^{-1}\).
For group elements use the product rule on words in the marked generators and their inverses.
Apply this expansion to \(\sum a_{ij}\delta(g_{1i})g_{j1}\), which equals the displayed tensor by the matrix unit relations.

Take these finite expansions for a basis of traceless matrices and multiply their outer ends by \(p_1\), which fixes their left sides.
Let the resulting first and second factors of the input balances be \(u,v\), so \(u=p_1u,\ v=vp_1\).
Include the \(g_{1i}\) in the first list and \(g_{i1}\) in the second.
In the corner \(p_1Up_1\) take
\[
          c=\left(p_1+\sum_u uu^*+\sum_v v^*v\right)^{-1}.
\]
This is a bounded positive element with support \(p_1\); the corner inverse is obtained by adding \(1-p_1\) before inversion in \(U\) and cutting by \(p_1\).
Each \(cu\) and \(vc\) is bounded because its squared norm is controlled by the norm of \(c\) before rescaling, using \(c(c^{-1})c=c\).
Rescale \(c\) by a positive constant so that \(\tau(c^2)=1\).
This uses at most one further scalar inverse in the finite-layer case.

Set \(x_i=cg_{1i},\ y_i^*=g_{i1}c\).
Both vectors \(x_i,y_i\) have right support \(p_i\), since \(c\) has full corner support and the matrix units give isomorphisms between the support modules.
The [left-translate span formula](Yin_C_A0157_v1.md#rank-one-commutator-sums-on-one-fixed-marking) gives \(Hp_i\) for each.
Since \(x_i y_j^*=\delta_{ij}c^2\), traciality gives biorthogonality and the \(E_{ij}\) multiply as matrix units.
After clearing the balances on both outer sides by \(c\), the finite-tensor correspondence \(u\otimes v\mapsto(h\mapsto u\tau(vh))\) turns them into the required commutators for each basis matrix.
Linearity supplies all traceless combinations.
Conversely the ordinary trace vanishes on every such commutator, while the trace of \(\sum a_{ij}E_{ij}\) is \(\sum_i a_{ii}\).
This proves the exact intersection for the original marking.

## Recovering the matrix units from the witnesses

Suppose a system as in the statement is given, with no inverse-layer premise on the bounded vectors.
For every left multiplier \(z\in\mathcal N(G)\), the ordinary trace of \(z\partial(T)\) is zero by cyclicity and commutation with right translations.
Applying this to \(E_{ii}-E_{jj}\) gives \(\tau(z(x_i y_i^*-x_j y_j^*))=0\) for every \(z\), hence all the products \(x_i y_i^*\) equal one element \(b\).
The initial support of \(x_i\) and the final support of \(y_i^*\) are both \(p_i\).
Thus \(bU=x_iU\) for every \(i\), its final support is a common projection \(e\), and \(\tau(p_i)=\tau(e)=1/q\).

Use a dagger for the relative inverse in \(U\), and put \(v_{ij}=x_i^\dagger x_j\).
The relations \(x_i x_i^\dagger=e,\ x_i^\dagger x_i=p_i\) and the orthogonality of the \(p_i\) give \(v_{ij}v_{hk}=\delta_{jh}v_{ik}\), \(v_{ii}=p_i\).
To verify membership in the regular closure, every boundary tensor vanishes over \(A\).
Right multiplication on the second tensor factor by \(b^\dagger\) replaces \(y_i^*\) by \(x_i^\dagger\), because \(y_i^*=x_i^\dagger b\) and \(bb^\dagger=e\).
The off-diagonal boundaries therefore give \(x_i\otimes_A x_j^\dagger=0\) for \(i\ne j\), and the diagonal differences give \(x_i\otimes_A x_i^\dagger=x_j\otimes_A x_j^\dagger\).
Multiplying the first identities on the outer sides by \(x_i^\dagger,x_j\) gives \(p_i\otimes_A p_j=0\) off the diagonal.
Summing over the partition gives \(p_i\otimes_A1=1\otimes_A p_i\).
Multiplying the diagonal equality on the outer sides by \(x_i^\dagger,x_j\) gives \(p_i\otimes_A v_{ij}=v_{ij}\otimes_A p_j\).
The equalizer property just proved for \(p_i,p_j\) now gives \(1\otimes_A v_{ij}=v_{ij}\otimes_A1\), proving the claimed membership.

If \(x_i\in D_k\), put \(T=\sum_i x_i^*x_i\).
Its blocks on the partition \(p_i\) have full support there, so \(T\) is an affiliated unit.
The element \(T^{-1}x_i^*\) equals \(x_i^\dagger\), by restriction to its two supports.
Thus \(v_{ij}=T^{-1}x_i^*x_j\) belongs to \(D_{k+1}\) in this same group.

## Off-diagonal rank-one boundaries alone

In the cyclic group \(C_q\), right multiplication by a generator is diagonal with \(q\) distinct eigenvalues in the character basis.
For any matrix \(T\) its commutator with this translation multiplies the \((i,j)\) entry by the difference of the corresponding eigenvalues.
Hence every off-diagonal matrix is a boundary in this basis, and every diagonal entry of a boundary is zero.
The character directions give a partition by cyclic spans, each of trace \(1/q\).
Nevertheless the group algebra is already a commutative regular algebra, so the full traceless system in the statement is impossible in any choice of directions.
This example distinguishes the simultaneous diagonal-difference requirement from the existence of all the individual off-diagonal rank-one outputs.

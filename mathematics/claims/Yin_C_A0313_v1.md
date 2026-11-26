---
author: Yin
---

# Central commutators at the noncyclic order-twenty marking

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and assume every nonzero element of \(\mathbb CH\) acts injectively in the regular representation.
Suppose \(H\) maps onto \(C_5\times C_2^2\) with marked images \((1,e_1),(2,e_2)\), where \(e_1,e_2\) are independent.
For \(K=B+At-s(D+Ct)\) with complex two-by-two corners write \(\delta=\dim_H\ker K\) with unnormalized coordinate trace.
If \(\delta=1/2\), then
\[
                       [H,H]=[H,[H,H]] .
\]
Every nilpotent image is abelian and every dihedral image is abelian.
In particular such an \(H\) cannot be residually nilpotent.
The [order-twenty classification](Yin_C_A0311_v1.md#statement) covers all other markings and gives \(H_{\rm ab}=C_5\times C_2^2\) at the putative half kernel.

More quantitatively, suppose \(0<\delta<1\), all four corners and \({\cal P}=\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) are invertible, and \(H\) has a quotient \(P\) of order eight with nontrivial central commutator and \(P_{\rm ab}=C_2^2\).
For the projected generators \(u,v\) write \(u^2=c^{f_s},v^2=c^{f_t}\), where \(c=[u,v]\) has order two and \(f_s,f_t\in\{0,1\}\).
Then \(\delta\le19/40\), and \(\delta\le9/20\) when \(f_s\ne f_t\).
Under the same corner and scalar assumptions every nonabelian dihedral quotient gives \(\delta\le9/20\).
The class-two conclusion concerns the lower central series and leaves the possible abelianization of \(H'\) open.

## The four square choices and their representations

The two generators of \(P\) have independent images modulo \(c\).
Its presentation on \(u,v,c\) is given by the displayed squares, \(c^2=1\), centrality of \(c\), and \(vu=cuv\).
Indeed these relations reduce all words to \(c^i u^j v^k\) with \(0\le i,j,k<2\), and the actual group has order eight.

For \(z^{20}=1\) take two complex coordinates indexed by \(0,1\).
Let \(U(z)\) and \(V(z)\) interchange the coordinates, with transports out of \(0,1\) weighted by \(z^{a_0},z^{a_1}\) and \(z^{b_0},z^{b_1}\), respectively.
The following table selects an integer \(l\) and signed sums \(S,T\).

| \(f_s,f_t\) | \(l\) | \(S\) | \(T\) |
| --- | --- | --- | --- |
| \(0,0\) | 0 | 0 | 0 |
| \(0,1\) | 3 | 4 | \(-2\) |
| \(1,0\) | 1 | \(-2\) | \(-4\) |
| \(1,1\) | 3 | \(-6\) | \(-2\) |

One has \(S\equiv8l+10 f_s,\ T\equiv16l+10 f_t\bmod20\), and \(|S|+|T|<10\).
Put
\[
 p=(S+T+10)/2,\qquad q=(S+T-10)/2,\qquad
 (a_0,a_1,b_0,b_1)=(0,S,p-S,q).
\]
The pure two-edge costs are \(S,T\) and the mixed costs are \(p,q\).
Consequently \(U(z)^2=z^S I,\ V(z)^2=z^T I,\ V(z)U(z)=z^{10}U(z)V(z)\).
In the last equality the two column ratios are \(z^{p-q}\) and its inverse, which agree on the twenty roots.
It follows from the presentation that \(u\mapsto z^{-4l}U(z),\ v\mapsto z^{-8l}V(z),\ c\mapsto z^{10}I\) is a unitary representation of \(P\).
Tensor its pullback with the order-five character of \(H\) taking \(s,t\) to \(z^{4l},z^{8l}\).
The resulting assignment \(s\mapsto U(z),t\mapsto V(z)\) therefore represents the actual group \(H\) at every one of the twenty roots.
For \(z=1\) both matrices are the swap, so the representation splits into the trivial character and the sign character taking both marks to \(-1\).
[Regular absorption](Yin_C_A0200_v1.md#the-degree-one-pencil-from-two-reflections) gives kernel dimension \(2\delta\) for the rectangle twisted by the two channels at each of the twenty parameters.

## A group-ring return matrix on twenty coordinates

Give the two \(s\)-edges costs \(a_0,a_1\) and the two \(t\)-edges costs \(b_0,b_1\).
At each vertex write \(X,Y\) for the outgoing \(t,s\) values and \(T_{\rm in},S_{\rm in}\) for their incoming values.
The equations
\[
             S_{\rm in}=BX+AT_{\rm in},\qquad
             Y=DX+CT_{\rm in}
\]
recover the twisted rectangle by substituting \(Y\) and transporting the edge values via \(z^{a_j}s,z^{b_j}t\).
Any two of the four ports determine the others by constant matrices, since all four corners and \({\cal P}\) are invertible. [Local port equations](Yin_C_A0226_v1.md#reversing-the-edges-of-a-minimum-circulation)

Reverse the \(s\)-edge from \(0\) and the \(t\)-edge from \(1\).
This reverses one input and one output at each vertex, inverting the group translation and negating the exponent on each reversed edge.
For \(z\ne0\) the resulting equations are equivalently solved by the new incoming ports prescribing the outgoing ones.
Their two costs from \(0\) to \(1\) are \(b_0,-b_1\), and those from \(1\) to \(0\) are \(a_1,-a_0\).
Every two-edge directed cycle now has positive cost.
Indeed the four sums are \(p,T-q,S-q,-q\), and
\[
              q<\min(0,S,T,S+T)\le\max(0,S,T,S+T)<p
\]
follows from \(|S|+|T|<10\).
Scale both ends of every port at vertex \(j\) by the same power \(z^{d_j}\).
Take \(d_0=0\) and \(d_1=-\min(b_0,-b_1)\).
This subtracts the minimum forward cost from both forward edges and adds it to both backward edges.
The four resulting exponents \(k_e\) are nonnegative, with zero edges only from \(0\) to \(1\), and their sum is \(p-q=10\).

For each positive edge \(e\) with outgoing value \(O_e\), introduce \(k_e\) two-coordinate states \(v_{e,j}=z^j O_e,\ 1\le j\le k_e\).
On such an edge the incoming port is \(g_e v_{e,k_e}\), where \(g_e\) is the possibly reversed group translation.
On a zero edge it is \(g_e O_e\).
From the last states of the positive edges one recovers every outgoing port by the local constant solutions, first at vertex zero and then at vertex one, since the zero edges all point forward.
These recovery matrices have entries in \(\mathbb CH\).
The first-state equations \(v_{e,1}=z O_e\) and the shifts \(v_{e,j}=zv_{e,j-1}\) now have the form \(v=zLv\) for a square matrix \(L\) over \(\mathbb CH\) of size \(2\sum_e k_e=20\).
For each \(z\ne0\) these substitutions are mutually inverse on solutions, including the identification with the original twisted rectangle through its \(X\) ports.
On ordinary group-ring columns all the transformations at a fixed nonzero parameter preserve ordinary group-ring entries.

The twenty eigenspaces of \(L\) at the twentieth roots therefore have dimension \(2\delta\) each.
The eigenspace at one contains no nonzero group-ring column, since the original twist splits there into two rectangles of nullity \(\delta<1\), and any nonzero group-ring column in such a kernel would generate a module of dimension one.
If \(L^{20}=I\), the interpolation idempotent for its eigenvalue one would be a nonzero group-ring matrix with all columns in that eigenspace, since \(\delta>0\).
Hence \(L^{20}-I\) has a nonzero group-ring entry and regular rank at least one.
Interpolation identifies its kernel with the direct sum of the twenty eigenspaces and gives \(40\delta\le19\).

In the two mixed-square rows \(a_0,a_1,b_0,b_1\) are all even.
Divide all costs by two, use ten parameters \(w^{10}=1\) and choose any square root \(z\) of \(w\).
The two initial matrices with divided exponents at \(w\) are exactly \(U(z),V(z)\), so all ten assignments are again genuine and the assignment at one is the pair of swaps.
The reversed costs now sum to five and have the same strict cycle inequalities.
The identical elimination gives a ten-coordinate group-ring matrix and \(20\delta\le9\).

## Nilpotent and dihedral images

At a half kernel all required corners and the assembly are invertible by the [endpoint test](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case) and [four-column reduction](Yin_C_A0184_v1.md#statement).
The abelianization is exactly \(Q=C_5\times C_2^2\).
In the class-two quotient \(G=H/[H,[H,H]]\) the commutator subgroup is central, generated by a single element \(c\) since \(G\) has two generators.
The alternating commutator pairing on \(Q\) factors through its exterior square \(C_2\): the fifth-primary component is cyclic, all pairings between different primary components are trivial, and the two independent binary generators have pairing of order dividing two.
Thus if \(c\ne1\), then \(G\) is nilpotent of order forty.
Its Sylow decomposition has a factor \(P\) of order eight with \(P'= \langle c\rangle\) and \(P_{\rm ab}=C_2^2\).
The quantitative result for \(P\) contradicts \(\delta=1/2\).
Hence the second and third lower central subgroups of \(H\) coincide, as do all subsequent terms.
It follows that all nilpotent images are abelian.
The group \(H\) itself is nonabelian, since its abelianization is nontrivial and finite while \(H\) is torsion-free.

Finally suppose a dihedral image has rotations of finite order \(m\ge3\).
If both marks are reflections, the [two-reflection inequality](Yin_C_A0200_v1.md#statement) gives \(\delta\le1/m\).
Otherwise exchange the marks by the adjoint rectangle and inversions if necessary so \(s\) is a reflection and \(t\) generates the rotations.
The two independent binary characters and the normalized fifth-primary slope persist under interchange and inversion up to the [marking symmetries](Yin_C_A0311_v1.md#the-noncyclic-quotient-of-order-twenty).
At \(m=4\) the projected generators have mixed squares and the ten-parameter bound applies to the original or normalized marking.
When \(m\) is odd, combine the dihedral quotient with the binary character trivial on the reflection and negative on the rotation.
The marked rotation in the product now has order \(2m\), the reflection still squares to one and conjugates it to its inverse.
Thus in every remaining case there is a marked dihedral quotient with rotation period \(M\ge6\).

At each \(z^M=1\) send the reflection to the swap and the rotation to \(\operatorname{diag}(z,z^{-1})\).
After multiplying the second column block by \(z\), the twisted rectangle is a four-square pencil of degree one with constant coefficient
\[
       \begin{pmatrix} B&-sCt\\ -sD&At\end{pmatrix}.
\]
Eliminating \(B\) gives \((A-s^2 D B^{-1} C)t\), a regular unit since its constant matrix at \(s^2=0\) is \(A\) and \(s^2\) has infinite order.
The [column-degree inequality](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) gives \(2M\delta\le4\).
Thus \(\delta\le1/3\) here.
An infinite dihedral image has a finite dihedral quotient with six rotations, giving the same bound.

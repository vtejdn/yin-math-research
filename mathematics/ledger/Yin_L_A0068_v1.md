---
author: Yin
---
# A cyclic change of generators for the type-preserving Gardam subgroup

The type-preserving subgroup of Gardam's group is isomorphic to the type-preserving subgroup of the cyclic triangle group in Barker, Boston, Peyerimhoff and Vdovina.
The latter group has a faithful representation by upper unitriangular matrices over \(\mathbb F_2\).
Together these facts give explicit separating finite \(2\)-group representations of the type-preserving subgroup and hence of all seven index-six ratio groups in [C106v2](../claims/Yin_C_A0106_v2.md#statement).
This supplies a literature-based route to the finite quotients used for the convolution questions in [A0001](../tasks/Yin_T_A0001_v1.md#contract) and [A0002](../tasks/Yin_T_A0002_v1.md#contract).

## Two triangle presentations

Let \(\Gamma\) have positive generators \(a,b,c,d,e,f,g\) and triangular relations
\[
                  acb,\ add,\ afg,\ bbf,\ cef,\ cdg,\ eeg.
\]
This is the presentation identified with Gardam's two-generator group in [C105v2](../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
Use the cyclic triangle presentation
\[
       A=\langle x_i\ (i\in\mathbb Z/7)\mid
                       x_i x_{i+1}x_{i+3}=1\ (i\in\mathbb Z/7)\rangle .
\]
Write \(\tau_\Gamma,\tau_A\) for the maps to \(\mathbb Z/3\) taking every positive generator of the respective presentation to \(1\).
Multiplication of indices by \(2\) gives an order-dividing-three automorphism \(s\) of \(A\).
Indeed \((2i,2i+2,2i+6)\) is a cyclic rotation of the defining triple starting at \(2i-1\), and \(2^3=1\bmod7\).
Number the letters of \(\Gamma\) by the bijection
\[
              p(a,b,c,d,e,f,g)=(1,6,0,3,5,2,4).
\]
On these letters let \(\delta\) act by doubling their \(p\)-indices, so its cycles are \((a\,f\,g)(b\,e\,d)\) with \(c\) fixed.
It takes the seven defining words, in the displayed order, to \(fce,fbb,fga,eeg,cdg,cba,dda\), all cyclic relations.
It therefore acts on \(\Gamma\), with \(\delta^3=1\).

An isomorphism of semidirect products is given by
\[
 \begin{aligned}
   \Gamma\rtimes_\delta\langle h\rangle &\longrightarrow A\rtimes_s\langle l\rangle,
       &h&\longmapsto l, &v&\longmapsto x_{p(v)}^{-1}l ,
       &h^3&=l^3=1 .
 \end{aligned}                                                     \tag{1}
\]
The defining conjugation follows from \(p(\delta v)=2p(v)\).
For a triple \(v w y\) the image of the relation, after cancelling the three powers of \(l\) and taking inverses, has index triple \((4p(y),2p(w),p(v))\).
For the seven displayed relators these triples in order are
\[
       (3,0,1),\ (5,6,1),\ (2,4,1),\ (1,5,6),\
       (1,3,0),\ (2,6,0),\ (2,3,5).
\]
Each is a cyclic relation of \(A\).
Rotating \(vwy\) to \(wyv\) rotates the resulting triple and multiplies its entries by \(4\), preserving the cyclic relations of \(A\).
The index-triple map is injective on ordered triples, so it takes the 21 cyclically based triangle relations of \(\Gamma\) onto all 21 of \(A\).
Conversely, in the left semidirect product of (1) define \(X_i=h\,v^{-1}\) for \(p(v)=i\).
Conjugation by \(h\) takes \(X_i\) to \(X_{2i}\).
The equality \(v=X_{p(v)}^{-1}h\) converts each relation \(vwy=1\) into the corresponding relation for the \(X_i\) by the preceding calculation.
Exhaustion of the 21 triples proves that \(x_i\mapsto X_i\), \(l\mapsto h\) defines a homomorphism in the opposite direction.
Both composites fix their displayed generators, proving (1).

An element of \(\Gamma\) maps into \(A\) precisely when its \(l\)-coordinate \(\tau_\Gamma\) vanishes.
Its \(A\)-component has type \(-\tau_\Gamma\), since \(s\) preserves \(\tau_A\).
Conversely, under the inverse map an element of \(A\) has \(h\)-coordinate \(\tau_A\) and \(\Gamma\)-component of type \(-\tau_A\).
Thus (1) restricts to an isomorphism \(\ker\tau_\Gamma\cong\ker\tau_A\).

## The separating finite quotients

The author editions used here are [BBPV15, arXiv v1, §3, pp. 5–7, (1)–(2)](../literature/pdf/BBPV15--arxiv-v1.pdf#page=5) and [PV11, arXiv v1, §2, pp. 3–6, (2)–(3)](../literature/pdf/PV11--arxiv-v1.pdf#page=3).
In BBPV15 the seven-generator group \(A\) is called \(G\), and the authors explicitly state faithfulness of (2) for that group on p. 6.
Its diagonal blocks are \(3\times3\) identities, all lower blocks are zero, and the upper blocks have entries in \(\mathbb F_2\).
In PV11 the same seven-generator group is called \(\Gamma\).
Their \(G=\langle x_0,x_1\rangle\) is its index-two subgroup by Proposition 2.1, and the displayed \(9\times9\) matrices and ensuing Toeplitz calculations on pp. 5–6 focus on its generators \(x_0,x_1\).
The whole-group assertion used here is explicitly given in BBPV15, which also gives the third generator matrix \(x_2\) on p. 7.
Faithfulness is an accepted external input at those passages.

Truncating at the first \(m\) block rows and columns is a homomorphism, since for an upper triangular product the \((i,j)\)-block sums only over \(i\le k\le j\).
The image lies in the group of upper unitriangular \(3m\times3m\) matrices over \(\mathbb F_2\).
This finite group has order \(2^{3m(3m-1)/2}\), so every image is a finite \(2\)-group.
Any nonidentity matrix has a nonzero entry above the diagonal, and sufficiently large truncations retain it.
The kernels therefore decrease to the identity.
Restricting along (1) yields the separating quotients of \(\ker\tau_\Gamma\).
Every generator \(v^{-1}w\) of a ratio group in C106v2 belongs to that kernel.
Quotients normal in the full group \(\Gamma\) can also be used: intersect each truncation kernel in \(\ker\tau_\Gamma\) with its three conjugates over the quotient \(C_3\), counting the identity conjugate once.
The resulting quotient of \(\ker\tau_\Gamma\) embeds in a product of three finite \(2\)-groups, and the resulting quotient of \(\Gamma\) is an extension of \(C_3\) by that finite \(2\)-group.

The group \(\Gamma\) itself has only cyclic finite \(2\)-group quotients.
Indeed its two-generator presentation gives abelian relations \(5a-2b=0\) and \(a+8b=0\), hence cyclic abelianization of order \(42\).
If \(Q\) is a finite \(2\)-group quotient of \(\Gamma\), the vector space \(Q/(Q^2[Q,Q])\) has dimension at most one.
Any lifts of its generators generate \(Q\), since a proper subgroup lies in a maximal subgroup of index two which contains \(Q^2[Q,Q]\).
Thus \(Q\) is cyclic, of order dividing \(2\).
In particular a separating chain for the full group requires retaining information beyond its \(2\)-group quotients.

---
author: Yin
---
# Exterior cyclic covers of the Nielsen–Soelberg eight-by-eight pair

The [NS24 author manuscript](../audits/literature/NS24/readme.md#author-manuscript), §4, p. 8, equations (4.1)–(4.2), gives two eight-element sets \(A=\{a_i\}\), \(B=\{b_j\}\) with no uniquely represented product in a torsion-free group \(G_3\).
Both sets admit exterior covers by exactly four cosets of the same infinite cyclic subgroup, with unequal Laurent widths.
Here “exactly four” counts the occupied cosets of the specified subgroup.
The group has finite abelianization, and the product table and the individual difference tables have actual double-coset collisions.

## The two covers

Use the source's generators \(x=a_2,\ y=b_5\) and its presentation
\[
      G_3=\langle x,y\mid (yx)^2(xy)^2=(xy^{-1})^2(xy)^2=1\rangle .
\]
Writing \(t=(xy)^2\) gives \(x^{-1}t x=(yx)^2=t^{-1}\).
Put \(w=yxy=t^{-1}x^{-1}\); then \(w^2=x^{-2}\).
The abelianized relations are \(4[x]+4[y]=4[x]=0\), so \(G_{3,\mathrm{ab}}\cong C_4\oplus C_4\) with the indicated generators.
In particular \(x\ne1\), and torsion-freeness implies \(x,w\) have infinite order.
Let \(H=\langle w\rangle\).

Solving the product relations (4.1) for the named vertices gives
\[
\begin{aligned}
(a_1,\ldots,a_8)
 &= (1,x,x^{-1},t^{-1},xy^{-1},x^{-1}y,t^{-1}y^{-1},t^{-1}y),\\
(b_1,\ldots,b_8)
 &= (1,x^{-1},x^{-2},xy,y,y^{-1}x^{-2},x^{-1}y^{-1}x^{-2},w).
\end{aligned}
\]
For instance \(b_2=x^{-1}, b_3=x^{-2}, a_3=b_3b_2^{-1}=x^{-1}\), and \(b_4=xy,\ a_5=xy^{-1},\ b_8=a_5^{-1}x b_4=yxy,\ a_4=b_8b_2^{-1}=t^{-1}\).
The relations \(xb_6=a_5b_3,\ xb_7=b_6,\ a_6b_6=a_3b_3,\ a_7y=a_4,\ a_8b_2=a_5\) give the remaining words, using \(xy^{-1}x=t^{-1}y\).

The following table lists the **nonempty** parts of \(A\) in right \(H\)-cosets and of \(B\) in left \(H\)-cosets.
The exponents in each row correspond in order to the displayed indices.

| Right coset for \(A\) | Indices \(i\) | Exponents in \(a_i=w^n r\) | Left coset for \(B\) | Indices \(j\) | Exponents in \(b_j=s w^n\) |
| --- | --- | --- | --- | --- | --- |
| \(H\) | \(1\) | \(0\) | \(H\) | \(1,8,3\) | \(0,1,2\) |
| \(Hx\) | \(2,4,3\) | \(0,1,2\) | \(x^{-1}H\) | \(2\) | \(0\) |
| \(Hxy^{-1}\) | \(5,7\) | \(0,1\) | \(xyH\) | \(4,6\) | \(0,1\) |
| \(Hx^{-1}y\) | \(6,8\) | \(0,-1\) | \(yH\) | \(5,7\) | \(0,1\) |

On the first side \(wa_2=t^{-1}=a_4,\ w^2a_2=a_3,\ wa_5=a_7\), and \(w^{-1}a_6=x t x^{-1}y=a_8\).
On the second side \(b_4^{-1}b_6=b_5^{-1}b_7=w^{-1}x^{-2}=w\).
Distinct exponents in each row give distinct group elements.
The character \(\ell:G_3\to C_4\) given by \(\ell(x)=-2,\ \ell(y)=1\) kills \(w\).
It takes the four row representatives in order to \(0,2,1,3\) and the four column representatives to \(0,2,3,1\), proving distinctness of all four cosets on each side.
Every homomorphism \(G_3\to\mathbb Z\) vanishes.

## Double cosets in the product and in the rank test

For a product cell \(Hr\,sH\), the residue \(\ell(r)+\ell(s)\) is constant throughout the double coset.
For each residue there is just one column per row, so every mixed double coset has at most four cells.
One containing the row and column of maximum width has all four.
In fact the following four cells belong to one mixed double coset:
\[
       (H,x^{-1}H),\quad (Hx,H),\quad (Hxy^{-1},yH),\quad
       (Hx^{-1}y,xyH).
\]
The equal products \((1,2)\sim(2,3)\), \((2,1)\sim(5,5)\), and \((3,3)\sim(6,6)\) from (4.1) join respectively the first and second, second and third, and second and fourth cells.
They exhaust residue \(2\).
The [Laurent endpoint test](Yin_L_A0037_v1.md#four-cells-with-equal-widths) for at most four cells depends on equal widths within each side.
Here the widths are \(0,2,1,1\) and \(2,0,1,1\).
The [coefficient obstruction on the actual fibers](Yin_L_A0041_v1.md) supplies the different conclusion that these exact supports cannot support a complex zero product.

For the [four-coset rank bound](../claims/Yin_C_A0023_v1.md#statement), apply the right-coset convention to \(A\), or to \(B^{-1}\) when testing the adjoint on the second side.
Both lists of representatives begin \(1,x\).
Because \(x^{-2}=w^2\in H\), one has \(Hx^{-1}H=HxH\), so the two off-diagonal ordered differences from these representatives already coincide as double cosets.

The corresponding conjugates \(H_i=r_i^{-1}Hr_i\) also fail the common-intersection hypothesis.
For both lists the first two conjugates contain \(\langle x^2\rangle=\langle w^2\rangle\).
All other pairs have trivial intersection, as can be checked in the following explicit quotient.
Let the integer Heisenberg group have multiplication
\[
 (p,q,c)(p',q',c')=(p+p',q+q',c+c'+p q')
\]
and let sign pairs \((i,j)\in\{\pm1\}^2\) act by \((p,q,c)\mapsto(ip,jq,ijc)\).
In the semidirect product with these sign pairs send \(x\) to \((1,0,0;1,-1)\) and \(y\) to \((0,1,0;-1,1)\).
The image of \((xy)^2\) is the central Heisenberg translation \((0,0,-1)\), and those of \((yx)^2\) and \((xy^{-1})^2\) are both \((0,0,1)\), so the map respects the presentation.
The image of \(w\) is \((-1,0,1;1,-1)\).
Direct multiplication gives the following translations for \(r_i^{-1}w^2r_i\) in the order of the table.

| Representatives \(r_i\) | Heisenberg coordinates in order |
| --- | --- |
| \(1,x,xy^{-1},x^{-1}y\) for \(A\) | \((-2,0,0),(-2,0,0),(2,0,-2),(2,0,2)\) |
| \(1,x,(xy)^{-1},y^{-1}\) for \(B^{-1}\) | \((-2,0,0),(-2,0,0),(2,0,2),(2,0,-2)\) |

The plane of translations \((p,0,c)\) is abelian, and entries on distinct lines in this plane have no common nonzero powers.
Since each displayed translation has infinite order, the quotient is injective on each of the cyclic subgroups being tested.
An element common to two conjugates would give equal even powers after squaring; the nonparallel lines rule this out for every pair except the first two.
For those two, the images of \(w\) and \(x^{-1}wx\) are \((-1,0,1;1,-1)\) and \((-1,0,-1;1,-1)\).
Their squares agree, while the third coordinates of all odd powers on the two sides are \(1\) and \(-1\), respectively.
Thus the first two conjugates intersect exactly in \(\langle w^2\rangle\) in the original group as well.

This pair exhibits the unequal-width, repeated-double-coset geometry of the current search inside a group with finite abelianization.
Its remaining scalar coefficient equations concern the specified \(8\)-by-\(8\) table; other product tables require their own analysis.

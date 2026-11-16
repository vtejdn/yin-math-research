---
author: Yin
---
# Four coefficient equations in the Nielsen–Soelberg eight-by-eight table

Pace P. Nielsen and Lindsay Soelberg constructed two eight-element sets with no uniquely represented product in their torsion-free group \(G_3\).
They also report that these sets cannot support a zero product over a domain and credit the verification to Soelberg's thesis.
The four fibers below give a short proof over the complex numbers, with the same calculation working in every commutative domain.
It exhibits the exceptional phase \(-1\) of the [pinned-pair test](../claims/Yin_C_A0026_v1.md#the-arithmetic-contribution-of-a-pinned-pair) in the authors' actual table.

## The actual fibers

Use the row generators \(a_i\) and column generators \(b_j\) of Nielsen and Soelberg's presentation (4.2), with \(a_1=b_1=1\), and write \(ij\) for the cell representing \(a_ib_j\).
Their [author manuscript, §4, p. 8](../literature/pdf/NS24--author.pdf#page=8), states that the complete \(G_3\) product table is equivalent under separate row and column permutations to the Section 3 table, with two three-element fibers and all other fibers of size two.
We use this multiplicity statement and the displayed relations (4.1).
The source's computation of the full table and proof of torsion-freeness are accepted inputs.

Three of the actual two-element fibers are
\[
              \{15,34\},\qquad \{62,71\},\qquad \{65,74\}.                 \tag{1}
\]
A finite group image certifying the three upper bounds on multiplicity is given below.
The no-unique-product property then gives equality in each case.

One of the three-element fibers is
\[
                           \{12,23,31\}.                                  \tag{2}
\]
Indeed, putting \(x=a_2\), the equalities \(11=22\), \(12=23\) and \(13=32\) in (4.1) yield \(b_2=x^{-1}\), \(b_3=x^{-2}\), and \(a_3=b_3b_2^{-1}=x^{-1}\).
Thus the three representatives in (2) all equal \(x^{-1}\), and the authors' upper bound of three makes (2) the whole fiber.

## The forced sign

Assign nonzero complex numbers \(u_i\) to all eight rows and \(v_j\) to all eight columns.
For a zero product, (1) would require
\[
             u_1v_5=-u_3v_4,\qquad
             u_6v_2=-u_7v_1,\qquad
             u_6v_5=-u_7v_4.
\]
Multiplying the ratios from the first two equalities by the inverse ratio from the third gives
\[
 \frac{u_1v_2}{u_3v_1}
   =\frac{u_1v_5}{u_3v_4}\,
     \frac{u_6v_2}{u_7v_1}\,
     \frac{u_7v_4}{u_6v_5}
   =-1 .                                                               \tag{3}
\]
In (2), the terms at \(12\) and \(31\) therefore cancel each other.
The complete coefficient at \(x^{-1}\) is \(u_2 v_3\ne0\).
For a commutative coefficient domain the same calculation takes place in its fraction field, including in characteristic two.
Equation (3) uses three paired fibers to determine the ratio on a single pair inside the triple.

## Certification of the three double fibers

Use a homomorphism from \(G_3\) into \(S_3\times S_3\times C_4\).
Realize each \(S_3\) as the affine maps \(z\mapsto u+e z\) of \(\mathbb Z/3\), where \(e=\pm1\).
Write an element as \((u,e,v,f,t)\), with \(t\in\mathbb Z/4\).
Its product with \((u',e',v',f',t')\) is
\[
             (u+e u',\,ee',\,v+f v',\,ff',\,t+t').
\]
In the following finite image put \(x=(1,1,0,-1,0)\), \(y=(0,-1,1,1,1)\), \(X=x^{-1}\) and \(Y=y^{-1}\).
Assign to the sixteen generators in (4.2) the following words evaluated in this group, in the original order:
\[
\begin{aligned}
(a_1,\dots,a_8)&\longmapsto(1,x,X,yxyx,xY,Xy,yxyxY,xYx),\\
(b_1,\dots,b_8)&\longmapsto(1,X,XX,xy,y,YXX,XYXX,yxy).
\end{aligned}
\]
The [finite calculation](../computations/programs/Yin_J_A0002/verify.py) verifies \(a_1=b_1=1\) and all fourteen relations \(a_i b_j=a_k b_\ell\) in (4.1), so these assignments define a homomorphism on the presented group.
Its enumeration of the \(64\) cells gives the following exact fibers in the image.

| Image element | All cells mapping to that element |
| --- | --- |
| \((0,-1,1,1,1)\) | \(15,34\) |
| \((0,-1,2,1,1)\) | \(62,71\) |
| \((2,1,1,-1,2)\) | \(65,74\) |

Equality of products in \(G_3\) implies equality of their image elements.
Thus no additional cell of the original table can occur in any of these three fibers, as required for (1).
The [reproduction instructions](../computations/programs/Yin_J_A0002/readme.md) give the program and its scope.

For [A0001](../tasks/Yin_T_A0001_v1.md#contract), this is a concrete overlapping table where the absence of any uniquely represented product still leaves a direct contradiction among its complex coefficients.
The [cyclic-cover calculation for these supports](Yin_L_A0042_v1.md) addresses their placement in the four-coset problem.
The coefficient contradiction concerns the displayed supports and uses no general domain or rank theorem for \(G_3\).

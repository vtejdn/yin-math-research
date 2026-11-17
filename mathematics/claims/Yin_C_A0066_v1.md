---
author: Yin
---

# Mixed commutators of translated graph relations in equal-label pairings

## Statement

Let \(A,B\) be finite connected rooted graphs immersed in a rose \(R\), let \(X\) be the complex obtained by coning both graphs to \(R\), and suppose \(X\) is aspherical.
Write \(F=\pi_1R\), \(G=\pi_1X\), and let \(\eta:G\to Q\) be a given finite quotient.
For the task of pairing equal forward labels on \(A\), use the binary vector spaces
\[
 U=\bigoplus_{q\in Q\setminus\{1\}} H_1(A;\mathbb F_2)_q,\qquad
 V=\bigoplus_{q\in Q}H_1(B;\mathbb F_2)_q .
\]
An explicit equality certificate on an \(A\)-path has a mixed tensor in \(U\otimes V\) whenever it has the balanced form defined below.
This includes arbitrary products of commutators of translated relations from either side, with no restriction on their conjugators.
Common readable steps preserve the tensor, its sum around every cycle is zero, and its total agrees for every two such matchings saturating exactly the same vertices.
The tensor is computable from the supplied free words, graph loops and quotient.
A nonzero difference always has a scalar witness in the dihedral group of order eight.
This uses both translated relator families in a single commutator. [One-family central signatures](Yin_C_A0063_v1.md#evaluating-an-equality-certificate)

Fix \(0<\delta<1\).
In the [four-line fourteen-color law](Yin_C_A0054_v1.md#a-planted-binary-coordinate-which-does-not-certify-any-of-the-six-colors), one may take a sufficiently small fixed positive logarithmic girth constant so that the following also holds with probability tending to one.
In each fine bin over left color \(3\), for \(k=\lfloor n^{\delta/128}\rfloor\), there are \(k\) independent classes \(u_i\) on \(A\) and \(k\) independent classes \(v_j\) on \(B\), all in their respective coarse \(Q=C_7\) summands of index \(3\).
For every \(1\le i,j\le k\) there are at least \(\lfloor n^{1-\delta}\rfloor\) distinct equal-label pairs with mixed tensor \(u_i\otimes v_j\).
The witnessing open paths can be chosen vertex-disjoint across all the pairs and indices in the bin.
In particular one can select \(2k\) vertices for which every balanced-form saturation uses at least \(k\) independent first-layer directions from each translated relator family.
These tuples retain the source types, root separation, torsion-free cone group and nonzero factors of zero product over \(\mathbb F_2\), and can have no order-21 quotient over the given \(C_7\).
The subset comparison gives no full pairing of that color.

There are also explicit graphs of arbitrary girth with a free cone group and separated roots in which the entire left color \(3\) pairs with nonzero mixed total.
An extra arc forces two conflicting complete pairings while preserving all the group labels of that color and the free group itself.
The second cone complex loses asphericity.
These small graph families have different vertex types from the four-line law.

## The finite tensor calculation

Let \(N=\ker(F\to G)\).
The lifted rose is a connected graph with \(\pi_1=N\).
The universal cover of \(X\) is contractible and is obtained from this graph by attaching one cone over each translated copy of each graph.
Its relative sequence gives an isomorphism from the direct sum of both families' \(H_1\)'s, indexed by \(G\), to \(H_1(N;\mathbb F_2)\). [Relative cone calculation](Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials)
In particular each based conjugate \(z=fLf^{-1}\) of a root loop \(L\) on either graph has first-layer class \([L]\) in its copy at \(\pi(f)\), where \(\pi:F\to G\).
The conjugating path goes to that deck vertex and retraces its steps.
Combine indices via \(\eta\) and discard the \(A\)-summand over the identity.
The resulting homomorphism \(N\to U\oplus V\) sends each \(z\) to an explicitly computable pair \((a_z,b_z)\), of which at least one entry is zero.
A walk originally based at another vertex of its graph is first conjugated by a root path to base it at the root, with the inverse root path inserted on the right of its original conjugator.

Use the finite two-group
\[
 P=U\times V\times (U\otimes V),\qquad
 (a,b,c)(a',b',c')=(a+a',b+b',c+c'+a\otimes b').
\]
Bilinearity gives associativity, and the last coordinate is a central elementary abelian subgroup.
Since \(N\) is a free group, lifting the images of its free generators gives a homomorphism \(\rho_0:N\to P\) inducing the prescribed \(U,V\) coordinates.
On root loops in the fixed copy of \(A\) it has only a central value, which is a linear function of their binary homology.
Use the displayed direct sum at the **actual** deck indices to extend that linear function by zero on the other summands.
Multiplying \(\rho_0\) by this central correction yields a homomorphism \(\rho\) trivial on the fixed \(A\)-loop group and with the same first two coordinates.
It need not extend to \(F\) or give a two-group quotient of \(G\).

Choose a root word \(p_x\) in \(A\) to each vertex \(x\).
For \(g_x=g_y\) in \(G\), the value \(\rho(p_y p_x^{-1})\) is independent of these choices since changing either word multiplies it on the left by a fixed-root \(A\)-loop.
If a path \(x\to y\) reads \(W\), its based word \(p_x W p_x^{-1}\) has this same image since \(p_x Wp_y^{-1}\) is a fixed-root \(A\)-loop.
In a *balanced certificate*, this based word is written in \(F\) as
\[
 z_{i_1}^{\epsilon_1}\cdots z_{i_h}^{\epsilon_h},\qquad
 \epsilon_\ell\in\{1,-1\},\qquad z_j=f_j L_j f_j^{-1}.
\]
Each named \(z_j\) denotes one fixed conjugate of a specified graph root loop and occurs an even number of times, counting both signs.
The free-word identity is part of the certificate.
Different conjugators with the same quotient index need not give the same \(z_j\).
An overall conjugation of a balanced word conjugates each of its named blocks and preserves this form.

Write \(a_\ell=a_{z_{i_\ell}}\), \(b_\ell=b_{z_{i_\ell}}\).
Every \(\rho(z_j)\) has order dividing two by the multiplication law and \(a_{z_j}\otimes b_{z_j}=0\).
In multiplying the images, its unknown last coordinate therefore cancels across all its occurrences, and its first coordinates cancel too.
Consequently the based word has image \((0,0,T)\) where
\[
                     T=\sum_{\ell<m} a_\ell\otimes b_m .                 \tag{1}
\]
In particular \([z,z']=zz'z^{-1}(z')^{-1}\) gives \(a_z\otimes b_{z'}+a_{z'}\otimes b_z\).
Group elements killed by the original cone presentation can be proved equal by many other words for which the balanced hypothesis does not hold.
Formula (1) makes no assignment to such a certificate solely from the first coordinates of its factors.

After the same readable right step \(t\) at both endpoints one may use \(p_xt,p_yt\) as their root paths, leaving the displacement unchanged.
Around any cycle the displacements telescope in reverse traversal order in \(N\).
The central elementary abelian images therefore sum to zero in \(U\otimes V\), and the even-degree symmetric difference of two saturations gives equality of their totals.
For linear forms \(\lambda:U\to\mathbb F_2,\ \mu:V\to\mathbb F_2\), taking coordinates \((\lambda(a),\mu(b),(\lambda\otimes\mu)(c))\) gives the same multiplication in the upper unitriangular group of order eight.
It is dihedral since the two off-diagonal elementary generators are involutions whose product has order four.
If a tensor difference is nonzero, some pair of coordinate functionals in any bases detects it.
Finally the rank of the tensor as a map \(U^*\to V\) is at most the dimension of the span of the \(b_\ell\) in any expression (1), and likewise at most the dimension of the span of the \(a_\ell\) by transposing.
Both bounds persist after summing over a matching using all of its factor directions.

## A grid of actual commutators in a four-line tuple

Work first in the unconditioned fourteen-color law and use the neutral ordinary letters with ordinary inverse from the [fresh-stub estimates](Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts).
All their matching blocks stay within a single fine color, and blocks on distinct sides or in different fine colors on the same side are independent.
Set \(a=\delta/32,\ b=a/2,\ R=\lceil a\log n/\log 64\rceil\).
In fine color \((0,0)\) on **each** side perform the [disjoint simple-cycle search](Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts) with these parameters.
Its proof uses \(0<a<1/8,\ b=a/2\), so the \(O(n^{1-b})\) exposure budget gives per-trial success \(\Omega(n^{2a-1})\) in \(\lfloor n^{1-b-a}\rfloor\) trials.
The failure probability to find \(k=\lfloor n^{a/4}\rfloor\) vertex-disjoint simple neutral cycles of length at most \(2R+2\) is \(\exp(-\Omega(n^{a-b}))\) on either side.
Write \(U_i,V_j\) for the words read on these respective oriented based cycles.
Their binary cycle classes are independent within each side since each simple cycle contains an edge absent from all the others.

For each \((i,j)\) choose a signed usable letter \(s\) outside the inverse pairs of the first and last letters of \(U_i,V_j\).
Such a letter exists since every vertex carries at least 120 usable stubs.
The word
\[
                    W_{ij}=[sU_i s^{-1},V_j]
\]
is freely reduced, has length at most \(8R+12\), and uses only neutral letters.
Condition on the two searches in fine color \((0,0)\).
The matching blocks needed to read these words in either left fine bin \((3,e)\) remain unexposed and independent of both searches.
In such a bin split \(\lfloor n^{1-b}/(8R+13)\rfloor\) open-path trials as evenly as possible among the \(k^2\) words.
Mark all vertices reached across every trial in the bin, including failures.
As in the [open-path estimate](Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths), a fresh first-stub vertex is available and every prescribed next turn reaches a fresh vertex with the required next stub with conditional probability at least \(1/300\).
Only \(O(n^{1-b})\) vertices have been exposed, the first-stub and turn pools have positive linear size, and free reduction ensures the two stubs required at a turn are distinct.
Thus each trial succeeds with conditional probability at least \(300^{-(8R+12)}\), producing a simple open lift disjoint from the other successes.
The binomial lower comparison for each word has mean at least
\[
     n^{\,1-b-a/2-8a\log(300)/\log(64)-o(1)}> n^{\,1-\delta/2}
\]
for all sufficiently large \(n\).
The binomial lower tail and a union bound give at least \(\lfloor n^{1-\delta}\rfloor\) successes per word in both bins, except with probability at most \(2k^2\exp(-\Omega(n^{1-\delta/2}))\) in this stage.

Choose a positive girth constant \(c_0\) with \(c_0\log(28|T_{\rm src}|/p)<a/4\) and \(2c_0\log132<1\), in the source notation for its signed alphabet and ordinary incidence frequency.
The [girth switching estimate](Yin_C_A0053_v1.md#exponents-arbitrarily-close-to-one), applied to the [fourteen-color blocks](Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts), costs at most \(\exp(O(n^{3a/8}\log n))\) in conditional failure probability.
Both unconditional failure probabilities above absorb this cost since \(a-b=a/2\).
The root components contain the two full graphs with conditional probability tending to one, simultaneously with asphericity, torsion-freeness, separated roots and the characteristic-two zero product.
The [finite-target conclusion](Yin_C_A0054_v1.md#excluding-all-orders-with-prescribed-simple-composition-factors), taking \(C_2,C_3\) among the fixed simple groups, excludes every order-21 quotient over the coarse character on this same high-probability event.

Both loops defining \(W_{ij}\) vanish in the original group, hence its open lifts really do pair equal labels.
For formula (1), conjugate the commutator by the left root word to its starting vertex.
The conjugator to the first graph root loop has coarse index \(3+\eta(s)-0=3\), and that to the second graph root loop has index \(3-0=3\), since their chosen cycle base vertices have color zero.
Ordinary graph root paths to those bases make this a product of precisely the two named conjugates and their inverses.
Thus (1) has value \(u_i\otimes v_j\), with the simple-cycle classes put in the stated summands.
Choose one lift for each \(i=j\).
Their sum has rank exactly \(k\), by independence of both lists, proving the lower bound for every other balanced-form saturation of their \(2k\) endpoints.
Every displayed commutator has zero integral first-homology class in \(N\), and killing either graph's whole relator family kills each of the displayed based words.
The open-path result uses sparse subsets of a typically surviving color. [Singleton and finite-quotient scope](Yin_C_A0054_v1.md#a-planted-binary-coordinate-which-does-not-certify-any-of-the-six-colors)

## Complete color pairings with a mixed tensor

Take disjoint sets of rose letters to make positive words \(U_0=u_1\cdots u_m\), \(V_0=v_1\cdots v_m\), with all \(2m\) letters distinct and \(m\ge3\).
Use four additional private letters \(r,s,t,d\).
All \(u_i\) have color zero modulo seven.
Give \(v_1\) color one, \(v_m\) color minus one and all other \(v_i\) color zero, so every strict nonempty prefix of \(V_0\) has color one.
Set \(\eta(r)=3,\ \eta(s)=\eta(t)=1,\ \eta(d)=2\).
Let \(B\) be the single cycle \(V_0\) with root at its start.
At the root of \(A\) put a cycle \(U_0\) and a private \(r\)-edge to \(x_1\).
Put \(J=sU_0s^{-1}\), \(W=[J,V_0]\), and attach a path from \(x_1\) through \(x_2,x_3\) to \(x_4\) with successive words \(W,W,tWt^{-1}\).
Use fresh interior vertices on all arcs.
Free reduction and distinct incident stubs at the branch points give immersed graphs.
The only fundamental graph relators are \(U_0,V_0\), so eliminating \(u_m,v_m\) leaves a free group.
The cone complex is homotopy equivalent to the presentation complex with those two disks, which collapses along their respective free edges to a graph.
Indeed each coned connected graph may be replaced in the attachment by the wedge of its fundamental loops along a spanning tree, using the homotopy invariance of the mapping cone.
In particular this first cone is aspherical.
The girth of each side is \(m\).
The non-root vertices on the two original cycles have nontrivial proper-prefix labels in the resulting free group, and every label beyond the \(r\)-edge has a surviving initial \(r\) with no subsequent occurrence of that letter.
Both roots are separated on their own sides.

On a \(W\)-arc the color returns to its initial value exactly after each of the four blocks \(J,V_0,J^{-1},V_0^{-1}\), and throughout each block every intermediate vertex is one color higher.
The \(tWt^{-1}\)-arc has no interior vertex of color three.
Thus the four \(x_i\) and the three strict block boundaries in each of the first two arcs give exactly ten vertices of that color.
All ten have original label \(r\), since each completed block is a relator conjugate or its inverse.
For \(h=0,1,2\), put
\[
        M_h=[U_0]_{4+h}\otimes[V_0]_{3+h}.
\]
These are distinct nonzero independent tensors for the given graph loops.
The signature of \(W\) read from an \(x_i\) is \(M_0\), and that of \(tWt^{-1}\) read there is \(M_1\).
Pair the three corresponding strict block boundaries of the two \(W\)-arcs with one another.
For each prefix \(p\) to a strict boundary its forward path to the corresponding boundary of the next arc reads \(p^{-1}Wp\) after free reduction.
Conjugating by the original prefix \(r p\) for the first arc gives the based word \(rWr^{-1}\), hence value \(M_0\).
Pair \(x_1,x_2\) and \(x_3,x_4\) by their arcs.
The total over all five pairs is \(3M_0+M_0+M_1=M_1\).
One may instead pair \(x_2,x_3\) by the middle arc and \(x_1,x_4\) by the entire long path, whose tensor is \(M_0+M_0+M_1=M_1\), obtaining the same total.

Now add a second arc \(x_1\to x_4\) with word \(dWd^{-1}\).
Distinct initial and terminal stubs preserve immersion and the new core cycle has length greater than \(m\).
All its interior vertices have color five or six, so the same ten vertices are the entire color three.
The resulting group is unchanged because the extra relation already follows from \(U_0,V_0\).
In particular both root separations and complete erasure still hold.
For the pairing using \(x_2,x_3\) and the new arc for \(x_1,x_4\), formula (1) would give \(3M_0+M_0+M_2=M_2\).
Here \([U_0]\) remains nonzero in the enlarged graph and its summands and the \(B\)-summands retain the indicated distinct indices.
The other full pairing still gives \(M_1\), contradicting the necessary condition for asphericity.
Every specified balanced displacement in these comparisons vanishes on killing all translates of either one of \(U_0,V_0\), and every displayed commutator has zero integral abelianization in \(N\).
This compares the given witnesses.
Other certificates can expose the redundant relation directly, and an unrestricted presentation identity need not admit the indicated tensor computation from its supplied factors.

## Assessment history

### Decision mixed-tensor-pairings

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:31 |
| status | proved |
| reason | Independent review verified the two-group computation, the actual grid of commutators and the complete comparison pairings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Mixed signatures for balanced certificates, the rank bounds in the fourteen-color model and the separate comparison examples. |
| argument | [The mixed tensor](#the-finite-tensor-calculation) | Class-two lifts, probabilistic exposure, fixed graph types, and the asphericity boundary for the explicit examples. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0102_v1.md#whole-argument-finding) | Independent review of the fixed argument and its stated applicability. |

## Current assessment

[Selected decision](#decision-mixed-tensor-pairings)

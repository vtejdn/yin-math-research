---
author: Yin
---

# A one-set obstruction to erasure by opposite-side relations

## Statement

Let \(X\) be obtained by coning two connected rooted graphs \(A,B\) immersed in a rose \(R\), and let \(\eta:\pi_1(X)\twoheadrightarrow Q\) be a known finite quotient.
Use binary chains and homology.
For any even set \(Z\) of vertices in one \(Q\)-color of \(A\), there is a computable class \(o_Q(Z)\) with the following properties.

1. A nonzero \(o_Q(Z)\) forbids a perfect pairing of \(Z\) proved using opposite-side loop words, with no bound on the number of bases in \(B\), copied loops, common-step propagations, or conjugating words.
   More precisely, it forbids a system of certificates using arbitrary translates of \(B\)-relators and only the fixed \(Q\)-translate of \(A\)-relators in the sense below.
   The test takes the whole set as input and needs no proposed matching or list of witnesses.
   Pairability using \(A\)-paths with words in the normal closure of the \(B\)-loops alone also has an exact criterion in a Schreier coset set.
2. If arbitrary \(Q\)-translates of *both* sides' cycle chains are allowed, the quotient vector space in this test is exactly \(H_1(\ker\eta;\mathbb F_2)\).
   The resulting linear condition is necessary for actual erasure in \(\pi_1(X)\).
3. There are connected torsion-free realizations with the exact coarse type and letter counts of [C_A0051](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings), including its nonzero characteristic-two zero product, for which \(Q=C_7\) and \(o_Q(Z)\ne0\) for **each** full first-side color \(Z=3,5,6\).
   On the same realizations \(H_1(\ker\eta;\mathbb F_2)=0\), and there is no order-21 quotient over the given \(C_7\).
   In particular no collection of opposite-side loop certificates, even with arbitrary bases, can erase color 3 there.
   A putative certificate of its actual erasure would need a nonzero contribution from nonidentity translates of first-side relations.
4. In a second family, for any fixed integer \(k\ge1\), every perfect pairing of first-side color 3 has at least \(2k\) pairs for which **no** path in \(A\) between the two vertices has word in the normal closure of the \(B\)-relations.
   The same lower bound is \(k\) in each of colors 5 and 6.
   These are again original four-line coarse counts on torsion-free realizations with \(H_1(\ker\eta;\mathbb F_2)=0\) and no quotient of order 21 over \(C_7\).

The construction gives a certificate against the indicated ways of pairing, while typical true survival also follows from vertex-label separation estimates.
The nonregular color states used in the construction are not asserted to be group quotient labels of the full cone group.

## An absolute class for one even set

Let \(R_Q\) be the rose cover on the vertices of \(Q\), with right steps given by the letter images.
Write \(i_A:A\to R_Q\) and \(i_B:B\to R_Q\) for the graph maps sending the two roots to the identity and assigning to other vertices the images of their forward path labels.
For \(q\in Q\), left translation of \(R_Q\) induces an action on its homology.
Set
\[
 \mathcal H_A(Q)=H_1(R_Q)\Big/
     \left(i_{A*}H_1(A)+\sum_{q\in Q}q\,i_{B*}H_1(B)\right).
\]
Choose a binary edge chain \(p\) in \(A\) with boundary \(\sum_{x\in Z}x\).
It exists since \(A\) is connected and \(|Z|\) is even, for example by summing the tree paths from its root to the indicated vertices.
The pushforward \(i_Ap\) is a cycle, since all the boundary vertices have the same \(Q\)-color.
Define \(o_Q(Z)=[i_Ap]\) in \(\mathcal H_A(Q)\).
Changing \(p\) adds a cycle in the fixed \(A\)-copy, so the class is independent of the tree or chain.
Finite graph boundary matrices, the labeled matchings and the given letter images in \(Q\) determine all these spaces, the class and a dual cochain witness for its nonvanishing by binary elimination.

Suppose one pairs \(Z\) by paths in \(A\) and each path word is a product of conjugates of based \(B\)-loop words in the free rose group.
Its image in \(R_Q\) is the sum of the corresponding translated \(B\)-cycles, since inverse conjugating segments cancel as binary edge chains.
Reversing a loop preserves its parity vector.
Propagation by common steps at two equal-color endpoints adds another pair of canceling Cayley edges.
Summing the paired paths gives an \(A\)-chain with the prescribed boundary, hence \(o_Q(Z)=0\).
In this argument one may also use based \(A\)-loop terms whose projected cycle is in the fixed copy \(i_A H_1(A)\).
For example an \(A\)-loop based at \(z\), conjugated by \(u\) in a certificate read from \(x\), contributes in the fixed copy if \(\eta(g_x)\eta(u)\eta(g_z)^{-1}=1\), with \(g_x,g_z\) the forward labels.
This verifies the asserted coverage of multiple relators. [Deck indices in certificates](Yin_C_A0055_v1.md#certificates-using-several-graph-relations)

For comparison, take the actual cover \(X_Q\) determined by \(\eta\).
The relative chain complex over its rose cover is the direct sum of one relative cone complex for each side and \(Q\)-translate.
Thus the image of \(H_2(X_Q,R_Q)\to H_1(R_Q)\) is the span of **all** translates of both side cycle spaces.
Also \(H_1(X_Q,R_Q)=0\), since each attached graph is connected and \(H_1(\operatorname{cone}(Y),Y)=\widetilde H_0(Y)=0\).
Exactness identifies the corresponding full quotient with \(H_1(X_Q)=H_1(\ker\eta;\mathbb F_2)\).
Actual erasure would provide group equalities pairing \(Z\), so their certificates using the full cone presentation put \(o_Q(Z)\) in the kernel of this last projection.
Equivalently the full test is the sum of the relative abelianized labels, which can be weaker than the entire histogram in a further group quotient. [Relative homology calculation](Yin_C_A0047_v1.md#a-finite-test-for-complete-erasure-of-a-color)
These chain statements require no asphericity of \(X\).

## An exact coset criterion for the opposite-side normal closure

Let \(F=\pi_1(R)\), let \(H_A\le F\) be the subgroup read on loops at the fixed root of \(A\), and put \(G_B=F/\langle\!\langle H_B\rangle\!\rangle\) using the corresponding rooted subgroup of \(B\).
Conjugation in the normal closure already allows loops at every \(B\)-vertex.
Let \(U\le G_B\) be the image of \(H_A\) and \(w_x\) a chosen \(A\)-root word to \(x\).
Assign \(x\) the coset \(U\overline w_x\) in \(U\backslash G_B\), where the bar denotes passage to \(G_B\).
Changing the root path does not change that coset.
The set of all free rose values of paths in \(A\) from \(x\) to \(y\) is exactly \(w_x^{-1}H_A w_y\), by concatenating the two root paths with arbitrary rooted loops.
This set contains a word trivial in \(G_B\) precisely when \(U\overline w_x=U\overline w_y\).
Consequently \(Z\) admits a perfect pairing certified by such paths if and only if each coset occurs an even number of times in \(Z\).
Odd coset counts therefore obstruct even this liberal use of arbitrary products of conjugates of \(B\)-relators, which includes words of actually synchronized opposite-side walks.

The coset set need not be finite, and no general membership algorithm for \(U\) is assumed.
Any finite \(G_B\)-set with a point fixed by \(U\) receives a well-defined map from \(U\backslash G_B\) by applying the coset representative to that point on the right.
An odd bin in this finite image already rules out complete pairing by the indicated paths.
Such a finite action need not factor through the group obtained after also coning \(A\).

## Asymmetric finite color actions with the exact four-line counts

Put \(V=\mathbb F_2^2\) with basis \(e_1,e_2\).
Use the finite group \(W=V^{C_7}\rtimes C_7\) acting on the right on the 28 states \(\Omega=C_7\times V\).
It is generated by the rotation \(r:(c,s)\mapsto(c+1,s)\) and the two permutations \(l_j:(c,s)\mapsto(c,s+\mathbf1_{\{c=0\}}e_j)\).
Conjugating the two additions by rotations gives independent additions at each of the seven coordinates, proving the description and the order \(|W|=7\cdot4^7\).
The map \(W\to C_7\) is its rotational coordinate.
Give the rose letters a surjection \(\theta:F\to W\) as follows.
Use \(r,r^2,r^4\) on the three positive intersection arrows of C_A0051, \(l_1,l_2\) on two of the three mixed inverse pairs, and identity on all other pairs, taking inverses on reverse readings.
The induced coarse map is the prescribed one.

On the first graph use the transitive action on \(\Omega\), with root state \((0,0)\).
On the second graph use the regular right action on \(W\), with root state its identity.
Take \(n\) through sufficiently large multiples of \(2(16513)^2 |W|\).
On each side start with an equal allocation of every source type among its fine states.
Use \(D=\{0,1,2,4\}\) and \(f_i(c)=7\mathbf1_{\{c=i\}}-1\).
On the four selected empty-extra types, indexed by \(i\in D\), make the following changes.

* On \(A\) add \(\mathbf1_{\{c=i+1\}}\) in state \((c,e_1)\), \(\mathbf1_{\{c=i+2\}}\) in state \((c,e_2)\), and \(f_i(c)-\mathbf1_{\{c=i+1\}}-\mathbf1_{\{c=i+2\}}\) in state \((c,0)\).
* On \(B\) add \(f_i(c)\) at the single group state \(r^c\) and zero at all other group states.

Both changes preserve each full type total and give precisely \(f_i(c)\) when summed at coarse color \(c\).
Each fine count remains positive for sufficiently large \(n\).
Intersection arrows on \(A\) rotate the \(c\) coordinate without changing \(s\), and those on \(B\) rotate the subgroup \(\langle r\rangle\) while preserving its complement under right multiplication by powers of \(r\).
The intersection line indices rotate by the same shift, so the corresponding stub totals match in every fine state.
Private ordinary pairs lie on the same selected line, have identity action and have the same modifications.
The mixed pairs touch no selected ordinary line or changed extra-bearing type, so their two fine populations are uniform and the permutations \(l_j\) match them exactly.
All other exterior pairs are unchanged.
These verifications are at the level of named integer matching pools.
Independently choose uniform bijections in each prescribed block for each side and inverse pair.

Both actions project equivariantly onto the coarse \(C_7\) rotation, so every closed graph word has trivial coarse increment and the cone group admits \(\eta:G\to C_7\).
Every \(B\)-loop in fact evaluates to the identity of \(W\), since the regular action fixes its initial group state only in that case.
On \(A\) the same assertion would require regularity and need not hold.
Instead the additional fine bit vector of an \(A\)-vertex is a primitive of the following \(V\)-valued cochain on its fixed graph map into \(R_{C_7}\).
Give each of the two specified mixed edges the value \(e_j\) when its initial coarse color is zero and zero otherwise, with the same value in reverse, and give all other rose-cover edges zero.
The mixed edges have zero coarse step, so this specifies an unoriented binary cochain.
Along any word its sum is exactly the change in the bit vector of the state at the specified initial coarse color.
It annihilates cycles in the fixed \(A\)-copy by construction, and all translates of \(B\)-cycles because each such word is the identity permutation on **every** state of \(\Omega\).
It thus evaluates elements of \(\mathcal H_A(C_7)\).
It is also a finite action as in the coset criterion: \(G_B\) acts through \(W\), and the image of \(H_A\) fixes the first-side root state \((0,0)\).

With connected sides, all named vertices occur.
The initial number \(n/28\) per first-side fine state is even.
In the \(e_1\) sheet the parity mask is \(D+1=\{1,2,3,5\}\), in the \(e_2\) sheet it is \(D+2=\{2,3,4,6\}\), and the \(e_1+e_2\) sheet is everywhere even.
For the whole set of vertices of color \(c\), evaluating the cochain on \(i_Ap\) gives the sum of their bit vectors, by the boundary identity.
The answers for \(c=3,5,6\) are respectively \(e_1+e_2,e_1,e_2\), all nonzero.
Hence no perfect matching of any of those three sets can be justified by opposite-side relations alone, with arbitrary conjugates and no bound on the number of base vertices.
Even allowing fixed-copy \(A\)-cycles, each putative full erasure needs the stated total vector from translated \(A\)-terms.
This conclusion tests a specified system of relations and makes no claim that the \(A\)-vertex states are invariants of original group labels.

## Geometric safeguards and the absence of group-quotient certificates

We verify the changes to the [finite-group matching estimates](Yin_C_A0044_v1.md#girth-conditioning-and-bounded-patterns) and their [bounded-perturbation version](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts).
Let \(d_A=28,d_B=|W|\), and on side \(Y\) put \(N_Y=n(129/16513)/d_Y\).
Each block size equals \(N_Y+O(1)\), and a prescribed positive turn frequency within a state differs by \(O(1)\) vertices from its balanced count.
Absent turns stay absent as no new type was introduced.
Choose the logarithmic girth constant small enough for the short-cycle bound using the larger of \(d_A,d_B\), and for the usual radius-\(2L\) switch ball to have \(o(n)\) vertices.
The cycle-expectation and reverse-switch proof works within the two differently sized pools, giving girth-event probability at least \(\exp(-o(n))\).
Under this condition a fixed \(E_Y=O(L)\) collection of feasible distinct prescriptions on side \(Y\) costs at most \(N_Y^{-E_Y}\exp(o(L))\), using the same switch within its state block.
For sufficiently small fixed \(\epsilon>0\), the small-set expansion proof for \(j\le\epsilon n\) uses \(2/N_Y\) per prescription and yields the same summable \([C(j/n)^{62.5}]^j\) bound and diameter \(O(L)\).

For the bounded-pattern estimate, an initial state per connected component and a word determine all of its transported states for **any** permutation action, with inconsistent paths discarded.
In a source multiplicity stage the state factor relative to the uncolored count is at most
\[
       \prod_{Y=A,B} d_Y^{\,b_Y+E_Y-V_Y+k_Y}\exp(o(L)).
\]
Here \(V_Y,E_Y,b_Y,k_Y\) count vertices, edges, components and fixed initial vertices of the stage on that side.
Counting within each side is important when their actions have different sizes.
Its stage consists of boundedly many whole chains, so each displayed exponent is bounded in absolute value.
The bounded changes in positive turn counts contribute only \((1+O(1/n))^{O(L)}\).
The unchanged word constraints and stage selection therefore give the source bounded-pattern conclusion, uniformly for specified roots.
The deterministic planar and cone-picture implications give root separation, asphericity, torsion-freeness and the genuine nonzero characteristic-two zero product with probability tending to one under girth conditioning. [Ope26f, Propositions 3.1, 4.5 and 5.1 and §6](../literature/pdf/Ope26f.pdf#page=7)
The limiting macroscopic-cut entropy argument is valid on each side because each action is transitive, so a cut constant within its states and preserved by all generators is constant across that entire side.
Combined with small-set expansion this gives connectedness with probability tending to one.
Uniform rerooting yields \(o(n)\) repeated vertices in probability, as in the [four-line singleton estimate](Yin_C_A0051_v1.md#connectedness-collection-and-the-erasure-threshold).
Consequently true labels survive at every coarse color on the typical tuples selected here, independently of the obstruction to a particular mechanism of erasure.

For completeness consider a fixed finite target \(E\) and homomorphism \(\varphi:F\to E\).
If it descends to the cone group, it gives an additional marking on just side \(A\) by right multiplication in \(E\).
The independent-block multinomial bound and the strict zero-loss analysis of [C_A0044](Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient) apply on the \(28\) states, including the fixed \(O(1)\) perturbations by compactness.
At zero loss every full type and signed letter in a fixed state is monochromatic for that marking.
The shared ordinary points connect all its full types.
The marking would therefore give a function \(F_0:\Omega\to E\) with \(F_0(\omega\theta(t))=F_0(\omega)\varphi(t)\) on every letter.
Every free word fixing the base state \((0,0)\) then lies in \(\ker\varphi\), by the regular right action of \(E\).
In particular \(\varphi\) factors through \(W\) and kills the stabilizer of this state and its normal closure.
The stabilizer consists of the functions \(C_7\to V\) vanishing at zero, with no rotation.
Its conjugates by rotations together generate the whole base group of functions.
The quotient of \(W\) by that normal closure is precisely \(C_7\).
Thus on a fixed finite list of targets every descended map factors through \(\eta\) except with probability exponentially small even after the subexponential girth cost.

Take the list consisting of the groups of order 21, \(C_{14}\), and \(\operatorname{AGL}(1,8)\).
This excludes a surjection over \(C_7\) to any group of order 21.
If \(H_1(\ker\eta;\mathbb F_2)\ne0\), its finite-dimensional \(C_7\)-module has a simple quotient of dimension one or three, by the factorization of \(X^7-1\) over \(\mathbb F_2\).
In the corresponding group extension by that elementary abelian quotient the eighth power of a generator lift has order seven and still maps to the chosen generator.
The extension therefore splits and gives a surjection to \(C_{14}\) or \(\operatorname{AGL}(1,8)\), impossible on the same event. [Relative binary module test](Yin_C_A0047_v1.md#why-every-relative-two-group-refinement-can-disappear)
Intersecting with the preceding geometry and connectivity events proves all the existence assertions.
The surviving cochain on the fixed \(A\)-copy and all \(B\)-copies consequently distinguishes the single sets here even though allowing all \(A\)-translates kills the entire degree-one homology test.

## Arbitrarily many pairs outside the opposite-side normal closure

In any finite \(G_B\)-set as in the coset criterion, let \(h\) be the number of states that receive an odd number of vertices of \(Z\).
Any perfect matching of the vertices of \(Z\) contains at least \(h/2\) pairs with different states at their endpoints.
Indeed pairs lying within one state leave its parity unchanged, and every different-state pair is incident to at most two odd states.
Such a different-state pair cannot be joined by *any* \(A\)-path with word trivial in \(G_B\).

For fixed \(k\ge1\), put \(m=4k+1\) and use \(W_m=(C_m)^{C_7}\rtimes C_7\) acting on \(\Omega_m=C_7\times C_m\) by rotations and coordinate additions.
Assign the three active arrows to the same powers of the rotation as before, one mixed pair to a generator of \(C_m\) acting only at coarse zero, and all remaining pairs to the identity.
These letters generate \(W_m\).
Use \(\Omega_m\) on \(A\), the regular \(W_m\)-set on \(B\), and sizes divisible by \(2(16513)^2|W_m|\).
In particular the unperturbed \(A\)-population per fine state is even.
Partition the nonzero internal states into two sets \(J_1,J_2\) of size \(2k\) each.
On the empty-extra type of selected line \(i\), put change \(\mathbf1_{\{c=i+1\}}\) at each state \((c,s)\) with \(s\in J_1\) and \(\mathbf1_{\{c=i+2\}}\) at each state with \(s\in J_2\).
At state \((c,0)\) put the remaining \(f_i(c)-2k\mathbf1_{\{c=i+1\}}-2k\mathbf1_{\{c=i+2\}}\).
On \(B\) use the previous changes supported on \(\langle r\rangle\), with \(r\) now the rotation in \(W_m\).
The coarse counts, stub equalities and positivity for sufficiently large \(n\) follow as before, since within each internal state the line changes are translates and the one mixed pair is untouched.

At \(c=3\) both \(D+1\) and \(D+2\) contain \(c\), so all \(4k\) nonzero internal states in this color are odd.
At \(c=5\) precisely those in \(J_1\) are odd, and at \(c=6\) precisely those in \(J_2\).
The zero state in each of the three colors has even count by the even coarse total.
Since all \(B\)-loops act as the identity on \(\Omega_m\), the bound \(h/2\) proves item 4.
It applies to *any* proposed pairing of the set, irrespective of whether its other pairs are actual equalities in \(G\).

For fixed \(k\) both action sizes are constants and the perturbations are bounded independently of \(n\).
Thus the preceding side-specific switching, bounded-pattern and connectivity proof applies with \(d_A=7m,\ d_B=7m^7\).
The stabilizer in \(W_m\) again consists of functions vanishing at the initial coordinate, and its conjugates generate all of the base group.
The finite-target argument on \(A\) therefore again excludes the same list of nonfactoring quotients, proving the stated homology and order-21 properties.
One can choose one sufficiently large safeguarded realization for each \(k\), with increasing \(n\), so the minimum required number of pairs outside the opposite-side normal closure diverges along that diagonal sequence.
The girth constant, size threshold and other estimates may depend on \(k\).
No claim of a uniform positive fraction of pairs, or of a complete erasing pairing in \(G\), follows from this choice.

## Assessment history

### Decision opposite-side-erasure-obstruction

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:53 |
| status | proved |
| reason | Independent review verified the one-set homology class, the exact coset criterion, the asymmetric matching construction and the required number of pairs outside the opposite-side normal closure. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Opposite-side erasure certificates, full relative homology and the stated torsion-free realizations at the exact four-line counts. |
| argument | [Proof](#an-absolute-class-for-one-even-set) | The chain and coset tests, finite actions, matching safeguards, exclusions of the listed quotients and the bounds for each fixed \(k\). |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0096_v1.md#whole-argument-finding) | Independent review of all four assertions, including the limits on what the tests decide about original-group erasure. |

## Current assessment

[Selected decision](#decision-opposite-side-erasure-obstruction)

---
author: Yin
---
# Lifting a characteristic-two zero product at a fixed residue point

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) | Seek a scalar counterexample over the complex numbers by lifting a fixed finite zero product in an actual torsion-free group. |

## Route

| Field | Value |
| --- | --- |
| parent | [Relations-compatible analytic and algebraic ranks](Yin_S_A0004.md#current-structural-investigation) |
| disposition | active |
| priority | Test many-basepoint pairings of left color 3 using alternate fillings and protected vertices in four-line tuples without an odd-bin certificate. |

## Input and distinction from rank sampling

The [Ope26f construction](../ledger/Yin_L_A0034_v1.md#scope-for-the-group-ring-product) supplies a scalar zero product in characteristic two in a torsion-free group, at the scope of the authors' theorem.
An exact lift over a number field would already give a scalar kernel of trace strictly between zero and one.
No hypothesis on the value \(1/2\), on amenability, or on the number of occupied cyclic cosets is needed for this implication.
The [local lifting equations](../claims/Yin_C_A0038_v1.md#the-incidence-matrix-and-lifting) test successive powers of the same prime.
The [local saturation test](../claims/Yin_C_A0039_v1.md#horizontal-specialization) allows arbitrary ramification and tests the specified residue point.

## Which equations can discriminate

First distinguish a necessary coarse equation from a sufficient refinement.
Under a verified group homomorphism every fiber for the images of the group products is a union of actual fibers.
Thus a contradiction among these coarse equations obstructs the corresponding lift in the original group.
For the first mod-four test one can work with repeated occurrences before collecting equal source labels.
An odd multiplicity can be assigned the desired lifted coefficient and cancelling pairs of \(1,-1\); for even multiplicity use only such pairs.
This shows why an inconsistency after quotienting and allowing all occurrence coefficients would also give an obstruction on the actual odd-multiplicity supports.
By contrast, different components of the simultaneous-step graph can map to the same actual group element, so failure after imposing one equation per component alone has no such implication.
Satisfaction of all the refined equations with the distinguished root coefficients nonzero can yield a zero product; check the two actual collected factors and the coefficient field at every application.

Seek a union of entire actual or quotient fibers with even incidence at every vertex and cell count \(2\bmod4\).
Such a union excludes every unramified lift of the marked point at the first step.
The [finite quotient test](../ledger/Yin_L_A0045_v1.md) rules out using any quotient of order at most four to detect this obstruction.
It also rules out detecting a mod-four obstruction after projection to an odd-order quotient when the input vertices of each side occupy every projected label.
For a verified sparse quotient, retain all occupied images and their occurrence counts.
In \(C_7\) three complete fibers already obstruct every characteristic-zero solution for the indicated sparse supports, while additional occupied labels can enlarge those same fibers.
The [ramified example](../claims/Yin_C_A0039_v1.md#a-group-table-that-requires-ramification-at-the-marked-point) shows why this would still leave the characteristic-zero question open.
For the next decision seek an identity \(2^j f\in I\) with \(f\) nonzero at the marked point, or exhibit a component in characteristic zero specializing to it.
Either certificate requires verified group-product equations at the scope used.
The published type counts and the [type-level calculation](../claims/Yin_C_A0038_v1.md#statement) do not determine the complete table of a particular choice of matchings.
The rank sampling and moment tests in the parent route remain available for questions about the ranks of an actual complex solution.

## Which cyclic quotients of the matching construction remain

The [finite-target entropy calculation](../claims/Yin_C_A0041_v1.md#statement) shows that the original random matching law admits a nontrivial map to any fixed finite target with exponentially small probability.
Both sides are [typically connected and almost all their vertex labels are distinct](../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots).
Alternatively, [independently matching seven equal color classes](../ledger/Yin_L_A0047_v1.md) gives genuine torsion-free realizations with a cyclic quotient of order seven.
Every quotient class then has exactly \(n/7\) vertex occurrences per side and an even positive number of collected group labels.
The projected equations lift by integer signs.
The [finite-target version](../claims/Yin_C_A0044_v1.md#statement) can arrange this compatibility simultaneously for every target in a preassigned finite list.

For any connected realization, the two collected supports have even cardinality.
The [cyclic lifting classification](../claims/Yin_C_A0042_v1.md#statement) proves that mod four always lifts here and that mod eight detects every obstruction to an exact lift at the marked point, even after allowing arbitrary finite ramification.
Only the two opposite four-class odd masks, each without any other occupied class, can fail.
Their [seven complete quotient fibers](../ledger/Yin_L_A0046_v1.md#complete-fibers-with-arbitrary-positive-odd-multiplicities) provide a direct certificate.
The [neighbor and integer-height tests](../claims/Yin_C_A0043_v1.md#neighbor-constraints) exclude these masks before collecting the connected vertex lists and constrain how they could arise after collection.

For this quotient, pursue only an exceptional matching with a verified nonzero character and sufficient group-label collision data to distinguish missing classes from occupied classes of even count.
In particular, in a nearly injectively labelled connected realization the remaining obstruction requires just one nonzero pair of letter increments and full occurrence coverage on at least one side.
Without a candidate meeting these conditions, use complete original fibers or investigate a different quotient.

## When can a whole color disappear?

For one permitted inverse pairing the [four-line construction](../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) realizes both nonzero odd masks in genuine connected, torsion-free Ope26f examples.
Before collection each side has \(n/7+3\) occurrences in each of its four odd classes and \(n/7-4\) in each remaining class.
The complete quotient fibers on vertex pairs have sizes \(n^2/7+84\) over zero and \(n^2/7-14\) over every other residue.
Typically all seven colors survive collection.
To force just the four odd classes on each side in this family, at least \(3n/7-12\) vertices per side must carry repeated labels.
The [resulting mergers of product fibers](../ledger/Yin_L_A0051_v1.md#consequences-for-a-sparse-quotient) would affect more than \(66\%\) of all pairs for large \(n\).
For proposed erased lists of sizes \(N_A,N_B\), a [fourth-moment calculation with independent vertex phases](../ledger/Yin_L_A0051_v1.md#a-fourth-moment-for-repetitions-on-both-sides) also yields an exclusion when the measured fourth-moment excess is below \(2N_A N_B\) in a verified quotient.

On a proposed matching, verify the character on fundamental loops and count the vertices in each color before collection.
For other prescribed inverse pairings the [binary type equations](../ledger/Yin_L_A0048_v1.md) always allow both odd masks for some increments.
For fixed increments the [integral feasibility test](../ledger/Yin_L_A0049_v1.md#correcting-a-lift-modulo-256) determines which parities can be realized by integer counts after a permitted even balanced enlargement.
When the desired four colors have odd counts, a further occupied color disappears exactly when its vertices can be paired by equal group labels.
The [pairing test](../claims/Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices) propagates those equalities along common edges and rejects pairings that identify a protected pair of vertices.
A connected example with arbitrary girth realizes all three erasures on each side, but its vertex types differ from the source and its two root factors have nonzero product.
For a proposed source-type matching, an [odd bin in the mod-two homology of the kernel](../claims/Yin_C_A0047_v1.md#a-finite-test-for-complete-erasure-of-a-color) certifies survival of a color.
A [lift of the character to a larger cyclic seven-group](../claims/Yin_C_A0048_v1.md#statement) gives another such test and bounds the required sizes of the two supports.
If these tests leave pairings, seek a word proof in the cone presentation for every paired equality, or a certified surviving group label in an outside color on either side.
Existence of a connected matching with these erasures, the prescribed source types, the geometric safeguards and the binary zero product remains open.

## Which exceptional matchings remain after testing the left color 3?

In genuine torsion-free realizations, [short cycles read as open paths on the other side](../claims/Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths) yield actual pairs inside the left color \(3\) and the other five designated colors at the same time.
For every fixed \(0<\delta<1\), a sufficiently small fixed logarithmic girth constant gives at least \(\lfloor n^{1-\delta}\rfloor\) disjoint equal-label pairs per specified bin with probability tending to one.
The number of different group elements that repeat in a coarse color must grow as well.
If \(r\) of its vertices share a label with another vertex and \(k\) distinct labels occur more than once, the [fold bound (3)](../ledger/Yin_L_A0052_v1.md#a-homological-rejection-test-under-the-source-safeguards) gives \(126(r-16513k)\le 2(r-k)\): a repeated label can use at most \(16513\) distinct ordinary lines, and the singleton labels contribute zero to both sums in (3).
Thus \(k\ge124r/(126\cdot16513-2)\).
Even with these collisions, the typical left color \(3\) still has \(n/7-o(n)\) surviving labels.

One can [force all six erasures by prescribed graph loops](../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group) while retaining connectedness, the prescribed types and logarithmic girth.
The resulting original cone group equals \(C_7\), so the construction loses torsion-freeness and root separation.
Asphericity rules out the same-line duplication method on a legitimate tuple: among the \(M/2\) proposed pairs in color \(3\), at most \(M/63\) can use vertices on the same ordinary projective line, where \(M=n/7-4\).
Once the [shortest nontrivial free relation](../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws) has length at least three, any full pairing needs at least [8193 distinct based witness words up to inversion](../ledger/Yin_L_A0052_v1.md#how-many-different-copied-words-are-needed).

In a legitimate [order-21 refinement](../ledger/Yin_L_A0053_v1.md#a-smaller-quotient-of-odd-order-even-when-the-relative-mod-two-test-is-trivial), put \(u=n/21\), an even integer.
At left color \(3\) the three fine counts are \(u-6,u+1,u+1\); no complete equal-label pairing exists there.
The same prescribed refinement supplies odd bins in the two other even colors on the left and all three on the right, and can do so with trivial relative mod-two homology.
For an arbitrary finite two-group image of the original group, [disagreement of the four odd pieces](../ledger/Yin_L_A0056_v1.md#the-six-coefficient-equations) is another necessary exclusion test for simultaneous erasure.
For a supplied pattern-free matching still passing those tests, the [bounded cone-picture algorithm](../claims/Yin_C_A0052_v1.md#enumerating-the-witnesses) decides the exact original equality partition in color \(3\) and then each remaining color.
An extension to all six now requires a legitimate tuple passing those six exact parity decisions.

## Many loops when finite quotients see even counts

The [fourteen-color construction](../claims/Yin_C_A0054_v1.md#excluding-all-orders-with-prescribed-simple-composition-factors) keeps both fine bins even over left color \(3\) and the other five target colors.
It can exclude every quotient of order \(21\) over the given character and every odd-bin test from relative finite kernels with any prescribed finite list of simple composition factors, at all orders for that list.
For each fixed \(0<\delta<1\), the same typical tuples in this exceptional family have [at least \(\lfloor n^{\delta/32}\rfloor\) independent opposite-side cycles](../claims/Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts), each giving at least \(\lfloor n^{1-\delta}\rfloor\) disjoint actual pairs per fine bin.
The paths for distinct cycles can be chosen disjoint. The occupied class still has \(n/7-o(n)\) distinct surviving labels.
For a certificate naming a particular survivor, fix a vertex of left color \(3\) before sampling and apply the [rooted separation test](../claims/Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices) to this root as well as the original roots.
The rooted bound is uniform for each fixed vertex in the perturbed law, so both separations hold simultaneously with probability tending to one.
On an individual tuple the additional rooted condition certifies that this vertex has multiplicity exactly one.

In any connected tuple with the four-line type counts, even all directly readable closed walks at any chosen 49 opposite-side base vertices, including their successive use, [leave some color-3 vertices untouched](../claims/Yin_C_A0054_v1.md#how-many-opposite-side-base-vertices-are-necessary).
For longer lists, each original equality carries an [opposite-side homology vector indexed by its translated starting label](../claims/Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials).
Alternative fillings saturating the same set must have equal vector totals. For example, retain an odd number of disjoint pairs per independent cycle in the preceding construction.
In any other pairing of those same vertices the total opposite-side edge chain must still include every retained cycle edge oddly, even after forgetting the translation indices.
For a full-color construction, test forced alternative fillings on the same vertex set and certify an original equality for each pair that remains.
The [restricted-turn result](../claims/Yin_C_A0059_v1.md#which-choices-of-letters-are-covered) gives a further exclusion on its high-probability event: distinct vertices joined by a reduced path on any 62 inverse pairs cannot be given the same group label by any cone relations.
Whether every legitimate tuple without a \(C_{21}\) certificate has an odd original label in left color \(3\) remains open.

## What happens to the original product in random matchings?

The [common-step walk and finite forest count](../ledger/Yin_L_A0050_v1.md#forest-and-return-probability) describe how pairs of vertices with the same group product are connected by shared letters.
The [two-root estimate](../claims/Yin_C_A0049_v1.md#statement) shows that in both the original and balanced cyclic matching laws, with probability tending to one, all but a vanishing fraction of pairs lie in a component that already contains their whole product fiber.
On two-vertex components that are whole fibers, cancellation of two unit terms forces [ratios along ordinary letters](../claims/Yin_C_A0046_v1.md#the-two-cycle-lattices).
With probability tending to one in either law, the [stability of the resulting cycle equations](../claims/Yin_C_A0050_v1.md#positive-density-for-the-actual-collected-supports) forces at least \(c n^2\) nonzero product coefficients simultaneously for every assignment of nonzero complex coefficients to the two exact collected supports, for a fixed \(c>0\).
The same bound excludes a lift of the marked binary point on these supports modulo four even after arbitrary finite ramification.
On each such matching the ideal of the complete product equations in the Laurent ring of unit coefficients contains \(2\).
Indeed its universal quotient has a unit zero-product solution, so the bound over every commutative ring with \(1\ne-1\) forces \(2=0\) in that quotient.
Thus the [local saturation test](../claims/Yin_C_A0039_v1.md#statement) already has an exponent-one certificate there.
In the balanced law every class of the prescribed quotient already has even occurrence count, so it cannot exhibit the four odd classes.
The [four-line law](../claims/Yin_C_A0051_v1.md#product-fibers-and-complex-coefficients-in-the-four-line-law) realizes the four odd classes on both sides and retains the positive-density bound in the original group.

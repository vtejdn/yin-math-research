---
author: Yin
---

# Mixed tensor signatures of two translated loop families

At 2026-11-17T03:23 UTC an agent outside the development of Yin_C_A0066_v1 independently reviewed its fixed statement and three proof sections for Sheng Yin.
The reviewer read the fixed input and its direct homological, matching and geometric inputs without receiving proof-development discussion, author explanations or previous findings on this claim.
The reviewer had previously inspected the one-family central test and the finite-color matching interfaces.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0066_v1.md#statement) | Aspherical cone, finite quotient, admissible balanced certificates, both-side tensor, rank obstruction, conditioned fourteen-color grid and separate small-graph examples. |
| [Whole-argument finding](#whole-argument-finding) | [Finite tensor](../../claims/Yin_C_A0066_v1.md#the-finite-tensor-calculation) | Direct sum and central correction, even multiplicities and signs, translates, propagation, matching comparison and dihedral detection. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line grid](../../claims/Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple) | Separate cycle and path exposures, conditional success and girth cost, simultaneous disjointness, index-three assignments and the rank-\(k\) consequence. |
| [Whole-argument finding](#whole-argument-finding) | [Complete pairings](../../claims/Yin_C_A0066_v1.md#complete-color-pairings-with-a-mixed-tensor) | Immersions and girths, original group and roots, all ten equal labels, the two complete totals and the effect of the extra relation on asphericity. |
| [Whole-argument finding](#whole-argument-finding) | [Relative homology](../../claims/Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials) | First homology of the lifted rose and translated cone-base boundary maps. |
| [Whole-argument finding](#whole-argument-finding) | [Repeated cycle trials](../../claims/Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts) | Fresh neutral-cycle and turn-pool estimates with bounded perturbations of fourteen-color blocks. |
| [Whole-argument finding](#whole-argument-finding) | [Open paths](../../claims/Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths) | Conditional fresh-endpoint estimates and permanent marking of all touched vertices. |
| [Whole-argument finding](#whole-argument-finding) | [Girth cost](../../claims/Yin_C_A0053_v1.md#exponents-arbitrarily-close-to-one) | Exponent of the inverse girth probability for a sufficiently small fixed logarithmic scale. |

## Whole-argument finding

The universal cover's relative boundary map identifies \(H_1(N;\mathbb F_2)\) with the actual deck-indexed direct sum of the two loop homologies.
The chosen quotient of this sum erases the \(A\)-coordinate at the identity of \(Q\), in particular on the fixed root copy of \(A\).
Lifting a free basis of \(N\) into the finite group \(P\) therefore sends the fixed \(A\)-loops into its central tensor coordinate.
Their values factor through binary homology, so the correction extends from that *actual* summand by zero and kills the complete fixed \(A\)-loop group.
Changing root paths can thus introduce only elements with trivial image on the left or right of the endpoint displacement.

Each named conjugate has first coordinates of just one family, so its square in \(P\) is the identity and either sign gives the same image.
Even multiplicity cancels all unknown central terms individually.
Multiplication of the ordered factors leaves exactly \(\sum_{\ell<m}a_\ell\otimes b_m\), which gives the stated mixed commutator formula for arbitrary conjugators.
Changing the endpoints by a common step preserves the displacement.
On cycles the reverse-ordered displacements telescope, and the central images add without orientation signs.
The same cycle calculation treats competing matchings of the same finite set.
For a nonzero tensor difference a pair of dual basis elements selects a nonzero coefficient, and applying them in all three coordinates respects multiplication into the indicated dihedral group.
The image and transpose-image bounds of the tensor give the claimed lower bounds on the two spans of directions.

Before girth conditioning the neutral cycle searches on each side use only pools at \((0,0)\).
They preserve the independent left pools at \((3,0)\) and \((3,1)\).
At \(a=\delta/32\), \(b=a/2\), the uniform cycle success probability and the number of trials give mean of order at least \(n^{a-b}\), which dominates \(k=\lfloor n^{a/4}\rfloor\).
Permanent marking makes the selected cycles vertex-disjoint within each side and their homology classes independent.
There are ample neutral letters outside the inverse pairs of the four end letters, so the separating letter makes each commutator freely reduced, of length at most \(8R+12\).
Conditionally on the cycle searches and all earlier path trials in the target bin, the used vertices are \(O(n^{1-b})\), while both the first-stub and the permitted turn pools have linear size.
The fresh-path probability is at least \(300^{-(8R+12)}\).
After splitting trials among \(k^2\) words, the exponent loss in the mean is \(\delta(1+8\log(300)/\log(64))/32<0.375\delta\), strictly smaller than \(\delta/2\).
Marking failures as well as successes preserves joint disjointness across words, and binomial lower domination needs no independence between their trial outcomes.
The girth cost \(\exp(O(n^{3a/8}\log n))\) is absorbed by the two search failure bounds since \(a-b=a/2>3a/8\).
One can therefore intersect the resulting conditional events with the source safeguards and the specified exclusion of order-21 quotients.

In each open lift the base color \(3\), the neutral separating letter and the two base vertices of color zero put the two conjugated cycles in their respective index-three summands.
The words are null in the actual cone, with central signature \(u_i\otimes v_j\).
Choosing one disjoint lift per diagonal pair gives a tensor of rank \(k\), so any balanced saturation of those same endpoints must span at least \(k\) directions on each side.
The witnesses are sparse inside left color \(3\), and the proof supplies no saturation of that entire color in the fourteen-color model.

In the first explicit graph only the original \(U_0,V_0\) cycles contribute relators.
Each eliminates a different free edge, so the cone is aspherical and its group is free.
Proper prefixes on these two cycles and the private \(r\) on the remaining left paths verify the two root separations.
On each plain commutator arc there are three interior block boundaries at color \(3\), while on the \(t\)-conjugated arc all interior colors are higher.
Together with the four marked endpoints this gives ten occurrences of the label \(r\).
Pairing corresponding block boundaries gives three copies of \(M_0\), since free reduction of the based corresponding-prefix word gives \(rWr^{-1}\).
The first complete pairing thus has tensor \(M_1\), and the alternative using the entire long path has the same total.
After adding the private \(d\)-arc no new vertex has color \(3\), the group remains free, and the alternative complete total becomes \(M_2\).
The \(A\)-class \([U_0]\) survives in the enlarged graph homology and the distinct tensor indices keep \(M_1,M_2\) independent.
Their discrepancy rules out asphericity of the enlarged cone.
Both explicit families have girth \(m\) and use vertex types different from those of the random construction.

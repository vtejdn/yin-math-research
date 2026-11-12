---
author: Yin
---
# Independent review of the noncentral finite-kernel and stable-shear obstruction

Review act: 2026-11-11T17:48 UTC.
The human record author is Yin.
This is an initial independent whole-artifact mathematical review of the complete uncommitted physical v1 of [L_A0023](../../ledger/Yin_L_A0023_v1.md), as available at that review time.
The reviewer did not participate in its proof development and received no development notes, proof-generation dialogue, author explanation, draft, or prior verdict on this candidate.
The supplied assignment identified the fixed candidate and requested review scope, together with operational metadata only.
The reviewer derived the obligations from the candidate, checked its calculations, and then inspected the fixed mathematical inputs named below.
No earlier review finding was used to establish the candidate's correctness.
Incidental assessment labels in the necessary fixed inputs were not used as proof evidence.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete candidate](../../ledger/Yin_L_A0023_v1.md) | Entire physical v1, including its question, all formulas (1)--(17), source comparisons and explicit limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Boundary matrix](../../ledger/Yin_L_A0023_v1.md#an-additive-noncentral-boundary-matrix) | Actual free amalgam, noncentral cyclic edge, additive vertex decomposition, analytic nullity and zero polynomial kernel. |
| [Whole-artifact finding](#whole-artifact-finding) | [Four-coordinate example](../../ledger/Yin_L_A0023_v1.md#a-four-square-witness-with-maximal-but-deficient-expected-support) | Congruence, membership of each transformed vertex summand, entire polynomial kernel, maximal expected-Gram rank and analytic-kernel distinction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Support compression](../../ledger/Yin_L_A0023_v1.md#smith-support-and-the-exact-compression-correction) | Exact cyclic shear, actual expected-kernel support, corner nullity and both padded support-cut corrections. |
| [Whole-artifact finding](#whole-artifact-finding) | [Stable shears](../../ledger/Yin_L_A0023_v1.md#a-support-lemma-for-additive-preserving-stable-shears) | Orbit-support lemma, every finite m at least one and every finite V satisfying entrywise additivity, whole polynomial kernel and exact nullity correction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Exclusion boundary](../../ledger/Yin_L_A0023_v1.md#what-this-does-and-does-not-exclude) | Cyclic rank invariance and independent padding, together with the restrictions to the displayed realization and shear family. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite-support input](../../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) | The free-tree boundary calculation only, independently rechecked in the actual free group used by the candidate. |
| [Whole-artifact finding](#whole-artifact-finding) | [Diffuse-support comparison](../../ledger/Yin_L_A0013_v1.md#full-support-does-not-supply-a-bounded-inverse-even-for-a-group-ring-matrix) | The stated distinction between full expected support and a bounded inverse; comparison only. |
| [Whole-artifact finding](#whole-artifact-finding) | [Earlier affine realization](../../ledger/Yin_L_A0014_v1.md#affine-realization-changes-the-support-behavior) | The earlier two support cuts and their two unit nullity corrections; comparison with the newly checked four-coordinate calculation. |
| [Whole-artifact finding](#whole-artifact-finding) | [Support-cut identities](../../claims/Yin_C_F0181_v1.md#trace-conventions-and-square-support-cuts) | Projection identities and unnormalized trace conventions only, without importing the finite-dimensional bounded-inverse implication to a diffuse base. |
| [Whole-artifact finding](#whole-artifact-finding) | [Cyclic coefficient normalization](../../claims/Yin_C_A0007_v3.md#polynomial-normalization-over-the-cyclic-edge) | Coset coefficient Gram identity and actual cyclic rational factors used in the candidate's comparison and rank-invariance scope. |
| [Whole-artifact finding](#whole-artifact-finding) | [Rank-deficient boundary](../../claims/Yin_C_A0007_v3.md#the-rank-deficient-normalization-boundary) | The stated missing-full-support question and the requirement for fresh compression corrections; no new review of the full Claim. |

## Obligations and decisive checks

### Actual group, analytic kernel and polynomial kernel

The displayed amalgam identifies with \(F(z,a,b)\) by the free-group presentations.
In particular, \(H=\langle z\rangle\) is infinite cyclic and is noncentral in both \(F(z,a)\) and \(F(z,b)\).
The matrix decomposition \(T=T_a+T_b\) is selfadjoint with the claimed vertex coefficients.

The equation \(A^*\xi=0\) forces an \(\ell^2(G)\) vector to be constant on each infinite \(\langle a\rangle\)-orbit and hence zero.
It follows that \(\partial^*\) is injective, the closure of the range of the row \(\partial=(A\ B)\) is all of the one-coordinate Hilbert module, and its unnormalized analytic rank is one.
Rectangular polar decomposition then gives \(\dim\ker\partial=2-1=1\).
The first coordinate of a vector in \(\ker T\) vanishes, and the remaining equation is exactly \(\partial(x_1,x_2)^t=0\), proving (1).

For a group-ring kernel vector, \(A^*x_0=0\) again gives \(x_0=0\).
Left multiplication by \(a,b\) preserves each right coset \(F(a,b)g\).
The equation \(Ax_1+Bx_2=0\) restricts on each such coset to a finite edge chain with zero boundary in a tree.
A finite nonempty edge support has a leaf whose incident coefficient cannot cancel; removing leaves proves both coefficients vanish.
This proves (2) over the entire group ring \(\mathbb CG\), not merely over \(\mathbb CF(a,b)\).
The distinction between analytic and polynomial kernels is therefore established without assuming an algebraic basis for the analytic kernel.

### Four-coordinate witness and maximal expected support

Direct block multiplication gives (3), and \(P^{-1}\) is a bounded finite group-ring inverse.
Thus the analytic nullity is \(1+\nu_3(T)=2\), with exactly one dimension supplied by the zero summand.
The calculation \(T_av=(Aa,A^*z,0)^t\) and its adjoint show every block of \(Y_a\) lies in \(\mathbb CG_1\).
The corresponding \(b\)-calculation does the same for \(Y_b\).
No commutation involving \(z\) is used.

Applying the polynomial inverses of \(P\) and \(P^*\) to a polynomial kernel vector reduces it to the kernel of \(0\oplus T\).
Equation (2) then proves the exact module equality in (6).
For the Gram expectation, coefficient extraction keeps precisely pairs of entries of \(W\) in the same right \(H\)-coset.
This gives (7), whose upper block is the positive rank-one matrix \((1,z)^t(1,z^{-1})\), with eigenvalues zero and two.
The remaining two diagonal entries are one.
Hence the expected Gram has rank three and a lower bound of one on its support.

For every finite number of polynomial kernel columns, the complete module equality writes them as \(WF\).
The base row \(\ell=(-z,1,0,0)\) annihilates them.
Bimodularity gives (8), and positivity makes the expected Gram annihilate \(\ell^*\).
Since \(\ell\ell^*=2\), this is a full one-coordinate kernel submodule, so every such Gram has rank at most three.
The original \(W\) attains three.
This checks maximality over all finite polynomial kernel matrices, not just over the exhibited column.

Finally, \(W^*W=4I\) makes its Hilbert-module range closed and of dimension one.
Finite group-ring coefficients are dense in that range.
The entire analytic kernel has dimension two, so its extra dimension is absent from the closed span of the entire polynomial kernel.
An invertible finite group-ring congruence of a constant matrix would transport a constant kernel basis to polynomial columns whose closed span is the complete analytic kernel.
The dimension discrepancy excludes exactly that possibility.

### Actual expected-kernel support and compression

The explicit \(Q\) and \(Q^{-1}\) are cyclic group-ring matrices.
Multiplying \(PQ^{-1}\) removes the \(z\) component of the shear and leaves \((0,a,b)^t\), which verifies every entry and sign of (14), including \(s=Aa+Bb\).
The transformed summands remain in their original vertex rings.

The equation \(A^*x_2=0\) forces the second coordinate of every analytic kernel vector to vanish.
On the other three coordinates, the only equation is \(R\eta=0\), where \(R=(-s,A,B)\).
The adjoint of \(R\) is injective because one of its coordinates is \(A^*\).
Therefore \(R\) has rank one and nullity two.
In particular, \(p_{\widehat Y}\le q\).

The vector \(W_0\) has \(W_0^*W_0=3I\), and its range projection is \(W_0W_0^*/3\).
That projection lies below \(p_{\widehat Y}\).
Expectation therefore gives the lower bound \(q/3\), while \(p_{\widehat Y}\le q\) gives the upper bound \(q\).
This proves (16) for the complete analytic kernel and identifies \(q\) as its actual expected support.

Every retained entry in \(q\widehat Yq\) is zero.
Viewed on the three-coordinate corner, its nullity is three, whereas the original four-coordinate matrix has nullity two.
The increase by one is independently the rank of \(R\).
If all four coordinates are retained instead, \(\widehat Yq\) has rank one and nullity three.
Its adjoint kills exactly the range of \(q\), since its only potentially nonzero input coordinate is tested injectively by \(A^*\).
The second cut yields the four-coordinate zero matrix with nullity four.
Thus the padded sequence has the exact nullities \(2,3,4\), with corrections one and one.
The corner nullity three and padded nullity four are different ambient conventions and are correctly distinguished in the candidate.
No integrality assumption for an unknown compression is used.

### Every additive-preserving stable shear in the stated family

For an orbit \(\langle a\rangle g\) outside \(G_1\), the orbit is disjoint from \(G_1\) and meets \(G_2\) at most once.
Two intersections would imply a nonzero power of \(a\) belongs to \(G_2\), contrary to the free-group normal form.
The coefficients of a finite difference \((a^{-1}-1)c\) sum to zero on each orbit.
Membership in \(\mathbb CG_1+\mathbb CG_2\) restricts that difference to at most one coefficient on the orbit, which therefore vanishes.
The original finite coefficient sequence is translation invariant there and hence zero.
This proves (9), and the \(b\)-version gives (10).

Now fix any finite integer \(m\ge1\) and any \(V\in M_{3,m}(\mathbb CG)\).
The proof assumes only that every entry of the total \(Y(V)\) lies in the additive linear space \(\mathbb CG_1+\mathbb CG_2\).
It does not assume that the separately conjugated summands have vertex membership.
The lower-left block contains \(-A^*c\) and \(-B^*c\).
Applying (10) entrywise forces the whole row \(c\) into \(\mathbb CH\).

The polynomial inverse of \(P_V\), together with (2), proves the full polynomial-kernel identity in (12).
Bounded invertible congruence gives analytic nullity \(m+1\), so the zero stabilization adds exactly \(m\) to the nullity of \(T\).
The base row \(\ell_V=(-c,1,0,0)\) annihilates the complete polynomial kernel module.
Its product \(\ell_V\ell_V^*=1+cc^*\) is boundedly invertible.
Consequently the same positive-Gram argument supplies a nonzero kernel submodule for every finite polynomial expected Gram.
These deductions hold for every admissible \(m,V\); they do not rely on a chosen finite list of kernel columns or on a special choice of the lower two rows of \(V\).

### Further transformations and exclusion limits

The cyclic affiliated field in this argument is the actual rational field \(\mathbb C(z)\) used in the fixed normalization input.
For a finite witness, its expected Gram is the coefficient Gram \(FF^*\) from a finite right-coset expansion.
An invertible cyclic rational factor preserves the field rank of that coefficient matrix whenever the transformed witness is again finite.
One may clear a common nonzero Laurent denominator to justify the coefficient identity using bounded bimodularity before invoking affiliated rank invariance.
The candidate's further-congruence statement therefore preserves exactly the claimed deficiency.
Adding separate zero-coordinate witnesses has block-diagonal expected Gram and raises ambient size and rank equally.

Neither observation classifies arbitrary alternating enlargements and congruences.
The candidate explicitly leaves invertible auxiliary blocks, more general additive realizations, general polynomial congruences and analytic boundary methods outside its exclusion.
The worked support compression succeeds with its certified corrections, so the result is not an obstruction to every repair.

## Source and dependency limits

The tree calculation, all displayed group-ring products, positivity arguments, orbit-support lemma and nullity corrections were checked directly.
The comparison with L_A0013 is applicable because its full-support expected kernel lacks a uniform lower bound, whereas the candidate's displayed Gram is uniformly positive on a proper support.
The comparison with L_A0014 and C_F0181 is at the actual projection identities and trace corrections.
No finite-dimensional implication that a diffuse full-support positive operator has a bounded inverse was used.

The accepted finite-trace polar-decomposition and affiliated-rank foundations were inspected in [MSY23-U004, Lemmas 5.1--5.5](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and [its Lemma 5.9 account](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof).
The actual subgroup and right-coset interface was checked against [Lin93-U001](../literature/Lin93/Yin_U001.md#ring-lemmas-and-the-extension-argument).
The broad assertion that free groups already have known Atiyah ranks is supported there as background and is not needed for any computed nullity in this candidate.
These foundations are accepted at their recorded source scope; the underlying general affiliated-algebra theory and the full Lin93 theorem were not re-audited.

The reference to Smith support is realized here by the explicit unimodular matrix \(Q\), so no uncomputed generic Smith reduction is needed for the example.
The generic normalization comparison retains the recorded Cohen locators in [C_A0007_v3](../../claims/Yin_C_A0007_v3.md#source-comparison-and-continuation-limit); it does not create a new source claim or require the full BBL21 boundary theorem in the present proof.
The compressed summands are zero, so the stated trivial subordination case needs no additional nontrivial analytic application.
Source completeness is supported for the candidate's actual uses at these declared existing-source boundaries.
No new original-source acquisition, historical priority search, formal verification or numerical validation was performed or claimed.

## Whole-artifact finding

The complete fixed L_A0023_v1 argument is mathematically supported at its stated scope.
No gap was found in its noncentral example, complete polynomial-kernel characterization, maximal deficient expected Gram, exact actual support compression, or universal quantifiers within the specified stable-shear family.
Its correction terms are established by direct kernel and rank calculations.
This finding does not establish a general impossibility theorem for other realizations or transformations, supply a new Atiyah group class, or select any Task completion.

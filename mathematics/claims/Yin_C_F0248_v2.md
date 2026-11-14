---
author: Yin
---

# Canonical dual domains on finite planar networks with unrestricted tangencies

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a bounded finite normal generating tuple satisfying actual starred ACSY in a finite von Neumann algebra with faithful normal probability trace.
Suppose \(\sigma(Z)\) is contained in a finite union of compact regular embedded \(C^2\) arcs, each regular up to its endpoints, with distinct edges meeting only at common endpoints after finite subdivision.
There is no condition on the angles or the order of contact of incident edges.
Closures of embedded cycles can be divided into edges.
Other coordinates are arbitrary bounded normal generators with any joint law satisfying the original hypothesis.

The [finite-network conclusions of v1](Yin_C_F0248_v1.md#statement) hold at this generality.
The original right slice on the represented mixed starred core has finite column cost, in both orientations.
Its closure and its Hilbert adjoint both contain \(M\Omega\) in their domains, and its negative closure is a generator-first strong dual at this coordinate.
If every coordinate has such a carrier, actual conjugate variables and the full strong dual condition are equivalent.
In particular two branches can meet to infinite order, as for \(x\pm i e^{-1/x^2}\) on \(0<x\le1\) with common vertex at zero.
No uniform cost over networks or laws is asserted.

## Argument

### Real parameters near a tangential contact

Use the [finite subdivision and pairwise charts of v1](Yin_C_F0248_v1.md#a-finite-subdivision-admitting-pairwise-graph-charts).
At an original vertex where two outgoing unit tangents agree, project both arcs onto that common direction.
On sufficiently short initial pieces this projection has positive derivative bounded away from zero and both branches have \(C^2\) graph parametrizations up to the vertex.
Since there are finitely many incident pairs, one may shorten the initial pieces for all the required charts.
For a fixed ordered pair choose a common projected length on both pieces, splitting off any excess piece.
For this pair the rectangle involving that excess piece and the other edge has positive separation by compactness and the absence of another shared endpoint on the selected short pieces.
This extra split can be chosen separately when estimating each pair.
The other rectangles in the original finite partition retain their own charts.

Translate and rotate about the vertex.
In the common projection the curves are \(z_\pm(x)=x+i(g(x)\pm d(x))\), \(0\le x\le R\), where \(g,d\in C^2[0,R]\), \(g(0)=d(0)=g'(0)=d'(0)=0\), and \(d(x)>0\) for \(x>0\).
Indeed the two heights cannot change order off the common vertex since equal heights at the same parameter would be an intersection.
We may restrict both branches to any smaller interval \(0\le x\le u\le R/2\).
In the rest of their cross rectangle either \(x\) or \(y\) belongs to \([u,R]\), giving two positive-distance pairs of compact sets.
They have finite original localized columns by [v1's separated-pair estimate](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple).

We construct a real parameter on the two small branches.
Take \(x_1=u\), \(x_{n+1}=x_n-c d(x_n)\), using a constant \(c>0\) so small that \(c\|d'\|_\infty<1/2\).
The lengths \(\ell_n=c d(x_n)\) are at most \(x_n/2\) by \(d(0)=0\).
The positive \(x_n\) decrease to zero, since a positive limit would give a positive limiting step.
Throughout a closed tile \([x_{n+1},x_n]\) its heights are between \(d(x_n)/2\) and \(3d(x_n)/2\) by the Lipschitz estimate.
On its interior give the two copies real labels
\[
 F_\pm(x)=10x_{n+1}+b_\pm\ell_n+(x-x_{n+1}),\qquad b_+=1,\quad b_-=4 .
\]
Their images are disjoint intervals in \([10x_{n+1},10x_n]\).
The errors \(\epsilon_\pm(x)=F_\pm(x)-10x\) satisfy \(|\epsilon_\pm(x)|\le C_c d(x)\).
On each labelled interval the forward map decodes \(x\) with slope one and returns \(z_\pm(x)\).
Interpolate its endpoint values across the gaps, extend constantly across the last top gap, and send zero to the vertex.
The within-tile gap has length \(2\ell_n\) and its endpoint images differ by at most \((1+\|g'\|_\infty)\ell_n+d(x_n)+d(x_{n+1})\).
The between-tile gap has length \(5\ell_{n+1}+\ell_n\) and the images there have distance \(2d(x_{n+1})\).
These bounds and continuity at zero give one finite forward Lipschitz constant on the small parameter interval.

Assign the remaining finitely many edge pieces disjoint, positively separated parameter intervals by arclength, interpolating between intervals to obtain a single Lipschitz forward map \(h\) on their real hull.
Restrict the assignment to the open labelled intervals of the actual edges.
The finite vertices and countable tile endpoints have zero spectral projections by diffuseness.
The map there has a Borel inverse onto its conull image, regardless of intersections involving the interpolating segments off the parameter support.
Consequently \(S=h^{-1}(Z)\) generates \(W^*(Z)\), with arbitrary bounded assignments on exceptional points.
As in [the real parameter argument](Yin_C_F0250_v1.md#a-real-parameter-interleaving-the-two-branches), scalar packing on the disjoint images of equal-mesh cells gives an \(L^3\) real density.
The invariant liberation vacuum has finite inverse real gap energy since \(|h(s)-h(t)|\le\operatorname{Lip}(h)|s-t|\).
The actual scalar vacuum and this finite energy give an actual real-coordinate vacuum; the other coordinates retain their own vacua.
The old right slice at \(S\) has finite mixed column cost by the [real-coordinate estimate](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column).

### A Schur bound from separation in height

All subsequent estimates concern the upper first leg and the lower second leg in the small chart.
They apply to arbitrary branch measures carried by it.
Write \(d_x=d(x),d_y=d(y), v=x-y\) and
\[
 D_0=v+i(d_x+d_y),\qquad D=D_0+i(g(x)-g(y)),\qquad
 K=\frac{F_+(x)-F_-(y)}{D}.
\]
The transpose gives the reversed rectangle.
We use the Schur multiplier norm for integral operators on the product of the two branch measures.
Pointwise products of Schur symbols compose their multiplication maps; separated factors cost the product of their supremum norms.

Put \(G(x,y)=\int_0^1 g'(\theta x+(1-\theta)y)\,d\theta\).
On \([0,u]^2\) one has \(\|G\|_{\rm Schur}\le C u\|g''\|_\infty\).
To see this, multiply \(g'(ut)\) on \([0,2]\) by a smooth cutoff equal to one on \([0,1]\) and zero near 2, and extend by zero for \(t<0\).
Because \(g'(0)=0\), its compactly supported periodic extension has \(H^1\) norm at most \(C u\|g''\|_\infty\).
Cauchy–Schwarz bounds the sum of the moduli of its Fourier coefficients by this same quantity times a fixed constant.
Each exponential evaluated at \((\theta x+(1-\theta)y)/u\) separates into two unitaries.
Integrating in \(\theta\) proves the claim, including pairs on the diagonal.
Choose \(u\) sufficiently small in the estimates below.
Then \(K_0=(1+iG)^{-1}\) has Schur norm at most two by its norm-convergent geometric series.

For \(M_0=\max(1,\|d''\|_\infty)\), the positive height satisfies
\[
                    |d'(x)|^2\le 2 M_0 d(x)\qquad(0<x\le u).
\]
Indeed \(|d'(x)|\le M_0x\) and \(x-d'(x)/M_0\) belongs to \([0,2u]\).
The upper Taylor bound for \(d\) at this test point and nonnegativity there give the inequality.
Thus \(\sqrt d\) is \(L_0=\sqrt{M_0/2}\)-Lipschitz up to zero.
This local one-sided calculation uses the square-root estimate of Glaeser's Lemma I, credited there to B. Malgrange. [Source and original hypotheses, pp. 203–204](../audits/literature/Gla63/readme.md#lemme-i)

Let \(D_*=\sup_{[0,u]}d\), \(\delta_j=2^{-j}D_*\), and partition each branch by the height bands \(\delta_j/2<d\le\delta_j\), \(j\ge0\).
These Borel sets need not be intervals.
Flat levels are allowed and the bands include exactly one copy of each positive height.

On two bands with indices differing by at most one, the factorization
\[
  \frac{i\sqrt{d_xd_y}}{D_0}
    =\int_0^\infty
        \sqrt{d_x}\,e^{-\lambda d_x+i\lambda x}\,
        \sqrt{d_y}\,e^{-\lambda d_y-i\lambda y}\,d\lambda
\]
gives Schur norm at most \(1/2\), since both Hilbert-space factor norms are \(1/\sqrt2\). [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001)
The heights vary by at most a factor four across either such rectangle.
Consequently \((d_x+d_y)/D_0\) and \(v/D_0=1-i(d_x+d_y)/D_0\) have numerical Schur norm bounds, by multiplying the factorization by the separated square-root ratios.
The same argument and \(|\epsilon_\pm|\le C_c d\) control \((\epsilon_+(x)-\epsilon_-(y))/D_0\).
Denote the numerical bound for \(v/D_0\) by \(C_1\); choose \(u\) so that \(C_1\|G\|_{\rm Schur}<1/2\).
Since \(D/D_0=1+iG v/D_0\), the quotient \(D_0/D\) has Schur norm at most two on each of these rectangles.
The identity
\[
   K=\left(10\,v/D_0+(\epsilon_+(x)-\epsilon_-(y))/D_0\right)D_0/D
\]
therefore bounds \(K\) uniformly there.
For any one of these three offsets both lists of band projections are pairwise orthogonal.
The product with the symbol masked to their union acts as the direct sum of the multiplied compressions, with norm at most the common rectangle bound.
This reasoning also applies to \(K-10K_0\) by restricting the bounded baseline.

For a remaining ordered pair of bands, place the higher band at scale \(\delta\), and group all lower bands \(d\le\delta/4\) in a single second set.
Either variable may be the higher one.
The square-root estimate forces
\[
            |v|\ge b\sqrt\delta,\qquad
            b=(1/\sqrt2-1/2)/L_0>0
\]
everywhere in this product set, with no restriction on the order of \(x,y\).
There is a Schur symbol \(J_\delta(x,y)\) equal to \(1/v\) there and of norm at most \(C_b/\sqrt\delta\).
Take an even smooth cutoff \(\chi\) vanishing near zero and equal to one for \(|t|\ge1\), and put \(\phi(t)=\chi(t)/t\), extended by zero at zero.
Both \(\phi\) and its first derivative are square integrable, so its Fourier transform is integrable by Plancherel and Cauchy–Schwarz with the inverse weight \(1/(1+\omega^2)\).
Fourier inversion writes \(\phi((x-y)/(b\sqrt\delta))/(b\sqrt\delta)\) as an integral of separated unitaries of this cost.
On the higher/lower rectangle \(A=d_x+d_y\) has separated norm at most \(2\delta\).
There \(D=v(1+iG+i A J_\delta)\).
By reducing \(u\) further we have \(\|G\|_{\rm Schur}+2C_b\sqrt{D_*}<1/2\), hence \((1+iG+i A J_\delta)^{-1}\) has Schur norm at most two on every such rectangle.
Subtracting the global baseline exactly gives
\[
 K-10K_0=
    (\epsilon_+(x)-\epsilon_-(y)-10i K_0 A)\,
    J_\delta(1+iG+i A J_\delta)^{-1}.
\]
Its rectangle norm is at most \(C\sqrt\delta\).
A rectangular symbol extends by zero to the whole cross product with the same bound, using the two projection compressions.
Summing over the two orientations and the geometric height scales costs at most \(2C\sum_j\sqrt{\delta_j}<\infty\).
Together with the three comparable offsets and \(10K_0\), this proves a Schur bound on the entire cross rectangle.
All these identities hold on the Borel parameter set of positive heights, including points where \(x=y\) in the comparable bands.
Pullback by the labelled coordinates is an isometric identification of the two branch measure spaces and preserves the multiplier estimate.

### Original mixed domains and finite assembly

Use the [localized original-core transfer](Yin_C_F0250_v1.md#recovery-of-the-original-columns) with this bounded cross symbol.
On the real parameter core the Schur insertion estimate bounds the slice on every finite column.
The forward Lipschitz decoder gives original word columns approximated in the real-coordinate derivation graph with limit superior of the input column norm at most \(1+\varepsilon\) for a target column of norm at most one.
On the original generators insertion gives the rectangle mask at \(Z\), its product with the original forced phase at \(Z^*\), and zero at the omitted starred generators.
The two localized derivations therefore agree on the entire represented mixed core.
A rigid rotation contributes its reciprocal as a single modulus-one factor.
Boundedness passes the estimate to the original graph limits, followed by \(\varepsilon\downarrow0\).

A single-piece pair, a positive-distance pair, or an incident pair with different outgoing tangents is covered by the corresponding [v1 localized proof](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple).
For these estimates all pieces outside the chosen chart occupy separate real parameter intervals, so same-direction tangencies elsewhere do not affect their application.
The new cross estimate, its transpose and finitely many positive-distance pieces handle every remaining incident pair.
All estimates land on the same original core even though the auxiliary real parameter varies with the ordered pair.
Summing over the finite spectral partition proves the distinguished column bound.
Reflection of the network gives the right estimate for the adjoint tuple, hence the left bound on original single inputs by the tracial flip.
The [two-slice theorem](Yin_C_F0072_v1.md#statement) gives both domains, and the core commutator passes to the closure by graph approximation.
The [normal strong-to-ACSY implication](Yin_C_F0070_v1.md#statement) supplies the reverse implication in the all-coordinate conclusion.

The interleaved encoding for the power-order example was developed by the check_countable agent.
The coordinating agent developed the separation by height, and check_countable checked the one-sided Taylor bound, encoding scale, height sum and local graph assembly during development.
Arcs with infinitely many intersections that admit no finite network subdivision are outside this statement.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:35 |
| status | open |
| reason | Fix the finite-network theorem without an outgoing-angle restriction and its height decomposition for independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite regular networks with arbitrary contacts, both original bounded-vector domains and the all-coordinate equivalence. |
| argument | [Argument](#argument) | Adaptive encoding, separated-height kernel, near-height direct sums, local original-column transfer and finite network assembly. |
| dependency | [Finite network subdivision](Yin_C_F0248_v1.md#a-finite-subdivision-admitting-pairwise-graph-charts) | Finite pairwise subdivision for single, distinct-angle and separated pieces. |
| dependency | [Untouched network rectangles](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Bounded local charts and localized positive-distance Fourier recovery on the original mixed core. |
| dependency | [Real encoding and ACSY](Yin_C_F0250_v1.md#a-real-parameter-interleaving-the-two-branches) | Scalar packing on disjoint images, invariance of liberation and finite transformed inverse-gap energy for a conull encoding with a Lipschitz decoder. |
| dependency | [Real-coordinate bound](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Original mixed right-column estimate for the selfadjoint distinguished parameter. |
| dependency | [Schur Hilbert factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | Product-measurable bounded Hilbert factors on the separate branch spaces. |
| dependency | [Original localized transfer](Yin_C_F0250_v1.md#recovery-of-the-original-columns) | Identification with the original derivative on generators, norm-controlled approximation of mixed columns and treatment of same-branch rectangles. |
| dependency | [Both original domains](Yin_C_F0072_v1.md#statement) | Part B from the two actual sliced estimates. |
| dependency | [Normal strong-to-ACSY implication](Yin_C_F0070_v1.md#statement) | Converse on the whole normal tuple. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:38 |
| status | proved |
| reason | Adopt the unrestricted tangency extension after independent review of both height estimates and the return to the original starred core. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite regular networks with arbitrary contacts, both original bounded-vector domains and the all-coordinate equivalence. |
| argument | [Argument](#argument) | Adaptive encoding, separated-height kernel, near-height direct sums, local original-column transfer and finite network assembly. |
| dependency | [Finite network subdivision](Yin_C_F0248_v1.md#a-finite-subdivision-admitting-pairwise-graph-charts) | Finite pairwise subdivision for single, distinct-angle and separated pieces. |
| dependency | [Untouched network rectangles](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Bounded local charts and localized positive-distance Fourier recovery on the original mixed core. |
| dependency | [Real encoding and ACSY](Yin_C_F0250_v1.md#a-real-parameter-interleaving-the-two-branches) | Scalar packing on disjoint images, invariance of liberation and finite transformed inverse-gap energy for a conull encoding with a Lipschitz decoder. |
| dependency | [Real-coordinate bound](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Original mixed right-column estimate for the selfadjoint distinguished parameter. |
| dependency | [Schur Hilbert factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | Product-measurable bounded Hilbert factors on the separate branch spaces. |
| dependency | [Original localized transfer](Yin_C_F0250_v1.md#recovery-of-the-original-columns) | Identification with the original derivative on generators, norm-controlled approximation of mixed columns and treatment of same-branch rectangles. |
| dependency | [Both original domains](Yin_C_F0072_v1.md#statement) | Part B from the two actual sliced estimates. |
| dependency | [Normal strong-to-ACSY implication](Yin_C_F0070_v1.md#statement) | Converse on the whole normal tuple. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0257_v2.md#finding) | Arbitrary finite regular networks, all contact orders, both orientations and bounded-vector domains, inverse-secant transfer and the normal all-coordinate equivalence. |

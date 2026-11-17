---
author: Yin
---

# Joint quotient kernels for restoring the words \(1+x^q y+yx\)

<a id="statement"></a>
## The conditional determinant comparison

Fix an integer \(q\ge2\), put \(m=q+1\), and use independent real symmetric Wigner inputs with the fixed centered laws and two moments of the [finite-variance Task](../tasks/Yin_T_F0012_v3.md#contract).
Write \(P_q=1+x^q y+yx\), \(P_N=P_q(X_N,Y_N)\), \(p=P_q(s_1,s_2)\), \(h_n=\lceil\log(n+3)\log\log(n+3)\rceil\), and \(k=2\lfloor\log^3(N+3)/2\rfloor\).
Let \(J\) omit a prescribed set of \(k\) sites, \(n=|J|\), \(T_w=P_q(X_{JJ},Y_{JJ})-wI\), and let \(t_1(w)\le\cdots\le t_n(w)\) be its singular values.
Write \(p_j(T)\) for the product of the largest \(j\) singular values.
For all sufficiently large \(N\), and for each bounded disk and each positive area tolerance, there are measurable exceptional parameter sets \(E_N\) whose probabilities of exceeding that tolerance are summable, such that, off \(E_N\) and the real axis,
\[
 |\det(P_N-wI)|\ \ge\
 e^{-C_{q,R}(h_n^3+k)\log N}\,
 p_{n-2h_n}(T_w)\min(1,t_{2h_n+1}(w))^{2h_n}.
 \tag{1}
\]
The statement holds under every permitted coupling across dimensions.
No initial principal-trim theorem is assumed for (1).

If the full-size retained logarithm at trim \(h_N\), the old-minor retained logarithm at trim \(2h_n\), and the old-minor adjacent loss satisfy
\[
 \begin{split}
 N^{-1}\log p_{N-h_N}(P_N-w)&\longrightarrow u(w),\\
 N^{-1}\log p_{n-2h_n}(T_w)&\longrightarrow u(w),\\
 (2h_n/N)\log^-t_{2h_n+1}(w)&\longrightarrow0
 \end{split}                                                   \tag{2}
\]
almost surely in disk \(L^1\) under every coupling, where \(u(w)=\tau\log|p-w|\), then the ordinary potentials converge to \(u\) almost surely in \(L^1_{\mathrm{loc}}\), and the empirical eigenvalue measures converge weakly almost surely to the Brown measure of \(p\).
Under the same hypothesis, for every \(R,\epsilon>0\), with ascending singular values,
\[
 \sum_{N>h_N}\Pr\left\{N^{-1}\int_{|w|\le R}
       \sum_{i\le h_N}\log^-s_i(P_N-wI)\,dA(w)>\epsilon\right\}<\infty .
\]
Thus (2), rather than independence of all \(m^2\) resolvent entries, is the remaining input for this implication.
The present statement makes no prescribed-parameter assertion at a parameter stratum where the chosen joint basis changes.

For \(q=3\), each physical restoration uses four directions and eight independent panels.
Its joint conditional small-ratio exponent on \(s\) nodes is \(s/512\); \(1024\) nodes suffice for the summable chronological bound.

<a id="kernels"></a>
## The actual kernel array, including its polynomial part

Use the [partial pencil and its exterior](../ledger/Yin_L_F0069_v3.md#partial), with \(q\) physical channels:
the first row is \(((1-w)I+YX,X,0,\ldots,0)\), the auxiliary diagonal is \(-I\), each auxiliary superdiagonal is \(X\), and block \((q,1)\) is \(XY\).
Denote this pencil by \(K_q(w)\) and put \(R_w=(P_q(X,Y)-wI)^{-1}\).
The first-column and first-row factors of its inverse are
\[
 L=(I,X^{q-1}Y,X^{q-2}Y,\ldots,XY)^{\mathsf T},\qquad
 D=(I,X,X^2,\ldots,X^{q-1}).
\]
Its remaining part is the inverse of the upper triangular auxiliary pivot, extended by zero in the first channel.
That auxiliary inverse has entries \(-X^{b-a}\) for auxiliary channel indices \(2\le a\le b\le q\) and zero below the diagonal.

For a physical vector \(v\), let \(F(v)\) have columns \((v,0,\ldots,0)\), \((Yv,0,\ldots,0)\), followed by \(v\) in each channel \(2,\ldots,q\).
The transpose-symmetric physical kernels of \(F(v)^{\mathsf T}K_q(w)^{-1}F(v)\) are consequently
\[
 \mathcal K_{ab}(w)=\operatorname{sym}(A_aR_wB_b+J_{ab}),\quad
 A=(I,Y,X^{q-1}Y,\ldots,XY),\quad
 B=(I,Y,X,\ldots,X^{q-1}),                            \tag{3}
\]
where \(J_{a b}=-X^{b-a}\) for \(3\le a\le b\le m\), and all its other entries vanish.
Here transpose reverses words but does not conjugate the scalar parameter.
For \(q=3\), the polynomial entries are \(J_{33}=J_{44}=-I\) and \(J_{34}=-X\).
In particular, discarding the entire auxiliary-pivot contribution would discard a nonscalar physical kernel.
Only scalar identity contributions disappear in distinct-panel corners.

<a id="quotient"></a>
## A joint quotient and detectors supported at one node

Fix distinct nodes \(w_1,\ldots,w_D\) in the open upper half-plane and include their conjugates.
At these parameters take the complex span of all entries of (3), modulo scalar rational functions.
No assertion of independence of the individual entries or of a direct sum over nodes is needed.
Choose a real basis \(G_1,\ldots,G_r\) of the real span of their entrywise real and imaginary parts modulo real scalars.
At real symmetric matrix evaluations these are real transpose-symmetric physical kernels.
There are complex coefficient matrices \(M_{\ell,z}\) and scalar matrices \(C_z\) such that
\[
       (\mathcal K_{ab}(z))_{ab}=C_z I+\sum_{\ell=1}^rM_{\ell,z}G_\ell.
                                                               \tag{4}
\]
The basis is joint over all nodes, rather than chosen independently at each node.

At commuting values write \(a=z-1\), \(d(x)=x^q+x\), and specialize to \(y=a/d(x)\).
The residue numerator of (3), before its nonzero scalar residue factor, is
\[
 l_z(x)r_z(x)^{\mathsf T},\qquad
 l_z(x)=(1,y,x^{q-1}y,\ldots,xy)^{\mathsf T},\quad
 r_z(x)=(1,y,x,\ldots,x^{q-1})^{\mathsf T}.             \tag{5}
\]
Choose once and for all \(m\) positive points \(x_j\) at which the two evaluation matrices in (5) are invertible for \(a=1\).
Such points exist by the [component-independence calculation](../ledger/Yin_L_F0069_v3.md#residues): their two nonzero rational determinants have a common nonempty open set of nonvanishing.
For other \(a\ne0\), the left evaluation matrix rescales its last \(q\) rows by \(a\), and the right one rescales its second row by \(a\).
Thus
\[
                B_z=\sum_{j=1}^m l_z(x_j)r_z(x_j)^{\mathsf T}       \tag{6}
\]
is invertible at every nonunit \(z\), with determinant a fixed nonzero constant times \((z-1)^m\).
Its norm and inverse determinant are uniformly bounded on each compact nonreal parameter set.

Consider any joint relation modulo scalars among the kernels at all nodes and conjugates.
In the commuting specialization, take the residue in \(y\) at \((z-1)/d(x_j)\).
All other nodes, the scalar term, and the polynomial pivot term are regular there.
Multiplying by the nonzero derivative \(d(x_j)\) shows that the coefficient array at \(z\) annihilates \(l_z(x_j)r_z(x_j)^{\mathsf T}\), under the bilinear entrywise pairing.
After summing in \(j\), it annihilates \(B_z\).
Finite-dimensional annihilator duality now puts the array supported by \(B_z\) at \(z\), and zero at every other node including the conjugates, in the coefficient image of the joint quotient.
Equivalently, there is \(\beta^{(z)}\in\mathbb C^r\) such that
\[
 \sum_\ell\beta^{(z)}_\ell M_{\ell,t}=\mathbf1_{t=z}B_z,
 \qquad
 \sum_\ell\beta^{(z)}_\ell\overline{M_{\ell,t}}=0
 \quad(t\text{ in the upper half-plane}).                         \tag{7}
\]

For explicit control, choose each real basis kernel from the real and imaginary entry list.
The real coefficient matrix of that list in the chosen basis then contains an identity submatrix.
The real-coordinate detector is \(B_z/2\) on the real-part entries at \(z\), \(-iB_z/2\) on the imaginary-part entries there, and zero elsewhere.
Its entries at the selected basis positions are exactly \(\beta^{(z)}\).
Hence \(\|\beta^{(z)}\|\le\|B_z\|_F\), up to an immaterial fixed factor, independently of a small coefficient minor.

If \(\ell_z\) is a complex linear functional on matrices and \(a_\ell=\sum_z v_z\operatorname{Re}\ell_z(M_{\ell,z})\), for real numbers \(v_z\), then (7) gives
\[
            \sum_\ell a_\ell\beta^{(z)}_\ell
                    =\tfrac12v_z\ell_z(B_z).                       \tag{8}
\]
Consequently, if every \(|\ell_z(B_z)|\ge c\) and \(\sum_zv_z^2=1\), the real joint basis coefficient vector \(a\) has norm bounded below by a positive constant depending only on \(c,D\) and the detector bound.
This replaces the separate-node independence step in the [fixed-dimensional polarization proof](Yin_C_F0363_v2.md#argument).

<a id="patches"></a>
## Compact parameter patches for the physical corners

Here is a precise choice of the joint bases and of the parameter sets on which the constants are uniform.
Every expression (3) is regular at the formal noncommuting origin, since \(1-z\ne0\).
Expand
\[
 (1-z+x^q y+yx)^{-1}
   =(1-z)^{-1}\sum_{b\ge0}[-(x^q y+yx)/(1-z)]^b.
\]
After removing the coefficient of the empty word, the real and imaginary kernels give a countable coefficient matrix with \(2Dm^2\) columns.
Every entry is a rational function of the real and imaginary node coordinates, with denominators nonzero on the upper-half-plane parameter domain.
Take its rank over the field of those real rational functions, and choose a nonzero maximal minor \(\Delta\), involving finitely many word rows.
On \(\Delta\ne0\), its selected columns form a basis and Cramer's rule supplies all the other coefficient columns.
Every extra row satisfies the same identities because every larger minor is identically zero.
Thus these are identities of formal series, and hence of the rational kernels modulo scalars.

For completeness, the last implication uses only the regular rational-series realization.
Expand each fixed word in the polynomial denominator into a finite path, as in the [word-chain construction](Yin_C_F0359_v1.md#construction), to represent a regular rational expression by a finite matrix of affine series.
Its word coefficients are the row functional evaluated on the states reachable from the initial column by the letter matrices.
If all coefficients vanish, that row functional vanishes on the reachable space, which is invariant under every letter matrix.
Restricting the finite realization to this space makes the expression zero wherever the realization is defined, and therefore zero in the free field.
Conversely a rational identity has zero series at its regular origin.
The [faithful semicircular free-field evaluation](Yin_C_F0011_v1.md#yin_c_f0011) identifies these algebraic relations with relations in the affiliated free model.

The numerator of \(\Delta\) is a nonzero real polynomial on this real parameter domain.
Its zero set has Lebesgue measure zero: this follows by induction on the number of real coordinates, viewing it as a polynomial in the last coordinate and excluding the common zero set of its nonzero coefficient polynomials.
On a bounded separated-tuple region, compact sets bounded away from this zero set exhaust the region up to a null set.
The chosen basis, its coefficients in (4), and the affiliated kernels are continuous in measure there, and the scalar coefficient bounds are uniform on each such compact set.
If several node subsets will be tested, impose the corresponding finitely many nonzero-minor conditions for those subsets; their union of excluded zero sets is still null.

For each unit real combination of the joint basis kernels, a distinct-panel corner in the free model is nonzero.
Indeed the equal-trace coordinate projections are free from the semicircular inputs, and the [free-corner argument](Yin_C_F0351_v9.md#kernels) would otherwise force this transpose-symmetric combination to be scalar.
This contradicts its independence modulo scalars.
Compactness of the parameter patch and of the coefficient sphere, together with continuity in measure, gives a fixed positive trace fraction of singular values above a fixed positive threshold.
Each denominator \(P_q(s)-z\) is a nonzero free-field element and has no zero singular atom, uniformly in the cutoff sense on a compact parameter set.

The [bounded physical-corner transfer](Yin_C_F0351_v6.md#physical-corners) therefore applies to this fixed joint basis.
Clip the two inputs, replace the inverse by its bounded regularization, and use the finite word telescoping bounds for the outside factors and the polynomial pivot entries in (3).
All word degrees and the number of kernels are fixed.
The total discrepancy rank can be chosen smaller than any specified fixed fraction of the corner-count margin, outside \(Ce^{-cn}\) on the old minor.
Additional rank \(O_q(k)\) changes fit within that margin.
The [projected output and Fourier estimate](Yin_C_F0351_v6.md#border-tests) is consequently uniform for the joint basis on this compact patch, after deleting the rank-error ranges, any fixed-dimensional space determined before the first panel draw, and any sufficiently small fixed fraction of output coordinates.

<a id="polarization"></a>
## Independent panels with a joint basis

Split the old physical sites into \(2m\) deterministic panels of asymptotically equal size.
The actual fresh strict-upper Wigner column has product law over these panels, also conditional on the old minor and all previously exposed columns.
This is the actual-column sampling hypothesis of the [independent-panel theorem](Yin_C_F0363_v3.md#statement), not merely a claim about the laws of separate difference vectors.

Use its independent panel differences and the polarized quantities \(U_{b,z}\) of [C363v2](Yin_C_F0363_v2.md#argument), with the fixed matrix \(B_z\) from (6).
When the last pair is kept together, its coefficient functional satisfies \(\ell_z(B_z)=U_{b-1,z}\).
The other pairings have last-panel coefficient vectors in a fixed-dimensional span determined before the penultimate draw.
Projection removes this span and all rank errors.
On nodes for which \(|U_{b-1,z}|\) exceeds the fixed threshold, (8) supplies a lower bound for every unit real combination of the simultaneous test coefficients in the joint basis.
The two-panel estimate therefore charges \(O(n^{-d/2})+O(e^{-cn})\) for any \(d\) such nodes.
The identical subset induction as in C363v2 gives \(O(n^{-s/2})+O(e^{-cn})\) for the final polarized smallness on \(s\) nodes.
The genuine Cartesian product of all \(2m\) panel laws permits the \(2^{2m}\)-fold Cauchy--Schwarz resampling, whose full difference kills every degree below \(2m\) and equals \(2^m c_zU_{m,z}\).
Thus, for kernels (3) with arbitrary past-measurable rank \(O_q(k)\) changes and lower terms of degree below \(2m\),
\[
 \Pr\{|c_z\det H_z(g)+b_z(g)|\le C_0|c_z|
                       \text{ at all }s\text{ nodes}\mid\text{past}\}
       \le C n^{-s/2^{2m+1}}+Ce^{-cn}.                    \tag{9}
\]
The constants are uniform on each compact parameter patch and all admissible histories; old-minor exceptions are charged separately.

<a id="flags"></a>
## The single-column initial flag

Keep \(Y\) fixed for the later restorations and put \(V=Y_{JI}\).
The common exterior orthogonal to the \(m\) columns of \(F(e_i)\), for every omitted site \(i\), has first channel in \(\operatorname{ran}(V)^\perp\) inside \(J\), with all other channels free on \(J\).
The two extra principal-block terms are \(VX_{IJ}\) at the top left and \(X_{JI}V^{\mathsf T}\) at the bottom left; the indicated projections kill them.
Eliminating the auxiliary pivot leaves exactly \(Q^{\mathsf T}T_wQ\), for an orthonormal frame of \(\operatorname{ran}(V)^\perp\).
Its determinant modulus equals that of the compressed partial pencil.
Every column of \(V\) therefore deletes one scalar direction, including an odd initial gap.

The [rectangular two-moment floor](Yin_C_F0351_v8.md#cross-block) and the Frobenius norm guard \(\|X\|,\|Y\|\le N^2\) give the same normal geometry as in [C362v2](Yin_C_F0362_v2.md#exterior), with \(m\) replacing three.
In particular the full normal map, and the current-site map after projection off future normals, have least singular value at least \(cN^{-2}\), outside a summable exception.
The extra \(q-1\) physical channel coefficients are controlled directly, while the first two coefficients are controlled by \(\sigma_{\min}(V)\) and \(\|Y\|\).

For clarity, the initial small-gap overlap needs no extension of a principal-trim theorem.
Use the [arbitrary-fixed-degree sparse near-vector estimate](Yin_C_F0186_v42.md#word-spread) with the real polynomial
\[
        \prod_{j=1}^d(P_q(X_{JJ},Y_{JJ})-w_j)
                        (P_q(X_{JJ},Y_{JJ})-\bar w_j).
\]
Its highest word \((x^q y)^{2d}\) has coefficient one, and the transpose has highest word \((yx^q)^{2d}\).
On the input norm guard, \(\|P_q(X_{JJ},Y_{JJ})\|\le C_qN^{2(q+1)}\).
Interpolation at the \(2d\) separated conjugate nodes gives the same polynomial lower bound for the norm of a real combination of bottom vectors as in [the cubic flag proof](Yin_C_F0362_v2.md#flag), with a larger constant exponent depending only on \(q,d\).
Choose \(D_0=12\), then a fixed \(B\) larger than those exponents and the sparse-frame scaling exponent, and then \(A>10(B+2)\).
The old-measurable largest gap \(r\le2h_n\) with \(t_r<N^{-Ah_n}t_{r+1}\), or \(r=0\), has the same initial overlap estimate after its first \(r\) fresh scalar deletions.
The joint failure bound is \(C(4h_n)^{D_0}(n/\log K_*)^{-D_0/4}+O(h_nN^{-3})\), with \(K_*=C\log^3(N+2)\), plus a summable sparse-vector exception.
The [complementary exterior-power calculation](Yin_C_F0351_v1.md#adaptive-gap) then starts the determinant comparison at
\[
 e^{-C_qh_n^3\log N}\,p_{n-2h_n}(T_w)
                          \min(1,t_{2h_n+1}(w))^{2h_n}.
\]

After that gap, each further scalar deletion has numerator \(g^{\mathsf T}R_sg\), where \(R_s\) differs from \(T_w^{-1}\) by rank at most \(s\).
The commuting scalar denominator \(1+(x^q+x)y-w\) has distinct poles in \(y\) at distinct nodes for a fixed positive \(x\).
Thus the single transpose-symmetrized resolvents at the nodes and their conjugates are independent modulo scalars.
The two-panel flag proof applies with exponent \(d/8\) for ratios below \(N^{-7}\), and with the actual raw column norm guard charged separately.
This completes all \(k\) scalar deletions.

<a id="restoration"></a>
## Restoring \(q+1\) directions at one physical site

Reveal \(Y,X_{JJ},X_{II}\), and reveal the columns \(u=X_{Ji}\) successively.
The [exact partial-pencil increment](../ledger/Yin_L_F0069_v3.md#partial) is
\[
 \Delta K_q=F(e_i)\Pi F(u)^{\mathsf T}
                       +F(u)\Pi F(e_i)^{\mathsf T},
\]
where \(\Pi\) is the fixed permutation matrix specified there.
Let \(W\) frame the incoming exterior, \(H\) the \(m\) restored orthonormal directions, and \(\widehat R=W(W^{\mathsf T}K_qW)^{-1}W^{\mathsf T}\) at a regular incoming node.
All coefficients are fixed before the current column, and unexposed columns can be set to zero because their increments vanish on the current compression.
The Schur determinant has degree at most \(2m\) in \(u\); its leading term, up to a fixed sign, is
\[
 \det(H^{\mathsf T}F(e_i))^2\det(F(u)^{\mathsf T}\widehat R F(u)).
\]
This follows by taking the quadratic Schur term and cancelling the two permutation determinants.
The normal floor bounds the first squared determinant below by \(cN^{-4m}\).
Writing \(u=N^{-1/2}g\) contributes \(N^{-m}\), so the leading scalar coefficient has modulus at least \(cN^{-5m}\).

The padded old principal pencil, with an identity on omitted channels, differs from the current pencil by rank \(O_q(k)\).
Moreover \(I-K_q\widehat R\) has rank at most the exterior codimension, also \(O_q(k)\), because its image is perpendicular to the incoming left space.
Multiplying by the padded old inverse bounds its discrepancy from \(\widehat R\) by \(O_q(k)\), without requiring invertibility of the full current pencil.
Replacing outside \(Y\) factors by their padded old blocks has the same rank cost.
Hence the quadratic entries are exactly the kernels (3) plus rank \(O_q(k)\) errors.
Applying (9) to ratios below \(N^{-(5m+4)}\) gives the claimed restoration exponent.
For \(q=3\), this uses the ratio threshold \(N^{-24}\), the coefficient floor \(cN^{-20}\), and the exponent \(d/512\).

<a id="area"></a>
## Tuple patches, chronological estimates, and the conditional limits

Use distinct filtrations for the scalar deletions and physical restorations.
A ratio is tested only at a regular incoming determinant, and a first outgoing zero after a good initial determinant counts as a bad ratio.
The finitely many exceptional spectral parameters of each sample have planar measure zero.
The initial scalar determinant and the partial-pencil exterior have identical determinant moduli, so the two comparisons join exactly.

Take \(D=2^{2m+2}\) separated upper-half-plane nodes.
On a fixed compact joint-basis patch, assign these nodes to chronological bad steps and multiply their conditional bounds in that order.
The restoration cost is \(Ck^D n^{-D/2^{2m+1}}=Ck^D n^{-2}\), and the deletion cost is smaller.
The old-minor exceptions are uniform for prescribed tuples in the patch and absorb the polynomial number of assignments; global and current-column norm guards and rectangular failures are added at their actual filtration stages.

To pass to area, first discard a narrow real strip and choose a separation so that every bad set of area at least a fixed tolerance has a set of separated \(D\)-tuples of measure at least \(b>0\), as in the [separated-tuple argument](Yin_C_F0351_v9.md#terminal).
Choose a compact subset of the nonzero-minor tuple region whose discarded ambient tuple measure is less than \(b/2\).
Such a subset exists by the exhaustion proved above; with several chosen basis charts, a finite union suffices and the largest of their finitely many constants is used.
Every relevant bad set still has at least \(b/2\) of its separated tuples in these compact patches.
Fubini therefore gives a summable probability for the positive bad-area deviation.
This argument does not infer uniform constants by extending a basis across its rank-drop locus.
The separate \(D_0\)-tuple initial-overlap estimate is already summable.
Multiplying the good ratios now proves (1).

Finally assume (2).
The normalized deterministic loss in (1) tends to zero.
On exceptional sets of vanishing area, the negative part of an ordinary monic logarithmic determinant has a uniform disk \(L^2\) bound: apply Jensen to \(\log^-|w-\lambda|\) averaged against its probability eigenvalue measure, and then integrate the uniformly bounded translated squared-logarithm kernel.
The same bound holds for the Brown potential, whose positive part is bounded on disks.
Cauchy--Schwarz therefore controls the lower deficit on the exceptional sets.
The full-size upper trim and the input norm guard control the upper deficit, since the at most \(h_N\) omitted positive logarithms contribute \(O_q(h_N\log N/N)\).
This proves the asserted almost-sure local \(L^1\) convergence and, by distributional Laplacians and total mass one, weak Brown convergence.
Subtracting the ordinary logarithm from the retained one shows that the normalized terminal negative loss tends to zero almost surely under every coupling.
If any fixed positive-deviation series for that loss diverged, the allowed independent coupling of the dimensions and the second Borel--Cantelli lemma would contradict this almost-sure conclusion.
This proves the conditional summability assertion without upgrading an unproved trim input.

## Current assessment
[Selected decision](#decision-joint-quotient-reviewed)

## Assessment history

### Decision joint-quotient-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18 |
| status | open |
| reason | Joint quotient detectors and compact parameter patches supply a candidate general restoration comparison; its complete argument awaits review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Comparison and conditional assembly](#statement) | Every fixed q under the original real two-moment laws; planar limits additionally require the precise principal trims. |
| argument | [Joint kernel argument](#kernels) | Exact polynomial kernel part, joint quotient, residue detectors, parameter patches, flags and physical restorations. |
| support | [Independent-panel extension](Yin_C_F0363_v3.md#statement) | The product law of the actual column and Cartesian resampling; the joint quotient detection is supplied here. |
| support | [Conditional planar passage](#area) | Finite compact tuple exhaustion, summable chronological estimates and the exact unresolved trim interface. |

### Decision joint-quotient-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:50 |
| status | proved |
| reason | The actual inverse, joint quotient detectors and compact tuple patches give the original-law restoration comparison at every fixed degree; the stated principal-trim limits imply the full planar conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Comparison and conditional Brown limit](#statement) | Fixed real finite-second-moment laws and arbitrary cross-dimensional coupling. |
| argument | [Complete proof](#kernels) | Polynomial inverse terms, coefficient relations, finite physical corners and the two filtrations. |
| support | [Planar assembly](#area) | The normalized summability claim under exactly the stated trim assumptions. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0371_v4.md#joint-quotient-whole-proof) | The unconditional inequality and conditional limiting statements. |

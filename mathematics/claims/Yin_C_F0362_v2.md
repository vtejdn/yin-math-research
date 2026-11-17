---
author: Yin
---

# Brown convergence for the unequal-length cubic \(1+x^2y+yx\)

<a id="statement"></a>
## The full spectrum and the ordinary determinant

Let \(X_N,Y_N\) be independent real symmetric Wigner matrices with the fixed centered laws of the [finite-variance contract](../tasks/Yin_T_F0012_v3.md#contract): the strict upper entries before \(N^{-1/2}\) scaling have variance one and the diagonal entries have finite second moments.
Let \(p=1+s_1^2s_2+s_2s_1\) for free standard semicircular elements in a finite von Neumann algebra with faithful normal tracial state \(\tau\).
Put \(P_N=I+X_N^2Y_N+Y_NX_N\), \(u(w)=\tau\log|p-w|\), and \(U_N(w)=N^{-1}\log|\det(P_N-wI)|\).
Under every coupling across dimensions, almost surely \(U_N\to u\) in \(L^1_{\mathrm{loc}}(\mathbb C)\), and the empirical eigenvalue measures of \(P_N\) converge weakly to the Brown measure of \(p\).
For \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\), ascending singular values \(s_i\), planar Lebesgue measure \(dA\), and every \(R,\epsilon>0\),
\[
 \sum_{N>h_N}\Pr\!\left\{N^{-1}\int_{|w|\le R}
       \sum_{i=1}^{h_N}\log^-s_i(P_N-wI)\,dA(w)>\epsilon\right\}<\infty .
\]
At each prescribed \(w\notin\mathbb R\), \(U_N(w)\to u(w)\) in probability and almost surely along \(N=2^j\); the full-sequence limsup at that point is \(u(w)\) almost surely under every coupling.
These assertions concern this cubic and its original real input laws.

<a id="argument"></a>
<a id="exterior"></a>
## Removing one background direction per site

For \(X=X_N,\ Y=Y_N\), use the two-coordinate matrix
\[
 K(w)=\begin{pmatrix}(1-w)I+YX&X\\XY&-I\end{pmatrix}.
\]
Its Schur complement on the first coordinate is \(P_N-wI\).
Choose \(k=2\lfloor\log^3(N+3)/2\rfloor\) deterministic sites \(I\), with complement \(J\) of size \(n=N-k\).
Write \(X_0=X_{JJ},\ Y_0=Y_{JJ},\ V=Y_{JI},\ U=X_{JI}\), \(M_0=I+X_0^2Y_0+Y_0X_0\), and \(T=M_0-wI\).
The three normals at a site \(i\in I\) are the columns of \(F_i=[(Ye_i,0),(e_i,0),(0,e_i)]\) on both sides.
The common orthogonal complement consists of \((h,l)\) with \(h_I=l_I=0\) and \(h_J\perp\operatorname{ran}V\).
Let \(Q\) be a real orthonormal frame of that last orthogonal complement in \(J\).
The extra \(JJ\) block of \(YX\) is \(VU^{\mathsf T}\), killed on the left, and that of \(XY\) is \(UV^{\mathsf T}\), killed on the right.
In the orthonormal coordinates \(h_J=Qa,\ l_J=b\) the compression is therefore
\[
 \begin{pmatrix}
 Q^{\mathsf T}((1-w)I+Y_0X_0)Q & Q^{\mathsf T}X_0\\
 X_0Y_0Q &-I_n
 \end{pmatrix}.
\]
Its absolute determinant is exactly \(|\det(Q^{\mathsf T}TQ)|\).
Thus one independent column of \(V\) removes just one direction from the scalar minor at each step, including when an odd number of directions must first be removed.

Work on \(\|X\|,\|Y\|\le N^2\), outside probability \(O(N^{-3})\) by the Frobenius second moment.
The [rectangular floor](Yin_C_F0351_v8.md#cross-block) gives \(\sigma_{\min}(V)\ge c>0\) with summable exceptional probabilities.
With \(E_I\) the inclusion of the site coordinates, the \(J\)-part of \(YE_Ia+E_Ib\) controls \(c\|a\|\); its \(I\)-part then controls \(b\) with loss \(C(1+\|Y\|)\).
The second coordinate \(E_Ic'\) controls \(c'\) exactly.
Consequently the map of all \(3k\) normal coefficients has least singular value at least \(c'N^{-2}\).
For current-site coefficients the same floor holds after projecting off all future normals, by minimizing over the coefficients at those future sites.

<a id="flag"></a>
## The scalar minor through all \(k\) deletions

Write \(h=h_n,\ t_1\le\cdots\le t_n\) for the singular values of \(T\), and \(p_j(T)\) for the product of the largest \(j\).
At regular \(T\) let \(r\) be the largest \(1\le r\le2h\) with \(t_r<N^{-Ah}t_{r+1}\), or zero if there is none.
Use \(D_0=12,\ B=40D_0+10,\ A=10(B+2)\).
For \(s\le k\) let \(Q_s\) frame the complement of the first \(s\) columns of \(V\) in \(J\).

Here is the cubic input to the [initial overlap proof](Yin_C_F0186_v42.md#initial-overlap).
On a compact region off the real axis use at most \(D_0\) separated upper-half-plane nodes \(w_j\).
The polynomial \(\prod_{j=1}^d(M_0-w_j)(M_0-\bar w_j)\) is real of degree \(6d\); the top word \((x^2y)^{2d}\) has coefficient one.
For the transpose the top word is \((yx^2)^{2d}\).
Hence the [sparse near-vector estimate for arbitrary fixed degree](Yin_C_F0186_v42.md#word-spread) applies on either side with \(K_*=C\log^3(N+2)\).
On the norm guard \(\|M_0\|\le N^7\), so each bottom vector at a selected gap has residual at most \((N^7+R)N^{-Ah}\).
Real linear combinations of their real parts at \(d\) nodes have unnormalized lower norm \(cN^{-7(2d-1)}\) for unit coefficients, by interpolation of degree \(2d-1\) on the \(2d\) conjugate nodes as in the cited proof.
After normalization their residual for the displayed real polynomial is \(o(1)\), since \(h\to\infty\).
Deleting \(cn/\log K_*\) entries thus leaves least singular value at least \(cN^{-7(2d-1)}K_*^{-C}\) for the real-part frame.
The disjoint bases, after rescaling by \(N^{B-1}\), give joint small-ball probability \(C(n/\log K_*)^{-d/2}\) for the scalar products with one fresh raw column at width \(N^{-B}\).
The same conclusion holds for the left frame with conjugate nodes.

At each of the first \(r\) stages test a unit bottom-frame direction orthogonal to the previously projected columns.
Successful scalar tests give raw projected volume at least \(N^{-Br}\); division by the unprojected raw volume, at most \(N^{2r}\) on the column norm guards, gives an orthonormal overlap determinant at least \(N^{-(B+2)r}\) on each side.
The adaptive \(r\) and these frames are determined before the relevant fresh draw, and the two sides can use the identical draw.
Assigning \(D_0\) failing nodes to sides and stages and testing the more frequent side at each stage gives probability at most \(C(4h)^{D_0}(n/\log K_*)^{-D_0/4}+O(hN^{-3})\), including the old sparse-vector exceptions with exponent greater than four.
This is summable, uniformly over the separated tuples.
For one node the corresponding error is \(O(h\sqrt{\log K_*/n}+hN^{-3})\).

By the [complementary exterior-power calculation](Yin_C_F0351_v1.md#adaptive-gap), the leading determinant contribution to the \(r\)-th compression has modulus at least \(p_{n-r}(T)N^{-2(B+2)r}\), and the remaining coefficient has modulus at most \(p_{n-r}(T)N^{-Ah}\).
For \(r=0\) one starts with the full old determinant.
Beyond \(r\) the adjacent gap ratios through \(2h\) give
\[
 |\det(Q_r^{\mathsf T}TQ_r)|\ \ge\
 e^{-C h^3\log N}\,p_{n-2h}(T)\min(1,t_{2h+1})^{2h}.
\]
No parity condition on \(r\) is involved.

At every subsequent deletion with regular incoming compression set \(R_s=Q_s(Q_s^{\mathsf T}TQ_s)^{-1}Q_s^{\mathsf T}\).
For the next raw column \(g=\sqrt N V_{:,s+1}\) the modulus of the ratio is \(|g^{\mathsf T}R_sg|/\|Q_s^{\mathsf T}g\|^2\), by the complementary cofactor formula.
One has \(\operatorname{rank}(R_s-T^{-1})\le s\) because \(\operatorname{ran}(I-TR_s)\) is orthogonal to the range of \(Q_s\).
The two-panel test uses \(R_s+R_s^{\mathsf T}\).
For the original resolvent, its scalar specialization is \(2/(1+x^2y+xy-w)\), with independent directions modulo scalars across distinct nodes and their conjugates by the simple poles in \(y\) at generic fixed \(x\).
The [physical-corner transfer](Yin_C_F0363_v1.md#corners) applies to this fixed kernel and its \(O(k)\)-rank change.
Therefore the [two-panel cofactor estimate](Yin_C_F0351_v9.md#flags) bounds simultaneous ratios below \(N^{-7}\) at \(d\) assigned nodes by \(O(n^{-d/8})\) plus exponentially small errors on the old-minor guards.
In this test \(\|g\|\le N^2\) makes the raw numerator at most \(N^{-3}\); pay the \(O(kN^{-3})\) upper-norm failure separately.
The rectangular floor controls dimension throughout the flag and is charged separately, without conditioning on future columns.

<a id="restoration"></a>
## Restoring three directions with one fresh row

Reveal \(Y,X_0,X_{II}\), then reveal the columns \(u=X_{Ji}\), padded by zero outside \(J\), successively for \(i\in I\).
Let \(W\) be a real orthonormal frame perpendicular to the remaining site normals, including the current \(F=F_i\), and let \(H\) add the three orthonormal directions which appear when \(F\) is restored.
All other unrevealed columns may be set to zero, since their perturbations vanish on compression.
For the current column the exact change from \(X\mapsto X+e_i u^{\mathsf T}+u e_i^{\mathsf T}\) is
\[
 \Delta K=F G_R^{\mathsf T}+G_LF^{\mathsf T},\quad
 G_R=[(u,0),(0,u),(Yu,0)],\qquad
 G_L=[(0,u),(Yu,0),(u,0)] .
\]
At a regular incoming matrix \(\widehat R=W(W^{\mathsf T}KW)^{-1}W^{\mathsf T}\) is independent of this \(u\) conditionally on the past.
In the completed frame \([W,H]\) the Schur ratio is a three-dimensional determinant, each entry of degree at most two in \(u\).
Its homogeneous term of degree six is
\[
 -\det(H^{\mathsf T}F)^2\det(G_R^{\mathsf T}\widehat R G_L).
\]
Indeed the new corner is affine and the quadratic part of the Schur complement is \(-(H^{\mathsf T}F)G_R^{\mathsf T}\widehat R G_L(F^{\mathsf T}H)\).
The earlier normal floor gives \(|\det(H^{\mathsf T}F)|^2\ge cN^{-12}\), since \(F\) is perpendicular to the old space and its projection off the future spans lies in \(\operatorname{ran}H\).
Using raw coordinates for \(u\) costs another \(N^{-3}\) in that degree.

To identify the kernels, permute the columns of \(G_R\) and \(G_L\) separately to the same ordering \(O=[(u,0),(0,u),(Yu,0)]\).
This changes at most the sign of the determinant.
Writing \(R=T^{-1}\), the inverse on the unperturbed \(J\) sites is
\[
 K_0^{-1}=\begin{pmatrix}R&RX_0\\X_0Y_0R&X_0Y_0RX_0-I\end{pmatrix}.
\]
The direct sum of \(K_0\) and an identity on the two \(I\) copies differs from \(K\) by rank \(O(k)\), by replacing the two inputs with their zero-padded \(J\) blocks in each product.
As \(\operatorname{ran}(I-K\widehat R)\perp\operatorname{ran}W\), this residual has rank at most \(3k\); multiplication by the padded inverse gives the same \(O(k)\) bound for its discrepancy from \(\widehat R\).
Replacing the outside \(Y\) factors in \(O\) by the padded \(Y_0\) again has rank cost \(O(k)\).
Thus the quadratic entries of \(O^{\mathsf T}\widehat R O\) in the \(J\)-site column have kernels, up to \(O(k)\) rank,
\[
 \operatorname{sym}(L_a R D_b)-{\bf1}_{a=b=2}I,\qquad
 (L_1,L_2,L_3)=(I,X_0Y_0,Y_0),\quad (D_1,D_2,D_3)=(I,X_0,Y_0),
\]
where \(\operatorname{sym}\) uses transpose without conjugating \(w\).

At \(d\) separated assigned nodes compare ratios of modulus below \(N^{-20}\).
Six Cartesian differences over disjoint site classes kill all lower-degree terms of the ratios.
After division by the normal factors and \(N^{-3}\), their mixed raw targets are \(O(N^{-5})\).
The [six-panel determinant estimate for these nine kernels](Yin_C_F0363_v1.md#statement) bounds the joint event by \(C_dn^{-d/128}\) plus exponentially small errors on the old-minor guards.
Only the fresh strict upper coordinates from the current \(X\) row enter this test.
The normal floor here depends on \(Y\), already revealed; corner exceptions for the old principal inputs are charged separately.

<a id="terminal"></a>
## Area estimates, the potential, and prescribed nodes

Use one filtration for the scalar deletions and another for the physical restorations.
At each assigned step count a bad ratio only when the incoming determinant is nonzero; a first outgoing zero after a good initial comparison is counted.
An irregular incoming matrix therefore requires no conditional inverse test.
Apart from the finitely many poles of \(T^{-1}\) per sample, which have zero planar area, all three determinant comparisons now join at exactly equal moduli.
In each filtration assign \(D=256\) separated upper-half-plane nodes to bad steps and condition in chronological order, testing a deletion only after its old-measurable \(r\).
For the restoration event this costs at most \(C_D k^D n^{-D/128}\) plus summable guard probabilities, and for the deletions the exponent is \(D/8\).
Old-minor corner guards for assigned subsets can be imposed before these tests; the exponentially small exceptions for a fixed tuple absorb all step assignments.
The global norm and rectangular guards are included by union bounds at their actual filtration stages.
The [separated-tuple area argument](Yin_C_F0351_v9.md#terminal) applies to each filtration and to the separate \(D_0\)-tuple initial failures: excise a real strip of arbitrarily small area, reflect into the upper half-plane and choose the separation so that every bad set of area above tolerance has a uniformly positive product area of separated tuples.
Fubini gives a summable probability of exceeding any fixed positive exceptional area on a disk.
Outside the resulting bad sets the full determinant satisfies
\[
 |\det(P_N-wI)|\ge e^{-C_R(h^3+k)\log N}\,
       p_{n-2h}(T)\min(1,t_{2h+1})^{2h}.                 \tag{1}
\]

By [the cubic trim theorem](Yin_C_F0362_v1.md#statement), the normalized retained log on the right converges in disk \(L^1\) to \(u\), and its normalized adjacent negative loss tends to zero there, almost surely in any permitted coupling.
The deterministic exponential loss in (1) is \(o(N)\) in the logarithm.
The negative parts of \(U_N\) and \(u\) have bounded disk \(L^2\) norm by Jensen applied to the translated \(\log^-\) kernel against probability measures, while \(u\) is bounded above there.
Thus Cauchy--Schwarz controls the lower deficit \((u-U_N)_+\) on exceptional sets of asymptotically zero area.
The full-size upper trim and the \(O(h_N\log N/N)\) positive logarithms possibly omitted from it bound \((U_N-u)_+\) in disk integral.
These estimates prove local \(L^1\) convergence almost surely.
Taking distributional Laplacians yields vague convergence, hence weak convergence since the limiting Brown measure is a probability measure.
The [terminal equivalence](Yin_C_F0362_v1.md#trim), using the allowed independent coupling across dimensions for necessity, gives the series in the statement.

For each compact nonreal region the one-node failure probability for (1) is \(O(h\sqrt{\log K_*/n}+k n^{-1/128}+kN^{-3})\) plus the summable norm, rectangular and old-minor probabilities.
The argument gives this estimate initially for planar almost every fixed node by Fubini.
Both sides of (1), including at singular nodes, are continuous in \(w\).
Approach any prescribed \(w\notin\mathbb R\) from the full-area set in a compact nonreal neighborhood and apply Fatou to the strict violation to obtain the same bound there.
The bound vanishes with \(N\) and is summable on \(N=2^j\).
The finite-variance cubic trim and its adjacent estimate at this node in both sizes now imply the pointwise lower bound in probability and almost surely on the dyadic subsequence.
The full-size trim gives the almost-sure upper bound on the full sequence, proving all the stated pointwise conclusions.

## Current assessment
[Selected decision](#decision-cubic-terminal-reviewed)

## Assessment history

### Decision cubic-terminal-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:28 |
| status | open |
| reason | The exact scalar exterior and the three-direction row test give a candidate proof of the full cubic terminal comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unequal-length cubic](#statement) | Ordinary potentials, eigenvalue measures, the terminal series and prescribed nonreal parameters. |
| argument | [Scalar exterior and determinant comparison](#argument) | Initial deletion, physical restoration and the probabilistic transfer. |
| support | [Physical restoration](#restoration) | Exact normal maps, Schur determinant and projected kernels. |
| support | [Terminal estimates](#terminal) | Area probabilities, comparison with the two trims and prescribed parameters. |
| dependency | [Cubic principal trims](Yin_C_F0362_v1.md#statement) | Two effective trim sizes and their adjacent loss under the original real laws. |
| dependency | [Six-panel estimate](Yin_C_F0363_v1.md#statement) | The original-law conditional determinant test for the nine displayed kernels. |

### Decision cubic-terminal-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:40 |
| status | proved |
| reason | Exposing X after fixing Y converts the initial exterior to a single scalar flag, and the three-direction Schur restoration controls the full cubic determinant. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unequal-length cubic](#statement) | Two real Wigner input laws with finite second moments and arbitrary cross-size coupling. |
| argument | [Complete proof](#argument) | Exact initial compression, terminal comparison and its probabilistic consequences. |
| support | [Limits and summability](#terminal) | Planar ordinary logarithms, terminal series and prescribed nonreal shifts. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0370_v2.md#cubic-terminal-whole-proof) | The three-direction input has its separate complete review. |

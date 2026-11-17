---
author: Yin
---

# Atomic tests for the two compression steps of the real quadratic Wigner model

This draft treats strictly atomic raw laws in the [terminal comparison](../tasks/Yin_T_F0012_v3.md#contract) for \(M=AB+2BA\).
The [Gaussian-flag calculation](../claims/Yin_C_F0351_v1.md#later-hyperplanes) involves quadratic forms of a fresh border in the transpose-symmetric part of a resolvent.
The [interior determinant](../claims/Yin_C_F0186_v33.md#argument) has a different source of randomness, consisting of the fresh upper entries of a symmetric principal block.
The tests below use these two actual interfaces.

<a id="squarefree"></a>
## A surviving coefficient for a discrete interior

Choose an interior of size \(k\) divisible by ten, which is compatible with even \(k\asymp\log^3 N\).
Let \(U=U^{\mathsf T}\) denote its normalized \(k\)-by-\(k\) real upper-entry matrix with scale \(N^{-1/2}\).
For any \(2k\)-by-\(2k\) complex matrix \(W\) fixed independently of these interior variables put \(f=\det(\operatorname{diag}(U,U)-W)\).
The same argument applies to each parameter at which the conditioned exterior target is defined.

Partition the \(k\) sites into five-element sets and let \(\mathcal E\) be the union of the ten edges of the complete graph inside each set.
There are \(2k\) different edges in \(\mathcal E\).
The coefficient of the squarefree monomial \(\prod_{e\in\mathcal E}\xi_e\) in the raw variables is
\[
 c_{k,N}=48^{k/5}N^{-k}.
\]
Indeed only the top homogeneous part \((\det U)^2\) can contribute.
Inside each five-site block each determinant must use a directed Hamiltonian cycle: a fixed point uses a diagonal variable and a transposition repeats an edge, both excluded by the chosen monomial.
The complement of an undirected five-cycle in the complete graph on five vertices is another five-cycle.
There are twelve choices for the first undirected cycle, two orientations for each of the two cycles, and both permutations have positive sign.
Different five-site blocks multiply, and \(2k\) entries at scale \(N^{-1/2}\) give the stated normalization.

The calculation remains valid after fixing every raw coordinate outside \(\mathcal E\).
For iid signs on \(\mathcal E\), the Walsh coefficient \(\mathbb E[f\prod_{e\in\mathcal E}\xi_e]\) equals \(c_{k,N}\): a monomial contributing to it must have odd exponent at every one of the \(2k\) positions while having total degree at most \(2k\).
Thus its conditional second moment is at least \(c_{k,N}^2\), and at least one sign assignment satisfies \(|f|\ge c_{k,N}\).
The conditional probability of this last event is at least \(2^{-2k}\).

More generally, suppose the iid raw law has two atoms \(a\ne b\), each of mass at least \(p>0\).
The successive two-point differences in all \(2k\) variables annihilate every monomial except the displayed one and give \(c_{k,N}(b-a)^{2k}\).
Consequently at least one assignment from \(\{a,b\}^{2k}\) satisfies
\[
 |f|\ge |c_{k,N}|(|b-a|/2)^{2k},
 \qquad\Pr\{\text{that assignment}\mid\text{exposed coordinates}\}\ge p^{2k}.
\]
This excludes identical discrete cancellation for the entire interior.
The monic quartic coefficients of the earlier perfect-matching argument can alias lower powers on a two-point support.

Several edge-disjoint top-coefficient test sets can improve such a fiber bound without attaining the required high probability.
For signs, the surviving coefficients from distinct edge sets are orthogonal in the conditional or unconditional second moment when the entries of their union are left independent.
A second moment lower bound alone gives no high-probability determinant lower bound.
In particular, success in one fiber may depend on the coordinates of all other chosen fibers through the value of \(f\).
Conditional lower bounds on each coordinate block cannot be multiplied into independent-trial amplification: the even-parity event on independent bits has conditional probability \(1/2\) on every one-bit fiber and unconditional probability \(1/2\), irrespective of the number of fibers.
The witness probability above tends to zero at the polylogarithmic block sizes, leaving the unconditioned summability obligation.

<a id="dense-intertwiner"></a>
## What exact physical-basis diagonal resolvents imply

Let \(A,B\) be deterministic real symmetric \(n\)-by-\(n\) matrices, with every strict off-diagonal entry of \(B\) nonzero.
Write \(X=AB\), \(M=X+2X^{\mathsf T}\) and \(\operatorname{sym}T=(T+T^{\mathsf T})/2\).
Assume that \(\operatorname{sym}((M-zI)^{-1})\) is diagonal in the physical basis throughout a nonempty open set of regular parameters.
Then either all eigenvalues of \(M\) are real, or for one \(c\in\mathbb R\),
\[
 \operatorname{spec}M\subset\mathbb R\ \cup\ (c+i\mathbb R).
\]

By the identity theorem for rational functions each off-diagonal entry vanishes identically.
Expansion at infinity shows that the symmetric parts of \(M,M^2,M^3\) are diagonal.
Set \(D=\operatorname{sym}M\) and \(K=M-D\), so \(D\) is real diagonal and \(K\) is real skew-symmetric.
The identities \(\operatorname{sym}(M^2)=D^2+K^2\) and \(\operatorname{sym}(M^3)=D^3+DK^2+K^2D+KDK\) give diagonal \(K^2\) and \(KDK\).
As \(K^2\le0\), on its distinct coordinate eigenspaces \(K^2=-\lambda I\) for \(\lambda\ge0\).
These spaces are invariant under \(D,K\), and on the zero block \(K=0\).
On each positive block put \(D'=K D K^{-1}=-(KDK)/\lambda\).
This is diagonal there, and conjugation by \(K\) exchanges \(D,D'\) because \(K^2\) is scalar.
Thus \(K\) exchanges the coordinate spaces with joint eigenvalue pairs \((a,b)\) and \((b,a)\) of \((D,D')\).

Group these spaces by the unordered pair \(\{a,b\}\) at fixed \(\lambda\), keeping any repetitions within one group.
On each resulting coordinate group \(DK+KD=(a+b)K\), \(D^2-(a+b)D+abI=0\), and \(K^2=-\lambda I\).
It follows that \(X=(2M^{\mathsf T}-M)/3=D/3-K\) and \(M=D+K\) have respective annihilating polynomials
\[
 t^2-\tfrac{a+b}{3}t+ab/9+\lambda,\qquad
 t^2-(a+b)t+ab+\lambda .
\]
On the zero block use groups with a common value of \(D\), where \(X,M\) are scalars.
The full matrices \(X,M\) are direct sums over all these coordinate groups.

Since \(BX=X^{\mathsf T}B\), its restriction between every pair of distinct groups is a nonzero intertwiner: the corresponding rectangular submatrix of \(B\) consists of nonzero entries.
A nonzero intertwiner implies common spectrum, by the primary decomposition or the Sylvester equation.
If a group has nonreal spectrum for \(M\), then \((a-b)^2<4\lambda\), so the annihilating quadratic for \(X\) has negative discriminant also.
As \(X\) is real on this nonempty coordinate group, its spectrum equals the conjugate pair of roots.
Every other group must then have that same conjugate pair for \(X\), since its spectrum is real-conjugation invariant and has at most two distinct points.
In particular there is no scalar group and every group has the same \(a+b\), equal to three times the sum of these two common roots.
All its nonreal \(M\) eigenvalues therefore have the same real part \((a+b)/2\), proving the claim also when there is just one group.

For sign borders, exact diagonality makes the quadratic form in the raw Rademacher column equal to the trace.
An unrestricted real matrix can have this property and the full roots of unity as eigenvalues, by using the real two-dimensional blocks of a cyclic orthogonal transformation.
The spectrum restriction excludes this circular cancellation configuration for the first uncompressed product with dense \(B\), allowing the matrix sizes to grow.
It does not pass through an arbitrary principal compression, which need not retain this product or the intertwiner, and gives no bound for an approximate cancellation over a disk.

<a id="original-law-at-infinity"></a>
## An unconditional coefficient estimate from the original Wigner entries

For any two centered real nondegenerate upper Wigner laws in the fixed two-color model, the original matrix \(\operatorname{sym}M\) has at least \(c n\) pairwise vertex-disjoint off-diagonal coefficients of magnitude at least \(c'/n\), outside probability \(C e^{-c''n}\).
Here the physical size and normalization are \(n,n^{-1/2}\), and constants depend only on the laws.
The same first-minor estimate uses \(c'/N\) with global \(N^{-1/2}\) scaling when \(n=N-o(N)\).

Choose a site \(\ell\) and a deterministic matching \((i_j,j_j)\) among the other sites having size \(\lfloor(n-1)/2\rfloor\).
Some fixed \(\kappa,p>0\) satisfy \(\Pr(|\sqrt n\,B_{i_j\ell}|\ge\kappa)\ge p\).
Independence gives a fixed positive proportion of such good indices except with exponentially small probability.
Condition on \(B\) and on all of \(A\) except the independent upper variables at the pairs \(\{\ell,j_j\}\).
Then the entries of \((3/2)(AB+BA)=\operatorname{sym}M\) at the chosen matching are constants plus \((3/2)B_{i_j\ell} A_{\ell j_j}\).
Indeed no tested row \(i_j\) is among the remaining row or column indices of \(A\), and only the \(\ell\)-term is fresh in column \(j_j\).
Nondegeneracy of the raw \(A\) law gives a fixed interval radius \(s>0\) such that the supremal interval mass at this radius is strictly below one.
For each good index the probability that the output lies outside a centered interval of radius \((3/2)\kappa s/n\) is therefore bounded below uniformly in its shift.
The remaining tests are conditionally independent.
A second Bernoulli lower-tail bound gives the claimed matching.

This excludes exact diagonal sign-cancellation through the first nontrivial Laurent coefficient of the original minor, with an unconditional exponential exceptional probability.
It does not transfer the matching at infinity to quantitative quadratic small-ball at a fixed nonreal spectral parameter or to the subsequent compressed minors.
The [multishift sign-flag estimate](../claims/Yin_C_F0351_v5.md#sign-flag-area) obtains fixed-shift physical corner spread from the full law of the minor and controls exceptional areas throughout the flag.

The [paired restoration estimate](../claims/Yin_C_F0351_v5.md#paired-sign-restoration) completes the terminal comparison when both matrices have sign diagonals and strict upper entries.

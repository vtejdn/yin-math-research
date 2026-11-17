---
author: Yin
---

# Uniform shrinking singular-value counts and fixed-shift trimmed logarithms

<a id="statement"></a>
## Uniformity in the constant coefficient

Let \(m,g\ge1\) and \(A_1,\ldots,A_g\in M_m(\mathbb C)\) be fixed.
Let \(K\subset M_m(\mathbb C)\) be a nonempty compact semialgebraic set in real and imaginary coordinates.
Evaluate \(L_b=b+\sum_j A_j x_j\) at free standard semicircular elements \(s_j\) and at the [fixed-law independent Hermitian Wigner matrices](../tasks/Yin_T_F0013_v1.md#input-model), with finite third absolute off-diagonal moments and finite second diagonal moments.
Write \(\nu_b\) and \(\nu_{n,b}\) for the free and empirical singular-value probability laws, using normalized traces of auxiliary size \(m\) and total size \(mn\), respectively.
Assume \(\nu_b(\{0\})=0\) for every \(b\in K\).
The constants below may depend on \(K\), all fixed variable coefficients and the entry laws.

There exist \(C<\infty,\ 0<\beta\le1\) such that, for \(0<t\le1\),
\[
 \sup_{b\in K}\nu_b([0,t])\le Ct^\beta,\qquad
 \sup_{b\in K}\mathbb E\nu_{n,b}([0,t])
 \le C\big(t^\beta+n^{-1/2}t^{-3}+n^{-1}t^{-6}\big).
 \tag{1}
\]
Fix \(0<\gamma<1/(6+2\beta)\).
There is \(C'<\infty\) such that, with summable exceptional probabilities in \(n\), simultaneously for \(b\in K\) and \(n^{-\gamma}\le t\le1\),
\[
 \nu_{n,b}([0,t])\le C't^\beta .
 \tag{2}
\]
For \(a>0\) write \(v_{n,a}(b)=\int\log\max(s,a)\,d\nu_{n,b}(s)\) and \(u(b)=\int\log s\,d\nu_b(s)\).
Then \(u\) is finite and continuous on \(K\) and
\[
 \sup_{b\in K}|v_{n,n^{-\gamma}}(b)-u(b)|\to0
 \quad\text{almost surely under every cross-size coupling}.
 \tag{3}
\]

<a id="scalar-shifts"></a>
For every fixed nonconstant scalar polynomial \(P\) in selfadjoint variables, (1)--(3) hold for the singular laws of \(P(W^{(n)})-zI\) and \(P(s)-z\), uniformly over any compact set of shifts \(z\in\mathbb C\), with constants allowed to depend on that set and \(P\).
This includes the shift \(P(0)\).
The cutoff in (3) retains the bottom logarithmic loss as a separate obligation for the [ordinary determinant question](../tasks/Yin_T_F0014_v1.md#contract).

<a id="argument"></a>
## The free resolvent on a semialgebraic family

Let \(B_0(b)=\left(\begin{smallmatrix}0&b\\b^*&0\end{smallmatrix}\right)\) and \(B_j=\left(\begin{smallmatrix}0&A_j\\A_j^*&0\end{smallmatrix}\right)\).
Their free Hermitization \(H_b=B_0(b)+\sum B_js_j\) has a symmetric spectral law supported on the two signed copies of \(\nu_b\).
For \(\eta>0\), the [affine Dyson equation and its pointwise uniqueness proof](Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness) identify the matrix expectation \(G\) of \((i\eta-H_b)^{-1}\) as the unique solution with \(-\operatorname{Im}G>0\) to
\[
 (i\eta I-B_0(b)-\textstyle\sum_j B_jGB_j)G=I .
\]
This system and the positive-definiteness test by principal minors are polynomial equalities and strict inequalities in real and imaginary matrix coordinates.
In particular the graph of
\[
 f(b,\eta)=-\eta\,\operatorname{Im}\operatorname{tr}_{2m} G
        =\int\frac{\eta^2}{s^2+\eta^2}\,d\nu_b(s)
\]
is semialgebraic by projection.
Here and below the projection and quantifier-elimination input is [Coste, An Introduction to Semialgebraic Geometry, Theorem 2.6, printed p. 28](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf).
This is used for real polynomial formulas with their fixed real coefficients.

At each fixed \(\eta>0\), \(f\) is continuous in \(b\) by the ordinary norm-resolvent identity.
For each \(b\) the displayed integral decreases to zero as \(\eta\downarrow0\), by the no-atom assumption.
The convergence is uniform on \(K\): given a tolerance, each point has a neighborhood where \(f\) at some positive scale is below that tolerance, and a finite cover and monotonicity give one common scale.
The maximum \(h(\eta)=\max_{b\in K}f(b,\eta)\) for \(0<\eta\le1\) has semialgebraic graph by the same theorem, since existence of a maximizer and the universal upper bound are first-order conditions.
Moreover \(h>0\) and \(h(\eta)\to0\).

Take a quantifier-free Boolean description of the graph by signs of finitely many nonzero real polynomials in \(\eta,y\), removing identically constant tests.
Some defining polynomial vanishes at each graph point with \(0<\eta<1\), because otherwise all signs persist on a neighborhood, whereas the graph has empty interior.
Their nonzero product \(Q\) vanishes on the graph.
Divide out its largest common power of \(\eta\) so that \(Q(0,y)\) is a nonzero polynomial.
The limit \(h(\eta)\to0\) forces \(Q(0,0)=0\).
Write \(Q(0,y)=y^r g(y)\) with \(r\ge1,\ g(0)\ne0\).
On a fixed neighborhood of zero,
\[
 c h(\eta)^r\le |Q(0,h(\eta))|
      =|Q(0,h(\eta))-Q(\eta,h(\eta))|\le C\eta .
\]
Thus \(h(t)\le C't^{1/r}\) on \((0,1]\), enlarging the constant away from zero.
Since \(\nu_b([0,t])\le2 f(b,t)\), this gives the first part of (1) with \(\beta=1/r\).
It also makes the free error from clipping below \(d\in(0,1)\) uniformly at most \(Cd^\beta/\beta\).
Fixed-\(d\) free integrals are continuous by norm continuity and continuous functional calculus on the common bounded spectral interval, so \(u\) is finite and continuous.

<a id="finite-count"></a>
## Comparison, nets and the moving cutoff

The [Wigner-to-GOE comparison](Yin_C_F0195_v1.md#statement) is uniform in \(B_0(b)\) by its derivative bound with arbitrary deterministic Hermitian background.
The [GOE estimate](../audits/literature/Sch05/Yin_U001.md#goe-hermitization-specialization) keeps its random coefficients fixed, sets the source drift to zero, and evaluates at \(itI-B_0(b)\) with norm bounded uniformly over \(K,\ 0<t\le1\).
Multiplying these comparisons by \(t\) as in the [fixed-pencil count proof](Yin_C_F0195_v1.md#count-proof) proves (1).
For \(t\ge n^{-\gamma}\) its two error terms are \(O(t^\beta)\).

Take an \(n^{-\gamma}\)-net in \(K\) in matrix operator norm, with centers in \(K\) and cardinality \(O_K(n^{2m^2\gamma})\), by a Euclidean packing in fixed dimension.
Take dyadic thresholds \(2^j n^{-\gamma}\) through at least four.
At each center and threshold \(t\in[n^{-\gamma},1]\) the normalized singular count is within \(t^\beta\) of its expectation except with probability \(2e^{-cn t^{2\beta}}\), by the [bounded-rank upper-row concentration inequality](Yin_C_F0186_v4.md#row-concentration) applied to the Hermitian dilation and the interval \([-t,t]\).
A change of one row group has rank bounded solely by the fixed sizes.
For thresholds above one the bound \(\nu_{n,b}([0,t])\le t^\beta\) is automatic.
The union bound is summable since \(1-2\gamma\beta>0\).
For every \(b,t\) in (2), shift to a net center by the ordered singular-value norm perturbation bound and enlarge \(t+n^{-\gamma}\) to the next dyadic threshold at most \(4t\).
This proves (2) including the exact smallest permitted threshold.

For fixed \(0<d\le1\), the normalized log clipped at \(d\) converges almost surely pointwise by the [finite-variance weak law](Yin_C_F0186_v4.md#finite-variance-weak) and [positive logarithmic tails](Yin_C_F0186_v4.md#log-statistics).
Both the ordered singular-value perturbation and the scalar log clipped at \(d\) give a Lipschitz constant \(1/d\) for the finite-matrix statistic as a function of \(b\).
Finite nets, or a fixed countable dense set and this Lipschitz bound, give uniform convergence on \(K\) on one event for a countable sequence of fixed \(d\)'s decreasing to zero.
By (2), eventually on this event the difference between the clips at \(n^{-\gamma}\) and \(d\) is uniformly bounded by \(\int_{n^{-\gamma}}^d C't^{\beta-1}\,dt\) whenever \(n^{-\gamma}<d\).
Together with the corresponding free clipping estimate this proves (3).

<a id="word-chain"></a>
## All shifts of a scalar polynomial

Enclose the given compact shift set in a closed disk.
The [word-chain linearization](../ledger/Yin_L_F0061_v2.md#linearization-transfer) for \(P-z\) has a fixed auxiliary block with polynomial inverse and drift depending real-affinely on \(z\), so the image of the disk is compact semialgebraic.
For every \(z\), \((P-z)^*(P-z)\) has nonzero homogeneous top term \(P_D^*P_D\), where \(D\ge1\) is the degree.
Indeed at top degree the coefficient of a word \(w^*w\), for a length-\(D\) word with coefficient \(c_w\ne0\), is \(|c_w|^2\) because the fixed-length split is unique.
The [SS15 scalar atomlessness statement](../audits/literature/SS15/Yin_U001.md#ss15-u001) therefore gives zero kernel for \(P(s)-z\).
The invertible triangular pivot and the Schur equations identify the kernel of the full free pencil with the graph over that scalar kernel.
Hence all drifts in this disk satisfy the no-atom hypothesis.

The [singular count graph inequality](Yin_C_F0195_v1.md#polynomial-transfer) transfers the normalized empirical count to the scalar polynomial with a factor equal to the fixed auxiliary size, at all thresholds, including exact zeros.
This gives (1)'s finite bound and (2).
For the scalar free count, take a fixed \(z,t\), use weak convergence of the expected scalar singular laws and the open interval \([0,t+\epsilon)\) relative to \([0,\infty)\), and then let \(\epsilon\downarrow0\).
Bound the larger threshold by (1) and take the upper limit in \(n\) first, using the trivial bound for \(t=1\) if necessary.
The same resulting constants work throughout the disk.
The fixed-\(d\) net argument now applies directly to the scalar singular values since \(z\) shifts by a scalar identity.
The clipping error from (2) proves the scalar form of (3).

<a id="fixed-shift-trim"></a>
## The real quadratic companion at prescribed shifts

For the [real fourth off-diagonal and second diagonal moment model](Yin_C_F0186_v36.md#statement), write \(P_N=A_NB_N+2B_NA_N\), \(P=s_1s_2+2s_2s_1\) and \(u(z)=\tau\log|P-z|\).
Let \(z_N\to z\) be any deterministic sequence with \(\operatorname{Im}z\ne0\).
For \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\), the physical and scalar trimmed logs obey, on a probability-one event for this sequence and every allowed coupling,
\[
 N^{-1}\log p_{3N-q_N}(L_N(z_N))\to u(z),\qquad
 N^{-1}\log p_{N-q_N}(P_N-z_N I)\to u(z).
 \tag{4}
\]
Here \(p_j\) is the product of the largest \(j\) singular values and \(L_N\) is the three-channel companion of C186v36.
On each fixed compact neighborhood separated from \(\mathbb R\), the same holds for a sufficiently large coefficient in \(q_N=\lceil C_K\log(N+3)\rceil\).
In particular one can prescribe \(z_N=z\) at every nonreal \(z\).

Use the [initial dimensions and scaling](Yin_C_F0186_v36.md#initial-product) with \(m_N=\lfloor N/\log^3(N+3)\rfloor,\ n=N-m_N,\ t=(n/N)^{1/2}\), initial deficit \(q_0=3m_N+q_N\) and rank \(r_0=3n-q_0\).
The canonical initial pencil has parameter \(w_N=z_N/t^2\to z\).
Choose a closed rectangle around \(z\) disjoint from the real axis containing these parameters eventually.
Its image in the constant coefficients of the companion is compact semialgebraic.
The same Schur kernel argument as above gives zero kernel for every such free companion.
Apply (2)--(3) on the canonical minors, using the bounded-multiplicity subsequence argument of C186v36 to handle the repeated values of \(n\).
Eventually the count at \(n^{-\gamma}\) is \(O(n^{1-\gamma\beta})=o(q_0)\) and the normalized clipped log sum at \(w_N\) tends to \(u(z)/3\), by the free Schur determinant identity and continuity.
The top \(r_0\) terms retain their genuine logarithms.
The omitted positive log sum is \(o(n)\), using the [positive-tail control](Yin_C_F0186_v4.md#log-statistics) at one fixed drift, the bounded drift perturbations and \(q_0/n\to0\).
The two constant invertible scaling matrices change each retained singular value by a factor in \([t^2,1]\).
This gives the same physical initial lower limit \(u(z)\) as in C186v36, now with final parameter \(z_N\).

For the rest of the chain the [actual projected border and rank estimates](Yin_C_F0186_v36.md#rank-loss) apply at each deterministic \(z_N\) with common constants in the rectangle.
The [propagation proof](Yin_C_F0186_v36.md#final-product) yields the lower bound in (4) with total logarithmic cost \(O(m_N\log N)=o(N)\).
For the upper bound, use the full normalized companion sum clipped at a fixed \(d\in(0,1)\), allowing \(q_N|\log d|/N\) extra for the removed terms.
Its limit is three times the normalized free companion integral clipped at \(d\), by the fixed-\(d\) net argument.
Let \(d\downarrow0\).

To transfer the result at possible exact finite eigenvalues, use the determinant-one left and right triangular factors in [C186v36](Yin_C_F0186_v36.md#final-product).
For either factor \(F\) of total size \(D=3N\), one has \(\|\bigwedge^{D-q}F\|=\|\bigwedge^q F^{-1}\|\) by the singular-value product formula and \(|\det F|=1\).
Each factor and its inverse has norm \(O(N^C)\) eventually almost surely by the same Frobenius estimate used there.
Exterior submultiplicativity applied to the factorization and its reverse compares the two retained products of size \(3N-q_N\) within factors \(\exp(O(q_N\log N))\), without dividing by a possibly vanishing full determinant.
They are positive eventually by the proved companion lower bound.
Inserting the \(2N\) unit singular values into the scalar singular list then changes the retained scalar log sum only by at most \(q_N\log^+\|P_N-z_NI\|=O(q_N\log N)\), because exchanging an omitted scalar value with a unit value can only exchange a scalar value at least one.
This proves (4).
Its probability-one event may depend on the chosen deterministic sequence, even though the initial clipped convergence (3) is uniform.

## Current assessment
[Selected decision](#decision-uniform-count-reviewed)

## Assessment history

### Decision uniform-count-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:36 |
| status | open |
| reason | The constant-drift resolvent family and the fixed-shift initialization have been assembled for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform counts and clipping](#statement) | Compact semialgebraic affine drifts with free zero kernel, scalar polynomial shifts and the prescribed nonreal quadratic companion application. |
| argument | [Complete proof](#argument) | Uniform free resolvent decay, random comparison, nets, exact scalar count transfer and prescribed-shift trimming. |

### Decision uniform-count-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:43 |
| status | proved |
| reason | Independent review verified the uniform free estimate, the Wigner comparison at a moving cutoff, the scalar application including the exceptional parameter, and the trimmed quadratic application. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform free and finite counts](#statement) | Fixed variable coefficients, prescribed compact semialgebraic parameter family and the stated assumptions on the free kernel. |
| argument | [Dyson equation and uniform exponent](#argument) | Positive solution at imaginary regularizer and semialgebraic uniform bound. |
| support | [Finite-size estimates](#finite-count) | Uniform comparison, shrinking counts and clipped logarithms. |
| support | [Scalar word chain](#word-chain) | All shifts of a fixed nonconstant polynomial. |
| support | [Quadratic companion](#fixed-shift-trim) | Trimmed estimates for the original fourth-moment model. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0201_v2.md#uniform-count-whole-proof) | Full theorem and its probability, compactness and moment requirements. |

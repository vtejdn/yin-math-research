---
author: Yin
---

# Phase spread and partial-alphabet exclusion without an input norm bound

<a id="statement"></a>
## Original-law exclusions

Let \(A,B\) be independent real symmetric Wigner matrices of order \(N\) with the [fixed-law assumptions of C198v1](Yin_C_F0198_v1.md#statement).
Each off-diagonal law is centered with variance one and finite fourth moment, and each real diagonal law is centered with finite second moment, before scaling by \(N^{-1/2}\).
Set \(M=AB+2BA\), and fix \(z=x+iy\) with \(y\ne0\).
There are \(b,d,s_0,c,C>0\) such that, outside an event of probability at most \(Ce^{-cN^{1/8}}\), every complex unit \(h\) with \(\|(M-zI)h\|\le b\) satisfies
\[
 \inf_{\theta\in\mathbb R,\ |D|\le s_0N}
 \|(\operatorname{Re}(e^{i\theta}h))_{D^c}\|\ge d.
 \tag{Original-phase}
\]
The constants may depend on \(z\) and the input laws.

Fix \(a_0,b_0>0\) and \(0<\chi<1\).
For every \(B\)-measurable finite dictionary of unit vectors \(\mathcal H_N(B)\) of size at most \(N^{(1-\chi)N}\),
\[
 \mathbb P\{\exists\,\|h_*\|=1:
       \operatorname{dist}(h_*,\mathcal H_N(B))\le a_0/\sqrt N,\
       \|(M-zI)h_*\|\le b_0/\sqrt N\}
       \le C e^{-cN^{1/8}}.
 \tag{Original-dictionary}
\]
More particularly, let \(0<\gamma\le1\) and \(0\le\alpha<1\).
The same summable estimate applies to existence of a unit \(h_*\) with residual at most \(b_0/\sqrt N\) for which on some set \(S\) of size at least \(\gamma N\), the restriction \((h_*)_S\) is within \(a_0/\sqrt N\) in Euclidean norm of a vector taking at most \(\lfloor N^\alpha\rfloor\) complex values.
Constants for these two estimates may also depend on their fixed parameters.
All probabilities are unconditional within-size probabilities for the original inputs, so the conclusions hold eventually almost surely for every coupling of the sizes.

## Current assessment
[Selected decision](#decision-tail-compensation-reviewed)

## Assessment history

### Decision tail-compensation-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T02:36 |
| status | open |
| reason | The sparse-tail compensation, uniform phase bound and unconditioned structured-vector exclusion are submitted for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous unguarded phase spread at fixed nonreal shift and summable dictionary and partial-alphabet exclusions for the actual finite-fourth-moment product. |
| argument | [Argument](#argument) | Tail-indicator conditioning, bounded representation, layered rectangle tests and conditional covariance and entropy. |
| dependency | [Sparse truncation](Yin_C_F0198_v1.md#sparse-truncation) | Summable bound on the number of marks and on the two truncated input norms. |
| dependency | [Fourth-moment row estimate](Yin_C_F0196_v1.md#affine-small-ball) | Uniform independent-row lower bound for the rectangular differences and for the exterior map on tail coordinates. |
| dependency | [Corner differences](Yin_C_F0196_v2.md#argument) | Conditional corner inequality and the forced word in the fourth-degree test, extended here to bounded nuisance coefficients. |
| dependency | [Exterior covariance and small-ball argument](Yin_C_F0194_v33.md#argument) | Spectral-window covariance count, short columns and uniform small-ball estimate, adapted below to a further vanishing deletion and conditional truncated laws. |
| dependency | [Dictionary covering](Yin_C_F0194_v33.md#partial-alphabet) | Complex entropy count with a positive constrained fraction and unrestricted complement. |
| dependency | [Short-column small-ball theorem](../audits/literature/KS26/Yin_U001.md#ks26-u001) | Koehler and Sohn, Proposition 2.4, at its recorded statement and applicability depth for centered variance-one real multipliers. |
| dependency | [Expected semicircle law](Yin_C_F0186_v4.md#finite-variance-weak) | Original single-color empirical interval masses on a finite mesh. |
| dependency | [Row concentration](Yin_C_F0186_v4.md#row-concentration) | Exponential deviations on the same mesh. |
| dependency | [Hermitian rank stability](Yin_C_F0186_v4.md#rank-stability) | Transfer of these eigenvalue counts to the truncated matrix. |

### Decision tail-compensation-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T02:42 |
| status | proved |
| reason | Independent whole-proof inspection verifies the original-law probability rates, the bounded representation of the marked tail contributions, phase spread and both structured-vector exclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Original finite-fourth-moment model, all deleted phases of fixed-shift near-modes and unconditional dictionary and partial-alphabet exclusion. |
| argument | [Proof](#argument) | Truncation and marked coordinates, bounded compensating coefficients, uniform row tests, original-law dictionary count. |
| dependency | [Sparse truncation](Yin_C_F0198_v1.md#sparse-truncation) | Tail count and norm control of both truncated inputs. |
| dependency | [Rectangular fourth-moment estimate](Yin_C_F0196_v1.md#affine-small-ball) | Independent rows in marked-coordinate reconstruction and rectangle differences. |
| dependency | [Corner calculation](Yin_C_F0196_v2.md#argument) | Conditional alternating difference on independent rectangles. |
| dependency | [Exterior covariance](Yin_C_F0194_v33.md#argument) | Short-column count for the further deleted bulk. |
| dependency | [Partial-alphabet entropy](Yin_C_F0194_v33.md#partial-alphabet) | Positive fraction of approximable coordinates with unrestricted remaining entries. |
| dependency | [KS26](../audits/literature/KS26/Yin_U001.md#ks26-u001) | Original Proposition 2.4 applied to centered standardized unmarked conditional variables. |
| dependency | [Weak semicircle law](Yin_C_F0186_v4.md#finite-variance-weak) | Expected macroscopic counts in one original color. |
| dependency | [Row concentration](Yin_C_F0186_v4.md#row-concentration) | Exponential deviations for fixed spectral windows. |
| dependency | [Rank estimate](Yin_C_F0186_v4.md#rank-stability) | Spectral-window transfer after tail deletion. |
| review | [Independent original-law finding](../audits/reviews/Yin_R_F0203_v3.md#original-law-whole-proof) | Complete statement and argument together with all nine direct dependency interfaces. |

<a id="argument"></a>
## Sparse tails and bounded coefficients

Use C198v1 with truncation exponent \(1/16\) and counting slack \(1/8\).
Mark the upper coordinates of either color whose raw absolute value exceeds \(N^{7/16}\), let \(E\) be the set of all endpoints of marks, and let \(A_0,B_0\) be the two truncations obtained by setting marked entries and their reflections to zero.
Except with probability \(Ce^{-cN^{1/8}}\), \(|E|\le2N^{3/8}\) and \(\|A_0\|,\|B_0\|\le K\) for a fixed \(K\).
Denote these two requirements together by \(\mathcal G\).
Condition on all mark indicators and all marked values, without conditioning the unmarked entries on the norm bounds.
Given these data, every unmarked off-diagonal raw entry is independent with its color's law conditional on \(|\xi|\le N^{7/16}\).
Its variance tends to one and its fourth moment stays bounded.
These facts hold uniformly over the mark data because the conditional law depends only on the color and \(N\).

Put \(M_0=A_0B_0+2B_0A_0\), \(R=M-M_0\), and write \(\mathbb C^E\) for the embedded coordinate space.
The identity \(R=(A-A_0)B+A_0(B-B_0)+2(B-B_0)A+2B_0(A-A_0)\) gives
\[
 \operatorname{ran}R\subset \mathbb C^E+A_0\mathbb C^E+B_0\mathbb C^E.
\]
For \(p=(p_0,p_1,p_2)\) supported on \(E\) write \(F(p)=p_0+A_0p_1+B_0p_2\).
On \(\mathcal G\), apart from a further \(Ce^{-cN}\) exception, every \(w\in\operatorname{ran}R\) admits a representation \(w=F(p)\) with \(\max_j\|p_j\|\le C_K\|w\|\).
Indeed, the real map \((a,b)\mapsto (A_0a+B_0b)_{E^c}\) on \(\mathbb R^E\oplus\mathbb R^E\) has a constant lower singular bound there.
For a fixed real unit pair its rows are independent normalized sums of unmarked entries.
Center the entries and absorb their deterministic means into the row centers.
Their variances belong to \([1/2,2]\) eventually, so after standardizing each variable the sum of squared coefficients is bounded below by \(1/2\) and the fourth moments stay bounded.
The [affine row estimate](Yin_C_F0196_v1.md#affine-small-ball) gives a fixed lower norm with failure \(e^{-cN}\).
A sufficiently fine constant-mesh net of cardinality \(\exp(O(|E|))\) extends this lower bound on \(\mathcal G\), since the map has norm at most \(2K\).
The same singular bound holds after complexification.
It controls both \(\|p_1\|\) and \(\|p_2\|\) from the \(E^c\) coordinates of any representation, and \(\|p_0\|\le\|w\|+K(\|p_1\|+\|p_2\|)\).
If \(E\) is empty, \(R=0\) and zero coefficients suffice.

For any rotated unit near-mode, retain the name \(h=u+iv\), put \(r=(M-zI)h\), and choose \(F(p)=Rh\).
Then
\[
 (M_0-zI)h+F(p)=r,\qquad
 \max_j\|p_j\|\le P
 \tag{Compensated}
\]
whenever \(\|r\|\le1\), for a fixed \(P\), since \(\|Rh\|\le1+3K^2+|z|\).
The coefficients can depend on the entire realization and on the rotation.
The following uniform estimates account for that dependence.

## Uniform rectangle tests for the compensation

Put \(D_0=M_0-xI\), \(H_0=D_0^2+y^2 I\).
Fix any constant radius \(P'>0\) for the coefficient triples, to be chosen large enough below, and restrict each of their real components to the ball of radius \(P'\) in \(\mathbb R^E\).
Conditional on mark data with \(|E|\le2N^{3/8}\), the following three properties hold on the truncated norm guard with joint failure probability at most \(Ce^{-cN}\).
All vectors and coefficient triples in the tests are real.

1. If \(a_0\) is supported on \(E\), \(\|a_0\|\ge1/4\), and all coefficients satisfy the radius bound, then \(\|D_0a_0+F(q)\|\ge t_2\) for a fixed \(t_2>0\).
2. For any fixed \(t>0\), if \(\max(\|a_1\|,\|a_2\|)\ge t\), then \(\|D_0F(a)+F(q)\|\ge t_3(t)>0\).
3. There exist \(s_0,t_4>0\) such that every real unit \(k\) on at most \(s_0N\) coordinates and any permitted triples \(a,q\) satisfy \(\|H_0 k+D_0F(a)+F(q)\|\ge t_4\).

To see this, for a fixed tuple with a specified nonzero leading vector, select directed panels starting at the support of that leading vector (one may use all of \(E\) in tests 1 and 2).
Choose the remaining two, three, or four disjoint panels outside \(E\) and the starting panel, each with \(\lceil N/5\rceil\) coordinates, taking \(s_0<1/10\) in test 3.
In test 1 the colors from the starting panel are \(B,A\).
In test 2 choose the first color \(A\) for \(a_1\), or \(B\) for \(a_2\), and then use \(B,A\).
In test 3 use \(B,A,B,A\).
All chosen rectangles consist of unmarked off-diagonal entries, including a first panel starting on \(E\), since the opposite endpoints lie outside \(E\).
Expose the remaining coordinates and duplicate each selected rectangle independently as in the [corner inequality](Yin_C_F0196_v2.md#argument).
If the norm is at most \(t'\) with conditional probability \(p'\), then with probability at least \((p')^{2^j}\) it is at most \(t'\) at all \(2^j\) corners, where \(j\) is the number of rectangles.

After restriction to the last panel the alternating difference of the degree-\(j\) expression is the product of its \(j\) directed difference rectangles on the leading vector, up to sign.
All smaller degrees vanish and a surviving walk must traverse each edge exactly once, in increasing panel order, since it starts on the first panel and finishes on the last.
In the third test the only word is \(ABAB\) in \(M_0^2\), with coefficient one.
In the first two tests the outer word is \(AB\) in \(M_0\) with coefficient one.
In test 2 the color of the innermost factor selects only one of \(a_1,a_2\), even when its color agrees with the next rectangle, because the corresponding unordered coordinate pairs are disjoint.
Each difference has centered independent entries and, before \(N^{-1/2}\) scaling, variance bounded below and fourth moment bounded above uniformly.
By successive independent applications of the rectangular row estimate, its complete product has norm at least a constant times the leading vector norm except with probability \(Ce^{-cN}\).
At all good corners for the hypothesized small-norm event the alternating difference would have norm at most \(2^j t'\).
Taking \(t'\) sufficiently small in proportion to the stated leading norm lower bound gives \(p'\le Ce^{-c'N}\), uniformly in the common background.

On the truncated norm guard the expressions in all three tests are Lipschitz in their vector parameters with a constant depending only on \(K,z\), for the sum of Euclidean parameter distances.
Cover the coefficient domains by nets of a sufficiently small fixed mesh, choosing points within the corresponding lower-norm constraints, with cardinalities \(\exp(O(|E|))\).
In test 3 cover each real support sphere similarly and sum over the at most \(\binom N{\lfloor s_0N\rfloor}\) supports of maximal size.
For a fixed mesh the further entropy is at most \(C s_0N\log(e/s_0)\), so \(s_0\) can be chosen small enough.
These unions and norm-guard extensions prove the three tests, with final lower bounds reduced by a fixed factor.
No probability estimate was conditioned on a favorable fresh-rectangle norm.

## From the real equations to phase spread

Set \(D=\|D_0\|\le3K^2+|x|\) on the truncated norm guard, using this fixed upper bound in all parameter choices.
Taking real and imaginary parts of (Compensated) gives
\[
 D_0u+yv+F(\operatorname{Re}p)=\operatorname{Re}r,\qquad
 D_0v-yu+F(\operatorname{Im}p)=\operatorname{Im}r .
\]
Take \(a=-\operatorname{Re}p/y\) and \(q=\operatorname{Im}p\).
Writing \(\epsilon=\|u\|+\|r\|\), these equations yield
\[
 \|v-F(a)\|\le C\epsilon,\qquad
 \|D_0F(a)+F(q)\|\le C\epsilon ,
\]
where \(C\) depends only on the fixed parameters.
If \(\epsilon\) is sufficiently small, \(\|F(a)\|\ge 1/2\) by \(\|v\|^2=1-\|u\|^2\).
First use test 1 with a coefficient radius covering \(a,q\).
Choose \(t>0\) so small that \(2Kt<1/4\) and \(2DKt<t_2/2\).
If both \(\|a_1\|,\|a_2\|<t\), then \(\|a_0\|\ge1/4\) and \(\|D_0 a_0+F(q)\|\le C\epsilon+2DKt\), contradicting test 1 for small \(\epsilon\).
Otherwise test 2 contradicts \(C\epsilon<t_3(t)\).
These choices give a fixed \(d_0>0\) with \(\|u\|\ge d_0\) whenever \(\|r\|\) is sufficiently small.
All tests hold uniformly over the coefficients, so the same conclusion holds for every phase at once.

Multiplication of (Compensated) by \(M_0-\bar zI\) and extraction of its real part give
\[
 \|H_0 u+D_0 F(\operatorname{Re}p)-yF(\operatorname{Im}p)\|
 \le (3K^2+|z|)\|r\|.
\]
Divide by \(\|u\|\) and apply test 3 with radius \(P'\ge (1+|y|)P/d_0\).
On the guard \(\|H_0\|\le D^2+y^2\).
Take a fixed \(\rho>0\) and then \(b>0\) small enough that
\((D^2+y^2)\rho+(3K^2+|z|)b/d_0<t_4\), also satisfying the preceding small-residual restriction.
The normalized vector \(u/\|u\|\) cannot lie within \(\rho\) of any real unit vector on at most \(s_0N\) coordinates.
For any real unit \(l\), the distance from \(l\) to its normalized nonzero truncation to a set \(D'\) is \(\sqrt{2(1-\|l_{D'}\|)}\le\sqrt2\|l_{(D')^c}\|\).
If the truncation is zero, the complementary norm is one.
This proves (Original-phase) with \(d=d_0\min(1,\rho/\sqrt2)\), including deletions intersecting or containing \(E\).
All mark-conditional exceptions in the tests have uniform bounds, so integration over the mark data costs no set enumeration.

## The one-color estimate with the exceptional coordinates fixed

Retain mark data and condition also on the entire original \(B\) and on all \(A\)-coordinates incident to \(E\).
The original \(B\)-dictionary, \(A_0\mathbb C^E\), and the values \(F(p)\) for any fixed coefficients on \(E\) are now determined.
For \(i<j\) outside \(E\), the remaining independent raw \(A\)-coordinates have the unmarked conditional law.
It is enough to use a spectral event measurable in the conditioned information.
For arbitrarily small fixed \(\beta>0\), take a fixed mesh of short real intervals covering the spectral windows of length \(2w\) intersecting \([-K,K]\) as in the [single-event argument](Yin_C_F0194_v33.md#argument).
Choose \(w\) by the uniform continuity of the semicircle distribution function so that each mesh interval has semicircle mass below \(\beta/4\).
The [one-color semicircle limit](Yin_C_F0186_v4.md#finite-variance-weak) and [row-block concentration](Yin_C_F0186_v4.md#row-concentration) place at most \(\beta N/2\) original \(B\) eigenvalues in each mesh interval, with unconditional failure \(Ce^{-cN}\).
Since \(B-B_0\) has support in \(E\times E\), [rank stability](Yin_C_F0186_v4.md#rank-stability) changes any interval count by at most \(2|E|\).
Thus on the size bound for \(E\), every relevant window for \(B_0\) has at most \(\beta N\) eigenvalues eventually.
The event used for the remaining conditional estimate includes this window bound and \(\|B_0\|\le K\).
Charging its complement together with the mark-size exception is done in the original law.

Suppose a prescribed unit dictionary vector \(h\) satisfies \(\|(\operatorname{Re}(e^{i\theta}h))_{T}\|\ge d/2\) for all phases and all \(|T^c|\le s_0N\).
This condition can be checked on the dictionary before using the remaining \(A\)-entries.
Write \(g=B_0h\), choose a large fixed \(L\), and put
\[
 U=\{i\notin E:\ |h_i|+|g_i|\le L/\sqrt N\},\qquad d_U=N-|U|.
\]
For any desired fixed small \(\epsilon_0>0\), one can arrange \(d_U\le\epsilon_0N\) eventually since \(|E|=o(N)\), \(\|h\|=1\) and \(\|g\|\le K\).
Take \(\epsilon_0<s_0\), write \(x_1,x_2\) for the real and imaginary parts of \(h_U\), and \(y_1,y_2\) for those of \(g_U\).
The two-channel Gram matrix of the \(x_a\) dominates \((d/2)^2I_2\), and the norm of \(G=(B_0)_{UU}\) is at most \(K\).
For each pair \(i<j\) in \(U\) put \(F_{ij}=e_ie_j^T+e_je_i^T\) on this coordinate space.
In the restriction to \(U\) the two real channel blocks of its column for \(M_0 h\) are \(N^{-1/2}(F_{ij}y_a+2G F_{ij}x_a)\).
After this restriction it suffices to test the residual using these columns alone and absorb the remaining independent coordinates into a translation.

For clarity, the [covariance count](Yin_C_F0194_v33.md#argument) applies on this smaller \(U\) as follows.
For the foregoing column map \(L_U\), \(N L_U L_U^T\) equals the block matrix with spectral fibers
\(\operatorname{Gram}(y_a+2\lambda x_a:a=1,2)\) over \(\lambda\in\operatorname{spec}(G)\), up to a real symmetric perturbation of rank at most 16 and a second perturbation of norm \(O_K(L^2/N)\).
This is the expansion of the symmetric matrix directions after adjoining and subtracting \(\sqrt 2 e_i e_i^T\), and involves no coordinates outside \(U\).
The determinant polynomial has degree four with leading coefficient \(16\det\operatorname{Gram}(x_a)\) bounded below, and the two eigenvalues of the fiber are bounded above uniformly on \([-K,K]\).
By factorization, a sufficiently small least eigenvalue forces \(\lambda\) into one of at most four windows of length \(2w\).
Each such window for \(G\) contains at most \(\beta N+2d_U\) eigenvalues by principal interlacing.
For each fixed \(0<\tau<1/4\), choose \(\epsilon_0,\beta\) small enough that \(2|U|-8(\beta N+2d_U)-16\ge \lfloor (2-\tau)N\rfloor=m\) for large \(N\).
There are consequently at least \(m\) singular values of \(L_U\) of size \(c_\tau/\sqrt N\) or greater.
Every column has norm \(O_K(L/N)\).

Center the remaining raw variables and divide by their conditional standard deviation, putting the means in the translation and the standard deviation into the columns.
Their variance before standardization tends to one, their centered standardized fourth moments are uniformly bounded, and a fixed \(M_*>0\) therefore satisfies \(\mathbb E[X^2\mathbf1_{\{|X|\le M_*\}}]\ge1/2\) for all standardized multipliers \(X\) eventually.
Project to \(m\) good left singular directions and scale the projected columns by a fixed sufficiently large multiple of \(\sqrt N\).
The resulting covariance dominates \(I_m\) and the columns have norm at most \(C/\sqrt N\).
For any fixed \(B'>0\), [Koehler and Sohn, Proposition 2.4](../audits/literature/KS26/Yin_U001.md#ks26-u001) gives
\[
 \sup_f\mathbb P\{\|(M_0-zI)h+f\|\le B'/\sqrt N
                     \mid\text{conditioned information}\}
 \le (C'/\sqrt N)^m\le N^{-(1-\tau)N}
\]
for large \(N\), with \(f\) fixed in this conditional law.
Indeed the radius in the scaled space is bounded, so in the proposition one may take \(t=C''/\sqrt N\) with \(C''\) large enough both for \(t\sqrt m\) to cover that radius and for the column bound.
All entries outside the retained pairs can be fixed first, including the diagonal, since the translated bound is uniform.
Applying this estimate does not require the conditional law on \(\|A_0\|\le K\).

## Passage to an approximant

On the good events, a near-mode \(h_*\) with residual at most \(b_0/\sqrt N\) obeys (Original-phase) and (Compensated) for large \(N\).
A dictionary approximant \(h\) within \(a_0/\sqrt N\) obeys the same deletion condition with lower bound \(d/2\), by contraction under rotation, real part and restriction.
Cover the complex coefficient triples with norms at most \(P\) on \(E\) by a mesh of Euclidean radius \(N^{-1/2}\) for each of the three balls.
Its cardinality is \((1+2P\sqrt N)^{6|E|}=\exp(o(N\log N))\), uniformly in the permitted mark counts.
This mesh is fixed after the indicators are known.
For the chosen approximant and one such mesh triple \(p'\), equation (Compensated) gives
\[
 \|(M_0-zI)h+F(p')\|
 \le [b_0+(3K^2+|z|)a_0+1+2K]/\sqrt N.
\]
Every center \(F(p')\) is fixed when applying the one-color estimate.
Taking \(\tau<\chi/2\) and summing over the mesh and the eligible dictionary costs \(N^{-c_\chi N}\).
Adding the original unconditional exceptions proves (Original-dictionary).

For the partial-alphabet conclusion use the [deterministic covering in C194v33](Yin_C_F0194_v33.md#partial-alphabet).
Choose \(\lceil\gamma N\rceil\) sites from the witness, round the \(k=\lfloor N^\alpha\rfloor\) possible values on a complex mesh of spacing \(1/N\), and cover the remaining complex unit ball at Euclidean scale \(N^{-1/2}\).
After normalization this yields unit centers at distance \(O_{a_0}(N^{-1/2})\) and a cardinality bound \(N^{[1-\gamma(1-\alpha)+o(1)]N}\), including \(\gamma=1\) or \(\alpha=0\).
Apply the dictionary estimate with any \(\chi<\gamma(1-\alpha)\).
The unrestricted near-mode and its contribution to the planar logarithmic defect remain open.

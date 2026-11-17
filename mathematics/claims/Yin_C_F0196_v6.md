---
author: Yin
---

# Near-kernel overlap for the two-sided real Wigner product with finite variance

<a id="statement"></a>
## Sparse phases, finite alphabets and fresh columns

Let \(A,B\) be independent real symmetric Wigner matrices of size \(N\).
Their fixed centered strict upper laws have variance one, their fixed centered diagonal laws have finite second moments, and coordinates above and on the diagonal are independent with scaling \(N^{-1/2}\).
Put \(M=AB+2BA\) and fix \(\mathcal K=\{|z|\le R,\ |\operatorname{Im}z|\ge\delta\}\) with \(0<\delta\le R<\infty\).
All probabilities below are within one dimension, with no cross-size assumption.

For any \(a_0,b_0>0,\ 0<\gamma\le1,\ 0\le\alpha<1\) and \(D>0\), outside probability \(O(N^{-D})\) simultaneously for \(z\in\mathcal K\), no complex unit \(h_*\) satisfying \(\|(M-zI)h_*\|\le b_0/\sqrt N\) has the following property.
On some set of at least \(\gamma N\) sites its restriction is at Euclidean distance at most \(a_0/\sqrt N\) from a vector taking at most \(\lfloor N^\alpha\rfloor\) complex values.
The same conclusion applies to \(M^{\mathsf T}\).
For \(M\) and any \(0<\chi<1\), one may instead exclude distance \(a_0/\sqrt N\) to a prescribed \(B\)-measurable dictionary of unit vectors of size at most \(N^{(1-\chi)N}\).
For the transposed product the analogous dictionary may depend on \(A\), after exchanging the colors.

A weaker phase bound than the constant bound at fourth moments suffices here.
In the argument \(K=C_D(\log(N+2))^3\).
At each fixed \(z\in\mathcal K\), outside probability \(O(N^{-D})\), every unit \(h\) with residual at most \(cK^{-10}\) satisfies
\[
 \inf_{\theta\in\mathbb R,\ |S|\le c'N/\log K}
 \|(\operatorname{Re}(e^{i\theta}h))_{S^c}\|\ge c''K^{-11}.
 \tag{1}
\]
Constants may depend on the fixed laws, \(D,R,\delta\) and the parameters of the relevant assertion.

The original first-column estimate of the [adaptive singular-gap argument](Yin_C_F0351_v2.md#discrete-overlaps) therefore holds with second moments alone.
Specifically, for \(n=N-o(N)\) principal sites with \(N-n\ge2h_n\) available cross columns and their \(N^{-1/2}\) normalization, take \(h_n=\lceil\log(n+3)\log\log(n+3)\rceil\).
On the minor norm guard \(\|M_0\|\le N^5\), choose the largest \(1\le r\le2h_n\) with \(t_r<N^{-40h_n}t_{r+1}\), or zero, using the ascending singular values of \(M_0-zI\) on this minor.
For either bottom \(r\)-dimensional left or right singular frame \(F\), the volume \(|\det(F^*V)|\), where \(V\) is an orthonormal frame of the first \(r\) independent real cross columns, is at least \(N^{-7r}\), outside probability \(O(h_n n^{-5/4}+n^{-D}+h_nN^{-3})\) in addition to the norm-guard failure at each fixed admissible shift.
Here the raw cross columns have the second input's strict upper law and are independent of the two principal minors.
The shift constants are uniform on the given compact region and the statement includes the empty product.

<a id="argument"></a>
<a id="truncated-core"></a>
## A polylogarithmic norm and few marked sites

Put \(\ell=\log(N+2)\) and cut the raw entries of both colors at \(T=\sqrt N\,\ell^2\), replacing those of larger modulus by zero including their reflections.
Denote the resulting matrices by \(A_0,B_0\), and for the moment use \(M_c=A_0B_0+2B_0A_0\).
Let \(E\) consist of the endpoints of all marked entries in either color.
By the second moments the expected number of independent marks is \(O(N/\ell^4)\).
Independence and the elementary exponential Markov bound for a Bernoulli sum imply \(|E|\le C N/\ell^3\) outside probability \(O(N^{-D})\) for every fixed \(D\).

Both core norms are at most \(K=C_D\ell^3\) outside \(O(N^{-D})\).
Indeed each centered normalized strict upper entry has absolute value at most \(2\ell^2\) and variance at most \(1/N\).
For the zero-diagonal centered symmetric matrix \(H\), expand \(\mathbb E\operatorname{Tr} H^{2p}\) in closed walks.
An edge occurring only once gives zero.
A connected pattern with \(v\) vertices and \(e\) distinct unordered edges has \(v\le e+1\) and its absolute expectation is at most \(N^{-e}(2\ell^2)^{2p-2e}\).
There are at most \((2p+1)^{2p}\) index patterns and at most \(N^v\) labelings of each.
Taking \(p=\lceil(D+3)\ell\rceil\) gives the asserted tail at a sufficiently large multiple of \(p\ell^2\).
The uncentered strict upper mean has norm \(O(\sqrt N/T)\) and the retained diagonal has norm at most \(\ell^2\).
After conditioning on the mark indicators and marked values, unmarked upper entries are independent with the raw law conditional on \(|\xi|\le T\).
We charge the norm exception in the original law.

The following elementary replacement for the fourth-moment row estimate is useful.
The centered unmarked laws, their independent differences and their standardized versions have variances bounded above and bounded below by positive constants for large \(N\); their squares are uniformly integrable by the fixed second moments and \(T\to\infty\).
The squared centered real sums of independent copies with coefficient squared sum one, also allowing the finitely many colors, are uniformly integrable.
Indeed at a fixed raw threshold \(H_0\), the sum of the centered tail parts has squared \(L^2\) norm at most a constant times the largest second tail moment, uniformly in the coefficients.
The sum of the independent centered bounded parts has a uniformly bounded fourth moment for that \(H_0\), by expansion.
These two facts imply uniform integrability of the squares by first choosing \(H_0\) large, then a large cutoff for the bounded-part sum.
The same reasoning applies to differences of independent sums.
Their variance lower bound and uniform integrability give constants \(d,p_0>0\) such that \(\Pr(|Z-Z'|>2d)\ge p_0\) for every such normalized row sum \(Z\) and its copy.
Thus \(\inf_x\Pr(|Z-x|>d)\ge p_0/2\).
For \(cN\) independent rows, Bernoulli concentration implies a Euclidean lower bound \(c'\) for the normalized affine row output on any real unit input outside probability \(Ce^{-c''N}\), uniformly in all deterministic row shifts.
Homogeneity gives the same bound times the norm of a specified input.

<a id="compensation"></a>
## Quantitative phase exclusion on the truncated norm event

With mark data exposed, the [range identity](Yin_C_F0196_v3.md#argument) gives \(\operatorname{ran}(M-M_c)\subset \mathbb C^E+A_0\mathbb C^E+B_0\mathbb C^E\).
Write \(F(p)=p_0+A_0p_1+B_0p_2\) for triples supported on \(E\).
For the exterior map \((u,v)\mapsto(A_0u+B_0v)_{E^c}\), the row bound just proved on any prescribed real unit pair has failure \(Ce^{-cN}\) conditionally on the marks.
All pairs joining \(E^c\) to \(E\) are unmarked.
A net of mesh \(c/K\) costs \(\exp(O(|E|\log K))=\exp(o(N))\) and extends the lower bound on the core norm event, since the map norm is at most \(2K\).
Its complexification has the same least singular bound.
Consequently any \(w\) in that range has a representation \(F(p)=w\) with \(\|p_1\|+\|p_2\|\le C\|w\|\) and \(\|p_0\|\le C K\|w\|\).
This also holds for empty \(E\) with zero triples.
Every rotated unit near-mode with residual \(r_0=(M-z)h\) of norm at most one therefore satisfies
\[
 (M_c-z)h+F(p)=r_0,\qquad \max_i\|p_i\|\le C K^3, \tag{2}
\]
because \(\|(M-M_c)h\|\le1+3K^2+R\).

Put \(D_0=M_c-\operatorname{Re}z,\ H=D_0^2+(\operatorname{Im}z)^2I\).
We give the scale bookkeeping for the [alternating rectangle tests](Yin_C_F0196_v3.md#argument).
For real coefficient triples \(a,q\) supported on \(E\), allow each component to have norm at most \(C'K^{10}\), with \(C'\) any fixed sufficiently large constant.
The three tests concern
\[
 D_0a_0+F(q),\qquad D_0F(a)+F(q),\qquad Hk+D_0F(a)+F(q).
\]
They have lower bounds \(c_1,\ c_2 t_*,\ c_3\), respectively, in the regimes \(\|a_0\|\ge1/4,\ \max(\|a_1\|,\|a_2\|)\ge t_*,\ \|k\|=1,\ |\operatorname{supp} k|\le s_NN\) for the corresponding test.
Here \(t_*=\varepsilon K^{-3}\) with a fixed small \(\varepsilon>0\), and \(s_N=c_*/\log K\).
For a fixed tuple, expose all but two, three or four disjoint rectangular panels starting at the leading input support, continuing on disjoint panels of size \(\lceil N/5\rceil\) outside that support and \(E\).
The \(2^j\)-corner Cauchy--Schwarz difference at degree \(j\) leaves a directed product of \(j\) independent difference rectangles, restricted to the last panel.
The colors in forward order are \(B,A\) for the first test, the color of the chosen \(a_1\) or \(a_2\) followed by \(B,A\) for the second, and \(B,A,B,A\) for the third.
The coefficient is one and shorter walks vanish, by the disjoint panels in [the original corner computation](Yin_C_F0196_v2.md#argument).
Sequential application of the finite-variance row lower bound gives the directed product a norm at least \(c\) times the leading norm outside \(Ce^{-c'N}\).
Taking the \(2^j\)-th root in the corner inequality leaves exponential fixed-tuple failure, also when the leading norm is \(t_*\).
This argument does not condition on the norm event of any fresh rectangle.
The vector Lipschitz constants of these linear tests on the core norm event are at most \(C K^4\).
Nets inside the stated parameter domains of mesh \(cK^{-8}\) suffice even at the second test's threshold \(c_2t_*\).
The coefficient entropy is \(O(|E|\log K)=o(N)\).
The sparse sphere, including support choices, adds at most \(C s_N N(\log K+\log(e/s_N))\); choose \(c_*\) small enough to absorb it in the fixed-tuple exponent.
This proves all three tests on the core norm guard with total exceptional probability \(Ce^{-cN}\) given admissible marks.

For \(h=u+iv\), write \(y=\operatorname{Im}z\).
The real and imaginary equations of (2) with \(a=-\operatorname{Re}p/y,\ q=\operatorname{Im}p\) give
\[
 \|v-F(a)\|\le CK^2 e,\qquad
 \|D_0F(a)+F(q)\|\le CK^4 e,\qquad e=\|u\|+\|r_0\|.
\]
If \(e<c K^{-7}\), then \(\|F(a)\|\ge1/2\).
When \(\|a_1\|,\|a_2\|<t_*\), this gives \(\|a_0\|\ge1/4\); the error in replacing \(D_0F(a)\) by \(D_0a_0\) is at most \(C K^3 t_*\).
Choose \(\varepsilon\) small relative to \(c_1\) to contradict the first test.
In the other case the second test contradicts the \(CK^4e\) bound for small enough \(c\).
Thus \(\|u\|\ge c'K^{-7}\) when the residual is sufficiently small compared to \(K^{-7}\).
Multiplying (2) by \(M_c-\bar z I\), taking the real part and dividing by \(\|u\|\), gives
\[
 \|H(u/\|u\|)+D_0F(\operatorname{Re}p/\|u\|)
                 -y F(\operatorname{Im}p/\|u\|)\|\le C K^9\|r_0\|.
\]
The two coefficient triples have norms at most \(C'K^{10}\).
Since \(\|H\|\le CK^4\), the third test excludes distance \(c K^{-4}\) of \(u/\|u\|\) to the sparse real unit vectors whenever \(\|r_0\|\le c K^{-10}\).
Normalizing the truncation of a unit real vector to a set changes it by at most \(\sqrt 2\) times its complementary norm if the truncation is nonzero.
All these tests apply to any rotation, proving (1).

<a id="dictionary"></a>
## Conditional covariance and polynomial-scale dictionaries

Condition additionally on the entire original \(B\) and all \(A\)-coordinates incident to \(E\).
The columns \(A_0\mathbb C^E\) and \(B_0\mathbb C^E\) and all dictionary vectors are now fixed.
For any prescribed small constant \(\epsilon_0>0\), the original \(B\) has at most \(\epsilon_0 N/2\) eigenvalues in any window of some sufficiently small fixed width \(2w\), except with probability \(Ce^{-c N}\).
Use a fixed finite mesh of intervals on \([-4,4]\), the atomless semicircle law and [finite-variance count concentration](Yin_C_F0186_v4.md#row-concentration); the mass outside \([-3,3]\) is also small by the same argument.
Hermitian rank comparison transfers this bound to \(B_0\) with cost at most \(2|E|\) per window.
Thus all windows have at most \(\epsilon_0 N\) eigenvalues in \(B_0\) for large \(N\), including windows centered beyond any fixed range.

A dictionary vector \(h\) which approximates a unit near-mode within \(a_0/\sqrt N\) inherits (1) with half its lower bound.
This inherited condition depends only on \(h\) and can be imposed before exposing the remaining \(A\)-coordinates.
Set \(g=B_0h\) and let \(U\) consist of the sites outside \(E\) with \(|g_i|+|h_i|\le K^2/\sqrt N\).
Because \(\|g\|\le K,\ \|h\|=1\), the deleted fraction is \(O(\ell^{-3}+K^{-2})=o(s_N)\).
Writing \(x_1,x_2\) for the real and imaginary parts of \(h_U\) and \(y_1,y_2\) for those of \(g_U\), one obtains \(\operatorname{Gram}(x_1,x_2)\succeq cK^{-22}I_2\).
Put \(G=(B_0)_{UU}\).
By the [physical column covariance identity](Yin_C_F0194_v33.md#argument), the \(N\)-scaled covariance of the two-channel linear column map in the unmarked raw entries of \(A\) on \(U\times U\), before multiplying by their common conditional variance, has fibers
\(\operatorname{Gram}(y_a+2\lambda x_a:a=1,2)\) over \(\lambda\in\operatorname{spec}G\), up to a real symmetric perturbation of rank at most 16 and the subtraction of the diagonal-column covariance.
The latter has norm at most \(C(1+K)^2 K^4/N\), by the deleted-source bound \(K^2/\sqrt N\) and \(\|G\|\le K\) in that identity.
The quartic determinant of the fiber has leading coefficient \(16\det\operatorname{Gram}(x_1,x_2)\ge cK^{-44}\).
Outside windows of width \(2w\) around the real parts of its four complex roots, its determinant is at least \(c_wK^{-44}\) and its norm is at most \(CK^2\).
The least fiber eigenvalue there is at least \(c_w K^{-46}\).
Deleting sites in passing from \(B_0\) to \(G\) costs at most \(2|U^c|\) in each interval count.
It follows, by first choosing \(\epsilon_0\) sufficiently small, that the original column map has at least \(m_0=\lfloor(2-\eta)N\rfloor\) singular values at least \(c_\eta K^{-23}/\sqrt N\) for each fixed \(0<\eta<1/4\) and all large \(N\).
The original column norms are at most \(CK^3/N\); the factors arise from the physical direction \(N^{-1/2}\), the two short source coordinates and at most one factor of \(G\).

Take the projection onto these \(m_0\) good left directions and absorb all other independent entries into the translation.
Center and standardize each retained raw entry by its conditional law, whose variance tends to one and whose square is uniformly integrable as established above.
Thus the uniform truncated second-moment hypothesis in [Koehler--Sohn, Proposition 2.4](../audits/literature/KS26/Yin_U001.md#ks26-u001) holds with a fixed raw cutoff there.
Scale the projected columns by \(C_\eta K^{23}\sqrt N\) to dominate identity covariance, leaving column norms at most \(C_\eta K^{26}/\sqrt N\).
Cover the complex compensator triples from (2) at mesh \(N^{-1/2}\), with log cardinality at most \(O(|E|(\log N+\log K))=o(N\log N)\).
Each selected triple and vector are fixed in the conditioning.
For an approximant \(h\) and a mesh triple \(p'\), the required output norm before scaling is at most \(C_{a_0,b_0}K^2/\sqrt N\), by (2) and the core norm guard.
Its scaled radius is at most \(C_\eta K^{25}\).
Apply the cited short-column theorem with parameter \(C'_\eta K^{26}/\sqrt N\), whose product with \(\sqrt{m_0}\) covers this radius and whose size covers the scaled columns.
For each pair of eligible centers the conditional probability is therefore at most \((C''_\eta K^{26}/\sqrt N)^{m_0}\).
The pointwise tests do not condition the unexposed coordinates on the core norm or phase event.
Choosing \(\eta<\chi/2\), and summing over the dictionary and compensator nets, leaves at most \(N^{-c_\chi N}\) besides the guard and phase exceptions.

The [partial-alphabet covering](Yin_C_F0194_v33.md#partial-alphabet) gives \(N^{[1-\gamma(1-\alpha)+o(1)]N}\) centers at distance \(O_{a_0}(N^{-1/2})\), including the unrestricted coordinates outside the chosen set.
The preceding dictionary estimate applies.
All constants use only \(R,\delta\) in the indicated range of shifts.
A mesh in an enlarged compact region of spacing \(O(N^{-1/2})\) costs \(O_R(N)\) centers, and shifting by one mesh distance just enlarges \(b_0\) by a constant.
Taking a larger failure exponent at the mesh points gives the stated simultaneous estimate.
For the transpose exchange the colors, and use the conjugate shift for the adjoint.

<a id="first-overlaps"></a>
## The singular gap chosen before the first columns

Use the arithmetic exclusion with \(\gamma=1/3,\alpha=9/10\).
The original minor has the canonical \(n\)-dimensional law after multiplying the quadratic and its spectral shift by \(N/n\), which keeps the shifts in a fixed enlarged nonreal compact region.
If \(r>0\) then each bottom singular unit combination has residual at most \((N^5+R)N^{-40h_n}\) on the norm guard.
Conditionally on the minor and past raw columns, choose a unit vector in that frame orthogonal in frame coordinates to the previously projected columns.
For its linear form on the fresh raw column the [two-dimensional real-scalar inverse Littlewood--Offord estimate](../audits/literature/Ngu12a/Yin_U001.md#real-scalar-geometric-inverse) gives small-ball probability less than \(n^{-5/4}\) at radius \(N^{-5}\).
Indeed a larger concentration would put at least half of the complex vector coordinates within \(O(N^{-5})\) of a progression of size \(O(n^{3/4})\), contradicting the established exclusion.
The required source difference condition holds for every fixed nondegenerate real strict upper law.
This applies to both frames even though they use the same fresh columns.
Gram--Schmidt gives projected volume at least \(N^{-5r}\), and the actual column volume is at most \(N^{2r}\) outside probability \(O(h_nN^{-3})\) by the second moments and Markov's inequality on raw column norms.
The union over both frames and the at most \(2h_n\) successive choices gives the asserted volume bound with the original minor's exceptional probability.
The second moments also make failure of the stated polynomial minor norm guard summable by Frobenius Markov, as in [the original trim comparison](Yin_C_F0351_v1.md#minor-trims).

## Current assessment
[Selected decision](#decision-finite-variance-overlap-reviewed)

## Assessment history

### Decision finite-variance-overlap-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:50 |
| status | open |
| reason | Polylogarithmic core norms, unchanged leading rectangle probabilities and the short-column covariance count give a complete candidate argument at finite variance. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-law exclusions](#statement) | Fixed finite second moments, partial alphabets and the first adaptive frame volumes. |
| argument | [Truncated inputs](#argument) | Mark counts, moments of closed walks and independent-row estimates. |
| support | [Phase spread](#compensation) | Compensated near-modes, rectangle tests and their actual scales. |
| support | [Dictionary exclusion](#dictionary) | Finite-variance conditional law, short columns and spectral windows. |
| support | [Frame overlaps](#first-overlaps) | Original-law Littlewood--Offord bounds and normalized frame volumes. |

### Decision finite-variance-overlap-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:02 |
| status | proved |
| reason | The compensated truncation and short-column estimates exclude partially structured vectors and give the adaptive overlaps with summable error. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-variance near-kernel overlaps](#statement) | The exact fixed-law statement and its dimension and coupling quantifiers. |
| argument | [Complete argument](#argument) | The compensated truncation and short-column estimates exclude partially structured vectors and give the adaptive overlaps with summable error. |
| support | [Quantitative compensated sparse phases](#compensation) | Quantitative compensated sparse phases. |
| support | [Partial-alphabet exclusion](#dictionary) | Partial-alphabet exclusion. |
| support | [Gram volumes of the two initial frames](#first-overlaps) | Gram volumes of the two initial frames. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0203_v6.md#finite-variance-overlap-whole-proof) | Fixed statement, applicable hypotheses and all mathematical interfaces as inspected. |

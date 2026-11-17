---
author: Yin
---

# Finite prefixes of polarized first-return means

At 2026-11-17T03:55 UTC a separate agent reviewed the complete fixed [C73](../../claims/Yin_C_A0073_v1.md) for Sheng Yin.
The reviewer previously reviewed the C67 identity and helped prepare its GV17 source reference.
The reviewer had no role in developing C73 and received no proof-development dialogue, author explanation or prior verdict for this claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [C73 statement](../../claims/Yin_C_A0073_v1.md#statement) | Fixed-endpoint hypotheses, error of the raw prefix, known-trace stopping, denominator correction, extrapolation and finite-data limitations. |
| [Whole-argument finding](#whole-argument-finding) | [Finite error formulas](../../claims/Yin_C_A0073_v1.md#argument) | Renewal in differences of unpadded moments, tail constants, trace decomposition in both coordinate cases, convolution split including its boundary, non-power and power error bounds. |
| [Whole-argument finding](#whole-argument-finding) | [Nonzero endpoint example](../../claims/Yin_C_A0073_v1.md#a-nonzero-signed-endpoint-and-the-rate-of-its-raw-first-mean) | Coisometry, signed moment and increment rates, \(16/35\), nonzero square-root bias, slit-disk coefficient bound, Richardson error and finite-power Perron exclusion. |
| [Whole-argument finding](#whole-argument-finding) | [Indistinguishable prefixes](../../claims/Yin_C_A0073_v1.md#how-long-two-different-signed-means-can-share-a-finite-prefix) | Nonclosed ranges, graph projection, \(11/240\) coefficient gap, coordinate travel times, identical swapped trace data, support under translations and fixed-size noise bound. |
| [Whole-argument finding](#whole-argument-finding) | [C67 normalization and reciprocity](../../claims/Yin_C_A0067_v1.md#argument) | Padded renewal and compression monotonicity. |
| [Whole-argument finding](#whole-argument-finding) | [Cyclic Green function](../../claims/Yin_C_A0067_v1.md#time-cancellation-on-a-gapless-cyclic-direction-of-a-four-line-group) | The lazy cyclic resolvent with the branch positive on \((0,1)\). |
| [Whole-argument finding](#whole-argument-finding) | [C69 finite and infinite blocks](../../claims/Yin_C_A0069_v1.md#finite-and-infinite-components-of-the-lifted-graph) | Two-column alternatives for a passing test. |
| [Whole-argument finding](#whole-argument-finding) | [C62 translation argument](../../claims/Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group) | Recovering a generating polynomial using a boundedly invertible projection corner. |

## Whole-argument finding

For a single sign, \((1-z)\sum u_nz^n=1-\sum_{n\ge1}(u_{n-1}-u_n)z^n\).
Including the stationary half gives \((1-z)h(z)=1-a(z)/2\), whose reciprocal is the survival series \(s\) by C67.
Each coefficient is nonnegative and the \(\ell^1\) mass of the decrement sequence \(a\) is \(1-a_\pm\le1\).
For \(h\) such increments and a total at least \(N\), a union bound designates one increment at least \(\lceil N/h\rceil\) and bounds the others by their full mass.
This gives \(K h^{1+\alpha}N^{-\alpha}\), including \(h>N\), and the constant \(L_\alpha\) after geometric weighting.
The raw mean omitted after \(N\) is \(N s_N+\sum_{l\ge N}s_l\).
Since at least \(N/2\) survival terms from \(\lceil N/2\rceil\) through \(N\) dominate \(s_N\), the factor \(1+2^{1+\alpha}\) suffices for either sign.
Adding the two tail bounds gives (1).

Keeping \(h\le H'\) uses only the one-factor tail \(u_{k-1}-a_\pm\) for \(k=\lceil N/H'\rceil\), with total coefficient at most \(\sum h2^{-h}=2\).
The remaining geometric masses sum to \(2^{-H'}\), proving (1a) without a rate or an unknown tail constant.
The signed mean interval follows by subtraction and the endpoint interval from \(c=1/m_+-1/m_-\), with positive lower bounds on both means.
The trace formulas are justified because \(a_++a_-=x^*px+y^*py\).
This counts the \(i,j\) identity-site diagonal coefficients once each for \(i\ne j\), and counts one coefficient twice for \(i=j\).
All other terms can be replaced by decreasing upper moments of \(H\), giving the stated increasing lower bounds.
The decreasing, summable survival sequence has \(Ns_N\to0\) by the same half-tail estimate.
Thus the finite intervals shrink with the specified \(H'\) when the required numerical input and trace are supplied.

For the convolution identity, \(a^-_n-a^+_n=2(v_n-v_{n-1})\).
Consequently the survival difference is the convolution of this endpoint increment with \(s^-*s^+\) after the factor \(1/2\), and its cumulative sum equals \(b*v\) since \(v_0=0\).
Summation by parts of the raw prefix gives \(L_N-(N+1)(L_N-L_{N-1})\), yielding (4) with precisely \(D_N=B_N-(N+1)b_N\).
In the difference \(E_N-E_{N-1}\), the common low-index piece ends at \(h=\lfloor N/2\rfloor\).
The reversed complementary sums have common range \(0\le l\le N-h-2\) and one extra term \(y_{N-h-1}b_{h+1}\).
This verifies both signs and the boundary in (5), also at \(N=1\).
The signed increment in the first piece is observable without knowing \(c\).
The bound for the ratio requires its computed denominator to be nonzero.

The decreasing \(s_n\) has pointwise decay \(O(n^{-1-\alpha})\) by its half-tail bound.
The C67 compression gives decreasing \(f_n\) for \(n\ge2\), so using its half-interval and the survival bound gives \(f_n=O(n^{-2-\alpha})\).
Splitting \(b_n\) at half its index bounds the large-index factor by this polynomial survival decay and sums the other factor by its finite mass.
In the first difference of \(b\) the corresponding large-index factor is differentiated, leaving two \(O(n^{-2-\alpha})\) sums and a midpoint product \(O(n^{-2-2\alpha})\).
This also proves \(D_N\to m_-m_+\).
For \(B_N^{(0)}\) and \(N B_N^{(1)}\) the two convolution halves contribute the separate terms \(O(N^{-\gamma})\) and \(O(N^{-1-\alpha}\sum_{l\le N/2}(1+l)^{-\gamma})\).
The midpoint in the difference costs \(O(N^{-\alpha-\gamma})\).
At \(\gamma=1\) the additional logarithm times \(N^{-1-\alpha}\) is \(O(N^{-1})\), proving (2) including that boundary.

For the example, \(TT^*=I\) and \(1-u\) is injective with dense nonclosed range.
Direct multiplication gives \(p_{12}=(u-u^{-1})/4\), the two unpadded diagonal identity coefficients \(1/2\), and the indicated signed endpoint \(1/4\).
The unpadded probe masses are therefore \(3/4,1/4\), and the reciprocal padded masses differ by \(8/5-8/7=16/35\).
In the positive spectral part, \((T^*H_0^nT)_{12}\) has coefficient at \(u\) equal to \((w_n(2)-w_n(0))/4\).
The sum of its two diagonal identity coefficients is \(w_n(0)\).
The displayed binomial ratios show that the signed error is \(O((1+n)^{-3/2})\) and its consecutive difference is \(O((1+n)^{-5/2})\), while the individual errors are \(O((1+n)^{-1/2})\).

Writing \(s=\sqrt{1-z}\), the two normalized padded Green functions have the stated constants and common linear term \(s/4\), because \(s(b^2-1)=O(s^2)\).
Independent differentiation gives \(c_1=(64/49-64/25)/4=-384/1225\).
Since \(f^--f^+=-s^2J(s)\), the generating function of the raw weighted prefixes is \(z(J+sJ'/2)/(1-z)\).
Its singular terms therefore have coefficients \(d\) and \(3c_1/2\), including the derivative contribution.
The rational functions of \(s\) are regular at zero after their stated singular terms are subtracted.
The spectral representation gives a uniform positive real part for the normalized padded Green functions on the closed unit disk up to their limiting value at one.
Nonvanishing on the remainder of this compact disk and analyticity in \(s\) near zero permit a sufficiently small outer disk slit from one.
The analytic-in-\(s\) remainder has slit jump \(O(\sqrt{x-1})\), whose coefficient integral is \(O(N^{-3/2})\).
Thus the nonzero leading bias is \(3c_1/2\) times \(4^{-N}\binom{2N}{N}\).
The central binomial asymptotic has error \(O(N^{-3/2})\) after its leading \(N^{-1/2}\) term, and the two-time formula cancels that term exactly.
The C69 exclusion also holds at the required strict normalization: a single irreducible passing block has zero projection or a gap from copies of one finite system, and two singleton blocks produce only a constant projection.
The example has both nonconstant projection and nonclosed range, properties preserved under a constant unitary change of coordinates.

In the last construction \(\|V\|\le1\), and \(5I/8\) dominates the remaining norm \(3/8\), giving bounded invertibility.
Forward substitution surjects onto the unweighted differences \(t_0,\ldots,t_{L-1}\), so weighting \(t_1\) by \(1-u\) makes the open range nonclosed.
The terminal constraint makes the second matrix injective and the vectors \(WV^{-1}\xi\) for unit approximate invariants of \(u\) have norm at least one and images tending to zero.
The stated common norm bound follows by bounding the unweighted array by \(1+r\), its row multiplier by two, and the terminal output separately by two.
The coefficient radii are bounded independently of \(L\).
For the open kernel the corner is \(p_{10}=rVD\) with \(\|D-I\|\le\sum_{j\ge1}r^{2j}=1/15\).
A single Fourier coefficient of \(V(D-I)\) has absolute value at most \(1/15\), while the real coefficient of \(V\) at \(u\) is at least \(1/4\).
Hence the real endpoint is at least \((1/4)(1/4-1/15)=11/240\), and multiplying by the two padded means cannot decrease that lower bound.
The corresponding coefficient and signed mean of the injective matrix vanish.

The input change modifies only the terminal diagonal block of \(I-A^*A/16\).
Tridiagonality forces at least \(2(L-1)+1\) factors for a changed path starting and ending among coordinates zero and one.
This proves exact agreement of all four selected matrix entries through order \(2L-2\), hence exact agreement of the selected moments and their two first-return prefixes.
At the first possible degree, only coordinate one can make the shortest round trip from this pair of coordinates.
The unique coordinate itinerary contributes a nonzero positive product up to its global subtraction sign, since its scalar shift factors on the cyclic subgroup are injective.
Swapping direct summands preserves every ordinary trace at every degree, and the graph column \(W\) has kernel-projection trace one because its domain is one whole copy and \(W^*W\) is invertible.
The bounded inverse of the translate of \(D\) recovers a translate of \(V\), with its identity and generating support, giving the support assertion for either direct sum.
Finally the scaled terminal row changes the contraction by at most \(\lambda^2/4\) in norm.
Telescoping powers and padding give moment discrepancies at most \(n\lambda^2/8\).
On taking the difference of reciprocal renewal functions, both additional factors \(1-f\) have coefficient \(\ell^1\) norm two.
Convolution therefore gives the coefficientwise bound \(N\lambda^2/2\) through order \(N\), with unchanged kernels for every \(\lambda>0\).
These arguments support the exact and noisy finite-prefix limitations at the specified endpoints and all the claimed positive error estimates.

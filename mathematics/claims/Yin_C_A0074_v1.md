---
author: Yin
---

# Signed returns with an infinite kernel projection on the original four-line group

## Statement

Fix one infinite finitely generated torsion-free group \(G\), in particular an original safeguarded four-line group with its rose marking.
Let \(s_1,\ldots,s_h\) generate \(G\), use their word length, and choose \(u\ne e\).
For \(d\ge1\) consider the integer group-ring row
\[
 T=(I,1-s_1,\ldots,1-s_h),\qquad a=(1-u)^d,\qquad A=aT .
\]
Its range is dense and nonclosed, its kernel dimension is \(h\), and it fails the [finite-power coefficient test](Yin_C_A0069_v1.md#statement) for every positive power, every constant unitary and every admissible normalization.
Its kernel projection has a nonzero coefficient at **every** group element.
Both the input and the projection require the whole group for their support even after independent translations of rows and columns.

Take \(M>\|A\|^2\), \(Q=I-A^*A/M\), and use the signed first-return means \(d_\zeta(i,j,g)\) and padded probes of [C67](Yin_C_A0067_v1.md#statement).
Number the row entries \(t_i\) of \(T\) starting at \(i=0\).
Put \(b=1+2h,\ \theta=2h/b\), and let \(P\) be the symmetric probability measure with a contribution \(1/(2h)\) from each \(s_j^{\pm1}\).
Define positive functions by convolution,
\[
 L(g)=b^{-1}\sum_{n\ge0}\theta^n P^n(g),\qquad
 E_{ij}=|t_i^*|*L*|t_j|.
\]
Absolute values on finite group-ring entries here mean coefficientwise absolute values.
In every nonidentity fiber, for each phase \(\zeta=1,\mathrm i\),
\[
 |d_\zeta(i,j,g)|\le4E_{ij}(g),\qquad
           L(g)\le|d_1(0,0,g)|\le4L(g).                              \tag{1}
\]
In particular the nonzero signed differences are controlled at distant endpoints, even though taking absolute values separately at each time gives a divergent weighted spatial square sum on every good four-line group when \(\beta>3\).
For all \(\beta\ge0\) and \(0<c<2\log(1/\theta)\) there is \(C_{\beta,c}\) such that
\[
 \sum_{|g|\ge R}(1+|g|)^\beta\!
    \left(\|\widehat p(g)\|_{\rm HS}^2+\sum_{i,j,\zeta}|d_\zeta(i,j,g)|^2\right)
 \le C_{\beta,c}e^{-cR},\qquad R\ge1 .                              \tag{2}
\]
At a finite real Abel time \(1/2\le z<1\), the corresponding signed return contrast satisfies
\[
 \left|\frac{f^+_{i,j,g,\zeta}(z)-f^-_{i,j,g,\zeta}(z)}{1-z}\right|
       \le 4E_{ij}(g)+C(1-z)^{1/(2d)}.                               \tag{3}
\]
The second term is uniform in the endpoint; it is removed at each endpoint before summation in (2).
Here \(T\) is an explicit same-kernel row of closed range, although the original input fails every finite-power test.
The upper bound comes from a sum of original-group walk fibers and a separate estimate on the time-dependent remainder.

On a good four-line group, time cancellation is necessary even in the **single real coordinate** \(i=j=0,\zeta=1\), where \(d_1(0,0,g)\ne0\) at every \(g\ne e\).
For this coordinate define \(U_g^\pm=\sum_n \big(n(f^-_n-f^+_n)\big)_\pm\), with both the positive and negative parts taken as nonnegative sizes.
For every \(\beta>3\) and every \(R\ge1\),
\[
   \sum_{|g|\ge R}(1+|g|)^\beta \min(U_g^+,U_g^-)^2=\infty .
\]
For any \(0<\eta<\log(1/\theta)\), the ratios \((U_g^++U_g^-)/(e^{\eta|g|}|d_1(0,0,g)|)\) are unbounded outside every finite ball.

## Resolvent of the original product fibers

Writing \(S=TT^*=b(I-\theta P)\) gives \(I\le S\le(1+4h)I\).
The first entry \(I\) of \(T\) makes it surjective.
The infinite-order cyclic shift shows by Fourier transform on right cosets that \(a\) is injective with dense nonclosed range.
Consequently \(A\) has that same range and nullity \(h\).
The row product \(AA^*=aSa^*\) lies between \(aa^*\) and \((1+4h)aa^*\).
Sublevel trace comparison and the circle symbol \(|1-e^{i\xi}|^{2d}\) yield positive spectral mass comparable to \(t^\alpha\) near zero, where \(\alpha=1/(2d)\); the zero atom for this row product is zero. [Trace comparison](Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group)

Let \(V=S^{-1/2}T,\ D=aS^{1/2},\ C=D^*D\).
Then \(VV^*=I,\ A=DV\), and \(C\) has the same positive spectral measure as \(DD^*=AA^*\), with no zero atom because \(D\) is injective.
For \(\lambda=M(1-z)/z>0\) write the normalized generating function of the actual powers as
\[
 R_z=(1-z)\sum_{n\ge0}z^n Q^n
 =I-V^*V+K_\lambda,\qquad
 K_\lambda=V^*\lambda(\lambda+C)^{-1}V .                              \tag{4}
\]
The identity follows by restricting to the range of \(V^*\), on which \(A^*A=V^* C V\), and to its orthogonal complement.
It also follows by geometric summation of the original column products.
No commutation of \(a\) with \(S\) is used.
The remainder is positive and
\[
 \tau_{h+1}(K_\lambda)=\tau\big(\lambda(\lambda+C)^{-1}\big)
 \le C_1\lambda^\alpha\quad(0<\lambda\le M).
\]
Indeed the part below \(\lambda\) costs \(O(\lambda^\alpha)\); on dyadic intervals \((2^j\lambda,2^{j+1}\lambda]\) use \(2^{-j}\) and the sublevel mass bound, extending its constant to the compact positive spectral interval.
The series converges since \(\alpha<1\).
Each absolute Fourier coefficient of this positive matrix is at most its trace, by Cauchy–Schwarz between the two coordinate vectors after applying its square root and by translation invariance of its diagonal entries.
Thus (4) isolates the endpointwise time error with a single scalar spectral estimate.
Spectral convergence identifies \(p=I-V^*V\).

The entries of \(V^*V=T^*S^{-1}T\) use the norm-convergent series \(S^{-1}=b^{-1}\sum_{n\ge0}\theta^n P^n\).
Each \(P^n(g)\) counts with its actual probability all length-\(n\) walks in \(G\) ending at \(g\).
Consequently the off-identity entries of \(I-V^*V\) are bounded by \(E_{ij}(g)\); the \(00\) entry is exactly \(-L(g)\) there.
Every \(g\) is reached by some walk, so \(L(g)>0\) throughout \(G\).
The identity coefficient of \(p_{00}\) is also positive: \(I-S^{-1}\ge0\) and is nonzero since some \(s_j\ne e\).
This proves the full support and the failure of **all** C69 tests by their finite-support conclusion.
For the input, the first entry \(a\) has the identity and \(u\) in its support.
For each \(s_j\notin\langle u\rangle\), the entry \(a(1-s_j)\) has disjoint supports for the two terms and contains both \(e\) and \(s_j\).
Taking differences \(xy^{-1}\) within each entry after row and column translations conjugates all these differences by the same left row element, forcing the full subgroup \(G\).

## Taking the signed time sum at its endpoint

For the two probes \(\xi_\pm\) of C67 write \(a_\pm(z)=(1+\xi_\pm^* R_z\xi_\pm)/2\).
The first-return series, computed by the scalar recursion from the original powers of \(Q\), obey
\[
 \frac{f^+(z)-f^-(z)}{1-z}
   =\frac{\operatorname{Re}(\zeta\,\widehat R_z(g)_{ij})}{a_+(z)a_-(z)} .
\]
Both real denominators lie between \(1/2\) and \(1\).
Applying the previous two coefficient estimates proves (3).
For each fixed endpoint this quotient tends to \(d_\zeta=\sum_n n(f^-_n-f^+_n)\), since both first-return sequences have total one and finite first mean.
Equation (4) gives its limit numerator and hence both bounds in (1).
The unsigned strong test fails by the [closed-range characterization](Yin_C_A0067_v1.md#two-stronger-tests-characterize-closed-range), even though the signed limit need not vanish at any positive distance.

For \(\sigma<\log(1/\theta)\), \(\sum_g e^{\sigma|g|}L(g)\le b^{-1}\sum_{n\ge0}(\theta e^\sigma)^n\) when \(\sigma\ge0\), since the walk has probability one and propagation \(n\).
The same weighted \(\ell^1\) finiteness holds for \(E_{ij}\) by the bounded shifts at the two ends.
It implies \(\sum_g e^{2\sigma|g|}E_{ij}(g)^2<\infty\).
Choose \(\sigma\) strictly between \(c/2\) and \(\log(1/\theta)\) to absorb the polynomial weight and obtain (2).

## Cancellation in the single coordinate with nonzero residual at every endpoint

The \(00\) entry of the positive remainder in (4) is
\[
 S^{-1/2}\lambda(\lambda+C)^{-1}S^{-1/2}.
\]
Its norm is at least \(1/\|S\|\) for every \(\lambda>0\), since multiplying on both sides by \(S^{1/2}\) recovers a positive contraction of norm one by nonclosed range.
Its coefficients tend to zero individually by the trace bound.
All coefficients of \((R_z)_{00}\) and \(p_{00}\) are real for real \(z\), since the matrices commute with complex conjugation in the standard group-coordinate basis.
Put \(V_g=U_g^++U_g^-=\sum_n n|f_n^--f_n^+|\).
The two first-return sequences have the same total mass one, hence \(|f^+(z)-f^-(z)|/(1-z)\le V_g\) by subtracting their values at one and using \(1-z^n\le n(1-z)\).
The real-probe formula and \(a_+(z)a_-(z)\le1\) give \(|\widehat{(R_z)_{00}}(g)|\le V_g\) off the identity.
If \(V\) had a finite weighted square sum of exponent \(\beta>3\), the [rapid-decay shell bound](Yin_C_A0067_v1.md#two-stronger-tests-characterize-closed-range) would uniformly approximate \((R_z)_{00}\) in operator norm by its truncations on finite balls.
The identity coefficients are uniformly bounded.
Coefficient convergence on each fixed ball and the same summable norm tail for \(p_{00}\) would then give \((R_z)_{00}\to p_{00}\) in operator norm, contradicting the lower bound.
Every finite set of entries of \(V\) is finite because each individual probe has first mean at most two.
Thus the squared weighted norm of \(V\) diverges on every exterior.
Subtracting \(|d_1(0,0,g)|\), whose weighted norm is finite by (1), and using \(V_g-|d_1(0,0,g)|=2\min(U_g^+,U_g^-)\) proves the divergence assertion.
Finally \(e^{\eta|g|}d_1(0,0,g)\) still has finite weighted square norm by the weighted Green estimate with \(\eta<\sigma<\log(1/\theta)\).
Any finite bound on the stated ratios outside a ball would again give finite weighted square norm for \(V\).

## Assessment history

### Decision nonzero-signed-green-tails

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:03 |
| status | proved |
| reason | Independent review checked the Green coefficient estimate, the noncommuting resolvent, the full support, the single-corner time cancellation and the failure of every finite-power test. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Nonclosed rows on the actual group with exponential spatial tails, nonvanishing signed limits and divergent opposite-sign contributions in one coordinate. |
| argument | [Proof](#resolvent-of-the-original-product-fibers) | Row spectral comparison, endpoint resolvent, positive walk kernel, weighted tails and the single-coordinate lower bound. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0110_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-nonzero-signed-green-tails)

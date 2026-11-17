---
author: Yin
---

# Complete convergence of the last singular-value contribution for a real quadratic Wigner polynomial with a Gaussian cross block

<a id="statement"></a>
## Real Wigner input and Brown limit

Let \(A_N,B_N\) be independent real symmetric Wigner matrices in the [fourth-moment model](Yin_C_F0186_v26.md#statement).
The two raw strict upper laws are centered with variance one and finite fourth moments, the diagonal laws are centered with finite second moments, and the entries are scaled by \(N^{-1/2}\).
Assume the strict upper law of \(B_N\) is standard normal.
Assume the strict upper law of \(A_N\) has a component of fixed positive mass satisfying the [second logarithmic concentration condition](Yin_C_F0186_v32.md#statement).
Equivalently for this hypothesis, the raw law can be written as \(p\nu+(1-p)\eta\), \(0<p\le1\), with
\[
 \int_1^\infty t Q_\nu(e^{-t})\,dt<\infty,\qquad
 Q_\nu(r)=\sup_{s\in\mathbb R}\nu([s-r,s+r]).
\]
Both diagonal laws may have atoms, and so may the residual strict upper component of \(A_N\).
Put \(P_N=A_NB_N+2B_NA_N\) and \(P=s_1s_2+2s_2s_1\) for free standard semicirculars.
For every coupling across dimensions the empirical eigenvalue measures of \(P_N\) converge weakly almost surely to the Brown measure of \(P\).
With \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\), descending singular values and \(\log^-s=\max(0,-\log s)\), for every integer \(R\ge1\) and \(v>0\),
\[
 \sum_N\Pr\left\{\frac1N\int_{|z|<R}\sum_{j>N-q_N}\log^-s_j(P_N-zI)\,dA(z)>v\right\}<\infty .
 \tag{1}
\]
It suffices to consider large enough \(N\) that \(q_N<N\).
Finite eigenvalue sets are immaterial to the planar integrals.
In particular this includes a Gaussian and atomic mixture for the first strict upper law and atomic diagonals for both colors.

<a id="argument"></a>
## Reduction to a compression of the independent minor

Fix an even deterministic \(k=2\lfloor\log^3(N+3)/2\rfloor\) and a prescribed set \(I\) of \(k\) physical sites, with complement \(J\) of size \(n=N-k\).
The [one-sided transfer C186v33](Yin_C_F0186_v33.md#statement) applies since \(k/\log N\to\infty\) and \(k\log N=o(N)\).
Its compression is
\[
 M=A_{JJ}B_{JJ}+2B_{JJ}A_{JJ},\qquad
 C=\pi_H M|_H,\quad H=\ker(B_{JI}^{\mathsf T}) .
\]
Here \(M,C\) are real even though their spectral shifts are complex.
The \(n\times k\) matrix \(\sqrt N B_{JI}\) has independent standard normal entries and is independent of \(M\).
Its columns span the first \(k\) directions of a real Haar flag, represented by successive real unit normals obtained by Gram--Schmidt.
In particular \(H\) has dimension \(n-k\) almost surely.
By C186v33 it suffices to prove that, for each integer disk \(D\) and every \(v>0\), the probabilities of
\[
 \frac1N\int_D\log|\det(C-zI)|\,dA(z)<\int_D u(z)\,dA(z)-v,
 \qquad u(z)=\tau\log|P-z|,
 \tag{2}
\]
are summable.
It is sufficient to prove that the corresponding lower limit is at least \(\int_Du\) almost surely under independent dimensions.
Indeed the events in (2) are independent then and the converse Borel--Cantelli lemma gives summability at the original marginals.
The estimates below apply under every cross-dimensional coupling.

<a id="minor-trims"></a>
## The two trims of the old minor

Write \(h=q_n\) and \(t_1(z)\le\cdots\le t_n(z)\) for the singular values of \(M-zI\) in increasing order.
Set \(b_\ell(z)=N^{-1}\sum_{i>\ell}\log t_i(z)\).
We will use, on every compact disk, almost surely,
\[
 b_h\to u,\qquad b_{2h}\to u\quad\hbox{in planar }L^1,\qquad
 \int_D\frac hN\log^-t_{2h+1}(z)\,dA(z)\to0.
 \tag{3}
\]
Indeed \(M=(n/N)P_n^{\rm can}\), where \(P_n^{\rm can}\) has precisely the canonical \(n\)-dimensional law.
As \(N\) runs through large integers, each \(n=N-k\) occurs at most three times, since \(k\) increases by two only at isolated integers separated by distances tending to infinity.
One may partition the deterministic sequence into at most three injective subsequences and extend their couplings to all canonical dimensions.
The [scalar trimmed theorem C186v36](Yin_C_F0186_v36.md#statement) applies separately on each.
With \(a=n/N\to1\), the retained sum for \(M-zI\) equals \(a\) times the canonical normalized retained sum at \(z/a\), plus \((n-h)N^{-1}\log a\).
Continuity of dilation of a fixed locally integrable function in local planar \(L^1\) gives the assertion for \(b_h\).

The event \(\|M\|\le N^5\) holds outside summable exceptions: the expected squared Frobenius norm of each input is \(O(N)\), so the failure of either bound \(N^2\) has probability \(O(N^{-3})\).
Thus the total of any \(2h\) positive logarithms is \(O_D(h\log N)=o(N)\) uniformly on each fixed disk.
Consequently \((b_h-b_{2h})_+=o(1)\) there.
For the upper control use
\[
 b_{2h}(z)\le \frac1{2N}\operatorname{Tr}\log\big((M-zI)^*(M-zI)+d^2 I\big)
                       +\frac{2h}{N}|\log d|,\qquad 0<d<1 .
\]
The [regularized potential theorem](Yin_C_F0186_v4.md#regularized-potentials) gives local uniform almost-sure convergence of the first term to the free regularization \(u_d\) for each fixed \(d\).
The change of dimensions uses the same \(a\), the shift \(z/a\), and \(d/a\) in place of \(d\), which changes each canonical regularized logarithm by at most \(|\log a|\).
Intersect the events for \(d=1/j\) and use \(u_d\downarrow u\) in local planar \(L^1\) to control \(\int_D(b_{2h}-u)_+\).
This proves the second assertion of (3).
Finally
\[
 h\log^-t_{2h+1}\le \sum_{i=h+1}^{2h}\log^-t_i
 = N(b_{2h}-b_h)+\sum_{i=h+1}^{2h}\log^+t_i ,
\]
which proves the last assertion of (3).

<a id="adaptive-gap"></a>
## A gap selected before sampling the flag

Fix a compact rectangle or disk portion \(K\subset\{|z|\le R,\ |\operatorname{Im}z|\ge\delta\}\), where \(R<\infty,\delta>0\).
All following probability estimates are uniform in \(z\in K\) and in real \(M\) with \(\|M\|\le N^5\).
For planar almost every \(z\) the matrix \(M-zI\) and each of its finitely many flag compressions are invertible for almost every sample, since each characteristic polynomial is monic.
Use measurable singular frames, with an arbitrary measurable choice at ties.

For fixed \(M,z\) choose the largest \(r\in\{1,\ldots,2h\}\) with \(t_r/t_{r+1}<N^{-40h}\).
If there is no such index, put \(r=0\).
This choice is independent of the flag, and eventually \(r\le2h<k\).
Each of the remaining adjacent ratios through \(2h\) is at least \(N^{-40h}\).
Therefore
\[
 b_r(z)\ge b_{2h}(z)-
 \frac{2h}N\log^-t_{2h+1}(z)-\frac{160h^3\log N}{N}.
 \tag{4}
\]

If \(r>0\), the largest singular value of \(\bigwedge^{n-r}(M-zI)\) equals \(\exp(Nb_r)\), and its second largest has ratio \(t_r/t_{r+1}\) to the largest.
For the first \(r\) flag columns let \(V\) denote an orthonormal frame of their span, and let \(W\) be an orthonormal frame of its real orthogonal complement.
The determinant of \(W^{\mathsf T}(M-zI)W\) is the diagonal matrix coefficient of that exterior power against the unit volume vector of \(W\).
The rank-one top singular term has modulus
\[
 \exp(Nb_r)\,|\det(F_L^*V)|\,|\det(F_R^*V)|,
\]
where \(F_L,F_R\) are orthonormal complex frames for the bottom \(r\) left and right singular spaces.
This follows from the complementary-minor identity in a unitary change of basis (the complementary determinants of the two blocks have equal modulus).
The remaining coefficient is at most \(\exp(Nb_r)N^{-40h}\) by its exterior operator norm.

For either fixed complex frame \(F\), let \(g_1,\ldots,g_r\) be the unnormalized real standard Gaussian columns used to generate \(V\).
At each projected step in \(\mathbb C^r\) choose a unit vector \(c\) orthogonal to the preceding \(F^*g_j\).
One of the real and imaginary parts of \(c^*F^*g\) for the fresh column has variance at least \(1/2\), since \(Fc\) is a complex unit vector.
The conditional probability of magnitude below \(N^{-5}\) is at most \(C N^{-5}\).
Gram--Schmidt in the projected column space gives \(|\det(F^*[g_1,\ldots,g_r])|\ge N^{-5r}\) outside \(CrN^{-5}\).
All full raw column norms are at most \(N^2\) with failure at most \(CkN^{-3}\) by the second moment.
Dividing by their column volume costs at most \(N^{2r}\).
The two determinant overlaps are consequently at least \(N^{-7r}\) each, outside a summable bound, by a union bound for the same sampled real frame.
Since \(14r\le28h\), the exterior remainder is less than half the leading modulus for all sufficiently large \(N\).
In the case \(r=0\) no compression or overlap bound is needed.
In both cases the log determinant after these first \(r\) deletions exceeds \(Nb_r-O(h\log N)\) with the preceding failure bound.

<a id="later-hyperplanes"></a>
## The subsequent real hyperplanes at nonreal shifts

Condition on \(M\) and the normals already used.
The next normal \(v\) is uniform on the real unit sphere in the remaining subspace, whose dimension \(d'\) lies between \(n-k+1\) and \(n\).
The current compressed matrix \(M'\) is real and satisfies \(\|M'\|\le N^5\).
For \(T=M'-zI\) invertible, the cofactor identity in an orthonormal basis ending in \(v\) gives the determinant of the next compression as \(\det T\,(v^{\mathsf T}T^{-1}v)\).
Only the complex symmetric part under transpose of \(T^{-1}\) enters this quadratic form.
It obeys
\[
 \operatorname{sym}(T^{-1})=T^{-\mathsf T}(\operatorname{sym}M'-zI)T^{-1},
 \qquad
 \|\operatorname{sym}(T^{-1})\|\ge\delta/\|T\|^2 ,
 \tag{5}
\]
because \(\operatorname{sym}M'\) is real symmetric.
This lower bound is independent of the inverse norm.
For large \(N\) it exceeds \(c_\delta N^{-10}\).

Represent \(v=g/\|g\|\) using a fresh standard real Gaussian on that subspace.
One of the real or imaginary parts of the symmetric matrix in (5) is real symmetric with norm at least half its indicated bound.
Orthogonally diagonalize that real part or imaginary part and condition on every Gaussian coordinate except one with a corresponding largest-modulus eigenvalue \(\lambda\).
The real quadratic component is \(\lambda X^2+c_0\) with \(X\) standard Gaussian, hence the probability its magnitude is \(\le b\) is at most \(C\sqrt{b/|\lambda|}\).
This follows by covering the real preimage by intervals of total length \(O(\sqrt{b/|\lambda|})\).
With \(\|g\|\le N^2\), a ratio \(|v^{\mathsf T}T^{-1}v|<N^{-36}\) forces \(b=N^{-32}\).
Thus the conditional failure at the step is \(O_\delta(N^{-11}+N^{-3})\), also counting the norm exception.
A union over the remaining at most \(k\) steps yields
\[
 N^{-1}\log|\det(C-zI)|\ \ge\
 b_{2h}(z)-\frac{2h}N\log^-t_{2h+1}(z)-o(1)
 \tag{6}
\]
outside a per-parameter probability bounded by \(C_{R,\delta}(1+k)N^{-3}\) and the norm guard failure.
Here the deterministic error is \(O((h^3+k)\log N/N)\).

<a id="planar-transfer"></a>
## Planar transfer and the remaining original-law cases

For the preceding compact region, Fubini followed by Markov and Borel--Cantelli shows that almost surely the exceptional parameter areas in (6) tend to zero, since their expectations are summable.
Null sets arising from singular intermediate compressions do not affect that conclusion, including when \(r\) varies, as there are only \(2h+1\) possible initial ranks.
The normalized negative part of any compressed characteristic logarithm has a deterministic uniform \(L^2(D)\) bound.
Indeed it is at most \(N^{-1}\sum_{\lambda}\log^-|z-\lambda|\), and Jensen with total mass \((n-k)/N\le1\) bounds the squared integral by \(\int_{|w|\le1}\log^2|w|\,dA(w)<\infty\).
The target \(u\) is locally square integrable by the same negative-kernel bound and compact support of the free Brown law.
Equations (3) and (6), and Cauchy--Schwarz on the exceptional sets, give
\[
 \int_K \big(u(z)-N^{-1}\log|\det(C-zI)|\big)_+\,dA(z)\longrightarrow0
 \quad\text{almost surely}.
\]
Use the countable regions of a fixed disk cut off by \(|\operatorname{Im}z|\ge1/j\).
On the remaining strip the integral of the negative part and of \(|u|\) are uniformly small by the square bounds and the vanishing area.
This proves (2) by the independent-dimension argument stated above.
C186v33 now proves the full Brown conclusion and the [terminal equivalence C186v36](Yin_C_F0186_v36.md#statement) gives (1).

This argument uses a Gaussian strict upper law to test a complex overlap with real random vectors and a quadratic form on every subsequently compressed subspace.
An atomic law on that cross block can give positive probability of an exact zero for a fixed linear or quadratic test.
The one-sided transfer also uses the regular component in the other color to control the genuine interior determinant.
The completely atomic case of [F0012](../tasks/Yin_T_F0012_v3.md#contract) requires further estimates.

## Assessment history

### Decision gaussian-cross-block-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:25 |
| status | proved |
| reason | Independent review verified the compression determinant, the complete lower comparison and terminal summability for the stated two laws. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Gaussian cross-block theorem](#statement) | Full Brown convergence and complete convergence of terminal disk losses with the stated raw input laws. |
| argument | [Compression proof](#argument) | Conditional flag, gap choice and integration of the untrimmed logarithm. |
| dependency | [Two trims](Yin_C_F0186_v36.md#statement) | Almost-sure trimmed convergence and its terminal equivalence. |
| dependency | [Interior transfer](Yin_C_F0186_v33.md#statement) | One-sided lower comparison for a regular component of the other color. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v1.md#finding) | Whole argument and its law, dimension and parameter restrictions. |

## Current assessment

[Selected decision](#decision-gaussian-cross-block-reviewed)

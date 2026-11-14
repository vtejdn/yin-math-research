---
author: Yin
---

# Dyadic column bounds for the normal divided difference

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let a finite tuple of bounded normal generators of a finite von Neumann algebra with faithful normal probability trace satisfy the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix one coordinate \(Z\), let \(N=W^*(Z)\), let \(K=\sigma(Z)\) have spectral law \(\mu\), and set \(D=\operatorname{diam}K>0\).
Write \(\delta\) for the distinguished derivation on the original represented starred polynomial core \(P\), \(\xi=\delta^*(1\otimes1)\), and \(\xi_N=\mathbb E_N\xi\).
Let \(\gamma\) be partial liberation of \(N\), let \(\eta=\gamma^*(1\otimes1)\), and let \(\nu\) be the joint spectral measure of \(\eta\) for the left and right actions of \(Z\) on \(H=L^2(M,\tau)\).
Use \(u=z-w\), \(C=\mathrm{id}\otimes\tau\) and the inner calculus \(I_{a\otimes b}(v\otimes w)=va\otimes bw\) on the coarse correspondence.
Thus \(\gamma=I_u\delta\) and \(V^2:=\|\xi-\xi_N\|_2^2=\int_{u\ne0}|u|^{-2}\,d\nu\). [Vacuum decomposition](Yin_C_F0238_v1.md#statement)

For a map \(T:P\to H\), denote its right column cost by
\[
 c(T)=\sup\left\{\left(\sum_k\|Tp_k\|_2^2\right)^{1/2}:
         p_k\in P,\ \Big\|\sum_kp_k^*p_k\Big\|\le1,\ k\text{ in a finite set}\right\}.
\]
Put \(\rho_j=2^{-j}D\) for \(j\ge0\), and define
\[
 a_j=\frac{\nu\{0<|u|\le8\rho_j\}^{1/2}}{\rho_j},\qquad
 b_j=\frac1{\rho_j}\left(\int \mu(\overline B(z,8\rho_j))^2\,d\mu(z)\right)^{1/2}.
 \tag{1}
\]
Write \(E=C\delta\), \(E_r=C I_{\bar u/(|u|^2+r^2)}\gamma\) for \(r>0\), and \(L_r=1+\log_+(D/r)\), with \(\log_+(x)=\max(0,\log x)\).
There is an absolute constant \(A\) such that
\[
\begin{split}
 c(E_r)&\le A\sum_{j\ge0}\min(1,\rho_j^2/r^2)(a_j+b_j)
        \le A\big(\|\xi_N\|_2 L_r+V\sqrt{L_r}\big),\\
 c(E)&\le A\sum_{j\ge0}(a_j+b_j).
\end{split}                                                          \tag{2}
\]
The constant in (2) may be enlarged between inequalities.
The same estimates hold for the distinguished right slice of the adjoint tuple with the same numerical sequences.
In particular, if \(\sum_j(a_j+b_j)<\infty\), the original canonical right slice has both its closure and its Hilbert adjoint defined on all bounded vectors.
The negative closure gives the strong dual at that coordinate.
The summability condition at every coordinate suffices for \(\mathsf S\).

A sufficient endpoint condition, for some \(\epsilon>0\), is
\[
 \int_{u\ne0}\frac{(1+\log(D/|u|))^{1+\epsilon}}{|u|^2}\,d\nu<\infty,
 \qquad
 \sup_{z\in K}\mu(\overline B(z,s))
 \le\frac{B\,s}{(1+\log(D/s))^{1+\epsilon}}
 \quad(0<s\le D/2).                                                  \tag{3}
\]
The first inequality of (2) also permits nonuniform marginal growth through the averaged masses in (1).
The proof gives an actual scalar example satisfying (3) for which no uniform marginal upper-growth exponent greater than one is possible.

## Argument

### The cost of a measurable spectral block

For a marginal projection \(e\), write \(t=\tau(e)\), \(G_e=C I_{e\otimes e}\gamma\), and \(\zeta=-i\eta=(i\gamma)^*(1\otimes1)\).
For every projection, including a Borel spectral projection with discontinuous symbol, the finite-kernel adjoint for \(i I_{e\otimes e}\gamma\) at \(1\otimes1\) is \(e\zeta e\), since its row and column corrections agree. [Marginal adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint)
In the [finite-kernel graph and energy calculation](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy), bounded marginal factors are obtained by uniformly bounded strong-star and \(L^2\) approximation from marginal polynomials.
Their liberation derivatives converge by the explicit inner formula on the marginal, and their outer multipliers converge strongly on the coarse Hilbert space.
Consequently the iterated finite-kernel calculations apply on words with these bounded factors, including in a free enlargement.
Only the liberation graph needs such an extension.

Here is the [projection square calculation](../drafts/Yin_D_F0002.md#an-exact-projection-block-lower-identity-and-its-summation-limit) with its upper estimate.
Every output \(G_ep\) ends in \(e\).
For \(q=e\otimes e\), the kernel row is \(te\) and \(q\circ q=tq\).
Let \(v=h\pm i\sqrt{1-h^2}\) for a strict selfadjoint contraction \(h\) in the core.
Use \(E_q=iG_e\) in (B0c) and (B0e) of the finite-kernel energy calculation.
Its term \(\operatorname{Im}\tau(te\,v^*iG_ev)\) is \(t\operatorname{Re}\langle v,G_ev\rangle\) by the right support and traciality.
The composition term \(\operatorname{Im}\langle v,E_{q\circ q}v\rangle\) gives the same scalar.
Thus, for inner products linear in the second variable,
\[
  \|iG_ev\|_2^2-2\operatorname{Re}\langle iG_ev,v e\zeta e\rangle
                  =t\operatorname{Re}\langle v,G_ev\rangle .           \tag{4}
\]
Both signs follow by the convergent binomial series in the first-derivative seminorms used in (B0d).
The last inner product may replace \(v\) by \(ve\), of Hilbert norm \(\sqrt t\).
It follows that \(\|G_ev\|_2\le2\|e\eta e\|_2+t^{3/2}\).
Averaging the two signs and rescaling proves the same bound for selfadjoint contractions in the core.
Taking real and imaginary parts costs a factor two on arbitrary contractions.

Adjoin two free Haar unitaries \(U,V_0\) jointly free from \(M\).
The [free extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) preserves the old vacuum and kills the new letters, so \(\gamma=I_u\delta\) has the same commutator vacuum \(\eta=[Z^*,\xi]\) and the same \(e\zeta e\).
Estimate (4) and the contraction bound hold on its enlarged polynomial core.
Encode an old column in \(\sum_k U^k V_0 U^{-k}p_k\), of norm at most \(2\|\sum p_k^*p_k\|^{1/2}\).
The inserted derivative is zero on these Haar coefficients.
Consequently its right slice is \(\sum_k U^k V_0 U^{-k}G_ep_k\), and its squared norm equals the sum of the old squared output norms by the [two-Haar encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries).
We obtain
\[
                     c(G_e)\le4(2\|e\eta e\|_2+t^{3/2}).             \tag{5}
\]

For orthogonal marginal projections \(e,f\) put \(G_{ef}=C I_{e\otimes f}\gamma\).
Expansion of \((e+f)\otimes(e+f)\) gives \(G_{ef}(p)=(G_{e+f}(p)-G_e(p))e\), since the right support after slicing is the first inner factor.
Thus \(c(G_{ef})\le c(G_{e+f})+c(G_e)\).
For a repeated projection use \(G_{ee}=G_e\).
In both cases, with \(q=e\vee f\), (5) gives
\[
                 c(G_{ef})\le A_0\big(\|q\eta q\|_2+\tau(q)^{3/2}\big) . \tag{6}
\]

### Annular multipliers on a square grid

Choose a smooth radial cutoff \(\phi\) on \(\mathbb R^2\), equal to one on the closed unit disk and zero outside the disk of radius two, nonincreasing in radius.
Put \(\psi(v)=\phi(v)-\phi(2v)\).
Then \(\psi\) is supported where \(1/2\le |v|\le2\), and \(\sum_{j\ge0}\psi(u/\rho_j)=1\) for \(0<|u|\le D\).
Let \(T_j\) be \(C I_{g_j}\gamma\) with \(g_j(u)=\psi(u/\rho_j)/u\), defined as zero at the origin.
Also let \(T_{j,r}\) have symbol \(g_{j,r}(u)=\psi(u/\rho_j)\bar u/(|u|^2+r^2)\).
These symbols are Fourier transforms of finite measures of total variation bounded by \(A_1/\rho_j\) and \(A_1m_{j,r}/\rho_j\), respectively, where \(m_{j,r}=\min(1,\rho_j^2/r^2)\).
Indeed at unit scale the second rescaled symbol is \(\psi(v)\bar v/(|v|^2+\lambda^2)\), \(\lambda=r/\rho_j\).
Its derivatives through order four are bounded by \(A_2\min(1,\lambda^{-2})\) on the fixed annulus, by differentiating the reciprocal, using its positive lower bound there for \(\lambda\le1\) and factoring out \(\lambda^{-2}\) for \(\lambda\ge1\).
Applying \((1-\Delta)^2\) before Fourier transformation bounds its Fourier density by an integrable multiple of \((1+|s|^2)^{-2}\) times this bound.
Dilation and the factor \(1/\rho_j\) give the assertion, with \(\lambda=0\) for \(g_j\).

Partition the plane into disjoint half-open squares of side \(\rho_j\).
Only finitely many meet \(K\).
Associate to them their spectral projections, omitting zero ones, and call an ordered pair neighbors when the distance between the closed squares is at most \(2\rho_j\).
This includes a square paired with itself and gives uniformly bounded degree in each variable.
Outside such rectangles both symbols vanish.
Write \(T_{ef}\) for the contribution of the rectangle \(e\otimes f\) to \(T_j\) or \(T_{j,r}\).
On a rectangle each Fourier character is the separated product of two continuous marginal unitaries \(v,w\).
For \(\theta=I_{e\otimes f}\gamma\) and \(G=C\theta\), the [right multiplication identity](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) reads
\[
               C I_{v\otimes w}\theta(p)=G(pw)v-pG(w)v .
\]
It extends to continuous \(w\) by uniform polynomial approximation, using the one-input bound for \(G\).
For the first term the column of products \(p_kw\) costs at most \(c(G)\|w\|\|\sum p_k^*p_k\|^{1/2}\), by the same approximation on each fixed column.
The second uses \(\sum_k\|p_kG(w)\|_2^2\le\|\sum p_k^*p_k\|\|G(w)\|_2^2\).
Hence integration against the Fourier measure and (6) bound \(c(T_{ef})\) by the total variation times \(2c(G_{ef})\).
The output of every such term ends in \(e\), as \(v\) commutes with this projection.
For each column the sums over different first squares are consequently orthogonal in the Hilbert direct sum.
Cauchy–Schwarz over the uniformly many second squares then gives \(c(\sum_{ef}T_{ef})^2\le A_3\sum_{ef}c(T_{ef})^2\).

For neighboring squares their union has diameter at most \((2+2\sqrt2)\rho_j\).
A fixed point pair belongs to \((e\cup f)^2\), in spectral-set notation, for at most a bounded number of ordered neighboring pairs, by the degree bound and disjointness.
Thus the sum of the squared compressions in (6) is at most \(A_4\nu\{0<|u|\le8\rho_j\}\), using \(\nu\ll\mu^2\) and diffuseness to remove the diagonal.
The mass cubes in (6) sum to at most \(A_5\sum_e\tau(e)^3\), by \((s+t)^3\le4(s^3+t^3)\) and the same degree bound.
For \(z\) in its square \(e\), the whole square lies in \(\overline B(z,8\rho_j)\).
In particular,
\[
 \begin{split}
  c(T_j)&\le A_6(a_j+b_j),\qquad c(T_{j,r})\le A_6m_{j,r}(a_j+b_j),\\
  c(T_{j,r})&\le A_6m_{j,r}\left(a_j+\rho_j^{-1}
                                      \Big(\sum_e\tau(e)^3\Big)^{1/2}\right).    \tag{7}
 \end{split}
\]
In fact \(b_j^2\le A_7\rho_j^{-2}\sum_e\tau(e)^3\).
For \(z\) in a square \(e\), its radius-\(8\rho_j\) ball meets only squares in a fixed bounded neighborhood of \(e\).
Bounding the square of their combined masses by their degree times the sum of their squared masses and then integrating gives a sum of \(\tau(e)\tau(f)^2\).
Use \(3st^2\le s^3+2t^3\) and the bounded degree in both variables.

### Removing the cutoff and summing the estimates

Apply the [marginal packing inequality](Yin_C_F0233_v1.md#statement), part 1, to the squares at a fixed scale and their separate centers.
Each satisfies \(\|(Z-\lambda)e\|_2\le\sqrt2\,\rho_j\sqrt{\tau(e)}\), and the squares partition the spectrum.
The summed inequality gives \(\rho_j^{-2}\sum_e\tau(e)^3\le A_8\|\xi_N\|_2^2\), hence \(\sup_j b_j\le A_9\|\xi_N\|_2\).
For \(x=|u|>0\), the numbers \(\rho_j^{-2}\) with \(x\le8\rho_j\) form a geometric progression whose sum is at most \(A_{10}/x^2\).
By Tonelli, \(\sum_j a_j^2\le A_{10} V^2\).
Since \(\sum_j m_{j,r}\le A_{11} L_r\) and \(\sum_j m_{j,r}^2\le A_{11} L_r\) by geometric summation, Cauchy–Schwarz gives the second bound in (2) for \(E_r\).

For each fixed finite column, the partial sums of \(T_j\) converge strongly on its inputs to \(E\) in the output Hilbert space.
Indeed their symbols acting on \(\delta(p)\) are \(\sum_j\psi(u/\rho_j)\) over the chosen initial segment.
They are bounded by one, tend to one off the diagonal, and the inner spectral measure of each coarse vector is dominated by \(\mu^2\). [Coarse spectral calculus](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)
For the soft cutoff multiply the same partial symbols acting on \(\delta(p)\) by \(|u|^2/(|u|^2+r^2)\).
The column triangle inequality and the preceding limits prove both of (2)'s shell-sum bounds.

For (3), put \(p=1+\epsilon\).
If \(x\le8\rho_j\) with \(0<x\le D\), then \(1+j\le A_{12}(1+\log(D/x))\).
Multiplying the geometric sum by this bound to the power \(p\) and integrating gives
\[
  \sum_{j\ge0}(1+j)^p a_j^2
  \le A_p\int_{u\ne0} (1+\log(D/|u|))^p |u|^{-2}\,d\nu.
\]
Thus \(\sum a_j\le(\sum_j(1+j)^{-p})^{1/2}(\sum_j(1+j)^pa_j^2)^{1/2}<\infty\).
For all sufficiently large \(j\), the second condition of (3) gives \(b_j\le A_{p}B(1+j)^{-p}\), which is summable as well.

For the adjoint tuple, its distinguished actual derivation on the same core is \(\epsilon(h)=(\delta(h^*))^\dagger\), with vacuum \(\xi^*\), where \((a\otimes b)^\dagger=b^*\otimes a^*\). [Normal companion](Yin_C_F0076_v1.md#statement)
Its partial liberation is precisely \(\gamma\), since the prescription on every polynomial in the marginal algebra and on the omitted starred generators is unchanged.
Equivalently \(I_{\bar u}\epsilon=\gamma\) on this core, as one checks on the generators.
The joint spectral measure for \(Z^*\) is the conjugation push-forward of \(\nu\) in both entries, so (1) and the inverse-gap energy are unchanged.
The original left slice at \(p\) is the tracial adjoint of the companion right slice at \(p^*\).
Finiteness of both one-input bounds therefore supplies the asserted domains by [the two-slice theorem](Yin_C_F0072_v1.md#statement), part B.
Writing \(X_k\) for the original generators and \(Z=X_i\), the identity \(E(X_kp)-X_kE(p)=\delta_{ik}\tau(p)1\) extends to the closure by graph approximation using boundedness of left multiplication and of the rank-one right side.
It gives the stated generator-first commutator for the negative closure.

### The logarithmic growth range

For an explicit marginal, choose independent real random variables \(U\) uniform on \([0,1]\) and \(Y\) with distribution function
\[
 \sigma([0,y])=\left(\frac5{\log(1/y)}\right)^3,\qquad 0<y\le e^{-5},
\]
supported in \([0,e^{-5}]\) with no atom at zero.
Let \(Z=U+iY\) in its abelian tracial algebra.
The density \(375/[y\log(1/y)^4]\) is decreasing on the support, since \(\log(1/y)\ge5\).
An interval of length \(2s\) therefore has \(\sigma\)-mass at most \(\sigma([0,2s])\) when \(2s\le e^{-5}\).
The projections of a planar radius-\(s\) ball onto both axes have length at most \(2s\), hence its \(\mu\)-mass is bounded uniformly by \(A_{13}s/(1+\log(D/s))^3\), increasing the constant for larger \(s\).
At \(z=1/2\), the ball contains \([1/2-s/2,1/2+s/2]\times[0,s/2]\), giving mass at least \(s(5/\log(2/s))^3\) for small \(s\).
Thus this marginal violates every \(O(s^\alpha)\) upper estimate with \(\alpha>1\) occurring in the [power-growth theorem](Yin_C_F0078_v1.md#statement).

The upper mass estimate implies \(\sup_{z\in K}\int|z-w|^{-1}d\mu(w)<\infty\) by summing annular contributions bounded by \(A_{14}(1+j)^{-3}\) at small scales.
The scalar difference quotient \((h(z)-h(w))/(z-w)\) is a represented coarse derivation on marginal starred polynomials.
Such polynomials are Lipschitz on the compact support and this quotient is bounded there off the null diagonal.
By absolute integrability, swapping \(z,w\) in its second term yields a bounded vacuum functional represented by the conjugate of \(2\int(z-w)^{-1}d\mu(w)\).
In the abelian one-coordinate system \(\gamma(h)=h\otimes1-1\otimes h\) has zero vacuum on the entire core.
This example therefore satisfies both parts of (3).
For an arbitrary correlated tuple the weighted condition on its own \(\nu\) remains part of this endpoint implication.
Actuality alone supplies the unweighted inverse-gap estimate used for the logarithmic soft bound.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:41 |
| status | open |
| reason | The dyadic column estimate, the unconditional soft-cutoff growth and the sufficient logarithmic endpoint conditions are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-coordinate soft and uncut column bounds, invariant companion estimates, sufficient full domains and the endpoint growth example. |
| argument | [Argument](#argument) | Local finite-kernel square, free amplification, summation of spectral squares, Fourier shell bounds, inverse-gap and marginal packing summations, graph limits and the explicit marginal law. |
| dependency | [Liberation recovery](Yin_C_F0238_v1.md#statement) | The original distinguished derivation, partial liberation vacuum, commutator identity, absolute continuity and exact inverse-gap norm splitting. |
| dependency | [Inner spectral calculus](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Domination of every coarse vector measure by the marginal product law and faithful inner insertion away from the diffuse diagonal. |
| dependency | [Separated multiplier after contraction](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Product rule for the right slice at a continuous marginal multiplier, its norm-approximation extension and its two finite-column estimates. |
| dependency | [Marginal actual tensor adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Finite real symmetric inner insertion has actual vacuum given by its action on the real liberation vacuum. |
| dependency | [Finite-kernel energy and enlarged core](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Bounded measurable marginal graph approximation, (B0c) and (B0e) with their analytic first-derivative limit for the signed unitaries. |
| dependency | [Two-Haar vacuum extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual old vacuum after adjoining free Haar letters and derivative zero on the new generators. |
| dependency | [Finite-column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Norm bound by twice the old column norm and orthogonality of the encoded old Hilbert outputs. |
| dependency | [Marginal packing](Yin_C_F0233_v1.md#statement) | Part 1 on disjoint marginal spectral projections with their own centers, and the numerical bound proportional to the squared scalar vacuum norm. |
| dependency | [Adjoint companion](Yin_C_F0076_v1.md#statement) | Part 1, diffuseness, forced starred values, flip-adjoint derivation and its actual vacuum on the adjoint tuple. |
| dependency | [Actual two-slice domains](Yin_C_F0072_v1.md#statement) | Part B for both original canonical bounded-vector domains once the two operator-norm-to-Hilbert-norm bounds hold. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:53 |
| status | proved |
| reason | Adopt the dyadic cutoff bound and the summable endpoint conditions after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-coordinate soft and uncut column bounds, invariant companion estimates, sufficient full domains and the endpoint growth example. |
| argument | [Argument](#argument) | Local finite-kernel square, free amplification, summation of spectral squares, Fourier shell bounds, inverse-gap and marginal packing summations, graph limits and the explicit marginal law. |
| dependency | [Liberation recovery](Yin_C_F0238_v1.md#statement) | The original distinguished derivation, partial liberation vacuum, commutator identity, absolute continuity and exact inverse-gap norm splitting. |
| dependency | [Inner spectral calculus](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Domination of every coarse vector measure by the marginal product law and faithful inner insertion away from the diffuse diagonal. |
| dependency | [Separated multiplier after contraction](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Product rule for the right slice at a continuous marginal multiplier, its norm-approximation extension and its two finite-column estimates. |
| dependency | [Marginal actual tensor adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Finite real symmetric inner insertion has actual vacuum given by its action on the real liberation vacuum. |
| dependency | [Finite-kernel energy and enlarged core](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Bounded measurable marginal graph approximation, (B0c) and (B0e) with their analytic first-derivative limit for the signed unitaries. |
| dependency | [Two-Haar vacuum extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual old vacuum after adjoining free Haar letters and derivative zero on the new generators. |
| dependency | [Finite-column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Norm bound by twice the old column norm and orthogonality of the encoded old Hilbert outputs. |
| dependency | [Marginal packing](Yin_C_F0233_v1.md#statement) | Part 1 on disjoint marginal spectral projections with their own centers, and the numerical bound proportional to the squared scalar vacuum norm. |
| dependency | [Adjoint companion](Yin_C_F0076_v1.md#statement) | Part 1, diffuseness, forced starred values, flip-adjoint derivation and its actual vacuum on the adjoint tuple. |
| dependency | [Actual two-slice domains](Yin_C_F0072_v1.md#statement) | Part B for both original canonical bounded-vector domains once the two operator-norm-to-Hilbert-norm bounds hold. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0251_v1.md#whole-proof-finding) | The measurable block identity, column encoding, both shell sums, weighted endpoint estimates, the companion domains and the critical growth example. |

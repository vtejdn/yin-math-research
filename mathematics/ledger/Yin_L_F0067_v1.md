---
author: Yin
---

# Independent row replacements and the truncated second eigenvalue moment

On 2026-11-08 Yin asked whether independence of the original [F0012 Wigner inputs](../tasks/Yin_T_F0012_v3.md#contract) gives the missing lower bound for the [disk-average statistic](../drafts/Yin_D_F0009.md#disk-moment).
This discussion for Yin gives a sufficient probabilistic estimate and tests the stronger bounded-differences hypothesis inside a fixed bounded Wigner law.
The derivation was checked during authoring and has not received independent review.

<a id="mean-and-influences"></a>
## The mean and the fourth moments of row replacements

Fix the polynomial \(P\), let \(A=P(W^{(N)})\), \(a=P(s)\), and take \(R>\|a\|\).
Write \(X(A)=N^{-1}\sum_j\min(|\lambda_j(A)|^2,R^2)\), \(X_N=X(A)\), and \(m=\int |w|^2\,d\mu_a^{\mathrm{Br}}(w)\).
The [disk argument](../drafts/Yin_D_F0009.md#disk-moment) gives \((X_N-m)_+\to0\) almost surely, and \(0\le X_N\le R^2\) makes the same convergence hold in mean.
Thus \(\limsup_N\mathbb EX_N\le m\).
Also \(\mathbb E(m-X_N)_+=m-\mathbb EX_N+\mathbb E(X_N-m)_+\), so \(\liminf_N\mathbb EX_N\ge m\) is already equivalent to \(X_N\to m\) in probability by boundedness.

Let \(Y_k\) consist of the upper-triangular entries in row \(k\), including the diagonal, of all input matrices at size \(N\).
The \(N\) blocks are independent.
Let \(I_{k,N}=X_N-X_N^{(k)}\), where an independent copy of \(Y_k\) replaces that block and the lower entries are reflected.
The [fourth-moment inequality of Boucheron, Bousquet, Lugosi and Massart](../audits/literature/BBLM05/Yin_U001.md#fourth-moment-resampling-bound) gives
\[
 \mathbb E|X_N-\mathbb EX_N|^4
 \le C N\sum_{k=1}^N\mathbb E|I_{k,N}|^4 .
\]
It applies under the stated finite-variance input assumptions because the statistic is bounded.
If \(\sum_N N\sum_k\mathbb E|I_{k,N}|^4<\infty\), fourth-moment Markov and first Borel--Cantelli give \(X_N-\mathbb EX_N\to0\) almost surely for every permitted cross-size coupling.
For example, \(\max_k\|I_{k,N}\|_4=O(N^{-1})\) would give a summable \(O(N^{-2})\) bound at each fixed deviation.
This is a sufficient fluctuation estimate and still requires the mean lower bound.
An alternative direct target is [summability of the uncentered one-sided marginal deviations](../drafts/Yin_D_F0009.md#wigner-lower-bound), which also supplies the mean.
Both the required mean identification and the proposed control of the random influences remain open here for arbitrary \(P\).

<a id="signed-replacement"></a>
## Exact signed integral for one replacement

Let \(A'\) denote the resampled output, \(D_R=\{|z|<R\}\), and \(g(z)=\log|\det(A'-zI)|-\log|\det(A-zI)|\).
Apply the scalar disk identity and circle mean in the [disk calculation](../drafts/Yin_D_F0009.md#disk-moment) to their eigenvalues.
Subtracting the circle contribution from the disk integral gives
\[
 X(A')-X(A)
 =\frac{2}{\pi N}\int_{D_R}g(z)\,d^2z
  -\frac{R}{\pi N}\int_{\partial D_R}g(z)\,ds(z),
\]
where \(ds\) is arclength and logarithmic roots are integrable in both terms, including on the circle.
In each input matrix a row-block replacement has rank at most two.
Telescoping each word of \(P\) one factor at a time therefore gives \(\operatorname{rank}(A'-A)\le 2\sum_{w}\deg w\), summing over its nonconstant monomials.
Factor \(A'-A=UV^*\) with at most that many columns.
Off the two spectra, the determinant identity gives \(g(z)=\log|\det(I+V^*(A-zI)^{-1}U)|\).
This specializes the [smooth-test row replacement calculation](../drafts/Yin_D_F0011.md#secondary-planar-resampling-lead) to the single radial statistic with its circle term.
An original-law fourth-moment estimate may use cancellation in this signed expression.
The fixed rank provides no such estimate on its own.

<a id="single-entry-oscillation"></a>
## Order-one oscillation at the Wigner entry scale

Take \(P(x_1,x_2)=x_1+i x_2\), \(R=5>\|s_1+i s_2\|\), and odd \(N=2q+1\ge5\).
Use the same fixed off-diagonal law for both inputs, choosing the uniform law on the complex disk of radius \(1\) with probability \(2/3\) and that on the disk of radius \(2\) with probability \(1/3\).
It is centered, has second absolute moment \((2/3)(1/2)+(1/3)2=1\), and has a bounded positive density in the open disk of radius \(2\).
Take all diagonals zero and all required upper entries independent.

Let \(J_{j,j+1}=1\) for \(1\le j<N\), with all other entries zero.
Choose a unitary \(V\) fixing all odd coordinate vectors and acting by the normalized \(q\)-point Fourier matrix on the even coordinates.
Put \(B=VJV^*\), \(H=(B+B^*)/2\), and \(K=(B-B^*)/(2i)\), so that \(P(H,K)=B\).
Every edge of the shift joins an odd and an even position.
For a fixed odd row there is at most one term of \(B\) going to even columns, and for a fixed odd column there is at most one term going to even rows.
Thus \(B\) vanishes on the two same-parity blocks, and every other entry is zero or has modulus \(q^{-1/2}\).
Both \(H,K\) have zero diagonals and raw entry moduli at most \(\sqrt{N/q}=\sqrt{2+1/q}<2\).
Their entries lie in the support of the specified product law.

Set \(h=N^{-1/2}\) and change the upper entry \(H_{1N}=0\) to \(h\), with its reflected lower entry.
All other independent entries of both matrices are fixed.
Both endpoints are odd, so the resampled output at this pair of configurations is
\[
 B'=V[J+h(E_{1N}+E_{N1})]V^* .
\]
Now \(X(B)=0\), and \(\|B'\|\le1+h<R\), so the cutoff is inactive.
The last row of the bracket has its only nonzero entry \(h\) in column one.
The complementary minor is upper triangular with unit diagonal, giving \(|\det B'|=h\).
The arithmetic-geometric mean inequality and the norm bound give
\[
 N^{-1/N}=h^{2/N}\le X(B')\le(1+h)^2 .
\]
Consequently \(X(B')-X(B)\to1\) along the odd sizes.

For fixed \(N\), \(X\) is continuous in the matrix entries because the unordered roots of a monic polynomial depend continuously on its coefficients.
The joint support of the common coordinates, original entry and independent replacement therefore gives positive probability to a jump exceeding any \(c<N^{-1/N}\).
The same conclusion holds for a whole-row resampling by taking its other replacement entries near their old targets.
Permuting the physical coordinates preserves the product support and moves the chosen edge to any upper off-diagonal position.
Thus even the essential suprema of the single-coordinate changes remain of order one for this bounded Wigner law.

These neighborhoods witness a failure of uniform bounded differences.
Their probabilities give no macroscopic lower bound on random fourth moments.
In fact one can intersect them with the condition that every original even-even upper off-diagonal entry of the first input has raw modulus below \(1/2\), while still keeping a neighborhood of the displayed pair.
The resulting event has probability at most \((3/16)^{q(q-1)/2}\) by independence and the disk law.
The size of the whole lower-deviation event and the typical effect of a fresh row remain to be estimated.

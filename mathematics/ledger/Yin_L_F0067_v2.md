---
author: Yin
---

# Independent row replacements and paired border growth

The [original row-replacement finding](Yin_L_F0067_v1.md) retains the fourth-moment sufficient condition, exact signed integral and order-one uniform-influence obstruction.
On 2026-11-09, a delegated research agent for Yin investigated whether sequential row exposure could instead supply the missing lower logarithmic bound in [F0012](../tasks/Yin_T_F0012_v3.md#contract).
This revision retains the paired-border calculation, its source comparison, a final one-dimensional cancellation and its exact planar cost in a fixed-law example.
The derivations were checked during authoring, with no independent proof review or accepted Claim assessment.

<a id="paired-border-growth"></a>
## Paired row and column growth of singular products

The source SSS25, inspected at [arXiv:2310.17600v2, Sections 2, 7 and 8](https://arxiv.org/html/2310.17600v2#S7), compares a full logarithmic determinant to a truncated singular-product sum of a large principal minor by sequential row and column exposure.
Its Lemma 7.2 gives a deterministic lower bound for the product of the largest \(r+1\) singular values after one row is added, in terms of the old largest \(r\) singular values and the fresh row's projection onto the remaining right-singular space.
The probabilistic step in Lemma 7.1 uses fresh randomness at each half-step.
Original Wigner symmetry couples the newly added row and column, so that second conditional independence requires a new argument.
The following deterministic paired-step deduction permits arbitrary dependence between the two borders.
It is a continuing investigation and has not received independent review.

Let \(M\in\mathbb C^{n\times n}\), \(u,v\in\mathbb C^n\), \(d\in\mathbb C\), and
\[
 B=\begin{pmatrix}M&u\\v^*&d\end{pmatrix}.
\]
Write singular values in decreasing order and \(p_j(T)=\prod_{i=1}^j s_i(T)\), with \(p_0=1\).
Fix \(0\le r\le n-2\) and a singular-vector decomposition of \(M\).
Let \(Q_L\) project onto its left-singular vectors indexed \(r+2,\ldots,n\), and let \(Q_R\) project onto its right-singular vectors indexed \(r+1,\ldots,n\).
Then
\[
 p_{r+2}(B)\ge\frac12p_r(M)\|Q_Lu\|\,\|Q_Rv\|.
 \tag{Paired-growth}
\]
The estimate is uniform in \(d\) and requires no invertibility of \(M\), probability law, or independence of \(u,v\).

If \(p_r(M)=0\), the right side vanishes and the assertion follows from nonnegativity.
Otherwise apply the singular-vector changes of bases and write
\[
 M=\begin{pmatrix}D_1&0\\0&D_2\end{pmatrix},\qquad
 u=\binom{u_1}{u_2},\quad v=\binom{v_1}{v_2},\qquad
 \alpha=d-v_1^*D_1^{-1}u_1.
\]
Here \(D_1\) consists of the first \(r\) singular values, and empty blocks have their natural meaning when \(r=0\).
Compress the exterior-power map \(\bigwedge^{r+2}B\) to the orthonormal exterior bases containing all first \(r\) coordinates, one tail coordinate and the new coordinate.
Its resulting matrix is
\[
 p_r(M)(\alpha D_2-u_2v_2^*).
\]
Since \(\|\bigwedge^{r+2}B\|=p_{r+2}(B)\), compression gives
\[
 p_{r+2}(B)\ge p_r(M)\|\alpha D_2-u_2v_2^*\|.
\]
Set \(E=u_2v_2^*-\alpha D_2\), and let \(Q\) remove the first coordinate of the tail left-singular space.
Choose a unit vector in the span of the first two tail right-singular directions that is orthogonal to \(v_2\).
On this vector \(E=-\alpha D_2\), so \(|\alpha|s_2(D_2)\le\|E\|\).
Since \(\|QD_2\|=s_2(D_2)\), it follows that
\[
 \|Qu_2\|\,\|v_2\|
 =\|Qu_2v_2^*\|
 \le\|QE\|+|\alpha|\|QD_2\|
 \le2\|E\|.
\]
This proves (Paired-growth).
Applying the same result to \(B^*\) gives the symmetric variant with the extra removed direction on the right.

Condition on an old matrix \(M\), and put \(h=n-r\ge2\).
Any conditional estimates
\(\mathbb P(\|Q_Lu\|<a_h\mid M)\le q_L\) and
\(\mathbb P(\|Q_Rv\|<b_h\mid M)\le q_R\)
give (Paired-growth) with gain at least \(a_hb_h/2\) outside probability \(q_L+q_R\), by the union bound.
Thus a simultaneous physical row and column addition can increase the number of controlled singular values by two while increasing the matrix dimension by one.
At scales \(a_h,b_h\) of order \(\sqrt{h/N}\), the normalized logarithmic cost of such a successful step is of order \(N^{-1}(1+\log(N/h))\).
The statement of that scale is conditional on the projection estimates and supplies no such estimates for a general coefficient tuple.

<a id="paired-border-terminal"></a>
## The final one-dimensional tail and the polynomial interface

At \(h=1\), the exterior compression is the scalar
\(p_{n-1}(M)(\alpha s_n(M)-u_2\overline{v_2})\).
Both projected borders can be nonzero while this scalar vanishes.
For example, take \(M=I_n\), \(d=1\), and \(u=v=n^{-1/2}(\varepsilon_1,\ldots,\varepsilon_n)^T\) with independent Rademacher signs.
Every coordinate projection of either border has norm \(n^{-1/2}\), yet \(\det B=\det M(1-u^*u)=0\) for every border sample.
This is a conditional obstruction for a deterministic background and legal independent border coordinates.

There is also a positive-probability realization of terminal cancellation inside a fixed Wigner law at one fixed real parameter.
Take zero diagonals and the fixed real off-diagonal law assigning masses \(1/2,1/4,1/4\) to \(0,\sqrt2,-\sqrt2\).
For even \(N\), put \(n=N-1\), condition on every entry of the old \(n\times n\) Wigner minor being zero, and shift the full matrix by \(z=1\).
This old-background event has probability \(2^{-n(n-1)/2}\).
The shifted old block is \(M=-I_n\), the new diagonal is \(d=-1\), and the fresh border has the unchanged independent original law scaled by \(N^{-1/2}\).
Writing \(K\) for its number of nonzero entries gives
\[
 \det B=\det(-I_n)(-1+2K/N).
\]
On \(K=N/2\) the determinant vanishes.
For the singular-vector choice using the last coordinate as the tail, the event that this coordinate is nonzero and \(K=N/2\) has conditional probability
\[
 \frac12\,2^{-(N-2)}\binom{N-2}{(N-2)/2}
 =\Theta(N^{-1/2}),
\]
and both border projections have norm \(\sqrt{2/N}\).
The exponentially rare old background prevents this from giving a nonsummable unconditional obstruction or a counterexample to F0012.

Planar integration does remove the difficulty in this particular zero-background example.
For arbitrary \(z\), its full characteristic determinant is
\[
 \det(W^{(N)}-zI)=(-z)^{n-1}(z^2-\|u\|^2).
\]
After the first \(n-1\) old singular factors, the remaining logarithmic term is \(\log|z^2-\|u\|^2|\).
For every disk \(D_R\), its negative part has integral at most \(\pi\), since \(\log^-|z-a|\) has whole-plane integral \(\pi/2\) and there are two roots.
Its normalized integrated negative contribution is therefore at most \(\pi/N\), including on the terminal atom event.
For a general old block depending on \(z\), the Schur scalar is rational with dimension-dependent numerator and denominator degrees, so this two-root estimate supplies no uniform terminal bound.

For a noncommutative polynomial, physical principal compression does not commute with evaluation of \(P\).
An application must use an exact affine linearization, where one physical addition introduces a fixed auxiliary block of rows and columns sharing the same fresh input borders.
The scalar inequality above alone does not control simultaneous auxiliary directions or their dependence after partial exposure.
The next concrete test is a block counterpart of (Paired-growth) for the actual coefficient maps, retaining its complete Schur block and a logarithmic cost summable over the added physical indices.
Even a successful block inequality would still require original-law projection estimates and a terminal small-dimensional Schur estimate, potentially after integration in \(z\).

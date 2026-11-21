---
author: Yin
---
# Recovery of cyclic edge boundaries from finitely many conjugates of the kernel

## Statement

Let \(G=N\rtimes\langle z\rangle\) with \(z\) infinite cyclic, \(H=\langle z\rangle\), \(B=\mathcal N(H)\), and \(\sigma=\operatorname{Ad}(z)\).
Use \(U(G)=L^0(\mathcal N(G))\) for the affiliated algebra and use the canonical subgroup inclusion for \(U(N)\).
Suppose that every element of \(G\setminus H\) has infinite orbit under conjugation by \(z\).
Let \(K\subset U(N)\) be a unital complex division subring closed under adjoints, with \(\sigma(K)=K\).
The skew Laurent ring \(K[z,z^{-1};\sigma]\) has its fraction division ring \(F\) inside \(U(G)\).
Then \(F\cap U(H)=\mathbb C(z)\).

Let \(Y=Y_1+Y_2\) be a bounded selfadjoint \(n\)-square matrix, with bounded selfadjoint summands having entries in \(F\), and put \(p=P_{\ker Y}\).
Assume the support of its entrywise conditional expectation \(E_H(p)\) is \(I_n\).
Then \(p\in M_n(F)\), its unnormalized trace \(r\) is a positive integer, and
\[
 S_m=\sum_{k=0}^{m}z^kpz^{-k},\qquad m=n-r,
\]
is invertible in \(M_n(F)\).
Here \(z\) acts diagonally, and the inverse is taken in the affiliated algebra.
Any \(b_j\in M_n(B)\) satisfying \((Y_j-b_j)p=0\) is recovered by
\[
 b_j=\left(\sum_{k=0}^{m} z^kY_jp z^{-k}\right) S_m^{-1}
       \in M_n\bigl(\mathbb C(z)\cap B\bigr).
\]
Thus the procedure uses only the input matrices, field operations and their kernel over \(F\).
If the summands are free over the amplified base \(M_n(B)\) and \(E_H(p)\) is boundedly invertible, the actual norm boundary coefficients at zero exist and satisfy the formula by BBL21.
In particular this recovers rational boundary coefficients for every such finite vertex pencil on \(F(z,a)*_{\langle z\rangle} F(z,b)\), without prescribing its denominator or requiring a polynomial kernel vector.

For arbitrary expected support \(q=s(E_H(p))\), the support projection itself has entries in \(\mathbb C(z)\cap B\).
The same finite joins stabilize at \(q\), including when \(q\ne I_n\).
If a bounded edge matrix satisfies the kernel relation, its restriction \(b_jq\) is recovered rationally using the inverse on that corner.

## Argument

### The fraction ring in the regular representation

For a finite list \(A_i\in U(N)\) there is a common left clearing factor \(c\in\mathcal N(N)\), injective with dense range, for which each \(cA_i\) is bounded.
Indeed take the bounded transform \(c=(1+TT^*)^{-1/2}\) of the affiliated row \(T=(A_i)_i\), using rectangular matrix amplification.
Its product with \(T\) is bounded by one by the polar decomposition, and \(c\) has zero kernel.
We use closed products and sums throughout the finite tracial affiliated algebra.

After shifting the lowest exponent, a nonzero formal skew polynomial has the form \(P=\sum_{i=0}^d A_i z^i\) with \(A_0,A_d\ne0\) in \(K\).
Clear its coefficients on the left as above and put \(C_i=cA_i\).
The bounded end coefficients have zero kernel since they are products of affiliated units.
For \(d=0\) the assertion of invertibility is immediate.
Otherwise express a vector as \(\xi=\sum_{l\in\mathbb Z}\xi_l z^l\), where the coefficients belong to \(L^2(\mathcal N(N))\).
For \((cP)\xi=0\) one has
\[
 \sum_{i=0}^d C_i\,\sigma^i(\xi_{l-i})=0\qquad(l\in\mathbb Z).
\]
Any \(d\) consecutive zero coefficients force every coefficient to be zero, using \(C_0\) to proceed forward and \(C_d\) to proceed backward.
Restriction to \(d\) fixed consecutive slices is therefore a bounded injective right \(N\)-module map on the Hilbert kernel.
Right multiplication on slice \(l\) is twisted by \(\sigma^l\), so each slice is unitarily isomorphic, as a right \(N\)-module, to a regular copy.
The polar decomposition of the restriction gives \(\dim_N\ker(cP)\le d\).
On the other hand the kernel projection \(e\) is in \(\mathcal N(G)\), and its \(N\)-dimension is the sum of the diagonal traces on all slices.
The distinguished unit vector of slice \(l\) is \(\delta_{z^l}\), giving diagonal trace \(\langle e\delta_{z^l},\delta_{z^l}\rangle=\tau_G(e)\) by right translation.
The sum can be finite only when \(e=0\).
Finite tracial polar decomposition then gives dense range of \(cP\), so \(cP\), and hence \(P\), is an affiliated unit.
This proves faithfulness and invertibility for the skew polynomial ring without an Atiyah premise on the ambient group.
The Euclidean algorithms over \(K\) give the left and right skew field of fractions, which now embeds in \(U(G)\) by Ore localization.
It is closed under adjoints since the original ring is.

### Its intersection with the edge algebra

Let \(b\in F\cap U(H)\).
Choose \(Q\ne0,P\) in the skew Laurent ring with \(Qb=P\), and write \(b=u/v\) in the commutative affiliated algebra \(U(H)\), with \(u,v\in B\) bounded and \(v\) nonzero almost everywhere.
For example \(v=(1+|b|)^{-1}\) works.
Clear the two finite lists of coefficients on the left simultaneously to get bounded Laurent sums \(Q'=\sum_i C_i z^i\ne0,\ P'=\sum_i D_i z^i\) with \(Q'u=P'v\).
Writing \(u_l,v_l\) for their scalar Fourier coefficients (of \(u,v\)), the equality on slice \(l\) reads
\[
 \sum_i C_i u_{l-i}=\sum_i D_i v_{l-i}\qquad\text{in }L^2(\mathcal N(N)).
\]
Indeed the expansions of \(u,v\) converge in \(L^2\), multiplication by each bounded sum is continuous there, and the Fourier coefficients of \(u,v\) are scalar.
Choose a continuous complex linear functional on \(L^2(\mathcal N(N))\) detecting one nonzero \(C_i\).
Applying it coefficientwise gives \(q(z)u=s(z)v\) with scalar Laurent polynomials \(q\ne0,s\).
Thus \(b=s/q\).
The opposite inclusion holds because \(\mathbb C\subset K\) and \(z\) is the regular cyclic generator.
This intersection calculation requires no hypothesis on conjugation orbits.

### Kernel projections and the translate sum

Gaussian elimination over \(F\) gives a right kernel basis \(W\) of \(Y\), with \(r\) columns.
The same invertible row and column operations in \(U(G)\) identify the full algebraic null module with \(W U(G)^r\) and give \(W\) a left inverse.
For \(r>0\), the Gram \(W^*W\) is invertible over \(F\): a column in its \(F\)-kernel would have \((Wv)^*(Wv)=0\), which by positivity in the affiliated algebra forces \(Wv=0\), hence \(v=0\).
Consequently \(W(W^*W)^{-1}W^*\) is a selfadjoint projection with exactly this right image.
Affiliated selfadjoint projections are bounded.
For a bounded \(Y\), its analytic kernel projection generates the same algebraic null module by the support identity or affiliated pseudoinverse.
The two projections therefore agree.
Polar decomposition of the rectangular \(W\) gives unnormalized trace \(r\) since its initial support is \(I_r\).
The zero-column case gives \(p=0\), excluded here by the support hypothesis.
The same reasoning computes the range projection and integer trace of any finite matrix over \(F\) using an independent column basis.

Let \(q_t\) be the join of \(p,\sigma(p),\ldots,\sigma^t(p)\), with entrywise conjugation.
It is the range projection of their concatenation and thus has integer trace.
Whenever \(q_{t+1}=q_t\), \(\sigma(q_t)\le q_t\); equality of traces gives equality of projections.
The fixed algebra of \(\sigma\) on \(\mathcal N(G)\) is \(B\): a fixed element has square-summable Fourier coefficients constant on each orbit, so all coefficients outside \(H\) vanish.
Every element of \(B\) is fixed.
It follows that a stationary \(q_t\) is an edge projection containing \(p\), and hence \(E_H(p)=q_t E_H(p)q_t\) forces \(q_t=I_n\).
Every step below \(I_n\) therefore increases the integer trace by at least one.
Starting at trace \(r\) proves \(q_{n-r}=I_n\).
The positive sum \(S_m\) has exactly that support, giving trivial analytic kernel.
It is invertible over \(F\) by finite-dimensional linear algebra and the kernel comparison above.
Conjugation fixes all entries of \(b_j\); summing \(z^kY_jp z^{-k}=b_j z^kpz^{-k}\) proves the recovery formula.
The recovered entries belong to \(F\cap B\), and the intersection calculation applies entrywise.
Rational elements bounded on the circle in the essential sense have no uncancelled pole there, but an inverse of \(S_m\) bounded as an ambient operator is unnecessary.

### Deficient expected support

For any \(p\), positivity and faithfulness show that \(q=s(E_H(p))\) is the least edge projection containing \(p\).
Indeed \(E_H((I-q)p(I-q))=0\) gives \(p\le q\), and any edge projection containing \(p\) contains the support of its expectation.
Conjugation fixes \(q\), so \(q_t\le q\) for all \(t\).
At any plateau \(q_{t+1}=q_t\), the same fixed-algebra proof makes \(q_t\) an edge projection containing \(p\), hence \(q_t=q\).
Starting at trace \(r\), either a plateau occurs before \(n-r\) increases, or the trace reaches \(n\) and \(q=I_n\).
Thus \(q_{n-r}=q\) in every case, including \(p=0\).
This identifies \(q\) with a range projection over \(F\) and puts its entries in \(F\cap B\).
Write \(S=S_{n-r}\), \(L_j=\sum_{k=0}^{n-r} z^kY_jp z^{-k}\).
Since \(S+I-q\) is injective it is invertible over \(F\), and \(S(S+I-q)^{-1}=q\).
For a bounded edge solution \(b_j\), \(L_j=b_j S\) gives \(b_jq=L_j(S+I-q)^{-1}\in M_n(F\cap B)\).
This computes the determined action on the expected support.
It neither asserts existence of a boundary limit on a deficient support nor determines its unrestricted action on the complementary corner.

### The free cyclic amalgam

For \(G=F(z,a,b)\) retract to \(H\) by killing \(a,b\) and take \(N\) to be the kernel.
This subgroup is free, and its complex group ring lies in a division ring of affiliated operators: use the known [free-group division-ring result and directed union passage](../audits/literature/Lin00/Yin_U004.md#lin00-u004).
Equivalently one can take the division subring generated by \(\mathbb C N\) in the ambient free-group division ring; the subgroup embedding of affiliated algebras preserves actual inverses.
The division closure of \(\mathbb C N\) in \(U(N)\) is adjoint- and \(\sigma\)-invariant.
Thus \(F\) contains every group polynomial on \(G\).
The centralizer of every \(z^l\), \(l\ne0\), in this free group is \(H\), for instance by the reduced free-product normal form on \(H*F(a,b)\).
This verifies the infinite-orbit hypothesis.
Matrices from its two vertex algebras are free over the amplified edge base in the usual sense of centered alternating products.
With the bounded inverse of the expected kernel, [BBL21, Theorems 3.2 and 3.5(vii), arXiv v2](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) supplies the actual norm limits with \((Y_j-b_j)p=0\).
This recovers the nonpolynomial coefficients of [v7](Yin_C_A0007_v7.md#statement) as part of a whole class.
The proof needs the cyclic splitting, the coefficient division ring and the specified fixed algebra; these conditions are not available for arbitrary torsion-free amalgams.

## Assessment history

### Decision cyclic-conjugate-recovery

| Field | Value |
| --- | --- |
| date | 2026-11-21T03:45 |
| status | proved |
| reason | Independent inspection supports the entire statement and argument at their stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cyclic fraction field, rational expected support and recovery of every determined boundary coefficient. |
| argument | [Proof](#argument) | Complete skew-ring, trace, orbit and corner proof, including the free amalgam application. |
| review | [Whole finding](../audits/reviews/Yin_R_A0020_v8.md#whole-finding) | Complete independent finding on the final proof and direct inputs. |
| dependency | [Free group input](../audits/literature/Lin00/Yin_U004.md#lin00-u004) | Actual division closure of the complex free group ring for the final application. |
| dependency | [Subordination](../audits/literature/BBL21/Yin_U001.md#bbl21-u001) | Norm boundaries and meet conclusion under bounded invertibility. |

## Current assessment

[Selected decision](#decision-cyclic-conjugate-recovery)

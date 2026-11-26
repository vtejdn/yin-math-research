---
author: Yin
---

# Rational kernel projections from the least occupied coset

## Statement

Let \(H\lhd G\) be discrete groups and fix a right-invariant total order on \(G/H\).
Write \(M_J=\mathcal N(J)\), \(U_J=L^0(M_J)\) and \(D_J=\operatorname{Div}_{U_J}(\mathbb CJ)\), and use unnormalized matrix traces for ranks.
Let \(A\) be a nonzero \(m\)-by-\(n\) matrix with finite coset support and bounded coefficients in \(D_H\).
Thus \(A=\sum_c B_c g_c\) with \(B_c\in M_{m,n}(D_H\cap M_H)\) and \(g_cH=c\).
Let \(B\) be the coefficient on the least occupied coset, put \(q=s(BB^*)\) and assume \(q\in M_m(D_H)\).
Set \(r_0=\operatorname{rk}_H B\) and \(r=\operatorname{rk}_G A\).
Then \(\overline{\operatorname{ran}(qA)}=q\ell^2(G)^m\), and
\[
 P=I_n-A^*q(I_m-q+qAA^*q)^{-1}qA\in M_n(D_G),
 \qquad P\ge p_{\ker A},\qquad
 (\operatorname{Tr}_n\otimes\tau_G)(P-p_{\ker A})=r-r_0.                 \tag{1}
\]
In particular \(P=p_{\ker A}\) exactly when \(AP=0\), or equivalently \(r=r_0\).
The subgroup projection and this one rational identity suffice to recover the kernel, even if \(B\) has both a kernel and a cokernel.
For any scalar \(u=\epsilon A^{[-1]}\gamma\) with constant row and column, this gives \(u\in D_G\) whenever \(AP=0\).
Every solution of the [unrestricted finite-rank equation](Yin_C_A0131_v1.md#statement) has such a realization with \(A\) over \(\mathbb CG\). [Relative inverse realization](Yin_C_A0137_v1.md#single-vector-vanishing-and-equation-1)

When \(G/H=\mathbb Z\), take \(t\) of height one and suppose \(A\) has heights in \([0,w]\).
Let \(T_N(A)\) be the compression to the same \(N\) input and output heights \(0,\ldots,N-1\), and put \(h_N=\operatorname{rk}_H T_N(A)\), \(h_0=0\).
Then
\[
 b_j=h_{j+1}-h_j \ \uparrow\ r,\qquad
                       \sum_{j\ge0}(r-b_j)\le wr .                         \tag{2}
\]
If \(D_H\) is regular, each \(b_j\) gives an explicit rational projection above \(p_{\ker A}\) of excess trace exactly \(r-b_j\).
One can test whether it is the full answer by multiplying it on the left by \(A\).
For \(N\ge1\) the projection from \(b_{N-1}\) has excess trace at most \(wr/N\).

Eventual attainment \(b_j=r\) for every square group-ring matrix that is an affiliated unit, over all finitely generated torsion-free groups equipped with an epimorphism onto \(\mathbb Z\) and all choices of nonnegative height support, is equivalent to the complex strong Atiyah conjecture throughout the finitely generated torsion-free class.
Thus finite attainment in this fixed direction can fail conditionally even for a zero kernel.

## Argument

### The ordered quotient

Write \(g_0\) for the representative of the least occupied coset and set \(A'=A(g_0^{-1}I_n)\).
Right invariance of the order makes the identity its least coset.
Using the representatives \(g_cg_0^{-1}\) leaves \(B\) as the identity coefficient.
Replacing \(g_c\) by \(h g_c\), \(h\in H\), would replace \(B_c\) by \(B_ch^{-1}\), which preserves its final support.

Write \(B=v|B|\) and \(e=v^*v\) in matrices over \(M_H\), so \(vv^*=q\).
Consider the bounded square matrix
\[
                         C=I_n-e+v^* A'e .
\]
Its identity coefficient \(I_n-e+|B|\) is injective, including when \(B\) has nonclosed range.
Multiplication on the right by \(e\) preserves every coset since \(g e g^{-1}\) belongs to \(M_n(M_H)\) for every \(g\in G\).
The other coefficients therefore lie strictly above the identity.

To apply Linnell's scalar theorem, take a finite group \(F\) with a matrix summand \(M_n(\mathbb C)\) in \(\mathbb CF\).
For example the permutation representation of \(S_{n+1}\) on the sum-zero subspace is irreducible of degree \(n\), since subtracting a transposed vector from a vector with two differing coordinates gives a multiple of a coordinate difference and the permutation orbit spans the subspace.
In \(M_{G\times F}=M_G\overline\otimes\mathbb CF\), put \(C\) on this summand and the identity on all the others.
The resulting scalar is bounded, hence gives an \(\ell^2(G\times F)\) coefficient vector, with least coset the identity of \((G\times F)/(H\times F)\).
Its least coefficient has zero Hilbert kernel on the regular representation of \(H\times F\), since on the chosen summand it acts columnwise by \(I_n-e+|B|\).
It therefore kills no nonzero right multiplier in \(M_{H\times F}\).
Linnell's Theorem 4 gives zero kernel on \(\ell^2(G\times F)\), hence injectivity of \(C\) on \(\ell^2(G)^n\). [Lin92, pp. 50–51](https://math.uchicago.edu/~shmuel/L%5E2%20cohomology%20readings/Linnell,%20zerol2.pdf)

On \(e\ell^2(G)^n\), this gives injectivity of \(v^*A'e\).
Consequently \(qA'e\) has rank \((\operatorname{Tr}_n\otimes\tau_H)(e)=r_0\) by polar decomposition.
Its range lies in the range of \(q\), which has the same trace, so \(qA'\), and hence \(qA\), has final support \(q\).
The positive operator \(I_m-q+qAA^*q\) is then an affiliated unit, acting as the identity on \(1-q\) and injectively on \(q\).
Its inverse has rational entries by [scalar Gram elimination](Yin_C_A0132_v1.md#argument).
Polar decomposition identifies the subtracted term in (1) with the initial support of \(qA\).
Thus \(P=p_{\ker(qA)}\), and inclusion of kernels and their dimensions give (1).
At equality \(A^{[-1]}=(A^*A+P)^{-1}A^*\), which proves the assertion for \(u\).

### Truncating the output in a cyclic quotient

First allow bounded coefficients in \(M_H\).
For a matrix \(L\) supported in nonnegative heights, let \(B_L\) be its height-zero coefficient, possibly zero, and set \(q_L=s(B_LB_L^*)\).
Replace \(L\) by the vertical stack
\[
                  L'=\binom{q_L L}{t^{-1}(1-q_L)L}.
\]
The stack on the output is an isometry, so \(L'\) has the same kernel and rank as \(L\).
Its heights are still nonnegative because the second part before translation has zero constant coefficient.
Starting from \(L_0=A\), iterate this step to form \(L_j\).
Write \(\beta_j=\operatorname{rk}_H B_{L_j}\).
The ordered-quotient argument gives \(\beta_j\le r\), also when the constant coefficient vanishes.
If \(D_H\) is regular then the final support of each coefficient matrix is rational by matrix regularity, and conjugation by \(t\) preserves \(D_H\).
All the coefficients of every \(L_j\) are consequently bounded and rational over \(H\).
Applying (1) to \(L_j\) gives the required rational upper projection once \(\beta_j=b_j\) is established.
For a zero constant coefficient the same formula with \(q=0\) gives \(I_n\).

Identify height \(i\) with \(t^iH\) using left translation and truncate all systems on columns over \(U_H\).
For \(k\ge1\), let \(S_k(L)\subseteq U_H^n\) consist of the possible height-zero coordinates of solutions of \(T_k(L)x=0\).
These are finitely generated projection modules, being coordinate images of kernels of finite affiliated matrices.
Restriction of a solution to its first \(k\) coordinates gives \(S_{k+1}(L)\subseteq S_k(L)\).
For every \(k\ge1\) one has \(S_k(L')=S_{k+1}(L)\).
Indeed the first part of \(L'\) imposes the \(q_L\) output equation through height \(k-1\), and the second imposes the complementary output equation through height \(k\), with the equation at height zero automatic.
At height \(i\), the indicated output projections have been conjugated by \(t^{-i}\).
The complementary equation at height \(k\) is independent of the as yet unspecified \(x_k\), since its diagonal coefficient is zero.
The missing \(q_L\) equation there can always be solved for \(x_k\), since the diagonal coefficient \(t^{-k}B_Lt^k\) maps the affiliated column module onto \((t^{-k}q_Lt^k)U_H^{\mathrm{rows}(L)}\).
Conversely every solution through height \(k\) satisfies these truncated equations after its last coordinate is dropped.
This uses surjectivity onto the final support in affiliated modules and requires no bounded inverse.

The kernel of first-coordinate extraction on \(\ker T_{j+1}(A)\) has dimension equal to the nullity of \(T_j(A)\).
Indeed a zero first coordinate leaves the same \(j\) input and output equations shifted one height, with a common trace-preserving conjugation of the coefficient algebra.
The dimension of \(S_{j+1}(A)=S_1(L_j)\) is therefore \(n-b_j\), and it also equals \(n-\beta_j\) by the constant coefficient equation.
This gives \(b_j=\beta_j\), and their monotonicity follows from inclusion of the \(S_k(A)\).

For \(N>w\), restrict the inputs to the first \(N-w\) heights.
All their outputs lie in the \(N\) tested heights, and the \(H\)-dimension of the kernel on those inputs is at most \((N-w)(n-r)\) by [coset trace compression](Yin_C_A0134_v1.md#finite-coset-matrices).
Hence \(h_N\ge (N-w)r\), which also holds for \(N\le w\) by positivity.
It follows that \(\sum_{j<N}(r-b_j)=Nr-h_N\le wr\), giving (2) and the stated bound on the last deficit.
For instance the binary lamplighter row \([1-tp,-t(1-p)]\) has \(b_0=r=1\).
The closed right-\(G\) span of the translates of its kernel vectors supported on \(N\) consecutive heights has \(G\)-dimension \(1-2^{-N}\). [Interval kernel calculation](Yin_C_A0136_v1.md#strict-growth-with-a-rational-kernel-in-the-lamplighter-group)

### Finite attainment on square units

Under the strong Atiyah conjecture throughout the stated class all \(h_N\) of group-ring matrices are integers.
Each finite compression has its coefficients in a finitely generated torsion-free subgroup of \(H\), whose regular trace agrees with the trace in \(H\).
The increasing bounded integer increments then attain their limit.

Conversely suppose a finitely generated torsion-free \(K\) fails the complex strong Atiyah conjecture.
The [weighted shift construction](Yin_C_A0146_v1.md#statement) gives a finitely generated torsion-free \(H=K\wr\mathbb Z\) and a bounded \(v\in D_H\) with \(\operatorname{rk}_H v^N=\theta^N\) for every \(N\ge1\), where \(0<\theta<1\).
In \(G=H\times\langle t\rangle\), the scalar \(t-v\) is an affiliated unit by the same result.
Its \(N\) truncated equations give \(x_{i-1}=vx_i\) for \(1\le i<N\) and \(v x_0=0\).
The last coordinate thus identifies the truncated kernel with \(\ker v^N\) on affiliated columns.
Its rank increment is \(1-(1-\theta)\theta^j\) at \(j\ge0\).

Choose a realization \(v=\alpha Q^{-1}\gamma\) over \(\mathbb CH\) with a square affiliated unit \(Q\) of size \(d\) and constant borders. [Rational realization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
The group-ring matrix \(\left(\begin{smallmatrix}t&\alpha\\ \gamma&Q\end{smallmatrix}\right)\) is an affiliated unit by Schur elimination.
Every truncation admits the same elimination because \(Q,\alpha,\gamma\) act within each height.
Its \(N\)-height rank is \(Nd+h_N(t-v)\), and every increment is strictly less than its global rank \(d+1\).
This proves the converse for group-ring square units.
The equivalence concerns attainment in the chosen direction, while the kernel projection in this construction is already rational.

## Assessment history

### Decision least-coset-and-finite-heights

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:01 |
| status | proved |
| reason | An injective compression on the least coset gives a rational upper projection, and the cyclic truncation deficits sum to at most the width times rank. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The rational upper projection, the cyclic rank estimates and the equivalence for finite attainment on square units. |
| argument | [Argument](#argument) | Ordered compression, dimension increments, deficit sum and the linearized weighted shift. |
| dependency | [Unrestricted equation](Yin_C_A0131_v1.md#statement) | The regular closure and the torsion-free Atiyah interface. |
| dependency | [Relative inverse realization](Yin_C_A0137_v1.md#single-vector-vanishing-and-equation-1) | Representation by a rationally bordered relative inverse. |
| dependency | [Gram elimination](Yin_C_A0132_v1.md#argument) | Scalar division closure of entries of the square inverse. |
| dependency | [Coset compression](Yin_C_A0134_v1.md#finite-coset-matrices) | The finite-interval kernel dimension bound. |
| dependency | [Interval kernel](Yin_C_A0136_v1.md#strict-growth-with-a-rational-kernel-in-the-lamplighter-group) | Ranks of the translated interval kernel spans. |
| dependency | [Weighted shift](Yin_C_A0146_v1.md#statement) | Ranks of powers from a nonintegral input. |
| dependency | [Rational realization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | A square group-algebra unit with constant borders. |
| review | [Least coset and finite heights](../audits/reviews/Yin_R_A0180_v1.md#least-coset-and-finite-heights) | Independent review of the statement and argument. |

## Current assessment

[Selected decision](#decision-least-coset-and-finite-heights)

---
author: Yin
---

# An invertible lamp matrix singular at every one-marker period

## Statement

Let \(K\) be finitely generated, let \(b\) be a projection in \(D_K=\operatorname{Div}_{\mathcal U(K)}(\mathbb CK)\) with group trace \(\beta\in(0,1)\), and put \(W=(K\times\mathbb Z)\wr\mathbb Z\).
The lamp at height \(i\) supplies a copy \(b_i\) of \(b\) and the canonical unitary \(x_i\) of its additional infinite cyclic factor.
The \(b_i\) are independent Bernoulli variables and the \(x_i\) are independent Haar circle variables, independent also of the \(b_i\).
The shift acts on their joint law by translation of the height.
Mark a height \(i\) when \(b_{i-1}=0,\ b_i=1\).

There is a two-by-two matrix \(P\), polynomial in \(b_0,x_0\), their translates and the shift, with the following properties.

1. \(P\) is invertible over \(\mathcal U(W)\).
   At every decorated periodic word with a single marked height per displayed period, its evaluation has kernel dimension one over the field \(\mathbb C(z)\), with \(z\) denoting translation through the period.
   In particular this holds on every \(1^n0^m\), whatever circle labels are chosen within the two runs and then repeated.
   The assertion concerns evaluation of the indicated commutative observations and the shift.
2. For \(q\ge1\), identify \(x_{i+q}=x_i\) while keeping the \(K\)-lamps independent, in the quotient
   \[
       W_q=\bigl(K^{(\mathbb Z)}\times\mathbb Z^q\bigr)\rtimes\mathbb Z .
   \]
   Its shift cyclically permutes the \(q\) extra generators.
   The unnormalized kernel dimension of the same formula in \(W_q\) is
   \[
       \beta(1-\beta)\Pr(N+M\equiv0\pmod q)>0 ,
   \]
   where \(N,M\) are independent run lengths on the positive integers with
   \(\Pr(N=n)=(1-\beta)\beta^{n-1}\) and \(\Pr(M=m)=\beta(1-\beta)^{m-1}\).
   These dimensions tend to zero, and \(W_q\) tends to \(W\) as a marked group for the common shift and lamp generators.
3. Alternatively reduce each infinite cyclic lamp independently modulo \(d\ge1\), giving \((K\times C_d)\wr\mathbb Z\).
   The unnormalized kernel dimension is then \(\beta(1-\beta)/d\).

One fixed square group-ring matrix \(A\) over \(\mathbb CW\) is invertible over \(\mathcal U(W)\) and has exactly the displayed nullities in the two families of group quotients.
For \(K=C_2\) one can use \(b=(1+k)/2\) for the nontrivial \(k\in C_2\) and \(A=4P\in M_2(\mathbb ZW)\).
For torsion-free \(K\) admitting the stated projection, \(W\) and every \(W_q\) are torsion-free.
This gives an obstruction to preserving rational denominators when transferring the [two-run lamp construction](Yin_C_A0173_v1.md#kernel-on-two-consecutive-runs).
The rationality of its kernel projection in the full torsion-free group algebra's division closure is still open.

## Argument

### The equations on one return interval

Use the regular crossed-product representation of the commutative lamp observations and the shift on the two-sided integer heights.
The trace representation follows from independence of the direct factors in the lamps and vanishing of the group trace at every nonzero shift power, as for [independent lamp projections](Yin_C_A0164_v1.md#independent-projections-at-the-lamps).
These facts also apply in the quotient models with their indicated joint laws.
Write \(S c(i)=c(i-1)\), let \(X\) multiply by \(x_i\), let \(E\) multiply by the marker \(e_i=(1-b_{i-1})b_i\), and put \(Q=I-E\).
Take
\[
       P=\begin{pmatrix}
          Q(I-S)-EX & E\\
          -EXS & Q(I-S)+ES
          \end{pmatrix}.
\]
At an unmarked site the two equations on \(P(c,d)^{\mathsf T}=0\) give \(c_i=c_{i-1}\) and \(d_i=d_{i-1}\).
At a marked site they give \(d_i=x_ic_i\) and \(d_{i-1}=x_ic_{i-1}\).
For two successive marks \(i<j\), the pair \((c,d)\) is therefore constant on \([i,j)\), and its constants satisfy both \(d=x_ic\) and \(d=x_jc\).
That cell contributes one independent kernel vector if \(x_i=x_j\), and zero otherwise.
Almost surely the marks extend indefinitely in both directions, since disjoint two-bit trials each have positive success probability.
The Hilbert kernel is the orthogonal sum of the successful cells' lines.
In the original group all pairs of distinct Haar coordinates are almost surely different, so the kernel is zero.
A square injective matrix over a finite von Neumann algebra is an affiliated unit.
The adjoint and matrix inverse stay in the group division closure by [Gram elimination](Yin_C_A0132_v1.md#argument).

On a periodic input with at least one marked height, cut the period at a mark.
The closing condition there compares two values from the preceding height, both carrying the same Bloch factor, which cancels.
Thus the same cell computation gives one dimension over \(\mathbb C(z)\) for each pair of successive marks whose circle labels agree, counting cyclically.
It also applies with labels in an extension field and a separate Bloch variable.
In a one-marker period the unique return always has equal labels.
Longer displayed periods containing several marks have nullity given by the same equality count.

### Trace and the two quotients

Each successful cell has exactly one normalized basis vector for its kernel.
The sum of the two diagonal entries of the kernel projection at each of its sites is \(1/(j-i)\), since \((c,d)\) is constant on the cell.
The group trace thus gives the probability of a successful cell starting at the origin.
Indeed, partition the diagonal trace at the origin by the offset \(r\ge0\) from its preceding mark.
Stationarity rewrites this sum as the expected contribution at offsets \(r\) of a successful cell starting at zero.
The contributions sum to one on that event and vanish otherwise.

The probability of a mark at zero is \(\beta(1-\beta)\).
Conditioned on this mark, the next mark occurs after a run of \(N\) ones followed by a run of \(M\) zeros.
Independence of future Bernoulli coordinates gives the product of the two geometric laws in the statement.
In \(W_q\) the \(q\) Haar coordinates on the circle are pairwise distinct almost surely, so the endpoint labels agree exactly when \(q\) divides the return time.
This event has positive probability for every \(q\), since the return time assigns positive mass to every integer at least two.
Its probability is at most \(\Pr(N+M\ge q)\), which tends to zero.
In the independent cyclic reductions the two endpoint labels are independent uniform \(d\)-th roots of unity, conditionally on the marks, and agree with probability \(1/d\).
For marked convergence observe that any fixed word visits finitely many lamp heights, and reduction modulo \(q\) eventually identifies none of those distinct heights.
For torsion-free \(K\), both bases in \(W,W_q\) are torsion-free and both top quotients are infinite cyclic, proving torsion-freeness.

### A single group-ring matrix before specialization

The only coefficients of \(P\) that require a rational expression over the group ring arise from the one fixed \(b\) and its translates.
Choose a [group-ring realization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) of \(b\) with an invertible pivot over \(\mathcal U(K)\).
The copy of \(K\) at any indicated height embeds as a subgroup in each quotient, so these pivots stay invertible and realize the corresponding copies of \(b\).
Use block triangular and block diagonal combinations for the finitely many sums and products to write \(P=\alpha L^{-1}\gamma\), with group-ring entries in \(\alpha,L,\gamma\).
All diagonal pivots used by these operations are the preceding invertible pivots or identity blocks, so \(L\) remains invertible at every quotient in assertions 2 and 3.
The fixed square matrix
\[
                      A=\begin{pmatrix}L&\gamma\\-\alpha&0\end{pmatrix}
\]
is equivalent by invertible block operations to \(\operatorname{diag}(L,P)\) in the original group and in each of those quotients.
It has precisely the claimed unnormalized nullities.
For \(K=C_2\) all coefficients of \(E\) and \(Q\) have denominators dividing four, so \(4P\) already has integral group-ring entries.
Testing the inverse gate of this one explicit matrix in the original mixed lamp group precludes its evaluation at every decorated one-marker period, even when each length is allowed its own choice of labels.
In the conditional torsion-free case only the polynomial observation formula itself is asserted to admit the periodic evaluation in assertion 1.

## Assessment history

### Decision decorated-periods

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:30 |
| status | proved |
| reason | Each interval contributes one kernel dimension precisely at a collision of its endpoint labels, which is null for independent Haar coordinates and certain in a one-marker period. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One invertible matrix, failure at every decorated one-marker period, and exact nullities for two quotient families. |
| argument | [Argument](#argument) | Interval equations, Bernoulli return times, conditional collision probabilities and one group-ring linearization. |
| dependency | [Two-run comparison](Yin_C_A0173_v1.md#kernel-on-two-consecutive-runs) | The periodic words in the obstruction to rationality. |
| dependency | [Group-ring realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | A square realization preserving the original and quotient nullities. |
| dependency | [Matrix inversion](Yin_C_A0132_v1.md#argument) | Inverse closure at an affiliated-unit pivot. |
| review | [Decorated periods](../audits/reviews/Yin_R_A0176_v1.md#decorated-periods) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-decorated-periods)

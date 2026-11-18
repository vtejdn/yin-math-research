---
author: Yin
---

# Disk maxima and Taylor minors of the cyclic Wigner determinant

<a id="statement"></a>
## A disk test for complete convergence

Fix one nonconstant scalar polynomial and one family of laws in the [finite-variance contract](../tasks/Yin_T_F0012_v3.md#contract).
On each of the [compact cyclic charts](Yin_C_F0359_v2.md#statement) indexed by integers \(R\ge1\), write \(n=mN,\ p_N(t)=\det(tI_n-T_N)\), \(U_N=n^{-1}\log|p_N|\), and \(u\) for the continuous free potential.
The pencil size \(m\) and its coefficients are fixed for this chart.
Let \(D=\overline B(t_0,r)\) range over disks in its interior with rational center coordinates and positive rational radius.
Full-sequence weak Brown convergence under every cross-size coupling for this model is equivalent to
\[
 \sum_N\Pr\{\sup_D U_N<\inf_D u-\epsilon\}<\infty
 \qquad\text{for every such }R,D\text{ and rational }\epsilon>0 .
 \tag{1}
\]
Equivalently one may replace \(\sup_D U_N\) by \((2n)^{-1}\log\sum_{k=0}^n |p_N^{(k)}(t_0)r^k/k!|^2\).

<a id="argument"></a>
## The submean inequality on a cover

Use the uniform complete convergence on each chart of \(V_N=n^{-1}\sum_i\log\max(N^{-B},s_i(tI-T_N))\) to \(u\), for any fixed \(B>0\).
This is the [reviewed cutoff estimate](Yin_C_F0359_v2.md#clip).
If (1) holds, first Borel–Cantelli gives one event of probability one in each coupling with uniform clipped convergence and all countably many eventual disk lower bounds.
Fix a compact \(K\) in the interior and cover it by at most \(C_K/r^2\) rational-center radius-\(r\) disks \(D_j\), using a square grid of sufficiently small rational spacing \(r\).
Their concentric triple disks are inside the chart.
For fixed \(r,\epsilon\) and all sufficiently large \(N\), each \(D_j\) contains a maximizer \(s\) with \(U_N(s)\ge\inf_{D_j}u-\epsilon\), and \(\sup|V_N-u|\le\epsilon\).
Since \(U_N\le V_N\) and \(D_j\subset\overline B(s,2r)\), the area submean inequality for the logarithm of the modulus of a polynomial gives
\[
 \int_{D_j}(V_N-U_N)\,dA\le4\pi r^2(2\epsilon+\omega_u(4r)).
\]
Here \(\omega_u\) is the modulus of continuity on the compact chart.
Summing, then sending \(r\) and \(\epsilon\) to zero, proves local \(L^1\) convergence in the interior.
The [finite and free chart identity](Yin_C_F0359_v2.md#chart) transfers this to every compact subset of \(\{|w|<R\}\).
Distributional Laplacians give vague convergence on the plane, and the limit has total mass one.

For necessity take independent tuples across sizes, one allowed coupling.
The [pathwise potential criterion](Yin_C_F0359_v2.md#equivalence) gives local \(L^1\) convergence on chart interiors almost surely.
Each failed disk test costs at least \(\epsilon |D|\) in \(L^1\), so occurs only finitely often.
Independence and the second Borel–Cantelli lemma imply (1).
Finally, if \(a_k=p_N^{(k)}(t_0)/k!\), Parseval on the boundary circle and Cauchy–Schwarz on the Taylor series bound \(\sup_D|p_N|\) between \((\sum |a_k|^2r^{2k})^{1/2}\) and \(\sqrt{n+1}\) times that same quantity.
The normalized logarithmic error tends to zero.

<a id="minors"></a>
## A sufficient test on the bottom singular spaces

At a center write \(t_0I-T_N=U\operatorname{diag}(s_1,\ldots,s_n)V^*\) in decreasing singular-value order, and set \(J=U^*V\).
Column expansion of \(\det(\operatorname{diag}(s)+hJ)\) gives, up to one unimodular factor shared by all orders,
\[
 a_k=\sum_{|I|=k}\det J[I,I]\prod_{j\notin I}s_j .
 \tag{2}
\]
This identity includes exact zero singular values.

Let \(c=N^{-B}\) and suppose \(q'=\#\{s_i<c\}\le q=o((N/\log N)^{1/3})\), where \(q\) is a positive integer bound.
Suppose an ordered SVD gives absolute determinant at least \(\delta=N^{-Cq}\), for fixed \(C>0\), on each principal submatrix of \(J\) indexed by the last \(k\) positions, \(1\le k\le q'\).
Then \(n^{-1}\log\sup_D|p_N|\ge V_N(t_0)-o(1)\) for fixed \(r>0\).
For a probabilistic use one may fix a measurable ordered SVD.

If \(q'=0\), the center suffices.
Otherwise descend from \(s_{n-q'}\ge c\) until the first step \(s_{n-k+1}<h s_{n-k}\), where \(h=\delta/(4nq)\).
All retained subcutoff values before that step exceed or equal \(ch^q\), and using them in place of their clipped values loses at most \(q^2|\log h|\) in the logarithm.
If there is no such gap this estimates \(a_0\).
At the first gap the last \(k\) indices in (2) have positive complementary product \(\prod_{j\le n-k}s_j\).
After division by this product all competing terms together have absolute value at most
\[
 \sum_{\ell\ge1}\binom{k}{\ell}\binom{n-k}{\ell}h^\ell
 \le e^{knh}-1\le\delta/2 ,
\]
since all minors of a unitary have modulus at most one.
Thus \(|a_k|\ge(\delta/2)\prod_{j\le n-k}s_j\).
Each omitted clipped value is \(c\le1\), and \(\sup_D|p_N|\ge r^k|a_k|\).
The total unnormalized error is bounded by \(q^2|\log h|+|\log(\delta/2)|+q|\log r|=o(n)\).
These are sufficient deterministic hypotheses on the singular vectors and values at one center.
Establishing the disk probability bound for arbitrary Wigner input laws remains open.

## Current assessment
[Selected decision](#decision-disk-witness-reviewed)

## Assessment history

### Decision disk-witness-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18T10:49 |
| status | open |
| reason | The disk equivalence and deterministic sufficient condition have a written argument. The Wigner lower bound in the general contract is open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Disk criterion](#statement) | Each fixed polynomial and model under every cross-size coupling. |
| argument | [Cover by disks](#argument) | Both implications and the Taylor coefficient norm. |
| support | [Bottom singular spaces](#minors) | A sufficient deterministic comparison with the clipped potential. |
| dependency | [Polynomial cutoff](Yin_C_F0359_v2.md#statement) | Uniform complete convergence and the finite and free chart identities. |

### Decision disk-witness-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-18T11:04 |
| status | proved |
| reason | Independent whole-proof review verifies the disk equivalence and the sufficient Taylor-minor bound for each fixed model. The general probability estimate required by the criterion remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Disk maxima and Taylor norm](#statement) | An equivalent summable disk test for the arbitrary-coupling weak limit. |
| argument | [Area submean and independent sizes](#argument) | Both implications and the coefficient-norm equivalence. |
| support | [Bottom singular spaces](#minors) | Deterministic sufficient estimate at a fixed center, also at singular matrices. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0367_v3.md#disk-minors-whole-proof) | Complete fixed argument, its dependency interfaces and the deterministic sufficient condition. |

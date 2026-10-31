---
author: Yin
---

<a id="kro81-u001"></a>
# Kro81-U001: Rational Laurent Series, Recurrences and Hankel Rank

Inspected edition: [Yin's source notes](readme.md#yin-edition).

- Source: [Kro81](../../../literature/pdf/Kro81.pdf), the 1897 collected-works reprint of the 1881 article.

- Locator: Articles VI–X, printed pp. 141–158, PDF pp. 30–47; the criterion is stated in IX, pp. 153–154, with the essential determinant induction in VII, pp. 147–149.
- Record: 2026-10-10, AI source audit under Yin.
The following proof reconstruction was self-reviewed; no independent second reviewer or formal verification is asserted.
- Assessment: audited within the stated scalar, formal-series scope.
The source's main rationality criterion is accepted, with the indexing and finite-data restrictions below.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Leopold Kronecker's Werke II, edited by K. Hensel, Teubner, 1897, pp. 113–192; 81-page retained scan. No collation with the original 1881 printing. |
| source-locator | VI–X, printed 141–158 / PDF 30–47; especially VII 147–149, VIII 149–152, IX 153–154 and X 154–158. |
| inspection | All these passages read; recurrence/rank equivalence, nonzero initial minor, determinant-defect induction, rational reconstruction and polynomial annihilator checked as below. Printed 148–150 visually inspected to resolve OCR and signs. Historical references are not separately audited. |

<a id="kro81-hankel-recurrence"></a>
## Statement and conventions

Work over the complex numbers, with a scalar sequence \(c=(c_j)_{j\ge0}\).
Put

\[
S(x)=\sum_{j\ge0}c_jx^{-j-1},\qquad
\mathsf H(c)=(c_{i+j})_{i,j\ge0},\qquad
H_m=\det(c_{i+j})_{0\le i,j<m},\quad H_0=1.
\]

These are formal Laurent series and an algebraic infinite matrix.
Its rank means the supremum of ranks of finite submatrices, equivalently the dimension of the span of its columns in the vector space of all sequences.
No bounded Hankel operator, measure, norm or convergence is assumed.
A recurrence of order \(m\) means constants \(\gamma_0,\ldots,\gamma_{m-1}\) such that

\[
c_{t+m}+\sum_{j=0}^{m-1}\gamma_jc_{t+j}=0
\quad\text{for every }t\ge0.
\tag{1}
\]

The terminal coefficient is normalized to one; \(\gamma_0\) may vanish.
The all-zero sequence has order and rank zero.
For a nonzero sequence the following are equivalent:

1. \(S\) is rational.
2. A recurrence (1) holds with a fixed finite order for all shifts from the start.
3. \(\mathsf H(c)\) has finite algebraic rank.
4. The leading determinants \(H_n\) are zero for all sufficiently large \(n\).

If \(m\) is the last index with \(H_m\ne0\), it equals the minimal recurrence order, the Hankel rank and the degree of the denominator of the reduced, strictly proper fraction \(S=P/Q\).
Here \(\deg P<\deg Q=m\).
This is the modern notation for VII's four characterizations and IX's rationality criterion; the source does not use the language of a Hilbert-space Hankel operator.

## Proof reconstruction

### Recurrences, rational functions and rank

Multiplying (1) by the appropriate negative powers of \(x\) says exactly that

\[
Q(x)S(x)\in\mathbb C[x],\qquad
Q(x)=x^m+\gamma_{m-1}x^{m-1}+\cdots+\gamma_0.
\]

The polynomial part has degree at most \(m-1\).
Conversely, the negative coefficients in \(QS=P\) give (1).
If \(S=P_*/Q_*\) is reduced, polynomiality of \(QS\) is equivalent to divisibility \(Q_*\mid Q\).
This proves the denominator-degree/minimal-order assertion without a separability or nonzero-root hypothesis.

Write \(v_j=(c_{i+j})_{i\ge0}\).
A recurrence gives \(v_m\) in the span of \(v_0,\ldots,v_{m-1}\), and shifting propagates this dependence to every subsequent column.
Conversely, if the column span has finite dimension, take the first dependent column.
Its predecessors are independent; the resulting monic relation holds in every row, hence is (1).
Thus the minimal order equals the rank.

For a minimal order \(m\), the first \(m\) columns restricted to the first \(m\) rows are independent.
Indeed, if a combination vanishes there, its entries themselves obey (1), so those first \(m\) zero entries propagate to all entries; this contradicts independence of the full columns.
Consequently \(H_m\ne0\), while rank at most \(m\) makes every larger minor zero.
This also checks the initial-block conclusion of VI in its actual recurrence setting.

### Why eventual vanishing of leading minors suffices

It is not legitimate to infer all-minor rank directly from one vanishing leading minor.
The source supplies a stronger induction.
Given \(H_m\ne0\), solve uniquely for \(\gamma_j\) so that (1) holds at \(t=0,\ldots,m-1\), and define

\[
\delta_t=c_{t+m}+\sum_{j=0}^{m-1}\gamma_jc_{t+j}.
\]

Suppose \(\delta_t=0\) for \(0\le t<m+r\).
In the determinant \(H_{m+r+1}\), replace each of the last \(r+1\) rows by its recurrence combination of the original rows.
This is multiplication by a triangular matrix with diagonal one.
The lower left block is zero.
In the lower right \((r+1)\)-square block, entries before the antidiagonal vanish and every antidiagonal entry is \(\delta_{m+r}\).
Therefore

\[
H_{m+r+1}=(-1)^{r(r+1)/2}H_m\delta_{m+r}^{\,r+1}.
\tag{2}
\]

If every \(H_n\) with \(n>m\) vanishes, (2) successively forces every remaining defect to vanish.
This proves (1).
Earlier \(H_j\), \(j<m\), are allowed to vanish.
If all positive-order \(H_j\) vanish, a first nonzero coefficient \(c_k\) would give \(H_{k+1}=(-1)^{k(k+1)/2}c_k^{k+1}\ne0\), a contradiction.
This covers the zero case.

The induction is the substantive step in VII, printed p. 148.
The reconstruction uses field arithmetic; no assertion over rings with nilpotents is imported.

### Determinantal reconstruction and coprimality

Let \(A_m=(c_{i+j})_{i,j<m}\), \(B_m=(c_{i+j+1})_{i,j<m}\), and \(v=(c_0,\ldots,c_{m-1})^T\).
Article VIII defines

\[
D_m(x)=\det(xA_m-B_m),\qquad
C_m(x)=v^T\operatorname{adj}(xA_m-B_m)v.
\]

Equivalently, its bordered determinant is \(UD_m-C_m\), with both off-diagonal blocks equal to \(-v\).
Set \(D_0=1,C_0=0\).
Cofactor condensation in that bordered determinant yields the source's equation (F), printed p. 150:

\[
C_mD_{m-1}-C_{m-1}D_m=H_m^2.
\tag{3}
\]

The mixed cofactors reduce to \(H_m\) by the successive moment-column operations; the two unmixed cofactors are \(D_m,D_{m-1}\).
This verifies the cancellation of the auxiliary variable \(U\) and the positive sign in (3).
It implies coprimality of \(C_m,D_m\) whenever \(H_m\ne0\), even when \(H_{m-1}=0\).

The coefficient of \(x^m\) in \(D_m\) is \(H_m\).
Its coefficients divided by \(H_m\) solve the first \(m\) recurrence equations, by Cramer's rule; the source's row operations (F')–(F'') give \(C_m\) as the polynomial part of \(D_mS\).
Under the full recurrence, all its negative coefficients vanish.
Hence

\[
S(x)=\frac{C_m(x)}{D_m(x)}.
\tag{4}
\]

Only \(c_0,\ldots,c_{2m-1}\) are needed for these polynomials.
They determine a unique rational continuation with reduced denominator degree \(m\); they do not force an arbitrary pre-existing continuation to be that one.

### Article X: gcd and annihilators

For a known proper rational function \(f_1/f\), \(\deg f=n\), the last nonzero \(H_m\) has \(m=n-\deg\gcd(f,f_1)\).
It suffices to examine \(H_1,\ldots,H_n\), because larger minors already vanish from the known denominator bound.
All polynomial multipliers of degree at most \(n\) that remove the negative Laurent part are precisely the multiples of the reduced denominator of degree \(m\); this space has dimension \(n-m+1\).
Division by the monic minimal denominator and the invertibility of \(H_m\) also prove completeness of the source's Cramer parametrization.
This finite test uses the known rational function and degree bound, not just a finite list of unexplained coefficients.

## Reuse boundaries

- A single zero determinant is insufficient: \(c_0=1,c_1=c_2=0,c_3=1\) gives \(H_1=1,H_2=0,H_3=-1\), regardless of \(c_4\).
  Arbitrarily long finite initial data also do not certify a specified infinite continuation.
- For the ordinary generating function \(R(z)=\sum c_jz^j\), one has \(S(1/z)=zR(z)\).
  Rationality transfers, but the rank is not generally the denominator degree of the reduced \(R\): \(R=1\) has Hankel rank one.
  Keep the strictly proper convention when quoting the degree assertion.
- Repeated roots and a zero constant coefficient of \(Q\) are permitted.
  Root-residue formulas from other passages are not needed for this proof.
- This is the classical coefficient criterion.
  The Hardy-projection commutator statement is the later operator formulation recorded in [Con94-U001](../Con94/Yin_U001.md#con94-u001) and the [existing one-letter audit](../Miy22/Yin_U009.md#exact-statement-and-conventions).
  It is not literally a statement about operators in Kro81.
  This audit does not add a new operator-domain theorem or change a project Claim decision.

## Verification facts and dependencies

The entire article was read, with this unit retaining the detailed verification of the criterion.
Dependencies are elementary polynomial division, finite-dimensional linear algebra and the determinant identity checked above.
Baltzer, Jacobi and earlier Kronecker papers cited in the source were not separately obtained or audited; the relevant identities were checked directly here.
No analytic convergence theorem is needed.
No machine proof was performed.
The source's final Bézout sign issue is downstream of (3)–(4) and is not used by this proof.
Initial unit issued 2026-10-10; no earlier inspection record is overwritten.

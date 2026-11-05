---
author: Yin
---

# Independent review of the Hermitian intermediate singular-value theorem

Review date: 2026-11-05T00:50 UTC.
Human record author: Yin.
The reviewing agent performed the preceding real-input review but did not develop the complex extension.
This follow-up received the fixed v2 candidate and exact review scope, without development drafts, proof-generation dialogue, author explanations or other reviewers' conclusions.
The entire v2 statement and argument were read before this finding was formed.
The unchanged steps reuse the reviewer's own [v1 finding](Yin_R_F0191_v1.md#intermediate-bound-reviewed) at the precise scopes identified below, after checking their applicability to the v2 proof.

## Inputs

- [Hermitian statement](../../claims/Yin_C_F0187_v2.md#statement): the fixed complex off-diagonal law with zero mean and unit absolute second moment, dependent real and imaginary parts permitted, independent real diagonals and arbitrary deterministic complex shifts.
- [Complete v2 argument](../../claims/Yin_C_F0187_v2.md#argument): independent complex coordinate blocks, both conjugate orientations, conditional truncation, distance concentration, row deletion and the singular-value argument.
- [Earlier independent finding](Yin_R_F0191_v1.md#intermediate-bound-reviewed): the already checked concentration-source locator and unchanged truncation exponents, dimension counts, median implication, complex row-distance identity, interlacing, normalization and probability arguments.

The accepted external input remains [GNT14, arXiv:1404.7013v1](https://arxiv.org/pdf/1404.7013v1), printed/PDF page 30, Theorem 3.7 and Corollary 3.8.
The earlier direct inspection of that complete page is reused here, including its explicit formulation for normed coordinate spaces.
No further source passage or proof audit is needed for the block specialization below.
The original concentration proof, attributed there to Maurey, remains outside the inspection depth.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Hermitian theorem finding](#complex-intermediate-bound-reviewed) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Hermitian theorem finding](#complex-intermediate-bound-reviewed) | [Statement](../../claims/Yin_C_F0187_v2.md#statement) | Entire complex Hermitian theorem, including dependent real and imaginary parts, arbitrary independent real diagonals, uniform deterministic complex shifts, independent random shifts and eventual almost-sure bounds under every cross-size coupling. |
| [Hermitian theorem finding](#complex-intermediate-bound-reviewed) | [Argument](../../claims/Yin_C_F0187_v2.md#argument) | Entire v2 proof, with new checks of block concentration, conjugate conditional means and covariances, and row orientation; unchanged steps reuse the exact earlier independent finding after interface comparison. |

<a id="complex-intermediate-bound-reviewed"></a>
## Hermitian theorem finding

The complete v2 argument supports the stated complex Hermitian extension.
No substantive mathematical gap was found.
The extension does not require independence of the real and imaginary parts or a condition on \(\mathbb E\xi^2\).

### Concentration acts on complex coordinates as blocks

Theorem 3.7 is stated for probability measures on normed coordinate spaces, and Corollary 3.8 applies to a convex 1-Lipschitz function on their product.
Take the coordinate space to be \(\mathbb C\) regarded as the real Euclidean space \(\mathbb R^2\), with norm \(|z|\), and equip its product with the Euclidean norm.
The independence required by the source is independence between these coordinate blocks.
It imposes no product decomposition within the two real components of one block.

After conditioning on the good-coordinate set, each retained coordinate is supported in the complex disk of radius \(n^{1/4}\), or in its translate after centering.
Its support therefore has diameter at most \(2n^{1/4}\), including when its law is conjugated.
Translation leaves this diameter unchanged.
Rescaling Corollary 3.8 gives
\[
 \mathbb P(|Z-\operatorname{med}Z|\ge t)
 \le 4\exp\!\left(-\frac{t^2}{16n^{1/2}}\right).
\]
For the needed \(Z:=\operatorname{dist}(y,H'_J)\), convexity and the Lipschitz constant one hold on the real Euclidean product because a complex linear subspace is also a real linear subspace and its distance function is convex and 1-Lipschitz.
Thus equation (9) is applicable even to singular laws supported on a line or to arbitrarily dependent real and imaginary components.

### Conjugate orientations and the conditional second moment

Fix any deterministic pattern in which the independent coordinates have laws \(\xi\) or \(\overline{\xi}\).
Conjugation preserves modulus, so all good-coordinate indicators have the same success probability and remain independent.
The binomial bound with \(p_n\le n^{-1/2}\) and bad-set threshold \(n^{5/8}\) therefore transfers unchanged from v1.
Conditioning on a specified positive-probability good set preserves the product law of the retained blocks.

For a retained coordinate of the first orientation, its mean is \(m_n\); for the conjugate orientation, its mean is \(\overline{m_n}\).
In either orientation the centered absolute second moment is \(v_n\).
Consequently, for the centered conditional vector \(y\),
\[
 \mathbb E\overline{y_a}y_b=v_n\delta_{ab}.
\]
The off-diagonal expectations vanish by independence between blocks and their zero conditional means, without a statement about the real covariance matrix inside a block.
For a fixed complex orthogonal projection \(Q\), this gives
\[
 \mathbb E\|Qy\|^2
 =\mathbb E(y^*Qy)
 =\sum_{a,b}Q_{ab}\mathbb E\overline{y_a}y_b
 =v_n\operatorname{Tr}Q.
\]
Pseudo-variance \(\mathbb Ey_a^2\) does not enter this identity.

Finite absolute second moment gives \(m_n\to0\) and \(v_n\to1\) by convergence of the first and absolute second truncated moments.
Using the orientation-dependent mean vector \(m_J\), the single added complex vector \(f_J+m_J\) removes the shift and conditional mean exactly.
Its magnitude costs no additional dimension.
The unchanged bound
\[
 \operatorname{codim}_{\mathbb C}H'_J
 \ge q-|J^c|-1\ge q/2
\]
therefore yields \(\mathbb E\|Qy\|^2\ge q/3\) eventually.
The v1 median argument now applies with the block concentration estimate above and gives the same \(C\exp(-cq/n^{1/2})\) conditional lower tail, uniformly in the orientation pattern, good set, subspace and shift.
This establishes the precise distance estimate needed by v2.

### Hermitian row dependence is removed by the same deletion

For a retained row \(i\), the coordinates before its diagonal have the laws of \(\overline{\xi}\), and those after its diagonal have the laws of \(\xi\).
They originate from distinct independent upper-triangular entries.
The coordinate orientations are fixed by their positions, so the distance lemma permits this exact row distribution.

For each other retained row, the only entry involving one of these same upper-triangular variables lies in column \(i\), as its complex conjugate.
Deleting that column from the other-row matrix removes every such dependence.
A variable whose partner row is not retained already occurs only in row \(i\).
After also deleting the diagonal coordinate of row \(i\), its remaining random vector is therefore independent of the projected other-row space.
The other diagonal variables are independent of the complete off-diagonal family by the statement's hypothesis.
No diagonal moment, bound or centering is needed.

The projected space still lies in \(\mathbb C^{n-1}\) and has at most \(n-k-1\) spanning rows, so its codimension is at least \(k\).
For \(k:=\lfloor j/2\rfloor\) in the stated range, \(k\ge c_0(n-1)^{3/4}\) with a fixed numerical \(c_0>0\).
Conditioning on that space thus permits the verified distance estimate with the deterministic row shift \(\sqrt n F_n\).
This checks the changed interface before the row union bound.

### Reused final argument and full theorem scope

The rest of the v2 argument agrees with the previously reviewed reasoning and remains valid for complex rows.
Positive row distances give full row rank, and the complex Gram-matrix Schur complement gives the negative-second-moment identity.
The decreasing-singular-value count is at least \(j-k\), in fact \(j-k+1\), at and below index \(n-j\).
Thus
\[
 s_{n-j}(B)^2\ge \frac{k(j-k)}{Cn},
 \qquad
 n^{-1/2}s_{n-j}(B)\ge c\,\frac jn.
\]
Principal-submatrix interlacing of \(BB^*\) inside \(AA^*\), for \(A:=\sqrt n(W_n+F_n)\), supplies the required inequality in the correct direction.
These facts, including the endpoint counts and the normalization, were checked in the v1 finding and compared with their unchanged v2 occurrences.

Union bounds over rows and \(j\) give \(Cn^2\exp(-cn^{1/4})\).
The bound is summable, so the first Borel--Cantelli lemma gives the eventual almost-sure statement without independence between sizes.
All auxiliary codimension constants are numerical, and both orientations have identical modulus tails and conditional variances; the resulting constants and sufficiently large threshold depend only on the fixed complex off-diagonal law.
No size or symmetry bound on the deterministic shift is introduced.
Conditioning on an independent random shift preserves the required matrix law and therefore gives the stated conditional extension.

The review covers the full v2 theorem, with the explicitly reused unchanged evidence and newly verified complex interfaces above.
It does not audit the original external concentration proof, establish a least-singular-value estimate, resolve general matrix-coefficient pencils or review Task completion.
C_F0186_v4 remains contextual and is not a premise or an inspected input of this finding.
This review does not change either Claim version's assessment or the earlier v1 review.

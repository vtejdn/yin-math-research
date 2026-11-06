---
author: Yin
---

# BBLM05: fourth moments under independent-block resampling

<a id="bblm05-u001"></a>
## Input and inspected scope

Use the [arXiv v1 electronic reprint](readme.md#arxiv-v1-electronic-reprint), Section 2.1, PDF pp. 3–4, and Theorem 2, PDF p. 5.
The reusable input is the fourth-moment specialization of that theorem for a real measurable function of finitely many independent random blocks.
The source theorem is accepted at this scope after direct checking of its statement, notation and hypotheses.
The original proof was not reviewed, and this is not an independent project-proof review.

<a id="independent-block-resampling"></a>
## Definition: independent-block replacements and variance proxies

Let \(X=(X_1,\ldots,X_n)\) consist of mutually independent random variables in measurable spaces, and let \(Z=F(X)\) be real and measurable.
For the finite fourth-moment interface below, assume \(Z\in L^4\).
The variables need not have identical laws.
Different block spaces may be embedded in their measurable disjoint union to match the source's common-space notation.

Take \(X'_1,\ldots,X'_n\) with the respective laws of \(X_1,\ldots,X_n\), mutually independent and independent of all the original variables.
Define
\[
 X^{(i)}=(X_1,\ldots,X_{i-1},X'_i,X_{i+1},\ldots,X_n),
 \qquad Z'_i=F(X^{(i)}),\qquad I_i=Z-Z'_i.
\]
Thus the same measurable function is evaluated after replacement of exactly one whole independent block by a fresh copy with its original law.
For real \(a\), write \(a_+=\max(a,0)\) and \(a_-=\max(-a,0)\).
The source's one-sided resampling variance proxies are
\[
 V^+=\mathbb E\!\left[\sum_{i=1}^{n}(I_i)_+^2\mid X\right],
 \qquad
 V^-=\mathbb E\!\left[\sum_{i=1}^{n}(I_i)_-^2\mid X\right].
\]
Here conditioning on \(X\) integrates the independent replacements while retaining all original blocks.
Use \(\|Y\|_q=(\mathbb E|Y|^q)^{1/q}\).
For the conversion below, set
\[
 \Gamma:=V^++V^-=\sum_{i=1}^{n}\mathbb E[I_i^2\mid X].
\]
The symbol \(\Gamma\) is a local abbreviation, not the source's separate \(V=\sum_i(Z-Z_i)^2\), where \(Z_i\) is a measurable function omitting coordinate \(i\).

<a id="theorem-2-at-four"></a>
## Theorem 2 at \(q=4\)

The source defines, for integer \(q\ge2\),
\[
 \kappa_q=\frac{1}{2\bigl(1-(1-1/q)^{q/2}\bigr)}.
\]
In particular, \(\kappa_4=8/7\), and its Theorem 2 gives
\[
 \|(Z-\mathbb EZ)_+\|_4
 \le \sqrt{\frac{48}{7}\|V^+\|_2},
 \qquad
 \|(Z-\mathbb EZ)_-\|_4
 \le \sqrt{\frac{48}{7}\|V^-\|_2}.
\]
The coefficient follows from
\[
 (1-1/4)\,2\kappa_4\,4=\frac{48}{7}.
\]
These are direct specializations of the two source inequalities, with no bounded-difference or coordinate-moment assumption added.
The standing \(L^4\) assumption makes every displayed quantity finite; bounded \(Z\) is sufficient regardless of the moments of the blocks themselves.

<a id="fourth-moment-resampling-bound"></a>
## Direct conversion to fourth moments of replacement influences

The following conversion is elementary and is recorded separately from the source statement.
Because the positive and negative parts have disjoint support,
\[
 \begin{aligned}
 \mathbb E|Z-\mathbb EZ|^4
 &\le \frac{2304}{49}
       \mathbb E\bigl[(V^+)^2+(V^-)^2\bigr]\\
 &\le \frac{2304}{49}\|\Gamma\|_2^2.
 \end{aligned}
\]
Minkowski's inequality and conditional Jensen give
\[
 \begin{aligned}
 \|\Gamma\|_2
 &\le \sum_{i=1}^{n}
       \|\mathbb E[I_i^2\mid X]\|_2\\
 &\le \sum_{i=1}^{n}(\mathbb E|I_i|^4)^{1/2}.
 \end{aligned}
\]
Consequently,
\[
 \boxed{\;
 \mathbb E|Z-\mathbb EZ|^4
 \le \frac{2304}{49}
       \left[\sum_{i=1}^{n}(\mathbb E|I_i|^4)^{1/2}\right]^2
 \le \frac{2304}{49}\,
       n\sum_{i=1}^{n}\mathbb E|I_i|^4 .
 \;}
\]
The final inequality is Cauchy–Schwarz on the finite sum.
Expectations in these bounds include both the original blocks and their independent copies.
No uniform conditional bound on \(I_i\) is required, but an actual unconditional fourth-moment estimate is still needed for a concentration application.

<a id="wigner-block-applicability"></a>
## Block matching and unresolved matrix input

For \(d\) independent real symmetric or complex Hermitian Wigner matrices of size \(N\), take as one block the diagonal entry \((r,r)\) and the independent upper-triangular entries \((r,s)\), \(s>r\), of one matrix.
There are \(n=dN\) mutually independent blocks.
After replacing one such block, reflect its entries to the lower triangle using the same symmetry or conjugate symmetry as in the original model.
A full displayed Hermitian row is not an independent coordinate block because it shares entries with other displayed rows.
Replacing a selected block means using its complete original joint law; a law obtained by conditioning the entire matrix on a norm or regularity event is not automatically a product law.

For any measurable matrix-valued function of these blocks, a real bounded eigenvalue statistic
\[
 Z=\frac1N\sum_{j=1}^{N} f(\lambda_j),
 \qquad f:\mathbb C\to\mathbb R\ \text{bounded and Borel measurable},
\]
with algebraic multiplicities, is bounded by \(\|f\|_\infty\) and hence meets the integrability requirement.
The eigenvalues are unordered here, so only the symmetric empirical statistic is used.
Thus the source inequality applies to original-law independent-block replacement of such a statistic even when the matrix entries have only finite second moments.
It supplies neither decay of the replacement influences nor identification of \(\mathbb EZ\).
In particular, no Wigner-product spectral convergence result or planar-defect estimate follows from this unit alone.
The consuming argument must establish the relevant fourth-moment influence estimates and its limiting expectation separately.

<a id="inspection-limits"></a>
## Reading and applicability limits

The source check on 6 November 2026 asked whether a fourth-moment replacement inequality can turn averaged spectral-statistic influences into summable deviation probabilities without requiring entry fourth moments.
The bounded primary-source search used the terms “Boucheron Bousquet Lugosi Massart 2005 moment inequalities functions independent random variables Efron Stein theorem pdf” and led to the electronic reprint identified above.
Direct reading covered the metadata on PDF p. 1, the notation on pp. 3–4 and Theorem 2 on p. 5.
The constants, the two one-sided definitions and the conversion displayed here were checked; the theorem's proof and its cited dependencies were not re-audited.
Reading stopped once that source interface was determined.
The unresolved input for a matrix application is an influence estimate under its actual random background, not an uninspected extension asserted by this source.

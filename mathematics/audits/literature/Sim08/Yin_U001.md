---
author: Yin
---

# Sim08: Christoffel minima, moment inverses and atom limits

<a id="sim08-u001"></a>
## Source and inspection

The inspected edition is [arXiv:0806.1528v1](readme.md#arxiv-v1).
The source conventions in Section 1, Theorem 2.1 and its first proof, Lemma 9.1 and Theorems 9.2 and 9.7 were read directly in the PDF text layer.
The displayed proof of Theorem 9.7 was also checked in the rendered page to distinguish typographical issues from extraction errors.
These are selected source definitions, statements and elementary proof checks, not a complete paper audit or an independent project-proof review.

<a id="christoffel-variational-principle"></a>
## Christoffel kernel and constrained minimum

Section 1, printed/PDF pages 2–4, starts with a positive measure \(\mu\) on \(\mathbb C\) having all finite moments and not supported on a finite set.
Write \(x_j\) for its orthonormal polynomials, with positive leading coefficients.
Equation (1.12) defines

\[
K_n(z,\zeta)=\sum_{j=0}^{n}\overline{x_j(z)}x_j(\zeta).
\]

The sum includes degree \(n\), and complex conjugation is on the first variable.
The normalization is not restricted to probability measures: equation (1.13) gives \(K_n(z,\zeta;c\mu)=c^{-1}K_n(z,\zeta;\mu)\) for \(c>0\).

Theorem 9.2, printed/PDF page 15, equations (9.6)–(9.7), states

\[
\lambda_n(z_0;\mu)
:=\min_{\substack{Q\in\mathbb C[z],\ \deg Q\le n\\Q(z_0)=1}}
\int |Q(z)|^2\,d\mu(z)
=\frac{1}{K_n(z_0,z_0)},
\qquad
Q_{n,z_0}(z)=\frac{K_n(z_0,z)}{K_n(z_0,z_0)}.
\]

The symbol \(\lambda_n\) here names the source's displayed minimum.
The proof expands \(Q\) in the orthonormal basis and applies Lemma 9.1 to a single linear constraint.
The minimizer is unique under the source's nondegeneracy assumption.

<a id="abc-moment-inverse"></a>
## Moment-matrix inverse

Section 2, printed/PDF pages 4–5, defines the matrices by

\[
M^{(n)}_{jk}=\int\overline{z}^{\,j}z^k\,d\mu(z),
\qquad
K_n(z,\zeta)=\sum_{j,m=0}^{n}k^{(n)}_{jm}\overline z^{\,m}\zeta^j.
\]

Theorem 2.1, equation (2.3), states \(k^{(n)}=(M^{(n)})^{-1}\).
The first proof, equations (2.4)–(2.6), uses the reproducing identity to check the matrix product directly.
For a measure on \(\mathbb R\), this moment matrix is the real symmetric Hankel matrix \(H_n=(m_{j+k})_{j,k=0}^{n}\), where \(m_r=\int x^r\,d\mu(x)\).
At the real evaluation point zero, the source formulas therefore give

\[
K_n(0,0)=(H_n^{-1})_{00},
\qquad
\lambda_n(0;\mu)=\bigl((H_n^{-1})_{00}\bigr)^{-1}.
\]

This is an ordinary inverse formula under invertibility, not a Moore–Penrose inverse assertion for singular moment matrices.
The finite-support case and any convention after the polynomial Gram matrix becomes singular require an explicit separate argument.

<a id="compact-support-atom-limit"></a>
## Compact-support atom limit and proof qualifications

Theorem 9.7, printed/PDF page 17, equation (9.21), states that for a compactly supported measure on \(\mathbb R\) and every \(x_0\in\mathbb R\),

\[
K_n(x_0,x_0)\longrightarrow\mu(\{x_0\})^{-1},
\qquad
\lambda_n(x_0;\mu)\downarrow\mu(\{x_0\}),
\]

where the first limit is \(+\infty\) when the mass is zero.
The second formula combines the first with Theorem 9.2 and the increasing polynomial spaces.
The global non-finite-support convention remains in force for the source's infinite sequence \(K_n\).

The rendered preprint proof has minor defects that should not be copied literally.
For arbitrary \(x_0\) outside the support, the stated choice \(A\ge\operatorname{diam}(\operatorname{supp}\mu)\) need not bound \(|x-x_0|\) on the support.
The trial polynomial in (9.23) has degree \(2n\), while (9.25) labels the resulting kernel bound by \(n\), and (9.26) omits the reciprocal on its right side.
The following direct reading of the intended argument resolves these issues without relying on those displayed bounds.
Choose \(A>0\) with \(A\ge\max_{x\in\operatorname{supp}\mu}|x-x_0|\), and set \(Q_{2n}(x)=(1-(x-x_0)^2/A^2)^n\).
Then \(Q_{2n}(x_0)=1\), \(|Q_{2n}|\le1\) on the support and \(|Q_{2n}|^2\) converges pointwise to \(1_{\{x_0\}}\).
Dominated convergence gives \(\lambda_{2n}(x_0;\mu)\le\int|Q_{2n}|^2\,d\mu\to\mu(\{x_0\})\), while every admissible polynomial has squared norm at least \(\mu(\{x_0\})\).
Monotonicity supplies the limit for the full sequence.
Thus the stated atom limit is valid at the inspected scope; the literal intermediate displays are not adopted as written.

<a id="group-ring-interface-limits"></a>
## Scope of a group-ring application

A bounded self-adjoint operator in a finite tracial von Neumann algebra has a finite compactly supported spectral measure, so its polynomial variational minimum has the setting of the compact-support argument above.
Using the inverse formula additionally requires the indicated finite moment matrix to be invertible.
The source does not prove that group-ring return moments force \(K_n(0,0)\) to diverge, that atoms have integer mass, or that a torsion-free amenable group supplies such an estimate.
Those are separate algebraic or analytic obligations of the consuming argument.

---
author: Yin
---

# Applications of the Finite-Residual Boundedness Lemma

<a id="finite-residual-applications"></a>
Date: 2026-09-09.
Authorization: the user asked which applications of [Yin_C_F0015](../claims/Yin_C_F0015_v1.md#yin_c_f0015) are already supported and which remain prospective.
This note classifies hypotheses and examples; it does not reopen [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), allocate a successor goal, or claim novelty.

## What Counts as an Application

Yin_C_F0015 needs three matched inputs: a specified full free-monoid orthonormal bounded-element basis, a subexponential homogeneous norm estimate, and finite residual dimension for the coefficients of the particular L2 element.
A theorem producing the third input for every affiliated rational L2 element is additional model-specific information.

Two distinctions matter.
A model can have a known positive theorem whose proof needs a reduced-word or subspace adaptation of Yin_C_F0015.
Conversely, a model can have a useful Haagerup estimate without an established theorem giving finite residuals for its rational elements.

| Class | Present status | Exact relation to Yin_C_F0015 |
| --- | --- | --- |
| Finite standard free semicircular families | Known positive theorem, audited in Miy26 | Literal application in the Wick word basis; Miy26 supplies finite residuals for affiliated rational L2 elements |
| Standard free circular families, using real and imaginary semicircular coordinates | Known positive consequence of the semicircular theorem | Literal application using the full $2d$-letter semicircular Wick basis, not only holomorphic circular words |
| Invertible polynomial coordinate changes of a semicircular tuple, including a nonfree shear | Supported by the existing coordinate-transfer framework and the same field/basis | Inherit the underlying semicircular grading; it is not ordinary degree in the new variables |
| Explicit square-summable finite-state Wick coefficient series | Direct examples of Yin_C_F0015 | Square summability and finite residuals are checked from the coefficients, without first assuming an affiliated rational expression |
| Finite free Haar-unitary families | Known positive theorem, audited in Miy26 and DR97 | Reduced-group-word version; not a literal full-free-monoid basis application |
| Classical analytic Hardy functions with finite Hankel rank | Known classical positive theorem | One-sided closed-subspace variant, not the full $L^2(\mathbb T)$ hypothesis of Yin_C_F0015 |
| Nonzero-$q$ Gaussian systems | Prospective beyond the stated source inputs | A homogeneous estimate is available; deformation of coefficient geometry and finite residual compatibility remain to be proved |
| Holomorphic free R-diagonal systems | An inspected strong Haagerup estimate, not a general rational-L2 theorem here | Holomorphic-subspace and rational coefficient/energy interfaces are needed |
| Free Meixner and related finite-recursion families | Prospective structural lead | Recursion alone does not verify norm growth or finite residuals for arbitrary rational functions |
| Analytic transports of semicircular laws | Prospective unless rational compatibility is separately proved | Analytic changes need not preserve either the rational field or finite coefficient realizations |

## 1. Direct Known Families

### Standard free semicircular variables

Let $s=(s_1,\ldots,s_d)$ be a finite standard variance-one free semicircular family and $M=W^*(s)$.
Its Wick polynomials satisfy
\[
U_w\Omega=e_w,\qquad
\left\|\sum_{|w|=m}\alpha_wU_w\right\|
\le(m+1)\left(\sum_{|w|=m}|\alpha_w|^2\right)^{1/2}.
\]
These are the full orthonormal basis and exact polynomial norm estimate verified in [Miy22-U004](../audits/literature/Miy22/Yin_U004_v1.md#miy22-u004).

For
\[
f\in F_s\cap L^2(M),\qquad
F_s=\operatorname{Div}_{U(M)}\mathbb C\langle s\rangle,
\]
[Miy26-U002](../audits/literature/Miy26/Yin_U002_v1.md#miy26-u002) proves that the right residuals of its Wick coefficients span a finite-dimensional space.
Its bounded regularizers and core commutator identity provide this missing interface; it is not inferred solely from an abstract rational expression.

Yin_C_F0015 then gives norm convergence in $C^*(s)$.
The full known result, with the additional Miy22 bounded-intersection theorem, is
\[
F_s\cap L^2(M)=F_s\cap M
=\operatorname{Div}_M\mathbb C\langle s\rangle.
\]
The final bounded scalar-closure equality is an imported model theorem, not part of Yin_C_F0015 alone.
This includes one semicircular variable; factoriality is not needed.

### Standard circular variables through semicircular coordinates

For $d$ standard free circular variables, use
\[
c_j=\frac{s_{2j-1}+is_{2j}}{\sqrt2},
\]
where $s_1,\ldots,s_{2d}$ are standard free semicircular.
The inverse linear formulas express both real coordinates in $c_j,c_j^*$.
Therefore
\[
W^*(c_1,\ldots,c_d)=W^*(s_1,\ldots,s_{2d}),
\qquad
F_{(c,c^*)}=F_s.
\]
Every affiliated rational L2 expression in $c,c^*$ is covered by the preceding theorem; expressions using only the $c_j$ lie in a subfield of this same ambient rational field and are covered as well.

The literal Yin_C_F0015 basis is the full semicircular Wick basis on $2d$ letters.
Holomorphic words $c_w$ span only a proper holomorphic subspace and must not be called a basis of the whole tracial L2 space.
The [Miy26 circular coordinate conventions](../audits/literature/Miy26/Yin_U001_v2.md#circular-word-conventions) retain that distinction.
No normality of the individual circular variables is asserted or needed for this coordinate application.

### A concrete nonfree polynomial-coordinate family

The [checked Yin_C_F0006 transfer](../claims/Yin_C_F0006_v1.md#yin_c_f0006) includes
\[
X_1=s_1+s_2^2-1,\qquad X_2=s_2,
\qquad
s_1=X_1-X_2^2+1,\quad s_2=X_2.
\]
Both coordinates are selfadjoint, and their polynomial algebras, affiliated division closures, and generated von Neumann algebras agree with those of $s_1,s_2$.
Thus an $f\in F_X\cap L^2$ is exactly an element of $F_s\cap L^2$ for purposes of the preceding theorem.

Use the inherited polynomials $P_w=U_w(s_1,s_2)$, now expressed as polynomials in $X_1,X_2$.
Their orthonormality, residual property and norm estimate are unchanged.
The grading is the original Wick word length in $s$, not the ordinary polynomial degree in $X$.
This supplies a positive nonfree family without asserting a new law-dependent estimate.
Nonfreeness is already checked in Yin_C_F0006 by
\[
\tau\bigl(X_1(X_2^2-1)\bigr)=1
\]
for centered factors.

Other boundedly invertible rational coordinate changes covered by Yin_C_F0006 preserve the appropriate rational fields and bounded closures under its exact hypotheses.
They permit inherited use of the known model, even when the transported basis elements are bounded rational functions rather than polynomials in the new coordinates.
This does not extend to an arbitrary analytic coordinate change.

## 2. Explicit Finite-State Coefficient Examples

These examples verify square summability before invoking Yin_C_F0015.
Their role is to illustrate the lemma directly, not to assert a new general rationality theorem.

### Rank-one coefficients in several semicircular variables

For scalars $t_1,\ldots,t_d$ with
\[
a=\sum_{i=1}^d|t_i|^2<1,
\]
put $\alpha_\varepsilon=1$ and
\[
\alpha_{i_1\cdots i_m}=t_{i_1}\cdots t_{i_m}.
\]
Then
\[
R_v\alpha=\alpha_v\alpha,\qquad
\sum_{|w|=m}|\alpha_w|^2=a^m,\qquad
\sum_w|\alpha_w|^2=\frac1{1-a}.
\]
Thus the residual space has dimension one, and the orthonormal Wick expansion defines an actual L2 vector, hence its canonical affiliated operator.
Yin_C_F0015 makes its homogeneous expansion norm convergent in $C^*(s)$.
This conclusion does not rely on an unproved identification of its scalar output with a formal inverse.

More generally, a prescribed finite realization with a positive definite state norm satisfying
\[
\sum_i\|A_iv\|_G^2\le\eta\|v\|_G^2,\qquad \eta<1,
\]
has square-summable output coefficients:
\[
\sum_{|w|=m}|\lambda A_w\gamma|^2
\le\|\lambda\|_{G,*}^2\,\eta^m\|\gamma\|_G^2.
\]
This follows by iterating the displayed state-energy estimate and the output-functional bound.
It is an explicit sufficient way to build examples, distinct from assuming that a rational element already comes with such a norm.

### One-variable Chebyshev resolvent

Let $s$ have the standard semicircular law and set
\[
W_0=1,\quad W_1=s,\quad W_{n+1}=sW_n-W_{n-1}.
\]
Thus $W_n=U_n^{\mathrm{classical}}(s/2)$; this states the normalization explicitly.
For real $|r|<1$,
\[
f_r=\sum_{n\ge0}r^nW_n,\qquad
\|f_r\|_2^2=\sum_{n\ge0}r^{2n}=\frac1{1-r^2}.
\]
The coefficients have residual rank one.
Also
\[
\sum_{n\ge0}\|r^nW_n\|
\le\sum_{n\ge0}(n+1)|r|^n
=\frac1{(1-|r|)^2}.
\]
Multiplying this norm-convergent sum by $1-rs+r^2$ and applying the recurrence cancels all positive-degree coefficients, giving
\[
f_r=(1-rs+r^2)^{-1}.
\]
The denominator is bounded below on $[-2,2]$ by $(1-|r|)^2>0$, independently confirming bounded invertibility.
The case $r=0$ is the constant $1$.
The example verifies both actual L2 convergence and operator-domain meaning; it is not merely a formal generating-function identity.

## 3. Known Results Requiring an Indexing or Subspace Adaptation

### Free Haar unitaries

For finitely many free Haar unitaries $u_i=\lambda(g_i)$ in $M=L(F_d)$, [Miy26-U003](../audits/literature/Miy26/Yin_U003_v1.md#miy26-u003), Theorem 3.5, proves the rational L2-to-bounded conclusion, with the retained Lin00/DR97 interfaces stated there.

The orthonormal Fourier basis is indexed by reduced group words.
It is not indexed by all words in the free monoid on $g_i,g_i^{-1}$: nonreduced words repeat group elements, so simply listing all of them destroys orthonormality.

The [DR97-U004 argument](../audits/literature/DR97/Yin_U004_v1.md#dr97-u004) handles this exactly.
Extend coefficients by zero on nonreduced words.
This reduced-word support is a regular language, with adjacent inverse letters forbidden.
The pertinent rationality theorem supplies a recognizable zero-extended series.
Its degree energy is rational, while the group Haagerup estimate applies to the reduced-support homogeneous sums.
The resulting scalar norm-convergence proof has the same mechanism as Yin_C_F0015.

Accordingly, the Haar result is already known and locally audited, but is not a literal substitution into Yin_C_F0015's full-monoid basis statement.
The word-language adaptation is supported by DR97; a universal theorem for other groups or normal-form languages is not established here.

### Classical Hardy functions

For $H^2(\mathbb T)$, the functions $z^n$, $n\ge0$, are orthonormal and satisfy the one-dimensional homogeneous estimate $K_n=1$.
They span a proper closed subspace of $L^2(\mathbb T)$, so this is a subspace variant of Yin_C_F0015.
For a square-summable analytic coefficient sequence of finite Hankel rank, the same finite-state decay argument gives a bounded rational boundary function.

The exact classical result and both Fourier-block conventions are recorded in [Miy22-U009](../audits/literature/Miy22/Yin_U009_v1.md#miy22-u009).
A Hankel operator on an arbitrary L2 symbol sees only one Fourier half; its finite rank does not make the entire symbol rational without a normalization or another block condition.
The full one-Haar case belongs to the preceding reduced-word discussion.

## 4. Prospective Model Classes and Their Missing Inputs

### Nonzero-q Gaussian systems

The [selected MS23 interface](../claims/Yin_C_F0016_v1.md#regularity-strategy-evidence) supplies a homogeneous Wick estimate in the deformed Hilbert norm and strong conjugate-variable regularity.
For $q\ne0$, the raw tensor-word vectors are not the standard free-monoid orthonormal basis used in Yin_C_F0015.

One can seek orthonormal coordinates within each homogeneous level, but such a change of coefficients need not preserve finite residual dimension or a fixed finite linear realization.
The required next result is a finite-residual/energy theorem compatible with the q-deformed geometry for the intended rational elements.
The norm estimate alone does not establish it.
The source's polynomial-domain duals also must not be silently assumed bounded.
No general rational-L2 boundedness theorem for this class is claimed from the inspected material.

### Holomorphic R-diagonal systems

The [KS07 statement already inspected](../claims/Yin_C_F0016_v1.md#regularity-strategy-evidence), Theorem 1.3, gives a square-root degree bound for homogeneous holomorphic polynomials in freely independent identically distributed bounded R-diagonal inputs.
Its estimate does not cover an arbitrary mixed-star expansion.

For a prescribed holomorphic coefficient series, a subspace version of Yin_C_F0015 is a plausible direct framework once orthonormal normalization and actual square summability are established.
A theorem for all affiliated rational L2 elements additionally needs to show that the relevant elements lie in the chosen holomorphic subspace and that their coefficients have finite residual dimension.
Neither follows from the homogeneous norm estimate.
The full circular case above is known through semicircular coordinates; that argument must not be transferred to arbitrary R-diagonal variables merely because they share R-diagonality.

### Free Meixner and finite-recursion families

[Ans07, *Free Meixner states*](https://arxiv.org/abs/math/0702158) is a discovery lead: its author-provided abstract describes orthogonal-polynomial recursions, resolvent-type generating functions, and tracial examples.
Only that abstract and publication metadata were inspected for this note.

A reasonable next test is a selected bounded faithful tracial model with finitely described Jacobi or word-recursion data.
One must verify a nondegenerate orthonormal basis, subexponential homogeneous norms, and a mechanism producing finite residuals for the particular rational inputs.
A finite recursion for the basis polynomials is not automatically a finite recurrence for the coefficients of every rational function in that basis.
Parameter regimes with atoms, degeneracy, or nontracial states need their own applicability check.
This is a proposed research family, not a confirmed Yin_C_F0015 application.

### Analytic transport and regularity hypotheses

The [GS14 interface](../claims/Yin_C_F0016_v1.md#regularity-strategy-evidence) gives analytic transport under quantitative analytic smallness assumptions.
It does not state that the transport or its inverse is rational.
Consequently rational fields and finite residual realizations need not pass through such a map.
The precise rational-coordinate examples in Section 1 provide supported transfers; a general analytic transport needs an additional compatibility argument.

[Yin_C_F0016](../claims/Yin_C_F0016_v1.md#yin_c_f0016) already rules out finite Fisher information as a substitute for the missing structure, and supplies a one-variable obstruction even with bounded Lipschitz conjugates.
These facts do not decide the named prospective model classes; they explain why their specific polynomial/shift geometry must do more than generic regularity.

## 5. Evidence and Next Use

This note read the existing Yin_C_F0015 proof, Miy22/Miy26/DR97 audits, Yin_C_F0006 coordinate transfers, and the selected regularity-source interfaces.
The explicit coefficient and Chebyshev examples were checked algebraically, with their actual L2 norms.
No numerical computation or formal verification was used.

One targeted primary search on 2026-09-09 addressed the Meixner recurrence lead.
The [arXiv record](https://arxiv.org/abs/math/0702158) and [author's publication list](https://people.tamu.edu/~manshel/publications.html) identify Michael Anshelevich, *Free Meixner states*, Communications in Mathematical Physics 276 (2007), 863-899, DOI 10.1007/s00220-007-0322-3.
The arXiv record has v1 submitted 2007-02-06.
The abstract and metadata were inspected; no PDF or exact theorem proof was read or downloaded.
The sole bibliography remains [literature/readme.md](../literature/readme.md).

Known positive families above are not presented as new results.
Further work should select one prospective model and discharge its identified input gaps.
No positive theorem for a new deformation, arbitrary R-diagonal family, general Meixner class, or analytic transport is asserted by this classification.

The actual [complete application-classification and example finding](../audits/reviews/Yin_R_F0055_v3.md#finite-residual-applications-finding) retains its original 2026-09-09 date, inspected scope and source-review limits.

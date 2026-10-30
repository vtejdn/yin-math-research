---
author: Yin
---

# Holomorphic R-Diagonal Boundedness: Positive Scope and Obstruction

<a id="holomorphic-r-diagonal-boundedness-route"></a>
Date: 2026-09-09.
Research route: [Yin_S_F0009](../strategies/Yin_S_F0009.md#s_f0009).
Authorization: the user's explicit Yin_T_F0001 extension selects the holomorphic R-diagonal model.
Claim assessments belong to the responsible Claim materials and their selected decisions; the [Claim index](../claims/index.md) provides navigation.

## Result of the first discriminating step

[Yin_C_F0017](../claims/Yin_C_F0017_v1.md#yin_c_f0017) proves that, for a finite free identically distributed bounded R-diagonal family, a recognizable holomorphic coefficient series which is actually square summable in the monomial L2 norm has a norm-convergent evaluation in scalar division closure.
Its proof adapts the Yin_C_F0015 sequence argument to the proper holomorphic subspace and then controls every entry of a minimal matrix realization before scalar elimination.

[Yin_C_F0019](../claims/Yin_C_F0019_v1.md#yin_c_f0019) proves the complementary obstruction: $a=uh$ with $u$ Haar, $h$ carrying the beta density $140t^3(1-t)^3$, and $u,h$ free, has an unbounded inverse of L2 norm squared 7.
The exact normal generating tuple $(u,h)$ has explicitly constructed bounded duals.
Thus restricting an affiliated rational expression to a single R-diagonal variable does not force rational L2 boundedness.

The original [Yin_C_F0017 finding](../audits/reviews/Yin_R_F0068_v1.md#historical-holomorphic-realization) and [Yin_C_F0019 finding](../audits/reviews/Yin_R_F0065_v1.md#r-diagonal-inverse-finding) found no mathematical gap at these exact hypotheses.
Their original dates, actual relationships and source boundaries remain in the linked findings.
There is no contradiction: the negative inverse lies in gauge degree $-1$, orthogonal to the positive-word holomorphic subspace.

[Yin_C_F0021](../claims/Yin_C_F0021_v1.md#yin_c_f0021) takes a further intrinsic step for one R-diagonal variable: an affiliated scalar rational element in the positive-power L2 subspace belongs to bounded scalar division closure.
It derives finite residual dimension from the polynomial equation on that subspace, where multiplication by $a$ is a scaled unilateral shift.
Its actual complete proof is selected by the current responsible Claim decision.
The [retained original finding](../audits/reviews/Yin_R_F0065_v1.md#intrinsic-holomorphic-finding) records the original 2026-09-09 check.
No separate coefficient-state hypothesis or injectivity assumption on $a$ is imposed.

## Three meanings of holomorphic rationality

| Meaning | What it supplies | What remains necessary |
| --- | --- | --- |
| A rational formal power series regular at zero | A finite linear realization, equivalently finite coefficient residual/Hankel rank | Weighted square summability at the given operator distribution, and identification of the evaluated operator with that series |
| An L2 vector in the positive-word subspace with finite residual dimension | The two coefficient hypotheses in Yin_C_F0017, hence its bounded scalar rational evaluation | Nothing further for Yin_C_F0017; arbitrary L2 vectors in that subspace need not have finite residual dimension |
| An affiliated evaluation of a rational expression using only $a_i$ and scalar inverses | An element of the corresponding affiliated division closure when all inverses are defined | It need not lie in the positive-word subspace or have square-summable Taylor coefficients; Yin_C_F0019 refutes unrestricted boundedness |

Regularity of the scalar rational function at zero does not resolve the evaluation distinction.
For a Haar unitary $u$ and $0<|\lambda|<1$, $(u-\lambda)^{-1}$ is bounded but has only negative Fourier powers.
Its formal Taylor series at zero has exponentially growing positive-power coefficients.
This elementary example is checked in Yin_C_F0017.

For one variable, Yin_C_F0021 proves the missing coefficient identification when the evaluated element is already in the positive-power subspace.
Its regular polynomial denominator gives an equation on the unilateral shift; this forces regularity at zero and a constant finite coefficient recurrence.
Thus the finite residual condition becomes a consequence of scalar rationality and the intrinsic subspace condition in this case.
Several noncommuting variables do not have the same scalar fraction reduction.

## Interface with the normal affiliated theorem

[Yin_C_F0013](../claims/Yin_C_F0013_v1.md#yin_c_f0013) assumes the listed generators are normal and have a bounded dual system.
A nonnormal R-diagonal tuple cannot be substituted into that theorem.

For circular variables, use the real and imaginary semicircular coordinates, with the appropriate scalar rescaling of the standard duals.
For Yin_C_F0019, use the normal polar-coordinate pair $(u,h)$ and its explicitly normalized free-product duals.
In a general R-diagonal model, passing to real and imaginary parts supplies normal generators but does not supply the dual hypothesis.
Already the real and imaginary parts of a Haar unitary obey a polynomial relation.
Yin_C_F0019 records this exact boundary.

The positive coefficient theorem Yin_C_F0017 needs neither normality nor duals.
Consequently it can be used independently of Yin_C_F0013 when its own coefficient assumptions are available.

<a id="ks07-selected-input"></a>
## Selected source inputs and reading evidence

The source-specific reusable record is [KS07-U001](../audits/literature/KS07/Yin_U001_v1.md#ks07-u001).
It records the accepted strong Haagerup theorem and the monomial L2 calculation.
The author of this route inspected the arXiv v2 text at Definition 1.2/Theorem 1.3 (printed pp. 2-3), the R-diagonal cumulant definition (pp. 7-8), and Section 4.1, equations (4.1)-(4.3) (p. 17).
The original complete inequality proof is not claimed reviewed.
Author-hosted journal PDF retrieval timed out, and the requested arXiv page screenshots failed; this reading used the parsed source formulas and their independent reconstruction.

For the negative example, [NS06-U001](../audits/literature/NS06/Yin_U001_v1.md#ns06-u001) records Corollary 15.9 and the relevant free polar-decomposition interface in the supplied local publisher-layout PDF.
Its source version differs from the online author copy used by the older Miy26 audit.

## Search, decisions, and remaining work

On 2026-09-09 the starting gap was whether the strong Haagerup estimate could be combined with actual monomial residuals.
The targeted primary-source reading found KS07's exact orthogonality calculation; this removes the orthogonal-basis obstacle within the holomorphic subspace.
Minimal realization then supplied a usable matrix inverse and scalar closure rather than only norm-closed-algebra membership.

The next test was whether an arbitrary affiliated rational L2 element must enter that subspace.
The explicit inverse in Yin_C_F0019 answers negatively.
A search for a normalized bounded-dual free-product extension did not identify a needed primary statement; the last-block construction was instead proved directly.
NS06 supplied the exact Haar-product R-diagonal statement.
Existing HL00 Brown-measure interfaces were consulted as possible leads, but no Brown-measure or spectrum theorem is needed in either proof.

This bounded search stopped after the positive coefficient theorem and negative affiliated example.
A subsequent local deduction produced Yin_C_F0021 without another source search.
No novelty or completeness claim is made.
After its independent review, continue by investigating the many-variable intrinsic subspace interface or bounded scalar reconstruction outside the positive-word subspace.
Any unrestricted affiliated-L2 claim for all bounded R-diagonal elements must retain the Yin_C_F0019 obstruction.

---
author: Yin
---

# Divided differences detect rational functions on abelian subgroups

## Statement

Let \(G\) be a finitely generated group with marked generators \(g_j\), and let \(D_G,R_G\) denote the division and \(*\)-regular closures of \(\mathbb CG\) in \(U_G=L^0(\mathcal N(G))\).
Suppose \(L\cong\mathbb Z^d\) is a subgroup whose inclusion induces an injection \(L\otimes\mathbb Q\to G_{\mathrm{ab}}\otimes\mathbb Q\).
Then
\[
                R_G\cap U_L=D_G\cap U_L=\operatorname{Frac}(\mathbb CL).
\]
This also holds if the injection condition holds for \(L\cap H\) in the abelianization of some finite-index subgroup \(H\le G\).
In particular a solution of the [unrestricted finite-rank equation](Yin_C_A0131_v1.md#statement) for an affiliated function supported on such an \(L\) always gives a constant lift of its graph symmetry, with contraction probability one. [Angular criterion](Yin_C_A0174_v1.md#statement)
The hypotheses concern only the position of \(L\) in \(G\) or a finite cover.
They allow nonamenable ambient groups and zero divisors in their division closures.

There is a quantitative one-variable assertion in the original group.
Let \(\chi:G\to\mathbb Z\) be a character, and let \(v\in D_G\) be a unitary which changes to \(s^k v\) under the trace-preserving action \(g\mapsto s^{\chi(g)}g\) for \(s\in\mathbb T\), with \(k\ne0\).
For any Haar-measurable complex function \(f\), finite almost everywhere, \(f(v)\) satisfies the unrestricted equation if and only if \(f\) agrees almost everywhere with a complex rational function.
Given a solution with \(\operatorname{rank}_{\mathbb C}T_j=r_j\), its reduced rational function satisfies
\[
                |k|\,\deg f\ \le\ \sum_j|\chi(g_j)|r_j .
\]
Here the degree is the larger of the two reduced polynomial degrees, and constants have degree zero.
For \(v=g\) with \(g\) of infinite order and a witness supported on that single marked label, equality can be attained whenever \(\chi(g)\ne0\).

## Argument

### A rank bound for a randomly sampled divided difference

Write \(\alpha_s\) for the indicated action of the circle on the affiliated ring.
On \(\ell^2(G)\) it is implemented by the diagonal unitary multiplying the basis vector at \(g\) by \(s^{\chi(g)}\).
It preserves the group trace and hence the affiliated functional calculus.
For any solution for \(u\), the [finite-rank tensor identity](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) gives
\[
  u\otimes1-1\otimes u=\sum_{j,\ell}
     (l_{j\ell}g_j\otimes b_{j\ell}-l_{j\ell}\otimes g_j b_{j\ell})
\]
in \(U_G\otimes_{\mathbb C}U_G\), with at most \(r_j\) simple input tensors for label \(j\).
For any \(N\) and pairwise distinct circle parameters \(s_1,\ldots,s_N,t_1,\ldots,t_N\), apply \(\alpha_{s_i},\alpha_{t_b}\) to the respective factors, multiply and divide by \(s_i-t_b\).
The matrix
\[
          \left[\frac{\alpha_{s_i}(u)-\alpha_{t_b}(u)}
                            {s_i-t_b}\right]_{i,b=1}^{N}
\]
has unnormalized affiliated rank at most \(B_\chi=\sum_j|\chi(g_j)|r_j\).
Indeed each simple tensor gives a scalar matrix with entries \((s_i^h-t_b^h)/(s_i-t_b)\), \(h=\chi(g_j)\), multiplied on its two sides by diagonal affiliated matrices with entries \(\alpha_{s_i}(l_{j\ell})g_j\) and \(\alpha_{t_b}(b_{j\ell})\).
The scalar rank is at most \(|h|\) by the finite geometric sum for positive \(h\), by multiplying that sum by invertible diagonals for negative \(h\), and by vanishing for \(h=0\).
Rank subadditivity gives the bound, including for unbounded \(u\).

Here is the measurable consequence of this bound.
Let \(F\) be a measurable function on the circle, finite almost everywhere.
Sample two independent infinite lists of independent uniform points \(s_i,t_b\).
For the first \(N\) from each list form the ordinary complex matrix of divided differences of \(F\).
Almost surely its ranks increase to the reduced rational degree of \(F\), with value \(+\infty\) if \(F\) is not rational almost everywhere.
To prove this, fix distinct \(t_1,\ldots,t_m\) where \(F\) is finite and consider the \(m\) column functions \((F(s)-F(t_b))/(s-t_b)\).
A nontrivial linear dependence almost everywhere gives
\[
 F(s)=\frac{\sum_b c_b F(t_b)/(s-t_b)}{\sum_b c_b/(s-t_b)} .
\]
The denominator is nonzero since its simple fractions have distinct poles.
Clearing their common denominator gives a rational function of degree at most \(m-1\).
Thus these columns are independent for every \(m\) up to the claimed limiting rank.
Independent columns as measurable functions produce full column rank eventually on independent sample rows almost surely.
In fact their row vectors have essential linear span \(\mathbb C^m\).
There is positive probability that \(m\) sampled rows span it, by successively drawing a vector outside any previously obtained proper span.
Independent repeated batches give the assertion, and taking the countable intersection over \(m\) suffices.
For the reverse bound when \(F=p/q\) has degree \(d'\), exclude its poles and the null set on which it differs from \(p/q\).
The polynomial \((p(s)q(t)-p(t)q(s))/(s-t)\) has degree at most \(d'-1\) in each variable for \(d'>0\).
All columns therefore lie in one \(d'\)-dimensional space after diagonal scaling.
Constants give zero columns.

For the unitary \(v\) of the statement, rotation invariance of the trace and surjectivity of \(s\mapsto s^k\) force its law to be Haar measure.
Take \(u=f(v)\).
In its abelian spectral representation the sampled affiliated rank is the Haar integral over \(x\) of the ordinary divided-difference rank for \(s\mapsto f(xs^k)\).
Ranks of matrices with entries in this abelian subalgebra agree in the ambient group algebra of affiliated operators, since their kernel projections and traces agree.
Average over all samples and use monotone convergence on increasing square submatrices and Fubini's theorem.
The expected limiting rank, also averaged over \(x\), is at most \(B_\chi\).
Choose Borel representatives for the functions.
Finite matrix rank is determined by minors, so all objects under the integral are measurable.
Consequently \(f(xs^k)\) is rational almost everywhere in \(s\) for almost every \(x\).
For any such \(x\), its rational representative is invariant under rotation of \(s\) by the \(|k|\)-th roots of unity, since almost-everywhere agreement of rational functions implies equality.
Their fixed field is \(\mathbb C(s^{|k|})\), by the basis \(1,s,\ldots,s^{|k|-1}\) over that field.
Rotating \(x\) back and using invariance of Haar measure under the power map now gives a rational representative for \(f\).
Composition with \(s\mapsto xs^k\) multiplies its degree by \(|k|\), including for negative \(k\) by inversion.
Thus the limiting rank averaged over \(x\) is precisely \(|k|\deg f\).
Conversely any nonzero denominator polynomial in \(v\) is an affiliated unit by its Haar law, so every rational \(f(v)\) belongs to \(D_G\).

For \(v=g\), choose coprime polynomials \(p,q\) representing \(f\).
For degree \(d'>0\) expand the preceding divided-difference polynomial as a sum of at most \(d'\) products of a polynomial in \(s\) and one in \(t\), by collecting the powers of \(s\).
Divide the two factors respectively by \(q(s)\) and \(q(t)\).
Substitution of \(g\) in both tensor legs then expresses \(\delta f(g)\) as at most \(d'\) simple input tensors at the single label \(g\), since the boundary operator on that pair of legs multiplies by \(s-t\).
The tensor identity restores the bounded denominator witnesses by clearing the finitely many affiliated factors.
Constants need no such tensors.
This proves sharpness.

### From circle slices to a rational function on a torus

Choose generators of \(L\) giving integral coordinates on its dual torus.
By the abelianization hypothesis, for each coordinate there is an integral character of \(G\) vanishing on the other generators of \(L\) and taking a nonzero value on the chosen one.
Indeed a rational functional on the image of \(L\otimes\mathbb Q\) extends to \(G_{\mathrm{ab}}\otimes\mathbb Q\), and finite generation permits clearing its denominators.
Write \(u=f(x_1,\ldots,x_d)\) in the Haar spectral representation of \(L\).
If \(u\in R_G\), apply the same averaged bound for each chosen character and integrate also over the other \(d-1\) coordinates.
It gives almost-everywhere rationality on almost every coordinate circle: finite limiting rank holds almost everywhere in the other coordinates and almost everywhere in the initial rotation \(x\).
The root-of-unity argument removes the power in each of these slices.

We give the passage from these separate assertions to a single rational function, since the degree bounds for the slices at this stage are only integral bounds in the other coordinates.
Induct on \(d\), writing coordinates as \(s,y\in\mathbb T\times\mathbb T^{d-1}\).
For almost every \(s\), \(f(s,\cdot)\) is rational almost everywhere in \(y\) by induction and Fubini.
For almost every \(y\), \(f(\cdot,y)\) agrees almost everywhere with a rational function \(r_y\).
Its degree is a measurable function of \(y\), since it equals the expected limiting rank of the sampled divided-difference matrices for that slice.
Choose \(a\ge0\) such that the set of \(y\) having degree exactly \(a\) has positive measure.
Choose \(2a+1\) distinct independent sample values \(s_i\).
Almost every such choice gives rational \(f(s_i,\cdot)\) and, for almost all \(y\) in this set, correct finite sample values of \(r_y(s_i)\).
For measurability in this last assertion the representatives \(r_y\) can be chosen measurably: use an infinite independent sample sequence on the first coordinate and solve the ordinary rational interpolation equations from its first \(2a+1\) values on degree-\(a\) slices.
Equivalently the event that the interpolated rational function agrees with the given slice almost everywhere is measurable by its integral equality test, using minors to choose a normalized solution, and it has sample probability one for each such \(y\).

With such a fixed sample, put \(K=\mathbb C(y_1,\ldots,y_{d-1})\) and consider the linear homogeneous interpolation equations over \(K\) for a pair of polynomials \(p,q\) of degrees at most \(a\) in \(s\).
There are \(2a+1\) equations on \(2a+2\) coefficients.
At almost every \(y\) of degree \(a\) their solution space is one-dimensional: cross multiplication against the reduced pair for \(r_y\) gives a polynomial of degree at most \(2a\) vanishing at all sample points.
Coprimality and exact degree then force proportionality.
Thus a maximal minor is nonzero somewhere on a positive-measure subset and hence is a nonzero element of \(K\).
The interpolation equations over \(K\) have a one-dimensional kernel, and a nonzero solution specializes to the correct pair up to a nonzero scalar for almost every \(y\) in this positive-measure set.
Here a nonzero rational function on a torus is finite and nonzero almost everywhere, by induction on the number of variables applied to its numerator and denominator polynomials.
Consequently \(p(s,y)=q(s,y)f(s,y)\) for almost all pairs with \(y\) in that set.
For almost every fixed \(s\), both sides are rational functions of \(y\), so equality on a positive-measure subset forces equality almost everywhere in \(y\).
Another application of Fubini proves joint rationality, as \(q\ne0\).
This proves \(R_G\cap U_L\subseteq\operatorname{Frac}(\mathbb CL)\).
The reverse inclusions follow because every nonzero Laurent polynomial on the torus is an affiliated unit.

### Passing to a finite cover

Put \(L_0=L\cap H\).
In the [finite-index coset representation](../ledger/Yin_L_A0073_v1.md#the-finite-index-coefficient-matrices), elements of \(R_G\) have entries in \(R_H\): the matrix ring over \(R_H\) is \(*\)-regular and its relative inverses agree with those in the affiliated ring by their support identities.
This includes the first diagonal compression of \(g^{-1}u\) for each \(g\in L\).
On \(U_L\) the group ring expansion by the finitely many \(L_0\)-cosets extends to every affiliated element, with coefficients in \(U_{L_0}\).
In fact on the dual torus the finite character group of \(L/L_0\) acts by rotations.
The projection onto each character component is the corresponding finite Fourier average, valid for finite almost-everywhere functions, and removal of a coset representative leaves an invariant function in \(U_{L_0}\).
The resulting finite expansion \(u=\sum_{g\in L/L_0} g u_g\), using one representative per coset, has first-block coefficient \(u_g\) for \(g^{-1}u\), since the other cosets send the first summand to different summands.
If \(u\in R_G\), each such coefficient thus lies in \(R_H\cap U_{L_0}\).
The preceding result in \(H\) places it in \(\operatorname{Frac}(\mathbb CL_0)\).
The finite expansion gives \(u\in\operatorname{Frac}(\mathbb CL)\), as asserted.

## Assessment history

### Decision abelian-subgroup-functions

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:01 |
| status | proved |
| reason | Sampled divided differences detect rational degree, and rational interpolation recovers the torus function. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equality on the affiliated ring of a visible free abelian subgroup and the one-variable degree bound. |
| argument | [Argument](#argument) | Sampled ranks, measurable slices, rational interpolation and restriction to finite-index subgroups. |
| dependency | [Tensor identity](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) | Finite rank of the character-twisted difference. |
| dependency | [Constant graph lift](Yin_C_A0174_v1.md#the-angular-probability-bound) | Contraction with probability one for a rational input. |
| dependency | [Coset matrices](../ledger/Yin_L_A0073_v1.md#the-finite-index-coefficient-matrices) | Restriction to a finite-index subgroup. |
| review | [Abelian subgroup functions](../audits/reviews/Yin_R_A0180_v1.md#abelian-subgroup-functions) | Independent review of the statement and argument. |

## Current assessment

[Selected decision](#decision-abelian-subgroup-functions)

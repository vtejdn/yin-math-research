---
author: Yin
---

# Conditional Haar addition and rank-one Schur determinant limits

This candidate was developed on 2026-11-05 for the [Haar affine determinant Task F0015](../tasks/Yin_T_F0015_v1.md#contract).
It gives a full logarithmic limit in a positive-FK, unbounded-free-inverse coefficient class, using a physical-size Haar perturbation after an exact rank-one Schur reduction.
The conditional Haar-additive argument and source preparation were developed collaboratively by the assigned proof-development agents for Yin.
The [independent complete review](../audits/reviews/Yin_R_F0198_v1.md#independent-conditional-schur-proof) supports its exact restricted scope, with no claim of novelty or unrestricted Task completion.

<a id="statement"></a>
## Exact statements

<a id="conditional-haar-additive-statement"></a>
## Conditional Haar-additive logarithmic theorem

Let \(\mathcal F_N\) be a background sigma algebra, let \(D_N\in M_N(\mathbb C)\) be \(\mathcal F_N\)-measurable, and assume that the conditional law of \(V_N\) given \(\mathcal F_N\) is Haar probability on \(U(N)\).
No relation between the sigma algebras or matrices at distinct dimensions is assumed.
Suppose that some fixed \(M<\infty\) and deterministic probability measure \(\mu\) on \([0,M]\) satisfy
\[
 \|D_N\|\le M\quad\text{eventually almost surely},
 \qquad \mu_{|D_N|}\Longrightarrow\mu\quad\text{almost surely}.
 \tag{Background}
\]
Put \(\nu=\widetilde\delta_1\boxplus\widetilde\mu\).
Assume that \(\widetilde\mu\) is supported at more than two points and that zero lies in the regular bulk of \(\nu\) as defined in [Ho--Zhong Definition 2.7](../audits/literature/HZ25/Yin_U001.md#regular-bulk-definition).
Let \(d\ge0\) have law \(\mu\), and let \(v\) be a Haar unitary free from \(d\), in a finite tracial von Neumann algebra.
Then
\[
 \frac1N\log|\det(D_N+V_N)|
 \longrightarrow c=\log\Delta(d+v)=\int\log|x|\,d\nu(x)\in\mathbb R
 \quad\text{almost surely}.
 \tag{Conditional-log}
\]
The singular-value measures also converge weakly almost surely to the positive-half singular law corresponding to \(\nu\).
This project deduction retains the exact regular-bulk and background hypotheses above.


<a id="affine-schur-statement"></a>
## Rank-one affine-pencil statement

Use the exact [F0015 input model](../tasks/Yin_T_F0015_v1.md#input-model-and-ordinary-determinant), with fixed auxiliary dimension m and coefficient tuple, independent full-complex Haar inputs within every dimension, and any allowed coupling between dimensions.
Separate one input, called V_N, whose coefficient is rank one, and write
\[
 L_N=B_N+(pq^*)\otimes V_N,\qquad
 B_N=A_0\otimes I_N+\sum_{j=1}^{r-1}A_j\otimes U_j^{(N)},
 \qquad p,q\in\mathbb C^m.
\]
Let B be the corresponding free background in M_m(M), let v be the remaining free Haar input, and assume that B is boundedly invertible.
Define
\[
 c=(q^*\otimes1)B^{-1}(p\otimes1)\in M,
 \qquad d=c^{-1},
\]
and assume that c is boundedly invertible and
\[
 \tau(d^*d)>1,\qquad \tau(c^*c)>1.
 \tag{Affine-bulk}
\]
Then the free pencil \(L=B+(pq^*)\otimes v\) has positive ordinary FK determinant and no bounded inverse, and
\[
 \frac1{mN}\log|\det L_N|
 \longrightarrow \log\Delta_{\operatorname{tr}_m\otimes\tau}(L)
 \quad\text{almost surely under every allowed coupling}.
 \tag{Affine-limit}
\]
Thus both full-limit and upper-limit assertions in both coupling regimes hold for this restricted coefficient class.
The condition permits arbitrary fixed dense background coefficients; it does not assert that every tuple containing a rank-one coefficient has the required inverses or strict bulk.
The [proved coefficient-position symmetry](Yin_C_F0192_v1.md#coefficient-gauge) permits first moving a rank-one coefficient from another position to the fresh Haar position, after which these assumptions must be verified for the resulting ordered tuple.

For every fixed invertible background B and invertible compression c_0 of nonconstant modulus, scaling the chosen rank-one coefficient by t gives this class throughout the nonempty open amplitude range
\[
 \|c_0\|_2^{-1}<|t|<\|c_0^{-1}\|_2.
 \tag{Amplitude}
\]
The proof supplies an explicit two-by-two tuple with
\[
 A_0=I_2,\quad
 A_1=\begin{pmatrix}1/10&0\\-2/5&0\end{pmatrix},\quad
 A_2=\begin{pmatrix}0&1\\0&1\end{pmatrix},
\]
for which d=(1+u/10)/(1+u/2), \(\tau(d^*d)=1+16/75\) and \(\tau(c^*c)=1+16/99\).
This example is not directly covered by the previously proved two-position, sparse fresh-edge or simultaneous triangular classes.


<a id="scalar-strict-triangle"></a>
## Direct scalar strict-triangle corollary

Let \(L_N=a_0I_N+a_1U_N+a_2V_N\) with fixed scalar coefficients and two independent Haar matrices within each dimension, and let \(L=a_0+a_1u+a_2v\).
Suppose that \(x_j=|a_j|^2\) satisfy
\[
 x_0<x_1+x_2,\qquad x_1<x_0+x_2,\qquad x_2<x_0+x_1.
 \tag{Scalar-triangle}
\]
Then every allowed cross-dimensional coupling satisfies
\[
 \frac1N\log|\det L_N|\longrightarrow\log\Delta(L)
 \quad\text{almost surely},
\]
and the free determinant is positive while the free inverse is unbounded.
This includes \(a_0=a_1=a_2=1\), where the complement \(1+u\) in a rank-one Schur presentation has no bounded inverse.
No conclusion at equality in (Scalar-triangle) or outside this strict region is asserted by this corollary.

## Accepted inputs and actual scope

[HZ25-U001](../audits/literature/HZ25/Yin_U001.md#model-and-local-law) supplies the inspected deterministic Haar-additive local law and its stochastic normalization from Theorem 2.8.
Its [subordination section](../audits/literature/HZ25/Yin_U001.md#subordination-neighborhood) supplies the exact regular-bulk and Proposition 2.2 continuity inputs; the fixed weak-neighborhood adaptation is proved locally below.
Its [least-value and tiny-integral section](../audits/literature/HZ25/Yin_U001.md#least-value-and-ultra-small-integral) supplies Theorem 3.2 and Lemma 4.4 with constants uniform over the additive deformation.
The source's global in-probability ESD theorem is not substituted for the logarithmic conclusion proved here.
The unit records the exact arXiv v4 edition, inspected passages, local displayed-index correction and original-proof inspection limits.

The [retained Haar interface](../ledger/Yin_L_F0062_v1.md#haar-pencils), with its [CM14 source note](../audits/literature/CM14/readme.md), supplies strong convergence for the fixed background coefficients.
Bounded inverse transfer and norm approximation by polynomials are used at the same exact scope as the bounded-inverse argument there.
The free rectangular identities below use [bounded ordinary FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) and [the retained triangular determinant identity](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) only with identity diagonal maps in the unipotent factors.
The coefficient permutation corollary uses the [proved structural result](Yin_C_F0192_v1.md#coefficient-gauge).
All conditional probability, integration, finite/free Schur identities and original coefficient checks are supplied explicitly below.

<a id="argument"></a>
## Complete candidate argument

<a id="conditional-haar-additive-argument"></a>
## Conditional Haar-additive resolvent proof

### A fixed neighborhood controls the empirical free convolution

Write \(\rho_N=\mu_{|D_N|}\), and denote \(\nu_\rho=\widetilde\delta_1\boxplus\widetilde\rho\) for any probability measure \(\rho\) supported on \([0,M]\).
For the limiting pair, regular bulk at zero means that both subordination values at zero are finite and have strictly positive imaginary parts, by Ho--Zhong Theorem 2.3.
The continuous boundary extensions in Proposition 2.1 and their ordinary upper-half-plane continuity give a bound for both limiting subordination functions on the compact segment \(i[0,1]\).
Their denominator \(\omega_1(i\eta)+\omega_2(i\eta)-i\eta\) has positive imaginary part at \(\eta=0\) by regular bulk and is nonzero for every \(\eta>0\), because it equals the reciprocal Cauchy transform there.
Continuity and compactness therefore give a strictly positive minimum for its absolute value on this whole segment.
Uniform convergence of both subordination functions then keeps every nearby empirical denominator above half that minimum, which is the needed uniform free-convolution bound.

Proposition 2.2 then implies
\[
 \sup_{0\le\eta\le1}|G_{\nu_\rho}(i\eta)|\le C
 \quad\text{whenever }d_{\mathrm L}(\rho,\mu)\le b,
 \tag{Free-neighborhood}
\]
for some fixed \(b,C>0\), with the same support bound \(M\).
Here is the needed passage from sequential convergence to an actual neighborhood.
If no such neighborhood existed, choose \(\rho_k\) supported in \([0,M]\) with \(d_{\mathrm L}(\rho_k,\mu)\to0\) and a violating value of \(\eta\in[0,1]\).
Bounded support makes this weak convergence equivalent to convergence of all moments.
Realize positive operators with those laws in one commutative finite tracial algebra, and apply Proposition 2.2 with \(\lambda=0\), \(K=\{0\}\), and \(K'=i[0,1]\).
Its uniform convergence of the two subordination functions contradicts the violation, using the correct identity \(G_{\nu_\rho}(z)=(\omega_{1,\rho}(z)+\omega_{2,\rho}(z)-z)^{-1}\).
The source's displayed denominator in the proof of Lemma 4.3 repeats the first subordination index; the governing relation (2.1) uses the sum of the two indices.
No quantitative convergence rate is used in this neighborhood argument.

Shrink \(b\) so that Theorem 2.8 also applies to the fixed pair \((\delta_1,\mu)\) and \(I=\{0\}\).
Define the within-dimension good background event
\[
 E_N=\{\|D_N\|\le M,\ d_{\mathrm L}(\rho_N,\mu)\le b\}.
\]
Assumption (Background) says that \(E_N\) holds eventually almost surely.
It does not require the probabilities of \(E_N^c\) to be summable.

### Conditional local law with a common deterministic bound

Conditional on \(\mathcal F_N\), singular-value decomposition of \(D_N\) reduces the singular values of \(D_N+V_N\) to those of \(\Xi_N+W_N\), where \(\Xi_N=\operatorname{diag}(s_j(D_N))\) and \(W_N\) remains Haar.
A single Haar matrix has the same distribution as a product of two independent Haar matrices, so this is the Ho--Zhong model with \(\Sigma_N=I_N\).
Theorem 2.8 supplies a uniform bound, in the [stochastic-domination convention](../audits/literature/HZ25/Yin_U001.md#stochastic-domination-definition), over the bounded deterministic inputs in its fixed Lévy neighborhood:
\[
 |G_N(i\eta)-G_{\nu_{\rho_N}}(i\eta)|
 \prec\frac1{N\eta(1+\eta)}.
 \tag{Conditional-local}
\]
The constants depend on the fixed limiting pair, support bound, spectral set, and chosen stochastic exponents, rather than on a convergence rate for \(\rho_N\).
Its fixed-neighborhood formulation permits each admissible finite input to be embedded into a deterministic sequence by filling other dimensions with bounded quantile approximations to \(\mu\).
Thus it is applicable inside \(E_N\) after conditioning on the background of this dimension.

For every fixed \(\eta>0\), (Conditional-local), (Free-neighborhood), and the convergence \(\rho_N\Rightarrow\mu\) give almost-sure convergence \(G_N(i\eta)\to G_\nu(i\eta)\), after intersecting a countable dense set of positive \(\eta\)'s.
The singular values are at most \(M+1\) eventually.
Compactness of probability measures on this interval, together with uniqueness of the Stieltjes transform on the positive imaginary axis for symmetric measures, identifies every weak subsequential limit with \(\nu\).
This proves the claimed almost-sure weak singular-value limit and hence convergence of every fixed positive-regularizer logarithm.
In particular, no extra random-matrix weak-convergence theorem is needed for the sum \(D_N+V_N\) once (Background) is supplied.

Only the within-dimension background is conditioned on.
Conditioning on the entire sequence of backgrounds could change the conditional Haar law under an arbitrary cross-dimensional coupling and is not used.
For any local-law failure event \(B_N\), uniformity gives
\[
 \mathbb P(E_N\cap B_N)
 =\mathbb E[1_{E_N}\mathbb P(B_N\mid\mathcal F_N)]
 \le N^{-D}.
\]
First Borel--Cantelli applies to these joint events, followed by the eventual almost-sure guard.
This is the step that preserves the contract's arbitrary-coupling quantifier.

### Integrating the local law instead of multiplying a floor by a count

Let \(h_N(\eta)=-\operatorname{Im}G_N(i\eta)\ge0\).
Fix \(\varepsilon\in(0,1)\) and a large fixed \(L\), and use the dyadic grid \(\eta_j=2^jN^{-L}\) up to one.
The number of grid points is \(O(\log N)\), and (Conditional-local) and (Free-neighborhood) imply, on \(E_N\) outside summable failures,
\[
 h_N(\eta_j)\le C+\frac{N^\varepsilon}{N\eta_j}.
 \tag{Grid}
\]
Choose the stochastic exponent \(D\) larger than three before the finite union over this grid.
For \(a\le\eta\le2a\), the spectral formula gives
\[
 \frac{\eta}{s^2+\eta^2}\le\frac{2a}{s^2+a^2},
 \qquad h_N(\eta)\le2h_N(a).
\]
Summing the grid intervals therefore gives, for each fixed \(\delta\in(0,1]\),
\[
 \int_{N^{-L}}^\delta h_N(\eta)\,d\eta
 \le C'\delta+O(N^{-1+\varepsilon}\log N)
 \quad\text{eventually almost surely}.
 \tag{Middle-integral}
\]
A final partial interval can be estimated by the same factor-two bound.

For the remaining ultra-small segment, Lemma 4.4 applies with \(\Sigma=I\), so its inverse condition holds for any fixed positive \(\alpha\).
Theorem 3.2 and the proof of Lemma 4.4 show that the constants are uniform over the deterministic additive deformation.
Consequently, for fixed positive \(c_0,C_0\),
\[
 \mathbb E\!\left[\int_0^{N^{-L}}h_N(\eta)\,d\eta
       \mid\mathcal F_N\right]
 \le N^{-c_0L/2+C_0}.
 \tag{Tiny-expectation}
\]
Choose \(L\) so large that \(c_0L/2-C_0>4\).
Markov's inequality at threshold \(N^{-1}\) and first Borel--Cantelli then show that this integral tends to zero almost surely, with no cross-dimensional independence.
The same least-singular-value bound, by sending its threshold to zero at fixed \(N\), gives invertibility almost surely, so the ordinary logarithms and the following defect identity are well defined on one countable intersection event.

Put \(Z_N=D_N+V_N\) and
\[
 \ell_{N,\delta}=\frac1{2N}\operatorname{Tr}\log(Z_N^*Z_N+\delta^2I),
 \qquad \ell_N=\frac1N\log|\det Z_N|.
\]
Direct differentiation of the finite spectral formula yields
\[
 \ell_{N,\delta}-\ell_N=\int_0^\delta h_N(\eta)\,d\eta.
 \tag{Defect}
\]
Combining (Middle-integral) and (Tiny-expectation) gives \(\limsup_N(\ell_{N,\delta}-\ell_N)\le C'\delta\) almost surely.
The fixed-regularizer limit \(\ell_{N,\delta}\to c_\delta\) follows from the already established compactly supported weak singular-value limit.
The regular-bulk bound near zero makes \(c_\delta\downarrow c\in\mathbb R\).
Thus
\[
 c_\delta-C'\delta\le\liminf_N\ell_N
 \le\limsup_N\ell_N\le c_\delta,
\]
and sending a countable sequence of \(\delta\)'s to zero proves (Conditional-log).

<a id="rank-one-schur"></a>
## Original affine-pencil Schur proof and examples

We apply the conditional Haar-additive lemma to a dense affine background and one rank-one fresh coefficient.
Separate one input V_N and write
\[
 L_N=B_N+(pq^*)\otimes V_N,
 \qquad
 B_N=A_0\otimes I_N+\sum_{j<r}A_j\otimes U_j^{(N)},
\]
with arbitrary fixed background coefficient matrices.
Let B be the corresponding free background and assume that B has a bounded inverse.
Define the scalar free compression
\[
 c=(q^*\otimes1)B^{-1}(p\otimes1),
\]
and assume that c also has a bounded inverse.
Put d=c^{-1} and impose the strict regular-bulk inequalities
\[
 \tau(d^*d)>1,\qquad\tau((d^{-1})^*d^{-1})>1.
 \tag{Schur-bulk}
\]
The claimed conclusion is the full almost-sure ordinary determinant limit for L_N under every allowed cross-dimensional coupling.
All background coefficients remain in the original affine contract, and the restrictions are explicit sufficient conditions on its actual free background and compression.

Strong Haar convergence and bounded polynomial approximation of the inverse give eventual invertibility of B_N and a uniform bound on B_N^{-1}, almost surely under every allowed coupling.
The corresponding finite compression
\[
 C_N=(q^*\otimes I_N)B_N^{-1}(p\otimes I_N)
\]
then converges strongly to c.
Because c has a bounded inverse, the same argument gives eventual invertibility and uniform inverse bounds for C_N.
The normality of C_N is not required.
Consequently D_N=C_N^{-1} has an eventual deterministic norm bound and its empirical singular-value distribution converges almost surely to that of |d|.
Whenever a finite inverse in this definition is unavailable, set D_N=0 merely to define a measurable statistic of the background at every dimension; the guard below excludes those exceptional early inputs.
The rational definitions agree eventually almost surely with the intended ones.

The complete normalized finite and free identities are
\[
 \det L_N=\det B_N\,\det C_N\,\det(D_N+V_N),
\]
and
\[
 m\log\Delta_{\operatorname{tr}_m\otimes\tau}(L)
 =m\log\Delta_{\operatorname{tr}_m\otimes\tau}(B)
  +\log\Delta_\tau(c)+\log\Delta_\tau(d+v).
 \tag{Schur-FK}
\]
For their common bounded rectangular step put \(X=B^{-1}(p\otimes1)\) and \(Y=q^*\otimes v\), and use the block matrix
\[
 T=\begin{pmatrix}I_m&X\\-Y&1\end{pmatrix}.
\]
Bounded unipotent multiplication reduces T both to diag(I_m+XY,1) and to diag(I_m,1+YX).
The unipotent determinants are one by the retained triangular identity with identity diagonal blocks.
Bounded ordinary FK multiplicativity therefore gives
\[
 m\log\Delta(I_m+XY)=\log\Delta(1+YX).
\]
Here YX=vc, whose ordinary determinant equals that of cv by unitary conjugation with v.
Finally 1+cv=c(d+v), with c boundedly invertible, giving (Schur-FK).
The finite identity follows by the same elimination or the ordinary rectangular determinant identity.
It applies whenever the finite B_N and C_N inverses exist, which is enough for the full-sequence limit.

Conditioning at dimension N on that dimension's background leaves V_N Haar on the full physical U(N).
The [conditional Haar-additive argument](#conditional-haar-additive-argument) is therefore applicable at its accepted source interface.
Its input law is the singular-value law of |d|, and the two inequalities (Schur-bulk) place zero in the regular bulk for d+v.
The law of |d| cannot be a point mass under both strict inequalities, so its symmetrization has support at more than two points, as required by the local-law input.
The free target in the generic conditional lemma depends only on the limiting singular law of the deformation.
To identify it with the possibly nonnormal operator d appearing here, strong Haar convergence and the bounded rational approximations above already give almost-sure weak convergence of the singular measures of D_N+V_N to that of |d+v|.
The conditional lemma independently identifies the same limit by the symmetrized free convolution, so uniqueness of the weak limit identifies these two free singular laws.
Their integrable logarithmic spectral integrals therefore agree.
The resulting full logarithmic limit for D_N+V_N, together with the bounded-inverse logarithmic limits for B_N and C_N, proves the original affine limit through the exact identities above.
The regular bulk has positive singular density arbitrarily close to zero and finite logarithmic integral, so d+v has positive ordinary FK determinant and no bounded inverse.
The bounded factors B and c preserve positivity of the FK determinant through (Schur-FK).
The bounded rectangular inverse identity, (I+XY)^{-1}=I-X(I+YX)^{-1}Y when the inverse on the right exists and its converse with X and Y exchanged, shows that L is invertible exactly when d+v is invertible.
Hence L itself has no bounded inverse under the strict bulk conditions.

This supplies aggregate negative-logarithm control for the stated dense-background rank-one class.
It still requires a rank-one selected coefficient, two bounded inverse assumptions and a strict regular-bulk condition, so it does not settle the unrestricted coefficient contract.

For a concrete two-by-two example, choose
\[
 A_0=I_2,\qquad
 A_1=\begin{pmatrix}1/10&0\\-2/5&0\end{pmatrix},\qquad
 A_2=\begin{pmatrix}0&1\\0&1\end{pmatrix}=pq^*,
 \quad p=\binom{1}{1},\quad q=\binom{0}{1}.
\]
Then
\[
 B=\begin{pmatrix}1+u/10&0\\-2u/5&1\end{pmatrix},
 \qquad
 c=\frac{1+u/2}{1+u/10},\qquad
 d=\frac{1+u/10}{1+u/2}.
\]
Both inverse assumptions follow from the circle bounds |1+z/10|≥9/10 and |1+z/2|≥1/2.
The exact strict moments are \(\tau(d^*d)=1+16/75\) and \(\tau((d^{-1})^*d^{-1})=1+16/99\).
The free operator d+v has a positive finite ordinary FK determinant and no bounded inverse under the regular-bulk interface; bounded Schur elimination and the rectangular inverse identity transfer the absence of a bounded inverse to L.
The two random coefficient matrices have no common invariant line, since the invariant lines of A_1 are span((1/10,−2/5)) and span((0,1)), while those of A_2 are span((1,1)) and span((1,0)).
They also cannot simultaneously become single-entry matrices under a similarity: their nonzero traces would force both single entries onto the diagonal, which would make them commute, whereas these two matrices do not commute.
Thus the previously proved two-position, sparse fresh-edge and triangular coefficient classes do not directly cover this example.

The [proved coefficient-position symmetry](../claims/Yin_C_F0192_v1.md#coefficient-gauge) permits first moving a rank-one coefficient from any position to a fresh Haar position.
After that exact transformation, the present background, compression and strict-bulk assumptions must still be verified for the resulting ordered tuple.
The symmetry alone does not show that every tuple containing a rank-one coefficient meets those sufficient conditions.

### A nonempty amplitude interval for each nonconstant compression

The strict bulk conditions need not be found by isolated coefficient guesses.
Fix an invertible background \(B\) and an invertible compression \(c_0=(q^*\otimes1)B^{-1}(p\otimes1)\) whose modulus is not a scalar.
Scale only the selected rank-one coefficient by a nonzero scalar t.
Then c_t=tc_0 and d_t=t^{-1}c_0^{-1}.
The two bulk inequalities are precisely
\[
 \|c_0\|_2^{-1}<|t|<\|c_0^{-1}\|_2.
\]
The interval is nonempty because Cauchy--Schwarz gives \(\|c_0\|_2\|c_0^{-1}\|_2>1\) when \(|c_0|\) is not scalar.
Thus the mechanism supplies an open annulus of fresh-coefficient amplitudes for every such background and compression.
It leaves all background matrices fixed and does not introduce additional independent copies of the same input.


<a id="scalar-strict-triangle-proof"></a>
## Proof of the direct scalar corollary

The strict triangle inequalities force all three coefficients to be nonzero.
Set
\[
 D_N=\frac{a_0I_N+a_1U_N}{a_2},\qquad d=\frac{a_0+a_1u}{a_2}.
\]
The matrices D_N have a uniform norm bound and a singular empirical law converging almost surely to that of |d| under every allowed coupling.
Their conditional deformation is a polynomial in the background Haar U_N, and V_N remains full Haar after conditioning on that dimension alone.
The modulus law is nonconstant because a_0 and a_1 are nonzero.
The exact moments are
\[
 \tau(d^*d)=\frac{x_0+x_1}{x_2},\qquad
 \tau((d^{-1})^*d^{-1})=
 \begin{cases}
 x_2/|x_0-x_1|,&x_0\ne x_1,\\
 +\infty,&x_0=x_1.
 \end{cases}
\]
The inverse in this display is the measurable spectral inverse for the moment test, and no bounded inverse is assumed.
For unequal x_0 and x_1 the second identity follows by a geometric-series Fourier expansion after factoring the larger coefficient; for equal values the circle integral has a nonintegrable inverse-square singularity at its single root.
Thus (Scalar-triangle) is exactly the pair of strict squared-norm bulk inequalities.
The exceptional atom condition at zero is absent because a_0+a_1u has no positive-mass zero set on the circle.
The accepted bulk interface in [HZ25-U001](../audits/literature/HZ25/Yin_U001.md#subordination-neighborhood) therefore verifies the conditional Haar-additive hypotheses.
Its logarithmic limit applies to D_N+V_N.
Multiplication by a_2 adds the fixed constant log|a_2| to the normalized finite and free logarithms.
As in the nonnormal-target identification above, ordinary Haar *-moment convergence identifies the actual free singular law of d+v with the conditional lemma's convolution law.
The regular bulk gives a finite logarithmic integral and excludes a spectral gap at zero, so the actual free scalar pencil has positive FK determinant and no bounded inverse.
This proves the stated full almost-sure limit and hence both upper-limit assertions as well.

## Current assessment
[Selected decision](#decision-conditional-schur-reviewed)

## Assessment history

### Decision conditional-schur-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T08:04 |
| status | open |
| reason | The conditional Haar-additive local-law adaptation and exact original affine Schur application are fixed as a complete candidate for separate mathematical review; no unrestricted Haar Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conditional and affine statements](#statement) | Conditional Haar-additive full logarithmic limit, arbitrary-coupling rank-one affine application, its positive-FK/unbounded-inverse scope, amplitude interval, exact matrix example and direct scalar strict-triangle corollary. |
| argument | [Complete candidate argument](#argument) | Uniform guarded local law, free-convolution neighborhood, dyadic and ultra-small resolvent integrals, inverse guards, exact finite/free Schur reduction, original coefficient checks and direct scalar bulk verification. |
| dependency | [Accepted HZ25 source unit](../audits/literature/HZ25/Yin_U001.md#hz25-u001) | Only Definition 2.6/2.7, Propositions 2.1/2.2, Theorems 2.3/2.8/3.2 and Lemma 4.4 at the exact bounded Haar-additive and regular-bulk interfaces proved locally applicable above. |
| dependency | [Haar background convergence](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Only fixed-coefficient strong Haar convergence and its bounded-inverse polynomial approximation consequences for B_N and C_N. |
| dependency | [Bounded ordinary FK products](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Only bounded multiplicativity, including zero values, used in the rectangular determinant and Schur factorizations. |
| dependency | [Identity-diagonal triangular factors](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only Theorem 14.18 for unipotent bounded block factors with identity diagonal maps; all required dense-range and injectivity hypotheses hold. |
| dependency | [Coefficient-position symmetry](Yin_C_F0192_v1.md#coefficient-gauge) | Only the proved Haar transformation used for the optional initial coefficient permutation, without supplying the new Schur or bulk hypotheses. |

### Decision conditional-schur-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T08:25 |
| status | proved |
| reason | Independent review checked the complete restricted conditional theorem, original affine application, amplitude and matrix examples, and scalar strict-triangle corollary with the exact source and coupling interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conditional and affine assertions](#statement) | All displayed conditional Haar-additive, rank-one affine, amplitude/example and scalar strict-triangle conclusions, under their original background and bulk hypotheses. |
| argument | [Complete conditional and Schur proof](#argument) | Guarded uniform local laws, free-convolution neighborhood, dyadic and ultra-small integrals, bounded rational guards, finite/free Schur reduction and all stated examples. |
| dependency | [HZ25 source interface](../audits/literature/HZ25/Yin_U001.md#hz25-u001) | Only the accepted model, Definitions 2.6/2.7, Propositions 2.1/2.2, Theorems 2.3/2.8/3.2 and Lemma 4.4 at their inspected v4 scope and the actual applicability verified here. |
| dependency | [Strong Haar background convergence](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Fixed-coefficient strong convergence under the stated coupling quantifier and its bounded-inverse polynomial approximation consequences. |
| dependency | [Ordinary bounded FK products](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Bounded multiplicativity in finite tracial algebras, including zero determinant, for the displayed Schur and rectangular factors. |
| dependency | [Unipotent triangular factors](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only the identity-diagonal bounded triangular factors in Theorem 14.18, with their injectivity, dense range and trace normalization. |
| dependency | [Coefficient-position symmetry](Yin_C_F0192_v1.md#coefficient-gauge) | Only the proved transformation for the optional initial coefficient permutation; it grants no new inverse or bulk hypotheses. |
| review | [Independent complete restricted review](../audits/reviews/Yin_R_F0198_v1.md#independent-conditional-schur-proof) | Complete exact statement, argument, all declared dependencies, actual original coefficient applications and source-proof limits; no unrestricted Task completion. |

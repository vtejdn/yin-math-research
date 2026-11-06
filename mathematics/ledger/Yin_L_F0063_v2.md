---
author: Yin
---

# Cyclic three-factor counting and its unresolved entropy loss

This bounded strategy comparison for Yin on 2026-11-06 concerns the original real three-Wigner product at a fixed nonreal parameter within [F0012](../tasks/Yin_T_F0012_v3.md#contract).
It retains ordinary exploration by an assigned strategic agent and the responsible main agent's evaluation, not an independent mathematical review.
The [preceding comparison](Yin_L_F0063_v1.md) retains its different moment, smoothing and propagation tests without being copied here.
The new content is a global real-imaginary area calculation, its coordinate restriction obstruction, an independence-preserving three-rectangle exposure, and the entropy loss of its unrestricted product net.
No summable small-ball estimate, new accepted external input, or solution of the Task is asserted.

<a id="full-numerator-boundary"></a>
## The complete numerator remains the relevant target

The [fixed branch comparison](Yin_L_F0066_v7.md#accepted-branch-comparison) establishes that the accepted C_F0194_v5 argument already controls the low-matching and tiny-full-numerator intersection with arbitrary polynomial error.
The unresolved error in that assembly is its high-matching term.
The [complete conditional numerator](../drafts/Yin_D_F0011.md#joint-small-numerator-probe) retains the actual center, linear terms, quadratic coefficients and random normalization.
Its definition does not discard that information.
Conditioning the second and third factors into an arbitrary shift, or replacing the full numerator by a single cofactor's rectangular copy difference, can discard information needed by a proposed proof of the target.

The [reviewed normalized odd-odd theorem](../claims/Yin_C_F0194_v15.md#statement) supplies a coefficient-energy comparison, not an arithmetic concentration estimate.
The [full-numerator exclusion](Yin_L_F0066_v7.md#common-factor-full-numerator) already explains why the retained rare-background common-factor atom does not obstruct the required tiny-ratio event.
Neither another energy statement nor a refinement confined to that low-matching event addresses the remaining high-matching error.

<a id="cyclic-global-area"></a>
## The original cyclic equations force only a global two-dimensional area

Let \(A,B,C\) be real symmetric \(N\)-by-\(N\) matrices and fix \(z=a+ib\), where \(b\ne0\).
For the intended application they are the three independent normalized real Wigner inputs with fixed laws.
The first proposed arithmetic pilot uses bounded atomic off-diagonal laws, but the following calculation is deterministic.
Assume, for \(L\ge1\) and \(N\ge2\), that
\[
 \max\{\|A\|,\|B\|,\|C\|,\|B^{-1}\|,\|C^{-1}\|\}\le N^L.
 \tag{Cycle-polynomial-guards}
\]
These are hypotheses of this calculation, not a newly proved probability estimate.
For a unit complex vector \(v\), put
\[
 r=(ABC-zI)v,\qquad \epsilon=\|r\|,\qquad
 u=Cv,\qquad t=Bu.
\]
The exact equations are
\[
 Cv=u,\qquad Bu=t,\qquad At=zv+r.
 \tag{Cycle-equations}
\]
They preserve two independent matrix constraints that would be hidden after replacing \(B,C\) by a deterministic product-inverse shift.

The norm comparisons are
\[
 N^{-L}\le\|u\|\le N^L,\qquad
 N^{-2L}\le\|t\|\le N^{2L}.
\]
Indeed the lower bounds follow from \(v=C^{-1}u=C^{-1}B^{-1}t\), and the upper bounds follow from the two forward products.
The cyclic residual identities are
\[
 (ABC-zI)v=r,\qquad
 (CAB-zI)u=Cr,\qquad
 (BCA-zI)t=BCr.
 \tag{Cycle-propagated-residuals}
\]
All three real coefficient matrices have norm at most \(N^{3L}\).
After normalizing each vector separately, their residual norms are at most \(\epsilon\), \(N^{2L}\epsilon\), and \(N^{4L}\epsilon\), respectively.

For any normalized complex vector \(w\), define its global real-imaginary area by
\[
 \mathfrak a(w)=
 \sqrt{\|\operatorname{Re}w\|^2\|\operatorname{Im}w\|^2
       -\langle\operatorname{Re}w,\operatorname{Im}w\rangle^2}.
\]
Multiplication by a unit complex scalar rotates the two real columns and preserves this quantity.
Choose such a phase so that \(w=x+iy\), \(x\perp y\), and \(\|x\|\ge\|y\|\).
This is diagonalization of the real symmetric two-by-two Gram matrix by a rotation, followed if necessary by a quarter-turn.
In particular \(\|x\|\ge1/\sqrt2\).

If \(H\) is real, \(\|H\|\le N^{3L}\), and \((H-zI)w=e\), taking imaginary parts gives
\[
 (H-aI)y-bx=\operatorname{Im}e.
\]
Consequently,
\[
 |b|\,\|x\|\le (N^{3L}+|a|)\|y\|+\|e\|.
\]
When \(\|e\|\le |b|/(2\sqrt2)\), this yields
\[
 \mathfrak a(w)=\|x\|\|y\|
 \ge \frac{|b|}{4(N^{3L}+|a|)}
 \ge c_zN^{-3L},
 \qquad c_z=\frac{|b|}{4(1+|a|)}.
 \tag{Cycle-global-area-bound}
\]
Thus, if
\[
 \epsilon\le \frac{|b|}{2\sqrt2}N^{-4L},
\]
the same bound holds for \(v,u/\|u\|\), and \(t/\|t\|\).
No symmetry of the three cyclic products is used; their reality and the displayed norm and residual bounds suffice.
This conclusion gives neither a least common denominator bound nor an area bound on the coordinate sets needed for independent row exposure.

<a id="coordinate-area-obstruction"></a>
## Global area can disappear after one coordinate is removed

Let
\[
 e=N^{-1/2}(1,\ldots,1)^T,\qquad
 \eta=N^{-q},\quad q\ge1,\qquad
 w=\frac{e+i\eta e_1}{\sqrt{1+\eta^2}},
\]
where \(e_1\) is the first standard coordinate vector.
Then \(\|w\|=1\), all coordinate magnitudes are \(O(N^{-1/2})\), and
\[
 \mathfrak a(w)
 =\frac{\eta\sqrt{1-1/N}}{1+\eta^2}.
 \tag{Cycle-concentrated-imaginary-area}
\]
The formula follows by substituting
\[
 \|e\|=1,\qquad \|\eta e_1\|=\eta,\qquad
 \langle e,\eta e_1\rangle=\eta/\sqrt N
\]
in the Gram determinant.
The area is therefore of polynomial order, and the real part is spread over all coordinates.
After deleting coordinate \(1\), however, the restricted vector is real and its real-imaginary area is zero.
Multiplying it by any common phase does not change that rank-one conclusion.

This example rules out passage from global area and coordinate flatness alone to area on every large retained set, including a set of small coordinates obtained by discarding the largest coordinates.
It is not asserted to be a near-kernel vector of the random product, an actual cofactor realization, or a counterexample to F0012.
A probabilistic statement excluding such restricted degeneracy for the original cyclic vectors would still need proof.

<a id="three-rectangle-exposure"></a>
## Three independent rectangles and their precise conditional equations

Fix deterministic coordinate sets \(J_A,J_B,J_C\subset[N]\) of size \(k=\lfloor\delta N\rfloor\), where \(0<\delta\le1/2\).
In each original matrix, retain its crossing block
\[
 X_A=A_{J_A^c,J_A},\qquad
 X_B=B_{J_B^c,J_B},\qquad
 X_C=C_{J_C^c,J_C}.
 \tag{Cycle-three-rectangles}
\]
Condition on all other independent upper-triangular coordinates, including the diagonals.
A crossing entry's reflected location is the same random variable, not an additional coordinate to be conditioned on.
Each retained block has independent original off-diagonal entries, and the three blocks are mutually independent.
The blocks have size \((N-k)\)-by-\(k\), so this exposure need not be confined to three half-by-half blocks.

For a fixed deterministic candidate triple \((v,u,t)\), the rows of (Cycle-equations) outside the selected column sets become
\[
 \begin{aligned}
 X_Cv_{J_C}
   &=u_{J_C^c}-C_{J_C^c,J_C^c}v_{J_C^c},\\
 X_Bu_{J_B}
   &=t_{J_B^c}-B_{J_B^c,J_B^c}u_{J_B^c},\\
 X_At_{J_A}
   &=zv_{J_A^c}+r_{J_A^c}
           -A_{J_A^c,J_A^c}t_{J_A^c}.
 \end{aligned}
 \tag{Cycle-conditional-row-equations}
\]
For a residual bound, the last equation is used as a small neighborhood of the displayed center with the residual term omitted.
The first two centers, and that last center without the residual, are measurable in the conditioned coordinates and the fixed candidate.
Within each line the \(N-k\) row sums are independent, and the three lines use independent factors.
The coefficient vectors are respectively \(v_{J_C},u_{J_B},t_{J_A}\), not three independent random vectors furnished for free by the equations.

A deterministic net may be organized separately for each choice of the three coordinate sets, paying at most
\[
 \binom Nk^3=\exp(O_\delta(N))
\]
choices.
Selecting sets from a fixed deterministic candidate before taking this union is legitimate.
Selecting them from an unknown random near-kernel vector and then conditioning on that selection does not preserve the preceding conditional law without a further argument.

<a id="free-net-entropy-loss"></a>
## The unrestricted three-vector net still loses at every fixed rectangle proportion

Here is an optimistic calculation that isolates the problem before any arithmetic theorem is invoked.
Let \(\gamma\in(0,1)\) be a common approximation scale after suppressing polynomial norm and normalization losses.
Suppose every retained complex row equation had the favorable fixed-vector small-ball factor \(C\gamma^2\).
Even under this stronger provisional input, the standard unrestricted product covering bound for three complex vectors is
\[
 |\mathcal N_\gamma|\le(C/\gamma)^{6N}.
\]
Allowing normalized spheres instead changes only a bounded number of powers; covering their permitted scalar norms adds no improvement to the leading dimension.
For the displayed covering bound, the union-bound expression has exactly the scale dependence
\[
 (C/\gamma)^{6N}(C\gamma^2)^{3(N-k)}
 =C^{O(N)}\gamma^{-6k}.
 \tag{Cycle-free-net-loss}
\]
For \(k=N/2\) this is \(C^{O(N)}\gamma^{-3N}\).
For \(k=\lfloor\delta N\rfloor\), it is \(C^{O(N)}\gamma^{-6\delta N+O(1)}\).
At \(\gamma=N^{-T}\), every fixed positive \(\delta\) therefore leaves a positive loss \(6\delta T N\log N+O(N+\log N)\) in the logarithm of that bound.
The choice of coordinate sets adds only order \(N\) to this logarithm.
The actual polynomial norm factors, restricted-area losses and atomic small-ball remainder have not been shown to improve this optimistic balance.

This calculation proves that the stated free-net estimates do not deliver a decaying union bound.
It is not a lower bound on all possible covering numbers, a lower bound on the true bad-event probability, or an impossibility theorem for cyclic counting.
Reducing \(\delta\) with \(N\) changes the available coefficient supports and their small-ball estimates and requires a new calculation; the fixed-proportion statement does not exclude it.
A successful argument needs a justified arithmetic covering gain or another source of constraints, not merely the observation that complex row sums have two real coordinates.

<a id="cyclic-elimination-boundary"></a>
## Two apparent eliminations do not provide that covering gain

The exact identities \(u=Cv\) and \(t=BCv\) formally parameterize the triple by \(v\).
If the three rectangles remain unexposed, however, the resulting images and their approximating net depend on \(X_B,X_C\).
The preceding fixed-candidate multiplication of the three row probabilities no longer applies to that random net.
Conditioning on all of \(B,C\) makes this parameterization fixed, but then their two row families are no longer fresh randomness available in the same product estimate.
This rejects that automatic use of a single-vector net, not every possible adaptive or conditional construction.

A second proposal is to solve for the complementary coordinates using a conditioned cyclic block.
Even when the same coordinate partition is used in the three factors, the complementary equations involve the shifted product of the three principal blocks, with crossing-block contributions on their right-hand sides.
A polynomial bound for the inverse of that nonzero-parameter shifted product is not supplied by the separate unshifted inverses of \(B,C\).
Using such a bound without proof reintroduces the same kind of product least-value obligation on a smaller block.
Without a justified inverse bound or a suitable singular-block alternative, this elimination provides no controlled approximation scale.
Its crossing-block-dependent right-hand sides also require an explicit independence argument.
No such conditional net organization was established in this exploration.

<a id="source-inspection-boundary"></a>
## Bounded primary-source comparison

The 2026-11-06 search asked whether cyclic product linearization and real-imaginary correlation could supply the missing arithmetic counting gain.
Queries used products of symmetric random matrices, cyclic linearization, nonreal spectral parameters, and real-imaginary small-ball correlation.
The inspected sources were:

- Rudelson--Vershynin, [arXiv:1506.04012v1](https://arxiv.org/html/1506.04012v1), canonical key RV16.
  Actual HTML reading covered Assumptions 1.1/1.4, Section 2.2.3, Theorems 7.5, 10.3, 11.2, 12.1, and the combination in Section 12.1.1.
  These passages pair arithmetic and correlation information with covering entropy.
  Theorem 10.3 retains an inverse-square-root dimension remainder; for \(n=(1-\varepsilon)N\), Theorem 12.1 treats the LCD threshold \(\min\{\sqrt N e^{c/\sqrt\varepsilon},\varepsilon N\}\) on its bounded-norm event.
  The cyclic sparse block matrix does not satisfy the stated whole-matrix independence/nondegeneracy assumptions.
  The [version-specific PDF](https://arxiv.org/pdf/1506.04012v1) and attempted [author-hosted PDF](https://www.math.uci.edu/~rvershyn/papers/no-gaps-delocalization.pdf) were inaccessible through the reading interface; the actual mathematical reading was HTML.
- Kopel--O'Rourke--Vu, [arXiv:1802.03004v3](https://arxiv.org/abs/1802.03004v3), canonical key KOV18.
  Only title, authors, version metadata and abstract were read.
  Its stated product linearization input has iid subgaussian entries and does not supply the present Wigner-factor estimate.

These are applicability comparisons, not adopted proof dependencies or whole-proof reviews.
The search stopped at those boundaries; it establishes neither theorem absence nor novelty.

<a id="conditional-restart-test"></a>
## Allocation consequence and a conditional restart test

No sufficiently supported replacement of the existing full-numerator high-matching route emerged from this comparison.
The cyclic viewpoint is retained only as a conditional restart lead.
The deterministic global-area calculation alone does not justify allocating another sequence of energy or area refinements.

A meaningful restart would specify an arithmetic level set for the actual restricted coefficient matrices
\[
 \begin{pmatrix}
  (\operatorname{Re}v_{J_C})^T\\
  (\operatorname{Im}v_{J_C})^T
 \end{pmatrix},\quad
 \begin{pmatrix}
  (\operatorname{Re}u_{J_B})^T\\
  (\operatorname{Im}u_{J_B})^T
 \end{pmatrix},\quad
 \begin{pmatrix}
  (\operatorname{Re}t_{J_A})^T\\
  (\operatorname{Im}t_{J_A})^T
 \end{pmatrix},
\]
a compatible covering bound, and an independence-preserving conditioning scheme.
It would then compare the actual net cardinality with the three conditional row probabilities at one fixed polynomial scale, including small-ball remainders, component norm ratios, coordinate selection and mixed arithmetic levels.
The scalar arithmetic denominator of a real-imaginary concatenation is not automatically the two-dimensional coefficient-matrix denominator used by a row small-ball estimate.
No compatible transfer or net bound is supplied here.

A negative leading \(N\log N\) balance obtained without a net depending on the retained rectangles or an unproved shifted cyclic inverse would be evidence for further development.
If the only bound remains (Cycle-free-net-loss), the proposed organization has not improved the existing arithmetic target.
Even a successful counting test would still leave the final boundary or distance conversion, summable probability estimate and original-model normalization to prove.
A complete three-real-factor estimate at fixed nonreal parameters would improve that pilot; it would not automatically handle general complex laws, repeated-variable polynomials or the full planar F0012 contract.

---
author: Yin
---

# Independent review: angular density and the normal polynomial core

Date/reviewer: 2026-09-11, the reviewing agent.

Target: [angular-density continuation](../../claims/Yin_C_F0048_v1.md).


**Outcome: pass.**
All sections of the frozen proof were read and independently checked.
No mathematical correction was requested.
No Claim ID or Role is assigned here.

Before the draft froze, root proposed the transfer mechanism.
The reviewer supplied rotation and graph-approximation prechecks, suggested the positive modification away from the support, and independently found the same Bernstein approximation source.
These contributions are disclosed; this audit does not describe the review as having occurred without prior collaboration.

## 1. Source and dependency scope

The proof uses the reviewed [Yin_C_F0047 radial criterion](../../claims/Yin_C_F0047_v1.md#yin_c_f0047), [Yin_C_F0025](../../claims/Yin_C_F0025_v1.md#yin_c_f0025), and the conditional free-product transfer [Yin_C_F0045](../../claims/Yin_C_F0045_v1.md#yin_c_f0045).

The reviewer independently retrieved the [Veretennikov--Veretennikova primary PDF](https://arxiv.org/pdf/1507.05235) and read Theorems 3 and 4(1), printed pp.6--7.
Their cube approximation applies to a globally C1 function on R2, approximating its values and first partial derivatives uniformly.
Affine rescaling of a square and separate treatment of real and imaginary parts give precisely the candidate's use of equation (17).
The delivered PDF has 19 pages, a v2 margin dated 2016-10-16 and a title-page date 2018-10-15.
This is acceptance of the selected statements; the higher-order proof and entire paper were not audited.

The companion [VV16 source audit](../literature/VV16/Yin_U001.md), was read in full.
Its institutional accepted-version locator and rectangle interface match the selected theorem.
The reviewer's separate White Rose PDF fetch timed out; the independent statement check above used the successfully retrieved arXiv PDF.
No full proof audit is inferred from either retrieval.

## 2. Forward transfer and the new vacuum vector

The lower and upper bounds on b give equivalent null sets and hence equal essential sup norms.
The upper bound gives \(\|f\|_\mu\le\sqrt B\|f\|_\nu\).
They do not identify Hilbert adjoints.

Yin_C_F0047 supplies both radial domains for bounded functions.
The polynomial commutator is a bounded integral operator.
Original polynomial graph approximants therefore prove domain invariance and the identity
\[
 E_\nu(pb)-pE_\nu b=K_{\nu,p}b=e_{\mu,0}p.
\]
This requires no derivative of a merely measurable b.
Both b and pb already belong to the original radial domain.
The two terms have the claimed estimate \(a_\mu=2B^{3/2}a_\nu\).

The actual vacuum vector must be established separately from that estimate.
Since b belongs to the actual radial adjoint domain, testing the last identity yields
\[
 \xi_\mu=E_\nu^*b-JE_\nu b=b\xi_\nu-2JE_\nu b.
\]
The reality of b and the inner product convention give these conjugations and signs.
Both terms belong to L2(mu).
Bound (13) follows from norm comparison.
Vacuum membership is not inferred from the infinity-to-2 bound.

The bounded-function extension of the radial adjoint identity is valid.
Uniformly bounded polynomial approximants converge in L2.
Their products with the fixed L2 vacuum vector converge in L2, by first truncating that vector to a bounded one.
Weak graph limits of both operators then give the displayed identity.

## 3. The inverse-density test is in the actual graph

The smooth positive kappa agrees with the identity on [m,B].
Composing it with the real C1 representative removes possible zero or negative values away from the spectral support while preserving the density almost everywhere.

For chi compactly supported away from radius zero, both phi and psi=phi/beta_+ are globally C1 and compactly supported.
The density derivatives can grow towards zero without affecting these tests.
Tensor-product Bernstein approximation on a containing square gives value and differential convergence.
Convexity of the square yields
\[
 \|\delta(p_n-\psi)\|_\infty
 \le\|d(p_n-\psi)\|_\infty\longrightarrow0.
\]
Thus the canonical integral images converge uniformly.
This proves psi belongs to the graph closure of the original core before any conclusion about the unknown mu infinity-to-2 estimate is used.
The real-coordinate polynomials are starred polynomials in z, so the original core is preserved.

## 4. Rotation, radial atoms and the reverse constant

After multiplication by the two densities, the kernel for the vacuum test is
\[
 \frac{\phi(z)b(w)-\phi(w)b(z)}{z-w}.
\]
It is a combined bounded divided-difference kernel.
Under simultaneous rotation, the phase of phi cancels the denominator phase.
The angular means of b then give the radial functional.
The uniform integrable majorant is \(B^2\operatorname{Lip}(\psi)\).
This proves the averaging step without separating singular Cauchy terms.

Input frequency one yields \(2\int A\chi\,d\sigma\), including the same-radius atom \(a(r)\chi(r)/r\).
No radial L2 assumption is used before this computation, because chi/r is bounded.
The original adjoint pairing gives
\[
 2\left|\int A\chi\,d\sigma\right|
 \le m^{-1/2}\|\xi_\mu\|_\mu\|\chi\|_\sigma.
\]
Density of the smooth annular tests, including for atomic radius laws, identifies the locally bounded A as an L2 function and proves \(\|A\|_\sigma\le\|\xi_\mu\|_\mu/(2\sqrt m)\).
Substitution into the forward bound gives exactly the constant in equation (6):
\[
 \frac{2c_{\rm rad}B^{3/2}}{\sqrt m}.
\]
No graph approximation to an untruncated 1/b is required.

## 5. Original domains and the nonradial example

For either measure, the vacuum vector and the symmetric bounded polynomial kernel give the actual identity \(e_0^*p=p\xi-Je_0Jp\).
This proves closability and the adjoint bound.
Bounded polynomial approximation and weak closedness of the original graphs then give both bounded-function domains.
For a marginal of a larger tuple, the full vacuum vector remains in the original adjoint formula.
Yin_C_F0045 supplies all-M domains only under its freeness hypothesis.

Both measures are nonatomic, despite atoms in the radius law.
The starred-generator phase kernel therefore still has Hilbert--Schmidt norm one.
This checks the exact Yin_C_F0025 compactness condition.

The example \(b=1+\varepsilon\cos\theta\), with nonzero real \(|\varepsilon|<1\), has the required C1 representative off zero and the same disk masses as the radial example.
The disk compression of a hypothetically bounded dual gives the same contradiction.
Hence the example is nonradial and has an actually unbounded Hilbert dual with the stated domains.

The necessity assertion retains the C1 hypothesis.
Sufficiency permits merely measurable densities satisfying the displayed bounded comparison.
No unrestricted normal-measure theorem, correlated-tuple all-M statement, or bounded rational reconstruction has been proved.

## Actual review arrangement

The reviewer supplied rotation and graph-approximation prechecks and the positive modification away from support before freezing, alongside the disclosed root transfer proposal. This is substantive target development context; the complete later fixed-artifact check remains self-reviewed. Its independent primary Bernstein statement check retains that narrower source depth.
The original 2026-09-11 date, full mathematical findings, source depths and exact boundaries remain unchanged.
This maintenance performs no new mathematical review or context-isolation certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#5-original-domains-and-the-nonradial-example) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#5-original-domains-and-the-nonradial-example) | [C_F0048 statement](../../claims/Yin_C_F0048_v1.md#statement) | Whole seven-section angular-density theorem: measurable bounded positive sufficiency, actual changed-measure vacuum and adjoints, C1-only necessity via inverse-density graph tests and rotation, exact constants, original domains and nonradial unbounded-dual example. No unrestricted angular law or correlated tuple conclusion. |
| [Original finding](#5-original-domains-and-the-nonradial-example) | [C_F0048 argument](../../claims/Yin_C_F0048_v1.md#3-transfer-from-a-radial-core-without-differentiating-the-density) | Whole seven-section angular-density theorem: measurable bounded positive sufficiency, actual changed-measure vacuum and adjoints, C1-only necessity via inverse-density graph tests and rotation, exact constants, original domains and nonradial unbounded-dual example. No unrestricted angular law or correlated tuple conclusion. |

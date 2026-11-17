---
author: Yin
---

# Winding obstructions and static observations for dissipative Wigner linearizations

An agent acting for Yin independently reviewed the two fixed working-tree Claims and their direct mathematical interfaces at 2026-11-17T06:25 UTC.
The reviewer took no part in their development and received the objects and review scope without proof-development dialogue, exploration notes, author explanations or prior findings on either Claim.
The earlier [iterated-observation review](Yin_R_F0190_v34.md#observability-whole-proof) concerned a different theorem.
The two findings below use the prior mathematical results at the indicated interfaces.

<a id="winding"></a>
## Winding and the canonical even lift

The [quadratic test](../../claims/Yin_C_F0349_v1.md#statement) excludes all positive multiplicities for a complex determinant identity and exactly the asserted odd multiplicities for its modulus obstruction.
Direct multiplication gives \(AB+2BA=tI+s\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).
At the center \((\alpha,\beta)\), the two shifted eigenvalue factors have values \(0,-2i\beta\).
On the radius-\(\rho\) circle they are \(\rho e^{i\theta}\) and \(-2i\beta+\rho e^{-i\theta}\).
Their product winds once for \(0<\rho<|\beta|\).
A nonzero disk factor or its reciprocal has boundary winding zero.
The dissipative determinant also has winding zero since interpolation to \(iI\) is strictly dissipative at every positive interpolation time and the starting loop is invertible.
A scalar rotation multiplies the determinant by a fixed nonzero constant.

For the modulus identity the leading Taylor degree \(k\) exists since the polynomial determinant is nonzero off the center.
Along a direction on which that term survives, the strictly positive limit of the modulus divided by \(\rho^r\) forces \(k=r\).
The same radial limit on every direction makes the leading form nonvanishing on the unit circle.
Uniform convergence there identifies its winding with that of the full determinant on a sufficiently small circle.
When \(r\) is odd, a continuous phase lift on the real line changes over a half-turn by a continuous odd multiple of \(\pi\), hence by a constant odd multiple.
This gives odd winding over a full turn, as required.

Elimination at \(iI\) in the canonical doubled matrix gives \(iA^*A\) as its Schur complement.
The raw rows and the rows \(J,JH\) generate the diagonal row module with generators \((I,0),(0,A)\), and every higher observation lies in it by multiplication of the even and odd powers.
Adjoining the invertible \(T\) adds a full identity row module since \(T^{-1}\) is polynomial.
Congruence multiplies this raw module on the right by \(S\), with the independent left transformation on the \(H\)-rows polynomially reversible.
This also proves the asserted iterated stabilization by adjoining identity blocks to the preceding right multiplier.
Each positive-degree transformed observation is a left multiple of the transformed Hermitian block, giving the claimed inclusion even when equality of observation modules after congruence is unavailable.

Writing total logarithms with the physical denominator \(N\) makes the product of \(M,\operatorname{diag}(I,A,I),S\) additive at finite size and under bounded FK multiplicativity.
A finite free total for the product gives finite totals for all factors because each is bounded at the free tuple.
At finite size singular events for any factor are contained in the singular event of the product.
For a deficit \(\eta\) of \(A\), either another factor overshoots its target by more than \(\eta/4\) or the product falls at least \(\eta/2\) short.
Regularized upper bounds imply that each such overshoot has probability tending to zero, and convergence of the product handles the deficit.
This proves the conditional subsequence conclusion for the canonical lift and its stated stabilizations.
It gives no decision on the random quadratic determinant at a nonreal shift.

<a id="static-observation"></a>
## Static observation, Gram equivalence and the affine lift

The [three-way equivalence](../../claims/Yin_C_F0350_v1.md#statement), the exact affine construction and the stated scalar applications hold.
On the invertible event for \(B=MH+KJ\), the common kernel of \(H,J\) is zero, and the imaginary quadratic form places \(\ker L\) in that common kernel.
With \(Z=L^{-1}\), the resolvent identity gives \((JZ)^*(JZ)=-\operatorname{Im}Z\).
On the top \(j\) right singular directions of \(JZ\), the numerical range bound for \(Z\) gives \(s_j(JZ)^2\le s_j(Z)\).
Using \(Z=B^{-1}(M+(K-iMJ^*)JZ)\), exterior-power product and sum bounds therefore leave one half of \(F_l(Z)\) on the left.
All polynomial terms, including rectangular ones, have the requisite positive logarithmic tail, and the finite-target hypothesis supplies the same tail for \(B^{-1}\).
The inverse-tail criterion gives convergence and a finite target for \(L\) on the same subsequence.

Conversely, for \(S=(H,J)^{\mathsf T}\) denoting vertical block stacking, \(Z[I,iJ^*]S=I\).
Projection of this left inverse onto the range on its input side gives \(S^+\).
Since \(G^{-1}=S^+(S^+)^*\), its decreasing positive inverse-log sums are bounded by twice the corresponding sums for \(Z\) and \([I,iJ^*]\) together.
The inverse-tail criterion gives the Gram assertion, and \(M=H,\ K=J^*\) gives its square witness.
The fixed-polynomial upper bound applies under every allowed coupling on the full sequence.
A deterministic subsequence with summable marginal lower deviations yields the matching lower bound by first Borel--Cantelli.

The pivot \(iI_r\) gives \(H+iJ^*J\) with the positive sign, and the lifted raw witness cancels its off-diagonal \(MJ^*\) to leave \(\operatorname{diag}(B,I_r)\).
For an entry indexed by a word the upper-unitriangular chain joins the first and last letters through the intervening letters in their original order.
Writing \(D^{-1}=\left(\begin{smallmatrix}0&T^{-1}\\(T^*)^{-1}&0\end{smallmatrix}\right)\) gives \(CD^{-1}C^*=(UT^{-1}V+(UT^{-1}V)^*)/2\).
The corresponding Hermitian Schur complement equals \(F_b\).
The lower unitriangular congruence fixes \(J_0\), and direct multiplication by the stated \(M_0,K_0\) gives \((M_0F+K_0J_0)T_0=\operatorname{diag}(B,I_r,I)\).
The flip in \(D\), the unit triangular factors and the \(iI_r\) pivot have determinant modulus and normalized FK determinant one.
This proves the finite identities for all Hermitian evaluations and the free identities including zero determinants.
Both free logarithms use the auxiliary size times the normalized trace logarithm, matching \(1/N\) times the finite log modulus.
The degree-at-most-one case omits the word chains.

For each fixed real \(z\), \(H-z\) is selfadjoint and \(-R(H-z)-zR+RH+b=b\).
The scalar theorem covers each nonzero affine \(b\), including a nonzero constant, through all even dimensions.
Neither this cancellation nor the probability argument requires disjoint inputs in \(H,R,b\).
At zero only \(RH+b\) is needed.
Evaluation at \(x=1,y=-1\) kills that row and each of its right powers of \(H\), while the static combination still evaluates to one.
The all-real-shifts application is pointwise in the shift, and the one-row conclusion is at zero.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Winding and doubling](#winding) | independently reviewed |
| [Static observation](#static-observation) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Winding and doubling](#winding) | [Claim](../../claims/Yin_C_F0349_v1.md#statement) | Exact nonreal parameter, regular factors, neighborhood and multiplicities. |
| [Winding and doubling](#winding) | [Argument](../../claims/Yin_C_F0349_v1.md#argument) | Complex winding, analytic leading form and antipodal parity. |
| [Winding and doubling](#winding) | [Even lift](../../claims/Yin_C_F0349_v1.md#even-doubling) | Canonical observation and raw modules, stabilization, congruences and probability implication. |
| [Winding and doubling](#winding) | [Bounded determinant](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) | Multiplicativity for bounded square factors in the finite tracial algebra. |
| [Winding and doubling](#winding) | [Upper bound](../../ledger/Yin_L_F0061_v2.md#upper-limit) | One-sided overshoot control for each fixed polynomial factor. |
| [Static observation](#static-observation) | [Claim](../../claims/Yin_C_F0350_v1.md#statement) | All three assertions on one fixed subsequence, finite targets and the coupling conclusion. |
| [Static observation](#static-observation) | [Argument](../../claims/Yin_C_F0350_v1.md#argument) | Inverse tails, pseudoinverse and Gram identities, and the passage to upper limits. |
| [Static observation](#static-observation) | [Affine lift](../../claims/Yin_C_F0350_v1.md#affine-lift) | Word order, Hermitian congruence, witness identities and both determinant normalizations. |
| [Static observation](#static-observation) | [Scalar application](../../claims/Yin_C_F0350_v1.md#real-axis-application) | Each fixed real shift with two rows, single row at zero, and separation from iterated rows. |
| [Static observation](#static-observation) | [Input laws](../../tasks/Yin_T_F0013_v1.md#input-model) | Fixed finite-second-moment Hermitian inputs and arbitrary cross-size couplings. |
| [Static observation](#static-observation) | [Tail lemma](../../claims/Yin_C_F0186_v34.md#logarithmic-tails-of-products) | Both directions for fixed square evaluations and high-probability invertibility. |
| [Static observation](#static-observation) | [Positive tails](../../claims/Yin_C_F0186_v4.md#positive-tail) | Fixed-degree polynomial blocks with fixed auxiliary dimensions. |
| [Static observation](#static-observation) | [Product and sum bounds](../../claims/Yin_C_F0186_v35.md#argument) | Rectangular exterior-power bounds and the square-root observation inequality. |
| [Static observation](#static-observation) | [Earlier observation](../../claims/Yin_C_F0186_v35.md#statement) | Inclusion of every finite iterated-row witness in the static row module. |
| [Static observation](#static-observation) | [Coupling criterion](../../claims/Yin_C_F0190_v1.md#coupling-criterion) | Deterministic subsequence with summable marginal failure probabilities. |
| [Static observation](#static-observation) | [Upper bound](../../ledger/Yin_L_F0061_v2.md#upper-limit) | Full-sequence almost-sure upper bound for each fixed polynomial. |
| [Static observation](#static-observation) | [Word chains](../../ledger/Yin_L_F0058_v2.md#exact-linearization) | Unit upper triangular elimination of each fixed matrix entry monomial. |
| [Static observation](#static-observation) | [Free trace weights](../../claims/Yin_C_F0186_v3.md#linearization-transfer) | Unit triangular factors and block-sum normalization including singular targets. |
| [Static observation](#static-observation) | [Scalar affine theorem](../../claims/Yin_C_F0186_v11.md#scalar-affine-statement) | Finite-target probability convergence through even dimensions for every nonzero scalar affine witness. |

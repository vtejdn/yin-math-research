---
author: Yin
---

# Review of measurable location and scale for a free selfadjoint noise

## Finding

At 2026-11-14T14:29 UTC a reviewer for Yin independently checked the entire [C_F0277 v1 candidate](../../claims/Yin_C_F0277_v1.md#decision-candidate) dated 2026-11-14T14:24.
The reviewer received the fixed argument and requested scope without development discussion, exploration notes, author explanations or a prior verdict on this candidate.
The three conditions are equivalent on the represented starred core, with the stated original graph domains, exact vacuum formula and disk thresholds.
The eight fixed inputs were checked at the interfaces bound below.

With \(e_n=1_{\{b\le n\}}\), the identity \((be_n)(T-k)(be_n)=e_nve_n\) recovers \(v\) by bounded strong convergence and identifies the intrinsic algebra with the free product.
Under actuality the normal starred-generator rule makes the \(T\)-derivation zero on base polynomials and makes the \(Z\)-derivation their scalar divided difference.
Freeness gives \(\|J_{v-\tau(v)}(ah\otimes hd)\|_2=\|v-\tau(v)\|_2\|ah\|_2\|hd\|_2\).
Subtracting the conditional expectation of \(aTd\) leaves precisely this vector.
Both sides of the vacuum pairing pass to bounded marginal approximants in \(L^2\).
Taking \(d=1\) and \(a=b^2e_n\) bounds \(\int b^2 e_n\) by a fixed multiple of its own square root, so monotone convergence forces the full inverse scale into \(L^2\).

For a finite insertion \(x\otimes y\), traciality makes the double trace of the inserted derivative at \(p\) equal to the double trace of the uninserted derivative at \(xpy\).
The latter is the scalar-noise pairing because cuts of reduced words with another centered factor have a centered segment on one trace leg.
Thus the vacuum is \(x^* s_\sigma y^*\), which gives the conjugation of both arguments in (3).
In a reduced word \(qfa\), earlier cuts have zero right trace, and the last cut places \(x\) after \(e_\sigma f\) and contributes \(\tau(ay)\).
The centered part of \(e_\sigma\) is bounded by \(a_\sigma\) and kills constants, so the centered column estimate of C_F0268 applies with this same terminal map.
Its scalar part is precisely the pairing with a centered \(s_\sigma\), as required by the two projected terms in that proof.
The bounds \(2\sqrt{4/\pi}\,a_\sigma\) and \(2\|s_\sigma\|_2\) therefore hold independently of the number of tensor summands or column entries.
Finite bounded tensors are dense in the Hilbert tensor space, and each fixed word evaluates by finitely many bounded outer actions, giving (3) even for \(b\otimes b\).

The scalar right and left weights give \(e_R f=e_0(fv)-f\) and \(e_L f=ve_0f\).
Exchange of the two scalar integration variables makes their vacua coincide at \(H=vg-1\).
Testing the scalar divided difference on adjoints, \(1\), and \(v\) gives \(g=g^*\), \(\tau(g)=0\) and \(\tau(vg)=1\).
Linear dependence would imply \((v-\lambda)g=1\) for real \(\lambda\).
Testing \((v-\lambda)^3\) would then force \(\tau((v-\lambda)^2)+\tau(v-\lambda)^2=0\), impossible for diffuse \(v\).
In the semicircular case \(g=v\) has degree one and \(H=v^2-1\) has degree two.

The insertion \(b\otimes b\) differentiates \(T\) to \(1\otimes1\), with vacuum \(J_g(b\otimes b)\).
On the one-generator subcore its values are the scalar divided differences at \(T\), and projecting the vacuum gives the actual scalar adjoint there.
Consequently \(T\) is diffuse already under \(b\in L^2\), before the liberation recovery at \(Z\).
In (4), multiplying the three inserted derivatives of \(v\) by \(h\) on the two outer legs cancels \(\gamma^0(k+hvh)\), including the unequal placements of \(v\) on the two noise terms.
The resulting liberation kills \(T\), and the vacuum of the free inner difference is zero by the centered-word trace.
The joint left-right action on \(a s d\) is multiplication at the first and last base coordinates.
Both one-noise ranges are perpendicular to the marginal, and their inner products give the joint density \(\|K H+L g\|_2^2\).
The positive least and finite largest Gram eigenvalues give exactly the integrability in (1).
The marginal and liberation recovery theorem applies to both diffuse marginals on the represented core and gives the orthogonal squared norm in (2).

For the column estimate write \(a=h(w)/h(z)>0\).
The two corrections \(a-1\) and \(1-a^{-1}\) have the same sign, so the absolute value of each is bounded by \(|K|\).
Since \(|t_r|\le1/|z-w|\) off the diagonal, all three regularized terminal symbols are uniformly square integrable under (1).
The free reference estimate in C_F0265 uses free normal factors with actual scalar vacua for its \(Z\)-column bound and the soft multiplier estimate for the factor three.
Both \(Z\) and the free selfadjoint \(v\) satisfy these requirements.
Bounded strong-star polynomial approximation of \(h,k\) controls their inner differences and every finite product with \(v\), including adjoints, in the \(\gamma^0\) graph.
For a target unit column the approximating column squares converge boundedly strongly to a positive contraction.
The smooth column cutoff equals one around its spectrum, so its outer divided difference vanishes on the limiting spectral square.
Uniform \(C^1\) polynomial approximation controls this divided difference on the larger common compact interval, giving graph approximants with column norm limsup at most \(1+\varepsilon\).
Fixed \(I_{t_r}\) is bounded, allowing the transfer before either the norm allowance or the spectral cutoff is removed.
Coarse inner spectral measures give no mass to the diffuse diagonal, so \(I_{t_ru}\) converges strongly to the identity there.

Conjugating the spectral base preserves (1), giving the right estimate for the adjoint tuple.
Flip-adjoint conjugation on a single starred input then gives the left estimate for the original tuple.
The two-contraction theorem puts every \(a\Omega\), \(a\in M\), in both the actual closure domain of each original right slice \(E_i\) and its Hilbert adjoint domain.
For graph approximants \(p_n\) to \(a\Omega\), the identity \(E_i(X_jp_n)=X_jE_i p_n+\delta_{ij}\tau(p_n)\Omega\) passes to the closed graph.
This gives the required generator-first commutator for \(-\overline E_i\) on all bounded vectors.
Conversely the supplied strong duals have the vacuum in their adjoint domains and satisfy the generator commutators there, giving actual starred derivations by C_F0070.

For disk area the scalar conjugate variable is \(2z\).
At radii \(r>s\) the geometric series gives the angular mean \(r^{-2}\sum_{n\ge0}(s/r)^{2n}=1/(r^2-s^2)\).
The two radial measures \(2r\,dr\) and \(2s\,ds\), both radial orderings and \(s=rx\) give the prefactor eight for both integrals.
Their \(x\)-integrands have order \(1-x\) at one and \(x^{1-2\alpha}\) at zero.
The remaining drift integral has exponent \(1+2\beta-4\alpha\) in \(r\), giving logarithmic divergence at \(\beta=2\alpha-1\).
For \(1/2<\alpha<1\) on that line the scale alone has finite energy, and the drift alone with \(h=1\) has finite energy since \(\beta>0\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0277_v1.md#decision-candidate) | The fixed decision of 2026-11-14T14:24 on free selfadjoint noise with measurable location and scale. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0277_v1.md#statement) | Three-way equivalence, canonical bounded-vector domains, both column orientations, Gram and vacuum formulas, and the radial thresholds. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0277_v1.md#argument) | Inverse-scale test, all three insertions, liberation and cutoff transfer on the represented core, original closure and adjoint, and radial integration. |
| [Finding](#finding) | [Normal generator rules](../../claims/Yin_C_F0076_v1.md#statement) | Forced marginal divided differences, diffuseness for the scalar target restriction, and flip-adjoint vacua. |
| [Finding](#finding) | [Scalar slice](../../claims/Yin_C_F0055_v1.md#statement) | Operator-norm-to-Hilbert bound for the scalar selfadjoint slice used in each weighted terminal map. |
| [Finding](#finding) | [Terminal-block estimate](../../claims/Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Last-noise formula (4), scalar deletion (5), the two constants and extension from finite insertions. |
| [Finding](#finding) | [Liberation recovery](../../claims/Yin_C_F0238_v1.md#statement) | Represented derivation, both diffuse marginals, inverse-gap criterion, norm decomposition, soft and coarse limits. |
| [Finding](#finding) | [Free reference and core transfer](../../claims/Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Free normal reference with a selfadjoint noise factor and smooth normalized-column approximation of both measurable substitutions. |
| [Finding](#finding) | [Two-contraction theorem](../../claims/Yin_C_F0072_v1.md#statement) | Original right-slice closure and its actual Hilbert adjoint on every bounded vector from the two single-input bounds. |
| [Finding](#finding) | [Strong-to-actual theorem](../../claims/Yin_C_F0070_v1.md#statement) | Generator-first commutators and the vacuum-adjoint domain of the supplied duals imply actuality on the starred core. |
| [Finding](#finding) | [Disk marginal](../../claims/Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Normalized area has the actual scalar vacuum \(2z\). |

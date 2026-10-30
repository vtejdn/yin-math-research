---
author: Yin
---

# Independent review: nonnegative bounded densities and original normal cores

Date/time: 2026-09-16T13:22.
Human record author: Yin.
Reviewer/method: another AI agent, separately organized full argument and source-interface review.

Reviewed statement: [Yin_C_F0052_v1](../../claims/Yin_C_F0052_v1.md#decision-candidate-0001).
Consumer scope: the original normal polynomial-core domain question.
Complete selected proof: [Yin_C_F0052_v1.md](../../claims/Yin_C_F0052_v1.md#nonnegative-density-normal-core-transfer), Sections 1--4 and example.

**Verdict: pass.**
The proof establishes the stated sufficient density-transfer result, including densities that vanish on sets of positive reference measure and without radiuswise angular normalization.
It constructs the actual vacuum adjoint, recovers both original bounded-function domains and the intrinsic marginal infinity-to-L2 estimate, and supplies the full original polynomial-core/free-tuple criterion at its stated scope.
No necessity result or unrestricted normal-vacuum domain theorem follows.

## 1. Statement and review arrangement

The reference law is the rotational lift `nu` of a probability `sigma` on `(0,R]`, with its midpoint quantity `A` in `L2(sigma)`.
The new law is `mu=b nu`, where `0<=b<=B<infinity` and `integral b dnu=1`.
The radial law of `mu` may differ from `sigma`.
The claimed bounds and original-domain inclusions concern the canonical divided-difference operator on the represented starred-polynomial core in `L2(mu)`.
The free-tuple consequence additionally retains freeness and all exact original C_F0025 core hypotheses.

The reviewer did not author this proof or its zero-extension mechanism.
Earlier work in the coordinated run concerned a different annulus-local module result in the normal-vacuum domain project and a review of the square-zero proof.
Before this review, the coordinator had supplied the general upper-density transfer idea, later suspended in favor of that square-zero review.
For the present task the reviewer received the completed candidate, the coordinator's requested checks, and the surrounding C_F0051 scope.
During the first read-only review, the coordinator suggested deleting the unused radiuswise angular normalization; the reviewer independently checked every displayed inference and confirmed that only total-mass normalization is needed.
This is an independent, non-blind review, with that preliminary scope discussion disclosed.
No separate-agent label or agreement substitutes for the checks below.

After the initial zero-set candidate, the author supplied the globally normalized candidate without the angular condition.
The reviewer read the final registered proof in full and compared it with that latter candidate: differences are the header/anchor and consumer metadata, rebased relative links, and removal of temporary candidate/pending-review wording.
Its mathematical statement, calculations, and scope boundaries are unchanged.

## 2. Fixed direct inputs and source boundaries

The following direct project dependencies are required for reviewed publication.
Their selected proof files were read at the relevant interfaces:

| Fixed dependency | Exact input and use |
| --- | --- |
| [Yin_C_F0047_v1](../../claims/Yin_C_F0047_v1.md#decision-candidate-0002) | Actual radial closure and adjoint on all bounded functions; midpoint sufficient condition, vacuum vector, and quantitative infinity-to-L2 bound. |
| [Yin_C_F0048_v1](../../claims/Yin_C_F0048_v1.md#decision-candidate-0002) | Polynomial commutator/graph transfer and actual density-pairing mechanism. Its positive-lower-bound theorem is not invoked outside its scope; the steps unused by that lower bound are checked explicitly here. |
| [Yin_C_F0025_v1](../../claims/Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal starred-core hypotheses, canonical normalization/marginal identification, and weak-form representability implying affiliated rationality. |
| [Yin_C_F0045_v1](../../claims/Yin_C_F0045_v1.md#decision-candidate-0002) | Lifting the intrinsic marginal bound through a free product, actual original dual/adjoint graph recovery, unchanged closure after restriction to M, and canonical free-product examples. |
| [Yin_C_F0024_v1](../../claims/Yin_C_F0024_v1.md#decision-candidate-0002) | Complete affiliated-fraction and bounded-element criterion after the original all-M hypotheses have been established. |

C_F0051 v2 is a reviewed comparison and not a proof dependency.
The zero-set result does not rely on its proof or on a provisional variant of it.
C_F0049 is likewise a scope comparison, not an additional logical premise.

The existing C_F0047/C_F0048 reviews and the C_F0045 source interfaces are reused within their established scope.
In particular, the complex little Grothendieck input remains the source-checked Pis12 interface consumed inside C_F0045; it is not newly asserted for an unsuitable domain norm here.
Bounded continuous approximation, Stone-Weierstrass, Hilbert adjoints and weakly closed linear graphs are the same standard interfaces already used in those accepted proofs.
No new external theorem, PDF inspection, recursive whole-source audit, or novelty search was performed.
The new zero-set assembly and all its applicability conditions were checked directly below.

## 3. Represented polynomials, vacuum, and closability

The measures are compactly supported as planar measures and have no point atoms.
The reference has no point atoms because its conditional angular measure is Haar, even when the radial measure has atoms; absolute continuity passes this property to `mu`.
A starred polynomial is Lipschitz on a compact square containing the support, so its divided difference is bounded off the null diagonal.

If a polynomial represents zero in `L2(mu)`, then its divided difference vanishes for `mu tensor mu` almost every pair.
Fubini proves that its canonical output represents zero as well.
This verifies the represented-core quotient before any adjoint computation.
Polynomial density follows on the actual compact support of `mu`; no equality of the two represented polynomial algebras or measure classes is assumed.

C_F0047 supplies `b,bp` in the actual radial operator domains.
The bounded polynomial commutator kernel extends the polynomial identity to every vector in the original radial domain by graph approximation.
Thus

\[
e_{\mu,0}p=E_\nu(bp)-pE_\nu b
\]

is an equality after the continuous restriction to `L2(mu)`.
The resulting initial estimate uses `||p||_(infinity,nu)`, exactly as stated; it is not prematurely used as the C_F0045 hypothesis.

Since `b` is real and belongs to the actual radial adjoint domain, pairing the preceding identity gives

\[
\int e_{\mu,0}p\,d\mu
=\int\bigl(\overline{E_\nu^*b}-E_\nu b\bigr)p\,d\mu.
\]

The asserted `xi_mu=E_nu* b-JE_nu b` is in `L2(mu)`: restriction has norm at most `sqrt(B)`, the radial operator bounds contribute `B a_nu`, and `b xi_nu` contributes `B||xi_nu||`.
This yields precisely the stated `B^(3/2)(||xi_nu||+2a_nu)` bound.
Thus the vacuum really belongs to the actual adjoint domain.
Neither division by `b` nor an equivalence of the two Hilbert adjoints is involved.

Testing the symmetric divided-difference kernel against represented polynomials gives the actual formula `e_mu,0* p=p xi_mu-J e_mu,0 Jp`.
Its domain contains the dense represented polynomial core, so closability follows before any later graph limit is invoked.
The argument is therefore noncircular.

## 4. Zero extension and intrinsic norm recovery

On `S={b>0}`, the measures `mu` and `nu|S` have the same null sets: a set of zero integral against the positive measurable `b` is `nu`-null there.
This statement needs no uniform positive lower bound.
Outside `S`, `mu` vanishes.
Zero extension therefore gives every `f in L-infinity(mu)` a `nu` representative with exactly the same essential supremum norm.

Uniformly bounded polynomial approximants to this extension can be chosen in `L2(nu)` with norm bound arbitrarily close to that supremum, and with an almost-everywhere convergent subsequence.
The inequality `mu<=B nu` gives convergence of their represented `mu` inputs to `f`.
The two initial estimates bound the original operator and actual adjoint outputs.
Weak subsequences and the weak closedness of those *original* linear graphs then place `f` in both domains.
Lower semicontinuity gives the intrinsic `mu` estimates.

This also works when `f` is the `mu` class of a polynomial whose zero extension differs from that polynomial as a `nu` function.
Both construction and the original core value lie in the same closed operator graph with the same first coordinate, so uniqueness identifies the outputs.
This is the decisive justification of equation (15); merely comparing essential suprema in the wrong direction would not establish it.

For the stated operator formula, `bp_n` converges strongly in `L2(nu)` to `b tilde f`, while its radial operator images are uniformly bounded.
Pairing against the dense radial adjoint domain identifies their weak limit.
The bounded restriction map preserves that weak convergence.
Dominated convergence gives strong convergence of `p_n E_nu b`.
These facts identify the actual `E_mu` value, not a newly selected extension.
Changing any extension only outside `S` leaves its first term unchanged in `L2(nu)` and its second term unchanged in `L2(mu)`.

For the adjoint formula, `p_n xi_mu` converges strongly and `E_mu Jp_n` converges weakly by the now proved intrinsic estimate and actual adjoint pairing.
Closedness identifies the actual adjoint output.
The use of complex conjugation is consistent with inner products linear in the second variable.

No step above uses the angular mean of `b` at an individual radius.
Only `integral b dnu=1` is needed to make the changed measure a probability.
Consequently deletion of the radiuswise condition is valid.
The reference midpoint belongs to `sigma`; the proof never converts it into a necessary condition for the different radial marginal of `mu`.

## 5. Free-product conclusion and example

Under the exact C_F0025 original-core assumptions, its normalized marginal restriction is the canonical operator just analyzed.
Equation (15) is now precisely an infinity-to-L2 bound using the marginal algebra's own operator norm, so it meets the crucial C_F0045 hypothesis.
C_F0045 recovers both original all-M domains and the generator relations there.
Its unchanged-closure conclusion is what makes the subsequent C_F0024 use concern the original operators, rather than arbitrary larger or smaller extensions.
Restriction back to the original polynomial core supplies the converse weak-form implication, while C_F0025 supplies the other direction.
The full affiliated-fraction criterion and its some/every fraction independence are used at their accepted scope.
The rational algebra remains unstarred throughout.

The existence assertion also has the needed interfaces: the pairing constructs each marginal vacuum adjoint; the canonical unstarred commutator is the rank-one vacuum projection because `mu` has total mass one; and the starred commutator's phase kernel has modulus one off the null diagonal, hence Hilbert-Schmidt norm one.
The existing C_F0045 construction then gives the original free-product cores.
No unspecified dual-system existence is assumed.

For the half-plane example, `b=2` on the right half-plane and zero on the left has total reference mass one, upper bound two, and a zero-density region of reference measure one half.
For `d sigma=beta r^(beta-1)dr`,

\[
A(r)=r^{\beta-1},\qquad
\|A\|_2^2=\beta\int_0^1r^{3\beta-3}\,dr
=\frac{\beta}{3\beta-2}
\]

when `2/3<beta<1`.
Thus it meets the actual sufficient hypotheses and genuinely lies outside the equivalent-measure class of C_F0051.
Its extra angular-mean-one property is harmless and is not reused as a general premise.

## 6. Conclusion and verification limits

The complete selected proof has no unresolved mathematical gap under its stated sufficient hypotheses.
Publication should attach the five fixed dependencies in Section 2; the initial registration's empty dependency list does not change their logical role.
This review changes no canonical record, generated index, Task contract, or proof artifact.

The result allows zeros and removes the unused angular normalization, while retaining the bounded-density and reference-radial midpoint premises.
It does not prove necessity, allow singular angular laws or unbounded densities, cover correlated tuples, assert bounded scalar rational reconstruction, or complete the unrestricted normal-vacuum domain project.
Internal mathematical review was performed; numerical experiments, rendered-document validation, proof-assistant verification, external human review, and historical priority assessment were not performed.

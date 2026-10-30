---
author: Yin
---

# Uniform actual soft-suppressed vacua and the relative-commutant projection

## Current assessment
[Selected decision](#decision-retained-complete-review)

## Statement

Assume the exact original canonical normal-tuple/coarse-derivation hypotheses of [C_F0025 v1](Yin_C_F0025_v1.md#yin_c_f0025).
For each fixed coordinate X, write partial for its original derivation on the starred polynomial core, xi=partial*(1 tensor 1), and eta for the projection of xi to L2(W*(X)).
Let mu be its diffuse spectral law and, for t>0, set
\[
 h_t(z,w)=\frac{t}{|z-w|^2+t},\qquad g_t=1-h_t,\qquad
 C_t\mu(z)=\int\frac{\overline{z-w}}{|z-w|^2+t}\,d\mu(w).
\]
Let T_h be the joint left-X/right-X spectral multiplier on L2(M), distinct from the inner coarse multiplier I_h.
Then h_t,g_t belong to the actual original adjoint domain and
\[
 \partial^*h_t=T_{h_t}\xi-2\overline{C_t\mu}(X),\qquad
 \|\partial^*h_t\|_2\le3\|\xi\|_2,\qquad
 \|\partial^*g_t\|_2\le4\|\xi\|_2.
\]
The suppressed derivation partial_t=I_(g_t)partial on the original polynomial core is closable and has the actual vacuum xi_t=partial* g_t and conjugate vacuum xi_t*.
The map T_(h_t) is normal, unital, trace preserving and completely positive; as t decreases to zero it converges strongly on L2(M) to the conditional expectation onto L2(X' intersect M).
In contrast h_t as a coarse tensor vector tends to zero, and the weak adjoint limits imply E_(X' intersect M)(xi)=eta.
These assertions hold for correlated tuples.
No uniform mixed contraction estimate, general rationality criterion or Task counterexample is asserted.

## Provenance and accepted inputs

The complete argument was originally authored on 2026-09-29 by another AI agent with root's completely positive multiplier/relative-commutant contribution.
The existing [R_F0033 complete finding](../audits/reviews/Yin_R_F0033_v1.md#independent-review-actual-soft-suppressed-vacua) checked the complete original mathematical body and source/dependency interfaces.
The accepted mathematical inputs remain [C_F0025 v1](Yin_C_F0025_v1.md#yin_c_f0025) and the [C_F0055 soft scalar vacuum bound](Yin_C_F0055_v1.md#soft-cauchy-vacuum-free-normal-criterion) at their actual original-domain scopes.
No new source theorem, isolated review or changed proof is asserted by the current C registration.

## Argument

### 1. Actual smooth tensor adjoint identity

Fix one coordinate X and its normalized original derivation partial on P=C<X_1,X_1*,...,X_d,X_d*>.
Put xi=partial*(1 tensor 1), partial-dagger(p)=(partial(p*))^dagger, with flip-adjoint dagger.
Let mu be the diffuse spectral law of X and let eta be the actual marginal vacuum, the Hilbert projection of xi onto L2(W*(X)).

For t>0 put

    h_t(z,w)=t/(|z-w|^2+t),   g_t=1-h_t,
    C_t mu(z)=integral conjugate(z-w)/(|z-w|^2+t) dmu(w).

For a bounded coordinate tensor h define T_h on L2(M) by the joint spectral calculus of commuting left X and right X.
For h=a tensor b this is T_h(v)=a v b.
Its L2 norm is bounded by ||h||infinity.
This map is different from the inner multiplier I_h on the coarse Hilbert space.

The original adjoint tensor product rule is

    partial*(a tensor b)
      =a xi b - [(id tensor tau)partial-dagger(a)] b
              -a [(tau tensor id)partial-dagger(b)]             (1)

for coordinate starred polynomials a,b.
One proves (1) by expanding partial(a* p b*) inside its vacuum pairing; all outer products are bounded on the coarse space.
This is an actual adjoint formula on P tensor P.

For a coordinate polynomial kernel h, its two correction terms in (1) are coordinate functions whose sum at z is

    integral [2h(z,z)-h(v,z)-h(z,v)]/(conjugate(z)-conjugate(v))
             dmu(v).                                            (2)

For h=h_t this equals 2 conjugate(C_t mu)(z), since h_t is symmetric and h_t(z,z)=1.
Therefore the claimed actual identity is

    partial* h_t = T_(h_t) xi-2 conjugate(C_t mu)(X).              (3)

To justify (3) without selecting a maximal extension, choose L larger than sup(|z-w|^2+t) on a square containing the spectrum and approximate h_t by the finite geometric polynomials

    (t/L) sum_(n=0)^N [1-(|z-w|^2+t)/L]^n.

They converge uniformly with all first real partial derivatives to h_t.
The factor in brackets lies between zero and 1-t/L<1.
Differentiated geometric series therefore converge uniformly too.
Their L2 tensor vectors converge to h_t.
In (1), the T_h xi term converges in L2 by its joint spectral multiplier bound, and the terms (2) converge uniformly by the first-derivative approximation and the mean-value estimate.
Closedness of the actual partial* gives h_t in Dom partial* and identity (3).

C_F0055 yields ||C_t mu||2<=||eta||2<=||xi||2.
Consequently

    ||partial* h_t||2 <= ||xi||2+2||eta||2 <=3||xi||2,
    ||partial* g_t||2 <=2||xi||2+2||eta||2 <=4||xi||2.             (4)

Define the original-domain suppressed derivation partial_t=I_(g_t)partial on P.
Its inner multiplier commutes with both outer actions, so it is still a derivation.
Since g_t is real symmetric, the actual vacuum of partial_t is

    xi_t=partial* g_t=xi-T_(h_t)xi+2 conjugate(C_t mu)(X).         (5)

The vacuum condition and polynomial Leibniz pairing put P tensor P in the actual adjoint domain of partial_t, hence partial_t is closable.
Its conjugate derivation has vacuum xi_t*.
Thus (4) is uniform actual vacuum control, valid for correlated tuples.

### 2. Completely positive structure and the correct diagonal limit

The integral identity

    h_t(z,w)=integral_0^infinity t exp(-ts) exp(-s|z-w|^2) ds

expresses h_t as an average of positive-definite Gaussian kernels.
More concretely, write X=S+iT with commuting bounded selfadjoints S,T.
The elementary Gaussian characteristic-function formula expresses exp(-s|z-w|^2) as an average of exp(i alpha Re(z-w)+i beta Im(z-w)).
Consequently T_(h_t) is an average of the trace-preserving automorphisms

    v -> exp(i alpha S+i beta T) v exp(-i alpha S-i beta T).

It is therefore normal, unital, trace-preserving and completely positive, and is contractive on M and on L2(M).
This paragraph is a direct Gaussian integral proof, not an appeal to a universal Schur-multiplier property of the nonsmooth normal phase.

As t tends to zero, the joint L2 spectral multiplier h_t tends pointwise to the indicator of the diagonal z=w.
Thus T_(h_t) converges strongly on L2(M) to the orthogonal projection onto L2(X' intersect M), equivalently the trace-preserving conditional expectation onto that relative commutant.
It does **not** tend to zero on L2(M).

By contrast h_t, viewed as a vector in L2(mu tensor mu), tends to zero in norm, because mu is nonatomic.
Formula (4) and weak closedness of the graph of partial* show that partial* h_t tends weakly to zero: each weak cluster point pairs to zero against the dense original partial domain.
Moreover C_F0055's uniform soft bound and the original vacuum pairing give

    2 conjugate(C_t mu) -> eta weakly in L2(mu).

Indeed the soft divided differences converge on scalar polynomials and their double integral is twice the polynomial pairing with C_t mu.
Density and the uniform bound extend the weak convergence to every L2 test.
Taking weak limits in (3) consequently gives the auxiliary identity

    E_(X' intersect M)(xi)=eta.                                 (6)

This is a condition on the projection of the joint conjugate vector.
It does not assert that W*(X) is a maximal abelian subalgebra or identify all of X' intersect M.

### 3. What remains missing

The derivatives partial_t approach partial on each original polynomial in the coarse norm, because their inner multipliers g_t tend strongly to the identity off the null product-spectral diagonal.
Their vacuum vectors remain uniformly bounded by (4).
Neither fact proves uniform boundedness of their contractions (id tensor tau)partial_t from operator norm to L2.
The known selfadjoint estimate uses an additional real/coassociative energy identity; here the suppressed derivations still have a mixed phase defect.
No estimate for that defect is supplied.

The possible use is a noncommutative regularized energy argument exploiting the actual formula (5) and complete positivity of T_(h_t), retaining a positive square instead of eliminating all mixed terms tautologically.
Pointwise scalar three-point positivity alone is not transferred to correlated mixed words.
No main criterion or counterexample follows from this note alone.

## Assessment history

### Decision registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:39 |
| status | open |
| reason | Retain the complete existing proof in its responsible C home before current adoption of the applicable original full finding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact original normal/coarse hypotheses, actual vacuum bounds, CP map and projection identity, with the mixed contraction gap retained. |
| argument | [Argument](#argument) | Complete original tensor-adjoint approximation, Gaussian multiplier and weak-limit proof, plus its exact remaining boundary. |

### Decision retained-complete-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:39 |
| status | proved |
| reason | Adopt the actual complete original R_F0033 finding for the unchanged retained mathematical argument and exact statement, at its disclosed self-reviewed relationship and original source/input depths. This is current adoption, not a new or redated mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete actual-vacuum, suppressed derivation, completely positive multiplier and relative-commutant projection conclusions, with no mixed contraction estimate. |
| argument | [Argument](#argument) | Whole retained Sections 1-3 chain and exact accepted C_F0025/C_F0055 interfaces. |
| review | [Original complete finding](../audits/reviews/Yin_R_F0033_v1.md#independent-review-actual-soft-suppressed-vacua) | Complete original proof and applicability check, preserving its actual 2026-09-29 date and disclosed prior summary context. |


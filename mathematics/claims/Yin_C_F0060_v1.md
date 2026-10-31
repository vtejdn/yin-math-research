---
author: Yin
---

# Original weak rationality with scalar polynomial denominators and arbitrary numerators

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Original finite-rank weak forms for scalar polynomial denominators

<a id="scalar-denominator-original-weak-criterion"></a>

Date: 2026-09-29.
Human author: Yin.
Authoring agent: counterexample.
Permanent consolidation of independently reviewed proofs.
This is a bounded weak-form criterion for the displayed classes, not the full arbitrary unbounded-fraction conclusion of T_F0001.

Exact original hypotheses: [C_F0025_v1](Yin_C_F0025_v1.md#yin_c_f0025).
The included arguments use the complete original graph module and affine state theorem in [the permanent affine proof](Yin_C_F0059_v1.md#kernel-affine-original-l2-states).
Scalar soft inversion is reproduced in Appendix A.
Its C1 polynomial approximation uses the previously accepted [VV16-U001 interface](../audits/literature/VV16/Yin_U001.md).
The scalar polynomial gcd/Bezout step reuses the Hun74 III.3.9/III.3.11 interface recorded in [Hun74-U006](../audits/literature/Hun74/Yin_U006.md#exact-retained-statement-and-proof-inspection-depth).
These are proof inputs at their recorded scopes, not new source audits.

The main theorem covers every unstarred polynomial numerator Q in a bounded P(X_k)^(-1)Q.
Appendix B covers bounded P(X_k)^(-1)X_i Q(X_k)^(-1), i!=k.
The latter includes two singular inverse states and is not inferred merely by multiplying one-sided results.

Historical independently reviewed inputs:
- Arbitrary numerator
- Two-sided class
- Scalar soft-inverse support
Mathematical bodies follow in full; only dependency pointers and section headings are normalized for permanent consolidation.
Appendix A drops the unused condition k!=i from the historical setup: its proof uses only k and applies without any second coordinate, including d=1.
Claim allocation and exact permanent review binding are separate administrative actions.

## 1. Statement and algebraic cancellation

Let k be a coordinate, P a nonzero scalar polynomial, Q any unstarred noncommutative polynomial in X_1,...,X_d, and suppose

    f=P(X_k)^(-1)Q(X) belongs to M.                            (1)

Then every original weak commutator of f is represented by a bounded finite-rank operator.
The numerator is not assumed linear in any coordinate.

There is a unique finite decomposition in the free polynomial algebra

    Q=D(x_k)+sum_w A_w(x_k) w,                                (2)

where each nonempty word w starts with a letter other than x_k, and D,A_w are scalar polynomials.
It is obtained by removing the maximal initial run of x_k from every monomial and collecting equal remaining words.
The current C_F0025 free-field embedding makes this formal decomposition valid after evaluation, with no accidental polynomial relation.

Divide P,D and every A_w by their common scalar polynomial gcd first.
This does not change (1): Q has that factor on the left and scalar polynomials in X_k commute with P.
For the rest of the proof use the reduced data, so

    gcd(P,D,(A_w)_w)=1.                                      (3)

The substantive state conclusion is that this reduced P(X_k)^(-1) is in L2.
No such conclusion is asserted for a denominator with an uncancelled common factor, for which it would plainly be false.

## 2. Polynomial probes outside the kernel are still permitted

Fix j!=k and put B_j=W*(X_l:l!=j), a=P(X_k), r=a^(-1).
Use the original closed coarse derivation d_j and its actual vacuum xi_j.
The permanent affine-kernel proof supplies the B_j graph module property.
Let `e_n=1_[1/n,n](|a|)`, `r_n=e_n r`; then `r_n Q=e_n f`.

For every fixed original starred polynomial c, the map

    z -> z(d_j c),  L2(M) -> coarse L2,

is bounded.
Indeed the polynomial derivative is a finite sum of tensors p tensor q and normal phase tensors p k_j q.
The inner phase unitary I_j commutes with all outer actions and

    p k_j q=I_j(p tensor q),

so multiplication of p by z costs at most ||p||||z||2, while q remains bounded.
Denote any resulting finite operator bound by K_(j,c).
This uses only the coarse Hilbert-space phase, never an operator Schur multiplier.
The same finite expressions show that right multiplication by c preserves the original closed graph, with its product rule.

Consequently, for bounded b in B_j, every term of

    d_j(b r_n Q c)
       =b r_n(d_j Q)c+b e_n f(d_j c)                         (4)

lies in the actual original graph calculation.
Pairing with the vacuum and using conditional expectation onto B_j yields

    tau(b r_n A_(j,c))
      =<xi_j,b e_n f c>-(tau tensor tau)(b e_n f(d_j c)),

where the bounded B_j element is

    A_(j,c)=E_(B_j)[(id tensor tau)((d_j Q)(1 tensor c))].

Thus

    |tau(b r_n A_(j,c))|
       <=||f|| (||xi_j||2||c||+K_(j,c)) ||b||2.              (5)

Putting b=(r_n A_(j,c))* and using monotone convergence in the extended trace proves

    r A_(j,c) belongs to L2                                 (6)

for EVERY fixed original polynomial c, including starred polynomials.
All tests in (4) are performed before removing the bounded cutoff.
This is the new point beyond kernel-only probes: the derivative of c contributes a controlled term, because r_n Q=e_n f is uniformly bounded.

## 3. Suffix probes and descending recovery of all left coefficients

For fixed j!=k, collect the unstarred polynomial derivative by distinct right-hand suffix words v:

    d_j Q=sum_v U_(j,v) tensor v.                            (7)

There are finitely many such suffixes.
Their evaluations are complex-linearly independent, since the unstarred free algebra embeds faithfully.
Their L2 Gram matrix is therefore positive definite.
Choose starred polynomial probes c_(j,v), finite linear combinations of the adjoints of those suffixes, with

    tau(v' c_(j,v))=delta_(v',v).

Equations (6)--(7) give

    r E_(B_j)(U_(j,v)) in L2.                                (8)

Now recover the coefficients A_w of (2) by descending length of w.
For a word w=jv beginning with j!=k, the suffix coefficient in (7) is EXACTLY

    U_(j,v)=A_w(X_k)
       +sum_(w'=u jv, u nonempty) A_(w')(X_k) u.              (9)

Every w' in the latter sum is one of the words from (2) and has length strictly larger than w.
Its nonempty prefix u begins with a letter other than k.
The derivative does not act on A_(w'), since j!=k.
These facts establish (9) directly, without any conditional independence assumption.

At maximal word length the sum is empty, so (8) yields r A_w in L2.
At an inductive step the already recovered r A_(w') belong to L2 and all E_(B_j)(u) are bounded.
Since A_(w') and r are affiliated with B_j, (9) gives

    r A_w
      =r E_(B_j)(U_(j,v))
         -sum_(w'=u jv, u nonempty)(r A_(w')) E_(B_j)(u),

which is in L2.
This proves r A_w in L2 for every w.
An identically zero suffix coefficient causes no problem: its equality (9) gives the same inductive conclusion with zero as the first term.
Equivalently, omit such suffixes from (7).

Finally, the affiliated identity

    rD(X_k)=f-sum_w (r A_w(X_k))w

puts rD in L2.
Scalar polynomial Bezout applied to (3) gives r in L2, since rP=1 and all remaining multipliers are bounded scalar polynomials in X_k.
The m=0 case uses the same argument directly from rD=f.

## 4. Original graphs and finite weak forms

The scalar soft-inverse step is reproduced in Appendix A below.
For

    r_t=conjugate(P)(X_k)/(|P(X_k)|^2+t),
    e_t=|P(X_k)|^2/(|P(X_k)|^2+t),

one has original graph convergence r_t -> r and

    partial_k r=-r(partial_k a)r,  partial_j r=0 (j!=k).

Set f_t=r_t Q=e_t f.
These are uniformly bounded by ||f||, and their derivatives converge in every original coarse graph to

    partial_j f=r partial_j Q                  (j!=k),
    partial_k f=-r(partial_k a)f+r partial_k Q.              (10)

Every term in (10) is an algebraic finite L2 tensor, because r is L2, the polynomial derivative tensors are bounded, and f is bounded.
The original product graph rule on f times every polynomial test gives, after contraction,

    beta_j^f(p,q)=<p,Theta(partial_j f)q>.

C_F0025 normalization invariance returns the exact originally specified duals.
Thus the conclusion concerns the original weak forms, not a replacement domain.
The analogous right fraction follows by the corresponding right cutoffs and reversed words, or by taking adjoints with the original conjugate derivations; that symmetric extension is not needed for the displayed theorem.

## 5. Scope and reuse

This upgrades the earlier linear-numerator state lemma to every unstarred polynomial numerator for a single-coordinate scalar polynomial denominator.
It excludes the proposed nonlinear Haar-phase radial sandwich immediately: for Q=X_i^2 and its zero first conditional moment, the probe c=X_i* gives A_(i,c)=tau(X_i X_i*)1, forcing the allegedly non-L2 inverse into L2.

The remaining general minimal-pencil difficulty is unchanged: a matrix or scalar denominator involving the differentiated coordinate cannot be damped inside its kernel algebra.
Its cutoff derivatives need an additional estimate.
No automatic full inverse integrability, full arbitrary-fraction criterion, or valid counterexample is claimed.

Reused inputs are exact C_F0025 original normalization and phase representation; the permanent affine-kernel graph module proof and Appendix A below; the existing Hun74 III.3.9/III.3.11 scalar PID/Bezout interface recorded in Hun74-U006; and finite Gram duality.
The suffix extraction is a direct finite polynomial calculation.
No new external source or acquisition is introduced.

## Appendix A. Original scalar soft inversion

Let k be any coordinate and let P be a nonzero complex polynomial.
Put a=P(X_k), r=a^(-1), and assume r in L2.
For t>0 define scalar functions on the X_k spectrum

    r_t(z)=conjugate(P(z))/(|P(z)|^2+t),
    e_t(z)=|P(z)|^2/(|P(z)|^2+t).

Each r_t is smooth on a rectangle containing the spectrum.
C1 polynomial approximation places it in every original coarse graph: its k derivative is the scalar divided difference, and all other coordinate derivatives vanish.
For nonzero u,v,

    |(conjugate(u)/(|u|^2+t)-conjugate(v)/(|v|^2+t))/(u-v)|
      <= (|u||v|+t)/((|u|^2+t)(|v|^2+t))
      <=1/(|u||v|).

If u=v, the composite numerator below is zero; no complex derivative or continuous diagonal extension is asserted.
Composing off-diagonal quotients with P gives

    |(r_t(z)-r_t(w))/(z-w)|
      <= |(P(z)-P(w))/(z-w)| |r(z)r(w)|.

The polynomial divided difference is bounded on the compact spectral square.
The right side is L2(mu_k tensor mu_k), because r is L2.
Dominated convergence therefore shows

    r_t -> r in every original coarse graph,
    partial_k r=-r (partial_k a) r,
    partial_j r=0 for j!=k.                                    (B)

The k derivative is a finite algebraic tensor with L2 factors, since P is a polynomial and commutes with r.
No arbitrary affiliated chain rule is used.


## Appendix B. Two-sided scalar denominators

### Statement

Let i!=k, let P,Q be nonzero scalar polynomials, and set

    a=P(X_k), c=Q(X_k), r=a^(-1), s=c^(-1).

If the affiliated rational output f=r X_i s belongs to M, then r,s belong to L2 and f belongs to EVERY original closed coarse derivation domain.
Its original weak forms have the bounded finite-rank representatives corresponding to the finite L2 tensors

    partial_i f=r tensor s,
    partial_k f=-r(partial_k a)f-f(partial_k c)s,
    partial_j f=0 for j not in {i,k}.                           (1)

All products in (1) mean the finite outer tensor products, whose factors are L2: r,s are L2 and f, all polynomial factors are bounded.
This is a rational weak converse for this class on arbitrary correlated normal tuples.
No boundedness of either inverse state or all-M contraction estimate is assumed.

### L2 states and original scalar graphs

The affine-kernel state lemma applies with B=W*(other coordinates than i), one nonzero left state r, one nonzero right state s, and constant term zero.
It gives both r,s in L2 from the actual i-vacuum.
Its proof uses bounded regular dampings and B probes; it does not initially apply a derivative to an unbounded coefficient.
C_F0025's maximal-Delta field embedding ensures regularity and nonzero states for every nonzero P,Q.

For t>0 put

    A_t=a*a+t, B_t=c*c+t,
    r_t=a* A_t^(-1), s_t=c* B_t^(-1),
    e_t=a*a A_t^(-1), j_t=c*c B_t^(-1).

The scalar soft inverse argument in Appendix A gives r_t->r and s_t->s in the original k-coarse graphs.
Each of these smooth coordinate functions has operator-norm and original graph polynomial approximants.
The exact derivative identities are

    partial_k r_t=-r_t(partial_k a)r_t
                       +t A_t^(-1)(partial_k a*)A_t^(-1),
    partial_k s_t=-s_t(partial_k c)s_t
                       +t B_t^(-1)(partial_k c*)B_t^(-1).       (2)

These follow by the ordinary product/inverse rules on the bounded graph algebra, or directly from the scalar quotient kernels.
Normality is used in a a*=a*a and c c*=c*c.

### Uniformly bounded output approximants and the residual terms

Define

    f_t=r_t X_i s_t=e_t f j_t.

Thus ||f_t||<=||f|| and f_t->f in L2.
For each fixed t, the polynomial graph approximations just described put f_t in every original coarse domain.
Its i derivative is r_t tensor s_t and the other derivatives except k vanish.

Substituting (2), the k derivative consists of the two main terms

    -r_t(partial_k a)f_t-f_t(partial_k c)s_t                    (3)

and two residuals.
The main terms converge in coarse L2 to their counterparts in (1): expand each polynomial derivative as a finite tensor, use L2 state convergence and the uniform boundedness/strong convergence of f_t.

Here the residuals cannot be discarded solely from convergence of r_t and s_t, since the other inverse coefficient need not be uniformly bounded.
Their exact factorizations resolve that issue.
Affiliated multiplication gives

    A_t^(-1) X_i s_t=r* f_t,
    r_t X_i B_t^(-1)=f_t s*.

Consequently the residuals are

    (t A_t^(-1))(partial_k a*)(r* f_t),
    (f_t s*)(partial_k c*)(t B_t^(-1)).                        (4)

For nonconstant P and a=P(X_k), its scalar spectral phase gives

    partial_k a*=I_(phase_a)(partial_k a),
    phase_a(z,w)=(conjugate(P(z))-conjugate(P(w)))/(P(z)-P(w)).

The phase is an inner unitary on the coarse Hilbert space and commutes with all outer actions.
Its exceptional zero-difference set has product measure zero: the scalar polynomial image of a diffuse spectral measure is diffuse.
The same holds for c when Q is nonconstant.
A constant P or Q has zero derivative and zero corresponding residual, so no phase is needed for it.
Since partial_k a is a finite polynomial tensor, there is a finite constant C_a with

    ||g(partial_k a*)h||_(coarse2)<=C_a||g||2||h||2             (5)

for the L2 vectors in (4).
Indeed commute the inner phase outside the outer products and estimate each finite tensor g a_l tensor b_l h.
This uses only coarse L2 unitarity, not a universal operator Schur bound.

Now ||r* f_t||2<=||r||2||f|| and ||f_t s*||2<=||f||||s||2, while t A_t^(-1) and t B_t^(-1) tend to zero in L2 by regularity and dominated spectral convergence.
Equations (4)--(5) therefore make both residuals tend to zero.
This proves convergence in every original coarse graph, with (1).

### Original weak representatives

For each t, choose polynomial approximants of f_t simultaneously in operator norm and all the finitely many coarse graph norms.
A diagonal sequence is uniformly bounded and converges to f with derivatives (1).
Multiplying by any original polynomial q preserves graph convergence through the product rule and strong convergence of the bounded left multipliers.
Therefore fq lies in the original normalized contraction domain and

    E_j(fq)-f E_j(q)=Theta(partial_j f)q.

The actual Hilbert adjoint pairing on original polynomial tests gives the claimed bounded finite-rank weak forms.
Normalization invariance is exactly C_F0025's identity, so the conclusion concerns the specified original duals.

The result includes singular sandwich outputs of the form X_k^(-1)X_i X_k^(-1), whenever bounded.
It gives no full arbitrary-affiliated-fraction criterion and no all-M contraction.
General rational outputs may have state coefficients outside the algebra annihilated by one derivation and remain outside this proof.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T23:55 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#scalar-denominator-original-weak-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Every bounded quotient P(Xk)^(-1)Q(X), with scalar polynomial P and arbitrary unstarred polynomial Q, has bounded finite-rank representatives of every original weak commutator.
The proof derives reduced inverse L2 integrability by starred probes, suffix descent and Bezout, and also treats two-sided scalar sandwiches.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:15 |
| status | proved |
| reason | Select the two exact original scoped findings with disclosed unknown initial relationships and restore the already invoked approximation source as an explicit input. The current statement selects the consolidated root: the older #statement locator remains the Appendix B substatement in its historical decisions. Preserve every theorem, proof, mathematical status and original dated selector; this is not a new mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#scalar-denominator-original-weak-criterion) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#scalar-denominator-original-weak-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original canonical coarse derivations, actual vacuum, inner phase, faithful unstarred free algebra and normalization interface. |
| dependency | [Exact material](Yin_C_F0059_v1.md#decision-candidate-0002) | Original kernel algebra graph module in the main proof and automatic L2 left/right states in Appendix B. |
| dependency | [Exact material](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted scalar polynomial PID, gcd cancellation and Bezout interface only. |
| dependency | [Exact source input](../audits/literature/VV16/Yin_U001.md#vv16-u001) | Existing C1 rectangle polynomial approximation used by Appendix A in the original scalar graph; no new source audit. |
| review | [Original finding](../audits/reviews/Yin_R_F0079_v1.md#retained-r101-scope-and-verdict) | Unknown initial context; main Sections 1–5 and Appendix A only, including arbitrary numerators, suffix probes, Bezout, original soft-inverse graphs and d=1. |
| review | [Original finding](../audits/reviews/Yin_R_F0079_v1.md#retained-r102-verdict-and-achieved-conclusion) | Unknown initial context; separate Appendix B two-sided singular scalar denominators, actual bounded output approximants, residuals and original graphs. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T01:27 |
| status | proved |
| reason | Adopt the fresh isolated whole-proof finding after its initial mathematical judgment and subsequent comparison with the separately preserved original unknown account(s). Preserve the exact statement, proof, mathematical status, all non-review inputs and every historical decision; no Task lifecycle change or mathematical repair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#scalar-denominator-original-weak-criterion) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#scalar-denominator-original-weak-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original canonical coarse derivations, actual vacuum, inner phase, faithful unstarred free algebra and normalization interface. |
| dependency | [Exact material](Yin_C_F0059_v1.md#decision-candidate-0002) | Original kernel algebra graph module in the main proof and automatic L2 left/right states in Appendix B. |
| dependency | [Exact material](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted scalar polynomial PID, gcd cancellation and Bezout interface only. |
| dependency | [Exact source input](../audits/literature/VV16/Yin_U001.md#vv16-u001) | Existing C1 rectangle polynomial approximation used by Appendix A in the original scalar graph; no new source audit. |
| review | [Fresh whole-proof finding](../audits/reviews/Yin_R_F0079_v1.md#fresh-c102-whole) | Independently reviewed. Whole main Sections 1-5 and complete Appendices A-B, original weak forms and exact input/source boundaries. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T23:58 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#scalar-denominator-original-weak-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original canonical coarse derivations, actual vacuum, inner phase, faithful unstarred free algebra and normalization interface. |
| dependency | [Exact material](Yin_C_F0059_v1.md#decision-candidate-0002) | Original kernel algebra graph module in the main proof and automatic L2 left/right states in Appendix B. |
| dependency | [Exact material](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted scalar polynomial PID, gcd cancellation and Bezout interface only. |
| review | [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r101) | Main theorem Sections 1-5 and Appendix A independently checked by another AI agent; Appendix B separately checked by another AI agent in the attached scoped review. Covers arbitrary unstarred polynomial numerators, actual starred probes, descending suffix coefficients, scalar Bezout, soft inverse original graphs, all original weak forms and two-sided scalar sandwiches. General mixed denominators and the full unbounded task remain open. |

Recorded mathematical summary: Every bounded quotient P(Xk)^(-1)Q(X), with scalar polynomial P and arbitrary unstarred polynomial Q, has bounded finite-rank representatives of every original weak commutator.
The proof derives reduced inverse L2 integrability by starred probes, suffix descent and Bezout, and also treats two-sided scalar sandwiches.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r102); [Exact material](../audits/literature/VV16/Yin_U001.md).

Main theorem Sections 1-5 and Appendix A independently checked by another AI agent; Appendix B separately checked by another AI agent in the attached scoped review.
Covers arbitrary unstarred polynomial numerators, actual starred probes, descending suffix coefficients, scalar Bezout, soft inverse original graphs, all original weak forms and two-sided scalar sandwiches.
General mixed denominators and the full unbounded task remain open.

Review: [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r101).

Material covered by that review: [Exact material](../audits/literature/VV16/Yin_U001.md); [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r102); [Exact material](Yin_C_F0060_v1.md).

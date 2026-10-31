---
author: Yin
---

# Complete Review of Yin_C_F0034-P1 and Yin_C_F0035-P1

## Actual review arrangements

The reviewer authored the original complete C_F0029 proof containing these arguments, participated in finite-range cancellation and tensor descent, and authored C_F0032/C_F0033. The complete new-artifact review therefore has known mathematical ancestry/development involvement and is self-reviewed for both lemmas.
The original dates, prior independent descriptions, mathematical findings and source-depth limits remain intact; these declarations perform no new mathematical review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete fraction-algebra lemma](#fraction-algebra-finding) | self-reviewed |
| [Complete algebraic equalizer lemma](#division-equalizer-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete fraction-algebra lemma](#fraction-algebra-finding) | [Exact fixed input](../../claims/Yin_C_F0034_v1.md#statement) | Entire C_F0034-P1 fraction-independent finite-rank algebra and generator containment, exact C_F0031 uses, accepted affiliated foundations and explicit non-reverse/non-adjoint limits. |
| [Complete fraction-algebra lemma](#fraction-algebra-finding) | [Exact fixed input](../../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1) | Entire C_F0034-P1 fraction-independent finite-rank algebra and generator containment, exact C_F0031 uses, accepted affiliated foundations and explicit non-reverse/non-adjoint limits. |
| [Complete algebraic equalizer lemma](#division-equalizer-finding) | [Exact fixed input](../../claims/Yin_C_F0035_v1.md#statement) | Whole same-unit possibly noncentral division-subring tensor equalizer argument, correct right/left orientation and ordinary algebraic basis choice; no analytic input or later source-proof audit added. |
| [Complete algebraic equalizer lemma](#division-equalizer-finding) | [Exact fixed input](../../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1) | Whole same-unit possibly noncentral division-subring tensor equalizer argument, correct right/left orientation and ordinary algebraic basis choice; no analytic input or later source-proof audit added. |

<a id="fraction-algebra-finding"></a>
### Complete fraction-algebra lemma

Entire C_F0034-P1 fraction-independent finite-rank algebra and generator containment, exact C_F0031 uses, accepted affiliated foundations and explicit non-reverse/non-adjoint limits.
The corresponding complete original checking account and its precise limits follow below.

<a id="division-equalizer-finding"></a>
### Complete algebraic equalizer lemma

Whole same-unit possibly noncentral division-subring tensor equalizer argument, correct right/left orientation and ordinary algebraic basis choice; no analytic input or later source-proof audit added.
The corresponding complete original checking account and its precise limits follow below.

<a id="yin_c_f0034-yin_c_f0035-fraction-tensor-review"></a>

Date: 2026-09-10.
Reviewer: the reviewing agent.
Reviewed author: another AI agent.
Result: both complete proof versions are mathematically accepted at their stated scopes; no required correction was found.

## 1. Exact Artifacts and Review Scope

The complete reviewed target is Fraction Algebra and Tensor Equalizers (original material now separated into [Yin_C_F0034_v1](../../claims/Yin_C_F0034_v1.md), [Yin_C_F0035_v1](../../claims/Yin_C_F0035_v1.md)), including the statements, all proof steps, dependencies, extraction provenance, limits and review metadata for [Yin_C_F0034-P1](../../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1) and [Yin_C_F0035-P1](../../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1).
I also read and reconstructed the entire direct project dependency [Yin_C_F0031-P1](../../claims/Yin_C_F0031_v1.md#yin_c_f0031-p1), at its stated scope.

This review checks that dependency's finite-range closure and dense-restriction cancellation arguments as actually used here.
It does not replace Yin_C_F0031's separate claim-level review record.
I checked the [batch authorization and version map](../../ledger/Yin_L_F0014_v1.md#authorization) and the accepted fraction/regularity interface and trust boundary recorded in [Miy22-U006](../literature/Miy22/Yin_U006.md#miy22-u006).
I did not perform a new primary-PDF audit or independently reprove the foundational construction of the affiliated algebra.
The source audit's existing distinction between reconstructed consequences and accepted affiliation foundations is retained.

The reviewer authored the original complete Yin_C_F0029 proof from which these arguments were extracted and participated in the earlier proof development, including the finite-range cancellation and tensor-descent discussion.
The reviewer also authored the newly extracted Yin_C_F0032/Yin_C_F0033 module.
These prior roles are disclosed: this is a fresh complete examination of the separately authored Yin_C_F0034/Yin_C_F0035 artifact, not a claim that the reviewer had no prior involvement in its mathematical ancestry.
Yin_C_F0032/Yin_C_F0033 are not direct inputs to either proof reviewed here.
No source-file or claim-index edits were made by this review.

## 2. Yin_C_F0034: Hypotheses, Closability and the Yin_C_F0031 Interface

The statement allows a dense left \(M\)-module \(\mathcal E\subseteq L^2(M,\tau)\) whose vectors can be unbounded.
The dense adjoint-test spaces \(V_i\) are also left \(M\)-modules.
These are exactly the domain properties needed for the displayed defects; no vacuum vector, bounded-vector inclusion, or right-module invariance is used.

For \(z\in\mathcal E\) and \(w\in V_i\), the arguments \(bz,tz\) lie in \(\mathcal E\), while \(s^*w,a^*w\) lie in \(\operatorname{Dom}D_{i,0}^*\).
With the inner product linear in the second variable, the adjoint calculation is

\[
\langle w,(sD_{i,0}b-aD_{i,0}t)z\rangle
=\langle b^*D_{i,0}^*(s^*w)-t^*D_{i,0}^*(a^*w),z\rangle.
\]

Thus each defect has a dense adjoint domain and is closable.
The outside bounded coefficients and the order of adjoints are correct.
This establishes closability before finite rank or any bounded extension is asserted.

I independently reconstructed both relevant parts of Yin_C_F0031.
A finite-range closable map is bounded on its dense initial domain: project its dense adjoint domain onto the finite-dimensional range, lift a range basis through that projection, and use the resulting finitely many bounded adjoint functionals to express the map.
Its graph closure is the everywhere-defined bounded extension with exactly the original range.
If its restriction to a Hilbert-dense subspace has finite range, that restriction's bounded closure already has a whole-domain graph contained in the original operator's closed graph.
Single-valuedness then forces the two closures to agree.
Hilbert density is not silently converted to graph density; graph density follows only after this argument.

For a bounded regular \(y'\in M\), the left action of \(y'\) has dense range, and \(y'\mathcal E\subseteq\mathcal E\).
Continuity of that action and density of \(\mathcal E\) imply density of \(y'\mathcal E\) in \(H\).
For a bounded regular \(y\), injectivity of its left action preserves the dimension of the tested range.
Consequently Yin_C_F0031 applies to \(z\mapsto yT(y'z)\), proving equivalence of finite rank and equality of the finite numerical ranks.
All hypotheses of this invocation are verified; bounded inverses and a pre-existing bounded defect are unnecessary.
The rank-zero case is included.

## 3. Yin_C_F0034: Fraction and Algebra Calculations

I checked every affiliated identity and every resulting equality on \(\mathcal E\), maintaining the order of factors.

**Bounded fractions.**
The functional-calculus choices
\[
s=(1+uu^*)^{-1/2},\quad a=su,\qquad
t=(1+u^*u)^{-1/2},\quad b=ut
\]
give bounded numerators and regular bounded denominators by the accepted polar/spectral calculus.
The formula uses the appropriate side of \(uu^*\) and \(u^*u\); it does not require a bounded inverse denominator.

**Common multiples.**
If \(s_1s_2^{-1}=x^{-1}y\), then \(xs_1=ys_2\).
The ratio is a unit in \(U(M)\), so \(y=x(s_1s_2^{-1})\) is a unit there and hence is regular as a bounded element.
The right-sided construction \(t_1^{-1}t_2=pq^{-1}\) similarly gives \(t_1p=t_2q\), with both new factors regular.
These constructions permit independent left and right common denominators.

**Independence and ranks.**
The four identities
\[
xs=ys_1,\quad tx'=t_1y',\quad xa=ya_1,\quad bx'=b_1y'
\]
give the exact operator equality
\[
yT_i^{s_1,a_1,b_1,t_1}(y'z)
=xT_i^{s,a,b,t}(x'z),\qquad z\in\mathcal E.
\]
Every inner multiplier preserves the specified domain.
Yin_C_F0031 applied to each side proves both fraction-independent finiteness and equality of the finite numerical ranks, including the ranks of the closures.
The proof correctly does not assert that the operators themselves are independent of the fractions.

**Linear operations.**
Common denominators express sums as sums of defects.
Complex linearity gives the scalar calculation, including the zero scalar.
The identity coefficient \(1\) acts on every domain vector and does not require \(\Omega\in\mathcal E\).

**Products.**
For
\[
a_1s_2^{-1}=x^{-1}y,\qquad t_1^{-1}b_2=pq^{-1},
\]
the identities are \(xa_1=ys_2\) and \(t_1p=b_2q\).
Only \(x,q\) need be regular.
The fraction pair
\[
u_1u_2=(xs_1)^{-1}ya_2=b_1p(t_2q)^{-1}
\]
has the correct denominator order, since \((xs_1)^{-1}=s_1^{-1}x^{-1}\) and \((t_2q)^{-1}=q^{-1}t_2^{-1}\).
Expanding \(xT_{i,1}(pz)+yT_{i,2}(qz)\) produces precisely the new defect.
The two middle terms cancel because both their outer coefficients and their actual domain inputs agree.
No derivative is evaluated at an arbitrary affiliated vector.
Finite rank of each summand uses only domain preservation and finite-dimensional range; injectivity of \(y\) or \(p\) is not needed.

**Inverses and division closure.**
When \(u\) is a unit of \(U(M)\), the bounded numerators \(a=su\) and \(b=ut\) are regular.
The inverse pair is \(u^{-1}=a^{-1}s=tb^{-1}\), whose defect is
\[
aD_{i,0}(tz)-sD_{i,0}(bz)=-T_i^{s,a,b,t}z.
\]
The proof therefore covers precisely inversion of ambient units.
It does not treat an arbitrary nonzero element of a ring with zero divisors as a unit.
The generator assumption in assertion 4 puts each \(X_j\) in the resulting inverse-closed algebra via its unit-denominator pair.
The definition of \(\operatorname{Div}_U A\) then gives the claimed containment.
No normality, generation, freeness or maximal-Delta hypothesis has entered this proof.

I checked the stated boundary example \(M=\mathbb C\oplus\mathbb C\), \(D_{1,0}=0\), \(X_1=1\).
All defects vanish and the optional generator premise holds, but the division closure of \(\mathbb C1\) is still only \(\mathbb C1\).
Thus the text correctly separates inverse-closed algebra structure and forward containment from any reverse rationality or free-field assertion.
It also makes no unsupported assertion of closure under adjoints.

## 4. Yin_C_F0035: The Same-Unit Division-Subring Equalizer

I reconstructed the full algebraic proof under the stated generality: \(U\) is any unital ring and \(F\subseteq U\) is a division subring with the same nonzero identity.
The first copy of \(U\) is a right \(F\)-module, the second a left \(F\)-module.
The forward direction follows directly from the balancing relation.

For \(u\notin F\), a right-linear relation \(a+ub=0\) with \(a,b\in F\) is trivial: if \(b\neq0\), right multiplication by \(b^{-1}\) gives \(u=-ab^{-1}\in F\), a contradiction.
Thus \(\{1,u\}\) can be extended to a right-\(F\) basis.
Taking the coefficient of \(u\) defines a right-\(F\)-linear functional \(\phi:U\to F\) with \(\phi(1)=0\) and \(\phi(u)=1\).

The orientation of the induced tensor map is essential and correct:
\[
\Psi(x\otimes_Fy)=\phi(x)y,\qquad
\phi(xf)y=\phi(x)fy=\phi(x)(fy).
\]
This is a balanced biadditive map even when \(F\) is noncentral.
Applying it to \(u\otimes_F1=1\otimes_Fu\) gives \(1_U=0\), contrary to the premise.
The proof uses no cancellation by an element outside \(F\), so zero divisors in \(U\) cause no problem.
It uses an algebraic basis theorem with its usual choice principle and no topological continuity.
The equalizer statement itself needs neither Yin_C_F0031 nor Yin_C_F0034, and supplies neither the division-subring hypothesis nor the tensor equality for a later application.

## 5. Dependency and Version Disposition

The complete proofs justify the declared direct project edges: Yin_C_F0031-P1 is an input to Yin_C_F0034-P1; Yin_C_F0035-P1 has no project-claim input.
The affiliation infrastructure is an explicit accepted analytic input to Yin_C_F0034.
The Yin_C_F0029/Yin_C_F0013 links record extraction provenance and do not create a dependency on either parent theorem's conclusion.
There is no logical cycle.

Both lemma roles and the extraction were explicitly authorized in the recorded batch.
The artifact's candidate and pending-review labels record its authorship-time disposition; this separate review supplies mathematical acceptance for the exact versions identified above.
Selection of the current proof versions, claim-index promotion and review of any new consuming assembly remain the record owner's tasks.
Acceptance of these modules alone does not certify a consuming theorem's hypotheses or replace its assembly review.

No mathematical or domain correction is required.
This is an agent proof review with the prior roles and accepted-input boundaries stated above.
It is not external human review, proof-assistant verification, numerical verification or a historical novelty assessment.

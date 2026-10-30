---
author: Yin
---

# Adjoint-generated variant under unchanged hypotheses; not adopted

## Current assessment
[Selected decision](#decision-exact-finding-scope)

## Assessing the Adjoint-Generated Rationality Variant

<a id="statement"></a>

<a id="yin_c_f0003"></a>
## Yin_C_F0003: The Adjoint-Generated Variant under the Original Dual Hypotheses

Goal/context: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
On 2026-09-08 the user asked whether the normal-generator conjecture should use the division closure of C<X,X*>.
This is a considered modification, **not an adopted replacement** for [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001).

Provenance: **mixed**.
The statement is the user's proposed variation of Yin_C_F0001.
The normalized disk-Cauchy counterexample is independently calculated below and linked to the known construction in [Xia23](https://www.acsu.buffalo.edu/~jxia/Preprints/integv3.pdf), Example 1.6, through [Xia23-U001](../audits/literature/Xia23/Yin_U001_v1.md#xia23-u001).
Source history is recorded there; no novelty is claimed.

Current assessment: [selected assessment](#decision-exact-finding-scope).
The [complete adjoint-variant finding](../audits/reviews/Yin_R_F0002_v1.md#complete-adjoint-variant-finding) identifies the inspected revision and the exact scope of the counterexample.
Its reviewer had analyzed this same proposed modification, so the actual relationship is contributor self-review.

### Exact Variant Being Tested

Keep all quantifiers and hypotheses of Yin_C_F0001: a finite von Neumann algebra with faithful normal tracial state tau, tau(1)=1; a finite tuple of normal generators X with M=W*(X); the left representation on H=L2(M,tau); and bounded duals satisfying [D_i,X_j]=delta_ij P_Omega.
Replace only the rational algebra by

\[
A_X^*=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
\qquad R_X^*=\operatorname{Div}_M(A_X^*).
\]

The star on A_X^* and R_X^* is a label for the adjoint-generated version.
Division closure still uses finite scalar operations and inverses of elements invertible in M, not a topological closure or an affiliated algebra.

The proposed statement is, for every such setting, every such bounded dual system, and every f in M,

\[
f\in R_X^*
\quad\Longleftrightarrow\quad
\operatorname{rank}[D_i,f]<\infty\quad\text{for every }i.
\tag{Star}
\]

The counterexample below contradicts even the forward implication, with d=1 and f=X*.

### Why the Annotated Haar Example Does Not Require This Change

The [Yin_C_F0002 Haar example](Yin_C_F0002_v1.md#checked-boundary-example-one-haar-unitary) concerns the minimal closed derivative with core C[U].
It does not show that U^{-1} is missing from Div_M C[U].
In fact, for every unitary generator, U_j*=U_j^{-1} already belongs to the original division closure.
Hence

\[
\operatorname{Div}_M\mathbb C\langle U,U^*\rangle
=\operatorname{Div}_M\mathbb C\langle U\rangle.
\tag{Haar}
\]

To check this for a tuple, the original division closure contains every adjoint and therefore contains the adjoint-generated polynomial algebra and its division closure.
The reverse inclusion follows from the inclusion of polynomial algebras.
The same equality holds for selfadjoint tuples.

For a single Haar unitary, the Laurent polynomial core C[U,U^{-1}] is dense in L2, whereas C[U] spans only the nonnegative Fourier modes.
Changing that core addresses the specific density issue while leaving the rational algebra unchanged.
No claim that either core is a graph core for every desired derivative is made here.

### The Necessary Compatibility with Adjoints

For a fixed dual system, let

\[
S_D=\{f\in M:\operatorname{rank}[D_i,f]<\infty\text{ for all }i\}.
\]

The commutator product and inverse identities in [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002) show that S_D is a unital inverse-closed subalgebra of M containing X_1,...,X_d.
Consequently

\[
R_X^*\subseteq S_D
\quad\Longleftrightarrow\quad
[D_i,X_j^*]\text{ is finite rank for every }i,j.
\tag{Adj}
\]

Necessity follows by testing each X_j* in A_X*.
For sufficiency, S_D contains all generators and adjoints, hence A_X* and its division closure.
The original dual relation controls [D_i,X_j], not the diagonal adjoint commutators.
Normality does not supply the finite-rank conclusion in (Adj), as follows.

### Counterexample: Normal Multiplication on the Disk

Let B={z in C: |z|<1}, let mu=dA/pi be normalized planar area measure, and take

\[
M=L^\infty(B,\mu),\quad \tau(f)=\int_B f\,d\mu,
\quad H=L^2(B,\mu),\quad \Omega=1,
\quad (Xf)(z)=zf(z).
\tag{Setting}
\]

The trace is a faithful normal tracial state and tau(1)=1.
Multiplication by z is bounded and normal, its adjoint is multiplication by bar(z), and its measurable functional calculus generates all M because the coordinate z generates the Borel sigma algebra of B, modulo completion.

Define on bounded functions, and then extend to H,

\[
(Df)(z)=\int_B\frac{f(w)}{w-z}\,d\mu(w).
\tag{D}
\]

**Boundedness.** For fixed z in B,

\[
\int_B\frac{d\mu(w)}{|w-z|}
\leq\frac1\pi\int_{|u|<2}\frac{dA(u)}{|u|}=4.
\tag{Schur}
\]

The same bound holds with the variables exchanged.
Write k(z,w)=|w-z|^{-1}; weighted Cauchy-Schwarz gives

\[
|Df(z)|^2\leq4\int_B k(z,w)|f(w)|^2\,d\mu(w).
\]

After integrating in z, the column bound gives ||Df||_2^2 <= 16 ||f||_2^2.
Thus D extends uniquely to a bounded operator with norm at most 4.
The kernel is locally integrable; its value on the diagonal is irrelevant.
There is no principal-value or unbounded-domain assumption in this construction.

**Dual relation.** For bounded f, direct cancellation yields

\[
([D,X]f)(z)
=\int_B\frac{w-z}{w-z}f(w)\,d\mu(w)
=\tau(f)\,1=P_\Omega f.
\tag{Dual}
\]

Both sides are bounded operators, and bounded functions are dense in H, so (Dual) holds on all H.
This supplies every dual-system hypothesis in d=1.

**The adjoint commutator has infinite rank.** For each integer n>=0, polar integration gives

\[
D(\bar z^{\,n})=-\frac{\bar z^{\,n+1}}{n+1}.
\tag{Mom}
\]

Here is an explicit verification.
Fix nonzero z with |z|=r.
On a circle |w|=rho<r, expand 1/(w-z)=-sum_{k>=0} w^k/z^{k+1}.
After multiplication by bar(w)^n, the angular average retains only k=n and equals -rho^{2n}/z^{n+1}.
For rho>r, the expansion sum_{k>=0} z^k/w^{k+1} has no surviving angular term.
Integrating against 2 rho d rho therefore gives

\[
-\frac{2}{z^{n+1}}\int_0^r\rho^{2n+1}\,d\rho
=-\frac{\bar z^{n+1}}{n+1}.
\]

For every fixed radius unequal to r, the series converges uniformly in the angle.
Absolute integrability of the original kernel for these bounded inputs justifies Fubini; the exceptional radius has measure zero.
At z=0 the angular average is directly zero, consistent with (Mom).

Applying (Mom) twice gives

\[
\boxed{
[D,X^*](\bar z^{\,n})
=\frac{\bar z^{\,n+2}}{(n+1)(n+2)},\qquad n\geq0.
}
\tag{Inf}
\]

These images are nonzero and pairwise orthogonal by angular integration.
Thus the range contains infinitely many linearly independent vectors and [D,X*] has infinite rank.
Its integral kernel is (bar(w)-bar(z))/(w-z), of modulus one off the diagonal, so it is nevertheless Hilbert-Schmidt.
This last observation distinguishes finite rank from Hilbert-Schmidt membership; only infinite rank is needed to contradict (Star).

Finally f=X* is already a generator of A_X*, hence belongs to R_X*.
Together with (Dual) and (Inf), this refutes (Star) while satisfying every retained hypothesis.
The conclusion does not address membership of X* in the original holomorphic R_X and does not refute Yin_C_F0001.

### What a Different Adjoint-Compatible Question Would Require

The following are possible future scopes, not new adopted goals or proved converse statements:

- If each X_j* already belongs to R_X, then the two division closures coincide by the same inclusion argument as (Haar).
  This includes selfadjoint and unitary generators.
  No change of rationality statement is needed in that situation.
- If the adjoint-generated algebra is desired for more general normal tuples, add the explicit hypothesis in (Adj).
  It is exactly what the revised forward implication requires.
  Whether the converse then holds is a different unresolved question; the extra hypothesis cannot be silently added to Yin_C_F0001.

One also cannot prescribe X and X* as independent free coordinates.
If T satisfied [T,X]=P and [T,X*]=0 for a normal X, commuting T with XX*-X*X=0 would give [P,X*]=0.
Applying this to Omega gives X*Omega=tau(X*)Omega, so faithfulness makes X scalar, contradicting [T,X]=P.
This observation only concerns that incompatible independent-coordinate prescription; it does not rule out derivations respecting the normal relation.

### Verification and Scope

The counterexample uses only the displayed norm estimate, bounded commutator calculation, polar integration, and orthogonality.
The stronger trace-class failure in the literature is not an input to this proof.
Yin_C_F0001's statement and Yin_C_F0002's audited proof remain unchanged.
The [proof-audit index](../audits/reviews/index.md) locates the separate review of this proposed modification.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | refuted |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#counterexample-normal-multiplication-on-the-disk) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0002_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision exact-finding-scope

Select the actual old mathematical finding through its precise current locator and truthful relationship.
The original inspection dates, proof, statement, negative findings and source limits remain unchanged; this is no new mathematical review.

| Field | Value |
| --- | --- |
| date | 2026-10-20T22:16 |
| status | refuted |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#counterexample-normal-multiplication-on-the-disk) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact complete finding](../audits/reviews/Yin_R_F0002_v1.md#complete-adjoint-variant-finding) | Actual whole 2026-09-08 contributor self-review of the exact proposed adjoint variant, disk counterexample, polar/Fubini argument, adjoint compatibility and future-scope limits; original normal hypotheses and refuted statement remain unchanged. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | refuted |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0002_v1.md).

Material covered by that review: [Exact material](Yin_C_F0003_v1.md).

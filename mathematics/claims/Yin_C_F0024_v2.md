---
author: Yin
---

# Normal-tuple affiliated criterion: proof through conjugate-variable certificates

Recorded at 2026-10-15T11:28.
Authoring agent: root.
This version retains a complete alternative proof of the original criterion and its full-natural-domain refinement.
The new step identifies an abstract finite-rank certificate with the supplied operators by clearing its tensor factors.
No independent review of this new proof is asserted.

The original statement, selected P2 proof and original assessment history remain those of v1.
P1 and P2 remain intact there.
The P3 argument below is an alternative candidate, locally self-checked at that checkpoint; it does not inherit the independent reviews of P1/P2 or change the selected Claim decision.
This describes the original 2026-10-15 checkpoint.
The later [independent P3 finding](../audits/reviews/Yin_R_F0067_v1.md#fresh-v2-p3) records its own complete inspection at 2026-10-22T20:14.
The current selected Claim decision still uses the unchanged v1 P2 and Section 7; that separate P3 inspection neither changes this choice nor broadens either review's checked inputs.


## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Unchanged criterion and sign conversion

<a id="statement"></a>

The authoritative statement is [v1, Section 1](Yin_C_F0024_v1.md#yin_c_f0024), including its three numbered conclusions and the interpretation of initially larger domains.
In that statement the supplied maps satisfy [D_i,X_j]=delta_ij P_Omega.
Write E_i=-D_i so that [X_j,E_i]=delta_ij P_Omega.
This sign change preserves domains, adjoint domains, finite rank and all rationality conclusions.

For the proof and its natural-domain refinement, let (M,tau) be finite tracial with faithful trace, H=L2(M,tau), Omega=1, and let X_1,...,X_d be bounded normal generators of M.
Let E_i be densely defined linear operators with M Omega contained in Dom E_i and Dom E_i^*, satisfying [X_j,E_i]=delta_ij P_Omega on M Omega.
For u in U=L0(M) and a fraction pair Q=(s,a,b,t), put
\[
 G_i(Q):=sE_i b-aE_i t
\]
on its natural domain {eta: b eta,t eta in Dom E_i}.
We prove that rationality of u in X is equivalent to finite rank of every G_i(Q), and to their closures being bounded finite-rank operators, for each Q.
The rank is independent of Q when finite.
For the original v1 operators on exactly M Omega this gives its finite-defect criterion.
Its bounded-element full-closure conclusion is proved in Section 5 below.

<a id="yin_c_f0024-p3"></a>
## Argument P3

### 1. Inputs and dependency boundaries

- [C_F0070 Parts A and C](Yin_C_F0070_v1.md#statement) give the actual starred derivations and vacuum adjoints from the all-M dual and adjoint hypotheses.
  Their closable special case also follows directly from the spectral-partition argument of [C_F0037](Yin_C_F0037_v1.md#yin_c_f0037-p1).
  This use depends only on operator hypotheses, not on the rationality conclusion being proved.
- [C_F0063 Sections 1--4 and Appendix A](Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion), with the starred-derivation interface of [C_F0025](Yin_C_F0025_v1.md#2-normalization-and-the-exact-acsy24-interface), supplies finite-rank certificates for every fraction under the conjugate-variable condition.
  For the present sign, the certificate is sum_i[rho(X_i),T_i]=sP_Omega b-aP_Omega t.
  Its rationality converse follows from [C_F0068 Part A, Sections 2--3](Yin_C_F0068_v1.md#argument), under maximal Delta.
  No assertion identifying T_i with a raw E_i-expression is imported.
- [C_F0068 Sections 2--3](Yin_C_F0068_v1.md#argument) supplies finite-family denominator clearing and the algebraic tensor/finite-rank correspondence.
  Its Part C rationality proof is not used.
- [C_F0033-P1](Yin_C_F0033_v1.md#yin_c_f0033-p1) supplies the fundamental identity on M Omega when the actual fraction commutators have bounded finite-rank extensions, with the sign changed as above.
- [C_F0031](Yin_C_F0031_v1.md) supplies the finite-rank closure fact.
  The direct adjoint test below gives closability on the full natural domain, as in [C_F0068 Section 5.4](Yin_C_F0068_v1.md#54-full-natural-domains-and-bounded-element-graph-invariance).
- ACSY24 Proposition 3.5 gives maximal Delta from the starred derivations and actual vacuum adjoints.
  [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) records that interface.
  The free-field conclusion then follows from the accepted [MSY23 interface](../audits/literature/MSY23/Yin_U004.md#msy23-u004).

In particular, the forward proof uses the existence of abstract finite-rank certificates, not the old sum/product/inverse proof for the actual fraction commutators.

### 2. A finite-rank certificate is the actual fraction commutator

This step needs neither normality nor generation once a certificate is supplied.
Assume the all-M domain and adjoint-domain conditions and the generator dual relations above, and suppose T_i in F(H) satisfy
\[
 \sum_j[\rho(X_j),T_j]=sP_\Omega b-aP_\Omega t.
\]
Use Theta(v tensor w^op)eta=v< Jw,eta> and put ell_i=-Theta^{-1}(T_i) in H tensor_alg H.
The tensor/commutator identity gives
\[
 \sum_j\Psi_j(\ell_j)=a\otimes t^{op}-s\otimes b^{op},
 \qquad
 \Psi_j(k)=k(X_j\otimes1-1\otimes X_j^{op}).
\]
Choose regular r,q in M clearing every tensor factor, so
\[
 m_j:=(r\otimes q^{op})\ell_j\in M\otimes_{\mathbb C}M^{op}.
\]
Then
\[
 \sum_j\Psi_j(m_j)
   =ra\otimes(tq)^{op}-rs\otimes(bq)^{op}.
\]
For fixed i and xi in M Omega, the rule
\[
 c\otimes e^{op}\longmapsto cE_i(e\xi)
\]
defines a complex-linear map on the bounded algebraic tensor product: its simple-tensor rule is bilinear and every input of E_i lies in M Omega.
On a difference tensor its value is
\[
 cX_jE_i(e\xi)-cE_i(X_je\xi)
   =\delta_{ij}cP_\Omega e\xi.
\]
Applying the map to the cleared equation gives
\[
 -rG_i(Q)q\xi=\Theta(m_i)\xi=-rT_iq\xi.
\]
The last equality uses Theta((r tensor q^op)ell)=rTheta(ell)q.
Injectivity of r therefore gives G_i(Q)=T_i on qM Omega, which is dense in H.

The full natural domain contains M Omega.
For eta in M Omega and z in that natural domain,
\[
 \langle\eta,G_i(Q)z\rangle
  =\langle b^*E_i^*(s^*\eta)-t^*E_i^*(a^*\eta),z\rangle.
\]
Thus M Omega lies in Dom G_i(Q)^*, proving closability.
Agreement with the bounded T_i on the dense space qM Omega means graph(T_i) is contained in graph(closure(G_i(Q))).
Since T_i is defined on all H, the inclusion is equality.
Hence
\[
 \overline{G_i(Q)}=T_i.
\]
In particular, G_i(Q) equals T_i on its entire natural domain, not just on M Omega.
No closability of cE_i e on an unspecified domain, simultaneous graph approximation of b z and t z, or boundedness of E_i on H is assumed.

### 3. Equivalence for every fraction

By the normal-conjugate input, the actual starred derivation condition holds.
ACSY24 gives Delta(X)=d and the accepted MSY23 result gives the free-field conclusion.

If u is rational, the every-fraction certificate input gives T_i for the specified Q.
Section 2 identifies their values with closure(G_i(Q)), proving both finite-rank conditions.
Conversely, if every G_i(Q) has finite rank, the adjoint test and the finite-rank closure fact give bounded finite-rank closures.
If these closures are supplied directly, the fundamental identity of C_F0033 gives
\[
 \sum_i[\rho(X_i),\overline{G_i(Q)}]
      =sP_\Omega b-aP_\Omega t.
\]
The certificate converse yields rationality.
This works for every Q, proving the some/every assertion without using the old fraction-algebra closure proof.

For a finite-rank bounded T, restriction to a dense linear domain has the same range: the restricted range is a dense linear subspace of the finite-dimensional range of T and hence is all of it.
This identifies the numerical ranks of G_i(Q) and its closure.

### 4. Coordinate ranks

For Q=(s,a,b,t) and Q'=(s',a',b',t') representing the same rational u, choose regular x,y,p,q with xs=ys' and tp=t'q.
Then xa=ya' and bp=b'q, so on M Omega
\[
 xG_i(Q)p=yG_i(Q')q.
\]
Both closures are bounded, so the identity extends to H.
Injectivity of the regular left multipliers and density of the ranges of the regular right multipliers preserve finite rank.
The two coordinate ranks are therefore equal.

### 5. Original v1 bounded-element conclusion

Take the original maps on exactly M Omega and let widehat E_i be their closures.
For f in M, the trivial fraction gives the finite-rank criterion for [E_i,f] on M Omega.
Let T_i be its bounded finite-rank extension.
Since M Omega is a graph core of widehat E_i by definition, approximate xi in Dom widehat E_i by xi_n in M Omega with xi_n -> xi and E_i xi_n -> widehat E_i xi.
Then
\[
 E_i(f\xi_n)=fE_i\xi_n+T_i\xi_n
   \longrightarrow f\widehat E_i\xi+T_i\xi,
 \qquad f\xi_n\longrightarrow f\xi.
\]
Closedness gives f xi in Dom widehat E_i and [widehat E_i,f]xi=T_i xi.
Restriction gives the converse.
Returning to D_i=-E_i proves all three original numbered conclusions.
No conclusion about an arbitrary larger closed extension replaces the closure of the original restriction.

<a id="assessment-and-manuscript-use"></a>
## Assessment and proof scope

Disposition: alternative candidate P3; complete local mathematical self-check, no separate independent review.
Checked both tensor signs, the opposite-factor multiplication order, all domains in the applied tensor map, density after regular multiplication, the graph inclusion on the full natural domain, the fundamental-identity hypotheses, rank preservation and the original graph-core conclusion.
The direct certificate-realization calculation in Section 2 is the additional argument retained by this version.
Prior P1/P2 decisions and reviews are unchanged.

This file introduces no new Task, changes no theorem designation and does not close or reopen a research objective.

## Assessment history

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:49 |
| status | proved |
| authority | Explicit user instruction on 2026-10-10 to designate C_F0024 as Theorem. |
| reason | Retain the unchanged proved theorem and explicit user-authorized role, selecting the exact assembly/original Section 7/recheck findings with their actual individual relationships. The R123 context-isolation fact remains unknown; no whole-Claim independent classification or new mathematical review is asserted. |

Role designation: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](Yin_C_F0024_v1.md#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](Yin_C_F0024_v1.md#yin_c_f0024-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact argument](Yin_C_F0024_v1.md#7-automatic-corollaries-and-optional-normalization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact dependency](Yin_C_F0029_v1.md#decision-candidate-0002) | Selected P2 specialization: E=V_i=M. |
| review | [Actual finding](../audits/reviews/Yin_R_F0012_v1.md#criterion-assembly-finding) | Complete unchanged statement/P2 specialization E=V_i=M, with original auxiliary Section 7 separately covered below. |
| review | [Actual finding](../audits/reviews/Yin_R_F0013_v1.md#normal-common-domain-finding) | Original complete P1 principal finding remains applicable to unchanged statement and selected Section 7 automatic corollaries/optional normalization, at its original accepted-input depths. |
| review | [Actual finding](../audits/reviews/Yin_R_F0013_v1.md#complementary-common-domain-finding) | Original complementary whole-artifact/final-revision finding for the same unchanged statement and selected Section 7, preserving its disclosed mathematical contribution. |
| review | [Actual finding](../audits/reviews/Yin_R_F0067_v1.md#conclusion) | Actual 2026-10-10 statement/P2/Section 7 recheck, exact bindings retained and initial context-isolation relationship genuinely unestablished. |

### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| authority | Explicit user instruction on 2026-10-10 to designate C_F0024 as Theorem. |
| reason | Adopt the actual new isolated review of the unchanged v1 statement, selected P2 and Section 7; preserve the authorized theorem role, original source boundaries and historical contributor/unknown findings. |

Role designation: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](Yin_C_F0024_v1.md#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](Yin_C_F0024_v1.md#yin_c_f0024-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact argument](Yin_C_F0024_v1.md#7-automatic-corollaries-and-optional-normalization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact dependency](Yin_C_F0029_v1.md#decision-candidate-0002) | Selected P2 specialization: E=V_i=M. |
| review | [New selected-proof finding](../audits/reviews/Yin_R_F0067_v1.md#fresh-selected-v1) | Actual isolated whole selected v1 statement/P2/Section 7 inspection at its exact domain and accepted-input boundaries; the separate v2 P3 inspection does not replace this proof selection. |

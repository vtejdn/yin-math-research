---
author: Yin
---

# Free marginal infinity-to-2 estimates restore both original all-M dual domains

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Lifting marginal polynomial-core estimates through a free product

<a id="statement"></a>
<a id="yin_c_f0045"></a>

Date/actor: 2026-09-11, another AI agent.
Consumer: the separate normal-domain investigation.
Record kind: complete conditional proof candidate and geometric application, initially awaiting independent review.
No Claim ID, Role or shared index is assigned.
The argument concerns the original starred polynomial domains; the unstarred rational algebra is unchanged.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0045** after [complete independent review](../audits/reviews/Yin_R_F0023_v1.md).
Freeness lifts a single marginal infinity-to-2 estimate to both original all-M domains, with the quantitative constants below.
This includes the Yin_C_F0044 geometric marginal class and restores the original unstarred affiliated criterion.
This assessment supersedes the initial pending label; arbitrary marginal estimates and correlated normal tuples remain unresolved.
The selected external inequality is indexed in [Pis12-U001](../audits/literature/Pis12/Yin_U001_v1.md#pis12-u001).
No Role or lemma extraction is assigned.

## 1. Exact statement

Use precisely the hypotheses and conventions of [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025).
In particular, X=(X_1,...,X_d) is a finite bounded normal generating tuple in a finite tracial von Neumann algebra (M,tau), H=L2(M,tau), and the original D_(j,0) have domain exactly

\[
 \mathcal P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle.
\]

They have the vacuum-adjoint condition, the rank-one unstarred generator commutators, and compact bounded starred-generator commutators required there.
Let D_j be their original Hilbert closures.
Normalize on the same core:

\[
 \eta_j=D_{j,0}1,\qquad E_{j,0}p=D_{j,0}p-p\eta_j,
 \qquad \xi_j=E_{j,0}^*1.                       \tag{1}
\]

Add the hypothesis that the abelian coordinate algebras B_j=W*(X_j) are freely independent.
Put H_j=L2(B_j), P_j=C[X_j,X_j*], and let e_j=E_(j,0)|P_j.
Yin_C_F0025's canonical divided difference makes e_j take values in H_j.
Suppose, for every j, there is a finite a_j such that

\[
                     \|e_j b\|_2\le a_j\|b\|_\infty
                     \qquad(b\in P_j).          \tag{2}
\]

Then

\[
                M\subseteq\bigcap_j
                  \bigl(\operatorname{Dom}D_j
                       \cap\operatorname{Dom}D_{j,0}^*\bigr).
                                                     \tag{3}
\]

These are the original closures and actual Hilbert adjoints.
A separate marginal adjoint bound is not required.
With k_C=4/pi, the squared constant in the complex little Grothendieck inequality (6), the proof gives on P and then on M

\[
 \begin{split}
 \|D_j f\|_2&\le
       (\sqrt{k_C}\,a_j+\|\eta_j\|_2)\|f\|_\infty,\\
 \|D_{j,0}^* f\|_2&\le
       \bigl(\sqrt{k_C}(a_j+\|\xi_j\|_2)
                           +\|\eta_j\|_2\bigr)\|f\|_\infty.
 \end{split}                                      \tag{4}
\]

The constants do not depend on the length of a mixed polynomial or the number of reduced-word coefficients used to represent it.
For a fixed j only (2) for that j is needed for its two bounds.

## 2. Reuse and the remaining imported functional-analytic input

The local reuse check read Yin_C_F0025's canonical normalization and normal phase kernel, [Yin_C_F0044](Yin_C_F0044_v1.md#yin_c_f0044) and its exact infinity-to-2 estimate, [Yin_C_F0043's original-operator graph restoration](Yin_C_F0043_v1.md#7-restoring-the-original-operators-and-their-adjoints), and [Voi98-U005](../audits/literature/Voi98/Yin_U005_v1.md#voi98-u005), especially its reconstruction of the free-product Hilbert space and right end actions in Sections 5.5-5.8.
The latter audit already separates the correct right lift from the invalid compressed formula in the source.
The currently used action is a right end action, and is checked directly on the full polynomial core below.

The additional standard input is the complex little Grothendieck theorem.
In the exact form needed, if K is compact and T:C(K)->H_0 is a bounded complex-linear map to a complex Hilbert space, then every finite family (b_r) in C(K) satisfies

\[
 \sum_r\|Tb_r\|_{H_0}^{2}
       \le k_C\|T\|^2
                 \left\|\sum_r |b_r|^2\right\|_{C(K)}.
                                                     \tag{6}
\]

The exact primary input is Gilles Pisier, *Grothendieck's theorem, past and present*, [arXiv:1101.4195](https://arxiv.org/abs/1101.4195), Section 5: equation (5.2), printed p.20 / PDF p.22, gives k_C=4/pi; Theorem 5.2(ii), printed p.21 / PDF p.23, gives (6).
The theorem's short proof on printed p.22 / PDF p.24 was also read in the independent source check by another AI agent.
The [PDF endpoint](https://arxiv.org/pdf/1101.4195) supplied an 87-page artifact whose arXiv margin says v3, 2011-06-04, while its title page displays 2024-11-26.
These are recorded version observations, not an assertion that the supplied bytes are unchanged since 2011.
The distinct 83-page January 2011 author-site manuscript is not used for these page numbers.
Published metadata are *Bulletin of the American Mathematical Society* 49 (2012), 237-323, [DOI 10.1090/S0273-0979-2011-01348-9](https://doi.org/10.1090/S0273-0979-2011-01348-9); shared bibliography registration is left to root.

This is the commutative theorem for arbitrary bounded complex-linear T; there is no normality or complete-boundedness premise.
It is not the projective-tensor injectivity statement previously imported from Haa85.
The factorization measure in the equivalent statement need not equal the spectral measure here; using the finite-family formulation (6) avoids any such identification.
Earlier Grothendieck foundations remain accepted external results, not newly audited full proofs.

## 3. An orthogonal right-module decomposition of the full core

For each k choose an orthonormal basis (a_(k,n)) of H_k minus C1 consisting of bounded centered starred polynomials, with algebraic span equal to the centered part of P_k.
Such a basis is obtained by Gram-Schmidt from an enumeration of the scalar starred monomials, dropping linearly dependent terms.
Each polynomial is reached after finitely many terms, so its expansion is finite.
The polynomial star algebra is L2 dense because it generates B_k; each basis vector is bounded.

Fix j.
Let U_j consist of 1 and all reduced products u=a_(i_1,n_1)...a_(i_m,n_m), where adjacent i's differ and i_m is different from j.
The free-product Hilbert model gives a unitary

\[
 V_j:\ell^2(U_j)\otimes_2 H_j\longrightarrow H,
                \delta_u\otimes b\longmapsto ub.      \tag{7}
\]

Here u is an actual bounded polynomial, and its left multiplication acts on every b in H_j.
To check (7), split b into its scalar and centered parts.
Since u ends outside j, its centered part is appended as a reduced tensor and its scalar part leaves u unchanged.
The resulting reduced tensors are an orthonormal basis of H, each occurring exactly once.
The case u=1 includes both the vacuum and the one-factor j summand.

Let E_(B_j):M->B_j be the trace-preserving conditional expectation.
The isometry in (7), paired against a,b in P_j and then using their L2 density, implies the stronger module identity

\[
             E_{B_j}(u^*v)=\delta_{u,v}1
                         \qquad(u,v\in U_j).          \tag{8}
\]

Indeed the scalar tests are tau(a* E_(B_j)(u*v)b)=delta_(u,v) tau(a*b); faithfulness determines the bounded B_j element.
This is a consequence of the free-product representation, not an assertion that u itself is a unitary.

Every polynomial p in P has a unique finite expression

\[
        p=\sum_{u\in F}u b_u,
        \quad b_u\in P_j,
        \quad b_u=E_{B_j}(u^*p),                      \tag{9}
\]

where F is finite.
To see algebraic finiteness, first expand p into reduced products of centered factor polynomials.
Expand each such polynomial in its finite basis expansion, and group the final j-factor, if any, as b_u.
The constant 1 supplies the final factor for words not ending in j.
In particular, (7) identifies the **entire original core** P with the algebraic direct sum of copies of P_j, not merely with a smaller test domain.

Expanding p*p and using (8) gives

\[
                 E_{B_j}(p^*p)=\sum_{u\in F}b_u^*b_u,
 \qquad
          \left\|\sum_{u\in F}|b_u|^2\right\|_\infty
                                  \le\|p\|_\infty^2. \tag{10}
\]

The more general finite-subfamily Bessel inequality is obtained by subtracting that partial sum before applying the positive conditional expectation.
For the finite full polynomial expansion, equality holds in the first part of (10).

## 4. The canonical normalized derivative is the marginal right lift

Yin_C_F0025 supplies the coarse derivations partial_j on P and

\[
                E_{j,0}p=(\mathrm{id}\otimes\tau)\partial_jp.
                                                     \tag{11}
\]

For k different from j, partial_j kills P_k, including its adjoints.
On P_j it takes values in H_j tensor_2 H_j and is the scalar divided difference

\[
          \partial_j b(z,w)=\frac{b(z)-b(w)}{z-w}.     \tag{12}
\]

Consider u b in (9).
In the Leibniz expansion of partial_j(u b), a cut at an earlier j-letter of u has a nonempty suffix c which starts and ends in factors different from j: the last factor of u is not j and adjacent reduced factors differ.
The suffix c is reduced, so E_(B_j)(c)=0 and hence E_(B_j)(c b)=0.
For every y in H_j,

\[
                       \tau(y c b)=0.                \tag{13}
\]

This identity follows by the conditional-expectation pairing, first for bounded y and then by L2 approximation.
It annihilates the contracted second leg of that cut.
The derivative tensor in (12) need not be algebraic: the bounded functional y->tau(ycb) vanishes on all of H_j, so the argument applies to its Hilbert tensor completion as well.
The preceding prefix is a bounded multiplier and does not alter the conclusion.

Only the final factor survives the contraction.
Therefore, including the vacuum and b=1 cases,

\[
                    E_{j,0}(u b)=u e_j b,
 \qquad
 V_j^* E_{j,0} V_j
              =\bigoplus_{u\in U_j}^{\mathrm{alg}} e_j
 \quad\hbox{on }\bigoplus_{u\in U_j}^{\mathrm{alg}}P_j.
                                                     \tag{14}
\]

No freeness assertion concerning arbitrary unrelated bounded coefficients is inserted: (13) uses precisely the reduced polynomial factors from (9).

## 5. Actual adjoints and the marginal vacuum vector

The operator e_j is closable, since it is the restriction of the closable E_(j,0) to the reducing coordinate copy in (14).
Testing a vector against the finite supported polynomial domain in (14) gives the exact adjoint formula

\[
 \begin{split}
 V_j^* E_{j,0}^* V_j&=\bigoplus_{u\in U_j} e_j^*,\\
 \operatorname{Dom}\!\left(\bigoplus_u e_j^*\right)
 &=\left\{(h_u):h_u\in\operatorname{Dom}e_j^*,\quad
                    \sum_u(\|h_u\|_2^2+\|e_j^*h_u\|_2^2)<\infty\right\}.
 \end{split}                                       \tag{15}
\]

For clarity, testing only one coordinate forces each h_u into the marginal adjoint domain.
Boundedness of the functional on all finite supported inputs is equivalent, by the Hilbert direct-sum norm, to square summability of their adjoint images.
This proves both directions of (15).
The closure of E_(j,0) is likewise the direct sum of the closures of e_j: finite coordinate truncation followed by marginal graph approximation proves the core assertion.
No assumption that P is a core for E_(j,0)* or D_(j,0)* is made.

The vacuum corresponds in (7) to the single coordinate delta_1 tensor 1.
Equation (15) and Yin_C_F0025's vacuum-adjoint condition therefore give

\[
                     \xi_j=e_j^*1\in H_j.             \tag{16}
\]

This assertion concerns the normalized xi_j.
The original D_(j,0)*1=xi_j+eta_j* need not belong to H_j.

On P_j the kernel (12) is symmetric in z,w.
The actual polynomial-adjoint identity from Yin_C_F0025, equivalently [Yin_C_F0044 equation (16)](Yin_C_F0044_v1.md#5-original-adjoints-and-actual-coordinate-domains), becomes

\[
           e_j^* b=b\xi_j-J_j e_j J_j b,
           \qquad J_j b=b^*.                         \tag{17}
\]

Both sides take values in H_j.
This gives from (2)

\[
               \|e_j^* b\|_2
                  \le(a_j+\|\xi_j\|_2)\|b\|_\infty
                  \qquad(b\in P_j).                 \tag{18}
\]

For p as in (9), (15) consequently says E_(j,0)*p=sum_u u e_j* b_u.
This is the actual global adjoint on the full original core, not the adjoint of its coordinate restriction silently substituted in its place.

## 6. The mixed-word estimates

By norm density, (2) extends e_j uniquely to a bounded linear map T_j:C*(X_j)->H_j with norm at most a_j.
Equation (18) independently extends e_j*|P_j to a bounded map T'_j with norm at most a_j+||xi_j||_2.
These extensions are used only as Banach-space maps for (6); they are not replacements for the closed Hilbert operators in (14)-(15).

The coordinate C*-algebra is C(sigma(X_j)) because X_j is normal.
Its norm agrees with its norm in B_j, so no distinction between essential and pointwise suprema affects (10).
Apply (6) to the finite family (b_u), and then (10), to obtain

\[
 \begin{split}
 \|E_{j,0}p\|_2^2
      &=\sum_u\|e_j b_u\|_2^2
         \le k_Ca_j^2\|p\|_\infty^2,\\
 \|E_{j,0}^*p\|_2^2
      &=\sum_u\|e_j^*b_u\|_2^2
         \le k_C(a_j+\|\xi_j\|_2)^2\|p\|_\infty^2.
 \end{split}                                       \tag{19}
\]

Commutativity of B_j is used in this precise column-square estimate.
No claim about arbitrary noncommutative factors follows from this application of the commutative theorem.

On P the original adjoint normalization is exact:

\[
       D_{j,0}p=E_{j,0}p+p\eta_j,
       \qquad D_{j,0}^*p=E_{j,0}^*p+p\eta_j^*.        \tag{20}
\]

Since ||p eta_j||_2 and ||p eta_j*||_2 are at most ||p||_infinity ||eta_j||_2, equations (19)-(20) prove the two original bounds (4) on P.
The right multiplier eta_j may be an arbitrary mixed L2 vector.
The proof does not assert that a sum of the two closed unbounded operators has the desired closure.

## 7. Restoring the original all-M domains and rationality interface

For f in M, bounded strong-star density and norm approximation in C*(X) give polynomial p_n converging to f in L2 with a uniform operator-norm bound.
One can take this bound arbitrarily close to ||f||_infinity.
The estimates (4) bound D_(j,0)p_n and D_(j,0)*p_n in H.
Select weakly convergent graph subsequences.
The graphs of the original closure D_j and the actual closed adjoint D_(j,0)* are closed linear subspaces of H direct-sum H, hence weakly closed.
Their limiting first coordinate is f.
This proves (3).
The uniqueness of the values and lower semicontinuity of the norm give (4) on M with the stated constants.
Separability holds because the tuple is finite; alternatively the same argument uses weakly convergent subnets.

Uniformly bounded L2-convergent input sequences in M have weakly convergent operator images, by the same bounds and adjoint pairing, as in Yin_C_F0024.
Applying this to the polynomial generator identities gives

\[
              D_j(X_k f)-X_kD_j f=\delta_{jk}\tau(f)1
                       \qquad(f\in M).               \tag{21}
\]

Restrict D_j to M.
Its closure is still the original D_j: it contains D_(j,0) and is contained in the closed D_j, so taking closures gives equality in both directions.
Its Hilbert adjoint is therefore still D_(j,0)*.
Thus [Yin_C_F0024](Yin_C_F0024_v1.md#yin_c_f0024) applies to these original operators and their all-M restrictions.

In particular the affiliated finite-rank criterion is restored with

\[
 \mathcal A_X=\mathbb C\langle X_1,\ldots,X_d\rangle,
 \qquad \operatorname{Div}_{L^0(M)}\mathcal A_X\cap M.
\]

Yin_C_F0025's bounded finite-rank weak-form condition becomes equivalent to membership in this intersection: its original implication remains valid, and the converse now follows from Yin_C_F0024 on M and restriction to P.
The all-M actual commutator criterion also follows exactly as in Yin_C_F0024.
No equality with Div_M(A_X) is asserted.

## 8. The geometric free-normal application and scope boundary

Assume the marginal spectral probabilities mu_j are compactly supported, have linear growth mu_j(B(z,r))<=L_j r, and finite total Menger curvature c^2(mu_j).
[Yin_C_F0044 Sections 3-5](Yin_C_F0044_v1.md#3-the-selected-primary-source-interface) then supply (2).
In its notation one may take

\[
 A_j=(c^2(\mu_j)+a L_j^2)^{1/2},\quad
 K_j=2(\sqrt{27}+2)A_j,\quad a_j=A_j+K_j,           \tag{22}
\]

where a is the absolute constant in the retained Tol17 curvature identity.
Hence all freely independent normal tuples with these marginals and the exact original Yin_C_F0025 hypotheses satisfy (3), not merely the coordinate-algebra inclusions proved in Yin_C_F0044.
Neither analytic parametrization nor selfadjointness is needed.

The geometric example need not assume existence without justification.
Yin_C_F0044 constructs the scalar canonical divided differences and their L2 vacuum adjoints for each such measure.
Extend those scalar derivations to the algebraic free product of the P_j, with zero derivatives on the other factors and the outer Leibniz rule.
The faithful free-product Hilbert representation identifies that algebra with the actual starred polynomial algebra.
The same calculation (14)-(16) gives an L2 global vacuum adjoint.
Moreover contraction and the Leibniz rule give [E_(j,0),a]=Theta(partial_j a) on P.
In particular [E_(j,0),X_k]=delta_(j,k)P and the starred commutator is either zero or the Hilbert-Schmidt normal phase kernel supported on H_j.
These are precisely the compact-core conditions of Yin_C_F0025.
Thus the construction gives actual canonical examples, and (20) allows arbitrary original right-multiplier normalizations compatible with that core.

The proof resolves a free-product lifting interface, not the unrestricted normal-domain question.
The marginal hypothesis (2) has not been proved automatic from bare Yin_C_F0025 for every normal spectral measure.
Yin_C_F0044 already shows linear growth itself is not automatic.
For correlated normal tuples, the right-module decomposition and vanishing of earlier cuts used in (13) are unavailable, so no conclusion for that remaining joint-distribution problem follows.

Review should verify the full-core identity (9), conditional expectation in (13) with completed derivative tensors, the actual direct-sum adjoint domain (15), the normalization distinction in (16)/(20), the exact complex source inequality (6), and the use of weak graphs of the original operators in Section 7.
The original frozen Yin_C_F0044 and Yin_C_F0043 proofs are not rewritten or replaced by this record.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0023_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:45 |
| status | proved |
| reason | Adopt the exact original finding at its actual self-reviewed relationship. Preserve the mathematical status, statement, selected proof, dependencies and all historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0023_v1.md#outcome) | Whole conditional free-product lifting proof and geometric applications; the reviewer proposed the substantive right-module/little-Grothendieck route before author development. Original polynomial core, both actual adjoints, constants, graph recovery and accepted inputs retained. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0023_v1.md).

Material covered by that review: [Exact material](Yin_C_F0045_v1.md).

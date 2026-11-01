---
author: Yin
---
# An exact actual-vacuum criterion for measurable Hermitian Gaussian kernels

Human author: Yin.
Root proposed the exact equivalence and measurable phase reduction after the positive-kernel theorem.
The normal branch verified the phase unitary, the zero-kernel obstruction and the sufficiency construction without supplied target derivations.
These are development contributions, not independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let Z be bounded normal, with diffuse compact spectral law mu in N=W*(Z), a finite abelian tracial algebra with faithful normal probability trace.
Let S be standard semicircular free from N and let M=W*(N,S).
Let a be an essentially bounded measurable Hermitian kernel,

\[
 a(v,z)=\overline{a(z,v)}\quad\mu^2\text{-almost everywhere}.
\]

Write b=|a|.
The bounded selfadjoint Gaussian element T_a has first relative S-chaos vector a and norm at most 2||a||infinity, as constructed in C_F0156.
Set M_a=W*(Z,T_a), with its restricted trace.
The following are equivalent:

1. The normal pair (Z,T_a) satisfies the actual starred ACSY condition A on its original target core C<Z,Z*,T_a>, with intrinsic coefficient space L2(M_a) tensor_2 L2(M_a).
2. The pair admits densely defined generator-first duals D_Z,D_T on L2(M_a) whose domains and actual adjoint domains contain all M_a Omega and whose coordinate commutators hold there, namely the strong condition S.
3. The scalar divided-difference derivation on C[Z,Z*] has an actual vacuum xi_N in L2(N), b is nonzero mu squared almost everywhere, and

\[
 \iint b(z,v)^{-2}\,d\mu(z)d\mu(v)<\infty,
 \tag{1}
\]
\[
 \iiint
 \frac{|b(w,v)/b(z,w)-b(z,w)/b(w,v)|^2}{|z-v|^2}
                  \,d\mu(z)d\mu(w)d\mu(v)<\infty.
 \tag{2}
\]

The ratios in (2) are defined on their full-measure nonzero set, and the endpoint diagonal is null by diffuseness.
Under these conditions M_a=M.
Both original canonical target closures and their actual adjoints contain all bounded vectors.
In particular the conditions imply bare F; no converse from bare F is asserted.

For b positive, the actual vacua are xi_N+chi_b and Psi(1/b), where chi_b is the H_2 kernel

\[
 \chi_b(z,w,v)
  =\frac{b(w,v)/b(z,w)-b(z,w)/b(w,v)}{\bar z-\bar v}.
\]

For general a put theta=a/b off its zero set and theta=1 on that set.
The phase unitary constructed below transports these vacua and all the canonical domains.
In particular the T vacuum is Psi(1/conjugate(a)), and the second-chaos Z component is theta(z,w)theta(w,v)chi_b(z,w,v), not the positive ratio formula with a substituted for b.
The quantitative estimates of C_F0156 have the same norms after this transport.

This is an exact criterion in the bounded measurable Hermitian Gaussian class.
It does not characterize arbitrary correlated normal laws, arbitrary unbounded Gaussian kernels, or bare F without the strong adjoint-domain condition.

## Reuse and scope

The bounded Gaussian creation model, actual moment necessity and weak algebraic-tensor commutator construction are [C_F0156](Yin_C_F0156_v1.md#argument).
The proof below checks explicitly which parts of that construction require only the three conditions in item 3, rather than a supplied target derivation.
The arbitrary-abelian-base Wick representation and actual degree-zero/one adjoints are [C_F0153](Yin_C_F0153_v1.md#statement).
The normal strong-to-actual-vacuum implication is [C_F0070, Part C](Yin_C_F0070_v1.md#statement).
No new external source is used.
The role of this Claim is the exact class criterion and measurable phase transport, not a restatement of the sufficient positive-kernel theorem.

## Argument

### 1. Measurable phases give an actual tracial automorphism

Let theta=a/b on b nonzero and theta=1 on the symmetric zero set.
Choose versions so theta(v,z)=conjugate(theta(z,v)) and |theta|=1 almost everywhere.
In the relative Wick representation H_n=L2(N) tensor_2 ... tensor_2 L2(N), with n+1 factors, define

\[
 (U_nf)(z_0,\ldots,z_n)
   =\left(\prod_{r=0}^{n-1}\theta(z_r,z_{r+1})\right)
        f(z_0,\ldots,z_n).
 \tag{3}
\]

Set U_0=I and U=direct sum U_n.
This is a unitary fixing Omega and the left N action.
In the creation action of S, the factor in (3) adds precisely theta(z_0,z_1) at the new leading edge.
In the annihilation action it removes that edge with coefficient theta(z_0,z_1) inverse=theta(z_1,z_0).
Thus the creation/annihilation computation of C_F0156 gives

\[
 USU^*=T_\theta.
 \tag{4}
\]

This is a bounded-operator identity, not a formal tensor substitution.

The algebra W*(N,T_theta) is M.
Indeed bounded finite marginal kernels q_l may approximate conjugate(theta) almost everywhere with a common bound.
The operators T_(theta q_l) are finite outer N combinations of T_theta; their uniformly bounded creation/annihilation actions converge strongly to those of S.
Thus S is in W*(N,T_theta).
Conjugation by U therefore maps M onto M and fixes N pointwise.
Since U Omega=Omega it preserves the trace.

For finite separated b_l, outer N multiplication and (4) give U T_(b_l) U*=T_(theta b_l).
Approximate the bounded kernel b almost everywhere by such b_l with a common bound, using the bounded Gaussian construction.
Passing to the strong limits gives

\[
 UT_bU^*=T_a.
 \tag{5}
\]

Consequently U carries M_b onto M_a, fixes Z and transports their entire target star cores.
Its Hilbert tensor square intertwines the coefficient bimodule actions.
Actual derivations, actual vacuum adjoints, densely defined duals, and their adjoint domains are therefore transported unitarily.
This proves equivalence of A and S between a and b without differentiating the measurable phase or extending a target derivative to S.
It also proves the stated vacuum formulas: U_1 multiplies 1/b by theta= a/b, giving 1/conjugate(a), and U_2 multiplies chi_b by the two-edge phase product in (3).

### 2. Actual target vacua force the three conditions

By Section 1 it suffices to take a=b nonnegative, initially allowing zeros and allowing M_b to be a proper subalgebra of M.
Assume A on M_b.
The normal relation and the diffuse outer spectral diagonal imply delta_T Z*=0 from delta_T Z=0, exactly as in C_F0156.
For marginal polynomials f,g the actual target vacuum psi satisfies

\[
 \langle\psi,f(Z)T_b g(Z)\rangle=\tau(f)\tau(g).
 \tag{6}
\]

Embed L2(M_b) in the reference H and project psi to H_1.
The first-chaos vector of f T_b g is f(z)b(z,v)g(v).
Thus (6), and density of polynomial tensor factors, give

\[
 b\,\overline{P_{H_1}\psi}=1\quad\mu^2\text{-almost everywhere}.
 \tag{7}
\]

No generation equality was needed for this projection.
Equation (7) excludes a positive-measure zero set of b and proves P_H1 psi=1/b in L2.
Hence (1) follows.
The bounded Gaussian generation argument in C_F0156 now applies and gives M_b=M.

The Z-coordinate derivation has its usual normal starred phase, and compressing its vacuum to N supplies the actual scalar xi_N.
The separated-endpoint quadratic tests f_0 T_b f_1 T_b f_2 in C_F0156 then identify the H_2 projection as chi_b.
Every test belongs to the actual original graph by C1 smooth approximation; the disjoint endpoints remove the degree-zero component.
That proof uses only boundedness, positivity almost everywhere and the actual target vacuum, all now established.
Therefore (2) follows.
This proves item 1 implies item 3, including the possible-zero case which had to be excluded before using the positive-kernel theorem.

### 3. The three conditions construct strong duals without a supplied target derivation

Assume item 3 and first take the positive kernel b.
Its nonzero set has full measure, so the bounded Gaussian generation argument again gives M_b=M.
The scalar actual vacuum supplies the free reference derivation delta_N on C<Z,Z*,S>, with delta_N S=0 and actual vacuum xi_N.
Its two reference contraction bounds are the normalized scalar/free bounds used in C_F0156.

Define beta* on the two orthogonal coefficient subspaces H_0 tensor H_1 and H_1 tensor H_0 by

\[
 \frac{r^{-1}-1}{\bar z-\bar v},\qquad
 \frac{1-r}{\bar z-\bar v},\qquad r=b(z,w)/b(w,v)>0.
 \tag{8}
\]

The two real numerators have the same sign, so the positive-ratio estimate gives ||beta||2<=||chi_b||2.
The actual degree-one theorem concatenates the two paths and gives partial_S* beta*=chi_b.
Hence the reference derivation delta_N+I_beta partial_S and its canonical contraction E'_Z have actual vacuum xi_N+chi_b and both full bounded-vector domains.
Their estimates are those of C_F0156, using only xi_N and chi_b, not a supplied target witness.

It remains to justify commutation with T_b.
This is exactly the premise-independent portion of the weak proof in C_F0156: bounded b and (8) make its two formal leg divided differences L2;
the soft-Cauchy lemma uses only the scalar actual xi_N and tests only the original algebraic tensors.
For uniformly bounded smooth polynomial kernels b_n tending almost everywhere to b, its identities (M7)--(M8) give

\[
 \langle u\otimes v^*,\delta_NT_{b_n}\rangle
       \longrightarrow\langle u\otimes v^*,G_b\rangle,
 \qquad I_\beta\partial_ST_{b_n}\longrightarrow-G_b.
\]

The actual full adjoint domain and bounded strong convergence of T_(b_n) therefore give [E'_Z,T_b]=0 on all bounded vectors by the matrix-element formula.
That proof does not use the earlier moment-test derivation once the coefficients xi_N and chi_b are given.
The original reference commutators also give [E'_Z,Z]=P and its normal starred commutator on all bounded vectors.
No claim about a maximal graph domain is substituted for these actual matrix-element limits.

Condition (1) supplies beta_T=1/b in H_0 tensor H_0.
The actual degree-zero theorem constructs E'_T from I_(1/b)partial_S, with both full bounded domains and actual vacuum Psi(1/b).
It commutes with Z,Z*.
Since b_n/b tends to 1 in L2 by uniform boundedness and dominated convergence against b^(-2)dmu squared, its commutator with T_(b_n) tends to P in Hilbert--Schmidt norm.
The same full-adjoint matrix-element passage yields [E'_T,T_b]=P on all bounded vectors.

Set D_j=-E'_j.
These are densely defined operators on the reference H whose domains and actual adjoint domains contain M Omega and which satisfy all generator-first coordinate commutators.
They prove S for the target pair, whose von Neumann algebra is M.
The phase automorphism transports them to the original a.
This proves item 3 implies item 2 without first assuming A or a target-to-reference derivative extension.

### 4. The strong condition supplies actual target derivations and the original canonical domains

For the normal generating pair in its intrinsic algebra, item 2 implies A by C_F0070 Part C: full M domains include Omega in each adjoint domain, and the normalized full-domain dual determines the unique represented starred derivation with actual vacuum.
This proves item 2 implies item 1 and closes the equivalence.

For the explicit operators just constructed, the normalization at 1 is zero.
Their restrictions to the original target core have precisely the canonical commutators and therefore equal the canonical contractions by induction on words.
The reference full adjoint domains and bounded estimates give actual target adjoint values; bounded original-core graph approximation gives the original target closure on all M, as in the proved C_F0156 argument.
Its quantitative estimates follow unchanged.
Thus the theorem does not merely provide a choice of unrelated full-domain extensions.

All vacuum formulas in the statement are now actual adjoint values.
The positive-kernel values follow from the construction and uniqueness on the dense target core; the complex values follow from the unitary transport in Section 1.
The zero case was excluded by an actual linear moment test, not by an assumed ability to invert a inside the target algebra.

## Scope

The bounded Hermitian Gaussian kernel hypothesis is substantive.
It supplies the bounded creation model, the degree-one correction and the explicit phase automorphism.
The conclusion A iff S is restricted to this class.
It implies F but does not prove F implies any of the three equivalent conditions.
There is no unrestricted normal comparison or extension to unbounded measurable kernels in this statement.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:15 |
| status | open |
| reason | Complete measurable phase transport, necessary moment conditions and sufficient actual reference construction give an exact A/S/integrability criterion for bounded Hermitian Gaussian kernels. Independent review pending; no bare-F converse or unrestricted normal conclusion claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact intrinsic A, strong S and scalar-vacuum/two-integral equivalence for bounded Hermitian Gaussian kernels, including zero-set exclusion, target generation and phase-correct vacua. |
| argument | [Argument](#argument) | Full phase automorphism, actual linear/quadratic moment necessity, sufficiency without a supplied target derivative, normal S-to-A and original canonical-domain identification. |
| dependency | [Measurable Gaussian proof](Yin_C_F0156_v1.md#argument) | Bounded creation and generation, actual moment extraction, weak algebraic-tensor integration by parts and full-adjoint commutator passage; sufficiency premises are rechecked explicitly here. |
| dependency | [Arbitrary-base relative degrees](Yin_C_F0153_v1.md#statement) | Relative Wick Hilbert model and actual degree-zero/one weighted derivative, vacuum and canonical-domain estimates. |
| dependency | [Normal strong-to-vacuum implication](Yin_C_F0070_v1.md#statement) | Part C under full bounded-vector dual and adjoint domains, and the resulting canonical starred uniqueness; no general bare-F converse imported. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:21 |
| status | proved |
| reason | Adopt the exact bounded measurable Hermitian Gaussian criterion after R_F0165 independently checked the entire statement, all four proof sections and three direct inputs, including sufficiency without supplied target A. The phase transport and both original target domains are established; bare F and unrestricted normal converses are not adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact intrinsic A, strong S and scalar-vacuum/two-integral equivalence for bounded Hermitian Gaussian kernels, including zero-set exclusion, target generation and phase-correct vacua. |
| argument | [Argument](#argument) | Full phase automorphism, actual linear/quadratic moment necessity, sufficiency without a supplied target derivative, normal S-to-A and original canonical-domain identification. |
| dependency | [Measurable Gaussian proof](Yin_C_F0156_v1.md#argument) | Bounded creation and generation, actual moment extraction, weak algebraic-tensor integration by parts and full-adjoint commutator passage; sufficiency premises are rechecked explicitly here. |
| dependency | [Arbitrary-base relative degrees](Yin_C_F0153_v1.md#statement) | Relative Wick Hilbert model and actual degree-zero/one weighted derivative, vacuum and canonical-domain estimates. |
| dependency | [Normal strong-to-vacuum implication](Yin_C_F0070_v1.md#statement) | Part C under full bounded-vector dual and adjoint domains, and the resulting canonical starred uniqueness; no general bare-F converse imported. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0165_v1.md#conclusion) | Whole statement and four-section proof, intrinsic zero-set exclusion, measurable phase automorphism, necessary and sufficient integral conditions, original domains, exact complex vacua and all three direct interfaces. |


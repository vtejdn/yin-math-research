---
author: Yin
---
# ACSY24 Theorem 3.4 and maximal Delta from full-domain duals

Date: 2026-10-14.
Human author Yin.
Root's self-checked comparison of the full-domain dual condition and primary literature, with the new mathematical bridge retained and separately reviewed in C_F0070.
This is a bounded continuation of [L_F0047](Yin_L_F0047_v1.md).

## Exact objects being compared

The [full-domain maximality argument](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) starts with linear maps D_i:M Omega -> H satisfying [X_j,D_i]=delta_ij P on every bounded vector and concludes Delta(X)=d.
This implication does not use normality, closability, an adjoint domain or a derivation.

[ACSY24 Theorem 3.4](../literature/pdf/ACSY24.pdf), published p.35, starts with a noncommutative derivation partial:A -> H tensor_2 H on a weakly dense star subalgebra and an actual vector partial*(1 tensor 1).
It constructs E_0=(id tensor tau)partial on A Omega and proves
\[
 [E_0,a]=\Theta(\partial a),\qquad
 A\Omega\subseteq\operatorname{Dom}E_0^*,\qquad
 E_0^*(a\Omega)=a\,\partial^*(1\otimes1)
                 -\Theta(\partial(a^*))^*\Omega.
\]
Consequently E_0 is closable.
The theorem itself does not impose a generator normalization or conclude maximal Delta, and it does not assert M Omega is in the original closure domain.
The exact source definition, statement and entire short proof were reread in the 73-page published artifact at pp.34--36; the arXiv v2 interface is printed/PDF p.29.
The existing [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) owns this source inspection and the reconstruction of Proposition 3.5.

Proposition 3.5 is the result with the same maximal-Delta conclusion as the full-domain maximality criterion.
It adds partial_i X_j=delta_ij (1 tensor 1) on the represented starred polynomial algebra to the actual vacuum premises.

## What direct replacement would require

Theorem 3.4 constructs an operator from a derivation and an actual vacuum adjoint.
The full-domain criterion instead deduces maximal Delta from already given operators.
Theorem 3.4 alone supplies neither full bounded-vector domains nor the maximality conclusion.
Conversely, the full-domain maximality argument does not reconstruct a canonical operator, its adjoint formula or closability from a derivation.

These observations about statements do not establish nonimplications between their normalized hypotheses.
For a normalized tuple, the relevant questions are:
- do the ACSY24 derivation/vacuum assumptions produce a full-domain dual to which the full-domain maximality criterion applies?
- do the bare full-domain assumptions yield the derivation/vacuum input for Theorem 3.4 and Proposition 3.5?

The preceding [L_F0047](Yin_L_F0047_v1.md) retained those as unresolved general correlated-normal questions.
The present continuation sharpens their exact missing interfaces.

## New bridge and the revised remaining gap

[C_F0070](../claims/Yin_C_F0070_v1.md#statement) proves that a normal generating tuple with bare full-domain duals already has unique coarse derivations delta_i on its full represented starred polynomial algebra, with prescribed unstarred generator values.
This uses [C_F0069](../claims/Yin_C_F0069_v1.md#statement)'s automatic M-to-H norm continuity and a continuous-partition argument replacing the closability-dependent spectral-projection step of C_F0038.
The complete proof belongs to C_F0070.

For normalized E_i(a)=-D_i(a)+aD_i Omega, the result gives
\[
 \delta_i(a)=\Theta^{-1}([E_i,a]),\qquad
 E_i|_A=(\mathrm{id}\otimes\tau)\delta_i,
\]
and the normal phase fixes all starred-generator values.
Thus derivation existence is now resolved under the bare normal premise.
This supersedes that particular outstanding target in L_F0047; the remaining condition is exactly
\[
 \left|(\tau\otimes\tau)(\delta_i p)\right|
       \le C_i\|p\|_2\qquad(p\in A),
\]
equivalently 1 tensor 1 in Dom delta_i*.
The theorem does not infer this estimate merely from M-to-H norm continuity.

Conversely, assume ACSY24 already holds for the normal tuple and let E_i0 be the canonical operators of Theorem 3.4.
C_F0070 proves the exact equivalence
\[
 \begin{gathered}
 \exists\text{ arbitrary bare full-}M\Omega\text{ dual system}\\
 \Longleftrightarrow\
 M\Omega\subseteq\operatorname{Dom}\overline{E_{i,0}}
       \quad\text{for every }i.
 \end{gathered}
\]
Any supplied normalized full-domain dual has the same starred-core derivations as the ACSY24 derivations by the injective spectral-difference argument.
Hence it supplies the uniform canonical core bound, and weak closed graph restores the actual canonical closure.
This establishes necessity as well as sufficiency of the domain bridge.
Seeking a different algebraic full-domain extension therefore does not bypass the canonical-domain question.

Equality with a supplied normalized map is asserted on A Omega only.
No all-M equality or Hilbert-space closability of that supplied map is inferred from operator-norm continuity, since A need not be norm dense in M.

## The additional adjoint-domain premise

Consider normal generators and the additional hypothesis
\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*.
\]
In particular Omega belongs to Dom D_i*.
C_F0070 Part C therefore supplies the actual vacuum explicitly:
\[
 \delta_i^*(\Omega\otimes\Omega)
     =-D_i^*\Omega+(D_i\Omega)^*.
\]
Under these stronger hypotheses, ACSY24 Proposition 3.5 can provide Delta(X)=d after the starred-derivation bridge is stated and justified.
Theorem 3.4 supplies the intermediate canonical construction, not the final maximality statement.

This yields maximal Delta under the additional adjoint-domain premise.
It does not show that the arbitrary-tuple bare full-domain condition implies the ACSY24 hypothesis.
The denominator-clearing argument in C_F0024 Section 3 gives maximal Delta under weaker assumptions than this derivation bridge requires.

## Outcome and continuation

The exact comparison yields a proved bridge, rather than a blanket assertion of either theorem containing the other.
For arbitrary correlated normal tuples the two remaining general questions are now:
1. whether an ACSY24 canonical core always satisfies the operator-norm-to-L2 bound that restores its full bounded-vector closure domain;
2. whether the unique starred derivations now obtained from bare full-domain duals always possess their actual L2 vacuum adjoints.

The first question is equivalent, under ACSY24, to applicability of the full-domain maximality criterion through existence of any full-domain dual.
The second question is the remaining converse input for Theorem 3.4 and Proposition 3.5.
Neither is refuted by absence of a hypothesis in a published statement; neither is resolved by this comparison.
The prior scalar and special-tuple positive results retain their exact scopes.

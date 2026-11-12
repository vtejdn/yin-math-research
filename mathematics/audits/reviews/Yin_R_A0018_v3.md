---
author: Yin
---
# Rational kernel projection transport: independent whole-argument review

The review act was completed at 2026-11-11T16:22 UTC, under the human authorship of Yin.
The inspected artifact is [C_A0005 v3](../../claims/Yin_C_A0005_v3.md#statement), dated 2026-11-12 in Asia/Hong_Kong, with its complete statement, argument, explicit example and final scope section.
This is new independent evidence for that fixed input in the existing projection-transport review family; no finding or binding is inherited from R_A0018 v2.

## Arrangement and inputs

An agent outside substantive proof development performed this initial independent whole-artifact inspection.
No development drafts, proof-generation dialogue, author proof summaries or previous review conclusions concerning v3 were supplied or consulted.
The reviewer read the fixed v3 statement and proof, worked backward from its conclusions, checked the forward derivations, and reread the complete saved artifact before forming the final finding.
The direct mathematical arguments in C_A0005 v2 were read as dependencies; its separate R finding was not opened or used as a substitute for those checks.

The inspected supporting interfaces were the [Boolean trace lower-bound argument](../../claims/Yin_C_A0005_v2.md#a-trace-lower-bound-forces-a-finite-boolean-orbit), [finite-component exhaustion](../../claims/Yin_C_A0005_v2.md#finite-starts-and-the-missing-infinite-components), [path blocks and bounded kernel equations](../../claims/Yin_C_A0005_v2.md#path-blocks-and-the-exact-kernel-dimension), and [augmentation rigidity](../../claims/Yin_C_A0005_v2.md#augmentation-rigidity-for-abelian-group-ring-matrix-projections).
The reviewer also checked the [subgroup trace comparison](../../tasks/Yin_T_A0001_v1.md#reduction-to-finitely-generated-groups) and the retained Lin93 interfaces for [affiliated closure and rank](../literature/Lin93/Yin_U001.md#affiliated-closure-and-rank-conventions) and [the covered group class](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems).
The latter are accepted source interfaces at their retained scope, not newly performed full source-proof audits.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#finding-rational-kernel-transport) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Statement](../../claims/Yin_C_A0005_v3.md#statement) | Complete hypotheses and conclusions (F1)--(F3), including arbitrary torsion-free abelian \(N\), commuting transport, period bound, integer Boolean traces, the exact nullity range, and the explicit-example assertions. |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Argument](../../claims/Yin_C_A0005_v3.md#argument) | Complete argument (F4)--(F5) and (1)--(11), all supporting interfaces, actual affiliated units, matrix amplification, explicit realization and complete kernel projection. |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Finite coefficient origin](../../claims/Yin_C_A0005_v3.md#finite-coefficient-origin-and-the-surviving-finite-orbit-certificate) | Rational kernel projection, Fourier rank, Boolean lower bound, periodicity, affiliated congruence, finite path sum and its upper bound. |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Actual group and denominator](../../claims/Yin_C_A0005_v3.md#actual-group-and-certified-denominator) | Torsion-freeness, index-four abelian subgroup, cyclic injectivity, positivity and centrality of \(s\). |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Spectral projection and two-cycle](../../claims/Yin_C_A0005_v3.md#actual-spectral-projection-and-its-two-cycle) | Identities (2)--(6), actual rational projections, traces, complementary transport, finite coefficient origin and the obstruction to a Laurent-polynomial representative. |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Finite realization and exact kernel](../../claims/Yin_C_A0005_v3.md#finite-group-ring-realization-and-exact-kernel) | Affiliated congruence (8), bounded kernel parametrization (9), all normalizations in (10), and completeness and boundedness of the Gram projection in (11). |
| [Whole-artifact finding](#finding-rational-kernel-transport) | [Scope and limitations](../../claims/Yin_C_A0005_v3.md#what-this-test-changes-and-does-not-change) | Nonstationarity of rational spectral projections, dependence on commuting transport, known abelian-by-cyclic coverage, and absence of an A0001 counterexample or new Atiyah group class. |

<a id="finding-rational-kernel-transport"></a>
## Whole-artifact finding

No mathematical gap was found in the complete fixed statement, argument, example or final scope qualifications.
The following checks support that conclusion.

### Rational origin, integer traces and periodicity

A nonzero Laurent polynomial on a finite torus has a Haar-null zero set, by induction on the number of variables and the finite-root property in one variable.
Each calculation uses finitely many coefficients and denominators in a finitely generated free abelian subgroup.
The subgroup/coset comparison therefore supplies the same actual trace and rank in arbitrary torsion-free abelian \(N\).
For a matrix over \(F\), a nonzero maximal minor and the vanishing of larger minors give agreement of field rank and almost-everywhere Fourier rank.
Formula (F4) consequently gives the actual orthogonal kernel projection, and the zero-kernel case is handled separately.

Every finite Boolean product remains a rational projection because the translated projections commute.
Its unnormalized trace is its integer Fourier rank; a nonzero product has trace at least one.
The directly checked Boolean lemma gives at most \(d\) nonzero Boolean atoms and at most \(2^d\) distinct projections in the transport orbit.
Invertible transport permutes that finite orbit, so it is periodic with the stated bound.
The proof correctly establishes intersection arithmetic, rather than inferring it merely from integer traces of individual projections.

### Affiliated reduction and the matrix path calculation

On the actual Fourier fibers, \(B+p\) is the identity on the kernel fiber and positive definite on its complement.
It is therefore an actual affiliated unit with rational inverse \(X\), and \(BX=XB=I_d-p\).
This verifies (F5) in the affiliated ring without applying an unbounded inverse to arbitrary Hilbert-space vectors.
Rank invariance under actual affiliated units, with the unnormalized matrix trace, applies to the displayed congruence.

The v2 path argument was checked at the matrix-amplified interface.
The commuting site projections define orthogonal interval components, and the maps given by powers of \(t\) remain right-\(G\)-equivariant unitaries between the corresponding modules in the \(d\)-coordinate space.
Compression removes the exterior terms and yields the ordinary finite path adjacency matrix on each component.
An odd path contributes one copy of its start module, while an even path contributes no kernel.
The all-open component reduces the amplified \(t+t^{-1}\), which is injective by the cyclic Fourier test.
The bounded full-kernel parametrization then adds exactly one free lower \(p\)-module.
These arguments do not require scalar-valued site projections.

If \(\ell\ge m\), the retained product contains \(p_{m-1}=p_{-1}\), which is annihilated by the deleted-neighbor factor.
Thus every \(e_\ell\) in that range vanishes, giving the finite sum in (F3).
The distinct start projections are orthogonal and lie under \(I_d-p_{-1}\), which bounds the odd-path contribution by \(d\) minus the trace of \(p\).
Together with integrality this gives the complete stated range.
The stationary case \(m=1\), \(p=0\) and \(p=I_d\) are consistent with the formula.

### Explicit two-cycle and polynomial obstruction

Projection to the infinite cyclic quotient proves torsion-freeness of the example group, and \(\sigma^4=1\) makes the specified abelian subgroup have index four.
The cyclic injectivity of \(a\) and the inequality \(s\ge a^*a\) certify the actual affiliated inverse of \(s\) independently of a whole-group Atiyah theorem.
The displayed skew-adjoint identities give (2), while preservation of \(s\) and exchange of the two columns give the complementary two-cycle in (4).
Both projections have unnormalized trace one.
The example fits \(B=A^*A\) by taking \(A=w^*\), and \(B=sq\) has precisely \(p\) as its kernel projection.
The stated overlap defect is \(p\).

The two distinct limits of (6) at the trivial character rule out a continuous Laurent-polynomial representative.
Almost-everywhere equality with such a representative would imply equality throughout the open complement of the common zeros, so changing values on the null singular set cannot remove that obstruction.
The absence of an augmentation value is therefore compatible with the v2 theorem, whose hypothesis requires an actual group-ring projection.

### Complete kernel and normalization

The actual unit in (8) gives the stated rank-preserving congruence.
Complementary transport implies \(Tp=qTp\) and \(pTp=0\).
The equations in (9) then give a bounded equivariant isomorphism from two copies of the \(p\)-module onto the complete kernel of \(H_p\), with the stated bounded inverse.
This proves nullity two and rank two for the original four-coordinate matrix \(H\).
Dividing the kernel trace by four gives the probability-normalized zero atom one half.
The path specialization has \(e_1=p\) and no longer retained paths, agreeing with the general formula.

For (11), \(F\) is bounded, \(HF=0\), and \(F^*F=C\) is positive injective on the \(p\)-corner because its first Gram summand is \(s^2p\).
The finite affiliated Gram calculus makes \(FC^{-1}F^*\) the bounded projection onto the closure of the range of \(F\).
That range has dimension one and is orthogonal to the free lower \(p\)-module, using \(pTp=0\).
The displayed sum is consequently an orthogonal subprojection of the complete kernel with trace two.
The previously established complete nullity and trace faithfulness prove equality.
This checks the full kernel projection without a pointwise-domain substitution involving \(s^{-1}\).

## Accepted foundations and limits

The established finite affiliated-operator calculus, the identification of bounded-operator rank with the trace of its closed range, and invariance under multiplication by affiliated units are accepted at the interface retained in the Lin93 source unit.
That unit identifies Lemma 2.3 and its underlying projection and finite-trace foundations.
This review checked the conventions and applicability but did not independently re-audit Berberian's original foundations or the complete original Lin93 proof.
The elementary cyclic Fourier, finite Laurent-polynomial and Gram calculations actually used in v3 were checked directly as described above.

The known-coverage statement matches the retained Lin93 group-class interface: a torsion-free abelian-by-cyclic group is elementary amenable, hence is within the stated existing coverage.
The general formula and the example do not use that coverage as a substitute for their direct computations.
No new group class, historical priority, fractional unnormalized rank or A0001 counterexample follows.
All translated projections must commute for the general Boolean and path arguments; no corresponding conclusion for noncommuting transport was checked or established.

This finding supplies independent whole-artifact evidence for C_A0005 v3 only at the exact bindings above.
It is not a completion review of A0001, an independent proof audit of every external foundation, a historical-priority search or formal verification.
C retains responsibility for any assessment and selection of this finding.

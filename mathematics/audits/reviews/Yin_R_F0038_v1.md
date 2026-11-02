---
author: Yin
---

<a id="c_f0066-existential-domain-review"></a>

# C_F0066: whole-proof review of the existential supplied-domain obstruction

- Timestamp: 2026-10-01T14:15.
- Human record author: Yin.
  The checkout's recorded actor was checked as Yin.
  This attribution does not assert personal human inspection.
- Review arrangement: a separately assigned mathematical AI agent, which did not construct this counterexample, performed an initial review of the complete fixed ledger proof.
  The reviewer reconstructed the obligations and decisive calculations below; this is independent agent review, not formal verification or external human review.
- Inputs and sequence: the assignment identified the fixed proof and requested a whole-proof and source-interface check.
  No proof-generation dialogue, exploration draft, author explanation, or earlier C_F0066 review report was supplied or opened.
  The proof itself includes historical statements about construction and an earlier conversational check; those statements were necessarily visible and were not treated as evidence for correctness.
  A session memory summary and a brief lookup of older T_F0001 domain conventions were also available; current contracts and source files were read instead of relying on their historical status.
  The obligations below were identified from the statement and literal domain definition before consulting the comparison materials.
  The existing source unit contains its own previous review history; only its identified mathematical interface and the primary passages checked below were used.
- Exact target: registered [Yin_C_F0066_v1](../../claims/Yin_C_F0066_v1.md#decision-candidate-0001), whose starting assessment is `open` / `unreviewed`.
  The complete candidate proof is material v1, [Yin_C_F0066_v1.md](../../claims/Yin_C_F0066_v1.md#existential-original-regular-commutator-counterexample), all sections, as read on 2026-10-01.
  Its explicit anchor is `existential-original-regular-commutator-counterexample`.
- Intended acceptance binding: this review supports a planned Claim v2 selecting that same proof v1 and anchor.
  It does not assert that v2 has already been published.
  There is no earlier proof that must be retained as auxiliary mathematical support for the counterexample.
- Scope: the whole counterexample, all fraction-pair quantifiers, actual supplied domains and adjoints, genuine unboundedness, source coverage, and the stated relationships and remaining hypothesis branches.
  The historical Task comparison is [Yin_T_F0001_v5](../../tasks/Yin_T_F0001_v5.md#decision-candidate-0008) and its [material v5 contract](../../tasks/Yin_T_F0001_v5.md#yin_t_f0001).
  This is not a new Task completion or lifecycle review.

## Obligations and findings

The conclusion to check is stronger than the earlier failure of fraction independence: one specified rational affiliated element must fail the existential dense-domain condition for **every** legal bounded left/right fraction pair.
It is therefore necessary to verify the supplied Hilbert-space model and every dual assumption, establish a nonempty class of legal fractions, prove the exact whole natural domain at arbitrary fractions, and verify the claimed unboundedness and scope distinctions.

### 1. The finite tracial model and exact polynomial domain

The full Fock space over two orthonormal real directions carries the fields \(X_j=\ell_j+\ell_j^*\).
The standard real semicircular model supplies a faithful normal tracial vacuum state on \(M=W^*(X_1,X_2)\), with \(H=L^2(M,\tau)\).
The source and normalization checks are recorded separately below.
Directly, \(\tau(X_j^2)=1\), and the two real orthogonal directions give free semicircular variables.

For a word \(w=x_{j_1}\cdots x_{j_n}\), the degree-\(n\) tensor component of \(w(X)\Omega\) is exactly \(e_{j_1}\otimes\cdots\otimes e_{j_n}\), with coefficient one.
For a nonzero polynomial of maximal degree \(n\), its top homogeneous coefficients therefore cannot cancel.
Descending in degree proves injectivity of polynomial evaluation on the vacuum.
The same triangular relation expresses each finite Fock word as a polynomial vacuum vector by induction on word length.
Thus \(\mathcal P\) is precisely the finite-word span, is Hilbert dense, and is invariant under the fields and right annihilators.
Selfadjointness of the two generators makes this exactly the starred-polynomial domain.
There is no assumption here of polynomial independence that is subsequently derived from the claimed counterexample.

**Finding:** the algebra, trace, normalization, generation, injectivity, and exact dense polynomial domain are valid.

### 2. The supplied duals, signs, and actual adjoints

For the vacuum, \(r_i^*\ell_j\Omega=\delta_{ij}\Omega\) and \(\ell_jr_i^*\Omega=0\).
On every nonempty Fock word, deleting its last letter and adding a first letter commute.
Hence
\[
[r_i^*,\ell_j]=\delta_{ij}P_\Omega.
\]
Left and right annihilation commute also on words of length zero and one, where both double-annihilation terms vanish.
This proves \([r_i^*,\ell_j^*]=0\), including the boundary lengths.
All operators used in these identities are bounded, so the word calculations extend to \(H\).

Restricting \(r_i^*\) to the invariant domain \(\mathcal P\) gives exactly the prescribed \(D_i\).
It follows that \([D_i,X_j]=\delta_{ij}P_\Omega\) on the whole supplied domain.
Since \(X_j=X_j^*\), this also proves the starred relation and its rank-one or zero compact extension.
Moreover \(D_i\Omega=0\).

For each \(\eta\in H\), the adjoint functional on \(\mathcal P\) is bounded by \(\|r_i\eta\|\|p\|\), and agrees with the bounded adjoint of \(r_i^*\).
Density of \(\mathcal P\) gives the exact Hilbert adjoint
\[
\operatorname{Dom}D_i^*=H,\qquad D_i^*=r_i,\qquad D_i^*\Omega=e_i.
\]
The graph closure is the graph of \(r_i^*\).
The finite-word span is a proper dense subspace of the infinite Fock space, so the supplied restriction is not closed.
Neither the calculation nor the later domain definition replaces it by that closure.

**Finding:** every required dual assumption holds, with actual adjoints and the positive commutator sign stated in the proof.
Both the no-starred-condition package and its compact-starred-commutator baseline are satisfied.

### 3. Rationality, regularity, and existence of bounded fractions

The variance-one semicircle law is diffuse and has positive density around zero.
Its zero spectral projection vanishes.
Faithfulness of the trace therefore makes \(X_1\) injective on the standard Hilbert space; selfadjointness makes its range dense.
Its spectral inverse is an affiliated operator.
Thus \(u=X_1^{-1}X_2\) belongs to the stated scalar affiliated division closure, using one legal inversion and one multiplication.
No assertion that an arbitrary nonzero affiliated element is invertible is used.

The pair \(s=X_1,a=X_2\) is a valid bounded left fraction.
For the displayed right fraction, write \(u=v|u|\) by polar decomposition.
Then
\[
t=(1+|u|^2)^{-1/2},\qquad
b=v\,|u|(1+|u|^2)^{-1/2}.
\]
The two scalar functions are bounded on \([0,\infty)\), and \(\|b\|\leq1\).
Their functional calculus and affiliation put \(t,b\) in \(M\).
The function defining \(t\) never vanishes at a finite spectral value, so \(\ker t=0\); positive selfadjointness then gives dense range.
Its affiliated inverse exists, and \(bt^{-1}=u\).
In particular, the universal quantifier over bounded fraction pairs is nonvacuous.
These statements concern the affiliated product, with the bounded equality \(ut=b\) well-defined because \(|u|t\) is bounded.

**Finding:** the witness is rational, the chosen denominators are regular, and a legal bounded pair exists.
The proof does not require a scalar right fraction with polynomial numerator and denominator.

### 4. The full natural domain for every fraction pair

Fix arbitrary \(s,a,b,t\in M\) with regular \(s,t\) and \(u=s^{-1}a=bt^{-1}\).
Associativity in the affiliated algebra gives \(X_1b=X_1ut=X_2t\).
Both resulting sides are bounded elements of \(M\), so this is an equality of their everywhere-defined bounded actions on \(H\); no illegal unbounded composition on an arbitrary vector is invoked.

For any \(q\) in the specified natural domain \(\mathcal E_i\), exact equality \(\operatorname{Dom}D_i=\mathcal P\) supplies finite free polynomials \(R,Q\) such that \(bq=R(X)\Omega\) and \(tq=Q(X)\Omega\).
The bounded identity now gives
\[
(x_1R-x_2Q)(X)\Omega=0.
\]
Polynomial injectivity established in finding 1 yields the formal identity \(x_1R=x_2Q\).
The word basis partitions into disjoint sets according to its first letter; therefore the subspaces \(x_1\mathbb C\langle x_1,x_2\rangle\) and \(x_2\mathbb C\langle x_1,x_2\rangle\) intersect only in zero.
It follows that \(R=Q=0\).
Regularity of \(t\), in particular injectivity on \(H\), then gives \(q=0\).
Conversely zero lies in every linear domain, proving exact equality rather than a mere upper bound:
\[
\mathcal E_i(s,a,b,t)=\{0\}
\quad\text{for all legal pairs and }i=1,2.
\]

The argument used no property of the arbitrary left coefficients.
It checks every vector of the entire natural composition domain, not only the vacuum or a selected test core.
Although the zero-domain expression has algebraic rank zero and many bounded extensions, its domain is not Hilbert dense.
Consequently no pair satisfies the conjunction in the investigated condition.

**Finding:** the decisive all-pair statement and the failure of the existential forward implication are proved, with the original fraction quantifiers intact.

### 5. Genuine unboundedness of the witness

Suppose \(u\) were bounded.
A bounded affiliated operator lies in \(M\), and \(X_1u=X_2\) would imply
\[
X_2^2=(X_1u)(X_1u)^*=X_1uu^*X_1\leq\|u\|^2X_1^2.
\]
Let \(e=1_{[-\varepsilon,\varepsilon]}(X_1)\).
The spectral interval has positive semicircular mass for every sufficiently small \(\varepsilon>0\).
Freeness of the generated von Neumann subalgebras and variance one give \(\tau(eX_2^2)=\tau(e)\tau(X_2^2)=\tau(e)>0\).
Compressing the operator inequality by \(e\) and taking the trace gives
\[
\tau(e)\leq\|u\|^2\tau(eX_1^2)\leq
\|u\|^2\varepsilon^2\tau(e).
\]
Choose \(\varepsilon\) with \(\|u\|^2\varepsilon^2<1\).
Division by the strictly positive \(\tau(e)\) is legitimate and gives a contradiction.
Compression and traciality justify this step without assuming that \(e\) commutes with \(X_2\).

**Finding:** the rational witness is genuinely unbounded; the argument does not rely on a merely unbounded chosen expression for a bounded element.

## Source coverage and accepted foundations

The main declared source is [Voi98-U005](../literature/Voi98/Yin_U005.md#voi98-u005), specifically its subsection on the semicircular model and sign correction.
The reviewer read that interface and checked the extracted primary text of Voi98, Section 5.13, printed pp. 212-213, PDF pp. 24-25 of the locally registered published journal article.
Those passages give the full Fock left/right creation model, the vacuum commutators, and the standard tracial representation.
The source uses \(s(h)=(\ell(h)+\ell(h)^*)/2\); the present \(X_j\) is \(s(2e_j)\), of variance one.
The source's printed imaginary-part sign is not imported: the needed real orthonormal-basis commutator was recomputed directly in finding 2, consistently with the local correction.
No general unbounded-dual theory or source Section 5.14 restriction assertion is used.

Standard finite-tracial affiliated-operator algebra, spectral calculus, and polar decomposition remain accepted foundations.
As a background comparison of the bounded-fraction and regularity conventions, the reviewer also read [Miy22-U006](../literature/Miy22/Yin_U006.md#miy22-u006) and checked the extracted primary Section 4 opening and Lemma 4.3 on printed/PDF p. 19 of the registered published Miy22 article.
That source records bounded fractions and the injective/dense-range meaning of regularity in this same semicircular setting.
It displays exponent \(-1\); the exponent \(-1/2\) used here is independently justified by the explicit scalar functions in finding 3.
This consultation checks background terminology and compatibility; it is not newly selected proof support or an added source-proof dependency.
The proof does not invoke its fraction-independence or rationality theorems.
The foundational proofs of the affiliated algebra and the spectral theorem were not re-audited, and earlier source-review verdicts do not substitute for the present calculations.

Polynomial injectivity, the exact restriction adjoints, the all-pair free-word obstruction, and the spectral-projection contradiction were checked directly.
They import no earlier project Claim as a mathematical premise.
The checks above supply the necessary attribution and source applicability; no novelty or earliest-priority search is claimed.
Primary-source inspection in this review used extracted text of the complete specified pages, not fresh rendered-page inspection or a new audit of either whole paper.

**Source-coverage verdict:** sufficient for this argument at the stated accepted-foundation boundary.
No unresolved source identification or applicability issue was found.
Voi98-U005 remains the proof's sole declared model source.
The Miy22-U006 background comparison does not require an additional selected source attachment or project dependency.

## Comparison interfaces and quantifier boundaries

The following are checked comparisons, not premises of the counterexample.
Their entire prior proofs and downstream dependency trees were not re-audited.

| Fixed material | Checked interface and finding |
| --- | --- |
| [T_F0001 recorded assessment 8](../../tasks/Yin_T_F0001_v5.md#decision-candidate-0008), [contract material v5](../../tasks/Yin_T_F0001_v5.md#yin_t_f0001) | Its literal domain and dense bounded finite-rank extension convention agree with the current definition. The earlier accepted counterexamples left the existential-only case undecided. C_F0066 supplies a subsequent failure of that forward implication without changing historical completion evidence. |
| [C_F0065 physical v1, original assessment 2](../../claims/Yin_C_F0065_v1.md#decision-candidate-0002), [two-model proof](../../claims/Yin_C_F0065_v1.md#original-regular-commutator-domain-counterexamples) | That statement gives a good and bad pair for a one-variable rational witness and separately a closed supplied extension. The present two-variable witness has no good pair and uses nonclosed restrictions. The stronger existential conclusion is distinct, while the closed-extension observation is not subsumed. |
| [C_F0026 physical v1, original assessment 3](../../claims/Yin_C_F0026_v1.md#decision-candidate-0002), [small-core obstruction](../../claims/Yin_C_F0026_v1.md#yin_c_f0026) | Its stated obstruction concerns fraction inputs leaving a domain at specified vectors, with its own noncompact starred-commutator boundary. It does not refute the existential dense-domain condition. The whole-domain, all-pair computation here supplies the missing kind of evidence. |
| [C_F0063 physical v1, original assessment 2](../../claims/Yin_C_F0063_v1.md#decision-candidate-0002), [intrinsic criterion](../../claims/Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion) | The exact polynomial domain, actual adjoint vacuum, normal generators, and compact starred commutators meet its C_F0025 hypothesis interface. Since the displayed element is rational, its theorem gives intrinsic finite-rank representers. Its tensor-test/Hilbert-Schmidt inverse realization does not claim equality with every literal supplied-domain expression; the zero-domain result does not contradict it. |
| [C_F0064 physical v1, original assessment 2](../../claims/Yin_C_F0064_v1.md#decision-candidate-0002), [bounded weak-form criterion](../../claims/Yin_C_F0064_v1.md#normal-small-core-bounded-rationality) | Its theorem concerns bounded \(f\in M\) and polynomial weak forms. The present \(u\) is unbounded, and the failed condition concerns the literal composition domain. Neither a counterexample to the weak-form theorem nor an identification of the two notions follows. |
| [C_F0013 physical v1, original assessment 3](../../claims/Yin_C_F0013_v1.md#decision-candidate-0002), [bounded-dual criterion](../../claims/Yin_C_F0013_v1.md#yin_c_f0013) | Replacing the restrictions by \(r_i^*\in B(H)\) satisfies its bounded-dual assumptions and makes every natural domain equal to \(H\). Its rationality criterion then applies. This is a different supplied operator and cannot repair the original restriction by silent substitution. |
| [S_F0011](../../strategies/Yin_S_F0011.md#s_f0011) | Its completed route and historical unresolved existential boundary explain the relationship. The new Claim refines that boundary; it does not itself select a new objective or execution run. |

The counterexample proves neither the separate reverse implication from the existential condition to rationality nor failure under an added requirement that the supplied operators be closed.
Here closedness is explicitly false.
Requiring equality with the closure of the polynomial restriction would likewise exclude this example.
The proof does not claim these strengthened hypotheses sufficient.
Removing density and counting only algebraic rank changes the criterion and invalidates this particular negative conclusion, as the proof explicitly observes.

## Review binding and outcome

The selected mathematical support should be exactly the complete v1 proof and its explicit anchor listed above, with its declared Voi98-U005 model-source attachment.
This review's Miy22-U006 consultation is only a background comparison, not an additional selected premise.
No version-qualified project Claim dependency is needed for the counterexample itself.
The listed fixed comparison Claims and Task are scope references, not dependency edges; no dependency cycle is introduced.

**Mathematical validity:** pass for the entire stated existential counterexample.
All substantive obligations, including fraction existence, exact zero domains for every legal pair, and genuine unboundedness, have been checked with the decisive derivations above.
No mathematical correction is required.

**Source completeness:** pass at the explicit standard-foundation boundary above.
This is not a certification of full original-source proofs or literature priority.

The supported recommendation is `proved` / `independently reviewed` for the planned acceptance version of C_F0066, using the unchanged proof material v1 and this whole-proof review.
Publication and canonical assessment remain the coordinating agent's operation.
No formal proof artifact, numerical experiment, or personal human review is claimed; the verification was exact mathematical reasoning and source/interface inspection.
This review changes no Task lifecycle, manuscript selection, proof file, registry, or historical review.

## Relationship arrangement

The distinct nonconstructing reviewer was assigned the complete fixed proof and source interface only.
The account expressly excludes proof-generation dialogue, exploration drafts, author explanation and earlier review reports before the mathematical findings.
Historical proof-internal provenance and general older domain conventions are legitimate fixed-input context and were not used as correctness evidence.
The initial independent findings required no mathematical correction; their original date and source-text inspection limits remain unchanged.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#c_f0066-existential-domain-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#c_f0066-existential-domain-review) | [Statement](../../claims/Yin_C_F0066_v1.md#statement) | Whole C_F0066 fixed proof: two-variable tracial Fock system, actual polynomial-domain duals and adjoints, bounded fractions, every-pair zero natural domain, genuinely unbounded witness and exact model-source/comparison boundaries. |
| [Original finding](#c_f0066-existential-domain-review) | [Whole counterexample](../../claims/Yin_C_F0066_v1.md#existential-original-regular-commutator-counterexample) | Whole C_F0066 fixed proof: two-variable tracial Fock system, actual polynomial-domain duals and adjoints, bounded fractions, every-pair zero natural domain, genuinely unbounded witness and exact model-source/comparison boundaries. |

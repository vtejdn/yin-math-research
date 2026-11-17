# Current Writing Opinions

These opinions concern [main.tex](main.tex) and its six included sections.
The revising agent read the abstract and all six sections under the [manuscript choices](../writing.md), Yin's applicable policies and the [common writing checks](../../../../../framework/rules/writing.md#manuscript-writing-rule-checks).
The review focuses on hypotheses, object references, terminology, explicit mathematical relationships and proof exposition; it supplies no independent proof assessment or fresh audit of every external source.

## Scope of the analytic criterion in the abstract

Required clarification in [the abstract](main.tex), at "a second criterion of an analytic nature using liberation dual systems": state the additional assumption that \(X_i-\lambda\) is regular for every \(i\) and every \(\lambda\in\mathbb C\).
Theorem 1.7 uses this assumption, while the abstract currently names only the liberation dual system.
Yin's [abstract policy](../../../../../profiles/Yin/writing/readme.md#abstract-concision) requires hypotheses needed for an accurate account of the result.
As an optional improvement in the following sentence, replace "further refines the second" with the concrete characterization by finite rank of fraction commutators.

## The zero-tuple condition for maximal Delta

Required clarification in [Subsection 1.1](sections/introduction.tex), at "there are no nonzero finite-rank operators": the nonzero object is the tuple, and some coordinates of a nonzero tuple may vanish.
State directly that, for \(T_i\in\mathcal F(H)\), the equality \(\sum_i[\rho(X_i),T_i]=0\) implies \(T_i=0\) for every \(i\).
This makes the quantifier and object explicit, consistently with Remark 2.8 and the [precise-object rule](../../../../../framework/rules/writing.md#precise-object-names).

## Density at the introduction of the common domain

Required clarification in [Subsection 1.2](sections/introduction.tex), immediately before Definition 1.6: describe \(\mathcal M\Omega\) as a dense subspace of \(H\), rather than giving only its set expression and inclusion in \(H\).
The [manuscript's introduction choice](../writing.md#introduction-and-explanatory-commentary) explicitly calls for this description at that location.
It also explains why the ensuing operator and adjoint domains are dense.

## Objects described in the Section 5 summaries

Required clarification in [the introduction's organization paragraph](sections/introduction.tex), at "proves independence of the fraction pair": identify the invariant quantities as the finite-rank property and, when finite, the rank of each fraction-commutator closure.
Lemma 5.2 does not assert independence of the operators themselves.
In the same sentence, replace the extra name "finite-rank certificates" with the already used "finite-rank solutions of equation (6)".
As an optional related improvement, the transition before Lemma 5.3 in [Section 5](sections/dual-system-criterion.tex), beginning "We next identify any finite-rank solution", can state that the coordinates equal the closures of the fraction commutators; the current transition omits the closures and shifts from a tuple to individual operators.
Keep overview sentences proportionate: an already explicit relationship need not be repeated as another displayed formula.

## Direct proof for finite sums in Lemma 3.1

Optional simplification in the proof of `lem:tensor-clearing` in [Section 3](sections/maximal-delta.tex), beginning "For simplicity of notation".
Write each \(k_i\) as a finite sum of simple tensors and choose common denominators for all of their factors at once.
One resulting tensor identity proves the stated result directly and avoids the detour through simple tensors followed by "The same argument applies to general finite sums".
Preserve the distinction between common left denominators for the first factors and common right denominators for the second factors.

## The auxiliary map used once in Theorem 1.4

Optional simplification in the implication \((5)\implies(1)\) in [Section 3](sections/maximal-delta.tex), at the definition of \(\Phi_{s,t}\).
Apply left multiplication by \(s^{-1}\) to the first tensor factor and right multiplication by \(t^{-1}\) to the second directly, briefly noting that these operations preserve the balancing relation.
The separate name \(\Phi_{s,t}\) serves only this application; omitting it removes a translation between notation and the operation under the [notation-in-context rule](../../../../../framework/rules/writing.md#notation-in-context).
Retain the well-definedness justification and the resulting equality \(u\otimes_F1=1\otimes_Fu\).

## Mathematical tuple in the proof of Lemma 2.2

Required typesetting correction in [Subsection 2.2](sections/preliminaries.tex), at "Extend (1,u) to a basis": put the tuple in math mode as `$(1,u)$`.
The current source prints its mathematical entries as ordinary text.

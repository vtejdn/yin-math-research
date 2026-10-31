---
author: Yin
---

# Bounded Linearization: Exploratory Evidence

Current follow-up, 2026-09-09: the scaled construction is completed and reviewed in [Yin_C_F0011](../claims/Yin_C_F0011_v1.md#yin_c_f0011), with its [full-chain audit](../audits/reviews/Yin_R_F0006_v1.md).
That authoritative proof establishes the strict bounded-intersection phenomenon under free-field embedding alone and proves that the scaled tuple has no bounded dual system.

Date: 2026-09-09; preserves exploration performed on 2026-09-08 by another AI agent.
Context: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), with the subsequent [MSY23 source audit](../audits/literature/MSY23/readme.md).
**Status: exploration and proof fragments, not an independently reviewed claim.
No new claim ID is allocated.**

The authoritative arguments for [Yin_C_F0004](../claims/Yin_C_F0004_v1.md#yin_c_f0004), [Yin_C_F0005](../claims/Yin_C_F0005_v1.md#yin_c_f0005), and [Yin_C_F0006](../claims/Yin_C_F0006_v1.md#yin_c_f0006), and the mechanism recorded in [Yin_S_F0004](../strategies/Yin_S_F0004.md#s_f0004), are not reproduced here.

## Question and Reuse Boundary

The exploration asks whether an affiliated free-field realization, together with boundedness of a scalar rational output, alone supplies a linear representation with a bounded matrix inverse.
A putative universal assertion would read:

\[
F_X\cong\mathbb C\!\left(\!\left\langle x_1,\ldots,x_d\right\rangle\!\right),
\quad f\in F_X\cap M
\quad\Longrightarrow\quad
f=uA(X)^{-1}v,
\quad A(X)^{-1}\in M_N(M),
\tag{L}
\]

where A is a polynomial matrix and u,v are scalar rows and columns.
Allowing polynomial rows and columns does not avoid the C*-algebra obstruction considered below.
A linear pencil is a special case of a polynomial matrix.

Assertion (L) has weaker assumptions than the bounded-dual setting of [Yin_C_F0001](../claims/Yin_C_F0001_v1.md#yin_c_f0001).
It would be a stronger general-purpose descent theorem than Yin_C_F0001 requires.
The historical test concerns this ambient-only shortcut and does not satisfy the original bounded-dual premise.
C_F0011 proves that the scaled tuple has no bounded dual system.
The stronger bounded-dual setting retains its separate [C_F0012 counterexample](../claims/Yin_C_F0012_v1.md#statement).

The published theorem actually available is [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004), with its affiliated ambient algebra, together with the bounded-dual implication in [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005).
The distinct domain-quantified bounded representation theorem is recorded in [MSY23-U003](../audits/literature/MSY23/Yin_U003.md#msy23-u003).
This note does not replace any of those precise interfaces by (L).

## Scaled-Semicircular Model

The complete scaled-semicircular construction, affiliated identities, continuous-section exclusion and absence of bounded duals are retained in [C_F0011](../claims/Yin_C_F0011_v1.md#yin_c_f0011).
Its proof covers every faithful full-support probability measure in the stated model.
The distinct weighted-measure compression diagnostic below retains its original calculation and scope.

## Optional Localization Fragment: No Dual-System Conclusion

The central localization used by the following compression test is established in [C_F0011, Section 1](../claims/Yin_C_F0011_v1.md#1-recovering-the-center-and-the-whole-tensor-product).

The elementary estimate it was meant to enable is worth preserving conditionally.
If `z_epsilon=1_(0,epsilon](t)` belongs to N and D_i is a bounded operator satisfying `[D_i,X_i]=P_Omega`, centrality and compression would give

\[
\tau(z_\epsilon)
=\|z_\epsilon P_\Omega z_\epsilon\|
\le2\|D_i\|\,\|X_i z_\epsilon\|
\le4\epsilon\|D_i\|.
\]

For `dnu=dt/(2 sqrt(t))`, the left side is `sqrt(epsilon)`; for `dnu=dt`, it is epsilon.
Thus the measure choice changes this proposed diagnostic.
This is the original conditional compression calculation, with the localization now supplied by C_F0011.
The two measure choices remain distinct; C_F0011 retains its separate complete no-bounded-dual argument.

## A Further Obstruction to Copying the Wick-Basis Method

Yin_S_F0004 already records the exact residual, realization, and norm-estimate structures required to reuse Miy22.
A narrower extra observation from the exploratory source search is that replacing Wick polynomials by arbitrary **orthogonal free Appell polynomials** does not automatically provide a broad new model.

The exact inspected monic free Appell recurrence, original edition/passages and source-reading limits are owned by [Ans04-U001](../audits/literature/Ans04/Yin_U001.md#ans04-u001).
For a nondegenerate selfadjoint orthogonal polynomial family, comparison with the three-term recurrence forces all free cumulants of degree at least three to vanish, so this particular family remains shifted/scaled semicircular.
This local comparison does not classify every possible residual model and leaves nonorthogonal expansions and more general finite-state recurrences available.

## Historical Bounded-Intersection Search Scope

The 2026-09-08 search was triggered by the proposed use of free-field identification to infer bounded scalar closure or a bounded matrix inverse.
It first inspected the published MSY23 pp. 41-48, then the relevant closure/ambient-algebra passages of two public older artifacts:

- [arXiv:1805.04150v2](https://arxiv.org/pdf/1805.04150v2), 70 pages, version dated 2020-04-16: contents, introduction, and boundedness/closure search hits were inspected.
  Its affiliated realization statements did not provide the sought bounded-intersection formula in those inspected passages.
  This is an older MSY artifact with a distinct arXiv identifier, not an interchangeable page reference to the registered 1905.08187v2 artifact or the published MSY23 PDF.
- [Sheng Yin's public thesis](https://www.yin-sheng.xyz/static/files/thesis.pdf), 109 PDF pages: Sections IV.5 and relevant V.2/V.3 passages were inspected in parsed primary text.
  The chosen ambient algebra in the relevant realization statements is L0; Remark V.2.6, printed pp. 74-75 / PDF pp. 84-85, identifies affiliated closures with the free field.
  The thesis was not bibliographically identified or audited in full here and is not the local manuscript keyed Unt20.

The published-paper portion is superseded as source evidence by the completed MSY23 units, especially MSY23-U003, MSY23-U004 and MSY23-U005.
The older-artifact searches are retained only to state what was actually inspected and avoid repeating an unchanged search.
Their bounded negative outcome proves neither nonexistence of a bounded-intersection theorem in the literature nor novelty of any proposed construction.
The search paused because the user prioritized full auditing of the published paper; it can be reopened with a specific theorem locator or changed hypothesis.

## Retained scope

This historical search does not remove the bounded-dual or finite-rank premises of the original C_F0001.
The actual refutation and its complete review evidence belong to C_F0012 and its selected decisions.

---
author: Yin
---

# Conditions for Descent from Affiliated to Bounded Division Closure

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Record kind: Claim/proof module and exploration checkpoint.
Authorization: the user's second autonomous research goal, coordinated by root as Yin_T_F0003/Yin_S_F0013.
This record retains the exploration and source comparison; [C_F0087](../claims/Yin_C_F0087_v1.md#yin_c_f0087) and [C_F0088](../claims/Yin_C_F0088_v1.md#yin_c_f0088) own the extracted statements, proofs and selected assessment decisions, with navigation in the [Claim index](../claims/index.md).

The question is the equality
\[
\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X\cap\mathcal M
=\operatorname{Div}_{\mathcal M}\mathcal A_X.
\tag{B}
\]
It differs from the stronger analytic assertion that every affiliated rational element in \(L^2(\mathcal M)\) is bounded.
In particular, [Yin_C_F0019](../claims/Yin_C_F0019_v1.md#yin_c_f0019) remains an obstruction to that stronger assertion.
The normal bounded-dual counterexample [Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012) remains valid.

## Reuse and Source Check

The initial local search read [Yin_C_F0006](../claims/Yin_C_F0006_v1.md#yin_c_f0006), [Yin_C_F0008](../claims/Yin_C_F0008_v1.md#yin_c_f0008), [Yin_C_F0015](../claims/Yin_C_F0015_v1.md#yin_c_f0015), [Yin_C_F0020](../claims/Yin_C_F0020_v1.md#yin_c_f0020), [Yin_C_F0021](../claims/Yin_C_F0021_v1.md#yin_c_f0021), and the [model synthesis](Yin_L_F0003_v1.md#boundedness-model-synthesis).
In particular, Yin_C_F0021, Section 2, already reduces one-coordinate division expressions to scalar fractions.
Yin_C_F0006 already covers specified elementary rational coordinate changes and is not re-registered here.
Neither Yin_C_F0021's stronger positive-power-subspace result nor its proof is replaced.

Primary-source searches on 2026-09-11 used the phrases `bounded rational function single operator Bezout inverse division closure affiliated operators`, `division closure principal ideal`, `division closure Bezout`, and `rational closure one variable operator`.
They identified classical commutative fraction/localization mechanisms and free-group power-series results, but no exact previously registered theorem in the arbitrary ambient-algebra scope below.
This bounded search does not establish novelty.
The argument uses the elementary principal-ideal/Bezout mechanism, not a new result about polynomial gcds.

### Checked Hungerford input

The exact accepted inputs on principal ideals, polynomial Euclidean division and Bezout coefficients, together with their original printed/PDF locators and proof inspection limits, are retained in [Hun74-U006](../audits/literature/Hun74/Yin_U006.md#exact-retained-statement-and-proof-inspection-depth).
The ambient-algebra application is proved in [C_F0087](../claims/Yin_C_F0087_v1.md#yin_c_f0087-p1-proof).

## Rational Changes of Coordinates: Exact Transfer Boundary

This is a direct closure observation used for route selection, not a re-registration of [Yin_C_F0006](../claims/Yin_C_F0006_v1.md#yin_c_f0006).
If two tuples \(X,Y\subset\mathcal M\) satisfy
\[
Y_j\in\operatorname{Div}_{\mathcal M}\mathcal A_X,
\qquad
X_i\in\operatorname{Div}_{\mathcal M}\mathcal A_Y
\quad\text{for every }i,j,
\tag{10}
\]
then their bounded division closures coincide, by minimality, and their affiliated division closures coincide for the same reason.
Therefore (B) transfers in both directions.
This argument requires no new formulas for dual operators and no normality assumption.
It extends the algebraic transfer observation to arbitrary finite rational coordinate changes whose intermediate inverse operations and inverse coordinate formulas are all admissible in \(\mathcal M\).

Equality of affiliated fields and generation of the same \(W^*\)-algebra do not imply (10).
Even equality of the generated \(C^*\)-algebras is insufficient, as the [classical cusp specialization in C_F0088](../claims/Yin_C_F0088_v1.md#yin_c_f0088) shows.



## Next Multivariable Discriminator

Yin_C_F0087 proves a commutative principal-ideal sufficient condition; it does not imply that (B) is stable under freely combining several one-coordinate algebras.
In a free product, a scalar rational expression need not be a single polynomial quotient, and a two-generated ideal need not be principal.
Thus the one-coordinate Bezout argument cannot be iterated solely from freeness of the marginals.

The next target is to test free-product stability under **freely independent normal coordinates**, separating this from the already known semicircular/Haar and bounded-rational-coordinate families.
A specific tractable comparison is a free product of finite cyclic group algebras: it gives freely independent finite-spectrum normal variables and a virtually free group.
The finite-index route initially appeared to need another bounded scalar elimination argument.
The subsequent Yin_C_F0089 proof instead reconstructs the bounded operator from finitely many scalar coefficients in the known subgroup closure.
This resolves that finite-index route; general free-product stability remains open.

The first web search for this discriminator used `rationality criterion virtually free`, `division closure free products bounded`, and `rational closure free projections`.
It found group-localization and Atiyah-property sources, but those conclusions alone are not (B).
Existing Haagerup or rapid-decay estimates likewise do not supply the missing finite-state/coefficient or bounded scalar reconstruction step.


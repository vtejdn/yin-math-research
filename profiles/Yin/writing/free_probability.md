# Yin: Free-Probability Writing Policy

## Default policy

Apply this subfield policy when the actual topic and intended human readership are free probability and the relevant operator-algebra setting; a research-line letter does not determine applicability.
Inherit the [author-wide policy](readme.md) where this file has no applicable override.
Manuscript choices take precedence under the [selection rule](../../../framework/rules/preferences.md#scope-and-adoption).

<a id="audience"></a>
## Audience and Background

The default audience is researchers in free probability and the operator-algebra setting of the paper.
A von Neumann algebra needs no basic definition or citation merely for the term.
State the actual finiteness, state/trace properties and representation required by the argument.
This exemption does not remove citation obligations for an external theorem or proof.
A manuscript for another audience can select a different explanation level.

<a id="operator-restriction-notation"></a>
## Operator Restriction Notation

Scope: Yin's free-probability and related operator-algebra writing.

Use a superscript circle for an operator restricted to a specified domain: for example, $D_i^\circ:=D_i|_{\mathcal M\Omega}$, rather than $D_{i,0}$.
Define the domain at introduction.
Write its adjoint as $(D_i^\circ)^*$ and its closure as $\overline{D_i^\circ}$, retaining any separately defined symbol such as $\widehat D_i$ for that closure.
Distinguish the original operator, its restriction and the closure of the restriction; do not identify the latter with the closure of the original operator without justification.
This is a notation preference, not a claim of a standard literature convention.

## Projection Notation and Local Explanations

Use $P_\Omega$ directly for the orthogonal projection onto $\mathbb C\Omega$, without introducing the alias $P$.
When this notation first appears in a theorem statement, place its brief explanation immediately after the complete statement, rather than inserting a detached notation sentence into the preceding discussion.

## Community References

### Terminology

For dual systems, use the convention $[X_j,D_i]=\delta_{ij}P_\Omega$, with the generator first, as in MSY23 Definition 6.1.
Voiculescu's original Definition 5.1 in Voi98 uses bounded selfadjoint $Y_i$ with $[X_j,Y_i]=\mathrm i\delta_{ij}P_\Omega$; the normalized convention is obtained by $D_i=-\mathrm iY_i$.
When adapting sources with $[D_i,X_j]=\delta_{ij}P_\Omega$, negate their dual operators and all affected construction formulas.
Keep boundedness, selfadjointness and domain assumptions explicit: adopting the sign convention does not identify an unbounded-domain extension with either source's bounded definition.
Preserve original source quotations and fixed inspection records.

For Hochschild chain differentials in Yin's free-probability writing, follow the $d$ notation of Wei94 Section 9.1.1 and write $d_n$ for its degree-n component, in particular $d_1$ in degree one.
Keep the face maps $\partial_i$ distinct from the alternating-sum differential.
This is the selected notation for this scope, not a claim that Wei94 uses $d$ exclusively: Section 9.6.5 also uses $b$.
See the [source observations](../../../mathematics/audits/literature/Wei94/Yin_U001.md#differential-notation-observations).


Use **free Haar unitaries** for a freely independent family of Haar unitaries, including the canonical generating unitaries in the free-group setting.
Avoid shortening this expression to **Haar generators** or **free Haar generators**.
When their generating role matters, state that role separately.

Use **von Neumann tensor product** for the completed tensor product $\mathcal M\bar\otimes\mathcal N$ of von Neumann algebras, and **Hilbert space tensor product** for $H\bar\otimes K$.
Reserve $\otimes$ for the algebraic tensor product and $\bar\otimes$ for a completion, following CS05 Section 1.1; CS05 Section 2.2.3 names $\mathcal M\bar\otimes\mathcal M^o$ the von Neumann tensor product.
Do not use **spatial tensor product** for either of these in Yin's free-probability writing.

Use **the usual trace on $\mathcal B(H)$** for the trace $\operatorname{Tr}$ on the bounded operators of a Hilbert space, whose value on a positive operator is its sum over any orthonormal basis.
Cite AP18 Section 8.4 where a locator is wanted; that source writes "the usual trace $\operatorname{Tr}$ on $B(\mathcal H)$" and records its basis independence.
Do not call this object **operator trace**, and do not leave it unnamed where it is first used to define an operator ideal.
Reserve **canonical trace** for the canonical normal faithful semifinite trace $\widehat\tau$ on the commutant $\mathcal B(\mathcal H_{\mathcal M})$ of a right $\mathcal M$-module (AP18 Section 8.4, Proposition 8.4.2), which supplies the von Neumann module dimension.
The two names must not denote the same object in one manuscript.

Use **von Neumann dimension** for the module dimension $\dim_{\mathcal M}$ entering $\Delta$-type definitions, and cite Luc02 Definition 1.10 for the name; that definition sets $\dim_{\mathcal N(G)}(V)=\operatorname{tr}_{\mathcal N(G)}(\operatorname{id}_V)$ for a Hilbert $\mathcal N(G)$-module.
Since its setting is a group von Neumann algebra, a sentence using the dimension of a module over a general tracial von Neumann algebra also needs the matching definition: CS05 Definition 2.10, which names the same object the **Murray-von Neumann dimension** over $\mathcal M\bar\otimes\mathcal M^o$, or AP18 Definition 8.5.4, which names it **the $M$-dimension**, $\dim(\mathcal H_M)=\widehat\tau(\operatorname{Id}_{\mathcal H})$.
Do not attribute the name von Neumann dimension to AP18 or to MSY23: AP18 uses $M$-dimension, and MSY23 writes only the symbol $\dim_{\mathcal M\bar\otimes\mathcal M^{\mathrm{op}}}$ without naming it.

### Reference Collection

| Work | Role and scope | Source observation |
| --- | --- | --- |
| Miy22 | Rationality in free semicircular operators: definitions, characterizations and proofs. | [Miy22](../../../mathematics/audits/literature/Miy22/readme.md#presentation-observations) |
| MS23 | q-Gaussian dual and conjugate systems. No passage note is recorded; consult the actual source for the needed passage. | Not recorded. |
| Miy26 | Spectra of polynomials in semicircular and circular operators. | [Miy26](../../../mathematics/audits/literature/Miy26/readme.md#integrability-terminology) |
| MS17 | Free-probability/random-matrix terminology and background exposition. | [MS17](../../../mathematics/audits/literature/MS17/Yin_U001.md#probability-and-freeness) |
| NS06 | Combinatorial free-probability terminology, notation and background. | [NS06](../../../mathematics/audits/literature/NS06/Yin_U002.md#ns06-definition-recheck) |

These community designations have no special permission to copy prose.
Use the [community-reference rule](../../../framework/rules/writing.md#use-and-reuse), preserving attribution and actual inspection scope.
They do not certify a whole work or create further familiarity exemptions.
Inherit Yin's author-wide models, Hun74 algebraic terminology and conditional object notation without duplicating those choices here.

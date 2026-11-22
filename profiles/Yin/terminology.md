# Yin: Mathematical Terminology and Notation

These are Yin's choices for the writing and slides specified below.
When discussing those texts, use their conventions; a more specific manuscript choice takes precedence.

<a id="free-field-terminology"></a>
## Free Field Terminology

Scope: Yin's mathematical writing.

Use **free field** as the standard term for the universal division ring of fractions of a free polynomial algebra.
Do not use **free skew field** for this object.

<a id="mathematical-symbols"></a>
## Mathematical Symbols

Scope: Yin's mathematical writing and presentation slides.

| Object | Preferred notation | Meaning and source boundary |
| --- | --- | --- |
| Linear functionals | `\varphi`, with indices such as `\varphi_j` when needed. | Default notation for linear functionals. |
| Projections | `\pi`, with indices such as `\pi_1` and `\pi_2` when needed. | Default notation for projections, including quotient maps; more specific conventions such as `P_\Omega` take precedence. |
| Free field | Use the user's supplied `\moverlay`, `\plangle` and `\prangle` macros to superimpose round parentheses with `<` and `>`, with the coefficient field in front. | Preserve the formal-field/evaluated-division-closure distinction. |
| Affiliated operators | `L^0(\M)`, with `\M=\mathcal M`. | The *-algebra of closed densely defined operators affiliated with the specified finite tracial von Neumann algebra. Sums and products use affiliated closures; this change of notation adds no domain hypothesis. |
| Algebra-generated GNS vectors | `\M\Omega` for the subspace; `x\Omega` for an individual vector with `x\in\M`. | In a tracial GNS space $H=L^2(\M,\tau)$ with $\Omega=1$, $\M\Omega=\{x\Omega:x\in\M\}$ is a dense subspace used for operator domains. Do not call its elements "bounded vectors"; use $\M\Omega$ or say "vectors of the form $x\Omega$ with $x\in\M$." |
| Finite-rank operators | `\F(H)`, with `\F=\mathcal F`. | The finite-rank bounded operators on H, matching MSY23, p. 13. Do not use this symbol as an abbreviation for the evaluated free field. |
| Finite-dimensional Fuglede-Kadison determinant | Use uppercase `\Delta_m(B)=\lvert\det B\rvert^{1/m}` for `B` in `M_m(\mathbb C)`, and the corresponding dimension subscript for other matrix sizes. Do not use lowercase `\delta` for this determinant. | The subscript records the matrix size and the normalized matrix trace. This changes notation only; Dirac masses, Kronecker symbols and unrelated uses of lowercase delta are unaffected. |
| Random-matrix expectation | Write the composite as `\mathbb E\circ\tr_N`, with the composition sign between the expectation and the normalized trace; do not write the bare product `\mathbb E\tr_N`. | The expectation is applied after the normalized trace, so the composition order is visible. This is a notation choice, not a probability-model hypothesis. |
| Limits | Use `\rightarrow` by default. | Use `\downarrow` when the decreasing approach or approach from above matters to the argument. |

<a id="operator-restriction-notation"></a>
## Operator Restriction Notation

Scope: Yin's free-probability and related operator-algebra writing.

Use a superscript circle for an operator restricted to a specified domain: for example, $D_i^\circ:=D_i|_{\mathcal M\Omega}$, rather than $D_{i,0}$.
Define the domain at introduction.
Write its adjoint as $(D_i^\circ)^*$ and its closure as $\overline{D_i^\circ}$, retaining any separately defined symbol such as $\widehat D_i$ for that closure.
Distinguish the original operator, its restriction and the closure of the restriction; do not identify the latter with the closure of the original operator without justification.
This is a notation preference, not a claim of a standard literature convention.

Use $P_\Omega$ directly for the orthogonal projection onto $\mathbb C\Omega$, without introducing the alias $P$.

## Free-Probability Terminology

Scope: Yin's free-probability writing, for the mathematical objects indicated below.

For dual systems, use the convention $[X_j,D_i]=\delta_{ij}P_\Omega$, with the generator first, as in MSY23 Definition 6.1.
Voiculescu's original Definition 5.1 in Voi98 uses bounded selfadjoint $Y_i$ with $[X_j,Y_i]=\mathrm i\delta_{ij}P_\Omega$; the normalized convention is obtained by $D_i=-\mathrm iY_i$.
When adapting sources with $[D_i,X_j]=\delta_{ij}P_\Omega$, negate their dual operators and all affected construction formulas.
Keep boundedness, selfadjointness and domain assumptions explicit: adopting the sign convention does not identify an unbounded-domain extension with either source's bounded definition.
Preserve original source quotations and fixed inspection records.

<a id="liberation-derivation-notation"></a>
Use $\delta_i$ rather than $\gamma_i$ for liberation derivations in Yin's free-probability writing, with $\delta_i^\circ$ for their restrictions to specified polynomial domains.

For Hochschild chain differentials in Yin's free-probability writing, follow the $d$ notation of Wei94 Section 9.1.1 and write $d_n$ for its degree-n component, in particular $d_1$ in degree one.
Keep the face maps $\partial_i$ distinct from the alternating-sum differential.
This is the selected notation for this scope, not a claim that Wei94 uses $d$ exclusively: Section 9.6.5 also uses $b$.
See the [source observations](../../mathematics/audits/literature/Wei94/Yin_U001.md#differential-notation-observations).

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

---
author: Yin
---

# Bar19: Kielak's amenability and Ore-domain equivalence

<a id="bar19-u001"></a>
## Source, theorem and actual review

The [inspected edition](readme.md#arxiv-v2) is arXiv:1605.09133v2.
On 2026-11-10 the source reviewer read the entire Kielak appendix, pp. 5–6, and checked its dependency on the complete Section 2 construction, pp. 3–5, including the combinatorial lemma and the generic linear-map step.
The relevant pages were visually checked, so the formula issues below are not inferred from OCR alone.
The reviewer was separate from current project proof development; this unit is source evidence, not a review of a project Claim.
The source's literal slips are identified separately from the checked reconstruction of its intended argument.
The reviewer supplied and self-checked the corrected conventions below; that act alone does not constitute a separate independent acceptance of the repaired text.

Theorem A.1 states: for a group \(G\) and a commutative field \(K\) such that \(KG\) has no zero divisors,

\[
G\text{ is amenable}
\quad\Longleftrightarrow\quad
KG\text{ is an Ore domain}.
\]

The domain hypothesis applies to the whole theorem.
It is not a theorem that every torsion-free group algebra is a domain, or that every group ring has classical fractions exactly when its group is amenable without that hypothesis.
The theorem concerns ordinary group algebras over fields; this appendix does not state the converse for arbitrary crossed products over arbitrary division rings.
The latter extension must not be inferred merely from [Lin06's broader forward implication](../Lin06/Yin_U001.md#amenable-domain-localization).

<a id="ore-definition-and-printed-slips"></a>
## Ore convention and literal slips in the preprint

Use the [right Ore convention checked in Lin06](../Lin06/Yin_U001.md#crossed-product-and-ore-conventions):
for \(a\in A\) and nonzero \(s\in A\), one seeks \(b\in A\) and nonzero \(t\in A\) with \(at=sb\).
For a domain this permits right fractions \(as^{-1}\), and their classical quotient ring is a division ring.
For \(KG\), the group-inversion anti-automorphism makes the left and right versions equivalent.

The displayed and prose formulas in the retained edition need the following corrections when reconstructing the proof.

| Location | Literal source issue | Checked interpretation |
| --- | --- | --- |
| Appendix opening, p. 5 | The purported Ore condition is \(at=bs\). Taken literally it is automatic in every ring, by taking \(t=s\), \(b=a\), so it cannot define Ore localization. | Read \(at=sb\), a common right multiple. |
| Forward proof, p. 5 | The source calls \(as=bt\) a linear system in the variables \(b,t\). With both \(b,t\) variable this is not that homogeneous linear system. | Use \(at-sb=0\) with \(a,s\) fixed. |
| Section 2, p. 4 versus p. 5 | The displayed operator uses \(\phi(sg)\), but the support argument at \(sf\) isolates the contribution \(\phi(f)\). | Use the consistent left-convolution convention \(\Theta\phi(g)=\sum_s\alpha_s\phi(s^{-1}g)\). |
| First sentence of p. 5 | It says “admits mutually erasable patterns” while proving injectivity on nonzero finitely supported inputs. | The argument and its conclusion require “admits no mutually erasable patterns”. |

These are concrete issues in the inspected preprint.
They do not refute the intended theorem: the corrected proof below checks the relevant implications.
The journal edition was not obtained, and no source-author confirmation or journal correction is claimed.

<a id="amenability-and-finite-support-conventions"></a>
## Amenability and the finite-support model

The paper uses the **Følner criterion** as its definition of amenability: for every finite \(S\subseteq G\) and every \(\varepsilon>0\), there is a nonempty finite \(F\subseteq G\) with \(|SF|<(1+\varepsilon)|F|\).
The intended nonempty condition is necessary for the strict inequality and for division by \(|F|\) below.
Replacing left translates by right translates gives an equivalent criterion by group inversion.

For a field \(L\), identify finitely supported functions \(G\to L^n\) with \((LG)^n\).
The left-convolution rule

\[
\Theta\phi(g)=\sum_{s\in S}\alpha_s\phi(s^{-1}g),
\qquad \alpha_s\in M_n(L),
\]

is multiplication by a matrix over \(LG\) on columns.
It is a homomorphism of right \(LG\)-modules.
Its support is contained in \(SF\) when \(\phi\) is supported on \(F\).
The fixed multiplication order is what permits the later tensor product \(-\otimes_{KG}Q\) to use a flat left \(KG\)-module.

<a id="amenable-direction"></a>
## Amenability implies Ore: the complete dimension argument

Fix \(a,s\in KG\), \(s\ne0\), and let \(S\) contain their finite supports.
Amenability supplies a nonempty finite \(F\) with \(|SF|<2|F|\).
The linear map

\[
KF\oplus KF\longrightarrow K(SF),\qquad (t,b)\longmapsto at-sb
\]

has more unknowns than equations, hence a nonzero kernel vector.
If \(t=0\), then \(sb=0\); since \(s\ne0\) and \(KG\) is a domain, \(b=0\), contradicting that choice.
Consequently \(t\ne0\), so \(at=sb\) verifies right Ore.
The case \(a=0\) is harmless: one may take \(b=0\) and any nonzero \(t\).
The anti-automorphism gives left Ore, and the usual domain localization is a division ring.

This checks the entire forward argument, including the otherwise omitted reason that the denominator is nonzero.
The source attributes it to Tamari.
The domain hypothesis is used after the dimension count; a nonzero solution in a ring with zero divisors would not necessarily provide a regular denominator.

<a id="nonamenable-linear-injection"></a>
## The nonamenable finite-support injection

For the converse, the appendix needs an injective map from a larger finite free module to a smaller one.
Section 2 produces it without assuming that \(G\) contains a free subgroup.
Nonamenability gives a finite \(S_0\) and \(\varepsilon>0\) such that \(|S_0F|\ge(1+\varepsilon)|F|\) for every nonempty finite \(F\).
Choose \(k\) with \((1+\varepsilon)^k>1+k\log|S_0|\), and put \(S=S_0^k\), \(m=|S|\).
Then

\[
|SF|>(1+\log m)|F|.
\]

Lemma 2.1 constructs a finite set \(Y\) and subsets \(X_s\), \(s\in S\), with sufficiently many coordinates unique to \(s\) within any prescribed \(T\subseteq S\).
Its underlying \(Y\) is the set of cycles marked by their ambient permutations in the symmetric group on \(m\) letters.
The two counts in the proof are

\[
|Y|=m!\sum_{j=1}^m\frac1j,\qquad
\left|X_s\setminus\bigcup_{t\in T\setminus\{s\}}X_t\right|=\frac{m!}{|T|}.
\]

The first is the cycle count by length; the second counts cycles meeting \(T\) precisely at \(s\) and uses the binomial summation displayed in (2.2).
The harmonic-number inequality is strict for \(m\ge2\).
Taking sufficiently many disjoint copies therefore leaves enough slack to add one new coordinate outside every \(X_s\).
For the enlarged \(Y\), with \(n=|Y|\), write

\[
X_{s,T}=X_s\setminus\bigcup_{t\in T\setminus\{s\}}X_t.
\]

Then \(|X_{s,T}|\ge n/((1+\log m)|T|)\), while \(\bigcup_sX_s\ne Y\).
The extra coordinate will make one output row identically zero.

Choose linear maps \(\alpha_s:L^Y\to L^{X_s}\subseteq L^Y\) such that every vertically stacked family of row restrictions \(\alpha_{s,T_s}\), with at least \(n\) rows in total, has rank \(n\).
There are finitely many such requirements.
For each requirement, a selected \(n\)-row determinant is a nonzero polynomial in distinct row variables: specialize those rows to the identity to verify this in every characteristic.
The finite product of these determinant polynomials is therefore nonzero over any field.
Over an infinite field \(K\), a suitable choice exists already in \(L=K\).
Over a finite \(K\), it exists in a sufficiently large finite extension \(L/K\), because a nonzero polynomial cannot vanish on all points of every sufficiently large finite extension.
This justifies the appendix's passage from the main text's “large enough finite field” to a finite extension of an arbitrary given field.
It does not require a special characteristic or a division-ring assumption on \(LG\).

Use the consistent convolution rule defined above.
For a nonzero input \(\phi\) with finite support \(F\), set

\[
\rho(g)=\frac1{|\{s\in S:g\in sF\}|}\quad(g\in SF).
\]

Double counting gives

\[
\sum_{f\in F}\sum_{s\in S}\rho(sf)=|SF|,
\]

so some \(f\in F\) satisfies \(\sum_s\rho(sf)>1+\log m\).
Let \(T_s=\{t\in S:sf\in tF\}\).
Then \(|T_s|=1/\rho(sf)\), and

\[
\sum_s|X_{s,T_s}|\ge
\frac{n}{1+\log m}\sum_s\rho(sf)\ge n.
\]

Writing \(\psi=\Theta\phi\), every contribution to \(\psi(sf)\) except the \(s\)-term is removed by projection to \(X_{s,T_s}\).
Indeed, an active \(t\)-term has \(t\in T_s\), its output lies in \(X_t\), and \(X_{s,T_s}\) avoids \(X_t\) for \(t\ne s\).
Thus

\[
\pi_{s,T_s}\psi(sf)=\alpha_{s,T_s}\phi(f).
\]

The stacked map is injective and \(\phi(f)\ne0\), so \(\psi\ne0\).
This proves injectivity on finitely supported configurations.
The extra coordinate outside \(\bigcup_sX_s\) makes one row of the corresponding \(n\times n\) matrix \(M\) identically zero.
Deleting that row yields an injective right \(LG\)-module map \((LG)^n\to(LG)^{n-1}\).
The cellular-automaton conclusions about forbidden patterns are not needed beyond this algebraic consequence.

<a id="ore-converse-and-flatness"></a>
## Ore implies amenability: scalar restriction and flatness

Let \(d=[L:K]\).
A \(K\)-basis of \(L\) identifies \(LG\), as a right \(KG\)-module, with \((KG)^d\).
Restricting scalars in the preceding injection therefore gives

\[
0\longrightarrow (KG)^{dn}\longrightarrow (KG)^{d(n-1)}.
\]

Suppose \(KG\) were an Ore domain, with classical division ring \(Q\).
Ore localization is flat as a left \(KG\)-module, so tensoring this injection on the right with \(Q\) gives

\[
0\longrightarrow Q^{dn}\longrightarrow Q^{d(n-1)}.
\]

Finite-dimensional right vector spaces over a division ring cannot admit this injection.
This contradicts nonamenability and proves the converse.

The flatness theorem is the single external ring-theoretic foundation explicitly cited at the appendix's final step: McConnell–Robson, Proposition 2.1.16.
Its original book proof was not inspected.
The required statement and module side agree with [Lin06's independently read localization interface](../Lin06/Yin_U001.md#crossed-product-and-ore-conventions).
The argument does not assume that an arbitrary embedding \(KG\hookrightarrow D\) into a division ring is flat.
For a free group, precisely that unjustified substitution would incorrectly contradict its known division-ring embeddings.

<a id="affiliated-applicability-boundary"></a>
## Applicability to actual affiliated closures

For \(\mathbb CG\) known to be a domain, this theorem classifies when scalar Ore fractions are available: exactly when \(G\) is amenable.
It identifies the obstruction without assuming a nonabelian free subgroup, and therefore extends the reach of [Lin06 Proposition 2.2](../Lin06/Yin_U001.md#free-subgroup-obstruction) in the domain/group-algebra setting.
It does not establish the domain premise merely from torsion-freeness.

Neither direction concerns the concrete map into \(U(G)\).
An actual affiliated localization still needs its nonzero denominators to be invertible in \(U(G)\).
Nonamenability rules out flat classical scalar localization, but it does not rule out matrix rational closure, Schur-complement expressions with valid affiliated inverses, or a division closure that is a division ring.
The free groups in [Lin93](../Lin93/Yin_U001.md#free-group-proof) exhibit exactly that distinction.

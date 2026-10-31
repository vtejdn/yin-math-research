---
author: Yin
---

<a id="lin00-u003"></a>
# Lin00-U003: Unbounded Domains and the Finite-Codimension Criterion

Inspected edition: [Yin's source notes](readme.md#yin-edition).

- Source: [Lin00, arXiv:math/9907075v1](../../../literature/pdf/Lin00--arxiv-v1.pdf), submitted 1999-07-12; seven PDF pages, with matching printed page numbers.
- Locator: the amplification and fraction-domain conventions on p. 2; the operator convention on p. 3; Proposition 1.2 and its domain clarification on p. 4; its complete proof on pp. 6-7.
  The French Proposition 2 on p. 2 has the same content.
- Record: 2026-10-10T09:14, authored under Yin.
  A separate audit agent directly read and reconstructed this part of the author's preprint of the published article and self-reviewed the reconstruction.
  Independent AI cross-reviews subsequently checked the complete unit, as recorded below.
- Assessment: the full proof of Proposition 1.2 is valid with **algebraic** finite codimension and equality of restriction domains.
  The infinite-amplification domain printed on p. 2 needs the square-summability correction below.
  The conclusion retains the scope and accepted inputs of [Theorem 1.1](Yin_U002.md#lin00-u002).

## Statement and precise domain convention

Put $H=\ell^2(G)$ and $K=\ell^2(E)\oplus\mathbb C$, where $E$ is the free $G$-set used in the source, and let $P:H\to K$ be its unitary.
Write $W=W(G)$, $U=U(G)$, and $D=D(G)$ for the group von Neumann algebra, its affiliated operators, and the division closure of $\mathbb CG$ in $U$, respectively.
If $E$ is a disjoint union of free orbits, use that decomposition to amplify operators from $H$ to $\ell^2(E)$.

For $\theta\in U$ write $\theta^+=\theta^E\oplus I_{\mathbb C}$ for the source's extension to $K$.
Proposition 1.2 says

$$
u\in D
\quad\Longleftrightarrow\quad
\text{there is a complex linear subspace }M\subseteq H,
\ \dim_{\mathbb C}(H/M)<\infty,
\text{ such that }(Pu)|_M=(u^+P)|_M.
$$

The restrictions here have domains $M\cap\operatorname{Dom}u$ and $M\cap P^{-1}\operatorname{Dom}u^+$, respectively.
Their equality includes both equality of these domains and equality of values there.
It does not mean merely equality on their common domain, does not require $M\subseteq\operatorname{Dom}u$, and does not assert that $M$ is closed.
The source explicitly requires domain equality immediately after the statement on p. 4.

For an arbitrary Hilbert direct sum $\bigoplus_{j\in J}H$, the correct amplification domain is

$$
\operatorname{Dom}\theta^+
=\left\{((h_j)_{j\in J},c):
(h_j)\in\bigoplus_{j\in J}H,\quad
h_j\in\operatorname{Dom}\theta\ (j\in J),\quad
\sum_{j\in J}\|\theta h_j\|^2<\infty,\quad c\in\mathbb C
\right\}.
$$

The printed Cartesian-product formula on p. 2 omits both the ambient Hilbert-sum restriction and, essentially, the image square-summability requirement.
Even after intersecting that Cartesian product with the Hilbert direct sum, the latter requirement is needed for an unbounded operator.
For example, take $H=\ell^2(\mathbb N)$, $\theta e_j=j e_j$, and place $h_j=e_j/j$ in the $j$th summand.
The input is square summable and each $h_j$ lies in $\operatorname{Dom}\theta$, but $\sum_j\|\theta h_j\|^2=\infty$.
The corrected operator is closed and densely defined: coordinate convergence proves closedness, while finite-support vectors with coordinates in $\operatorname{Dom}\theta$ prove density.
With finitely many orbits this additional summability issue disappears.

## Fractions and the scalar summand

If $u=s^{-1}a=bt^{-1}$ with $a,b,s,t\in W$ and $s,t$ nonzero divisors, the needed domain facts are

$$
\operatorname{Dom}u=\{h\in H:ah\in sH\},
\qquad tH\subseteq\operatorname{Dom}u,
\qquad ut=b\text{ on }H.
$$

Here $s^{-1}a$ is its natural closed composition: left multiplication by the inverse of the bounded injective operator $s$ is closed, and composition on the right by bounded $a$ remains closed.
The right fraction $bt^{-1}$ denotes its affiliated closure, which agrees with its natural product on $tH$; equality of that natural product's domain with $\operatorname{Dom}u$ is not needed.
The source's Lemma 2.2 gives injectivity and dense range of regular denominators, and the fraction-ring input ensures these facts describe the given affiliated element.

The same identities hold after amplification.
In particular,

$$
u^+=(s^+)^{-1}a^+,\qquad
t^+K\subseteq\operatorname{Dom}u^+,\qquad
u^+t^+=b^+.
$$

For infinitely many summands, membership $a^+k\in s^+K$ gives a square-summable vector of inverse images, so it gives exactly the corrected amplification domain, not merely coordinatewise membership.

The map $a\mapsto a^+$ is multiplicative, preserves adjoints, and respects inverse fractions, but is **not additive**.
If $e$ denotes projection onto the last scalar summand, then

$$
a^++b^+-(a+b)^+=e,\qquad
(\lambda a)^+-\lambda a^+=(1-\lambda)e.
$$

Thus the conventions on p. 2 must not be read as a complex-linear representation of $W$ on $K$.
Additive expansions involving this convention are exact only after including the displayed rank-one errors, or modulo finite-rank operators.
All such errors remain finite rank after bounded composition; multiplicative steps and the domain arguments below hold exactly.
The scalar summand can alternatively be made zero to obtain a linear nonunital amplification for bounded-coefficient calculations, but doing so changes the source's domain convention and requires its own comparison.
This unit retains $a^E\oplus I$ throughout.

## Forward implication, including both domain inclusions

Suppose $u\in D$.
Theorem 1.1 supplies $a,s\in S(G)$ with $u=s^{-1}a$ and regular $s$.
Its bounded criterion supplies finite rank of $Pa-a^+P$ and $Ps-s^+P$.
On $H$ put

$$
A=P^{-1}a^+P,\qquad S=P^{-1}s^+P.
$$

Then $a-A$ and $s-S$ have finite rank, $s,S$ are injective, and

$$
P^{-1}u^+P=S^{-1}A.
$$

Let $N=\ker(s-S)$.
Its codimension is finite and $L=sN=SN$.
Because $s$ and $S$ are injective, $sH/L$ and $SH/L$ are finite dimensional, and consequently $(sH+SH)/L$ is finite dimensional.
Choose an **algebraic** complement $F$ of $L$ in $sH+SH$, and an algebraic complement $Z$ of $sH+SH$ in $H$.
Then

$$
V=L\oplus Z,
\qquad H=V\oplus F,
\qquad V\cap(sH+SH)=L.
$$

Hence $V$ has finite codimension.
Set

$$
M=\ker(a-A)\cap a^{-1}(V).
$$

The map $H/a^{-1}(V)\to H/V$ induced by $a$ is injective, so $M$ also has finite codimension.
For $x\in M$ write $y=ax=Ax\in V$.
Then

$$
y\in sH\iff y\in L\iff y\in SH.
$$

This proves $M\cap\operatorname{Dom}u=M\cap\operatorname{Dom}(S^{-1}A)$.
If this membership holds, there is $n\in N$ with $y=sn=Sn$, so injectivity gives

$$
ux=s^{-1}ax=n=S^{-1}Ax=P^{-1}u^+Px.
$$

Multiplying by $P$ proves equality of the restrictions, including their domains.
This supplies the linear-algebra detail implicit in the source's choices of $N_1,N_2,M_3,M_4$ on p. 6 and checks both inclusions separately.
Those choices concern subspaces that need not be closed.
A finite-dimensional algebraic quotient does not by itself give a continuous quotient map or a closed complement; a stronger conclusion with closed $M$ is therefore not established by this argument.

## Reverse implication and both cleared commutators

Suppose the restrictions agree on an algebraic finite-codimension subspace $M$.
Choose $u=s^{-1}a=bt^{-1}$ with $s,t$ regular.
The preimage

$$
N=t^{-1}(M)=\{h\in H:th\in M\}
$$

has finite codimension.
For $h\in N$, the vector $th$ belongs to $M\cap\operatorname{Dom}u$, so domain equality gives $Pth\in\operatorname{Dom}u^+$ and

$$
Pbh=Put h=u^+Pth.
$$

After applying $s^+$ this gives

$$
(s^+Pb-a^+Pt)h=0.
$$

This bounded operator vanishes on a finite-codimension subspace, hence factors algebraically through the finite-dimensional space $H/N$ and has finite rank.
No closedness or density of $N$ is required.

The same equality of restrictions, transported by $P$, gives

$$
(uP^{-1})|_{PM}=(P^{-1}u^+)|_{PM},
$$

again with equal domains.
The space $PM$ has finite codimension in $K$.
Set $N'=(t^+)^{-1}(PM)$.
Since $t^+K\subseteq\operatorname{Dom}u^+$, for $k\in N'$ the transported domain equality gives $P^{-1}t^+k\in\operatorname{Dom}u$ and

$$
uP^{-1}t^+k=P^{-1}b^+k.
$$

Apply $s$ to obtain

$$
(sP^{-1}b^+-aP^{-1}t^+)k=0.
$$

The second bounded operator also has finite rank because $N'$ has finite codimension.
Thus both conditions defining $R'(G)$ hold, and Theorem 1.1 yields $u\in D(G)$.
In particular, the proof uses domain equality to justify multiplication on every vector considered; equality only on an unspecified common core would not supply this step.

## Dependencies, scope, and downstream use

The source's full Theorem 1.1, including rational bounded denominators and the bounded criterion, is an actual input to the forward implication; the identity $R'(G)=D(G)$ is an actual input to the reverse implication.
Their proof and external dependency boundaries are owned by [Lin00-U002](Yin_U002.md#lin00-u002).
The fraction representation and Lemma 2.2 interface, also reviewed there, are used with the exact domains displayed above.
Once these inputs hold, the present domain argument does not use the number of generators.
It therefore transfers at precisely the scope at which those inputs are accepted, and does not separately settle an infinite-rank extension of the bounded DR97 theorem.

This is an audit reconstruction of Proposition 1.2, not a new project Claim.
It distinguishes three notions: two cleared finite-rank expressions; agreement of unbounded operators on an algebraic finite-codimension restriction including domain equality; and a bounded finite-rank extension of a cleared commutator.
The source establishes the first two as rationality criteria in its free-group setting.
No general normal-tuple criterion, equivalence with a prescribed common core, closed finite-codimension refinement, or omission of one of the two cleared expressions is claimed here.

## Verification facts

Direct inspection used the retained preprint and local PDF renders of pp. 2-4 and 6-7, checked against extracted text.
The missing summability condition and scalar extension are visible in the PDF, not extraction artifacts.
The proof reconstruction above checks domain equality, both finite-rank conclusions, and all finite-codimension constructions.
No numerical test, proof assistant, external human review, complete journal/preprint comparison, or author-confirmed erratum was used.
The original PDF remains unchanged; these repairs and interpretation limits belong to this audit record.

At 2026-10-10T09:18 the independent AI review evidence was recorded: the algebra audit agent independently read the complete unit and verified the amplification-domain repair, fraction identities, the construction of $V$ and $M$, both domain inclusions, equality of values, and both reverse cleared defects.
The coordinating agent additionally reported its own and the interface audit agent's successful complete-unit checks.
These reviews found no remaining issue in this unit and requested only a bibliographic wording clarification.
The coordinating record in [U004](Yin_U004.md#lin00-u004) supplies the overall audit and dependency boundary; cross-review of this local proof does not expand those inputs.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Lin00, arXiv:math/9907075v1, submitted 1999-07-12, seven-page preprint retained as `Lin00--arxiv-v1.pdf`; published journal pagination is separate. |
| source-locator | Amplification and fraction domains p. 2; scalar-summand convention pp. 2-3; Proposition 1.2 and domain clarification p. 4; complete proof pp. 6-7; corresponding French Proposition 2 p. 2. Printed and PDF page numbers coincide. |
| inspection | 2026-10-10T09:14: direct statement and full local proof inspection with rendered-page confirmation; complete domain and algebraic finite-codimension reconstruction; infinite-sum domain correction and nonadditive scalar convention recorded. At 2026-10-10T09:18, successful independent AI checks of the entire reconstruction by the algebra, interface and coordinating agents were recorded, with no remaining local issue. Theorem 1.1 and external inputs retain the separately recorded U002/U004 scope; no formal check or journal-version transfer. |

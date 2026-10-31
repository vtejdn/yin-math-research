---
author: Yin
---

<a id="lin00-u002"></a>
# Lin00-U002: Fraction Independence, Algebraic Closure, and Theorem 1.1

Inspected edition: [Yin's source notes](readme.md#yin-edition).

- Source: [Lin00](../../../literature/pdf/Lin00--arxiv-v1.pdf), arXiv:math/9907075v1, 12 July 1999, seven pages.
  All locators below are the matching printed and PDF page numbers of this preprint, not journal pagination.
- Record: 2026-10-10, the algebra audit agent, under Yin; source reading, local reconstruction, and self-review.
  Independent cross-review, if completed, is recorded separately in [U004](Yin_U004.md#lin00-u004).
- Scope: Lemmas 2.1-2.3, Lemmas 3.1-3.5, and the proof of Theorem 1.1, pp. 4-6, with the definitions on pp. 2-3.
  The full seven-page source text was read for context.
  The domain criterion in Proposition 1.2 is audited in [U003](Yin_U003.md#lin00-u003).
- Assessment: the local algebraic chain is reconstructed below with explicit repairs.
  The final rationality conclusion uses the bounded free-group criterion from DR97, with the finite-generator scope of the existing DR97 audit.
  The separate infinite-rank interface is not silently assumed resolved here.

## Setting and precise conclusion

Write $M=W(G)$, $H=\ell^2(G)$, and $U=U(G)$ for the $*$-algebra of closed densely defined operators affiliated with $M$.
Sums and products in $U$ mean the closed affiliated sums and products.
A regular denominator is an element of $M$ that is not a zero divisor; it is invertible in $U$ and is injective with dense range on $H$.
Left and right fractions and their common denominators are the finite von Neumann algebra interfaces recorded in [U001](Yin_U001.md#lin00-u001).

Let $K=\ell^2(E)\oplus\mathbb C$ and let $P:H\to K$ be the Cayley-tree unitary.
For $c\in M$ denote its source-convention action on $K$ by

$$
\widetilde c=c^E\oplus I_{\mathbb C},
\qquad Q=0\oplus I_{\mathbb C}.
$$

Here $c^E$ is the bounded amplification along the free $G$-orbits of $E$.
This notation distinguishes the two operator spaces that the source denotes by the same letter.
For $u=s^{-1}a=bt^{-1}$, with $a,b,s,t\in M$ and regular $s,t$, put

$$
A(s,a;b,t)=\widetilde sPb-\widetilde aPt:H\longrightarrow K,
\qquad
B(s,a;b,t)=sP^{-1}\widetilde b-aP^{-1}\widetilde t:K\longrightarrow H.
$$

These are bounded maps on the whole indicated Hilbert spaces.
Let $R'$ mean that one fraction presentation has both defects of finite rank; let $R$ mean that every such presentation does.
Let $D$ be the division closure of $\mathbb CG$ in $U$, and let $S$ be its rational closure in $C_r^*(G)$, which the bounded DR97 theorem identifies with its scalar inverse closure there.
Theorem 1.1 asserts

$$
D=R=R',\qquad D\cap M=S,
$$

and that every $u\in D$ has left and right fractions with all coefficients and denominators in $S$.

## The scalar summand must be handled explicitly

The source's lift is multiplicative and preserves adjoints, but is not additive:

$$
\widetilde{cd}=\widetilde c\widetilde d,\qquad
\widetilde{c^*}=\widetilde c^{\,*},\qquad
\widetilde{c+d}=\widetilde c+\widetilde d-Q,
\qquad
\widetilde{zc}=z\widetilde c+(1-z)Q.
\tag{1}
$$

Consequently the two displayed additive equalities in Lemma 3.2 are not literally valid under the convention printed on p. 2.
Their errors have rank at most one.
All later finite-rank conclusions survive, but not because this lift is an algebra homomorphism.
The zero-action convention on the extra scalar summand used in DR97 differs from this lift by $Q$; for bounded commutators, and for each fraction defect above, this changes the map only by finite-rank terms.
Thus the two conventions give the same finite-rank tests.
No replacement of finite rank by compactness is involved.

## Lemmas 2.1 and 2.2: cancellation of finite rank

For bounded maps $\theta:H_0\to H_1$ and $\phi:H_1\to H_2$, injectivity of $\phi$ makes the restriction of $\phi$ to $\operatorname{im}\theta$ injective.
Hence finite rank of $\phi\theta$ implies finite rank of $\theta$.
If instead $\theta H_0$ is dense in $H_1$, continuity gives

$$
\phi H_1\subseteq\overline{\phi\theta H_0}.
$$

When $\phi\theta$ has finite rank its range is finite dimensional and therefore closed; thus $\phi$ has finite rank.
These two parts of Lemma 2.1 require boundedness and, in the second part, density; algebraic fraction identities alone would not suffice.

For $s\in M$, its kernel projection belongs to $M$.
If $s$ is regular, that projection is zero.
The same holds for $s^*$, so $sH$ is dense.
Equivalently this follows from invertibility in $U$, as in Lemma 2.2.
The amplification $\widetilde s=s^E\oplus I$ is also injective with dense range, including for infinitely many free orbits.
These are precisely the cancellation hypotheses used below.

## Lemma 2.3: a scalar shift is invertible

The argument works for an arbitrary element $u$ of the affiliated algebra of a finite von Neumann algebra with faithful normal tracial state.
Let $e_\lambda$ be the kernel projection of $u-\lambda$.
Then

$$
K_\lambda=\{x\in M:(u-\lambda)x=0\}=e_\lambda M.
$$

For distinct $\lambda_1,\ldots,\lambda_n$, the corresponding eigenspaces have algebraically direct sum.
Applying $\prod_{j\ne i}(u-\lambda_j)$ to a finite sum of eigenvectors isolates the $i$th component; every such vector is in the domains needed for this finite calculation.
The bounded row operator

$$
T:\bigoplus_{i=1}^n e_{\lambda_i}H\longrightarrow H,
\qquad T(\xi_1,\ldots,\xi_n)=\sum_i\xi_i
$$

is injective.
Its polar decomposition as a matrix over $M$ gives an initial projection $\operatorname{diag}(e_{\lambda_1},\ldots,e_{\lambda_n})$ and a final projection at most $1$.
The trace therefore gives

$$
\sum_{i=1}^n\tau(e_{\lambda_i})\leq1.
$$

Only countably many $e_\lambda$ can be nonzero: for each positive integer $k$, only finitely many have trace at least $1/k$.
Choose $\lambda$ with $e_\lambda=0$.
The affiliated polar decomposition of $u-\lambda$ then has initial projection $1$; finiteness of $M$ forces final projection $1$ as well.
Its affiliated inverse exists, so $u-\lambda$ is invertible in $U$.

This supplies the trace step attributed to the source's reference [8], without accepting an uninspected lemma from that paper.
On p. 5 the source says that $u-\lambda$ is a nonzero divisor **in $W(G)$**; that is a type error when $u$ is unbounded.
One may also repair it by writing $u-\lambda=s^{-1}a$ with $s,a\in M$ and regular $s$.
The vanished kernel implies that $a$ is injective; finite von Neumann algebra polar decomposition makes $a$ regular.
Thus both $a$ and $s$ are invertible in $U$, and so is $u-\lambda$.

## Lemma 3.1: one fraction presentation suffices

First change only the left fraction from $s^{-1}a$ to $s_1^{-1}a_1$.
Write the invertible affiliated element $ss_1^{-1}=x^{-1}x_1$ with $x,x_1\in M$ regular.
Then

$$
xs=x_1s_1,\qquad xa=x_1a_1.
$$

Multiplicativity in (1) gives exact identities

$$
\widetilde x_1 A(s_1,a_1;b,t)=\widetilde x A(s,a;b,t),
\qquad
x_1B(s_1,a_1;b,t)=xB(s,a;b,t).
$$

Injectivity of $\widetilde x_1$ and $x_1$, with Lemma 2.1(i), transfers finite rank to the new defects.

Next change $bt^{-1}$ to $b_1t_1^{-1}$.
Choose regular $y,y_1\in M$ with $ty=t_1y_1$; then $by=b_1y_1$.
For the fixed left fraction,

$$
A(s_1,a_1;b_1,t_1)y_1=A(s_1,a_1;b,t)y,
$$

$$
B(s_1,a_1;b_1,t_1)\widetilde y_1
=B(s_1,a_1;b,t)\widetilde y.
$$

The ranges of $y_1$ and $\widetilde y_1$ are dense.
Lemma 2.1(ii), not its injective version, now removes the right factors.
This proves $R'=R$ for the exact bounded defects above, with no choice of core or domain cancellation left implicit.

## Lemma 3.2: addition and the needed scalar closure

For $u,v\in R$, choose common left and right denominators

$$
u=s^{-1}a=bt^{-1},\qquad v=s^{-1}c=dt^{-1}.
$$

Using (1), the correct identities for $u+v$ are

$$
A(s,a+c;b+d,t)
=A(s,a;b,t)+A(s,c;d,t)+QPt,
$$

$$
B(s,a+c;b+d,t)
=B(s,a;b,t)+B(s,c;d,t)-sP^{-1}Q.
\tag{2}
$$

The added terms have rank at most one.
Thus the selected fraction defects of $u+v$ have finite rank, and Lemma 3.1 gives $u+v\in R$.

Before using scalar shifts in Lemma 3.3 one also needs scalar multiplication, rather than just addition.
For $z\in\mathbb C$,

$$
A(s,za;zb,t)=zA(s,a;b,t)+(z-1)QPt,
$$

$$
B(s,za;zb,t)=zB(s,a;b,t)+(1-z)sP^{-1}Q.
\tag{3}
$$

These prove $z u\in R$, including $z=0,-1$.
Group polynomials belong to $R$ because their bounded Cayley-tree commutators have finite rank, and Lemma 3.1 changes the fraction presentation.
This establishes the linear-space and additive-group properties actually used next.

## Lemma 3.3: multiplication

Choose scalars $\lambda,\mu$ so that $u-\lambda$ and $v-\mu$ are invertible.
If multiplication is proved for invertible members of $R$, (2)-(3) and

$$
uv=(u-\lambda)(v-\mu)+\mu u+\lambda v-\lambda\mu
$$

give the general case without assuming multiplicative closure in advance.

For invertible $u,v$, all numerators and denominators in a fraction presentation may be taken regular.
Write $u=s^{-1}a$, $v=t^{-1}b$, and $at^{-1}=w^{-1}c$ with $s,a,t,b,w,c$ regular.
The relation $wa=ct$ gives compatible presentations

$$
u=p^{-1}q,\qquad v=q^{-1}r,
\qquad p=ws,\ q=wa=ct,\ r=cb.
$$

Common right denominators similarly give $u=xy^{-1}$ and $v=yz^{-1}$, with all factors regular.
Thus $uv=p^{-1}r=xz^{-1}$.
The defects for $u$ and $v$ telescope:

$$
\widetilde pPx-\widetilde rPz
=(\widetilde pPx-\widetilde qPy)
+(\widetilde qPy-\widetilde rPz),
$$

and the analogous identity holds for $P^{-1}$.
The two terms on the right have finite rank, so Lemma 3.1 applies to $uv$.

The p. 6 source display uses a minus sign between these two parentheses.
The required operation is addition; this is a local algebraic sign error, independent of the scalar-summand issue in Lemma 3.2.
Correcting it completes multiplication closure.

## Lemmas 3.4 and 3.5: inverses and adjoints

If $u=s^{-1}a=bt^{-1}$ is invertible, then $a,b$ are regular and

$$
u^{-1}=a^{-1}s=tb^{-1}.
$$

Its two selected defects are exactly the negatives of those for $u$.
Lemma 3.1 proves inverse closure.

For the adjoint,

$$
u^*=(t^*)^{-1}b^*=a^*(s^*)^{-1}.
$$

The selected defects for $u^*$ are, in order, $-B(s,a;b,t)^*$ and $-A(s,a;b,t)^*$ because $P^*=P^{-1}$ and the lift preserves adjoints.
Taking adjoints preserves finite rank for bounded maps.
This proves adjoint closure.
In particular $R$ is a unital, inverse-closed $*$-subalgebra of $U$ containing $\mathbb CG$, and therefore $D\subseteq R$.

## Theorem 1.1: the bounded intersection and regularization

For bounded $u\in M$, use $s=t=1$ and $a=b=u$.
Then

$$
A=Pu-\widetilde uP,\qquad
B=P^{-1}\widetilde u-uP^{-1}=-P^{-1}AP^{-1}.
$$

Thus $R\cap M$ is exactly the bounded finite-rank algebra.
The bounded criterion reconstructed in [DR97-U002](../DR97/Yin_U002.md#dr97-u002), [DR97-U003](../DR97/Yin_U003.md#dr97-u003), and [DR97-U004](../DR97/Yin_U004.md#dr97-u004) gives

$$
R\cap M=S.
\tag{4}
$$

The different scalar action is harmless by (1).
The existing DR97 input verifies (4) for finitely generated free groups; its arbitrary-rank use is a separate interface obligation discussed below.

For $u\in R$, set

$$
s=(1+uu^*)^{-1},\qquad t=(1+u^*u)^{-1},
\qquad a=su=ut.
$$

The spectral calculus for $|u|$ and the polar decomposition show that $s,t\in M$ are injective with dense range, and that $a\in M$ with $\|a\|\leq1/2$.
For example the relevant scalar function is $r/(1+r^2)$ for $r\geq0$.
The equality $su=ut$ is an identity in the affiliated algebra; it does not assert that an initially unclosed composition has an arbitrarily enlarged domain.

The already proved algebraic properties give $s,t,a\in R$.
By (4) they belong to $S$, and

$$
u=s^{-1}a=at^{-1}.
\tag{5}
$$

Since $S\subseteq D$ and $D$ is inverse closed in $U$, (5) proves $R\subseteq D$.
Together with $D\subseteq R$ and Lemma 3.1 this proves all equalities of Theorem 1.1, including $D\cap M=S$.
Formula (5) also proves both promised fraction representations inside $S$; the source spells out only the left one in its final paragraph.

The theorem proof does not need the separate result that $D(G)$ is a division ring or its identification with a free field.
Those are introductory interfaces with Linnell's earlier work, not hidden dependencies of the argument above.
Its substantive free-group input is (4).

## Scope, dependencies, and review limits

The fraction algebra, the scalar-shift lemma, and the regularization argument above are valid without a finite-generation or separability assumption.
Bounded amplification over an arbitrary family causes no problem.
Unbounded amplifications require the square-summability domain specified in [U003](Yin_U003.md#lin00-u003), but none is used in the bounded fraction defects in this unit.

The exact external interfaces consumed are the affiliated ring and fraction calculus recorded in U001; the spectral and polar decompositions for affiliated operators; and the bounded DR97 criterion in (4).
The source's Lemma 2.3 trace argument and its regularizer estimate are reconstructed explicitly, so their supporting references are not additional unchecked proof premises.
No full audit of the foundational finite von Neumann algebra theory is claimed.

The preprint says only that $G$ is free, with no finite-generation restriction.
The available completed DR97 audit proves its bounded criterion for finite free generating sets, and its finite-alphabet proof cannot simply be applied to an infinite set.
This unit therefore proves Theorem 1.1 outright in that audited finite-generator scope, and proves its local reduction for arbitrary free groups conditional on the corresponding bounded input.
It does not call the broader source statement false, nor infer that input from the fact that each group polynomial uses finitely many generators: a general member of $W(G)$ need not do so.
Any resolution of this remaining interface must have its own actual evidence in U001 or the integrated review.

No project Claim has been created by this source reconstruction.
In particular no general tuple, semicircular, or maximal-$\Delta$ theorem follows merely by replacing the Cayley-tree $P$ with another operator.
Any Lin00 comparison must retain its actual free-group scope.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Lin00, retained arXiv:math/9907075v1, 12 July 1999, seven-page preprint. No line-by-line journal-version comparison or author-confirmed erratum is asserted. |
| source-locator | Definitions, pp. 2-3; Lemmas 2.1-2.3, pp. 4-5; Lemmas 3.1-3.5 and Theorem 1.1 proof, pp. 5-6. Printed page numbers equal PDF page numbers in this artifact. |
| inspection | 2026-10-10: all seven source text pages read; all stated local algebra steps in this unit reconstructed and self-reviewed. The scalar-summand additive errors, multiplication sign error, unbounded type error in Lemma 2.3, scalar-closure interface, and right-fraction conclusion are repaired explicitly. DR97's existing finite-generator audit is reused at its exact scope. Independent cross-review belongs to U004; no formal verification, external human review, blanket audit of references, or unsupported infinite-generator conclusion is claimed. |

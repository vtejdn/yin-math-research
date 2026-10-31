---
author: Yin
---

# ACSY24: Small-Core Derivations and Maximal Delta

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | ACSY24, published 73-page PDF. |
| source-locator | Section 3.2, pp.34–36; references [31], [42], [44], p.73. |
| inspection | Coverage: the derivation definition, Theorem 3.4 with its proof, and Proposition 3.5 with a reconstruction of its abbreviated final step; Lemmas 3.3 and 3.6 are inspected supporting interfaces. |

<a id="acsy24-u001"></a>
## ACSY24-U001 — Proposition 3.5 and Its Domain Interface

- Date and authorization: 2026-09-10; the user specifically requested Proposition 3.5 to reassess the domain hypothesis in the normal-dual program.
- Source: ACSY24, published 73-page PDF; Section 3.2, pp. 34-36, and references [31], [42], [44] on p. 73.
- Coverage: the derivation definition, Theorem 3.4 with its proof, and Proposition 3.5 with a reconstruction of its abbreviated final step; Lemmas 3.3 and 3.6 are inspected supporting interfaces.
- Assessment: source statement verified; the proof reconstruction below has a separate review record in Section 6.
- Consumers: [Yin_T_F0001](../../../tasks/Yin_T_F0001_v1.md#yin_t_f0001), comparison with [Yin_C_F0024](../../../claims/Yin_C_F0024_v1.md#yin_c_f0024).

## General source derivation definition

<a id="coarse-valued-derivation"></a>

The following complete general definition was read separately on 2026-09-10.
This adds the actual general definition scope to the existing sufficient theorem/adjoint unit, without a new source opening or extension of the original Section 6 review to fresh content.

Exact source: Section 3.2, p. 34, unnumbered definition preceding Lemma 3.3.
Existing home: [U001, Section 1](Yin_U001.md#1-exact-hypotheses); the general definition below separates the source construction from that section's particular tuple.
For a tracial \(W^*\)-probability space \((M,\tau)\), a source non-commutative derivation is a complex-linear, possibly unbounded map

\[
\partial:\mathcal A\subseteq L^2(M,\tau)\longrightarrow
L^2(M,\tau)\otimes_2L^2(M,\tau),
\]

where \(\mathcal A\subseteq M\) is a weakly dense star-algebra and \(\partial(ab)=a\cdot\partial(b)+\partial(a)\cdot b\).
The outer actions are \(a\cdot(\xi\otimes\eta)\cdot b=(a\xi)\otimes(\eta b)\).
Closability, a reality condition, and an adjoint vacuum vector are not clauses of this general definition.
The source defines membership in the Hilbert adjoint domain by the adjoint pairing against every input in \(\mathcal A\).
The codomain is the Hilbert tensor product; it need not be an algebraic tensor of bounded elements.

<a id="starred-core-application-boundary"></a>
## 1. Exact Hypotheses

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal probability trace, $H=L^2(M,\tau)$, $\Omega=1$, and $P=P_\Omega$.
Let $X=(X_1,\ldots,X_d)$ be bounded operators generating $M$ as a von Neumann algebra, and put
\[
\mathcal A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle.
\]
Proposition 3.5 assumes complex-linear derivations
\[
\partial_i:\mathcal A\subset H\longrightarrow H\otimes_2 H,
\qquad
\partial_i(X_j)=\delta_{ij}\Omega\otimes\Omega,
\qquad
\Omega\otimes\Omega\in\operatorname{Dom}\partial_i^*.
\tag{1}
\]
The bimodule actions are the outer actions $a\cdot(\xi\otimes\eta)\cdot b=(a\xi)\otimes(\eta b)$.
The codomain is the Hilbert tensor product, not necessarily the algebraic tensor product of bounded elements.
Neither normality of $X$ nor a reality condition on the derivations occurs in the proposition.
Its conclusion is
\[
\Delta(X_1,\ldots,X_d)=d.
\tag{2}
\]

The starred polynomial domain is essential to this stated interface: it is weakly dense and closed under adjoints.
The proposition does not merely assume a derivation on the possibly non-dense holomorphic algebra $\mathbb C\langle X\rangle$.
The values $\partial_i(X_j^*)$ must respect the actual relations in $\mathcal A$; they are not free extra coordinates that can arbitrarily be set to zero.

<a id="canonical-contraction-dual"></a>
## 2. Theorem 3.4: Construction and Adjoint

Identify $H\otimes_2H$ isometrically with the Hilbert-Schmidt operators through
\[
(a\otimes b)\#P=aPb\qquad(a,b\in M).
\]
For $\xi_i=\partial_i^*(\Omega\otimes\Omega)$, Theorem 3.4 constructs
\[
D_{i,0}=(\mathrm{id}\otimes\tau)\partial_i,
\qquad \operatorname{Dom}D_{i,0}=\mathcal A,
\qquad D_{i,0}\Omega=0.
\tag{3}
\]
The Leibniz identity gives, on $\mathcal A$,
\[
[D_{i,0},a]=(\partial_i a)\#P=:T_{i,a}\in S_2(H)
\qquad(a\in\mathcal A).
\tag{4}
\]
In particular, the commutators with both $X_j$ and $X_j^*$ have bounded Hilbert-Schmidt extensions.
The source's adjoint calculation gives
\[
\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*,
\qquad
D_{i,0}^*a=a\xi_i-T_{i,a^*}^*\Omega.
\tag{5}
\]
Consequently $D_{i,0}$ is closable.
Formula (5) must not be replaced by $a\xi_i-D_{i,0}a$ without an additional compatibility argument.
Theorem 3.4 and (5) assert the polynomial domain inclusion, not an inclusion of all $M$.

## 3. Reconstructing the Unbounded Step in Proposition 3.5

The final paragraph on p. 36 refers to [MSY23 Proposition 6.2](../MSY23/Yin_U005.md#msy23-u005) and abbreviates its extension to unbounded duals.
The following regularization supplies the needed domain justification.
It does not assume that $D_i$ is affiliated with $M$; ordinary dual operators generally are not.

Fix $i$, write $D=\overline{D_{i,0}}$, and suppress the first index on $T$.
Because $\mathcal A$ is a core for $D$, (4) and closedness give
\[
a\operatorname{Dom}D\subseteq\operatorname{Dom}D,
\qquad [D,a]=T_a\quad\text{on }\operatorname{Dom}D.
\tag{6}
\]
Indeed approximate a graph vector by $z_n\in\mathcal A$ and use $D(az_n)=aDz_n+T_a z_n$.
Applying (6) to $a^*$ and taking adjoints also gives
\[
a\operatorname{Dom}D^*\subseteq\operatorname{Dom}D^*,
\qquad [D^*,a]=-T_{a^*}^*.
\tag{7}
\]

On $H\oplus H$ use the selfadjoint operator and bounded multiplier
\[
S=\begin{pmatrix}0&D^*\\ D&0\end{pmatrix},
\qquad Z_j=\begin{pmatrix}X_j&0\\0&X_j\end{pmatrix}.
\]
Equations (6)-(7) verify domain invariance and the bounded extension
\[
C_j=[S,Z_j]
=\begin{pmatrix}0&-T_{X_j^*}^*\\\delta_{ij}P&0\end{pmatrix}
\in S_2(H\oplus H).
\tag{8}
\]
For $t>0$ put $R_t=(1+tS^2)^{-1}$.
The resolvent commutator formula gives the identity of bounded operators
\[
[SR_t,Z_j]=R_t C_jR_t-tSR_t C_jSR_t.
\tag{9}
\]
One can derive (9) directly from
\[
SR_t=\frac1{2t}\big((S-i/\sqrt t)^{-1}+(S+i/\sqrt t)^{-1}\big),
\qquad
[(S-z)^{-1},Z_j]=-(S-z)^{-1}C_j(S-z)^{-1}.
\]
Thus no unverified invariance of $\operatorname{Dom}S^2$ is needed.
Spectral calculus gives
\[
R_t\longrightarrow I\text{ strongly},\qquad
B_t:=\sqrt t\,SR_t\longrightarrow0\text{ strongly},\qquad
\|B_t\|\le\tfrac12.
\]
Both families are selfadjoint.
Finite-rank approximation of a fixed Hilbert-Schmidt operator therefore yields
\[
\|R_t C_jR_t-C_j\|_2\longrightarrow0,
\qquad \|B_t C_jB_t\|_2\longrightarrow0.
\]
Taking the lower-left block of (9) gives bounded operators
\[
D_{i,t}=D_i(1+tD_i^*D_i)^{-1}\in B(H),
\qquad
\|[D_{i,t},X_j]-\delta_{ij}P\|_2\longrightarrow0,
\tag{10}
\]
where $D_i$ now denotes the closure in (3).
Their norms need not stay bounded as $t\downarrow0$; (10) suffices.

Let $(F_1,\ldots,F_d)$ be a finite-rank cycle $\sum_k[F_k,X_k]=0$.
For arbitrary $Q_1,Q_2\in M'$ the ordinary trace calculation with the bounded operator $Q_1D_{i,t}Q_2$ gives
\[
0=\sum_k\operatorname{Tr}\big(F_kQ_1[X_k,D_{i,t}]Q_2\big).
\]
All products are finite rank before taking their trace.
Equation (10) and Hilbert-Schmidt trace duality imply
\[
\operatorname{Tr}(F_iQ_1PQ_2)=0.
\]
This is $\langle Q_2^*\Omega,F_iQ_1\Omega\rangle=0$.
Since $M'\Omega$ is dense in $H$, the two independent choices imply $F_i=0$.
The [MSY23 finite-cycle characterization](../MSY23/Yin_U002.md#msy23-u002) now proves (2).

The regularization also clarifies a weaker sufficient operator hypothesis.
If $D_{i,0}$ is closable on the common dense starred polynomial core, its generator commutators are $\delta_{ij}P$, and its adjoint-generator commutators have merely bounded extensions, then (6)-(9) still apply.
For bounded $C_j$, the same spectral bounds give $R_t C_jR_t\to C_j$ and $B_t C_jB_t\to0$ strongly.
Finite-rank trace pairings are continuous for this convergence, so the cycle proof still yields maximal Delta.
Compactness improves convergence to operator norm; the Hilbert-Schmidt hypothesis actually supplied by ACSY24 improves it to the Hilbert-Schmidt norm in (10).
None of these arguments requires uniform boundedness of the approximating duals $D_{i,t}$ themselves.

## 4. Consequences and Limits for the Main Theorem

For the maximal-Delta step, the reconstruction only needs a closable dual on a common dense starred polynomial core and bounded extensions of its commutators with the adjoint generators.
The source derivations provide exactly these data through (3)-(5).
In particular, requiring $M\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*$ is stronger than necessary for that step.
Together with the accepted [MSY23 affiliated realization](../MSY23/Yin_U004.md#msy23-u004), (2) realizes
\[
F_X=\operatorname{Div}_{U(M)}\mathbb C\langle X\rangle
\]
as the free skew field, without adjoining $X^*$ to this division closure.
The starred analytic domain and the holomorphic rational algebra serve different purposes.

[Yin_C_F0024](../../../claims/Yin_C_F0024_v1.md#yin_c_f0024) remains a proved sufficient theorem with a stronger domain hypothesis.
That hypothesis also supplies the separate analytic work for
\[
T_i z=sD_i(bz)-aD_i(tz),\qquad z\in M,
\]
for arbitrary bounded fraction coefficients $s,a,b,t$.
It gives well-definedness, adjoint tests, continuity on bounded sets, and regular-cutoff cancellation.
Proposition 3.5 alone does not establish these all-$M$ properties or identify the rationality class of such defects under its smaller-domain hypotheses.
The rationality theorem should therefore distinguish the small-core algebraic input from whichever analytic domain extension its chosen defect formulation needs.
Whether all those analytic hypotheses can be weakened is a further obligation, not a consequence of maximal Delta.

If $X$ is selfadjoint, $\mathcal A=\mathbb C\langle X\rangle$ and (1) is precisely existence of the usual L2 conjugate system, hence finite non-microstates free Fisher information for finite $d$.
The existing [Dab10 contraction interface](../Dab10/Yin_U002.md#dab10-u002) separately supplies the all-$M$ domains needed for the Yin_C_F0024 corollary; the two uses must not be conflated.

Lemma 3.6, p. 36, supplies another stated application: for a unitary $U$ with L3 density relative to circle Lebesgue measure, the required derivation exists on $\mathbb C[U,U^{-1}]$, and $\Delta(U)=1$.
The source obtains it by twisting the unitary derivation $d(U)=1\otimes U$ by $1\otimes U^{-1}$ using Lemma 3.3.
For the Haar case one can check this directly: $D(U^n)=U^{n-1}$ for $n>0$ and $0$ for $n\le0$, so $[D,U]=P$, $[D,U^{-1}]=-U^{-1}PU^{-1}$, and $D^*\Omega=U$.
The general L3 existence theorem cited there, Voiculescu's Proposition 8.7 in source reference [44], was not independently proof-audited here and is not needed for (1)-(2).

## 5. Sources and Inspection Boundaries

The local published PDF was text-inspected on pp. 34-36 and visually checked on pp. 35-36, with bibliography entries read on p. 73.
The [publisher metadata](https://www.sciencedirect.com/science/article/abs/pii/S0001870824001105) and [arXiv record](https://arxiv.org/abs/2107.11507) were located on 2026-09-10 to identify the supplied article.
No arXiv/publisher theorem-version comparison, whole-paper audit, or new source download was performed.
Theorem 3.4's stated formula is checked directly from the derivation and adjoint identities; its original reference, Shlyakhtenko's Theorem 1, need not be assumed for this reconstruction.
Lemma 3.3's full adjoint-domain equivalence is not an input to the proof of Proposition 3.5 above.
Standard closed-operator selfadjoint doubling, spectral calculus, Hilbert-Schmidt approximation and the previously audited MSY23 finite-cycle characterization remain accepted foundations.
There is no numerical experiment, proof-assistant verification, external human review, or novelty assessment.

## 6. Review Record

The independent free-field algebra agent read the source, developed the regularization reconstruction, and checked the exact source codomain and domain interfaces.
The coordinating agent independently checked the reconstruction and integrated this record.
On 2026-09-10, the selfadjoint-interface agent separately read the complete relevant source text on published pp. 34-36 and the entire written source audit, including the Haar example and scope boundaries.
That reviewer did not author Sections 1-5, and supplied the additional convergence observation recorded below after checking the proposed reconstruction.
This is a separate artifact review with that contribution disclosed, not an external human review or claim of independent rediscovery of the regularization route.

The review confirms the exact source hypotheses: the domain is a weakly dense star algebra, the codomain is the Hilbert tensor product, and no normality or reality condition is imposed in Proposition 3.5.
The adjoint formula follows directly by applying the derivation to a-star times b and pairing with the vacuum tensor, with the displayed multiplication order retained.
Graph approximation proves the closed-domain commutator identity.
Adjoint pairing using the commutator with a-star proves both adjoint-domain invariance and the minus sign in equation (7).
The selfadjoint block operator has domain $\operatorname{Dom}D\oplus\operatorname{Dom}D^*$, and these two invariance statements justify its bounded commutator with the diagonal generator.

The resolvent signs and coefficients in equation (9) are correct.
For $G_\pm=(S\mp i/\sqrt t)^{-1}$, the bounded resolvent commutator is $-G_\pm C G_\pm$, and $G_\pm=tSR_t\pm i\sqrt t R_t$.
Adding the two resolvent formulas cancels their mixed terms and gives exactly $R_t C R_t-tSR_t C SR_t$.
This derivation needs invariance of $\operatorname{Dom}S$ only and makes no unsupported claim about $\operatorname{Dom}S^2$.
The lower-left block is the displayed bounded $D(1+tD^*D)^{-1}$.
The selfadjoint strong limits and uniform bounds justify the Hilbert-Schmidt convergence through finite-rank approximation.
The subsequent ordinary traces are traces of bounded finite-rank products, and their limits give the correct two independent commutant vacuum tests.
Thus the reconstruction proves maximal Delta without requiring affiliation of a dual with M.

The reviewer additionally checked that the Delta conclusion needs only bounded extensions of the generator and adjoint-generator commutators in this regularization argument.
For bounded C, the two terms R_t C R_t and B_t C B_t converge strongly to C and zero, respectively.
Finite-rank trace functionals are continuous for weak operator convergence, so strong convergence of the approximate dual commutators already permits the same final cycle test.
Compact C gives convergence in operator norm, and Hilbert-Schmidt C gives convergence in Hilbert-Schmidt norm as used above.
The source provides the stronger Hilbert-Schmidt hypothesis automatically.

The direct Haar formulas are correct on every integer Fourier mode, including the negative modes and the rank-one inverse commutator.
In that example the vacuum adjoint is U, and the Laurent polynomial domain is dense.
The review also confirms that the starred analytic domain does not enlarge the holomorphic affiliated division closure in the conclusion imported from MSY23.
The finite-Fisher specialization invokes the separate Dab10 analytic estimates at their selfadjoint scope.
Neither the source statement nor this resolvent proof supplies an infinity-to-L2 bound for the dual itself on all bounded vectors, so no all-M domain conclusion is inferred here.

Outcome: the exact source interface and the local reconstruction pass review, with no unresolved mathematical correction.
The source foundations and inspection limits in Section 5 are retained.
The current Yin_C_F0024 proof and its accepted inspection scope are preserved unchanged; this source audit corrects any suggestion that its all-$M$ domain condition is necessary merely to obtain maximal Delta.

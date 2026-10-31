---
author: Yin
---
# Rationality for nonatomic normal generators with liberation dual systems

Context: the human requested the liberation-dual criterion with nonatomic normal generators and subsequently removed vacuum normalization from the domain definition.
The normalized formulation is retained in [C_F0079 v1](Yin_C_F0079_v1.md#statement).
The argument below proves the criterion directly with the domain and commutator assumptions; its final normalization calculation also identifies the two existence conditions.
The conjugate-variable criterion in [C_F0063](Yin_C_F0063_v1.md#statement) remains a sufficient case.

## Statement

Let (M,tau) be a tracial W*-probability space with faithful normal tracial state, H=L2(M,tau), Omega=1, and U=L0(M).
Elements of M act on H by left multiplication; rho(x) is right multiplication by x, and P_Omega is the orthogonal projection onto C Omega.
Let X=(X_1,...,X_d) be bounded normal generators of M.

<a id="liberation-dual-system"></a>
**Definition.** A liberation dual system for X consists of linear operators L_i on H satisfying
\[
 M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*,\qquad
 [X_j,L_i]|_{M\Omega}=\delta_{ij}[X_i,P_\Omega]|_{M\Omega}
 \quad(1\leq i,j\leq d).
\]
This is a local domain variant of the commutation pattern in [Voi99 Definition 13.1](../audits/literature/Voi99/Yin_U001.md#bounded-liberation-dual-system).
That source requires bounded selfadjoint operators; this definition requires the displayed common domain and adjoint domain and imposes no condition on L_i Omega.
The domain inclusion already implies dense definition and closability.
Write A_X=C<X_1,...,X_d> and
\[
 \Psi_i(k)=k(X_i\otimes1-1\otimes X_i^{\rm op}),\qquad
 \Theta(c\otimes d^{\rm op})=cP_\Omega d
\]
for bounded factors, extending Theta to the algebraic L2 tensor product as the finite-rank identification.
Tensor multiplication uses the opposite second factor.

Assume additionally that each X_i has nonatomic spectral distribution in the following three assertions.

**Proposition.** If X admits a liberation dual system, then Delta(X)=d.

**Tensor recovery.** Under the same hypotheses, if k_i belong to U tensor_alg U^op and h=sum_i Psi_i(k_i) belongs to M tensor_alg M^op, then every k_i belongs to H tensor_alg H.

**Rationality criterion.** Under the same hypotheses, for each u in U the following are equivalent: u belongs to Div_U A_X; there is a fraction pair Q=(s,a,b,t) for u and bounded finite-rank T_i satisfying the equation below; and there are such T_i for every fraction pair Q.
Here s,t are regular elements of M and u=s^{-1}a=bt^{-1}.
The equation is
\[
 \sum_i[\rho(X_i),T_i]=sP_\Omega b-aP_\Omega t.
\]
For a fixed fraction pair Q the solution tuple is unique.

**Normalization.** For the domain variant just defined, existence is equivalent to existence of such operators with L_i Omega=0.
This equivalence does not require nonatomicity.
The normalization is performed on M Omega; no equality of the original full operator domains is asserted.

## Argument

### Algebraic and analytic inputs

We use the finite-rank-cycle characterization of maximal Delta, the rank-one tensor representation and its four factor actions, and finite common-denominator clearing in a finite von Neumann algebra.
Their exact source interfaces are retained in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002), [CS05-U002](../audits/literature/CS05/Yin_U002.md#cs05-u002), and [C_F0068 Part A](Yin_C_F0068_v1.md#argument).
The maximal-Delta rationality theorem is used at its fixed Part A scope; its printed right-hand side has the opposite sign, converted by replacing all finite-rank witnesses by their negatives.
The criterion for a prescribed fraction follows from its tensor proof as described below.
The finite-rank closure fact is the established statement inspected in [Kat95](../audits/literature/Kat95/readme.md): a densely defined closable finite-rank operator has an everywhere-defined bounded finite-rank closure with the same range.

For completeness, that closure fact follows as follows.
If T has finite-dimensional range F, its graph closure still has range in F.
The restriction to F of the dense domain of T* is dense in F, hence equals F, because T vanishes against vectors in F-perp.
Thus every coordinate functional of T on F is bounded on its domain.
The resulting bounded extension has range equal to F and is the closure of T.

If x-lambda is regular for every complex lambda, left and right multiplication by x on U have no nonzero finite-dimensional invariant subspace: such a subspace would contain an eigenvector killed by an invertible x-lambda.
For linear maps A on V and B on W, the map A tensor I-I tensor B is injective on V tensor_alg W if B has no nonzero finite-dimensional invariant subspace.
Indeed, a nonzero tensor in its kernel has a minimal decomposition sum_r v_r tensor w_r with both families independent.
Projecting the second factor modulo span{w_r} forces that finite-dimensional span to be B-invariant.
The same assertion holds with A instead of B.
In particular k maps to k(x tensor 1-1 tensor x^op) injectively on U tensor_alg U^op.
If its image belongs to H tensor_alg H, project the first factor modulo H and use injectivity with left multiplication by x on the second factor.
Exactness of tensoring over C gives k in H tensor_alg U^op.
Project the second factor modulo H and use right multiplication by x on H to obtain k in H tensor_alg H.
Nonatomic normality supplies the required regularity of every X_i-lambda by spectral calculus and finiteness of M.

### Coordinate separation

On bounded algebraic tensors define
\[
 \Phi_i(c\otimes d^{\rm op})=cL_id|_{M\Omega},
 \qquad\Phi_i:M\otimes_{\mathbb C}M^{\rm op}\longrightarrow
 \operatorname{Hom}_{\mathbb C}(M\Omega,H).
\]
This is well defined by bilinearity; all inputs of L_i remain in M Omega.
The commutator relation gives, on M Omega,
\[
 \Phi_i(\Psi_j(z))=\delta_{ij}\Theta(\Psi_i(z)),\qquad
 \Phi_i((s\otimes t^{\rm op})z)=s\Phi_i(z)t
\]
for z in M tensor_alg M^op and s,t in M.
For example the first identity on c tensor d^op is c[X_j,L_i]d=delta_ij c[X_i,P_Omega]d.
Also Psi_i(rk)=r Psi_i(k) for affiliated algebraic tensors, by associativity.

### Proof of the proposition

Let T_i be a finite-rank tuple with sum_i[rho(X_i),T_i]=0, and set k_i=Theta^{-1}(T_i).
Then sum_i Psi_i(k_i)=0.
Choose common regular s,t in M so that m_i=(s tensor t^op)k_i all have bounded algebraic factors; this is finite common-denominator clearing separately in the two tensor factors.
Hence sum_i Psi_i(m_i)=0.
Applying Phi_i gives Theta(Psi_i(m_i))=0, so Psi_i(m_i)=0.
The preceding individual injectivity gives m_i=0.
Cancel s tensor t^op inside U tensor_alg U^op to obtain k_i=0 and T_i=0.
The finite-rank-cycle characterization implies Delta(X)=d.
This proof uses the liberation commutator relations and nonatomicity; it does not rely on the tensor-recovery conclusion or on a conjugate-variable hypothesis.

### Proof of tensor recovery

Write h=sum_r c_r tensor d_r^op, with c_r,d_r in M, and put S_i=Phi_i(h) on M Omega.
For eta in M Omega the adjoint identity gives
\[
 S_i^*\eta=\sum_r d_r^*L_i^*(c_r^*\eta).
\]
Thus M Omega is contained in Dom S_i* and S_i is closable.
Choose regular s,t in M with m_j=(s tensor t^op)k_j bounded algebraic tensors.
Applying Phi_i to the cleared identity gives
\[
 sS_it=\Theta(\Psi_i(m_i))\quad\hbox{on }M\Omega.
\]
The right side has finite rank and s is injective, so S_i restricted to t M Omega has finite rank.
The latter domain is dense because t has dense range and M Omega is dense.
The restriction is closable, and its closure is bounded finite-rank on all H.
The closure of S_i extends that closure and must equal it, since an operator on all H has no proper operator extension.
Put h_i=Theta^{-1}(overline{S_i}) in H tensor_alg H.
Extend the displayed equality by boundedness and density; the outer tensor actions then give
\[
 (s\otimes t^{\rm op})h_i=\Psi_i(m_i)
 =(s\otimes t^{\rm op})\Psi_i(k_i).
\]
Cancellation yields Psi_i(k_i)=h_i in H tensor_alg H.
The individual tensor-recovery argument above implies k_i in H tensor_alg H.

### Proof of the rationality criterion

The proposition supplies Delta(X)=d.
By C_F0068 Part A, a rational u has affiliated tensors k_i satisfying sum_i Psi_i(k_i)=u tensor 1-1 tensor u^op.
For an arbitrary fraction pair Q=(s,a,b,t), let ell_i=(s tensor t^op)k_i.
Then
\[
 \sum_i\Psi_i(\ell_i)=a\otimes t^{\rm op}-s\otimes b^{\rm op}
 \in M\otimes_{\mathbb C}M^{\rm op}.
\]
Tensor recovery gives ell_i in H tensor_alg H.
Taking T_i=-Theta(ell_i) and using Theta Psi_i=[rho(X_i),Theta] gives the desired equation with sP_Omega b-aP_Omega t.
Existence for every fraction pair implies existence for some pair, because every affiliated operator has a fraction pair.
Conversely a finite-rank solution for some pair implies rationality by C_F0068 Part A, with its sign conversion already specified.
Two solutions for fixed Q differ by a finite-rank cycle, which vanishes since Delta(X)=d.

### Why the nonatomic hypothesis is retained

A liberation dual system alone does not imply the proposition or fixed-pair uniqueness.
For d=1 and any normal generator X, L=P_Omega-I is bounded, satisfies L Omega=0 and [X,L]=[X,P_Omega].
In M=C^2 with its normalized trace and X=(0,1), a nonzero rank-one spectral projection of rho(X) commutes with rho(X).
It is a nonzero finite-rank cycle, so Delta(X) is not 1.
At u=0 and Q=(1,0,0,1), both that projection and zero solve the certificate equation.

### Vacuum normalization on the common domain

<a id="vacuum-normalization"></a>
Let L_i satisfy the domain and liberation commutator conditions, and set eta_i=L_i Omega in H.
Define an operator on the common dense domain M Omega by
\[
 \widetilde L_i(a\Omega)=L_i(a\Omega)-a\eta_i,\qquad a\in M.
\]
Every product a eta_i belongs to H because a is bounded.
The correction a Omega maps to a eta_i commutes with the left action of M on this domain, so
\[
 [X_j,\widetilde L_i]|_{M\Omega}
 =[X_j,L_i]|_{M\Omega}
 =\delta_{ij}[X_i,P_\Omega]|_{M\Omega},
 \qquad \widetilde L_i\Omega=0.
\]
For a,b in M, with the inner product linear in its second variable, traciality gives
\[
 \langle b\Omega,a\eta_i\rangle
 =\tau(b^*a\eta_i)
 =\tau(\eta_i b^*a)
 =\langle b\eta_i^*,a\Omega\rangle.
\]
Consequently
\[
 b\Omega\in\operatorname{Dom}\widetilde L_i^*,\qquad
 \widetilde L_i^*(b\Omega)=L_i^*(b\Omega)-b\eta_i^*\in H.
\]
Thus M Omega is in both required domains, and the normalized operators are closable.
Their closures may also be used: they retain the displayed relations on M Omega and their adjoints contain M Omega.
The reverse existence implication is immediate.
For a given system, the zero-vacuum property is not automatic: for d=1, L=P_Omega satisfies all the domain and commutator conditions but L Omega=Omega.
The proposition, recovery proof and rationality proof above do not use this normalization.

## Current assessment
[Selected decision](#decision-domain-definition-reviewed)

## Assessment history
### Decision domain-definition
| Field | Value |
| --- | --- |
| date | 2026-10-18T05:32 |
| status | open |
| reason | The user removed vacuum normalization from the liberation-dual definition. The complete criterion proof is retained with the reduced assumptions, and the normalization equivalence is recorded separately. |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common domains and liberation commutators; nonatomic criterion and normalization equivalence. |
| argument | [Argument](#argument) | Direct proposition, tensor recovery, rationality and normalization on the common domain. |
| dependency | [C_F0068 Part A](Yin_C_F0068_v1.md#argument) | Maximal-Delta rationality and affiliated tensor witnesses with the explicit sign conversion. |

### Decision domain-definition-reviewed
| Field | Value |
| --- | --- |
| date | 2026-10-18T05:33 |
| status | proved |
| reason | The definition without a vacuum condition, the direct criterion proof and the common-domain normalization equivalence passed the authoring-agent self-review of this exact version. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Domain definition, nonatomic criterion and normalization equivalence. |
| argument | [Argument](#argument) | Direct proposition, tensor recovery, rationality and normalization on the common domain. |
| dependency | [C_F0068 Part A](Yin_C_F0068_v1.md#argument) | Maximal-Delta rationality and affiliated tensor witnesses with the explicit sign conversion. |
| review | [Self-review](../audits/reviews/Yin_R_F0058_v2.md#finding) | Exact v2 statement and complete proof, including absence of vacuum-condition dependence and the separate normalization equivalence; self-review only. |


---
author: Yin
---
# Rationality from liberation dual systems and regular scalar shifts

Context: the human requested replacement of normality and nonatomicity in the liberation criterion by regularity of X_i-lambda for every index and every complex scalar.
The nonatomic normal formulation is retained in [C_F0079 v3](Yin_C_F0079_v3.md#statement), with earlier variants at their own fixed versions.
The conjugate-variable sufficient condition from [C_F0063](Yin_C_F0063_v1.md#statement) and the ordinary dual-system results retain their normality and generation hypotheses.

## Statement

Let (M,tau) be a tracial W*-probability space with faithful normal tracial state, H=L2(M,tau), Omega=1, and U=L0(M).
Elements of M act on H by left multiplication; rho(x) is right multiplication by x, and P_Omega is the orthogonal projection onto C Omega.
Let X=(X_1,...,X_d) be any tuple in M^d, with d>=1.

<a id="liberation-dual-system"></a>
**Definition.** A liberation dual system for X consists of linear operators L_i on H satisfying
\[
 M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*,\qquad
 [X_j,L_i]|_{M\Omega}=\delta_{ij}[X_i,P_\Omega]|_{M\Omega}
 \quad(1\leq i,j\leq d).
\]
This is a local domain variant of the commutation pattern in [Voi99 Definition 13.1](../audits/literature/Voi99/Yin_U001.md#bounded-liberation-dual-system).
That source requires bounded selfadjoint operators; this definition requires the displayed common domain and adjoint domain and imposes no condition on L_i Omega.
The domain inclusion already implies dense definition and closability, since M Omega is dense in H independently of X.
The definition prescribes the displayed generator commutators; it does not assert corresponding relations for adjoints or generated von Neumann subalgebras for an arbitrary tuple.
Write A_X=C<X_1,...,X_d> and
\[
 \Psi_i(k)=k(X_i\otimes1-1\otimes X_i^{\rm op}),\qquad
 \Theta(c\otimes d^{\rm op})=cP_\Omega d
\]
for bounded factors, extending Theta to the algebraic L2 tensor product as the finite-rank identification.
Tensor multiplication uses the opposite second factor.

An element of M is regular if it is invertible in U, equivalently injective with dense range on H.
In the following three assertions, assume
\[
 X_i-\lambda\text{ is regular}
 \qquad(1\leq i\leq d,\ \lambda\in\mathbb C).
\]
No normality or generation of M is assumed.

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
This equivalence requires neither regularity of scalar shifts nor generation of M.
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
The scalar-shift hypothesis supplies this regularity for each X_i directly.
Bounded left and right multiplication preserve H even when X_i is not normal, so both quotient-factor arguments apply.

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
This characterization is for arbitrary bounded tuples in M and does not assume M=W*(X).
This proof uses the liberation commutator relations and regularity of all scalar shifts; it does not use normality, the tensor-recovery conclusion or a conjugate-variable hypothesis.

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
Neither of these density statements requires the polynomial algebra in X to be dense in H.
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
C_F0068 Part A explicitly requires neither normality nor generation of the ambient algebra, so it applies to this tuple in M.
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

### Why scalar-shift regularity is required

A liberation dual system alone does not imply the proposition or fixed-pair uniqueness.
For d=1 and any bounded operator X, L=P_Omega-I is bounded, satisfies L Omega=0 and [X,L]=[X,P_Omega].
In M=C^2 with its normalized trace and X=(0,1), the scalar shifts at 0 and 1 are not regular, and a nonzero rank-one spectral projection of rho(X) commutes with rho(X).
It is a nonzero finite-rank cycle, so Delta(X) is not 1.
At u=0 and Q=(1,0,0,1), both that projection and zero solve the certificate equation.

### The normal case and a nonnormal example

For normal x in M with spectral distribution mu_x, faithfulness of the trace gives
\[
 \mu_x(\{\lambda\})=0
 \Longleftrightarrow 1_{\{\lambda\}}(x)=0
 \Longleftrightarrow\ker(x-\lambda)=\{0\}
 \Longleftrightarrow x-\lambda\text{ is regular}.
\]
Thus the nonatomic normal hypotheses of v3 imply exactly the scalar-shift condition in that case.
This uses regularity in U, not bounded invertibility in M.

The new statement also applies to nonnormal tuples.
Take M=L-infinity([0,1]) tensor M_2(C), with Lebesgue measure and normalized matrix trace, and set
\[
 X(t)=\begin{pmatrix}t&1\\0&t\end{pmatrix}.
\]
Then [X,X*]=diag(1,-1), so X is not normal.
For each complex lambda, t-lambda vanishes on at most a null set, and
\[
 (X-\lambda)^{-1}(t)=
 \begin{pmatrix}
 (t-\lambda)^{-1}&-(t-\lambda)^{-2}\\
 0&(t-\lambda)^{-1}
 \end{pmatrix}
\]
is a measurable matrix representing an affiliated inverse.
It can be assigned any value on the null set where t=lambda.
Thus every scalar shift is regular.
For d=1, the bounded operator L=P_Omega gives [X,L]=[X,P_Omega] and has both required domains equal to H.

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
[Selected decision](#decision-regular-scalar-shifts-reviewed)

## Assessment history
### Decision regular-scalar-shifts
| Field | Value |
| --- | --- |
| date | 2026-10-18T06:08 |
| status | open |
| reason | The user replaced normality and nonatomicity by regularity of every scalar shift. The complete proof, normal-case comparison and nonnormal example are retained for exact-scope self-review. |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Liberation dual systems with all scalar shifts regular; maximal Delta, tensor recovery, every-fraction rationality, uniqueness and normalization equivalence. |
| argument | [Argument](#argument) | Algebraic injectivity and quotient recovery, coordinate separation, closure, rationality, the normal specialization, a nonnormal example and normalization. |
| dependency | [C_F0068 Part A](Yin_C_F0068_v1.md#argument) | Maximal-Delta rationality for arbitrary bounded tuples in the ambient algebra, with the stated certificate-sign conversion. |

### Decision regular-scalar-shifts-reviewed
| Field | Value |
| --- | --- |
| date | 2026-10-18T06:12 |
| status | proved |
| reason | The complete argument was checked under regularity of every scalar shift, without normality or generation. The proof and examples have no unresolved gap in the stated scope; the review is an authoring-agent self-review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Liberation dual systems with all scalar shifts regular; maximal Delta, tensor recovery, every-fraction rationality, uniqueness and normalization equivalence. |
| argument | [Argument](#argument) | Complete proof, normal specialization, nonnormal example, missing-regularity example and common-domain normalization. |
| dependency | [C_F0068 Part A](Yin_C_F0068_v1.md#argument) | Maximal-Delta rationality for arbitrary bounded tuples in the ambient algebra, with the stated certificate-sign conversion. |
| review | [R_F0058 v4](../audits/reviews/Yin_R_F0058_v4.md#finding) | Exact statement and complete argument self-review, with source applicability and review-scope limits. |


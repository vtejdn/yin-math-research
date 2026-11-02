---
author: Yin
---
# Maximal Delta without any bare full-domain coordinate dual: independent complete review

Date: 2026-10-14T19:42.
Human record author: Yin.
This separately organized agent review covers the entire fixed [C_F0147 v1](../../claims/Yin_C_F0147_v1.md#statement), all four proof sections and all four direct source interfaces.
Its initial decision is dated 2026-10-14T19:39.

The reviewer did not contribute to this construction.
Earlier work on other T_F0011 comparisons, normal contraction domains and weighted liberation counterexamples is separate from this proof.
The supplied assignment described the claimed tuple and the verification targets and identified root and the general-branch author as developers.
No D_F0003 development text or proof-generation dialogue was consulted.
Developer checks are not treated as independent evidence.
The fixed C and the exact source units were read and the calculations below were independently reconstructed.

During the review, the author repaired two stale extracted equation references and explicitly wrote E_i=-D_i with its operator-first identity.
That correction was reread against equation (1), as described below.
These mathematical-reference and notation repairs changed neither the mathematical claim nor the argument under review.
No earlier C_F0147 review conclusion was supplied or relied on.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0147 statement](../../claims/Yin_C_F0147_v1.md#statement) | General finite-row obstruction; maximal Delta in N; nonexistence of either bare coordinate dual; star algebraic freeness and nonnormality; failed Hilbert-valued reference lifting; explicit unresolved target-A boundary. |
| [Conclusion](#conclusion) | [C_F0147 argument](../../claims/Yin_C_F0147_v1.md#argument) | All four sections, including actual range versus range closure, bounded kernel columns in the target algebra, finite trace and symmetry, polynomial fullness retraction, and opposite-factor order. |
| [Conclusion](#conclusion) | [Miy22-U001](../literature/Miy22/Yin_U001.md#miy22-u001) | Standard variance-one free semicircular Fock model, faithful trace, word basis and recurrence used for actual reference vacua, algebraic freeness and the generator-swap symmetry. Foundational source limits remain those of the unit. |
| [Conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 applied only to the bounded generating reference tuple (2+s0,S1,S2), whose full-core actual vacuum hypotheses are verified locally. No target-A premise or conclusion is imported. |
| [Conclusion](#conclusion) | [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) | Both directions of Theorem 3.1: maximal Delta versus injectivity of all full affine linear square matrices. Exact arbitrary-bounded-tuple and finite-tracial hypotheses apply in both reference and target algebras. |
| [Conclusion](#conclusion) | [MSY23-U004](../literature/MSY23/Yin_U004.md#msy23-u004) | Theorem 5.6, full affine linear to full polynomial matrices, together with the finite-algebra equivalence of injectivity and affiliated invertibility. No bounded-inverse or selfadjointness conclusion is used for the target. |

## Findings

### 1. The finite row relation excludes arbitrary linear witnesses

The generator-first convention [X_j,D_i]=delta_ij P implies, for E_i=-D_i,

\[
 E_i(X_ja)=X_jE_i(a)+\delta_{ij}\tau(a)1.
\]

This is the corrected identity now present in Section 1.
Every input X_j a_j is bounded and belongs to the stipulated full domain.
Applying linearity to their finite sum gives

\[
 0=\sum_jX_jE_i(a_j)+\tau(a_i)1.
\]

Since tau(a_i) is nonzero, this places 1 in the algebraic sum of ranges X_j L2(M), contradicting the hypothesis.
No continuity, module-linearity, normalization, closability or adjoint assumption was inserted.
The assertion concerns the actual range sum, not its closure; a dense range does not defeat this obstruction.

### 2. The concrete relation belongs to the target algebra

For h=2+s0, the shifted semicircular law is diffuse on [0,4], with density proportional to sqrt(t(4-t)).
Hence h is regular and h inverse is not L2: its inverse-square integral has the nonintegrable t^(-3/2) behavior at zero.
Each S_j is regular as well.

The row R=[X1,X2] belongs to M_(1,2)(N), so its kernel projection p is in M2(N), by spectral calculus applied to R*R.
This statement also holds in the ambient faithful normal representation on L2(tilde M)^2.
Since left multiplication by h is injective there, the kernel is exactly that of [S1,S2].
The latter row has dense final range because its adjoint column is injective, already from regularity of S1.
Rectangular polar decomposition gives final projection 1 and initial projection 1-p; the unnormalized finite matrix trace therefore gives Tr_2 tensor tau(p)=1.

The Fock permutation of S1 and S2 fixes h and preserves the joint trace.
It restricts to an automorphism of N and takes the row to RJ, hence its kernel projection to JpJ.
It follows that the two diagonal traces of p equal 1/2.
The diagonal entries need not themselves be projections; only their positive trace and boundedness are used.

Thus each column of p supplies bounded a_j in N satisfying the row relation, with the designated diagonal coefficient of trace 1/2.
For eta_j in L2(N), the sum X1 eta_1+X2 eta_2 belongs to h L2(tilde M), because S_j are bounded.
A solution h eta=1 would force eta to equal the affiliated inverse h inverse.
Equivalently, spectral truncations give arbitrarily large lower bounds for ||eta||2 from the divergent inverse-square integral.
Therefore 1 is not in that actual range.
The preceding obstruction excludes each coordinate witness separately, and hence every bare full-domain system on N.

No assertion N=tilde M is needed.
Membership of the kernel columns in N is established before they are used as inputs to a proposed map on N.

### 3. The fullness retraction establishes maximal Delta independently

The standard word-cut formula for a free semicircular derivative pairs with the vacuum tensor only at the one-letter word.
It therefore represents the vacuum functional by the corresponding semicircular L2 vector on the entire polynomial core.
Translating s0 to h leaves that core unchanged and supplies the actual reference conjugates (s0,S1,S2).
The reference tuple is bounded and generates tilde M, so ACSY24 Proposition 3.5 applies and gives maximal reference Delta.

For a full n-by-n polynomial matrix P in two formal variables, suppose P(h s1,h s2) factored over the three-variable free polynomial algebra through r<n columns.
Applying the unital polynomial retraction h to 1 and s_j to x_j to both factors would give a factorization of P through r columns.
This contradiction proves fullness of the substituted matrix.
The argument does not assume that arbitrary polynomial substitutions preserve fullness.

MSY23 Theorem 3.1 and Theorem 5.6 now imply that every such evaluated matrix is injective on the ambient L2 space.
The evaluated coefficients belong to N, and any kernel vector in L2(N)^n would also be an ambient kernel vector.
Thus it remains injective on the target standard Hilbert space.
In particular all full affine linear target matrices are injective, and Theorem 3.1 in the target algebra gives Delta_N(X1,X2)=2.

Both checked MSY interfaces explicitly allow nonnormal bounded tuples.
Their finite-algebra injectivity/invertibility bridge is affiliated invertibility, not bounded invertibility.
The target generates N by definition; no unproved generation of the larger reference algebra is required.
There is no circular use of a target bare dual or of an actual target conjugate system.

### 4. Algebraic freeness and the exact failed-reference-lift scope

A nonzero polynomial in free semicircular variables has a nonzero top Fock-word component.
The invertible scalar translation to h preserves algebraic freeness.
The four target symbols correspond to the distinct length-two words hS1,hS2,S1h,S2h.
Concatenations are decoded at the fixed successive length-two boundaries, so distinct target words stay distinct reference words.
This proves the stated star-algebraic freeness.
The reference words in \(hS_j^2h-S_jh^2S_j\) differ, proving each target variable is nonnormal.
Neither conclusion provides an actual target vacuum adjoint.

For a full-reference derivation, alpha=delta h and beta_j=delta S_j would be Hilbert tensors.
The Leibniz rule gives

\[
 (h\otimes1)\beta_j+(1\otimes S_j^{\mathrm{op}})\alpha
 =\delta_{ij}1.
\]

The second coefficient is left multiplication in the coarse algebra, representing the outer right action; its order is correct.
Let r be the column of these second-factor coefficients and q the kernel projection of r*.
It is a matrix over the second factor alone, so it commutes with h tensor 1.
The same rectangular polar-trace and swap argument gives trace(q_ii)=1/2.
Multiplication by q kills r alpha and forces equation (8).

For a completely explicit L2 check, truncate h inverse at its spectral cutoff \(e_n=1_{[1/n,4]}(h)\).
The squared norm of the truncated right side of (8) is

\[
 \tau(h^{-2}e_n)\sum_j\tau(q_{ji}^*q_{ji})
 =\tfrac12\tau(h^{-2}e_n)\longrightarrow\infty.
\]

The equality uses q squared=q=q* and the tensor-product trace, not a freeness assertion between h and entries within the same factor.
Since q is bounded, its product with the Hilbert column beta has finite L2 norm, giving the contradiction.
No choice of alpha can avoid it.

This proves nonexistence only for derivations on the full reference polynomial algebra.
The target star algebra is a different domain.
No extension from that domain to h,S_j through weak density or affiliated inverses is justified or claimed.
Its actual ACSY condition is consequently still open in this example.

## Source and review limits

The four exact source units and their invoked hypotheses were read.
The general proofs underlying their foundational Fock, affiliated-algebra and free-field inputs are accepted at the units' recorded inspection limits; this is not a fresh audit of all original source pages.
The new project reasoning was checked completely, including both signs after the extraction repair.
No computation or formal verification is represented as proof evidence.

The result separates maximal Delta from full-domain bare existence.
It does not separate A from F, prove a normal-tuple nonimplication, establish a target conjugate system, or exclude target derivations merely because the reference lift fails.
These limits agree with the fixed statement.

## Conclusion

The exact statement and complete corrected argument of C_F0147 v1 pass this independent review, with all four declared dependency interfaces applicable and no remaining mathematical gap found.
They support a `proved` and `independently reviewed` assessment upon adoption by the responsible decision.
The target-A question is explicitly unresolved and is not part of the accepted conclusion.

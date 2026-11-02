---
author: Yin
---
# Relative maximal Delta from bounded duals for arbitrary tuples

Date: 2026-10-14.
Human author Yin; mathematical authoring agent root.
Authorized by the explicit request to formulate, prove, compare with literature and retain the general relative version of CS05 Theorem 4.11.
This is an explicit source-based extension, with no novelty or priority claim.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Definitions

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), \(J(a\Omega)=a^*\Omega\), and \(\rho(a)=Ja^*J\).
Algebra elements act by left multiplication unless \(\rho\) is displayed.
Write \(\mathcal F(H)\) and \(\mathcal S_2(H)\) for finite-rank and Hilbert--Schmidt operators, respectively, and \(N=\mathcal M\bar\otimes\mathcal M^{\mathrm{op}}\).

The action \((a\otimes b^{\mathrm{op}})T=aTb\) on \(\mathcal S_2(H)\) identifies it with the standard \(N\)-module: \(a\otimes b^{\mathrm{op}}\) corresponds to \(aP_\Omega b\).
In particular its \(N\)-dimension is one.
A closed invariant subspace of \(\mathcal S_2(H)^r\) has dimension equal to the canonical trace of its projection in the commutant of \(N\).
The dimension of a nonclosed image below means the dimension of its Hilbert-space closure.

For an ordered finite tuple \(Z=(Z_1,\ldots,Z_r)\) in \(\mathcal M\), with no adjoints implicitly appended, set
\[
 K_Z=\overline{\left\{T\in\mathcal F(H)^r:
             \sum_{j=1}^r[T_j,\rho(Z_j)]=0\right\}}^{\|\cdot\|_2},
 \qquad \Delta_{\mathcal M}(Z)=r-\dim_N K_Z.                 \tag{1}
\]
The cycle space is an \(\mathcal M\)-bimodule, since left multiplications commute with all \(\rho(Z_j)\), and its closure is a closed \(N\)-module.
This absolute definition agrees with [MSY23, Section 3, pp.12--13](../literature/pdf/MSY23.pdf).

For \(X=(X_1,\ldots,X_d)\), \(Y=(Y_1,\ldots,Y_m)\), \(Z=(X,Y)\), and \(E=\mathcal S_2(H)^d\oplus0^m\), define
\[
 \boxed{\Delta_{\mathcal M}(X:X,Y)
       =d-\dim_N(K_{(X,Y)}\cap E).}                        \tag{2}
\]
Here \(E\) is identified with \(\mathcal S_2(H)^d\).
The HS closure is taken BEFORE intersection with \(E\).
An element of the intersection is an HS limit of finite-rank full cycles \((T_\alpha,S_\alpha)\) with \(S_\alpha\to0\); the approximating last components need not vanish identically.

Since \(K_X\oplus0\subseteq K_{(X,Y)}\cap E\),
\[
 0\le\Delta_{\mathcal M}(X:X,Y)
       \le\Delta_{\mathcal M}(X)\le d,\qquad
 \Delta_{\mathcal M}(X:X)=\Delta_{\mathcal M}(X).            \tag{3}
\]
No generation assumption is needed to define these tuple quantities in the specified ambient algebra.
No generator-invariance or homological identification beyond the source's hypotheses is asserted.

## Statement

Suppose \(X,Y\) are arbitrary bounded tuples as above and \(D_1,\ldots,D_d\in\mathcal B(H)\) satisfy
\[
 [X_j,D_i]=\delta_{ij}P_\Omega,\qquad
 [Y_k,D_i]\in\mathcal S_2(H)
 \quad(1\le i,j\le d,\ 1\le k\le m).                       \tag{4}
\]
Then
\[
 \boxed{\Delta_{\mathcal M}(X:X,Y)=\Delta_{\mathcal M}(X)=d.} \tag{5}
\]
Individual normality, closure of either tuple under adjoints, and generation of \(\mathcal M\) are unnecessary.
The case \(m=0\) is allowed.
Retaining \(\mathcal M=W^*(X)\) gives the requested general-tuple relative version of CS05 Theorem 4.11.

## Argument

Use the HS inner product \(\langle T,S\rangle_2=\sum_j\operatorname{Tr}(S_j^*T_j)\), linear in its first argument.
Put
\[
 \mathcal V_Z=
 \overline{\{([B,\rho(Z_j)])_{j=1}^r:B\in\mathcal B(H)\}}^{\mathrm{WOT}}
       \cap\mathcal S_2(H)^r.                              \tag{6}
\]
The closure is taken in \(\mathcal B(H)^r\) with the product WOT.
This intersection is HS closed, since HS convergence implies WOT convergence.
It is invariant under \(T\mapsto aTb\), since this replaces \(B\) by \(aBb\), so it is a closed \(N\)-module.

We first establish the exact Hilbert-space identity
\[
 \mathcal V_{Z^*}=K_Z^\perp,\qquad
 Z^*=(Z_1^*,\ldots,Z_r^*).                                 \tag{7}
\]
The WOT-continuous linear functionals on \(\mathcal B(H)^r\) are the tuples of finite-rank trace functionals.
For finite-rank \(T\) and bounded \(B\),
\[
 \sum_j\operatorname{Tr}(T_j[B,\rho(Z_j)])
   =-\operatorname{Tr}\left(\sum_j[T_j,\rho(Z_j)]B\right).  \tag{8}
\]
The trace pairing with all \(B\) separates finite-rank operators.
Hence the bilinear annihilator of the commutator range consists exactly of the finite-rank cycles.
The locally convex double-annihilator theorem identifies its WOT closure with their annihilator in \(\mathcal B(H)^r\).
On restricting to HS tuples, the bilinear pairing is HS continuous, so one may replace the cycles by their HS closure \(K_Z\).
Componentwise adjoint maps \(K_Z\) onto \(K_{Z^*}\), since
\[
 \left(\sum_j[T_j,\rho(Z_j)]\right)^*
       =-\sum_j[T_j^*,\rho(Z_j^*)].
\]
Thus \(\sum_j\operatorname{Tr}(T_jV_j)=0\) for all \(T\in K_Z\) means \(V\perp K_{Z^*}\).
This proves (7).
It does not assert that the unclosed commutator range is HS closed.

Let \(\pi_X\) be projection onto the first \(d\) coordinates.
For any closed subspace \(K\subseteq E\oplus E^\perp\),
\[
 \overline{\pi_X(K^\perp)}^{\|\cdot\|_2}
       =(K\cap E)^\perp_E.                                \tag{9}
\]
Indeed \(u\in E\) is perpendicular to \(\pi_X(K^\perp)\) exactly when \((u,0)\perp K^\perp\), or equivalently \((u,0)\in K\).
Taking orthogonal complements yields (9).
Dimension additivity, (7), and (9) prove
\[
 \Delta_{\mathcal M}(X:X,Y)
   =\dim_N\overline{\pi_X\mathcal V_{(X^*,Y^*)}}^{\|\cdot\|_2}. \tag{10}
\]

Now put \(B_i=-JD_iJ\in\mathcal B(H)\).
Conjugation by the antilinear isometry \(J\) preserves composition and Schatten norms; \(JP_\Omega J=P_\Omega\).
Equation (4) yields
\[
 [B_i,\rho(X_j^*)]=J[X_j,D_i]J=\delta_{ij}P_\Omega,\qquad
 [B_i,\rho(Y_k^*)]=J[Y_k,D_i]J\in\mathcal S_2(H).           \tag{11}
\]
Therefore the full commutator tuple of \(B_i\) belongs to \(\mathcal V_{(X^*,Y^*)}\), and its projection has \(P_\Omega\) in coordinate \(i\), with zeros in the other coordinates.
Replacing \(B_i\) by \(aB_i b\), \(a,b\in\mathcal M\), puts \(aP_\Omega b\) in that coordinate.
Such rank-one operators span an HS-dense subspace: \(aP_\Omega b\) sends \(\xi\) to \(\langle\xi,b^*\Omega\rangle a\Omega\), and \(\mathcal M\Omega\) is dense in \(H\).
Thus the projected closure in (10) is all \(\mathcal S_2(H)^d\).
Its dimension is \(d\), proving the relative equality in (5); (3) gives the absolute equality.

For explicit comparison with the source, the unstarred numerical formula also holds:
\[
 \Delta_{\mathcal M}(X:X,Y)
   =\dim_N\overline{\pi_X\mathcal V_{(X,Y)}}^{\|\cdot\|_2}.  \tag{12}
\]
Componentwise adjoint \(A:T\mapsto T^*\) is an antiunitary, exchanges \(\mathcal V_Z\) and \(\mathcal V_{Z^*}\), and commutes with coordinate projection.
It intertwines the \(N\) action with the conjugate-linear factor switch
\[
 a\otimes b^{\mathrm{op}}\longmapsto
       b^*\otimes(a^*)^{\mathrm{op}}.
\]
Under the standard-module identification this conjugation induces the same trace-preserving switch on the commutant, including its matrix amplification; the canonical traces of the corresponding projections agree.
Therefore \(A\) preserves the dimension of closed submodules.
Apply this observation to the two projected closures in (10) and (12).
The subspaces themselves are not claimed equal.

## Source relationship

[CS05](https://alainconnes.org/wp-content/uploads/betti.pdf), equations (3.9) and (3.13), supplies the relative construction in its self-adjoint-family setting; Lemma 2.16 supplies the WOT annihilator argument; Theorem 4.11 supplies the bounded-dual proof mechanism.
The checked author-hosted artifact has 39 pages; the relevant passages are printed/PDF pp.18--22 and 33.
Definition (2) extends the coordinate cycle construction.
Formula (12) recovers the projected-range dimension formula, making the closure of the projection explicit.

The source's self-adjoint set means closure under adjoints, as specified on p.19, not necessarily that each displayed generator is individually selfadjoint.
Its dual-first sign is converted to (4) by negating the dual operators.
Formula (11) checks that convention directly.
In arbitrary tuples the precise orthogonality formula uses \(Z^*\), as in (7); omitting this distinction would conflate the bilinear trace pairing with the Hermitian HS inner product.

[MSY23, Definition 6.1 and Proposition 6.2, pp.47--48](../literature/pdf/MSY23.pdf) already proves the arbitrary-tuple absolute conclusion without normality or generation.
This is attribution and comparison; the relative proof above is complete.
[CS05-U001](../audits/literature/CS05/Yin_U001.md#cs05-u001) records the exact source inspection and bounded literature search.
No separately stated general-tuple relative theorem was found in those checked sources and search leads.
The proper attribution is an explicit general relative formulation of the CS05 argument; no novelty or earliest-priority claim follows.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14 |
| status | open |
| reason | Complete candidate retained for separate review, including the adjoint correction in the transpose identity. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary bounded tuples, bounded duals and HS side commutators imply relative and absolute maximality. |
| argument | [Argument](#argument) | Cycle, annihilator, projection, rank-one density and adjoint dimension arguments. |
| support | [CS05 source check](../audits/literature/CS05/Yin_U001.md#cs05-u001) | Source relative construction and proof mechanism; standard finite module dimension conventions accepted. |

### Decision reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14 |
| status | proved |
| reason | A separately organized review checked the complete arbitrary-tuple definition and proof, including both transpose formulas, dimension preservation and precise source attribution, without a remaining gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full arbitrary bounded-tuple relative and absolute maximality, with no normality or generation assumption. |
| argument | [Argument](#argument) | Complete cycle, annihilator, projection, bounded-dual, density and adjoint-switch proof. |
| support | [CS05 source check](../audits/literature/CS05/Yin_U001.md#cs05-u001) | Verified source definition and proof mechanism, general absolute comparison, and bounded search limits. |
| review | [Independent whole review](../audits/reviews/Yin_R_F0182_v1.md#conclusion) | Definitions, statement, whole proof and source interfaces of this fixed version. |


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:55 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Full arbitrary bounded-tuple relative and absolute maximality, with no normality or generation assumption. |
| argument | [Exact material](#argument) | Complete cycle, annihilator, projection, bounded-dual, density and adjoint-switch proof. |
| support | [Exact material](../audits/literature/CS05/Yin_U001.md#cs05-u001) | Verified source definition and proof mechanism, general absolute comparison, and bounded search limits. |
| review | [Original finding](../audits/reviews/Yin_R_F0182_v1.md#conclusion) | Complete arbitrary-tuple relative/absolute maximal-Delta definitions, proof, annihilator/adjoint/dimension formulas and exact source interfaces; initial context for the earlier informal idea is unknown. |


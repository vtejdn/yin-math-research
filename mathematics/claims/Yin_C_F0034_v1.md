---
author: Yin
---

# Fraction-independent finite defects form an inverse-closed algebra

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Yin_C_F0034: Fraction Independence and the Algebra of Finite Defects

<a id="statement"></a>
<a id="yin_c_f0034"></a>

Role: lemma.
Provenance: project deduction extracted from existing complete proofs.
Extraction origin: agent-proposed shared-lemma organization, explicitly authorized by the user; see the [authorization record](../ledger/Yin_L_F0014_v1.md#authorization).
Proof version: [Yin_C_F0034-P1](#yin_c_f0034-p1), candidate, review pending.

### Extraction Provenance

The closability and fraction calculations originate in [Yin_C_F0029, Sections 5–6](Yin_C_F0029_v1.md#yin_c_f0029).
The earlier bounded-operator fraction calculations occur in [Yin_C_F0013, Sections 3–4](Yin_C_F0013_v1.md#yin_c_f0013).
These are extraction-provenance links, not dependencies on either theorem's conclusion.
The standalone statement below omits normality, generation, maximal Delta and free-field assumptions because none is used in these arguments.
Its scope and every invocation still require the new review recorded for this proof version.

### Statement and Scope

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let
\[
H=L^2(M,\tau),\qquad U=U(M).
\]
Use the inner product linear in its second variable.
Elements of \(M\) act on \(H\) by bounded left multiplication; the same symbols denote these actions.
Products and inverses in \(U\) mean the affiliated algebra operations.
A bounded element of \(M\) is called regular when it is invertible in \(U\), equivalently when its left action on \(H\) is injective with dense range.

Let \(d\geq1\) be finite.
Let \(\mathcal E\subseteq H\) be a Hilbert-dense complex-linear left \(M\)-module, and let
\[
D_{i,0}:\mathcal E\longrightarrow H,\qquad 1\leq i\leq d,
\]
be complex-linear operators with domain exactly \(\mathcal E\).
For each \(i\), assume that a Hilbert-dense complex-linear left \(M\)-module \(V_i\subseteq H\) satisfies
\[
V_i\subseteq\operatorname{Dom}D_{i,0}^*.
\tag{34.1}
\]
In particular, every \(D_{i,0}\) is closable.
Neither \(\mathcal E\) nor \(V_i\) is required to consist of bounded vectors, contain the vacuum, or be invariant under right multiplication.

For \(u\in U\), a bounded fraction pair is a choice
\[
u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
\qquad s,t\text{ regular}.
\tag{34.2}
\]
Every affiliated element admits such a pair.
Define its cleared defects on the specified common domain by
\[
T_i^{s,a,b,t}z=sD_{i,0}(bz)-aD_{i,0}(tz),
\qquad z\in\mathcal E.
\tag{34.3}
\]
All inputs of \(D_{i,0}\) in (34.3) lie in \(\mathcal E\).
Finite rank on this domain means finite complex dimension of the range, without an initial boundedness assumption.

Then the following assertions hold.

1. Every defect (34.3) is densely defined and closable.
   If it has finite rank, its Hilbert closure is the unique bounded finite-rank extension to all of \(H\), with the same rank.
2. For fixed \(u\) and \(i\), finite rank of (34.3) is independent of the bounded fraction pair.
   Whenever this rank is finite, its numerical value is also independent of the fraction pair.
3. The set
   \[
   \mathcal R=\{u\in U:T_i^{s,a,b,t}\text{ has finite rank for every }i
          \text{ for some bounded fraction pair}\}
   \tag{34.4}
   \]
   is a unital complex subalgebra of \(U\), closed under inversion of every one of its elements that is invertible in \(U\).
   In (34.4), “some” can equivalently be replaced by “every”.
4. If \(X_1,\ldots,X_m\in M\) satisfy
   \[
   [D_{i,0},X_j]|_{\mathcal E}\text{ has finite rank}
   \quad(1\leq i\leq d,\ 1\leq j\leq m),
   \tag{34.5}
   \]
   then, with \(A=\mathbb C\langle X_1,\ldots,X_m\rangle\),
   \[
   \operatorname{Div}_U A\subseteq\mathcal R.
   \tag{34.6}
   \]
   Here \(\operatorname{Div}_U A\) denotes the smallest unital complex subalgebra of \(U\) containing \(A\) and closed under inverses of its elements that are units of \(U\).
   This notation does not assert that the resulting algebra is a division ring.

In particular, the usual identities \([D_{i,0},X_j]=\delta_{ij}P_\Omega\) on \(\mathcal E\) are sufficient for (34.5) when the index sets agree.
The generators need not be normal, selfadjoint, algebraically free, or generators of \(M\).
No reverse inclusion in (34.6) is asserted.

### Proof Dependencies for Yin_C_F0034-P1

- [Yin_C_F0031-P1](Yin_C_F0031_v1.md#yin_c_f0031-p1) supplies the bounded extension of a densely defined closable finite-range operator and cancellation through bounded injective left and dense-range right operators when the right operator preserves the initial domain.
  Its hypotheses are checked below each time it is used.
- The accepted finite-tracial affiliated fraction and regularity interface is recorded in [Miy22-U006](../audits/literature/Miy22/Yin_U006.md#miy22-u006), with its shared affiliation foundations and source-inspection limits retained.
  It supplies the algebra \(U(M)\), the inclusion of \(M\), bounded left and right fractions for every affiliated element, and the stated operator meaning of bounded regularity.
  Only this infrastructure is accepted here; the common-multiple, defect and algebra calculations are proved below.
- Hilbert adjoints, finite-dimensional range, and complex linearity are used at their usual elementary scope.

For clarity, bounded fraction existence can be realized by
\[
s=(1+uu^*)^{-1/2},\quad a=su,
\qquad t=(1+u^*u)^{-1/2},\quad b=ut.
\tag{34.7}
\]
The affiliated functional calculus makes \(s,t\) bounded regular and \(a,b\) bounded.
No boundedness of \(s^{-1}\), \(t^{-1}\), or \(u\) is inferred.

<a id="yin_c_f0034-p1"></a>
### Yin_C_F0034-P1: Complete Candidate Proof

#### 1. Defect Closability and Finite-Rank Extensions

Fix a bounded fraction pair and an index \(i\).
For \(w\in V_i\) and \(z\in\mathcal E\), left-module invariance gives \(s^*w,a^*w\in V_i\) and \(bz,tz\in\mathcal E\).
Thus every adjoint evaluation in the identity
\[
\begin{aligned}
\langle w,T_i^{s,a,b,t}z\rangle
&=\langle s^*w,D_{i,0}(bz)\rangle
  -\langle a^*w,D_{i,0}(tz)\rangle\\
&=\left\langle
 b^*D_{i,0}^*(s^*w)-t^*D_{i,0}^*(a^*w),z
 \right\rangle
\end{aligned}
\tag{34.8}
\]
is defined.
Consequently \(V_i\) is contained in the adjoint domain of the defect.
Its density makes the defect closable, proving the first part of assertion 1.
If the range is finite dimensional, the finite-rank extension part of Yin_C_F0031 applies to this densely defined closable operator.
It gives precisely the unique bounded finite-rank closure asserted in 1.

We will also use the cancellation part of Yin_C_F0031 as follows.
For bounded regular \(y,y'\in M\), the left action of \(y\) is injective and that of \(y'\) has dense range.
Moreover \(y'\mathcal E\subseteq\mathcal E\) by the left-module property.
Thus, for any of the closable defects \(T\), finite rank of
\[
z\longmapsto yT(y'z),\qquad z\in\mathcal E,
\tag{34.9}
\]
is equivalent to finite rank of \(T\), and their finite numerical ranks agree.
In particular, no graph-density assumption on \(y'\mathcal E\), or global operator-norm-to-\(L^2\) estimate, is being added.

#### 2. Common Bounded Regular Multiples

If \(s_1,s_2\in M\) are regular, write a bounded left fraction
\[
s_1s_2^{-1}=x^{-1}y,
\qquad x,y\in M,\quad x\text{ regular}.
\]
The ratio \(s_1s_2^{-1}\) is a unit of \(U\).
Hence \(y=x(s_1s_2^{-1})\) is a unit of \(U\), so the bounded element \(y\) is also regular.
Multiplication inside \(U\) yields the bounded identity
\[
xs_1=ys_2.
\tag{34.10}
\]
Both sides are regular because they are products of units of \(U\).

For regular \(t_1,t_2\in M\), write a bounded right fraction
\[
t_1^{-1}t_2=pq^{-1},
\qquad p,q\in M,\quad q\text{ regular}.
\]
The same unit argument makes \(p\) regular and gives
\[
t_1p=t_2q,
\tag{34.11}
\]
a common bounded regular right multiple.
These constructions can be applied independently to left and right denominators.

#### 3. Fraction Independence and Numerical Ranks

Let \((s,a,b,t)\) and \((s_1,a_1,b_1,t_1)\) be bounded fraction pairs for the same \(u\).
By (34.10)–(34.11), choose bounded regular \(x,y,x',y'\) satisfying
\[
xs=ys_1,\qquad tx'=t_1y'.
\]
Multiplication of the equal affiliated fractions then gives bounded identities
\[
xa=ya_1,\qquad bx'=b_1y'.
\tag{34.12}
\]
For example, both sides of the first identity equal \((xs)u=(ys_1)u\) in \(U\); both sides of the second equal \(u(tx')=u(t_1y')\).

Every argument of \(D_{i,0}\) below belongs to \(\mathcal E\).
Using these four coefficient identities gives
\[
\begin{aligned}
yT_i^{s_1,a_1,b_1,t_1}(y'z)
&=ys_1D_{i,0}(b_1y'z)-ya_1D_{i,0}(t_1y'z)\\
&=xsD_{i,0}(bx'z)-xaD_{i,0}(tx'z)\\
&=xT_i^{s,a,b,t}(x'z)
\qquad(z\in\mathcal E).
\end{aligned}
\tag{34.13}
\]
If the old defect has finite rank, the right side has finite rank.
The cancellation implication (34.9) therefore makes the new defect finite rank.
Interchanging the fraction pairs proves equivalence.
Applying the numerical-rank statement of (34.9) on both sides of (34.13) shows
\[
\operatorname{rank}T_i^{s_1,a_1,b_1,t_1}
=\operatorname{rank}T_i^{s,a,b,t}
\tag{34.14}
\]
whenever one, and hence both, is finite.
Their bounded closures have the same ranks by assertion 1.
This proves assertion 2 and the equivalence of the two definitions of \(\mathcal R\).
The operator itself may change when the fractions change; (34.14) asserts equality of finite numerical ranks.

#### 4. Constants, Addition and Scalar Multiplication

A scalar \(c1\) has the fraction pair \((1,c1,c1,1)\).
Its defect vanishes because \(D_{i,0}(cz)=cD_{i,0}z\).
Thus \(\mathbb C1\subseteq\mathcal R\).
The use of the bounded coefficient \(1\) does not require the vacuum vector to belong to \(\mathcal E\).

Take \(u_1,u_2\in\mathcal R\) and bounded fraction pairs for each.
Use common regular left and right denominators to express both as
\[
u_\ell=s^{-1}a_\ell=b_\ell t^{-1},
\qquad \ell=1,2,
\]
with bounded numerators and common regular \(s,t\).
Assertion 2 ensures that their defects at these pairs are finite rank.
The sum has bounded fraction pair
\[
u_1+u_2=s^{-1}(a_1+a_2)=(b_1+b_2)t^{-1}.
\]
Complex linearity of \(D_{i,0}\) makes its defect the sum of the two defects, so the sum belongs to \(\mathcal R\).
For any \(c\in\mathbb C\), the pair \((s,ca,cb,t)\) represents \(cu\) and has defect \(cT_i^{s,a,b,t}\).
It follows that \(\mathcal R\) is a complex-linear subspace containing the unit.

#### 5. Products

Write
\[
u_\ell=s_\ell^{-1}a_\ell=b_\ell t_\ell^{-1},
\qquad \ell=1,2,
\]
with finite-rank defects.
Bounded fraction existence applied to \(a_1s_2^{-1}\) and \(t_1^{-1}b_2\) gives
\[
a_1s_2^{-1}=x^{-1}y,
\qquad t_1^{-1}b_2=pq^{-1},
\tag{34.15}
\]
where \(x,y,p,q\in M\) and \(x,q\) are regular.
Neither ratio is assumed invertible, so \(y,p\) are not assumed regular.
The corresponding bounded identities are
\[
xa_1=ys_2,\qquad t_1p=b_2q.
\tag{34.16}
\]
Associativity in \(U\) gives
\[
\begin{aligned}
u_1u_2
&=s_1^{-1}(a_1s_2^{-1})a_2
 =(xs_1)^{-1}ya_2,\\
u_1u_2
&=b_1(t_1^{-1}b_2)t_2^{-1}
 =b_1p(t_2q)^{-1}.
\end{aligned}
\tag{34.17}
\]
The denominators \(xs_1\) and \(t_2q\) are bounded regular.
For \(z\in\mathcal E\), the defect at (34.17) is
\[
xs_1D_{i,0}(b_1pz)-ya_2D_{i,0}(t_2qz).
\tag{34.18}
\]
On the other hand, expanding
\[
xT_i^{s_1,a_1,b_1,t_1}(pz)
+yT_i^{s_2,a_2,b_2,t_2}(qz)
\tag{34.19}
\]
gives the first and last terms of (34.18), together with
\[
-xa_1D_{i,0}(t_1pz)+ys_2D_{i,0}(b_2qz).
\]
These middle terms cancel because (34.16) identifies both their bounded outside coefficients and their inputs of \(D_{i,0}\).
The inputs are actual equal vectors of \(\mathcal E\), since it is a left \(M\)-module.
Thus (34.18) equals (34.19).
Each summand of (34.19) has finite rank: the inner multiplier preserves \(\mathcal E\), the original defect has finite-dimensional range, and the outer multiplier is bounded.
Therefore \(u_1u_2\in\mathcal R\).

#### 6. Inverses and Division Closure

Suppose \(u\in\mathcal R\) is invertible in \(U\), and fix a bounded fraction pair (34.2) with finite-rank defects.
Since \(a=su\) and \(b=ut\) are products of units of \(U\), the bounded elements \(a,b\) are regular.
The inverse has bounded fraction pair
\[
u^{-1}=a^{-1}s=tb^{-1}.
\]
Its defect on \(\mathcal E\) is
\[
aD_{i,0}(tz)-sD_{i,0}(bz)=-T_i^{s,a,b,t}z.
\tag{34.20}
\]
It is finite rank, so \(u^{-1}\in\mathcal R\).
Together with Steps 4–5, this proves assertion 3.

Under (34.5), the fraction pair \((1,X_j,X_j,1)\) shows \(X_j\in\mathcal R\) for every \(j\).
As \(\mathcal R\) is a unital complex algebra, it contains \(A\).
As it is closed under taking inverses of its ambient units, it contains the smallest algebra with those properties, namely \(\operatorname{Div}_U A\).
This proves assertion 4 and completes Yin_C_F0034-P1.

### Checks, Limits and Review Status

Zero and scalar elements use no inverse, and the product proof does not assume the auxiliary numerators in (34.15) are regular.
The inverse step applies only to units of \(U\), so zero divisors in \(U\) cause no missing case.
Every cancellation of a right denominator uses Yin_C_F0031 with an explicitly invariant dense initial domain, not an unproved boundedness assertion for a general unbounded operator.
All fraction representatives and operator compositions are bounded-coefficient expressions on \(\mathcal E\); no raw commutator with an arbitrary affiliated input is introduced.

The hypotheses do not make \(\mathcal R\) a free field or prove equality in (34.6).
For example, take \(M=\mathbb C\oplus\mathbb C\) with its faithful equal-weight trace, \(\mathcal E=V_1=H=M\), \(D_{1,0}=0\), and \(X_1=1\).
Then every defect vanishes, so \(\mathcal R=U=M\), whereas \(\operatorname{Div}_U\mathbb C1=\mathbb C1\) is a proper subalgebra.
This is consistent with the optional assertion, which imposes no generation or dual-system condition beyond finite-rank commutators.

Yin_C_F0034-P1 awaits separate review of the statement, Yin_C_F0031 interface, all fraction calculations and scope.
Its extraction sources were previously reviewed at their own scopes, but those reviews do not automatically certify this separately stated lemma.
No numerical test, proof-assistant verification or historical novelty assessment is asserted.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0034-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0021_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:45 |
| status | proved |
| reason | Select the actual retained finding scopes and their known mathematical-development relationships, preserving status, authorized role, exact statement/proof/dependency selections and all historical decisions. No new mathematical review is asserted. |

Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0034-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0021_v1.md#fraction-algebra-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0021_v1.md).

Material covered by that review: [Exact material](Yin_C_F0034_v1.md), [Exact material](Yin_C_F0035_v1.md) (together retain the original whole-source scope).

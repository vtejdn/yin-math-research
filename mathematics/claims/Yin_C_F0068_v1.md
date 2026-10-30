---
author: Yin
---

# Maximal-Delta finite-rank rationality and its dual-system specializations

Date: 2026-10-09T16:42.
Human author: Yin.
Provenance: project deduction assembled from the accepted inputs identified below.
Authorization: the user requested Claim registration, an independent audit, and verification that the result recovers the dual-system and conjugate-variable cases.
Initial role: agent-proposed lemma for reuse.
The user designated the Claim as Theorem on 2026-10-10; the current decision below records that role change.
Extraction provenance: the exploratory synthesis Yin_D_F0008, dated 2026-10-10, is preserved mathematically in this fixed material; its redundant working copy was removed after acceptance.
It is not a proof dependency.
The preceding mathematical discussion and its local checks are not substituted for the independent reviews selected below.

## Current assessment
[Selected decision](#decision-theorem-role-2026-10-10)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace.
Set H=L2(M,tau), Omega=1, P=P_Omega and U=U(M).
Inner products are linear in the second variable.
Elements of M act by left multiplication unless rho is written; rho(x)q=qx is right multiplication.
Fix a finite bounded tuple X=(X_1,...,X_d), d>=1, and put A=C<X_1,...,X_d> and F=Div_U A.
All tensor products below are algebraic, not completed.

**A. Maximal-Delta criterion.**
Assume Delta(X)=d.
Neither normality nor M=W*(X) is required for this part.
For every u in U, the following three conditions are equivalent:
\[
 u\in F; \tag{A1}
\]
\[
 u\otimes1-1\otimes u=\sum_{i=1}^d\Psi_i(k_i),
 \quad k_i\in U\otimes_{\mathbb C}U,\quad
 \Psi_i(g\otimes h)=gX_i\otimes h-g\otimes X_i h; \tag{A2}
\]
\[
 \begin{gathered}
 \text{there exist }s,a,b,t\in M,\quad s,t\text{ invertible in }U,\quad
 u=s^{-1}a=bt^{-1},\\
 \text{and finite-rank }T_i\in B(H)\text{ such that}\\
 \sum_{i=1}^d[\rho(X_i),T_i]=aPt-sPb.
 \end{gathered}\tag{A3}
\]
The tensors in (A2) are unique.
For a fixed quadruple (s,a,b,t), a finite-rank solution tuple in (A3), if it exists, is unique.
No specified dual operators occur in these conditions.

**B. Sharpness.**
Even for two bounded selfadjoint generators of M with Delta(X)=2, a bounded element of F need not satisfy (A3) for the trivial fraction s=t=1.
Such a tuple need not admit linear operators defined on all of M Omega with the generator dual relations, even without an adjoint-domain requirement.
The explicit example is h uniform on (0,1), S standard semicircular free from h, X=(h,hSh), and u=S.
A nontrivial bounded fraction for the same u does satisfy (A3).

<a id="dual-specializations"></a>
**C. Dual-system realization and its two applications.**
Suppose now that the X_i are normal, M=W*(X), and there are densely defined linear D_i on H such that
\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
 \qquad [D_i,X_j]|_{M\Omega}=\delta_{ij}P|_{M\Omega}. \tag{D}
\]
Write D_{i,0}=D_i|_{M Omega} and \(\widehat D_i=\overline{D_{i,0}}\).
Then Delta(X)=d, and for every u in U and every legal bounded fraction Q=(s,a,b,t),
\[
 u\in F
 \quad\Longleftrightarrow\quad
 x\Omega\longmapsto sD_{i,0}(bx\Omega)-aD_{i,0}(tx\Omega)
 \text{ has finite rank for all }i. \tag{D1}
\]
Equivalently, with
\[
 \mathcal E_i(Q)=\{q\in H:bq,tq\in\operatorname{Dom}\widehat D_i\},
\]
each raw expression
\[
 q\longmapsto s\widehat D_i(bq)-a\widehat D_i(tq) \tag{D2}
\]
on its entire natural domain \(\mathcal E_i(Q)\) has a bounded finite-rank extension.
Every \(\mathcal E_i(Q)\), and their intersection, contains M Omega and is dense, whether or not u is rational.
Existence of (D1) or (D2) for one common Q is equivalent to existence for every Q.
The bounded representatives are unique and satisfy (A3); their rank in each coordinate is independent of Q.

For rational u let k_i(u) denote the unique affiliated tensors in (A2).
The representatives just described satisfy
\[
 \Theta^{-1}(T_i(Q))=s\,k_i(u)\,t
 \in H\otimes_{\rm alg}H,\qquad
 \Theta(g\otimes h)q=g\tau(hq). \tag{D3}
\]
In particular, for f in M,
\[
 f\in F
 \iff [D_{i,0},f]|_{M\Omega}\text{ has finite rank for all }i. \tag{D4}
\]
This is also equivalent to invariance \(f\operatorname{Dom}\widehat D_i\subseteq\operatorname{Dom}\widehat D_i\) together with a bounded finite-rank commutator on that full closed domain, for every i.

Condition (D), and consequently (D1)--(D4), apply in each of the following cases:
- X is a bounded normal generating tuple and has a bounded dual system B_i on H, with [B_i,X_j]=delta_ij P; take D_i=B_i.
- X is a bounded selfadjoint generating tuple with L2 conjugate variables xi_i.
  Take the canonical polynomial operator \(D_i^0=(\mathrm{id}\otimes\tau)\partial_i\) and its Hilbert closure.
  Its all-M and adjoint domains follow from the analytic finite-Fisher estimates, not from Delta alone.
  The closed operator in (D2) is exactly this canonical closure.

Parts A and B do not imply (D).
Part C uses the additional analytic hypotheses explicitly.
It reconstructs the affiliated and bounded-element rationality criteria, not an equality with scalar division closure inside M.

<a id="argument"></a>
## Argument P1

The complete proof consists of Sections 1--5 below.
Section 5 proves the dual/conjugate specialization without invoking the final rationality assertions of C_F0024, C_F0022 or C_F0013.

## 1. Existing inputs and the question

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, H=L2(M,tau), Omega=1, P=P_Omega, and U=U(M).
Let X=(X_1,...,X_d) be bounded elements of M, and assume Delta(X)=d.
Put A=C<X_1,...,X_d> and F=Div_U A.
Normality and generation of M are allowed but are not used in the positive algebraic argument.

The exact reused inputs are:

- [MSY23-U002](../audits/literature/MSY23/Yin_U002_v1.md#msy23-u002): maximal Delta is equivalent to absence of a nonzero tuple of finite-rank operators satisfying sum_i[rho(X_i),T_i]=0.
  Here rho(x) is right multiplication.
- [MSY23-U004](../audits/literature/MSY23/Yin_U004_v1.md#msy23-u004): maximal Delta supplies an injective free-field evaluation, and F is its image, a same-unit division subring of U.
- [C_F0035](Yin_C_F0035_v1.md#yin_c_f0035): u tensor_F 1 = 1 tensor_F u if and only if u belongs to F.
- [C_F0007, Section 1](Yin_C_F0007_v1.md): its extension of finite-cycle injectivity from L2 tensors to affiliated tensors uses only maximal Delta and clearing finitely many outer denominators.
  The full C_F0007 statement has stronger bounded-dual assumptions; only the explicit argument is reused below under its actual inputs.
- [MSY23-U005](../audits/literature/MSY23/Yin_U005_v1.md#msy23-u005), Section 6 entropy interface: freely independent atomless bounded selfadjoint variables have maximal Delta.
  This is an accepted source interface, not a new audit of free-entropy theory.

Primary source checked for the free-field background: Mai, Speicher and Yin, The free field: realization via unbounded operators and Atiyah property, [arXiv:1905.08187](https://arxiv.org/abs/1905.08187).
The certificate and counterexample below are assembled deductions, not attributed as statements of that paper.

The earlier [C_F0024](Yin_C_F0024_v1.md#yin_c_f0024) assumes actual duals and their adjoints have all bounded vectors in their domains.
[C_F0063](Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion) still starts from the specified polynomial-core dual data of C_F0025 and actual liberation closures; its word "intrinsic" does not make it a Delta-only theorem.

## 2. An affiliated tensor criterion

All tensor products in this section are algebraic.
Define
\[
 \Psi_i(g\otimes h)=gX_i\otimes h-g\otimes X_i h,
 \qquad \Psi((k_i)_i)=\sum_i\Psi_i(k_i),
 \qquad \delta u=u\otimes1-1\otimes u.
\]
The outer U-bimodule action is
\[
 a\cdot(g\otimes h)\cdot b=ag\otimes hb.
\]
Each Psi_i respects this action.

**Proposition.**
Under Delta(X)=d, for every u in U,
\[
 u\in F
 \quad\Longleftrightarrow\quad
 \delta u=\sum_i\Psi_i(k_i)
 \quad\text{for some }k_i\in U\otimes_{\mathbb C}U.
 \tag{T}
\]
When they exist, these tensors are unique.

For the forward implication, choose a finite scalar rational expression for u in the division ring F.
Form its derivative tensors by
\[
 \partial_i c=0\ (c\in\mathbb C),\qquad
 \partial_i X_j=\delta_{ij}(1\otimes1),\qquad
 \partial_i(vw)=(\partial_i v)\cdot w+v\cdot(\partial_i w),
\]
\[
 \partial_i(v^{-1})=-v^{-1}\cdot(\partial_i v)\cdot v^{-1}.
\]
All resulting tensors lie in F tensor_C F.
The map delta satisfies the same product and inverse identities, and delta(X_j)=Psi_j(1 tensor 1).
Induction gives (T).
This construction uses a chosen expression; uniqueness below subsequently proves expression independence.

For the reverse implication, project U tensor_C U onto U tensor_F U.
Every Psi_i(k_i) vanishes by balancing over X_i in F.
Thus u tensor_F 1=1 tensor_F u, and C_F0035 gives u in F.

For uniqueness, suppose Psi((k_i))=0.
Choose finite decompositions of all k_i.
There exist bounded regular s,t in M such that every first factor g satisfies sg in M and every second factor h satisfies ht in M.
To see this, put finitely many first factors into an affiliated row G and take s=(1+GG*)^(-1/2); for an affiliated column C of the second factors take t=(1+C*C)^(-1/2).
These are bounded, injective and have dense range, and the indicated products are bounded.
Finite affiliated matrix functional calculus is used here.

Then s k_i t lies in M tensor_C M, and Psi((s k_i t))=0.
The identification
\[
 \Theta(g\otimes h)q=g\tau(hq),\qquad g,h\in H,
\]
is a linear bijection from H tensor_alg H to the finite-rank operators on H.
It satisfies
\[
 [\rho(X_i),\Theta(k)]=\Theta(\Psi_i(k)).
 \tag{I}
\]
Maximal Delta therefore implies s k_i t=0 for each i.
Outer multiplication by the units s,t of U is invertible, so k_i=0.
This proves uniqueness and rational-expression independence.

## 3. A finite-rank certificate using some bounded fraction

Call Q=(s,a,b,t) a legal bounded fraction quadruple for u if s,a,b,t belong to M, s,t are regular (invertible in U), and u=s^(-1)a=bt^(-1).

**Proposition.**
Under Delta(X)=d,
\[
 u\in F
 \quad\Longleftrightarrow\quad
 \begin{gathered}
 \text{there exist a legal }Q=(s,a,b,t)
 \text{ and finite-rank }T_i\in B(H)\\
 \text{such that }\sum_i[\rho(X_i),T_i]=aPt-sPb.
 \end{gathered}
 \tag{FR}
\]
Products on the right use bounded left multiplication.
No D_i is part of this criterion.
For a fixed Q, a finite-rank solution tuple is unique.

If u belongs to F, take the tensors k_i from (T).
Choose s clearing on the left both u and all finitely many first tensor factors, and choose t clearing on the right both u and all second factors.
Put a=su, b=ut and T_i=Theta(s k_i t).
Then a,b are bounded and
\[
 \sum_i\Psi_i(s k_i t)
 =s(\delta u)t=a\otimes t-s\otimes b.
\]
Apply (I) and Theta to obtain (FR).

Conversely, every finite-rank T_i has a tensor l_i in H tensor_alg H, canonically included in U tensor_C U.
Equation (I) and injectivity of Theta give
\[
 \sum_i\Psi_i(l_i)=a\otimes t-s\otimes b.
\]
Outer division by s,t gives (T) with k_i=s^(-1) l_i t^(-1).
Thus u belongs to F.
Uniqueness for fixed Q follows directly by subtracting two solutions and using maximal Delta.

The existential quantifier over Q is essential.
The positive argument does not assert that every prescribed Q clears the derivative factors into L2.
The next section proves that such an assertion is false.

<a id="sharpness-proof"></a>
## 4. A selfadjoint example separating some from every fraction

Take h(t)=t in L-infinity((0,1),dt), and let S be a standard semicircular element free from h in their finite tracial free-product algebra M.
Put
\[
 Y=hSh,\qquad X=(h,Y),\qquad q=h^{-1}.
\]
Then h and Y are bounded selfadjoint,
\[
 q\notin H,\qquad \|q\|_2^2=\int_0^1 t^{-2}\,dt=\infty.
\]
Nevertheless S=qYq is a bounded element of F.
Also W*(h,Y)=M: with \(e_n=\mathbf 1_{[1/n,1]}(h)\), the bounded expression e_n qYq e_n equals e_n S e_n, converges strongly to S, and belongs to W*(h,Y).

The sandwich mechanism is related to [C_F0012](Yin_C_F0012_v1.md#yin_c_f0012), but this is a different distribution: that Claim uses 4t^3 dt, for which q is in L2.
Its bounded-dual conclusion is not transferred to the uniform-law example.

### 4.1 Maximal Delta survives the sandwich

The free atomless pair (h,S) has Delta(h,S)=2 by the accepted MSY23-U005 interface.
Write
\[
 R=\rho(h),\qquad B=\rho(S),\qquad \rho(Y)=RBR.
\]
For any bounded operator T,
\[
 [RBR,T]=[R,BRT+TRB]+[B,RTR].
 \tag{S}
\]
If finite-rank T_h,T_Y satisfy [R,T_h]+[RBR,T_Y]=0, (S) produces the base-pair cycle
\[
 [R,T_h+BRT_Y+T_YRB]+[B,RT_YR]=0.
\]
Hence RT_YR=0 and T_h+BRT_Y+T_YRB=0.
Since R is injective with dense range, T_Y=0, and then T_h=0.
Thus Delta(h,Y)=2.

### 4.2 The trivial fraction has no finite-rank certificate

For u=S choose s=t=1 and a=b=S.
If (FR) held for this Q, then
\[
 [R,T_h]+[RBR,T_Y]=SP-PS=[B,P].
\]
Using (S), maximal Delta of the base pair gives
\[
 RT_YR=P.
\]
Apply this to Omega:
\[
 R(T_Yh)=\Omega.
\]
The vector T_Yh belongs to H, but right multiplication by h can send a vector v to Omega only if v=h^(-1)=q in U.
Since q is not in H, this is impossible.

Thus an element of F intersect M need not admit a certificate for the trivial fraction, even for a bounded selfadjoint generating pair with maximal Delta.

Equivalently, the unique affiliated rational derivative in the Y coordinate is q tensor q, which is not in H tensor_alg H.
The preceding operator proof does not need this equivalent description.

### 4.3 An explicit good fraction

For the same u=S choose
\[
 s=t=h,\qquad a=hS,\qquad b=Sh.
\]
Then a bounded finite-rank certificate is
\[
 T_Y=P,\qquad T_h=-PSh-hSP.
\]
Indeed these correspond under Theta to
\[
 l_Y=1\otimes1,\qquad l_h=-1\otimes Sh-hS\otimes1.
\]
A direct application of Psi_h and Psi_Y gives
\[
 \Psi_h(l_h)+\Psi_Y(l_Y)=hS\otimes h-h\otimes Sh,
\]
which is exactly the right side of (FR) for this Q.

### 4.4 The original all-M dual system cannot exist

Suppose a linear operator D_Y has all of M Omega in its domain and satisfies
\[
 [D_Y,h]=0,\qquad [D_Y,hSh]=P
 \quad\text{on }M\Omega.
\]
All products needed below have bounded-vector inputs.
Expanding on Omega gives
\[
 h\bigl(D_Y(Sh\Omega)-S D_Y(h\Omega)\bigr)=\Omega.
\]
The vector in parentheses lies in H, whereas the equation hv=Omega forces v=q not in H.
This is a contradiction.

The obstruction already excludes an all-M dual without any adjoint-domain requirement.
Therefore maximal Delta cannot supply the common hypothesis of C_F0024.


<a id="proof-dual-specializations"></a>
## 5. Recovering the dual-system and conjugate-variable criteria

### 5.1 Exact analytic inputs and absence of circularity

The additional direct inputs are:
- [C_F0034-P1](Yin_C_F0034_v1.md#yin_c_f0034-p1), with E=V_i=M Omega: finite-defect closability, bounded finite-rank extensions, independence of fractions and their numerical ranks, and closure of the finite-defect class under affiliated rational operations.
  This is a standalone fraction-calculus lemma, not the final rationality criterion.
- [C_F0033-P1](Yin_C_F0033_v1.md#yin_c_f0033-p1): for normal generators and closable duals on the indicated left module, bounded cleared defects satisfy the fundamental right-commutator identity.
  This lemma does not conclude rationality or maximal Delta.
- [C_F0022, analytic Sections 2--3](Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input): construction of the canonical polynomial dual, its adjoint formula, the operator-norm-to-L2 estimates, extension of both actual domains to M Omega, and generator identities there.
  Its affiliated-rationality conclusion is not used.

For transparency, the short maximal-Delta argument from [C_F0024, Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors), the adjoint bridge from [C_F0067, Section 4](Yin_C_F0067_v1.md#4-adjoint-testing-extends-agreement-to-the-full-natural-domain), and the graph-core passage are reproduced below.
These identify reused arguments and are not dependencies on those Claims' final rationality conclusions.
The proof graph is: source maximal-Delta/free-field inputs and C_F0035 imply Part A; standalone C_F0034/C_F0033 and (D) connect actual defects to Part A; the finite-Fisher analytic construction verifies (D).

### 5.2 Condition (D) supplies maximal Delta

Because the adjoint of D_i contains M Omega, the adjoint of its restriction D_{i,0} also contains M Omega.
Thus D_{i,0} is closable.

Use the left-multiplication form of the finite-rank-cycle characterization from MSY23-U002.
Suppose sum_i[T_i,X_i]=0, with all T_i finite rank.
Choose a bounded regular r in M making every vector in the finite-dimensional sum of their ranges bounded after right multiplication, and set Q_r=rho(r).
For arbitrary c,e in M, put
\[
 S_i=\rho(c)Q_rT_i\rho(e).
\]
These operators have ranges in M Omega and satisfy the same zero-cycle identity.
Every D_{j,0}S_i is an everywhere-defined bounded finite-rank operator: choose a finite basis of the range of S_i and use its bounded coordinate functionals.
The dual relations give
\[
 0=\sum_i(D_{j,0}S_iX_i-D_{j,0}X_iS_i)
   =\sum_i[D_{j,0}S_i,X_i]-PS_j.
\]
Taking the ordinary trace is legitimate, since all operators in this equality are bounded and each summand is finite rank.
Consequently
\[
 0=\operatorname{Tr}(PS_j)
   =\langle\rho(c)^*\Omega,Q_rT_j\rho(e)\Omega\rangle .
\]
Both test-vector families are independently dense.
Hence Q_rT_j=0, and injectivity of Q_r gives T_j=0.
Therefore Delta(X)=d.

The needed simultaneous right denominator is the construction from Section 2 applied to finitely many H vectors.
No boundedness of D_i on H, normalization at Omega, or adjoint beyond the stated domain condition is used in this maximality step.

### 5.3 All fractions and actual finite-rank representatives

Take E=V_i=M Omega in C_F0034.
E and V_i are dense left M-modules, D_{i,0} has domain E, and V_i is contained in its adjoint domain by (D).
Generator defects are delta_ij P, hence finite rank.
Every hypothesis of that lemma is now explicit.

Its forward inclusion gives, for u in F, finite rank of the actual cleared defects for every Q.
It also gives unique bounded finite-rank extensions T_i(Q) and coordinatewise rank independence.
No maximal-Delta-only argument is being used to claim the every-fraction assertion.

Conversely, suppose the actual cleared defects are finite rank for some Q.
C_F0034 gives their bounded extensions.
The hypotheses of C_F0033 hold: the X_i are normal and generate M; D_{i,0} is closable on the dense left M-module M Omega; the generator dual relations hold there; and sb=at follows from s^{-1}a=bt^{-1}.
Thus
\[
 \sum_i[\rho(X_i),T_i(Q)]=aPt-sPb.
\]
Part A, already proved without the dual data, implies u in F.
This proves (D1) with SOME/EVERY.

The same identity holds for the representatives of every rational u.
Applying Theta inverse and outer division by s,t, their tensors solve (A2).
Its uniqueness gives (D3).
Thus the L2 membership of the cleared rational tensors for every Q is a derived analytic consequence, not a hypothesis imported into Part A.

### 5.4 Full natural domains and bounded-element graph invariance

By construction, M Omega is contained in the domains of \(\widehat D_i\) and \(\widehat D_i^*\).
Hence every \(\mathcal E_i(Q)\) contains M Omega, as does the intersection.

Fix i and a bounded representative K agreeing with the cleared defect on M Omega.
For eta in M Omega put
\[
 v_\eta=b^*\widehat D_i^*(s^*\eta)
              -t^*\widehat D_i^*(a^*\eta).
\]
The adjoint-domain hypothesis makes these terms well-defined.
For z in M Omega,
\[
 \langle v_\eta,z\rangle
 =\langle\eta,s\widehat D_i(bz)-a\widehat D_i(tz)\rangle
 =\langle K^*\eta,z\rangle.
\]
Density gives v_eta=K*eta.
For any q in \(\mathcal E_i(Q)\), the same adjoint pairing therefore gives
\[
 \langle\eta,s\widehat D_i(bq)-a\widehat D_i(tq)\rangle
 =\langle K^*\eta,q\rangle=\langle\eta,Kq\rangle.
\]
Density of the test vectors eta proves equality on the entire natural domain.
Conversely, a bounded finite-rank representative there restricts to one on M Omega.
This proves (D2), uniqueness, and its equivalence to (D1).
No simultaneous graph approximation of bq and tq is assumed.

For bounded f take Q=(1,f,f,1) in (D1).
To obtain the full-domain version of (D4), take q_n in M Omega converging to q in the graph norm of \(\widehat D_i\), which is possible by its definition.
The identity
\[
 D_{i,0}(f q_n)=fD_{i,0}q_n+T_i q_n
\]
and closedness imply \(fq\in\operatorname{Dom}\widehat D_i\) and the same bounded commutator formula there.
The converse follows by restriction to M Omega.
The choice of closure is explicit; no arbitrary larger closed extension is substituted.

### 5.5 Bounded duals and canonical conjugate-variable duals

For bounded B_i, both Hilbert domains are H, and the restrictions have closures B_i.
This checks (D) directly and proves the stated bounded-dual specialization.

For selfadjoint X with xi_i in L2, the polynomial dual \(D_i^0=(\mathrm{id}\otimes\tau)\partial_i\) is well-defined and closable.
The exact analytic input from C_F0022 Sections 2--3 gives
\[
 (D_i^0)^*p=p\xi_i-D_i^0p,\quad
 \|D_i^0p\|_2\le4\|\xi_i\|_2\|p\|,\quad
 \|(D_i^0)^*p\|_2\le5\|\xi_i\|_2\|p\|.
\]
The right-hand norms are operator norms.
Kaplansky approximation and weak closedness of the actual Hilbert graphs give
\[
 M\Omega\subseteq\operatorname{Dom}\overline{D_i^0}
       \cap\operatorname{Dom}(D_i^0)^*.
\]
The same bounded-set weak continuity extends the polynomial generator relations to M Omega.
The analytic source includes the one-variable reduction, so no d>=2 restriction is added here.

Set \(D_i=\overline{D_i^0}\).
Since the polynomial graph core is contained in M Omega, the closure of \(D_i|_{M\Omega}\) is exactly \(D_i\).
Therefore the natural-domain operators in (D2) are the original canonical closed duals, and the result supplies the affiliated SOME/EVERY, bounded finite-rank, full-natural-domain and coordinatewise-rank conclusions in the finite-Fisher setting.

This verifies recovery of the dual/conjugate criteria by an acyclic assembly.
It does not select replacement proofs in those older Claims, assert boundedness of the canonical duals on H, or establish scalar division closure inside M.

## Mathematical operation and review boundary

The user-requested operation registers the exact maximal-Delta criterion, its prescribed-fraction obstruction, and the dual/conjugate specialization in one responsible Claim.
The new statement has materially different starting hypotheses and quantifiers from C_F0024; that older Claim and all fixed proofs/reviews remain unchanged.
No mathematical novelty or historical-priority assertion is made.

The complete proof is offered for fresh independent review, including all analytic interfaces in Part C.
Earlier discussion checks and the exploratory draft are provenance only.
There is no claim of formal verification, external human peer review, publication, or a new Task completion.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-09T16:42 |
| status | open |
| reason | User-requested registration of the assembled maximal-Delta criterion, sharpness example, and dual/conjugate specialization; fresh independent review pending. |

Recorded authoring stage: proof draft.
Recorded review label: under review.
Recorded role label: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A, B and C, including exact hypotheses, SOME/EVERY distinction and canonical closed-domain scope. |
| argument | [Argument P1](#argument) | Complete Sections 1--5, including counterexample and noncircular dual/conjugate specialization. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002_v1.md#msy23-u002) | Maximal Delta and finite-rank-cycle characterization for bounded tuples. |
| dependency | [MSY23-U004](../audits/literature/MSY23/Yin_U004_v1.md#msy23-u004) | Affiliated algebra and matrix foundations; maximal-Delta free-field embedding. |
| dependency | [MSY23-U005](../audits/literature/MSY23/Yin_U005_v1.md#msy23-u005) | Free atomless selfadjoint base pair has maximal Delta in the sharpness example. |
| dependency | [Tensor equalizer](Yin_C_F0035_v1.md#yin_c_f0035-p1) | Part A reverse implication over the same-unit division subring F. |
| dependency | [Fraction calculus](Yin_C_F0034_v1.md#yin_c_f0034-p1) | Part C forward inclusion, defect extensions, fraction and rank independence with E=V_i=M Omega. |
| dependency | [Fundamental identity](Yin_C_F0033_v1.md#yin_c_f0033-p1) | Part C actual bounded defects satisfy the finite-rank certificate equation. |
| dependency | [Finite-Fisher analytic construction](Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input) | Only Sections 2--3 construction, estimates, both all-M domains and generator identities; no rationality conclusion. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-09T16:51 |
| status | proved |
| authority | User requested Claim registration, independent audit, and confirmation of the dual/conjugate cases. |
| reason | Two separately organized reviewers accepted the complete fixed statement and argument with no required mathematical repair. Adopt Parts A--C and the acyclic dual/conjugate assembly at the recorded external-input boundaries. |

Recorded review label: independently reviewed.
Recorded role label: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A, B and C, including exact hypotheses, SOME/EVERY distinction and canonical closed-domain scope. |
| argument | [Argument P1](#argument) | Complete Sections 1--5, including counterexample and noncircular dual/conjugate specialization. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002_v1.md#msy23-u002) | Maximal Delta and finite-rank-cycle characterization for bounded tuples. |
| dependency | [MSY23-U004](../audits/literature/MSY23/Yin_U004_v1.md#msy23-u004) | Affiliated algebra and matrix foundations; maximal-Delta free-field embedding. |
| dependency | [MSY23-U005](../audits/literature/MSY23/Yin_U005_v1.md#msy23-u005) | Free atomless selfadjoint base pair has maximal Delta in the sharpness example. |
| dependency | [Tensor equalizer](Yin_C_F0035_v1.md#yin_c_f0035-p1) | Part A reverse implication over the same-unit division subring F. |
| dependency | [Fraction calculus](Yin_C_F0034_v1.md#yin_c_f0034-p1) | Part C forward inclusion, defect extensions, fraction and rank independence with E=V_i=M Omega. |
| dependency | [Fundamental identity](Yin_C_F0033_v1.md#yin_c_f0033-p1) | Part C actual bounded defects satisfy the finite-rank certificate equation. |
| dependency | [Finite-Fisher analytic construction](Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input) | Only Sections 2--3 construction, estimates, both all-M domains and generator identities; no rationality conclusion. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0040_v1.md#conclusion) | Complete statement Parts A--C and Argument P1 Sections 1--5, exact dependency and source limits. |
| review | [Independent interface and whole-proof review](../audits/reviews/Yin_R_F0041_v1.md#conclusion) | Complete statement and argument, with separate reconstruction of sharpness, dual/conjugate recovery, every-fraction ranks and full natural domains. |

### Decision theorem-role-2026-10-10

| Field | Value |
| --- | --- |
| date | 2026-10-09T17:44 |
| status | proved |
| authority | Explicit user instruction on 2026-10-10 to designate C_F0068 as Theorem. |
| reason | The Claim role changes from lemma to theorem. The Parts A--C statement, Argument P1, dependencies and reviews remain those selected by the preceding decision. |

Recorded role label: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A, B and C, including exact hypotheses, SOME/EVERY distinction and canonical closed-domain scope. |
| argument | [Argument P1](#argument) | Complete Sections 1--5, including counterexample and noncircular dual/conjugate specialization. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002_v1.md#msy23-u002) | Maximal Delta and finite-rank-cycle characterization for bounded tuples. |
| dependency | [MSY23-U004](../audits/literature/MSY23/Yin_U004_v1.md#msy23-u004) | Affiliated algebra and matrix foundations; maximal-Delta free-field embedding. |
| dependency | [MSY23-U005](../audits/literature/MSY23/Yin_U005_v1.md#msy23-u005) | Free atomless selfadjoint base pair has maximal Delta in the sharpness example. |
| dependency | [Tensor equalizer](Yin_C_F0035_v1.md#yin_c_f0035-p1) | Part A reverse implication over the same-unit division subring F. |
| dependency | [Fraction calculus](Yin_C_F0034_v1.md#yin_c_f0034-p1) | Part C forward inclusion, defect extensions, fraction and rank independence with E=V_i=M Omega. |
| dependency | [Fundamental identity](Yin_C_F0033_v1.md#yin_c_f0033-p1) | Part C actual bounded defects satisfy the finite-rank certificate equation. |
| dependency | [Finite-Fisher analytic construction](Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input) | Only Sections 2--3 construction, estimates, both all-M domains and generator identities; no rationality conclusion. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0040_v1.md#conclusion) | Complete statement Parts A--C and Argument P1 Sections 1--5, exact dependency and source limits. |
| review | [Independent interface and whole-proof review](../audits/reviews/Yin_R_F0041_v1.md#conclusion) | Complete statement and argument, with separate reconstruction of sharpness, dual/conjugate recovery, every-fraction ranks and full natural domains. |

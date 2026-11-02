---
author: Yin
---
# Kernel tensor coefficients controlled by their actual vacua

Human author: Yin.
Root developed the finite kernel-tensor energy identity.
The acsy_to_full_domain agent checked its order, supplied the full nonunitary error and limiting domains, developed the simultaneous spectral approximation, and constructed the Sylvester-coordinate corollary.
Both are mathematical developers; independent fixed-version review was pending at the original candidate checkpoint.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let Z be bounded selfadjoint generators of a finite von Neumann algebra (M,tau) with faithful normal probability trace and joint L2 conjugates.
Put H=L2(M,tau), Omega=1, P=P_Omega and A=C<Z>.
Fix one free difference quotient delta=partial_i, its actual selfadjoint vacuum xi, and the specified closure E=overline{(id tensor tau)delta}.
Inner products are linear in their second variable.
Let B be a unital star subalgebra of A such that delta(B)=0.

**Finite coefficients.**
For beta=sum_alpha a_alpha tensor b_alpha in B tensor B, define
\[
 I_\beta(u\otimes w)=\sum_\alpha u a_\alpha\otimes b_\alpha w,
 \quad
 T_\beta p=(\mathrm{id}\otimes\tau)I_\beta\delta p,
 \quad
 v_\beta=\sum_\alpha a_\alpha^*\xi b_\alpha^* .
 \tag{S1}
\]
Then I_beta delta has actual vacuum v_beta, and
\[
 \|T_\beta p\|_2\le4\|v_\beta\|_2\|p\|,\qquad
 T_\beta^*p=pv_\beta-T_{\beta^\#}p,\qquad
 \|T_\beta^*p\|_2\le5\|v_\beta\|_2\|p\|,
 \tag{S2}
\]
for p in A, where beta#=sum b_alpha* tensor a_alpha*.
The adjoint statement is actual membership of the polynomial core in the Hilbert adjoint domain.

**Measurable coefficients in one kernel algebra.**
Suppose B=C[h] for a bounded selfadjoint h in A.
Let mu be its law, and let nu_xi be the joint spectral vector measure of the commuting left and right actions L_h,R_h on H at xi.
For a measurable beta on sigma(h)^2 assume
\[
 \beta\in L^2(\mu\otimes\mu+\nu_\xi).
 \tag{S3}
\]
Regard beta as a coarse Hilbert tensor in L2(W*(h)) bar tensor L2(W*(h)).
For delta p=sum u_j tensor w_j define delta_beta p=sum u_j dot beta dot w_j.
This is a represented derivation on A, with actual vacuum
\[
 v=\overline{\beta}(L_h,R_h)\xi.
\]
Its core contraction is closable, and its closure K has
\[
 M\Omega\subseteq\operatorname{Dom}K\cap\operatorname{Dom}K^*,
 \quad
 \|Ka\|_2\le4\|v\|_2\|a\|,
 \quad
 \|K^*a\|_2\le5\|v\|_2\|a\|,\qquad a\in M.
 \tag{S4}
\]
The multiplier value defining v is an actual joint-spectral-domain value.
No freeness hypothesis is used in these two parts.

**Sylvester-coordinate corollary.**
Let S_0,S be free standard semicirculars, h=2+S_0, and 0<r<1.
Then X=(h,hS+i rSh) generates M=W*(S_0,S) and is nonnormal.
It satisfies all three conditions:

- A(X): represented starred coarse derivations with prescribed coordinate values and actual vacuum adjoints;
- S(X): generator-first duals [X_j,D_i]=delta_ij P on M Omega with all bounded vectors in both actual domains;
- F(X): bare linear duals on all M Omega with those commutators.

In contrast (h,hS) satisfies none of A, S or F.
The invertible real-linear transformation z -> z+i r z* therefore does not preserve any of these three conditions for general nonnormal tuples.
The corollary is not a separation between A and F.

## Argument

The reference core adjoint formula, real/coassociative free difference quotient, specified closures and all-M reference domains are the exact interfaces in [Dab10-U002, Sections 1-3](../audits/literature/Dab10/Yin_U002.md#dab10-u002).
The [analytic-unitary passage of C_F0136, Section 3](Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) is reused at its original real-coassociative reference scope.
The finite coefficient identity and its error term are proved below; they are not attributed to the printed Dab10 statement.

### 1. Finite kernel coefficients and their energy identity


Let delta=partial_i be one real free difference quotient of a bounded selfadjoint finite-Fisher generating tuple.
Set E=overline{(id tensor tau)delta} and xi=delta*(1 tensor 1).
Let B be a unital star subalgebra of the polynomial algebra with delta(B)=0.
For a finite tensor beta=sum_alpha a_alpha tensor b_alpha in B tensor B put

\[
 \delta_\beta=I_\beta\delta,\qquad
 T_\beta(p)=\sum_\alpha E(p b_\alpha)a_\alpha,\qquad
 v_\beta=\sum_\alpha a_\alpha^*\xi b_\alpha^* .
 \tag{31}
\]

The equality T_beta=(id tensor tau)delta_beta follows because delta b_alpha=0.
The actual core adjoint at 1 is v_beta, from E*a_alpha*=a_alpha* xi.

The uniform estimate proved below is

\[
 \|T_\beta p\|_2\le4\|v_\beta\|_2\|p\|.
 \tag{32}
\]

For p in the core, write delta p=sum u tensor v.
Expanding the squared norm and applying the actual core adjoint to E(p b_gamma)a_gamma a_alpha* gives N=A-B, where

\[
 \begin{aligned}
 N&=\sum_{\alpha,\gamma}
 \tau(E(pb_\alpha)^*E(pb_\gamma)a_\gamma a_\alpha^*),\\
 A&=\sum_{\alpha,\gamma}
 \tau(b_\alpha^*p^*E(pb_\gamma)a_\gamma a_\alpha^*\xi),\\
 B&=\sum_{\alpha,\gamma,u\otimes v}
 \tau(b_\alpha^*p^*u)\,
 \tau(v b_\gamma\xi a_\gamma a_\alpha^*).
 \end{aligned}
 \tag{33}
\]

For the second application of E, coassociativity and the kernel property give E(E(p b_gamma)c)=sum u tau(v b_gamma xi c), where c=a_gamma a_alpha*.
This uses tau(Ew c)=tau(w xi c), valid for every c in B, without selfadjointness of c.

Reality and the product rule imply

\[
 \sum_{u\otimes v}\tau(b_\alpha^*p^*u)v
 =
 (\tau\otimes\mathrm{id})
       (b_\alpha^*\cdot\delta(p^*p))
 -E(pb_\alpha)^*p.
 \tag{34}
\]

Therefore B=-C+Q, with

\[
 C=\sum_{\alpha,\gamma}
 \tau(E(pb_\alpha)^*p b_\gamma\xi a_\gamma a_\alpha^*)
 =\langle T_\beta p,p v_\beta^*\rangle,
 \tag{35}
\]

and the precise nonunitary error is
\[
 Q=\sum_{\alpha,\gamma}\tau\left(
       (\tau\otimes\mathrm{id})
          (b_\alpha^*\cdot\delta(p^*p))
       b_\gamma\xi a_\gamma a_\alpha^*\right).
\]
All factors paired with the Hilbert slice are in L2 because xi is in L2 and the other coefficients are bounded.
Swapping alpha,gamma and conjugating shows A=conjugate(C).
Hence

\[
 \|T_\beta p\|_2^2
 =2\operatorname{Re}\langle T_\beta p,p v_\beta^*\rangle-Q.
 \tag{36}
\]

For analytic-core unitaries u, approximate by the same binomial polynomials as C_F0136.
The derivative delta(p_n* p_n) tends to zero in H bar tensor H.
The Q terms tend to zero: each applies the bounded slice (tau tensor id)(b_alpha* dot -) and then pairs its H value with a fixed L2 vector formed from bounded coefficients and xi.
Moreover T_beta p_n tends in H, since each delta(p_n b_alpha) converges.
Thus

\[
 \|T_\beta u\|_2^2
 =2\operatorname{Re}\langle T_\beta u,u v_\beta^*\rangle
 \le2\|T_\beta u\|_2\|v_\beta\|_2.
\]

The usual selfadjoint/unitary decomposition and real/imaginary decomposition prove (32).
No positivity, selfadjointness, commutativity or freeness of the coefficients a_alpha,b_alpha was used.

Let beta^#=sum b_alpha* tensor a_alpha*.
Then v_(beta#)=v_beta*, so the same bound applies to T_(beta#).
On the polynomial core, actual adjoints obey

\[
 T_\beta^*q=qv_\beta-T_{\beta^\#}q,
 \qquad
 \|T_\beta^*q\|_2\le5\|v_\beta\|_2\|q\|.
 \tag{37}
\]

For each finite beta this follows directly from T_beta*=sum rho(b_alpha*)E*rho(a_alpha*) on bounded core inputs and the source adjoint formula.
These are core identities and domain inclusions, not an assertion about complete product-adjoint domains.

### 2. Abelian spectral coefficients and both actual domains

Now take B=C[h] for a bounded selfadjoint h in the kernel, with law mu, and put N=W*(h).
The commuting left and right actions of h on H have joint spectral resolution; let nu_xi be their finite positive vector measure at xi.
Thus for finite separated beta(s,t)=sum a_alpha(s)b_alpha(t),

\[
 v_\beta=\overline{\beta}(L_h,R_h)\xi,\qquad
 \|v_\beta\|_2^2=\int|\beta(s,t)|^2\,d\nu_\xi(s,t).
 \tag{38}
\]

The corresponding coarse vector has norm ||beta||_(L2(mu tensor mu)).
Since xi is selfadjoint and the tracial involution interchanges L_h and R_h, nu_xi is invariant under the flip (s,t)->(t,s).
The coarse measure has the same symmetry.

Suppose a measurable coefficient beta belongs to

\[
 L^2(\mu\otimes\mu+\nu_\xi).
 \tag{39}
\]

Polynomials in s,t are dense in this finite-measure L2 space on the compact spectral square.
Choose beta_n in C[h] tensor C[h] converging in both measures.
For each fixed polynomial p, define delta_beta p by replacing each finite term u tensor v of delta p with u dot beta dot v.
Boundedness of those outer factors shows delta_(beta_n)p -> delta_beta p in the Hilbert tensor norm.
The actual vacuum vectors v_(beta_n) converge to the genuine multiplier value v=overline(beta)(L_h,R_h)xi.

The flip symmetry also gives beta_n# -> beta# in both measures, and v_(beta_n#) -> v*.
Thus both contraction limits are defined.
From (32),

\[
 \|T_\beta p\|_2,\ \|T_{\beta^\#}p\|_2
 \le4\|v\|_2\|p\|.
 \tag{40}
\]

For fixed p,q in the core, pass to the limit in the actual adjoint pairings (37).
This gives q in Dom T_beta*, with T_beta*q=qv-T_(beta#)q, hence the uniform 5||v||||q|| bound.
The core operator is closable.
To verify the full-domain assertion, take uniformly operator-norm bounded polynomial approximants p_n -> a in H for a in M.
The bound (40) yields weakly convergent subsequences of T_beta p_n; weak-closedness of the graph of its Hilbert closure K puts a in Dom K.
Apply the same argument to the closed operator T_beta* on the polynomial core using its 5||v|| bound.
This puts a in Dom K*=Dom T_beta*.
Allowing arbitrarily small excess in the approximants' norm gives
\[
 \|Ka\|_2\le4\|v\|_2\|a\|,\qquad
 \|K^*a\|_2\le5\|v\|_2\|a\|,\qquad a\in M.
\]
No equality of complete product domains is claimed.

Likewise the vacuum pairing limit proves delta_beta*(1 tensor 1)=v, an actual Hilbert adjoint.
Thus (39) is a complete sufficient spectral condition for both domains of this kernel-coefficient derivation.
The argument does not claim that an arbitrary supplied target derivation automatically yields a beta satisfying (39); that inverse-identification step depends on the coordinate change.

### 3. A nonnormal Sylvester-coordinate corollary

Let S_0,S be free standard semicircular elements, let h=2+S_0, and set

\[
 Y=hS+\mathrm i r S h,\qquad 0<r<1,\qquad X=(h,Y).
 \tag{41}
\]

The reference pair (h,S) has joint conjugates (S_0,S), and h is positive regular.
In this section B_h denotes the specified closure of (id tensor tau)partial_h, and xi_h=S_0.
The law mu of h is supported on [0,4], with density proportional to sqrt(t(4-t)).
In particular h^{-1} is not L2, because its squared inverse has density comparable to t^(-3/2) near zero.

Let

\[
 F(s,t)=s+\mathrm i r t,\qquad
 \beta(s,t)=\frac1{s+\mathrm i r t}.
 \tag{42}
\]

The only zero of F on the nonnegative spectral square is (0,0), which has mu tensor mu measure zero.
The coefficient beta belongs to L2(mu tensor mu): near the origin its squared integrand is bounded by a constant times sqrt(st)/(s^2+t^2), whose two-dimensional polar integral is finite; away from the origin the denominator is bounded away from zero locally.

For the reference xi_S=S, freeness gives nu_xi=mu tensor mu.
Indeed ||a(h)S b(h)||2^2=||a(h)||2^2||b(h)||2^2 and the polarized version holds for sums.
Therefore beta satisfies the simultaneous graph condition (39).

The core derivation delta_beta has delta_beta h=0 and delta_beta Y=F beta=1 tensor 1.
Its closed contraction K has both M domains and [K,Y]=P on M, [K,h]=0.
The passage of these commutators from the core to M uses the uniform estimate (40).

The tuple X generates M.
Since

\[
 hS=\frac{Y-\mathrm i rY^*}{1-r^2},
\]

its star algebra contains hS; bounded spectral inverses of h recover S strongly.
Moreover

\[
 [B_h,Y]=PS+\mathrm i rSP.
\]

Thus the operator-first correction

\[
 E_h=B_h-K\rho(S)-\mathrm i r\rho(S)K
 \tag{43}
\]

has the required h commutator and zero Y commutator on M.
All its actual adjoint domains contain M because each bounded coefficient preserves M and K,B_h have both actual M domains.
Together with E_Y=K, negating these operator-first witnesses gives S(X).

The actual ACSY derivations are also explicit.
On A_0 put
\[
 \delta_Y=\delta_\beta,\qquad
 \delta_h=\partial_h-I_C\delta_\beta,\qquad
 C=1\otimes S+\mathrm i r S\otimes1.
\]
Their values on h,Y are the prescribed coordinate tensors.
Let v be the actual vacuum of delta_beta, already proved in Section 2.
The right contraction of delta_h on the core is
\[
 Q_hp=E_hp+p\,K(S).
\]
Indeed the coefficient 1 tensor S contributes K(pS)-pK(S), and the coefficient i r S tensor 1 contributes i r(Kp)S.
Right multiplication by the H vector K(S), restricted to M, has actual adjoint q -> q(K(S))* on M.
Therefore the actual h-vacuum is the H vector
\[
 \xi_h-vS+\mathrm i r K^*S+(K(S))^*.
\]
This proves the full actual vacuum condition after restriction to A_X, and hence A(X), independently of any general S-to-A theorem.

The tuple is nonnormal for 0<r<1.
With Z=hS, [Y,Y*]=(1-r^2)[Z,Z*].
The polynomial hS^2h-Sh^2S is nonzero for free semicircular S_0,S: its highest-degree monomials S_0 S^2 S_0 and S S_0^2 S are distinct.
Algebraic freeness of the selfadjoint semicircular pair, part of the standard finite-Fisher interface used here, therefore gives [Z,Z*] nonzero.

In contrast A(h,hS) and F(h,hS) both fail: the necessary condition h^{-1} in L2 in C_F0134 applies to this same free reference pair.
The invertible real-linear transformation Z -> Z+i r Z* sends hS to Y, but this candidate would show that A,F,S for nonnormal tuples need not be invariant under that transformation.
This is not a counterexample to A-to-F.
It establishes failure of invariance of the three input conditions under this invertible real-linear change for nonnormal tuples, and shows that the coefficient construction extends the preceding one-sided transport class.


## Scope and continuation

The simultaneous-measure hypothesis is essential to this stated construction: it provides both coarse tensor convergence and actual vacuum convergence.
No extension from arbitrary square-integrable coefficients to their adjoint domains is asserted without that second graph norm.
The result does not show that every ACSY derivation is a kernel-coefficient change of a real free difference quotient.

The argument creates full domains for the specified closed core operators; it does not identify arbitrary supplied bare maps with those operators.
There is no assertion of a universal A-to-F implication, and the corollary has A and F both true.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:51 |
| status | open |
| reason | Complete finite-kernel energy theorem, measurable abelian simultaneous-graph extension and a nonnormal Sylvester-coordinate corollary retained for independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Kernel-coefficient theorem and corollary](#statement) | Finite coefficient bounds and actual core adjoints, simultaneous-measure extension with both domains, and the stated nonnormal coordinate example. |
| argument | [Complete argument](#argument) | Sections 1-3, including the exact nonunitary error, both graph limits, actual h-coordinate vacuum and failure of the previous coordinate condition. |
| dependency | [Selfadjoint contraction interfaces](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Real coassociative represented difference quotients, actual core adjoints and reference closures; standard selfadjoint finite-Fisher algebraic freeness for the semicircular example. |
| dependency | [Analytic-unitary approximation](Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) | The actual first-derivative binomial-series limit and unitary decomposition, adapted with the explicit finite coefficient error proved here. |
| dependency | [One-sided free transport necessity](Yin_C_F0134_v1.md#statement) | Failure of A and F for (h,hS) when h inverse is not L2 in the corollary. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:00 |
| status | proved |
| reason | Complete independent review verified the finite energy estimate, both spectral graph norms and actual domains, and the complete Sylvester-coordinate example. The sole requested subscript correction in (31) has been applied without changing its map or proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Kernel-coefficient theorem and corollary](#statement) | Finite coefficient bounds and actual core adjoints, simultaneous-measure extension with both domains, and the stated nonnormal coordinate example. |
| argument | [Complete argument](#argument) | Sections 1-3, including the exact nonunitary error, both graph limits, actual h-coordinate vacuum and failure of the previous coordinate condition. |
| dependency | [Selfadjoint contraction interfaces](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Real coassociative represented difference quotients, actual core adjoints and reference closures; standard selfadjoint finite-Fisher algebraic freeness for the semicircular example. |
| dependency | [Analytic-unitary approximation](Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) | The actual first-derivative binomial-series limit and unitary decomposition, adapted with the explicit finite coefficient error proved here. |
| dependency | [One-sided free transport necessity](Yin_C_F0134_v1.md#statement) | Failure of A and F for (h,hS) when h inverse is not L2 in the corollary. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0146_v1.md#conclusion) | Complete statement, all three proof sections, all direct inputs and exact noninvariance quantifiers, including the permitted notation-only correction. |


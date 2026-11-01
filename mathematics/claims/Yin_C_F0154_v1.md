---
author: Yin
---
# An inverse-trace criterion for affine matrix pencils under actual ACSY derivations

Human author: Yin.
Root proposed the strictly positive scalar compression and the normalization extending the row-resolvent argument.
The general ACSY-to-full-domain branch checked the matrix indices, actual-core Neumann approximation, normalized weak limits, and actual polar-range conclusion, and fixed this complete proof.
Both are developers, not independent reviewers.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, H=L2(M), and X=(X_1,...,X_d) a bounded generating tuple.
Let cal A=C<X,X*>.
Suppose that for i=1,...,d there are complex-linear represented outer derivations delta_i:cal A->H tensor_2 H satisfying
\[
 \delta_i X_j=\delta_{ij}1\otimes1,\qquad
 1\otimes1\in\operatorname{Dom}\delta_i^*.
\]
Write xi_i=delta_i*(1 tensor 1).
Inner products are linear in their second variable.
No reality or prescribed starred-generator value is assumed.

Let A_0,...,A_d be scalar n by m matrices and define
\[
 L=A_0+\sum_{i=1}^d A_iX_i\in M_{n,m}(M),\quad Q=LL^*,
 \quad p=\ker L,\quad C=(\mathrm{id}\otimes\tau)(p),\quad
 B=\sum_{i=1}^d A_i C A_i^* .
 \tag{1}
\]
Here A_i X_i denotes the matrix with entries (A_i)_(r,k) X_i, p is the matrix projection onto the kernel of L:H^m->H^n, and the partial trace defining C is entrywise.
Assume Q is regular on H^n and the scalar matrix B is strictly positive definite.

Then
\[
 (\operatorname{Tr}_n\otimes\tau)(Q^{-1})<\infty.
\]
Tr_n denotes the unnormalized scalar matrix trace.
Every bounded column a in M_(n,1)(M) belongs to the actual range L H^m.
If L=Q^(1/2)W is its rectangular polar decomposition, an actual right inverse on such columns is
\[
 z=W^*Q^{-1/2}a\in H^m,\qquad Lz=a,\qquad
 \|z\|_{H^m}^2\le
     \|a\|_{M_{n,1}(M)}^2
       (\operatorname{Tr}_n\otimes\tau)(Q^{-1}).
\]
No trace-inverse conclusion is asserted when B is singular.
The result gives a sufficient matrix range condition, not the construction of coherent coordinate duals or the elimination of all finite polynomial-module obstructions.

## Reuse and source scope

The exact [C_F0148 resolvent mechanism](Yin_C_F0148_v1.md#argument), Sections 1--2, supplies the starting actual-core and weak-tensor method.
The present proof gives all changed matrix formulas and normalization estimates explicitly.
Only the coordinate-resolvent mechanism is transferred; C_F0148's use of maximal Delta and its special two-coordinate example are not hypotheses or inputs here.
In particular Q regularity is assumed, not inferred through an unverified rectangular-rank theorem.

A bounded reuse search of fixed row obstructions, actual-vacuum records, polynomial-matrix entries, and the source registry found no fixed version of the present positive-compression matrix criterion.
External primary-source queries by conjugate variables, polynomial-matrix kernels, inverse integrability and derivation resolvents located neighboring formulations but supplied no theorem used below.
No new external source result is adopted.
The proof uses ordinary finite-matrix trace order, spectral truncation, Hilbert weak convergence and rectangular polar decomposition at their stated scope.

## Argument

For epsilon>0 set R_epsilon=(Q+epsilon I_n)^-1,
\[
 U_\varepsilon=(\operatorname{Tr}_n\otimes\tau)(R_\varepsilon),
 \quad V_\varepsilon=R_\varepsilon L,\quad
 C_\varepsilon=I_m-(\mathrm{id}\otimes\tau)
                           (L^*R_\varepsilon L),
 \quad B_\varepsilon=\sum_iA_i C_\varepsilon A_i^*.
 \tag{2}
\]
The bounded positive contractions L*R_epsilon L increase strongly to I_m-p.
Thus C_epsilon decreases in scalar matrix order to C, and B_epsilon>=B>=c I_n for some c>0.
Put
\[
 T_\varepsilon=
   \operatorname{Tr}_n\bigl((\mathrm{id}\otimes\tau)
                               (R_\varepsilon)B_\varepsilon\bigr)
       \ge c U_\varepsilon>0,\qquad
 f_{i,\varepsilon}=\operatorname{Tr}_n
                       (R_\varepsilon L A_i^*)\in M.
 \tag{3}
\]

All derivative formulas for these test elements are justified on the original core.
For fixed epsilon choose a scalar b>||Q||+epsilon and expand R_epsilon=b^-1 sum_(k>=0)(I_n-(Q+epsilon I_n)/b)^k.
Each entry of every partial sum is in the original star core.
In the matrix Hilbert bimodule M_n(H tensor_2 H), the derivative norm of the kth power is at most k theta^(k-1)||delta_i Q||2/b, with theta<1.
Thus the differentiated series converges in Hilbert norm.
Multiplying by L A_i* and taking the finite diagonal sum preserves this graph convergence.
Pairing each scalar test against the actual xi_i therefore passes to the limit.
This argument does not assume closability of delta_i or an inverse in its initial algebraic domain.

Put K_(i,b,l)=delta_i(L_(b,l)*), a fixed Hilbert tensor.
Entrywise multiplication of the inverse rule gives
\[
 \langle\xi_i,f_{i,\varepsilon}\rangle
 =\operatorname{Tr}_n\bigl((\mathrm{id}\otimes\tau)
                  (R_\varepsilon) A_i C_\varepsilon A_i^*\bigr)
 -\sum_{r,b=1}^n\sum_{k,l=1}^m
       \overline{(A_i)_{rk}}\,
       \langle K_{i,b,l}^*,\,
                  (V_\varepsilon)_{rl}\otimes
                  (V_\varepsilon)_{bk}\rangle .
 \tag{4}
\]
Here K* is componentwise adjoint without a flip.
To check the indices, write f_i=sum_(r,s,k) R_(rs)L_(sk) conjugate(A_i[r,k]).
The constant derivative delta_i L=A_i produces Tr(tau(R)A_i A_i*).
The constant part of delta_i Q has entries sum_l (A_i)_(al) tensor L_(bl)*, whose contribution is minus Tr(tau(R) A_i D_epsilon A_i*) with D_epsilon=(id tensor tau)(L*R L).
Their sum is the first term in (4).
The remaining part of delta_i Q has entries sum_l L_(al) dot K_(i,b,l).
Summing the adjacent factors of R and L gives precisely V_(rl) dot K_(i,b,l) dot V_(bk).
Traciality identifies its double trace with the pairing in (4); this identity extends from elementary tensors by Hilbert approximation.

Assume for contradiction that (Tr_n tensor tau)(Q^-1)=infinity.
Then U_epsilon tends to infinity by monotone spectral convergence.
Traciality gives
\[
 \sum_{r,l}\|(V_\varepsilon)_{rl}\|_2^2
   =(\operatorname{Tr}_n\otimes\tau)
          (Q R_\varepsilon^2)\le U_\varepsilon.
 \tag{5}
\]
Each normalized column V_epsilon e_l/sqrt(U_epsilon) is bounded in H^n and converges weakly to zero.
Indeed, for e_t=1_(0,t)(Q), its high-spectral part is at most ||L e_l||2/(t sqrt(U_epsilon)), which tends to zero for fixed t.
The low-spectral pairing against any fixed z is bounded by ||e_t z||2, which tends to zero as t decreases to zero because Q is regular.
Taking the two limits in that order proves the assertion.
Thus each normalized matrix entry is weakly null, and so are the tensors of any two entries, uniformly bounded in H tensor_2 H.

Summing (4) over i and dividing by T_epsilon gives 1 minus an error tending to zero: in each error pairing factor out U_epsilon/T_epsilon<=1/c and use those normalized tensor weak limits.
On the other hand,
\[
 \|f_{i,\varepsilon}\|_2
 \le\|A_i\|_{\mathrm{HS}}
          \left(\sum_{r,l}\|(V_\varepsilon)_{rl}\|_2^2\right)^{1/2}
 \le\|A_i\|_{\mathrm{HS}}\sqrt{U_\varepsilon},
 \tag{6}
\]
so every actual-vacuum pairing divided by T_epsilon tends to zero.
This contradiction proves inverse-trace integrability.

Finally write L=Q^(1/2)W in its rectangular polar decomposition.
Regularity gives W W*=I_n.
For a bounded column a in M^n, Q^-1/2 a is an actual Hilbert column and
\[
 \|Q^{-1/2}a\|_{H^n}^2
 \le\|a\|_{M_{n,1}(M)}^2
                   (\operatorname{Tr}_n\otimes\tau)(Q^{-1}).
 \tag{7}
\]
This follows by bounded spectral truncation and the positive trace inequality with aa*.
Therefore z=W*Q^-1/2 a lies in H^m, obeys the same bound and satisfies Lz=a.
This uses Q^-1/2, not an unjustified composition L*Q^-1 on bounded columns.

For n=1 and L=[X_1,...,X_d], the compression B is the scalar sum_i tau(p_ii)=d-1 when Q is regular, recovering the full-system row mechanism for d>=2.
For a general matrix pencil, B can be singular.
In that case the normalization in (3) need not control U_epsilon, and the unknown-star tensor terms in (4) still have two unweighted V legs.
Replacing the hypothesis by a weaker weighted inverse criterion requires a new argument.
This proof constructs no coherent full-domain dual and does not remove all finite polynomial-module obstructions.


## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:51 |
| status | open |
| reason | Complete developer-checked matrix resolvent proof under explicit regularity and strictly positive scalar-compression hypotheses; actual bounded-column range follows by polar decomposition. Independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Inverse trace and actual bounded-column row range for affine pencils with Q regular and B strictly positive, with the singular-B and coherent-dual limitations. |
| argument | [Argument](#argument) | Original-core matrix Neumann tests, exact constant and arbitrary starred terms, normalized weak tensor contradiction, and actual polar right inverse. |
| dependency | [Actual coordinate resolvent mechanism](Yin_C_F0148_v1.md#argument) | Sections 1--2: actual original-core resolvent graph approximation and weak normalized-tensor method. All matrix indices and positive-compression estimates are checked here; no maximal-Delta or special-example conclusion is transferred. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:04 |
| status | proved |
| reason | Adopt the complete affine matrix inverse-trace criterion after R_F0162 independently checked every matrix index, original-core test, normalized weak limit, polar-domain conclusion and its exact direct input. The strict scalar-compression positivity and regularity assumptions remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Inverse trace and actual bounded-column row range for affine pencils with Q regular and B strictly positive, with the singular-B and coherent-dual limitations. |
| argument | [Argument](#argument) | Original-core matrix Neumann tests, exact constant and arbitrary starred terms, normalized weak tensor contradiction, and actual polar right inverse. |
| dependency | [Actual coordinate resolvent mechanism](Yin_C_F0148_v1.md#argument) | Sections 1--2: actual original-core resolvent graph approximation and weak normalized-tensor method. All matrix indices and positive-compression estimates are checked here; no maximal-Delta or special-example conclusion is transferred. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0162_v1.md#conclusion) | Whole statement and argument, matrix normalization and tensor order, actual inverse-square-root range, all stated limits and exact C_F0148 Sections 1--2 dependency. |


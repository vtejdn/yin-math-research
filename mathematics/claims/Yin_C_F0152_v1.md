---
author: Yin
---
# A full-domain dual for a semicircular product with a singular positive factor

Human author: Yin.
The general ACSY-to-full-domain branch developed the complete-block cancellation, the centered partial-block estimate, and the actual closure/compression proof.
Root supplied the original hidden-factor coefficient route, identified the unique alpha suffix cut, and checked the final cancellation and column estimates.
These are development contributions, not independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let s_0,S be freely independent standard variance-one semicircular elements in a finite tracial von Neumann algebra with faithful normal probability trace.
Set M=W*(s_0,S), H=L2(M), h=2+s_0, X=hS and N=W*(X).
Inner products are linear in the second variable, and tensor coefficient actions are outer.

Use the represented reference derivation and actual vacuum of [C_F0150](Yin_C_F0150_v1.md#statement):
\[
 \delta=I_\alpha\partial_h+I_\beta\partial_S,\qquad
 \alpha(u,v)=\frac{v}{u^2+v^2},\quad
 \beta(u,v)=\frac{u}{u^2+v^2},
 \tag{1}
\]
on A_0=C<h,S>, where u is the first h variable and v the second S variable.
Here I_eta(a tensor b)=a dot eta dot b, delta X=1 tensor 1, and ||alpha||2^2+||beta||2^2<=1.
Define the original core operator E=(id tensor tau)delta:A_0->H.

Then E is closable, its actual Hilbert closure has M in its domain, and
\[
 \|\overline E\,a\|_2\le
   \bigl(\sqrt2+1+2\|\beta\|_2\bigr)\|a\|,
 \qquad [\overline E,X]a=\tau(a)1
 \quad(a\in M).
 \tag{2}
\]
In particular the constant in (2) is at most sqrt(2)+3.

Let Q_N be trace-preserving conditional expectation onto L2(N), and let delta_N=(Q_N tensor Q_N)delta restricted to C<X,X*> be the intrinsic derivation from C_F0150.
Its canonical contraction E_N=(id tensor tau)delta_N=Q_N E on that target star core is closable; its actual closure has all of N in its domain and obeys the same bound and commutator.
Thus
\[
 D=-\overline{E_N}|_N:N\Omega\longrightarrow L^2(N),
 \qquad [X,D]=P_\Omega
 \quad\hbox{on all }N\Omega .
 \tag{3}
\]
This proves F(N;X) for the same single hidden-factor example for which C_F0150 proves A(N;X), despite h^-1 not belonging to L2.
No full bounded-vector domain for E* or E_N* is asserted.
The general implication A implies F for arbitrary generating tuples remains unresolved.

## Reuse and source scope

C_F0150 supplies the actual reference and intrinsic target derivations, both Hilbert coefficients, the actual vacuum, and the exact marginal facts h regular, tau(h^-1)=1 and ||h||=4.
The [Miy22-U001 Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) supplies the standard right creation/deletion normalization and orthonormal Wick words; the exact reference derivative word-cut identity is the one proved in [C_F0144](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint).
These are the direct inputs.

The finite-degree contraction mechanism in C_F0145 motivated the initial cut analysis, but its summable degree bound does not apply term by term to the coefficients below.
The proof here supplies its own cancellation and bounded-column estimates and does not invoke that theorem.
A bounded local/source search also inspected free-product projection and Hilbert-transform statements; none was selected as a missing estimate.
The actual argument is the elementary Fock decomposition given below, not an unverified endpoint multiplier theorem.

## Argument

### 1. The square-summable coefficient expansion and exact contraction

Write r_0,r_1 for the right creation isometries for s_0,S.
On H, rho(a) means right multiplication by a, so rho(h)=2I+r_0+r_0*.
In particular right coefficient multiplication in the following formulas is performed after the indicated annihilations.

Let
\[
 q(u)=\frac{\sqrt{u^2+4}-u}{2},\qquad
 0<q(u)<1\ (u>0),\qquad 1-q(u)^2=u q(u).
 \tag{4}
\]
The monic Chebyshev recurrence U_(n+1)(v)=v U_n(v)-U_(n-1)(v) gives its generating series.
Substituting z=-i q(u) gives
\[
 \frac1{u+i v}
 =\sum_{n\ge0}(-i)^n q(u)^{n+1}U_n(v).
 \tag{5}
\]
For fixed u>0 this is the usual generating series.
Orthonormality in the S leg and (4) show convergence in the coarse Hilbert space, because
\[
 \sum_{n\ge0}\|q(h)^{n+1}\|_2^2
 =\tau\!\left(\frac{q(h)}h\right)\le\tau(h^{-1})=1.
 \tag{6}
\]
Taking the real and imaginary parts in the two commuting tensor variables yields
\[
 \beta=\sum_{k\ge0}(-1)^kq(h)^{2k+1}\otimes U_{2k}(S),
 \qquad
 \alpha=\sum_{k\ge0}(-1)^kq(h)^{2k+2}\otimes U_{2k+1}(S).
 \tag{7}
\]
In particular sum over odd n of ||q(h)^n||2^2 is exactly ||beta||2^2.

The reference word-cut formula says partial_j U_w is the sum of U_prefix tensor U_suffix over occurrences of the letter j in w.
Contracting its second leg against U_n(S) retains precisely a pure-1 suffix of length n.
Therefore on each Wick polynomial,
\[
 Ep=\sum_{\substack{n\ge1\\n\ {\rm odd}}}
  \epsilon_n\left\{\rho(q^n)r_1^{*n}p+
                     \rho(q^{n+1})r_0^*r_1^{*n}p\right\},
 \qquad \epsilon_n=(-1)^{(n-1)/2}.
 \tag{8}
\]
Only finitely many terms are nonzero for each p.
Coarse convergence of (7), bounded outer multiplication for the finite derivative of p, and continuity of id tensor tau identify (8) with the original E.
It is not being asserted that the operator series in (8) converges in Hilbert operator norm.

### 2. Cancellation for complete terminal blocks

Put Q=rho(q(h)), H_h=rho(h), P_1=r_1r_1*, P_0=I-P_1, and
\[
 B=(I+Qr_0^*)P_0,\qquad C_n=P_0r_1^{*n}.
 \tag{9}
\]
The initial projection C_n*C_n selects exactly words with a terminal 1 block of length n; the empty prefix is allowed.
These projections are mutually orthogonal.
Thus C:p mapped to (C_n p) over odd n is a contraction from H into the Hilbert direct sum of copies of H.
The output of C_n lies in P_0H.

By (4),
\[
 (1-q(u))^2=\frac{u^2q(u)^2}{(1+q(u))^2}\le u
 \qquad(0<u\le4).
 \tag{10}
\]
Let A=I+Qr_0*=(I+r_0*)-(I-Q)r_0*.
The elementary operator inequality (V+W)(V+W)*<=2VV*+2WW* gives
\[
 BB^*\le AA^*\le
  2(I+r_0^*)(I+r_0)+2(I-Q)r_0^*r_0(I-Q)
  =2H_h+2(I-Q)^2\le4H_h.
 \tag{11}
\]
The orders in this calculation are essential; no commutation between r_0* and Q is used.
Consequently all finite rows with entries Q^n B, n odd, have square bounded by
\[
 \sum_{n\ {\rm odd}}Q^nBB^*Q^n
 \le4H_h\sum_{n\ {\rm odd}}Q^{2n}
 =4\rho\!\left(\frac{q}{1+q^2}\right)\le2I .
 \tag{12}
\]
The infinite row therefore extends with norm at most sqrt(2).
Composing with the cut column proves that
\[
 Kp=\sum_{n\ {\rm odd}}\epsilon_n Q^nB C_n p,
 \qquad \|K\|_{H\to H}\le\sqrt2.
 \tag{13}
\]
The series converges in H, since the input column is square summable and the row is bounded.

Since r_0* P_1=0, r_0*C_n=r_0*r_1*^n.
Thus on the polynomial core K is exactly the entire alpha contribution in (8), plus that part of the beta contribution which removes the complete terminal 1 block.
The remaining contribution is
\[
 Rp=\sum_{n\ {\rm odd}}\epsilon_n
           \bigl(P_1r_1^{*n}p\bigr)q(h)^n .
 \tag{14}
\]
For each polynomial p this remains a finite sum, and E p=K p+R p.

### 3. A bounded column for the partial-block terms

The right semicircular operator is rho(S)=r_1+r_1*.
The isometry relation r_1*r_1=I and the Chebyshev recurrence imply
\[
 r_1^{*n}=\rho(U_n(S))-r_1\rho(U_{n-1}(S))
 \qquad(n\ge1).
 \tag{15}
\]
For completeness, the identity U_n(r+r*)=sum_(j=0)^n r^(n-j)r*^j follows by induction from the same recurrence; subtracting r U_(n-1)(r+r*) leaves r*^n.

For p in A_0, set a_n=P_1r_1*^n p, with n odd.
Equation (15) gives
\[
 a_n=P_1\bigl(pU_n(S)\bigr)-r_1\bigl(pU_{n-1}(S)\bigr).
 \tag{16}
\]
Both families U_n(S) and U_(n-1)(S), indexed by odd n, are orthonormal in H.
Left multiplication by p has Hilbert operator norm ||p||; P_1 and r_1 have norm one.
It follows that the map A_p:ell2(odd n)->P_1H sending e_n to a_n satisfies
\[
 \|A_p\|\le2\|p\|.
 \tag{17}
\]
This is a column operator estimate, not a claimed square-sum bound for the vectors a_n.

Let H_h^circ=L2(W*(h)) orthogonal to 1, and set
\[
 m_n=\tau(q(h)^n),\qquad b_n=q(h)^n-m_n1.
 \tag{18}
\]
Centering decreases the squared norms, so sum over odd n of ||b_n||2^2<=||beta||2^2.
Applying A_p tensor identity to sum_n epsilon_n e_n tensor b_n gives
\[
 \left\|\sum_{n\ {\rm odd}}\epsilon_n a_n\otimes b_n
       \right\|_{P_1H\otimes_2 H_h^\circ}
 \le2\|p\|\|\beta\|_2.
 \tag{19}
\]

### 4. Orthogonal concatenation and the scalar means

Multiplication is an isometry from P_1H tensor_2 H_h^circ into H.
Indeed a Wick word in P_1H ends in 1, while an orthonormal basis of H_h^circ consists of the nonempty pure-0 words U_m(s_0), m>=1.
Their products are distinct concatenated Wick words: the terminal 0 block determines the split uniquely.
Thus multiplication on these bases is isometric and extends by density.
For polynomial first factors and bounded functions of h in the second factor this extension equals their actual product, by polynomial L2 approximation.

Hence (19) proves the centered part of (14) has norm at most 2||p||||beta||2.
For the scalar part, positivity and monotone convergence give the exact identity
\[
 \sum_{n\ {\rm odd}}m_n
 =\tau\!\left(\frac{q(h)}{1-q(h)^2}\right)
 =\tau(h^{-1})=1 .
 \tag{20}
\]
Each P_1r_1*^n is a Hilbert contraction.
Therefore sum_n epsilon_n m_n P_1r_1*^n converges in Hilbert operator norm with norm at most one.
Combining (13), (19) and (20) proves
\[
 \|Ep\|_2\le
  \bigl(\sqrt2+1+2\|\beta\|_2\bigr)\|p\|,
 \qquad p\in A_0.
 \tag{21}
\]
Every decomposition used to obtain this bound agrees on the original core with (8).
In particular no replacement of E by a convenient unrelated extension has occurred.

### 5. Closability and the actual ambient domain

C_F0150 gives v_0=delta*(1 tensor 1) as an actual Hilbert vector on the full mixed reference core.
Define delta-dagger(a)=(delta(a*))^dagger, where dagger on tensors is flip followed by componentwise adjoint.
The actual tracial integration-by-parts identity on the reference polynomial core is
\[
 E^*a=a v_0-(\mathrm{id}\otimes\tau)\delta^\dagger(a).
 \tag{22}
\]
One way to verify all domain assertions in (22) is to approximate alpha and beta by finite polynomial tensor coefficients in their separated-leg Hilbert spaces.
C_F0150 proves that both relevant reference adjoints on those spaces are isometries.
The coefficient approximants therefore converge in their actual adjoint graphs; their flipped adjoints do too, with labels reversed.
For finite polynomial coefficients (22) is the ordinary Leibniz identity obtained from the real reference derivatives.
For each fixed polynomial a, finite bounded outer multiplication makes every term converge in H, and pairing against every reference polynomial proves actual membership in Dom E*.
In particular Dom E* is dense, so E is closable.

For any a in M choose Kaplansky approximants p_lambda in A_0 converging to a in L2, with operator norms uniformly bounded by ||a||+epsilon for arbitrary epsilon>0.
Such polynomial approximants follow from Kaplansky density in C*(h,S) and norm approximation within that algebra.
Equation (21) bounds E p_lambda in H.
A weakly convergent subnet and the weakly closed graph of the Hilbert closure give
\[
 a\in\operatorname{Dom}\overline E,\qquad
 \|\overline E a\|_2\le
  \bigl(\sqrt2+1+2\|\beta\|_2\bigr)(\|a\|+\varepsilon).
\]
Uniqueness follows from the graph being that of an operator; letting epsilon tend to zero gives (2)'s bound.

On A_0, the exact normalization delta X=1 tensor 1 yields
\[
 E(Xp)=XEp+\tau(p)1.
 \tag{23}
\]
Using the same approximants, X p_lambda tends in L2 to X a and its E values tend weakly along the chosen subnet to X overline(E)a+tau(a)1.
Weak closedness of the same graph therefore extends (23) to all a in M.
This proves the ambient commutator assertion in (2).
It uses neither an h^-1 product on an unverified domain nor a full domain for E*.

### 6. Intrinsic target closure and dual

For a in N, define T a=Q_N overline(E)a.
Conditional expectation is a Hilbert contraction and commutes with bounded left multiplication by N.
Therefore (2) gives
\[
 \|T a\|_2\le
   \bigl(\sqrt2+1+2\|\beta\|_2\bigr)\|a\|,
 \qquad [T,X]a=\tau(a)1 .
 \tag{24}
\]
This already constructs an intrinsic full-N dual -T.

It also identifies the specified canonical closure.
On the target star core, conditional expectation commutes with the right contraction:
\[
 E_Np=(\mathrm{id}\otimes\tau)(Q_N\otimes Q_N)\delta p
      =Q_N Ep.
 \tag{25}
\]
The actual target vacuum from C_F0150 and its represented target derivation give dense actual adjoint domain, by the same Leibniz argument as (22), now on C<X,X*>.
Thus E_N is closable.
Equation (21) bounds it on that core.
Target Kaplansky approximation and weak graph closure put every a in N in Dom overline(E_N).
If p_lambda are such target approximants, the ambient graph argument simultaneously gives weak limits E p_lambda=overline(E)a; applying Q_N identifies
\[
 \overline{E_N}a=T a \qquad(a\in N).
 \tag{26}
\]
This proves every assertion of (3) and the stated canonical-domain refinement.

## Scope

The singular inverse h^-1 remains outside L2, as established in C_F0150.
The proof exploits the joint normalization of alpha and beta and the free-word location of their coefficients.
Their separate square-summable expansions are insufficient for the older degree-summability criterion.
The complete-block cancellation and partial-block column estimate supply the missing bound.

No full adjoint domain follows from (21); the present result establishes the required bare full-domain dual and the actual forward canonical closure.
It neither proves the general implication A implies F nor asserts an implication for arbitrary separated Hilbert coefficient kernels.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:40 |
| status | open |
| reason | Complete developer-checked cancellation and partial-block column proof gives an actual full canonical forward domain and intrinsic bare dual for the singular hidden-factor example. Independent review is pending; no full adjoint-domain conclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact ambient and intrinsic full forward domains, explicit operator-norm bound, all-bounded-vector commutator and bare target dual, without an adjoint-domain claim. |
| argument | [Argument](#argument) | Six complete steps: coefficient expansion, complete-block cancellation, partial-block column, orthogonal concatenation and means, actual ambient closure, and intrinsic target closure/compression. |
| dependency | [Actual coefficient construction](Yin_C_F0150_v1.md#statement) | The represented delta and delta_N, their actual vacua, coefficient Hilbert norms, separated-leg adjoint isometries, regular h with tau(h inverse)=1 and norm h=4. |
| dependency | [Fock normalization](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Right creation/deletion operators, faithful trace and Wick/Chebyshev orthonormality, including right semicircular multiplication. |
| dependency | [Reference word-cut identity](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) | Exact polynomial free-derivative word-cut formula used to derive (8); no nonlinear example or degree-summability result is transferred. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:45 |
| status | proved |
| reason | Adopt the full forward-domain and intrinsic bare-dual construction after R_F0160 independently checked the entire statement, six proof sections and all three exact inputs. The hidden-factor example satisfies A and F; no full adjoint domain or unrestricted implication is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact ambient and intrinsic full forward domains, explicit operator-norm bound, all-bounded-vector commutator and bare target dual, without an adjoint-domain claim. |
| argument | [Argument](#argument) | Six complete steps: coefficient expansion, complete-block cancellation, partial-block column, orthogonal concatenation and means, actual ambient closure, and intrinsic target closure/compression. |
| dependency | [Actual coefficient construction](Yin_C_F0150_v1.md#statement) | The represented delta and delta_N, their actual vacua, coefficient Hilbert norms, separated-leg adjoint isometries, regular h with tau(h inverse)=1 and norm h=4. |
| dependency | [Fock normalization](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Right creation/deletion operators, faithful trace and Wick/Chebyshev orthonormality, including right semicircular multiplication. |
| dependency | [Reference word-cut identity](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) | Exact polynomial free-derivative word-cut formula used to derive (8); no nonlinear example or degree-summability result is transferred. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0160_v1.md#conclusion) | Whole statement and six-section argument, exact noncommuting cuts, column/isometry estimates, actual original ambient and intrinsic target graphs, dual sign and all direct interfaces. |


---
author: Yin
---
# A weighted criterion for full-domain duals after a correlated coordinate change

Human author: Yin.
The acsy_to_full_domain agent developed this reduction in D_F0003 and fixed the complete argument for independent review during the authorized continuation of T_F0011.
Root suggested the homogeneous automatic-continuity interface used in the all-witness direction.
This mathematical development is distinct from the free semicircular weighted estimate.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Use inner products linear in their second variable.
In a finite von Neumann algebra with faithful normal probability trace, let H=L2(M), Omega=1, and P=P_Omega.
Left multiplication by an element is unmarked, and rho(a) is right multiplication by a.

For a bounded generating tuple Z, put A_Z=C<Z,Z*> and define:

- \(\mathsf A(Z)\): there exist outer derivations \(\delta_i:A_Z\to H\bar\otimes H\), with \(\delta_i Z_j=\delta_{ij}1\otimes1\) and actual \(1\otimes1\in\operatorname{Dom}\delta_i^*\).
- \(\mathsf F(Z)\): there exist complex-linear maps \(D_i:M\Omega\to H\) satisfying \([Z_j,D_i]=\delta_{ij}P\) on all M Omega, without continuity or adjoint-domain assumptions.
- \(\mathsf S(Z)\): the same identities hold for densely defined operators with \(M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*\).


Let M=W*(h,S), H=L2(M), Omega=1, P=P_Omega.
Assume h is bounded, positive, regular and diffuse, and S is bounded selfadjoint.
Assume the original selfadjoint pair (h,S) has joint L2 conjugate variables xi_h,xi_S.
Its represented free difference quotients are partial_h,partial_S on A_0=C<h,S>.
Assume only the S-coordinate canonical contraction

\[
 B_S=(\mathrm{id}\otimes\tau)\partial_S
 \tag{1}
\]

extends to a bounded operator on H.
In particular B_S1=0, [B_S,h]=0 and [B_S,S]=P on H.
The h-coordinate canonical closure B_h need not be bounded on H: [Dab10-U002, Sections 2-3](../audits/literature/Dab10/Yin_U002.md#dab10-u002) supplies M in Dom B_h intersect Dom B_h*, both operator-norm-to-L2 bounds, B_h1=0 and the required full-M commutators.

Put Y=hS and X=(h,Y).
Then X generates M, as proved below.
Write b=h^{-1} when that affiliated inverse belongs to H.

The following precise reduction is established below:

\[
 \mathsf A(X)\quad\Longleftrightarrow\quad h^{-1}\in L^2(M).
 \tag{2}
\]

When b is in L2, the remaining conditions satisfy

\[
 \mathsf F(X)\quad\Longleftrightarrow\quad\mathsf S(X)
 \quad\Longleftrightarrow\quad
 \exists C<\infty\ \forall p\in A_0:
       \|(B_Sp)b\|_2\le C\|p\|.
 \tag{3}
\]

For b in L2, the ACSY derivations constructed below have actual vacuum vectors
\[
 B_S^*b,\qquad \xi_h-(B_S^*b)S+b.
 \tag{V}
\]
If the weighted bound holds, let K_0p=(B_Sp)b on A_0.
Its Hilbert closure K has M contained in both actual domains, and
\[
 K^*q=B_S^*(qb),\qquad q\in M.
 \tag{D}
\]
One may take the generator-first full-domain duals to be the negatives of K|_M and B_h|_M-K rho(S)|_M, for the Y and h coordinates respectively.

Consequently, a correlated reference pair satisfying the premises and b in L2 but violating the weighted bound would refute A-to-F.
The theorem neither supplies such a pair nor proves that the bound always holds.


## Argument

### 1. Generation and the reference interfaces

The spectral cuts e_n=1_[1/n,infinity)(h) increase strongly to 1.
The bounded element c_n=h^{-1}e_n belongs to W*(h), and c_nY=e_nS tends strongly to S.
Hence W*(h,Y)=M, and both A_0 and A_X=C<h,hS,Sh> are L2 dense.

The original conjugate-variable hypothesis is the selfadjoint one: the represented partial_h and partial_S on A_0 have values 1 tensor 1 on their respective coordinates and zero on the other coordinate, and their actual vacua are xi_h,xi_S.
The normalization B_S1=0 is part of being the bounded extension of the canonical contraction, rather than an arbitrary bounded raw dual.

The accepted [Dab10-U002, Sections 2-3](../audits/literature/Dab10/Yin_U002.md#dab10-u002) gives the closed B_h and its actual adjoint on M, with bounds 4||xi_h||2 and 5||xi_h||2 from operator norm to L2.
Its bounded-set weak continuity extends [B_h,h]=P, [B_h,S]=0 from polynomial inputs to M.
We do not infer Hilbert-space boundedness of B_h.
Boundedness of B_S on H is instead an explicit additional hypothesis.

The proof uses [C_F0129, Section 3](Yin_C_F0129_v1.md#3-automatic-continuity-with-a-general-hilbert--schmidt-commutator) only with a diffuse selfadjoint h and Hilbert--Schmidt commutator zero.
Its full independently reviewed proof covers this homogeneous case.
No bounded-division-closure premise from the larger theorem is needed for that auxiliary lemma.

### 2. Actual ACSY derivations and necessity


Suppose b is in L2.
On the represented algebra A_0 define

\[
 \delta_Y=I_{b\otimes1}\partial_S,\qquad
 \delta_h=\partial_h-I_{1\otimes S}\delta_Y,
 \tag{4}
\]

where I_(b tensor 1)(u tensor v)=ub tensor v on finite polynomial tensors, and I_(1 tensor S)(eta tensor v)=eta tensor Sv.
These maps commute with the outer actions on their indicated domains; no bounded extension of I_(b tensor 1) to the whole Hilbert space tensor product is asserted.
Restrict (4) to A_X=C<h,hS,Sh>.
They are represented starred derivations with delta_Y h=0, delta_Y(hS)=1 tensor 1, delta_h h=1 tensor 1, delta_h(hS)=0.

For p in A_0, B_Sp lies in A_0 and hence is bounded, so the right contractions have actual values

\[
 K_0p=(B_Sp)b,\qquad
 Q_hp=B_hp-K_0(pS)+pb.
 \tag{5}
\]

For every q in M, qb is in H.
Boundedness of B_S gives the actual core-adjoint identity

\[
 \langle q,K_0p\rangle
 =\langle qb,B_Sp\rangle
 =\langle B_S^*(qb),p\rangle,
 \qquad p\in A_0,\ q\in M.
 \tag{6}
\]

In particular M is contained in Dom K_0*, and K_0* q=B_S*(qb).
Applying (5)-(6) at 1 gives the actual vacuum vectors

\[
 \delta_Y^*(1\otimes1)=B_S^*b,\qquad
 \delta_h^*(1\otimes1)=\xi_h-(B_S^*b)S+b.
 \tag{7}
\]

Both belong to H.
These identities require only boundedness of the S-coordinate canonical operator, not its h-coordinate counterpart.
They prove A(X).

Conversely, for any A(X) witness, its Y-coordinate derivation satisfies delta_Y(f(h)Y)=f(h) tensor 1 for each scalar polynomial f.
If xi is its actual vacuum, then

\[
 |\tau(f(h))|\le\|\xi\|_2\|h f(h)S\|_2
 \le\|\xi\|_2\|S\|\,\|h f(h)\|_2.
 \tag{8}
\]

Let mu be the compactly supported law of h.
Polynomials are dense in L2(mu), and multiplication by t has dense range because mu has no atom at zero.
Thus t C[t] is dense.
Inequality (8) makes the functional t f -> integral f dmu bounded on this subspace.
If w in L2(mu) is its Riesz representative, then
\[
 \int (t\overline{w(t)}-1)f(t)\,d\mu(t)=0
\]
for all polynomials f.
The coefficient defines a finite complex measure.
Uniform polynomial density in the continuous functions on [0,||h||] implies t overline{w(t)}=1 almost everywhere.
Therefore h^{-1} belongs to L2, with norm at most ||xi||2 ||S||.
No functional-calculus extension of a supplied derivation has been assumed.
This proves (2).

### 3. Any full-domain witness forces the weighted bound

Suppose F(X), and let E=-D_Y be any operator-first Y witness on all M.
Since [E,h]=0 and h is diffuse selfadjoint, the [general Hilbert--Schmidt automatic-continuity lemma in C_F0129, Section 3](Yin_C_F0129_v1.md#3-automatic-continuity-with-a-general-hilbert--schmidt-commutator), with K=0, implies that E:M with its operator norm to H is bounded.
That independently accepted interface does not require a rank-one commutator.

Set eta=E1 and E^circ(a)=E(a)-a eta.
This is still bounded from M to H, is normalized at 1, and has the same left commutators.
It need not be a bounded operator on H.
Since

\[
 h[E^\circ,S]=[E^\circ,hS]=P,
 \tag{9}
\]

evaluation at 1 gives h E^circ(S)=1, so b belongs to H.
Regularity of h now lets (9) be canceled pointwise on H:

\[
 [E^\circ,h]=0,\qquad [E^\circ,S]=bP.
 \tag{10}
\]

The polynomial map K_0 from (5) has exactly (10) and value zero at 1.
For each word in h,S, induction on its length determines its image from these generator commutators and that value.
Consequently

\[
 E^\circ(p)=K_0p=(B_Sp)b,\qquad p\in A_0.
 \tag{11}
\]

The bound for E^circ therefore proves (3)'s weighted estimate.
S need not belong to the target polynomial algebra A_X: the supplied E is defined on all M, so (9)-(11) are legitimate on the larger original selfadjoint core A_0.
No equality between E and a selected canonical closure on every bounded vector is used.

### 4. The weighted bound supplies both domains

Conversely suppose b is in H and the estimate in (3) holds.
Equation (6) proves K_0 is closable and M is already in its actual adjoint domain, with

\[
 \|K_0^*q\|_2\le\|B_S\|\,\|b\|_2\|q\|,
 \qquad q\in M.
 \tag{12}
\]

Let K=overline{K_0}.
Uniformly bounded Kaplansky approximants from A_0, the assumed weighted bound and weak-closedness of the graph give

\[
 M\subseteq\operatorname{Dom}K\cap\operatorname{Dom}K^*,
 \quad\|Ka\|_2\le C\|a\|.
 \tag{13}
\]

Here K*=K_0*, so the adjoint-domain assertion does not require a second bound to be discovered.
The polynomial commutators [K_0,h]=0, [K_0,S]=bP extend to M by the bounded-approximant weak-graph argument, applying it simultaneously to p_n, h p_n, S p_n.
Thus [K,hS]=P on M.

Define on M

\[
 E_Y=K|_M,\qquad E_h=B_h|_M-K\rho(S)|_M.
 \tag{14}
\]

The identities [B_h,hS]=PS and [K rho(S),hS]=P rho(S)=PS show that (14) has all desired operator-first commutators.
Here P rho(S)=PS uses the trace identity tau(aS)=tau(Sa); it does not assert SP=PS.
Its actual adjoints on M are K* and B_h* minus rho(S)K*, respectively.
Therefore -E_h,-E_Y establish S(X), proving the remaining direction of (3).


## Scope

The reference pair need not be free, semicircular or related by a bounded change of variables.
The only Hilbert-space bounded canonical operator required is B_S.
The h-coordinate uses the weaker selfadjoint conjugate-variable contraction bound with all-M actual domains.

The weighted criterion concerns every bare witness: Section 3 first bounds and normalizes any such witness, then determines its values on the original selfadjoint core.
The original core may be larger than A_X; this causes no domain problem for a witness defined on all M.
Section 4 supplies the converse with actual closed and adjoint domains.
The result does not identify an arbitrary supplied map with K on all M.

No right-order assertion about (h,Sh), general adjoint invariance of F, or counterexample to the general A-to-F implication is part of this statement.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:24 |
| status | open |
| reason | Complete correlated-coordinate criterion with explicit actual ACSY vacua and an all-witness weighted characterization of bare/full-adjoint dual existence; independent fixed-version review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Weighted characterization](#statement) | Generation, A iff inverse in L2, F iff S iff the weighted bound, and actual domain and vacuum formulas. |
| argument | [Complete argument](#argument) | Sections 1-4, including arbitrary-witness normalization and actual core-adjoint/graph restoration. |
| dependency | [Selfadjoint contraction interface](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Sections 2-3 provide B_h and its actual adjoint on M with operator-norm-to-L2 bounds and bounded-set weak continuity. |
| dependency | [General Hilbert--Schmidt automatic continuity](Yin_C_F0129_v1.md#3-automatic-continuity-with-a-general-hilbert--schmidt-commutator) | The independently reviewed auxiliary lemma, used only for diffuse h and homogeneous commutator zero. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:30 |
| status | proved |
| reason | Independent whole-proof review verified the exact correlated-coordinate reduction, actual vacua and domains, and necessity of the weighted estimate for every bare full-domain witness. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Weighted characterization](#statement) | Generation, A iff inverse in L2, F iff S iff the weighted bound, and actual domain and vacuum formulas. |
| argument | [Complete argument](#argument) | Sections 1-4, including arbitrary-witness normalization and actual core-adjoint/graph restoration. |
| dependency | [Selfadjoint contraction interface](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Sections 2-3 give B_h and its actual adjoint on M with operator-norm-to-L2 bounds and bounded-set weak continuity. |
| dependency | [General Hilbert--Schmidt automatic continuity](Yin_C_F0129_v1.md#3-automatic-continuity-with-a-general-hilbert--schmidt-commutator) | Accepted auxiliary lemma for diffuse h and homogeneous commutator zero. |
| review | [Independent full review](../audits/reviews/Yin_R_F0142_v1.md#conclusion) | Complete fixed statement, four proof sections and both input interfaces, with exact all-witness and actual-domain scope. |


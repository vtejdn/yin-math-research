---
author: Yin
---
# Normal representatives of bare normal duals and an exact L1-to-L2 reduction

Date: 2026-10-14.
Human author Yin.
Root developed the normal-representative construction and exact range criterion during the user-directed study of left contractions for normal tuples.
The review_adjoint_closure agent supplied the L1 conjugate formula and dyadic boundary example; root checked and integrated them.
The acsy_rationality_check agent checked the preliminary normal-part algebra.
These discussions are not a completed fixed-artifact review.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

Let (M,tau) be finite tracial with faithful normal tracial state, H=L2(M,tau), Omega=1, P=P_Omega, and inner product linear in the second variable.
Let X=(X_1,...,X_d) be a finite normal generating tuple with bare complex-linear maps D_i:M Omega -> H satisfying [X_j,D_i]=delta_ij P.
Put A=C<X,X*>.
Write delta_i for the unique starred derivations in [C_F0070](Yin_C_F0070_v1.md#statement), R_i=(id tensor tau)delta_i and L_i=(tau tensor id)delta_i.

A map M -> H is called normal when it is ultraweak-to-weak continuous; for M -> L1(M) the target carries the weak Banach-space topology.

**A. Normal representatives.**
There exist unique normal bounded maps E_i:M -> H satisfying
\[
 E_i1=0,\qquad [E_i,X_j]=\delta_{ij}P. \tag{1}
\]
They agree with R_i on A.
For any normalized supplied E_i^{raw}(a)=-D_i(a)+aD_i1, the construction gives ||E_i|| <= 2||E_i^{raw}|| in the M-operator-norm-to-H norm.
If N_i=W*(X_j:j neq i), then
\[
 E_i(ba)=bE_i(a),\qquad E_i(b)=0\quad(b\in N_i,\ a\in M). \tag{2}
\]
No equality with arbitrary nonnormal supplied maps on all M is asserted.

**B. Full-M L1 conjugate implementation.**
Define E_i^flat:H -> L1(M) by
\[
 \tau((E_i^\flat b)^*a)=\langle b,E_i(a)\rangle,\qquad
 \xi_i=E_i^\flat1. \tag{3}
\]
Then
\[
 G_i(b)=b\xi_i-E_i^\flat b\qquad(b\in M) \tag{4}
\]
is normal and bounded M -> L1, with G_i1=0 and ||G_i||_{infinity to 1} <= 2||E_i||.
On A,
\[
 G_i(b)=(L_i(b^*))^*=(\mathrm{id}\otimes\tau)\delta_i^\#(b),
 \quad \delta_i^\#(b)=(\delta_i(b^*))^\dagger, \tag{5}
\]
where (u tensor v)^dagger=v* tensor u*.
Thus its core values lie in H.
Write K_i=Theta(k_i) for the actual HS starred commutator in C_F0070.
As L1 equalities on all M,
\[
 [G_i,X_j]=\delta_{ij}K_i^*,\qquad [G_i,X_j^*]=\delta_{ij}P. \tag{6}
\]

**C. Exact remaining criterion.**
The following are equivalent:

1. Every L_i:A -> H is bounded for the operator norm.
2. G_i(M) is contained in L2(M) for every i.
3. Every G_i is bounded M -> H.

Each condition gives the ACSY24 actual-vacuum condition and both canonical bounded-vector domains by C_F0072.
This statement does not prove the conditions always hold.

**D. General HS relations are insufficient.**
There is a normal E:L-infinity(0,1) -> L2(0,1), E1=0 and ||E|| <= 2, whose restriction to C[x], x(s)=s, is closable and whose commutator with x is HS.
The induced outer derivation on C[x] has bounded right contraction E but no actual vacuum and an unbounded left contraction.
Its full-M normal L1 conjugate implementation fails to take all bounded inputs into L2.
In this example [E,x] is NOT P, so it is not a counterexample to the normal rank-one dual question.

## Argument

### 1. The normal part and source interface

The newly inspected [Bla06-U002](../audits/literature/Bla06/Yin_U002.md#bla06-u002) supplies the canonical normal homomorphism theta:M** -> M, dual to inclusion M_* -> M*, and its central-summand description.
The exact source is Blackadar's 8 February 2017 author revision, III.5.2.5--9 (printed338--339/PDF346--347), III.5.2.14--15 (printed340/PDF348), and III.1.1.13 (printed238--239/PDF246--247).
Statements and applicability were read directly and accepted; their full foundational predecessor proofs were not re-audited.

Let ker theta=(1-e)M** with e central and let j:M -> eM** be the inverse of theta on this summand.
For the canonical C*-inclusion iota,
\[
 j(a)=e\iota(a),\qquad \|j(a)\|=\|a\|. \tag{7}
\]
A normal functional on M extends to M** through theta, hence has its original value at j(a).

For a bounded Banach-space map T:M -> H, reflexivity defines
\[
 \mathcal N(T)=T^{**}j:M\to H^{**}=H. \tag{8}
\]
This map is normal, linear in T, has norm at most ||T||, and fixes a normal T.
The last assertion follows by testing with Hilbert functionals and the preceding normal-functional identity.
The construction commutes with postcomposition by bounded operators on H.
It commutes with precomposition by left or right multiplication by any a in M: the bidual maps multiply by iota(a), and centrality gives j(ab)=iota(a)j(b), j(ba)=j(b)iota(a).
Thus the normal-part construction has precisely the module compatibility used next; no complete-boundedness hypothesis is required.

### 2. Normalized representatives and uniqueness

[C_F0069 Part A](Yin_C_F0069_v1.md#statement) makes the supplied maps and normalized E_i^{raw} bounded M -> H.
Apply (8) to [E_i^{raw},X_j]=delta_ij P.
The right side is normal since P(a)=tau(a)1.
Hence [N(E_i^{raw}),X_j]=delta_ij P.
Put
\[
 E_i(a)=\mathcal N(E_i^{raw})(a)-a\mathcal N(E_i^{raw})(1). \tag{9}
\]
The correction is normal M -> H, because scalar pairings with a fixed L2 vector are L1 normal functionals.
It commutes with all left multipliers, so (1) and the claimed norm bound follow.

The difference E_i-E_i^{raw} commutes with each X_j.
The homogeneous bounded-map Fuglede argument in [C_F0070](Yin_C_F0070_v1.md#argument) makes it commute with each X_j*.
It vanishes at 1, so vanishes on A.
This proves agreement with R_i.
Two normalized normal solutions have a difference vanishing on A by the same argument; ultraweak density and normality give zero on all M.
This proves uniqueness.

For j neq i, E_i commutes with X_j and X_j*.
Thus E_i(ba)=bE_i(a) when b is a polynomial in these other starred coordinates.
For fixed a, both sides are ultraweak-to-weak continuous in b.
Density extends to N_i; taking a=1 proves (2).
No operator-norm density in M is assumed.

### 3. The L1 preadjoint

Use the accepted [AP18 tracial L1 interface](../audits/literature/AP18/Yin_U003.md#l1-predual-interface), Theorems7.4.5 and7.4.9.
The scalar functional a -> <b,E_i(a)> is normal, so (3) has a unique L1 representing vector and
\[
 \|E_i^\flat b\|_1\le\|E_i\|\|b\|_2,\qquad
 \|\xi_i\|_1\le\|E_i\|. \tag{10}
\]
The star in (3) makes E_i^flat complex linear.
Consequently (4) is bounded M -> L1 with norm at most 2||E_i|| and vanishes at 1.
It is normal: for c in M,
\[
 \tau(cE_i^\flat b)=\langle E_i(c^*),b\rangle,
\]
a normal functional of b in M; multiplication b -> b xi_i is also normal after pairing against M.

On A, let phi_i=(tau tensor tau)delta_i=tau E_i.
Then phi_i(a)=tau(xi_i* a), and the Leibniz identity gives
\[
 \phi_i(ab)=\tau(L_i(a)b)+\tau(aR_i(b)). \tag{11}
\]
For a,b in A this yields
\[
 \langle a,E_i(b)\rangle
 =\phi_i(a^*b)-\tau(L_i(a^*)b)
 =\tau\big((a\xi_i-(L_i(a^*))^*)^*b\big).
\]
All densities in this identity are L1.
Normal pairing and the ultraweak density of A identify them, so
\[
 E_i^\flat a=a\xi_i-(L_i(a^*))^*. \tag{12}
\]
This proves (5), including its H-valued core assertion, without assuming xi_i in H.

C_F0070 gives [E_i,X_j*]=delta_ij K_i on all M.
Transposing the two generator identities in the pairing (3) gives
\[
 \begin{split}
 E_i^\flat(X_jb)&=X_jE_i^\flat b-\delta_{ij}K_i^*b,\\
 E_i^\flat(X_j^*b)&=X_j^*E_i^\flat b-\delta_{ij}Pb .
 \end{split}
\]
Subtracting from multiplication by xi_i proves (6).
These are L1 identities; the HS terms lie in L2 and hence in L1.

### 4. Exact range equivalence

If G_i(M) is contained in L2, its graph as a map M -> L2 is closed.
For a_n -> a in operator norm and G_i(a_n) -> v in L2, the same images converge in L1 both to G_i(a), by the L1 bound, and to v, by continuous inclusion L2 into L1.
Thus v=G_i(a).
Closed graph gives boundedness M -> H.
Boundedness conversely gives the range inclusion and, by (5), the left-contraction bound on A.

Suppose conversely that all L_i are bounded on A.
The contractions of delta_i# are J L_i J and J R_i J, where J(a)=a*.
Both are bounded.
C_F0072 makes the canonical right contraction of delta_i# closable with a closure containing M.
Its commutator with X_j* is delta_ij P on the core; boundedness of this commutator and graph approximation pass it to the full closure domain.
Negation therefore gives full-domain duals for X*.

Apply the already proved Part A to X*, yielding normalized normal maps F_i:M -> H with [F_i,X_j*]=delta_ij P.
The C_F0070 uniqueness theorem for X* identifies their starred derivations with delta_i#, so F_i|A=G_i|A by (5).
Viewed as M-to-L1 maps, both F_i and G_i are normal.
They agree on the ultraweakly dense A, hence on M.
Thus G_i(M) lies in L2.
Part A was proved without this range criterion, so this use is not circular.

C_F0072 applied directly to delta_i gives the stated actual vacuum and both canonical domains.

### 5. A dyadic averaging boundary example

Let I_n=(2^{-n},2^{-n+1}], ell_n=2^{-n}, and let J_n be the left subinterval of I_n of length epsilon_n=ell_n squared.
Define on M=L-infinity(0,1)
\[
 (Ef)(s)=\epsilon_n^{-1}\int_{J_n}f(t)\,dt-f(s)
 \quad(s\in I_n). \tag{13}
\]
Then E1=0 and |Ef|<=2||f||, proving ||E||_{infinity to 2}<=2.
For a test g in L2 its scalar transpose has density
\[
 \sum_n\epsilon_n^{-1}1_{J_n}\int_{I_n}\overline{g(s)}\,ds
 -\overline g .
\]
Its L1 norm is at most 2||g||_1<=2||g||_2.
This verifies normality directly.

Each block operator on L2(I_n) is bounded.
The maximal direct sum is closed: convergence of a vector and its image determines the limit on each block, and the limiting image is square summable.
It contains every bounded input by the estimate above.
Therefore E|C[x] is closable, where x(s)=s.

The commutator [E,x] has kernel
\[
 K(s,t)=\sum_n\frac{t-s}{\epsilon_n}1_{I_n}(s)1_{J_n}(t),\qquad
 \|K\|_{HS}^2\le\sum_n\frac{\ell_n^3}{\epsilon_n}
 =\sum_n\ell_n<\infty. \tag{14}
\]
For each polynomial p put
\[
 \delta(p)(s,t)=
 \sum_n\frac{p(t)-p(s)}{\epsilon_n}1_{I_n}(s)1_{J_n}(t). \tag{15}
\]
The polynomial Lipschitz bound and (14) put this in L2((0,1)^2).
The elementary difference-of-products identity proves the outer Leibniz rule.
The right contraction, integrating t, is E(p).
The left contraction is
\[
 (Lp)(t)=\frac{1_{J_n}(t)}{\epsilon_n}
       \left(\ell_n p(t)-\int_{I_n}p(s)\,ds\right)
 \quad(t\in I_n). \tag{16}
\]
Its squared norm is at most Lip(p) squared times sum ell_n^4/epsilon_n = Lip(p) squared times sum ell_n squared, so each polynomial output lies in H.

The actual L1 preadjoint gives
\[
 \xi=E^\flat1=\frac{\ell_n}{\epsilon_n}1_{J_n}-1
 \quad\text{on }I_n. \tag{17}
\]
Its block L1 norm is 2(ell_n-epsilon_n), so xi is in L1.
Its block L2 square is ell_n squared/epsilon_n-ell_n=1-ell_n, so xi is not in L2.
If tau E on C[x] had an L2 representing vector, its difference from xi would be an L1 density annihilating every polynomial, hence every continuous function by uniform approximation.
Uniqueness of finite measures on [0,1] would force equal densities, a contradiction.
Thus 1 tensor 1 is not in Dom delta*.

The full map G(f)=f xi-E^flat f is the same expression (16) with f in place of p, and is normal bounded M -> L1.
Choose f=1 on each J_n and f=-1 on I_n minus J_n.
Then
\[
 \|Gf\|_2^2
 =\sum_n\frac{4(\ell_n-\epsilon_n)^2}{\epsilon_n}
 =4\sum_n(1-\ell_n)^2=\infty. \tag{18}
\]
The left contraction cannot be bounded on C[x]: otherwise the right bound and C_F0072 would give the actual vacuum just disproved.
Here delta(x)=K, not 1 tensor 1.
The example therefore rules out a general-HS shortcut, not the special rank-one dual conjecture.

## Scope and continuation

The newly inspected source input is Bla06-U002; C_F0069/C_F0070 supply the bare-normal continuity, Fuglede and uniqueness interfaces, C_F0072 supplies the two-contraction result, and the AP18 interface supplies tracial L1.
The dyadic example uses only the displayed elementary integrals and the standard direct-sum graph argument.
No new singular-integral theorem is imported.

The remaining general question is whether the special normal rank-one identities force the maps G_i in (4) to take every bounded input into L2.
Part A also retains the other-coordinate module property (2), which may be useful in that step.
No rank-one counterexample, unrestricted left estimate, equality with arbitrary supplied maps off the core, or new mathematical Task completion is asserted.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14 |
| status | open |
| reason | Complete normal-representative and exact range-reduction candidate, with a dyadic general-HS boundary example; independent fixed-artifact review remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A-D with exact normality, range, domain and non-rank-one qualifications. |
| argument | [Argument](#argument) | Normal bidual summand, representative uniqueness, L1 preadjoint, exact range criterion and dyadic computations. |
| dependency | [Automatic continuity](Yin_C_F0069_v1.md#statement) | Bare normal full-domain duals are bounded M to H. |
| dependency | [Starred derivation and uniqueness](Yin_C_F0070_v1.md#argument) | Homogeneous bounded-map Fuglede, actual starred commutators and unique core derivations. |
| dependency | [Two-contraction criterion](Yin_C_F0072_v1.md#statement) | Actual vacua and both canonical domains under two bounds. |
| dependency | [Normal bidual source](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Exact universal bidual, normal quotient and central-summand interface, directly inspected in the retained source. |
| dependency | [AP18 L1 interface](../ledger/Yin_L_F0035_v1.md#l1-predual-interface) | Normal functional densities, norm identity and uniqueness in tracial L1. |

### Decision reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T14:11 |
| status | proved |
| reason | The complete fixed normal-representative, L1 implementation, exact range criterion and dyadic boundary example passed independent review. The special rank-one L1-to-L2 range question remains open; the general-Hilbert-Schmidt example does not refute it. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A-D with exact normality, range, domain and non-rank-one qualifications. |
| argument | [Argument](#argument) | Normal bidual summand, representative uniqueness, L1 preadjoint, exact range criterion and dyadic computations. |
| dependency | [Automatic continuity](Yin_C_F0069_v1.md#statement) | Bare normal full-domain duals are bounded M to H. |
| dependency | [Starred derivation and uniqueness](Yin_C_F0070_v1.md#argument) | Homogeneous bounded-map Fuglede, actual starred commutators and unique core derivations. |
| dependency | [Two-contraction criterion](Yin_C_F0072_v1.md#statement) | Actual vacua and both canonical domains under two bounds. |
| dependency | [Normal bidual source](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Exact universal bidual, normal quotient and central-summand interface, directly inspected in the retained source. |
| dependency | [AP18 L1 interface](../ledger/Yin_L_F0035_v1.md#l1-predual-interface) | Normal functional densities, norm identity and uniqueness in tracial L1. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0138_v1.md#conclusion) | Exact fixed statement and complete argument, with actual source interfaces, review arrangement and unresolved scope disclosed. |

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:02 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Parts A-D with exact normality, range, domain and non-rank-one qualifications. |
| argument | [Exact material](#argument) | Normal bidual summand, representative uniqueness, L1 preadjoint, exact range criterion and dyadic computations. |
| dependency | [Exact material](Yin_C_F0069_v1.md#statement) | Bare normal full-domain duals are bounded M to H. |
| dependency | [Exact material](Yin_C_F0070_v1.md#argument) | Homogeneous bounded-map Fuglede, actual starred commutators and unique core derivations. |
| dependency | [Exact material](Yin_C_F0072_v1.md#statement) | Actual vacua and both canonical domains under two bounds. |
| dependency | [Exact material](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Exact universal bidual, normal quotient and central-summand interface, directly inspected in the retained source. |
| dependency | [Exact material](../audits/literature/AP18/Yin_U003.md#ap18-u003) | Normal functional densities, norm identity and uniqueness in tracial L1. |
| review | [Original finding](../audits/reviews/Yin_R_F0138_v1.md#conclusion) | Whole Parts A–D and Sections 1–5 normal bidual representatives, full-M L1 implementation, exact L2 range criterion and dyadic general-HS boundary example; preliminary-route/context relationship unknown, no recorded substantive reviewer repair. |

---
author: Yin
---
# Actual vacua and both full domains after a singular coordinate change

Human author: Yin.
The acsy_to_full_domain agent developed the actual-vacuum necessity, converse transport, unbounded product domains, and full-domain restoration.
Root supplied the input-weight energy mechanism and the separately fixed output-weight theorem C_F0136.
The preparatory exchanges checked these interfaces together; they do not constitute an independent review of this new complete argument.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be finite with faithful normal probability trace, H=L2(M,tau), Omega=1 and P=P_Omega.
Let h,S be bounded selfadjoint generators of M with a joint L2 conjugate system xi_h,xi_S.
Assume h is positive and regular.
Put

\[
 A_0=\mathbb C\langle h,S\rangle,\qquad Y=hS,\qquad
 X=(h,Y),\qquad A_X=\mathbb C\langle h,hS,Sh\rangle .
 \tag{1}
\]

Let partial_h,partial_S denote the represented selfadjoint free difference quotients on A_0.
No freeness assumption on h,S and no Hilbert-space boundedness of either canonical contraction is imposed.

For a bounded generating tuple Z, use the following existential conditions, in the generator-first convention.

- \(\mathsf A(Z)\): there are outer derivations \(\delta_i:A_Z\to H\bar\otimes H\), where \(A_Z=\mathbb C\langle Z,Z^*\rangle\), with \(\delta_i Z_j=\delta_{ij}1\otimes1\) and actual \(1\otimes1\in\operatorname{Dom}\delta_i^*\).
- \(\mathsf S(Z)\): there are densely defined operators \(D_i\) with \(M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*\), satisfying \([Z_j,D_i]=\delta_{ij}P\) on M Omega.
- \(\mathsf F(Z)\): there are arbitrary complex-linear maps \(D_i:M\Omega\to H\) with those commutators, without adjoint-domain assumptions.

Then X generates M, and

\[
 \boxed{\mathsf A(X)\ \Longleftrightarrow\ \mathsf S(X)
 \ \Longleftrightarrow\
 \bigl[b=h^{-1}\in L^2(M)\ \hbox{and}\ b\xi_S\in L^2(M)\bigr].}
 \tag{2}
\]

Each condition in (2) implies F(X).
No reverse implication from F(X) is asserted.

The product b xi_S is the actual affiliated multiplication product.
Since b and xi_S are selfadjoint, the L2 condition is equivalent to xi_S b in L2, with the same norm.
When (2) holds, the constructed derivations have actual vacua

\[
 v_Y=b\xi_S,\qquad
 v_h=\xi_h-b\xi_SS+b.
 \tag{3}
\]

Write E=overline{(id tensor tau)partial_S} and B_h=overline{(id tensor tau)partial_h}.
The core operator

\[
 K_0p=(Ep)b,\qquad p\in A_0,
 \tag{4}
\]

is closable.
Its closure K and its actual adjoint contain all M Omega in their domains.
On M,

\[
 \|Ka\|_2\le4\|b\xi_S\|_2\|a\|,\qquad
 \|K^*a\|_2\le5\|b\xi_S\|_2\|a\|.
 \tag{5}
\]

One may choose D_Y=-K|_M and D_h=-(B_h-K rho(S))|_M.
Here rho(S) is right multiplication by S.
Complete product domains beyond the stated inclusions are not identified.

## Argument

### 1. Reference domains, generation and weighted polynomial approximation

The exact selfadjoint conjugate-variable interface in [Dab10-U002, Sections 1-3](../audits/literature/Dab10/Yin_U002.md#dab10-u002) supplies represented partial_h,partial_S, their real coassociative algebraic structure, and the closed canonical operators E,B_h.
Their domains and actual adjoint domains contain M, with operator-norm-to-L2 bounds.
In particular

\[
 [E,h]=0,\quad [E,S]=P,\qquad
 [B_h,h]=P,\quad [B_h,S]=0
 \quad\hbox{on }M.
 \tag{6}
\]

The source's polynomial adjoint formula is

\[
 E^*q=q\xi_S-Eq,\qquad q\in A_0.
 \tag{7}
\]

These are the original specified closures.
Boundedness of E on H is not assumed.

For e_n=1_[1/n,infinity)(h), the bounded c_n=h^{-1}e_n belongs to W*(h), and c_nY=e_nS tends strongly to S.
Hence W*(h,Y)=M and A_X is L2 dense, before any assumption that b belongs to L2.

We will use one joint approximation.
Suppose b and b xi_S belong to H.
Let mu be the spectral law of h and let nu be the finite positive measure nu(B)=tau(xi_S^2 1_B(h)).
The L1 density xi_S^2 defines a normal positive functional, so this is well-defined even if xi_S is unbounded.
The two assumed norms give 1/t in L2(mu+nu).
Real polynomials are dense in that space on the compact interval [0,||h||].
Thus one can choose c_n=c_n* in C[h] with

\[
 c_n\longrightarrow b,\quad
 c_n\xi_S\longrightarrow b\xi_S,\quad
 \xi_Sc_n\longrightarrow\xi_Sb
 \quad\hbox{in }H.
 \tag{8}
\]

For the second and third convergences use ||xi_S(c_n-b)||2^2=int |c_n(t)-1/t|^2 dnu(t) and the tracial involution.
The c_n need not be uniformly bounded; each is a bounded polynomial, and the specified three H convergences are what the later closed-graph arguments require.

### 2. An actual ACSY vacuum forces both integrability conditions

Assume A(X), and take the Y-coordinate derivation delta with actual vacuum v.
Its assigned values are delta h=0 and delta Y=1 tensor 1.
The represented relation Yh=hY* implies

\[
 (h\otimes1)\delta(Y^*)=1\otimes h.
 \tag{9}
\]

Slice the second tensor leg against the nonzero H vector h.
The slice w belongs to H and satisfies hw=||h||2^2 1.
Regularity forces w=||h||2^2 h^{-1}, proving b in H.
Left multiplication by h is injective on H and therefore on the first leg of H bar tensor H.
Consequently (9) uniquely determines

\[
 \delta(Y^*)=b\otimes h.
 \tag{10}
\]

Define the bounded inner coefficient map I_(h tensor 1)(u tensor v)=uh tensor v.
It commutes with both outer actions.
Its composition with delta agrees with partial_S on h,Y,Y*: the values are respectively zero, h tensor 1 and 1 tensor h.
Both are represented derivations, so

\[
 \partial_S|_{A_X}=I_{h\otimes1}\delta.
 \tag{11}
\]

Since delta(hp)=h dot delta(p), the actual adjoint identity tested on A_X is delta*(h tensor 1)=hv.
Pairing (11) against 1 tensor 1 and comparing with the original actual conjugate xi_S gives xi_S=hv on the dense core.
Hence v=b xi_S belongs to H.
This argument neither extends delta to functional calculus nor assumes a full-domain dual.

### 3. The integrability conditions construct the actual vacua

Suppose b and b xi_S belong to H.
For the polynomials c_n in (8), partial_S c_n=0 and E c_n=0.
Equation (7) gives E*c_n=c_n xi_S.
Closedness of E* yields

\[
 b\in\operatorname{Dom}E^*,\qquad E^*b=b\xi_S.
 \tag{12}
\]

On A_0 define the inner coefficient operations on finite polynomial tensors by

\[
 I_{b\otimes1}(u\otimes v)=ub\otimes v,\qquad
 I_{1\otimes S}(\eta\otimes v)=\eta\otimes Sv,
\]

and set

\[
 \delta_Y=I_{b\otimes1}\partial_S,\qquad
 \delta_h=\partial_h-I_{1\otimes S}\delta_Y.
 \tag{13}
\]

Every value is a Hilbert tensor because the input derivatives are finite tensors of bounded factors and b is in H.
Both operations commute with the outer actions on these domains.
The two maps are derivations on the represented algebra A_0; restriction to A_X respects all starred relations and gives the required values on h,Y.

For p in A_0 their right contractions are

\[
 Q_Yp=K_0p=(Ep)b,\qquad
 Q_hp=B_hp-K_0(pS)+pb.
 \tag{14}
\]

The latter identity follows from the Leibniz rule and traciality on the second tensor leg.
Pairing K_0p against 1 and using (12) gives its actual vacuum b xi_S.
Pairing the second expression in (14) against 1 gives xi_h-(b xi_S)S+b.
These H vectors therefore certify the actual vacuum-adjoint domains of the two derivations, proving A(X) and (3).

### 4. An input-weight estimate and its actual domains

The new estimate needed for the adjoint uses the same real coassociative core calculation as the [output-weight theorem C_F0136](Yin_C_F0136_v1.md#statement).
For z in A_0, that theorem's core energy identity with weight 1 is

\[
 \|Ez\|_2^2
 =2\operatorname{Re}\tau((Ez)^*z\xi_S)
  -(\tau\otimes\tau)
       \bigl(\partial_S(z^*z)(1\otimes\xi_S)\bigr).
 \tag{15}
\]

Take c=c* in C[h], and an analytic-core unitary u=a+i(1-a^2)^(1/2) with a=a* in A_0 and ||a||<1.
Its binomial partial sums u_n converge in operator norm, and their partial_S derivatives and adjoint derivatives converge in H bar tensor H by the differentiated absolutely convergent series.
As partial_S c=0, the same holds for z_n=u_n c, with

\[
 \partial_S(z_n^*z_n)
 =c\cdot\partial_S(u_n^*u_n)\cdot c\longrightarrow0.
\]

The contractions E z_n converge in H; closedness identifies the limit with E(uc).
Thus (15) passes to the limit exactly as in C_F0136, using bounded c and pairing the last term against the fixed tensor 1 tensor xi_S.
Since u is unitary,

\[
 \|E(uc)\|_2^2
 =2\operatorname{Re}\langle E(uc),uc\xi_S\rangle
 \le2\|E(uc)\|_2\|c\xi_S\|_2.
\]

Applying the same argument to u*, decomposing a=(u+u*)/2, rescaling selfadjoint a, and decomposing arbitrary p into its real and imaginary parts gives

\[
 \|E(pc)\|_2\le4\|c\xi_S\|_2\|p\|,
 \qquad p\in A_0,\quad c=c^*\in\mathbb C[h].
 \tag{16}
\]

For the sequence (8) and fixed p in A_0, the exact polynomial formula

\[
 E(pc_n)=(\mathrm{id}\otimes\tau)(\partial_Sp\cdot c_n)
\]

converges in H because partial_S p is a finite tensor and c_n -> b in H.
Also pc_n -> pb in H.
Closedness and (16) therefore give actual membership and the bound

\[
 pb\in\operatorname{Dom}E,\qquad
 E(pb)=(\mathrm{id}\otimes\tau)(\partial_Sp\cdot b),\qquad
 \|E(pb)\|_2\le4\|b\xi_S\|_2\|p\|.
 \tag{17}
\]

Equation (7) at pc_n, together with (8) and (17), similarly gives

\[
 pb\in\operatorname{Dom}E^*,\qquad
 E^*(pb)=pb\xi_S-E(pb),\qquad
 \|E^*(pb)\|_2\le5\|b\xi_S\|_2\|p\|.
 \tag{18}
\]

These are actual products and actual Hilbert adjoints.
They are not inferred from a formal expression E*rho(b).

### 5. Both domains and the transported dual system

The output-weight theorem C_F0136 applies to partial_S, B=C[h], and the positive affiliated b.
Its two integrability premises are exactly those in (2), by selfadjointness.
Thus

\[
 \|K_0p\|_2\le4\|b\xi_S\|_2\|p\|,\qquad p\in A_0.
 \tag{19}
\]

For p,q in A_0, (18) gives the actual pairing

\[
 \langle q,K_0p\rangle
 =\langle qb,Ep\rangle
 =\langle E^*(qb),p\rangle .
 \tag{20}
\]

Hence A_0 is contained in Dom K_0*, with K_0*q=E*(qb).
It follows that K_0 is closable; write K=overline{K_0}.
Equations (18)-(19) supply both operator-norm-to-L2 bounds on this common dense star core.

For any a in M, choose uniformly bounded Kaplansky approximants p_n in A_0 tending to a in H.
Boundedness of K_0p_n gives a weakly convergent subsequence, and weak-closedness of the closed graph of K puts a in Dom K.
Apply the same argument to the closed operator K_0*=K*, using (18), to obtain a in Dom K*.
Letting the harmless norm-approximation tolerance tend to zero gives (5).

On A_0, K_0 has [K_0,h]=0 and [K_0,S]=bP.
The uniform bound (19) and weak closed graphs extend these identities to M, by applying bounded approximants simultaneously to p_n, hp_n and Sp_n.
In particular [K,hS]=P.

Define on the dense domain M

\[
 E_Y=K|_M,\qquad E_h=(B_h-K\rho(S))|_M.
 \tag{21}
\]

All products are defined since aS belongs to M.
Their actual adjoints on M are K* and B_h* minus rho(S)K*, respectively.
The identities [B_h,hS]=PS and [K rho(S),hS]=P rho(S)=PS show that the correction cancels the unwanted Y commutator; P rho(S)=PS uses tau(aS)=tau(Sa).
Consequently -E_Y,-E_h prove S(X).

### 6. Full adjoint domains imply the actual ACSY condition in this class

For clarity, this direction uses only h positive regular, S bounded selfadjoint and M=W*(h,S); the original conjugate system is not needed.

Assume S(X).
Change to operator-first witnesses and normalize at 1 by subtracting a -> a eta_i, where eta_i is the original witness value at 1.
This operation preserves all full-M commutators and keeps M in the actual adjoint domains: the map a -> a eta_i, restricted to M, has actual adjoint q -> q eta_i* on every q in M.

Call the normalized witnesses E_Y,E_h.
From [E_Y,h]=0 and [E_Y,hS]=P,

\[
 h[E_Y,S]=P,\qquad h E_Y(S)=1.
\]

Thus b=h^{-1} belongs to H.
Expand the represented identity Yh=hY* using the full-M commutator product rule.
It gives

\[
 [E_Y,Y^*]=bPh,\qquad
 [E_h,Y^*]=SP-bPY^*
 \quad\hbox{on }M.
 \tag{22}
\]

Each right side extends to a bounded Hilbert--Schmidt operator, because b is an H vector and all other displayed coefficients are bounded.

Use the unitary identification

\[
 \Theta:H\bar\otimes H\longrightarrow\mathcal S_2(H),
 \qquad \Theta(u\otimes v)(a)=u\,\tau(va).
 \tag{23}
\]

For bounded u,v this is uPv.
The formula extends by the rank-one Hilbert--Schmidt norm to all tensors, obeys Theta(a dot zeta dot c)=a Theta(zeta)c, and has Theta(zeta)1=(id tensor tau)zeta.
These precise interfaces are the ones recorded in [C_F0070, statement and interfaces](Yin_C_F0070_v1.md#statement-and-interfaces); none of that Claim's normal-coordinate inference is being used.

Equations (22) and the prescribed generator commutators imply that [E_i,p] on M has a bounded Hilbert--Schmidt extension for every p in A_X.
Its extension is unique because M is dense.
The commutator depends on the represented element p, not a formal expression, so

\[
 \delta_i(p)=\Theta^{-1}([E_i,p])
\]

defines a represented outer derivation on A_X with the required values on h,Y.
Normalization gives E_i(p)=(id tensor tau)delta_i(p).
Since 1 belongs to the actual adjoint domain of E_i, pairing yields

\[
 \langle1\otimes1,\delta_i(p)\rangle
 =\langle1,E_i(p)\rangle
 =\langle E_i^*1,p\rangle .
\]

Thus 1 tensor 1 belongs to the actual adjoint domain of delta_i.
This proves A(X) and completes (2).

## Scope and continuation

C_F0135 characterized the weighted obstruction under a Hilbert-space bounded canonical S-contraction.
C_F0136 and the input-weight calculation above remove that extra assumption and force both domains whenever the actual target vacuum exists.
Therefore the earlier one-sided correlated-reference counterexample search cannot separate A from F in the present finite-Fisher reference class.

The theorem does not prove F implies A in this class or any implication A-to-F for arbitrary nonnormal tuples.
It also does not treat a coordinate change whose inverse weights are outside the kernel of the reference derivation.
Such cases require additional arguments.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:37 |
| status | open |
| reason | Complete candidate proving A iff full-adjoint-domain duals iff the two actual integrability conditions for a correlated finite-Fisher reference pair; input/output weight limits and all actual adjoint domains are proved at the stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual-vacuum and full-domain equivalence](#statement) | Equivalence (2), consequence F, actual vacua, operator constructions and both quantitative bounds. |
| argument | [Complete argument](#argument) | Sections 1-6, including actual-vacuum necessity, input-weight domain passage, full graph restoration and S-to-A reconstruction. |
| dependency | [Selfadjoint contraction and adjoint interface](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Sections 1-3 provide represented real free difference quotients, specified canonical closures, core adjoint identities and both actual M domains for E and B_h. |
| dependency | [Output kernel-weight estimate](Yin_C_F0136_v1.md#statement) | The affiliated output estimate, core energy identity and analytic-unitary first-derivative approximation used in Sections 4-5. |
| dependency | [Hilbert--Schmidt tensor identification](Yin_C_F0070_v1.md#statement-and-interfaces) | Only the universal unitary tensor identification and its outer-action/vacuum compatibility; no normal-coordinate theorem is imported. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:48 |
| status | proved |
| reason | Complete independent review verified arbitrary-witness necessity, simultaneous weighted approximation, actual reference product domains, both contraction estimates, full-domain restoration and strong-witness reconstruction. The converse from F remains outside the result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual-vacuum and full-domain equivalence](#statement) | Equivalence (2), consequence F, actual vacua, operator constructions and both quantitative bounds. |
| argument | [Complete argument](#argument) | Sections 1-6, including actual-vacuum necessity, input-weight domain passage, full graph restoration and S-to-A reconstruction. |
| dependency | [Selfadjoint contraction and adjoint interface](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Sections 1-3 provide represented real free difference quotients, specified canonical closures, core adjoint identities and both actual M domains for E and B_h. |
| dependency | [Output kernel-weight estimate](Yin_C_F0136_v1.md#statement) | The affiliated output estimate, core energy identity and analytic-unitary first-derivative approximation used in Sections 4-5. |
| dependency | [Hilbert--Schmidt tensor identification](Yin_C_F0070_v1.md#statement-and-interfaces) | Only the universal unitary tensor identification and its outer-action/vacuum compatibility; no normal-coordinate theorem is imported. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0145_v1.md#conclusion) | Entire fixed statement, all six proof sections and all three dependency interfaces, with exact domain and existential limits. |


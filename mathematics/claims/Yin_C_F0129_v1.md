---
author: Yin
---
# Closed normalized duals under bounded division closure of adjoints

User-directed preparation, 2026-10-14T12:04.
Human author Yin.
The assess_new_reverse agent organized the preceding dialogue's proposed reverse implication into the candidate argument below.
The user requests fixed mathematical materials and comparison updates.
This bounded follow-up does not reopen a completed Task.

Status: **proof draft**.
This is a complete candidate assembled from the listed accepted inputs and the new arguments written here.
No independent review of this complete written candidate has yet occurred, and no existing Claim assessment is changed.
The source and review obligations are stated at the end.

## Question and scope

Let \(M=W^*(X)\) be finite tracial and put \(\mathcal R_X=\operatorname{Div}_M\mathbb C\langle X\rangle\).
The question is whether bare linear dual identities on every bounded vector imply the existence of normalized closed duals with every bounded vector in both actual domains, under the additional assumption \(X_j^*\in\mathcal R_X\).

The bounded division closure and its adjoint-closure hypothesis are already used in [C_F0008, Section 4](Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target).
The new proposed implication concerns operator domains.
It does not follow merely by renaming the normal-tuple assertion in [C_F0069](Yin_C_F0069_v1.md#statement).
The new steps are implementation of the conjugate derivation on all bounded vectors, extension of that automatic-continuity mechanism to a general finite-rank commutator with a diffuse selfadjoint element, and the simultaneous restoration of both Hilbert-space domains.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

### 1. Candidate statement and conventions

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state.
Let \(H=L^2(M,\tau)\), \(\Omega=1\), and let \(P\) be the orthogonal projection onto \(\mathbb C\Omega\).
The inner product is linear in its second variable.
We identify \(a\in M\) with \(a\Omega\in H\), and write \(a\) also for bounded left multiplication by \(a\).
Right multiplication is
\[
 \rho(a)\xi=\xi a\qquad(a\in M,\ \xi\in H).
\]
It is an anti-representation: \(\rho(a)\rho(b)=\rho(ba)\).

Let \(d\geq1\), let \(X=(X_1,\ldots,X_d)\in M^d\) generate \(M\) as a von Neumann algebra, and suppose that complex-linear maps
\[
 D_i:M\Omega\longrightarrow H,
 \qquad [X_j,D_i]=\delta_{ij}P\quad\hbox{on }M\Omega
 \tag{1}
\]
exist.
No continuity, Hilbert-space closability, normalization, or adjoint-domain condition is imposed on these supplied maps.

Define \(\mathcal R_X\) to be the smallest unital complex subalgebra of \(M\) containing the \(X_j\) and closed under taking the inverse of an element whenever that element is invertible **in \(M\)**.
All intermediate expressions lie in \(M\).
In particular this is not the division closure in the affiliated algebra.
Assume
\[
 X_j^*\in\mathcal R_X\qquad(1\leq j\leq d).
 \tag{2}
\]
Put \(A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle\), as a represented unital star algebra in \(M\).

**Candidate conclusion.**
There are densely defined closed operators \(\widehat D_i\) on \(H\) such that
\[
 \begin{split}
 &M\Omega\subseteq\operatorname{Dom}\widehat D_i
                  \cap\operatorname{Dom}\widehat D_i^*,\qquad
   \widehat D_i\Omega=0,\\
 &[X_j,\widehat D_i]=\delta_{ij}P
       \quad\hbox{on }M\Omega.
 \end{split}
 \tag{3}
\]
In fact they can be chosen as
\[
 \widehat D_i=-\overline{E_{i,0}},\qquad
 E_{i,0}=E_i|_{A\Omega},\qquad
 E_i(a\Omega)=-D_i(a\Omega)+aD_i\Omega.
 \tag{4}
\]
Thus the new operators agree with the normalized supplied maps on the star-polynomial core, with the sign in (4).
No equality on all \(M\Omega\), or closability of the supplied maps on that larger domain, is asserted.

The conclusion supplies all four combinations in the motivating question: use either the dense star-polynomial core \(A\Omega\) or the dense invariant subspace \(M\Omega\), and use either actual vacuum-adjoint membership or closability.
The dual relation is the generator relation (1); it does not prescribe independent dual values for the adjoint generators.

## Argument

## 2. Normalization, algebraic derivations and a diffuse selfadjoint element

Write \(B=\mathcal R_X\).
For \(\eta_i=D_i\Omega\in H\), the map \(a\mapsto a\eta_i\) is defined on all \(M\), commutes there with left multiplication, and obeys \(\|a\eta_i\|_2\leq\|a\|\|\eta_i\|_2\).
Hence the maps in (4) satisfy
\[
 E_i\Omega=0,\qquad [E_i,X_j]=\delta_{ij}P
       \quad\hbox{on }M\Omega.
 \tag{5}
\]
This normalization does not assume that right multiplication by \(\eta_i\) is bounded on \(H\).

Condition (2) implies that \(B\) is a star algebra: taking the adjoint of a finite sum, product, or admissible inverse expression produces an expression of the same kind, since \((b^{-1})^*=(b^*)^{-1}\) and invertibility is preserved by the adjoint.
In particular \(A\subseteq B\), and \(B\Omega\) is dense in \(H\).
Every admissible bounded inverse of an element of \(C^*(X)\) remains in \(C^*(X)\), by inverse closure of a unital C*-subalgebra.
Thus
\[
 A\subseteq B\subseteq C^*(X),\qquad
 \overline B^{\|\cdot\|}=C^*(X).
 \tag{6}
\]

For any linear map \(E:M\Omega\to H\), the product and inverse commutator rules are legitimate on the whole stated domain:
\[
 \begin{split}
 [E,ab]&=[E,a]b+a[E,b],\\
 [E,b^{-1}]&=-b^{-1}[E,b]b^{-1}\quad(b\in M^\times).
 \end{split}
 \tag{7}
\]
For the second equality apply the first to \(bb^{-1}=1\).
Both \(b\) and \(b^{-1}\) preserve \(M\Omega\), so no unbounded-operator product outside that domain is involved.

Use the tensor identification
\[
 \Theta(u\otimes v)=uPv,
 \qquad \Theta:H\otimes_2H\longrightarrow\mathcal S_2(H),
 \tag{8}
\]
where \(\mathcal S_2(H)\) denotes the Hilbert space of Hilbert--Schmidt operators.
Its restriction to \(B\otimes_{\mathrm{alg}}B\) is injective, and
\[
 \Theta(a\cdot\eta\cdot b)=a\Theta(\eta)b,
 \quad
 \Theta(\eta^\dagger)=\Theta(\eta)^*,
 \quad
 (u\otimes v)^\dagger=v^*\otimes u^*.
 \tag{9}
\]
The convention in (8) is the one used in [C_F0070, equations (S13)--(S15)](Yin_C_F0070_v1.md#bare-normal-tuples-determine-starred-core-derivations).
Its application here uses bounded rational expressions in place of the normal spectral construction.

Equations (5) and (7), by induction through an expression for \(b\in B\), show that \([E_i,b]\) is the restriction of a finite-rank bounded operator of the form \(\sum_k a_kPc_k\), with \(a_k,c_k\in B\).
This extension is unique because \(M\Omega\) is dense.
It is determined by the represented element \(b\): if an expression represents zero, its commutator on \(M\Omega\) is zero, and the bounded extension is zero.
Therefore
\[
 \delta_i:B\longrightarrow B\otimes_{\mathrm{alg}}B,
 \qquad
 \Theta(\delta_i b)|_{M\Omega}=[E_i,b]
 \tag{10}
\]
is a well-defined outer-bimodule derivation, with
\[
 \delta_iX_j=\delta_{ij}1\otimes1,
 \qquad E_i(b\Omega)=(\operatorname{id}\otimes\tau)\delta_i b.
 \tag{11}
\]
The second equality follows by applying (10) to \(\Omega\).

We next produce a diffuse selfadjoint element of \(B\), independently of any continuity conclusion.
The full-domain finite-rank argument in [C_F0024, Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) gives \(\Delta(X)=d\) from (1).
That section explicitly requires neither normality nor adjoint domains nor continuity; we use only that section, not the normality assumptions of the larger Claim.
The accepted maximal-\(\Delta\)/free-field equivalence in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) and [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004) therefore identifies
\[
 F=\operatorname{Div}_{\mathcal U(M)}\mathbb C\langle X\rangle
 \tag{12}
\]
with the embedded free skew field.
In particular every nonzero element of \(F\) is invertible in \(\mathcal U(M)\), and \(B\subseteq F\cap M\).

No \(X_j\) is scalar, since its commutator with \(D_j\) is the nonzero projection \(P\).
Choose, for example, a nonscalar member \(Y\) of
\[
 \left\{(X_1+X_1^*)/2,\ (X_1-X_1^*)/(2\mathrm i)\right\}.
\]
Then \(Y=Y^*\in B\).
For every real \(\lambda\), the element \(Y-\lambda1\) is nonzero in \(F\) and hence is affiliated-invertible.
Thus its bounded left multiplication on \(H\) has zero kernel.
Equivalently \(1_{\{\lambda\}}(Y)=0\).
The spectral distribution of \(Y\) is nonatomic, and every spectral measure of \(Y\) on \(H\) is nonatomic.
This is a scalar argument; no claim about atomlessness of arbitrary rational matrices is used.

## 3. Automatic continuity with a general Hilbert--Schmidt commutator

**Auxiliary candidate lemma.**
Let \(Y=Y^*\in M\) have nonatomic spectral distribution.
Suppose \(E:M\Omega\to H\) is complex linear and
\[
 [E,Y]=K|_{M\Omega},\qquad K\in\mathcal S_2(H).
 \tag{13}
\]
Then \(E\), viewed as a map from \(M\) with its operator norm to \(H\), is bounded.

This generalizes the triangular proof of [C_F0069, Part A](Yin_C_F0069_v1.md#a-automatic-boundedness), whose stated commutator is \(P\).
The proof below retains the exact accepted [Lau88-U001](../audits/literature/Lau88/Yin_U001.md#lau88-u001) interface and supplies the additional argument for general \(K\).

Let \(\iota:M\to H\) be the continuous inclusion, let \(N=\lambda(Y)\) on \(H\), and let \(T=L_Y\) on the Banach space \((M,\|\cdot\|)\).
On \(\mathcal Y=H\oplus M\) put
\[
 S=\begin{pmatrix}N&K\iota\\0&T\end{pmatrix},
 \qquad J(a)=(E(a\Omega),a).
 \tag{14}
\]
The map \(J\) is initially only algebraic.
Equation (13) says exactly \(SJ=JT\).

### 3.1. The smooth triangular calculus

Left and right multiplication by \(N\) are commuting selfadjoint operators on \(\mathcal S_2(H)\).
Their joint spectral resolution gives the double operator integral
\[
 \Gamma_\phi
 =\iint_{z\ne w}\frac{\phi(z)-\phi(w)}{z-w}
             \,dE_N(z)\,K\,dE_N(w)
 \qquad(\phi\in C^\infty(\mathbb C)).
 \tag{15}
\]
Only the compact real spectrum of \(Y\) is relevant.
The multiplier in (15) is bounded there by a first-derivative seminorm of \(\phi\) on a fixed compact neighborhood.
Consequently \(\Gamma_\phi\in\mathcal S_2(H)\) and
\[
 \|\Gamma_\phi\|_2\leq C_{\phi}\|K\|_2.
 \tag{16}
\]

The joint spectral projection of the diagonal \(z=w\) is zero on \(\mathcal S_2(H)\).
Indeed, for a rank-one tensor its joint scalar spectral measure is the product of two vector spectral measures of \(N\); both are nonatomic, so the diagonal has product measure zero.
Rank-one tensors span a dense subspace of \(\mathcal S_2(H)\), and the joint spectral projection is bounded.
It therefore vanishes on the entire space.
This justifies, for general \(K\), the identities \(\Gamma_1=0\) and \(\Gamma_z=K\); assigning a value to the quotient on the diagonal changes nothing.

The divided-difference product identity gives
\[
 \Gamma_{\phi\psi}=\phi(N)\Gamma_\psi+\Gamma_\phi\psi(N).
 \tag{17}
\]
Define
\[
 \Phi(\phi)=
 \begin{pmatrix}
  \phi(N)&\Gamma_\phi\iota\\
  0&L_{\phi(Y)}
 \end{pmatrix}.
 \tag{18}
\]
Since \(\psi(N)\iota=\iota L_{\psi(Y)}\), (17) proves that \(\Phi\) is a unital algebra homomorphism, \(\Phi(z)=S\), and \(\Phi(1)=I\).
Estimate (16) makes it continuous for the usual smooth-function seminorms on a fixed compact neighborhood.
Thus this is an actual bounded smooth calculus, not a formal commutator expansion.

For completeness, it supplies the super-decomposability used in Lau88.
First \(\sigma(S)=\sigma(Y)\): the block inverse gives the inclusion \(\sigma(S)\subseteq\sigma(Y)\), and approximate eigenvectors of the selfadjoint \(N\), inserted in \(H\oplus\{0\}\), give the reverse inclusion.
Given a two-set open cover \(U_0,U_1\) of this spectrum, choose smooth \(\chi_0,\chi_1\) whose sum is one near \(\sigma(Y)\) and whose compact supports \(K_j\) lie in \(U_j\).
Put \(\mathcal Y_j=\overline{\operatorname{Ran}\Phi(\chi_j)}\).
These are closed \(S\)-invariant subspaces.
The bounded operator \(\Phi(\chi_0)\) commutes with \(S\), has range in \(\mathcal Y_0\), and \(I-\Phi(\chi_0)=\Phi(\chi_1)\) has range in \(\mathcal Y_1\).
If \(\lambda\notin K_j\), choose a smooth \(g\) equal to \((z-\lambda)^{-1}\) near \(K_j\).
Multiplicativity shows that \(\Phi(g)\) preserves \(\mathcal Y_j\) and is a two-sided inverse for \((S-\lambda)|_{\mathcal Y_j}\).
Thus \(\sigma(S|_{\mathcal Y_j})\subseteq K_j\).
This is super-decomposability, hence well-decomposability in the sense of Lau88.
The operator \(T\) is decomposable: spectral projections of \(Y\), acting by left multiplication on \(M\), produce the required closed invariant subspaces for a finite spectral cover.

### 3.2. Divisible subspaces and critical eigenvalues

A linear subspace \(V\) is algebraically \(R\)-divisible if \((R-\lambda)V=V\) for every \(\lambda\in\mathbb C\).
A bounded normal operator \(N\) on a Hilbert space has no nonzero such subspace, by the elementary argument already used in C_F0069.
We include it to make the present hypothesis check complete.

If \(v\) belongs to a divisible subspace, then \(v\in\operatorname{Ran}(N-\lambda)^2\) for every \(\lambda\).
If \(\nu_v\) is its spectral measure, this implies
\[
 I(\lambda)=\int|z-\lambda|^{-4}\,d\nu_v(z)<\infty
       \quad(\lambda\in\mathbb C).
 \tag{19}
\]
Were \(\nu_v\ne0\), some measurable bounded set \(A_n=\{\lambda\in\operatorname{supp}\nu_v:I(\lambda)\leq n\}\) would have positive \(\nu_v\)-measure.
For \(\lambda\in A_n\), \(\nu_v(B(\lambda,r))\leq nr^4\).
A grid covers the bounded set \(A_n\) by \(O(r^{-2})\) discs of radius \(O(r)\), each centered at a point of \(A_n\).
It follows that \(\nu_v(A_n)\leq Cnr^2\) for all sufficiently small \(r\), a contradiction.
Hence \(v=0\).

If \(V\subseteq\mathcal Y\) is \(S\)-divisible, its second-coordinate projection is \(T\)-divisible.
The injective intertwining inclusion \(\iota\) sends that projection to an \(N\)-divisible subspace, so it is zero.
Now \(V\subseteq H\oplus\{0\}\), where divisibility reduces to divisibility for \(N\).
Hence \(V=0\).

The operators \(N\) and \(T\) have no eigenvalues, because \(Y\) has no spectral atoms and the trace is faithful.
The triangular form (14) then shows that \(S\) has no eigenvalues either.
By Lau88 Proposition 3.7, well-decomposability and the absence of divisible subspaces make every algebraic spectral subspace \(E_S(F)\) closed for closed \(F\).
Since \(T\) is decomposable and \(S\) has no eigenvalues, the pair \((S,T)\) has no critical eigenvalues.
Lau88 Theorem 4.1 therefore makes the algebraic intertwiner \(J\) continuous.
Its first component is \(E\).
This proves the auxiliary lemma.

### 3.3. Application to the normalized supplied system

For the \(Y\) constructed in Section 2, (10) makes \([E_i,Y]\) finite rank with bounded coefficients, hence Hilbert--Schmidt.
The auxiliary lemma proves
\[
 C_i:=\|E_i:(M,\|\cdot\|)\to H\|<\infty.
 \tag{20}
\]
This conclusion concerns the supplied normalized maps themselves as Banach-space maps.
No Hilbert-space adjoint or closure is inferred from (20) alone.

## 4. Full-domain implementation of the conjugate derivation

For a derivation \(\delta:B\to B\otimes_{\mathrm{alg}}B\), set
\[
 \delta^\#(b)=\bigl(\delta(b^*)\bigr)^\dagger.
 \tag{21}
\]
Because both involutions are conjugate linear, \(\delta^\#\) is complex linear.
Reversing both the product and the tensor legs in the Leibniz rule shows
\[
 \delta^\#(ab)=\delta^\#(a)\cdot b+a\cdot\delta^\#(b).
 \tag{22}
\]
Moreover \((\delta^\#)^\#=\delta\), and \((c\delta)^\#=\overline c\,\delta^\#\).

Fix \(i\).
Since \(X_j^*\in B\), choose finite decompositions
\[
 \delta_i^\#(X_j)=\sum_k a_{ijk}\otimes b_{ijk},
       \qquad a_{ijk},b_{ijk}\in B.
 \tag{23}
\]
Define on all \(M\Omega\)
\[
 F_i^{\mathrm{raw}}
   =\sum_{j,k}\rho(a_{ijk})E_j\rho(b_{ijk}),
 \qquad
 F_i(a\Omega)=F_i^{\mathrm{raw}}(a\Omega)
                     -aF_i^{\mathrm{raw}}\Omega.
 \tag{24}
\]
These are well-defined: each input right multiplier preserves \(M\Omega\), and each output right multiplier is bounded on \(H\).
For \(a,b\in M\), traciality gives
\[
 \rho(a)P\rho(b)\xi=\tau(\xi b)a
                  =a\tau(b\xi)=aPb\xi
       \qquad(\xi\in H).
 \tag{25}
\]
Here \(\tau(\xi b)=\tau(b\xi)\) is the usual bounded--\(L^2\) trace pairing.
Right multipliers commute with every left \(X_\ell\).
Thus
\[
 [F_i^{\mathrm{raw}},X_\ell]
   =\sum_k\rho(a_{i\ell k})P\rho(b_{i\ell k})
   =\Theta\bigl(\delta_i^\#X_\ell\bigr)
       \quad\hbox{on }M\Omega.
 \tag{26}
\]
The normalization in (24) leaves these commutators unchanged and gives \(F_i\Omega=0\).

Both \(b\mapsto[F_i,b]\) and \(b\mapsto\Theta(\delta_i^\#b)\) satisfy the same product and inverse rules (7) on \(B\).
They agree on every \(X_j\), so induction through an admissible bounded rational expression gives
\[
 [F_i,b]=\Theta(\delta_i^\#b)|_{M\Omega},
 \qquad
 F_i(b\Omega)=(\operatorname{id}\otimes\tau)\delta_i^\#b
       \quad(b\in B).
 \tag{27}
\]
This proves implementation on the entire represented algebra without requiring any formal independence of the adjoint generators.

The full-domain continuity of \(F_i\) already follows from (20) and (24):
\[
 \|F_i^{\mathrm{raw}}(a\Omega)\|_2
 \leq\left(\sum_{j,k}\|a_{ijk}\|C_j\|b_{ijk}\|\right)\|a\|,
\]
and the normalization term has norm at most \(\|a\|\|F_i^{\mathrm{raw}}\Omega\|_2\).
Write
\[
 C_i'=\|F_i:(M,\|\cdot\|)\to H\|<\infty.
 \tag{28}
\]
No second application of automatic continuity is required.

## 5. Realification and actual vacuum vectors

Define
\[
 \begin{array}{ll}
 \alpha_i=(\delta_i+\delta_i^\#)/2,
   &G_i=(E_i+F_i)/2,\\
 \beta_i=(\delta_i-\delta_i^\#)/(2\mathrm i),
   &H_i=(E_i-F_i)/(2\mathrm i).
 \end{array}
 \tag{29}
\]
Both tensor maps are derivations on \(B\).
By the conjugate-linearity rule after (22),
\[
 \alpha_i^\#=\alpha_i,
 \qquad
 \beta_i^\#
   =\frac{\delta_i^\#-\delta_i}{-2\mathrm i}=\beta_i.
 \tag{30}
\]
Thus both derivations are real in the precise dagger convention of C_F0071.
Their right contractions are respectively \(G_i|_B\) and \(H_i|_B\), by (11) and (27), and
\[
 \|G_i:M\to H\|,\ \|H_i:M\to H\|
            \leq (C_i+C_i')/2.
 \tag{31}
\]
All these maps vanish at \(1\).

Apply [C_F0071_v2, Part A and its symmetric-form argument](Yin_C_F0071_v2.md#application-to-a-real-derivation) to each of the real derivations on the dense star algebra \(B\), whose C*-closure is (6).
This gives actual vectors
\[
 \zeta_i^G=\alpha_i^*(1\otimes1),
 \qquad
 \zeta_i^H=\beta_i^*(1\otimes1)
 \tag{32}
\]
and the estimates
\[
 \|\zeta_i^G\|_2\leq2\sqrt2\|G_i:M\to H\|,
 \qquad
 \|\zeta_i^H\|_2\leq2\sqrt2\|H_i:M\to H\|.
 \tag{33}
\]
Reality makes both vectors selfadjoint under the tracial involution.
Indeed the corresponding vacuum functionals are Hermitian, as in that symmetric-form lemma; density of \(B\Omega\) makes their representing vectors selfadjoint.
No coassociativity or pre-existing closability is used.

Since \(\delta_i=\alpha_i+\mathrm i\beta_i\), its actual vacuum vector is
\[
 \xi_i=\delta_i^*(1\otimes1)
           =\zeta_i^G-\mathrm i\zeta_i^H.
 \tag{34}
\]
The minus sign is required by the inner product being linear in its second variable.
Explicitly, for \(b\in B\),
\[
 (\tau\otimes\tau)(\delta_i b)
     =\langle\xi_i,b\Omega\rangle,
 \qquad
 \|\xi_i\|_2\leq2\sqrt2(C_i+C_i').
 \tag{35}
\]

## 6. Core adjoints and restoration of both full domains

All adjoints in this section are Hilbert-space adjoints of explicitly identified core operators.
We do not take the adjoint of a full-domain algebraic map using only pairings tested on \(B\).

For a real derivation \(\alpha\) with right contraction \(G\) and vacuum \(\zeta=\zeta^*\), the exact symmetric-form identity from C_F0071 reads
\[
 \langle Ga,b\rangle+\langle a,Gb\rangle
       =\langle\zeta,a^*b\rangle
       =\langle a,b\zeta\rangle
       \qquad(a,b\in B).
 \tag{36}
\]
The last equality uses traciality and \(\zeta^*=\zeta\).
With \(a\) restricted to \(A\), (36) is an actual adjoint identity for \(G_0=G|_{A\Omega}\):
\[
 B\Omega\subseteq\operatorname{Dom}G_0^*,
 \qquad G_0^*(b\Omega)=b\zeta-G(b\Omega).
 \tag{37}
\]
Apply this to \((G_i,\zeta_i^G)\) and \((H_i,\zeta_i^H)\).
Since \(E_i=G_i+\mathrm iH_i\) and \(F_i=G_i-\mathrm iH_i\), it follows directly by pairing with \(a\in A\) that
\[
 B\Omega\subseteq\operatorname{Dom}E_{i,0}^*,
 \qquad E_{i,0}^*(b\Omega)=b\xi_i-F_i(b\Omega),
 \qquad E_{i,0}=E_i|_{A\Omega}.
 \tag{38}
\]
We need only the inclusion and the displayed values; no assertion that the adjoint of a sum equals a sum on its whole maximal domain is used.
Since \(A\Omega\subseteq B\Omega\) is dense, (38) proves closability of \(E_{i,0}\).
Equations (20), (28), and (38) give the two required estimates on the same polynomial core:
\[
 \begin{split}
 \|E_{i,0}(a\Omega)\|_2&\leq C_i\|a\|,\\
 \|E_{i,0}^*(a\Omega)\|_2
       &\leq(\|\xi_i\|_2+C_i')\|a\|
       \qquad(a\in A).
 \end{split}
 \tag{39}
\]

Put \(\widetilde E_i=\overline{E_{i,0}}\).
Fix \(a\in M\).
Kaplansky density for \(C^*(X)\subset M\), followed by norm approximation inside \(C^*(X)\) by \(A\), supplies a uniformly operator-norm-bounded net \(a_\gamma\in A\) with \(a_\gamma\Omega\to a\Omega\) in \(H\).
The first bound in (39) makes \(E_{i,0}(a_\gamma\Omega)\) weakly relatively compact in \(H\).
A weakly convergent subnet of the graph pairs has limit \((a\Omega,v)\).
The graph of the closed linear operator \(\widetilde E_i\) is a norm-closed linear subspace of \(H\oplus H\), hence weakly closed.
Consequently
\[
 M\Omega\subseteq\operatorname{Dom}\widetilde E_i.
 \tag{40}
\]
Apply the second bound in (39) to the same approximating net.
The operator \(E_{i,0}^*\) is closed.
A weak graph-cluster pair therefore proves
\[
 M\Omega\subseteq\operatorname{Dom}E_{i,0}^*
             =\operatorname{Dom}\widetilde E_i^*.
 \tag{41}
\]
The two subnet arguments need not choose the same subnet; they establish membership in two separately specified closed graphs.
This is the existing graph-restoration mechanism of [C_F0070, Part B](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses), with the additional adjoint estimate supplied explicitly in (39).

Finally the polynomial core is invariant under every left \(X_j\), and (5) holds there.
If \(v\in\operatorname{Dom}\widetilde E_i\), choose \(p_n\in A\Omega\) converging to \(v\) in the graph norm of \(\widetilde E_i\).
Then
\[
 X_jp_n\to X_jv,
 \qquad
 E_{i,0}X_jp_n=X_jE_{i,0}p_n+\delta_{ij}Pp_n
       \longrightarrow X_j\widetilde E_iv+\delta_{ij}Pv.
\]
Closedness proves
\[
 X_j\operatorname{Dom}\widetilde E_i
       \subseteq\operatorname{Dom}\widetilde E_i,
 \qquad [\widetilde E_i,X_j]v=\delta_{ij}Pv.
 \tag{42}
\]
Set \(\widehat D_i=-\widetilde E_i\).
It is closed and densely defined, it vanishes at \(\Omega\), and (40)--(42) give exactly (3), with the generator-first sign of (1).
This completes the candidate proof.

## 7. Exact scope, dependencies and remaining review

The statement covers arbitrary bounded generating tuples satisfying (2), whether or not their coordinates are normal.
It does not settle the reverse question for tuples whose bounded division closure does not contain their adjoints.
Normality alone does not imply (2), as already explained in [C_F0008, Section 4](Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target).
No claim about equivalence with every weaker dense-domain hypothesis is made.

The positive output is existential and specific: the operators in (4) are closures of the supplied normalized maps restricted to the star-polynomial core.
The argument has not proved that the supplied maps on all \(M\Omega\) are Hilbert-space closable, that they equal these closures on all bounded vectors, or that all possible normalized systems coincide.
None of these stronger conclusions is needed for (3).

| Input | Exact use and boundary |
| --- | --- |
| [C_F0008, Section 4](Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target) | The same bounded scalar division closure and adjoint-closure condition; no matrix elimination conclusion is needed. |
| [C_F0024, Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Bare all-bounded-vector dual identities imply maximal Delta; that section explicitly has no normality, closability or adjoint premise. |
| [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002), [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Maximal Delta gives the embedded affiliated free field for arbitrary bounded tuples. Only nonzero scalar elements being affiliated-invertible is used to obtain diffuse Y. |
| [C_F0069, Part A](Yin_C_F0069_v1.md#a-automatic-boundedness) | Proof provenance for triangular automatic continuity and the elementary absence of divisible subspaces. Its rank-one statement is not cited as if it already asserted the general K lemma. |
| [Lau88-U001](../audits/literature/Lau88/Yin_U001.md#lau88-u001) | Accepted Proposition 3.7 and Theorem 4.1, with decomposability, closed algebraic spectral subspaces and absence of critical eigenvalues verified in Section 3. The unit's original-proof inspection limits are retained. |
| [C_F0071_v2, Part A](Yin_C_F0071_v2.md#application-to-a-real-derivation) | Real derivations with bounded right contractions have actual vacuum vectors, with constant 2 sqrt(2); its reality and dense-star-algebra hypotheses are checked in Sections 2 and 5. |
| [C_F0070, Part B](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Provenance for Kaplansky/weak-graph restoration. Section 6 supplies both present bounds and checks both actual graphs; no normal-tuple starred uniqueness is imported. |

No new external theorem is presumed beyond these accepted interfaces and standard tracial Hilbert-space/spectral calculus.
In particular LWZ95 is not a dependency of this written candidate.
Its proposed use in the preceding dialogue is replaced here by the already retained Lau88 input and the explicit general-K extension.
No new external source inspection or full re-audit of an accepted source's predecessor proofs is claimed.

The complete written candidate still requires its own fixed-version mathematical review before a proved assessment is selected.
The review must cover: the general-K double-operator-integral calculus and Laursen interface; the full-domain coefficient implementation (24)--(27), including right-action order; the conjugate-linear realification signs (29)--(35); and the actual core-adjoint/closure interfaces (36)--(42).
Existing reviews of C_F0069 or C_F0071 do not review these new combined steps.
The current author has checked these calculations during preparation, but this authoring activity is not a newly registered independent review.
The general reverse question remains open outside the hypothesis (2).

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T12:12 |
| status | open |
| reason | Complete candidate for the user-requested reverse implication under bounded division closure of all adjoints. The general Hilbert--Schmidt automatic-continuity extension and the combined conjugate-derivation, vacuum and two-domain interfaces still require independent fixed-version review. This is not an adopted theorem or a resolution for arbitrary tuples. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact bounded-division-closure premise and existence of new normalized closed duals with all bounded vectors in both domains. |
| argument | [Argument](#argument) | Sections 2--7, including the general-K auxiliary lemma, implementation, realification, actual core adjoints, graph restoration and review obligations. |
| dependency | [C_F0008 Section 4](Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target) | Bounded division closure containing adjoints and its star closure. |
| dependency | [C_F0024 Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Bare full-domain finite-rank proof of maximal Delta; no normality premise in that section. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal-Delta characterization for bounded tuples. |
| dependency | [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Affiliated free-field embedding used to obtain diffuse Y. |
| dependency | [C_F0069 Part A](Yin_C_F0069_v1.md#a-automatic-boundedness) | Triangular mechanism and no-divisible-subspace argument; the general-K extension is proved as a candidate here. |
| dependency | [Lau88-U001](../audits/literature/Lau88/Yin_U001.md#lau88-u001) | Exact accepted Proposition 3.7 and Theorem 4.1 with their recorded inspection limits. |
| dependency | [C_F0071 Part A](Yin_C_F0071_v2.md#application-to-a-real-derivation) | Actual vacua for real derivations with bounded contractions. |
| dependency | [C_F0070 Part B](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky and weak-graph restoration mechanism, with both estimates supplied here. |

### Decision reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:22 |
| status | proved |
| reason | The complete fixed argument passed a separately organized review of the general Hilbert-Schmidt automatic-continuity extension, conjugate-derivation implementation, actual vacua and both canonical graph domains. This establishes the forward implication from bare full-domain duals to the ACSY24 hypothesis under bounded division closure of the adjoints, without normality. The reverse implication and the unrestricted comparison remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact bounded-division-closure premise and normalized canonical closed duals with all bounded vectors in both domains. |
| argument | [Argument](#argument) | Complete Sections 2--7 and all actual operator-domain interfaces. |
| dependency | [C_F0008 Section 4](Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target) | Bounded division closure containing the adjoints. |
| dependency | [C_F0024 Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Maximal Delta from bare full-domain duals, without normality. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal-Delta characterization for bounded tuples. |
| dependency | [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Affiliated free-field embedding used to construct a diffuse selfadjoint element. |
| dependency | [C_F0069 Part A](Yin_C_F0069_v1.md#a-automatic-boundedness) | Provenance of the triangular continuity and divisible-subspace argument; the general Hilbert-Schmidt extension is proved here. |
| dependency | [Lau88-U001](../audits/literature/Lau88/Yin_U001.md#lau88-u001) | Accepted Proposition 3.7 and Theorem 4.1, with the stated local hypotheses verified. |
| dependency | [C_F0071 Part A](Yin_C_F0071_v2.md#application-to-a-real-derivation) | Actual vacuum vectors for real derivations with bounded contractions. |
| dependency | [C_F0070 Part B](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky and weak-graph mechanism, applied with both bounds proved here. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0136_v1.md#conclusion) | Exact fixed statement and whole argument; source interfaces, checking arrangement and remaining general questions disclosed. |

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:54 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact bounded-division-closure premise and normalized canonical closed duals with all bounded vectors in both domains. |
| argument | [Exact material](#argument) | Complete Sections 2--7 and all actual operator-domain interfaces. |
| dependency | [Exact material](Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target) | Bounded division closure containing the adjoints. |
| dependency | [Exact material](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Maximal Delta from bare full-domain duals, without normality. |
| dependency | [Exact material](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal-Delta characterization for bounded tuples. |
| dependency | [Exact material](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Affiliated free-field embedding used to construct a diffuse selfadjoint element. |
| dependency | [Exact material](Yin_C_F0069_v1.md#a-automatic-boundedness) | Provenance of the triangular continuity and divisible-subspace argument; the general Hilbert-Schmidt extension is proved here. |
| dependency | [Exact material](../audits/literature/Lau88/Yin_U001.md#lau88-u001) | Accepted Proposition 3.7 and Theorem 4.1, with the stated local hypotheses verified. |
| dependency | [Exact material](Yin_C_F0071_v2.md#application-to-a-real-derivation) | Actual vacuum vectors for real derivations with bounded contractions. |
| dependency | [Exact material](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky and weak-graph mechanism, applied with both bounds proved here. |
| review | [Original finding](../audits/reviews/Yin_R_F0136_v1.md#conclusion) | Whole Sections 2–7 under bounded scalar division closure of all adjoints, including general-HS automatic continuity, conjugate implementation, realification, actual core adjoints and both graphs; exact initial-context relationship unknown. |

---
author: Yin
---
# Adjoint tuples, right duals and the missing left-contraction bound

Date: 2026-10-14T13:55.
Human author Yin.
The acsy_rationality_check agent developed the adjoint-tuple reduction and reversal-symmetry application under the explicit request to continue comparing full-domain duals with the ACSY24 derivation condition.
Root checked the proposed conjugation identities before this fixed candidate was prepared.
This is a complete candidate awaiting fixed-material review, not a claim that the general normal-tuple equivalence has been resolved.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

Let \((M,\tau)\) be finite with a faithful normal tracial state, \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
The inner product is linear in its second variable.
Write \(J(a\Omega)=a^*\Omega\), and let \(\lambda(a)\) and \(\rho(a)\) be bounded left and right multiplication.
For a finite bounded generating tuple \(Y=(Y_1,\ldots,Y_d)\), \(d\ge1\), put \(A(Y)=\mathbb C\langle Y,Y^*\rangle\).

The condition \(\mathsf A(Y)\) means that there are outer-bimodule derivations
\[
 \partial_i:A(Y)\longrightarrow H\otimes_2H,\qquad
 \partial_i(Y_j)=\delta_{ij}1\otimes1,\qquad
 1\otimes1\in\operatorname{Dom}\partial_i^*.
\]
The adjoints are actual Hilbert adjoints with core domain \(A(Y)\Omega\).
The condition \(\mathsf F(Y)\) means that complex-linear maps
\[
 D_i:M\Omega\longrightarrow H,\qquad
 [Y_j,D_i]=\delta_{ij}P\quad\hbox{on }M\Omega
\]
exist.
No continuity, closability or adjoint-domain premise is imposed on these supplied maps.

**A. Actual vacua are invariant under adjoint tuples.**
For every bounded generating tuple, normal or not,
\[
 \mathsf A(Y)\ \Longleftrightarrow\ \mathsf A(Y^*).                \tag{1}
\]
Define
\[
 \delta^\#(a)=(\delta(a^*))^\dagger,\qquad
 (u\otimes v)^\dagger=v^*\otimes u^*.                            \tag{2}
\]
If \(\xi=\delta^*(1\otimes1)\), then \((\delta^\#)^*(1\otimes1)=\xi^*\).

**B. Exact reduction for full-domain normal duals.**
Suppose \(X\) is a normal generating tuple and \(\mathsf F(X)\) holds.
Let \(\delta_i\) be the unique starred derivations supplied by [C_F0070 Part A](Yin_C_F0070_v1.md#statement).
Put
\[
 E_i=(\mathrm{id}\otimes\tau)\delta_i,\qquad
 L_i=(\tau\otimes\mathrm{id})\delta_i.                            \tag{3}
\]
Their right contractions \(E_i\) already have bounded extensions from \(M\), with its operator norm, to \(H\).
The following are equivalent:

1. For every \(i\), \(\|L_i(a)\|_2\le C_i'\|a\|\) for \(a\in A(X)\), with a finite constant \(C_i'\).
2. Complex-linear maps \(R_i:M\Omega\to H\) satisfy
   \[
    [R_i,\rho(X_j)]=\delta_{ij}P\quad\hbox{on }M\Omega.            \tag{4}
   \]
3. \(\mathsf F(X^*)\) holds.

If (4) holds, the normalized right dual
\[
 R_i^0(a\Omega)=R_i(a\Omega)-R_i(\Omega)a                         \tag{5}
\]
is bounded \(M\to H\) and restricts to \(L_i\) on \(A(X)\Omega\).
The equivalent conditions imply \(\mathsf A(X)\); the canonical core right contractions for both \(X\) and \(X^*\) have closures whose domains and adjoint domains contain all \(M\Omega\).

No implication from \(\mathsf F(X)\) alone to the three conditions is asserted.

**C. A sufficient reversal symmetry.**
In Part B suppose that a trace-preserving complex-linear star antiautomorphism satisfies
\[
 \sigma:M\to M,\qquad \sigma(X_j)=X_j\quad(1\le j\le d).          \tag{6}
\]
Then the three conditions hold.
Choose normalized full-domain realizations
\[
 E_i(a\Omega)=-D_i(a\Omega)+aD_i(\Omega),\qquad
 C_i=\|E_i:M\to H\|<\infty .
\]
The constant is finite by C_F0069, and
\[
 \|L_i(a)\|_2\le C_i\|a\|,\qquad
 \|\delta_i^*(1\otimes1)\|_2\le4C_i.                             \tag{7}
\]
The two canonical full-domain conclusions in Part B follow.

In particular, Part C applies to every freely independent normal generating tuple satisfying \(\mathsf F(X)\).
This does not assert the existence of full-domain duals for arbitrary free normal laws.

## Argument

### 1. Conjugate derivations and actual adjoints

Tracial conjugation gives
\[
 J\lambda(a)J=\rho(a^*),\qquad J\rho(a)J=\lambda(a^*).            \tag{8}
\]
This is the convention of AP18 Section 7.1.1, inspected in [the existing foundational-reference note](../audits/literature/AP18/Yin_U002.md#ap18-u002).
The displayed identities follow directly on bounded vectors and then by density.

The antiunitary involution \(\dagger\) on the coarse Hilbert space satisfies
\[
 (a\eta b)^\dagger=b^*\eta^\dagger a^*.
\]
The two conjugate-linear operations in (2) make \(\delta^\#\) complex linear.
Applying the Leibniz rule to \(b^*a^*\) and then \(\dagger\) proves
\[
 \delta^\#(ab)=\delta^\#(a)b+a\delta^\#(b).
\]
Thus it is an outer derivation on the same represented star algebra.
A derivation normalized on \(Y_j\) becomes one normalized on \(Y_j^*\).

If \(\xi=\delta^*(1\otimes1)\), put \(\phi(a)=(\tau\otimes\tau)\delta(a)=\tau(\xi^*a)\).
Then
\[
 \begin{split}
 (\tau\otimes\tau)\delta^\#(a)
 &=\overline{\phi(a^*)}
 =\overline{\tau(\xi^*a^*)}\\
 &=\tau(a\xi)=\tau(\xi a)
 =\langle\xi^*,a\Omega\rangle .
 \end{split}                                                   \tag{9}
\]
All pairings of an \(L^2\) vector with a bounded element are legitimate.
Equation (9) is an \(L^2\)-bounded functional on the entire dense core, proving the actual adjoint assertion.
Since \((\delta^\#)^\#=\delta\), Part A follows without normality.

The two contractions satisfy
\[
 E_i^\#(a)=J L_i(Ja),\qquad L_i^\#(a)=J E_i(Ja).                 \tag{10}
\]
These formulas hold first for elementary tensors and then on the Hilbert completion by continuity of the slice maps and conjugations.

### 2. The adjoint tuple is equivalent to the left-contraction bound

For the normal tuple \(X\), C_F0069 makes the normalized supplied full-domain maps bounded \(M\to H\).
C_F0070 Part A supplies the unique Hilbert-valued derivations on the entire starred algebra and identifies their right contractions with those maps on the core.

Assume additionally \(\mathsf F(X^*)\).
The same two Claims applied to the normal tuple \(X^*\) give a unique starred derivation \(\varepsilon_i\) normalized on \(X_j^*\), with bounded right contraction.
The existing \(\delta_i^\#\) has exactly these generator values.
Starred uniqueness in C_F0070 yields \(\varepsilon_i=\delta_i^\#\).
Its bounded right contraction is \(J L_iJ\), so \(L_i\) is bounded for the operator norm.

Conversely, assume the left bounds in Part B(1).
Formula (10) makes both contractions of \(\delta_i^\#\) bounded.
Apply [C_F0072](Yin_C_F0072_v1.md#statement), and let \(N_i\) be the Hilbert closure of its core right contraction.
Then
\[
 M\Omega\subseteq\operatorname{Dom}N_i\cap\operatorname{Dom}N_i^*.
                                                               \tag{11}
\]
On the starred core the Leibniz rule gives
\[
 [N_i,X_j^*]=\delta_{ij}P.                                     \tag{12}
\]
The core is invariant under left \(X_j^*\).
If \(v\in\operatorname{Dom}N_i\), approximate \(v\) by a core sequence in the graph norm.
Equation (12) and boundedness of \(X_j^*\) and \(P\) show that its \(X_j^*\)-images converge in the graph as well.
Closedness gives \(X_j^*v\in\operatorname{Dom}N_i\) and (12) on that domain.
Hence \(D_i'=-N_i|_{M\Omega}\) proves \(\mathsf F(X^*)\).

Applying C_F0072 also to \(\delta_i\) proves \(\mathsf A(X)\) and both full canonical domains.
The application to \(\delta_i^\#\) gives the corresponding conclusions for \(X^*\).
No equality of arbitrary supplied full-domain maps with these closures has been inferred.

### 3. Right-action duals and their normalization

Using (8), a system satisfying (4) gives
\[
 D_i'=-JR_iJ,\qquad
 [X_j^*,D_i']=J[R_i,\rho(X_j)]J=\delta_{ij}P.                    \tag{13}
\]
Conversely, \(R_i=-JD_i'J\) transforms a generator-first system for \(X^*\) into (4).
The domain \(M\Omega\) is preserved by \(J\), and double conjugation gives complex-linear maps.

To identify the core values, put \(G_i=JR_iJ\).
It satisfies \([G_i,X_j^*]=\delta_{ij}P\).
Normalize
\[
 G_i^0(a\Omega)=G_i(a\Omega)-aG_i(\Omega).
\]
C_F0069 gives its operator-norm-to-\(H\) boundedness.
Section 2 identifies its starred-core restriction with \(E_i^\#=J L_iJ\).
Direct conjugation gives
\[
 JG_i^0J(a\Omega)=R_i(a\Omega)-R_i(\Omega)a=R_i^0(a\Omega).
\]
This proves \(R_i^0|_A=L_i\), including boundedness.
The subtracted term in (5) commutes with every right multiplication, so normalization preserves (4).
All three conditions in Part B are now equivalent.

In contrast, direct conjugation of the original right contraction gives
\[
 [JE_iJ,\rho(X_j^*)]=\delta_{ij}P,                              \tag{14}
\]
which is a right-action system for \(X^*\), not (4) for \(X\).
An opposite-algebra relabeling or a single use of \(J\) therefore does not complete the missing estimate.

### 4. Reversal symmetry produces the required right system

Assume (6).
Trace preservation and the antiautomorphism property give
\[
 \|\sigma(a)\|_2^2
 =\tau(\sigma(a)^*\sigma(a))
 =\tau(\sigma(aa^*))=\|a\|_2^2.
\]
Surjectivity extends \(V(a\Omega)=\sigma(a)\Omega\) to a complex-linear unitary on \(H\), fixing \(\Omega\).
A star antiautomorphism preserves the operator norm.
On bounded vectors,
\[
 V\lambda(a)V^{-1}=\rho(\sigma(a)).                             \tag{15}
\]
For the normalized full-domain \(E_i\), define \(R_i=VE_iV^{-1}\).
Since \(\sigma(X_j)=X_j\), these maps satisfy (4), vanish at \(\Omega\), and have the same \(M\)-to-\(H\) norm \(C_i\).
Section 3 gives \(R_i|_A=L_i\).
Consequently both contraction bounds are available with constant \(C_i\); C_F0072 gives \(2(C_i+C_i)=4C_i\) for the actual vacuum and restores both canonical domains.
This proves Part C.

### 5. Word reversal for freely independent normal coordinates

Let the abelian algebras \(B_j=W^*(X_j)\) be freely independent and generate \(M\).
Put \(H_j^\circ=L^2(B_j)\ominus\mathbb C1\).
The pointed free-product Hilbert model identifies
\[
 H=\mathbb C\Omega\oplus
 \bigoplus_{\substack{n\ge1\\i_k\ne i_{k+1}}}
 H_{i_1}^\circ\otimes_2\cdots\otimes_2H_{i_n}^\circ              \tag{16}
\]
through centered reduced products.
This exact inner-product and end-action interface is reconstructed in [Voi98-U005, Free products 5.5-5.8](../audits/literature/Voi98/Yin_U005.md#free-products-55-58) and used on the full polynomial core in [C_F0045 Section 3](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core).
Only that Hilbert model is used here; the further contraction hypotheses or conclusions of C_F0045 are not imported.

Define \(V\Omega=\Omega\) and
\[
 V(\eta_1\otimes\cdots\otimes\eta_n)
   =\eta_n\otimes\cdots\otimes\eta_1.                           \tag{17}
\]
Reversal is a complex-linear isometry from each summand to the reversed-index summand.
Thus \(V\) is a unitary involution.

For \(a\in B_j\), the reduced-word end actions give
\[
 V\lambda(a)V=\rho(a).                                        \tag{18}
\]
The left creation, multiplication and scalar-contraction components become the respective right-end components.
If an end index equals \(j\), reversal changes the internal order; abelianness of \(B_j\) identifies it with right multiplication.
The vacuum obeys the same identity.
Bounded centered factor vectors span the model, so this determines the bounded operators on all \(H\).

Right multiplication is a normal anti-representation of \(M\).
By (18) and generation,
\[
 VMV=W^*(\rho(B_1),\ldots,\rho(B_d))=\rho(M).
\]
Define \(\sigma\) by \(\rho(\sigma(a))=V\lambda(a)V\).
The inverse of \(\rho\) on its image is a complex-linear star anti-isomorphism; hence \(\sigma\) is a complex-linear star antiautomorphism of \(M\).
Equation (18) makes it the identity on each \(B_j\), and therefore on \(X_j\).
Finally,
\[
 \tau(\sigma(a))
 =\langle\Omega,\rho(\sigma(a))\Omega\rangle
 =\langle\Omega,V\lambda(a)V\Omega\rangle
 =\tau(a).
\]
This verifies (6).
Freeness was used only to construct the reversal symmetry.

## Scope and relation to the general question

Part B turns the missing left-contraction bound into an exact existence question for the adjoint tuple.
It does not show that \(\mathsf F(X)\) is invariant under adjoints for arbitrary normal tuples.
Part A cannot supply that inference: it concerns the stronger actual-vacuum condition.

The additional symmetry in Part C is sufficient and is not asserted to follow from normality.
The free-normal application is conditional on \(\mathsf F(X)\).
No arbitrary-normal counterexample, universal finite-Fisher conclusion, novelty claim or general equivalence is asserted.
Normal/singular decompositions of Banach-space maps are not used here.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:55 |
| status | open |
| reason | Complete adjoint-tuple reduction, right-dual identification and trace-reversal application retained for independent fixed-material review. |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A-C, exact equivalence under F(X), actual vacuum conjugation and free-normal application. |
| argument | [Argument](#argument) | Full conjugation, uniqueness, graph extension, right-dual normalization and free-product reversal proof. |
| dependency | [C_F0069 Part A](Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness for full-domain normal duals. |
| dependency | [C_F0070 Part A](Yin_C_F0070_v1.md#statement) | Unique starred Hilbert-valued derivations and normalized right contractions. |
| dependency | [C_F0072](Yin_C_F0072_v1.md#statement) | Two contraction bounds imply actual vacuum and both canonical full domains, also for the conjugate derivation. |
| dependency | [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | The pointed free-product Hilbert model and end actions in Sections 5.5-5.8; the reversal is checked above. |
| dependency | [C_F0045 Section 3](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Existing full-core reduced-word realization only. |
| dependency | [AP18 conjugation interface](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Existing source inspection of tracial J; the left/right identities are checked directly in Section 1. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T14:11 |
| status | proved |
| reason | The complete fixed adjoint-tuple equivalences and reversal-symmetry application passed independent review, including actual vacua, right normalization, graph domains and the free-normal implementation. General adjoint stability of bare normal duals remains unresolved. |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A-C, exact equivalence under F(X), actual vacuum conjugation and free-normal application. |
| argument | [Argument](#argument) | Full conjugation, uniqueness, graph extension, right-dual normalization and free-product reversal proof. |
| dependency | [C_F0069 Part A](Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness for full-domain normal duals. |
| dependency | [C_F0070 Part A](Yin_C_F0070_v1.md#statement) | Unique starred Hilbert-valued derivations and normalized right contractions. |
| dependency | [C_F0072](Yin_C_F0072_v1.md#statement) | Two contraction bounds imply actual vacuum and both canonical full domains, also for the conjugate derivation. |
| dependency | [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | The pointed free-product Hilbert model and end actions in Sections 5.5-5.8; the reversal is checked above. |
| dependency | [C_F0045 Section 3](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Existing full-core reduced-word realization only. |
| dependency | [AP18 conjugation interface](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Existing source inspection of tracial J; the left/right identities are checked directly in Section 1. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0046_v1.md#conclusion) | Exact fixed statement and complete argument, with actual source interfaces, review arrangement and unresolved scope disclosed. |

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:02 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Parts A-C, exact equivalence under F(X), actual vacuum conjugation and free-normal application. |
| argument | [Exact material](#argument) | Full conjugation, uniqueness, graph extension, right-dual normalization and free-product reversal proof. |
| dependency | [Exact material](Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness for full-domain normal duals. |
| dependency | [Exact material](Yin_C_F0070_v1.md#statement) | Unique starred Hilbert-valued derivations and normalized right contractions. |
| dependency | [Exact material](Yin_C_F0072_v1.md#statement) | Two contraction bounds imply actual vacuum and both canonical full domains, also for the conjugate derivation. |
| dependency | [Exact material](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | The pointed free-product Hilbert model and end actions in Sections 5.5-5.8; the reversal is checked above. |
| dependency | [Exact material](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Existing full-core reduced-word realization only. |
| dependency | [Exact material](../audits/literature/AP18/Yin_U002.md#ap18-u002) | Existing source inspection of tracial J; the left/right identities are checked directly in Section 1. |
| review | [Original finding](../audits/reviews/Yin_R_F0046_v1.md#conclusion) | Whole Parts A–C and Sections 1–5: actual-vacuum adjoint invariance, left-bound/right-dual/F(X*) equivalence, normalization, canonical graphs and full free-normal reversal extension; initial-context relationship unknown. |

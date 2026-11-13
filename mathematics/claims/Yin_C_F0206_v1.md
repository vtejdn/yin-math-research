---
author: Yin
---
# Gluing full-domain duals across a central projection in the derivation domain

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) generate a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, and let \(e\) be a central projection with \(0<\tau(e)<1\).
Write \(e_1=e,\ e_2=1-e,\ M_a=e_aM,\ t_a=\tau(e_a),\ \tau_a=\tau|_{M_a}/t_a,\ X_j^a=e_aX_j\).
Use the [definitions of \(\mathsf A,\mathsf F,\mathsf S\)](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) with generator-first commutators.
In each corner these definitions use its unit \(e_a\), its normalized trace \(\tau_a\), and the tuple \(X^a\).

Suppose \(\mathsf A(X)\) holds, and for each coordinate choose an actual ACSY derivation \(\delta_i\) on the represented star polynomial algebra \(\mathcal A\) in \(X,X^*\).
Each \(\delta_i\) is closable as an operator from \(H=L^2(M,\tau)\) to \(H\otimes_2 H\).
If \(e\in\bigcap_i\operatorname{Dom}\overline{\delta_i}\), then
\[
 \mathsf F(X)\ \Longleftrightarrow\ \mathsf F(X^1)\ \text{and}\ \mathsf F(X^2),
 \qquad
 \mathsf S(X)\ \Longleftrightarrow\ \mathsf S(X^1)\ \text{and}\ \mathsf S(X^2).
\]
The two off-diagonal blocks of a glued dual can always be taken Hilbert--Schmidt.
The graph-domain hypothesis holds for every such choice of derivations if \(e\in C^*(X_1,\ldots,X_d)\).

Independently, let two single bounded generators \(X^a\in M_a\) have disjoint compact spectra.
Their direct sum with any two positive trace weights summing to one generates \(M_1\oplus M_2\).
If both components have \(\mathsf A\), their sum has \(\mathsf A\).
For each of \(\mathsf F\) and \(\mathsf S\), their sum has the condition exactly when both components do.
In particular there is a single nonnormal generator whose algebra has a nontrivial central projection and whose actual ACSY, bare full-domain and full operator-and-adjoint domain conditions all hold.

## Argument

### The closed derivation and the central spectral cutoff

Fix one \(\delta=\delta_i\), and use inner products linear in the second variable.
The vacuum functional \(\langle1\otimes1,\delta x\rangle\) is bounded for the \(L^2\) norm of \(x\in\mathcal A\).
For \(a,b\in\mathcal A\), expand \(\delta(a^*xb^*)\) by Leibniz and pair with \(1\otimes1\).
The middle term is \(\langle a\otimes b,\delta x\rangle\).
The full pairing has absolute value at most \(\|\delta^*(1\otimes1)\|_2\|a\|\|b\|\|x\|_2\).
The two remaining terms are bounded by \(\|\delta(a^*)\|_2\|b\|\|x\|_2\) and \(\|\delta(b^*)\|_2\|a\|\|x\|_2\), by transferring the bounded outer multipliers onto the vacuum in each pairing.
Thus \(\mathcal A\otimes_{\rm alg}\mathcal A\subset\operatorname{Dom}\delta^*\), so density gives closability.

If \(e\in C^*(X)\), take a selfadjoint \(b\in\mathcal A\) with \(\|b-e\|<1/4\).
Because \(e\) is central, the spectra of the restrictions of \(b\) on \(e_1,e_2\) lie respectively in \([3/4,5/4]\) and \([-1/4,1/4]\).
Choose a real smooth \(f\) equal to one on the first interval and zero on the second, so \(f(b)=e\).
On an interval containing both spectra choose real polynomials \(q_n\) converging to \(f\) in \(C^1\), by uniform polynomial approximation of \(f'\) followed by integration.
The two outer multipliers \(L_b,R_b\) on the coarse Hilbert space are commuting bounded selfadjoints.
The polynomial Leibniz formula gives
\[
 \delta(q_n(b))=q_n^{[1]}(L_b,R_b)\delta b,
 \qquad q^{[1]}(s,t)=\frac{q(s)-q(t)}{s-t},\quad q^{[1]}(s,s)=q'(s).
\]
The divided differences converge uniformly to \(f^{[1]}\) by the \(C^1\) bound, and \(q_n(b)\to e\) in operator norm.
This gives the required graph approximation for every \(\delta_i\).

### The mixed tensor blocks and the generator-first sign

Work in the inherited Hilbert spaces \(H_a=e_aH\), where \(\|v\|_{H_a}=\sqrt{t_a}\|v\|_{2,\tau_a}\).
For \(v\in H\otimes_2H\) denote by \(v_{ab}\) its projection on \(H_a\otimes_2H_b\).
Fix \(i\), set \(K=\overline{\delta_i}(e)\), and choose \(x_n\in\mathcal A\) converging to \(e\) in its graph.
Thus \(x_n\to e\) in \(L^2\) and \(\delta_i x_n\to K\) in the coarse Hilbert space.
For each \(j\), the inputs \([x_n,X_j]\) converge to zero in \(L^2\).
Their derivatives converge by Leibniz to
\[
 K X_j-X_j K+\delta_{ij}(e\otimes1-1\otimes e).
\]
Here \(X_j\) acts by bounded outer multiplication and \(x_n\otimes1,\ 1\otimes x_n\) converge in the Hilbert tensor norm.
Closability makes this limit zero.
Writing \(s_1=1,\ s_2=0\), we get, for \(a\ne b\),
\[
 X_j^aK_{ab}-K_{ab}X_j^b
   =\delta_{ij}(s_a-s_b)e_a\otimes e_b .
\]
Set \(k_{i,ab}=K_{ab}/(s_a-s_b)\).
In particular these two tensors are \(K_{12}\) and \(-K_{21}\), respectively.

The coarse-to-Hilbert--Schmidt identification is \(\Theta_\tau(u\otimes v)=L_uP_\Omega L_v\) for bounded \(u,v\), with \(P_\Omega h=\tau(h)1\) on \(M\).
Indeed its value at \(h\) is \(u\,\tau(vh)\), the rank-one map with vectors \(u,v^*\), which extends the identification isometrically and intertwines the outer actions with left and right composition by left multiplication.
This is the [coarse Hilbert--Schmidt convention of ACSY24](../audits/literature/ACSY24/Yin_U001.md#canonical-contraction-dual).
Thus \(T_{i,ab}=\Theta_\tau(k_{i,ab}):H_b\to H_a\) is Hilbert--Schmidt and
\[
 L_{X_j^a}T_{i,ab}-T_{i,ab}L_{X_j^b}
 =\delta_{ij}\Theta_\tau(e_a\otimes e_b),\qquad
 \Theta_\tau(e_a\otimes e_b)h=t_b\tau_b(h)e_a .
\]
The positive sign gives \([X_j,D_i]\), and switching to \(E_i=-D_i\) negates all operator blocks.

### Compression and assembly

On \(H_a\), the diagonal block of \(P_\Omega\) sends \(h\mapsto t_a\tau_a(h)e_a\), namely \(t_a\) times the probability-vacuum projection of \(M_a\).
A full-domain witness \(D_i\) thus compresses to the intrinsic corner witness \(D_i^a(v)=t_a^{-1} e_aD_i(v)\) on \(v\in M_a\).
For \(\mathsf S\), restrict the compressed operator to \(M_a\), a dense domain, and test its adjoint against \(h\in M_a\).
In the intrinsic pairing the adjoint value at \(h\) is \(t_a^{-1}e_aD_i^*h\), by the ambient adjoint identity and constant norm rescaling.
These implications from the whole algebra to the corners require no derivation.

Conversely, use \(t_aD_i^a\) on each diagonal and the \(T_{i,ab}\) above off diagonal, on \(M=M_1\oplus M_2\).
Every block has the required generator commutator with the corresponding block of \(P_\Omega\), so the assembled map witnesses \(\mathsf F\).
For \(\mathsf S\), the restricted corner witnesses on the bounded vectors have adjoint domains containing the bounded vectors of their corners.
The direct sum retains this inclusion and adding the two bounded Hilbert--Schmidt blocks preserves it.
This proves the two equivalences.

### Disjoint spectra of single generators

Assume \(X=X^1\oplus X^2\) with disjoint spectra and consider either ordered pair \(a\ne b\).
Use a rectifiable positively oriented contour cycle \(\Gamma_a\) in the common resolvent set with index one on \(\sigma(X^a)\) and zero on \(\sigma(X^b)\).
Such a cycle can be obtained as the oriented boundary of a finite union of small grid squares containing \(\sigma(X^a)\) in its interior and disjoint from \(\sigma(X^b)\).
The integral of \((z-X)^{-1}\) on \(\Gamma_a\), divided by \(2\pi i\), equals \(e_a\) by holomorphic functional calculus.
In particular the generated von Neumann algebra contains both corner units and both generated algebras.
Define
\[
 k_{ab}=\frac1{2\pi i}\int_{\Gamma_a}
      (z-X^a)^{-1}\otimes(z-X^b)^{-1}\,dz
       \quad\text{in }H_a\otimes_2 H_b,
\]
where each resolvent uses its own corner unit.
The integrand is continuous in the tensor norm.
Multiplying by \(X^a\) on the left and subtracting multiplication by \(X^b\) on the right cancels the terms containing \(z\).
The two remaining contour integrals give \(X^a k_{ab}-k_{ab}X^b=e_a\otimes e_b\).
This is the contour formula for the Sylvester equation, also given in [Nevanlinna, Theorem 1.2](https://arxiv.org/pdf/1904.07549).
Using \(\Theta_\tau(k_{ab})\) off diagonal and the preceding diagonal scaling proves the assertions for \(\mathsf F\) and \(\mathsf S\) directly.

Suppose now that intrinsic actual derivations \(\delta^a\) exist in both corners.
For \(w\in\mathcal A\), put \(w_a=e_aw\).
Define the diagonal tensor components by \((\delta w)_{aa}=\delta^a(w_a)\), using the same tensor vectors with their inherited norms.
On the mixed components put \((\delta w)_{ab}=w_a k_{ab}-k_{ab}w_b\).
These prescriptions depend only on the represented entries of \(w\), satisfy the outer product rule, and give \((\delta X)_{ab}=e_a\otimes e_b\) on all four blocks, hence \(\delta X=1\otimes1\).
For the diagonal component the ambient vacuum pairing is \(t_a^2\langle e_a\otimes e_a,\delta^a(w_a)\rangle_{\tau_a\otimes\tau_a}\), bounded by \(t_a^2\|(\delta^a)^*(e_a\otimes e_a)\|_{2,\tau_a}\|w_a\|_{2,\tau_a}\).
For a mixed component, transfer \(w_a,w_b\) in turn onto the mixed vacuum to bound its pairing by
\[
 \|k_{ab}\|_{H_a\otimes H_b}
 \big(\sqrt{t_b}\|w_a\|_{H_a}+\sqrt{t_a}\|w_b\|_{H_b}\big).
\]
All four bounds give a finite constant times \(\|w\|_H\).
The represented star algebra is Hilbert dense since \(X\) generates the direct sum, so this is the actual adjoint-domain condition.

For a concrete example, take two copies of the [circular generator of C_F0074](Yin_C_F0074_v1.md#statement) and use \(X^1=c,\ X^2=c+\lambda1\) with real \(\lambda>2\|c\|\).
The closed disks of radius \(\|c\|\) around \(0,\lambda\) are disjoint and contain the respective spectra.
Translation leaves the star algebra, derivation generator value, vacuum and commutator unchanged.
Both components therefore satisfy \(\mathsf A\) and have bounded whole-Hilbert-space duals.
The construction gives actual \(\mathsf A\) and a bounded whole-Hilbert-space dual for the sum.
The generator satisfies \([X,X^*]=[c,c^*]\oplus[c,c^*]\ne0\), and its generated algebra contains the nontrivial central \(e_1\).

## Provenance and scope

This is a single-generator example and a finite central decomposition argument for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
For general tuples the graph-domain assumption secures simultaneous mixed-block equations for all \(j\), with one operator per ordered pair and coordinate \(i\).
The proof gives no bound on a sum of mixed blocks across infinitely many central projections.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:22 |
| status | open |
| reason | The complete two-corner, separated-spectrum and circular arguments are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two-corner equivalences, the graph condition for central C-star projections, disjoint single spectra and the nonnormal example. |
| argument | [Argument](#argument) | Actual closability, central cutoff, mixed tensors, trace scalings and adjoint domains, contour solutions and vacuum estimates. |
| dependency | [Coarse identification](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The rank-one convention for the isometric Hilbert--Schmidt identification and outer actions. |
| dependency | [Circular generator](Yin_C_F0074_v1.md#statement) | A bounded nonnormal single generator with an actual vacuum and a dual bounded on the whole Hilbert space. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:30 |
| status | proved |
| reason | Adopt the two-corner equivalences, separated-spectrum construction and nonfactor circular example after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two-corner equivalences, the graph condition for central C-star projections, disjoint single spectra and the nonnormal example. |
| argument | [Argument](#argument) | Actual closability, central cutoff, mixed tensors, trace scalings and adjoint domains, contour solutions and vacuum estimates. |
| dependency | [Coarse identification](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The rank-one convention for the isometric Hilbert--Schmidt identification and outer actions. |
| dependency | [Circular generator](Yin_C_F0074_v1.md#statement) | A bounded nonnormal single generator with an actual vacuum and a dual bounded on the whole Hilbert space. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0214_v1.md#finding) | Complete fixed statement and proof, both direct inputs, contour signs, trace normalization and both actual domains. |

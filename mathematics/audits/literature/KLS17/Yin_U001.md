---
author: Yin
---
# KLS17: complete journal-edition audit and the algebraic generation boundary

<a id="kls17-u001"></a>
## Edition, complete scope and principal finding

The source is the [journal edition](readme.md#journal-edition), printed pp. 659--677, PDF pp. 1--19 of the local twenty-page file; PDF p. 20 is the blank journal page 678.
On 2026-11-12 the responsible source reviewer read every article page, including all four sections and the bibliography, and reconstructed the internal implications below.
The rectangular-dimension formula and the complete Theorem 3.7 statement and proof were also inspected in rendered pages.
There is no supplied table of contents to transcribe.
The reviewer had the current A0001 research context but no development context for the source paper and consulted the retained Lin93 audit and current strategy materials for the later applicability comparison.
This is a complete inspection with explicitly retained unresolved steps and accepted external foundations, rather than a claim that every printed implication has been cleared or every cited proof recursively audited.
It is not a new independent review of any project Claim.

The principal usable result is the equivalence between the center-valued conjecture, the specified semisimple Artinian division closure, and finite-subgroup generation of its projective K-theory with that Artinian hypothesis retained.
The argument for these three conditions is reconstructed below without the problematic separate G-theory passage or the density detour.
Theorem 3.7(3) alone leaves the general implication to (4) unresolved.
The [amenable case](../../../claims/Yin_C_A0015_v1.md#amenable-induction) has a separate argument through dimension-flat induction.
Several displayed arithmetic and dimension formulas require the explicit corrections below.
No counterexample to the theorem or to the Atiyah conjecture is asserted.

## Conventions and complete definitions

Let G be a discrete group and let ell be the least common multiple of the orders of its finite subgroups.
The paper's nonvacuous assertions assume ell finite.
The canonical scalar trace is tau and all matrix traces are unnormalized, so the dimension of the free module of rank n is n, rather than one.
Unless the subring version is expressly mentioned, K is a subfield of the complex numbers closed under complex conjugation.

### Center-valued trace and dimension

Definition 2.1, p. 664, uses the unique normalized positive center-valued trace
\[
 T_G:\mathcal N(G)\longrightarrow Z(\mathcal N(G)),
 \qquad T_G(ab)=T_G(ba),\quad T_G(c)=c\ (c\in Z(\mathcal N(G))).
\]
The matrix extension is \(T_{G,n}((a_{ij}))=\sum_iT_G(a_{ii})\).
For a closed invariant subspace V with orthogonal projection p, its center-valued dimension is \(\dim_G^u V=T_{G,n}(p)\).
The scalar dimension is \(\tau(T_{G,n}(p))\).
The existence, uniqueness, normality and projective-module comparison theorem are accepted finite-von-Neumann-algebra foundations; see also the [retained comparison input](../MSY23/Yin_U004.md#ambient-algebra-domains-and-foundational-inputs).
They do not assert that a kernel projection lies in a group ring or its division closure.

### Finite conjugacy center and finite normal subgroup

Definition 1.9, p. 662, writes \(\Delta(G)\) for the subgroup of elements with finite conjugacy class.
Its torsion subgroup \(\Delta^+(G)\) is, under the bounded-order hypothesis, the largest finite normal subgroup of G.
The paper uses Passman's group-ring facts for these subgroup assertions; their original proofs are accepted, not re-audited here.
An element of the center of \(\mathcal N(G)\), viewed in \(\ell^2(G)\), has constant coefficients on conjugacy classes and zero coefficients on infinite conjugacy classes.
Consequently a center-valued trace of a finite-support element supported on torsion is supported on \(\Delta^+(G)\).
Torsion-freeness makes \(\Delta^+(G)=1\); it does not make \(Z(\mathcal N(G))\) trivial or make \(\Delta(G)=1\).

### The permitted trace lattice and the conjecture

For a subring K with conjugation-closed fraction field F, Definition 1.2, p. 661, defines
\[
 L_K(G)=\left\langle T_G(p):p=p^*=p^2\in F[H],\ H\le G\text{ finite}\right\rangle_{\mathbb Z}.
\]
The center-valued Atiyah conjecture requires \(T_{G,n}(p_{\ker A})\in L_K(G)\) for every square matrix over K[G].
Rectangular matrices are covered by zero padding with the appropriate integer free-module correction.
Passing between K and F uses clearing finitely many scalar denominators; the explanatory implication labels on p. 661 are reversed, but the denominator argument is valid.
For a finite H, closure of K under conjugation keeps the projection onto a matrix kernel in a matrix ring over K[H].
This follows from the spectral projection at zero being a polynomial over K in the finite-dimensional positive matrix \(A^*A\).
Matrix projections over a semisimple finite-group algebra split into scalar minimal ideals, so Definition 1.2's scalar finite-subgroup generators suffice for their traces.
Proposition 1.3 follows by applying tau: finite-group projection traces lie in \(\ell^{-1}\mathbb Z\).

### Actual division closure and central-idempotent extension

Definition 1.6 uses the actual inclusion \(K[G]\subset\mathcal U(G)\), with affiliated sums and products understood as the closed ring operations.
The division closure D is the smallest subring containing K[G] and closed under inverses that exist in \(\mathcal U(G)\).
It is not defined to be a division ring, a regular ring or the ring containing all kernel projections.
The source's scalar closure and the [general actual-closure convention](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) agree at this instance.

For \(R\subset S\), Definition 2.2, p. 665, adjoins central idempotents e of S satisfying \(eS=rS\) for some r in R, forms the ring \(C(R,S)=\sum_e eR\), and alternates this operation with division closure.
Starting with \(E_0=R\), put \(E_{\alpha+1}=\operatorname{Div}_S(C(E_\alpha,S))\) and take unions at limit ordinals.
The stable union is E(R,S); in the paper R=K[G], S=\(\mathcal U(G)\).
Only central idempotents with the indicated principal-ideal witness are adjoined.
Arbitrary noncentral kernel projections are not included by this definition.
Conjecture 2.3, D=E under the bounded-order hypothesis, is an unresolved general assertion in the source; Theorem 1.10 proves it under the center-valued conjecture.

## Finite blocks, Galois descent and the lattice denominator

Lemmas 3.1--3.3, pp. 667--668, first split K[Delta-plus] after adjoining the required roots of unity, then descend by the finite Galois action.
Primitive central projections of the finite group algebra are permuted by conjugation in G.
Sums over the conjugation orbits, followed by the Galois orbit grouping, give the primitive projections
\[
 P_1,\ldots,P_c\quad\text{of}\quad
 Z(\mathcal N(G))\cap K[\Delta^+(G)].
\]
The character formula, orthogonality, uniqueness of the containing block and invariance of the identity coefficient under Galois automorphisms were checked.
The identity coefficient of a finite-group idempotent is its complex regular-representation rank divided by the group order, hence rational; this supplies the rationality used in Lemma 3.2 without assuming a Galois automorphism preserves arbitrary complex inner products.
Maschke semisimplicity, the character-idempotent formula and ordinary Galois descent are accepted established inputs, with their use reconstructed here rather than their textbook proofs audited.

For finite \(H\supset\Delta^+(G)\) and an irreducible projection Q in K[H], Lemma 3.4 gives the exact formula
\[
 T_G(Q)=q_Q P_j,\qquad
 q_Q=\frac{\dim_{\mathbb C}(Q\mathbb C[H])\,m}{|H|\,d_j},
 \quad m=|\Delta^+(G)|,\quad
 d_j=\dim_{\mathbb C}(P_j\mathbb C[\Delta^+(G)]),
\tag{1}
\]
where QP_j=Q.
The proof projects coefficients onto the conjugacy-invariant part supported on Delta-plus.
Galois transitivity makes the coefficients equal inside each descended block, and the identity coefficient computes their common value.
This checks both the numerator m and the division by d_j, including the unnormalized matrix convention.

The first line of p. 670 claims that these coefficients are all integer multiples of \(1/\ell\).
That stronger denominator assertion does not follow from (1); the factor d_j cannot simply be discarded.
A sufficient corrected bound is
\[
 q_Q\in\frac1{\ell d_j}\mathbb Z,
\tag{2}
\]
because \(\ell/|H|\) is an integer.
This proves Corollary 3.5's actual conclusion: the entire trace group lies in a fixed discrete lattice in the finite-dimensional span of the P_j.
No stronger universal \(1/\ell\) coefficient statement is used here.

### Atiyah-expected Artinian structure

For each j, let L_j be the smallest positive integer for which every coefficient q_Q in that block belongs to \(L_j^{-1}\mathbb Z\).
The coefficients form a finite set, by their bounded integer numerators and denominators in (1).
They generate exactly \(L_j^{-1}\mathbb Z\), because the irreducible summands of P_j in K[Delta-plus] already have coefficient sum one.
Equivalently, with \(b_j=\ell d_j\) and \(a_Q=\dim_{\mathbb C}(Q\mathbb C[H])\,m\ell/|H|\),
\[
 L_j=\frac{b_j}{\gcd(b_j,(a_Q)_Q)},\qquad
 L_K(G)=\bigoplus_j\frac1{L_j}\mathbb ZP_j.
\tag{3}
\]
This reproduces Definition 3.6's least-common-denominator formula, with integral quantities throughout.
Its term *Atiyah-expected Artinian* means that D is semisimple Artinian, its primitive central idempotents are precisely the P_j, and \(P_jD\cong M_{L_j}(F_j)\) for skew fields F_j.
Finite dimension of F_j over its center is not part of this definition.

## Rank-group preservation and Theorem 1.10

Lemma 2.4, p. 666, asserts equality of the additive groups generated by center-valued image dimensions of all finite matrices over K[G] and over E.
The underlying scalar proof was compared with LS12, Lemmas 2.1--2.4, journal pp. 317--318.
For a central e with \(eU=xU\), the new matrix \(\beta+e\gamma\) splits into its e and 1-e parts.
The dimension of \(\beta eU^n\) equals that of \(\beta(xI_n)U^n\), so subtraction expresses the new rank using old ranks.
The division step uses a finite stabilization and invertible row and column operations over U; its identity block contributes an integer multiple of the central identity.
These operations preserve center-valued dimensions as well as scalar dimensions.
A finite matrix over a union of stages occurs before any limit stage at which it first appears.
Transfinite induction therefore proves the stated equality, using the accepted finite linearization theorem; no Ore condition on K[G] or inverse for a singular input is assumed.

Under the center-valued conjecture every such dimension lies in L_K(G).
If e is an idempotent in E which is central in U, then e is a bounded central projection, and its image dimension is e itself.
The lattice support calculation gives \(e\in K[\Delta^+(G)]\subset K[G]\).
Thus every central idempotent that the transfinite construction can adjoin is already in K[G]; induction on the construction leaves E inside D.
The opposite inclusion is definitional, proving Theorem 1.10.
The printed proof stops after locating e in K[Delta-plus]; this final construction argument is needed to make its conclusion explicit.
Remark 2.5 correctly notes that finite torsion support of the dimensions suffices for this step; it does not derive that support from torsion-freeness alone.

## Theorem 3.7: three verified formulations and the unresolved G-theory branch

Theorem 3.7, pp. 670--672, states four equivalent conditions: expected Artinian structure; semisimple Artinian D with surjectivity from finite-subgroup K_0; surjectivity from finite-subgroup G_0 without an explicit Artinian assumption; and the center-valued conjecture.
Here K_0 uses finitely generated projectives with direct-sum relations, while the printed G_0 uses arbitrary finitely generated modules and short-exact-sequence relations.
These are distinct constructions before semisimplicity has been established.

### The projective formulation with its full hypothesis

Write
\[
 \Phi_K:\bigoplus_{H\le G,\ |H|<\infty}K_0(K[H])\longrightarrow K_0(D)
\]
for induction of projective modules along the actual inclusions.
Condition (2) is **D semisimple Artinian and Phi_K surjective**, not just a statement about K_0(K[G]) or scalar traces.
In a matrix block the class of a minimal right ideal generates its K_0, and [P_jD] is L_j times that generator.
The finite-subgroup ideal classes have coefficients L_j q_Q; their gcd is one by (3).
Bezout's identity therefore proves (1) implies (2).
This interprets the source's rational notation in integral K_0 and supplies the precise arithmetic behind its Chinese-remainder wording.

Conversely, under (2), a finite K[G]-presentation has a finitely generated projective cokernel after tensoring with D, because D is semisimple.
Its K_0 class is a signed sum of induced finite-subgroup projectives.
Tensoring these projective decompositions and stable isomorphisms with U preserves them; no flatness assertion about arbitrary D-modules is required.
The induced U-dimension is therefore in L_K(G).
For \(A:U^l\to U^n\), the correct relation is
\[
 \dim_G^u\operatorname{coker}A=n-l+\dim_G^u\ker A,
 \qquad
 \dim_G^u\ker A=l-n+\dim_G^u\operatorname{coker}A.
\tag{4}
\]
The formula on p. 665 is incorrect, and p. 671's last line of the (3)-to-(4) argument has the same image/kernel confusion.
Even for a square matrix its cokernel dimension equals its kernel dimension.
Formula (4), and the fact that integer multiples of one belong to L_K(G), complete the valid implication (2) to (4).

### Recovering the specified blocks without the density detour

Assume (4).
Theorem 1.10 gives D=E, and taking the scalar trace of the finite lattice (3) gives one common denominator for all matrix ranks over K[G].
The applicable input is LS12, Theorem 2.7, journal pp. 319--321: this rank-denominator hypothesis makes E semisimple Artinian.
Its exact primary statement and its minimal-rank and maximal-conjugate-span mechanism were inspected; its general affiliated and ring-theoretic foundations remain accepted inputs.
Consequently D is semisimple Artinian.

The division closure is star closed.
A central idempotent c of D commutes with its adjoint, so it is a normal affiliated idempotent and therefore a bounded orthogonal projection.
It commutes with every group unit, hence lies in the center of N(G).
Lemma 2.4 and (4) then put c in K[Delta-plus].
The P_j are already primitive in the central algebra \(Z(\mathcal N(G))\cap K[\Delta^+(G)]\), so they are precisely the primitive central idempotents of D.

Put \(P_jD=M_{r_j}(F_j)\) and choose a minimal idempotent f in that block.
The r_j isomorphic minimal ideals sum to P_jD, so induction to U gives \(\dim_G^u(fU)=P_j/r_j\).
Lemma 2.4 and (3) imply \(r_j\mid L_j\).
Each finite-subgroup Q in this block is an integral sum of minimal D-ideals, so \(q_Q\in r_j^{-1}\mathbb Z\); minimality of L_j gives \(L_j\mid r_j\).
Thus r_j=L_j, proving (4) to (1) directly from the preceding source results and elementary semisimple module structure.
This reconstruction verifies the (1), (2), (4) equivalence and Theorem 1.8 without using condition (3).

The printed final arithmetic on p. 672 must also be corrected if its longer route is followed.
From \(n_\alpha T_G(c)\in\mathbb ZP_j\) for every alpha and \(\gcd_\alpha n_\alpha=1\), Bezout gives \(T_G(c)\in\mathbb ZP_j\); lcm cannot replace gcd.
The final minimal-ideal dimension gives \(r_j\mid L_j\), while the finite-subgroup decomposition gives the opposite divisibility.
The source prints the same divisibility twice and also prints an lcm equal to one where the defined gcd is one.

### Why condition (3) has not been cleared

Journal p. 671 and [arXiv v2, Theorem 3.9, p. 15](https://arxiv.org/pdf/1605.09069v2#page=15) both pass directly from (3) to a stable module isomorphism.
Condition (3) expresses the class of the induced cokernel as a finite signed sum in the quotient by all finitely generated short-exact-sequence relations.
An equality in the group completion for direct sums would allow a common stabilizing summand after moving negative terms across the equality.
The additional exact-sequence relations in \(G_0(D)\) need not yield any such isomorphism.
Semisimplicity of each finite-subgroup algebra makes induction *from that algebra* exact but gives no exactness for induction *from \(D\)*.
Condition (2) separately implies (3) because the target in (2) is semisimple Artinian.

For right modules let \(F=-\otimes_D U\) and \(0\to X'\xrightarrow{i}X\to X''\to0\) be a short exact sequence witnessing a class relation.
The left-hand defect is
\[
 E_i=\ker F(i)=\operatorname{im}\bigl(\operatorname{Tor}_1^D(X'',U)\longrightarrow F(X')\bigr).
\]
It can be smaller than the entire first Tor since the connecting map can have a kernel.
The [central-cut dimension calculation](../../../claims/Yin_C_A0015_v1.md#applying-an-exact-sequence-class-relation) shows exactly how this image contributes to the defect of additivity.
All modules in a witness are finitely generated, but only the initial matrix cokernel and the induced finite projectives are known to be finitely presented.
More precisely, let \(C=\operatorname{coker} A_D\) and \(P_j^D\) be the finite-subgroup projectives induced to \(D\).
In the free abelian group on isomorphism classes a witness for (3) has the form
\[
 [C]-\sum_j a_j[P_j^D]
    =\sum_s m_s\bigl([X_s]-[X'_s]-[X''_s]\bigr).
\]
For each constituent sequence there is a bounded positive central element \(e_s\) determined by \(\tau(ze_s)=\dim_U(E_{i_s}z)\) for all central projections \(z\).
Indeed, these cuts form a finitely additive measure bounded by \(k_s\tau(z)\) when \(X'_s\) has \(k_s\) generators, so normality and a bounded Radon–Nikodym density follow on the abelian center.
Applying the cut calculation to the displayed witness gives
\[
 \dim_G^u F(C)-\sum_j a_j\dim_G^u F(P_j^D)=-\sum_s m_s e_s.
\]
For this matrix it is therefore necessary and sufficient that the signed defect sum lie in \(L_K(G)\), since the finite-projective contributions and the rectangular rank correction already lie there.
A stronger sufficient hypothesis is zero scalar dimension of each such image.
Requiring this for every finitely generated short exact sequence is equivalent to the [matrix test](../../../claims/Yin_C_A0015_v1.md#matrix-test-for-the-left-hand-defect) that the \(U\)-span of the \(D\)-kernel of every finite \(D\)-matrix exhausts its \(U\)-kernel up to dimension zero.
Conversely, [the separate argument from (4) to (1)](#recovering-the-specified-blocks-without-the-density-detour) gives a semisimple Artinian \(D\), over which \(U\) is flat, so (4) implies the matrix test.
Hence, on groups satisfying (3), the matrix test and (4) are equivalent.
The missing general implication can be stated precisely as the assertion that (3) forces this test in the regular representation.

For amenable \(G\), the [conditional repair](../../../claims/Yin_C_A0015_v1.md#statement) obtains this zero defect by restricting modules to \(K[G]\), applying Lück's dimension-flatness theorem and checking the extra \(D\)-balancing relations after extension to \(U\).
It gives (3) implying (4) for every conjugation-closed coefficient field in the theorem when \(G\) is amenable.
Separately, if the actual \(D\) is known to be von Neumann regular, every left \(D\)-module is flat and the same dimension argument applies.
Using the \(*\)-regular closure would require a comparison with (3), which concerns \(G_0(D)\).
For example, [SP25, Definition 2.9 and the following paragraph](https://doi.org/10.1007/s00039-025-00710-4) uses \(K_0\) of the \(*\)-regular closure and projectivity of finitely presented modules over that ring.
The general case with only the hypotheses printed in (3) remains unresolved in this audit.

#### A faithful representation detecting both failed formal steps

Take \(G=\mathbb Z\), \(R=\mathbb C[t,t^{-1}]\), and represent \(t\) as the coordinate function on the unit circle with measure \(\mu=(m+\delta_1)/2\), where \(m\) is Haar probability measure.
This gives a faithful algebra embedding and the finite tracial algebra it generates has affiliated ring \(W=L^0(\mathbb T,\mu)\).
A nonzero Laurent polynomial is invertible in \(W\) exactly when its value at the atom \(1\) is nonzero, since its Haar zero set is finite.
The actual scalar division closure for this embedding is the discrete valuation ring \(D'=R_{(t-1)}\), since every such fraction is obtained using an ambient unit and a fraction in this ring is an ambient unit exactly when its numerator is nonzero at \(1\).
Put \(\pi=t-1\) and \(k=D'/\pi D'\).
The exact sequence \(0\to D'\xrightarrow{\pi}D'\to k\to0\) gives \([k]=0\).
All finitely generated modules over this principal ideal domain are sums of a free module and cyclic torsion modules, and the same exact sequence with \(\pi^j\) kills each torsion class.
The fraction-field rank detects the remaining free class, so \(G_0(\mathbb C)\to G_0(D')\cong\mathbb Z\) is an isomorphism.
Yet \(k\oplus X\cong X\) is impossible for a finitely generated \(X\), as reduction modulo \(\pi\) would give two finite-dimensional vector spaces whose dimensions differ by one.
After tensoring with \(W\), both the kernel and cokernel of multiplication by \(\pi\) are \(1_{\{1\}}W\), of scalar dimension \(1/2\).
Thus the zero class can have an induced cokernel of positive nonintegral dimension even for an inverse-closed domain and a one-entry matrix.
The regular representation of \(\mathbb Z\) has Haar spectral measure, under which \(t-1\) is invertible in the affiliated ring.
This verifies the failure of the formal inference and leaves the KLS17 assertion for regular representations open at the indicated scope.
In the actual group setting the same diagnostic has a precise conditional form.
If multiplication by \(a\in D\) is injective on \(D\), then the exact sequence of \(D\)-modules already gives \([D/aD]=0\), independently of (3).
Whether its induced scalar kernel vanishes is precisely the extra analytic question for that sequence.

### Density, quantization and the coefficient-field boundary

The source's alternative construction of the direct sum in equation (3), p. 672, imports LS12's density argument.
The decisive source input is a strong-convergence kernel estimate, followed by a fixed discrete rank lattice, which changes a sufficiently small defect into exactly zero.
LS12's journal Lemma 2.13, pp. 322--323, supplies that convergence assertion; its Lemma 2.12 is only the preceding trace inequality, so KLS17's numbering mixes the earlier numbering with the journal citation.
The convergence estimate itself was checked by its spectral cut and trace argument and requires no spectral gap of the limit.
For K=complex numbers, bounded strong-star approximation of the finitely many ambient bounded operators is available and the quantization step applies.
For a general conjugation-closed real subfield, bare Kaplansky density does not make K[G] strongly dense in the complex N(G); an additional real-form or coefficient-extension argument would be needed for that literal approximation step.
The direct semisimple reconstruction above avoids that step for the verified equivalence, so it is not treated as a premise supplied by an unproved density assertion.

## Section 4: inheritance and the approximation interface

### Directed unions, virtually free groups and elementary amenable quotients

Definition 2.7 specifies Linnell's class C as generated from free groups by directed unions and extensions with elementary amenable quotient.
Lemma 4.1 uses the virtually free Artinian and finite-subgroup projective induction arguments of Lin93; Lemma 4.2 passes finite matrix coefficients through a directed union.
For the latter, subgroup-coset decomposition gives the actual affiliated inclusion, and composing the ambient center-valued trace with the subgroup one gives the correct induced dimension.
Finite-subgroup generators remain finite-subgroup generators after induction.
The [complete Lin93 inspection](../Lin93/Yin_U001.md#routine-lemmas-and-induction) supplies the retained Artinian and K_0 induction scope, including the separate free-field boundary.
These arguments are not scalar Ore localization and do not assume that all torsion-free groups belong to class C.

Proposition 4.3 assumes that **every** inverse image of a finite subgroup of the elementary amenable quotient satisfies the center-valued conjecture.
It uses transfinite reduction, a virtually abelian crossed product and Moody's induction theorem.
Moody's original Theorem 1 has a Noetherian graded-ring setting, virtually polycyclic grading group and units in every degree; its first-page statement was inspected, not its fourteen-page proof.
The ring and localization interfaces are substantive hypotheses, not induction available for an arbitrary torsion-free group.
As printed, Proposition 4.3 concludes through Theorem 3.7(3), so that proof needs the G-theory interface just identified for its actual target group.
The amenable repair applies if the total group is amenable, while the elementary amenability of the quotient alone does not establish its dimension-flatness premise.
In the already Artinian Lin93 class-C setting, one can instead use the projective formulation (2); this does not rely on the unresolved general G_0 shortcut.
Theorem 4.5 follows the cited class-C hierarchy at that retained scope; no new group class is inferred here.
For a finite quotient, the finite subgroup equal to the whole quotient occurs among the hypotheses of Proposition 4.3, whose inverse image is G itself.
The proposition therefore does not establish arbitrary finite-extension permanence from the kernel alone.

### Precise coefficient approximation and finite-subgroup lifting

Theorem 2.6 and Proposition 4.4 use algebraic coefficients, \(K\subset\overline{\mathbb Q}\), not arbitrary complex coefficients.
The external input is Kne11, Theorem 3.2: for a descending normal chain with trivial intersection and the specified determinant-bound hypotheses, the Fourier coefficients of kernel center-valued dimensions converge at each element of the finite conjugacy center.
Its arXiv v2 statement and relevant inverse-system setup were inspected; its determinant estimates and entire proof were not audited.
For a nonsquare or nonpositive input, use a positive square \(A^*A\) and zero padding without changing the kernel being measured.
No norm convergence of kernel projections is asserted.

Proposition 4.4 adds that every finite subgroup of each quotient lifts isomorphically to a finite subgroup of G.
Choose a finite subgroup M of maximal order in G.
Its finite core is Delta-plus; finitely many conjugates suffice to compute that core.
Eventual injectivity on their finite union, together with the lifting condition and maximality, identifies Delta-plus of G with Delta-plus of every sufficiently late quotient.
This verifies the finite-core stabilization argument on pp. 673--674.
An infinite-order element has infinite-order image eventually, because injectivity on its first ell+1 powers rules out all possible finite image orders.
For Fourier coefficients outside the finite conjugacy center no approximation theorem is needed: a central square-summable vector already has zero coefficients there.
Thus the printed application of Theorem 2.6 to infinite-order g needs only g in Delta(G), exactly where that theorem applies.

Write \(T_i=T_{G/G_i}(p_{\ker A[i]})\), rather than the printed trace of a quotient projection in the original group algebra.
The approximation and core identification make the remaining finitely many coefficients converge in one fixed finite-dimensional space.
For the final membership conclusion, it suffices that the quotient lattice pull back into L_K(G); the printed assertion of exact identification of every relevant finite-subgroup representation is stronger than necessary.
That needed inclusion can be checked as follows.
Enlarge a finite subgroup F of a late quotient to contain its Delta-plus and take an isomorphic finite lift F-prime.
Then \(H=F'\Delta^+(G)\) is finite, maps onto F, and has finite normal kernel N under this map.
Inflate a projection Q in K[F] to the N-invariant summand of K[H], by averaging over N, to obtain a projection \(\widetilde Q\).
Its coefficient at \(\delta\in\Delta^+(G)\) is the coefficient of Q at its image divided by |N|.
The conjugacy actions on the identified finite normal subgroups agree, so
\[
 T_{G/G_i}(Q)=|N|\,\pi_i(T_G(\widetilde Q)).
\tag{5}
\]
Both center traces have support in the respective Delta-plus.
The equality proves the required inclusion of additive lattices and avoids an unsupported identification of individual lifted irreducible representations.
Discreteness then places the limit in L_K(G).
This reconstruction does not assert the stronger equality of lattices from the printed short explanation.

If G is torsion free, the lifting hypothesis forces every quotient in this proposition to be torsion free: an isomorphic finite lift would otherwise be a nontrivial finite subgroup of G.
It is not a device for extracting integrality from finite quotients with growing denominators.
The determinant-bound premise, algebraic coefficient restriction and lifting premise remain separate.
Theorem 4.6 and Theorem 1.11(2) additionally import the cited residual constructions, goodness and geometric results for the listed braid, Artin, link and special groups and products.
Those original proofs were not re-audited, and their stated conclusion is not enlarged to all torsion-free amenable groups or to all complex coefficients.
Question 1.12 is a source-era comparison about congruence groups; it is not adopted as a claim about the current frontier.

## Exact torsion-free use and remaining research obligations

For torsion-free G, Delta-plus is trivial, the finite-subgroup trace lattice is \(\mathbb Z1\), there is one P_j and L_j=1.
The verified projective criterion therefore specializes to
\[
 D\text{ a division ring}
 \quad\Longleftrightarrow\quad
 D\text{ semisimple Artinian and }
 K_0(\mathbb C)\longrightarrow K_0(D)\text{ surjective},
\tag{6}
\]
with the actual complex group-ring inclusion understood.
This is a specialization of the known criterion, not a new proof of either side for an unknown group.
It does not follow from integer trace on K_0(K[G]), integer trace on C*-projections, finite-support density of kernels, or formal adjunction of kernel projections.
The Artinian and generation assertions must be obtained independently for the actual closure or for a rigorously kernel-equivalent smaller object.
The scalar amenable principal-annihilator and coefficient-mass obligations in the current routes are not discharged by the paper.

The rank-density construction uses already established quantization before it certifies exact units and direct sums.
Using it to establish that same quantization without another structural input would be circular.
The trace lattice describes admissible values of actual algebraic projectives; a finite-window limit or an expected-kernel support does not automatically create the needed projective class.
Semisimple Artinian structure allows skew fields of infinite central dimension, so the [faithful central-finite obstruction](../../../ledger/Yin_L_A0029_v1.md#a-faithful-central-finite-model-forces-virtual-abelianness) does not exclude this different ring-theoretic target.
However, replacing the division assertion by the pair in (6) supplies an interface and a useful separation of obligations, not independent progress on the full Task.

## Accepted sources, unresolved interface and inspection limits

The external inputs are finite-von-Neumann and affiliated-operator foundations; finite-dimensional character theory and Galois descent; LS12's rank-linearization and Artinian theorem; the exact Lin93 induction interfaces; Kne11's coefficient approximation; Moody's stated induction theorem; and the residual and geometric source results explicitly identified by KLS17.
LS12 journal numbering was checked against its original pp. 317--324, with its preprint compared only where needed for the numbering discrepancy.
The publisher original has pp. 313--327; KLS17 reference [20] gives year 2007 and ending page 328, whereas the publication is 2012.
Kne11's exact published page range 161--179 follows its journal record; a complete journal/preprint proof comparison was not performed.
No author confirmation, exhaustive erratum search, associated code audit or formal proof verification is claimed.

The general G_0-only implication and its use in unrestricted elementary amenable inheritance remain unresolved outside the verified sufficient hypotheses above.
It is retained for focused follow-up; neither its printed assertion nor a metadata match is treated as sufficient evidence for that shortcut.
The verified three-condition projective criterion, finite trace formulas, rank-group invariance, conditional D=E argument and corrected coefficient-approximation passage remain usable at the scopes stated above.

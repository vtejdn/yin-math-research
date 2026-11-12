---
author: Yin
---
# Independent review of global rational Promislow descent

Review performed at 2026-11-11 18:37 UTC for Yin.
The exact principal input is the whole working-tree [L_A0028_v2](../../ledger/Yin_L_A0028_v2.md), including every displayed equation, claimed equivalence and bounded conclusion.
This is a new independent inspection of that physical version, not an extension of a verdict about L_A0028_v1.
The reviewer was outside substantive proof development and received the fixed input, necessary prerequisite locators, review assignment and execution metadata only.
No development drafts, proof-generation dialogue, author proof summary or earlier review conclusions were supplied or consulted.
After forming the findings, the reviewer read only the author header and title of R_A0037_v1 to confirm the same-topic family; its findings remain unconsulted and are not evidence here.
The reviewer made no mathematical repair or edit to the candidate.

The necessary fixed prerequisites inspected were [L_A0024_v1](../../ledger/Yin_L_A0024_v1.md#the-actual-left-matrices-and-right-semilinear-symmetries), [L_A0003_v1](../../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding), [its complete norm criterion](../../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness), [L_A0010_v1](../../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model), and [L_A0022_v1](../../ledger/Yin_L_A0022_v1.md#producing-the-rational-orthogonal-kernel-projection).
Their actual interfaces were reconstructed directly rather than accepted from previous R findings.
The reference to L_A0028_v1 supplies the earlier research question; none of its formal-lifting assertions is needed to prove the reductions in the present input, and that older version was not re-reviewed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-input finding](#whole-input-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-input finding](#whole-input-finding) | [L_A0028_v2](../../ledger/Yin_L_A0028_v2.md) | Whole physical version: actual covariance algebra, coefficient division ring, mixed norm reduction and elimination, valuation limitation, determinant cocycles, exterior equations, fixed field, quadratic form, all equivalences and stated unresolved scope. |
| [Whole-input finding](#whole-input-finding) | [Actual matrices and semilinear symmetries](../../ledger/Yin_L_A0024_v1.md#the-actual-left-matrices-and-right-semilinear-symmetries) | Right-coefficient convention, both right semilinear matrices, original square translations and unitarity used in the whole-input derivation. |
| [Whole-input finding](#whole-input-finding) | [Actual affiliated embedding](../../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding) | Subgroup affiliated embedding, finite-coset independence and the right-module matrix convention needed here. |
| [Whole-input finding](#whole-input-finding) | [Complete norm criterion](../../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness) | Division criterion and rank-one matrix witness specialized to the stated Promislow subgroup; unrelated example and its residue proof are outside this review. |
| [Whole-input finding](#whole-input-finding) | [Promislow group prerequisite](../../ledger/Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test) | Group, normal forms, index-two subgroup, twisting data and finite abelianization, checked against the specified Gardam passage and directly where used. |
| [Whole-input finding](#whole-input-finding) | [Actual four-coset model](../../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model) | Faithful normal representation and affiliated extension; adjoining translation rational functions uses the elementary abelian Fourier argument immediately following this section. |
| [Whole-input finding](#whole-input-finding) | [Rational Gram projection](../../ledger/Yin_L_A0022_v1.md#producing-the-rational-orthogonal-kernel-projection) | Generic rational Gram construction, zero-set argument and transfer of unitary covariance, directly reconstructed with three variables. |

## Actual algebra, division criterion and valuations

The faithful Fourier model of the translation subgroup sends a nonzero Laurent polynomial to a measurable multiplier with zero kernel: its zero set has Haar measure zero by the polynomial root bound and Fubini.
Its inverse is therefore an actual affiliated multiplier.
Clearing finitely many translation denominators reduces any asserted rational coset relation to a group-algebra relation, so the four right-coefficient cosets remain independent.
This justifies the actual four-dimensional right \(F\)-space without an abstract-to-affiliated identification premise.

If an \(F\)-linear endomorphism commutes with the right translations by \(a,b\), it commutes with their products and has value \(cr\) on each basis element \(r\in\{1,a,b,ab\}\), where \(c\) is its value at \(1\).
Right \(F\)-linearity then identifies it with left multiplication by \(c\) on every vector.
Conversely, associativity gives both commuting equations.
Applying this argument to each block proves the stated commutant identification with \(M_n(\mathscr A)\).

For \(\mathscr D=F\oplus Fb\), direct multiplication on both sides gives equation (1), with zero \(b\)-coefficient.
The scalar \(f\beta(f)-yg\beta(g)\) is \(\beta\)-fixed and hence commutes with \(b\).
For nonzero \(f,g\), its summands have \(y\)-valuations \(2v_y(f)\) and \(1+2v_y(g)\), so it is nonzero; the one-zero cases give the same conclusion immediately.
Dividing the displayed conjugate by this nonzero scalar supplies a two-sided inverse in the actual algebra.
All translation rational functions and \(b\) belong to the actual division closure of \(\mathbb CH\), while this division subring contains \(\mathbb CH\); the claimed equality with that closure follows in both directions.

The subgroup normal forms give \(H=\langle x,z\rangle\rtimes\langle b\rangle\), with \(b\) inverting \(x,z\) and \(b^2=y\).
The identity \(z=abab\) yields \(aba^{-1}=xz b^{-1}\), and applying this automorphism twice to \(b\) gives \(x^2b=xbx^{-1}\).
Thus the non-involutive twisting data in (2) are correct.
In the right \(\mathscr D\)-basis \(1,a\), the matrix of left multiplication by \(a+k\) is
\[
 \begin{pmatrix}k&x\\1&\alpha^{-1}(k)\end{pmatrix}.
\]
The two factorizations in the fixed norm criterion show that it is invertible exactly when \(x-\alpha(k)k\ne0\).
When this difference vanishes, \(x=k\alpha^{-1}(k)\), and the displayed matrix factors as the nonzero column \((k,1)^T\) times the row \((1,\alpha^{-1}(k))\).
Its right \(\mathscr D\)-rank and kernel dimension are both one, and restricting scalars gives \(F\)-rank and kernel dimension both two.
This establishes the witness used later without assuming division of the full Promislow algebra.

Expanding \(\alpha(f+gb)(f+gb)\) gives exactly the two coefficients in (4).
For \(g=0\), \(x\)-valuation excludes the norm equation; for \(f=0\), applying \(\sigma_a\) gives \(g\gamma(g)=z\), excluded by \(z\)-valuation.
When both coefficients are nonzero, substitution \(f=vg\) gives
\[
 \frac{\beta(g)}g=-\frac{y\sigma_a(v)}{xz\beta(v)},\qquad
 \sigma_a(g)g\,\frac{\sigma_a(v)(N-y)}{\beta(v)}=x.
\]
The same even/odd \(y\)-valuation argument proves \(N-y\ne0\), so these are equivalent to (5), not merely necessary consequences.
Taking the \(\beta\)-norm of the first identity gives \(1=y^2\sigma_a(N)/N\), which verifies (6) with its stated necessary-only role.
No valuation argument here excludes the mixed system.

An \(\alpha\)-invariant homomorphism \(\nu:\mathscr D^\times\to\mathbb Z\) extends on the group through the assignments in the candidate because conjugation and the relation \(a^2=x\) are respected.
Abelianizing the two original defining relations gives precisely \(4a=4b=0\), so the resulting homomorphism to \(\mathbb Z\) vanishes and \(\nu(x)=0\).
Also, on the skew Laurent expression with coefficient field \(\mathbb C(x,z)\), \(\alpha\) reverses exponents of \(b\), interchanging the negative of the highest exponent with the lowest exponent.
The stated failure of invariance of the one-sided valuation and its completion therefore follows.
This obstruction is scoped to the proposed invariant valuation, not to every possible valuation method.

## Determinant and exterior calculations

The multiplier products are \(p\sigma_a(p)=x^2\), \(q\beta(q)=y^2\), and \(q\beta(p)=x^{-1}z\).
The last multiplier has \(\gamma\)-norm \(z^2\).
Conjugation of the scalar \(x^2\) by the semilinear \(b\)-map inverts it, and conjugation of \(y^2\) by the \(a\)-map inverts it.
Thus the two defining group relations hold for these line maps, and their three squared generators give the squared translation character on all of \(N\).
This verifies the entire right-action cocycle, including the order in (8), rather than only separate square equations.
The determinants of the two actual four-dimensional matrices are \(p^2,q^2\).
For an arbitrary determinant rank \(d\), the \(x\)-valuation of \(m_a\sigma_a(m_a)=x^d\) gives \(2v_x(m_a)=d\); the explicit rank-two line data show why this condition cannot give divisibility by four.

The reviewer computed the images of all six ordered basis bivectors under both exterior matrices.
For example, after normalization by \(p^{-1}\), the \(a\)-map sends \(e_{12}\) to \(-yz e_{12}\), \(e_{13}\) to \(e_{24}\), \(e_{14}\) to \(x^{-1}e_{23}\), \(e_{23}\) to \(xe_{14}\), \(e_{24}\) to \(e_{13}\), and \(e_{34}\) to \(-(yz)^{-1}e_{34}\).
After normalization by \(q^{-1}\), the \(b\)-map sends these same six vectors respectively to \(y^{-1}e_{34},-e_{13},-e_{23},-e_{14},-e_{24},ye_{12}\).
These give exactly every equation in (10).
The squared translation cocycle cancels against the line cocycle, so the normalized maps factor through the actual quotient \(C_2^2\), and hence are commuting semilinear involutions.
Solving the coordinate pairs gives (11)--(12) with no extra compatibility equation.
The four-dimensional Plucker relation is necessary and sufficient for a nonzero bivector to be decomposable, and substitution gives precisely (14).

## Fixed field, quadratic form and descent

The Cayley variables have the claimed sign actions.
Since \(w=T/(uv_0)\), the extension \(F/L\) has degree at most four; the four displayed distinct \(L\)-automorphisms force degree four and identify \(L\) as the full fixed field.
The elements \(U,V,T\) are algebraically independent because \(F\) has transcendence degree three and is finite over their field.
The three quadratic fixed fields are consequently exactly \(L(u),L(v_0),L(w)\).
Dividing the three equations in (11) by the respective nonzero solutions \(1-yz,u,1-x\) gives precisely those fixed fields, proving existence and uniqueness of (16).

The three terms of the Plucker equation become
\[
 y^{-1}h\beta(h)=d(H_1^2-UH_2^2),\qquad
 r\sigma_a(r)=U(R_1^2-VR_2^2),\qquad
 s\beta(s)=-e(S_1^2-WS_2^2).
\]
These independently verify all signs and coefficients of (17), including \(d=4(V-W)/((1-V)(1-W))\) and \(e=4U/(1-U)\).
Both coefficients are nonzero elements of the stated rational field.
The injective parameterization identifies nonzero solutions of this six-variable equation with nonzero invariant decomposable bivectors.

For the converse descent from an invariant two-plane, its exterior line is stable under both normalized maps.
On its underlying \(L\)-space the two commuting involutions have the four projectors displayed in the candidate, whose sum is the identity.
A nonzero projected vector has one of the four sign characters, and multiplication by the corresponding element of \(\{1,u,v_0,uv_0\}\) cancels those signs because their characters exhaust all four possibilities.
This produces a fixed nonzero vector in the same exterior line and preserves decomposability.
Thus a preserved line does not merely provide unspecified multiplier data: the proof really supplies the invariant vector required for (10)--(17).

For a rational two-plane, choose an \(F\)-basis matrix \(V\) and use the involution that conjugates constants and inverts \(x,y,z\).
A nonzero minor remains nonzero off a measure-zero subset of the torus, so the ordinary Hermitian Gram matrix there is positive definite and its rational determinant cannot vanish identically.
Consequently \(V(V^\star V)^{-1}V^\star\) is a rational rank-two orthogonal projection.
The original monomial right matrices are unitary on the torus and their automorphisms preserve its Haar measure, so they transport the generic plane fibers and their unique orthogonal projections.
The resulting covariance holds on a full-measure set and hence as rational identities, by the same nonzero-polynomial zero-set argument.
This verifies the affiliated-model interface without imposing everywhere-defined operations on unbounded Hilbert-space vectors.

Combining this projection construction, the commutant identification and the rank-one \(\mathscr D\)-witness proves each direction of (18).
In particular, if \(\mathscr A\) is a division ring, an idempotent image in \(\mathscr A^n\) is a finite-dimensional right \(\mathscr A\)-space and its restricted \(F\)-dimension is four times its dimension over \(\mathscr A\).
Conversely, failure of division supplies the rank-two projection already constructed, so the assertion over all matrix sizes has the same obstruction as size one.
Prescribing the specialization \(E_y\) would require a further constraint and is correctly excluded from this equivalence.
The example \(H_1=1\) and all other coordinates zero has Plucker value \(d\ne0\), so it proves nonemptiness of linear exterior descent without supplying an invariant plane.

## Source verification and limits

The reviewer inspected the local original of [Gardam, arXiv v4, Section 3.1, pp. 4--5](../../literature/pdf/Gar21--arxiv-v4.pdf#page=4).
Those pages give the stated presentation, torsion-freeness, normal translation subgroup isomorphic to \(\mathbb Z^3\), four cosets, conjugation actions and cocycle.
Conversion from the source's left-coefficient cocycle to the candidate's right-coefficient matrices agrees with the explicitly checked products above.
The source's unit construction and known zero-divisor discussion were not used as a division premise.

The reviewer also inspected [Lewis, publisher edition, Section 1.2, Theorem 6, p. 47](../../literature/pdf/Lew06.pdf#page=7).
It defines the six-dimensional Albert form of a biquaternion algebra and states its anisotropy equivalence with division, matching the candidate's comparison-only account.
The candidate makes no tensor-decomposition identification of \(Q\), and its direct proof does not invoke that theorem.
The original proof cited by Lewis was not re-audited, and no exhaustive novelty or whole-library priority search was performed.
These limits do not leave an external theorem unresolved in the direct derivation of (18).

## Whole-input finding

No mathematical gap was found in the whole reviewed L_A0028_v2 reduction.
The coefficient division argument, exact mixed system, determinant-line insufficiency and complete quadratic-form equivalence are valid under the stated actual Promislow model and rational coefficient fields.
The conclusion is a reduction with a precise unresolved anisotropy problem, not a proof that the quadratic form is anisotropic or that the mixed system has no solution.
The review neither assumes known division coverage of \(P\) nor independently establishes that coverage, and it supplies no completion finding for T_A0001.
Further work must exclude all nonzero \(L\)-rational solutions of (17), equivalently all mixed solutions of (4), if this route is to prove the remaining obstruction without importing known division results.

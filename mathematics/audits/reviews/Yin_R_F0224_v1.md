---
author: Yin
---
# Independent review of the finite type I summand exclusion for closable coordinate derivations

## Whole-proof finding

At 2026-11-13T14:28 UTC a separate agent outside proof development reviewed the complete [C_F0216 v1 candidate](../../claims/Yin_C_F0216_v1.md#decision-candidate) dated 2026-11-13T14:25 UTC.
The reviewer received the fixed Claim and the scope of the requested checks, without proof-development dialogue, exploratory notes, an author explanation or a previous finding on this Claim.
The argument proves the single-coordinate exclusion of all nonabelian finite type I summands and all abelian atoms, the exclusion of the entire finite type I summand for two or more coordinates, and the claimed actual full-domain dual in the single-coordinate type I case.

For fixed \(t\), the differentiated Neumann series converges in the coarse norm by summability of \(k\|u\|^{k-1}\).
The differentiated remainder tends to zero by the same estimate.
Solving the limit product rule on the left gives the claimed derivative of \(g_t\), and multiplying the polynomial approximants by \(q\) places \(f_t\) in the domain of \(\bar\delta\).
In the term containing \(\delta(q^*)\), the two factors of \(f_t\) give \(t\|f_t\|^2\le 1/4\).
Hence the derivatives form a bounded sequence while \(f_t\to0\) in \(H\).
The weak closure of the graph puts every weak cluster point over zero at \((0,0)\), proving weak convergence to zero.
The projection \(r\) onto \(\ker q^*\) kills \(f_t\) on the left and satisfies \(rh_t=r\), while the projection \(p\) onto \(\ker q\) satisfies \(g_tp=p\).
These identities give \(r\delta(q)p=0\) even for arbitrary coarse values of \(\delta(q^*)\).
If \(eq=0\) for central \(e\), both kernel projections dominate \(e\), so the double compression descends to a derivation on the represented corner with generator values \(\delta_{ij}e\otimes e\).
For \(q=X_i-\lambda\), the same identity reads \(r\otimes p=0\) and the polar partial isometry gives \(\tau(1-p)=\tau(1-r)\).
Faithfulness therefore kills both kernels.
This reasoning works on a type I central corner in the presence of a type \(\mathrm{II}_1\) complement and uses closability only on the original algebra.

I checked the bounded product of finite matrix-valued function algebras in Niemiec and Wegert, Theorem 2.2, and the immediately preceding definition of its measurable matrix entries, on [p. 3 of arXiv:1307.4696v1](https://arxiv.org/pdf/1307.4696v1#page=3).
A faithful finite trace charges at most countably many nonzero component units and induces an equivalent finite measure on each center.
Within a component, traciality on the matrix units gives the normalized matrix trace against that measure.
Approximation of each constant matrix unit in \(L^2\) by represented star polynomials has an almost everywhere convergent subsequence.
Intersecting the finitely many resulting conull sets puts every matrix unit in the closed finite-dimensional word span at each remaining fiber.
At a fixed complex \(\lambda\), fiberwise kernel functional calculus and the lower bound \(1/n\) for a nonzero normalized kernel trace imply that the fibers having eigenvalue \(\lambda\) form a null set.
The common-root resultant is measurable, and each fixed fiber has finitely many eigenvalues, so Fubini removes the common-spectrum pairs.

The component extraction \(a\otimes b\mapsto(a_{ri}b_{j\ell})_{r,\ell}\) intertwines the outer multipliers with ordinary left and right matrix multiplication.
Representatives of the two letter derivatives consequently realize the triangular word evaluations simultaneously on one conull set.
There are only countably many word substitutions in the alternating identity, whose represented values and compressed derivatives are zero.
After their null sets are removed, complex multilinearity extends the identity to all polynomial substitutions in its image, including linear combinations selected after fixing the pair.
The coprime characteristic polynomials give a polynomial lifting \((I,0)\) diagonally, and multiplication by each diagonal central idempotent separates the two full word spans.
A nonzero kernel of the diagonal projection would contain all upper-right matrix units by the bimodule action of the surjective diagonal algebra.
The image would then contain the entire upper triangular block algebra, since any lift of a prescribed diagonal could have its upper-right entry removed.
In the given test of the identity, the flanking units at slot \(k\) select precisely the row \(a_k\) and column \(b_k\), including at the transition from the first to the second block.
Only the identity permutation survives, giving \(E_{1,n+1}\) and ruling out such a kernel.
Commutation with the unique lift of the diagonal central idempotent gives \(D_{ij}(p)=p_sK_{ij}-K_{ij}p_t\) with this sign.

For disjoint spectra the same separating polynomial forces \(\ker S=0\) for \(S(C)=x_sC-Cx_t\), so \(S\) is invertible on the finite matrix space.
The letter \(X\) has component \(E_{ij}\), and its adjoint letter has component \(S^*S^{-1}(E_{ij})\) by the split representation.
The indices \((r,i,j,\ell)\) account for every tensor entry once.
With the normalized trace on each leg this gives exactly \(n^{-2}\|S^*S^{-1}\|_{\mathrm{HS}}^2\) for the squared coarse fiber norm, where the Hilbert--Schmidt norm of the map refers to the ordinary Hilbert--Schmidt matrix space.
Root ordering is Borel and the spectral kernel projection is the displayed pointwise resolvent limit.
Its first nonzero column thus supplies a measurable unit eigenvector \(v_s\).
Full star-word span for \(n\ge2\) precludes a reducing eigenline, so the orthogonal component of \(x_s^*v_s\) has a positive lower bound \(c\) on some set of positive measure.
Given a unit left eigenvector \(u^*\) at \(t\), the rank-one \(C=v_su^*\) satisfies \(S(C)=(\lambda_s-\lambda_t)C\) and \(\|(I-v_sv_s^*)S^*C\|_{\rm HS}\ge c\).
Testing the operator norm of \(S^*S^{-1}\) at \(S(C)/\|S(C)\|_{\rm HS}\) gives the inverse-distance estimate independently of eigenvalue multiplicity or Jordan form.
The eigenvalue pushforward of the restricted measure is boundedly supported and diffuse by the fixed-\(\lambda\) kernel test.
Summing squared cell masses on a planar grid gives a lower bound proportional to \(r^2\) for pairs at distance at most \(r\).
Layer integration against \(2r^{-3}\,dr\) makes its inverse-square energy infinite, contradicting the norm of the compressed adjoint-letter vector.
The contradiction is componentwise and requires no uniformity in \(n\).
An atom on an abelian component would likewise put positive trace in a fixed scalar kernel.

For several coordinates, minimal degree of a holomorphic relation in any nonzero corner makes all shorter evaluated words independent, and their simple tensors independent in the Hilbert tensor product.
In the \(i\)-th derivative the coefficient of each empty-prefix tensor \(e\otimes w(eX)\) is precisely the coefficient of \(x_iw\).
Thus all positive-degree coefficients vanish, and the remaining scalar cannot be a nonzero relation on \(e\).
The alternating polynomial of degree \(n^2+1\) vanishes on every fiber \(M_n(\mathbb C)\) by multilinearity in a space of dimension \(n^2\).
Substitution of the words \(x_1x_2^j\) yields distinct words for distinct permutations, giving an actual nonzero relation on the whole homogeneous corner.

For actual ACSY the vacuum pairing on \(\delta(a^*xb^*)\) bounds the pairing with \(a\otimes b\) by a constant times \(\|x\|_2\) after the other two Leibniz terms are transferred to the vacuum.
The algebraic core tensors are dense, so this gives the claimed closability for each coordinate.
In the single-generator type I case the abelian diffuse spectral measure identifies the generator with multiplication by \(z\).
The Leibniz rule applied to \(Xp=pX\) gives the canonical divided difference off the null diagonal, so the vacuum adjoint represents exactly the functional in the scalar part of C_F0055 v1.
I used its [reviewed scalar estimate and domain conclusion](Yin_R_F0037_v1.md#scalar-findings) at that interface.
The identity \(E_0(Xp)=XE_0p+P_\Omega p\) passes to every vector of the domain of the original closure by graph approximation and boundedness of \(X\) and \(P_\Omega\).
Thus \(D=-E\) has \([X,D]=P_\Omega\) on bounded inputs, its actual adjoint also contains those inputs, and its restriction is bounded from operator norm to \(L^2\).
The external structure theorem was checked at the statement and applicability level.
The single-generator type \(\mathrm{II}_1\) case and completion of the general Task are outside this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0216_v1.md#statement) | Closable normalized coordinate derivations with arbitrary adjoint values, both summand conclusions, actual ACSY and the single-generator type I dual. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0216_v1.md#argument) | Resolvent graph limits, central descent, measurable fibers, the triangular polynomial identity and splitting, exact norm and eigenline estimate, polynomial relations and scalar domains. |
| [Whole-proof finding](#whole-proof-finding) | [Type I structure source](../../claims/Yin_C_F0216_v1.md#type-i-structure-source) | Niemiec and Wegert, Theorem 2.2, checked in the indicated edition for bounded finite type I algebras with finite matrix size on each component. |
| [Whole-proof finding](#whole-proof-finding) | [Critical planar energy](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Grid mass and layer integral for the nonzero bounded diffuse eigenvalue law. |
| [Whole-proof finding](#whole-proof-finding) | [ACSY closability](../../claims/Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | The actual vacuum and bounded outer multipliers put a dense algebraic tensor space in each adjoint domain. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar canonical domains](../../claims/Yin_C_F0055_v1.md#statement) | Scalar divided-difference vacuum, bounded restriction and both original bounded-input domains for the polynomial right contraction. |

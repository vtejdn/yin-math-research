---
author: Yin
---

# Independent review of the restricted Haar-pencil structural theorem

<a id="independent-haar-structural-proof"></a>
## Finding: the exact restricted statement and argument are supported

Review act: 2026-11-05T07:35, human record author Yin.
A separately organized AI reviewer outside substantive development checked the fixed [statement](../../claims/Yin_C_F0192_v1.md#statement) and [complete argument](../../claims/Yin_C_F0192_v1.md#argument) against the [original F0015 contract](../../tasks/Yin_T_F0015_v1.md#contract).
The supplied review context contained the assignment, exact fixed target, scope, human authority and applicable operational limits.
It contained no exploration notes, proof-generation dialogue, author explanations, mathematical development summaries or previous conclusions about this proof.
The reviewer read the proof and its necessary mathematical dependencies directly, formed initial findings before proposing any repair, and made no substantive repair.
No earlier review of this candidate was consulted or relied upon.

The five assertions are supported at their exact stated scope.
The coefficient-position symmetry preserves the finite marginal laws and free determinant, the zero-free-kernel hypothesis implies eventual almost-sure finite invertibility, and the stated two-position, sparse-component and triangular classes have the full extended logarithmic limit under every allowed cross-dimensional coupling.
This also gives their upper-limit conclusions and their independent-across-dimensions cases.
No remaining mathematical gap was found in this restricted theorem.
It does not settle the unrestricted F0015 contract, and this review supplies no Task-completion finding.

## Checked logical interfaces

### Coefficient positions and two-position pencils

The left multiplier for exchanging the constant position with position k leaves the squared modulus unchanged.
Conditioning on the kth Haar matrix gives the product Haar law for the transformed remaining variables, independently of that kth matrix.
Taking its adjoint as the new variable therefore gives a fully independent Haar tuple at each size.
These transformations act separately at each dimension and preserve independence across dimensions when imposed.
Moment convergence of the original tuple and the transformed Haar tuple identifies the free transformed variables, so there is no unproved free-invariance assumption in this step.
Random-position permutations and these exchanges generate every coefficient permutation.

For two effective positions, diagonalization of the single Haar matrix gives the scalar polynomial f(z)=det(B_0+zB_1) with the normalization 1/(mN).
If f is identically zero, every finite fiber is singular and the free direct integral has kernel trace at least 1/m.
If f is nonzero, its finitely many off-circle root factors have continuous logarithms on the circle, while the on-circle root factors use the fixed-point CUE mean and variance input.
The resulting deviation bound is summable over every positive integer dimension.
First Borel--Cantelli needs no cross-dimensional independence, and a finite intersection handles all root factors.
The zero-position and one-position cases also have their asserted deterministic extended limits.
No coefficient invertibility hypothesis is introduced.

### Eventual invertibility

The proof uses only the algebraic part of [C_F0186_v2](../../claims/Yin_C_F0186_v2.md#generic-rank), rather than its GUE estimates or probability-limit conclusion.
I rechecked that the maximum-rank locus for the homogeneous blow-up intersects the open locus where the zeroth physical matrix is invertible.
Right multiplication then identifies the homogeneous maximum rank with the affine maximum rank.
The selected square-blow-up rank is a multiple of N, so any deficient dimension has normalized kernel mass at least 1/m.
Haar moment convergence and the fixed norm bound give convergence in probability of the squared-singular-value measures and weak convergence of their deterministic expectations.
Portmanteau on the closed set consisting of zero contradicts zero free kernel if deficient dimensions occur infinitely often.
This proves that the affine determinant polynomial is nonzero in every sufficiently large dimension.

The Cayley chart argument correctly transfers nonidentity to Haar almost-sure nonsingularity.
The complex rational Cayley map is birational on the required nonempty open set, and a real basis of Hermitian matrices is also a complex matrix-space basis.
Thus clearing denominators cannot give an identically zero polynomial on those real coordinates.
Polynomial zero sets have Lebesgue measure zero there, the smooth Haar chart has a density, and scalar rotational invariance removes the excluded eigenvalue event.
A countable intersection gives the claimed probability-one eventual-invertibility event for every allowed coupling.
Zero free kernel is sufficient even if the ordinary free determinant is zero through logarithmic divergence.
The deduction supplies no positive singular-value floor or logarithmic-tail estimate.

### Sparse components and the four-entry example

The hypotheses make every random supported edge carry one distinct Haar input and prohibit a constant contribution at that position.
The recursive row and column unitary assignments are consistent on a tree and change neither singular values nor determinant magnitude.
For a component with one cycle containing a random edge, deleting such an edge leaves exactly one chord variable.
Its two endpoint multipliers depend only on other inputs, so conditioning on them leaves the chord word Haar.
The free word is Haar by the corresponding finite word moments and the accepted asymptotic moment input.
No joint freeness of extra residual words is required because all remaining component entries are scalar multiples of the identity.
For an entirely deterministic cycle, rooting on that cycle makes all its tree multipliers and its chord multiplier identities, even when random branches are attached.

Balanced components become square direct summands with the correct auxiliary-size weights.
Finite intersections and addition of their limits are valid; if one limiting determinant is zero, the fixed norm upper bounds on the other components force the extended sum to minus infinity.
An unbalanced component forces finite singularity at every dimension by its rectangular rank deficit.
The proved generic-rank contrapositive then gives nonzero free kernel, with no reliance on a logarithmic approximation theorem for this case.

For the explicit four-entry pencil I checked the row and column multipliers, the word U_3^*U_4U_2^*U_1, and the Schur-complement determinant identity.
The scalar circle integral gives one half of log max{|ad|,|bc|} with the required 2N normalization.
At equality of the two moduli, the Schur complement has a null spectral point of Haar measure zero, so its affiliated inverse exists and is unbounded while its ordinary determinant is positive.
The four nonzero scalar matrix units have no common proper nonzero invariant auxiliary subspace.
This example therefore lies within the sparse theorem without depending on simultaneous triangularization.

### Triangular extension

The fixed similarity uses bounded multiplicativity and cancels the scalar determinants of the change of basis and its inverse.
For positive determinant diagonal blocks, each block is injective and has dense range in its finite tracial algebra.
Solving the triangular block equations from the last row proves injectivity of the whole triangular matrix and of each suffix used in the iteration.
In the canonical free-group realization, the maps are bounded equivariant maps between finite free Hilbert modules.
The first diagonal map has dense image and the second is injective at each application of the selected triangular determinant identity.
All relevant maps are injective, so kernel removal changes none of their determinants.
The source's unnormalized matrix trace produces the stated auxiliary-size weights after division by m.
This argument requires no bounded inverse of the diagonal operators.

For the particular diagonal classes, a nonzero scalar single-Haar determinant polynomial has finite logarithmic integral.
Thus zero determinant in these classes is exactly the identically singular polynomial or deterministic singular case described in the proof.
The corresponding finite diagonal block is singular at every dimension, forcing finite singularity of the whole triangular pencil.
The generic-rank contrapositive again supplies nonzero free kernel for the whole pencil.
This verifies the minus-infinity branch separately from the positive-determinant triangular identity.

## Source inputs and limits

The accepted Haar asymptotic input in [L_F0062_v1](../../ledger/Yin_L_F0062_v1.md#haar-pencils) matches fixed complex coefficients and full-complex Haar inputs.
I inspected [CM14](../literature/CM14/readme.md) in the [published primary PDF](https://smf.emath.fr/download/pdf/44403), Theorem 1.4 and Corollary 2.3, printed pp. 150 and 154 / PDF pp. 5 and 9.
The former gives trace convergence and the latter the matrix-coefficient norm interface.
Their original proofs were accepted rather than re-audited.
Only moment convergence and its single-unitary continuous-test consequence are necessary here.

For [the retained single-Haar application](../../ledger/Yin_L_F0062_v1.md#single-haar), I inspected [BHNY08](../literature/BHNY08/readme.md) in the [author-hosted primary PDF](https://math.nyu.edu/~bourgade/papers/Duke2008.pdf), Section 4.2, PDF pp. 15--17.
The centered fixed-point real logarithm and variance asymptotic one half of log N provide exactly the summable Chebyshev input.
The source's coupling-specific iterated-logarithm theorem is unused, and no whole-paper proof audit is claimed.

I checked [DM17](../literature/DM17/readme.md) in the [published primary PDF](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.54.pdf#page=6), Definitions 2.1--2.2 and Proposition 2.3, journal p. 49 / PDF p. 6.
Its assertion concerns the maximum rank of the square blow-up over the infinite field, not every evaluated matrix.
It applies over the complex numbers exactly as used in [the retained definition](../../claims/Yin_C_F0186_v2.md#matrix-space-rank).
The underlying IQS proof was accepted without re-audit.

The selected [Luc22 unit](../literature/Luc22/Yin_U001.md#luc22-u001) is used only for [its determinant convention and triangular interface](../literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant).
I inspected the retained arXiv:1901.00827v2 primary PDF, Definition 14.14 and Theorem 14.18(2), pp. 23--24.
Its dense-image and injectivity assumptions, kernel-removed convention and unnormalized module trace are all matched above.
Its cited foundational book proof was accepted without re-audit.

The selected [FK52 unit](../literature/FK52/Yin_U001.md#fk52-u001) supplies only [bounded multiplicativity and its finite-tracial adaptation](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
I read the retained original scan, Theorem 1 and Lemmas 2--3 on pp. 522--524, and Lemma 5 with the analytic product extension on pp. 528--529.
The unit's extension from a finite factor uses functional calculus, trace cyclicity and unitary polar decomposition available in a finite tracial algebra.
No affiliated inverse is inserted into that product identity.

I checked [Ken11](../literature/Ken11/readme.md) in the [primary arXiv:1001.4028v3 PDF](https://arxiv.org/pdf/1001.4028v3), Section 3.1, PDF pp. 4--5.
It supports the stated connection, gauge-equivalence and monodromy attribution.
It is not a theorem input for the Haar determinant limit.
No priority finding, exhaustive literature search, formal verification, or associated code audit is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Exact statement](../../claims/Yin_C_F0192_v1.md#statement) | All five restricted assertions, both coupling regimes, extended logarithms and the exact four-entry example; no unrestricted Task completion. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Complete argument](../../claims/Yin_C_F0192_v1.md#argument) | Complete gauge, scalar-polynomial, rank, Cayley-chart, sparse-component and triangular proof with the declared source limits. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Haar asymptotic input](../../ledger/Yin_L_F0062_v1.md#haar-pencils) | Fixed-coefficient Haar moment convergence and its applicability; other determinant formulas and survey-status assertions are outside this finding. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Single-Haar application](../../ledger/Yin_L_F0062_v1.md#single-haar) | Polynomial determinant reduction, fixed-point logarithmic variance, summable Chebyshev bound and first Borel--Cantelli under arbitrary coupling. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Affine rank identification](../../claims/Yin_C_F0186_v2.md#generic-rank) | Homogeneous-to-affine maximum-rank equality and divisibility only; no GUE geometric or logarithmic estimate is imported. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Matrix-space rank](../../claims/Yin_C_F0186_v2.md#matrix-space-rank) | Exact square-blow-up definition and maximum-rank divisibility over the complex numbers. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Luc22 source unit](../literature/Luc22/Yin_U001.md#luc22-u001) | Only the kernel-removed determinant convention and Theorem 14.18 triangular interface, matched through injectivity, dense image and the matrix-trace normalization. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [Luc22 selected interface](../literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) | Theorem 14.18(2) for bounded free-group module maps with dense first diagonal image and injective second diagonal map; no singular unrestricted multiplicativity. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [FK52 source unit](../literature/FK52/Yin_U001.md#fk52-u001) | Only ordinary bounded determinant multiplicativity and the retained finite-tracial adaptation. |
| [Restricted Haar structural proof](#independent-haar-structural-proof) | [FK52 selected interface](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) | Cancellation of the fixed similarity factors through bounded multiplicativity, including zero determinant values. |

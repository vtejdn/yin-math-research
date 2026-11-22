---
author: Yin
---
# Independent review of finite-support syzygies at the first noninteger matrix size

## Whole finding

At 2026-11-22T04:11 UTC a reviewer outside the development of C_A0113_v1 checked the full statement, proof and both examples for Yin.
The reviewer received the fixed Claim and the requested scope, read its cited inputs and received no proof-development dialogue or earlier verdict on this Claim.
The proof establishes the asserted restrictions for every discrete group under the respective size and scalar hypotheses.
The two examples show that the absence of a finite zero pairing allows either endpoint of the Schur rank interval.

### Minimal submatrices and rectangular ranks

Write the rank of a deletion-minimal fractional submatrix as \(h+\delta\), where \(h\) is an integer and \(0<\delta<1\).
Removing one column lowers rank by at most one, so the only possible integer rank of the deletion is \(h\).
In building its column span every intermediate submatrix is proper and has integer rank.
A retained column therefore increases rank by exactly one, whereas a discarded column already has image in the preceding closed span by faithfulness of the trace on the difference of the nested range projections.
Exactly \(h\) retained columns and the originally removed column give rank \(h+\delta\).
Minimality forces those \(h+1\) columns to be all the columns, including when \(h=0\).
Taking adjoints exchanges deletion of rows and columns and preserves ranks, so the row count is also \(h+1\).
This gives the stated square inside the original matrix and rules out fractional rank for any rectangle with either side below the first failing square size.

### Arbitrary full row combinations

For \(M=\overline{\operatorname{im} A}\), boundedness of \(X\) gives \(\overline{X(M)}=\overline{\operatorname{im}(XA)}\).
The restriction of \(X\) to \(M\) loses dimension \(\dim_G(M\cap\ker X)\le n-k\).
Thus \(\operatorname{rk}(XA)>k-1\), and rectangular integrality forces rank \(k\).
For the same reason greedy column selection in \(X\) produces \(k\) columns of full rank.
After permutation these give an affiliated-invertible leading block, so appending the remaining coordinate rows completes \(X\) over the group ring to an affiliated-invertible square.
The adjoint construction completes \(Y\), placing its columns last.
If \(XAY=0\), the completed triangular matrix has rank at most \(\operatorname{rk}D+n-k\) by row addition and at most \(k+\operatorname{rk}H\) by column addition, in the notation of (4).
Its rank exceeds \(n-1\), forcing both smaller diagonal blocks to have full integer rank.
Triangular inversion over \(U\) would give rank \(n\), a contradiction.

Every selected list of at most \(n-k\) finite syzygies forms a matrix with fewer than \(n\) columns, so each strict increase in its closed image adds one to its rank.
The preceding contradiction prevents \(n-k\) increases.
At termination, every finite syzygy belongs to the resulting closed image, since its associated convolution column applied to \(\delta_e\) recovers that syzygy.
Conversely, all right translates of the selected syzygies are finite syzygies and span a dense subspace of the selected closed image.
This proves (1), including \(k=n-1\), and gives the left-hand assertions by adjunction.
For an amenable group, complete kernel localization applies to \(XA\) on the finitely generated subgroup containing its coefficient supports, and the decomposition over right cosets extends density to the whole group.

### The scalar pivot and the finite-dimensional test

Under scalar injectivity every nonzero row and every nonzero column of length two has rank one, by restricting to a nonzero entry.
Elimination with the affiliated inverse of \(a\) gives \(\operatorname{rk}A=1+\operatorname{rk}s\).
Fractional Schur rank thus makes size two minimal and yields \(uAv\ne0\) for every nonzero pair, which also verifies the common-multiple test by contraposition.
Fixing \(u\) gives an injection \(B^2\longrightarrow B\) with proper image, since a right-module isomorphism would remain an isomorphism after tensoring with the left augmentation module and would identify \(\mathbb C^2\) with \(\mathbb C\).
In a polynomial relation, the constant term consequently vanishes.
Separating by the first letter then produces two relations of strictly smaller degree, by injectivity of the row.
Induction gives independence of all words including the empty word.
Restriction of the row injection to \(\mathbb C[J]^2\) proves the one-sided support bound.

For \(e=\dim E,\ f=\dim F,\ w=\dim W\), the induced tensor map is surjective onto \(W\).
When \(w\le e+f-2\), its kernel has dimension at least \((e-1)(f-1)+1\).
This is exactly the two-factor threshold in [Parthasarathy, Proposition 1.4, arXiv v1, pp. 5–6](https://arxiv.org/pdf/quant-ph/0405077#page=5).
The Segre variety has dimension \(e+f-2\), so the projective intersection argument also works when either factor has dimension one.
The resulting nonzero decomposable tensor yields a pair with \(uAv=0\).
For the support spaces the two dimensions are \(2|H|\) and \(2|J|\), and each output is supported in \(HSJ\), giving exactly (3).

### Both integral endpoints

For \(F(x,y)\times\mathbb Z\), Linnell's division-ring theorem applies with normal free subgroup \(F(x,y)\) and quotient \(\mathbb Z\).
The free-tree boundary has trivial finite kernel by the leaf-edge argument, and its adjoint has the corresponding property for finite rows.
Over the free group algebra the two resulting nonzero scalars have nonzero product.
For Laurent inputs the coefficient of least total degree \(i+j\) of either pairing is this product on the two lowest input coefficients, because the additional central term raises the degree by one.
The nonzero first diagonal entry and the factorization through one column place \(\operatorname{rk}(cr)\) exactly at one.
The bounds \(\|x-1\|,\|y-1\|\le2\) give \(\|(10t)^{-1}cr\|\le 8/10<1\), hence \(cr+10tI_2\) has bounded inverse.
The Schur complements therefore have ranks zero and one, while the pairing and support tests hold for both.
The external inputs used here are the finite-trace affiliated rank calculus, projective dimension theorem, and Linnell's division-ring theorem at the cited hypotheses.
This review checks their application and the conditional conclusions, leaving the general Atiyah question open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0113_v1.md#statement) | All quantifiers, the two nullity conclusions, the Schur alternatives and both finite-dimensional bounds. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0113_v1.md#argument) | Minimal square extraction, rectangular integrality, arbitrary full-rank combinations, syzygy span, free algebra and dimension test. |
| [Whole finding](#whole-finding) | [Integral-rank examples](../../claims/Yin_C_A0113_v1.md#two-integral-ranks-with-no-finite-zero-pair) | Both ranks and all polynomial pairings over the Laurent extension of the free group algebra. |
| [Whole finding](#whole-finding) | [Affiliated rank calculus](../literature/MSY23/Yin_U004.md#msy23-u004) | Trace rank of closed images, rank-nullity, and square full-rank invertibility. |
| [Whole finding](#whole-finding) | [Kernel localization](../../claims/Yin_C_A0001_v2.md#proof-of-complete-rational-kernel-localization) | Density of finite kernel columns for a group-ring matrix over a finitely generated amenable group. |
| [Whole finding](#whole-finding) | [Arbitrary amenable groups](../../claims/Yin_C_A0001_v2.md#passage-beyond-finite-generation) | Right-coset transfer of finite kernel density. |
| [Whole finding](#whole-finding) | [Linnell's theorem](../literature/Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate) | Scalar injectivity for the torsion-free group with normal free subgroup and cyclic quotient. |
| [Whole finding](#whole-finding) | [Free-tree boundary](../../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) | Finite edge chains with zero boundary vanish. |

---
author: Yin
---
# Central-finite obstructions to extending the Promislow certificate

This development on 2026-11-12 serves [T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route seven](../strategies/Yin_S_A0007.md).
It screens a proposed extension of the [global Promislow certificate](../claims/Yin_C_A0013_v1.md#statement) before investing in further Brauer calculations.
The natural proposal is to retain a finite group quotient and its actual cocycle while replacing the translation field by an independently controlled noncommutative coefficient division ring.
The completed obstruction below shows that imposing finite dimension over a central field on that entire coefficient ring confines a finite-extension construction to virtually abelian groups.
The concrete candidate \(F_2\times P\) retains the original cocycle and has independently controlled coefficients, but fails this central-finiteness requirement explicitly and is already covered by Linnell's theorem.
Auxiliary finite-dimensional invariants which do not faithfully contain the coefficient group algebra remain outside the obstruction.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0039_v1.md#whole-artifact-finding) checks the obstruction, actual candidate, source applications and limitations; it does not resolve the Task.

## The actual proposed input chain

The fixed [Promislow certificate](../claims/Yin_C_A0013_v1.md#exact-source-inputs-and-reuse-boundary) uses Siv10, Theorem 1.10, for a central finite-dimensional division algebra over a commutative field.
Its actual input is a constant quaternion algebra, two specified quadratic constant-field extensions that remain division, and a rational parameter whose symbol increases the index.
The [whole-artifact finding](../audits/reviews/Yin_R_A0037_v5.md#whole-artifact-finding) checks the particular algebraic and analytic back-transfer.
It does not provide that theorem for division rings of infinite dimension over their centers.

For a proposed finite extension \(H\triangleleft G\), the first independent input would be division of the actual \(D_{\mathbb C}(H)\subseteq\mathcal U(H)\).
The second input would identify the actual crossed product \(D_{\mathbb C}(H)*(G/H)\) and its group cocycle.
Only after those inputs can one ask whether a central finite-dimensional algebra and an applicable global index criterion have actually been derived.
Replacing the words "field" or "central division algebra" in Siv10 by a general coefficient skew field is not a valid substitution.
The obstruction in the next section applies before any detailed cocycle calculation when the proposed finite-dimensional object contains the entire coefficient group algebra faithfully.

## A faithful central-finite model forces virtual abelianness

Let \(\Gamma\) be a group and let \(B\) be a unital algebra of finite dimension \(d\) over a field \(k\subseteq Z(B)\).
Assume that there is an injective unital complex-algebra homomorphism
\[
 \mathbb C\Gamma\longrightarrow B.
 \tag{1}
\]
No division or simplicity assumption on B is needed.
Then \(\Gamma\) has an abelian subgroup of finite index.

Here is the full reduction to the external group-algebra theorem.
For a positive integer m define the standard noncommutative polynomial
\[
 s_m(X_1,\ldots,X_m)
   =\sum_{\pi\in\mathfrak S_m}\operatorname{sgn}(\pi)
       X_{\pi(1)}\cdots X_{\pi(m)}.
 \tag{2}
\]
The \(m!\) monomials are distinct in the free complex algebra, so this is a nonzero polynomial.
Its evaluation on B is k-multilinear because k is central, and alternating because exchanging two arguments reverses the signs in the sum.
For \(m=d+1\), expand every argument in a k-basis of B.
Each resulting basis tuple has a repeated entry, and the corresponding terms cancel in pairs.
Thus
\[
 s_{d+1}(b_1,\ldots,b_{d+1})=0
 \qquad\text{for all }b_i\in B.
 \tag{3}
\]
Injectivity of (1) makes (3) a nonzero polynomial identity on \(\mathbb C\Gamma\).
This elementary dimension argument does not invoke the sharper Amitsur--Levitzki identity or a central-simple-algebra classification.

[Pas71, Corollary 1.5(ii), printed p. 428](../literature/pdf/Pas71--journal.pdf#page=5), states that a characteristic-zero twisted group algebra satisfying a polynomial identity has an abelian subgroup of finite index whose corresponding twisted algebra is commutative.
Take \(k=\mathbb C\) in that theorem and take its factor system identically one, so its twisted algebra is exactly \(\mathbb C\Gamma\).
Its conclusion is the asserted virtual abelianness.
The source theorem has no finite-generation, torsion-freeness, amenability or algebraically-closed-field hypothesis beyond the stated characteristic restriction; our use satisfies characteristic zero.
The use of k for B's central field above is independent of the source theorem's coefficient field, which in this application is \(\mathbb C\).

Consequently, if \(H\leq G\) has finite index and its actual coefficient division ring \(D_{\mathbb C}(H)\) is finite-dimensional over its center, then H and G are virtually abelian.
Indeed \(\mathbb CH\) injects into that division ring by the actual regular representation.
The result supplies an abelian \(A\leq H\) with finite index, and
\[
 [G:A]=[G:H][H:A]<\infty.
 \tag{4}
\]
Normality of A is unnecessary for (4).
If a normal abelian subgroup is wanted, the intersection of its finitely many G-conjugates is again abelian and has finite index.
For torsion-free G this remains within the known virtually abelian coverage; see the [checked comparison in R_A0037_v5](../audits/reviews/Yin_R_A0037_v5.md#earlier-extensions-and-the-original-task).
Thus allowing a noncommutative but central-finite coefficient division ring cannot enlarge that coverage through a finite group extension.

The same conclusion applies directly if an actual algebra faithfully containing \(\mathbb CG\), rather than only \(\mathbb CH\), is finite over a central field.
It also applies to a faithful map into a finite matrix algebra over such a B, since that matrix algebra is finite-dimensional over k.
A faithful group homomorphism into the units is weaker than (1): it need not induce an injective homomorphism of complex group algebras.
The proof requires the latter injectivity and does not rule out ordinary finite-dimensional faithful group representations.

## A concrete noncommutative candidate with the original cocycle

Let \(F_2=\langle u,v\rangle\), and retain the actual Promislow presentation and translation subgroup
\[
 P=\langle a,b\mid b^{-1}a^2b=a^{-2},\ a^{-1}b^2a=b^{-2}\rangle,
 \qquad x=a^2,\quad y=b^2,\quad z=(ab)^2,
 \qquad N=\langle x,y,z\rangle\cong\mathbb Z^3.
 \tag{5}
\]
The fixed [actual model](../ledger/Yin_L_A0024_v1.md#fixed-setting-and-proposed-test), checked against Gardam's original presentation in the [review](../audits/reviews/Yin_R_A0037_v5.md#actual-model-back-transfer-and-analytic-endpoint), supplies torsion-freeness and \(P/N\cong C_2^2\).
Set
\[
 G=F_2\times P,\qquad H=F_2\times N,\qquad D=D_{\mathbb C}(H).
 \tag{6}
\]
Both G and H are torsion free, H is normal in G, and \([G:H]=4\).
The elements u and v commute with all the elements in (5), but do not commute with each other.

Division of D is independently available without using any division theorem for G or P.
Namely \(F_2\times\{1\}\triangleleft H\) is free and \(H/(F_2\times\{1\})\cong\mathbb Z^3\) is elementary amenable.
The exact [Lin93 Theorem 1.3 interface](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) therefore proves that the actual D is a division ring.
The accepted proof and source-foundation limits remain those of that audit.
The translations x, y and z commute with every element of \(\mathbb CH\), hence with all inverses used in D, so they lie in \(Z(D)\).
They are algebraically independent over \(\mathbb C\), because distinct translation group elements are linearly independent in \(\mathbb CH\).
Thus \(\mathbb C(x,y,z)\subseteq Z(D)\), with actual inverses in D.
No assertion identifying D with an abstract tensor product or an abstract rational function skew field is needed.

Conjugation by a and b extends to automorphisms \(\alpha,\beta\) of D.
On the generating group algebra they satisfy
\[
\begin{array}{c|ccccc}
 &u&v&x&y&z\\\hline
 \alpha&u&v&x&y^{-1}&z^{-1}\\
 \beta&u&v&x^{-1}&y&z^{-1}.
\end{array}
 \tag{7}
\]
Since \(a^2=x\) and \(b^2=y\) are central in D, both automorphisms are involutions on D.
They commute because the commutator of a and b belongs to N, which is central in H and D.
The actual four-coset algebra is
\[
 \mathscr A=D+Da+Db+Dab\subseteq\mathcal U(G),
 \tag{8}
\]
with relations
\[
 ad=\alpha(d)a,\qquad bd=\beta(d)b,\qquad
 a^2=x,\qquad b^2=y,\qquad (ab)^2=z,
 \qquad ba=ab\,xy^{-1}z^{-1}.
 \tag{9}
\]
The final relation is written with its translation coefficient on the right, exactly as in [L_A0024_v1](../ledger/Yin_L_A0024_v1.md#the-actual-left-matrices-and-right-semilinear-symmetries).
The direct product makes every one of these identities unchanged from P.
For instance u and v are fixed by (7), so moving them across a or b creates no additional cocycle factor.
These equations determine the actual multiplication of all four representatives and retain all three square translations.

The sum in (8) is direct, and this assertion does not assume division of \(\mathscr A\).
Apply the finite-coset bounded-denominator argument already retained in [L_A0003_v1](../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding) to a relation among its four terms.
A common bounded left denominator in \(\mathcal N(H)\), invertible in \(\mathcal U(H)\), makes all four coefficients bounded.
Applying the resulting relation to \(\delta_e\) separates the four orthogonal coset spaces.
The separating-vector property on each copy of \(\ell^2(H)\) makes every bounded coefficient zero, and inverting the denominator makes every original coefficient zero.
Thus (8) is the faithful actual crossed product, of dimension four over D on either side.
The same [finite-dimensional inverse-closure argument](../ledger/Yin_L_A0003_v1.md#division-and-rational-closure-comparison), with dimension four in place of two, identifies it with both actual division and rational closures of \(\mathbb CG\).
Explicitly, left multiplication by any ambient-invertible matrix over \(\mathscr A\) is an injective endomorphism of a finite-dimensional right D-space, hence is surjective and supplies its inverse within the same matrix algebra.
The reverse inclusion holds because D is generated from \(\mathbb CH\) by actual inverses and the four representatives lie in G.

This completes the independent coefficient-division and actual-cocycle inputs for a specific noncommutative candidate.
It does not make D finite over a central field or supply the remaining index criterion.

## Explicit failure of every finite central dimension in the candidate

For every positive integer m set
\[
 g_i=u^iv\in F_2\qquad(1\leq i\leq m).
\]
The product associated with a permutation is the positive reduced free-group word
\[
 g_{\pi(1)}\cdots g_{\pi(m)}
   =u^{\pi(1)}v\,u^{\pi(2)}v\cdots u^{\pi(m)}v.
 \tag{10}
\]
Its consecutive u-run lengths recover the entire permutation.
Thus the \(m!\) words in (10) are pairwise distinct, and
\[
 s_m(g_1,\ldots,g_m)\ne0\quad\text{in }\mathbb CF_2.
 \tag{11}
\]
The inclusion \(\mathbb CF_2\subseteq\mathbb CH\subseteq D\) is faithful, so (11) remains nonzero in D and in \(\mathscr A\).
If D, \(\mathscr A\), or any containing algebra were finite-dimensional d over a central field, (3) with \(m=d+1\) would contradict (11).
The same contradiction excludes faithful embedding of these full algebras in any algebra finite-dimensional over a central field.
This explicit obstruction needs no assertion about the exact center of D and does not use the group-algebra classification theorem.
The candidate group is itself not virtually abelian.
Otherwise a finite-index abelian subgroup of G would intersect its copy of \(F_2\) in a finite-index abelian subgroup, which would contain positive powers of both u and v.
Those powers do not commute, since their two ordered products are distinct reduced free-group words.

The target G is already covered independently of this obstruction.
Its normal subgroup \(F_2\times\{1\}\) is free and its quotient is P, which is elementary amenable because it is an extension of \(\mathbb Z^3\) by \(C_2^2\).
Lin93 Theorem 1.3 therefore applies to G itself.
This final application is a coverage comparison, not the premise used earlier to establish division of D.
Consequently the candidate supplies a precise test of the proposed input chain but no new group-class conclusion.

There is also a direct algebraic warning against transplanting the earlier coefficient calculation unchanged.
Over the commutative field F, [L_A0028_v2](../ledger/Yin_L_A0028_v2.md#an-elementary-coefficient-division-ring-and-the-exact-mixed-equation) uses
\[
 (f+gb)(\beta(f)-gb)=f\beta(f)-yg\beta(g).
 \tag{12}
\]
For arbitrary \(f,g\in D\), with b acting by \(\beta\) and \(b^2=y\), the actual expansion is instead
\[
 (f+gb)(\beta(f)-gb)
  =f\beta(f)-yg\beta(g)+(gf-fg)b.
 \tag{13}
\]
Indeed the two cross terms are \(-fgb\) and \(gb\beta(f)=gfb\).
Taking \(f=u\) and \(g=v\), the extra coefficient \(vu-uv\) is nonzero by free-group linear independence.
Thus even the elementary norm formula preceding the Albert reduction cannot be reused merely by replacing F with D.
The coefficient-division theorem for H does not remove this commutator term.

## What a finite-input escape would actually require

Suppose \(\Gamma=\langle h_1,\ldots,h_r\rangle\) is finitely generated.
If a central-finite algebra inside the actual affiliated algebra contains all of
\[
 h_1,h_1^{-1},\ldots,h_r,h_r^{-1},
 \tag{14}
\]
then its complex subalgebra contains \(\mathbb C\Gamma\) faithfully.
The obstruction above therefore makes \(\Gamma\) virtually abelian.
It is enough for the proposed algebra to contain the entries of the single finite row whose entries are (14).
Allowing its dimension or central field to depend on that row does not change this conclusion.
An entrywise faithful matrix model over a central-finite algebra has the same limitation, since its finite matrix algebra is again central-finite.

This statement is deliberately narrower than an obstruction to every finite-dimensional invariant.
An auxiliary quaternion algebra, quadratic form, determinant, quotient, or finite-dimensional representation attached to one expression need not contain the actual group algebra injectively.
The biquaternion in C_A0013 is itself handled through an exact anisotropy equivalence rather than a claimed isomorphism to the crossed product.
Such an auxiliary construction can therefore escape the embedding obstruction in principle.
To advance beyond it, one must derive the auxiliary object from the noncommutative actual cocycle and prove an implication controlling every relevant kernel or rational idempotent.
A faithful model for all support units is excluded in the non-virtually-abelian case; an invariant that forgets those units still needs a proved back-transfer.
Neither finiteness of the original matrix nor existence of the abstract auxiliary algebra supplies that missing implication.

The screened proposal to extend Siv10 simply by imposing central-finiteness on the independently controlled coefficient division ring should be rejected for new group coverage.
A useful reopening input would be an actual non-virtually-abelian finite extension with independently established coefficient division, together with a specific finite-dimensional invariant or a valuation theorem that genuinely applies to its infinite-dimensional coefficient ring and has a complete back-transfer.
The present work establishes no such construction and leaves the arbitrary torsion-free Task unresolved.

## Source inspection and retention scope

The local comparison read C_A0013_v1, R_A0037_v5, the actual-model and coefficient sections of L_A0028_v2 and L_A0024_v1, L_A0003_v1, S_A0007, S_A0001, and the applicable Lin93 and Lin00 source evidence.
A bounded search of local A-series and source materials for polynomial identities, finite central dimension, virtual abelianness and Passman found no adequate existing account of the new obstruction.
The external search on 2026-11-12 used "Passman group algebra polynomial identity characteristic zero abelian subgroup finite index" and the title of the polynomial-identity papers, stopping when the exact applicable original was obtained.

The new source is Donald Steven Passman, *Group rings satisfying a polynomial identity. II*, Pacific Journal of Mathematics 39(2) (1971), 425--438, DOI [10.2140/pjm.1971.39.425](https://doi.org/10.2140/pjm.1971.39.425).
The publicly available [publisher PDF](https://msp.org/pjm/1971/39-2/pjm-v39-n2-p09-s.pdf) was retained locally as [Pas71--journal.pdf](../literature/pdf/Pas71--journal.pdf).
Its metadata and first article page match the title, author, volume and issue; the file has 17 pages including the publisher cover and back matter, with the 14 article pages numbered 425--438.
The actual text read was the twisted-algebra definition on p. 425, Theorem 1.4 and its argument on pp. 427--428, and Corollary 1.5 with its preceding characteristic-zero explanation on p. 428.
Corollary 1.5 is accepted as an external theorem at statement and exact-applicability depth.
The proof invokes earlier work and a finite twisted-group-algebra semisimplicity result; those original proofs were not recursively audited.
No general redistribution licence is inferred from public publisher access.

The authoring agent checked the dimension argument (2)--(3), the finite-index deduction (4), every hypothesis in the two separate Lin93 applications, the unchanged actual cocycle (7)--(9), the free-word noncancellation (10)--(11), and the noncommutative expansion (13).
The source inspection described here was ordinary checking within development; the separate independent review records its own direct inspection and accepted source-proof limits.
The virtual-abelianness conclusion is a direct application of the established source theorem, so this account makes no claim to a new polynomial-identity theorem and does not require a separate Claim merely to restate it.

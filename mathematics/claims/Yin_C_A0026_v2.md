---
author: Yin
---
# One residual product fiber, multiplicative lifts and exact-support transfer

## Statement

Let \(A=\{x_1,\ldots,x_a\}\) and \(B=\{y_1,\ldots,y_b\}\) be finite nonempty sets of distinct elements of a group \(G\).
All fibers below are the actual fibers of \((i,j)\mapsto x_i y_j\).
An exact-support solution has nonzero coefficients at every specified row and column.
Torsion-freeness is not needed for the transfer statements; it is needed to interpret the complex solution as a counterexample to [A0002](../tasks/Yin_T_A0002_v1.md#contract).
The [unit and norm tests of the earlier version](Yin_C_A0026_v1.md#coefficient-table-and-statement), its [one-direction gcd test](Yin_C_A0026_v1.md#exact-test-with-one-remaining-direction), and the [saturated triple obstruction](Yin_C_A0025_v1.md#statement) retain their separate scopes.

### A multiplicative lift detected by the reversed product

Suppose \(p\) is odd and
\[
 \alpha=\sum_i u_i x_i,\qquad \beta=\sum_j v_j y_j,\qquad
 u_i,v_j\in\mathbb F_q^\times,\quad q=p^f,\qquad \alpha\beta=0.
\]
Fix \(g_*\in G\).
Suppose that, in every actual product fiber other than \(g_*\), its cells can be partitioned into pairs whose coefficient products are opposite:
\[
                  u_i v_j=-u_k v_\ell.                         \tag{1}
\]
Fibers of size two automatically meet this condition.
If
\[
                         \beta g_*^{-1}\alpha\ne0,             \tag{2}
\]
then the multiplicative lifts of all coefficients to \((q-1)\)-st roots of unity already give an exact-support zero product over \(\mathbb Q(\zeta_{q-1})\).
At a suitable place above \(p\), these coefficients are units and reduce to the specified point.
Thus neither a large-prime bound nor any restriction on a pair-lattice index is needed.
A singleton fiber at a nonidentity element of the reversed table
\[
                    (j,i)\longmapsto y_j g_*^{-1}x_i
\]
suffices for (2).
For a witness over an arbitrary field of odd characteristic, the same hypotheses imply existence of an exact-support complex zero product after finite-field specialization preserving (1) and one nonzero reverse coefficient.
This last statement does not assert specialization through the original point when its coefficients are transcendental over \(\mathbb F_p\).

### Exactly one larger fiber

Suppose every actual product fiber has two cells, except for a single fiber \(F_*\) of size greater than two.
Put \(M=\mathbb Z^{A\sqcup B}\), with separate basis vectors for rows and columns, and \(v_{ij}=e_i+f_j\).
Choose an oriented difference \(d_t\) in each two-cell fiber and put
\[
 L=\langle d_t\rangle_{\mathbb Z},\qquad
 S=(L\otimes_{\mathbb Z}\mathbb Q)\cap M,\qquad
 Q=M/S.
\]
Assume the pair equations are consistent in odd characteristic, equivalently
\[
 \sum_t n_td_t=0\ \Longrightarrow\ \sum_t n_t\equiv0\pmod2.
                                                                    \tag{3}
\]
They prescribe a character \(\chi:L\to\{1,-1\}\) with \(\chi(d_t)=-1\).
Let \(e\) be the exponent of \(S/L\), using \(e=1\) if it is trivial, and set \(N=2e\).
Choose a splitting \(M=S\oplus U\), where \(U\cong Q\), and write
\[
 e_i=s_i+a_i,\quad f_j=t_j+b_j,\qquad s_i,t_j\in S,\ a_i,b_j\in U.
\]
For a branch \(\rho:S\to k^\times\) extending \(\chi\), over an algebraically closed field \(k\) of characteristic different from two, define Laurent polynomials on the torus with character lattice \(U\):
\[
 U_\rho(T)=\sum_i\rho(s_i)T^{a_i},\qquad
 V_\rho(T)=\sum_j\rho(t_j)T^{b_j},\qquad
 F_\rho(T)=\sum_{(i,j)\in F_*}\rho(s_i+t_j)T^{a_i+b_j}.
                                                                    \tag{4}
\]
Combine terms with equal exponent before testing their monomial support.
Then
\[
                         F_\rho=U_\rho V_\rho.                 \tag{5}
\]
An exact-support solution exists on this branch if and only if \(F_\rho\) is zero or has at least two nonzero monomials.
Equivalently, it fails to exist precisely when both \(U_\rho\) and \(V_\rho\) are nonzero scalar monomials.
This criterion permits any number of independent directions in \(Q\).

For an odd prime \(p\), set \(N_p=N/p^{v_p(N)}\).
Every characteristic-\(p\) pair branch \(\bar\rho\) lifts to a characteristic-zero branch \(\rho_0\) with values in \(\mu_{N_p}\), preserving reduction at a suitable prime of \(\mathbb Q(\zeta_{N_p})\).
This remains true when \(p\mid[S:L]\).
For a fixed prime of \(\mathbb Q(\zeta_N)\) and fixed residue embedding, all lifts of \(\bar\rho\) are
\[
 \rho_0\psi,\qquad
 \psi\in\operatorname{Hom}\bigl((S/L)_{(p)},\mu_{p^{v_p(N)}}\bigr).
                                                                    \tag{6}
\]
Here \((S/L)_{(p)}\) is the \(p\)-primary subgroup, and \(\psi\) is extended trivially on the prime-to-\(p\) part.
There are exactly \(|(S/L)_{(p)}|\) such lifts.

In particular, an exact-support characteristic-\(p\) witness transfers to characteristic zero whenever \(F_{\bar\rho}\ne0\).
For a finite-field witness in this case, a number-field unit lift through the same residue point exists, allowing ramification.
When \(F_{\bar\rho}=0\), existence of a complex point and lifting the specified residue point remain distinct questions.

### Exceptional primes and class-size bounds

Suppose there is no complex exact-support solution on the given table.
For every complex pair branch write
\[
 U_\rho=\alpha_\rho T^{a_\rho},\qquad
 V_\rho=\beta_\rho T^{b_\rho},\qquad
 \alpha_\rho\beta_\rho\ne0.
                                                                    \tag{7}
\]
All branch values belong to \(E=\mathbb Q(\zeta_N)\), and the displayed coefficients are algebraic integers.
Define the nonzero positive integer
\[
 \Delta=\prod_{\rho}
       \left|N_{E/\mathbb Q}(\alpha_\rho\beta_\rho)\right|,
                                                                    \tag{8}
\]
where the product is over all complex branches extending \(\chi\).
The odd characteristics admitting an exact-support solution over their algebraic closures are exactly the odd prime divisors of \(\Delta\).
Using one representative from each Galois orbit of branches gives the same set of prime divisors.
This is a finite exact test, not a polynomial-time claim about enumerating the branches.

There is a simpler cutoff that uses only exponent-class sizes.
Let
\[
 q_A=\max_{u\in Q}\#\{i:\bar e_i=u\},\qquad
 q_B=\max_{u\in Q}\#\{j:\bar f_j=u\},\qquad
 q_*=\max_{u\in Q}\#\{(i,j)\in F_*:\bar v_{ij}=u\},
\]
and put \(q_0=\min(q_*,\max(q_A,q_B))\).
If an exact-support solution exists in odd characteristic \(p\) and
\[
 p^{f_p}>q_0^{D_p},\qquad
 D_p=\varphi(N_p),\qquad f_p=\operatorname{ord}_{N_p}(p),
                                                                    \tag{9}
\]
then an exact-support complex solution exists.
Use \(D_p=f_p=1\) if \(N_p=1\).
The marginal bound \(\max(q_A,q_B)\) does not involve the size of the larger fiber.
The remaining bound \(q_*\) can be better, so both are retained.

For a particular lifted branch in the failure case (7), one can replace \(q_A,q_B,q_*\) by the sizes of its actual surviving exponent classes, or use the computed coefficient norms directly.
A singleton class among the exponents of \(F_*\) rules out exceptional odd characteristics altogether.
The same conclusion holds if each of the two marginal exponent lists has a singleton class.
If either marginal list has two distinct singleton classes, consistency of the pair equations alone already supplies a complex exact-support solution.

## Multiplicative lifts and the reverse identity

Choose a prime of \(\mathbb Q(\zeta_{q-1})\) and a residue embedding identifying its \((q-1)\)-st roots of unity with \(\mathbb F_q^\times\).
Reduction is an isomorphism on these roots because \(p\nmid(q-1)\).
Its inverse \(\omega:\mathbb F_q^\times\to\mu_{q-1}\) is multiplicative and satisfies \(\omega(-1)=-1\), since \(p\) is odd.
Set
\[
 \widetilde\alpha=\sum_i\omega(u_i)x_i,\qquad
 \widetilde\beta=\sum_j\omega(v_j)y_j.
\]
Every pair in (1) cancels exactly after this lift.
Thus
\[
                 \widetilde\alpha\widetilde\beta=cg_*,
                 \qquad c\equiv0\pmod{\mathfrak p}.           \tag{10}
\]
Suppose \(c\ne0\).
The complex group algebra is directly finite: its faithful left-regular representation lies in a finite von Neumann algebra.
For completeness, a bounded right inverse makes an operator surjective; polar decomposition and equality of the traces of its initial and final support projections then make its kernel projection zero.
It is therefore bijective and its right inverse is also its left inverse.
Applying this to
\[
        \widetilde\alpha\bigl(c^{-1}\widetilde\beta g_*^{-1}\bigr)=1
\]
gives
\[
                   \widetilde\beta g_*^{-1}\widetilde\alpha=c1.
                                                                    \tag{11}
\]
Both sides of (11) have coefficients in the same cyclotomic integer ring: it is an exact identity there, even though its proof used division by \(c\) over \(\mathbb C\).
Reducing it gives \(\beta g_*^{-1}\alpha=0\), contradicting (2).
Hence \(c=0\), proving the same-point multiplicative lift.
A singleton reverse fiber has a nonzero coefficient because all input coefficients are nonzero.

The same argument works for any algebraic-integer lifts of the given nonzero factors whose product is supported on at most one group element.
These lifts need not preserve exact support if some of their nonzero coefficients vanish after reduction.
Oddness is needed only to construct the multiplicative lift from (1), not for this more general reverse-identity argument.

For a witness over an arbitrary field of characteristic \(p\), retain the finite actual product and reverse-product tables.
Impose the full zero-product equations, the chosen opposite-pair equations, inverse equations for every row and column coordinate, and an inverse equation for one reverse coefficient known to be nonzero.
This finite polynomial system over \(\mathbb F_p\) has a point over the given field, so its ideal is proper.
The weak Nullstellensatz gives a point over \(\overline{\mathbb F}_p\), whose finitely many coordinates lie in one finite field.
The preceding construction applies there.
Asymmetry of a zero product alone is not a general criterion for failure of direct finiteness; the argument uses the one-output identity (10) in characteristic zero.

## The single residual Laurent equation

Condition (3) is precisely the [integer character-consistency criterion](Yin_C_A0022_v1.md#equal-moduli-for-the-paired-coefficient-equations).
It makes \(\chi\) well defined, and Smith normal form extends it to \(S\).
A branch has \(\rho(u)^{2e}=1\) for every \(u\in S\), since \(eu\in L\).
Thus the characteristic-zero branches are a finite set with values in \(\mu_N\).

Because \(S\) is saturated, \(Q\) is free abelian and the chosen splitting exists.
Every extension of \(\rho\) to a character \(z:M\to k^\times\) is specified by a torus point on \(U\).
Its original row and column coefficients are \(\rho(s_i)T^{a_i}\) and \(\rho(t_j)T^{b_j}\), all nonzero.
The two terms in a paired fiber have the same exponent in \(Q\) and opposite branch coefficients.
They therefore cancel as Laurent polynomials, not only at one torus point.
Expanding \(U_\rho V_\rho\) and deleting those zero sums proves (5).
It is also the augmentation identity for the group-ring product.

A nonzero scalar monomial has no zero on a torus.
Conversely, for a Laurent polynomial with at least two surviving exponent vectors, choose an integer linear functional taking distinct values on those vectors.
The one-parameter substitution associated with that functional gives a Laurent polynomial with at least two terms and no combined exponents.
After a monomial shift it is a nonconstant ordinary polynomial with nonzero constant term.
Over an algebraically closed field it has a nonzero root.
The corresponding torus point solves the original Laurent equation.
Finally, the units in a Laurent polynomial ring over a field are exactly its nonzero scalar monomials.
For example, if a product were a unit and a factor had two terms, the preceding torus-zero argument would contradict invertibility.
Since this ring is a domain, (5) proves all branch criteria, including the case where one marginal vanishes identically.

## Lifting pair branches, including index-dividing primes

Fix a characteristic-\(p\) branch \(\bar\rho\), with \(p\) odd.
Its values have order dividing \(N_p\), since a field of characteristic \(p\) has no nontrivial \(p\)-power roots of unity.
At a prime of \(E_0=\mathbb Q(\zeta_{N_p})\), choose a residue embedding into \(\overline{\mathbb F}_p\).
Reduction identifies \(\mu_{N_p}\) with the group of \(N_p\)-th roots in that algebraic closure.
Indeed it is injective: a nontrivial prime-to-\(p\) root of order \(d\) reducing to one would make \(1+\zeta+\cdots+\zeta^{d-1}=0\) reduce to \(d=0\), a contradiction.
Both root groups have \(N_p\) elements, so it is also surjective.
Lift each value of \(\bar\rho\) through this multiplicative isomorphism.
The resulting \(\rho_0\) is a character, and its restriction to \(L\) is exactly \(\chi\), because the reductions of \(1,-1\) remain distinct.

In \(E=\mathbb Q(\zeta_N)\), the kernel of reduction on \(\mu_N\) is exactly its \(p\)-primary subgroup.
The quotient of any two branches lifting \(\bar\rho\) is trivial on \(L\) and has values in this kernel.
Conversely every such character can multiply \(\rho_0\).
This proves (6), with the cardinality obtained by decomposing the finite abelian \(p\)-group into cyclic factors.
No assumption that \(p\) avoids \([S:L]\) has entered.

If \(F_{\bar\rho}\ne0\) and has a torus zero, it has at least two nonzero monomials.
Those coefficients are nonzero in every lift, so \(F_{\rho_0}\) also has at least two monomials and supplies a complex solution.
For the stronger marked-point statement, work over the valuation ring \(\mathcal O_{E_0,\mathfrak p}\) and put \(R=\mathcal O_{E_0,\mathfrak p}[U]\), the Laurent polynomial ring.
The reduction of \(F_{\rho_0}\) is nonzero.
If a uniformizer \(\pi\) satisfies \(\pi H=F_{\rho_0}K\), reduction in the Laurent polynomial domain over the residue field gives \(\bar K=0\).
Dividing \(K\) by \(\pi\) proves \(H\in(F_{\rho_0})\).
Iteration shows
\[
                  (F_{\rho_0}):\pi^\infty=(F_{\rho_0}).
\]
The horizontal-specialization argument in [C39](Yin_C_A0039_v1.md#horizontal-specialization) applies over this localization of a number ring just as over \(\mathbb Z_{(p)}\).
At the finite-field torus point it gives a number-field specialization whose coordinates are local units and have the prescribed residues, after a residue-field extension.
Reconstructing the row and column coefficients by their monomials preserves the entire original point and every support label.
This argument does not assert an unramified or a multiplicative lift of the torus coordinates.

## Norms and exceptional characteristics

Assume first that no complex exact-support solution exists.
The branch criterion forces (7) on every branch.
If an odd-characteristic exact-support solution exists, lift its branch as above to some \(\rho\) in \(E\) at a prime \(\mathfrak p\) above \(p\).
Reduction of its residual polynomial is the monomial
\[
             \overline{\alpha_\rho\beta_\rho}
                        T^{a_\rho+b_\rho}.
\]
Having a torus zero forces \(\alpha_\rho\beta_\rho\in\mathfrak p\).
Hence \(p\) divides the corresponding integer norm and therefore \(\Delta\).
Conversely, if \(p\) divides one of these norms, a prime \(\mathfrak p\) above \(p\) contains that coefficient.
Reduction of the branch still solves all pair equations, while its residual polynomial is identically zero.
Choosing all free torus coordinates to be one gives an exact-support solution over a finite residue field.
This proves the exact exceptional-prime assertion.
Galois conjugation permutes branches and does not change the relevant rational norm, proving the orbit reduction.

For the bound (9), suppose instead that a given characteristic-\(p\) witness fails to yield any complex exact-support solution and take its prime-to-\(p\) lift \(\rho_0\) in \(E_0\).
Write its marginals as \(\alpha T^u,\beta T^v\).
The residue degree of the chosen prime of \(E_0\) is \(f_p\): the reduction of \(\zeta_{N_p}\) has order \(N_p\), and the smallest finite field containing it has degree \(\operatorname{ord}_{N_p}(p)\).
The equality \(\overline{\alpha\beta}=0\) makes at least one of \(\alpha,\beta\) lie in that prime.
For each nonzero algebraic integer \(\lambda\) in the prime,
\[
                 p^{f_p}\le |N_{E_0/\mathbb Q}(\lambda)|.
                                                                    \tag{12}
\]
If its marginal exponent class has \(h\) terms, \(\lambda\) is a sum of \(h\) roots of unity.
Every complex conjugate has modulus at most \(h\), so
\[
                 |N_{E_0/\mathbb Q}(\lambda)|\le h^{D_p}.
                                                                    \tag{13}
\]
Using \(\lambda=\alpha\) or \(\beta\) yields \(p^{f_p}\le\max(q_A,q_B)^{D_p}\).
Using the nonzero residual coefficient \(\lambda=\alpha\beta\), a sum over one exponent class of \(F_*\), also yields \(p^{f_p}\le q_*^{D_p}\).
This proves (9) and its branch-specific refinements.

A singleton exponent class has a root of unity as its coefficient, which never vanishes in any characteristic.
If \(F_*\) has such a class and its characteristic-zero polynomial is a monomial, that coefficient must be the surviving one and cannot disappear on reduction.
If both marginals have singleton classes and both are monomials, both surviving coefficients are roots of unity and neither can disappear.
These observations prove the two unconditional odd-prime transfer criteria.
Two distinct singleton classes in one marginal keep it nonmonomial on every branch, proving the last assertion.

## A cyclic table with a collapsing pair branch

Let \(G=C_7=\langle z\rangle\), and take row exponents \(0,1,2,4\) and column exponents \(0,-1,-2,-4\).
The identity fiber has four diagonal cells.
Every other group element has exactly two representations.
Normalize the coefficients at exponent zero to one and index the remaining column coefficients by the corresponding positive row exponent.
The six pair equations are
\[
\begin{gathered}
 u_1+u_2v_1=0,\qquad v_1+u_1v_2=0,\qquad
 u_2+u_4v_2=0,\\
 v_2+u_2v_4=0,\qquad u_4v_1+v_4=0,\qquad
 u_1v_4+u_4=0.
\end{gathered}
\]
Using nonzero coordinates, the first four give
\[
 u_2=-u_1/v_1,\quad v_2=-v_1/u_1,\quad
 u_4=-u_1^2/v_1^2,\quad v_4=-v_1^2/u_1^2.
\]
The last two imply \(u_1^4=-v_1^3\) and \(v_1^4=-u_1^3\).
Multiplying them and cancelling nonzero factors gives \(u_1v_1=1\), and then \(u_1^7=-1\).
Thus all pair solutions are
\[
 u=(1,t,-t^2,-t^4),\qquad
 v=(1,t^{-1},-t^{-2},-t^{-4}),\qquad t^7=-1.
\]
The remaining identity coefficient is \(1+1+1+1=4\).
There is no exact-support zero product on these supports in any odd characteristic or in characteristic zero.
In characteristic two the displayed solutions do give zero products.
The normalized pair exponent matrix has determinant of absolute value \(7\), so \([S:L]=7\).
At \(p=7\), its seven characteristic-zero branches all reduce to \(t=-1\), while the residual coefficient remains nonzero.
This verifies that branch collapse at an index-dividing odd prime need not create a zero product.
It is a diagnostic in a group with torsion, not a torsion-free construction.

<a id="the-witnesses-in-mghirbi-douglas-section-75"></a>
## The witnesses in Mghirbi–Douglas Section 7.5

[Mghirbi–Douglas, Proposition 7.11, PDF page 30](../literature/pdf/MD26.pdf#page=30), gives \(a,b,c\in\mathbb F_p[H]\) with
\[
                  ab=1,\qquad ac=0,\qquad c\ne0
\]
under its stated root-protection hypothesis.
For every \(g\in H\),
\[
                  (cg^{-1}a)b=cg^{-1}\ne0.
\]
Thus the reversed product needed in (2) is automatically nonzero.
For odd \(p\), if all but one actual fiber of the collected \(a,c\) table admits the opposite-term pairing (1), the multiplicative lift theorem would supply a complex zero product with exactly those collected supports and prescribed residues.
The proposition does not supply this pairing condition.
The geometric and probabilistic hypotheses establishing the source witnesses are not re-audited here.

There is a definite obstruction to obtaining that shortcut from the source's original integer occurrence sums.
Write those sums before reduction as
\[
 A_{\mathbb Z}=\sum_{x\in A'}\sigma(x)g_x,\qquad
 C_{\mathbb Z}=\sum_{y\in B'}h_y^{-1}.
\]
Their reductions are \(a,c\), with repeated labels collected in the group ring.
The augmentation \(\varepsilon(A_{\mathbb Z})\) is nonzero modulo \(p\), since \(\varepsilon(a)\varepsilon(b)=1\).
Also \(\varepsilon(C_{\mathbb Z})=|B'|>0\) as an integer.
Hence \(A_{\mathbb Z}C_{\mathbb Z}\ne0\) by its nonzero augmentation.
All its integer coefficients are divisible by \(p\), because \(ac=0\).
It cannot be supported at just one group element: the general lift argument following (11), with the automatically nonzero reverse product, would force it to vanish.
Therefore it has at least two nonzero group coefficients, each divisible by \(p\).
This conclusion is deterministic and uses neither typicality nor a support-size estimate.
In particular, exact balance of the integer signs outside a single output cannot occur for these particular occurrence lifts.

For the canonical multiplicative lifts of the collected pair \(a,c\), the augmentation of the lift of \(a\) is again nonzero, since its reduction is \(\varepsilon(a)\ne0\).
If one nonzero coefficient value of \(c\) occurs on more than half of its actual support, the augmentation of its multiplicative lift is nonzero as well.
Indeed its equal root-of-unity terms have total modulus exceeding the sum of the moduli of all remaining terms.
In this case the lifted product is nonzero by augmentation and the same reverse argument forces at least two nonzero output coefficients.
Thus the opposite-pair shortcut is also impossible under that dominance hypothesis.
Without dominance, the actual cyclotomic augmentation and the complete output table must still be checked.
Occurrence coefficients, collected coefficients and their multiplicative lifts cannot be interchanged: the multiplicative lift preserves products, not addition.

## Assessment history

### Decision one-residual-fiber

| Field | Value |
| --- | --- |
| date | 2026-11-21T03:45 |
| status | proved |
| reason | Independent inspection supports the entire statement and argument at their stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact-support transfer, branch classification, exceptional norms and reverse-product criterion. |
| argument | [Proof](#multiplicative-lifts-and-the-reverse-identity) | Complete proof including finite-field descent, marked lifts, class bounds, cyclic example and source application. |
| review | [Whole finding](../audits/reviews/Yin_R_A0057_v2.md#whole-finding) | Complete independent finding on the final proof and direct inputs. |
| dependency | [Marked-point specialization](Yin_C_A0039_v1.md#horizontal-specialization) | Horizontal point over a localization of a number ring with finite residue field. |
| dependency | [MD26 source interface](../audits/literature/MD26/Yin_U001.md#md26-u001) | Actual root-protected source witnesses and original occurrence signs in Proposition 7.11. |

## Current assessment

[Selected decision](#decision-one-residual-fiber)

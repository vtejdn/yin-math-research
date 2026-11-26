---
author: Yin
---

# A group-independent gap at noncyclic order twenty when the five character ranks are at most two

## Statement

There is an absolute \(\epsilon>0\) with the following property.
Let \(H=\langle g,h\rangle\) be torsion-free and assume its nonzero complex group-ring scalars act injectively in the regular representation.
Suppose it has the marked noncyclic quotient \(C_5\times C_2^2\) of the [five sign squares](Yin_C_A0333_v1.md#statement).
For any two-square rectangle with noninteger regular nullity \(\delta\), form the [four-square commutator on the common index-four subgroup](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator).
If all five quotient characters of that subgroup give numerical rank at most two, then
\[
                                \delta\le\tfrac12-\epsilon .
\]
The bound is uniform in the group, the four complex coefficient matrices, and the two normalized orientations.
It removes the approximation hypothesis in the [earlier uniform gap](Yin_C_A0343_v2.md#statement).
The proof gives no numerical value of \(\epsilon\).
If the character condition fails, a half kernel would force a strict group-ring inner rank drop on this subgroup by the [second-layer basis](Yin_C_A0331_v2.md#statement).

The finite-parameter degenerations in the proof are tested on marked limits which need not be scalar-injective.
For the other degeneration there is a separate quantitative conclusion: on the normalized prototypes the nullity is \(O(|d|^{-1/2})\) as the trace parameter \(d\) tends to infinity, uniformly on all noncommuting torsion-free markings with the two signs.
Here \(d=\operatorname{tr}(M(0)M(\infty))\).
The estimate at infinity applies without imposing the five numerical rank inequalities.

## The limiting group and the two trace identities

Suppose groups and rectangles violating any such uniform gap exist.
The order-twenty upper bound gives a sequence with \(\delta_n\to1/2\).
By the [two-end and determinant argument above two fifths](Yin_C_A0343_v2.md#the-determinant-reduction-above-two-fifths), pass to one normalized orientation and sign and use prototypes \(M_n=N_n/q\), \(q(y)=y^2-s_0y+2,\ s_0=\pm\sqrt5\).
The [Clifford budget](Yin_C_A0342_v1.md#statement) makes the parameters \(d_n\) real for all sufficiently large \(n\).
Each group has the following word inequalities by the [cyclic denominator elimination](Yin_C_A0343_v1.md#which-group-words-can-contribute-to-the-trace):
\[
 \langle h\rangle\cap g\langle h\rangle g^{-1}=\{1\},\qquad
                g^{-1}h^i g^{-1}h^j\ne1\quad (i,j\in\mathbb Z).
\]
That argument needs only noninteger nullity to exclude indicability and a normalized cyclic power.

Take a subsequence for which satisfaction of each fixed word relation stabilizes, by diagonal extraction in the free group on the two marks.
The stabilized relations form the kernel of a marked quotient \(H_*\).
It is torsion-free: if \(w^k=1\) in it for some \(k>0\), the relation holds eventually, hence \(w=1\) holds eventually.
The actual marking characters survive since every limiting relation maps trivially to the fixed finite marked quotient.
Infinite order of \(h\), the trivial cyclic intersection and the two-step inequalities survive by stabilization of their individual word tests.
Thus the two [trace formulas for cyclic Laurent coefficients](Yin_C_A0343_v1.md#which-group-words-can-contribute-to-the-trace) hold in \(H_*\).
We use these properties of the limit independently of scalar injectivity there.

## Bounded parameters including the three degenerate forms

If a subsequence satisfies \(d_n\to d_*\in\mathbb R\), use the eight-square group-ring pencil \(K(d)\) of the [exterior algebra construction](Yin_C_A0342_v1.md#a-linear-pencil-on-eight-coordinates).
Its entries are polynomials in \(d\) with fixed finite group support.
The regular spectral measures of \(K(d_n)^*K(d_n)\) in the changing groups converge weakly to that of \(K(d_*)^*K(d_*)\) in \(H_*\).
Indeed every moment is a finite word sum with convergent coefficients and eventually constant word traces, and the operators have a uniform norm bound.
With the trace normalized on group coordinates only, upper semicontinuity of the mass of \(\{0\}\) gives
\[
                    2=\lim 4\delta_n\le\dim_{H_*}\ker K(d_*).
\]

If \(d_*\notin\{1/2,2,5/2\}\), the Clifford blocks and the two signs express the right hand side as four times the nullity of a two-square prototype \(M_*(h)-gI\).
Choose the constant metric of the appropriate type by the [Gram classification](Yin_C_A0337_v1.md#signature-and-simultaneous-similarity) and the sign-reversal argument in the [centering construction](Yin_C_A0343_v1.md#centering-a-constant-indefinite-form).
For a definite form use the unitary square \(U^2\) in the definite basis.
For the two indefinite cases use \(W^2\) and \(V\) in the centered scattering bases.
In each case the tracial computations require only the two word identities of the preceding section, and the finite coefficient contradiction requires only the actual marking characters and independence of the three traceless coefficients.
If the two-square nullity is at least \(1/2\), the corresponding unitary has normalized trace zero and mass at least \(1/2\) at one, so its square is the identity.
The contradicting numerical characters are identified in the [fixed-parameter word test](Yin_C_A0343_v2.md#a-word-cutoff-for-each-fixed-real-parameter).
In particular the two-square nullity is strictly less than \(1/2\).

At \(d_*=1/2,2,5/2\) the radical-ideal filtration of the [degenerate Clifford algebra](Yin_C_A0342_v1.md#full-rank-at-a-degenerate-gram-matrix) gives four diagonal two-square blocks of the same quotient type.
We need only that their nullities are strictly below \(1/2\).
For the real basis \(X,Y,Z\) in the [Gram calculation](Yin_C_A0337_v1.md#from-the-boundary-equation-to-three-traceless-matrices), the real form after removing the radical has signature \((1,1)\) at \(1/2\) and \((2,0)\) at \(2,5/2\).
After multiplication of all three by \(i\) the corresponding forms have signatures \((1,1)\) and \((0,2)\).
Each embeds isometrically into the real space of traceless matrices selfadjoint for \(J=\operatorname{diag}(1,-1)\), whose trace-pairing signature is \((1,2)\).
These matrices realize the quotient two-generator Clifford algebra: two orthogonal generators of nonzero square anticommute, and their complex algebra is \(M_2(\mathbb C)\).
Undoing the multiplication by \(i\) gives the negative-sign case \(M_*^*JM_*=-J\) on the circle, with the same \(M_*^2=(p/q)I\), \(p(y)=2y^2-s_0y+1\).
The quotient generators have no common invariant line because they generate the full matrix algebra.
This suffices for the logarithmic centering argument, which uses the absence of a common boundary invariant line.
The [negative-sign scattering contradiction](Yin_C_A0343_v1.md#negative-sign-scattering) then applies unchanged: its final nonzero remainder depends only on \(p,q\) and the marking.
Each diagonal block has nullity strictly less than \(1/2\).
The nullity of a block triangular operator is at most the sum of the diagonal nullities, by projection of its kernel to the last input block and restriction to the kernel of that projection.
This again contradicts the limiting inequality.

## The binomial at infinite parameter

Choose \(u\) with \(u^2=1/d\).
In the scaled numerator \(uN_d\) the required Gram matrix is \(G_1+u^2G_0\), where \(G(d)=dG_1+G_0\) is the [linear Gram matrix](Yin_C_A0342_v1.md#a-linear-pencil-on-eight-coordinates).
At zero \(G_1\) has nonzero entries \(G_{02}=G_{20}=1,\ G_{11}=-2\), indexing from zero.
It is nonsingular, and is realized by the three coefficients of
\[
                     N_\infty(y)=c\binom{1}{y}(-y,\ 1),\qquad c^2=-2 .
\]
An analytic realization of the scaled forms with these limiting matrices is obtained by the change of basis \(S(u)=(I+u^2G_1^{-1}G_0)^{1/2}\), using the convergent square-root series about the identity.
The matrix inside the square root is selfadjoint for the symmetric bilinear form \(G_1\), hence \(S(u)^{\mathsf T}G_1 S(u)=G_1+u^2G_0\).
Taking the three column combinations of the limiting coefficient basis yields a numerator
\[
                        uN_d(y)=N_\infty(y)+O(u^2)
\]
in coefficient norm, uniformly for small \(u\).
The Clifford block decomposition and the \(g\)-sign make its transfer nullity identical to that of any realization of the same signed parameter, also by constant similarity up to sign as in the [comparison of Gram realizations](Yin_C_A0340_v1.md#algebraic-representatives-and-the-sofic-determinant-bound).

Consider \(uN_d(h)-u gq(h)I\), with the same nullity as the rectangle.
Multiply on the left by \(\left(\begin{smallmatrix}1&0\\-h&1\end{smallmatrix}\right)\) and on the right by \(\left(\begin{smallmatrix}0&1\\1&h\end{smallmatrix}\right)\).
These are bounded changes of coordinates with bounded inverses, uniform in the marking.
They send \(N_\infty(h)\) to \(\operatorname{diag}(c,0)\).
The upper-left pivot is now \(cI+O(u)\), with uniformly bounded inverse for small \(|u|\).
The off-diagonal entries are \(O(u)\).
The lower-right entry is
\[
             -u(-h,\ 1)\,gq(h)\binom{1}{h}+O(u^2)
                      =-u(gh-hg)q(h)+O(u^2).
\]
Elimination of the pivot changes this entry by \(O(u^2)\).
After division by \(-u\) and multiplication by \(q(h)^{-1}\) on the right, the remaining scalar differs from \(gh-hg\) by at most \(C|u|\) in operator norm, with an absolute \(C\) for the two normalized signs.
All these steps preserve its kernel dimension.
The uniform inverse bound for \(q(h)\) follows from its two roots having modulus \(\sqrt2\).

In a noncommuting torsion-free marking \(w=(gh)^{-1}hg\) is nonidentity of infinite order.
Since \(gh-hg=gh(I-w)\), its singular distribution is that of \(|1-e^{i\theta}|\) on the Haar circle.
The kernel dimension of a scalar within operator norm \(t\) of this binomial is at most the trace of the binomial's singular projection on \([0,t]\).
Indeed its kernel intersects the spectral complement trivially, so the trace dimension inequality for two projections gives the bound.
For \(0\le t\le2\) this trace is \(2\arcsin(t/2)/\pi\).
It follows that the nullity along the infinite-parameter end is \(O(|d|^{-1/2})\) uniformly in the markings.
All groups in the proposed sequence are noncommuting by the word tests.
The finite-parameter and infinite-parameter alternatives have both contradicted \(\delta_n\to1/2\), proving the uniform gap.

## Assessment history

### Decision the-infinite-parameter-binomial-and-the-absolute-gap

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:25 |
| status | proved |
| reason | The word identities are closed in the marked limit, the three finite degenerations retain a scattering contradiction, and the infinity limit is a uniformly controlled binomial. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The word identities are closed in the marked limit, the three finite degenerations retain a scattering contradiction, and the infinity limit is a uniformly controlled binomial. |
| argument | [The limiting group and the two trace identities](#the-limiting-group-and-the-two-trace-identities) | The limiting group and the two trace identities. |
| argument | [Bounded parameters including the three degenerate forms](#bounded-parameters-including-the-three-degenerate-forms) | Bounded parameters including the three degenerate forms. |
| argument | [The binomial at infinite parameter](#the-binomial-at-infinite-parameter) | The binomial at infinite parameter. |
| dependency | [Earlier result, version 1](Yin_C_A0343_v1.md#statement) | The two indefinite scattering identities and their actual characters exclude all remaining real parameters. |
| review | [Scattering excludes every exceptional determinant line](../audits/reviews/Yin_R_A0236_v1.md#scattering-excludes-every-exceptional-determinant-line) | Independent inspection of the preceding version. |
| dependency | [Earlier result, version 2](Yin_C_A0343_v2.md#statement) | Two extreme corners and an annular word cutoff transfer strict exclusion to coefficient and group gaps. |
| review | [Word cutoffs and the uniform sofic gap](../audits/reviews/Yin_R_A0236_v1.md#word-cutoffs-and-the-uniform-sofic-gap) | Independent inspection of the preceding version. |
| review | [The infinite-parameter binomial and the absolute gap](../audits/reviews/Yin_R_A0236_v1.md#the-infinite-parameter-binomial-and-the-absolute-gap) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-infinite-parameter-binomial-and-the-absolute-gap)

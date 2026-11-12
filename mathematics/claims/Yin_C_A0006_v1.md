---
author: Yin
---
# Arbitrary coefficient kernels inside an admissible inverse-difference array

Date: 2026-11-12 (Asia/Hong_Kong).
This investigation serves [route four](../strategies/Yin_S_A0004.md) of [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract).
It gives an exact limitation of extending the inverse-difference induction from group-element parameters to actual rational Haar-unitary parameters.
All initial cross differences and row differences in the construction are independently units, but its next rational separation has exactly the rank of an arbitrary selfadjoint finite group-ring matrix.
The scalar specialization retains the scalar analytic zero-divisor problem, and the block version retains the full all-size integer-rank problem.
No fractional kernel is exhibited, and no new positive Atiyah group class is claimed.

## Statement

Let \(H\) be a torsion-free group, let \(m\geq1\), and choose
\[
a=a^*\in M_m(\mathbb CH).
\]
Let
\[
\Gamma=\langle t,g\mid tgt^{-1}=g^{-1}\rangle,
\qquad z=t^2,
\qquad G=H\times\Gamma.
\tag{1}
\]
The [existing Klein bottle calculation](../ledger/Yin_L_A0011_v1.md#an-actual-torsion-free-collision-after-one-step) proves that \(\Gamma\) is torsion-free, that \(z\) is central, and that \(t,tg,tg^2\) have infinite order.
Thus \(G\) is torsion-free.
All group symbols below denote their actual left regular unitaries, amplified by \(I_m\) when needed.
The product representation identifies \(\mathcal N(G)\) with \(\mathcal N(H)\,\overline\otimes\,\mathcal N(\Gamma)\), with the product of their canonical traces.
This follows directly by identifying \(\ell^2(G)\) with \(\ell^2(H)\otimes\ell^2(\Gamma)\) and the identity vector with \(\delta_e\otimes\delta_e\).
Write \(U_G=\mathcal U(\mathcal N(G))\).
All matrix ranks and kernel dimensions use the unnormalized matrix trace, so an invertible \(m\)-square block has rank \(m\).
The normalized trace \(\overline\tau_m=m^{-1}\operatorname{Tr}_m\otimes\tau_G\) is used only when stating Haar moments.
All unbounded products and inverses mean closed operations in the actual affiliated matrix algebra.

Choose \(\varepsilon>0\), and set
\[
B=I_m-i\varepsilon a,
\qquad C=I_m+i\varepsilon a,
\qquad q=CB^{-1}.
\tag{2}
\]
Both \(B\) and \(C\) are boundedly invertible independently of the kernel of \(a\).
Indeed \(B^*B=BB^*=C^*C=CC^*=I_m+\varepsilon^2a^2\geq I_m\), and the same lower bound for the adjoint gives surjectivity as well as injectivity.
Since \(B,C\) and their inverses commute, \(q^*q=qq^*=I_m\).
Thus \(q\) is an actual bounded rational unitary, and
\[
I_m-q^2=-4i\varepsilon aB^{-2},
\qquad I_m+q=2B^{-1}.
\tag{3}
\]
These identities use no inverse of \(a\).

Define the three row parameters
\[
x_1=tI_m,
\qquad x_2=tgI_m,
\qquad x_3=q\,tg^2,
\tag{4}
\]
and the three central column parameters \(\lambda_1=2\), \(\lambda_2=3\), \(\lambda_3=4\).
The array of interest is
\[
\mathcal K_a=\bigl((x_i-\lambda_jI_m)^{-1}\bigr)_{i,j=1}^3
\in M_{3m}(U_G).
\tag{5}
\]
Every entry and every inverse explicitly certified below is evaluated from the finite group-ring input \(a,t,g\), with no passage to a formal free field.

All initial cross differences and pairwise row differences are actual units, and each row parameter has the Haar law for the normalized actual trace.
Nevertheless, \(\operatorname{rk}_G\mathcal K_a=2m+\operatorname{rk}_H a\) and \(\dim_G\ker\mathcal K_a=\dim_H\ker a\).
The explicit finite group-ring matrix \(\mathcal P_a\) in (14) has the same rank and nullity.
Consequently integer rank for this entire block-array class is equivalent to the all-size Task, whereas the scalar specialization retains only the scalar analytic zero-divisor question.
The exact next-separation formula, allowed partial block-rank example, and mixed-word limitation below are part of the assertion.

## Argument

### Initial inverse certificates and canonical trace

Each \(x_i\) is unitary because \(q\) commutes with the Klein bottle factor.
Every cross difference \(x_i-\lambda_jI_m\) is boundedly invertible by the norm-convergent Neumann series, since \(\lambda_j>1\).
Every distinct column difference is a nonzero scalar.

The three row differences have the ordered factorizations
\[
x_1-x_2=t(1-g)I_m,
\qquad
x_1-x_3=t(I_m-qg^2),
\qquad
x_2-x_3=tg(I_m-qg).
\tag{6}
\]
For \(r=1,2\) and every nonzero integer \(n\), product-trace factorization gives
\[
\overline\tau_m\bigl((qg^r)^n\bigr)
=\left(m^{-1}\operatorname{Tr}_m\otimes\tau_H\right)(q^n)
\,\tau_\Gamma(g^{rn})=0.
\tag{7}
\]
Here \(q\) commutes with \(g\), while \(g^{rn}\ne e\) by infinite order.
The [retained relative-unitary moment certificate](../ledger/Yin_L_A0011_v1.md#a-relative-path-certificate-and-its-missing-premise) therefore proves \(I_m-qg^r\) injective and affiliated invertible before the next separation is examined.
The same cyclic argument certifies \(1-g\).
Consequently every initial row difference in (6) is independently a unit, regardless of the rank of \(a\).
These inverses need not be bounded.

All three row parameters are individually Haar unitaries for the normalized actual trace.
For \(x_1,x_2\), this is the usual infinite-order group calculation.
For \(x_3\), every nonzero integer \(n\) gives
\[
\overline\tau_m(x_3^n)
=\left(m^{-1}\operatorname{Tr}_m\otimes\tau_H\right)(q^n)
\,\tau_\Gamma((tg^2)^n)=0.
\tag{8}
\]
Thus the construction preserves actual ambient canonical trace, rational origin, individual diffuse unitary laws, and independently certified original pairwise separations.
None of these assertions presupposes scalar or matrix Atiyah for \(H\).

### The next separation is the original coefficient kernel

Put \(c_i=x_1-x_i\) for \(i=2,3\), whose inverses have just been certified, and use the actual transformed parameters
\[
x_i'=c_i^{-1}x_i c_i.
\]
The [central-column shape identity](../ledger/Yin_L_A0011_v1.md#a-shape-invariant-with-central-column-parameters) applies in the ring \(M_m(U_G)\) exactly as it does for scalar entries.
It uses the known factors
\[
U_i=(x_i-\lambda_1I_m)^{-1}c_i,
\qquad
V_j=(\lambda_j-\lambda_1)(x_1-\lambda_jI_m)^{-1},
\]
and writes the first Schur block as \(U_i(x_i'-\lambda_jI_m)^{-1}V_j\).
Each transformed cross difference remains an independently certified unit by similarity.

The squares in the present construction are
\[
x_1^2=x_2^2=zI_m,
\qquad x_3^2=q^2z.
\tag{9}
\]
The elementary ordered identity
\[
c_i(x_i'+x_1)=x_ic_i+c_ix_1=x_1^2-x_i^2
\tag{10}
\]
therefore gives
\[
x_2'=-x_1,
\qquad
x_3'+x_1=c_3^{-1}z(I_m-q^2).
\]
Consequently the remaining row separation is
\[
\boxed{
x_2'-x_3'=4i\varepsilon\,c_3^{-1}z\,aB^{-2}.}
\tag{11}
\]
Every factor outside \(a\) in (11) is independently an actual unit.
The [three-square rank identity](../ledger/Yin_L_A0011_v1.md#a-shape-invariant-with-central-column-parameters), with the two block pivots contributing \(2m\), now yields
\[
\boxed{
\operatorname{rk}_G\mathcal K_a=2m+\operatorname{rk}_H a,
\qquad
\dim_G\ker\mathcal K_a=\dim_H\ker a.}
\tag{12}
\]
The coefficient matrix rank is unchanged under the product-group embedding, as is clear either from the product representation or the canonical trace on its kernel projection.
Equation (12) concerns closed kernel dimensions through affiliated rank invariance, not a claimed everywhere-defined Hilbert-space bijection obtained by multiplying an unbounded inverse.

### An explicit finite group-ring matrix with the same rank

There is also a direct bounded denominator clearing that places the same obstruction in a displayed finite group-ring matrix.
For each row put
\[
D_i=(x_i-2I_m)(x_i-3I_m)(x_i-4I_m).
\]
These are independently bounded units, and ordinary polynomial multiplication gives
\[
\operatorname{diag}(D_1,D_2,D_3)\mathcal K_a
=\mathcal V_a(F\otimes I_m),
\]
\[
\mathcal V_a=
\begin{pmatrix}
I_m&x_1&x_1^2\\
I_m&x_2&x_2^2\\
I_m&x_3&x_3^2
\end{pmatrix},
\qquad
F=\begin{pmatrix}12&8&6\\-7&-6&-5\\1&1&1\end{pmatrix},
\qquad \det F=-2.
\tag{13}
\]
The three columns are the explicit coefficients of \((s-3)(s-4)\), \((s-2)(s-4)\), and \((s-2)(s-3)\), respectively.
Multiplying the third block row of \(\mathcal V_a\) by the known bounded unit \(B^2\) gives
\[
\mathcal P_a=
\begin{pmatrix}
I_m&tI_m&zI_m\\
I_m&tgI_m&zI_m\\
B^2&BC\,tg^2&C^2z
\end{pmatrix}
\in M_{3m}(\mathbb CG).
\tag{14}
\]
Thus \(\mathcal P_a\), \(\mathcal V_a\), and \(\mathcal K_a\) have the same rank and closed-kernel dimension.
Subtracting the first row from the second and \(B^2\) times the first row from the third leaves
\[
\begin{pmatrix}
I_m&tI_m&zI_m\\
0&t(g-1)I_m&0\\
0&BC\,tg^2-B^2t&(C^2-B^2)z
\end{pmatrix}.
\tag{15}
\]
The first pivot is \(I_m\), the second is the independently certified cyclic unit \(t(g-1)I_m\), and the last residual block is
\[
(C^2-B^2)z=4i\varepsilon az.
\tag{16}
\]
The ordinary closed Schur rank calculation proves (12) a second way without presuming that a rationally written matrix has integer rank.
Only the second pivot in this verification may have an unbounded inverse.

### Exact scope of the obstruction

For \(m=1\), (11) shows that a zero-or-unit assertion for this next separation, over all torsion-free \(H\) and all nonzero selfadjoint \(a\in\mathbb CH\), would already prove the scalar analytic zero-divisor assertion.
Replacing a scalar \(b\in\mathbb CH\) by \(a=b^*b\) preserves its kernel and makes it selfadjoint, so restricting the retained scalar obstruction to selfadjoint inputs loses no scalar injectivity difficulty.
This statement alone is not an equivalence with the all-matrix Atiyah conjecture.

For arbitrary \(A\in M_{r,m}(\mathbb CH)\), choose \(a=A^*A\), which is still a finite group-ring matrix and satisfies \(\ker a=\ker A\).
The block construction then gives the exact all-size identity
\[
\dim_G\ker\mathcal K_{A^*A}
=\dim_G\ker\mathcal P_{A^*A}
=\dim_H\ker A.
\tag{17}
\]
Integer rank for this whole explicitly constructed block-Cauchy class would therefore imply the full Task.
Conversely, the Task gives integer rank to \(\mathcal P_a\) directly, and (13)--(14) transfer it to \(\mathcal K_a\).
The subgroup \(H\) and its matrix input remain arbitrary; adjoining the known Klein bottle factor does not solve their kernel arithmetic.

A block separation need not be zero or invertible even in a completely resolved finite example.
Take \(H=\{e\}\), \(m=2\), \(a=\operatorname{diag}(0,1)\), and \(\varepsilon=1/2\).
Then \(q=\operatorname{diag}(1,(3+4i)/5)\), all initial certificates above hold, and
\[
\operatorname{rk}_\Gamma\mathcal K_a=5,
\qquad \dim_\Gamma\ker\mathcal K_a=1,
\qquad \operatorname{rk}_\Gamma(x_2'-x_3')=1.
\tag{18}
\]
These are unnormalized ranks, so (18) is an allowed integer defect and is not an Atiyah counterexample.
The block problem is integer-rank control, not an invalid requirement that every nonzero block be invertible.

The construction also admits the actual character grading sending \(t\) to degree one and \(H,g\) to degree zero.
Every \(x_i\) and the separation (11) has degree one under that action.
This does not invoke the character-orbit criterion at a nonzero scalar spectral parameter: the remaining question is the zero kernel of its coefficient \(a\).
It is a concrete inverse-difference realization of the [already identified coefficient obstruction](../ledger/Yin_L_A0008_v1.md#degree-one-still-contains-fractional-coefficient-defects), not a refutation of the valid graded certificate.
Likewise, putting the parameters into one component over a known coefficient division ring cannot be assumed here, since that premise would already control the unknown coefficient kernel retained in (11).
No new energy certificate or nonindicable positive calibration is inferred from this construction.

The original four-parameter family \((1-f)-(1-h)(1-g)^{-1}(1-k)\), with all four labels actual group elements, has not been classified by this argument.
Here \(x_3\) is an actual rational unitary, and in general is not a group element of the specified ambient group.
The result instead identifies a precise obstruction to a natural proposed closure of the inverse-difference induction under rational unitary parameters.

### Joint words still contain the unknown input

The canonical ambient trace does not make the rational row parameters a regular group tuple.
Indeed their exact mixed word is
\[
x_3x_2^{-1}x_1x_2^{-1}=q.
\tag{19}
\]
If \(a\ne0\), this word is not the identity, since \(q-I_m=2i\varepsilon aB^{-1}\ne0\).
Choose \(\varepsilon\|a\|<1\); this optional restriction does not alter any preceding rank formula.
Then
\[
\operatorname{Re}q
=(I_m-\varepsilon^2a^2)(I_m+\varepsilon^2a^2)^{-1}
\geq\frac{1-\varepsilon^2\|a\|^2}{1+\varepsilon^2\|a\|^2}I_m>0,
\tag{20}
\]
so the mixed word (19) has nonzero trace despite all the individual Haar moment identities (8).
The new separation therefore does not inherit the zero-relative-moment certificate used for the original differences in (7).
This is an actual finite-input version of the distinction between individual diffuse laws and joint regular-word information, rather than an enlargement to an arbitrarily chosen tracial direct sum.

## Source scope and remaining question

The actual inverse-difference factorization, shape transformation, rank interface, and Klein bottle group facts are reused at the exact [L_A0011 scopes](../ledger/Yin_L_A0011_v1.md#source-attribution-and-remaining-scope).
That source account already compares the general Schur and actual-ring inverse premises with Gelfand, Gelfand, Retakh and Wilson, without importing formal free-field evaluations.
The new identities (9)--(17) are direct ordered computations in those actual rings.

The Cayley construction in (2) is classical.
Feld18, the UBC-hosted notes [The Cayley Transform and Self-adjoint Extensions](../literature/pdf/Feld18--cayley.pdf), dated November 27, 2018, was inspected at Theorem 1(c), printed/PDF p. 1, and its proof on p. 2.
Their transform is \(C_+(T)=(T-iI)(T+iI)^{-1}\), and the present \(q\) is \(-C_+(\varepsilon a)\).
This is attribution for the bounded unitary conversion, whose required inverse and adjoint identities are also checked above; no selfadjoint-extension theorem or unbounded Cayley-domain assertion is used.
No full audit of those notes or historical priority claim is made.

The remaining useful invariant must constrain the actual coefficient \(a\) or its surviving kernel by information stronger than rational origin, individual Haar laws, original difference-unit certificates, and the mere existence of an ambient character.
Equations (11), (14), and (17) make this requirement explicit without asserting that any forbidden fractional defect actually occurs.

## Assessment history

### Decision reviewed-coefficient-obstruction

| Field | Value |
| --- | --- |
| date | 2026-11-11T16:33 |
| status | proved |
| reason | Independent whole-claim review supports both exact rank reductions, all initial unit and Haar certificates, the finite group-ring realization and the distinction between scalar, block and joint-word obstructions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete arbitrary selfadjoint coefficient input, independently admissible array, exact rank and nullity, finite realization and all-size equivalence. |
| argument | [Argument](#argument) | Formulas (1)--(20), both rank proofs, actual units and domains, scalar and block limits, partial-rank example, mixed-word obstruction and source qualifications. |
| review | [Independent whole-claim finding](../audits/reviews/Yin_R_A0019_v1.md#whole-claim-finding) | Exact complete saved statement, argument and source/continuation limitations, with directly inspected dependency and primary-source scopes. |

## Current assessment

[Selected decision](#decision-reviewed-coefficient-obstruction)


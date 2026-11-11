---
author: Yin
---
# Degree-one reduction and extreme-coefficient rank certificates

Date: 2026-11-11 (Asia/Hong_Kong).
The main research agent and two development helpers carried out this investigation for Yin under [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract).
The question is whether induction reducing polynomial degree to one strengthens the actual rational-closure and complementary-block criterion.
An explicit classical stabilization gives a terminating reduction with exact kernel-dimension preservation and only independently invertible triangular factors.
The reduction increases matrix size and does not manufacture an invertible extreme coefficient or integer rank for an arbitrary affine matrix.
A direct unit-completion argument yields an extreme-coefficient rank bound, and the earlier concrete families can be treated under the weaker hypothesis that their supporting subgroup is indicable.
These are known linearization and cyclic-extension mechanisms with explicit application interfaces, not a new Atiyah group class or a historical-novelty claim.
All affiliated operations are closed operations in the actual finite affiliated algebra, with unnormalized matrix traces.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0010_v1.md#whole-artifact-finding) covers the complete reduction, rank bounds, examples, parameter boundaries and exact source-use limits.

## A single exact lowering step

Let \(S\) be any unital ring and let
\[
A\in M_{n,m}(S),\qquad B\in M_{n,k}(S),\qquad C\in M_{k,m}(S),\qquad P=A+BC.
\]
Set
\[
Q=\begin{pmatrix}A&B\\-C&I_k\end{pmatrix},\qquad
E=\begin{pmatrix}I_n&-B\\0&I_k\end{pmatrix},\qquad
F=\begin{pmatrix}I_m&0\\C&I_k\end{pmatrix}.
\]
Direct multiplication in the displayed noncommutative order gives
\[
EQF=\begin{pmatrix}P&0\\0&I_k\end{pmatrix}.
\tag{H1}
\]
The inverses of \(E,F\) are obtained by changing the signs of their off-diagonal blocks.
Thus no inverse of \(A,B,C\), or \(P\) is used.
The only pivot is the independently invertible identity block.

When \(S\subseteq\mathcal U(M)\) for a finite tracial von Neumann algebra, the accepted [affiliated rank invariance](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) gives
\[
\operatorname{rk}_M Q=k+\operatorname{rk}_M P,\qquad
\dim_M\ker Q=\dim_M\ker P.
\tag{H2}
\]
The matrix traces are unnormalized, and the second equality subtracts the respective ranks from the respective numbers of columns.
For bounded entries there is additionally the bounded module isomorphism
\[
\ker P\longrightarrow\ker Q,\qquad x\longmapsto(x,Cx),
\]
whose inverse is first-coordinate projection.
For unbounded affiliated entries, (H2) uses rank inequalities and closed affiliated products, without asserting this pointwise Hilbert-space formula on unrestricted domains.

## Terminating induction for word polynomials

Fix a finite tuple of ring elements \(X=(X_1,\ldots,X_s)\), and choose a finite expanded noncommutative polynomial representative of every entry of a matrix \(P(X)\).
The tuple may consist of regular group generators and their inverses.
For each displayed nonzero monomial of length \(\ell\), count \(\max(\ell-1,0)\), and let \(\mu(P)\) be the sum over this chosen representation of all entries.
This is a complexity of a written representative, not a claimed degree function on a group algebra modulo its relations.

If \(\mu(P)>0\), choose a term
\[
cX_{i_1}\cdots X_{i_\ell}
\]
of length \(\ell\ge2\) in entry \((a,b)\).
Remove that occurrence to obtain \(A\), and write the removed matrix term as \(BC\), where
\[
B=c\,e_aX_{i_1}\cdots X_{i_{\ell-1}},\qquad
C=X_{i_\ell}e_b^{\mathsf T}.
\]
Apply (H1) with \(k=1\).
The displayed terms of \(Q\) have total complexity exactly \(\mu(P)-1\): the removed term contributes \(\ell-1\), the new prefix contributes \(\ell-2\), and the last letter and identity contribute zero.
One need not combine or cancel monomials to make this decrease valid.
Iterating without optional simplification therefore terminates after exactly \(K=\mu(P)\) such steps.
The resulting matrix \(\Lambda(X)\) is affine linear in the fixed tuple and satisfies
\[
\operatorname{rk}_M\Lambda(X)=K+\operatorname{rk}_MP(X),\qquad
\dim_M\ker\Lambda(X)=\dim_M\ker P(X).
\tag{H3}
\]
It has \(n+K\) rows and \(m+K\) columns if \(P\) has \(n\) rows and \(m\) columns.
All equivalences are products of the explicitly invertible triangular factors in (H1), evaluated in the same actual algebra.
They hold regardless of relations among the \(X_j\).
No freeness, universal-field evaluation, scalar injectivity premise, or Atiyah premise enters the reduction.

The precise established source for this step is [Coh06, Section 5.8, printed p. 311, opening paragraphs before equation (1)](../audits/literature/Coh06/Yin_U002.md#coh06-u002).
The source inspection records the checked elementary transformation and finite iteration, its name as Higman's trick, and the boundary excluding the later free-algebra highest-term results from an arbitrary relations quotient.
The same arithmetic is compatible with the polynomial realization mechanism already inspected in [MSY23 Theorem 4.3 and its polynomial-consistency construction](../audits/literature/MSY23/Yin_U003.md#theorem-43-constructive-existence-of-representations).
The local formulas verify the exact rank and complexity interfaces, without claiming a new linearization theorem or replacing the source's fuller rational representation theorem.

## An efficient ordered one-variable version

Let \(t\in S\) and \(A_0,\ldots,A_d\in M_n(S)\), and put \(T=tI_n\).
Consider the ordered expression
\[
P=A_0+A_1T+\cdots+A_dT^d.
\]
No commutation between \(T\) and the coefficients is assumed.
For \(d\ge2\), define the \(dn\)-square block matrix
\[
H_d(T)=
\begin{pmatrix}
A_0+A_1T&A_2T&A_3T&\cdots&A_dT\\
-T&I_n&0&\cdots&0\\
0&-T&I_n&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&-T&I_n
\end{pmatrix}.
\tag{H4}
\]
For \(d=1\), set \(H_1(T)=P\).
The lower-right block \(D\) in (H4) is \(I-N\), where \(N\) has \(T\) on its first subdiagonal and \(N^{d-1}=0\).
Consequently
\[
D^{-1}=I+N+\cdots+N^{d-2}
\]
is a finite polynomial matrix, independently of \(P\) and of all coefficient invertibility questions.
Writing (H4) as \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\), direct multiplication gives
\[
\begin{pmatrix}I&-BD^{-1}\\0&I\end{pmatrix}
H_d(T)
\begin{pmatrix}I&0\\-D^{-1}C&I\end{pmatrix}
=\operatorname{diag}(P,D).
\tag{H5}
\]
Indeed, \(D^{-1}C\) has block entries \(-T,-T^2,\ldots,-T^{d-1}\), so the Schur complement is
\[
A_0+A_1T+\sum_{j=2}^d A_jTT^{j-1}=P.
\]
Multiplying the lower block by \(D^{-1}\) proves the exact stable equivalence to \(\operatorname{diag}(P,I_{(d-1)n})\).
In particular,
\[
\operatorname{rk}_M H_d(T)=(d-1)n+\operatorname{rk}_M P,\qquad
\dim_M\ker H_d(T)=\dim_M\ker P.
\tag{H6}
\]
The quadratic step is already illustrative:
\[
A_0+A_1T+A_2T^2
\quad\rightsquigarrow\quad
\begin{pmatrix}A_0+A_1T&A_2T\\-T&I_n\end{pmatrix}.
\]
Repeated elimination of the last identity block in (H4) reconstructs the ordered Horner expression, while reversing those eliminations gives the desired induction lowering each occurrence of a power to degree one.

These identities hold directly for ordered actual expressions and also as identities over a skew polynomial ring \(S_0[t;\sigma]\), with coefficients written on the left and \(ta=\sigma(a)t\).
A central formal polynomial over a noncommutative coefficient ring can be evaluated by a ring homomorphism only when the chosen value of its central indeterminate commutes with the coefficients.
Thus a central-indeterminate notation cannot silently justify an incompatible evaluation; (H4)--(H5) avoid that mistake by retaining the multiplication order throughout.

## Exactly what the degree-one endpoint inherits

Write the formal version of (H4) as \(H_0+H_1t\), with all coefficients on the left.
Its constant coefficient is
\[
H_0=\operatorname{diag}(A_0,I_n,\ldots,I_n).
\tag{H7}
\]
It is a unit precisely when \(A_0\) is a unit.
The leading coefficient has first block row \((A_1,A_2,\ldots,A_d)\), subdiagonal blocks \(-I_n\), and all other blocks zero.
Moving its last block column to the first position makes it block upper triangular with diagonal blocks \(A_d,-I_n,\ldots,-I_n\).
Therefore
\[
\operatorname{rk}_M H_1=(d-1)n+\operatorname{rk}_M A_d,
\tag{H8}
\]
and \(H_1\) is a unit precisely when \(A_d\) is a unit.
Neither extreme-coefficient unit hypothesis is manufactured by this linearization.

Suppose now that a trace-preserving action fixes every \(A_j\) and satisfies \(\alpha_\theta(t)=e^{i\theta}t\).
If \(A_0\) is independently an actual unit, then \(H_0\) is independently a unit and
\[
H_0^{-1}H_d(T)=I_{dn}+H_0^{-1}H_1(tI_{dn})
\]
has a homogeneous degree-one second term.
The [character-orbit certificate](../ledger/Yin_L_A0007_v1.md#the-character-orbit-certificate) proves this matrix invertible, and (H6) proves \(P\) invertible.
This gives a literal degree-one endpoint for one-sided skew polynomials with an independently invertible constant term.
It is an alternative explicit implementation of the already retained graded companion argument, with the same essential hypotheses and known cyclic-extension coverage.

For a group homomorphism \(\phi:H\to\mathbb Z\) onto the integers, choose \(t\in H\) with \(\phi(t)=1\), put \(N=\ker\phi\), and let \(\sigma=\operatorname{Ad}t\).
Every group-ring polynomial supported in nonnegative degrees can be written in the preceding ordered form with coefficients in \(\mathbb CN\).
The character fixes those coefficients and rotates \(t\), so the hypotheses match exactly when the constant coefficient is independently invertible in the actual affiliated algebra.
The character need only exist on the supporting subgroup.
An arbitrary nonzero coefficient in \(\mathbb CN\) is not automatically an actual unit without an additional verified argument.

## The concrete anticommutator after lowering

For the previous anticommutator numerator
\[
p=2-2g-2h+gh+hg,
\]
two applications of (H1) give the affine matrix
\[
\Lambda_p=
\begin{pmatrix}
2-2g-2h&g&h\\
-h&1&0\\
-g&0&1
\end{pmatrix}.
\tag{H9}
\]
Here \(A=2-2g-2h\), \(B=(g\ h)\), and \(C=(h\ g)^{\mathsf T}\), so \(A+BC=p\) in the correct order.
The identity pivot is \(I_2\), and consequently
\[
\operatorname{rk}_G\Lambda_p=2+\operatorname{rk}_Gp,\qquad
\dim_G\ker\Lambda_p=\dim_G\ker p.
\tag{H10}
\]
Its constant coefficient is \(\operatorname{diag}(2,1,1)\), which is independently invertible.
If \(\phi(g)=\phi(h)=1\), every entry of its nonconstant part has degree one under the actual character action.
The normalized matrix \(\operatorname{diag}(1/2,1,1)\Lambda_p\) is therefore identity plus a homogeneous degree-one matrix and is invertible by the existing character certificate.
Equations (H9)--(H10) then prove \(p\) invertible without any inverse of \(p\) being used in the lowering steps.
This directly realizes the proposed degree reduction on the selected example, with the same common-grading hypothesis and known cyclic-extension coverage as its earlier companion proof.
Without that actual common grading, the displayed triangular equivalence remains valid, but this character argument supplies no invertibility conclusion.

## Why a scalar or fixed-size base case does not follow

The word-polynomial induction reduces degree by increasing matrix size.
Consequently, its sufficient base statement is integer analytic rank for all affine matrix sizes, exactly the criterion already established in [L_A0004](../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria).
Knowing the ranks of the scalar entries alone does not supply the required matrix base case.
Even over \(\mathbb C\mathbb Z\), the affine matrix
\[
\begin{pmatrix}1&g\\g^{-1}&1\end{pmatrix}
=\binom{1}{g^{-1}}\begin{pmatrix}1&g\end{pmatrix}
\]
has rank one although all four entries are units.
Eliminating its identity pivot recreates the degree-two expression \(1-gg^{-1}=0\).
For the general quadratic matrix in (H4), the same elimination recreates \(A_0+A_1T+A_2T^2\), so induction on matrix size cannot use that elimination as a simultaneous strict decrease in polynomial degree.

There is also a precise algebraic reason not to expect a uniformly fixed-size polynomial equivalence.
Over \(\mathbb C[z]\), consider \(P(z)=(1+z^d)I_n\).
If an affine \(N\)-square pencil were polynomial-unimodularly equivalent to \(\operatorname{diag}(P,I_{N-n})\), its determinant would have degree \(nd\), because the determinants of polynomial-unimodular factors are nonzero constants.
The determinant of an affine \(N\)-square pencil has degree at most \(N\).
Hence \(N\ge nd\).
The size \(dn\) in (H4) is therefore necessary in this family for this type of stable polynomial equivalence.
This does not preclude special expressions from having smaller realizations or additional independently certified rational multipliers.

Finally, scalar Laurent-polynomial units cannot universally lower support width.
In \(\mathbb C[g^{\pm1}]\), every ring unit is \(cg^k\), since the highest and lowest exponents of a product add and a product equal to one must have zero support width in both factors.
Multiplication on either side by such units preserves the difference between the highest and lowest exponents.
Thus \(1+g^3\), of width three, cannot be converted in this way into an affine expression in the fixed tuple \((g,g^{-1})\), whose width is at most two.
The cyclic affiliated inverse of \(1+g^3\) exists by a separate known argument, but using that inverse to normalize the target would derive no new invertibility fact.

## A unit completion instead of assuming an invertible extreme coefficient

Let a trace-preserving action \(\alpha_\theta\) on a finite von Neumann algebra \(M\) act entrywise on matrices and extend to affiliated operators.
Suppose
\[
P=\sum_{j=0}^d A_j\in M_n(\mathcal U(M)),
\qquad \alpha_\theta(A_j)=e^{ij\theta}A_j.
\]
The coefficient \(A=A_0\) is not assumed injective.
Use the actual [relative inverse and support projections](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions), without presuming membership in a smaller rational closure.
Let \(A^\dagger\) be its relative inverse and set
\[
e=A^\dagger A,\qquad f=AA^\dagger,
\qquad r=\operatorname{rk}_M A.
\]
The projections \(e,f\) have trace \(r\), and \(A^\dagger\) has rank \(r\).
Uniqueness of the relative inverse makes \(A^\dagger,e,f\) fixed by the action.
The two explicitly known matrices
\[
C_0=
\begin{pmatrix}
A&1-f\\
1-e&-A^\dagger
\end{pmatrix},
\qquad
D_0=
\begin{pmatrix}
A^\dagger&1-e\\
1-f&-A
\end{pmatrix}
\]
satisfy \(C_0D_0=D_0C_0=I_{2n}\).
For example, the upper-left product is \(AA^\dagger+(1-f)^2=f+(1-f)=1\), and the off-diagonal products vanish by the support identities.
Consequently
\[
C(P)=
\begin{pmatrix}
P&1-f\\
1-e&-A^\dagger
\end{pmatrix}
=C_0+\sum_{j=1}^d
\begin{pmatrix}A_j&0\\0&0\end{pmatrix}
\]
is an actual unit by the existing graded companion criterion, since its degree-zero coefficient is the explicitly invertible \(C_0\).
No inverse of \(A\) or \(P\) has been assumed.
On the other hand,
\[
C(P)=\operatorname{diag}(P,-A^\dagger)
 +\begin{pmatrix}0&1-f\\1-e&0\end{pmatrix}.
\]
The second summand has rank \(2(n-r)\), so rank subadditivity gives
\[
2n\leq \operatorname{rk}_M P+r+2(n-r).
\]
Therefore
\[
\boxed{\operatorname{rk}_M P\geq\operatorname{rk}_M A_0,\qquad
\dim_M\ker P\leq\dim_M\ker A_0.}
\tag{R1}
\]
The operations are exact affiliated matrix operations, not Hilbert-space substitutions through an unbounded graph.
The construction uses relative inverses and support projections in the ambient affiliated algebra; it is an analytic rank certificate rather than a claim that every auxiliary entry lies in the actual rational closure under study.

For an actual cyclic extension, take a homogeneous unit \(t\) of degree one and write
\[
P=\sum_{j=0}^d B_jt^j,
\qquad \alpha_\theta(B_j)=B_j.
\]
Multiplication on the right by the independently known unit \(t^{-d}\), followed by reversing the grading, puts \(B_d\) at degree zero and every other term in a nonnegative degree.
Applying (R1) to that polynomial gives
\[
\boxed{\operatorname{rk}_M P\geq
\max\{\operatorname{rk}_M B_0,\operatorname{rk}_M B_d\}.}
\tag{R2}
\]
Reversing the action alone is insufficient to move the top coefficient to degree zero; the actual homogeneous unit is part of this top-end argument.
For group rings the lift of the quotient generator supplies that unit.
If the low or high coefficient is independently injective, (R2) recovers the full-rank criterion.
For a singular extreme coefficient it bounds the possible defect without making that defect integral.

## Degree one still contains fractional coefficient defects

Let
\[
M=L^\infty([0,1]\times\mathbb T),\qquad
t(x,z)=z,\qquad p(x,z)=\mathbf 1_E(x),
\]
where \(E\subset[0,1]\) has measure \(\theta\in(0,1)\).
Use product Lebesgue trace and the circle action rotating the second coordinate, so \(p\) has degree zero and \(t\) degree one.
The multiplier \(1+t\) has zero set of measure zero and is an actual affiliated unit.
Thus
\[
P=p+pt=p(1+t)
\]
has rank \(\theta\) and kernel dimension \(1-\theta\), even though both coefficients are nonzero and a genuine infinite character orbit is present.
This attains equality in (R1) and (R2).
It is a finite-tracial test of the proposed proof mechanism, not a torsion-free group-ring counterexample or a claim that \(p\) belongs to the rational closure of such a group ring.

For \(\theta=1/2\), compare
\[
P=p+pt,\qquad Q=(1-p)+pt.
\]
The coefficient ranks are \((1/2,1/2)\) in both pencils, but \(P\) has rank \(1/2\), whereas \(Q\) is an actual unit with inverse \((1-p)+pt^{-1}\).
Therefore the two individual coefficient ranks do not determine the pencil rank.
The same half-rank example occurs over the actual group ring of \(C_2\times\mathbb Z\), using \(p=(1+a)/2\) for the order-two element \(a\); this group has torsion and does not meet the Task's hypothesis.

Even removing a common right kernel and a common left kernel of the two coefficients does not suffice for invertibility.
Over \(\mathbb C[t^{\pm1}]\), take
\[
K(t)=
\begin{pmatrix}
1&t&0\\
0&0&1\\
0&0&t
\end{pmatrix}
=A+tB.
\]
Here \(\ker A\cap\ker B=0\) and \(\ker A^*\cap\ker B^*=0\), but \(K(t)(-t,1,0)^{\mathsf T}=0\), and the matrix has analytic rank exactly two.
Its first and third columns are independent, and the second is the first multiplied by \(t\).
This is a direct degree-one obstruction to a proposed criterion using only those two common-kernel tests, already over the infinite cyclic group.

There is also an exact obstruction to using degree induction to avoid the coefficient problem.
For any torsion-free \(N\), consider \(G=N\times\mathbb Z\) and a nonzero matrix \(A\) over \(\mathbb CN\).
The genuine degree-one polynomial \(A+At=A(1+t)\) has precisely the rank of \(A\), because \(1+t\) is independently invertible in the actual affiliated algebra.
Thus a universal integer-rank assertion for cyclic degree-one pencils already includes all the coefficient-group integer-rank assertions.
A successful induction must supply those coefficient inputs by a genuinely decreasing measure or a separate theorem.

## A singleton extreme support term and the earlier examples

Let \(p=\sum_{g\in S}c_g g\) have finite support with nonzero complex coefficients, and let \(H=\langle S\rangle\).
If an actual homomorphism \(\phi:H\to\mathbb Z\) has a unique minimum at \(g_0\in S\), then \(g_0^{-1}p\) has the independently invertible scalar constant coefficient \(c_{g_0}\) and only positive-degree remaining terms.
The retained graded criterion therefore makes \(p\) an actual affiliated unit.
A unique maximum is treated after reversing the grading.
This is a direct specialization of the established criterion and of known cyclic-extension behavior, not a new group-class theorem.

The following application weakens the common degree-one hypothesis of the earlier examples to indicability of their actual supporting subgroup.
Let \(G\) be torsion-free, let \(g,h\ne e\), and suppose the coefficient subgroup \(H=\langle g,h\rangle\) admits a nonzero homomorphism \(\phi:H\to\mathbb Z\).
Write \(m=\phi(g)\) and \(n=\phi(h)\), which are not both zero.
No common degree-one or same-sign hypothesis is required.
Set \(a=1-g\) and \(b=1-h\), whose actual inverses are independently certified by the cyclic test.

For distinct \(g,h\), the two numerators
\[
s_q=(1+q)-qg-h,\qquad
c_q=(1-q)+qg-h
\]
are actual units for every \(q\in\mathbb C\).
For \(q\notin\{0,1,-1\}\), every coefficient on the distinct support \(\{e,g,h\}\) is nonzero, and the degree multiset \(\{0,m,n\}\) has a singleton extreme whenever \((m,n)\ne(0,0)\).
If \(m=n\ne0\), the identity is alone at an extreme; if exactly one is zero, the other group element is alone at an extreme; if all three degrees differ, both extremes are singletons.
The singleton-extreme criterion applies to each numerator.
For \(q=0\), both are \(1-h\); for \(q=1\), \(c_q=g-h\); for \(q=-1\), \(s_q=g-h\).
The binomial \(g-h=g(1-g^{-1}h)\) is an actual unit since \(g\ne h\) and \(G\) is torsion-free, and the remaining numerator has the same singleton-extreme test.
When \(g=h\), use the exact degeneracies already recorded in [the original parameter classification](../ledger/Yin_L_A0007_v1.md#the-full-complex-parameter-range-under-the-common-grading), rather than treating the two equal support labels as distinct.
All ordered rational identities and certified multipliers from that classification continue to hold under this weaker indicability hypothesis.

For the ordered-product numerator
\[
p_\eta=(1-g)(1-h)-\eta(1-h)(1-g)
=(1-\eta)(1-g-h)+gh-\eta hg,
\]
assume first \(\eta\ne1\).
The following cases independently certify an invertible extreme coefficient.

| Degrees | Extreme coefficient and justification |
| --- | --- |
| \(mn>0\) | The identity term is alone at the low or high extreme and has nonzero scalar coefficient \(1-\eta\). |
| \(mn<0\) | If \(m>0>n\), the degree \(n\) term is uniquely \(-(1-\eta)h\), while the degree \(m\) term is uniquely \(-(1-\eta)g\); swap the labels for the other sign arrangement. |
| \(m=0,n\ne0\) | The degree-zero coefficient is \((1-\eta)(1-g)\), an independently certified cyclic unit; the only other possible degree is \(n\), so reverse the grading if \(n<0\). |
| \(n=0,m\ne0\) | The degree-zero coefficient is \((1-\eta)(1-h)\), with the same cyclic-unit argument. |

In the opposite-sign case \(m>0>n\), one has \(n<\min\{0,m+n\}\leq\max\{0,m+n\}<m\), so neither product term reaches the selected extreme.
Thus \(p_\eta\) is an actual unit for \(\eta\ne1\).
For \(\eta=1\), the existing factorization \(gh-hg=gh(1-h^{-1}g^{-1}hg)\) gives zero in the commuting case and a cyclic unit otherwise.
The exact denominator clearing \((ba)r_\eta(ab)=p_\eta\), for \(r_\eta=a^{-1}b^{-1}-\eta b^{-1}a^{-1}\), transfers these conclusions with unchanged analytic kernel dimension.
This strengthens the applicability condition of the previous worked examples to any indicable coefficient subgroup, while remaining covered by the known cyclic-extension mechanism.
It leaves the nonindicable-support case and the general degree-one matrix rank problem unresolved.

## Known coverage and the remaining induction step

The extreme-coefficient estimate is already recorded in [JZLA20's natural-extension construction](../audits/literature/JZLA20/Yin_U001.md#natural-extensions), and [Proposition 3.11](../audits/literature/JZLA20/Yin_U001.md#hughes-free) supplies the actual group-rank interface for any indicable supporting subgroup.
The unit-completion proof above is a direct analytic derivation using the retained character criterion; it does not require that the coefficient algebra already be a division ring.
The new scope comparison for the worked examples is an application of that known mechanism, without claiming a new positive class for the full complex Atiyah conjecture.
The classical degree reduction is sourced to Coh06 and agrees with the already inspected MSY23 polynomial representation mechanism.
A bounded primary-source search on 11 November 2026 located the same Higman step in Arvind and Joglekar's 2024 ECCC revision, but the retained local Coh06 passage supplies the needed exact attribution, so no additional source or priority claim is used.

A usable inductive statement must quantify over all matrix sizes generated by stabilization and specify the coefficient class, actual evaluation, admissible inverses and decreasing complexity.
An original bordered pencil already affine in the chosen group generators is already at this degree-one endpoint.
The lowering construction is useful for a higher-degree complementary numerator, a polynomial obtained after justified denominator clearing, or degree in a selected cyclic direction; it does not by itself add a constraint to an already affine border.
For rational expressions, the required inverse domain remains a separate premise under the existing MSY23 representation theorem.
For arbitrary group-word polynomials the written multiplication count decreases, but the degree-one endpoint is the unresolved all-size affine rank problem from [L_A0004](Yin_L_A0004_v1.md#setting-and-exact-criteria).
For a genuine cyclic extension the polynomial degree reduces to one, while the exact example \(A(1+t)\) shows that unresolved coefficient ranks remain unresolved there.
A nonzero integer character is extra structure, and torsion-freeness alone does not supply it, as in the retained [Promislow calibration](Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test).
Further useful work should therefore choose a degree-one pencil whose extreme coefficients are not yet independently controlled, and seek a rank mechanism sensitive to their interaction or a separately justified decrease in coefficient complexity.
An added formal degree variable or a change of names for the actual group labels does not supply this missing base theorem.
The specific two-resolvent and ordered-product families above need further testing only outside the now completed indicable-support scope, or for a different mechanism with demonstrably new coverage.

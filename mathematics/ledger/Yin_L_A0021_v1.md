---
author: Yin
---
# An ordered-quotient certificate and a normality barrier for the surviving trinomial

Date: 2026-11-12 (Asia/Hong_Kong).
This route-four development concerns the actual scalar \(T=1+u-v\), with \(u,v\) actual elements of a torsion-free group \(G\), retained by the [power-column reduction](../ledger/Yin_L_A0020_v1.md#exact-inclusion-of-an-equal-modulus-trinomial-problem).
The positive conclusion is a precise application of the already checked Lin92 ordered-quotient theorem.
The separate direct calculations classify two normality tests and show why they add no mechanism outside the retained cyclic-normalizer scope.
These are scalar statements, with no claim of full matrix Atiyah integrality or a new group class.

## Actual setting and fixed inputs

Put \(H=\langle u,v\rangle\), \(M=\mathcal N(H)\), and \(U=\mathcal U(M)\), with their actual regular representation and canonical trace.
Use closed affiliated products in \(U\).
Injectivity of a bounded element of \(M\) implies invertibility in \(U\): its polar decomposition has initial support \(1\), equality of finite traces makes its final support \(1\), and the inverse on the dense range is affiliated.
This standard actual-inverse convention is the same one used in the [retained cyclic proof](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions).
No claim of a bounded inverse follows.

The augmentation of \(T\) is \(1\), including coincident-label cases, so \(T\ne0\) in \(\mathbb CH\).
If \(u=e\), then \(T=2-v\) has a bounded Neumann-series inverse.
If \(v=e\), then \(T=u\), and if \(v=u\), then \(T=1\).
It therefore suffices below to treat three distinct labels \(e,u,v\).

For the connection to the original rational expression, retain the hypotheses \(u\ne e\) and \(uv\ne e\).
The fixed identity is
\[
r=(1+u+u^2)^{-1}uT(1-uv),
\qquad
\dim_G\ker r=\dim_G\ker T.
\tag{1}
\]
Both outside cyclic factors in (1) are independently invertible by torsion-freeness.
The excluded case \(uv=e\) is not restored to (1): there the original Schur value is zero while \(T=1+u-u^{-1}\) is a nonzero cyclic unit.

## A nontrivial right-orderable quotient suffices

Suppose there is a surjective homomorphism
\[
\pi:H\longrightarrow Q
\]
onto a nontrivial right-orderable group.
No injectivity or division-closure hypothesis is imposed on the group algebra of \(N=\ker\pi\).
Then \(T\) is injective on \(\ell^2(H)\), hence is a unit in \(U\).

Here is the complete application of the source theorem.
Choose a right order on \(Q\) and a transversal \(s:Q\to H\).
Writing coefficients on the left gives
\[
T=\sum_{q\in\pi(\{e,u,v\})}a_qs(q),
\qquad
a_q=\sum_{\substack{w\in\{e,u,v\}\\\pi(w)=q}}c_w\,w\,s(q)^{-1}\in\mathbb CN,
\quad (c_e,c_u,c_v)=(1,1,-1).
\tag{2}
\]
Since \(u,v\) generate \(H\) and \(Q\ne\{e\}\), the three images \(\pi(e),\pi(u),\pi(v)\) cannot all coincide.
Consequently each fiber in (2) contains at most two support elements.
Distinct support elements give distinct elements \(ws(q)^{-1}\) of \(N\), so no displayed two-term coefficient vanishes by coefficient cancellation.
Thus each \(a_q\) is either a nonzero scalar multiple of a group unit or a nonzero group binomial.

For completeness, write such a binomial as
\[
a_q=\alpha n_1+\beta n_2
=\alpha n_1(1+\gamma n),
\qquad
n=n_1^{-1}n_2\ne e,\quad \gamma=\beta/\alpha\ne0.
\tag{3}
\]
The subgroup \(N\) is torsion free, so \(n\) has infinite order.
On every orbit of \(\langle n\rangle\), its regular representation is the bilateral shift.
The Fourier multiplier \(1+\gamma z\) has at most one zero on the circle, a Haar-null set; hence (3) is injective on \(\ell^2(N)\) and has an actual affiliated inverse.
This coefficient certificate uses the canonical regular representation, not just an abstract infinite-order unitary.
In particular \(a_q\phi\ne0\) for every nonzero \(\phi\in\mathcal N(N)\).
One may also see the last statement by applying the injective operator \(a_q\) to each vector in the nonzero range of \(\phi\).

The finite nonempty quotient support in (2) has a least term \(q_0\).
Its coefficient \(a_{q_0}\) satisfies exactly the premise of [Lin92 Theorem 4 as checked in C_A0004_v3](../claims/Yin_C_A0004_v3.md#ordered-quotient-source).
That theorem excludes \(T\beta=0\) for every nonzero \(\beta\in\ell^2(H)\).
The source input is the scalar theorem on printed pp. 50--51 of *Zero divisors and \(L^2(G)\)*, already registered as Lin92, with the retained primary-statement and applicability inspection.
The historical proof is not independently re-audited here.
Neither algebraic absence of group-ring zero divisors nor a formal ordered-series embedding replaces this analytic source input.

For an ambient torsion-free \(G\), decompose \(\ell^2(G)\) into the orthogonal sum of the right \(H\)-cosets \(Hs\).
Left multiplication by \(T\) preserves every summand, and each restriction is unitarily equivalent to its action on \(\ell^2(H)\).
Therefore \(T\) is injective on \(\ell^2(G)\) as well.
Its scalar analytic rank is \(1\), and, under the nondegenerate hypotheses of (1), \(r\) also has rank \(1\) and zero kernel dimension.
The original two-by-two matrix in L_A0020 then has rank \(2\) by its already justified Schur identity.

This strengthens the explicit indicable-support screen for this trinomial: a nontrivial right-orderable quotient may be used directly, without first producing a map to \(\mathbb Z\).
It also does not require the supporting subgroup itself to be right orderable.
No example separating this criterion from every other known Atiyah class is claimed.
The contribution is the three-point support check ensuring an independently certified least coefficient, not a new ordered-quotient theorem.
In particular, the known source result is not promoted to integer ranks for all matrices over \(H\).

## Normality of the relative operator is exactly a cyclic-normalizer relation

A natural alternative is the bounded relative operator
\[
R=(1+u)v^{-1},
\qquad
T=(R-1)v.
\tag{4}
\]
The right factor \(v\) is unitary, so \(\ker T=v^{-1}\ker(R-1)\) as closed Hilbert subspaces.
Their von Neumann dimensions agree, without any inverse of the unknown pivot.
Direct multiplication gives
\[
RR^*=2+u+u^{-1},
\qquad
R^*R=v(2+u+u^{-1})v^{-1}.
\tag{5}
\]
For \(u\ne e\), torsion-freeness makes \(u\ne u^{-1}\).
Equality in (5), compared in the linearly independent regular group basis, therefore gives the exact equivalence
\[
R\text{ is normal}
\quad\Longleftrightarrow\quad
vuv^{-1}\in\{u,u^{-1}\}.
\tag{6}
\]
The reverse implication follows immediately from (5).
This is an actual joint-word condition, but it is already the retained cyclic-normalizer situation.

The normality premise does give a complete independent kernel argument.
If \((R-1)\xi=0\) and \(R\) is normal, then \((R^*-1)\xi=0\), since the normal operator \(R-1\) and its adjoint have equal norms on every vector.
It follows from (5) that
\[
(1+u+u^{-1})\xi=0.
\tag{7}
\]
The Laurent polynomial \(1+z+z^{-1}\) is nonzero and has only finitely many circle zeros, so the cyclic regular-representation certificate forces \(\xi=0\).
The case \(u=e\) gives the scalar multiplier \(3\) in (7) and was already covered above.
Thus normality proves injectivity, but (6) prevents this particular premise from reaching an unnormalized, genuinely new coefficient component.

Weakening the premise to a one-sided sign on the self-commutator does not enlarge it.
Indeed the bounded selfadjoint operator
\[
D=R^*R-RR^*
\]
has \(\tau(D)=0\).
If \(D\ge0\) or \(D\le0\), faithfulness of the finite trace implies \(D=0\), returning to (6).
This is the usual fact that a hyponormal or cohyponormal element of a finite von Neumann algebra is normal.
For attribution, the precise checked primary passage is Marie Choda and Hisashi Choda, *Some Characterizations of Certain von Neumann Algebras*, Proc. Japan Acad. 46 (1970), 1086--1090, Remark after Theorem 3 on p. 1087, in the registered [CC70 publisher original](../literature/pdf/CC70.pdf).
Only that remark and its surrounding definitions were inspected; the one-line finite-trace proof needed here is supplied above.
That source supplies attribution, not an additional hypothesis or a substitute for the direct proof.

## Normality of the trinomial itself has a second exact collapse

For comparison, \(T\) is normal if and only if \(d=u-v\) is normal.
Expanding the two products gives
\[
dd^*=2-uv^{-1}-vu^{-1},
\qquad
d^*d=2-u^{-1}v-v^{-1}u.
\tag{8}
\]
Assume \(u\ne v\), and put \(a=uv^{-1}\), \(c=u^{-1}v\).
Torsion-freeness makes the two elements in each inverse pair distinct.
The group-basis identity \(a+a^{-1}=c+c^{-1}\) is therefore equivalent to \(c=a\) or \(c=a^{-1}\).
The first alternative is equivalent to \(u^2=v^2\), and the second to \(uv=vu\).
Consequently
\[
T\text{ is normal}
\quad\Longleftrightarrow\quad
uv=vu\ \text{ or }\ u^2=v^2.
\tag{9}
\]
The case \(u=v\) gives \(T=1\) and satisfies both conclusions.

The common-square alternative has its own elementary kernel certificate.
Suppose \(u^2=v^2=z\) and \(u\ne v\).
Then \(z\) commutes with both \(u\) and \(v\), and \(z\ne e\), since otherwise torsion-freeness would give \(u=v=e\).
Moreover \(d^*=z^{-1}d\).
If \(T\xi=0\), then \(d\xi=-\xi\); normality gives \(d^*\xi=-\xi\), whence \(z\xi=\xi\).
The infinite-order regular group element \(z\) has no nonzero fixed vector, so \(\xi=0\).
In the commuting alternative, \(H\) is finitely generated torsion-free abelian, and Fourier transform makes the nonzero group-ring polynomial \(T\) injective because its zero set has Haar measure zero.
This last assertion is the ordinary abelian polynomial certificate, already within known coefficient-field coverage.

The common-square case likewise supplies no new group-relation mechanism beyond the cyclic normalizer.
For \(w=uv^{-1}\), direct use of \(u^2=v^2\) gives
\[
vwv^{-1}=vuv^{-2}=vu^{-1}=w^{-1}.
\tag{10}
\]
Thus \(H=\langle w,v\rangle\) normalizes the cyclic subgroup generated by \(w\), exactly the known normalized-component configuration.
The direct proof above clarifies the kernel argument without claiming additional Atiyah coverage.

## Consequence and remaining scope

The positive scalar screen is now: before treating \(1+u-v\) as residual, test every available nontrivial right-orderable quotient of its supporting subgroup, not just integer characters.
The crucial preserved feature is that such a quotient leaves at most two original group labels in each coefficient fiber, whose actual inverses are certified independently.
No such quotient is supplied by torsion-freeness alone.
A new normality or one-sided-self-commutator argument for (4) cannot cross that gap, because its exact group-relation consequences are (6) and (10).
The nonindicable Promislow example remains covered by its existing four-coset proof; no assertion about its orderability is needed here.

The bounded literature check for a small-support analytic injectivity input was resolved by reusing the already registered and primary-checked Lin92 criterion at its exact scalar scope.
No literature-wide novelty or unresolved-status claim for the remaining trinomial is made.
The unrestricted actual-group trinomial problem, and still more the all-size rational Schur problem, remain beyond the conditions proved here.
The source application and the direct normality calculations are retained at this scalar scope; they do not resolve A0001.

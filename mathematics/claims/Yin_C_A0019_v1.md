---
author: Yin
---
# Regular rank from covers of the support by cyclic cosets

## Statement

Let \(G\) be a discrete torsion-free group, let \(p\in\mathcal N(G)\) be an orthogonal projection in the left regular representation, and write \(\delta:=\tau_G(p)\).
Suppose that \(p z=z\) for a nonzero vector \(z\in\mathbb C[G]\) with support of cardinality \(s\).
For an infinite cyclic subgroup \(H\le G\), let \(Y=\bigsqcup_{i=1}^k g_iH\) be the union of the left \(H\)-cosets meeting this support, and put \(L:=\{u\in G:uY=Y\}\).
Write \(E_L\) for the trace-preserving conditional expectation from \(\mathcal N(G)\) to \(\mathcal N(L)\).
Then \(L\) is cyclic, possibly trivial, and
\[
       \|p-E_Lp\|_2^2\le k\delta-1.                                      \tag{1}
\]
If \(k=1\), then \(p=1\).
For \(k\ge2\), define
\[
 t:=\frac{1-1/k}{4},\qquad
 c:=\frac{1}{2s}\left(\frac{t}{2}\right)^{2^{s-1}-1}.
\]
Then
\[
                     \delta\ \ge\ \frac{1+c^2t^2}{k}.                    \tag{2}
\]
In particular, the lower bound is uniform over the complex coefficients and over the exponents appearing in the cyclic coordinates.

If \(L=\{e\}\), then \(\delta(1-\delta)\le k\delta-1\).
For two covers of the support by respectively \(k_1,k_2\) occupied cosets of infinite cyclic subgroups, with stabilizers \(L_1,L_2\) satisfying \(L_1\cap L_2=\{e\}\), one has
\[
                  \delta(1-\delta)\le (k_1+k_2)\delta-2.                 \tag{3}
\]
In particular, for a single cover with trivial stabilizer,
\[
                   \delta\ge \frac{\sqrt{(k-1)^2+4}-(k-1)}2 .
\]

For \(a\in\mathbb C[G]\), write \(r_G(a)\) for the trace of the projection onto the closed image of left convolution by \(a\).
If \(a\ne0\) is supported in at most two left cosets of an infinite cyclic subgroup, then \(r_G(a)>1/2\).
Consequently \(ab\ne0\) whenever \(a,b\in\mathbb C[G]\) are nonzero and each support has such a cover, allowing different cyclic subgroups.

## Compression to the occupied cosets

Let \(e_Y\) be coordinate projection onto \(\ell^2(Y)\), and identify this space with \(\bigoplus_{i=1}^k\ell^2(H)\) via \(h\mapsto g_i h\).
The right regular action of \(H\) is diagonal in these coordinates.
Both \(p\) and \(e_Y\) commute with that action.
The restriction \(b:=e_Y p e_Y|_{\ell^2(Y)}\) therefore belongs to \(M_k(\mathcal N(H))\), with \(0\le b\le 1\).
Its unnormalized trace \(\operatorname{Tr}_{H,k}\) is the sum of its diagonal matrix coefficients at \(\delta_{g_i}\), hence \(\operatorname{Tr}_{H,k}(b)=k\delta\).

Let \(q\) be the projection onto the closed span of the right \(H\)-translates of \(z\).
This subspace lies in \(\ell^2(Y)\) and \(p\) fixes it pointwise.
Fourier transformation on \(H\cong\mathbb Z\) identifies \(z\) with a vector \(v\) of \(k\) Laurent polynomials on \(\mathbb T\).
At least one component is nonzero almost everywhere.
The closure of the polynomial multiples of \(v\) has projection onto the line \(\mathbb C v(\theta)\) almost everywhere.
Indeed, orthogonality to all those multiples means that the scalar inner product with \(v(\theta)\) has all Fourier coefficients zero.
Thus \(\operatorname{Tr}_{H,k}(q)=1\), and \(bq=qb=q\).
Since \(b^2\ge q\),
\[
      \operatorname{Tr}_{H,k}(b-b^2)\le k\delta-1.
\]

Put \(\widehat p(u):=(p\delta_e)(u)\).
The identity \(p^2=p\) gives \(b-b^2=e_Yp(1-e_Y)pe_Y|_{\ell^2(Y)}\).
Summing its diagonal coefficients at the representatives gives
\[
 \operatorname{Tr}_{H,k}(b-b^2)
   =\sum_{i=1}^k\|(1-e_Y)p\delta_{g_i}\|_2^2
   =\sum_{u\in G} n(u)|\widehat p(u)|^2,\qquad
 n(u):=\#\{i:ug_iH\not\subset Y\}.
\]
Left multiplication preserves distinctness of the \(k\) cosets and sends each one to a whole left \(H\)-coset.
Hence \(n(u)=0\) exactly when \(uY=Y\).
The expectation \(E_L\) restricts Fourier coefficients to \(L\), so the sum dominates \(\|p-E_Lp\|_2^2\).
This proves (1), and \(k=1\) forces \(\delta=1\) and \(p=1\) by faithfulness.
For \(L=\{e\}\), the squared norm on the left is \(\delta-\delta^2\).
For two stabilizers with trivial intersection, each nonidentity coefficient is counted at least once in the two sums over their complements, which proves (3).

## The stabilizer

The action of \(L\) on the finite set of occupied left cosets has a finite-index point stabilizer \(L\cap g_1 H g_1^{-1}\), which is cyclic.
The kernel \(C\) of this permutation action is a normal subgroup of finite index in \(L\) contained in that cyclic group.
If \(C\) is trivial, \(L\) is finite and torsion-freeness makes \(L\) trivial.
Otherwise choose a generator \(d\) of \(C\).
Any \(u\in L\) satisfies \(u^m=d^j\) for some \(m\ge1\) and integer \(j\).
If \(u\) conjugated \(d\) to \(d^{-1}\), conjugating this equality by \(u\) would force \(j=0\) and hence \(u=e\), which fixes \(d\).
It follows that \(C\) is central.
Choose representatives \(v_i\) of the \(r:=[L:C]\) cosets and define integers \(a_i(u)\) by \(u v_i=v_{\pi_u(i)}d^{a_i(u)}\), where \(\pi_u\) is the coset permutation.
Then \(T(u):=\sum_i a_i(u)\) is a homomorphism to \(\mathbb Z\), and \(T(d)=r\).
The equalities \(T(u)=0\) and \(u^m=d^j\) give \(rj=0\), hence \(u=e\).
Thus \(L\) embeds in \(\mathbb Z\).

## A coefficient-independent estimate on the circle

Write \(e_n(x):=\exp(2\pi\mathrm i nx)\) on \(\mathbb R/\mathbb Z\) with Haar probability measure.
Suppose \(f=\sum_{j=1}^d b_j e_{n_j}\) has distinct frequencies and nonzero coefficients, with \(M:=\max_j|b_j|\).
If \(|f|\le\eta\) on a measurable set of measure at least \(u\), \(0<u\le1\), then
\[
                 \eta\ge M (u/2)^{\,2^{d-1}-1}.                        \tag{4}
\]
For \(d=1\) the modulus is constant.
For \(d\ge2\), choose a subset \(D\) of the given set of measure \(u\), an index \(j\) of a largest coefficient, and another index \(l\).
For \(m(h):=|D\cap(D-h)|\), translation invariance gives \(0\le m(h)\le u\) and \(\int m(h)\,dh=u^2\).
The set where \(|e_{n_j-n_l}(h)-1|<u\) has measure \(2\arcsin(u/2)/\pi\le u/2\), because \(n_j-n_l\ne0\) and \(\arcsin v\le \pi v/2\) for \(0\le v\le1\).
Integrating \(m\) over the complement gives at least \(u^2/2\).
Choose \(h\) in that complement with \(m(h)\ge u^2/2\).
The polynomial \(f(x+h)-e_{n_l}(h)f(x)\) has at most \(d-1\) terms and a coefficient of modulus at least \(Mu\).
It has modulus at most \(2\eta\) on the overlap.
Applying the induction estimate at measure \(u^2/2\) gives (4), since
\[
 (u/2)\big((u^2/2)/2\big)^{\,2^{d-2}-1}=(u/2)^{\,2^{d-1}-1}.
\]

## Quantitative trace bound

Normalize \(\|z\|_1=1\) and set \(B:=E_Lp\), a positive contraction of trace \(\delta\).
Right multiplication by \(z\) on the group algebra extends to a bounded operator on \(\ell^2(G)\) of norm at most \(\|z\|_1\), commuting with left convolution.
Since \(p z=z\), (1) yields
\[
                         \|(1-B)z\|_2^2\le k\delta-1 .                   \tag{5}
\]
For infinite cyclic \(L\), the left action of \(B\) on each right coset \(Lv\) is given under Fourier transformation by the same symbol \(b_L\) on \(\mathbb T\), where \(0\le b_L\le1\) and \(\int b_L=\delta\).
Choose a right coset containing a coordinate of \(z\) of largest absolute value.
Its restriction to that coset gives a polynomial \(f\) with at most \(s\) terms and a coefficient of modulus at least \(1/s\).
If \(L\) is trivial the same integral formulas hold using constant functions \(b_L=\delta\) and \(f\) equal to that coordinate.
In both cases (4) implies that \(|f|\ge c\) outside a set of measure less than \(t\).
Indeed, on a set of measure \(t\) the bound \(|f|\le c\) would contradict (4) by the defining factor \(1/2\) in \(c\).
If \(\delta\le 1-2t\), it follows that \(\int_{\{|f|\ge c\}}(1-b_L)\ge t\).
Cauchy–Schwarz gives
\[
 k\delta-1\ \ge\ \|(1-B)z\|_2^2
 \ \ge\ \int_{\mathbb T}(1-b_L)^2|f|^2
 \ \ge\ c^2 t^2 .
\]
If \(\delta>1-2t\), then \(k\delta-1>(k-1)/2\ge c^2t^2\).
These two cases prove (2).

## Consequences for group-ring products

Take \(p\) to be the range projection of left convolution by \(a\ne0\).
It fixes the vector \(a\delta_e\), whose support is the support of \(a\), so (1) and (2) apply with \(\delta=r_G(a)\).
If the support has \(s\ge2\) elements, choose distinct \(u,v\) in it and take \(H=\langle u^{-1}v\rangle\).
This subgroup is infinite cyclic and \(u,v\) belong to a single left \(H\)-coset, so \(k\le s-1\).
In particular any witness supported in \(s\ge3\) points forces \(r_G(a)>1/(s-1)\).

For a bounded scalar convolution, polar decomposition equates the traces of its range and initial projections, giving \(r_G(a^*)=r_G(a)\) and \(\dim_G\ker a=1-r_G(a)\).
If \(ab=0\), the closed image of \(b\) lies in \(\ker a\) and therefore \(r_G(a)+r_G(b)\le1\).
Applied to each factor with its own left-coset cover, the two-coset bound gives a contradiction.

For the [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract), [finite-support kernel localization](Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) supplies finite scalar zero products from any amenable counterexample.
The exclusion proved here restricts the two supports of such a witness.
A general finite support may occupy many cosets of every infinite cyclic subgroup, and in that regime the sum of the two lower bounds can be below one.

## Assessment history

### Decision cyclic-cosets

| Field | Value |
| --- | --- |
| date | 2026-11-16T23:23 |
| status | proved |
| reason | The independent review covers the complete fixed statement and proof at the indicated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cyclic-coset concentration, the explicit uniform bound, stabilizer estimates and the two-factor exclusion. |
| argument | [Proof](#compression-to-the-occupied-cosets) | All hypotheses, coset orientations and the range-rank consequences. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0050_v1.md#whole-argument-finding) | Independent review of the complete claim, including its limits for A0001. |

## Current assessment

[Selected decision](#decision-cyclic-cosets)

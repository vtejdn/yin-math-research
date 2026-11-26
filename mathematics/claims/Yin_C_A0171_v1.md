---
author: Yin
---

# A finite complex rank test on the ranges of a commutator solution

## Statement

Let \(G\) be a finitely generated torsion-free group, \(M=\mathcal N(G)\), \(H=\ell^2(G)=L^2(M)\), \(U=L^0(M)\), and \(D_G\) the division closure of \(\mathbb CG\) in \(U\).
Use a finite marking \(X_1,\ldots,X_d\) of \(G\), identifying each marked group element with its left multiplier in \(M\).
For a nontrivial group, assume the marking has a nonempty freely reduced relator when its labels are treated as free generators.
Every symmetric marking of a nontrivial torsion-free group satisfies this assumption, since the distinct labels of a nonidentity element and its inverse give a two-letter relator.

For \(u\in U\), consider \(s,a,b,t\in M\) and finite-rank \(T_j\in B(H)\) satisfying
\[
 s,t\in U^\times,\qquad u=s^{-1}a=bt^{-1},\qquad
 \sum_j[\rho_j,T_j]=sP_e b-aP_e t,                                      \tag{1}
\]
where \(\rho_j\xi=\xi X_j\) and \(P_e\) projects onto \(\mathbb C\delta_e\).
Identify \(H\subset U\), and form the finite-dimensional complex space prescribed by these witnesses,
\[
                 V=\mathbb C1+s^{-1}\sum_j\operatorname{Ran}T_j .
\]
In the algebraic tensor product \(U\otimes_{\mathbb C}U\), write
\[
 \delta v=v\otimes1-1\otimes v,\qquad
 \Psi_j(l\otimes r)=lX_j\otimes r-l\otimes X_jr .
\]
Then \(u\in D_G\) if and only if (1) has witnesses for which
\[
                     \delta V\ \subseteq\ \sum_j\Psi_j(V\otimes_{\mathbb C}V). \tag{2}
\]
One may require \(s=t\) to be a positive injective contraction.

For a basis \(v_1,\ldots,v_n\) of the prescribed \(V\), take coordinates in \(E\otimes_{\mathbb C} F\), with \(E=V+\sum_j VX_j\) and \(F=V+\sum_j X_jV\).
Form the complex matrix \(C\) with columns \(\Psi_j(v_i\otimes v_k)\) and the complex matrix \(B\) with columns \(\delta v_i\).
Condition (2) is the scalar rank equality \(\operatorname{rank}_{\mathbb C} C=\operatorname{rank}_{\mathbb C}[C\ B]\).
Given the linear relations in the two finite lists of first translates, this uses ordinary finite-dimensional linear algebra.
It replaces the [Hilbert-space kernel test on the witness ranges](Yin_C_A0131_v4.md#statement) at the level of existence of witnesses.
Complete deletion of a test on the witnesses remains open for general torsion-free \(G\).

## Argument

### Tensor identities on a finite-dimensional space

For any finite marking, \(u\in D_G\) if and only if there exists a finite-dimensional complex \(W\subset U\) containing \(1,u\) with \(\delta W\subseteq\sum_j\Psi_j(W\otimes_{\mathbb C}W)\).
To see sufficiency, consider any complex-linear \(\phi:W+\sum_j WX_j\to U\) with \(\phi(1)=0\) and \(\phi(wX_j)=\phi(w)X_j\) on \(W\).
Apply \(\phi\) to the first factor of a tensor identity for \(\delta w\), then multiply the two factors in \(U\).
Every boundary on the right maps to zero and the left side maps to \(\phi(w)\).
Thus \(\phi\) vanishes throughout \(W\), and the [whole-space criterion](Yin_C_A0137_v1.md#testing-a-whole-space-or-a-single-vector) gives \(W\subset D_G\) by applying it to each element of \(W\).

For necessity take an [affine realization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) \(u=\alpha J\beta\), where \(J=L^{-1}\), \(L=L_0+\sum_j L_jX_j\), and \(\alpha,\beta,L_j\) have complex entries.
Take \(W\) to be the span of \(1\) and all entries of \(J\), so that \(u\in W\).
The inverse difference identity in matrices over \(U\otimes_{\mathbb C}U\) gives
\[
 \delta J_{ik}
   =-\sum_{j,p,q}(L_j)_{pq}\,\Psi_j(J_{ip}\otimes J_{qk}).
\]
Indeed this is the \((i,k)\) entry of \((J\otimes1)((1\otimes L)-(L\otimes1))(1\otimes J)\), with the two embeddings applied entrywise.
This proves the assertion for \(W\).

Suppose now that (1) and (2) hold on the prescribed \(V\).
The same vanishing argument gives \(V\subset D_G\).
The left side of (1) has range in \(sE\), and its value at \(t^*\delta_e\) is \(s\tau(bt^*)-a\tau(tt^*)\).
Since \(\tau(tt^*)>0\), division on the left by \(s\) gives \(u\in E\subset D_G\).
This proves sufficiency on every marking.

### Realizing the prescribed space

Let \(G\) be nontrivial, and choose \(W\) from the inverse difference identity.
For a basis \(w_i\) of \(W\), take
\[
                 c=\left(1+\sum_i(w_iw_i^*+w_i^*w_i)\right)^{-1/2}.
\]
It is a positive injective contraction in \(M\), and \(cw_i,w_ic\in M\) since both \(cw_iw_i^*c\) and \(cw_i^*w_ic\) are bounded by \(1\).
Write \(\delta u=\sum_j\Psi_j(d_j)\) with \(d_j\in W\otimes_{\mathbb C}W\).
The identification \(\Theta(l\otimes r)\xi=l\tau(r\xi)\) from \(H\otimes_{\mathbb C}H\) to finite-rank operators sends \(\Psi_j\) to the commutator with \(\rho_j\). [Finite-rank tensor identity](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
Multiply the first tensor factors of \(d_j\) by \(c\) on the left and their second factors by \(c\) on the right.
The resulting operators \(T_j^0=-\Theta(c d_j c)\) satisfy (1) with \(s=t=c\), \(a=cu\), \(b=uc\), and every range lies in \(cW\).

Choose a shortest nonempty freely reduced relator of length \(\ell\), cyclically rotated and inverted if necessary to start with a positive letter.
Orient its edges by each positive generator from the tail \(q\) to the head \(h=qX_j\), and give each edge the sign \(\epsilon\) of its traversal.
Let \(S\) be the set of positive tails and \(D\) the ball of radius \(\ell\) in the word metric of the marking and its inverses.
In particular \(e\in S\cap D\).
For each \(j\), form \(b_j=\sum\epsilon q\otimes h^{-1}\) over its edges.
The sum \(\sum_j\Psi_j(b_j)\) telescopes to zero around the cycle, and the heads of a given label are distinct. [Shortest relator cycle](Yin_C_A0131_v4.md#an-infinite-group-with-a-relator-in-the-chosen-generators)

For every \(i\) and \(b\in D\), add \(\Theta(cw_i b\, b_j k_{i,b})\) to \(T_j^0\), where the products on \(b_j\) act on its outer tensor factors.
Choose the group elements \(k_{i,b}\) so that the second factors \(h^{-1}k_{i,b}\) avoid a finite coordinate set on which the span of the old second factors restricts injectively, and so that the inverse-head sets for different \((i,b)\) have pairwise disjoint translates.
Such a finite coordinate set exists by finite dimensionality, and at each choice only finitely many translates are forbidden in the infinite group \(G\).
For a fixed label, its new second factors are therefore distinct group vectors, linearly independent modulo the old second-factor space.
The commutator sum is unchanged because each added tuple has zero boundary.
Contracting the second factors against linear functionals now shows that the new range for each label is the sum of its old range and the spans of all its added first factors. [Range of the perturbed tensor](Yin_C_A0131_v4.md#an-infinite-group-with-a-relator-in-the-chosen-generators)
Thus the prescribed normalized space for this one solution is exactly
\[
                       V=\sum_{b\in D,\ q\in S} Wbq .
\]
Indeed the old ranges normalize into \(W\), and \(e\) occurs in both indexing sets.

To verify (2), take \(w\in W\), \(b\in D\), \(q\in S\), and write
\[
                \delta(wbq)=(\delta w)bq+w(\delta b)q+wb\,\delta q ,
\]
where each product again acts on the outer tensor factor.
The first term has a boundary representation with first factors in \(W\) and second factors in \(Wbq\).
For a path from \(e\) to \(b\) of minimal length, \(\delta b\) is the sum of \(\epsilon\Psi_j(p\otimes h^{-1}b)\) over its edges from positive tail \(p\) to positive head \(h\), by telescoping.
Both \(p\) and \(h^{-1}b\) have word length at most \(\ell\).
Consequently \(wp\in V\) and \(h^{-1}bq\in V\), using \(1\in W\).
For \(\delta q\), use the analogous expansion along the initial segment of the relator reaching \(q\).
Each positive tail \(p\) lies in \(S\), and \(h^{-1}q\) has word length at most \(\ell\) along this segment.
Hence \(wbp\in V\) and \(h^{-1}q\in D\subset V\).
All three terms belong to \(\sum_j\Psi_j(V\otimes_{\mathbb C}V)\), proving (2).
For the trivial group \(U=\mathbb C\), and the zero tuple with \(s=t=1\) has \(V=\mathbb C1\) and \(\delta V=0\).

On a marking containing the distinct labels \(g,g^{-1}\), the construction needs only the cycle from \(e\) to \(g\) and back, based at \(e\).
Its positive tails are \(e,g\), giving \(V=W+Wg\) after one perturbation for each basis vector of \(W\).
The formula \(\delta(wg)=(\delta w)g+\Psi_g(w\otimes1)\) directly verifies (2).

### A free marking

On a free basis, (1) alone characterizes \(D_G\). [Homogeneous injectivity on a free marking](Yin_C_A0131_v4.md#a-free-marking-or-a-finite-group)
The extra tensor condition can fail there even for a group element.
Take the free group on \(x,y\) in that positive marking and put \(u=xyx\).
For any (1) witnesses the normalized tensors \(d_j=-s^{-1}\Theta^{-1}(T_j)t^{-1}\) have boundary sum \(\delta u\).
This tuple is unique in \((U\otimes_{\mathbb C}U)^2\), since any finite homogeneous tuple can be cleared simultaneously on the outer sides into \(H\otimes_{\mathbb C}H\), where homogeneous injectivity applies.
Expansion along the word gives \(d_x=1\otimes yx+xy\otimes1\) and \(d_y=x\otimes x\).
Their first factors span the normalized witness ranges, so \(V=\operatorname{span}_{\mathbb C}\{1,x,xy\}\) for every solution.
The unique boundary representation for \(\delta(xy)\) has \(x\)-label tensor \(1\otimes y\) and \(y\)-label tensor \(x\otimes1\).
Since \(y\notin V\), condition (2) fails.

## Assessment history

### Decision witness-range-tensors

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:30 |
| status | proved |
| reason | An affine inverse supplies tensor boundaries for a finite space, and a relator enlarges the ranges of one solution to a space closed under those boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The prescribed witness space, the complex matrix rank equality, one positive denominator and the exception for a free marking. |
| argument | [Argument](#argument) | Tensor difference of an inverse, homogeneous relator perturbation, finite supports along paths and the free word xyx. |
| dependency | [Whole-space criterion](Yin_C_A0137_v1.md#testing-a-whole-space-or-a-single-vector) | Vanishing on a space implies rationality of each member. |
| dependency | [Affine realization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | An affine inverse representing one rational input. |
| dependency | [Relator cycles](Yin_C_A0131_v4.md#argument) | Homogeneous padding and injectivity for a free marking. |
| review | [Witness range tensors](../audits/reviews/Yin_R_A0176_v1.md#witness-range-tensors) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-witness-range-tensors)

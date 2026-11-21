---
author: Yin
---
# Product-set and socle deficits for minimal zero-product supports

## Statement

Let \(G\) be a group and let \(k_0=\mathbb Q\) or \(\mathbb F_p\).
Let \(A=\{g_1,\ldots,g_a\}\) and \(B=\{h_1,\ldots,h_b\}\) be finite sets of distinct group elements.
Assume geometric inclusion-minimality over \(\bar k_0\): some nonzero zero product exists on these allowed supports, but none exists on a proper nonempty pair of subsets.
This means minimality over all coefficient choices over the algebraic closure.
For each actual product \(w\in AB\), put
\[
 F_w(X,Y)=\sum_{g_i h_j=w}X_iY_j,\qquad
 Z=V(F_w:w\in AB)\subseteq\mathbb P^{a-1}\times\mathbb P^{b-1}.
\]
Set
\[
 \begin{split}
 d&=a+b-2,& N&=\binom{a+b-2}{a-1},& c&=|AB|,\\
 r&=c-d,& s&=\min(a-1,b-1),&
 h_i&=\binom{a-1}{i}\binom{b-1}{i}\quad(0\le i\le s).
 \end{split}                                                    \tag{1}
\]
Here \(a,b\ge2\).
By [v1](Yin_C_A0103_v1.md#statement), \(Z\) is nonempty and finite, lies entirely in the coefficient torus, and has length \(\ell\).
The following strengthen its degree bound without discarding scheme multiplicities.

1. One has \(c\ge d\), hence \(r\ge0\), and
   \[
                         \ell\le N-r.                         \tag{2}
   \]
   If \(r>0\), the stronger bound is
   \[
                         \ell\le N-r-s+1.                     \tag{3}
   \]
   The improvement by \(s-1\) uses the socle of an Artinian reduction of the Segre coordinate ring.
   It holds in every indicated characteristic.

2. Put \(m=h_1-r=ab-c-1\), which must be nonnegative.
   With the convention \(\binom{m+i-1}{i}=0\) when \(m=0\) and \(i>0\), there is also the Hilbert-function bound
   \[
       \ell\le U_h:=
       1+\sum_{i=1}^{s}
          \min\left\{h_i,\binom{m+i-1}{i}\right\}.              \tag{4}
   \]
   Take \(U=N\) when \(r=0\), and
   \[
                         U=\min\{N-r-s+1,U_h\}
                           \quad\hbox{when }r>0.              \tag{5}
   \]
   Then \(\ell\le U\).

3. Retain the normalized table grading, degree-zero algebra and coefficient fields of v1:
   \[
   \Gamma=
   \mathbb Z^{a+b-2}/
   \langle\epsilon_i+\eta_j-\epsilon_{i'}-\eta_{j'}:
                    g_i h_j=g_{i'}h_{j'}\rangle,\qquad q=|\Gamma|,
                                                               \tag{6}
   \]
   where \(\epsilon_1=\eta_1=0\).
   If \(R\) is the normalized coefficient algebra and \(R_0\) its degree-zero subalgebra, then
   \[
              \ell=q\dim_{k_0}R_0\le U,\qquad
              q\le U,\qquad
              \dim_{k_0}R_0\le\lfloor U/q\rfloor.              \tag{7}
   \]
   For a normalized geometric point, let \(K\) be its joint coordinate field and \(F\) the image field of \(R_0\).
   Then
   \[
                         q[F:k_0]\le U.                       \tag{8}
   \]
   In characteristic zero, \([K:\mathbb Q]\le U\).
   In characteristic \(p\), writing \(q=q_pq'\) with \(q_p\) a power of \(p\) and \(p\nmid q'\), one has \([K:\mathbb F_p]\le U/q_p\).
   The normalized common support subgroup \(H\) of v1 still satisfies \(|H_{\rm ab}|\mid q\), so \(|H_{\rm ab}|\le U\).
   These are sharpenings of v1's numerical bounds; its exact grading, field, separability and minimality hypotheses remain in force.

If \(G\) is torsion-free, product-set structure supplies further restrictions.
The torsion-free inequality \(c\ge a+b-1=d+1\) alone gives
\[
                         \ell\le N-s<N.                       \tag{9}
\]
Its equality characterization, together with regularity of a factor supported in a cyclic coset, improves this to
\[
             c\ge a+b=d+2,\qquad \ell\le N-s-1.                \tag{10}
\]
If \(\max(a,b)\ge4\), the stronger small-product inequality gives
\[
             c\ge a+b+1=d+3,\qquad \ell\le N-s-2.              \tag{11}
\]
Precise source statements and the coset orientations are given below.
In particular, the Segre saturation \(q=N\), as well as \(\ell=N\), is impossible for an actual torsion-free realization.
The exclusions concern the actual number of distinct products, not the rank of an abstract lattice alone.

## Linear sections and the first deficit

Work over \(k=\bar k_0\); lengths are unchanged by this extension.
Let
\[
 S=\bigoplus_{n\ge0}
   k[X_1,\ldots,X_a]_n\otimes_k k[Y_1,\ldots,Y_b]_n
\]
be the standard graded coordinate ring of the Segre embedding.
Its dimension is \(d+1\), and \(\dim_k S_1=ab\).
It is Cohen–Macaulay.
For this particular ring the cohomological criterion is direct: projective-space cohomology and the product formula give
\[
 H^j(\mathbb P^{a-1}\times\mathbb P^{b-1},
                     \mathcal O(n,n))=0
              \quad(0<j<d,\ n\in\mathbb Z).                  \tag{12}
\]
A mixed contribution would require the same integer \(n\) to support both degree-zero cohomology on one factor and top cohomology on the other, which is impossible.
The ring is the full section ring, so \(H^0_{S_+}(S)\) and \(H^1_{S_+}(S)\) also vanish.
The local-cohomology description of section rings therefore gives depth \(d+1\).
This is also the polynomial-ring case of the Segre product facts in [HHS19, §4.4](../literature/pdf/HHS19--arxiv-v3.pdf#page=17).

The \(c\) forms \(F_w\in S_1\) are linearly independent: their nonempty monomial supports partition the \(ab\) distinct monomials \(X_iY_j\).
Since their projective base scheme \(Z\) is finite and nonempty, their ideal has height \(d\).
The height bound by the number of generators gives \(c\ge d\).
Choose \(d\) linear combinations \(L_1,\ldots,L_d\) of the \(F_w\) successively as a regular sequence on \(S\).
This is possible because the common projective base is zero dimensional, and at each positive-dimensional projective stage a generic member avoids the finitely many associated components.
The initial and successive quotient rings are Cohen–Macaulay, so no embedded component obstructs this choice.
The choice is over the infinite algebraically closed field \(k\), not necessarily over the finite prime field.

Put \(T=S/(L_1,\ldots,L_d)\).
This is a one-dimensional Cohen–Macaulay standard graded ring.
Its projective scheme \(Y\) contains \(Z\) and has length \(N\), as in [v1's hyperplane argument](Yin_C_A0103_v1.md#the-finite-segre-section-and-its-length).
The ring \(T\) has no irrelevant-ideal torsion.
Thus the ideal of this complete linear section is saturated in \(S\), and its degree-one part is exactly the span of \(L_1,\ldots,L_d\).
Equivalently, no further linear form vanishes scheme-theoretically on all of \(Y\).
A merely set-theoretic count of \(Y\) would not justify this conclusion.

Let \(J\subset T\) be the saturated homogeneous ideal of \(Z\) in \(Y\).
It contains the images of all the \(F_w\), whose span in \(T_1\) has dimension \(r=c-d\).
The exact sequence
\[
       0\longrightarrow\widetilde J(1)
       \longrightarrow\mathcal O_Y(1)
       \longrightarrow\mathcal O_Z(1)\longrightarrow0
\]
on the finite scheme \(Y\) gives
\[
              \dim_k H^0(Y,\widetilde J(1))=N-\ell.
\]
The map \(J_1\to H^0(Y,\widetilde J(1))\) is injective, because \(T\) has no irrelevant-ideal torsion.
Consequently \(N-\ell\ge\dim_kJ_1\ge r\), proving (2).
This checks independence modulo the chosen complete intersection, rather than only independence in the original polynomial ring.

## Artinian reduction and its socle

Choose a further linear form \(\lambda\in T_1\) that is a non-zero-divisor both on \(T\) and on \(T/J\).
Such a choice exists by avoiding the finitely many points of \(Y\).
A saturated coordinate ring of a nonempty zero-dimensional projective scheme has depth one, so \(T/J\) is Cohen–Macaulay as well.
Define
\[
       \mathcal A=T/\lambda T,\qquad
       \mathcal B=(T/J)/\lambda(T/J),\qquad
       I=\ker(\mathcal A\longrightarrow\mathcal B).            \tag{13}
\]
Their dimensions are \(N,\ell\), and \(N-\ell\), respectively.
Non-zero-divisibility on \(T/J\) gives
\[
                 J\cap\lambda T=\lambda J.
\]
Since \(J_0=0\), it follows that \(I_1\cong J_1\).
In particular
\[
                       \dim_k I_1\ge r.                     \tag{14}
\]

The Hilbert series identity
\[
 \sum_{n\ge0}
       \binom{n+a-1}{a-1}\binom{n+b-1}{b-1}t^n
   =
 \frac{\displaystyle\sum_{i=0}^{s}
         \binom{a-1}{i}\binom{b-1}{i}t^i}
      {(1-t)^{a+b-1}}                                      \tag{15}
\]
follows from the binomial coefficient identities, or by induction on \(a,b\).
The \(d+1=a+b-1\) regular linear forms multiply this series by \((1-t)^{d+1}\).
Therefore
\[
                 \dim_k\mathcal A_i=h_i\quad(0\le i\le s),
              \qquad \mathcal A_i=0\quad(i>s).               \tag{16}
\]

There is no socle below degree \(s\):
\[
          \operatorname{Soc}(\mathcal A)
          :=\{u:\mathcal A_+u=0\}
          =\mathcal A_s.                                    \tag{17}
\]
Here is the canonical-module calculation, including the degree shift.
Assume \(a\le b\), so \(s=a-1\).
For the polynomial Segre ring,
\[
       (\omega_S)_n
          =k[X_1,\ldots,X_a]_{n-a}
               \otimes_k k[Y_1,\ldots,Y_b]_{n-b},             \tag{18}
\]
with negative degrees interpreted as zero.
This is the Segre canonical-module formula used in the proof of HHS19, Theorem 4.15, on PDF/printed page 17.
Its assumptions hold: both polynomial rings are standard graded Gorenstein of dimensions at least two, and \(S\) is Cohen–Macaulay.
The formula also follows by dualizing the top diagonal cohomology in (12).
The first nonzero degree in (18) is \(b\).
Polynomial multiplication shows that \(\omega_S\) is generated by that degree: multiplication of degree \(n-b\) in \(S\) with \(k[X]_{b-a}\otimes k[Y]_0\) spans the entire displayed degree \(n\).
For the regular sequence of \(d+1\) linear forms,
\[
 \omega_{\mathcal A}\cong
   \big(\omega_S/(L_1,\ldots,L_d,\lambda)\omega_S\big)(d+1).
                                                               \tag{19}
\]
The regular sequence is also regular on the maximal Cohen–Macaulay module \(\omega_S\); each linear quotient induces the displayed shift by one.
Thus all its minimal generators have degree \(b-(d+1)=-(a-1)=-s\).
The canonical module of a finite graded \(k\)-algebra is its graded \(k\)-dual.
The dual of \(\omega_{\mathcal A}/\mathcal A_+\omega_{\mathcal A}\) is precisely \(\operatorname{Soc}(\mathcal A)\), with degrees reversed.
This proves (17); the case \(b\le a\) is symmetric.
The argument requires neither reducedness nor characteristic zero.

If \(r>0\), choose \(0\ne u\in I_1\).
In a finite standard graded algebra, repeatedly multiplying a homogeneous element by degree-one elements until further multiplication vanishes reaches a nonzero socle element.
By (17) the first such endpoint cannot occur below degree \(s\).
There is therefore a nonzero chain through every degree \(1,\ldots,s\), all contained in the ideal \(I\).
Using (14) at degree one gives
\[
              N-\ell=\sum_i\dim_k I_i
                    \ge r+\sum_{i=2}^{s}1=r+s-1,
\]
which proves (3).
More precisely, equality forces
\[
                  \dim_kI_1=r,\qquad
                  \dim_kI_i=1\quad(2\le i\le s).              \tag{20}
\]
These are necessary conditions on the actual multiplication maps of the reduction, not automatic properties of a supplied table.

## Hilbert-function and finite multiplication tests

The quotient \(\mathcal B\) is standard graded and satisfies
\[
      \dim_k\mathcal B_1
          =h_1-\dim_kI_1\le h_1-r=m.
\]
A standard graded algebra with at most \(m\) degree-one generators is a quotient of a polynomial ring in \(m\) variables.
Consequently
\[
     \dim_k\mathcal B_i
        \le\min\left\{h_i,\binom{m+i-1}{i}\right\}
                \quad(1\le i\le s),
\]
and summing proves (4).
If \(m<0\), the proposed minimal coefficient scheme cannot exist.
When \(r=0\), (4) is at most \(N\), but no positive socle deficit is asserted.

The reduction also gives a finite multiplication-rank lower bound for the deficit.
Let \(V\subseteq\mathcal A_1\) be the \(r\)-dimensional span of the residual fiber forms.
Their span in \(T_1\) lies in \(J_1\), whereas \(\lambda\notin J_1\), so passing to \(\mathcal A_1\) preserves this dimension.
For \(1\le i\le s\), form the ordinary finite-dimensional multiplication map
\[
       \mu_i:V\otimes_k\mathcal A_{i-1}
                    \longrightarrow\mathcal A_i,\qquad
                         v\otimes u\longmapsto vu.            \tag{21}
\]
Since its image lies in \(I_i\),
\[
                      N-\ell\ge
                         \sum_{i=1}^{s}\operatorname{rank}\mu_i.
                                                               \tag{22}
\]
This is a sufficient table-specific improvement after choosing and verifying the regular linear section.
The image \(I\) of the saturated ideal \(J\) can contain more than the ideal generated by \(V\), so equality in (22) is not automatic.
The universal socle bound uses only \(\operatorname{rank}\mu_1=r\) and the fact that every higher image is nonzero.
It does not assert a Lefschetz property for these particular fiber forms.

For example, when \(a=3\) and \(b\ge3\), one has
\[
       (h_0,h_1,h_2)
          =\left(1,\,2(b-1),\,\binom{b-1}{2}\right).
\]
If \(r>0\), at least one quadratic contribution is forced, so the deficit is at least \(r+1\).
A claim of deficit exactly \(r\) in this range would contradict (17).
For \(a=b\), the Artinian reduction is Gorenstein, but this fact alone does not establish a larger uniform rank for every \(\mu_i\).
No additional multiplication-rank bound is assumed in (3).

## Torsion-free product sets and coset regularity

The source used here is the complete arXiv v1 of Böröczky–Pálfy–Serra, [BPS12](../literature/pdf/BPS12--arxiv-v1.pdf), dated 30 September 2010.
Its introduction on PDF/printed page 2 states the following classical results for finite nonempty subsets of an arbitrary torsion-free group:

- Equation (4), attributed to Kemperman, gives \(c\ge a+b-1\).
- The paragraph immediately after (4), attributed to Brailovsky–Freiman, says that when \(a,b\ge2\), equality forces \(A\) and \(B\), up to appropriate left and right translations, to be progressions of a common cyclic subgroup.
  In particular \(A\) is contained in a left cyclic coset and \(B\) in a right cyclic coset.
- Equation (5), attributed to Hamidoune–Lladó–Serra, gives \(c\ge a+b+1\) when \(b\ge4\) and \(A\) is not contained in a left cyclic coset.

These are the exact statements inspected in this primary research paper; the older original proofs are not independently re-audited here.
No commutativity, ordering or unique-product hypothesis is added.

A nonzero element supported in a left coset \(u\langle t\rangle\) of a cyclic subgroup of a torsion-free group is left-regular over every field.
Indeed write it as \(u f(t)\), where \(f\) is a nonzero Laurent polynomial; for a nontrivial subgroup \(t\) has infinite order.
Left multiplication by \(f(t)\) preserves each right coset \(\langle t\rangle v\).
On each such coset it is multiplication by \(f\) in the Laurent polynomial domain \(k[t^{\pm1}]\).
It is therefore injective on every finitely supported component.
The trivial cyclic subgroup gives a monomial unit and the same conclusion.
The symmetric argument proves right-regularity for a factor supported in a right cyclic coset.
Thus neither cyclic containment can occur for a nonzero zero-product pair.

Equation (4) gives \(r\ge1\), and (3) yields (9).
Its equality case is excluded by cyclic-coset regularity, so \(r\ge2\), giving (10).
If \(b\ge4\), equation (5) gives \(r\ge3\), proving (11).
If instead \(a\ge4\), apply equation (5) to \(B^{-1},A^{-1}\).
The anti-isomorphism \(g\mapsto g^{-1}\) carries the original zero product to one in that reversed order.
The absence of a right cyclic coset for \(B\) is exactly the absence of a left cyclic coset for \(B^{-1}\), and \(|B^{-1}A^{-1}|=|AB|\).
This checks the orientation needed for the symmetric assertion.

Theorem 2 and its following remark in the same BPS12 edition, PDF/printed page 3, give a quantitative version:
for every integer \(k\ge1\), if \(A\) is not in a left cyclic coset and \(b>32(k+3)^6\), then \(c>a+b+k\).
The strict inequalities imply \(r\ge k+3\).
After applying inverses when necessary, a zero-product support pair with \(\max(a,b)>32(k+3)^6\) therefore satisfies
\[
                         \ell\le N-k-s-2.                    \tag{23}
\]
This uses the constants and strict inequalities of the inspected v1, without substituting another edition.

## Arithmetic consequences and limits

The unit-grading proof of [v1](Yin_C_A0103_v1.md#the-normalized-coefficient-algebra-and-a-finite-basis) gives \(\ell=q\dim R_0\) in every characteristic, including the full \(p\)-part of \(q\).
Its field proof gives \(q[F:k_0]\le\ell\), \([K:F]\le q\) in characteristic zero and \([K:F]\le q'\) in characteristic \(p\).
Substituting \(\ell\le U\) proves (7)–(8) and the joint field bounds.
The divisibility \(|H_{\rm ab}|\mid q\) is unchanged.
The geometric coefficient count is at most \(U\) in characteristic zero and at most \(U/q_p\) in characteristic \(p\), while remaining a multiple of \(q\) or \(q'\), respectively.

A finite table with \(q>N-r-s+1\), for \(r>0\), cannot satisfy the geometric minimality and existence assumptions even before group realizability is decided.
For an actual torsion-free realization, (9)–(11) make this stricter.
As a numerical screen, \(a=3,b=13\) gives \(N=91,s=2\), and (11) yields \(\ell\le87\).
Orders \(q=88,89,90,91\) are therefore excluded in this support range.
This calculation is not an example of a realizable zero-product table.

Small invariant quotient dimension has a precise consequence but supplies no further group obstruction here.
If \(q>U/2\), then (7) forces \(\dim R_0=1\), hence \(R_0=k_0\) and \(\ell=q\).
In characteristic zero the explicit binomial algebra of v1 is then geometrically reduced, with one free orbit under the table-character group.
In characteristic \(p\) the same fiber has \(q'\) geometric points and length \(q\).
Nothing proved here forces an extra Galois orbit or \(\dim R_0\ge2\) for every torsion-free realization.
Such a conclusion would require input beyond the product count and the Segre socle calculation.

For comparison, the actual torsion example \(A=B=\{1,t\}\subset C_2\) from v1 has
\[
                         c=d=2,\quad r=0,\quad N=\ell=q=2.
\]
It attains the old Segre bound in all characteristics; in characteristic two it is one geometric point of length two.
Thus the excluded torsion-free saturation uses group structure, and the characteristic-two distinction cannot be removed.
The present bounds do not decide torsion-free realizability for the surviving tables and do not settle the complex zero-divisor conjecture.

## Assessment history

### Decision socle-deficit

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:15 |
| status | proved |
| reason | Independent review checks the Artinian reduction, the socle, source hypotheses and the consequences in both characteristics. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Length, graded arithmetic and product-set bounds on a geometrically inclusion-minimal pair. |
| argument | [Proof](#linear-sections-and-the-first-deficit) | The linear section, its Artinian reduction, the multiplication tests, torsion-free product bounds and arithmetic conclusions. |
| review | [Whole finding](../audits/reviews/Yin_R_A0139_v2.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Minimal support algebra](Yin_C_A0103_v1.md#decision-minimal-support-degree) | The finite coefficient scheme, normalized grading, common support subgroup and coordinate fields. |

## Current assessment

[Selected decision](#decision-socle-deficit)

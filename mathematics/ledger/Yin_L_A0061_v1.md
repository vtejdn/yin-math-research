---
author: Yin
---

# Compression tests for integral lifts of a modular right inverse and annihilator

This analysis records coefficient choices, sufficient compression tests and geometric restrictions for [A0002](../tasks/Yin_T_A0002_v1.md#contract).
The fixed general transfer and spectral exclusion are proved in [C_A0039 v3](../claims/Yin_C_A0039_v3.md#statement).
The additional calibrations here are development calculations.

## Fixed integral coefficients and two obstructions to automatic compression

Let \(a,b,c\in\mathbb F_p[G]\) satisfy \(ab=1\), \(ac=0\), and \(c\ne0\).
Fix integral lifts \(A,B,C\), and put
\[
 f=AB=1-pD,\qquad r=AC=pF,\qquad D,F\in\mathbb Z[G].
\]
The primitive finite-precision annihilators from [C_A0039 v2](../claims/Yin_C_A0039_v2.md#all-precisions-from-one-modular-right-inverse) can be written
\[
 C_e=C-pB\sum_{j=0}^{e-2}p^jD^jF,\qquad
 AC_e=p^eD^{e-1}F,\qquad C_e\bmod p=c.                 \tag{1}
\]
All support counts refer to collected group elements.
The discussion fixes \(A\); modifying an integral coefficient by a multiple of \(p\) can change its characteristic-zero kernel.

The modular relations alone cannot guarantee sublinear support growth for every integral lift, even when the actual group and the support of the left factor are fixed.
Use the actual torsion-free group and modular triple supplied by Mghirbi–Douglas, and choose integral representatives on precisely \(\operatorname{supp}a\).
At one \(g_0\in\operatorname{supp}a\), change the coefficient by a sufficiently large multiple of \(p\) to obtain
\[
                    |A_{g_0}|>\sum_{g\ne g_0}|A_g|.
\]
The support and reduction of \(A\) are unchanged.
Factoring out \(A_{g_0}g_0\) gives a Neumann-series inverse in \(\ell^1(\mathbb C[G])\).
Thus \(A\) has no nonzero finite complex annihilator.
Nevertheless (1) supplies primitive annihilators modulo every \(p^e\).
C_A0039_v2 therefore gives
\[
                 s_e\ge e\log p/\log\|A\|_2
\]
whenever \(s_e\) is finite, which it is here.
This is an example in the original source group, with the original collected modular support.
It does not rule out a favorable small-coefficient or canonical occurrence lift.

A second source-based obstruction avoids coefficient dominance and gives a simpler linear lower bound.
Let \(H\) be the actual torsion-free source group, let \(A_0\in\mathbb Z[H]\) lift \(a\), and pass to
\[
                 G=H\times\langle t\rangle,\qquad
                 A=A_0+p^k t,\qquad k\ge1.
\]
The modular triple embeds unchanged, so primitive annihilators again exist at every precision.
There is no finite complex annihilator: for a nonzero Laurent polynomial \(v(t)\) with coefficients in \(\mathbb C[H]\), the highest \(t\)-degree term of \(Av\) has coefficient \(p^k\) times the highest coefficient of \(v\), and is nonzero.
No zero-divisor assumption on \(\mathbb C[H]\) is needed.

In fact every primitive annihilator modulo \(p^e\) has at least \(\lceil e/k\rceil\) distinct \(t\)-layers and therefore at least that many group elements in its support.
Write it as \(\sum_j v_jt^j\), and choose a layer \(v_j\) with a coefficient not divisible by \(p\).
The coefficient recurrence is
\[
                   A_0v_{j+\ell}+p^k v_{j+\ell-1}=0.
\]
For a group-ring coefficient vector modulo \(p^e\), let its valuation be the least coefficient valuation, with valuation \(e\) for zero.
Multiplication by integral \(A_0\) cannot lower valuation.
Inductively the displayed equation forces
\[
 v_p(v_{j+\ell})\le k\ell<e
       \qquad(0\le\ell<\lceil e/k\rceil).
\]
Indeed the previous layer, multiplied by \(p^k\), is still nonzero whenever the indicated next index is needed.
Thus
\[
                            s_e\ge\lceil e/k\rceil.            \tag{2}
\]
This modifies the ambient group to \(H\times\mathbb Z\) and adds a coefficient that disappears modulo \(p\).
Torsion-freeness is preserved; the source's word-hyperbolicity conclusion is not claimed for the product group.
No matching linear upper bound for \(s_e\) is asserted.

## A finite common-multiple certificate

For the fixed lift, suppose one can find finite \(R,H_1\in\mathbb Z[G]\) such that
\[
                  FR=fH_1,\qquad R\equiv1\pmod p.             \tag{3}
\]
Then
\[
                         V=CR-pBH_1
\]
is an exact integral annihilator of \(A\), and \(V\bmod p=c\ne0\).
Indeed \(AV=pFR-pfH_1=0\).
Thus a finite right common multiple with this residue condition replaces the infinite correction sum.
The condition is sufficient; a finite characteristic-zero kernel need not have been presented in this form.

A particularly small certificate is commutation of the two correction terms:
\[
 [D,F]=0
 \quad\Longrightarrow\quad
 V=Cf-Br=CAB-BAC,\qquad AV=0,\qquad V\bmod p=c.
                                                                    \tag{4}
\]
More generally, if one group element \(g\) satisfies \([D,Fg^{-1}]=0\), put
\[
             V=Cg^{-1}fg-Br.
\]
Then
\[
 AV=rg^{-1}fg-fr
   =(rg^{-1}f-frg^{-1})g=0,\qquad V\bmod p=c.
                                                                    \tag{5}
\]
These are identities in the actual group algebra.
They can be checked from finitely many group products and collected coefficients.

There is a useful precision test even when (4) is not exact:
\[
                  A(Cf-Br)=p^2[D,F].                         \tag{6}
\]
Thus divisibility of the actual commutator by \(p^m\) supplies precision \(m+2\) on the fixed support of \(Cf-Br\).
If its actual size is \(s\) and \(p^{m+2}>\|A\|_2^s\), C_A0039_v2 gives a finite complex annihilator.
The original type congruences alone do not give such enhanced commutator divisibility.

## Finite left orbits and finite commutator orbits

A finite-dimensional rational left orbit is sufficient for (3).
Suppose
\[
                 W=\operatorname{span}_{\mathbb Q}
                         \{D^jF:j\ge0\}
\]
is finite dimensional.
Choose a basis among its integral orbit vectors and let \(T\) be the finite union of their actual supports.
Then \(W\subseteq\mathbb Q^T\), and the full lattice
\[
                         \Lambda=W\cap\mathbb Z^T
\]
is stable under left multiplication by \(D\).
It is a full lattice because \(W\) is spanned by integer vectors; stability follows from integrality and invariance of \(W\).
In an integral basis of \(\Lambda\), let \(K\) be the matrix of that multiplication.
Set \(\delta=\det(I-pK)\), so \(\delta\equiv1\pmod p\).
Applying \(\operatorname{adj}(I-pK)\) to \(F\) yields an integral vector \(H_1\in\Lambda\) with
\[
                         fH_1=\delta F.
\]
Taking \(R=\delta\) in (3) gives
\[
                         V=\delta C-pBH_1,\qquad AV=0,
                         \qquad V\bmod p=c.
                                                                    \tag{7}
\]
This criterion concerns a verified finite orbit inside the actual group algebra, not a freely chosen finite matrix.
The first rational dependence of the left Krylov vectors propagates by multiplication by \(D\), so a genuine dependence supplies a finite certificate of the hypothesis.

The [finite commutator-orbit test](../claims/Yin_C_A0039_v3.md#a-finite-adjoint-orbit-test-for-an-exact-annihilator) controls the iterates of the commutator with D instead of the left powers of D.
It gives an exact annihilator reducing to the original residue up to sign whenever the orbit span is finite dimensional.
The same displayed recursion, applied to a monic polynomial of degree k whose value on the orbit is divisible by a further power p^m, gives precision k+m+1.
The support of the resulting vector must be counted after collecting its coefficients.

## A geometric compression that the source relations exclude

Suppose a subgroup \(K\le G\) and an element \(g\in G\) satisfy
\[
                \operatorname{supp}D\subseteq K,\qquad
                \operatorname{supp}F\subseteq Kg.
                                                                    \tag{12}
\]
Then every \(D^jF\) is supported in the right coset \(Kg\).
For \(K'=g^{-1}Kg\), formula (1) gives
\[
 \operatorname{supp}C_e
 \subseteq\operatorname{supp}C
       \ \cup\!
       \bigcup_{b\in\operatorname{supp}B}(bg)K'.
                                                                    \tag{13}
\]
The finite set \(\operatorname{supp}C\) can itself be covered by at most \(|\operatorname{supp}C|\) left cosets of \(K'\).
Thus all precisions use at most
\[
                   |\operatorname{supp}B|+|\operatorname{supp}C|
\]
left cosets of this one subgroup.
If \(K\) is amenable, so is \(K'\), giving the precise geometric premise for the amenable-coset transfer in [C_A0039 v3](../claims/Yin_C_A0039_v3.md#independent-translates-and-amenable-cosets).
No equality of a right coset \(Kg\) and a left coset \(gK\) is assumed.
If \(\operatorname{supp}F\) is spread over several right cosets \(Kg_i\), this argument instead produces cosets of the possibly different subgroups \(g_i^{-1}Kg_i\).
They cannot be treated as cosets of one common amenable subgroup without an additional containment hypothesis.

However, (12) with amenable \(K\) is impossible under the fixed modular triple \(ab=1,\ ac=0,\ c\ne0\).
The obstruction uses both the correction's localization and the existence of the original modular right inverse.

First, \(f=1-pD\) has no nonzero finite complex right annihilator in any group containing its support.
A finite complex kernel vector would give a nonzero rational one on the same finite support.
Clearing denominators and dividing the coefficient gcd gives a primitive integral vector \(w\) with \(fw=0\).
Reduction would then give \(\bar w=0\), a contradiction.
If \(\operatorname{supp}D\subseteq K\) with \(K\) amenable, the complete amenable kernel localization in [C_A0001 v2](../claims/Yin_C_A0001_v2.md#rational-kernel-localization) implies \(\ker_{\ell^2(K)}f=0\).
One can restrict first to the finitely generated subgroup generated by \(\operatorname{supp}D\), which is still amenable.
Left multiplication by \(f\) on \(\ell^2(G)\) is the direct sum of its copies on right cosets \(Kg\), so it also has zero analytic kernel in \(G\).
Its finite tracial support is therefore full, and \(f=AB\) is an affiliated unit.
The regular-rank inequalities
\[
                   1=\operatorname{rk}(AB)
                         \le\min(\operatorname{rk}A,\operatorname{rk}B)
\]
make \(A\) and \(B\) affiliated units as well.
In particular \(A\) has no nonzero finite complex right annihilator.

On the other hand, (13) would cover all the primitive \(C_e\) by a fixed number of left cosets of the amenable subgroup \(K'\).
C_A0039_v3 would produce a nonzero finite complex right annihilator of \(A\), a contradiction.
The same argument excludes the case of finitely many right cosets \(Kg_i\) whenever all conjugate subgroups \(g_i^{-1}Kg_i\) lie in one common amenable subgroup.
Thus, if the actual correction \(D\) is supported in an amenable subgroup, the correction \(F\) must spread across right cosets whose conjugates cannot all be absorbed in one amenable subgroup.
This is a restriction on every actual source triple and its integral lifts, not merely a missing construction.

For abelian \(K\), the contradiction can also be seen without the density criterion: \(D\) and \(Fg^{-1}\) commute, so (5) gives a finite annihilator, contradicting the preceding affiliated invertibility of \(A\).
Likewise, amenable support for \(D\) rules out the finite left-orbit and finite commutator-orbit conditions above for this nonzero residue \(c\).
Those finite certificates remain potentially discriminating when the subgroup generated by \(\operatorname{supp}D\) is not controlled by amenability.

## What the actual source gives for the corrections

The canonical occurrence lifts in Mghirbi–Douglas are
\[
 A=\sum_{x\in A'}\sigma(x)g_x,\qquad
 B=-\sum_{x'\in A'}g_{x'}^{-1},\qquad
 C=\sum_{y\in B'}h_y^{-1}.
\]
Use the [integer signed identity (7), Lemma 6.1(a), pp.18–19](../literature/pdf/MD26.pdf#page=18) and the [types of Definition 7.1 and Lemma 7.2, p.24](../literature/pdf/MD26.pdf#page=24).
For these particular lifts define the integer type corrections
\[
 \kappa_{xx'}=
   \frac{|S_x\cap S_{x'}|-1-[x=x'=r]}p,\qquad
 \lambda_{xy}=\frac{|S_x\cap S_y|-1}p.
\]
The root has \(g_r=1\) and \(\sigma(r)=1\), and it is the only root-type vertex on \(A'\); \(B'\) has no root-type vertex.
Substituting in the signed identity gives the exact integral formulas
\[
 D=-\sum_{x,x'\in A'}\sigma(x)\kappa_{xx'}g_xg_{x'}^{-1},
 \qquad
 F=-\sum_{x\in A',\,y\in B'}\sigma(x)\lambda_{xy}g_xh_y^{-1}.
                                                                    \tag{14}
\]
For example, the first signed identity reads \(0=-AB+1+p\sum\sigma(x)\kappa_{xx'}g_xg_{x'}^{-1}\), giving the sign in (14).
These are actual collected group-ring identities even though their displayed descriptions use occurrences.
They provide concrete input for the commutator and common-multiple tests.

The parameter \(q=p^5\) does not by itself yield five levels of divisibility for these corrections.
Two distinct extra blocks meet in \(p^2-p\) letters, whose contribution after division by \(p\) is \(p-1\), a unit modulo \(p\).
The root-root correction is \(p^4+p+1\), also a unit modulo \(p\).
The ordinary same-line contribution is \(q/p=p^4\), but it coexists with those terms.
These weights supply no additional termwise factor of \(p\); divisibility of the collected corrections and their commutator requires further information.
Conversely, unit occurrence weights do not prove that a collected coefficient is a unit: different occurrences can still have the same group label and cancel.
No claim that the natural source corrections fail the proposed tests follows from these weights.

The remaining geometric input is therefore specific: compute the actual supports and collected coefficients in (14), and test a finite left or commutator orbit, an exact common multiple (3), or sufficient extra divisibility in (6) or in the adjoint-orbit recurrence, while retaining the subgroup restrictions just proved.
The tempting common-amenable-coset localization is excluded and is not a constructive target for this modular triple.
Neither the modular right inverse nor the incidence congruences already establish any of the surviving compression certificates.

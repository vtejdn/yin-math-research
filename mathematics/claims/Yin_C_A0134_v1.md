---
author: Yin
---

# Rational annihilators from a coamenable subgroup

## Statement

Let \(G\) be a finitely generated discrete group and let \(H\leq G\) be coamenable, so the left action on \(G/H\) has the Følner property.
For \(J=H,G\), let \(M_J=\mathcal N(J)\), \(U_J=L^0(M_J)\), and \(D_J=\operatorname{Div}_{U_J}(\mathbb CJ)\).
The subgroup \(H\) may be infinitely generated or nonnormal.
For a rectangular affiliated matrix, \(\operatorname{rk}_J\) and \(\nu_J\) denote the von Neumann dimension of its closed range and kernel, using the group trace and unnormalized matrix traces.

Let \(P\in M_{m,n}(D_G)\), and fix a group-ring realization
\[
 P=A-BQ^{-1}C,\qquad
 L=\begin{pmatrix}A&B\\ C&Q\end{pmatrix},\qquad Q\in M_k(\mathbb CG)\cap GL_k(U_G).
\]
Here \(L\) has \(m+k\) rows and \(n+k\) columns.
Such a realization follows by taking block sums of the invertible pencils for the entries and inserting their constant rows and columns in the appropriate output and input positions. [Scalar realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Take a finite set \(S\subset G\) containing \(1\) and the supports of all entries of \(L\).
Assume first that \(D_H\) is von Neumann regular.
For every nonempty finite \(F\subset G/H\), there is a positive matrix \(b_F\in M_n(D_G\cap M_G)\) with \(Pb_F=0\) and
\[
 \nu_G(P)-\operatorname{rk}_G(L)\frac{|SF\setminus F|}{|F|}
 \ \leq\ \frac{\dim_H\ker L_F}{|F|}
 \ \leq\ \operatorname{rk}_G(b_F)
 \ \leq\ \nu_G(P).                                                   \tag{1}
\]
Here \(L_F\) is left convolution by \(L\) from inputs on \(F\) to outputs on \(SF\), with each coset represented as a copy of \(\ell^2(H)\).

In particular, for each scalar \(x\in D_G\),
\[
 \nu_G(x)=
 \sup\{\operatorname{rk}_G(b): b\in D_G\cap M_G,\ b\geq0,\ xb=0\}.     \tag{2}
\]
Every nonunit of \(D_G\) has a nonzero bounded positive right annihilator.
The supremum in (2) is attained exactly when \(p_{\ker x}\in D_G\).
Consequently the unrestricted finite-rank equation characterizes \(D_G\) if and only if every scalar right annihilator ideal in \(D_G\) is finitely generated, equivalently if and only if \(D_G\) is right coherent. [A0003](../tasks/Yin_T_A0003_v3.md#contract)
These statements apply in particular when \(G\) is torsion-free.

There are two conclusions under weaker hypotheses on the subgroup.

1. Suppose each nonunit of \(D_H\) has a nonzero right annihilator in \(D_H\).
   Then every rectangular matrix over \(D_G\) with nonzero Hilbert kernel admits a nonzero bounded kernel column over \(D_G\).
   In particular the equivalences with finite generation of scalar annihilators and right coherence still hold for \(G\).
2. Suppose the Hilbert kernel of every finite rectangular matrix over \(\mathbb CH\) is the closed linear span of the ranges of its bounded kernel columns over \(D_H\).
   Then the Hilbert kernel of every finite rectangular matrix over \(D_G\) is the closed linear span of the ranges of its bounded kernel columns over \(D_G\).
   In particular (2) holds for \(G\).

The first hypothesis supplies an individual solution for a singular matrix.
The second accounts for the entire kernel after closure.
Regularity of \(D_H\) supplies a finite family spanning each kernel on a fixed window, which gives the individual matrix \(b_F\) in (1).

<a id="argument"></a>
## Finite coset matrices

Choose representatives \(g_c\) of the left cosets \(c\in G/H\).
The isometry \(J_F\) carries the \(c\)-coordinate of \(\ell^2(H)^F\) onto \(\ell^2(g_cH)\) by \(\delta_h\mapsto\delta_{g_ch}\).
Use the same notation for its coordinate amplifications and write \(C_F=J_FJ_F^*\).
The rectangular matrix \(L_F=J_{SF}^*LJ_F\) has entries in \(\mathbb CH\).
Indeed a term \(\lambda_G(s)\) sends input \(c\) to output \(sc\) with block \(\lambda_H(g_{sc}^{-1}sg_c)\).
All its outputs lie over \(SF\).

If \(\pi\) projects onto a closed right-\(G\)-invariant subspace of \(\ell^2(G)^d\), then
\[
 (\operatorname{Tr}\otimes\tau_H)(J_F^*\pi J_F)
       = |F|(\operatorname{Tr}_d\otimes\tau_G)(\pi).
\]
Right translation identifies the diagonal inner product at \(\delta_{g_c}\) with the one at \(\delta_e\) in each coordinate. [Coset compression](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets)
In particular any closed right-\(H\)-invariant subspace supported on \(F\) and contained in \(\operatorname{ran}\pi\) has \(H\)-dimension at most this trace, by domination of its projection by \(C_F\pi C_F\).

The closed image of \(LJ_F\) is supported on \(SF\) and lies in the global closed image of \(L\).
The trace bound with \(SF\) yields \(\operatorname{rk}_H L_F\leq |SF|\operatorname{rk}_G L\).
Block elimination over \(U_G\) by the invertible triangular matrices with off-diagonal entries \(-BQ^{-1}\) on the left and \(-Q^{-1}C\) on the right gives the diagonal blocks \(P,Q\).
Thus \(\nu_G L=\nu_G P\) and \(\operatorname{rk}_G L=n+k-\nu_G P\).
Subtracting \(\operatorname{rk}_H L_F\) from \((n+k)|F|\) proves the first inequality in (1).

This finite-window estimate can be sharp even for scalar \(P\).
Take \(G=\langle t\rangle\cong\mathbb Z\), \(H=\{e\}\), \(P=0\), and \(L=\left(\begin{smallmatrix}0&0\\ t&1\end{smallmatrix}\right)\).
For \(F=\{1,t,\ldots,t^{N-1}\}\), \(S=\{1,t\}\), the relation \(y=-tx\) with both coordinates supported on \(F\) leaves \(N-1\) free coordinates.
Since \(\operatorname{rk}_G L=\nu_G P=1\) and \(|SF\setminus F|=1\), the first inequality is an equality for every \(N\geq1\).

## Lifting kernel columns

Every matrix algebra over \(D_H\) is regular and its inherited involution is positive definite.
Consequently the orthogonal kernel projection \(E_F\) of \(L_F\) has entries in \(D_H\cap M_H\). [Matrix regularity and kernel projections](../ledger/Yin_L_A0073_v1.md#ascent-and-descent-of-kernel-projections)
One can apply the square-matrix statement to \(L_F^*L_F\).
The inclusion \(U_H\subset U_G\) sends \(D_H\) into \(D_G\) by preservation of the group-algebra generators and their scalar rational operations.

Index one column of \(E_F\) by \(a\), and, for \(1\leq i\leq n+k\), put
\[
 v_{ia}=\sum_{c\in F}\lambda_G(g_c)(E_F)_{(i,c),a}\in D_G\cap M_G .
\]
Under the coset isometry, \(v_{ia}\delta_e\) is the \(i\)-th coordinate of this column applied to the trace vector in its input copy of \(\ell^2(H)\).
Thus \(Lv_a\delta_e=0\).
All entries of \(Lv_a\) are bounded left multipliers, so separation by the trace vector gives \(Lv_a=0\) in \(M_G\).
Write \(v_a=\binom{y_a}{w_a}\) with \(n\) upper coordinates.
Then \(w_a=-Q^{-1}Cy_a\) and \(Py_a=0\) by identities in the affiliated ring.

The map that keeps the upper \(n\) coordinates is an injective bounded right-\(H\)-module map on \(J_F\ker L_F\).
Indeed a kernel vector \(\binom{0}{w}\) satisfies \(Qw=0\), and the bounded matrix \(Q\) is injective on \(\ell^2(G)^k\).
The closed image of this coordinate map has \(H\)-dimension \(\dim_H\ker L_F\) by polar decomposition and is supported on \(F\).
It is spanned after closure by all right \(H\)-translates of the vectors \(y_a\delta_e\), since applying \(E_F\) to the coset-coordinate basis vectors and their right \(H\)-translates spans its image.

Let \(Y_F\) be the matrix with columns \(y_a\) and let \(b_F=Y_FY_F^*\).
These bounded matrices have entries in \(D_G\) and \(Pb_F=0\).
Their common closed image in \(\ell^2(G)^n\) is the closed span of the right \(G\)-translates of the vectors \(y_a\delta_e\).
It contains the preceding closed right-\(H\)-module on \(F\), so the coset compression bound gives \(\dim_H\ker L_F\leq |F|\operatorname{rk}_G b_F\).
This use of the full right-\(G\)-invariant image allows \(H\) to be nonnormal.
Finally \(Pb_F=0\) in \(U_G\) implies \(p_{\ker P}b_F=b_F\) by the affiliated support identity, proving the last inequality in (1). [Affiliated support and Hilbert kernels](Yin_C_A0001_v2.md#actual-realizations-and-affiliated-domains)

## Attaining the kernel dimension

Coamenability supplies \(F\) with \(|SF\setminus F|/|F|\) arbitrarily small.
Inequality (1) gives (2), including a nonzero \(b_F\) as soon as \(\nu_G(x)>0\).
Finiteness of the trace and division closure give \(\nu_G(x)>0\) for each nonunit \(x\in D_G\).
When \(H=\{e\}\), coamenability is amenability of \(G\), and the entries of \(E_F\) are complex numbers.
In this case the \(b_F\) themselves belong to the group algebra, recovering finite-support annihilators. [Amenable kernel localization](Yin_C_A0001_v2.md#rational-kernel-localization)

Suppose \(xb=0\), \(b\in D_G\cap M_G\), \(b\geq0\), and \(\operatorname{rk}_G b=\nu_G(x)\).
The range support of \(b\) is dominated by \(p=p_{\ker x}\) and agrees with it by faithfulness of the trace.
The positive affiliated operator \(x^*x+b\) has zero kernel because these summands have complementary supports.
It is a unit and scalar division closure gives
\[
                         p=b(x^*x+b)^{-1}\in D_G .
\]
Conversely \(p\in D_G\) itself attains (2).
The nonunit detection just proved verifies the first hypothesis of the scalar annihilator criterion. [Scalar annihilators and regularity](Yin_C_A0133_v1.md#statement)
That criterion and the characterization by kernel projections give the stated equivalences with finite generation and right coherence. [The unrestricted finite-rank equation](Yin_C_A0131_v1.md#which-rationality-is-detected)

## Scalar detection and rectangular matrices

Let \(D\) be any division-closed unital \(*\)-subring of a finite tracial affiliated algebra \(U\).
Suppose every scalar nonunit in \(D\) has a nonzero right annihilator in \(D\).
Given a rectangular matrix \(T=[c_1,\ldots,c_n]\) over \(D\) with positive kernel dimension, choose the first \(j\) for which the prefix \([c_1,\ldots,c_j]\) has nonzero kernel.
Hilbert kernels may equivalently be tested on affiliated columns, since the affiliated kernel is the image of its Hilbert kernel projection.
Write \(V=[c_1,\ldots,c_{j-1}]\).
When \(j>1\), its Gram matrix \(V^*V\) and each leading principal block are affiliated units, because the corresponding columns are injective and the involution on affiliated matrices is proper.
Successive Schur complements therefore give \((V^*V)^{-1}\) over \(D\), also for unbounded entries of \(V\). [Gram elimination](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Put \(E=I-V(V^*V)^{-1}V^*\), the orthogonal projection onto the complement of the closed range of \(V\).
For \(j=1\) take \(V\) empty and \(E=I\), omitting all preceding-coordinate terms below.

An affiliated relation \(Vu+c_jw=0\) with \((u,w)\ne0\) has \(w\ne0\) by injectivity of \(V\).
Hence \(Ec_jw=0\), and \(c_j^*Ec_j\in D\) is a scalar nonunit.
Choose \(0\ne d\in D\) with \(c_j^*Ec_jd=0\).
Properness gives \(Ec_jd=0\), so the column with first \(j-1\) entries \(-(V^*V)^{-1}V^*c_jd\), followed by \(d\) and then zeros, is a nonzero rational kernel column of \(T\).
For any such column \(z\), the normalized column \(z(1+z^*z)^{-1}\) still has entries in \(D\), is bounded by polar decomposition, and has the same closed range since the right factor is an affiliated unit.
Thus the scalar hypothesis implies nonzero kernel detection at every matrix size, and taking one-by-one matrices gives the converse.

Apply this result over \(H\) to the group-ring matrices \(L_F\).
If \(\nu_G(P)>0\), the window trace estimate in the first inequality of (1) supplies \(F\) with \(\dim_H\ker L_F>0\), since its proof uses only coamenability and finite propagation.
Take a nonzero bounded kernel column \(z\) of \(L_F\) over \(D_H\).
The coset sum \(v_i=\sum_{c\in F}\lambda_G(g_c)z_{(i,c)}\) gives a bounded \(D_G\)-column with \(Lv=0\), by the trace-vector computation used for columns of \(E_F\).
It is nonzero because the nonzero vector \(z\delta_e\) embeds isometrically by \(J_F\).
Its upper column \(y\) is nonzero by injectivity of \(Q\), and elimination gives \(Py=0\).
For a scalar nonunit \(P=x\), this gives a nonzero bounded positive annihilator \(yy^*\).
The [scalar annihilator criterion](Yin_C_A0133_v1.md#statement) now gives the equivalences in conclusion 1.

## Ascent of density of rational kernel columns

Assume the matrix kernel density hypothesis of conclusion 2 for \(\mathbb CH\), and let \(W\) be the closed span of all ranges of bounded \(D_G\)-kernel columns of the prescribed rational matrix \(P\).
It is a closed right-\(G\)-invariant subspace of \(\ker P\).
For each finite \(F\), the Hilbert kernel of \(L_F\) is spanned after closure by the ranges of bounded \(D_H\)-kernel columns \(z\).
For each such column, form the lifted upper column \(y\) as above.
The upper coordinates of \(J_Fz\delta_h\) equal \(y\delta_h\) for \(h\in H\) by right translation of the identity at \(\delta_e\).
Consequently \(W\) contains the closed image of \(J_F\ker L_F\) under projection to the upper coordinates.
This image is supported on \(F\) and has \(H\)-dimension \(\dim_H\ker L_F\), since the upper coordinate map is injective there.
Compression of the projection onto \(W\) therefore gives
\[
 \nu_G(P)-\operatorname{rk}_G(L)\frac{|SF\setminus F|}{|F|}
 \ \leq\ \frac{\dim_H\ker L_F}{|F|}\ \leq\ \dim_G W .
\]
Passing along a Følner net yields \(\dim_G W=\nu_G(P)\), and faithfulness of the trace gives \(W=\ker P\).
For scalar \(P=x\), the range projections of the positive operators \(\sum_{y\in C}yy^*\), with \(C\) a finite set of bounded rational kernel columns, increase to \(p_{\ker x}\).
Normality of the trace gives (2).

## Assessment history

### Decision coamenable-annihilators

| Field | Value |
| --- | --- |
| date | 2026-11-25T09:22 |
| status | proved |
| reason | Finite coset matrices lift exact rational kernel columns and bound their rank loss by the relative boundary; scalar nonunit detection and matrix kernel density also pass separately through the inclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-window estimates, attainment, and qualitative transfer for a coamenable subgroup. |
| argument | [Argument](#argument) | Realization, coset compression, lifting, scalar reconstruction, and transfer of detection and density. |
| dependency | [Coset compression](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) | Trace estimates for closed subspaces supported on finitely many cosets. |
| dependency | [Scalar realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Group-ring Schur presentations of matrices over the division closure. |
| dependency | [Right annihilator criterion](Yin_C_A0133_v1.md#statement) | Deletion under detection of nonunits and finite generation. |
| review | [Independent proof review](../audits/reviews/Yin_R_A0166_v1.md#coamenable-subgroups) | Whole proof, sharpness example, weaker hypotheses and all affiliated domains. |

## Current assessment

[Selected decision](#decision-coamenable-annihilators)

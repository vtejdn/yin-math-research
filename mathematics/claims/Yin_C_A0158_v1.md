---
author: Yin
---

# Subgroup coefficients of rational kernel projections in amenable coset actions

## Statement

Write \(M_J=\mathcal N(J)\), \(U_J=L^0(M_J)\), and let \(D_J\) and \(R_J\) be the division closure and the \(*\)-regular closure of \(\mathbb CJ\) in \(U_J\).
Let \(G\) be a finitely generated group and \(H\le G\).
Suppose some coamenable subgroup \(K\le G\) has only finite orbits on \(G/H\).
Thus \(G/K\) has Følner sets and \([K:K\cap g^{-1}Hg]<\infty\) for every \(g\in G\).
This holds for every subgroup \(H\) of an amenable \(G\), using \(K=\{1\}\), and for every coamenable commensurated \(H\), using \(K=H\).
Let \(E_H:M_G\to M_H\) be the trace-preserving conditional expectation, applied entrywise to matrices.

For a rectangular matrix \(X\) over \(R_G\) with \(n\) columns, put \(p=p_{\ker X}\) and \(Q=s(E_H(p))\), the support of its positive expectation.
Then \(Q\) is the increasing supremum and the rank-metric limit of projections in \(M_n(R_H)\) dominated by \(Q\).
If \(R_H\) is semisimple Artinian, then \(Q\in M_n(R_H)\).
In particular, if \(D_H\) is a division ring, the expectation of every nonzero scalar kernel projection of this kind has full support in \(M_H\).

For every \(u\in R_G\cap U_H\) there are projections \(q_j\in R_H\), increasing to \(1\), with \(u q_j\in R_H\).
Consequently
\[
          R_H\ \subseteq\ R_G\cap U_H\ \subseteq\
                  \overline{R_H}^{\,\operatorname{rk}_H}.
\]
If \(R_H\) is semisimple Artinian, then \(R_G\cap U_H=R_H\).
If \(D_H\) is semisimple Artinian, both \(D_G\cap U_H\) and \(R_G\cap U_H\) equal \(D_H\).

Suppose now that \(G\) is torsion-free and amenable, and write \(\Delta\) for its subgroup of elements with finite conjugacy class.
With \(D_\Delta=\operatorname{Frac}(\mathbb C\Delta)\), one has
\[
                       Z(R_G)=Z(D_G)=D_\Delta^{\,G},
\]
where \(G\) acts by conjugation.
Every matrix \(X\) over \(R_G\), and every matrix with entries in its rank-metric closure, satisfies
\[
  \operatorname{rk}_G(eX)=\tau_G(e)\operatorname{rk}_G(X)
        \qquad(e\in Z(M_G)\text{ a projection}).                    \tag{1}
\]
Here ranks use the unnormalized matrix trace.
Thus even the rank-metric closure has only the trivial projections in \(Z(M_G)\).
If a scalar \(x\in D_G\) were to witness failure of the [kernel criterion for complete deletion](Yin_C_A0131_v1.md#which-rationality-is-detected), its projection would lie outside \(M_H\) for every subgroup \(H\) with semisimple Artinian \(D_H\), including every abelian subgroup.
Its kernel would still have the same normalized dimension on every nonzero central cut.
These restrictions leave the rationality of a general noncentral kernel projection open.

## Argument

### Group-ring equations for a regular-closure matrix

Every \(a\in R_G\) can be written \(\epsilon B^{[-1]}\gamma\), where \(B\) is a rectangular group-ring matrix, \(B^{[-1]}\) is its affiliated relative inverse, and \(\epsilon,\gamma\) are constant complex vectors. [Single-vector characterization and realization](Yin_C_A0137_v1.md#single-vector-vanishing-and-equation-1)
The relation \(y=av\) is the image, on coordinates \(y,v\), of a finite homogeneous group-ring system with auxiliary column \(h\).
Indeed, with \(T=BB^*\), impose
\[
                 T^2h=T\gamma v,\qquad y=\epsilon B^*h .
\]
One solution of the first equation is \(h=T^{[-1]}\gamma v\).
All choices differ by an element of \(\ker T^2=\ker T=\ker B^*\), and \(B^*T^{[-1]}=B^{[-1]}\) by polar decomposition.
These identities are on right affiliated module columns and require no boundedness of \(a\).
Applying this construction separately to the entries of \(X\), then adding the equations for each row sum, gives a single group-ring matrix \(L\).
The coordinate projection of \(\ker_{U_G} L\) onto the original \(n\) unknowns is exactly \(\ker_{U_G}X=pU_G^n\).
The same construction gives the graph \(\{(ub,b):b\in U_G\}\) for a given scalar \(u\in R_G\).

### Coefficients on the subgroup

The finite-window kernel columns for \(L\) over \(G/K\) have entries of the form \(\sum_{gK\in F}g a_g\), with \(F\) finite and \(a_g\in R_K\cap M_K\).
Their closed ranges together span the Hilbert kernel of \(L\).
Indeed the window projection belongs to \(M_\ell(R_K)\) by matrix regularity, and the coset lifting and boundary estimate give dimensions tending to the full kernel dimension along Følner sets. [Window projections, their lifted columns and the trace estimate](Yin_C_A0134_v1.md#lifting-kernel-columns)
That construction gives coefficients in \(R_K\) for every \(K\), since only the relative inverse of the finite window matrix is needed to obtain its kernel projection.

Fix a summand \(g a_g\) and set \(J=K\cap g^{-1}Hg\).
The finite index of \(J\) in \(K\) lets us express \(a_g=\sum_\ell c_\ell r_\ell\) with \(r_\ell\in K\) and \(c_\ell\in R_J\cap M_J\).
In detail, the [finite-index coefficient representation](../ledger/Yin_L_A0073_v1.md#the-finite-index-coefficient-matrices) embeds \(U_K\) into a matrix algebra over \(U_J\), sends \(\mathbb CK\) into matrices over \(\mathbb CJ\), and takes relative inverses to relative inverses by preservation of the support projections and inverse identities.
It therefore sends \(R_K\) into matrices over \(R_J\).
Apply its first-column decomposition to \(a_g^*\) and take adjoints to obtain the asserted left coefficients, which are bounded since \(a_g\) is bounded.
Now \(g c_\ell g^{-1}\in R_H\cap M_H\).
Collecting terms in the same right coset of \(H\) writes every lifted column, including any coordinate part \(y\), as
\[
                         y=\sum_{Ht} b_t t,\qquad b_t\in (R_H\cap M_H)^n .
\]
For any projection \(q\in M_n(M_H)\), the equality \(qy=y\) is equivalent to \(q b_t=b_t\) at every coset, by disjoint Fourier supports.

The least projection in \(M_n(M_H)\) dominating \(p\) is \(Q=s(E_H(p))\), by bimodularity and faithfulness of the expectation. [Support of an expected projection](Yin_C_A0150_v1.md#argument)
Such a projection dominates \(p\) exactly when it fixes the original coordinate parts of every lifted column.
Indeed the columns span the Hilbert kernel of \(L\) after closure, so a bounded row annihilating all these columns annihilates its kernel projection and thereby its entire affiliated kernel module.
The projection of this module onto the original coordinates is \(pU_G^n\).
It follows that \(Q\) is the join of the range projections of all the \(b_t\).
For each finite selection the projection onto their closed span lies in \(M_n(R_H)\) by the rectangular relative inverse.
Increasing selections give a sequence with trace tending to \((\operatorname{Tr}_n\otimes\tau_H)(Q)\), by normality of the finite trace.
For projections below \(Q\) the trace difference is their rank distance from \(Q\).
If \(R_H\) is semisimple Artinian, the right submodule of \(R_H^n\) generated by the selected columns over all windows is finitely generated.
A finite selection therefore has the full closed span.
In the scalar case with \(D_H\) a division ring, \(R_H=D_H\) since a regular division-closed \(*\)-subring contains its relative inverses. [Regular closure](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)
Every nonzero coefficient column in size one is then an affiliated unit.

### Exact agreement on subgroup projections

For \(u\in R_G\cap U_H\), use lifted columns for the group-ring system defining its graph.
Write their two visible coordinates \(w,v\) on right \(H\)-cosets with coefficients \(b_t,a_t\), respectively.
Since \(w=uv\), uniqueness of the coefficients gives \(b_t=u a_t\).
For unbounded \(u\) first multiply the equality on the left by a bounded affiliated unit in \(M_H\) clearing \(u\), and compare the resulting bounded coefficients.
The closed ranges of all \(a_t\) span \(\ell^2(H)\).
Indeed a subgroup projection fixing all \(a_t\) would fix all the \(v\), hence the second coordinate throughout the affiliated graph, which ranges over \(U_G\).
Choose increasing finite sets of coefficient pairs for which the range projections \(q_j\) of the rows \(V_j=[a_t]\) tend to \(1\) in rank.
For the corresponding rows \(W_j=[b_t]\) one has
\[
                       q_j=V_j V_j^{[-1]},\qquad
                       u q_j=W_j V_j^{[-1]}\in R_H .
\]
The rank error is at most \(\tau_H(1-q_j)\).
For a semisimple Artinian \(R_H\), finite generation of the right ideal generated by all the \(a_t\) gives a finite row with \(q_j=1\).
The inclusions \(D_H\subseteq D_G\) and \(R_H\subseteq R_G\) follow from the subgroup representation preserving affiliated units and relative inverses.
When \(D_H\) is semisimple Artinian it is already regular, so \(R_H=D_H\).

### Central cuts in a torsion-free amenable group

The subgroup \(\Delta\) is torsion-free abelian, and every central projection of \(M_G\) belongs to \(M_\Delta\). [Finite conjugacy classes and the abelian subgroup](../ledger/Yin_L_A0071_v1.md#central-fourier-coefficients-and-finite-index)
The same inclusion holds for central affiliated operators by their spectral projections, applied to their real and imaginary parts.
Here an element central in \(R_G\) or \(D_G\) commutes with every group unitary and hence is affiliated with the center of \(M_G\).
Nonzero elements of \(\mathbb C\Delta\) are affiliated units by Fourier transformation on their finitely generated free abelian supports.
The subgroup intersection theorem with \(K=\{1\}\) therefore places every such central element in the field \(D_\Delta\).
Conversely the conjugation-fixed elements of this field commute with \(U_G\) and belong to \(D_G\), giving the two center identities.

To prove (1), first take a rectangular group-ring matrix \(L\), with kernel projection \(P\), and a finite set \(F\subset G/\Delta\).
Let \(L_F\) be its window matrix with all outputs induced by inputs in \(F\), and let \(d_F=\dim_\Delta\ker L_F\).
Gaussian elimination over \(D_\Delta\) shows that \(d_F\) is an integer and that after cutting by a central projection \(e\in M_G\) the window kernel dimension is exactly \(\tau_G(e)d_F\).
Indeed \(e\in M_\Delta\) commutes with the coefficient field and its invertible basis changes, and \(e\) acts on every coset coordinate by the same projection since it commutes with \(G\).
The cut window kernel lies inside \(eP\) and is supported on \(F\).
The [coset compression trace identity and boundary estimate](Yin_C_A0134_v1.md#finite-coset-matrices) give
\[
    (\operatorname{Tr}\otimes\tau_G)(eP)\ \ge\
           \tau_G(e)\,\frac{d_F}{|F|},\qquad
    \frac{d_F}{|F|}\ \longrightarrow\ (\operatorname{Tr}\otimes\tau_G)(P)
\]
along a Følner sequence of \(G/\Delta\).
Applying the same lower bound to \(1-e\) forces equality in the limit.
This gives the cut formula for group-ring kernel dimensions as well as ranks.

For a matrix \(X\) over \(R_G\), take the group-ring system \(L\) above and let \(L_0\) be its restriction to the auxiliary unknowns with all original coordinates zero.
Projection onto the original coordinates yields the exact affiliated module sequence from \(\ker L_0\) through \(\ker L\) onto \(\ker X\).
It remains exact on every central cut, so subtraction of the two group-ring kernel dimensions gives the cut formula for \(\ker X\) and hence (1).
The rank triangle inequality extends (1) to rank limits since multiplication by \(e\) cannot increase rank.
For a central projection \(p\) in that closure, taking \(e=p\) and \(X=p\) gives \(\tau_G(p)=\tau_G(p)^2\).
Finally any \(p_{\ker x}\) for \(x\in D_G\) lies in \(R_G\), so its membership in \(M_H\) for a semisimple Artinian \(D_H\) already gives \(p_{\ker x}\in D_H\subseteq D_G\).

## Assessment history

### Decision subgroup-kernel-support

| Field | Value |
| --- | --- |
| date | 2026-11-25T12:56 |
| status | proved |
| reason | Finitely supported solutions on coset windows recover the subgroup support from below, and Fourier decomposition makes the ranks of central cuts proportional. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Subgroup support and intersection theorems, the centers of the two closures, and rank proportionality on central cuts. |
| argument | [Argument](#argument) | Lifting group-ring equations, extracting subgroup coefficients, approximating graph projections, and the central rank formula. |
| dependency | [Kernel realization](Yin_C_A0137_v1.md#single-vector-vanishing-and-equation-1) | A group-ring system for an element of the regular closure. |
| dependency | [Coset kernels](Yin_C_A0134_v1.md#lifting-kernel-columns) | Approximation by finitely supported solutions over a coamenable subgroup. |
| dependency | [Coset matrices](Yin_C_A0134_v1.md#finite-coset-matrices) | Compression and dimension bounds. |
| dependency | [Finite-index coefficients](../ledger/Yin_L_A0073_v1.md#the-finite-index-coefficient-matrices) | Regular-closure coefficients after restriction of scalars. |
| dependency | [Subgroup spectrum](Yin_C_A0150_v1.md#argument) | The support of a conditional expectation. |
| dependency | [Regular closure](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Matrix relative inverses and support projections. |
| dependency | [Finite conjugacy classes](../ledger/Yin_L_A0071_v1.md#central-fourier-coefficients-and-finite-index) | The center is supported on the abelian FC subgroup. |
| dependency | [Scalar kernel criterion](Yin_C_A0131_v1.md#which-rationality-is-detected) | The obstruction to complete deletion. |
| review | [Subgroup supports](../audits/reviews/Yin_R_A0172_v1.md#subgroup-supports) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-subgroup-kernel-support)

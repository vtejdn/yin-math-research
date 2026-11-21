---
author: Yin
---
# Finite cone-contact elimination and sparse-alphabet probability certificates

## Statement

Let \(X\) be the complex obtained by coning finite graphs immersed in a finite rose, and assume that \(X\) is aspherical.
Write \(G=\pi_1(X)\), and let \(\widetilde R\) be the rose preimage in its universal cover, with its marked Cayley edges.
Choose \(k\) distinct lifted cone copies and let \(\Lambda=\bigsqcup_{i=1}^k\Lambda_i\) be the disjoint union of their abstract base graphs.
Their actual edge and vertex maps have image a finite graph \(\Gamma\subseteq\widetilde R\).
Loops, parallel marked edges, and multiple source edges mapping to the same actual edge are allowed.
A repeated occurrence of the same lifted cone is combined into its one cycle-space summand.
All chain spaces below have coefficients in \(\mathbb C\), with one chosen orientation per geometric edge.

For an inverse-closed set \(S\) of marked letters, let \(\Lambda_S\) retain exactly the edges with labels in \(S\), including all vertices of \(\Lambda\).
Let \(f_1:C_1(\Lambda)\to C_1(\Gamma)\) be the actual signed edge map.
Write
\[
 D_{\mathrm{out}}=\ker\bigl(C_1(\Lambda_{\mathrm{out}})
                \longrightarrow C_1(\Gamma_{\mathrm{out}})\bigr),
 \qquad
 Q_S=C_0(\Lambda)/\partial C_1(\Lambda_S),
 \qquad
 T_S=\pi_S\partial|_{D_{\mathrm{out}}},
\]
where \(\Lambda_{\mathrm{out}}\) and \(\Gamma_{\mathrm{out}}\) retain the complementary edges and \(\pi_S\) is the quotient map.
The basis of \(Q_S\) can be taken to be the connected components of \(\Lambda_S\).
Define the full sparse output space
\[
 W_S=f_1 Z_1(\Lambda)\cap C_1(\Gamma_S).
\]
The following assertions hold.

1. There is an exact sequence
   \[
   0\longrightarrow Z_1(\Lambda_S)
   \longrightarrow \ker(f_{\mathrm{out}}|_{Z_1(\Lambda)})
   \longrightarrow \ker T_S\longrightarrow0,
   \]
   and consequently
   \[
                \dim_{\mathbb C}W_S=b_1(\Lambda_S)+\dim_{\mathbb C}\ker T_S.       \tag{1}
   \]
   The matrices in this formula concern the whole cycle spaces of the selected cone bases.
   They use finite ordinary linear algebra after the actual edge identifications are supplied.
2. A row of \(T_S\) with exactly one nonzero entry forces the corresponding variable to vanish in every kernel vector.
   Iterating this deletion and ordinary pivots gives a finite exclusion certificate.
   In particular, if \(\Lambda_S\) is a forest and this elimination removes every contact variable, then \(W_S=0\).
3. Suppose an actual four-line tuple also satisfies the linear cone-filling conclusion of [L_A0054](../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws), with girth at least \(L\ge3\) and supplied constant \(c_*>0\).
   Every null word of length at most
   \[
       H=2\left\lceil\frac{\log n}{\log(65/64)}\right\rceil+4
   \]
   has a cone filling with at most
   \[
                              K_n=\left\lfloor\frac{H}{c_*L}\right\rfloor          \tag{2}
   \]
   nonempty cone-boundary occurrences.
   For \(L=\lfloor c\log n\rfloor\) and fixed \(c,c_*>0\), these numbers are bounded independently of large \(n\).
   Thus a finite family of configurations of at most \(K_n\) distinct lifted cones can cover the chains of all the short relations used in [C_A0091](Yin_C_A0091_v1.md#statement).
4. Fix such a covering family on one tuple, independently of the subsequent alphabet draw.
   Let \(\mathcal A\) be the inclusion-minimal nonempty sets of neutral inverse-pair types supporting a nonzero sparse output from some covering configuration.
   Retain only those sets of size at most \(s=62\).
   They form a finite antichain in the set of \(D=8252\) neutral inverse-pair types.
   Then
   \[
   \Pr_S\{\operatorname{rk}_{K_S}R_{S,H}\ge1/128\}
     \le \Pr_S\{\exists A\in\mathcal A:A\subseteq S\}
     \le\sum_{A\in\mathcal A}
        \frac{\binom{D-|A|}{s-|A|}}{\binom Ds}.                         \tag{3}
   \]
   A final sum at most \(1/4000\) excludes full color erasure by C_A0091.

Formula (1) supplies no identification between finite complex dimension and regular module dimension.
The passage in (3) uses the zero-output event, which forces the entire short-relation matrix to be zero.
The estimates do not assert that the required antichain bound holds for every safeguarded four-line tuple.

<a id="argument"></a>
## Full cone-cycle spaces and the exact sequence

The long exact sequence of the pair \((\widetilde X,\widetilde R)\) gives an injection
\[
 \bigoplus_{\text{lifted cones }\mathcal C}H_1(\Lambda_{\mathcal C};\mathbb C)
       \longrightarrow H_1(\widetilde R;\mathbb C).
\]
Indeed \(\widetilde X\) is contractible, so \(H_2(\widetilde X;\mathbb C)=0\), while each cone relative to its base contributes the first homology of that base in relative degree two.
This is the coefficient-independent relative-cone argument used in [C_A0055](Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials).
Graphs have no degree-two chains, so their first homology is their cycle space.
Restriction to the selected distinct lifted cones therefore makes \(f_1\) injective on \(Z_1(\Lambda)\).
Actual folds in their graph maps are still permitted.

For a cycle \(z=z_S+z_{\mathrm{out}}\), its image has support in \(S\) exactly when \(z_{\mathrm{out}}\in D_{\mathrm{out}}\).
Since \(\partial z=0\),
\[
 \partial z_{\mathrm{out}}=-\partial z_S
       \in\partial C_1(\Lambda_S),
\]
so \(T_S z_{\mathrm{out}}=0\).
Conversely, if \(h\in D_{\mathrm{out}}\) and \(T_Sh=0\), choose \(z_S\in C_1(\Lambda_S)\) with \(\partial z_S=-\partial h\).
Then \(z_S+h\) is a cycle with zero outside image.
The freedom in choosing \(z_S\) is exactly \(Z_1(\Lambda_S)\).
Projection to \(z_{\mathrm{out}}\) proves the exact sequence, and the injectivity above identifies its middle space with \(W_S\).
This proves (1).

The construction is explicit.
For an actual outside edge \(e\), orient its source preimages \(e_0,\ldots,e_{r_e-1}\) consistently with \(e\).
The differences \(e_j-e_0\), \(1\le j<r_e\), form the corresponding basis of \(D_{\mathrm{out}}\).
If fixed source orientations are retained instead, insert their signs in these differences.
After contracting each component of \(\Lambda_S\), apply \(\partial\) to these vectors to obtain the columns of \(T_S\).
An edge difference can have four component incidences, some of which cancel.
Self-folds and contacts involving three source occurrences are included by the same construction.
An incidence graph recording only which cones touch discards these component and sign data.

A unique nonzero entry in a row gives a scalar equation \(a h_j=0\) with \(a\ne0\), forcing \(h_j=0\).
Removing that variable preserves the remaining kernel equations.
Repeated deletion proves assertion 2, including when coefficients obtained from folds have magnitude greater than one.
A leaf in the coarse graph of cones by itself supplies no such unique-row condition.

## Two and three chosen cycle columns

The following specializations concern a selected single cycle column from each of two or three cones.
They are finite tests for that chosen span.
To certify the full cone-cycle space one must instead apply (1), or use a complete basis of each \(Z_1(\Lambda_i)\).

Let \(z_1,\ldots,z_k\) be the chosen nonzero integer oriented cycle columns, with \(k=2\) or \(3\), and let \(O\) be their outside-edge matrix.
Their full image columns are independent by asphericity when they belong to distinct lifted cones.
Thus their sparse output dimension is \(k-\operatorname{rank}_{\mathbb C}O\).
Assume initially that every nonzero row of \(O\) meets at most two columns and every nonzero entry is \(+1\) or \(-1\).
These are extra conditions on the actual collected columns.
Arbitrary immersed walks or folds need not satisfy them.

A singleton row anchors its column variable to zero.
For a row meeting \(i,j\), write its equation as
\[
      a_{ei}\lambda_i+a_{ej}\lambda_j=0,\qquad
      \lambda_j=\eta_{ij}\lambda_i,\qquad
      \eta_{ij}=-a_{ei}/a_{ej}\in\{1,-1\}.
\]
Form a graph on the column variables with one edge for each such row.
In a connected component, a spanning tree expresses all variables as signs times one parameter.
An anchor forces that parameter to zero.
An extra edge preserves the parameter exactly when the product of the gains around its fundamental cycle is \(1\).
Consequently each unanchored component with every cycle gain \(1\) contributes one kernel dimension, and every other component contributes zero.
An isolated column with no outside coefficient is an unanchored component.
Parallel contact edges must also have consistent gains.

For two columns, one opposite-sign contact row \((1,-1)\) leaves the parameter \((1,1)\).
The two rows
\[
                 \begin{pmatrix}1&1\\1&-1\end{pmatrix}
\]
have determinant \(-2\), so they leave no complex sparse output.
Their reduction modulo two does have a kernel.
This is an explicit finite obstruction to transferring a binary contact cancellation to complex coefficients.

For three columns, a contact tree with no anchors still leaves one parameter.
For a triangle the parameter survives exactly when
\[
                         \eta_{12}\eta_{23}\eta_{31}=1.
\]
For example,
\[
 O_-=\begin{pmatrix}1&-1&0\\0&1&-1\\-1&0&1\end{pmatrix},
 \qquad
 O_+=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}
\]
have ranks two and three over \(\mathbb C\), respectively.
The first has kernel spanned by \((1,1,1)\), while \(\det O_+=2\).
Both sign patterns have a kernel modulo two.
When a contact row meets all three columns, retain its full equation \(a\lambda_1+b\lambda_2+c\lambda_3=0\).
One may first solve the pair-contact and anchor equations and then impose the remaining triple rows on the surviving parameters.
This is again exact finite linear algebra.
No assertion is made that either displayed toy contact matrix occurs in a safeguarded four-line tuple.
They specify the sign information that its actual finite calculation must preserve.

## The number of cones required at the C_A0091 scale

Use a reduced cone picture for a cyclically reduced null word \(w\), as in L_A0054.
Its total inner boundary length is at most \(|w|/c_*\).
Every nonempty cyclically immersed inner boundary in a graph of girth at least \(L\) has length at least \(L\).
Therefore the number of such occurrences is at most \(|w|/(c_*L)\), proving (2).
If several boundaries belong to the same lifted cone, add their cycle chains in that one summand.
This reduces the number of distinct lifted cones.
The connecting paths cancel in the boundary chain of the picture, so the chain of \(w\) is in the image of the sum of these cone-cycle spaces.

For fixed positive \(c,c_*\),
\[
 \frac{H}{c_*L}\longrightarrow
       \frac{2}{c_*c\log(65/64)}
       \qquad(n\longrightarrow\infty).
\]
This constant may be very large.
The two-cone and three-cone tests cover only the corresponding initial part of this finite range.

For a fixed tuple, there are finitely many words of length at most \(H\) in the finite marking.
Choose one bounded-perimeter filling for each null word.
The finite union of the lifted cone configurations appearing in these fillings gives a covering list independent of \(S\).
The existence of this list follows from the supplied filling theorem.
Constructing it from data requires the actual tuple, the filling constant and verified group-word comparisons.
L_A0054 gives a finite word-decision search when these data are available.
This assertion supplies no practical enumeration complexity bound.

It is essential to include the whole-cycle contribution \(b_1(\Lambda_S)\) in (1).
An intrinsic \(S\)-cycle in one selected cone already contributes, without using any outside contacts.
The strengthened probabilistic event in [C_A0059](Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction) excludes all sparse relations simultaneously with high probability.
Its extra alphabet-restricted pattern estimate is not a deterministic consequence asserted here for every tuple satisfying the original geometric safeguards.

## Exact alphabet probabilities and a usable conditional threshold

Fix the covering list.
For one configuration let \(V=f_1Z_1(\Lambda)\).
For a nonzero vector \(v\in V\) with only neutral labels, let \(\ell(v)\) be the set of neutral inverse-pair types of the actual edges with nonzero coefficients.
Take all inclusion-minimal such sets across the list, dropping repetitions and sets larger than \(s\).
They form \(\mathcal A\).
Finiteness follows because the neutral alphabet is finite.
For each \(S\),
\[
 \{\text{some covering configuration has }W_S\ne0\}
       \quad\Longleftrightarrow\quad
 \{\text{some }A\in\mathcal A\text{ satisfies }A\subseteq S\}.
\]
These sets can in principle be determined by ordinary rank computations for the relevant row restrictions.
If all covering outputs vanish, every short-relation chain vanishes.
Thus \(R_{S,H}=0\), proving the first inequality in (3).
The second is the union bound, using
\[
          \Pr(A\subseteq S)=
             \frac{\binom{D-|A|}{s-|A|}}{\binom Ds}
             =\frac{(s)_{|A|}}{(D)_{|A|}}.
\]
If desired, the exact union probability is given by inclusion-exclusion, replacing \(|A|\) with the cardinality of each union of antichain members.
This condition concerns a common set of good alphabets on which all covering configurations vanish simultaneously.

For the actual numerical values,
\[
 p_2=\frac{1891}{34043626}
     \approx 5.55463745254398\cdot10^{-5},\qquad
 p_3=\frac{1891}{4680998575}
     \approx 4.0397363291228945\cdot10^{-7}.
\]
If a certified covering antichain consists of \(m_2\) two-element sets and \(m_3\) three-element sets, the explicit sufficient inequality is
\[
                    m_2p_2+m_3p_3\le1/4000.                         \tag{4}
\]
For example (4) holds for at most four two-element sets alone, at most 618 three-element sets alone, or at most four two-element sets together with 68 three-element sets.
These integer thresholds follow by exact rational division.
Larger support sets can be retained with their corresponding summands in (3).
The statement assumes that the list covers all relevant output supports, including any one-element support if a neutral generator is trivial.
If each neutral generator is nontrivial in the torsion-free group, one-element supports are impossible because its marked cyclic Cayley graph has no nonzero finite cycle.

These are conditional bounds on a fixed tuple.
The exact four-line type counts, asphericity and linear filling estimate have not here supplied a small enough antichain or a full-rank certificate for all its configurations.
The number of source vertices, the number of words, and the number of cone contacts alone do not replace the signed row restriction.
The new finite output criterion and bounded-\(K_n\) coverage identify the remaining calculation precisely.
They give no new unconditional exclusion of erasure and no completed result for A0001.

## Assessment history

### Decision reviewed-contact-criterion

| Field | Value |
| --- | --- |
| date | 2026-11-21T02:59 |
| status | proved |
| reason | Independent whole-proof inspection supports the full-cone exact sequence, signed elimination tests, conditional bounded-cone coverage and fixed-tuple probability certificate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete finite contact theorem and conditional probability criterion, with the supplied geometric hypotheses. |
| argument | [Argument](#argument) | Full cycle-space proof, signed two- and three-column calculations, bounded filling coverage, common antichain event and exact thresholds. |
| review | [Whole-artifact finding](../audits/reviews/Yin_R_A0128_v1.md#whole-artifact-finding) | Independent complete proof and exact source-interface inspection; no claim of a small antichain for actual tuples. |
| dependency | [Linear cone fillings](../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws) | Perimeter bound and cyclically immersed inner boundaries, assumed for the fixed tuple in parts 3 and 4. |
| dependency | [Erasure forces short-relation rank](Yin_C_A0091_v1.md#statement) | Strict lower probability greater than 1/4000 at regular-rank threshold 1/128, on the same fixed tuple and sampled alphabet. |

## Current assessment

[Selected decision](#decision-reviewed-contact-criterion)

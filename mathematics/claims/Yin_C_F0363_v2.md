---
author: Yin
---

# A conditional Schur restoration bound for every fixed number of directions

<a id="statement"></a>
## A matrix in the span of the corner coefficients

Fix a positive integer \(m\) and a fixed finite number of spectral nodes.
At each node \(z\) let \(H_z(g)=(g^{\mathsf T}K_{ij,z}g)_{i,j\le m}\) for transpose-symmetric physical kernels fixed before the independent fresh raw real column \(g\) is exposed.
The scalar Schur statistic is \(c_z\det H_z(g)+b_z(g)\), where \(c_z\ne0\) and \(b_z\) is a polynomial of degree less than \(2m\), also fixed before the draw.
Use \(2m\) disjoint physical panels of asymptotically positive densities.
The real row law and the kernel transfers are required to obey the two-panel output-spread and Fourier hypotheses spelled out below.

Specifically, modulo scalar identity matrices and errors of total rank \(o(n)\), write the kernel array at each node as
\[
       (K_{ij,z})_{ij}=\sum_{\ell=1}^{r_z}M_{\ell,z}\,K_{\ell,z}^{\,0}
\]
where \(M_{\ell,z}\) are scalar \(m\)-by-\(m\) coefficient matrices, all family sizes are fixed, and the \(K_{\ell,z}^{\,0}\) are physical kernels.
On every ordered pair of different panels assume the following bound for these basis kernels, jointly over the nodes.
For an independent difference vector on the first panel, project the output vectors on the second panel off all ranges of the transposed corner rank errors, and off any additional fixed-dimensional real subspace determined before this first draw.
Complex ranges are removed by their real and imaginary parts.
Uniformly in all real unit arrays of coefficients of the real and imaginary basis kernels, the resulting output combination has norm at least \(c\sqrt n\) after also removing any prescribed or adaptively chosen set of at most \(\rho n\) output coordinates, with a simultaneous exception \(Ce^{-cn}\).
Here the projections remove the span of the indicated spaces and the deleted coordinate axes together.
At a real node with real basis kernels use the real coefficient family alone; in this case all coefficient matrices and directions below are taken real.
The raw-coordinate difference law in the second panel satisfies the [disjoint-basis Fourier bound](Yin_C_F0351_v6.md#border-tests).
These are conditional hypotheses on the history and the original law, with constants uniform on the set of node tuples being tested.

At each node suppose there are scalars \(\beta_{\ell,z}\) of bounded Euclidean norm for which
\[
       B_z=\sum_\ell\beta_{\ell,z}M_{\ell,z},
       \qquad |\det B_z|\ge c_0>0.                                      \tag{1}
\]
For any prescribed \(s\) nodes satisfying these assumptions and any fixed \(C_0<\infty\), the simultaneous small-ratio probability is at most
\[
 \Pr_g\{\,|c_z\det H_z(g)+b_z(g)|\le C_0|c_z|
                 \text{ at all }s\text{ nodes}\,\}
       \le C n^{-s/2^{\,2m+1}}+Ce^{-c n}.                              \tag{2}
\]
The constants can depend on the fixed family, number of nodes, panel densities and \(C_0\).
For the [three-direction cubic kernels](Yin_C_F0363_v1.md#corners) the entries form the full basis and one may take \(B_z=I_3\).
Condition (1) also applies to smaller coefficient spans, for example a single physical kernel multiplied by a fixed invertible matrix.

<a id="argument"></a>
## Polarized determinants with progressively fewer fixed arguments

For independent difference vectors \(u_a\) on the panels put \(H_{ab,z}=(u_a^{\mathsf T}(K_{ij,z})_{ab}u_b)_{ij}\).
Let \(\mathcal D_m(H_1,\ldots,H_m)\) be the coefficient of \(t_1\cdots t_m\) in \(\det(\sum t_jH_j)\).
For \(0\le q\le m\) define
\[
  U_{q,z}=\sum_{\pi}\mathcal D_m\big((H_{ab,z})_{\{a,b\}\in\pi},
                                \underbrace{B_z,\ldots,B_z}_{m-q}\big),
\]
where the sum ranges over unordered pair partitions of the first \(2q\) labels.
In particular \(U_{0,z}=m!\det B_z\).
After the first \(2q-2\) draws, the sum of terms that pair the last two labels is a linear functional \(\ell_z\) of \(H_{2q-1,2q,z}\).
Multilinearity gives exactly \(\ell_z(B_z)=U_{q-1,z}\).
In every other pairing the last vector pairs with one of the first \(2q-2\) vectors, so its coefficient lies in a fixed-dimensional space spanned by their images under the transposed corners into the last panel.
The space is determined before the penultimate draw; its multipliers may depend on that draw.

If \(|U_{q-1,z}|\) exceeds a fixed positive threshold, (1) and Cauchy--Schwarz show that the basis coefficient vector \((\ell_z(M_{\ell,z}))_\ell\) has norm bounded below.
For \(q=1\) use the deterministic lower bound on \(|U_{0,z}|\).
On the remaining nodes test real parts of the complex linear forms.
The real coefficient pair of each complex scalar is its real part and minus its imaginary part.
The separate coordinates of different nodes mean that every real unit combination of these tests has combined basis coefficient norm bounded below, even for unbounded individual functionals.
Identity kernel contributions vanish across distinct panels.
Projecting away the rank errors and the already known finite-dimensional space, and scaling the combined coefficients to unit norm, gives the lower bound \(c'\sqrt n\) after any allowed coordinate deletion.
The full unprojected outputs retain that lower bound on the complement of the deleted coordinates because projection only decreased norms and killed the extra summands.
The [maximum-volume extraction and Fourier argument](Yin_C_F0351_v6.md#border-tests) therefore give \(O(n^{-d/2})+O(e^{-cn})\) for a fixed-radius box on \(d\) such nodes, after the independent last draw, including the penultimate-draw exception.

Inductively, for any assigned subset of \(s\) nodes, classify the first \(2q-2\) draws by the subset on which \(|U_{q-1,z}|\le1\).
A subset of size \(s-d\) has probability at most \(O(n^{-(s-d)/2})+O(e^{-cn})\) by the preceding stage, with the empty-subset bound one.
Condition on the first \(2q-2\) vectors, charge the \(d\) other nodes by the two-panel estimate, and sum over the finitely many subsets.
At the first stage use the deterministic pivots on every node.
This proves the \(O(n^{-s/2})+O(e^{-cn})\) bound for small \(|U_{q,z}|\), allowing any fixed target radius at the final stage.
After \(2m\) Cartesian Cauchy--Schwarz steps, a successful resampling cube yields a small alternating difference.
Only the top-degree term survives, with alternating difference exactly \(2^m c_z U_{m,z}\), since both orders of each pair give the same entry of its symmetric physical kernel.
Taking the \(2^{2m}\)-th root gives (2).

<a id="scope"></a>
## Application to cyclic pencils

For fixed \(m\), \(O(\log^a N)\) transitions and at least \(2^{2m+2}\) separated nodes, the [chronological assignment and area argument](Yin_C_F0363_v1.md#polarization) makes the joint-error term summable, provided the kernel and normal guards themselves have the stated uniform, summable costs.
Verifying those hypotheses for the actual compressed inverse, finding an initial determinant comparable to the retained singular product, and locating the first regular transition are separate tasks.
A padded path in a [general cyclic linearization](Yin_C_F0359_v1.md#construction) can have a deterministic column with no variable coefficient.
In the seven-channel example the second-layer coordinate for the constant monomial has this property, so simply applying a full-channel random-border test before eliminating the deterministic directions would leave a zero variable direction.
The scalar-polynomial [local cutoff criterion](Yin_C_F0359_v2.md#statement) remains the unconditional equivalence; (2) gives a restoration mechanism when the required physical data can be exhibited.

## Current assessment
[Selected decision](#decision-fixed-directions-candidate)

## Assessment history

### Decision fixed-directions-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:34 |
| status | open |
| reason | An invertible matrix in the coefficient span gives successive nonzero polarizations under projected two-panel spread. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed-dimensional restoration test](#statement) | Explicit corner-spread, coefficient-span and fresh-law hypotheses. |
| argument | [Polarized determinant recursion](#argument) | All mixed pairings and conditional costs through the final difference. |
| support | [Application to pencil charts](#scope) | Sufficient transition estimates and remaining geometry. |

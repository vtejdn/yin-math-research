---
author: Yin
---

# Commutator bounds for marginal projections and the scale of free noise between spectral blocks

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be a bounded normal operator with diffuse marginal in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Let a unital represented starred coefficient algebra \(N_0\) and \(Z\) generate \(M\), and let \(\delta\) on their joint starred polynomial algebra be an outer derivation with \(\delta Z=1\otimes1\), \(\delta N_0=0\), and actual vacuum \(\xi=\delta^*(1\otimes1)\).
Put \(N=W^*(N_0)\), \(\eta=[Z^*,\xi]\).
For any mutually orthogonal spectral projections \(e_j\in W^*(Z)\) of traces \(0<t_j<1\), take arbitrary selfadjoint \(H_j\in N\) with \(\|H_j\|\le K\), and put \(v_j=\tau((H_j-\tau(H_j)1)^2)\).
Then
\[
     \sum_j\frac{t_j^2(1-t_j)^2v_j^2}{\|[H_j,e_j]\|_2^2}
                  \ \le\ 4 K^2(1+\|\eta\|_2)^2 .                        \tag{1}
\]
Here terms with \(v_j=0\) are taken as zero.
Every denominator with \(v_j>0\) is nonzero.
For fixed \(K\) and \(v_j\) bounded away from zero, \(\|[H_j,e_j]\|_2/t_j\to\infty\) whenever \(t_j\to0\), even without orthogonality.
Only the derivative at \(Z\) is assumed.

Consider a normal coordinate \(Z\) in a tracial base algebra \(M_0\) with a countable spectral partition \(1=\sum_j e_j\), \(0<t_j=\tau(e_j)<1\), and a bounded selfadjoint \(H_0\in M_0\) commuting with every \(e_j\).
Set \(D=\sum_j d_j e_j\) for bounded positive numbers \(d_j>0\).
For a bounded centered selfadjoint \(V\) of positive variance free from the base, put \(Y=H_0+DVD\).
In the generated pair \((Z,Y)\), the actual distinguished derivative at \(Z\) killing \(Y\) requires
\[
                         \sum_j t_j/d_j^2 <\infty .                       \tag{2}
\]
The initial block operators \(e_jH_0e_j\) may fail to commute with \(e_jZ\).
Conversely, when (2) holds and \(V\) has an actual scalar conjugate variable \(g\), the derivative at \(Y\) killing \(Z,Z^*\) exists with vacuum equal to the trace Hilbert projection of \(D^{-1}gD^{-1}\) onto \(L^2(W^*(Z,Y))\).
Its norm is at most \(\|g\|_2\sum_j t_j/d_j^2\).
The perturbation inside block \(j\) has normalized trace Hilbert norm \(d_j^2\sqrt{t_j\,\tau(V^2)}\).

There is a planar normal marginal with \(t_j=3\cdot4^{-j}\), \(j\ge1\), for which the pair \(Z,Y=DVD\), with \(V\) free of uniform law on \([-1,1]\) and \(d_j=j^\alpha 2^{-j}\), has both actual conjugate variables and strong duals exactly for \(\alpha>1/2\).
At and below that threshold the distinguished vacuum at \(Z\) already fails.
This realizes the summability threshold in (2).
For general \(H_0\), condition (2) supplies the stated derivative at the noisy coordinate when \(V\) has an actual scalar conjugate variable.
The derivative at \(Z\) and the full-domain question there depend on the joint law.

## Argument

### Testing a double commutator against partial liberation

Use the coarse correspondence as \(L^2(M\bar\otimes M^{\mathrm{op}})\), with the two outer actions on the left of this tensor algebra and inner marginal multiplication \(I_{z-w}\) on its right.
The [liberation calculation](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) gives \(\gamma=I_{z-w}\delta\), killing the coefficients and taking \(b\) in the marginal core to \(b\otimes1-1\otimes b\), with vacuum \(\eta\).
The argument uses only the distinguished vacuum and the generator and adjoint values, the latter forced at \(Z^*\) by normality and diffuseness.
The [graph on measurable spectral blocks](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) extends this marginal formula to every spectral projection \(e\).
The closed graph is invariant under left and right multiplication by omitted elements and their adjoints, acting by the outer actions on its tensor component.
Indeed the Leibniz rule first gives invariance for \(N_0\), and commutation of the graph projection extends it to \(N\) by normality, as in the [omitted-algebra graph argument](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra).
The same graph argument applies to the closable liberation derivation, whose tensor adjoint is densely defined by its vacuum and polynomial Leibniz rule.

For one \(e,H\) in the statement put \(t=\tau(e)\), \(q=1-e\), \(P=e\otimes1-1\otimes e^{\mathrm{op}}\), and \(A=H\otimes1-1\otimes H^{\mathrm{op}}\).
Then \(\bar\gamma[H,e]=AP\).
The [marginal adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) for \(\gamma\) gives \(\gamma^*P=[e,\eta]+2(e-t1)\), because the row and column of the antisymmetric symbol are \(e-t1\) and \(t1-e\).
The adjoint relation and omitted graph invariance give \(\gamma^*(AP)=[H,\gamma^*P]\), since \(H\) is selfadjoint.
Consequently
\[
 \|AP\|_{2,\tau\otimes\tau}^2
    =\langle [H,[e,\eta]+2(e-t1)],[H,e]\rangle .
                                                                    \tag{3}
\]

For the two positive states \(\tau_p(x)=\tau(px)/\tau(p)\), \(p=e,q\), let \(m_p=\tau_p(H)\), \(s_p^2=\tau_p(H^2)-m_p^2\).
Use traciality and \(P^2=e\otimes q^{\mathrm{op}}+q\otimes e^{\mathrm{op}}\) to obtain
\[
 \|AP\|_2^2=2t(1-t)\{s_e^2+s_q^2+|m_e-m_q|^2\}.
\]
The expression in braces bounds \(v=t s_e^2+(1-t)s_q^2+t(1-t)|m_e-m_q|^2\) from below.
This calculation requires no commutation between \(e\) and \(H\).
Equations (3) and Cauchy–Schwarz give
\[
             t(1-t)v\le K\,\|[e,\eta]+2(e-t1)\|_2\,\|[H,e]\|_2.
\]
Both \(\sum_j\|e_j\eta\|_2^2\) and \(\sum_j\|\eta e_j\|_2^2\) are at most \(\|\eta\|_2^2\), and \(\sum_j\|e_j-t_j1\|_2^2\le\sum_jt_j\le1\).
The triangle inequality in the Hilbert direct sum proves (1).
As \(t\to0\), normality of the vector functionals of \(\eta,\eta^*\) gives \(\|[e,\eta]\|_2\to0\) uniformly in spectral projections of that trace, and \(\|e-t1\|_2\le\sqrt t\).
This proves the individual small-trace assertion.

### Noise on a block-diagonal operator

For \(a\in M_0\), freeness and centering give \(\mathbb E_{M_0}(VaV)=\tau(V^2)\tau(a)1\).
In particular \(Y\) has positive variance, since \(DVD\) is centered and orthogonal to \(L^2(M_0)\) with squared norm \(\tau(V^2)\tau(D^2)^2>0\).
As \(H_0\) commutes with \(e_j\), its off-diagonal blocks vanish.
Thus
\[
 \|[Y,e_j]\|_2^2
   =2\|(1-e_j)DVD e_j\|_2^2
   =2\tau(V^2)d_j^2 t_j\,\tau((1-e_j)D^2).
\]
This identity and (1) bound the sum of \(t_j(1-t_j)^2/d_j^2\), since \(\tau((1-e_j)D^2)\le\|D\|^2\).
At most one \(t_j\) exceeds \(1/2\), proving (2).
Also \(\|e_j V e_j\|_2^2=t_j^2\tau(V^2)\), which gives the asserted normalized disturbance inside each block.

Under (2), \(b=D^{-1}\) is affiliated with the base and belongs to its trace Hilbert space.
Use the derivation \(\partial_V\) on the algebraic free product \(M_0 * \mathbb C[V]\) which kills \(M_0\) and sends \(V\) to \(1\otimes1\).
The positive variance and scalar actual vacuum imply diffuseness of the noise law, so this is its represented polynomial algebra.
Freeness gives faithful realization of the algebraic free product and extends its vacuum as \(g\): a derivative cut in a centered reduced word with at least two blocks retains a centered free segment on a trace leg, and pure noise words give the scalar vacuum identity.
For bounded truncations \(b_m=\min(b,m)\), inner insertion of \(b_m\otimes b_m\) in \(\partial_V\) has vacuum \(b_m g b_m\), by the outer Leibniz adjoint formula with two constant base legs.
For each fixed word the inserted tensors converge in coarse Hilbert norm as \(m\to\infty\) since each derivative is a finite sum of bounded outer coefficients applied to the two truncated vectors.
Since \(g\) is centered and free from the base, \(\|a g c\|_2=\|a\|_2\|c\|_2\|g\|_2\) for bounded base factors \(a,c\), by the same trace calculation, extending to \(g\in L^2\) by centered bounded truncations.
Hence the vacua converge in Hilbert norm to the indicated \(b g b\) with norm \(\|b\|_2^2\|g\|_2\).
The limiting derivation still kills the base, and on \(Y\) its value is \(Db\otimes bD=1\otimes1\).
On the pair's represented starred core its values therefore lie in the coarse Hilbert space of \(W^*(Z,Y)\), so Hilbert projection of the ambient vacuum gives its actual vacuum there.
This proof allows \(H_0\) to have arbitrary dependence with \(Z\) inside the base blocks.

### A non-Gaussian example at the summability threshold

Give each closed disk of center \(2^{-j}\) and radius \(2^{-j-4}\) normalized area with total mass \(t_j=3\cdot4^{-j}\).
The resulting \(\mu\) is a compact planar probability with bounded area density and pairwise disjoint disks.
Its scalar vacuum exists by the [geometric criterion](Yin_C_F0255_v1.md#statement).
Indeed \(\mu(B(z,r))\le C r^2\) gives bounded maximal linear density, using \(\mu(B(z,r))\le1\) at large radii.
For fixed \(z\) the squared Menger curvature is at most \(4/\max(|z-w|,|z-v|)^2\) off the null diagonals; the part with this maximum in \((2^{-n-1},2^{-n}]\) has \(\mu^2\)-mass \(O(2^{-4n})\), giving summable small-scale contributions.
The free uniform noise has an actual scalar vacuum by the [real \(L^3\)-density criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate).
The projections of the disks form the claimed partition, and \(t_j/d_j^2=3j^{-2\alpha}\).
This excludes the distinguished vacuum at \(Z\) for \(\alpha\le1/2\).

For \(\alpha>1/2\) apply the [measurable free location and scale theorem](Yin_C_F0277_v1.md#statement) with zero drift.
Only its scale-ratio energy remains to check.
The same-block contribution is zero, and the separation for \(m<n\) is at least \(2^{-m}/3\).
Since \(d_j=j^\alpha2^{-j}\) is eventually decreasing, \(d_n/d_m\) is uniformly bounded for \(n>m\).
On different disks the squared difference of the two positive ratios is at most the sum of their squares.
The cross terms with the \(d_n/d_m\) ratio are bounded by a constant depending on \(\alpha\) times \(\sum_m4^m t_m\sum_{n>m}t_n<\infty\).
For the reverse ratio use
\[
  \sum_m4^m t_m d_m^2\sum_{n>m} t_n/d_n^2<\infty,
\]
since \(4^m t_m=3,\ \sum_m d_m^2<\infty\), and (2) holds.
Both conditions follow from that theorem.
At the borderline a nonzero coupling of adjacent spectral blocks thus still leaves insufficient mixing for the distinguished vacuum.
The example supplies no counterexample to the general implication.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:57 |
| status | open |
| reason | Fix the summable marginal commutator obstruction, its consequence for smoothing arbitrary block operators and the non-Gaussian threshold example for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Summable lower bounds from one distinguished vacuum, necessary noise scale, actual noisy-coordinate derivative and sharp threshold model. |
| argument | [Argument](#argument) | Liberation adjoint pairing, product trace variances, orthogonal block sum, free noise insertion, and cross-disk energy estimates. |
| dependency | [Liberation recovery](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Partial liberation with commutator vacuum and the forced normal marginal derivative. |
| dependency | [Measurable spectral blocks](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Bounded approximation of spectral projections in the liberation graph. |
| dependency | [Omitted graph actions](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Closure of left and right omitted graph multipliers to the full von Neumann algebra. |
| dependency | [Marginal adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Adjoint on the antisymmetric marginal tensor and the row and column correction. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Scalar vacuum existence from bounded maximal linear density and finite squared curvature. |
| dependency | [Real scalar density](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Scalar actuality on the line under an \(L^3\) density. |
| dependency | [Free location and scale](Yin_C_F0277_v1.md#statement) | The positive direction for the specified zero-drift scalar model under inverse-scale and ratio energies. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:13 |
| status | proved |
| reason | Independent review verified the commutator inequality, the necessary inverse-noise scale, the converse for the noisy coordinate with a scalar noise vacuum, and the non-Gaussian threshold example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Summable lower bounds from one distinguished vacuum, necessary noise scale, actual noisy-coordinate derivative and sharp threshold model. |
| argument | [Argument](#argument) | Liberation adjoint pairing, product trace variances, orthogonal block sum, free noise insertion, and cross-disk energy estimates. |
| dependency | [Liberation recovery](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Partial liberation with commutator vacuum and the forced normal marginal derivative. |
| dependency | [Measurable spectral blocks](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Bounded approximation of spectral projections in the liberation graph. |
| dependency | [Omitted graph actions](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Closure of left and right omitted graph multipliers to the full von Neumann algebra. |
| dependency | [Marginal adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Adjoint on the antisymmetric marginal tensor and the row and column correction. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Scalar vacuum existence from bounded maximal linear density and finite squared curvature. |
| dependency | [Real scalar density](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Scalar actuality on the line under an \(L^3\) density. |
| dependency | [Free location and scale](Yin_C_F0277_v1.md#statement) | The positive direction for the specified zero-drift scalar model under inverse-scale and ratio energies. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0311_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

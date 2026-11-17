---
author: Yin
---

# Controlling signed shell sums by commutators with perturbations of four group translations

## Statement

Use the group, free elements \(u,v\), conjugation average \(\mathsf P\), and nonidentity coefficient norm bound \(\rho=\sqrt3/2\) from [C80](Yin_C_A0080_v1.md#conjugation-on-the-nonidentity-coefficients).
Let \(A\) be a finite group-ring matrix with \(m\) columns and let \(p\) project onto its regular kernel.
For \(h\in H=\{u,u^{-1},v,v^{-1}\}\), take finite input-square matrices \(V_h=hI_m+E_h\), and suppose that
\[
                 \theta=\rho+\tfrac12\sum_{h\in H}\|E_h\|<1.           \tag{1}
\]
Here the norm in (1) is the regular operator norm.
Any certified upper bound, including a sum of coefficient norms, suffices.
The following are two ways to obtain a spatial estimate from the original matrix.

1. Suppose its kernel reduces every \(V_h\).
   Then \(\|1_{|g|\ge R}\widehat p\|_2\le C e^{-cR}\).
   This hypothesis can also be expressed using only original products by requiring for each \(D=V_h,V_h^*\) that \(\inf_X\|AD-XA\|_2=0\), over finite output-square matrices \(X\).
   No inverse or lower bound for a row operator is assumed.
2. For the dyadic return bound of [C76, equation (2)](Yin_C_A0076_v1.md#statement), take its finite \(K_j=(1-z_j)\sum_{l=0}^{N_j}z_j^lQ^l\) as in [C80](Yin_C_A0080_v1.md#statement).
   Fix \(\beta\ge0,\ \kappa\alpha>\beta\).
   Put \(D_j=\frac14\sum_h h^*[V_h,K_j]\), where brackets denote \(XY-YX\).
   Let \(w\ge1\) be an integer bounding the change in length in one application of the maps \(\mathsf P,\mathcal T\) below.
   Fix \(a>\beta/(2\log_2(1/\theta))\), \(k_j=\lceil a(j+1)\rceil\), and widen the dyadic shell \(S_j\) by \(wk_j\) on both sides to get \(S'_j\).
   If \(\sum_j2^{\beta j}\|1_{S'_j}\widehat D_j\|_2^2<\infty\), the truncated signed first-return array and the kernel projection have finite weighted square sums.
   This second test does not require exact reduction of the kernel.

Under exact reduction and the dyadic return bound, the original unperturbed conjugate-endpoint difference \(t_j\) of [C80, equation (1)](Yin_C_A0080_v1.md#statement) satisfies
\[
               t_j\le C(e^{-c2^j}+2^{-\kappa\alpha j/2}).
                                                                         \tag{2}
\]
The weighted square sum of the finite signed first-return array outside \(R=2^J\) is then \(O(e^{-c'R}+R^{-(\kappa\alpha-\beta)})\).
On the good four-line groups the spatial criterion for integral kernel trace applies when \(\beta>3\). [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace)

## Finite products and contraction off the identity

On the trace coefficient Hilbert space define
\[
   \mathcal T X=\tfrac14\sum_h h^*(X E_h-E_h X),\qquad
   X-(\mathsf P+\mathcal T)X=\tfrac14\sum_h h^*[V_h,X].
                                                                         \tag{3}
\]
Left and right multiplication by \(E_h\) each has norm at most \(\|E_h\|\).
Let \(\Pi\) discard the coefficient at the identity, and write \(\mathcal L=\Pi(\mathsf P+\mathcal T)\Pi\).
On its offidentity space \(\|\mathcal L\|\le\theta\).
One may take \(w\) to bound \(2|h|\) and \(|h|+\max_{g\in\operatorname{supp}E_h}|g|\) for every nonzero summand.
For any \(X\), the identity coefficient contributes a source \(\Pi\mathcal T(I-\Pi)X\) supported in the ball of radius \(w\).
In the exact case this gives
\[
  \Pi p=\sum_{l\ge0}\mathcal L^l\Pi\mathcal T(I-\Pi)p .
\]
The \(l\)-th term has support in the ball of radius \((l+1)w\) and norm at most \(C\theta^l\), proving exponential decay.
To verify the row-fit formulation, \(ADp=0\) is equivalent to invariance of the kernel under \(D\).
The infimum of the fit residual equals \(\|ADp\|_2\): multiply the residual on the right by \(p\) for the lower bound, and approximate \(AD(A^*A+tI)^{-1}A^*\) for the upper bound as in [the row-fit identity](Yin_C_A0080_v1.md#a-finite-upper-bound-from-row-fits).
Testing the adjoints supplies reduction.

For \(X=K_j\), iterate (3) \(k_j\) times after projecting away the identity.
For large \(j\) the source at radius \(w\) cannot reach the shell in \(k_j\) steps.
The direct bound on the remaining terms is
\[
 \|1_{S_j}\widehat K_j\|_2
    \le (1-\theta)^{-1}\|1_{S'_j}\widehat D_j\|_2+\theta^{k_j}\sqrt m.
                                                                         \tag{4}
\]
Here \(\|K_j\|_2\le\sqrt m\), and a term reaching \(S_j\) starts in \(S'_j\).
Every coefficient of \(D_j\) is determined by the original product fibers: insert \([V_h,Q]\) between \(Q^b\) and \(Q^{l-1-b}\), sum over \(0\le b<l\), multiply on the left by \(h^*\), then sum over \(l,h\) before taking the norm.
For \(E_h=0\) these are precisely differences at conjugate endpoints.
For nonzero \(E_h\) formula (3) accounts for both finite convolution corrections.
The padded-probe polarization and finite-time errors in [C80](Yin_C_A0080_v1.md#signed-estimates-on-widened-shells) pass (4) to the first-return array with the same square summability.
The remaining comparison to \(p\) is [C76, equation (3)](Yin_C_A0076_v1.md#statement).
No shell volume enters (4).

Under reduction, \(\|K_j-p\|_2=O(2^{-\kappa\alpha j/2})\) by the dyadic return and the C76 truncation.
Thus even the global norm of \(D_j\) has this rate by (3) and \([V_h,p]=0\).
For the original \(t_j\), all four conjugations change length by a bounded amount, and its widened shell has inner radius \(2^j-O(j)\).
The exponential estimate for \(p\) and the unweighted estimate for \(K_j-p\) give (2).
The stated exterior bound also follows directly from the two-sided signed-array comparison in C76 and the exponential exterior of \(p\), absorbing polynomial weights into a smaller exponential.

## A nonclosed example with a whole-group row Gram and projection

In an individual good four-line group let \(t_1=u,t_2,\ldots,t_q\), \(q\ge2\), generate \(G\), take \(P\) to be a finitely supported symmetric generating probability, and put \(U=1-u,\ \ell=UU^*\).
Use \(D=100I+P\), \(L=UDU^*\), and the column \(F_i=\varepsilon(1-t_i)\).
With \(W=\binom{I}{F}\), \(Z=\binom{-F^*}{I_q}\), define
\[
             A=(LI_q) Z^*,\qquad
             V_h=W h W^*+ Z(hI_q) Z^* .
\]
Here \(W^*Z=0\), \(Z^*\) is onto, and its kernel is the graph of \(F\), the closed range of \(W\).
Since \(U\) and \(U^*\) are injective with dense range and \(99I\le D\le101I\), \(L\) is positive injective, with \(99\ell\le L\le101\ell\).
It has dense nonclosed range, by comparison with the circle multiplier \(\ell=2-u-u^{-1}\) at phase one.
The same range property holds for \(A\).
Each \(V_h\) and its adjoint preserve both complementary graphs, and \(V_h\to hI_{q+1}\) in operator norm as \(\varepsilon\to0\).
Choose rational \(0<\varepsilon<1\) small enough for (1).
The projected graph has
\[
            p=W(I+F^*F)^{-1}W^* .
\]
Its first diagonal entry has support all of \(G\): the inverse of \( (1+2q\varepsilon^2)I-\varepsilon^2\sum_i(t_i+t_i^{-1})\) has a positive Neumann series reaching every element.
In particular its coefficient array is infinite.

No choice of \(q\) columns gives a full square block over any common cyclic subgroup even after independent group translations of rows and columns.
Each choice contains a column with entry \(L\), as there is only one column outside the \(q\) diagonal columns.
The identity and \(u\) coefficients of \(L\) are nonzero since \(\|L-100\ell\|\le4\).
If its support were in a translated subgroup coset \(xHy\), the identity would make this set a conjugate subgroup containing \(u\).
Within that subgroup's von Neumann algebra the affiliated inverses of \(U,U^*\) recover \(D\) from \(L\), and hence the full generating support of \(P\).

Even the first diagonal entry \(B=L(I+\varepsilon^2\ell)L\) of \(AA^*\) needs the whole group.
The \(u\) coefficient of \(10000\ell^2\) is \(-40000\), whereas \(\|L^2-10000\ell^2\|\le4(404+400)\).
Shrink \(\varepsilon\) further so that \(\varepsilon^2\|L\|^2\|\ell\|<10000\).
Thus any subgroup carrying \(B\) contains \(u\).
Writing \(S=I+\varepsilon^2\ell\), one recovers \(L=S^{-1/2}(S^{1/2}BS^{1/2})^{1/2}S^{-1/2}\), so the subgroup equals \(G\).
The four-line group itself is nonfree by its nonzero binary zero product. [C51](Yin_C_A0051_v1.md#statement)

Finally \(AA^*=(LI_q)(I_q+FF^*)(LI_q)\) lies between fixed positive constant multiples of \(L^2 I_q\).
Trace spectral comparison for \(L\) with \(\ell\), followed by squaring the spectral variable, gives positive spectral mass comparable to \(s^{1/4}\) at zero for \(AA^*\).
Indeed the circle length where \(2-2\cos x\le t\) is comparable to \(t^{1/2}\).
The positive spectra of the two rectangular Grams agree in trace, hence C76's dyadic bound holds with \(\alpha=1/4\).
For every \(\beta>3,\ \kappa>4\beta\), (2) controls the original signed sums in this example.
Here \(Z^*\) is also an explicit closed-range row matrix with the same kernel.
The general argument in (3)–(4) uses the four polynomial commutators and applies whenever its hypotheses can be verified, regardless of the availability of such a matrix.

## Assessment history

### Decision perturbed-conjugation-shells

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:37 |
| status | proved |
| reason | Independent review verifies both commutator criteria and the whole-group scope of the example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Conjugation commutator criteria for spatial decay and finite signed shell sums on nonclosed input. |
| argument | [Proof](#finite-products-and-contraction-off-the-identity) | Offidentity contraction, original product insertions, bounded propagation and the example of spectral exponent one fourth. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0125_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-perturbed-conjugation-shells)

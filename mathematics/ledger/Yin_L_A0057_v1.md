---
author: Yin
---

# How far the free product-fiber moments control an actual four-line kernel

Fix one finite complex word matrix \(A\) on the free rose group \(F\) and its images on the pattern-free groups \(G_n\).
The [marked systole and inner-rank bounds](Yin_L_A0054_v1.md#the-rank-seen-by-a-fixed-matrix) give a lower bound \(\sigma_n\to\infty\) on nontrivial reduced null-word lengths and \(\alpha_n\ge\alpha\) for the respective unnormalized kernel traces on \(G_n\) and \(F\).
Normalize both Gram matrices \(B=A^*A/M\) to positive contractions by the same sum-of-coefficients norm bound, and let \(w\ge1\) bound the word radius of the free Gram entries.
Write \(p_n,p_F\) for the actual kernel projections.

If \(2kw<\sigma_n\), the marked ball of radius \(kw\) is identified by a root-distance-preserving bijection with the corresponding ball in \(F\), since two different words in that ball cannot have the same image, and every quotient element of that length has a lift of no greater length.
Distances between two arbitrary points of the ball need not be the same on both sides.
For every polynomial \(q\) of degree at most \(k\) satisfying \(q(0)=1\), all group coefficients of \(q(B)\) agree under the ball identification, with zero coefficients outside it.
Let
\[
 e_k=\min_{\deg q\le k,\ q(0)=1}
         (\operatorname{Tr}\otimes\tau_F)(q(B_F)^*q(B_F))-\alpha .
\]
This nonnegative number is determined by finitely many free product fibers and the free-field nullity. It tends to zero by the [polynomial minimum calculation](../claims/Yin_C_A0014_v2.md#a-moment-increment-criterion-with-no-unknown-atom-in-its-hypothesis), or by using \(q(t)=(1-t)^k\).
For a minimizing \(q\), the squared \(L^2\) distances from \(q(B_F)\) to \(p_F\), and from \(q(B_n)\) to \(p_n\), equal \(e_k\) and \(e_k+\alpha-\alpha_n\), respectively.
Indeed \(q(B)p=p\) on either group and the two finite squared norms agree.

View the Fourier coefficient arrays in one Hilbert space by identifying the two balls and keeping the two complements on disjoint coordinates.
Their common polynomial approximant and the triangle inequality give
\[
      \|\widehat p_n-\widehat p_F\|_2 \le 2\sqrt{e_k}.
\]
In particular the two distributions on word radii of squared Fourier mass differ in \(\ell^1\) by at most \(4\sqrt{m e_k}\), for \(m\) input columns, by Cauchy–Schwarz and the bound \(\|p\|_2\le\sqrt m\).
This also bounds the difference of every pair of limiting endpoint moments \(D(2^{-j})\) in [the weighted fiber test](../claims/Yin_C_A0057_v1.md#argument), uniformly in \(j\), since their radial multipliers lie between zero and one.

For any exponent \(\beta>0\), restriction to radii at most \(R\le kw\) bounds the weighted coefficient norm of the difference by \(2(1+R)^{\beta/2}\sqrt{e_k}\).
By [bounded free-group rationality and inverse approximation](../claims/Yin_C_A0058_v1.md#argument), \(p_F\) has an exponentially weighted square sum even in the nonclosed-range case.
Along a good sequence choose \(k_n\to\infty\) with \(2k_nw<\sigma_n\).
Consequently on every window \(R_n\to\infty\) with \(R_n\le k_nw\) and \((1+R_n)^\beta e_{k_n}\to0\), the truncated weighted masses of the actual projections converge to the full weighted mass on \(F\).
Such a diverging choice always exists by taking the smaller of \(k_nw\) and \(e_{k_n}^{-1/(2\beta)}\), interpreted as infinity if \(e_{k_n}=0\).
When \(e_k=0\) at an accessible finite order, the common polynomial is already the exact projection in both groups.

This gives finite higher-moment bounds for a growing spatial window of a fixed word matrix involving any rose letters.
It does not bound the weighted mass outside that window on an individual group, even though the unweighted leakage tends to zero along the sequence.
For example a mass \(1/r\) at a radius \(r\to\infty\) is negligible in total variation but has divergent weighted contribution for \(\beta>1\).
This last example concerns the logical strength of the comparison and is not a claimed kernel projection in the four-line groups.

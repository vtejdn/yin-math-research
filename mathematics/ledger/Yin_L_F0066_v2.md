---
author: Yin
---

# Complex orientation and diagonal-floor boundaries for Wigner cofactors

This comparison retains explicit failed deterministic implications arising in the complex-law investigation for [F0012](../tasks/Yin_T_F0012_v3.md#contract), [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract).
The earlier [real cofactor and Riccati-fiber comparison](Yin_L_F0066_v1.md) remains at its fixed scope.
These are calculations checked within proof development, not an independent review or counterexamples to the original Tasks.
The new retained comparisons were checked on 2026-11-05T13:04 UTC.

<a id="transpose-noncancellation-failure"></a>
## A real transpose coefficient can vanish for a complex Hermitian input

For a purely imaginary upper law \(i\varepsilon\), with real Rademacher \(\varepsilon\) and zero diagonal, every realization is both Hermitian and transpose-skew.
If an even-dimensional minor \(D\) is invertible, then \(D^{-1}\) is transpose-skew and
\[
 A=\operatorname{adj}D=(\det D)D^{-1}\ne0,
 \qquad \operatorname{sym}A=(A+A^T)/2=0.
\]
For example \(D=\operatorname{diag}(J,\ldots,J)\), with \(J=\begin{pmatrix}0&i\\-i&0\end{pmatrix}\), has these properties.
Thus a graph based on the symmetric adjugate has no edges at any positive threshold despite a nonzero full adjugate.
No assertion that every even random realization is invertible is needed.
The [fixed odd-size obstruction](../claims/Yin_C_F0194_v6.md#odd-skew-obstruction) separately records the parity-forced zero determinant; neither statement refutes a dimension-limsup or Brown-convergence contract.

<a id="mixed-orientation-cancellation"></a>
## Positive real variance and an invertible symmetric part do not prevent cancellation

Let \(c=(1+i)/\sqrt2\), take a real Rademacher amplitude, and consider two oppositely oriented internal coordinates
\[
 z=(c\varepsilon_1,\overline c\varepsilon_2)^T,\qquad
 R=\begin{pmatrix}0&1-i\\1+i&0\end{pmatrix},\qquad B=R/2.
\]
Since \(R^2=2I\), this is exactly \(R=B^{-1}\).
Moreover
\[
 \|B\|=1/\sqrt2,\qquad
 \operatorname{sym}B=\tfrac12\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad s_{\min}(\operatorname{sym}B)=1/2.
\]
Put
\[
 E=\operatorname{diag}(1,-1),\qquad
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 T=\begin{pmatrix}0&-i\\i&0\end{pmatrix}.
\]
Writing \(z=x+iy\), one has \(x=(\varepsilon_1,\varepsilon_2)^T/\sqrt2\), \(y=Ex\), and \(iTE=-S\).
The actual internal coefficient map therefore satisfies
\[
 \Phi(z)=\frac{Rz+R^T\overline z}{2}
        =Sx+iTy=Sx+iTEx=0
\]
for every pair of signs.
Thus a bound on \(\|B\|\), a positive least value of \(\operatorname{sym}B\), and positive variance of \(\operatorname{Re}\xi\) do not by themselves force any positive singular rank in this mixed-orientation map.
Direct sums give the same deterministic cancellation in every even internal dimension when the orientation groups are balanced.

This two-coordinate configuration is realizable inside an actual shifted Hermitian matrix.
At dimension \(N=3\), expose the row of index \(2\), whose two internal column orientations at coordinates \(1,3\) are \(\xi,\overline\xi\).
Take zero diagonal law and deterministic shifts
\[
 F_{13}=(1-i)/2-c/\sqrt N,\qquad
 F_{31}=(1+i)/2-\overline c/\sqrt N,
\]
with zero internal diagonal shifts.
These shifts are Hermitian and bounded.
On the event \(\varepsilon_{13}=1\), of probability \(1/2\), the internal block on coordinates \(1,3\) is exactly \(B\), independently of the two exposed signs.
This verifies that the failed conditional implication is not based on an impossible internal block.
It is a fixed-dimensional event, not a nonvanishing asymptotic failure probability for a full random Wigner minor.
The [reviewed phase-line proof](../claims/Yin_C_F0194_v6.md#majority-orientation-lemma) uses additional majority-orientation information at its exact scope, rather than the false unrestricted deterministic implication.

<a id="independent-real-component-boundary"></a>
## A nonreal line law need not contain independent additive real noise

An independent real additive component is a useful sufficient hypothesis for reducing a complex matrix to real Wigner noise plus an independent shift.
It is strictly different from positive real-part variance.
Suppose \(\xi=c\eta_0\), where \(\eta_0\) is nondegenerate and real and \(\operatorname{Im}c\ne0\).
There is no distributional representation
\[
 \xi=a\eta+\theta,\qquad a>0,\qquad
 \eta\text{ real},\quad\operatorname{Var}\eta=1,\quad
 \eta\perp\theta,
\]
with finite second moments.
Indeed the real linear functional \(L(w)=\operatorname{Im}(\overline c\,w)\) vanishes almost surely on \(\xi\), whereas independence would imply
\[
 \operatorname{Var}L(a\eta+\theta)
 =a^2(\operatorname{Im}c)^2+\operatorname{Var}L(\theta)>0.
\]
This is a contradiction.
In particular \(\operatorname{Re}c\ne0\) does not supply that additive decomposition.
The example excludes this reduction, not the [reviewed phase-line floor](../claims/Yin_C_F0194_v6.md#statement) when its actual nonzero-real-part hypothesis holds.
Allowing a general complex multiplier \(a\) would change the latent real symmetric matrix identity and is outside the proposed reduction.

<a id="principal-compression-boundary"></a>
## A full symmetric-part floor does not pass to every principal compression

Let \(S\) be block diagonal with two-by-two blocks \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\).
It is real symmetric and all its singular values equal one.
Deleting a single coordinate leaves a principal compression with one zero row and column, hence zero least singular value.
Thus a positive full-matrix least value does not imply a positive least value for every principal compression.
The compression in this example loses only one singular direction; every earlier singular quantile is still one.
It therefore does not refute a hypothesis asking only for the \(k\)-th singular value of each actual compression, with \(k\) well below its dimension.

These failures identify missing assumptions in specific deterministic or latent-noise steps.
The actual random-minor estimates must use their precise orientation, independence and singular-quantile hypotheses.
None of the examples supplies a failure of the original fixed-law, fixed-polynomial, arbitrary-coupling objectives.

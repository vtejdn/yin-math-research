---
author: Yin
---

# Review of fixed-trace domains and canonical cutoff divergence

## Finding

At 2026-11-14T14:57 UTC an agent outside proof development reviewed the full [C_F0282 v1 candidate](../../claims/Yin_C_F0282_v1.md#decision-candidate) dated 2026-11-14T14:55 and its eight direct dependency interfaces.
The reviewer received the fixed proof and the requested issues to check, including the scope of the ACSY adjoint theorem.
No substantive development dialogue, exploration notes or prior finding on this candidate was supplied or consulted.
The dichotomy, the sharp constant for each trace, and the cutoff and domain conclusions follow under the stated hypotheses.

For a projection of positive trace in a diffuse finite algebra, repeated splitting produces nonzero pieces of arbitrarily small trace.
Normality of the trace on increasing chains gives an upper bound for every chain of subprojections of trace at most \(s\).
A maximal such projection exhausts \(s\), since any remaining positive deficit could be filled by a smaller nonzero piece of the residual corner.
Dyadic partitions in each corner therefore realize a diffuse probability algebra.
The average of \(l\) circle translates of an interval of mass \(v\) differs in norm from \(v1\) by at most \(1/l\), since the number of equally spaced points in a half-open arc is either \(\lfloor lv\rfloor\) or \(\lceil lv\rceil\).
Neither comparison nor averaging requires equivalence of projections of equal scalar trace.

Polar decomposition of \((1-q)p\) gives the trace identity \(\tau(p\vee q)+\tau(p\wedge q)=\tau(p)+\tau(q)\).
For a pair of trace \(s\) this bounds the discarded trace of \(e_0\) by \(2s\) and leaves at least \(1-2s\) outside their join.
Thus the common \(f\) of trace \(t-2s\) and its extension \(b\) of trace \(t-s\) exist under the stated restrictions.
Each \(e=b+p,b+q\) contains \(f\), so \(\tau(e_0e)=\tau(e_0 e e_0)\ge\tau(f)\) and \(\|e-e_0\|_2^2\le4s<\epsilon^2\).
Subtracting the two inputs and averaging the second projection gives the ball bound \(2K\) on \(T(p-s1)\), by weak compactness of the outputs and weak closure of the graph.
Equal-trace splitting with \(l=\lceil1/s_0\rceil\) then gives a uniform projection bound using \(1\in\operatorname{Dom}T\).
Spectral mesh approximations of positive contractions and four positive parts give full bounded inclusion.
Conversely, a closed Hilbert graph is also closed for operator-norm convergence in \(M\), so the closed graph theorem applies to the full restriction.
The same graph argument closes each norm sublevel in the trace layer, which is complete because bounded \(L^2\) limits of projections preserve the operator bound, involution, square and trace.
For deficient operators each sublevel consequently has empty interior on every layer, and Baire's theorem applies also to the countable intersection.

When \(T1=0\), one may replace \(t\) by \(m=\min(t,1-t)\) and an arbitrary projection by its complement.
For \(s=\tau(p)\le m\), averaging trace-\(m\) supersets yields the coefficient \((1-m)/(1-s)\) of \(Tp\).
For \(m\le s\le1/2\), averaging trace-\(m\) subsets yields the coefficient \(m/s\).
These give precisely the two upper bounds in (1).
The two-half signed density attains the ratio \(1/(2m)\).
For the density \(1_A/s-1\) with \(0<s<m\), both extreme overlaps \(0,s\) occur on the \(m\)-layer, so \(B_m=\max(m,1-m)=1-m\) and \(B_{\rm all}=1-s\).
Letting \(s\downarrow0\) gives the other lower bound for every \(m\), including \(m=1/2\).
Comparison with \(4D_t B_t\) on all contractions follows from the same four-part spectral approximation.

For the normal tuple, a diffuse marginal excludes a finite matrix factor, and the two-coordinate relative-commutant theorem gives factoriality for \(d\ge2\).
For \(d=1\) the generated marginal itself is diffuse.
At each \(r>0\), the inner identity \(\gamma=I_{z-w}\delta\) in C_F0238 identifies its \(CI_{k_r}\gamma\) with the right slice in the candidate.
That result gives finite single-input norm from its column bound and strong convergence on each fixed core input as \(r\to0\).
The inner multiplier commutes with both outer actions, so the suppressed map is still a derivation on the original weakly dense starred core \(P\).
C_F0081 supplies its actual adjoint vacuum.
The published ACSY24 definition on p. 34 and Theorem 3.4 and its proof on p. 35 require only this derivation and vacuum for the construction of the right slice and its polynomial adjoint domain.
Generator normalization enters Proposition 3.5 separately.
Indeed, for either derivation \(\theta\), \(L=(\mathrm{id}\otimes\tau)\theta\) satisfies \([L,b]=\Theta(\theta b)\) on \(P\), where \(\Theta(u\otimes v)x=u\tau(vx)\) extends isometrically to Hilbert–Schmidt operators.
Since \(L^*1=\theta^*(1\otimes1)\), testing this identity at \(b^*\) gives \(L^*b=bL^*1-\Theta(\theta b^*)^*1\) for \(b\in P\).
Thus each sliced core has dense adjoint domain, and the bidual argument in C_F0276 gives the normal extension with its exact core norm.
This step makes no assertion about the original Hilbert graph containing every bounded vector before the uniform estimate has been obtained.

For a bounded original slice, C_F0237 gives the product estimate \(2a\) for every separated pair of marginal spectral unitaries, including the continuous Fourier characters by approximation in the marginal \(C^*\)-algebra.
The Fourier measure for \(r^2/(|z-w|^2+r^2)\) is a probability by the Gaussian mixture in C_F0238, yielding \(3a\) after subtraction.
In reverse, normality makes the sublevels of the extensions closed on bounded \(L^2\)-convergent inputs.
The patch averages and spectral approximations use uniformly bounded inputs, and every extension vanishes on \(1\).
Thus a common bound on one patch bounds all extension norms, and a common bound on the whole trace layer gives \(4D_t\) times that bound.
Passing to core inputs proves (2) along the prescribed sequence without monotonicity.
If \(a=\infty\), finite supremum is a union of nowhere dense sublevels, and infinite supremum is infinite limsup because each individual output is finite.
Kaplansky approximation from the core and weak graph closure show that \(a<\infty\) suffices for \(M\subseteq\operatorname{Dom}\overline{S_0}\).
The converse follows from the closed graph theorem.
Intersecting the two dense \(G_\delta\) sets gives (3).
The adjoint separately has \(1\) in its domain by the exact vacuum formula above, so its own graph proves the claimed category conclusion even without an adjoint core assertion.
Using all coordinates in both orientations invokes the strong-system equivalence and the generator-first convention of C_F0075.
The implication from infinite original column cost uses \(c\le\sqrt2\,a\) precisely in the stated range \(d\ge3\).
The candidate leaves universal boundedness of the cutoff sequences unresolved.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0282_v1.md#decision-candidate) | Complete fixed candidate at 2026-11-14T14:55 and its eight direct dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0282_v1.md#statement) | Every prescribed trace, both sharp comparisons, family category assertion, cutoff sequence, original domains and dimension-three column implication. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0282_v1.md#argument) | Diffuse-corner constructions, projection dimension, sharp examples, closed graphs, normal extensions, Fourier averaging and Baire intersections. |
| [Finding](#finding) | [Normal marginal](../../claims/Yin_C_F0076_v1.md#statement) | Represented starred derivations and diffuse coordinate spectral laws under the full actual hypothesis. |
| [Finding](#finding) | [Factoriality](../../claims/Yin_C_F0202_v1.md#statement) | Scalar center for at least two coordinates, ruling out an atomic summand in conjunction with the diffuse marginal. |
| [Finding](#finding) | [Cutoff and Fourier formulas](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Identification via partial liberation, finite individual column norms, core convergence and the Gaussian probability mixture. |
| [Finding](#finding) | [Suppressed actual vacuum](../../claims/Yin_C_F0081_v1.md#statement) | Outer derivation on the original starred core and actual vacuum at parameter \(r^2\). |
| [Finding](#finding) | [Actual slice adjoint](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 and its adjoint construction checked against published pp. 34–35 for original and suppressed derivations, independently of generator normalization. |
| [Finding](#finding) | [Original single-input reduction](../../claims/Yin_C_F0276_v1.md#statement) | Normal summand from a bounded core map with dense adjoint, and \(c\le\sqrt2\,a\) for \(d\ge3\). |
| [Finding](#finding) | [Single-input multiplier estimate](../../claims/Yin_C_F0237_v1.md#two-slice-identities-and-the-different-component-terms) | Bounded right slice of a separated multiplier and integration over continuous unitary characters. |
| [Finding](#finding) | [Normal domains](../../claims/Yin_C_F0075_v1.md#statement) | Two bare orientations imply the strong system with the canonical forward and adjoint domains and generator-first sign. |

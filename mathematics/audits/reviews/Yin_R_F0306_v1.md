---
author: Yin
---

# Review of singular states on the essential fibers of a Borel shift

## Finding

Review time (UTC) 2026-11-16T15:32.
A separate agent outside development reviewed the complete candidate dated 2026-11-16T15:30, starting from its statement, proof and direct inputs.
The reviewer received no development discussion, author explanation or previous finding about this candidate.
The argument establishes all the stated conclusions for one fixed bounded Borel shift.

At a positive radius set \(Q=(T^*T+s^2)^{-1}\) and \(Q'=(TT^*+s^2)^{-1}\).
Then \(h=s^2Q,\ h'=s^2Q'\) and \(V=sTQ\).
Differentiating \(TQ\) combines its two terms containing \(\delta T\) by \(1-TQT^*=s^2Q'\).
Differentiating \(Q\) puts \(TQ\) on the right of \(\delta T^*\) and \(QT^*\) on the left of \(\delta T\).
Inserting the marginal derivatives \(-D,-D'\) gives exactly both signs, both copies of \(V\) in the first identity and the single \(V^*\) in the second.
The actual starred core supplies these derivatives for the Lipschitz approximants and their conjugates, with uniform convergence on the spectrum and coarse convergence off the diffuse diagonal.
The tensor-adjoint formula for the approximating legs of \(g\otimes g\) converges in \(L^2\), since multiplication against the fixed vacuum converges in that norm and the two partial traces are contractions on the coarse Hilbert space.
Cyclicity moves the real tensor test next to the marginal symbol on both legs, including the opposite leg.

For the Borel limit, the fixed bump in the gluing construction meets only the region where the Lipschitz extension agrees almost everywhere with \(f\).
Consequently bounded \(L^2(\mu)\) approximation survives gluing, while \(g(y)g(w)D_m(y,w)\) and its conjugate-numerator counterpart are fixed bounded symbols almost everywhere for every \(m\).
The inverse identities above give bounded strong-star convergence of all three regularizations at this radius.
For instance, testing the product of two converging outer factors against the fixed bounded symbol passes to the limit by normality of the product trace on bounded strongly convergent sequences.
This justifies localization with no uniform Lipschitz constant required across the glued sequence.

For \(b=f(Y)\) the omitted-algebra hypothesis at \(Z\) holds, so the kernel and the two concentration results apply.
The discarded radii with \(s<1\) and \(F(s)\le s^{3/4}\) cost at most \(\int_0^1s^{-3/4}\,ds=4\) of the divergent integral.
They therefore consume vanishing probability in the truncated scale selection.
The original finite-stage inequalities for marginal tests at \(Z\) and for all dyadic scales leave positive probability for the extra countably enumerated bump adjoints at \(Y\), imposed finitely at each stage.
Since the family is a singleton, \(F/2\le H\le6F\), and the same trace norm bound \(A/H\le24\) controls the complex marginal restricted to either coordinate.
The common point \(z_0\) and the secant lower bound at \(Z\) survive subsequences.
The residual second moments are \(s^2(1-H)/H\) in their respective orientations and tend to zero.
The Hilbert seminorm triangle inequality then controls the second moment of \(f(Y)-z_0\) in each state, using normality on the adjoint side.
The joint continuous functional calculus of \(Y,f(Y)\) has spectrum equal to the support of their traced law by faithfulness.
Passing to subsequential limits there therefore puts both probabilities on the correct essential fiber, including at discontinuities.

For a tested point the error in replacing its localized symbols by \(d,d'\) is bounded by their local oscillations times a fixed product variation bound.
Weak limits on each continuous bump may thus precede shrinking the bump to the point.
This order gives \(dL_vR_v=d'G_v^2\) and \(R_v(d'G_v+d\overline{G_v})=0\) on one sequence for every tested point.
For \(R_v>0\) these equations yield \(L_vR_v+|G_v|^2=0\).
The lower bound on the local divided difference makes each regular inverse branch injective, and continuity there identifies the essential graph with the representative's graph.
If every point is regular, compactness makes the discrete fiber finite, so the positive limits have disjoint supports.
Separating these supports with a continuity set gives a projection \(p\) with \(\|(1-p)e_n\|_2+\|e'_n p\|_2=o(\sqrt{F(s_n)})\), since the hard weights are bounded by twice the soft ones and \(H/F\le6\).
Inserting \(1=p+(1-p)\) gives the asserted normalized overlap.
The singleton criterion follows by contraposition.
For a holomorphic polynomial, the second secant is the conjugate of the first times \((\bar y-\bar w)/(y-w)\), verifying the simple-root example under the stated chord hypothesis.

The finding covers the direct interfaces below and the candidate's deduction from them.
It gives no uniform estimate over omitted shifts and leaves the general implications of Task F0011 open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0298_v1.md#decision-candidate) | Complete candidate dated 2026-11-16T15:30 with all six declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0298_v1.md#statement) | Common sequence and essential fiber, regular-point atom exclusion, finite regular fibers, hard overlap, singleton consequence and polynomial example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0298_v1.md#argument) | Both localized identities, Borel approximation, joint scale selection, concentration at both coordinates, diagonal limits and all consequences. |
| [Finding](#finding) | [Starred hypothesis](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Two distinct normal coordinates with original represented starred derivations and their actual vacuum adjoints. |
| [Finding](#finding) | [Shifted singular laws](../../claims/Yin_C_F0229_v1.md#statement) | Both kernels vanish for the fixed omitted shift, giving a unitary polar factor. |
| [Finding](#finding) | [Marginal symbols and adjoint](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuseness, both starred symbols, omitted derivatives at the other coordinate and the tensor-adjoint formula. |
| [Finding](#finding) | [Lipschitz approximation](../../claims/Yin_C_F0257_v1.md#comparing-the-two-represented-cores-in-both-directions) | Uniform approximation on the compact marginal with bounded Lipschitz constants and joint coarse convergence for conjugate functions. |
| [Finding](#finding) | [Mixed resolvent derivatives](../../claims/Yin_C_F0287_v1.md#the-two-derivations-and-the-polar-resolvents) | Opposite outer multiplication and geometric inverse approximation at each fixed positive radius. |
| [Finding](#finding) | [Spectral concentration](../../claims/Yin_C_F0269_v1.md#argument) | Arbitrary countable fixed Hilbert tests within the scale selection, both positive marginal limits and the complex variation bound. |
| [Finding](#finding) | [Local secant theorem](../../claims/Yin_C_F0273_v1.md#argument) | Simultaneous dyadic inequalities, total variation away from the concentration point and the numerical secant bound. |

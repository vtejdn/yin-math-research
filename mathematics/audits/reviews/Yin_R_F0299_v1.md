---
author: Yin
---

# Review of the Möbius coupling of a free Haar unitary

## Finding

At 2026-11-14T16:01 an agent outside the proof development independently checked the whole argument of the [fixed candidate](../../claims/Yin_C_F0290_v1.md#decision-candidate).
The reviewer received its statement, argument and required scope and used its cited mathematical inputs.
No development discussion, author explanation or prior finding on this candidate entered the review.
The argument proves the three-way equivalence, both exact vacuum norms, the two orientations of column control and the disk example, including the possibly singular case \(\|h\|_\infty=1\).

For the endpoint construction I checked the ordering
\[
 (Wh^*)^n=\left(\prod_{j=1}^{n} W^j h^*W^{-j}\right) W^n
\]
with the product taken in increasing order.
The conjugated algebras are free by the centered reduced-word test, so cyclic extraction of each squared letter gives the geometric \(L^2\) bound.
The bare series telescopes on both sides and the regularized unitaries converge boundedly strongly-star.
In the algebra of affiliated operators the linear relation for \(aY\) yields \(W a(1-h^*Y)=a(Y-h)\).
The full support of \(D\) and \(\|v\|_2^2-\|h^*Yv\|_2^2=\|DYv\|_2^2\) give injectivity, and finiteness gives dense range.
The resulting inverse lies in the affiliated algebra of \(W^*(Z,Y)\) and recovers \(W\).
Positive Fourier degrees in the gauge action give the Poisson moments.
The resulting fibers are diffuse, have variance \(1-|h|^2\) at the test \(u\mapsto u\), and have mean \(h\).
The conditional divergence estimate therefore forces \(I<\infty\) on splitting at \(|h|=(1+|\tau Y|)/2\).

I computed the cuts of both \(W^n\) and \(W^{-n}\) for \(n>0\).
The first and last of the four scalar slices have vacua \(W,-W^*\), respectively, and both mixed slices have zero vacuum.
All slices are shifts restricted to one Fourier half-space and have Hilbert norm at most one.
The terminal estimate in the cited argument uses the scalar slice, its vacuum and the commutative noise algebra, so it applies to the Laurent polynomial algebra here.
For an insertion \(f\otimes g\), trace cyclicity against a word \(p\) gives the vacuum pairing with \(f^*v_{lr}g^*\).
The terminal block leaves the right coefficient \(g\) paired with the trailing base block and the left coefficient \(f\) after the scalar slice.
This checks the order of the coefficients in both uses of (4), including Hilbert-tensor approximation.

Differentiating the bounded-parameter expression leaves the outside factors \(D(1+Wh^*)^{-1}\) and \((1+h^*W)^{-1}D\).
Expanding \(PY\otimes Q-P\otimes YQ\) gives all four signs in (6).
The two surviving Haar modes are orthogonal under every base multiplier because \(\tau(W^2)=0\).
Their measures give the liberation density \(2|h(z)-h(w)|^2a(z)^2a(w)^2\) and the unitary-coordinate norm \(I^2+(I-1)^2\).
Dominated kernel convergence for finite \(I\) yields limiting vacuum pairings.
Testing a represented relation between arbitrary polynomial multipliers forces its derivative to vanish against a dense set of simple tensors.
The normal inverse-gap theorem applies with both diffuse marginals and gives the correction \(2J\) to the squared marginal vacuum norm.

For the column estimates I checked the two reference subtractions against \(\Gamma W=W\otimes1-1\otimes W\).
Writing \(d_x^2=1-|x|^2\), the inequalities \(0\le\operatorname{Re}(1-\bar xy)-d_xd_y\le |1-\bar xy|-d_xd_y\le |x-y|\) and \(|\operatorname{Im}(\bar xy)|\le |x-y|\) give the asserted uniform bound for both mixed kernels.
The two inner base actions commute with the outer actions, so multiplying by the regularized inverse gap before slicing gives exactly the four weighted kernel estimates.
The free reference estimate applies on the \(Z,W\) core with the actual scalar vacuum at \(Z\) and Haar noise.
Bounded polynomial approximations to the base letters converge in the inner-difference graph.
For fixed \(s<1\) the Neumann approximants to target words converge in both derivation graphs.
The inner spectral measure on the coarse tensor space is dominated by \(\mu^2\), so removal of the soft cutoff converges on each fixed target column.

For the final transfer \(S_s=p_s^*p_s\) converges boundedly strongly-star and its derivative converges in coarse norm, including all starred generator values in the product rule.
For a clipping function constant near \([0,1]\), its outer divided difference vanishes on \(\sigma(p^*p)^2\).
Uniform \(C^1\) polynomial approximation controls errors by the derivative error times \(\|\partial S_s\|_2\).
This proves graph convergence with column norms bounded in the limit by \(1+\epsilon\) and justifies the endpoint estimate even if the raw column norms fail to converge.
Taking adjoints replaces the base by \(Z^*\), its parameter by \(h^*\) and the free Haar input by \(W^*\).
The opposite right contraction therefore controls the original left contraction on single inputs by the flip-adjoint formula.
The two-contraction theorem gives both bounded-vector domains, and the product rule extends the commutator from the core to the closure domain by graph approximation.
Negating the closures gives the required generator-first sign.
For the converse, the strong adjoint-domain condition includes the vacuum and hence satisfies part C of the normal strong-domain theorem.

For area measure the scalar vacuum is \(2Z\).
Angular averaging at \(0<v<r\) gives \(1/(r^2-v^2)\), and substituting \(v=rt\) leaves \(r\,dr\) times a density comparable near zero to \(t^{1-\alpha}\) and near one to \(1-t\).
Both \(I\) and \(J\) are finite precisely for \(0<\alpha<2\), with logarithmic divergence at the threshold.
The normalized disk projections give squared errors \(r^2/2\) and \(4r^\alpha/(\alpha+2)\) for the two generators and the same for their adjoints.
Telescoping proves continuity of character evaluation for every \(\alpha>0\), while the radial chords in the \(Z\) spectrum supply the whole circle of limiting directions.
The review uses the seven established Claim results and the Task's definitions at the scopes indicated below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0290_v1.md#decision-candidate) | Original fixed candidate and the scope of its selected inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0290_v1.md#statement) | All parameters, both full-domain conditions, both vacuum norms, conditional law, generation and disk assertions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0290_v1.md#argument) | Whole proof, including the noncommutative order, singular limits, free estimates, conjugated orientation and example. |
| [Finding](#finding) | [Task definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred derivations, actual vacuum, bounded-vector domains and generator-first commutator. |
| [Finding](#finding) | [Conditional product densities](../../claims/Yin_C_F0281_v1.md#the-exact-row-and-column-norms) | Integrability of the conditional variance test in the base fibers of a normal generating pair. |
| [Finding](#finding) | [Free terminal estimate](../../claims/Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) | Ordered base insertions, scalar vacua and column estimate under the four bounded scalar Haar slices. |
| [Finding](#finding) | [Liberation recovery](../../claims/Yin_C_F0238_v1.md#statement) | Actual normal derivative from the marginal vacuum, descended liberation and its inverse-gap energy. |
| [Finding](#finding) | [Reference cutoff](../../claims/Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Finite free reference cost, uniform soft bound and graph transfer with normalized columns. |
| [Finding](#finding) | [Canonical domains](../../claims/Yin_C_F0072_v1.md#statement) | Canonical closure and Hilbert adjoint from the two contraction bounds on the represented core. |
| [Finding](#finding) | [Strong-to-actual implication](../../claims/Yin_C_F0070_v1.md#statement) | Part C for a normal generating pair with the vacuum in the adjoint domains. |
| [Finding](#finding) | [Area marginal](../../claims/Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Actual scalar vacuum for normalized disk area. |

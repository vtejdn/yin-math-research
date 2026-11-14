---
author: Yin
---

# Independent review of marginal domination at the semicircular coordinate

An independent reviewer for Yin examined the complete [candidate dated 2026-11-14T12:16](../../claims/Yin_C_F0259_v1.md#decision-candidate).
The reviewer received its locator and scope, had no role in developing the proof, and received no development dialogue, exploration notes, author explanations or earlier findings about this candidate.

## Finding

At 2026-11-14T12:19 UTC the reviewer found that the constructed pair has finite column cost at \(T\) and admits faithful ambient domination, while every probability density in \(L^1(W^*(T))\) fails domination on the stated mixed polynomial tests.
The following checks cover the entire candidate and the applicability of its three proved project inputs.

The radial density on \(D_0\) is \(2s\,ds\) before multiplication by its mixture weight.
It gives mean \(4/5\) for \(\sqrt{s}\), hence mean zero for \(b\) in the mixture and unit row mass for \(P=1+b\otimes b\).
On opposite disks \(P\) equals the value of \(m\) at the point in \(D_0\), while on each individual disk \(P\ge1\).
Thus \(P\ge m\otimes m\), with positive values off a null set, and \(\int m^{-2}\,d\mu=43/8\).
The local area integral of \(|z-v|^{-1}\) on a unit disk is \(2\pi\), giving the uniform bound \(9/4\) after adding the complement.
Absolute integrability allows the two terms of the scalar divided difference to be integrated separately and the endpoints exchanged, yielding the stated vacuum \(2\overline B\) with the inner product linear in the second variable.
The symmetric real coefficient \(\sqrt P\) consequently has unit row norm and full rank almost everywhere.
The first covariance integral is bounded by \((\int m^{-1}\,d\mu)^2\).
In the second, subtracting the edge probabilities gives \(b(w)(b(v)-b(z))\), whose squared modulus is at most \(4|z-v|\).
Splitting \((m(z)m(v))^{-1}\) by the arithmetic mean of the inverse squares then gives the stated upper bound \(4(9/4)(43/8)^2\).
The Gaussian criterion applies in the generated finite tracial algebra and supplies the actual starred vacua and both bounded-vector domains of the canonical duals.
The Gaussian column theorem applies to these same represented slices in each orientation, and the optimal-density theorem at \(T\) gives attainment by a faithful ambient density with the bounded rank-one commutator.

Successively integrating the squared path products gives norm one in every degree, and annihilation of their leftmost edge contributes the unit row integral.
The resulting three-term recurrence identifies \(U_n(T)\Omega\) with the unit path product in degree \(n\).
These vectors span the cyclic polynomial space and give zero expectation for \(U_n\) when \(n>0\).
Under \(t=2\cos\theta\), the proposed semicircular density gives the same moments by orthogonality of \(\sin\theta\) and \(\sin((n+1)\theta)\) on \([0,\pi]\).
The \(U_n\) span all polynomials, and both laws have compact support, so the moments identify the law.

For \(p=eTf\), the constant coefficient of \(p^*p=fTeTf\) in this cyclic space is \(A=\int eQf\,d\mu\).
For the coefficient of \(U_2\), the path inner product integrates \(P(z,w)P(w,v)f(z)e(w)f(v)\) over the three vertices, giving \(B=\int e(Qf)^2\,d\mu\).
Every other coefficient vanishes by orthogonality of the relative degrees.
Thus the trace-preserving conditional expectation is exactly \(A+B(T^2-1)\), bounded above by \(4A\) since \(0\le B\le A\) and \(T^2-1\le3\).
Pairing first with bounded truncations and using \(L^1\) convergence proves the same upper bound on \(\tau(wp^*p)\) for every marginal probability density, including unbounded densities.

For \(e=e_r,\ f=1_{D_1}\), direct integration gives \(A=(2q/5)\sqrt r\,\mu(e_r)\), where \(q=3/8\).
In particular this mixed moment is strictly below \(\mu(e_r)\mu(f)\), the free value for a centered semicircular \(T\) of variance one.
On a single edge the commutator has coefficient \((z-v)a(z,v)\), of positive squared integral since the diagonal is null and \(P>0\) almost everywhere.
Both nonfreeness and noncommutation follow.

Uniform boundedness and tracial \(L^2\) convergence of the real polynomial cutoffs give strong convergence of their left multiplications by testing first on bounded vectors.
The same argument applies to their adjoints, and multiplication by \(T\) preserves strong convergence for the uniformly bounded products.
This justifies testing \(p_n=u_nTv_n\) on the particular \(L^2\) vector \(\sqrt w\) for every fixed \(w\).
The forced normal derivative of \(Z^*\) at \(T\) vanishes, so the original right slice on these polynomials is \(u_n\tau(v_n)\), with limit \(q e_r\).
Consequently any uniform domination constant must satisfy \(q^2\mu(e_r)\le4C^2 A\le2qC^2\sqrt r\,\mu(e_r)\) for every positive \(r<1\).
Choosing \(r\) with \(2C^2\sqrt r<q\) makes the limiting inequality fail strictly, so an individual polynomial approximant violates the inequality for the proposed \(w,C\).
The project inputs were checked at the indicated interfaces using their selected proved decisions.
The review covers this example and its failure of marginal domination.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0259_v1.md#decision-candidate) | The complete candidate for the fixed two-disk law and its semicircular coordinate. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0259_v1.md#statement) | Actual ACSY and full strong domains, nonfreeness, finite column cost, attained ambient domination and failure for each marginal density on individual mixed polynomials. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0259_v1.md#argument) | All kernel and vacuum estimates, the semicircular law, the exact conditional square, approximation on the original core and the diverging constant. |
| [Finding](#finding) | [Gaussian criterion](../../claims/Yin_C_F0209_v1.md#statement) | Single positive real coefficient, row and rank conditions, scalar vacuum, both covariance integrals and intrinsic dual domains. |
| [Finding](#finding) | [Gaussian paths](../../claims/Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | Orthogonality of degrees, endpoint multiplication and the one-channel creation and annihilation actions. |
| [Finding](#finding) | [Gaussian columns](../../claims/Yin_C_F0241_v1.md#statement) | Item 1 applies to the actual intrinsic law and the adjoint tuple. |
| [Finding](#finding) | [Optimal density](../../claims/Yin_C_F0211_v1.md#statement) | Attainment by a faithful normal density and a bounded rank-one commutator for the same represented right slice. |
| [Finding](#finding) | [Normal starred derivatives](../../claims/Yin_C_F0076_v1.md#statement) | Item 1 forces the derivative of the other normal coordinate's adjoint to vanish on the polynomial core. |

---
author: Yin
---

# Independent review of oriented soft Cauchy cutoffs on a fixed planar pair

For Yin I examined the entire [candidate dated 2026-11-14T11:48](../../claims/Yin_C_F0253_v1.md#decision-candidate) and its direct inputs.
I took no part in developing the proof and received no author explanation, development dialogue, exploration notes or earlier finding about this candidate.

## Finding

At 2026-11-14T11:49 UTC I found that the proof establishes both lower bounds of (2) on the single stated correlated planar law and the exact cancellation and uniform full-cutoff column bound in (3).
The angular square-mean lower bound has a single mixed polynomial witness for each sufficiently small \(r\), with the law, represented derivations and vacua fixed throughout.

The vertical distribution function has limit zero at zero and value one at \(e^{-1}\).
Differentiation on the intervening open interval gives exactly \(1/(2y(\log(1/y))^{3/2})\), whose integral is one by the substitution \(s=\log(1/y)\).
The horizontal law \(dx/2\) is also normalized, giving positive planar density on the interior, full rectangular support, and zero mass on every affine line.
Scalar starred polynomials form a dense domain in \(L^2(\mu)\) by polynomial approximation of continuous functions on the rectangle.
Their divided difference is a well-defined bounded function off the product-null diagonal, satisfies the outer product rule, and takes value one at \(Z\).

Horizontal integration of \((h-i(y-y'))/(h^2+a^2)\), with \(a^2=(y-y')^2+r^2\) and horizontal probability weight \(1/2\), gives the coefficient \(1/4\) in the logarithm and imaginary part bounded by \(\pi/2\).
For \(r\le1\) the logarithm is uniformly controlled by \(C+|\log(1-|x|)|\), which belongs to \(L^2(dx/2)\), so integrating in \(y'\) gives the required uniform \(L^2(\mu)\) row bound.
Swapping \(z,w\) in the term containing \(f(w)\) gives the positive factor two by antisymmetry.
The regularized difference quotients converge to the actual divided difference with the Lipschitz constant of each fixed test as an integrable majorant.
Hence the double trace of its derivative is bounded for the input Hilbert norm on the dense polynomial domain, which puts the coarse vacuum in the domain of the actual Hilbert adjoint.

The one-channel coefficient \(a\in[1/2,3/2]\) is real and symmetric and represents the specified selfadjoint field by the endpoint actions.
Its row bound gives \(\|T\|\le3\), its inverse square is integrable, and in the second Gaussian integral the numerator \(Q/P-P/Q\) has size at most \(C|P-Q|\le C|z-v|/4\).
The scalar vacuum and full rank therefore give the actual starred and strong conditions for the intrinsic pair, and the Gaussian column theorem includes its adjoint orientation.
The shift by ten preserves the represented unital core and every normalized generator derivative, and \(B\ge7\).
The one-edge contraction gives \(\mathbb E_N(T^2)=(1+x/4)^2+1/48\) because \(\mathbb E x=0\) and \(\mathbb E x^2=1/3\).
In particular \(\tau(XT^2)=1/6\), while freeness of the two coordinate algebras would give \(\tau(X)\tau(T^2)=0\).
The first-chaos coefficient \((z-w)a(z,w)\) of \([Z,B]\) has strictly positive squared integral by diffuseness and the positive lower bound on \(a\).

For \(t=\log(1/r)\ge2\log16\), the sector \(|\theta|\le\pi/6\) admits the same region \(4r\le h=x-x'\le1/4,\ 0<y,y'\le r,\ |x|\le1/2\).
Here \(x'\in[-1,1]\), and \(\operatorname{Re}(e^{i\theta}\bar u)=h\cos\theta+(y-y')\sin\theta\ge h/2\).
The denominator is at most \(2h^2\), so the rotated real part of the soft kernel is at least \(1/(4h)\).
It is nonnegative throughout the entire selected half-plane, so the rest of the row cannot reduce this lower bound.
Horizontal integration with \(dx'/2\) and the vertical mass \(\sigma([0,r])=t^{-1/2}\) give \(R_r^\theta\) of modulus at least \((t-\log16)/(8\sqrt t)\ge\sqrt t/16\) on a set of probability \(1/(2\sqrt t)\).
It follows that its Hilbert norm is at least \(t^{1/4}/(16\sqrt2)\) uniformly in the sector.

For each fixed \(r>0\), the symbol \(m_\theta k_r\) is bounded by \(1/(2r)\).
The liberation values on actual core inputs give exactly \(E_r^\theta q=T_r^\theta q\) for marginal polynomials and \(E_r^\theta(Bq)=B T_r^\theta q\) by the outer product rule.
For \(f_N=e^{iNx}\), the subtracted term in \(T_r^\theta f_N\) is a Fourier coefficient at \(N\) of a bounded function of the horizontal integration variable after vertical integration at fixed \(z,\theta,r\).
It tends to zero pointwise, and the fixed-\(r\) majorant gives convergence to zero both at each angle in \(L^2(\mu)\) and in \(L^2(d\mu\,d\theta/(2\pi))\).
The term \(f_N R_r^\theta\) has exactly the row norm in either space for every \(N\).
Uniform approximation by the complex polynomial \(q_N(x)\) introduces at most \(1/(rN)\) in the sliced difference uniformly in \(\theta\), using differences of two input values and the kernel bound.
Since \(X=(Z+Z^*)/2\), \(Bq_N(X)/26\) is an actual represented starred polynomial of norm at most one.
Left multiplication by \(B\) has Hilbert lower bound seven, valid without commuting \(B\) with the marginal output.

The sector occupies \(1/6\) of the angular probability measure.
The row lower bound thus gives \(7t^{1/4}/(26\cdot16\sqrt{12})\) as a lower bound for the limit inferior of the sector norms of these mixed inputs.
For example, reducing this constant by a factor two gives a single polynomial at sufficiently large \(N\) witnessing the full angular inequality for each fixed \(r<1/256\).
The separate fixed-angle supremum has at least the larger lower bound with \(\sqrt2\) replacing \(\sqrt{12}\).
The argument takes \(N\) large after fixing \(r\) and uses one input at a time for the whole angular integral.

For each fixed \(\theta\), the exceptional equality \(\operatorname{Re}(e^{-i\theta}(z-w))=0\) is null by the affine-line property and Fubini.
Domination of the spectral measure of every coarse vector by \(\mu^2\) therefore makes the two opposite projections add to the identity on the entire coarse space.
The full regularization bound in the inverse-gap theorem gives \(\sup_{r>0}c(E_r)\le3c(C\delta_i)\) at this actual law.
The angular mean of the vectors exists by bounded joint measurability on each fixed cyclic spectral space and equals \(E_rp/2\) by pairing opposite angles.
The growth conclusion is a lower bound for one-sided truncations, with the tested sector and order of limits specified above.
The established Gaussian and cutoff results were checked at the precise interfaces below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0253_v1.md#decision-candidate) | The single planar pair with both cutoff inequalities and opposite-orientation identity. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0253_v1.md#statement) | Probability law, correlation, actual derivations and domains, column costs, common-input angular estimate and full-cutoff cancellation. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0253_v1.md#argument) | Scalar adjoint by uniform row control, Gaussian criterion, two-dimensional positive sector, polynomial witnesses and opposite masks. |
| [Finding](#finding) | [Gaussian covariance criterion](../../claims/Yin_C_F0209_v1.md#statement) | Intrinsic one-channel pair, row norm, rank and both integrals, actual starred and strong conditions. |
| [Finding](#finding) | [One-edge representation](../../claims/Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | Endpoint action and contraction for the conditional second moment and noncommutation. |
| [Finding](#finding) | [Gaussian column bounds](../../claims/Yin_C_F0241_v1.md#statement) | Part 1 for all canonical right columns of the intrinsic pair and of its adjoint tuple. |
| [Finding](#finding) | [Liberation and full soft cutoff](../../claims/Yin_C_F0238_v1.md#statement) | Actual inner-difference prescription, zero derivative of the omitted field and equation (2) for the radius-uniform full column bound. |
| [Finding](#finding) | [Inner coarse measure class](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination for the exceptional angle boundary on the whole coarse space. |

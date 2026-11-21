---
author: Yin
---
# Biquadratic rank failure in the regular representation

## Whole finding

At 2026-11-21 05:33 UTC an agent outside the development of C104 v2 independently inspected its complete [statement](../../claims/Yin_C_A0104_v2.md#statement) and [argument](../../claims/Yin_C_A0104_v2.md#argument) for Yin.
The reviewer received the fixed Claim and the points to scrutinize, without exploration notes, development dialogue, author explanations or a prior verdict on v2.
The earlier [review of the Galois divisor](Yin_R_A0141_v1.md#whole-finding) was consulted for the v1 input.
The four conditions are equivalent under the stated rational rank hypothesis on \(G^2\), and the two exclusions and the normalizer calculation hold for the indicated nonzero pairs.

For the biquadratic field \(K\), the [Galois divisor and rank calculation](../../claims/Yin_C_A0104_v1.md#statement) give \(s^2\mid[K:K\cap D]\mid4\) and ranks in \(s^{-1}\mathbb Z\).
Thus a nonintegral rank forces \(s=2\), and \(s=2\) forces \(K\cap D=\mathbb Q\).
Applying the same result to the degree-two field \(\mathbb Q(\alpha)\) makes \(L=D[\alpha]\) a division ring.
When \(K\cap D=\mathbb Q\), the central element \(\alpha\notin D\) gives the basis \(1,\alpha\).
If the scalar \(\beta\) were in \(L\), the automorphism fixing \(D\) and negating \(\alpha\) would take \(\beta\) to \(\beta\) or \(-\beta\), since its image lies in the center and squares to \(b\).
The corresponding eigenspaces are \(D\) and \(D\alpha\), respectively.
Either case puts a nonrational scalar from \(K\) in \(D\).
Consequently evaluation has kernel exactly \((T^2-b)\) in \(L[T]\), since a linear remainder vanishing at \(\beta\) would put \(\beta\) in \(L\).
The left Euclidean algorithm makes this quotient a division ring if the central quadratic is irreducible.
Indeed every nonzero class then has a left inverse, which is two-sided by finite-dimensionality.
A monic proper factorization has factors \(T+w,T-w\), and their nonzero classes have zero product exactly when \(w^2=b\).
The coefficients of \(w=u+\alpha v\) then give the two equations of condition 3, and the only available nondivision case is \(M_2(V)\).

The [square test](../../claims/Yin_C_A0096_v2.md#the-square-test-for-a-scalar-affiliated-element) makes every element of \(D\) algebraic over \(\mathbb Q\) scalar.
If either coordinate vanishes under condition 3, this puts \(\pm\beta\) or \(\pm\beta/\alpha\) in \(K\cap D\).
Conversely, a nontrivial intersection contains \(\alpha,\beta\) or \(\alpha\beta\), since these generate the three quadratic subfields.
If \(\alpha\in D\), then \(w\in D\) with \(w^2=b\) is scalar, so \(u=w-\alpha v\) commutes with \(v\), forcing \(uv=0\).
If \(\alpha\notin D\), either \(\beta\in D\) or \(\beta=(\alpha\beta/a)\alpha\in D\alpha\), so \(\beta\) is central in \(L\).
The factorization of \(w^2-b\) in this division ring yields \(w=\pm\beta\), with one of its two coordinates zero.
This verifies the replacement of the intersection hypothesis by nonvanishing of both coordinates.

Under condition 3, \(\beta\notin L\) makes \(e=(1+w/\beta)/2\) a nontrivial idempotent in \(M_2(V)\).
Its image and kernel split \(V^2\) into lines, so conjugacy with a diagonal matrix unit gives \(\dim eU(G)=1/2\).
Indeed the diagonal units generate isomorphic right modules whose direct sum is \(U(G)\).
Since \(\beta-w=2\beta(1-e)\), its right annihilator consists exactly of the elements \(x=ex\), and hence has the dimension of the analytic kernel projection.
Realizing \(u,v\) as entries of inverses over the actual affiliated algebra follows from the [fixed-ambient rational closure](../literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures).
Writing \(Q=\operatorname{diag}(Q_1,Q_2)\), \(B=(l_1,\alpha l_2)\) and \(C=\binom{r_1}{r_2}\), block elimination gives the top entry \(\beta-BQ^{-1}C=\beta-u-\alpha v\).
The lower block \(Q\) is invertible, so the finite square matrix over \(K[G]\) has nullity \(1/2\) and nonintegral rank with the unnormalized matrix trace.

For nonconstant \(u=f(g)\) and \(v=q(h)\), the spectral projections of \(u^2=b-av^2\) belong to both cyclic subgroup algebras.
Their intersection is the von Neumann algebra of \(H=\langle g\rangle\cap\langle h\rangle\), since the Fourier coefficients of an element in the intersection vanish off \(H\).
If \(H\) is trivial, \(f(T)^2\) is constant by the Haar law, contradicting nonconstancy.
If \(H=\langle g^m\rangle=\langle h^n\rangle\), the \(m\)-th root rotation fixes \(f(T)^2\), and the integral domain \(\mathbb C(T)\) forces the rotation to multiply \(f(T)\) by a single sign.
The power basis over \(\mathbb C(T^m)\) then puts \(f(g)\) in \(g^i\mathbb C(g^m)\), with \(i=0\) or, for the negative sign, \(i=m/2\).
The same argument applies to \(q(h)\), since \(h^n=g^{\pm m}\).
The two rational factors in the common generator are units commuting with \(g\) and \(h\).
After cancellation the anticommutator would vanish in the group ring, although its augmentation is two.

For \(J=N_G(\langle g\rangle)\), conjugation induces a map to \(\{1,-1\}\) with kernel \(C_G(g)\).
In the nontrivial quotient choose an inverting representative \(s\).
The sign automorphism has bounded fixed algebra \(\mathcal N(C_G(g))\) by Fourier support.
An affiliated fixed operator has its polar partial isometry and all spectral projections of its absolute value in this fixed algebra.
Consequently splitting into sign eigenspaces gives \(v=d_0+d_1s\) with unique coefficients affiliated with \(\mathcal N(C_G(g))\).
The even equation kills \(d_0\), since the nonzero \(f(g)\) is invertible and central in that affiliated algebra.
Now \(d_1=vs^{-1}\) is invertible, so the odd equation forces \(f(T^{-1})=-f(T)\).
Multiplying \(d_1s\) by itself gives the stated norm \(d_1(sd_1s^{-1})s^2\) with precisely this order of factors.
Conversely the inversion and norm identities give both equations, with membership of \(u,v\) in \(D\) and the scalar intersection checked separately for condition 3.
If the quotient is trivial, \(f(g)\) commutes with every such \(v\).
The argument covers the normalizer and gives no obstruction on the rest of a larger commensurator.

Finally, \(t=v^2\) is nonscalar, since the factors \(v-\lambda\) at the two square roots of a putative scalar \(t\) are units by the square test.
The [single-generator result](../../claims/Yin_C_A0096_v2.md#one-rational-affiliated-generator) therefore applies at \(t\).
If both powers are group monomials, \(c^2g^2=(b-at)^m\) and \(e^2h^2=t^n\) commute and are algebraically dependent in \(\mathbb C(t)\).
Their orders at \(b/a\) and \(0\) force both exponents of any multiplicative relation modulo scalars to vanish.
Thus \(g^2,h^2\) generate a copy of \(\mathbb Z^2\), whose distinct basis elements in \(\mathbb C[G]\) preclude that algebraic dependence.
These conclusions leave unrestricted rational affiliated pairs unresolved.
The cited [quaternion construction](../../claims/Yin_C_A0102_v1.md#statement) uses a different trace and supplies no example for the regular representation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0104_v2.md#statement) | All four conditions under rational integrality on the square, the nonzero-pair formulation, both exclusions and the normalizer criterion. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0104_v2.md#argument) | The quadratic tower and scalar intersections, affiliated half-nullity witness, cyclic rotations, normalizer cosets and independence of group monomials. |
| [Whole finding](#whole-finding) | [Galois divisor](../../claims/Yin_C_A0104_v1.md#statement) | Actual scalar intersections, the matrix-ring index and regular rank denominators for the quadratic and biquadratic fields. |
| [Whole finding](#whole-finding) | [Square test](../../claims/Yin_C_A0096_v2.md#the-square-test-for-a-scalar-affiliated-element) | Scalar translates of nonscalar elements of the rational division closure are affiliated units. |
| [Whole finding](#whole-finding) | [One generator](../../claims/Yin_C_A0096_v2.md#one-rational-affiliated-generator) | Faithful rational evaluation at the nonscalar \(v^2\). |
| [Whole finding](#whole-finding) | [Matrix inverses](../literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures) | Realization of both elements of the actual division closure as entries of inverses of rational group-ring matrices. |

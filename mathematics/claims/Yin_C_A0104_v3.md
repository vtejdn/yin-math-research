---
author: Yin
---
# A cyclic coefficient and its anticommuting partners in the regular representation

## Statement

Let \(g\) have infinite order in a discrete group \(G\), put \(H=\langle g\rangle\), and fix a nonconstant rational function \(f\in\mathbb C(T)\).
Write \(u=f(g)\) in the affiliated algebra \(U(G)\) of the regular representation.
The poles of \(f\) on the unit circle have Haar measure zero.
For \(\varepsilon\in\{1,-1\}\) define a union \(S_\varepsilon\) of double cosets \(HxH\) as follows.

* Form the subgroup of \(\mathbb Z^2\) consisting of the pairs \((i,j)\) for which \(g^i x=xg^j\).
  If it is nonzero, write its generator as \((m,n)\) with \(m>0\).
* Include the double coset in \(S_\varepsilon\) exactly when \(n=\eta m\) for some \(\eta=\pm1\) and there is a root of unity \(\zeta\), \(\zeta^m=1\), with
  \[
                   f(\zeta T^\eta)=\varepsilon f(T)
                   \quad\text{in }\mathbb C(T).
                   \tag{1}
  \]
  A double coset with trivial subgroup is excluded.

For every bounded \(T_0\in\mathcal N(G)\) satisfying \(uT_0=\varepsilon T_0u\) as affiliated operators, its group Fourier coefficients vanish off \(S_\varepsilon\).
Conversely every label in \(S_\varepsilon\) occurs with nonzero coefficient in a finite group-ring intertwiner over \(\mathbb C\), and even over \(\mathbb Q\) if \(f\in\mathbb Q(T)\).
For an arbitrary affiliated solution \(v\) of \(uv=\varepsilon vu\), the same assertion holds for every bounded truncation \(v1_{[0,N]}(|v|)\).
In particular, if \(f\) has no sign-reversing symmetry (1) with a root of unity and either exponent, even an affiliated anticommuting partner must be zero.

Now assume that \(G\) is torsion-free, rational strong Atiyah holds on \(G^2\), and \(D=\operatorname{Div}_{U(G)}(\mathbb Q[G])\).
Let \(a,b\in\mathbb Q^\times\) have independent square classes, and suppose \(u=f(g)\in D\).
If an integral character \(\chi:G\to\mathbb Z\) vanishes on \(g\) and is odd at every element of \(S_{-1}\), then there is no nonzero \(v\in D\) such that
\[
                         uv+vu=0,\qquad u^2+a v^2=b.
                         \tag{2}
\]
This tests an unrestricted rational partner for a prescribed cyclic input in the [biquadratic criterion](Yin_C_A0104_v2.md#statement).
The Klein bottle group below has bounded measurable solutions of (2) in its canonical regular representation even though this character excludes every rational partner for that input.

## Argument

### Fourier analysis on a double coset

Realize \(L^2(\mathcal N(G))=\ell^2(G)\) with the group basis.
Left and right multiplication by \(g\) are commuting unitaries that act on a double coset by \((i,j)\cdot x=g^i x g^j\).
If \(g^i x=xg^j\) and either exponent is zero, both vanish.
The subgroup in the definition of \(S_\varepsilon\) therefore projects injectively onto each coordinate of \(\mathbb Z^2\), so it has the indicated cyclic form or is trivial.
Changing \(x\) to \(g^k xg^\ell\) leaves this subgroup unchanged.
With generator \((m,n)\), the stabilizer for the left and right action is \(\mathbb Z(m,-n)\).
Fourier transformation on the discrete group \(\mathbb Z^2/\mathbb Z(m,-n)\) identifies \(\ell^2(HxH)\) with the Haar \(L^2\)-space of
\[
                        \{(z,w)\in\mathbb T^2:z^m=w^n\}.
                        \tag{3}
\]
The two unitaries become multiplication by \(z,w\), respectively.
For a trivial stabilizer the compact group is the whole torus.

Choose \(\lambda\in\mathbb C\) outside both \(f(\mathbb T)\) and \(\varepsilon f(\mathbb T)\), taking the images in the Riemann sphere to include poles.
These images have empty interior since a rational map on the circle traces finitely many smooth arcs in sphere coordinates.
The two resolvents \(A=(u-\lambda)^{-1}\) and \(B=(\varepsilon u-\lambda)^{-1}\) are bounded normal operators.
The affiliated intertwining relation for \(T_0\) gives \(AT_0=T_0B\) by multiplying by these inverses.
On each Fourier space above its \(L^2\)-vector is consequently supported where
\[
                   (f(z)-\lambda)^{-1}=(\varepsilon f(w)-\lambda)^{-1}.
\]
Outside a Haar-null set of poles this is exactly \(f(z)=\varepsilon f(w)\).
On the whole torus the equality locus has measure zero by Fubini, since each fiber of a nonconstant rational function is finite.

For (3), put \(q=\gcd(m,|n|)\).
The group has \(q\) circle components parametrized, up to fixed phases \(z_0,w_0\), by \(z=z_0 t^{n/q}\), \(w=w_0t^{m/q}\) for \(t\in\mathbb T\).
Indeed the primitive relation specifies one connected circle and the possible \(q\)-th roots of unity in \(z^{m/q}w^{-n/q}\) label its translates.
Haar measure restricts to a multiple of circle Haar measure on each component.
Positive measure of the equality locus forces the two rational functions of \(t\) to agree identically on that component.
Their degrees as maps of the Riemann sphere are \((\deg f)|n|/q\) and \((\deg f)m/q\), so \(|n|=m\).
In this case the components are \(w=\zeta z^\eta\), \(\zeta^m=1\), \(\eta=n/m\).
The equality then gives (1), proving the claimed support inclusion for \(T_0\).

Conversely take a label \(x\) and a component \(w=\zeta z^\eta\) that satisfies (1).
The finite group-ring element
\[
              T_x=\frac1m\sum_{i=0}^{m-1}\zeta^{\eta i}\,g^i xg^{-\eta i}
\]
has Fourier transform on (3) equal to the indicator of this component, by summing the finite geometric series in \(\zeta^\eta z w^{-\eta}\).
The \(m\) group labels in the sum are distinct by minimality of \(m\), so the coefficient at \(x\) is \(1/m\).
Its Fourier transform gives \(AT_x=T_xB\) in \(L^2\) and hence as bounded operators by faithfulness.
Multiplying by the affiliated inverses of the two resolvents gives \(uT_x=\varepsilon T_xu\).
If \(f\in\mathbb Q(T)\), every Galois conjugate of \(\zeta\) over \(\mathbb Q\) satisfies (1).
Summing the finite intertwiners over these conjugates gives rational coefficients and a positive coefficient at \(x\).
The second equation of (2) is an additional requirement on an anticommuting partner.

### From affiliated identities to bounded truncations

For a closed affiliated \(v\) the equality \(Av=vB\) still holds in \(U(G)\).
The operator \(vB\) on its natural domain is closed since \(B\) is bounded, and the closed product \(Av\) extends its value on \(\operatorname{dom}v\).
Thus \(B\operatorname{dom}v\subset\operatorname{dom}v\), with \(vB\xi=Av\xi\) there.
The graph of \(v\) is invariant under the bounded normal operator \(N_0=\operatorname{diag}(B,A)\).
Its orthogonal projection \(P\) belongs to \(M_2(\mathcal N(G))\) by affiliation.
In this finite tracial algebra the invariant projection reduces \(N_0\).
Indeed the block form relative to \(P,1-P\) is upper triangular, and the \(P\)-diagonal block of \(N_0N_0^*=N_0^*N_0\), followed by the trace, makes the squared \(L^2\)-norm of the upper off-diagonal block zero.

The graph entries \(P_{11}=(1+v^*v)^{-1}\) and \(P_{21}=v(1+v^*v)^{-1}\) therefore satisfy \(BP_{11}=P_{11}B\) and \(AP_{21}=P_{21}B\).
For \(e_N=1_{[0,N]}(|v|)\), the bounded operator \((1+|v|^2)e_N\) is a bounded Borel function of \(P_{11}\) and hence commutes with \(B\).
Multiplying the second graph identity on the right by this function gives \(A v e_N=v e_N B\).
The preceding Fourier argument applies directly to this bounded resolvent identity.
Since \(v e_N\to v\) in measure, empty \(S_\varepsilon\) forces \(v=0\).
The support assertion concerns ordinary Fourier coefficients of bounded operators and does not require coefficients of an unbounded operator to be defined.

### An integral character excluding a rational partner

We may suppose \(S_{-1}\ne\varnothing\).
Dividing \(\chi\) by the positive generator of its image preserves oddness on \(S_{-1}\), because that generator divides an odd value.
Write \(G_0=\ker\chi\) and choose \(s\in G\) with \(\chi(s)=1\) after this normalization.
On the regular group algebra the sign character defines a trace-preserving automorphism \(\theta(x)=(-1)^{\chi(x)}x\), \(x\in G\).
It extends to \(\mathcal N(G)\) and \(U(G)\) by conjugation by the diagonal sign unitary on \(\ell^2(G)\).
Each bounded truncation of an anticommuting \(v\) has support in \(S_{-1}\), and thus changes sign under \(\theta\).
Taking the limit in measure gives \(\theta(v)=-v\).

Write \(D_0=\operatorname{Div}_{U(G_0)}(\mathbb Q[G_0])\).
Subgroup restriction of the regular representation preserves affiliated inverses and ranks, so \(D_0\subset D\) and both rings are division rings under the rational hypothesis.
Use the [skew Laurent construction](Yin_C_A0036_v1.md#an-abelianized-norm-obstruction-and-the-limit-of-integer-valuations) for this rational coefficient field.
For clarity, if \(\delta(d)=sds^{-1}\), then \(D_0[s^{\pm1};\delta]\) embeds in \(D\).
In fact the powers of \(s\) are linearly independent even over \(U(G_0)\).
For a finite sum, the common left multiplier \((1+\sum_i d_i d_i^*)^{-1/2}\) is an affiliated unit making all coefficients bounded.
The resulting bounded terms have disjoint group Fourier supports in \(G_0s^i\).
As all nonzero skew Laurent polynomials are units in \(D\), their Ore division ring of fractions embeds in \(D\) and contains \(\mathbb Q[G]\).
Minimality of the division closure gives equality with \(D\).

In particular
\[
                             D\cap U(G_0)=D_0.
\]
Indeed write \(y\) in this intersection as a right fraction \(P_0Q_0^{-1}\) in the skew Laurent ring.
In \(yQ_0=P_0\), uniqueness of coefficients over \(U(G_0)\) gives \(yq_i=p_i\) at any nonzero coefficient \(q_i\) of \(Q_0\).
Thus \(y=p_iq_i^{-1}\in D_0\).
This intersection argument uses the cyclic quotient selected by \(\chi\).

Expand fractions in the skew Laurent series ring \(D_0((s;\delta))\).
Such expansions exist by factoring off the lowest monomial of each nonzero denominator and inverting its remaining positive-degree tail by a geometric series.
The lowest exponent \(\nu\) is an additive valuation on products of nonzero elements, since the product of twisted leading coefficients is nonzero.
Here \(\theta\) fixes \(D_0\) and sends \(s\) to \(-s\), so \(\theta(v)=-v\) for \(v\ne0\) forces \(\nu(v)\) odd by comparing leading coefficients.
But (2) puts \(v^2=(b-f(g)^2)/a\) in \(D\cap U(G_0)=D_0\) because \(g\in G_0\).
This nonzero element has valuation zero, in contradiction with \(\nu(v^2)=2\nu(v)\).
The intersection calculation allows even a cyclic rational expression with complex coefficients, provided its prescribed value \(u\) actually belongs to \(D\).

### A measurable solution in the Klein bottle group

Let \(G=\langle g,h\mid hgh^{-1}=g^{-1}\rangle=\mathbb Z\rtimes\mathbb Z\) with its canonical trace, and set \(u=g-g^{-1}\), \(a=2\), \(b=3\).
The subgroup \(H\) is normal, and \(x=g^i h^j\) has \(m=1\) and \(\eta=(-1)^j\) in (1).
Since \(f(T)=T-T^{-1}\) changes sign under inversion, \(S_{-1}\) consists exactly of the odd \(h\)-cosets.
The character \(\chi(g)=0,\ \chi(h)=1\) is odd on all of them.

Here the necessary rational division property can also be verified directly for \(G\) and \(G^2\).
For \(P=G\) or \(G^2\) the product of the subgroups \(\langle g,h^2\rangle\) in its coordinates gives a normal free abelian subgroup \(A_0\) of finite index.
The group algebra \(\mathbb Q[P]\) is a domain by successive skew Laurent extensions from the free abelian group generated by the \(g\)-coordinates, adjoining the \(h\)-coordinates one at a time.
For a nonzero \(x\in\mathbb Q[P]\), left multiplication is injective on the finite free right \(\mathbb Q[A_0]\)-module \(\mathbb Q[P]\).
Its matrix has nonzero determinant over the commutative fraction field by clearing denominators in any proposed kernel vector.
The determinant is therefore a nonzero Laurent polynomial and vanishes on a Haar-null subset of the torus of \(A_0\).
The coset representation makes \(x\) an affiliated unit in \(U(P)\).
Every nonzero element of \(\mathbb Q[A_0]\) has a central multiple given by the product of its finitely many conjugates under \(P/A_0\).
Inverting all nonzero invariant elements of \(\mathbb Q[A_0]\) therefore puts its whole fraction field in the localized group ring inside \(U(P)\).
This localization is still a domain and is finite-dimensional on the right over that fraction field, using coset representatives and normality of \(A_0\).
Left multiplication by any nonzero element is then a bijection on this finite-dimensional space, so the localization is a division ring.
It contains \(\mathbb Q[P]\), and all inverted elements already have inverses in the actual division closure, proving equality.
Gaussian elimination now gives integer ranks for finite rational group-ring matrices in both powers.

On the other hand \(u^*=-u\), so \(c=((3-u^2)/2)^{1/2}\) is a positive bounded unit.
The unitary \(h\) changes the sign of \(u\) and commutes with \(c\).
The unitary \(h^2\) is central, so choose any Borel function \(q\) on the circle with \(q(z)^2=z^{-1}\) and put
\[
                             v=c\,h\,q(h^2).
\]
The last factor is a central unitary, \(h q(h^2)\) is an involution, and consequently \(uv=-vu\) and \(v^2=(3-u^2)/2\).
Thus \(u,v\in\mathcal N(G)\) solve (2) with the canonical group representation.
The valuation argument excludes \(v\) and every other nonzero partner for this particular \(u\) from \(D\).
This example distinguishes a measurable solution from the rational affiliated solution required for the [finite matrix of nullity one half](Yin_C_A0104_v2.md#a-finite-matrix-with-half-dimensional-kernel).

## Assessment history

### Decision cyclic-partners

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:15 |
| status | proved |
| reason | The independent finding checks the Fourier criterion, affiliated truncations, skew valuation and the two kinds of partners in the same representation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Support of signed cyclic intertwiners, the rational character test and the explicit measurable Klein bottle example. |
| argument | [Proof](#argument) | Double-coset support, label realization, bounded truncation, parity and the Klein bottle calculation. |
| review | [Whole finding](../audits/reviews/Yin_R_A0141_v3.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Biquadratic criterion](Yin_C_A0104_v2.md#decision-biquadratic-equations) | Actual rational inputs required for the rank-failure application. |
| dependency | [Skew Laurent argument](Yin_C_A0036_v1.md#decision-prime-index-witness) | Faithful grading construction used for the integral-character valuation. |
| dependency | [Division closure criterion](Yin_C_A0096_v1.md#decision-alternating-coefficients) | The rational division-ring criterion after restriction. |

## Current assessment

[Selected decision](#decision-cyclic-partners)

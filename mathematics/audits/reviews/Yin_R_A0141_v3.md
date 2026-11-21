---
author: Yin
---
# Fourier support and the integral-character obstruction for a cyclic coefficient

## Whole finding

At 2026-11-21T05:40 UTC an agent outside the development of C104 v3 independently reviewed its full [statement](../../claims/Yin_C_A0104_v3.md#statement) and [argument](../../claims/Yin_C_A0104_v3.md#argument) for Yin.
The reviewer received the fixed claim and the questions to check, without exploration notes, proof-development dialogue, author explanations or an earlier verdict on v3.
The [earlier review](Yin_R_A0141_v2.md#whole-finding) was consulted for the biquadratic criterion in v2.
The Fourier support characterization, the passage to bounded truncations, the rational obstruction and the regular Klein bottle example all hold under their stated hypotheses.

On \(\ell^2(HxH)\), right multiplication by \(g\) sends the group vector at \(y\) to the vector at \(yg\).
Consequently \((m,-n)\) fixes \(x\), and the two multipliers \(z,w\) satisfy \(z^m=w^n\).
Both coordinate projections have Haar circle law, so the poles of \(f\) can be discarded for both coordinates.
The resolvents at the chosen \(\lambda\) are bounded because the two circle images in the sphere are compact and omit \(\lambda\).
Their equality on the support of the Fourier vector is equivalent there almost everywhere to \(f(z)=\varepsilon f(w)\).
On the full torus each fiber of this equality is finite.
On a circle component of the proper subgroup, equality on a set of positive measure implies equality of the two rational maps of the parameter, whose degrees are \(\deg(f)|n|/\gcd(m,|n|)\) and \(\deg(f)m/\gcd(m,|n|)\).
Thus \(|n|=m\), and the accepted components are exactly those in (1).

For each such component the ratio \(\zeta^\eta z w^{-\eta}\) is an \(m\)-th root of unity everywhere on the compact subgroup and equals one precisely when \(w=\zeta z^\eta\), for either sign of \(\eta\).
Its average over the powers from \(0\) to \(m-1\) is the component indicator.
The inverse transform has coefficient \(1/m\) at the specified \(x\), since a second summand at \(x\) would give a stabilizer exponent strictly between \(0\) and \(m\).
Equality of the two bounded resolvent products in \(L^2\) is equality in the von Neumann algebra by faithfulness of the trace, so inverting the resolvents in \(U(G)\) recovers the desired relation.
For \(f\in\mathbb Q(T)\), averaging over the conjugates of \(\zeta\) preserves this relation and the nonzero coefficient at \(x\), and makes all coefficients rational.

For affiliated \(v\), \(vB\) on its natural domain is closed, and equality with the closure of \(Av\) places \(\operatorname{dom}v\) in \(\operatorname{dom}(vB)\).
This gives invariance of the graph under \(\operatorname{diag}(B,A)\).
Writing this normal operator in upper triangular form relative to the graph projection, normality gives \(aa^*+dd^*=a^*a\) on the graph for the upper row \((a,d)\).
Faithfulness and traciality force \(d=0\).
The graph therefore reduces the diagonal operator, and the two stated identities for \(P_{11}\) and \(P_{21}\) follow.
The bounded Borel multiplier of \(P_{11}\) equals \((1+|v|^2)1_{[0,N]}(|v|)\), giving the same resolvent relation for \(v1_{[0,N]}(|v|)\).
These truncations converge in measure since the trace of the omitted spectral projection tends to zero.

For the character obstruction, normalization by the positive generator of the image divides by an odd integer when \(S_{-1}\) is nonempty.
The sign automorphism acts as minus one on every truncation by its Fourier support, and conjugation by the sign unitary preserves convergence in measure.
The rational rank hypothesis restricts from \(G^2\) to \(G\) and \(G_0=\ker\chi\) by the regular coset decompositions with the same trace.
The fixed-group division-closure criterion thus applies to both torsion-free groups.
Clearing finitely many affiliated left coefficients by the common multiplier in the claim gives bounded terms on disjoint cosets, proving independence of the Laurent powers even over \(U(G_0)\).
The skew fraction field of \(D_0[s^{\pm1};\delta]\) embeds into \(D\), and its being a division subring containing \(\mathbb Q[G]\) gives the reverse inclusion.
For \(y\in D\cap U(G_0)\), the right fraction identity \(yQ=P\) gives \(yq_i=p_i\) coefficient by coefficient, with \(q_i\ne0\) for at least one \(i\).
It follows that \(y\in D_0\).
The sign automorphism fixes \(D_0\) and multiplies the coefficient of degree \(j\) in the Laurent series by \((-1)^j\).
A nonzero odd element must therefore have odd least exponent, also for negative exponents.
Its square has twice that exponent, whereas \((b-f(g)^2)/a\), if equal to that square, is a nonzero element of \(D_0\) with exponent zero.
This argument uses the actual rational division closure even when \(f\) is presented with complex coefficients.

For \(G\) the Klein bottle group, the normal form \(g^ih^j\) gives precisely the odd \(j\) as sign-reversing double cosets.
For \(P=G,G^2\), the successive skew Laurent extensions are domains and the finite-index abelian subgroup makes left multiplication by a nonzero rational group-ring element a matrix over a Laurent polynomial ring.
Its injectivity on the free module implies nonzero determinant over the fraction field and invertibility almost everywhere on the torus, hence affiliated invertibility.
Localizing at the nonzero central invariants inverts each nonzero Laurent polynomial through its orbit product.
The resulting domain is finite-dimensional on the right over the abelian fraction field, so every nonzero left multiplication is bijective.
This gives the actual rational division closure, in which matrix elimination yields integer regular ranks.
Finally \(3-u^2\ge3\), and \(h\) fixes \(u^2\) while negating \(u\).
The Borel square root of \(z^{-1}\) at the central unitary \(h^2\) makes \(h q(h^2)\) an involution commuting with \(c\).
Both equations follow for the indicated bounded unit \(v\).
The obstruction excludes rational partners for this prescribed \(u\), leaving the existence question for other inputs to the biquadratic criterion open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0104_v3.md#statement) | Both signs, realizability of each label with complex or rational coefficients, affiliated truncations, the integral-character exclusion and the canonical example. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0104_v3.md#argument) | The complete argument from the double-coset spectral decomposition to the bounded measurable solution and exclusion of every rational partner for its prescribed cyclic input. |
| [Whole finding](#whole-finding) | [Skew Laurent construction](../../claims/Yin_C_A0036_v1.md#an-abelianized-norm-obstruction-and-the-limit-of-integer-valuations) | Applicability of the faithful integer grading and fraction-field argument to the rational coefficient field. |
| [Whole finding](#whole-finding) | [Fixed-group division-closure criterion](../../claims/Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings) | The torsion-free rational criterion used after restricting ranks to the indicated subgroups. |
| [Whole finding](#whole-finding) | [Biquadratic criterion](../../claims/Yin_C_A0104_v2.md#statement) | The requirement that both coordinates belong to the actual rational division closure in the application to nonintegral rank. |
| [Whole finding](#whole-finding) | [Half-dimensional kernel](../../claims/Yin_C_A0104_v2.md#a-finite-matrix-with-half-dimensional-kernel) | The rational input requirement distinguishing that earlier matrix construction from the measurable solution in v3. |

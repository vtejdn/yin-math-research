---
author: Yin
---

# Review of the two marginal tests and the two-block estimate

## Finding

At 2026-11-14T13:42 UTC an agent outside proof development independently checked the whole [C_F0271 v1 candidate](../../claims/Yin_C_F0271_v1.md#decision-candidate), including its explicit vacuum-adjoint hypothesis for every coordinate, and all four declared dependency interfaces.
The reviewer received the candidate and the review scope without exploration notes, proof-generation discussion or previous findings about this candidate.
The proof establishes (1)–(5), the equivalence with an exact density on the original core, and the estimate on the stated span of bounded inputs.

Pairing the derivative of \(a^*p\) with the joint vacuum gives \(Ta=a\xi-(F(a^*))^*\).
For a marginal test \(a\), the second term is \(JE_BJa\), since the scalar divided difference is symmetric.
The two terms in \(Ta=T_Ba+a\eta\) lie in orthogonal marginal and mean-zero subspaces.
In particular the variance contribution to the two real identities uses \(\mathbb E_B(\eta\eta^*)\), with this order following from the trace of \(\eta^*f^2\eta\).
The scalar energy identity therefore gives exactly (1), also at \(f^2\).

The two defects sum to the integral of \(\kappa(z,w,s)^2|z-w|^2/4\), equal to the squared-sine integral by the sine rule and diffuseness.
With \(a(s)=\int k(z,s)\,d\mu(z)\) and \(c=\int a\,d\mu\), the conditional squared difference of the two unit phases gives \(2D=1-\|a\|_2^2\).
The two centered one-coordinate projections of \(k-c\) have equal squared norm \(\|a\|_2^2-|c|^2\) and are orthogonal in the product law.
Their sum has squared norm at most \(1-|c|^2\), which yields \(4D\ge1-|c|^2\).
For \(c\ne0\), choose the line through the mean with direction \(\phi\) satisfying \(e^{-2i\phi}=c/|c|\), and for \(c=0\) take any direction.
The independent-difference formula then bounds the transverse variance by \(d^2(1-|c|)/4\).
The minimum transverse variance is attained and vanishes precisely for support on a line.
Faithfulness identifies that support with the spectrum.
Polarizing the proposed full-core identity at \(1,f^2\) forces both defects to vanish because \(T1=\xi\).
Conversely, an affine rotation to a selfadjoint generator preserves the represented core, changes the distinguished slice and adjoint by unimodular factors, and preserves all other generator and vacuum conditions.
The selfadjoint-coordinate density thus gives the claimed full-core identity on that line.

In the marginal projection formula the trace pairing moves the correlation term to \(p\eta^*\).
The scalar slice is closable because its adjoint contains the dense scalar core.
Polynomials approximate \(\mathbb E_Bp\) in the finite measure \((1+W)\mu\), giving convergence in the original graph by the scalar slice bound.
Conditional Schwarz with truncated weights bounds its weighted input by \(\|p\sqrt W\|_2\).
The other term has norm at most \(\|p\eta^*\|_2\), yielding the asserted column density with \(\eta^*\eta\).

For each finite list in \(N\), testing (4) on squared linear combinations with complex rational coefficients gives the two matrix bounds on a single full-measure set.
Continuity permits evaluation at the varying scalar coefficient vectors.
Hence \(U(n\otimes a)=na\) has closed range \(K\) and \(mI\le G=U^*U\le M_0I\).
Right multiplication by \(B\) reduces \(K\) and intertwines \(U\), so its bounded multipliers commute with \(G\).
In the vacuum pairing for \(a^*n^*p\), the derivative of \(n^*\) vanishes, and contraction of \((\delta_i a^*)n^*\) against the first trace gives \(F(a^*)n^*\).
Taking the adjoint leaves the order \(nJE_BJa\) in (6).
For \(h=U^{-1}P_Kp\) and \(s=\min(\sqrt W,t)\), the inequality \(G^2\le M_0G\) gives \(\|sGh\|^2\le M_0\|P_K(ps)\|^2\le M_0\|ps\|^2\).
The limit places \(Gh\) in the joint unweighted and weighted Hilbert tensor space required for the scalar adjoint pairing.
The scalar bound for \(JT_BJ\) contributes \(\sqrt2\), and \(\|u\|\le m^{-1/2}\|Uu\|\) then gives exactly \(\sqrt{2M_0/m}\) in (5).
Squaring and summing gives the stated coefficients for each finite column.

Bounded strong-star approximation by omitted polynomials preserves zero derivative for \(n,n'\).
Multiplying these approximants on the two sides of a fixed \(a\) gives graph convergence to \(nan'\), since bounded strongly convergent outer multipliers converge on the fixed vector \(\delta_i a\).
In the right slice, the second leg of \(\delta_i a\in L^2(B)\otimes L^2(B)\) is integrated against \(\mathbb E_B n'\), leaving an \(L^2(B)\) vector multiplied on the left by \(n\).
The resulting output belongs to \(K\), which proves the full-output assertion on the specified span.
The two-block estimate on general core inputs controls their projection onto \(K\) under (4).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0271_v1.md#decision-candidate) | Fixed candidate dated 2026-11-14T13:38 and its four direct dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0271_v1.md#statement) | All-coordinate actual vacua, both marginal energies, two-test rigidity, projected and two-block constants, and the full-output input span. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0271_v1.md#argument) | Complete proof through the conditional phase variance, affine change, weighted scalar graph, ordered Gram comparison, tensor duality and graph approximation. |
| [Finding](#finding) | [Normal starred symbols](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, the scalar divided difference, closability and both omitted generator symbols under the actual vacuum hypothesis. |
| [Finding](#finding) | [Scalar energies and bounds](../../claims/Yin_C_F0267_v1.md#statement) | Real scalar identities, integrability of \(W,g\), and the two complex weighted bounds used in (1), (3) and (5). |
| [Finding](#finding) | [Selfadjoint distinguished coordinate](../../claims/Yin_C_F0266_v1.md#statement) | One positive integrable density for the full-core adjoint square after translating and rotating the distinguished generator. |
| [Finding](#finding) | [Omitted-coordinate algebra](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Zero derivative and outer multiplication in the actual graph for bounded omitted coefficients, including both sides of \(nan'\). |

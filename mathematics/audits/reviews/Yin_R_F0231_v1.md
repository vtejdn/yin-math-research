---
author: Yin
---
# Independent review of column bounds for the first cyclic output spaces

## Whole-proof finding

At 2026-11-13T16:07 UTC a reviewer outside this proof's development checked the whole [statement](../../claims/Yin_C_F0223_v1.md#statement) and [argument](../../claims/Yin_C_F0223_v1.md#argument) of the candidate dated 2026-11-13T16:00.
The reviewer had previously encountered the omitted-coordinate result and worked on a separate nonnormal branch of the Task.
The reviewer received the fixed candidate and its designated inputs without the candidate's draft, development discussion, author explanations or a prior review of its proof.
Both projected estimates hold, with the unconditional two-occurrence conclusion for the specified unstarred inputs.

The omitted-coordinate polynomial core has derivative zero for both \(\delta\) and \(\epsilon\).
Kaplansky approximation of the real and imaginary parts by uniformly bounded selfadjoint elements gives strong-star approximants for arbitrary bounded coefficients in \(N\), including \(\mathbb E_NX_i\).
On the tracial Hilbert space both left and right multiplications from such nets converge strongly, and they converge strongly on their respective outer tensor legs by density of elementary tensors and the uniform bounds.
This proves the graph product rule for \(y^*p\) by taking the product of the coefficient nets with the stipulated approximating net for \(p\).
It also puts every word in the asserted span of \(N,NxN,NxNxN\) in the stated bounded graph class.

For \(y=axb\) and \(K=c\otimes d\) the differentiated factor \(y^*\) gives \(b^*d^*\otimes c^*a^*\).
Its trace pairing after right multiplication by \(p\) is \(\tau(a^*pc^*)\tau(b^*d^*)\), which equals the pairing with \((p\otimes1)\Phi(K)^*\) in that order, using the opposite second factor.
By continuity in \(K\) this applies to the true tensor, whose adjoint in the opposite-algebra model is unitary by the marginal phase formula.
The other product-rule term pairs \(y\) with \(Ep\), and the adjoint vacuum term is \(\langle y,p\xi^*\rangle\) by traciality.
For \(y=qx\) the resulting correction pairs \(q\) with \(V_p\), which is exactly \(\langle qh^{1/2},V_p h^{-1/2}\rangle\) by \(L^2\)-\(L^2\) tracial cycling.
The partial isometry vanishes on its kernel and maps the regular component of \(qx\) onto \(qh^{1/2}\).
Density thus gives the identity on the whole first cyclic space, including its kernel summand.
Testing against the omitted algebra gives zero correction and centering gives the orthogonality of the two spaces.
Conditional Schwarz bounds \(\sum_jV_{p_j}^*V_{p_j}\) by \(\|\sum_jp_j^*p_j\|1\), so the correction has column norm at most \(\|h^{-1/2}\|_2\|\sum_jp_j^*p_j\|^{1/2}\).
The other term costs at most \(\|\xi\|_2\|\sum_jp_j^*p_j\|^{1/2}\), proving the first estimate with the cited inverse-density bound.
On \(axbxd\) the two unstarred cuts give \(a\tau(bxd)+axb\,\tau(d)\).
The first vanishes by \(\mathbb E_N x=0\), and the second belongs to \(NxN\), establishing the full-slice assertion on these inputs.

In the spatial tensor algebra let \(k=\Phi(\bar\delta x^*)\).
Symmetry of the marginal phase in its two variables gives \(\Phi(\bar\epsilon x)=k^*\), so \(K_0=k\).
For \(y=qx+rx^*\) the derivative values are \(q+rk\) and \(qk^*+r\).
With \(Ty=q+rk\), the two conjugated vacuum functionals on \(y\) are \(\langle Ty,1\rangle\) and \(\langle Ty,k\rangle\).
Indeed \(\tau_{\mathcal B}((q^*+k^*r^*)k)=\tau_A(tq^*+r^*)\), using tracial cycling and \(kk^*=1\).
Consequently both projected vacua annihilate the kernel of the closed restriction \(T\) by graph continuity.
Opposite-side unitary actions preserve this restricted graph and its defining core in both directions.
The final space of the polar isometry reduces the normal left action of \(A\) on \(L^2(\mathcal B)\), which supplies the required normal action on \((\ker T)^\perp\).
This justifies bounded approximation of \(A\)-coefficients in pairings with the two projected vacua even when the full cyclic space has a singular summand.

Moving algebraic coefficient adjoints onto \(y\) gives coefficients \(a+tb\) of \(q^*\) and \(t^*a+b\) of \(r^*\).
The order agrees with the left action and with the positive block matrix whose upper-right entry is \(t\).
The phase gap makes the inverse norm at most \((1-\|t\|)^{-1}\).
Applying its square bound to the column \((V_{p_j},U_{p_j})^{\mathsf T}\), and then conditional Schwarz to its two entries, gives \(\sum_j(a_{p_j}^*a_{p_j}+b_{p_j}^*b_{p_j})\le 2(1-\|t\|)^{-2}\|\sum_jp_j^*p_j\|1\).
Each projected vacuum has norm at most \(\|\xi\|_2\), yielding the asserted constant after the direct-sum triangle inequality, with the omitted-algebra projection contributing zero to the correction.
In both cases orthogonal decomposition of each column entry proves the finiteness equivalence for the complementary outputs.
The review used the cited source interfaces at their recorded scope and did not re-audit the proof of Kaplansky density.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0223_v1.md#statement) | Both projected estimates, graph class, two unstarred occurrences and complementary-output equivalences. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0223_v1.md#argument) | Endpoint and phase conventions, inverse-density pairing, polar normality, matrix order, constants and graph limits. |
| [Whole-proof finding](#whole-proof-finding) | [Normal derivatives](../../claims/Yin_C_F0076_v1.md#statement) | Closability, actual reversed vacuum, symmetric unitary marginal phase and the opposite-algebra adjoint. |
| [Whole-proof finding](#whole-proof-finding) | [Omitted-coordinate graph](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Vanishing on all omitted coefficients, graph intertwining and centering. |
| [Whole-proof finding](#whole-proof-finding) | [Cyclic polar data](../../claims/Yin_C_F0217_v1.md#polar-decomposition-and-the-integrable-inverse-density) | Partial isometry and kernel, pointed \(h^{1/2}\), inverse-density estimate and normal action on the polar support. |
| [Whole-proof finding](#whole-proof-finding) | [Bounded strong approximation](../literature/AP18/Yin_U001.md#ap18-u001) | Selfadjoint Kaplansky nets for both parts of a coefficient and uniformly bounded strong-star approximation. |
| [Whole-proof finding](#whole-proof-finding) | [Full column cost](../../claims/Yin_C_F0208_v1.md#statement) | Represented full-core column norm with denominator \(\|\sum_jp_j^*p_j\|^{1/2}\). |

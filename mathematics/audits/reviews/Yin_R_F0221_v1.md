---
author: Yin
---
# Independent review of vacuum and bounded-dual costs for the noisy Jordan block

## Whole-proof finding

At 2026-11-13T14:05 a separate agent outside proof development inspected the [statement](../../claims/Yin_C_F0213_v1.md#statement) and [argument](../../claims/Yin_C_F0213_v1.md#argument) fixed in the November 13 candidate.
The reviewer received the fixed proof and review scope and consulted its four declared inputs and the Task definitions.
No development dialogue, author explanation or earlier finding about the candidate was supplied or consulted.
All four assertions hold, including the equivalence for \(k=2\) with the stated lower-limit condition.

For \(R=r(u)^*\), the two orders of right deletion and prepending \(u\) agree on every nonempty Fock word, while \(R\ell(u)\Omega=\Omega\) and \(\ell(u)R\Omega=0\).
Prepending \(v\) has zero vacuum contribution, and left and right deletions commute even on one-letter words.
The two intrinsic commutators therefore have signs \(+P_\Omega\) and zero, respectively.
In the pointed free product the lift has the same norm as \(R\) and commutes with the matrix left action.
For the circular left action the intrinsic commutator is supported on the vacuum plus the single circular syllable, where its nonzero part is supported only on the vacuum.
Compression to \(L^2(W^*(Z))\) preserves these identities because this subspace reduces both left multipliers and contains the vacuum.
The resulting \(E_0\) kills \(1\), has norm at most \(\varepsilon^{-1}\), and its restriction has this same upper bound from the algebra norm to the Hilbert norm.

The operator representing an elementary cut \(a\otimes b\) has output vector \(a\) and input functional \(h\mapsto\langle b^*,h\rangle\).
Evaluation of the commutator between vacuum vectors thus gives \(\langle E_0^*1,p\rangle\) for \(d_x\).
Taking operator adjoints gives the positive \(Z^*\)-commutator for \(U=-E_0^*\).
The contribution from \(U1\) is \(-\tau(p\,U1)\), which verifies the second vacuum \(U^*1-(U1)^*\).
For either cut, expanding \(\delta(apb)\) pairs \(a^*\otimes b^*\) against \(\delta p\).
The two error terms pair \(\delta a\) and \(\delta b\) against \(1\otimes(pb)^*\) and \((ap)^*\otimes1\), respectively.
Their norms are controlled by \(\|p\|_2\) times the stated bounded multipliers.
The middle pairing from the adjoint vacuum on \(apb\) is likewise continuous in \(\|p\|_2\), so the whole tensor core belongs to the adjoint domain and both cuts are closable.

Circular Fock degree counts all circular letters across reduced syllables.
Matrix multiplication can cancel a matrix syllable but cannot increase this count, and one circular left multiplier increases it by at most one.
In the top degree of a word of length \(m\) only its all-circular, all-creation choice survives, yielding its specific tensor of \(u,v\) with coefficient \(\varepsilon^m\).
Projection onto this degree separates the terms of largest length in any polynomial relation.
The algebraic tensor of the resulting injective evaluation maps is injective, also in the Hilbert tensor completion.
The coefficient of \(a\otimes b\) in the \(y\)-cut recovers the coefficient of \(ayb\), so the polynomial kernel is exactly the analytic polynomials.

The phases of \(J\) can be implemented by \(\operatorname{diag}(1,e^{-it},\ldots,e^{-(k-1)it})\), which extends together with the circular rotation to the trace-preserving free-product rotation.
This gives orthogonality of analytic powers and zero traces in positive degree.
Only the monomial \(x\) among analytic monomials has nonzero scalar \(x\)-cut, with value one.
It follows that the projection of every vacuum onto the analytic closure is \(Z/\|Z\|_2^2\), with \(\|Z\|_2^2=(k-1)/k+\varepsilon^2\).
Inserting \(g\otimes h\) at a \(y\)-cut \(a\otimes b\) contributes \(\tau(ag)\tau(hb)=\langle g^*\otimes h^*,a\otimes b\rangle\).
The formula extends continuously in the tensor, which verifies the componentwise adjoint and the positive sign of the freely chosen term.
The desired difference of functionals annihilates the polynomial kernel, and its factor on each finite-degree image has a Riesz representative there.
Choosing its componentwise adjoint imposes all of the degree-bounded tests simultaneously.

For \(y^{k-1}x^k\), every \(y\)-cut at zero noise has a right factor containing \(J^k\).
In the scalar \(x\)-cuts all terms before the final cut have a positive remaining power of \(J\) with zero trace.
The final cut leaves \((J^*)^{k-1}J^{k-1}=e_{kk}\) on the left.
Polynomial norm continuity with \(k\) fixed makes both the word and its \(y\)-cut \(O_k(\varepsilon)\), whereas its scalar \(x\)-cut tends to \(1/k\).
This forces the claimed starred-value lower bound in every degree \(n\ge 2k-1\), since the prescribed vacuum functional on the test has norm bounded by \(\sqrt{2}\|r(Z)\|_2\).

The commutator on the bounded powers gives \(E(Z^j)=Z^jE1+Z^{j-1}\) for every \(j\ge1\), by the zero positive analytic moments.
For \(j=k\), the two terms involving \(E\) cost at most \(2\|E\|\|Z^k\|_\infty\) in total.
The first-order coefficient of \(Z^k\) has norm at most \(2k\), and \(Z^{k-1}\) converges in norm to \(e_{1k}\), of tracial Hilbert norm \(1/\sqrt{k}\).
These yield the lower-limit constant \(1/(4k^{3/2})\) even with \(E1\) unrestricted.

Finally, algebraic freeness makes every \(K\) a legitimate starred value on the core.
Its scalar pairing has an actual Hilbert representative exactly when \(K^\sharp\in\operatorname{Dom}T^*\), because the adjoint of the closable core operator equals the adjoint of its closure.
The attainable set is precisely \(\xi_0+\operatorname{Ran}T^*\).
Its distance to zero is \(\|P_{\ker T}\xi_0\|_2\), and convergence of analytic polynomials in \(H\) gives graph convergence with second coordinate zero.
If the scaled distance tends to zero along a sequence, one can choose actual vacua of norm below \(d_2(\varepsilon)+1\), so their scaled norms also tend to zero while \(\varepsilon\beta\) has positive lower limit.
Conversely \(\varepsilon d_2\le(\varepsilon\beta)(\|\xi\|_2/\beta)\) and \(\varepsilon\beta\le1\).
This proves the sequence criterion, and the cutoff-free implication in the declared ratio theorem applies directly to those actual vacua.
The identification of the polynomial kernel supplies only the inclusion of the analytic closure in the closed kernel.
The lower limit in (1) and the existence of a separating tuple from these laws remain unresolved.
The free-product source was used at the recorded end-action identity and the ratio theorem at its proved implication.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0213_v1.md#statement) | Both actual cuts, holomorphic vacuum projections, finite-degree tests, bounded-dual costs and the conditional separation criterion. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0213_v1.md#argument) | All four proof sections, including domains, cost lower bounds, the affine attainable set and both directions of the sequence condition. |
| [Whole-proof finding](#whole-proof-finding) | [Circular Fock construction](../../claims/Yin_C_F0074_v1.md#argument) | Orthonormal complex creation letters, norm-one right deletion, operator-first commutators and normalization. |
| [Whole-proof finding](#whole-proof-finding) | [Free-product end actions](../literature/Voi98/Yin_U005.md#voi98-u005) | Cross-factor commutation and localization of the same-factor commutator to the embedded factor Hilbert space. |
| [Whole-proof finding](#whole-proof-finding) | [Starred-value word cuts](../../claims/Yin_C_F0201_v1.md#argument) | Componentwise adjoint and outer-action pairing for the freely chosen starred value. |
| [Whole-proof finding](#whole-proof-finding) | [One-generator ratio criterion](../../claims/Yin_C_F0210_v1.md#statement) | Unbounded ratios for actual vacua at arbitrary finite cutoffs imply a length-two counterexample. |
| [Whole-proof finding](#whole-proof-finding) | [Task hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual adjoint on the represented star core and bare generator-first dual obtained by negating the operator-first convention. |

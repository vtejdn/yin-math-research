---
author: Yin
---

# Independent review of the semicircular mixed-word test

At 2026-11-14T11:28 UTC, an agent outside the development of the argument reviewed the [candidate fixed at 2026-11-14T11:25](../../claims/Yin_C_F0249_v1.md#decision-candidate) for Yin.
The initial review used the fixed statement, full proof, cited literature units and graph-vacuum Claim.
The reviewer received no substantive development dialogue, exploration notes, author explanations or earlier findings on this candidate.
The literature units were used for their cited conventions and semicircular basis, and the established graph-vacuum theorem was used at its stated scalar scope.

## Finding

All three assertions hold with the stated normalizations.
The divergence is witnessed within the two stated operator balls.
The square-sum bound holds for the inverse secant of each fixed graph.

**Mixed derivative and trace.**
In the semicircular orthonormal basis \(u_j\), the generating function \(F_s(z)=(1-sz+z^2)^{-1}\) obeys \((F_s-F_t)/(s-t)=zF_s F_t\).
Comparing coefficients for \(v_n=(u_n-u_{n-2})/2\) gives the two anti-diagonals with indices \(n-1\) and \(n-3\).
The rank-\(n\) reversal \(J_n\) pairs with their difference with trace \(n\), because its product with \(J_{n-2}\) has zero diagonal.
Thus \(B_n=(J_n-J_{n-2})/4\) has rank at most \(n\) and nuclear norm at least \(n/4\).
The same lower bound holds for the full mixed derivative since \(f\mapsto T f(S)\) is an isometry from \(L^2(\mu)\) into \(L^2(M)\) by freeness and \(\tau(T^2)=1\).
Using \(T/2\) in the first leg hence scales the singular values of \(O_{H_n}\) by \(1/2\), including when the second-leg space is enlarged from the marginal to \(L^2(M)\).
Only the \(u_0\) term survives the right trace, so the squared output norm is \((1/16)\|u_{n-1}-u_{n-3}\|_2^2=1/8\), including \(n=3\).
The test has \(\|T\|_2=1\) and the column has norm at most \((\|T\|/2)\|v_n(S)\|\le1\).

For a bounded product symbol, freeness evaluates the first trace as \(\tau(T^2 u_i(S)v(S))/2=\int u_i v\,d\mu/2\).
Boundedness of \(H_n\) at each fixed \(n\) makes the double integral continuous for \(L^2(\mu^2)\) approximation of a general bounded symbol.
In the operator trace the second kernel is evaluated with arguments reversed, and it is real symmetric.
The second-linear convention therefore gives exactly \(\operatorname{Tr}(O_K B_n)\), with no conjugation of \(K\).

**Heat and weak trace-class tests.**
Gaussian averages of the stated conjugations give the graph multiplier on Hilbert–Schmidt kernels for every Lipschitz constant of \(g\).
Unital complete positivity puts each column variance of a contraction between zero and the identity by the Schwarz inequality, and the same bound holds for its adjoint.
The graph map has first coordinate \(s\), hence it separates every pair \(s\ne u\).
For each fixed \(n\), dominated convergence applied to the squared kernel of \(J_n\) gives decay in Hilbert–Schmidt norm and therefore in the required weak-star sense.
The source BMO convention applies to these tests via this decay and the verified variance formula.
Evaluating their traces gives \(n/4\).
On the \(n\)-dimensional support of \(D_n\), reversal is unitary, so \(J_nD_n\) has singular values \(1/k\), \(1\le k\le n\), and weak trace-class quasinorm one for the ordinary operator trace.
Its trace after multiplication by \(J_n\) is \(\sum_{k=1}^n1/k\).
Multiplication by \(J_{n-2}\) gives zero diagonal.
The finite polynomial kernels realize both witnesses within the domain of the trace pairing, so their growth already excludes a degree-independent bound over the indicated balls.

**Fixed inverse secant.**
The scalar semicircle has actual conjugate vector \(S\), as the double trace of \(\partial_Su_j\) is one only for \(j=1\) and is zero for the other basis elements.
C_F0244 applies in the one-coordinate algebra to every stated real Lipschitz \(g\).
The graph polynomial \(v_n((y+\bar y)/2)\) pulls back to \(v_n(s)\) and its scalar divided difference equals \(K_hH_n\) off the diffuse diagonal.
The adjoint identity with \(\xi_h\) consequently gives the coefficient difference \((d_n-d_{n-2})/4\).
Each shifted sequence has \(\ell^2\) norm at most \(\|\xi_h\|_2\) by Bessel's inequality and the isometry of pullback along \(h\).
Their difference thus gives the squared bound \(\|\xi_h\|_2^2/4\) after division by \(16\).
The estimate applies to all degrees simultaneously for that graph and the chosen words and Hilbert test.
The uniform column problem for arbitrary mixed words remains open under this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0249_v1.md#statement) | Normalized mixed column, tensor nuclear norm, trace pairing, two endpoint witnesses and square-sum bound for each fixed graph. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0249_v1.md#argument) | Complete proof from the two Chebyshev anti-diagonals through the heat variances, weighted reversal and scalar vacuum coefficient estimate. |
| [Finding](#finding) | [Semicircular Wick basis](../literature/Miy22/Yin_U001.md#miy22-u001) | Free variance-one normalization and real orthonormal monic basis, with project inner-product convention applied in the mixed pairing. |
| [Finding](#finding) | [Graph heat variance](../literature/CJSZ20/Yin_U001.md#cjsz20-u001) | Column and row variance definitions and large-time decay convention. The proof constructs the needed semigroup directly on \(B(H)\). |
| [Finding](#finding) | [Weak trace-class convention](../literature/CSZ18/Yin_U001.md#csz18-u001) | Singular-value convention specialized to finite rank for the ordinary trace, with the endpoint used for comparison. |
| [Finding](#finding) | [Lipschitz graph vacua](../../claims/Yin_C_F0244_v1.md#statement) | Item 3 for the scalar semicircle with its actual conjugate vector, supplying the represented scalar graph vacuum identity. |

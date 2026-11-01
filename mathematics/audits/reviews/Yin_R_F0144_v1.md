---
author: Yin
---
# Independent review of C3 spectral-graph invariance of full-domain conditions

Review performed and recorded: 2026-10-14T17:39.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0137 v1](../../claims/Yin_C_F0137_v1.md).
Root supplied the fixed candidate and the review obligations.
The candidate's author self-check was visible, but no author D material, proof-generation discussion or informal explanation was read.
The reviewer read the complete fixed candidate selected by its initial decision dated 2026-10-14T17:32 and the exact six direct dependency interfaces.
The reviewer had earlier independently reviewed C_F0075 and C_F0076; their unchanged accepted statements are reused only at the scopes identified below, not as evidence that this new assembly is valid.

This is an initial whole-proof review of the five-way equivalence and the actual canonical-domain conclusion.
It covers the C3 extensions and both Fourier estimates, actual exponential and tensor-adjoint graph domains, graph-valued Bochner integration, the projective correction and its actual adjoint, the different polynomial cores, all full-M commutator passages, and the complete implication chain.
No freeness, analytic extension of g, unrestricted normal-spectral theorem, or equality of holomorphic rational fields is inferred.

The selected project/source inputs remain accepted at their recorded inspection boundaries.
The elementary periodic Fourier estimates are reconstructed below from Parseval and Cauchy-Schwarz, including dimension and extension hypotheses.
No new original-PDF or recursive predecessor-proof inspection is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0137 statement](../../claims/Yin_C_F0137_v1.md#statement) | Exact C3 real graph hypotheses, normality and generation, equivalence of A(X), A(S), F(S), F(X), S(X), and both actual domains of the specified canonical X contractions. |
| [Conclusion](#conclusion) | [C_F0137 argument](../../claims/Yin_C_F0137_v1.md#argument) | Complete Fourier summability, actual multiplier-adjoint/Bochner proof, projective correction and adjoint series, all coordinate-change implications, and final canonical identification. |
| [Conclusion](#conclusion) | [C_F0069 Part A](../../claims/Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness for each supplied bare normal dual and its normalization; no Hilbert boundedness or adjoint premise is inferred. |
| [Conclusion](#conclusion) | [C_F0070 Parts A and C](../../claims/Yin_C_F0070_v1.md#statement) | Actual normal starred commutators on all bounded vectors under F(X), and actual vacuum/derivation existence from the subsequently available strong-domain system. |
| [Conclusion](#conclusion) | [C_F0076 Part 1](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, closability and the unique normal starred phase under A(X), used to derive delta_i(S_j)=delta_ij K_i. Its second-derivative and coassociativity results are not used. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Selfadjoint actual canonical contractions and their adjoints on M, with both operator-norm-to-H estimates; no bounded-H assumption is added. |
| [Conclusion](#conclusion) | [C_F0071 Part B](../../claims/Yin_C_F0071_v2.md#statement) | Exact equivalence F(S) iff A(S) for the selfadjoint generating tuple, including actual joint vacuum rather than merely marginal data. |
| [Conclusion](#conclusion) | [C_F0075 Part 4](../../claims/Yin_C_F0075_v1.md#statement) | Actual canonical operator and adjoint full-M domains for normal X after S(X) is established, with normalization compatibility and no identification of an arbitrary bare system. |

## Coordinate setting and phase calculation

For each coordinate, S_i commutes with its selfadjoint functional calculus g_i(S_i), so X_i is normal.
The exact identity S_i=(X_i+X_i*)/2 proves W*(X)=W*(S)=M and P_S contained in P_X.
Both are dense starred cores, but they need not be equal.
No inclusion of S in the unstarred rational field of X is used.

Write f(s)=s+i g(s).
Its real part is s, so f is injective on the real interval.
The real divided difference h=g^[1] is well-defined even on the diagonal through the integral formula in (G2).
It is C2 on a slightly larger real square because each derivative of total order at most two differentiates g' at most twice.
It is real, so J=1+i h has real part 1 and K=1/J is C2 with modulus at most 1 there.

Under A(X), C_F0076 Part 1 supplies the actual normal phase and diffuse laws.
Pulling the phase back along f gives

\[
k_X(f(s),f(t))=\frac{1-i h(s,t)}{1+i h(s,t)}.
\]

Consequently delta_i(S_j)=delta_ij(1+k_X)/2=delta_ij K_i.
The same calculation applies to the full-M starred commutators from C_F0070 under F(X).
The diagonal has product measure zero whenever these hypotheses hold, and the continuous J,K formulas are already defined there.
These interfaces do not assume a joint free law.

## C3 and two-dimensional Fourier estimates

The open-interval hypothesis provides a positive margin around the compact I.
A smooth cutoff supported inside that open interval and equal to one on a neighborhood of I converts g into a compactly supported C3 function.
Place its support inside a larger period interval and extend periodically.
It is zero near the period endpoints, so no endpoint jumps in derivatives are introduced.
A degenerate chosen I can first be enclosed in a nondegenerate interval within the same open domain.

For the resulting periodic function, Parseval applied to the third derivative yields sum n^6 abs(c_n)^2 finite, up to the fixed frequency scaling.
Cauchy-Schwarz with the one-dimensional summable sequence n^-2 gives sum n^2 abs(c_n) finite; the zeroth mode and low frequencies are harmless.
This proves (G3), and in particular uniform absolute convergence of the function and first derivative series.
Integrating that first derivative on the line segment from t to s gives (G4), including on the diagonal.
Its rank-one exponential factors have norm one, and the projective norm is bounded by the summable coefficient series sum abs(n omega c_n).

The inverse K is defined and C2 on a larger real square, since J does not vanish there.
Choose a smooth two-variable cutoff equal to one near I squared and supported inside that square.
After zero extension and periodic repetition on a larger rectangle, this is a C2 function on a two-dimensional torus.
It need not remain an inverse outside the spectral rectangle, which is irrelevant to the subsequent operator identities.

Parseval for derivatives of order at most two bounds the Fourier coefficients in the weighted square sum with weight (1+m squared+n squared) squared.
In dimension two the reciprocal square weight has a finite sum: shell counting gives a tail bounded by a constant times sum r^-3.
Cauchy-Schwarz therefore proves the absolute coefficient sum (G5).
The resulting uniformly convergent Fourier series represents the same L2 function; continuity makes it equal pointwise to the periodic extension, hence exactly to K on the full spectral rectangle.
This supplies a discrete projective expansion in bounded unitary exponentials without requiring a holomorphic inverse theorem or a general multiplier lifting result.

The two estimates have distinct roles.
The n squared weight for J controls the later adjoint graph norm.
The two-dimensional unweighted absolute sum for K controls both the full-domain operator correction and its adjoint correction.

## Actual exponential domains and the tensor-adjoint formula

Assume A(X) and fix its i-th derivation delta with vacuum xi.
On polynomials in S_i, its derivative is the scalar divided difference times K_i.
For exp(i alpha S_i), choose polynomials approximating that function and its first real derivative uniformly on the interval.
For example, uniform polynomial approximation of the derivative followed by integration gives this elementary one-variable C1 approximation.
The divided-difference kernels then converge uniformly, and hence in the coarse Hilbert norm.
Since abs(K_i) is at most 1, their limit has norm at most abs(alpha).
These are graph approximants in the original P_X domain because P_S is contained in P_X.
Closability therefore gives the actual original closed derivative and (G7), and the same reasoning applies to adjoints.

For original-core a,b, put R=(id tensor tau)delta and L=(tau tensor id)delta.
Expanding the actual vacuum pairing of a* p b*, for every p in the original P_X, gives

\[
\delta^*(a\otimes b)
=a\xi b-(L(a^*))^*b-a(R(b^*))^*.
\]

The factor orders follow directly from the outer actions.
This formula bounds the norm by norm(a) norm(b) norm(xi)_2 plus norm(delta(a*))_2 norm(b) plus norm(a) norm(delta(b*))_2.
It is an actual adjoint pairing on the whole original domain, not merely on P_S.

For the polynomial approximants to exponential a,b, uniform function convergence makes the vacuum product term Cauchy in H.
The two derivative-slice terms are Cauchy because the derivatives converge in the Hilbert tensor norm and the other multipliers converge uniformly.
Thus the adjoint vectors converge in H.
Closedness of the original delta* puts a tensor b in its domain with the same formula and bound.
Taking the functions to be unitary exponentials gives exactly norm(xi)_2+abs(alpha)+abs(beta).
This also proves continuity in the adjoint graph norm on compact frequency sets, since the function and divided-difference kernels vary continuously there.

## Bochner integration proves the actual J-multiplier vacuum

The inner map I_(a tensor b)(u tensor v)=u a tensor b v is bounded on the coarse Hilbert space and commutes with the outer actions.
Its Hilbert adjoint is I_(a* tensor b*).
Thus I_J*(1 tensor 1)=conjugate(J), with the ordinary conjugation in the abelian marginal tensor algebra; it is not a swapped-leg assertion.

For each Fourier mode in (G4), the parameter theta maps continuously into the graph of the original delta*, by the preceding exponential graph estimate.
Bochner integration of the pair consisting of tensor and adjoint value remains in this closed linear graph.
Its norm bound is abs(n) omega abs(c_n) times (norm(xi)_2+abs(n) omega).
This is summable by (G3).
The same estimates apply to conjugated coefficients and negative frequencies.
Hence the constant term and conjugated series converge in that actual graph to conjugate(J), proving its membership in Dom delta*.

It follows that theta_i=I_Ji delta_i restricted to P_S has actual vacuum delta_i*(conjugate(J_i)).
The map is an outer derivation and its S-coordinate values are the required Kronecker values because I_J K=1 tensor 1 on the marginal spectral rectangle.
Density of P_S makes this the exact A(S) condition.
A merely bounded tensor multiplier was never assumed to preserve an adjoint domain; the weighted Fourier graph estimate supplies the needed domain statement explicitly.

## Projective correction and its actual adjoint series

For one term rho(a) E rho(b), right multipliers preserve the domain M and commute with every left element.
On bounded elementary tensor factors,

\[
\rho(a)\Theta(u\otimes v)\rho(b)
=\Theta(u a\otimes b v).
\]

This follows by traciality in the rank-one pairing and extends to arbitrary coarse tensors by Hilbert-Schmidt continuity.
Hence the inner-action order in (G11) is correct.

If E is operator-norm-to-H bounded on M, the norm of rho(a)E rho(b) as such a map is at most norm(a) norm(E) norm(b).
The projective expansions therefore converge in B(M,H).
The J expansion is treated by the analogous operator-norm Bochner integral, whose integrands are continuous in theta.
The commutator identities pass through those sums or integrals in B(M,H), while the tensor side converges in the Hilbert-Schmidt norm.
No Hilbert-space boundedness of E is used.

When E and its actual adjoint both contain M and their restrictions have the stated bounds, fix q in M.
Testing each term against every p in M gives the actual adjoint value

\[
\rho(b^*)E^*\rho(a^*)q.
\]

The input q a* is bounded and belongs to Dom E*.
The sum of these vectors converges absolutely in H with the same projective coefficient control and the E* restriction bound.
Pairing with p then proves membership in the actual adjoint domain of the summed domain-M operator.
Scalar Fourier coefficients conjugate as part of this adjoint calculation.
This verifies (G12), without claiming an identity of complete maximal product-adjoint domains.

## The two full-domain coordinate passages

Under A(S), Dab10-U002 supplies the specified canonical E_i^S and its actual adjoint on all M, with both operator-norm-to-H bounds.
For the function s+i g_j(s), uniform C1 polynomial approximation gives uniform convergence of divided-difference kernels.
Thus the corresponding commutators converge in Hilbert-Schmidt norm.
For a fixed bounded test b, the E_i^S(p_n(S_j)b) terms converge by its operator-norm-to-H bound and uniform function convergence; the remaining bounded multiplier terms converge on H.
This proves (G13) on all M.
Off-diagonal coordinate commutators remain zero.
No equality of the two polynomial algebras or general functional-calculus domain theorem is required.

Apply the projective correction with K_i.
The scalar identity K_i J_i=1 on the spectral rectangle gives the prescribed rank-one coordinate commutators for Q_Ki(E_i^S).
The adjoint series gives its actual adjoint on all M.
Thus its negative, on the dense domain M, is an S(X) witness and is closable.
This direction constructs the strong system before invoking any canonical X comparison.

Conversely, under F(X), C_F0069 makes the supplied maps operator-norm-to-H bounded.
Normalization E_i(a)=-D_i(a)+aD_i1 preserves the positive operator-first commutators and gives zero vacuum; the normalization term is itself operator-norm-to-H bounded.
C_F0070's actual starred commutators then give [E_i,S_j]=delta_ij Theta(K_i) on M.
Correcting with the projective J_i yields [Q_Ji(E_i),S_j]=delta_ij P.
Its negative is a bare full-M system for S.
This direction uses no adjoint of the supplied bare E_i.

## Full equivalence and canonical conclusion

The accepted C_F0071 Part B gives F(S) iff A(S) at the actual joint selfadjoint scope.
The preceding arguments prove

\[
A(X)\Longrightarrow A(S)\Longrightarrow S(X)
\Longrightarrow F(X)\Longrightarrow F(S).
\]

C_F0070 Part C supplies S(X) implies A(X), because the constructed strong systems have their vacuum in the actual adjoint domain and X is normal.
These arrows prove all five equivalences without replacing existential conditions by success of one chosen candidate.

After S(X) has been established, C_F0075 Part 4 applies to this normal generating tuple.
It gives both full-M domains for the specified canonical X right contractions and their actual adjoints.
The starred derivation is the unique normalized one at that strong-system scope, so the conclusion refers to the actual P_X canonical core in the statement.
It does not identify an arbitrary supplied unclosable bare full-domain map with that closure on M, or assert equality of natural domains beyond the cited compatibility result.

## Verification and source limits

All six declared dependencies have the stated accepted scopes and supply only the interfaces identified above.
C_F0076's later second-derivative theorem is unused.
C_F0071's scalar, unitary and affine extensions are unused.
The cited earlier analytic-graph materials are mechanism/scope comparisons, not proof inputs to the nonanalytic C3 passage.
The proof's periodic extensions satisfy the needed endpoint conditions, the Fourier dimension counts are explicit, and every actual-domain assertion is obtained by a graph approximation or adjoint pairing at its stated domain.

Only same-coordinate spectral functions commute in the argument.
Right multipliers commute with left multipliers for representation-theoretic reasons, irrespective of the joint law.
Therefore no freeness or hidden commutation of distinct coordinates is required.
There is no numerical, proof-assistant or priority claim, and the accepted inputs' predecessor-proof inspection boundaries are unchanged.

## Conclusion

The complete statement and argument of C_F0137 v1 pass this independently organized review with no required mathematical correction.
The six direct dependency interfaces and the elementary Fourier/extension hypotheses are adequate at their stated scopes.
This finding supports proved / independently reviewed for the fixed candidate if its responsible decision adopts it.

The result is the five-way existential equivalence and the actual canonical two-domain conclusion for coordinatewise real C3 spectral graphs over a selfadjoint generating tuple, with arbitrary correlations.
C3 is sufficient here, not claimed sharp.
The proof does not cover arbitrary normal spectral sets, identify the unstarred rational fields of S and X, or settle the full unrestricted normal-tuple comparison in T_F0011.

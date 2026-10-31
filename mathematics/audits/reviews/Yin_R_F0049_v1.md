---
author: Yin
---
# Independent review of actual phase second derivatives and normal coassociativity

Review performed and recorded: 2026-10-14T16:53.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0076 v1](../../claims/Yin_C_F0076_v1.md).
Root supplied the fixed candidate, its intended review scope, and a disclosure that the author had performed preparation checks.
Root stated that the reviewer had not participated in the proof and did not supply its development discussion.
No such discussion, separate exploratory notes or informal author explanation was consulted.
The reviewer read the complete fixed candidate selected by its initial decision dated 2026-10-14T16:44 and all four direct dependency interfaces before forming this conclusion.
Earlier unrelated reviews by this reviewer supply no evidence for the present proof.

The review covers the entire statement and all five proof sections: normal marginal diffuseness and phase determination, closability, simultaneous tensor-leg graph approximation, the regularized kernel inequality, identification and norms of all eight phase derivatives, bounded spatial coefficient rules, and both coassociativity identities on the full represented starred core.
It does not review or infer contraction bounds, canonical full-M domains, reality, freeness, or Task completion.

The four selected mathematical inputs were read at their precise used scopes.
The reviewer also read VV16's primary accepted-version PDF at equation (5), Theorem 3 and Theorem 4(1), and independently checked the four-dimensional application.
ACSY24's local published PDF was text-inspected on pp.34-35 and visually checked on p.35 for Lemma 3.3's actual tensor-adjoint conclusion.
These are bounded source-statement and applicability checks; no new audit of the original proofs cited by those source statements is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0076 statement](../../claims/Yin_C_F0076_v1.md#statement) | All three parts: diffuse phase values and closability, actual joint closed-graph domains and all eight phase-derivative bounds, full starred-core domains and both coassociativity identities. |
| [Conclusion](#conclusion) | [C_F0076 argument](../../claims/Yin_C_F0076_v1.md#argument) | Complete five-section argument, including the actual four-dimensional C1 approximation, soft-kernel domination, weak joint graph limit, bounded spatial product rules and cancellation. |
| [Conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 at its exact represented starred-domain and actual-vacuum premise, and Lemma 3.3's dense algebraic-tensor adjoint-domain implication; the latter statement was additionally checked in the original published pp.34-35. |
| [Conclusion](#conclusion) | [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta is equivalent to absence of nonzero finite-rank right-multiplication cycles; used to exclude every spectral atom of each normal coordinate. |
| [Conclusion](#conclusion) | [C_F0055 Sections 4-5](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Exact scalar actual-vacuum soft-Cauchy estimate, positive Q_t formula and limiting curvature bound, after verifying compact support, nonatomicity and the marginal projected vacuum. No free-product lifting or full-M conclusion is imported. |
| [Conclusion](#conclusion) | [C_F0073 Part A](../../claims/Yin_C_F0073_v1.md#argument) | Actual-vacuum conjugation for the derivation epsilon, including complex linearity, outer Leibniz rule and vacuum xi star. No later symmetry or bare-dual hypothesis is used. |

## Diffuse laws, the unique phase and bounded values

The exact ACSY hypotheses imply Delta(X)=d.
If a normal marginal had a nonzero atomic spectral projection e at z, then e Omega is nonzero by trace faithfulness.
Right multiplication by X_j and its adjoint have respective eigenvalues z and conjugate(z) on this line.
Thus the line reduces that normal right multiplier, and its rank-one orthogonal projection commutes with it.
Placing this projection in the j-th coordinate gives the nonzero cycle prohibited by the precise MSY23 characterization.
This proves diffuseness of every marginal without assuming a dual on all bounded vectors.

Differentiating X_j X_j*=X_j* X_j gives the candidate's equation (6) with the stated sign and multiplication order.
On the whole coarse Hilbert space, the spectral representation of lambda(X_j) on the first leg and rho(X_j) on the second is a normal representation of the product marginal algebra.
Its diagonal projection is zero because the faithful marginal product measure gives the diagonal measure zero.
Therefore their difference has trivial kernel on the entire coarse space.
The bounded phase k_j solves the differentiated relation in the abelian marginal tensor subspace; injectivity gives the asserted starred-generator values, including zero for j unequal to i.

Lemma 3.3 of ACSY24 states that the actual vacuum adjoint implies membership of every algebraic starred-core tensor in Dom delta*.
That tensor subspace is dense in H tensor H, so delta is closable.
C_F0073's conjugation pairing supplies the actual vacuum xi* for epsilon, and the same lemma proves epsilon closable.
The reversal in the coarse antiunitary matters: k(z,w)=k(w,z), so epsilon(X_i)=conjugate(k), while epsilon(X_i*)=1 tensor 1.
Each generator value is a bounded spatial tensor.
Finite Leibniz expansions using bounded core coefficients therefore put delta(p) and epsilon(p) in M bar-tensor M for every p in A.

On one marginal algebra the two derivations act by divided differences with denominator z-w and conjugate(z-w), respectively.
The normalization and the normal phase values determine those formulas on all represented marginal star polynomials.
Pairing the first formula with the vacuum projects xi onto L2(W*(X_i)); this is exactly the actual scalar vacuum assumed in C_F0055.
Compact support follows from boundedness, and the nonatomicity premise was proved above.
No vector for a different normalization or a merely formal moment identity is substituted.

## One simultaneous C1 approximation and the actual joint closure

For every fixed t>0, h_t(z,v)=conjugate(z-v)^2/(abs(z-v)^2+t) is globally smooth in four real variables.
It is bounded by one and converges to k off the null diagonal.
On a convex product box, first-real-derivative uniform convergence of polynomials controls both complex divided-difference errors by the real mean-value estimate.
The denominators for epsilon have the same modulus, so the identical polynomial sequence approximates all four quotient coordinates, not four unrelated maximal-domain representatives.

The [VV16 accepted-version PDF](https://eprints.whiterose.ac.uk/id/eprint/106084/1/tr182a2-copy-for-UoL.pdf) defines the tensor-cube approximants in equation (5), printed p.4, and states uniform function convergence in Theorem 3, p.6, and uniform derivative convergence in Theorem 4(1), p.7.
The dimension is arbitrary; d=4,m=1 is admissible.
Rescale the box and apply the real statement separately to real and imaginary parts.
The function is globally C1, so no boundary extension is needed.
The earlier [VV16-U001](../literature/VV16/Yin_U001.md#vv16-u001) retains its original d=2 application; this review does not rewrite that scope or claim a source-proof audit.

The candidate's elementary finite-difference argument also supplies this approximation: the derivative of the tensor Bernstein polynomial is the positive binomial average of a first finite difference, which is an interval average of the continuous first derivative.
Uniform continuity and uniform concentration give convergence of that derivative; the corresponding argument gives convergence of the function.
Only first real derivatives are needed.

Under evaluation in the two marginal tensor legs, every real-coordinate polynomial is an element of A tensor_alg A.
The quotient formulas (10)-(11) agree with the tensor-leg derivations there.
Since delta and epsilon are closable, their tensor-leg restrictions on this dense algebraic core are closable; this also follows by testing against algebraic tensors from their dense adjoint domains.
A convergent graph sequence for the four-component operator approaching input zero must have all four output limits zero, proving joint closability.
The simultaneous polynomial approximation then puts h_t, and separately conjugate(h_t), in the actual closure of this one common algebraic graph, with the four stated derivatives.

## Positive-kernel inequality and uniform graph control

The marginal vacuum identity and C_F0055 give norm(C_t mu)_2 at most norm(xi_marg)_2 and

\[
\int Q_t\,d\mu^3
=3\operatorname{Re}\langle\xi^{\rm marg},\overline{C_t\mu}\rangle
\le3\|\xi^{\rm marg}\|_2^2.
\]

The Q_t in the candidate is the same positive three-point expression from C_F0055.
The identity between H_0=abs(conjugate(a)b-conjugate(b)a)^2 and sixteen times squared triangle area matches its original H.
Collision diagonals are product-null, and the original smooth divided differences are bounded for fixed t, so their integral expressions are legitimate before introducing inverse side lengths.

For the left quotient, direct expansion gives

\[
\bar a^2B_t-\bar b^2A_t
=\bar a\bar b(\bar a b-\bar b a)
+t(\bar a-\bar b)(\bar a+\bar b).
\]

Applying the square-sum bound and abs(a+b)^2 at most 2(x+y) gives exactly the two terms in (14).
The H-dependent part satisfies Q_t^H at least H_0/(2 A_t B_t r).
Since xy at most A_t B_t, the first term in (14) is at most 4 Q_t^H.
For the remaining term, A_t B_t at least t(x+y+t), together with r+t at most x+y+r+6t, bounds its ratio to Q_t^0 by 8.
Thus abs(q_L h_t)^2 at most 8 Q_t and its squared norm at most 24 norm(xi_marg)_2 squared.
The symmetry of h_t, permutation invariance of the product measure, conjugate denominators, and complex conjugation give the same estimate for all four derivatives of both h_t and its conjugate.

This constant 24 is only the uniform approximating-graph bound.
It is not incorrectly substituted for the sharper final constant 6.

## Weak joint graph limit and all eight actual derivatives

For t_n decreasing to zero, the first components converge strongly to k in L2(mu squared) and the four output components are bounded in L2(mu cubed).
A subsequence converges weakly in their finite Hilbert direct sum.
The graph of the closed joint operator is a norm-closed linear subspace and therefore weakly closed.
Its limit proves actual membership of k in the joint closure domain.
Repeating the same argument with conjugates proves membership of conjugate(k).
This is stronger than separate domain membership inferred from pointwise formulas.

For each derivative coordinate the quotient converges almost everywhere off collisions to its divided-difference limit.
Uniform L2 boundedness implies uniform integrability in L1 on this probability space; hence the convergence is in L1 against bounded tests.
Density of bounded tests and the uniform L2 bound identify the weak Hilbert limit.
Thus no unidentified weak limit or maximal distributional extension is used.

The two delta derivatives of k are the symmetric second divided difference of the function z mapped to conjugate(z).
Algebraically both equal

\[
C(z,w,v)=\frac{(\bar z-\bar v)(w-v)-(\bar w-\bar v)(z-v)}
{(z-v)(w-v)(z-w)}.
\]

Its modulus squared is H_0/(xyr).
The curvature estimate of C_F0055 Section 5 therefore gives norm(C)_2 squared at most 6 norm(xi_marg)_2 squared.
The epsilon left/right derivatives of k multiply the corresponding delta quotients by the unimodular ratios (z-w)/conjugate(z-w) and (w-v)/conjugate(w-v).
The delta derivatives of conjugate(k) are conjugates of these epsilon derivatives, while its epsilon derivatives are both conjugate(C).
Hence all eight actual derivative norms have the claimed square-root-6 bound.
Collinear configurations simply give zero curvature and cause no exceptional case; all collision sets are null.

## Bounded spatial coefficient rules and coassociativity

The four displayed extra-term rules were checked on an elementary input eta=x tensor y, using ordinary spatial multiplication with the prescribed order.
For example,

\[
(\gamma b)_{12}\eta_{23}
=\sum u\otimes vx\otimes y
\quad\text{if }\gamma b=\sum u\otimes v,
\]

which is the cross term of gamma(bx) tensor y.
Similarly eta_13(gamma b)_12 gives the cross term for gamma(xb), while (gamma b)_23 eta_13 and eta_12(gamma b)_23 give the two second-leg rules.
The formulas extend from finite tensor presentations to the actual bounded spatial gamma(b) by normal multiplication on tracial L2; no reversal into an opposite multiplication convention is made.

The insertion maps are isometries because the omitted vacuum has norm one.
Left and right multiplication by gamma(b), now known to be a bounded spatial tensor, are bounded on the appropriate L2 tensor space.
Thus each extra-term map is bounded in eta, with norm at most the spatial operator norm of gamma(b).
Input multiplication by b preserves A tensor_alg A, and output multiplication is bounded.
Apply all four rules to one sequence approximating eta in the joint graph: every right-hand side converges, proving that the corresponding input multiplier preserves the joint domain and proving the actual product rules there.
This verifies the domain passage instead of assuming a general Leibniz rule for unbounded closed operators.

Finite wordwise expansions express delta(p) and epsilon(p) through core outer multipliers of 1 tensor 1, k and conjugate(k).
The established joint-domain invariance therefore puts all these values in the same joint closure domain.
Every mixed iteration asserted in the statement is consequently defined.

For p,q in A, both iterated delta derivatives of delta(pq) have the identical cross term (delta p)_12(delta q)_23.
It is a bounded spatial product, so it cancels with the same order in their difference B_delta.
The remaining terms give the ordinary outer derivation rule for B_delta into H tensor H tensor H.
It vanishes on all X_j, on X_i* by the established equality of the two actual phase derivatives, and on the other adjoint generators because their first derivatives vanish.
Hence it vanishes on all A.
For epsilon, the corresponding two derivatives of conjugate(k) both equal conjugate(C), and the identical product-rule argument proves its coassociativity.
No commutativity between distinct coordinates or freeness is needed.

## Source and verification boundaries

ACSY24-U001 and MSY23-U002 are used at their already retained maximality and cycle interfaces.
The additional direct local ACSY24 inspection confirms the exact Lemma 3.3 premise and algebraic-tensor adjoint conclusion on published pp.34-35; the original external proof cited by that lemma was not audited.
C_F0073 supplies only its conjugation-vacuum part.
C_F0055 is used only for its scalar actual-vacuum inequalities and curvature bound, after every scalar premise was verified.
Its freely independent lifting and scalar full-domain conclusions are not inputs to a correlated-tuple full-domain assertion here.

The four-dimensional Bernstein statement was directly verified as described above, and its elementary mechanism was also checked in the candidate.
Neither that reading nor the old VV16-U001 implies a prescribed convergence rate or a general operator graph estimate; the quotient and joint graph work is the present proof.
There is no dependency cycle, numerical verification, proof-assistant verification, or novelty assertion.

## Conclusion

The complete fixed statement and all five proof sections of C_F0076 v1 pass this independently organized review with no required mathematical correction.
Source use and applicability are adequate at the explicit inspection boundaries.
The finding supports proved / independently reviewed for this exact candidate if adopted by its responsible Claim decision.

The supported result is actual joint phase-domain membership, the stated derivative bounds, all starred-core mixed domains, and separate coassociativity of delta_i and epsilon_i under the full normal ACSY premise.
It supplies neither an operator-norm-to-L2 contraction bound nor all-M canonical operator/adjoint domains.
No reality condition, freely independent reduction or completion of the broader research project follows from this finding alone.

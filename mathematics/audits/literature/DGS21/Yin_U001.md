---
author: Yin
---

<a id="dgs21-u001"></a>
# DGS21-U001: Endpoint Estimates and the Actual Canonical Dual Domains

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [DGS21, retained published journal PDF](../../../literature/pdf/DGS21--published.pdf), New Zealand Journal of Mathematics 52 (2021), 259--359.

Passages: Section 2.3, printed pp.271--272 / PDF pp.13--14; Appendix B.4, Lemma B.36(2), its proof attribution and formula (51), printed pp.335--337 / PDF pp.77--79. Supporting Dab10 passages: Lemma 10, Remark 11 and Lemma 12, retained arXiv v2 pp.8--9.

Inspection: 2026-10-16T04:25, AI source reader for Yin; source state: Read, with the exact hypotheses, both endpoint assertions and the complete printed proof of part (2) rechecked. The standard duality and closed-graph application below was fully reconstructed and self-checked. No independent review, full-paper audit, or new reconstruction of the general amalgamated estimate is claimed.


The question is whether the two endpoint estimates give both bounded-vector domains of the specified Hilbert-space closure, and whether the source applies to arbitrary normal coordinate derivations.
The earlier selected source reading left the graph identification to a separate argument.
This unit supplies that identification using standard operator duality and the same weak-graph mechanism already retained in [C_F0072, argument Section 4](../../../claims/Yin_C_F0072_v1.md#4-restoration-of-both-full-domains).
It is a direct application of the source estimates, not a new general-normal contraction theorem.

## Exact scalar specialization and normalization

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace.
Write \(H=L^2(M,\tau)\), identify \(a\Omega\) with \(a\), and use the inner product \(\langle a,b\rangle=\tau(a^*b)\), linear in the second variable.
For bounded selfadjoint generators \(X_1,\ldots,X_d\), let \(A=\mathbb C\langle X_1,\ldots,X_d\rangle\).
Assume the actual conjugate variables \(\xi_i=\partial_i^*(1\otimes1)\) exist in \(H\).

In DGS21 take both the coefficient algebra and the amalgamating algebra to be \(\mathbb C1\).
Its contraction becomes the actual core operator
\[
 C_{i,0}:A\Omega\longrightarrow H,\qquad
 C_{i,0}(a\Omega)=(\mathrm{id}\otimes\tau)\partial_i(a).
 \tag{1}
\]
The first assertion of Lemma B.36(2) gives finite constants \(K_{\infty,i},K_{1,i}\) such that
\[
 \|C_{i,0}a\|_2\le K_{\infty,i}\|a\|,
 \qquad
 \|C_{i,0}a\|_1\le K_{1,i}\|a\|_2
 \quad(a\in A).
 \tag{2}
\]
The second inequality gives a unique continuous extension
\[
 B_i:H\longrightarrow L^1(M)
 \tag{3}
\]
because \(A\Omega\) is dense in \(H\).
Neither inequality in (2) asserts \(L^2\)-to-\(L^2\) boundedness.

The Leibniz rule fixes the sign:
\[
 C_{i,0}(X_ja)-X_jC_{i,0}(a)
 =\delta_{ij}\tau(a)\Omega.
 \tag{4}
\]
Thus the generator-first canonical dual is
\[
 D_i^{\mathrm{can}}=-\overline{C_{i,0}}.
 \tag{5}
\]
The stronger part of B.36(2), involving bounded first and second conjugate variables, is unnecessary for the bounded-vector domain conclusion.

For the genuinely relative contraction \(C_i=(1\otimes E_{\mathcal D})\partial_i\), the right side of (4) is instead \(\delta_{ij}E_{\mathcal D}(a)\).
On \(H\), this is the orthogonal projection onto \(L^2(\mathcal D)\).
It becomes the rank-one \(P_\Omega\) only when the amalgamating algebra is scalar.
The relative statement therefore must be specialized before claiming the rank-one dual relation.

## The \(L^2\)-to-\(L^1\) estimate gives the whole adjoint domain

Suppress the index \(i\).
For every \(x\in M\) and \(a\in A\), noncommutative Holder gives
\[
 |\langle x,C_0a\rangle|
 =|\tau(x^*C_0a)|
 \le \|x\|\|C_0a\|_1
 \le K_1\|x\|\|a\|_2.
 \tag{6}
\]
This is exactly the actual Hilbert-adjoint domain criterion.
Consequently
\[
 M\Omega\subseteq\operatorname{Dom}C_0^*,
 \qquad
 \|C_0^*(x\Omega)\|_2\le K_1\|x\|.
 \tag{7}
\]
Since \(M\Omega\) is dense, \(C_0\) is closable.
Put \(C=\overline{C_0}\); then \(C^*=C_0^*\).

This step uses neither a selfadjoint generator nor a reality identity for the derivation.
It does not first define a formal adjoint on the core and subsequently guess an extension.
The representing functional in (6) identifies the actual adjoint on every bounded vector directly.

## The operator-norm-to-\(L^2\) estimate gives the original closure domain

Fix \(x\in M\) and \(\varepsilon>0\).
Kaplansky density for the norm closure of \(A\), followed by norm approximation from \(A\), supplies a net \(a_\alpha\in A\) with
\[
 a_\alpha\Omega\longrightarrow x\Omega\ \text{in }H,
 \qquad
 \sup_\alpha\|a_\alpha\|\le\|x\|+\varepsilon.
 \tag{8}
\]
The first inequality in (2) makes \(C_0a_\alpha\) bounded in \(H\).
A subnet converges weakly to some \(y\in H\).
The graph of \(C\) is a norm-closed linear subspace of \(H\oplus H\), hence is weakly closed.
Since each \((a_\alpha,C_0a_\alpha)\) lies in that graph, its weak limit gives
\[
 x\Omega\in\operatorname{Dom}C,\qquad C(x\Omega)=y.
 \tag{9}
\]
Weak lower semicontinuity and then \(\varepsilon\downarrow0\) yield
\[
 \|C(x\Omega)\|_2\le K_\infty\|x\|.
 \tag{10}
\]
Thus the result concerns the original canonical closure, not an arbitrary Banach-space extension of the core map.

The extension in (3) also identifies its value:
\(B(a_\alpha)\to B(x\Omega)\) in \(L^1\).
For every \(z\in M\), that convergence and the weak \(H\) convergence give
\[
 \tau(z^*B(x\Omega))
 =\lim_\alpha\tau(z^*C_0a_\alpha)
 =\tau(z^*Cx).
\]
The \(M\)-pairing separates \(L^1(M)\), so \(B(x\Omega)=Cx\) as an \(L^1\) element.
In particular \(B(x\Omega)\) actually belongs to \(L^2\).
An unspecified bounded extension from \(M\) to \(H\) need not be identified by norm density of \(A\) in \(M\); the canonical \(H\)-to-\(L^1\) extension and the graph argument remove that ambiguity.

Combining (7) and (9) proves
\[
 M\Omega\subseteq\operatorname{Dom}D_i^{\mathrm{can}}
 \cap\operatorname{Dom}(D_i^{\mathrm{can}})^*.
 \tag{11}
\]

## The dual identity extends to every bounded vector

The core relation (4) has a bounded right side.
For any \(\eta\in\operatorname{Dom}C\), take a core sequence \(a_n\) converging to \(\eta\) in the graph norm.
Then
\[
 X_ja_n\to X_j\eta,\qquad
 C_0(X_ja_n)=X_jC_0a_n+\delta_{ij}P_\Omega a_n
 \to X_jC\eta+\delta_{ij}P_\Omega\eta
\]
in \(H\).
Closedness gives \(X_j\eta\in\operatorname{Dom}C\) and the same identity there.
Using (5) and (11),
\[
 [X_j,D_i^{\mathrm{can}}]\big|_{M\Omega}
 =\delta_{ij}P_\Omega\big|_{M\Omega}.
 \tag{12}
\]
No additional weak-limit argument for the commutator is required.
This also verifies invariance of the actual closed-operator domain under the generators.

## What the endpoint conditions mean without selfadjointness

The reasoning in (6)--(10) works for any linear operator \(C_0:A\Omega\to H\) on a weakly dense unital star subalgebra satisfying (2).
It needs no derivation, normality, reality or coassociativity.
For a closable \(C_0\), those two inequalities are also necessary for both full bounded-vector domains.

Indeed, if \(M\Omega\subseteq\operatorname{Dom}C\cap\operatorname{Dom}C^*\), the restrictions \(C|_M\) and \(C^*|_M\) have closed graphs from the Banach space \(M\) to \(H\).
They are therefore bounded.
Using \(L^1\)-\(M\) duality,
\[
 \|C_0a\|_1
 =\sup_{\|x\|\le1}|\langle x,C_0a\rangle|
 =\sup_{\|x\|\le1}|\langle C^*x,a\rangle|
 \le\|C^*|_M\|\|a\|_2.
 \tag{13}
\]
The other inequality is the restriction of the \(M\)-to-\(H\) bound for \(C\).

For an actual-vacuum derivation \(\delta:A\to H\otimes_2H\), write
\[
 E_0=(\mathrm{id}\otimes\tau)\delta,\qquad
 F_0=(\tau\otimes\mathrm{id})\delta,\qquad
 \xi=\delta^*(1\otimes1).
\]
The general formula, with no reality premise, is
\[
 E_0^*a=a\xi-\bigl(F_0(a^*)\bigr)^*,\qquad a\in A.
 \tag{14}
\]
This is the actual-adjoint interface in [ACSY24-U001](../ACSY24/Yin_U001.md#acsy24-u001) and [C_F0072](../../../claims/Yin_C_F0072_v1.md#statement).
Therefore an operator-norm-to-\(L^2\) bound for \(F_0\) gives the \(L^2\)-to-\(L^1\) estimate for \(E_0\), with constant at most \(\|\xi\|_2+\|F_0\|_{\infty\to2}\).
To justify the \(L^1\) norm using only core tests in this direction, the unit ball of \(A\) is weak-star dense in the unit ball of \(M\), up to an arbitrarily small norm tolerance, by Kaplansky density.
Conversely (7) and (14) bound \(F_0\) by \(\|\xi\|_2+K_1\).
Thus the endpoint formulation is equivalent, under the actual-vacuum hypothesis, to the existing two-contraction formulation.
It does not eliminate the missing analytic estimate in the unrestricted normal problem.

## Why DGS21 does not itself establish the normal estimates

DGS21 Section 2.3 explicitly defines its tuple space by \(X_i=X_i^*\).
The absence of a repeated selfadjoint adjective in the isolated wording of B.36 does not change that standing setting.
Its entire printed proof of part (2) is an attribution to the relative variant of Dab10 Remark 11 and Lemma 12.
The referenced argument uses the real free difference quotient and its coassociative energy identity.
[Dab10-U002](../Dab10/Yin_U002.md#dab10-u002) and [Mai15-U002](../Mai15/Yin_U002.md#mai15-u002) retain the exact identities and their roles.

For arbitrary normal generators under the actual starred-core vacuum hypothesis, the core is
\(A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle\).
The holomorphic algebra alone need not be dense in \(H\).
For instance nonnegative powers of a Haar unitary span a proper Hardy subspace.

Normality forces the starred derivative to be
\[
 \delta_i(X_j^*)=\delta_{ij}k_j,\qquad
 k_j(z,w)=\frac{\bar z-\bar w}{z-w}
\]
on the product-null-diagonal complement of its diffuse marginal law.
Usually \(k_j\ne1\), so \(\delta_i(a^*)=\delta_i(a)^\dagger\) fails.
The phase has modulus one, but that is a bound on a tensor multiplier, not either endpoint bound for the contracted map.
[C_F0076](../../../claims/Yin_C_F0076_v1.md#statement) already supplies the actual iterated Hilbert-tensor domains and pure coassociativity in this normal setting.
Accordingly the missing ingredient must not be described merely as unavailable coassociativity.
Reality and the resulting energy control remain additional requirements; algebraic core-tensor range is also absent in general from the literal hypotheses of Mai15.

Writing \(X=A+\mathrm iB\) with selfadjoint \(A,B\) does not justify applying the ordinary selfadjoint free-difference-quotient theorem to the doubled tuple.
Normality imposes \(AB=BA\).
An alleged coordinate derivation with \(\partial_A A=1\otimes1\) and \(\partial_A B=0\) would give
\[
 0=\partial_A(AB-BA)=1\otimes B-B\otimes1,
\]
which forces \(B\) to be scalar.
A scalar \(B\) cannot simultaneously have its own free coordinate derivative equal to \(1\otimes1\).
Thus the real and imaginary parts do not inherit the needed independent-coordinate derivations.

As an explicit check of the lost real identity, take a Haar unitary \(U\) in its abelian tracial algebra.
On Laurent polynomials,
\[
 C_0U^n=
 \begin{cases}U^{n-1},&n\ge1,\\0,&n\le0,\end{cases}
 \qquad
 \xi=U,\qquad
 C_0^*U^n=
 \begin{cases}U^{n+1},&n\ge0,\\0,&n<0.\end{cases}
\]
These formulas are the radius-one case of the already retained circle computation in [C_F0047](../../../claims/Yin_C_F0047_v1.md#2-the-same-radius-calculation).
For \(a=U^{-1}\), the real-case formula \(C_0^*a=a\xi-C_0a\) would give \(1\), whereas the actual value is \(0\).
Likewise, with \(T=C_0^*|_A\), the real coassociative energy equality
\(\|Ta\|_2^2=\langle T(a^*a),\xi\rangle\) would read \(0=1\).
This refutes that literal proof transfer, not the endpoint estimates: here \(C_0\) is already bounded on \(H\).

## Current positive normal scopes and remaining boundary

The selfadjoint finite-Fisher conclusion follows completely from the scalar specialization above.
Beyond it, the current repository has separate positive arguments:
[C_F0071 v2](../../../claims/Yin_C_F0071_v2.md#statement) treats mixed selfadjoint/unitary coordinates and affine changes of selfadjoint coordinates.
[C_F0162](../../../claims/Yin_C_F0162_v1.md#statement), at its selected independently reviewed decision, supplies the two contraction bounds and both original canonical domains for every scalar normal actual-vacuum law and every freely independent normal tuple satisfying that hypothesis.
Those normal conclusions are project results with their own arguments; they are not attributed to DGS21.

For arbitrary correlated normal tuples, existence of the starred derivations and actual vacuum alone has not supplied the two estimates in (2) in the checked current materials.
No normal counterexample to the full bounded-vector domain conclusion is produced by this unit.
The failure of the real identity above, or failure of the optimal real constant in [C_F0161](../../../claims/Yin_C_F0161_v1.md#statement), does not refute the existence of some finite endpoint constants.

The resulting source use is precise: B.36(2), specialized to scalar amalgamation and selfadjoint coordinates, plus standard duality and the existing weak-graph mechanism gives both canonical domains and the rank-one commutator.
For normal coordinates, the same domain argument is valid as soon as the two endpoint estimates are proved by an applicable argument.
The source does not prove those estimates under normality alone.

## Verification boundary

The complete domain application, sign, relative projection, commutator closure passage, endpoint equivalence and Haar-unitary check were self-checked in this reading.
The established scalar endpoint theorem is accepted with its stated assumptions.
The source's general amalgamated proof and the extended Haagerup results in the other parts of B.36 were not independently reconstructed.
The checked local positive-normal and coassociativity results are reused at their selected scopes; their full proofs were not audited anew here.
The primary search rechecked the journal record and the exact B.36 passage; the retained published PDF supplied the direct reading.
This bounded source analysis does not select a new manuscript proof, alter a fixed Claim assessment, or settle the unrestricted correlated-normal question.

---
author: Yin
---

# Ele03 finite-support kernels and the exact boundary estimate

<a id="ele03-u001"></a>
## Source and inspection

Yin's coordinating agent read the complete four-page [arXiv v1](readme.md#yin) and reconstructed every step of Theorem 1 and Proposition 1 on 10 November 2026.
The source's definitions and dimension facts are made explicit below, including the closure of a possibly nonclosed range.
The mathematical inspection is the coordinator's source-proof reconstruction.
The source's four background references were identified as citations, and their original proofs were not recursively audited.
The elementary Hilbert-space and finite-von-Neumann-algebra foundations used below are retained inputs.
The matrix and Schur-complement deduction is retained separately in [the fixed project argument](../../../claims/Yin_C_A0001_v1.md).

## The theorem's actual hypotheses

Theorem 1, p.2, assumes a finitely generated amenable group \(G\), a nonzero \(\alpha\in\mathbb CG\), and a nonzero \(\beta\in\ell^2(G)\) with \(\alpha\beta=0\).
It concludes that \(\alpha\gamma=0\) for some nonzero \(\gamma\in\mathbb CG\).
Torsion-freeness is absent from this theorem.
It occurs in the two zero-divisor conjectures in the introduction, whose equivalence for amenable groups follows from the theorem and \(\mathbb CG\subseteq\ell^2(G)\).
The result therefore converts an analytic zero divisor into an algebraic zero divisor under amenability.
It supplies no proof of the algebraic zero-divisor conjecture from torsion-freeness.

<a id="folner-and-propagation"></a>
## Følner sets and propagation

Fix a finite symmetric generating set, its word length \(|\cdot|\), and the right-invariant metric
\[
d(x,y)=|xy^{-1}|.
\]
For a nonempty finite \(F\subset G\) and \(r\ge0\), put
\[
\partial_rF=\{x\in F:d(x,G\setminus F)\le r\},\qquad
F^{-r}=F\setminus\partial_rF.
\]
For a finite group and \(F=G\), distance to the empty complement is interpreted as infinity.
The source's Følner formulation of amenability is an increasing finite exhaustion \(F_k\) satisfying
\[
|\partial_rF_k|/|F_k|\longrightarrow0
\quad\text{for each fixed }r.
\]
The equivalence with other definitions of amenability is a retained standard characterization.
The proof itself only needs finite sets with this limit for the single width under consideration.

For \(\alpha=\sum_{s\in S}a_s s\ne0\), its width is
\[
w=\max_{s\in S}|s|.
\]
Left convolution \(M_\alpha\) is bounded with norm at most \(\sum_s|a_s|\), commutes with right translations, and has propagation at most \(w\).
Indeed, an input coefficient at \(x\) can contribute only at \(sx\), and
\[
d(sx,x)=|s|\le w.
\]
Consequently
\[
\operatorname{supp}\xi\subseteq F^{-w}
\quad\Longrightarrow\quad
\operatorname{supp}(M_\alpha\xi)\subseteq F.
\]
This is the precise use of finite propagation on p.3.
The right-invariant metric is consistent with left convolution and right-module invariance.

<a id="local-dimension"></a>
## Local dimension and invariant dimension

For any linear subspace \(W\subseteq\ell^2(G)\), let \(P_W\) denote projection onto its Hilbert closure.
For nonempty finite \(F\), define
\[
\dim_F W=\frac1{|F|}\sum_{g\in F}\langle P_W\delta_g,\delta_g\rangle.
\]
For a right-translation-invariant subspace \(V\), define
\[
\dim_G V=\langle P_V\delta_e,\delta_e\rangle.
\]
Invariance makes every diagonal coefficient equal, giving \(\dim_F V=\dim_G V\) for every \(F\).
If \(W\subseteq Z\), projection order gives \(\dim_F W\le\dim_F Z\).
If \(W\) is supported on \(F\), the trace of its finite-dimensional projection gives
\[
\dim_F W=\dim_{\mathbb C}W/|F|.
\]
These statements require neither amenability nor finite propagation.

Faithfulness is also direct.
If \(P_V\) has zero diagonal at \(e\), then \(P_V\delta_e=0\).
Commutation with right translations then gives \(P_V\delta_g=0\) for every \(g\), hence \(P_V=0\).
Thus nonzero invariant \(V\) has strictly positive dimension.

For a bounded right-equivariant \(T\), polar decomposition gives equivalent initial and final support projections.
The finite trace therefore gives
\[
\dim_G\ker T+\dim_G\overline{\operatorname{im}T}=1.
\]
The source writes \(\operatorname{Ran}T\), consistently using its closure in the definition of dimension.
Closed range is not an assumption.
Existence of polar decomposition and the tracial property are the retained operator-algebra inputs.

<a id="boundary-proof"></a>
## Complete proof of Proposition 1

Set \(K=\ker M_\alpha\), \(I=\overline{\operatorname{im}M_\alpha}\), and \(\delta=\dim_G K\), \(\rho=\dim_G I=1-\delta\).
For a finite \(F\), restrict \(M_\alpha\) to
\[
T_F:\mathbb C[F^{-w}]\longrightarrow\mathbb C[F].
\]
Finite propagation supplies the displayed codomain.
Finite-dimensional rank-nullity gives
\[
\dim_{\mathbb C}\ker T_F+\dim_{\mathbb C}\operatorname{im}T_F=|F^{-w}|.
\]
The domain and both resulting subspaces are supported on \(F\).
Moreover
\[
\ker T_F\subseteq K\cap\mathbb C[F]\subseteq K,\qquad
\operatorname{im}T_F\subseteq I.
\]
Local-dimension monotonicity, equality on invariant subspaces, and finite-dimensional projection trace give
\[
u_F:=\frac{\dim_{\mathbb C}\ker T_F}{|F|}
\le
v_F:=\frac{\dim_{\mathbb C}(K\cap\mathbb C[F])}{|F|}
\le\delta,\qquad
t_F:=\frac{\dim_{\mathbb C}\operatorname{im}T_F}{|F|}\le\rho.
\]
The rank-nullity identity is
\[
u_F+t_F=1-\varepsilon_F,\qquad
\varepsilon_F=|\partial_wF|/|F|.
\]
Thus both errors are nonnegative and their sum is exactly the boundary fraction:
\[
(\delta-u_F)+(\rho-t_F)=\varepsilon_F.
\]
In particular,
\[
\boxed{\delta-\varepsilon_F\le u_F\le v_F\le\delta.}
\]
This explicitly supplies the squeeze argument compressed into equations (1)-(4) on pp.3-4.
For a Følner sequence, \(\varepsilon_{F_k}\to0\), and therefore \(v_{F_k}\to\delta\), which is Proposition 1.
Amenability is used at this final limiting step through the boundary fraction.
All preceding finite-set inequalities remain valid for any finitely generated group.

## Complete proof of Theorem 1

The assumed nonzero vector \(\beta\) makes \(K\ne0\), so faithfulness gives \(\delta>0\).
Choose a Følner set with \(\varepsilon_F<\delta\).
The quantitative estimate then gives \(u_F>0\), hence a nonzero finitely supported \(\gamma\in\ker T_F\subseteq K\).
This proves the stated conclusion.
The source uses \(v_F\to\delta\) instead, with the same outcome.
There is no assumption that \(\delta\) is an integer and no lower bound on \(\delta\) other than positivity.
The argument found no unresolved internal step in this edition's theorem proof.

## Dependency accounting

The Dodziuk-Mathai result cited before Proposition 1 is motivation for a variant, and the displayed proof establishes that variant directly.
The Eckmann citation accompanies the finite-set dimension notation, whose used properties were checked above.
Linnell's cited work supplies the formulation of the analytic conjecture.
Pansu is cited for invariant dimension and its standard properties, which are reduced above to projection trace and polar decomposition.
Thus the source's proof has no hidden approximation theorem as an additional premise beyond these stated foundations and the Følner characterization.

## Transfer to rational closures

The matrix extension preserves finite propagation and uses the unnormalized matrix trace.
Its exact error is the number of input components times the boundary fraction.
The proof and its Schur-complement application are in [Yin_C_A0001](../../../claims/Yin_C_A0001_v1.md#argument).

Direct application to an affiliated rational expression can fail before any boundary limit is taken.
For an infinite-order \(g\),
\[
(2-g)^{-1}=\sum_{j\ge0}2^{-j-1}g^j
\]
already has infinite propagation.
For \(G=\mathbb Z=\langle g\rangle\), the affiliated inverse \((1-g)^{-1}\) corresponds under Fourier transform to multiplication by \((1-z)^{-1}\).
The vector \(\delta_e\) corresponds to the constant function, and \((1-z)^{-1}\notin L^2(\mathbb T)\).
Thus finite-support input vectors need not even belong to the domain of an unbounded rational inverse.
The finite-dimensional restriction \(T_F\) in the source proof is consequently unavailable for that inverse.

Block linearization recovers a bounded finite-propagation matrix over \(\mathbb CG\).
It also preserves the kernel-dimension information through affiliated rank identities, as used in the fixed deduction.
The resulting boundary estimate still requires Følner sets.
The free-group tree boundary example in the [earlier exploration](../../../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) explains why general finite-propagation matrix kernels need not contain finite-support vectors.
The infinite-order denominator argument from torsion-freeness supplies no vanishing boundary ratio for a group generated by all the numerator and denominator coefficients.

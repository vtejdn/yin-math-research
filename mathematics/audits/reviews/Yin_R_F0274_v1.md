---
author: Yin
---

# Review of the Borel-phase energy criterion and finite-column bounds

At 2026-11-14T13:12 UTC a separate agent reviewed the complete [candidate of 2026-11-14T13:07 UTC](../../claims/Yin_C_F0265_v1.md#decision-candidate) for Yin.
The reviewer took no part in developing the argument and received the fixed claim, the review scope and its mathematical references without proof-generation dialogue, exploration notes, author explanations or earlier conclusions about this candidate.

## Finding

The normalized derivative at \(Y=h^*V\) exists on the represented starred core for every allowed base law.
In the larger algebraic free product its right slice is the free right slice at \(V\) followed by right multiplication by \(h\).
On each reduced prefix ending in the base factor, cuts before the final unitary block have a centered base letter on the right trace leg and zero conditional expectation onto \(B=W^*(V)\).
Orthonormalizing the finitely many letters of a column gives Laurent coefficients with \(\sum_{j,q} b_{jq}^*b_{jq}=\mathbb E_B(\sum_jp_j^*p_j)\).
The commutative finite-family bound applied to this single family gives the stated column cost, and the orthogonal sum gives the claimed stronger bound whenever the scalar slice is Hilbert-space bounded.
Moving the inner factor \(h\) around the first trace gives the vacuum \(h^*\xi_V\).
On Laurent polynomials in \(Y\) the derivative takes values in the scalar two-leg space by the inverse rule, so projecting the vacuum gives the scalar adjoint pairing and forces the law of \(Y\) to be diffuse.

For the derivation \(L(V)=1\otimes V\), the marginal slice is \(Db=E_V(bV)-b\), including \(D1=0\).
Its double trace is represented by the centered \(H=\xi_VV^*-1\).
For a centered reduced word with at least two blocks, each cut in the free extension of \(L\) or of \(\gamma^0\) leaves a centered reduced segment next to a letter of a different factor on one trace leg.
This verifies the two vacuum identities on the algebra containing all bounded base letters.
The correction \((I_{h\otimes h^*}-1)L\) cancels \(\gamma^0(h^*)V\) when applied to \(h^*V\), and trace cyclicity gives the liberation vacuum \(h^*Hh-H\).
Freeness identifies \(aHb\) with \(a\otimes b\) up to the factor \(\|H\|_2\), by testing products of bounded base elements and taking centered bounded approximations to \(H\).
The coefficient of the vacuum in this representation is \(\overline{h(z)}h(w)-1\), so its squared spectral density is \(\|H\|_2^2|h(z)-h(w)|^2\).
The inverse-gap theorem gives precisely (2) and the base-vacuum existence criterion when \(\mu\) is diffuse, and full actuality forces diffuseness in the necessary direction.
Vanishing of \(H\) forces the positive moments of \(V\) to vanish successively because the first term of the \(n\)-th double trace is \(m_n\) and the other terms involve earlier moments.
Conversely the double traces on all nonzero Laurent powers vanish for the Haar law.
In that case the integrand in (2) is zero pointwise off the diagonal for every Borel phase.
For the Poisson law the Haar variable \(W=(V-r)(1-rV)^{-1}\) has \(\|W-W^*\|_2^2=2\), which gives the stated coefficient, and \(\mathbb E_A(Y)=r h^*\) detects dependence whenever \(h\) is nonconstant as an element of \(A\).

I checked (3) on arbitrary finite columns in the algebraic free product.
For a separated kernel \(v\otimes e\) and a word \(qba\) with final centered \(B\)-block \(b\), every earlier cut has a right-leg \(B\)-coefficient followed by a centered base block and a suffix containing the final \(b\).
After cycling the two end base factors together, expanding this factor and the right-leg coefficient into mean and centered parts gives zero trace in each term.
At the last cut the right trace is \(\tau(eda)=\tau(d)\tau(ae)\) for \(d\in B\), giving \(q(Db)v\tau(ae)\).
Writing \(R=(1-P_1)D\), the centered output at a Hilbert-bounded \(D\) acts by \(\mathrm{id}\otimes R\otimes O_k\) on the orthogonal summand indexed by the final \(B\)-block.
Its Hilbert norm bound gives the same finite-column bound by taking the trace of the input column square.

For general \(D\), a unit column gives \(\mathbb E_B(e^*\sum_j p_j^*p_j e)\le\|e\|_2^2 1\).
This bounds the column of all terminal coefficients of \(p_je\), and the squared scalar means removed by \(P_B\) sum to at most the trace of that conditional expectation.
The projected coefficient column thus costs at most \(2\|e\|_2\), including the unaltered empty-prefix coefficient.
The finite-family inequality on \(C^*(V)\) applies simultaneously to every entry and prefix since \(\|R\|\le a_V+1\).
It produces a single map \(T_p\) on \(L^2(A)\) of norm at most \(2\sqrt{4/\pi}(a_V+1)\).
All outputs end in a centered \(B\)-letter, so appending the last base variable is isometric on their tensor product with \(L^2(A)\).
Applying \(T_p\otimes\mathrm{id}\) to \(\sum_\ell e_\ell\otimes v_\ell\) yields the required centered estimate with the Hilbert norm of \(k\), uniformly in both column length and number of kernel summands.

The scalar output uses the projection \(P_A(p_j e_\ell H^*)\).
On \(qba\), centering \(ae_\ell\) leaves a word ending in \(H^*\) which this projection removes, while its mean contributes \(q\tau(bH^*)\tau(ae_\ell)\).
For orthonormal \(e_\ell\), freeness gives \(\mathbb E_A(H e_\ell^*e_n H^*)=\delta_{\ell n}\|H\|_2^2 1\) in \(L^1(A)\), using centered \(L^2\) truncations of \(H\).
Thus multiplication of a vector of bounded base functions by the row \((e_\ell H^*)_\ell\) has Hilbert norm \(\|H\|_2\) times the input norm, and left multiplication by the unit column is contractive.
Localization to measurable sets gives the same operator norm bound almost everywhere for the joint fiber matrix, including all column entries at once.
The right base-module coordinates identify \(1-P_A\) with projection of the average onto the nonempty prefixes ending in \(B^\circ\).
Subtracting that projected average from the fiber matrix costs at most \(2\|H\|_2\), which bounds (5) after applying the matrix to \((v_\ell(z))_\ell\).
Rectangle conditional expectations approximate a bounded Borel kernel almost everywhere with uniform bounds, so the coarse spectral domination identifies the resulting limit with the indicated actual slice on each input.
The \(L^2\)-kernel extension follows by completion in column norm.

In the Haar case each change of sign between neighboring \(V\)-powers in the cyclic tests for \(h^*V\) leaves a centered base separator, possibly conjugated by \(h\).
Terms in which an intervening base coefficient contributes its scalar part can only merge exponents of one sign.
Hence the nonzero powers are centered, and all cyclic mixed tests vanish by freeness.
General alternating tests follow by cycling together and centering end blocks from the same algebra, reducing their number in the scalar term.
This proves that the free estimates apply for every measurable phase in the Haar branch.

For the non-Haar branch, multiplication by \(t_\epsilon\) changes the target liberation identity into (7), whose second kernel is bounded for each fixed cutoff and has \(L^2\) norm at most \(\sqrt{J_\mu(h)}\).
On the free polynomial core, the two-Haar encoding and the one-input free estimate give the claimed reference column constant, and the soft cutoff costs at most three times that constant.
Bounded strong-star polynomial approximants to \(h,h^*\) converge in the graph of the inner difference on the base, which suffices for the first term of (7).
For a finite target column the positive approximating sums \(S_\lambda\) converge strongly-star with convergent derivatives by the product rule.
Uniform \(C^1\) approximation controls the outer divided differences of \(g\) on a common spectral interval.
Their limiting action on the derivative of the target square is zero because its spectrum lies in \([0,1]\).
This gives entrywise graph convergence while the cutoff on \(\sqrt{s}|g(s)|\) controls the whole input column norm.
One can therefore pass the free estimate at fixed \(\epsilon\), then remove the column normalization error and finally take the coarse limit on every finite target column.
The reference approximation imposes no additional derivative-graph hypothesis on \(h\).

Conjugation by \(h\) takes \((Z^*,V^*h)\) to \((Z^*,hV^*)\).
The new free marginal is \(V^*\) and the conjugated spectral law of the base gives exactly the original energy for \(z\mapsto\overline{h(\bar z)}\).
Both scalar vacua transform by adjoint, and transport of the core by the trace-preserving conjugation preserves the right-column bounds.
Flip-adjoint conjugation gives \(C\epsilon_i(p)=((\tau\otimes\mathrm{id})\partial_i(p^*))^*\) on the original core.
The two-contraction theorem then gives both full bounded-vector domains for the specified original closure.
Graph approximation extends its operator-first commutator to the closure domain, and negation gives the generator-first identity.
Part C of the normal strong-to-actual theorem applies since \(1\) belongs to each supplied adjoint domain.
The statement and full argument are supported for the stated Borel-phase class, including the independent second-coordinate assertion and both orientations under (1).
The cited results were checked at their applied statements and interfaces.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0265_v1.md#statement) | Exact equivalence, vacuum norm, unconditional unitary coordinate, Poisson example and finite-column and domain conclusions in both orientations. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0265_v1.md#argument) | Whole proof, including terminal cuts, simultaneous column estimates, both phase branches, original-core approximation and adjoint transport. |
| [Finding](#finding) | [Task conventions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred core, actual adjoints, generator-first commutators and bounded-vector domains. |
| [Finding](#finding) | [Poisson marginal](../../claims/Yin_C_F0057_v1.md#2-a-free-reference-pair-with-bounded-duals) | Moments, actual vacuum and Hilbert-bounded marginal right slice. |
| [Finding](#finding) | [Free right-module decomposition](../../claims/Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Orthonormal prefixes, finite letter expansions and conditional expectation onto a terminal factor. |
| [Finding](#finding) | [Commutative finite-family inequality](../../claims/Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input) | Complex commutative operator-norm-to-Hilbert estimate on the whole coefficient family. |
| [Finding](#finding) | [Actual scalar estimate](../../claims/Yin_C_F0055_v1.md#statement) | Finite marginal slice bound from the diffuse scalar vacuum. |
| [Finding](#finding) | [Terminal correction](../../claims/Yin_C_F0058_v1.md#4-the-triangular-correction-is-a-bounded-contraction) | Centered projection and scalar deletion applied to joint input columns in the reviewed proof. |
| [Finding](#finding) | [Poisson phase vacuum](../../claims/Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Haar change of variable and exact nonzero squared norm. |
| [Finding](#finding) | [Normal starred values](../../claims/Yin_C_F0076_v1.md#statement) | Marginal diffuseness, forced generator values and adjoint orientation. |
| [Finding](#finding) | [Inverse-gap criterion](../../claims/Yin_C_F0238_v1.md#statement) | Single distinguished actual vacuum, spectral norm contribution and uniform soft-cutoff estimate. |
| [Finding](#finding) | [Free column criterion](../../claims/Yin_C_F0208_v1.md#statement) | Two-Haar augmentation, preserved free vacua and control of old finite columns. |
| [Finding](#finding) | [Free one-input estimate](../../claims/Yin_C_F0162_v1.md#statement) | Part B on the actual augmented free reference tuple. |
| [Finding](#finding) | [Graph cutoff](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Strong-star graph convergence with a uniform bound on each complete approximating column. |
| [Finding](#finding) | [Two-contraction theorem](../../claims/Yin_C_F0072_v1.md#statement) | From both original operator-norm-to-Hilbert bounds to the original closures and their adjoint domains. |
| [Finding](#finding) | [Normal strong-to-actual theorem](../../claims/Yin_C_F0070_v1.md#statement) | Part C applied to strong duals with the vacuum in their adjoint domains. |

---
author: Yin
---
# Independent review of the amplified two-point modulus derivation rank and normal encoding limits

## Whole-proof finding

At 2026-11-13T17:16 UTC a separately assigned agent completed independent review of the [statement](../../claims/Yin_C_F0232_v1.md#statement) and [argument](../../claims/Yin_C_F0232_v1.md#argument) of the [17:13 candidate](../../claims/Yin_C_F0232_v1.md#decision-candidate).
The reviewer had previously reviewed the distinct single nonnormal generator theorem C_F0225 and was familiar with its positive-modulus group-ring model and with compactness of normal laws.
The reviewer did not develop this matrix-amplified rank proof or its normal encoding exclusions, receive their development reasoning or access the development draft or prior findings on this candidate.
The complete fixed argument establishes the rank obstruction, all endpoint encoding exclusions and both kinds of moment-limit divergence.
The four declared inputs were checked at their stated uses.
The numerical comparison with published dimensions was checked separately at the cited source statements.

### Dense range and the matrix-amplified parameter count

Test the matrix-unit balancing identity on \(f=e_{ij}\).
Both its sides equal \(\sum_b e_{ib}\otimes e_{bj}\).
Applying \(x\otimes y\mapsto x\cdot\delta y\) on the right therefore gives \(\eta_0\cdot f+\delta f\), after division by \(k\), since \(\sum_{a,b}e_{ab}e_{ba}=k1\).
This verifies the sign of the inner correction.
The averaging action of \(Q\) sends a vector \(z\) to \(k^{-1}\sum_{a,b}e_{ab}\cdot z\cdot e_{ba}\).
Its image commutes with all matrix units by the same balancing identity, the action fixes a central vector, and its adjoint is itself.
Thus removal of \(Q\eta_0\) leaves the values of the inner derivation on \(F\) unchanged.
Only the \(k\) summands with \(a=b\) have nonzero product trace, each \(1/k^2\) before the outside \(1/k\), so \(\tau_{\mathcal B}Q=k^{-2}\), including \(Q=1\) for \(k=1\).

The residual derivative of either group generator commutes with \(F\) by differentiating its commutation with every \(f\in F\).
Since \(s\cdot w+w\cdot s=0\), left multiplication by \(s\) gives \(s\cdot w\cdot s=-w\).
The group projection \(P_-\) has product trace \(1/2\), and commutes and factors in trace with the matrix projection \(Q\).
The parameter space therefore has diagonal support \(1-Q,Q,QP_-\) with summed trace \(1+1/(2k^2)\).

Every entry in the derivative of a fixed word is an outer left or right multiplication by represented bounded elements, hence is a left matrix coefficient over \(\mathcal B\), including the two factors of the derivative of \(u^{-1}\).
It suffices that all actual parameters land in this matrix domain, irrespective of whether every abstract parameter is realized by a derivation.
For each normalized coordinate the corresponding unit column belongs to the actual range of \(CD\).
This range is invariant under right multiplication by \(\mathcal B\), whose vectors from the unit column are dense in the corresponding \(L^2\) coordinate.
The left rectangular matrix consequently has full final support \(I_d\), while its initial support is bounded by \(D\).
Applying the same finite trace on a common square amplification yields \(d\le1+1/(2k^2)<2\).
For a single normal generator its represented star algebra is commutative, whereas \(us\ne su\) in the group ring by reduced words.
The normalized derivations in the rank part need no adjoint or closability hypothesis.

### The zero endpoint and moving moment targets

For positive \(\varepsilon\), \(Z^*Z=\varepsilon^2p+1-p\) recovers \(p\) and \(Z(\varepsilon^{-1}p+1-p)\) recovers \(u\) at the star-polynomial level.
Also \(\operatorname{Re}Z,\operatorname{Im}Z\) recover \(Z,Z^*\), and the polar pair recovers \(p=(1-h_\varepsilon)/(1-\varepsilon)\) for the entire closed parameter range.
At zero only the real-imaginary pair needs a different test.
Its two kernel projections are exactly \(p=1-Z^*Z\) and \(upu^*=1-ZZ^*\), both in its own star algebra and of trace \(1/2\).
The derivation normalized at the first selfadjoint coordinate would give \(\delta Z=1\otimes1\).
Under actual ACSY it is closable by C_F0076, and C_F0216 forces its compressed tensor \(upu^*\otimes p\) to vanish.
The Hilbert norm of that tensor is \(1/2\), a contradiction entirely in the generated representation.

For a failure of divergence of the maximum vacuum norm there is an infinite subsequence with every coordinate norm bounded.
In the moving-pair case pass to a constant encoding type and a convergent subsequence of the parameters.
Norm continuity of \(h_\varepsilon,Z_\varepsilon\) and their real and imaginary parts gives convergence on every fixed star word, so the discrepancy hypothesis makes the actual laws converge to precisely that encoding.
Common coordinate cutoff and normality allow the normal-law closure assertion of C_F0201 v2, in the generated tracial representation.
The obtained actual ACSY contradicts the established exclusion, also for the singular zero real-imaginary target.
For a fixed amplified tuple no parameter selection is needed, and generation of the entire represented star algebra together with the faithful trace identifies the limiting represented law with the excluded target.
The conclusion concerns the maximum of the coordinate norms and requires no claim that each individual coordinate norm diverges.

### Published dimension comparison

The reviewer checked the displayed free-product formula in Lück, Example 1.38, and equations (2.12)–(2.13) of Connes and Shlyakhtenko, Proposition 2.3, in the cited project PDF editions.
The order-two factor has zeroth Betti number \(1/2\), the infinite cyclic factor has zero, and their first Betti numbers vanish, giving \(0,1/2\) in degrees zero and one for the free product.
The group-algebra formula and its selfadjoint generating hypothesis are explicit in Charlesworth and Nelson, Proposition 5.1, arXiv v2, p. 17, whose proof cites Mineyev and Shlyakhtenko for the nonmicrostates dimension equality.
A selfadjoint algebraic generating list is available as \(\operatorname{Re}u,\operatorname{Im}u,s\).
The normalized one-summand matrix case of Charlesworth and Nelson, Theorem 2.5, arXiv v2, p. 8, gives \(1+k^{-2}(3/2-1)\).
These inspections cover the stated comparisons and their hypotheses, without a new audit of the published dimension theorems.
The candidate's matrix-range calculation supplies its own obstruction for arbitrary complex generators and actual normalized derivations; the contextual dimension values provide no extension from a proper represented subalgebra.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0232_v1.md#statement) | All matrix sizes and arbitrary complex star generators, impossibility for normal star generators, both normal encoding families including zero, moving and fixed moment limits. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0232_v1.md#argument) | Matrix-unit averaging and inner correction, group support, dense rectangular range, normalized trace, endpoint kernels, moving parameter compactness, and contextual dimension identifications. |
| [Whole-proof finding](#whole-proof-finding) | [Positive two-point modulus](../../claims/Yin_C_F0225_v1.md#the-represented-coordinates-and-their-derivation) | Group-ring core recovered from \(Z,Z^*\) through \(p,h^{-1},u\) at \(0<\varepsilon\le1/2\). |
| [Whole-proof finding](#whole-proof-finding) | [Normal coordinate theorem](../../claims/Yin_C_F0076_v1.md#statement) | Item 1, closability of the normalized derivation under actual ACSY at a selfadjoint generator. |
| [Whole-proof finding](#whole-proof-finding) | [Kernel compression](../../claims/Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Outer derivative vanishes between the two actual kernel projections of the represented \(Z\). |
| [Whole-proof finding](#whole-proof-finding) | [Compact normal laws](../../claims/Yin_C_F0201_v2.md#statement) | Common cutoff, normality, uniform coordinate vacua and inheritance of actual ACSY in the generated tracial representation at a fixed moment cluster law. |

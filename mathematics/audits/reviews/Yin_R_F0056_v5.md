---
author: Yin
---

# Self-review of the Kato proof for the sandwich example

Date: 2026-11-22T09:27, UTC.
Human record author: Yin.

The agent preparing v5 performed this self-review with the manuscript discussion, the Kato and Voiculescu source units, and the v4 proof and review available.
The check covers the new construction and its composition with the retained bounded-dual argument.

<a id="kato-sandwich-finding"></a>
## Finding

Formula (2.2) of the published Kato article applies to bounded selfadjoint multiplication by \(t\) and to the projection \(P_1\).
The adjoint \(E_X(I)P_1\) has norm \(\|E_X(I)1\|_2\), and the density bound gives \(\mu(I)\leq4|I|\).
Since the positive commutator is \(P_1=P_1^{1/2}\), Theorem (6.2) and its sufficiency proof apply with squared smoothness norm at most \(4\).
The positive solution has spectrum in \([0,8\pi]\), so subtracting \(4\pi I_K\) gives the norm bound and leaves the commutator unchanged.
Multiplication by \(i\) gives the generator-first equation \([X,T_0]=P_1\).

Voiculescu's §5.5 applies to the two pointed \(L^2\) spaces since the represented trace and the vector \(1\) give the free product on \(H\).
The cross commutator with \(S\) vanishes.
The same-factor commutator is the extension by zero of \([X,T_0]\) from the vacuum-plus-first-factor subspace, with the two copies of the vacuum identified.
The tensor model has the same right creation operator as v4.
The only nonzero component of \([S,r]\) is \(l^*r=P_1\) on \(H_0\), where \(rl^*=0\).

For the transfer, the two commutators of the new \(T\) give \([Y,T]=XSP_\Omega+P_\Omega SX\).
The normalized tracial state makes \(\|\Omega\|=1\), and \(Xq=\Omega\) converts the weighted rank-one operator into \(P_\Omega\) by two-sided multiplication by \(X\).
Injectivity and dense range give the reverse implication, and the right multiplications cancel the two terms of \([Y,T]\) with the v4 orientations.
The second-dual calculation in v4 uses \(\|q\|_2^2=2\) and the same row \(L^2\) bound for \(k\), with \(R^*-R\) giving the required commutator sign.
The domain argument for \(QrQ\) uses \(Qr\) appending \(q\); its values on concentrated functions show unboundedness.
The bounded spectral cutoffs verify the generation claim.
These interfaces and the new scalar step supply the v5 statement.
The norm separation used in Example 6.3 is covered by the separate [v1 finding](Yin_R_F0056_v1.md#main-counterexample-finding).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Kato sandwich finding](#kato-sandwich-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Kato sandwich finding](#kato-sandwich-finding) | [v5 statement](../../claims/Yin_C_F0012_v5.md#statement) | Transfer with the unit tracial vacuum, bounded duals and direct unbounded composition in the example. |
| [Kato sandwich finding](#kato-sandwich-finding) | [v5 argument](../../claims/Yin_C_F0012_v5.md#argument) | Smoothness bound, centering, normalization, free-product lift, both transfer interfaces and generation. |
| [Kato sandwich finding](#kato-sandwich-finding) | [Kat68-U001](../literature/Kat68/Yin_U001.md#kat68-u001) | Application of published (2.2), Theorem (6.2) and the positive-solution bound on p. 545. |
| [Kato sandwich finding](#kato-sandwich-finding) | [Voi98-U005](../literature/Voi98/Yin_U005.md#free-products-55-58) | Right lift, the vacuum-plus-first-factor embedding and the cross-factor commutator. |
| [Kato sandwich finding](#kato-sandwich-finding) | [v4 argument](../../claims/Yin_C_F0012_v4.md#argument) | Rank-one equivalence, right-multiplier correction, inverse weights and the bounded second-dual construction, within the scope of the [v4 self-review](Yin_R_F0056_v4.md#sandwich-coordinate-change-finding). |

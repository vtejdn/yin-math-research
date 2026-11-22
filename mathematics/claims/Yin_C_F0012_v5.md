---
author: Yin
---

# Counterexamples with bounded dual systems

This proof of the bounded-dual part of the [selfadjoint example in v1](Yin_C_F0012_v1.md#statement) uses Kato's positive commutator theorem for the scalar factor.
It replaces the weighted Hilbert-transform step used in [v4](Yin_C_F0012_v4.md#original-free-pair-and-the-inverse-weights) and retains the coordinate change, inverse weights and last-two-factor kernel from that proof.
This proof was used for the bounded duals in an earlier version of [F0001's example on bounded division closures](../manuscripts/Yin/Yin_T_F0001/readme.md#mathematical-provenance).
The [norm-separation argument in v1](Yin_C_F0012_v1.md#6-exclusion-from-the-norm-closed-and-scalar-division-algebras) supplies the other part of the example.

## Current assessment
[Selected decision](Yin_C_F0012_v3.md#decision-quadratic-independently-reviewed)

## Statement

Let \((M,\tau)\) be a von Neumann algebra with faithful normal tracial state, let \(H=L^2(M,\tau)\) with unit vector \(\Omega=1\), and let \(P_\Omega\) project onto \(\mathbb C\Omega\).
The inner product is linear in the second variable.
Let \(X,S\in M\) be selfadjoint, with \(X\geq0\) injective and \(q:=X^{-1}\Omega\in H\).
Put \(Y=XSX\), and suppose \(T\) is bounded with \([X,T]=P_\Omega\) and \([S,T]=0\).
A bounded \(D_2\) commuting with \(X\) satisfies \([Y,D_2]=P_\Omega\) if and only if
\[
 [S,D_2]\xi=q\langle q,\xi\rangle
\]
on \(H\).
In that case, with \(\rho(a)\) denoting right multiplication by \(a\), the pair \((D_1,D_2)\) is a generator-first dual system for \((X,Y)\), where
\[
 D_1=T-\rho(XS)D_2-D_2\rho(SX).
\]

In the selfadjoint example, \(X\) has law \(d\mu(t)=4t^3\,dt\) on \((0,1)\), \(S\) is a standard semicircular element free from \(X\), and \(M=W^*(X,S)\).
For this pair \(W^*(X,Y)=M\), and there are bounded \(T,D_2\) with the stated properties.
In the tensor realization below, \(r\) appends the vector \(1\) at the right end, and \(\rho(X)^{-1}r\rho(X)^{-1}\) is unbounded on its natural domain.

## Argument

### The scalar dual from Kato's theorem

On \(K=L^2((0,1),\mu)\) let \(X\) act by coordinate multiplication, and let \(P_1\) project onto the constant functions.
For any bounded interval \(I\), the spectral projection \(E_X(I)\) gives
\[
 \|P_1E_X(I)\|^2=\|E_X(I)1\|_2^2=\mu(I)\leq 4|I|.
\]
The squared \(X\)-smoothness norm of \(P_1=P_1^{1/2}\) is therefore at most \(4\) by [Kato's formula (2.2), p. 536](../audits/literature/Kat68/Yin_U001.md#t-smoothness).
Apply [Kato's Theorem (6.2), p. 543](../audits/literature/Kat68/Yin_U001.md#kat68-u001) with selfadjoint operator \(X\) and positive commutator \(P_1\).
Its sufficiency proof on p. 545 gives a bounded selfadjoint \(B\) with \(i[X,B]=P_1\) and \(0\leq B\leq 8\pi I_K\).
Consequently
\[
 T_0=i(B-4\pi I_K),\qquad [X,T_0]=P_1,\qquad \|T_0\|\leq4\pi .
\]

### The dual system for the free pair

The pointed factors are \(K\) and \(L^2(W^*(S),\tau)\), each pointed by \(1\).
Their reduced free product is \(H\) because \(X,S\) are free and generate \(M\).
By [Voiculescu's right free-product representation, §5.5](../audits/literature/Voi98/Yin_U005.md#free-products-55-58), the lift \(T\) of \(T_0\) commutes with left multiplication by \(S\).
The same-factor commutator is
\[
 [X,T]=V[X,T_0]V^*=VP_1V^*=P_\Omega ,
\]
where \(V:K\to H\) is the inclusion of the vacuum-plus-first-factor space.
The right lift is norm preserving, so \(\|T\|\leq4\pi\).

In the [tracial tensor model of v1](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model), \(H=\bigoplus_{n\geq0}H_n\) with \(H_n=K^{\bar\otimes(n+1)}\).
The vacuum is \(1\) in \(H_0\), and \(X\) and \(\rho(X)\) multiply the first and last factors by the coordinate, respectively.
Here \(S=l+l^*\), where \(l\) prepends \(1\) and \(l^*\) contracts the first factor on positive degrees and vanishes on \(H_0\).
The right creation \(r\) commutes with \(X\) and \(l\).
The two orders of applying \(r\) and \(l^*\) agree on positive degrees, while \(l^*r=P_1\) and \(rl^*=0\) on \(H_0\).
Thus \([S,r]=P_\Omega\), and \((T,r)\) is a bounded dual system for \((X,S)\).

### The change of generators and the bounded second dual

The [rank-one equivalence and first-dual correction in v4](Yin_C_F0012_v4.md#the-rank-one-commutator-after-the-change-of-generators) give the general assertion of the statement.
They use only the boundedness of \(T\) and its two commutators with \(X,S\), so they apply to the right lift above.

In the concrete example, \(X\) is injective because \(\mu(\{0\})=0\) and \(\tau\) is faithful.
Here \(q(t)=t^{-1}\) on \(H_0=K\), with \(\|q\|_2^2=4\int_0^1t\,dt=2\).
The direct inverse-weight transport is \(QrQ\), where \(Q=\rho(X)^{-1}\).
The [inverse-weight calculation in v4](Yin_C_F0012_v4.md#original-free-pair-and-the-inverse-weights), starting with \(q(t)=1/t\), applies to the same \(Q,r\).
Its domain is \(\operatorname{Dom}Q\), since \(Qr\) appends \(q\), and \(QrQf=(qf)\otimes q\) for bounded \(f\) on \(H_0\).
Unit vectors supported where \(t\leq\varepsilon\) give the lower bound \(\|q\|_2/\varepsilon\) for these images, proving unboundedness.

The [bounded second-dual construction in v4](Yin_C_F0012_v4.md#the-bounded-second-dual) uses the same \(q,\mu\) and this tensor model.
It splits \(q(s)q(t)\) into \(k(s,t)+k(t,s)\) almost everywhere with \(k(s,t)=1_{\{t\leq s\}}/(st)\).
The resulting bounded \(R\), acting on the last two factors in positive degrees, gives \(D_2=R^*-R\) with \([X,D_2]=0\) and \([S,D_2]=q\langle q,\cdot\rangle\) on \(H\).
These are precisely the hypotheses of the transfer with the \(T\) constructed above.

Finally \(a_\varepsilon=X^{-1}1_{[\varepsilon,1]}(X)\) is bounded and belongs to \(W^*(X)\).
The equality \(a_\varepsilon Y a_\varepsilon=1_{[\varepsilon,1]}(X)S1_{[\varepsilon,1]}(X)\) gives strong convergence to \(S\) because \(1_{[\varepsilon,1]}(X)\rightarrow1\) strongly as \(\varepsilon\rightarrow0\).
This proves \(W^*(X,Y)=W^*(X,S)\).

## Assessment history

### Decision kato-scalar-dual

| Field | Value |
| --- | --- |
| date | 2026-11-22T09:27 |
| status | proved |
| reason | The self-review verifies the Kato norm and sign, the right free-product lift and the application of the fixed transfer and second-dual calculations to this lift. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized tracial transfer, concrete bounded duals and unbounded direct inverse-weight composition. |
| argument | [Argument](#argument) | Scalar positive commutator, free-product lift and assembly of the transfer. |
| support | [Kat68-U001](../audits/literature/Kat68/Yin_U001.md#kat68-u001) | Published formula (2.2), Theorem (6.2) and its sufficiency estimate for the positive projection \(P_1\). |
| support | [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Right lift and same- and different-factor commutator identities in §5.5. |
| support | [v1 tracial tensor model](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | The same measure, semicircular creation space and represented tracial space. |
| support | [v4 rank-one calculation and correction](Yin_C_F0012_v4.md#the-rank-one-commutator-after-the-change-of-generators) | Bounded-operator transfer with the newly obtained \(T\). |
| support | [v4 original free pair and inverse weights](Yin_C_F0012_v4.md#original-free-pair-and-the-inverse-weights) | Domain and unboundedness of \(QrQ\) for the verified right creation operator. |
| support | [v4 bounded second dual](Yin_C_F0012_v4.md#the-bounded-second-dual) | The last-two-factor construction for the same \(\mu,q\) and representation. |
| review | [Self-review of the Kato proof](../audits/reviews/Yin_R_F0056_v5.md#kato-sandwich-finding) | Scalar step, lift and exact interfaces with the retained v4 argument. |

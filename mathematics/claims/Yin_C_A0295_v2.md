---
author: Yin
---

# Bounded commutator witnesses for two original Schur kernels

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity, let \(P(z)=Az+B,\ Q(z)=Cz+D\) be complex two-square linear pencils, and put \(K_\nu=P(t)-\nu sQ(t)\).
Suppose two distinct nonzero parameters \(\lambda,\mu\) give positive noninteger regular nullities summing to one.
Fix the input coordinates, choose a nonzero first-column pivot at each parameter, and write \(\sigma_\nu\) for the corresponding Schur scalar.
Let \(p_\nu\) be its orthogonal kernel projection in \(\mathcal N(H)\).
Both projections belong to the second scalar inverse layer of the original group.
No closed-range condition is needed on the pivot or the rectangle.

For each \(\nu=\lambda,\mu\) there are two ordinary rank-two operators \(T_{s,\nu},T_{t,\nu}\) on the original \(\ell^2(H)\) with
\[
   [\rho_s,T_{s,\nu}]+[\rho_t,T_{t,\nu}]=u_\nu P_e v_\nu,\qquad
   {\rm supp}_r u_\nu=1-p_\nu,\quad {\rm supp}_l v_\nu=p_\nu .
\]
Here \(P_e\) projects onto the identity vector and \(\rho_g\) denotes right multiplication.
The output has ordinary rank one, with left translation spans \(L^2(\mathcal N(H))(1-p_\nu)\) and \(L^2(\mathcal N(H))p_\nu\) on its two legs.
Each input is a sum of two tensors with bounded left factors in the first inverse layer and bounded right factors in the second.
A single positive scalar inverse from the group ring suffices for all first-layer expressions below, and one further bounded inverse of a positive affiliated scalar suffices jointly for the right factors and both orthogonal projections.

If a sign character fixes \(t\), negates \(s\), and \(K_1\) has half nullity, the assertion applies to \(1,-1\).
For the automorphism \(\iota\) induced by that sign, the first-layer algebraic idempotent \(e\) giving the Schur kernel satisfies
\[
                  [1]=[e]+\iota_*[e]\quad\text{in } K_0(D_1(H)).
\]
In particular any \(\iota_*\)-invariant integer-valued homomorphism taking odd value on the unit excludes this sign case.
The equation gives divisibility by two in the coinvariants of this action.

## Two orthogonal range projections in one further inverse

Use the [common kernel coordinate](Yin_C_A0330_v1.md#the-common-kernel-coordinate-and-the-inner-rank).
There is a single column \(Z=(z,1)^{\mathsf T}\) and there are two complementary algebraic idempotents \(e_\lambda,e_\mu\) with \(\ker K_\nu=Z e_\nu U(H)\).
The second coordinate identifies \(\ker\sigma_\nu=e_\nu U(H)\) for the chosen pivot.
All these data use the inverse of one nonzero group-ring scalar.
If the other input coordinate is desired, one may permute the two columns in both pencils first.
The dimension of the image of \(e_\nu\) is the nullity at that parameter.

Write \(e=e_\lambda\) and
\[
      G_e=1-(e-e^*)^2=e e^*+(1-e^*)(1-e).
\]
It is at least one as a positive affiliated scalar since \(e-e^*\) is skew adjoint.
The first summand supports the image of \(e\), which equals \(\ker(1-e)\).
The second supports its orthogonal complement.
Thus \(p_\lambda=e e^* G_e^{-1}\) by the [range projection formula](Yin_C_A0282_v1.md#recovering-the-scalar-idempotent-from-the-schur-coordinate).
The expression \(1-(e-e^*)^2\) is unchanged on replacing \(e\) by \(1-e\), so \(p_\mu=e_\mu e_\mu^* G_e^{-1}\).
The orthogonal range projections need not be complementary for two oblique idempotents.
In the sign case the explicit odd involution in the [scalar norm](Yin_C_A0330_v1.md#the-scalar-norm-on-the-sign-kernel) gives \(e=(1+Vs^{-1})/2\) and \(\iota(e)=1-e\).
The direct-sum identity for the projectives of complementary idempotents proves the \(K_0\) assertion.

## Two bounded tensors for each label

For each parameter permute the output rows, if necessary, to place its chosen pivot in position \((1,1)\).
Use those row-permuted pencils in the calculation for that parameter.
Write \(K_\nu=\left(\begin{smallmatrix}a&b\\ c&d\end{smallmatrix}\right)\), \(\ell=(-ca^{-1},1)\) and \(z_\nu=Z e_\nu\).
Thus \(K_\nu z_\nu=0,\ (z_\nu)_2=e_\nu,\ \ell K_\nu=(0,\sigma_\nu)\).
With \(\Psi_g(x\otimes y)=xg\otimes y-x\otimes gy\), balancing at each matrix entry gives
\[
 \begin{split}
 \sigma_\nu\otimes e_\nu
   &=-\nu\,\Psi_s\!\left(\sum_{i=1}^2\ell_i\otimes(Q(t)z_\nu)_i\right)\\
   &\quad+\Psi_t\!\left(\sum_{j=1}^2
              (\ell(A-\nu s C))_j\otimes(z_\nu)_j\right).
 \end{split}
\]
This is the [two-label balance](Yin_C_A0295_v1.md#a-balance-with-the-specified-two-labels) obtained by first cutting each mixed word between \(s\) and \(t\).
The equality uses the actual kernel idempotent at this parameter and the same \(Z\) for both parameters.

For the left multiplier put \(J_\nu=(1+xx^*)^{-1}\), \(x=ca^{-1}\).
Then \(J_\nu=1-c(a^*a+c^*c)^{-1}c^*\) and \(J_\nu x=c(a^*a+c^*c)^{-1}a^*\).
Both are bounded, so multiplying the outer left legs by \(J_\nu\) gives bounded factors, including \(u_\nu=J_\nu\sigma_\nu=J_\nu d-(J_\nu x)b\).
For the outer right legs, stack all entries of the columns \(z_\nu,Q(t)z_\nu\) at the two parameters in a single column \(B_0\) and put \(G_z=1+B_0^*B_0\).
The entries of \(B_0 G_z^{-1}\) are bounded, and \(v_\nu=e_\nu G_z^{-1}\) is among them.
Multiplying the outer tensor legs as indicated commutes with both balancing operations.
The [regular tensor identification](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) now yields the two commutators in the statement.
Among the two outside affiliated units, the first preserves \(\ker\sigma_\nu\) and the second preserves the affiliated image of \(e_\nu\).
Thus the two bounded output factors have the claimed supports.
Their positive support dimensions give a rank-one output.
Each input has rank at most two by the displayed sums, and the [small-input exclusion](Yin_C_A0166_v2.md#statement) forces both to have rank exactly two.

Finally take an ordered product \(g\) of the common group-ring denominator for \(Z,e_\nu\), both chosen nonzero pivots, and the two nonzero group-ring scalars \(a^*a+c^*c\) for the left legs.
The ring generated by the group ring and the single positive scalar inverse \((g^*g)^{-1}\) is closed under adjoints.
It contains \(g^{-1}=(g^*g)^{-1}g^*\), hence the inverse of each factor by multiplying by the suffix on the left and the prefix on the right.
This supplies all the first-layer expressions, including \(G_e,G_z\).
For the second step take \(g_1=G_e G_z\).
Its affiliated inverse is bounded since both inverse factors are contractions.
Adjoining \((g_1^*g_1)^{-1}\), a bounded positive inverse, recovers \(G_e^{-1},G_z^{-1}\) by the same factor argument.
This proves the asserted joint control of the inverse layers.

## Assessment history

### Decision bounded-rank-one-outputs-for-both-schur-kernels

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | The complementary algebraic idempotents give both original orthogonal projections and bounded rank-two commutator inputs with the specified support traces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two bounded outputs, shared inverse layers and sign coinvariants. |
| argument | [Two orthogonal range projections in one further inverse](#two-orthogonal-range-projections-in-one-further-inverse) | Exact range projections of both complementary algebraic idempotents. |
| argument | [Two bounded tensors for each label](#two-bounded-tensors-for-each-label) | The splitting at two actual labels, bounded legs, exact ranks and both inversions. |
| review | [Bounded rank-one outputs for both Schur kernels](../audits/reviews/Yin_R_A0227_v1.md#bounded-rank-one-outputs-for-both-schur-kernels) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-bounded-rank-one-outputs-for-both-schur-kernels)

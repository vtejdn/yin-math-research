---
author: Yin
---
# Boundedness does not preserve the von Neumann module conclusion

Record kind: research operation.
Date and owner: 2026-10-16T01:22, Yin; complete local hypothesis check by the authoring AI agent.
This record retains the failed boundedness substitution, a complete counterexample and the exact conclusion that survives.
The argument is locally self-reviewed; no independent review, fixed Claim assessment change or manuscript edit is claimed.

## Current proof home

The complete original argument and its original dates, local-check statements and earlier review descriptions remain below.

## Question and reused inputs

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, let H=L2(M,tau), and identify M with M Omega.
Suppose x_1,...,x_m in M are normal, the maps E_i:M to H are bounded, and A_i in B(H) preserve M Omega and commute with every x_j.
Suppose B in B(H) satisfies
\[
 \sum_i [[E_i,x_j],A_i]=[B,x_j]\qquad(1\le j\le m)
\]
on M Omega.
The proposed conclusion is that
\[
 T:=\sum_i[E_i,A_i]-B|_{M\Omega}
\]
is a left W*(x_1,...,x_m)-module map.
The check asks whether taking normal parts allows boundedness of the E_i to replace ultraweak-to-weak continuity.

The [bounded-map Fuglede interface](../audits/literature/CS77/Yin_U001.md#cs77-u001) and the [normal-part construction](../claims/Yin_C_F0132_v1.md#1-the-normal-part-and-source-interface) are reused at their recorded scopes.
The normal central-summand interface is retained in [Bla06-U002](../audits/literature/Bla06/Yin_U002.md#bla06-u002).
The [CS89 normal-part and balancing interface](../audits/literature/CS89/Yin_U001.md#cs89-u001) explicitly extends relations for the normal part, rather than identifying an arbitrary form with that part.
Local searches in F-line Claims, drafts and ledger records for singular module maps, ultrafilters and normal-part commutator obstructions found no existing record of the counterexample below.
The published CS77 and CS89 passages were reread; no new external result or source artifact is adopted.

## What boundedness still proves

The map on M induced by each A_i is bounded by the closed graph theorem.
Indeed, if z_n tends to z in M norm and A_i(z_n Omega)=y_n Omega with y_n tending to y in M norm, boundedness of A_i on H gives y Omega=A_i(z Omega).
Faithfulness identifies y with the induced image of z.
Consequently E_i A_i, A_i E_i and T are bounded from M to H.

The matching identities and Jacobi give
\[
 [T,x_j]
 =\sum_i[[E_i,A_i],x_j]-[B,x_j]
 =\sum_i[[E_i,x_j],A_i]-[B,x_j]=0.
\]
The bounded-map Fuglede implication gives [T,x_j*]=0.
Products, linear combinations and norm closure therefore give
\[
 T(az)=aTz
 \qquad(a\in C^*(1,x_1,\ldots,x_m),\ z\in M).
\]
This argument alone does not pass to the von Neumann closure.

Write T_n for the normal part of T and S:=T-T_n.
Compatibility of the normal-part construction with left multiplication gives [T_n,x_j]=0 and [S,x_j]=0.
The map T_n is ultraweak-to-weak continuous, so Fuglede followed by ultraweak closure makes it W*(x_1,...,x_m)-linear.
The map S is bounded and C*(1,x_1,...,x_m)-linear, but need not be W*(x_1,...,x_m)-linear.
The following example has T_n=0 and S=T.

## Counterexample with one selfadjoint generator

Let
\[
 M:=\ell^\infty(\mathbb N_0),\qquad
 \tau(a):=\sum_{n=0}^\infty 2^{-n-1}a_n,\qquad
 H:=L^2(M,\tau),\qquad \Omega:=1.
\]
This is a finite commutative von Neumann algebra with faithful normal probability trace.
Set
\[
 x:=(0,1,1/2,1/3,\ldots),\qquad
 p:=(1,0,0,\ldots).
\]
The element x is selfadjoint and p=1_{\{0\}}(x).
Every coordinate projection is a Borel spectral projection of x, so W*(x)=M.

Fix a nonprincipal ultrafilter U on the positive integers and put
\[
 \phi(a):=\lim_{n\to U}a_n.
\]
Ultrafilter limits of bounded complex sequences are linear and positive, with norm one, and agree with the ordinary limit whenever it exists.
In particular, phi(1)=1 and phi vanishes on c_0.

Define on M Omega
\[
 E(a\Omega):=\phi(a)p\Omega,\qquad A:=L_p,\qquad B:=0.
\]
Then
\[
 \|E(a\Omega)\|_2
 \le \|p\Omega\|_2\,\|a\|
 =2^{-1/2}\|a\|.
\]
Thus E is bounded from M to H.
The operator A is an orthogonal projection in B(H), preserves M Omega and commutes with x.

For every a in M, xa belongs to c_0 and xp=0.
It follows that
\[
 E(xa\Omega)=0=xE(a\Omega),
 \qquad [E,x]=0.
\]
Hence the required matching identity holds with one E, one A and one x:
\[
 [[E,x],A]=0=[B,x].
\]

Since pa has finite support and Ap=p,
\[
 EA=0,\qquad AE=E,\qquad T=[E,A]-B=-E.
\]
But
\[
 T(p\Omega)=0,\qquad pT(\Omega)=-p\Omega\ne0.
\]
Since p belongs to W*(x), the proposed module conclusion fails.

The example even has A in M acting by left multiplication and E(M Omega) contained in M Omega.
It therefore refutes the proposed relaxation before using the extra freedom of arbitrary bounded A_i preserving M Omega.
It uses a spectral atom at zero, which is permitted by the stated normal-generator hypotheses.

## The surviving singular part

The positive functional phi vanishes on every coordinate projection.
Its positive normal part is dominated by phi and must therefore vanish on every coordinate projection, hence everywhere.
Thus E_n=0 and T_n=0.
All of T=-E is the singular remainder that the normal-part substitution would lose.

There is also a direct continuity check.
For q_N:=1_{\{0,\ldots,N\}}, one has q_N increasing ultraweakly to 1, while E(q_N Omega)=0 and E(Omega)=p Omega.
The needed continuity is genuinely absent.

The precise spectral-projection obstruction can be seen within continuous functional calculus.
Put f_k(t):=max(1-kt,0) for t in the nonnegative spectrum of x.
Then f_k(x) converges strongly to p, but
\[
 \phi(f_k(x))=1,\qquad
 E(f_k(x)\Omega)=p\Omega,\qquad E(p\Omega)=0.
\]
Thus C*(1,x)-linearity cannot be extended through this approximation.
In particular p is not in C*(1,x), since continuous functions on the spectrum have their values at 1/n converge to their value at zero.

## Normal parts and general precomposition

For the general A_i permitted in the question, normality of the induced map does not by itself give
\[
 \mathcal N(EA_i)=\mathcal N(E)A_i.
\]
This additional issue is distinct from the counterexample, which already uses a left multiplier and does not need it.

For an explicit check, keep M and E above and take A_0:=P_Omega.
Its induced map on M is a->tau(a)1, which is ultraweakly continuous, and A_0 preserves M Omega.
Nevertheless
\[
 (EA_0)(a\Omega)=\tau(a)p\Omega
\]
is nonzero and ultraweak-to-weak continuous.
Therefore
\[
 \mathcal N(EA_0)=EA_0\ne0=\mathcal N(E)A_0.
\]
If a commuting generator is required for this auxiliary example, take the generator to be zero.
The normal-part construction commutes with precomposition by left or right multiplication, as proved in C_F0132, but not with every ultraweakly continuous map M to M.
Taking the normal part of T as a whole avoids this unjustified interchange, yet still leaves the non-module singular remainder demonstrated above.

## Consequence and limits

Boundedness of the E_i guarantees C*(1,x_1,...,x_m)-linearity of T and W*(x_1,...,x_m)-linearity of its normal part.
It does not guarantee the original W*(x_1,...,x_m)-module conclusion.
The normal-part reduction for an adjoint commutator uses a different cancellation: a bounded difference commuting with x also commutes with x* by Fuglede.
No corresponding cancellation removes sum_i[S_i,A_i] under the present assumptions.

The current continuity hypothesis must not be weakened to boundedness on the basis of that reduction.
The counterexample and all operator-domain checks above were verified locally.
No statement about a separately strengthened diffuse-spectrum version, and no independent mathematical review, is made.
The manuscript was not modified.

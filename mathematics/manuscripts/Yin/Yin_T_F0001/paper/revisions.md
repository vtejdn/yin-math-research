# Section 6 revision suggestions

These optional changes replace arguments in [Section 6](sections/examples.tex) using the results checked in the [literature search](literature-seek.md).

## Example 6.1

Replace the odd-moment convolution argument in `ex:liberation-without-duals` by a resolvent argument if adopting the cited arcsine Cauchy transform.
For $r>1$, the bounded operator $R_r=(r-X)^{-1}\in M$ preserves $M\Omega$.
Applying the commutator product rule to $(r-X)R_r=1$ on $M\Omega$ gives $(r-X)[R_r,D]=P_\Omega R_r$, hence $[R_r,D]=R_rP_\Omega R_r$.
Consequently $(r-1)\langle\Omega,[R_r,D]\Omega\rangle=(r-1)\tau(R_r)^2=1/(r+1)$ by the cited formula.
For each $t\in(-1,1)$, the function $(r-1)/(r-t)$ takes values in $[0,1]$ and tends to zero as $r\downarrow1$, so dominated convergence gives $\|(r-1)R_r\Omega\|_2\to0$.
By selfadjointness of $R_r$ and the domain conditions on $D,D^*$, the absolute value of $(r-1)\langle\Omega,[R_r,D]\Omega\rangle$ is at most $(\|D\Omega\|_2+\|D^*\Omega\|_2)\|(r-1)R_r\Omega\|_2$, which contradicts the limit $1/2$.

## Example 6.2

In `ex:normality`, the exclusion of finite-rank solutions after the construction of $L=P_\Omega$ follows from Theorem 1.7, assertions (1) and (2), and the already established $c^*\notin\operatorname{Div}_{L^0(M)}\mathbb C[c]$.
This replaces the separate argument using Lemma 5.3 and the nonvanishing of $s[P_\Omega,c^*]t$.
Use assertion (2) to conclude that no fraction pair admits a finite-rank solution, since that assertion requires existence for some fraction pair.

## Example 6.3

- In `ex:bounded-rational-closure`, set $N=W^*(X,Y)$ and use the bicommutant theorem in place of the strong approximation by $a_\varepsilon Y a_\varepsilon$.
  For $B\in N'$, the relation $X[B,S]X=[B,Y]=0$ implies $[B,S]=0$ because $X$ is injective with dense range.
  This gives $S\in N''=N$.
  Retain the identity $S=X^{-1}YX^{-1}$ in $L^0(M)$ to exhibit rational membership there.
- Apply spectral permanence to the unital inclusion $M_n(C^*(X,Y))\subseteq M_n(M)$ for every $n$.
  It gives inverse closure at all matrix sizes in place of the proof with $B^*B$ and continuous functional calculus.
  Use this to conclude $\operatorname{Rat}_M A\subseteq C^*(X,Y)$.
- After constructing the scalar dual $T_0$ on $L^2(W^*(X))$, apply Voiculescu's free-product lifting in §5.5 of Voi98 to $W^*(X)*W^*(S)$.
  The lift $T$ satisfies $[X,T]=P_\Omega$ and $[S,T]=0$ by the same-factor and cross-factor commutator identities, respectively.
  This replaces the verification of these identities on the graded Hilbert space for the lift of $T_0$.
  The boundedness and the scalar commutator of $T_0$ established using the Hilbert transform supply the input.

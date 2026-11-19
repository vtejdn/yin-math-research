# Current writing opinions

This review covers the proof exposition in Sections 5 and 6.
See [Yin's proof readability guidance](../../../../../profiles/Yin/writing/readme.md#proof-readability).

## Why multiplication preserves rank in Lemma 5.1

Optional clarification at “These multiplications preserve the rank” in the proof of `lem:fraction-ranks`.
For \(S\in\mathcal F(H)\), the subspace \(S(pH)\) is dense in the finite-dimensional space \(S(H)\) because \(pH\) is dense in \(H\).
Hence \(S(pH)=S(H)\), and the injectivity of \(x\) gives \(\operatorname{rank}(xSp)=\operatorname{rank}S\).
See [Section 5](sections/dual-system-criterion.tex).

## The evaluation of the tensor sum in Lemma 5.2

Clarify how the map \(c\otimes e^{\mathrm{op}}\mapsto cD_i(e\xi)\) acts on the left side of the tensor equality in the proof of `lem:finite-rank-identification`.
The simple-tensor calculation gives the evaluated sum \(\sum_j\delta_{ij}\Theta(\ell_j')\xi=\Theta(\ell_i')\xi\), which makes the use of the dual relation explicit.
Then use the bimodule identity for \(\Theta\) to give \(\Theta(\ell_i')=s'\Theta(\ell_i)t'=-s'T_it'\).
See [Section 5](sections/dual-system-criterion.tex).

## The two norms in the closed graph argument in Lemma 5.4

Optional clarification at “The graph of \(T:\mathcal M\to H\) is norm closed” in the proof of `lem:module-commutation`.
If \(z_n\to z\) in the operator norm of \(\mathcal M\), then \(\|(z_n-z)\Omega\|_2\leq\|z_n-z\|\), so \(z_n\Omega\to z\Omega\) in \(H\).
If also \(T(z_n\Omega)\to\eta\) in \(H\), closedness of \(\overline T\) gives \(\eta=T(z\Omega)\).
This connects the closure on \(H\) to the norm required by the closed graph theorem on \(\mathcal M\).
See [Section 5](sections/dual-system-criterion.tex).

## The scalar shift and fraction identities in Lemma 5.5

At the start of the proof of `lem:fundamental`, use \(eX_i=X_ie=\lambda e\) to display \(e[X_i,D_i]e=\lambda eD_ie-\lambda eD_ie=0\) on \(\mathcal M\Omega\).
Evaluating \(eP_\Omega e=0\) at the vacuum gives \(\langle\Omega,eP_\Omega e\Omega\rangle=|\tau(e)|^2=0\), so faithfulness gives \(e=0\).
This exhibits how the dual relation eliminates the spectral atom.

In the proof that \(\Gamma[Q,C]\xi=0\), state that \(C\) commutes with all left multipliers by Lemma 5.4 because the normal \(X_j\) generate \(\mathcal M\) and \([X_j,C]=0\) on \(\mathcal M\Omega\).
As in Lemma 5.1, display the fraction calculation \(sb=s(ut)=(su)t=at\) in \(L^0(\mathcal M)\).
At the end, the sum \(\sum_i L_i=P_\Omega\) is evaluated at the two vectors \(b\xi,t\xi\in\mathcal M\Omega\), giving \(\sum_i\overline{\Gamma[Q,L_i]}\xi=sP_\Omega b\xi-aP_\Omega t\xi\).
See [Section 5](sections/dual-system-criterion.tex).

## The vacuum estimate in Remark 6.1

In `rem:liberation-without-duals`, display the pairing before applying Cauchy–Schwarz.
\[
 \langle\Omega,[X^{2n+1},D]\Omega\rangle
 =\langle X^{2n+1}\Omega,D\Omega\rangle-\langle D^*\Omega,X^{2n+1}\Omega\rangle.
\]
This shows where the two domain conditions are used in the contradiction.
See [Section 6](sections/examples.tex).

## The space and commutators in Remark 6.2

When introducing \(D\in\mathcal B(H)\) in `rem:normality`, identify \(\mathcal M=W^*(c)=W^*(S_1,S_2)\) and state that the full Fock space is \(H=L^2(\mathcal M,\tau)\) in the standard realization with the vacuum trace.
The source for this realization is listed in [the citation map](../citation.md#voi98).

To relate the noncommutation of \(c^*\) with \(c\) to rationality, note that the elements of \(L^0(\mathcal M)\) commuting with \(c\) form a unital subalgebra closed under inversion in \(L^0(\mathcal M)\).
In the final nonvanishing argument, evaluate \([P_\Omega,c^*]\Omega=-c^*\Omega\ne0\) using \(\tau(c^*)=0\).
See [Section 6](sections/examples.tex).

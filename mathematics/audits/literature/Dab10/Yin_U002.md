---
author: Yin
---

<a id="dab10-u002"></a>
# Dab10-U002: Vacuum Contractions, Their Domains, and Bounded Duals

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Source: Dab10, the same [arXiv:0804.2906v2](https://arxiv.org/abs/0804.2906v2) identified in [U001](Yin_U001.md#dab10-u001); [primary 12-page PDF](https://arxiv.org/pdf/0804.2906). |
| source-locator | Coverage: Lemma 10 and Remark 11, PDF/printed p. 8; their displayed calculation and Lemma 12 with its proof, p. 9. |
| inspection | Method: the complete selected passages were read in parsed primary text and reconstructed below, with adjoints and limiting domains made explicit. |

- Record: 2026-09-09; author the conjugate-criterion agent, responding to the user's request to reconsider the main rationality theorem under conjugate variables.
- Source: Dab10, the same [arXiv:0804.2906v2](https://arxiv.org/abs/0804.2906v2) identified in [U001](Yin_U001.md#dab10-u001); [primary 12-page PDF](https://arxiv.org/pdf/0804.2906).
- Coverage: Lemma 10 and Remark 11, PDF/printed p. 8; their displayed calculation and Lemma 12 with its proof, p. 9.
- Method: the complete selected passages were read in parsed primary text and reconstructed below, with adjoints and limiting domains made explicit.
- Limits: the publisher version was not compared, and PDF screenshots were unavailable from the reader in this run.
  No local source PDF was retained, and no whole-paper or external-foundation audit is claimed.

## 1. Conventions and the Exact Source Interfaces

Let $X=(X_1,\ldots,X_d)$ be bounded selfadjoint generators of a finite tracial von Neumann algebra $(M,\tau)$.
Put $A=\mathbb C\langle X\rangle$, $H=L^2(M,\tau)$, and $\Omega=1$.
Suppose its conjugate variables $\xi_i\in H$ exist, so that
\[
\tau(\xi_i p)=(\tau\otimes\tau)(\partial_i p),\qquad p\in A.
\tag{1}
\]
The standard algebraic-freeness, selfadjointness of $\xi_i$, and closability interfaces are the already accepted Voi98/MSY inputs.
All polynomial domains below are dense in $H$ because the generators are selfadjoint.
Use the inner product linear in its second variable, and define the normalized polynomial-domain dual
\[
D_{i,0}p=(\mathrm{id}\otimes\tau)\partial_i p.
\tag{2}
\]
It satisfies $D_{i,0}\Omega=0$ and $[D_{i,0},X_j]=\delta_{ij}P_\Omega$ on $A$.

The source writes $\delta_i$ for $\partial_i$, and its $\Delta(X_i)$ in these passages is the conjugate variable $\xi_i$.
It is not the numerical maximal-Delta invariant used by MSY23.
The occasional word “microstates” preceding $\Phi^*$ is inconsistent with the notation: the hypothesis is finite non-microstates Fisher information.

For a selfadjoint or unitary $z\in M\cap\operatorname{Dom}\overline\partial$, Lemma 12 gives
\[
\|(\mathrm{id}\otimes\tau)\overline\partial_i z-z\xi_i\|_2
\le \|\xi_i\|_2\|z\|.
\tag{3}
\]
Its proof first handles unitaries using the preceding identity, then expresses a selfadjoint strict contraction as the average of two unitaries in the closed-derivation domain.
The required functional-calculus stability is explicitly imported there from the theory of closed real derivations.
The passage from strict to non-strict contractions is by rescaling.
This audit accepts that functional-calculus interface and reconstructs the consequences of (3); it does not reprove the complete Dirichlet-form foundation.

Lemma 10 additionally gives, when a second conjugate variable $\mathcal J_{2,i}$ exists in the indicated integrability class,
\[
\|D_i z\|_2
\le 2\|z\xi_i\|_2+|\tau(z^*z\mathcal J_{2,i})|^{1/2}.
\tag{4}
\]
Consequently Remark 11 supplies a bounded extension on $H$ if both first and second conjugate variables are bounded.
In particular a valid bound from this interface is
\[
\|D_i\|_{B(H)}\le 2\|\xi_i\|+\|\mathcal J_{2,i}\|^{1/2}.
\tag{5}
\]
The source also discusses spectral-gap and property-(T) consequences; these are outside this unit's required interface.

## 2. An Explicit Bound for Arbitrary Polynomials

For selfadjoint $p\in A$, (3) and the triangle inequality give
\[
\|D_{i,0}p\|_2\le 2\|\xi_i\|_2\|p\|.
\]
Writing an arbitrary polynomial as $p=a+ib$ with $a,b$ selfadjoint and $\|a\|,\|b\|\le\|p\|$ therefore gives the sufficient uniform estimate
\[
\boxed{\|D_{i,0}p\|_2\le 4\|\xi_i\|_2\|p\|.}
\tag{6}
\]
No optimal constant is needed for the rationality application.

The polynomial adjoint formula, with the tensor legs fixed as in (2), is
\[
E_{i,0}p:=\partial_i^*(p\otimes1)=p\xi_i-D_{i,0}p,
\qquad E_{i,0}\subseteq D_{i,0}^*.
\tag{7}
\]
Indeed $\langle D_{i,0}a,p\rangle=\langle\partial_i a,p\otimes1\rangle$ for $a,p\in A$.
Thus $D_{i,0}$ and $E_{i,0}$ are densely defined and closable, and
\[
\|E_{i,0}p\|_2\le5\|\xi_i\|_2\|p\|.
\tag{8}
\]
The two contractions $(\mathrm{id}\otimes\tau)\partial_i$ and $(\tau\otimes\mathrm{id})\partial_i$ must not be interchanged in (7).

The source prints $d\ge2$ in Lemmas 10 and 12 because of its factoriality/non-Gamma applications.
For the contraction estimates alone, $d=1$ follows without assuming a one-generator factor.
Adjoin a standard semicircular variable freely to $(M,\tau)$ in a larger finite tracial free product.
The original conjugate variable and the added semicircular variable form the enlarged conjugate system; this is the standard conjugate-variable free-product identity, checked on reduced centered words.
Apply the printed two-generator estimate and then restrict to $A$.
Its norm and conjugate-variable constants are unchanged.
Alternatively the selected calculation uses only one fixed coordinate and has no division by $d-1$.
The former argument gives an explicit reduction to the printed statement.

## 3. The Closed Canonical Dual and Its Adjoint Are Defined on M

Write $D_i=\overline{D_{i,0}}$ and $E_i=\overline{E_{i,0}}\subseteq D_i^*$.
The following argument identifies a definite extension; it does not choose an arbitrary Banach-space extension from $C^*(X)$ to $M$.

For $x\in M$, Kaplansky density followed by norm approximation inside $C^*(X)$ supplies polynomials $p_n$ with $p_n\to x$ in $L^2$ and a uniform operator-norm bound, as close to $\|x\|$ as desired.
The Hilbert space is separable because a finite tuple generates $M$; a sequence suffices, or the same argument can be expressed with nets.
By (6), $D_{i,0}p_n$ is bounded in $H$.
Any weakly convergent subsequence has a limit $v$ with $(x,v)$ in the graph of $D_i$.
This follows because a norm-closed linear graph in $H\oplus H$ is weakly closed.
Consequently $x\in\operatorname{Dom}D_i$ and the limit is necessarily $D_i x$.
The same proof using (8) applies to $E_i$.
It yields
\[
M\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
\quad
\|D_i x\|_2\le4\|\xi_i\|_2\|x\|,
\quad
\|E_i x\|_2\le5\|\xi_i\|_2\|x\|.
\tag{9}
\]
Here $E_i x=D_i^*x$ because $E_i\subseteq D_i^*$.
The sharper norm bounds on the approximants are obtained by first using a fixed positive tolerance and then letting it tend to zero.

An important additional consequence is bounded-set weak continuity:
\[
x_n\to x\text{ in }L^2,\quad\sup_n\|x_n\|<\infty
\quad\Longrightarrow\quad D_i x_n\rightharpoonup D_i x.
\tag{10}
\]
Every subsequence has a weakly convergent subsubsequence by the uniform estimate, and weak-closedness of the graph identifies its unique possible limit.
This proves (10) for the whole sequence, and likewise for the adjoint on $M$.
It is weaker than boundedness $H\to H$, but suffices for the regular-denominator cutoff step of a conjugate-variable finite-defect theorem.

## 4. A Reconstructed Bounded-Dual Consequence of Lipschitz Conjugates

The following proof gives a more direct sufficient condition than separately assuming a bounded second conjugate variable.
It is a reconstruction of the same adjoint/coassociativity mechanism behind Lemma 10, not a claim that this exact statement is printed as a theorem in Dab10.

Fix one coordinate and suppose, in addition to (1), that
\[
\xi_i\in\operatorname{Dom}\overline\partial_i,
\qquad
B_i:=(\mathrm{id}\otimes\tau)\overline\partial_i\xi_i\in M.
\tag{11}
\]
In particular, Lipschitz conjugate variables as in MS23 satisfy (11): the partial trace is a contractive normal map on the bounded spatial tensor product.

For $p\in A$, graph approximation of $\xi_i$ by polynomials shows $p\xi_i\in\operatorname{Dom}\overline\partial_i$ and
\[
\overline\partial_i(p\xi_i)
=p\overline\partial_i\xi_i+(\partial_i p)\cdot\xi_i.
\tag{12}
\]
The second term is legitimate even without assuming $\xi_i\in M$: $\partial_i p$ is a finite sum of tensors of bounded elements, and right multiplication of its second factor by the $L^2$ vector $\xi_i$ is continuous for each such factor.
The same approximants, after applying the bounded partial-trace map on Hilbert tensor products, put $p\xi_i$ in $\operatorname{Dom}D_i$.

If $\partial_i p=\sum_k a_k\otimes b_k$, conjugacy and coassociativity give
\[
\begin{aligned}
D_i(p\xi_i)
&=pB_i+\sum_k a_k\tau(b_k\xi_i)\\
&=pB_i+(\mathrm{id}\otimes\tau\otimes\tau)
       (\mathrm{id}\otimes\partial_i)\partial_i p\\
&=pB_i+(\mathrm{id}\otimes\tau\otimes\tau)
       (\partial_i\otimes\mathrm{id})\partial_i p\\
&=pB_i+D_{i,0}^2p.
\end{aligned}
\tag{13}
\]
Thus (7) places $E_{i,0}p$ in $\operatorname{Dom}D_i$ and gives $D_iE_{i,0}p=pB_i$.
The adjoint relation now yields
\[
\|E_{i,0}p\|_2^2
=\langle p,D_iE_{i,0}p\rangle
=\tau(p^*pB_i)
\le\|B_i\|\|p\|_2^2.
\tag{14}
\]
The equality also implies $B_i\ge0$, by density and continuity of the bounded right-multiplication quadratic form.

Equation (14) makes $E_{i,0}$ bounded on its dense polynomial domain, hence it has a unique bounded extension $E_i^{\mathrm b}$ to $H$.
The polynomial adjoint identity gives $D_{i,0}\subseteq(E_i^{\mathrm b})^*$, so its closure is the bounded operator $(E_i^{\mathrm b})^*$ on all of $H$.
The polynomial dual relation then extends by continuity to
\[
\boxed{D_i\in B(H),\qquad[D_i,X_j]=\delta_{ij}P_\Omega,
\qquad\|D_i\|\le\|B_i\|^{1/2}
\le\|\overline\partial_i\xi_i\|^{1/2}.}
\tag{15}
\]
The last inequality assumes the bounded spatial-tensor hypothesis of Lipschitz conjugates.
In fact (13), by bounded extension, gives $D_iD_i^*=\rho(B_i)$ and hence $\|D_i\|^2=\|B_i\|$.
No smallness of the derivative norm is needed.

This supplies the missing interface from MS23's all-$|q|<1$ Lipschitz conclusion to a simultaneous bounded canonical dual system.
The earlier MS23 audit correctly observed that its vacuum-functional estimate alone does not bound the whole dual.
It did not take this additional contraction argument into account, so a blanket statement that the combined literature supplies only small-$q$ bounded duals needs a dated correction.
This consequence concerns bounded duals and the affiliated rationality criterion; it does not establish multivariable rational $L^2$ boundedness or scalar bounded-division-closure equality.

For comparison with Remark 11, if $\xi_i$ is bounded and its closed derivative is bounded, graph approximation and the standard adjoint formula also give
\[
\mathcal J_{2,i}
=\partial_i^*(1\otimes\xi_i)
=\xi_i^2-(\tau\otimes\mathrm{id})\overline\partial_i\xi_i\in M.
\tag{16}
\]
The two partial traces in (11) and (16) occupy different tensor legs; (13) fixes the orientation needed for (15).
Either (15) or the weaker bound (5) suffices for the MS23 application.

## 5. Verification Boundaries and Review

The source statement, adjoint identities, constants sufficient for arbitrary complex polynomials, graph-closure extension to all bounded vectors, and the Lipschitz consequence have been reconstructed here.
Accepted external inputs are the finite-Fisher algebraic-freeness and closability theory, the closed-real-derivation functional calculus used inside Lemma 12, Kaplansky density, and the finite tracial free-product construction for the one-variable reduction.
No entropy, factoriality, non-Gamma, or property-(T) proof is promoted by this unit.

Independent review, 2026-09-09, the triangular-dual reviewer: read all five sections and independently retrieved the primary arXiv:0804.2906v2 pp. 8-9, including Lemma 10, Remark 11, their displayed proof, and Lemma 12 with its proof.
The reviewer checked the sufficient constants, the retained functional-calculus boundary, both closed-graph extensions to $M$, bounded-set weak continuity, the product graph limits, tensor-leg order, coassociativity, positivity, and the final bounded-extension argument.
It independently confirmed $D_iE_{i,0}p=pB_i$ and $D_iD_i^*=\rho(B_i)$, and recommended acceptance without a mathematical correction.
The reviewer had previously developed a separate particle-degree construction of the q-Gaussian bounded dual; that involvement is disclosed, and its argument is not a dependency of this unit.
This paragraph adds the subsequent review record without changing the inspected mathematical text.

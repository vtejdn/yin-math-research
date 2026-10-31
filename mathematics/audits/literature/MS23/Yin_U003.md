---
author: Yin
---

<a id="ms23-u003"></a>
# MS23-U003: Vacuum Adjoints and Norm-Convergent Conjugate Variables

Inspected edition: [Yin's source notes](readme.md#yin-edition).

- Source: [MS23](../../../literature/pdf/MS23.pdf), 36-page published article in Advances in Mathematics 413 (2023), 108834.
- Locator: Theorem 4.6, Corollary 4.7, and Remark 4.8, printed/PDF pp. 22-26; supporting norm conventions and Lemma 2.2, pp. 6-7.
- Record: 2026-09-09, the estimate agent; direct full-proof reconstruction and self-review of this unit.
Independent review, if completed, is separately identified in the [source index](readme.md).
- Coverage: `Audited within scope`, retaining the homogeneous Haagerup inequality and the declared foundational interfaces as external inputs; no formal verification.

## Statement and Conventions

Fix a finite integer $d\ge1$ and $q\in(-1,1)$.
Let $H_q=\mathcal F_q(\mathbb C^d)$, let $\Omega$ be its vacuum, and let $A_i=\ell_i+\ell_i^*$ be the canonical variance-one q-Gaussian generators of $M=\Gamma_q(\mathbb R^d)$.
The source writes $\ell_i$ for left q-annihilation and $\ell_i^*$ for left creation.
The faithful vacuum trace identifies $H_q$ with $L^2(M)$.

The algebraic duals from Proposition 4.5 act on the dense polynomial/algebraic Fock domain, satisfy $D_i\Omega=0$ and $[D_i,A_j]=\delta_{ij}P_\Omega$ there.
The additional assertion of Theorem 4.6 is
\[
\Omega\in\operatorname{dom}(D_i^*),\qquad
\xi_i=D_i^*\Omega\in H_q.
\tag{1}
\]
Theorem 2.5 then identifies $(\xi_i)$ as the conjugate system.
With the source's free right deletion operators
\[
r_i e_{wj}=\delta_{ij}e_w,\qquad r_i\Omega=0,\qquad
r_w=r_{w_1}\cdots r_{w_m},\qquad r_{iw}=r_i r_w,
\]
Corollary 4.7 gives the absolutely convergent vector series
\[
\boxed{\displaystyle
\xi_i=\sum_{m\ge0}(-1)^m q^{m(m+1)/2}
             \sum_{|w|=m}r_{iw}^*e_w.}
\tag{2}
\]
Its Wick-operator realization also converges absolutely in operator norm; hence $\xi_i=X_i\Omega$ for an $X_i\in C^*(A_1,\ldots,A_d)\subset M$.

Here $r_i^*$ is the adjoint in the **actual q-inner product**.
For $q\ne0$, $r_i$ is not the right q-annihilator, and $r_i^*$ is not plain right concatenation.
For a finite vector $\eta$, $\|\eta\|_q$ means its Hilbert norm, whereas $\|W(\eta)\|$ means the operator norm of its Wick polynomial.
Neither statement (1) nor the norm convergence in (2) asserts $D_i\in B(H_q)$.

## Fully Paired Diagrams and the Quadratic Exponent

In Proposition 4.5 only terms with no surviving singletons contribute to $\langle D_i e_v,\Omega\rangle_q$.
If $|v|=2m-1$, this forces the distinguished pair to be $(0,m)$ and the remaining $m-1$ right vertices to pair bijectively with the $m-1$ left vertices.
There are no vacuum contributions from even degrees.

Every such diagram corresponds to a permutation $\sigma\in S_{m-1}$.
Its color constraints give words of the form $\sigma(w)iw$, where $|w|=m-1$.
Repeated colors cause no overcounting error: the calculation sums over diagrams, and different permutations with identical colored words retain their multiplicities, exactly as in the q-symmetrizer.

Using the source's rectangular drawing and its assigned heights, the arc whose right endpoint is $k\in\{1,\ldots,m-1\}$ crosses exactly $k$ lower arcs on the right.
Thus the unavoidable right crossings contribute
\[
1+\cdots+(m-1)=\frac{m(m-1)}2.
\]
The remaining left crossings are the inversions of $\sigma$.
Consequently
\[
\operatorname{cross}(\pi)=\frac{m(m-1)}2+\operatorname{inv}(\sigma).
\tag{3}
\]
The figure on p. 22 and the decomposition on p. 23 were visually inspected.
This quadratic number of compulsory crossings is the essential source of decay, and does not require a small-$q$ bound depending on $d$.

For a finite vector $\eta=\sum_v\alpha_v e_v$, let $P_n$ denote the orthogonal projection to degree $n$.
Summing the residual $q^{\operatorname{inv}(\sigma)}$ by the q-symmetrizer gives the exact functional identity
\[
\langle D_i\eta,\Omega\rangle_q
=\sum_{m\ge1}(-1)^{m-1}q^{m(m-1)/2}
  \sum_{|w|=m-1}\langle r_{iw}P_{2m-1}\eta,e_w\rangle_q.
\tag{4}
\]
This is initially a finite sum in degree, so no unproved interchange of an infinite series occurs.
The source uses inner products linear in the first argument; $q$ and the signs are real, so adjoint conversion introduces no missing conjugate coefficient.

## Theorem 4.6: Boundedness of the Vacuum Functional

Put $t=|q|$, $[n]_t=1+t+\cdots+t^{n-1}$, $[n]_t!=\prod_{k=1}^n[k]_t$, and
\[
c=w(q)^{-1/2},\qquad
w(q)^2=(1-t^2)^{-1}\prod_{k\ge1}\frac{1-t^k}{1+t^k}.
\]
For every fixed $t<1$, $w(q)>0$.
Lemma 2.2 gives $\|r_i\|\le c$.
Hence $\|r_{iw}\|\le c^m$ when $|w|=m-1$.
The basis vectors need not be normalized, but
\[
\|e_w\|_q^2
\le\sum_{\sigma\in S_{m-1}}t^{\operatorname{inv}(\sigma)}
=[m-1]_t!.
\tag{5}
\]
The first inequality remains valid for negative $q$ by absolute values.
Cauchy-Schwarz in the q-inner product, the contractivity of $P_{2m-1}$, and the count $d^{m-1}$ now give
\[
|\langle D_i\eta,\Omega\rangle_q|
\le\|\eta\|_q\sum_{m\ge1}
t^{m(m-1)/2}d^{m-1}c^m\sqrt{[m-1]_t!}.
\tag{6}
\]
For $0<t<1$, consecutive summands have ratio
\[
t^m d c\sqrt{[m]_t}\ \longrightarrow\ 0,
\tag{7}
\]
because $[m]_t\le(1-t)^{-1}$.
Thus the series is finite for every fixed $q\in(-1,1)$ and finite $d$.
At $q=0$ only the $m=1$ contribution survives, with the usual convention $q^0=1$.

Equation (6) proves that $\eta\mapsto\langle D_i\eta,\Omega\rangle_q$ extends to a bounded functional on $H_q$.
By the definition of an unbounded operator's adjoint, this is exactly $\Omega\in\operatorname{dom}(D_i^*)$.
It does **not** bound $\|D_i\eta\|_q$ in terms of $\|\eta\|_q$: every non-vacuum output of $D_i$ was discarded in passing to (4).
Theorem 4.6 has no assertion about the norm of the whole dual operator.

## Corollary 4.7: From a Vacuum Adjoint to a Bounded Conjugate

Each $r_{iw}^*e_w$ with $|w|=m$ belongs to degree $2m+1$, because right deletion lowers degree by one and its q-adjoint raises degree by one.
Moreover
\[
\|r_{iw}^*e_w\|_q\le c^{m+1}\sqrt{[m]_t!}.
\tag{8}
\]
The same ratio estimate proves absolute Hilbert convergence of (2).
Taking inner products with finite-degree vectors and using (4) identifies its limit with $D_i^*\Omega$; the distinct-degree orthogonality justifies removal of the projections in the scalar identities.

Let
\[
C_t=\prod_{k\ge1}(1-t^k)^{-1}.
\]
The accepted homogeneous q-Haagerup inequality says
\[
\|W(\eta_n)\|\le(n+1)C_t^{3/2}\|\eta_n\|_q,
\qquad \eta_n\in H^{\otimes n}.
\tag{9}
\]
Apply it in degree $n=2m+1$, not degree $m$.
Equations (2) and (8) yield the absolute operator-norm bound
\[
\sum_{m\ge0}\sum_{|w|=m}
t^{m(m+1)/2}\|W(r_{iw}^*e_w)\|
\le C_t^{3/2}\sum_{m\ge0}
d^m t^{m(m+1)/2}(2m+2)c^{m+1}\sqrt{[m]_t!}.
\tag{10}
\]
Its successive ratio is
\[
t^{m+1}dc\,\frac{m+2}{m+1}\sqrt{[m+1]_t}\ \longrightarrow\ 0.
\]
Every summand is a Wick polynomial because its vector is in one finite-dimensional particle space.
Thus the operator-norm limit lies in $C^*(A)$, and applying it to $\Omega$ agrees with the Hilbert-space limit already identified.
The p. 25 formula was visually checked for the factor $2m+2$ and the inverse power $w(q)^{-(m+1)/2}$.

## Remark 4.8 and Boundary Checks

For $d=1$, $\|e_m\|_q^2=[m]_q!$ and right deletion is $r_1e_m=e_{m-1}$.
Its q-adjoint is therefore
\[
r_1^*e_m=\frac{e_{m+1}}{[m+1]_q},\qquad
(r_1^*)^{m+1}e_m=\frac{[m]_q!}{[2m+1]_q!}e_{2m+1}.
\]
Substitution in (2) gives
\[
\xi_1=\sum_{m\ge0}(-1)^m q^{m(m+1)/2}
             \frac{[m]_q!}{[2m+1]_q!}e_{2m+1},
\]
which is precisely Corollary 3.4 after shifting its index.
For negative $q$, the actual coefficient uses $[m]_q!$, whereas the estimates use $[m]_{|q|}!$.
These must not be interchanged in the identity.

At $q=0$, (2) gives $\xi_i=e_i$, the usual semicircular conjugate.
At $q=\pm1$ the hypotheses and estimates fail; the conclusions are not extended to those endpoints.
The constants are allowed to deteriorate as $|q|\uparrow1$ or $d$ grows.
Finite $d$ is used essentially in the count $d^m$.

## Dependencies, Scope, and Downstream Use

The local chain consumes Proposition 4.5's algebraic dual formula, Lemma 2.2's q-Fock deletion bound, the q-symmetrizer, and Theorem 2.5's normalized-dual/conjugate interface.
Their separate review belongs to the corresponding units in the [source index](readme.md).
This unit fully checks the passage from those interfaces to (1), (2), and operator-norm convergence.

The external homogeneous bound (9) is cited on MS23 pp. 6-7 as Bozejko 1999, Proposition 2.1.
The same precise estimate is directly accepted from the primary Dab14 Theorem 28 in [Dab14-U001](../Dab14/Yin_U001.md#dab14-u001).
Its original proof is not re-audited here.
The Bozejko 1998 symmetrizer input to Lemma 2.2 likewise retains the verification boundary recorded by the foundations unit.

For [Yin_C_F0020](../../../claims/Yin_C_F0020_v1.md#yin_c_f0020) and [Yin_S_F0008](../../../strategies/Yin_S_F0008.md#s_f0008), this supplies an all-$q$ explicit conjugate system and a rigorously controlled vacuum-adjoint expansion.
It does not replace the small-$q$ construction of simultaneous **bounded** duals, establish a finite residual space for q-Wick coefficients, or prove multivariable rational $L^2$ boundedness.
The passage to Lipschitz conjugates requires the derivative estimates in [MS23-U004](Yin_U004.md#ms23-u004).

## Verification Facts and Corrections

The complete pp. 22-26 argument was read in the exact published artifact; diagrams and crucial estimates on pp. 22, 23, 25, and 26 were inspected as rendered images.
The factorial ratios, operator-versus-Hilbert norm distinction, repeated-color multiplicities, q-negative estimates, and one-variable specialization were reconstructed independently of source assertions.

No theorem-invalidating error was found in this unit.
The shorthand $\|D_i^*\Omega\|$ in the source's operator-norm proof is read via the convergent sequence of Wick polynomials: membership in $M$ is the conclusion of that argument, not an input.
All infinite-limit identifications were supplied above.
No numerical experiment or formal proof assistant is used for this unit, and no separate errata search is claimed here.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | MS23, the supplied 36-page published article, Advances in Mathematics 413 (2023), 108834; printed and one-based PDF pages agree. The earlier 30-page arXiv reading and external source editions retain their separate recorded scopes. |
| source-locator | Theorem 4.6, Corollary 4.7 and Remark 4.8, printed/PDF pp. 22-26; norm conventions and Lemma 2.2 on pp. 6-7. |
| inspection | 2026-09-09: complete local reconstruction and self-review of the vacuum-adjoint estimate, factorial ratios and operator-norm conjugate series, with source-image inspection; separate artifact review is recorded in the source home. Homogeneous Haagerup and the declared foundations remain external inputs. No numerical experiment, formal proof assistant or separate errata search was claimed. |

---
author: Yin
---

# Finite-variance Wigner frontier and coupling obstructions

This working draft supports the [finite-variance almost-sure Brown-measure task](../tasks/Yin_T_F0012_v3.md#contract).
It records source preparation and new adversarial calculations on 2026-11-05, not independent review or Task completion.
The exact fixed-law and arbitrary cross-size coupling quantifiers of that contract are retained.
No counterexample to that complete contract has been found in this bounded investigation.

## Two distinctions that change the proof route

Finite second moments do not imply convergence of every normalized trace moment, even for a single Wigner matrix with a fixed atom law.
They also do not imply almost-sure bounded normalized Hilbert--Schmidt norm under every allowed coupling between sizes.
Neither failure contradicts weak convergence of the empirical measures against bounded continuous functions.
These distinctions prevent importing stronger intermediate statements into the current Task.

### A fixed-law example with divergent fourth trace moments

Let \(\eta\) be a symmetric real random variable with a Pareto tail of exponent \(5/2\), rescaled to variance one.
Thus, for some \(c>0\) and all sufficiently large \(t\),
\[
 \mathbb P\{|\eta|>t\}=ct^{-5/2},\qquad
 \mathbb E\eta=0,\qquad \mathbb E\eta^2=1.
\]
This law even has a moment of order \(2+\varepsilon\) for every \(0<\varepsilon<1/2\).
At each size \(N\), take independent copies \(\eta_{ij}^{(N)}\), \(i<j\), above the diagonal, reflect them across the diagonal, and take independent Rademacher diagonal entries.
Let \(W_N\) be this real symmetric matrix divided by \(\sqrt N\).
The model satisfies the current contract, independently of how the matrices of different sizes are coupled.
Writing \(\operatorname{tr}_N=N^{-1}\operatorname{Tr}\), Hermiticity gives
\[
 \operatorname{tr}_N(W_N^4)
 \ge \frac{\|W_N\|^4}{N}
 \ge \frac{\max_{i<j}|\eta_{ij}^{(N)}|^4}{N^3}.
 \tag{1}
\]
For every fixed \(R>0\), the independence within each size therefore implies, for all sufficiently large \(N\),
\[
 \begin{aligned}
 \mathbb P\{\operatorname{tr}_N(W_N^4)\le R\}
 &\le
 \left(1-cR^{-5/8}N^{-15/8}\right)^{N(N-1)/2}\\
 &\le \exp(-c_RN^{1/8}).
 \end{aligned}
 \tag{2}
\]
This upper bound is summable in \(N\).
First Borel--Cantelli, followed by the countable intersection over positive integers \(R\), proves
\[
 \operatorname{tr}_N(W_N^4)\longrightarrow+\infty
 \quad\text{almost surely under every cross-size coupling.}
 \tag{3}
\]
In particular, convergence of all normalized trace moments to semicircular moments is false under the bare second-moment hypotheses.
For \(P(x)=x^4\), (3) concerns an unbounded test function of the input empirical law; it does not refute the weak spectral limit of \(P(W_N)\).
This is an elementary calculation developed here, not a theorem attributed to a source.

### Independent sizes can have unbounded second trace moments

Keep the same fixed law, and now choose the matrices independently across different sizes.
This is one of the couplings permitted by the contract.
For fixed \(R>0\), let
\[
 E_{N,R}=\left\{\max_{i<j}|\eta_{ij}^{(N)}|>\sqrt R\,N\right\}.
\]
Then
\[
 \mathbb P(E_{N,R})
 =1-\left(1-cR^{-5/4}N^{-5/2}\right)^{N(N-1)/2}
 \asymp_R N^{-1/2}.
 \tag{4}
\]
On \(E_{N,R}\),
\[
 \operatorname{tr}_N(W_N^2)
 =N^{-2}\sum_{i,j}|\eta_{ij}^{(N)}|^2>R.
 \tag{5}
\]
The events \(E_{N,R}\) are independent across \(N\), and their probabilities have divergent sum.
Second Borel--Cantelli and the countable intersection over positive integers \(R\) yield
\[
 \limsup_N\operatorname{tr}_N(W_N^2)=+\infty
 \quad\text{almost surely.}
 \tag{6}
\]
By comparison, with the usual nested infinite-array construction, enumerate the upper triangular entries in increasing order of their maximal index.
The ordinary strong law for the iid integrable variables \(|\eta_{ij}|^2\), along the subsequence of the first \(N(N-1)/2\) entries, gives \(\operatorname{tr}_N(W_N^2)\to1\) almost surely; the Rademacher diagonal contributes only \(1/N\).
Thus a proof that silently replaces arbitrary cross-size coupling by a nested-array strong law loses a genuine quantifier in the Task.
Equation (6) remains a failure of an auxiliary norm bound, not a failure of weak empirical-measure convergence.

## Primary-source boundaries

The following are direct inspections of selected primary sources, rather than an exhaustive literature search or complete audits of their proofs.
No external source below is acquired as an accepted input by this draft.
The search found no theorem that discharges the exact general-polynomial finite-variance almost-sure contract.

### Belinschi--Capitaine: do not read Proposition 2.2 as a bare-second-moment moment theorem

The inspected edition is [arXiv:1611.07440v2](https://arxiv.org/pdf/1611.07440v2), dated 19 September 2017.
The global model on PDF p. 5 assumes fourth-moment tail domination in (1.5) and a uniform third-moment bound.
PDF p. 12 defines \(\theta_* = \sup_{i<j}\mathbb E|X_{ij}|^3\) and repeats fourth-moment domination in (2.4).
Proposition 2.2 on PDF pp. 15--16 explicitly restates only centered unit second moments, while its proof imports the operator-norm approximation (2.15), expressed in terms of that \(\theta_*\), and the preceding truncation argument.
Its conclusion uses noncommutative distribution, defined through all normalized trace moments.
Equations (1)--(3) rule out the bare-finite-variance interpretation of that conclusion.
The safe boundary is to retain the stronger carried model hypotheses when using the cited norm argument; this draft does not assert an official erratum or resolve the authors' intended scope.
For the present Task, prove weak self-adjoint spectral convergence by a finite-variance truncation/rank argument instead of citing this proposition as all-moment freeness.

### Han: nonnormal universality has a different input class

The inspected primary edition is [Han, arXiv:2606.01664v1](https://arxiv.org/html/2606.01664v1), particularly Theorems 1.2 and 1.4 and Questions 1.7--1.8.
The retained repository source and audit are [Han26.pdf](../literature/pdf/Han26.pdf) and [the existing source audit](../audits/literature/Han26/Yin_U001.md).
Theorem 1.2 treats holomorphic polynomials in independent complex Ginibre matrices and states weak convergence in probability.
Theorem 1.4 treats centered variance-one complex iid full matrices with bounded planar density and all moments; the discussion after it allows a sufficiently high finite moment depending on the polynomial.
It does not identify a universal second-moment threshold.
Real Gaussian variables, removal of density, and polynomials involving adjoints are explicit further questions in that introduction.
Consequently this theorem does not supply the Wigner-symmetry, atomic-law, finite-variance, or arbitrary-coupling almost-sure interfaces required here.

### Two Wigner factors are an informative benchmark

The inspected edition is [O'Rourke--Renfrew--Soshnikov--Vu, arXiv:1403.6080v3](https://arxiv.org/pdf/1403.6080v3), dated 2 March 2015, PDF pp. 4--5.
Theorem 2.8 gives almost-sure square-circular convergence for two real Wigner factors with iid on-or-above-diagonal entries and \(2+\tau\) moments.
The general elliptic-product Theorem 2.3 requires \(2+\tau\) moments and \(|\rho_k|<1\); Remark 2.5 discusses removing those restrictions.
This supplies a concrete special-case comparison, not a finite-variance theorem for arbitrary Wigner polynomials.
For research triage, \(P(x,y)=xy\) with two real Wigner inputs and only second moments is already a useful target for the new logarithmic-tail interface.

### A sharper finite-variance smallest-value starting point

Nguyen's [journal article, EJP 17 (2012), no. 53](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2165/2165-10579-1-PB.pdf), DOI 10.1214/EJP.v17-2165, was inspected at Condition 1.3 and Theorem 1.4 on PDF p. 2 and the initial truncation on PDF p. 3.
For real symmetric matrices whose on-or-above-diagonal entries are iid, it assumes centered unit variance and \(\mathbb P\{|\xi-\xi'|\ge c_1\}\ge c_2>0\), and allows a deterministic symmetric perturbation with entries bounded by a fixed power of \(N\).
For every \(B>0\), it gives an \(A>0\) with \(\mathbb P\{s_{\min}(X_N+F_N)\le N^{-A}\}\le N^{-B}\) eventually.
The [author-hosted 23-page preprint](https://people.math.osu.edu/nguyen.1261/cikk/singular-noLO.pdf) labels this Theorem 1.3 and has placeholder journal metadata; the actual journal theorem number is 1.4, not the number 1.5 cited in the product paper.
The full proof has not been audited here, and the complex-symmetric deterministic-shift extension is not silently included.

The anti-concentration condition is automatic for each fixed nondegenerate real law: since \(\mathbb P\{\xi\ne\xi'\}>0\), some positive threshold \(c_1\) has positive exceedance probability.
This observation uses no moment above two.
The equality of diagonal and off-diagonal laws in this statement is an extra restriction relative to the current Task.

Section 7 of the product paper, especially Theorems 7.2--7.3 and the proof on PDF pp. 25--26, conditions on the second factor and uses the identity
\[
 (W_1W_2-wI)^{-1}
 =W_2^{-1}(W_1-wW_2^{-1})^{-1}.
 \tag{8}
\]
For real symmetric \(W_2\), the conditional shift \(-wW_2^{-1}\) is complex symmetric, and its norm is polynomially bounded on the good invertibility event.
The product paper attributes the complex-symmetric-shift extension to a personal communication with Nguyen.
Its Theorem 7.3 explicitly retains the assumptions of Theorem 2.8, including \(2+\tau\) moments and iid diagonal/off-diagonal laws; it does not itself state the finite-variance or arbitrary-diagonal extension.
Thus checking that extension at finite variance is a specific source/proof interface, rather than a reason to require \(2+\tau\) for the preliminary smallest-value estimate.
Its crude polynomial upper-norm step uses only a second-moment Markov bound.
Even success with (8) gives neither intermediate singular-value counting nor the full negative-log uniform integrability in (7).

### Finite-variance elliptic sources do not automatically include the Wigner boundary

The inspected [Nguyen--O'Rourke elliptic-law edition, arXiv:1208.5883v4](https://arxiv.org/pdf/1208.5883v4), is dated 9 September 2014.
Definition 1.3 uses an infinite double array with independent mirror pairs.
Theorem 1.5, PDF p. 3, gives the real finite-variance elliptic law almost surely for \(|\rho|<1\), including specified deterministic perturbations.
Theorem 1.8 uses the complex covariance pattern in Definition 1.6, not merely a bound on one complex correlation.
In particular, its real and imaginary mirror covariances have opposite prescribed signs, so it cannot be applied automatically to the equal complex mirror entries of \(W_1+iW_2\) formed from real symmetric Wigner matrices.
The paragraph following that theorem conjectures a fuller complex extension.
The source's nested-array formulation also needs attention before importing its almost-sure statement under arbitrary size coupling.

The inspected [Götze--Naumov--Tikhomirov edition, arXiv:1404.7013v1](https://arxiv.org/pdf/1404.7013v1), has arXiv date 28 April 2014 and internal date 6 July 2021.
Its Theorem 1.1, PDF p. 2, proves convergence in probability of products of at least two real elliptic matrices under uniform integrability of squared entries, with strict \(|\rho|<1\).
This is a genuinely low-moment result, but neither the real Wigner boundary \(\rho=1\) nor the almost-sure conclusion is included in that theorem.

## Why the tempting counterexamples do not decide the Task

The fixed-law requirement excludes a triangular array that puts size-dependent probability on exceptionally large entries while changing its atom law with \(N\).
The moment divergences (3) and (6) do not provide a bounded continuous spectral test with a failed limit.
A positive probability of exact determinant zero at one fixed spectral parameter makes an expected logarithm \(-\infty\), but does not by itself give a positive limiting atom or an almost-sure failure of the empirical eigenvalue measure.
Parity-forced zero eigenvalues of real skew-symmetric polynomial evaluations likewise have mass at most \(1/N\) when only one zero is forced.
One must distinguish such negligible or nonsummable auxiliary events from a macroscopic spectral discrepancy.

Nor does the availability of low-rank truncation settle nonnormal weak convergence by itself.
For example, if \(J_N\) is the nilpotent shift and \(C_N=J_N+e_Ne_1^*\) is its cyclic completion, then \(\operatorname{rank}(C_N-J_N)=1\), while the empirical laws converge respectively to \(\delta_0\) and uniform measure on the unit circle.
This deterministic example is outside the Wigner-polynomial model, so it only invalidates a proposed universal low-rank perturbation argument.

## Concrete next proof targets

The robust finite-variance part should be formulated for bounded spectral test functions of self-adjoint linearizations or Hermitizations.
Use finite-variance truncation to obtain convergence of their expectations and bounded-rank row exposure to obtain summable concentration estimates.
This avoids both the false all-moment import and the false arbitrary-coupling pathwise Hilbert--Schmidt bound.

For a fixed polynomial \(P\) and almost every spectral parameter \(z\), let \(\nu_{N,z}\) be the empirical singular-value law of \(P(W_N)-zI\).
Once weak singular-value convergence and positive-log-tail control are established, the decisive additional target is an almost-sure negative-log-tail bound such as
\[
 \lim_{\delta\downarrow0}\limsup_{N\to\infty}
 \int_{(0,\delta)}|\log t|\,d\nu_{N,z}(t)=0,
 \tag{7}
\]
with eventual absence of an atom at zero at the relevant \(z\), or a directly sufficient planar-integrated version.
If the route is through a matrix-valued linear pencil, its Schur-complement determinant transfer and all logarithmic-error terms must be established at this same moment and coupling level.
The Gaussian tube probability used in the completed [GUE result](../claims/Yin_C_F0186_v3.md#statement) cannot simply be applied to an atomic product measure.
A polynomial that is not identically zero can still vanish with positive probability on an atomic support.
Conditioning must preserve enough independent entry randomness and must address coefficient-space degeneracy, not merely formal nonidentity of the determinant.

A concrete intermediate deliverable is to prove a summable small-singular-value/negative-log estimate first for the two-factor Wigner product benchmark under exactly second moments.
The general pencil argument will require intermediate singular-value counting or an equally strong integrated logarithmic estimate in addition to a lower bound for the single smallest singular value.
An estimate with a distribution-dependent polynomial failure probability is not automatically summable, so its conversion to the Task's arbitrary-coupling almost-sure conclusion must be explicit.
These are proof targets, not established statements in this draft.

## Two-factor pilot: intermediate singular values and a conditional closure

This continuation isolates the new small-singular-value input needed for \(P(x,y)=xy\).
The calculations below are proof development requiring review; no new accepted Claim is asserted.
The [product article's metadata](https://arxiv.org/abs/1403.6080) identifies its journal publication as J. Stat. Phys. 160 (2015), 89--119.
The inspected mathematical edition remains arXiv v3.

### A finite-variance distance estimate with summable failure

We use the standard bounded-product convex concentration inequality: if independent real coordinates have support in intervals of diameter at most \(2b\), and \(f\) is convex and 1-Lipschitz for Euclidean distance, then
\[
 \mathbb P\{|f-\operatorname{med}f|\ge t\}
 \le C\exp(-ct^2/b^2).
 \tag{9}
\]
One inspected primary-source pointer is the bounded-product input stated as Theorem 3.7 and Corollary 3.8 on PDF p. 30 of [Götze--Naumov--Tikhomirov](https://arxiv.org/pdf/1404.7013).
Their adjacent projection scheme motivated the following explicit choice of different truncation and codimension exponents.
The proof of the concentration theorem itself is an external input and is not audited here.

Let \(x=(\xi_1,\ldots,\xi_n)\) have independent copies of a fixed real centered variance-one law with finite second moment.
Let \(H\subset\mathbb C^n\) be a deterministic complex linear subspace with complex codimension \(q\ge c_0n^{3/4}\), and let \(f\in\mathbb C^n\) be arbitrary and deterministic.
There are constants \(c,C>0\), independent of \(H\) and \(f\), such that eventually
\[
 \mathbb P\{\operatorname{dist}(x+f,H)\le c\sqrt q\}
 \le C\exp(-cn^{1/4}).
 \tag{10}
\]
To prove this, truncate by conditioning on the good-coordinate set
\[
 J=\{i:|\xi_i|\le n^{1/4}\}.
\]
Since \(\mathbb P\{|\xi|>n^{1/4}\}\le n^{-1/2}\), a binomial Chernoff bound gives
\[
 \mathbb P\{|J^c|>n^{5/8}\}\le \exp(-c n^{5/8}\log n)
 \tag{11}
\]
for all large \(n\).
Conditional on a fixed good set \(J\), its retained coordinates remain independent, with the common law of \(\xi\) conditional on \(|\xi|\le n^{1/4}\).
Let its mean and variance be \(m_n,v_n\); finite variance gives \(m_n\to0\) and \(v_n\to1\).
Project onto the coordinates in \(J\), and enlarge the projected subspace by the single vector \(f_J+m_n\boldsymbol1\).
Denote the enlarged space by \(H_J'\).
Its codimension is at least
\[
 q-|J^c|-1\ge q/2
\]
eventually whenever \(|J^c|\le n^{5/8}\).
Consequently
\[
 \operatorname{dist}(x+f,H)
 \ge \operatorname{dist}(x_J-m_n\boldsymbol1,H_J').
 \tag{12}
\]
For the centered conditional vector \(y=x_J-m_n\boldsymbol1\), the right-hand distance is convex and 1-Lipschitz as a function of its real coordinates.
If \(Q\) is the complex orthogonal projection onto \((H_J')^\perp\), then
\[
 \mathbb E\|Qy\|^2=v_n\operatorname{Tr}Q\ge q/3.
 \tag{13}
\]
Equation (13) holds although the coordinates are real, since their covariance matrix is \(v_nI\).
By integrating (9), the mean differs from the median by at most \(Cn^{1/4}\), and the variance is at most \(Cn^{1/2}\).
The median is therefore at least \(c\sqrt q\), because \(n^{1/4}=o(\sqrt q)\).
Applying (9) once more gives a conditional lower-tail bound \(C\exp(-cq/n^{1/2})\), uniformly in \(J,H,f\).
Combining it with (11) proves (10).
Separating the bad-coordinate exponent \(5/8\) from the codimension exponent \(3/4\) is essential to the displayed dimension inequality.

### Intermediate singular values of Wigner plus an arbitrary complex shift

Let \(W_n\) be a normalized real symmetric Wigner matrix with the off-diagonal law just used.
Its diagonal can have any independent law, and may instead be deterministic.
Let \(F_n\) be any deterministic complex matrix, with no symmetry or norm bound required in this subsection.
Write singular values in decreasing order.
There are constants \(c,C>0\), uniform over \(F_n\), such that
\[
 \mathbb P\left\{\exists j\in[\lceil n^{3/4}\rceil,n-1]:
  s_{n-j}(W_n+F_n)<c\frac jn\right\}
 \le Cn^2\exp(-cn^{1/4}).
 \tag{14}
\]
Fix such a \(j\), put \(k=\lfloor j/2\rfloor\), and retain the first \(n-k\) rows of \(\sqrt n(W_n+F_n)\), giving a rectangular matrix \(B\).
For each retained row index \(i\), let \(H_i\) be the span of the other retained rows.
Delete coordinate \(i\) from that row and from \(H_i\).
The projected row has independent off-diagonal entries, and is independent of the projected row space: its mirrored partners are precisely the entries in column \(i\), which has been deleted.
The remaining deterministic shift is absorbed into \(f\) in (10).
The ambient dimension is \(n-1\), while the projected span has dimension at most \(n-k-1\), so its codimension is at least \(k\).
Equation (10), conditioning on the projected row space, proves that every retained row has distance at least \(c\sqrt k\) from the other rows, except on a set of probability at most \(Cn\exp(-cn^{1/4})\).
On this event \(B\) has full row rank, and the negative-second-moment identity gives
\[
 T:=\sum_{r=1}^{n-k}s_r(B)^{-2}
   =\sum_{i=1}^{n-k}\operatorname{dist}(B_i,H_i)^{-2}
   \le C\frac nk.
 \tag{15}
\]
Indeed, the Schur formula for the \(i\)-th diagonal entry of \((BB^*)^{-1}\) gives the reciprocal squared row distance, and taking its trace gives both sides of the identity.
There are at least \(j-k\) singular values of \(B\) no larger than \(s_{n-j}(B)\), and hence
\[
 (j-k)s_{n-j}(B)^{-2}\le T.
\]
Combining this with (15), row-deletion interlacing, and the factor \(1/\sqrt n\), yields
\[
 s_{n-j}(W_n+F_n)\ge n^{-1/2}s_{n-j}(B)
 \ge c\frac jn.
\]
A union bound over \(j\) proves (14).
The bound is summable and therefore works for every cross-size coupling.
It also holds conditionally for a random \(F_n\) independent of \(W_n\), because all constants are uniform in the shift.

### What one complex-symmetric invertibility lemma would settle

Let \(W_1,W_2\) be the two independent real Wigner inputs at size \(n\).
Consider the following candidate input, denoted CS: for each fixed centered unit-variance off-diagonal law, each fixed polynomial bound on a complex symmetric deterministic shift, and each \(B>0\), a polynomial lower threshold exists whose failure probability is \(O(n^{-B})\).
The input is required either for the actual diagonal laws, or uniformly with deterministic diagonals followed by conditioning on the actual diagonals.
This formulation is not yet adopted as a proved theorem here.

If CS is established, its zero-shift case gives \(s_{\min}(W_2)\ge n^{-a}\) outside an event of arbitrarily small polynomial probability.
On this event, \(-zW_2^{-1}\) is a polynomially bounded complex symmetric shift, independent of \(W_1\).
CS applied conditionally and the factorization
\[
 W_1W_2-zI=(W_1-zW_2^{-1})W_2
 \tag{16}
\]
give, for each fixed \(z\),
\[
 \mathbb P\{s_{\min}(W_1W_2-zI)<n^{-a_z}\}=O(n^{-B})
 \tag{17}
\]
for every prescribed \(B>0\), with \(a_z\) allowed to depend on \(B,z\) and the laws.
Here and below, an inequality concerning \(W_2^{-1}\) is only used on the good invertibility event.

Apply (14) to \(W_2\) and, conditionally, to \(W_1-zW_2^{-1}\).
For increasing singular values \(a_r\), the min--max product inequality is
\[
 a_{r+s-1}(AB)\ge a_r(A)a_s(B),\qquad r+s-1\le n.
 \tag{18}
\]
One proof intersects a dimension-\(n-r+1\) lower-bound subspace for \(A\) with the image under \(B\) of a dimension-\(n-s+1\) lower-bound subspace for \(B\), using invertibility on the good event.
Equations (14), (16), and (18) yield
\[
 a_r(W_1W_2-zI)\ge c(r/n)^2,
 \qquad r\ge Cn^{3/4},
 \tag{19}
\]
apart from a summable probability bound.
Combining (17)--(19), the empirical singular law \(\nu_{n,z}\) obeys almost surely, eventually,
\[
 \nu_{n,z}([0,t])\le C\sqrt t+Cn^{-1/4},\qquad
 s_{\min}(W_1W_2-zI)\ge n^{-a_z}.
 \tag{20}
\]
Stieltjes integration of (20) implies, for \(0<\delta<1\),
\[
 \int_{(0,\delta)}|\log t|\,d\nu_{n,z}(t)
 \le C\sqrt\delta\,(1+|\log\delta|)
      +Ca_zn^{-1/4}\log n.
 \tag{21}
\]
Thus CS plus (14) gives the required negative-log uniform integrability, with summable exceptions, rather than merely a smallest-value floor.
There is no remaining nested-array assumption in this implication.
For every fixed \(z\), first Borel--Cantelli suffices; Fubini then produces the almost-everywhere-in-\(z\) assertion on one probability-one event used by Hermitization.
Combined with the finite-variance weak singular laws, positive-log-tail control and logarithmic-potential identification being developed for the main Task, this would prove its two-real-factor special case under arbitrary cross-size coupling.

### Bounded direct adaptation work on CS

An independently available primary ingredient is [Nguyen, arXiv:1105.5733v1](https://arxiv.org/pdf/1105.5733), particularly Theorem 1.3 and Theorem 1.8 on PDF pp. 2--5.
Its linear and quadratic inverse Littlewood--Offord statements allow coefficients in \(\mathbb R^d\), with arbitrary linear terms in the quadratic concentration function.
Taking \(d=2\) supplies the actual complex-coefficient structural input needed by the complex-symmetric extension.
The [published article](https://cdm.ucalgary.ca/article/download/62130/46739/177715) was also inspected at its \(\mathbb R^d\) definitions and linear theorem; the later theorem inspection used the explicitly identified arXiv edition because repeated retrieval of the later journal pages failed.
This is a source for the structural input, not a citation of CS itself.

The following direct adaptation has been checked at the individual interfaces, but its full probability-profile count has not yet been rewritten and independently reviewed.
For a complex symmetric matrix, the cofactor matrix remains symmetric and satisfies the adjugate identities over \(\mathbb C\).
Normalize it by \((\sum|c_{ij}|^2)^{1/2}\), and retain the bilinear relation \(v^Tr_i=0\); inserting a conjugate into this algebraic relation would be an error.
Complex deterministic row shifts in the quadratic expansion contribute linear and constant terms, already allowed by the \(\mathbb R^2\) inverse theorem.
All norm and Cauchy--Schwarz estimates then use complex absolute values.

The resulting structured vectors have entries and GAP generators in \(\mathbb C\cong\mathbb R^2\).
Replacing a real rational grid by two rational coordinate grids multiplies the logarithm of its cardinality by a fixed factor; the exceptional-coordinate contribution remains \(O(n^{1-\varepsilon}\log n)=o(n)\).
The favorable GAP-size factor \(\rho^{-1}/\sqrt{n'}\) in the multidimensional inverse theorem is unchanged.
The support-covering lower bound for a concentration probability changes from a power of \(\beta\) to a power of \(\beta^2\), still a fixed polynomial when \(\beta=n^{-A}\).
Consequently the number of probability-profile bins stays bounded independently of \(n\), after enlarging its constants.

The one-dimensional clustering step also has an explicit replacement.
Suppose every \(q\)-element subcollection of complex numbers has more than \(q/2\) points in a disk of radius \(r\).
Projecting onto the real axis, sorting, and discarding at most \(q\) extreme indices places all remaining real coordinates in an interval of length \(2r\); do the same for imaginary coordinates.
After at most \(2q\) exceptions, the points lie in a square of side \(2r\), hence within \(2\sqrt2r\) of a common point.
This is enough for coarse complex-grid approximation, since doubling a sublinear exceptional set leaves it sublinear.
For even \(q=2h\), the real assertion follows by contradiction: if the interval between order statistics \(h\) and \(n-h+1\) has length greater than \(2r\), the \(h\) smallest and \(h\) largest points violate the hypothesis.
Changing the constants or discarding one additional point handles odd \(q\).

Finally, deterministic diagonals can be separated from the off-diagonal randomness in row exposure.
If \(\rho_i\) denotes the concentration function of the tail sum \(\sum_{j=i}^{n_0}u_j\xi_j\), the usual product with a random diagonal is \(\prod_{i=1}^{n_0}\rho_i\).
After conditioning on all diagonals, exposure uses strictly upper entries and gives \(\prod_{i=1}^{n_0-1}\rho_{i+1}\), losing only the factor \(1/\rho_1\).
At polynomial resolution and on the polynomial entry-truncation event, covering the complex support disk gives \(\rho_1\ge n^{-C_A}\).
This polynomial loss is harmless compared with the exponentially small structured-vector count, if that count has been established uniformly for complex shifts.
For independent finite-variance diagonal laws, the event that any raw diagonal exceeds \(n^K\) has probability \(O(n^{1-2K})\), so conditioning on polynomially bounded diagonals can have arbitrarily summable failure by choosing \(K\) large.
These observations identify the diagonal extension precisely; the printed iid-diagonal hypothesis has not simply been dropped from a quoted theorem.

The remaining check for CS is to complete the complex probability-profile enumeration with these changes and verify all constants are uniform over the polynomially bounded deterministic shift.
Until that check and the necessary source/review acceptance are complete, (17)--(21) are a conditional two-factor route, not an established finite-variance Brown theorem.

### An abandoned shortcut and its exact limitation

A polynomial smallest-value floor plus qualitative weak singular convergence cannot replace (14).
For example, put \(r_n=1/\sqrt{\log n}\) and
\[
 \nu_n=(1-r_n)\delta_1+r_n\delta_{n^{-A}}.
\]
Then \(\nu_n\Rightarrow\delta_1\) and every support point is at least \(n^{-A}\), while the negative logarithmic integral equals \(A\sqrt{\log n}\).
This is only a counterexample to that inference, not a Wigner model.
It explains why the summable intermediate control in (14) is substantive progress even if CS is eventually proved.

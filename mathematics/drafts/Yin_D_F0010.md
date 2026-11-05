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

<a id="complex-symmetric-gap"></a>
### A complete candidate proof of CS

An independently available primary ingredient is [Nguyen, arXiv:1105.5733v1](https://arxiv.org/pdf/1105.5733), particularly Theorem 1.3 and Theorem 1.8 on PDF pp. 2--5.
Its linear and quadratic inverse Littlewood--Offord statements allow coefficients in \(\mathbb R^d\), with arbitrary linear terms in the quadratic concentration function.
Taking \(d=2\) supplies the actual complex-coefficient structural input needed by the complex-symmetric extension.
The [published article](https://cdm.ucalgary.ca/article/download/62130/46739/177715) was also inspected at its \(\mathbb R^d\) definitions and linear theorem; the later theorem inspection used the explicitly identified arXiv edition because repeated retrieval of the later journal pages failed.
This is a source for the structural input, not a citation of CS itself.

The following proof closes the previously unwritten probability-profile enumeration as a candidate derivation.
It is not an independent review, and the two inverse Littlewood--Offord theorems remain explicitly identified external inputs.
No step imports the \(2+\tau\) assumption or the personal-communication extension from the product paper.

#### Statement and parameter convention

Let \(X_n\) be real symmetric with zero diagonal and iid off-diagonal entries of a fixed real law \(\xi\) satisfying \(\mathbb E\xi=0\) and \(\mathbb E\xi^2=1\).
For every \(\gamma,B>0\), there are \(A,C,n_0>0\), depending only on \(\xi,\gamma,B\), such that
\[
 \sup_{\substack{F=F^T\in M_n(\mathbb C)\\ \max_{ij}|F_{ij}|\le n^\gamma}}
 \mathbb P\{s_{\min}(X_n+F)\le n^{-A}\}
 \le Cn^{-B},\qquad n\ge n_0.
 \tag{CS}
\]
In particular the diagonal of \(F\) is arbitrary and deterministic.
Independent real diagonal variables with a fixed finite-second-moment law are allowed by the conditioning argument at the end of the proof.
All constants below may be enlarged finitely many times; the small exponent \(\varepsilon=1/100\) is fixed throughout.
Every exponent specifying a coordinate-rounding precision is chosen to be an integer.
The fractional exponents used for exception counts and probability bins do not specify coordinate meshes.

Choose an integer \(K\) larger than \(\gamma+2\) and \((B+5)/2\).
The probability that any raw off-diagonal entry exceeds \(n^K\) is \(O(n^{2-2K})\).
Conditional on their all being bounded, the entries remain independent with common law \(\xi_n=(\xi\mid |\xi|\le n^K)\).
The laws \(\xi_n\) have uniform constants in
\[
 \mathbb P\{c_1\le|\xi_n-\xi_n'|\le c_2\}\ge c_3>0,
 \tag{22}
\]
because \(\xi\) is nondegenerate and \(\xi_n\) converges in total variation to \(\xi\).
The same statement holds for the symmetrized law \(\eta(\xi_n-\xi_n')\) with an independent nontrivial Bernoulli selector \(\eta\).
The inverse theorems' constants depend only on their displayed anti-concentration constants, the fixed coefficient dimension two, and their fixed exponents, so they apply uniformly to these truncated laws.
Neither centering nor variance renormalization of \(\xi_n\) is needed in these inverse-theorem uses.
Absorb fixed factors into \(K\), so every entry of the truncated matrix \(M=X_n+F\) has absolute value at most \(n^K\).

#### Structured-vector consequence of quadratic concentration

Let \(D\) be a complex symmetric \(m\)-by-\(m\) matrix with entries bounded by \(n^K\), where \(m=n-1\).
Write \(C_D=\operatorname{adj}D\), assume \(C_D\ne0\), and put \(A_D=C_D/\|C_D\|_F\).
Suppose a quadratic form with quadratic coefficients \(A_D\), arbitrary complex linear coefficients, and iid real \(\xi_n\) variables has concentration at least \(n^{-b}\) in a disk of radius \(n^{-2a}\), where \(a\) is a positive integer.
Then there is an integer constant \(C_0\), depending on \(b,K,\varepsilon\) and (22) but not on \(a\), and a vector \(u\in\mathbb C^m\), with the following properties when \(a\) is sufficiently large:

- \(1/2\le\|u\|\le2\), and \(|(Du)_i|\le n^{-a+C_0}\) for all but \(C_0\) rows.
- All but \(C_0n^\varepsilon\) coordinates of \(u\) belong to a generalized arithmetic progression of rank at most \(C_0\) and size at most \(n^{C_0}\).
- Each real and imaginary coordinate of \(u\), and of the progression's generators, is rational with numerator and denominator bounded by \(n^{a+C_0}\).

Here a progression is a finite integer box mapped into \(\mathbb C\); properness is unnecessary for the counting consequence.
To establish the assertion, apply the vector-valued quadratic inverse theorem to \(A_D\in M_m(\mathbb R^2)\).
It gives a nonzero integer \(k\), a bounded list of rows indexed by \(I_0\), and integers \(k_{ij}\), all bounded by \(n^{O_b(1)}\), such that for all but \(O(n^\varepsilon)\) row indices
\[
 r_i'=k r_i(A_D)+\sum_{j\in I_0}k_{ij}r_j(A_D)
\]
has linear concentration at least \(n^{-O_b(1)}\) at radius \(n^{-2a+O_b(1)}\) for the symmetrized variables.
If one such \(r_i'\) has norm at least \(n^{-a}\), normalize it and apply the vector-valued linear inverse theorem.
This gives the progression and rational grid at resolution \(n^{-a+O_b(1)}\), including separate grid rounding of the exceptional coordinates.
Use a deterministic larger radius \(n^{-a+C}\) in this application, with integer \(C\), so the grid scale is an integer power of \(n\), hence rational and independent of the row's possibly irrational norm.
The adjugate identity \(A_DD=(\det D/\|C_D\|_F)I\) shows that the original normalized row is bilinearly orthogonal to all but \(|I_0|+1\) rows of \(D\).
Coordinate approximation changes each of these row products by at most \(n^{K+1}\) times the approximation error.

If every \(r_i'\) has norm below \(n^{-a}\), choose a column of \(A_D\) with norm at least \(m^{-1/2}\).
Its entries outside the exceptional index set are, within \(n^{-a+O_b(1)}\), integer combinations of the bounded list of selected column entries divided by \(k\).
Round the selected entries and exceptional coordinates on a complex rational lattice, and use those integer relations to define the other coordinates.
Keep the bounded index set \(I_0\) among the exceptional coordinates when making this definition, so no selected generator is overwritten by a relation.
The resulting vector approximates that column at norm error \(n^{-a+O_b(1)}\), has a progression of bounded rank and polynomial size, and has rational coordinates of the asserted height.
Multiply it by the integer \(\lceil1/\|v\|\rceil\), which is at most \(O(\sqrt n)\), to place its norm between one and two.
The adjugate identity gives bilinear orthogonality of the original column to all but one row, and the same error estimate applies.
All tolerances and rational heights are absorbed into \(C_0\).
The use of \(\lceil1/\|v\|\rceil\) avoids a zero multiplier when rounding makes \(\|v\|\) slightly larger than one.
These arguments use \(\sum|c_{ij}|^2\) for the Frobenius norm and \(\sum_jD_{ij}u_j\) for adjugate orthogonality; no Hermitian conjugation is inserted into that algebraic identity.

#### Uniform counting of the resulting complex vectors

We prove that a truncated random complex symmetric \(M\), with real iid off-diagonal randomness satisfying (22) and arbitrary deterministic complex entries bounded by \(n^K\), has such a vector with probability at most \(\exp(-cn)\), once \(a\) is chosen sufficiently large.
This argument works equally for a principal minor, since replacing \(n\) by \(n-1\) only changes fixed polynomial factors.
Let \(\beta_0=n^{-a+C_0}=n^{-s}\).
The number of possible vectors described above is
\[
 n^{C_*n+O_a(n^\varepsilon)+O_a(1)},
 \tag{23}
\]
with \(C_*\) independent of \(a\): the generators and box lengths have polynomially many choices, the nonexceptional coordinates have at most \(n^{C_0}\) choices each, and only \(O(n^\varepsilon)\) coordinates use the full rational grid.
The choice of exceptional indices is included in (23).

Add a largest coordinate of \(u\) as one additional progression generator if necessary.
This changes its size by a factor at most three and its rank by one.
Choose a bulk set of size \(n_0=n-O(n^\varepsilon)\), all of whose coordinates lie in the progression, containing that coordinate.
After a permutation determined by the exceptional set and the largest coordinate, suppose the bulk occupies \(1,\ldots,n_0\) and
\[
 |u_{n_0}|\ge(2\sqrt n)^{-1}.
 \tag{24}
\]
The number of these choices and permutations is \(\exp(o(n))\).
We retain an arbitrary set of at least \(n-C_0\) row constraints; it need not be a consecutive set.
There are at most \(n^{O(C_0)}\) choices of the omitted row indices, which are included in the union bounds below.

For a deterministic coefficient vector define
\[
 \rho_i(u,t)=\sup_{z\in\mathbb C}
 \mathbb P\left\{\left|\sum_{j=i}^{n_0}u_j\xi_{n,j}-z\right|\le t\right\}.
\]
These numbers are nondecreasing in \(i\).
For \(\beta_0\le t\le1\), covering the support disk of radius \(O(n^{K+1})\) by disks of radius \(t\) gives a uniform lower bound
\[
 \rho_i(u,t)\ge n^{-D},
 \tag{25}
\]
where \(D=O(s+K)\), also for coefficient vectors within distance \(O(\beta_0)\) coordinatewise of the norm-bounded vectors considered here.
The same lower bound, with an enlarged \(D\), applies to every rounded vector below.

Condition first on entries connecting the bulk to its complement, and then expose the bulk rows in increasing order.
The random part left in row \(i\) consists of strictly upper entries, so its conditional small-ball bound is \(\rho_{i+1}(u,t)\).
Omitting the at most \(C_0\) unconstrained rows and using (25) proves
\[
 \mathbb P\{|(Mu)_i|\le t\text{ on the prescribed rows}\}
 \le n^{D(C_0+1)}\prod_{i=1}^{n_0}\rho_i(u,t).
 \tag{26}
\]
This is the precise deterministic-diagonal adjustment: the shifted product starting at \(\rho_2\) loses only \(\rho_1^{-1}\), not one loss per row.
By (22) and (24), for \(t\le c/\sqrt n\), each tail concentration is at most a fixed \(p_0<1\).
The direct row-exposure bound is consequently \(p_0^{n_0-C_0-1}\) at this resolution.

Choose \(C_1>C_*+10\).
For vectors with \(\prod_{i=1}^{n_0}\rho_i(u,\beta_0)<n^{-C_1n}\), (23) and (26) already give total probability \(n^{-cn}\).
It remains to count vectors with the reverse inequality.
Put
\[
 q=\lceil n^{1-\varepsilon}\rceil,\qquad
 \kappa=\varepsilon/10,\qquad
 t_*=n^{-K-5}.
\]
Call a vector degenerate if every \(q\)-element subset of its bulk coordinates has concentration at least \(q^{-1/2+\kappa}\) at radius \(t_*\).
For each such subset, apply the linear inverse theorem with allowed exception count \(\lfloor q/2\rfloor\).
The progression-size bound becomes
\[
 |Q|\le\max\{Cq^{-\kappa},1\}=1
\]
eventually, so the proper symmetric progression is \(\{0\}\).
Thus at least \(\lceil q/2\rceil\) coordinates in every \(q\)-subset have modulus at most \(t_*\).
It follows that at most \(\lfloor q/2\rfloor\) bulk coordinates have modulus greater than \(t_*\), since otherwise a \(q\)-subset with too many such coordinates could be chosen.

Round these exceptional coordinates and the coordinates outside the bulk on a complex lattice of mesh \(t_*\), and set every other coordinate to zero.
There are at most \(\exp(O_K(q\log n))=\exp(o(n))\) resulting vectors \(u'\).
Their coordinate errors are at most \(2t_*\), so the row tolerance becomes at most
\[
 \beta_0+2n^{K+1}t_*\le3n^{-4}
\]
when \(s\) is large.
The large coordinate in (24) survives this rounding.
The direct bound \(p_0^{n_0-C_0-1}\) and a union bound therefore give \(\exp(-cn)\) for the degenerate vectors.
No order structure on \(\mathbb C\) is used.

For a nondegenerate vector, select a \(q\)-subset with concentration below \(q^{-1/2+\kappa}\), and include the large coordinate if it is not already in that set.
Place this set at the end of the bulk; its size is \(q_0\in\{q,q+1\}\).
This costs only \(\exp(O(q\log n))=\exp(o(n))\) choices.
Set \(p=n_0-q_0=n-o(n)\).
Every tail starting at \(i\le p\) contains the selected subset, so for every \(t\le t_*\),
\[
 \rho_i(u,t)\le n^{-b_0},\qquad
 b_0=1/2-3\varepsilon/4>1/2-\varepsilon.
 \tag{27}
\]
Let \(\pi_t(u)=\prod_{i=1}^p\rho_i(u,t)\).
The high-concentration case under consideration has \(\pi_{\beta_0}(u)\ge n^{-C_1n}\).
Take \(L=n^{K+3}\), \(t_\ell=L^\ell\beta_0\), and \(L_0=\lceil C_1/\varepsilon\rceil+2\).
Choose \(s\) so large that \(t_{L_0+1}\le t_*\).
For at least one \(0\le\ell\le L_0\),
\[
 \pi_{t_{\ell+1}}(u)\le n^{\varepsilon n}\pi_{t_\ell}(u),
 \tag{28}
\]
since otherwise iteration from \(n^{-C_1n}\) would exceed one.

Fix this \(\ell\), and partition the possible values of \(\rho_i(u,t_\ell)\) into bins \([r_h,n^\varepsilon r_h)\), with endpoints powers of \(n\), between the lower bound in (25) and the upper bound in (27).
There are only \(H=O_{s,K}(1)\) bins.
Monotonicity in \(i\) makes their index sets consecutive blocks, with sizes \(m_h\) summing to \(p\).
There are at most \((n+1)^H\) such profiles.
At the first index of each block apply the vector-valued linear inverse theorem to the entire corresponding tail, with exception count
\[
 n'=\lfloor n^{1-2\varepsilon}\rfloor.
\]
The tail has length at least \(q\), so this exception count lies in the permitted range of that theorem.
Rescale the tail if necessary; its norm is at most two, and the zero-norm case is immediate.
All but \(n'\) entries of that block can be rounded within \(t_\ell\) to a progression \(Q_h\) of bounded rank and size
\[
 |Q_h|\le C r_h^{-1}n^{-1/2+\varepsilon}.
 \tag{29}
\]
The maximum with one in the inverse theorem is harmless here: (27) implies the right side of (29) is at least a positive power of \(n\).
For clarity, if the tail norm is \(\sigma>0\), apply the inverse theorem to its normalized coefficients at radius \(t_\ell/\sigma\).
Each coordinate of a normalized generator has the form \((t_\ell/\sigma)p_{ij}/p\), so rescaling the generator by \(\sigma\) gives exactly \(t_\ell p_{ij}/p\).
The possibly irrational norm therefore cancels, and \(\sigma\le2\) bounds the integers \(p_{ij}\) and \(p\) polynomially in \(n\).
Since \(t_\ell\) is an integer power of \(n\), these rescaled real and imaginary generator coordinates are rational of polynomial height.
Thus the finitely many progressions have only polynomially many choices.
Round the at most \(Hn'+q_0+(n-n_0)=o(n)\) remaining coordinates on the complex \(t_\ell\)-lattice.
The choices of their positions and values contribute \(\exp(o(n))\), since their number is \(O(n^{1-\varepsilon})\) and the mesh has polynomial precision.

Consequently the number of rounded vectors for this profile is at most
\[
 \exp(O(n)+o(n))\,
 n^{-(1/2-\varepsilon)p}\prod_h r_h^{-m_h}.
 \tag{30}
\]
Every such rounded vector has at least one original witness in the fixed profile.
Choose one witness for each rounded vector.
Its row tolerance is at most \(t'=\beta_0+Cn^{K+1}t_\ell\).
For every tail, comparing the rounded vector with that witness changes the sum by at most \(Cn^{K+1}t_\ell\), hence
\[
 \rho_i(u',t')\le\rho_i(u,t_{\ell+1})
\]
for all large \(n\).
Use (26), discard the last \(q_0\) tail factors, and apply (28) and the profile upper endpoints.
The probability for each rounded vector is at most
\[
 n^{O_{s,K,C_0}(1)}n^{2\varepsilon n}\prod_h r_h^{m_h}.
 \tag{31}
\]
Multiplying (30) and (31) cancels the concentration factors exactly.
Since \(p=n-o(n)\), the result is at most
\[
 \exp(O(n)+o(n))\,
 n^{-(1/2-\varepsilon)p+2\varepsilon n}
 \le n^{-n/3}
 \tag{32}
\]
eventually.
The polynomial number of profiles, bounded number of scales, and \(\exp(o(n))\) reservoir/permutation choices do not change this conclusion.
This completes the structured-vector counting bound uniformly over every allowed deterministic complex shift and deterministic diagonal.

The parameter order is noncircular.
First fix \(b,K,\varepsilon\), then the structural constant \(C_0\) and leading entropy constant \(C_*\), then \(C_1,L_0\), and finally choose \(a\) so that \(s=a-C_0\) meets the scale requirements.
Constants from the later linear inverse applications may depend on \(a\), but they affect only the polynomial number of progressions, fixed multiplicative constants to the power \(n\), and the \(\exp(o(n))\) exceptional-coordinate factors.
They do not alter the negative \(n\log n\) coefficient in (32).

#### From the counting lemma to the smallest singular value

First restrict to invertible \(M\).
If \(s_{\min}(M)\le n^{-A}\), then \(\|\operatorname{adj}M\|_F\ge n^A|\det M|\).
For some row index, after paying a factor \(n\) in a union bound, its squared cofactor-row norm is at least \(n^{2A-1}|\det M|^2\).
Delete the corresponding row and column to obtain \(D\).
Cofactor expansion and Cauchy--Schwarz, with \(\max|M_{ij}|\le n^K\), give
\[
 \|r_i(\operatorname{adj}M)\|^2
 \le 2n^{2K+1}\|\operatorname{adj}D\|_F^2.
\]
Therefore \(\operatorname{adj}D\ne0\) and
\[
 \frac{|\det M|}{\|\operatorname{adj}D\|_F}
 \le\sqrt2\,n^{-A+K+1}.
 \tag{33}
\]
Choose \(A\ge2a+K+3\), so the last quantity is at most \(n^{-2a}\).
Conditional on \(D\), the off-diagonal entries of the deleted row are independent of \(D\), and the determinant divided by \(\|\operatorname{adj}D\|_F\) is a quadratic form whose quadratic matrix is, up to sign, \(A_D\).
Its linear and constant coefficients may be complex and are allowed to be arbitrary.
If its conditional concentration is below \(n^{-b}\), the event in (33) costs at most \(n^{-b}\).
Otherwise the structural consequence above produces one of the vectors counted in (23)--(32) for \(D\).
Taking \(b>B+3\) proves an \(O(n^{-B-1})\) bound for the event that \(M\) is invertible and has the stated small singular value, uniformly over \(F\).

To include matrices of every rank, no rank-boost extension is needed.
For each fixed realization of \(M\), the polynomial \(t\mapsto\det(M+tI)\) is monic of degree \(n\), so it has only finitely many real zeros.
Tonelli implies that for almost every deterministic real \(t\) in any nonempty interval, \(M+tI\) is invertible almost surely.
Choose such a \(t\) with \(0<t\le n^{-A-1}\).
The Lipschitz inequality for the least singular value gives
\[
 \{s_{\min}(M)\le n^{-A-1}\}
 \subseteq
 \{s_{\min}(M+tI)\le2n^{-A-1}\}.
\]
Apply the invertible estimate to the deterministic symmetric shift \(F+tI\), whose entries satisfy the same polynomial bound with a harmless exponent increase.
The constants are uniform in this choice of \(t\).
This proves the desired estimate for all \(M\), after increasing the final exponent by one.
Add the discarded probability \(O(n^{2-2K})\) to obtain (CS) for the original finite-variance entries.

#### Independent diagonal laws and normalization

Let the raw diagonal entries instead be independent copies of a fixed real law \(\zeta\), independent of the off-diagonal variables, with \(\mathbb E|\zeta|^2<\infty\).
For any prescribed \(B\), choose \(K_d\) so large that
\[
 \mathbb P\{\max_i|\zeta_i|>n^{K_d}\}
 \le n^{1-2K_d}\mathbb E|\zeta|^2=O(n^{-B-2}).
\]
Conditional on any diagonal realization in this event's complement, absorb that diagonal into \(F\) and use the uniform deterministic-diagonal theorem.
This proves the same arbitrary polynomial failure bound for these diagonal laws, including deterministic zero diagonals.
Replacing \(X_n\) by \(W_n=X_n/\sqrt n\) only increases the deterministic-shift exponent by \(1/2\) before application and changes the final singular-value exponent by \(1/2\).
Thus the candidate CS theorem has exactly the normalization and diagonal scope needed in (16)--(21).

The proof supplied here is a proposed complete mathematical adaptation, with the external vector-valued inverse theorems stated at their actual scope.
It still requires independent review and source-input acceptance before it can be used as an accepted theorem or to declare the two-factor Brown-convergence pilot complete.

### An abandoned shortcut and its exact limitation

A polynomial smallest-value floor plus qualitative weak singular convergence cannot replace (14).
For example, put \(r_n=1/\sqrt{\log n}\) and
\[
 \nu_n=(1-r_n)\delta_1+r_n\delta_{n^{-A}}.
\]
Then \(\nu_n\Rightarrow\delta_1\) and every support point is at least \(n^{-A}\), while the negative logarithmic integral equals \(A\sqrt{\log n}\).
This is only a counterexample to that inference, not a Wigner model.
It explains why the summable intermediate control in (14) is substantive progress even if CS is eventually proved.

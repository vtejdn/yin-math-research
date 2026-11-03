---
author: Yin
---
# Square-summable marginal phases and the failure of universal phase lifting

Date: 2026-10-14T13:56.
Human author Yin.
The acsy_to_full_domain agent developed the marginal coefficient estimate and the finite-model obstruction under the explicit request to continue comparing ACSY24's actual-vacuum condition with bare full-domain duals.
Root suggested the all-row harmonic lower bound and requested this fixed complete candidate.
No independent review of the complete fixed material has yet been adopted.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

### A. Square-summable phase coefficients suffice

Let (M,tau) be finite tracial with faithful normal tracial state, H=L2(M,tau), Omega=1 and P=P_Omega.
Let X=(X_1,...,X_d) be bounded normal generators of M.
Suppose complex-linear maps D_i:M Omega to H satisfy

\[
 [X_j,D_i]=\delta_{ij}P\quad\hbox{on }M\Omega.
 \tag{1}
\]

No continuity, closability or adjoint-domain hypothesis is imposed on the supplied maps.
By [C_F0070 Part A](Yin_C_F0070_v1.md#statement), the marginal laws mu_i are diffuse, the normalized maps

\[
 E_i(a)=-D_i(a\Omega)+aD_i\Omega
 \tag{2}
\]

are bounded M with its operator norm to H, and they induce unique outer derivations delta_i on A=C<X,X*> with

\[
 \delta_i(X_j)=\delta_{ij}1\otimes1,\qquad
 \delta_i(X_j^*)=\delta_{ij}k_i,\qquad
 k_i(z,w)=\frac{\bar z-\bar w}{z-w}\quad(z\ne w).
 \tag{3}
\]

The diagonal value is irrelevant because mu_i is diffuse.
Write N_i=W*(X_i) and C_i=||E_i:M to H||.
Assume that for every i there are a_in,b_in in N_i such that

\[
 \overline{k_i(z,w)}=\sum_{n=1}^{\infty}a_{in}(z)b_{in}(w)
 \quad(\mu_i\otimes\mu_i\hbox{-almost everywhere}),
 \tag{4}
\]

and the pointwise increasing sums of nonnegative functions satisfy

\[
 A_i^2=\left\|\sum_{n\ge1}|a_{in}|^2\right\|_\infty<\infty,
 \qquad
 B_i^2=\left\|\sum_{n\ge1}|b_{in}|^2\right\|_\infty<\infty.
 \tag{5}
\]

No convergence of the square-sum tails in L-infinity norm is required.
The series (4) is automatically pointwise absolutely convergent outside product-null sets by Cauchy-Schwarz.

Then the left contractions F_i=(tau tensor id)delta_i satisfy

\[
 \|F_i(p)\|_2\le \frac4{\sqrt\pi}C_iA_iB_i\|p\|
 \qquad(p\in A).
 \tag{6}
\]

Consequently the actual ACSY24 vacuum adjoints exist, with

\[
 \xi_i=\delta_i^*(1\otimes1),\qquad
 \|\xi_i\|_2\le2C_i\left(1+\frac4{\sqrt\pi}A_iB_i\right).
 \tag{7}
\]

The canonical contraction E_i0=E_i|A Omega is closable, and its original Hilbert closure and actual adjoint both have every bounded vector in their domains:

\[
 M\Omega\subseteq\operatorname{Dom}\overline{E_{i0}}
                \cap\operatorname{Dom}E_{i0}^*.
 \tag{8}
\]

These conclusions concern the canonical core operators.
They do not identify arbitrary supplied full-domain maps with these closures outside the core.

### B. Boundedness of the phase alone does not suffice for a universal lifting estimate

There is no numerical constant K such that for every finite commutative tracial algebra M, every normal x in its unit ball, and every bounded E:M to L2(M), the pointwise phase Schur action satisfies

\[
 \|Q_{k_x}(E)\|_{\infty\to2}\le K\|E\|_{\infty\to2},
 \quad k_x(z,w)=\frac{\bar z-\bar w}{z-w}\ (z\ne w),
 \quad k_x(z,z)=0.
 \tag{9}
\]

The same failure holds for the conjugate phase.
Explicit models below have

\[
 \|E_n\|_{\infty\to2}\le\frac\pi{\sqrt2},\qquad
 \|Q_{k_x}(E_n)\|_{\infty\to2}
 \ge\frac3{5\sqrt2}H_{n-1},
 \tag{10}
\]

where H_m=sum_{j=1}^m 1/j.
The failure also persists when E is normalized by E(1)=0 and the lifted map is subsequently normalized at 1.

The finite atomic models in Part B are not full-domain dual systems: an atomic normal coordinate cannot have (1).
They refute only the universal lifting shortcut which ignores the special commutator identities.
They do not refute the general implication from bare full-domain duals to the ACSY24 condition.

## Argument

### 1. Reuse and the exact Grothendieck input

[C_F0070](Yin_C_F0070_v1.md#statement) supplies the bounded E_i, diffuse marginals and unique starred derivations under precisely (1).
[C_F0072](Yin_C_F0072_v1.md#statement) supplies the actual vacuum and both canonical domains once both contractions are bounded.
[C_F0039](Yin_C_F0039_v1.md#yin_c_f0039-p1) supplies the earlier projectively summable coefficient mechanism, at its original closable full-domain scope.
The proof below replaces its absolute coefficient-norm summation by (5), removes its closability premise using C_F0070, and uses C_F0072 to obtain an actual L2 vacuum.

The exact external inequality already checked in [Pis12-U001](../audits/literature/Pis12/Yin_U001.md#pis12-u001), Theorem 5.2(ii), is

\[
 \sum_n\|Tb_n\|_H^2\le\frac4\pi\|T\|^2
            \left\|\sum_n|b_n|^2\right\|_\infty
 \tag{11}
\]

for a bounded complex-linear map T from any commutative unital C*-algebra to a complex Hilbert space and a finite family b_n.
Each application below can be restricted to the unital commutative C*-algebra generated by its coefficient family, so no normality of T or identification of a Pietsch measure with tau is presumed.

The noncommutative little Grothendieck theorem was also inspected as a possible alternative: the author's January 26, 2011 [83-page survey](https://webusers.imj-prg.fr/~gilles.pisier/grothendieck.pdf), Theorem 8.1, printed p.25/PDF p.27, gives the two-state and row/column forms.
It is not needed as an additional dependency, since the coefficients used here belong to a single commutative marginal algebra and (11) gives the sharper required constant.
Its two-state domination does not by itself prove (9).

The earlier [AP16 phase reading](../audits/literature/AP16/Yin_U001.md) refutes a universal B(H) Schur lifting; the proof of Part B here addresses the different Banach norm B(M,L2(M)) directly.
The original AP16 PDF could not be re-fetched during this pass, so no new source inspection beyond that retained record is claimed.

### 2. The marginal coefficient series defines a bounded map

Fix i and omit its subscript.
For p in M set

\[
 Q(p)=\sum_{n\ge1} E(pb_n)a_n.
 \tag{12}
\]

For the bounded map T_p:N to H, T_p(b)=E(pb), one has ||T_p||<=C||p||.
Apply (11) to each initial finite coefficient family and pass to the increasing limit:

\[
 \sum_{n\ge1}\|E(pb_n)\|_2^2
 \le\frac4\pi C^2\|p\|^2 B^2.
 \tag{13}
\]

Right multiplication rho(a)xi=xi a gives a row operator from the Hilbert direct sum of copies of H to H.
For finite families its norm is at most A, since

\[
 \sum_n\rho(a_n)\rho(a_n)^*
 =\rho\!\left(\sum_n a_n^*a_n\right),
 \qquad
 \left\|\sum_n a_n^*a_n\right\|\le A^2.
 \tag{14}
\]

For any finite interval of indices, (14) bounds the corresponding output sum by A times the l2 norm of the input vectors.
The input sequence in (13) is square summable.
Therefore (12) converges strongly in H for every p in M, even though the tails in (5) need not tend to zero in operator norm.
Moreover

\[
 \|Q(p)\|_2\le\frac2{\sqrt\pi}CAB\|p\|.
 \tag{15}
\]

This proves a genuine bounded linear map on all M.
It does not assert operator-norm convergence of the finite maps Q_N.

### 3. The series implements the conjugate derivation on the core

Let Theta:H tensor_2 H to S2(H) be the unitary map Theta(g tensor h)=gPh.
Bounded right coefficients satisfy

\[
 \rho(a)\Theta(g\otimes h)\rho(b)
 =\Theta(ga\otimes bh).
 \tag{16}
\]

Every right multiplier commutes with bounded left multiplication.
Thus for Q_N, the first N terms of (12),

\[
 [Q_N,X_j]=\delta_{ij}\Theta\!\left(\sum_{n\le N}a_n\otimes b_n\right)|_M.
 \tag{17}
\]

For j different from i the commutator with X_j* is also zero, by C_F0070.
For j=i its tensor kernel is

\[
 k_i(z,w)\sum_{n\le N}a_n(z)b_n(w),
 \tag{18}
\]

because every coefficient belongs to N_i.
Pointwise Cauchy-Schwarz gives

\[
 \left|\sum_{n\le N}a_n(z)b_n(w)\right|\le AB.
\]

The kernels converge almost everywhere to bar k_i by (4), and multiplication by k_i preserves their absolute bound.
Dominated convergence in the marginal product L2 space gives Hilbert-Schmidt convergence of (17)-(18).
Strong convergence Q_N(p) to Q(p), applied also to X_j p and X_j* p, therefore proves on all M

\[
 [Q,X_j]=\delta_{ij}\Theta(\overline{k_i}),\qquad
 [Q,X_j^*]=\delta_{ij}P.
 \tag{19}
\]

Diffuseness is used in k_i bar k_i=1 almost everywhere.

Define the conjugate derivation by

\[
 \delta_i^\dagger(p)=(\delta_i(p^*))^\dagger,
 \qquad (g\otimes h)^\dagger=h^*\otimes g^*.
\]

It is complex-linear and satisfies the outer Leibniz rule.
Symmetry k_i(z,w)=k_i(w,z) makes its generator values exactly the two kernels in (19).
The commutator product rule therefore identifies its Hilbert-Schmidt implementation with [Q,p] for every p in A.
Evaluating at Omega and normalizing yields

\[
 Q^0(p):=Q(p)-pQ(1)
 = (\mathrm{id}\otimes\tau)\delta_i^\dagger(p)
 \quad(p\in A).
 \tag{20}
\]

Hence

\[
 F_i(p)=\bigl(Q^0(p^*)\bigr)^*.
 \tag{21}
\]

By (15), ||Q^0||_{infinity to 2}<=2||Q||<=4CAB/sqrt(pi), proving (6).

### 4. Vacuum and actual domains

The right contraction of delta_i is E_i on A, with norm at most C_i, by C_F0070.
The left contraction has (6).
Apply C_F0072 with these two constants.
Its quantitative vacuum estimate gives (7), and its exact core-adjoint and original-closure graph argument gives (8).
No closability of the supplied D_i is used to establish either bound.

Condition (5) includes every projectively summable expansion used in C_F0039.
Indeed, if sum_n ||c_n||||d_n||<infinity, rescale each nonzero elementary tensor by

\[
 a_n=\left(\frac{\|d_n\|}{\|c_n\|}\right)^{1/2}c_n,
 \quad
 b_n=\left(\frac{\|c_n\|}{\|d_n\|}\right)^{1/2}d_n.
\]

Then a_n tensor b_n=c_n tensor d_n, and both square sums are bounded by sum_n ||c_n||||d_n||.
The present proof additionally allows bounded square sums whose tails do not converge in L-infinity norm.
No strict inequality between finite commutative projective and Hilbert-factorization tensor norms is claimed; the completion and convergence conditions are what differ here.

### 5. A uniform bound for the input matrices

For n>=2 let M_n=C^{2n} with normalized counting trace, and let H_n=L2(M_n).
Label the coordinates z_1,...,z_n,w_1,...,w_n.
Let x_n have distinct values

\[
 z_i=2^{i-n},\qquad w_j=\mathrm i\,2^{j-n}.
 \tag{22}
\]

Thus x_n is normal and ||x_n||<=1.
Define E_n:M_n to H_n by

\[
 (E_n f)(z_i)=\sum_{\substack{1\le j\le n\\j\ne i}}
                 \frac{f(w_j)}{i-j},\qquad
 (E_n f)(w_j)=0.
 \tag{23}
\]

We record the complete Fourier proof of the matrix bound needed here.
On L2 of the circle with normalized measure, multiplication by

\[
 m(t)=\mathrm i(\pi-t),\qquad0<t<2\pi,
\]

has norm at most pi.
Direct integration gives its Fourier coefficients m_hat(0)=0 and m_hat(k)=1/k for every nonzero integer k.
Apply this multiplication operator to the trigonometric polynomial sum_{j=1}^n v_j exp(i j t), and project its Fourier coefficients onto indices 1,...,n.
The resulting matrix is H_ij=1/(i-j) off the diagonal and zero on the diagonal.
Parseval and orthogonal projection therefore give

\[
 \|H_n:\ell_2^n\to\ell_2^n\|\le\pi.
 \tag{24}
\]

Since ||(f(w_j))||_{ell2}<=sqrt(n)||f||infinity and the target H_n norm includes the factor 1/sqrt(2n), (24) proves

\[
 \|E_n\|_{\infty\to2}\le\pi/\sqrt2.
 \tag{25}
\]

This is the usual discrete Hilbert-transform matrix estimate, proved here in the exact form used.
Source attribution was checked against H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73-82, [author-hosted original article](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf), introduction p.73, equation (1.1) and the following sharp-constant discussion.
Its full original proof is not an input or a new full-paper audit; (24) is proved directly above.

### 6. Phase lifting creates a logarithmic lower bound

For a finite diagonal algebra, Q_k acts on the ordinary matrix of E by entrywise multiplication:

\[
 (Q_kE)_{rs}=k(x_r,x_s)E_{rs}.
 \tag{26}
\]

For the cross-block entries in (23), the phase is

\[
 k_{ij}=\frac{2^{i-n}+\mathrm i2^{j-n}}
              {2^{i-n}-\mathrm i2^{j-n}},\qquad
 \operatorname{Re}k_{ij}
 =\frac{1-2^{2(j-i)}}{1+2^{2(j-i)}}.
 \tag{27}
\]

For i different from j this gives

\[
 \operatorname{Re}\frac{k_{ij}}{i-j}
 =\frac{1-4^{-|i-j|}}{1+4^{-|i-j|}}\frac1{|i-j|}
 \ge\frac3{5|i-j|}.
 \tag{28}
\]

Take f equal to 1 on the w-block and 0 on the z-block, so ||f||infinity=1.
Every output row has real part at least

\[
 \frac35\bigl(H_{i-1}+H_{n-i}\bigr)
 \ge\frac35 H_{n-1}.
\]

The last inequality follows by comparing the last n-i terms of H_{n-1} with the first n-i terms.
There are n such rows out of 2n equally weighted coordinates.
Consequently

\[
 \|Q_kE_n\|_{\infty\to2}
 \ge\frac3{5\sqrt2}H_{n-1}.
 \tag{29}
\]

The same computation holds for bar k because its real part is the same.
Combining (25) and (29) shows that the norm of this phase action on B(M_n,H_n) is at least 3H_{n-1}/(5pi), tending to infinity.
This proves Part B directly in the required infinity-to-L2 norm.

### 7. Normalizing both maps does not remove the obstruction

Put v_n=E_n(1) and B_n(f)=tau(f)v_n.
Then

\[
 E_n^0=E_n-B_n,\qquad E_n^0(1)=0,\qquad
 \|E_n^0\|_{\infty\to2}\le\sqrt2\pi.
\]

The matrix of B_n is v_n(r)/(2n).
Since |k|<=1,

\[
 |(Q_kB_n)f(r)|
 \le|v_n(r)|\|f\|_\infty,
 \qquad
 \|Q_kB_n\|_{\infty\to2}\le\|v_n\|_2\le\pi/\sqrt2.
 \tag{30}
\]

Define the subsequently normalized lift

\[
 R_n(f)=(Q_kE_n^0)(f)-f\,(Q_kE_n^0)(1).
\]

For the block indicator f used above, the subtracted term is zero on the z-block.
All output of Q_kE_n^0 is on that block, because both E_n and B_n have zero w-rows.
Thus (29)-(30) give

\[
 \|R_n\|_{\infty\to2}
 \ge\frac1{\sqrt2}\left(\frac35H_{n-1}-\pi\right).
 \tag{31}
\]

The right side tends to infinity while the normalized input maps have the fixed bound sqrt(2)pi.
The same holds with the conjugate phase.
This verifies the strengthened normalization assertion without introducing an unproved dual relation.

## Scope and continuation

Part A supplies an explicit sufficient phase condition for the full-domain-to-ACSY implication and restores both canonical domains.
It does not prove that every normal marginal has such a factorization, nor that the special commutator relations force one.
Part B shows that no proof can obtain the necessary lifting estimate for arbitrary E merely from its infinity-to-L2 norm and boundedness of the phase.
A successful general argument must use more of the dual identities or another source of structure.

Both parts were derived symbolically; no finite model is treated as evidence of a true dual-system counterexample.
The arbitrary correlated-normal equivalence remains unresolved by this candidate.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:56 |
| status | open |
| reason | Complete candidate giving a square-summable phase sufficient condition and an exact obstruction to a universal infinity-to-L2 lifting shortcut; independent fixed-version review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sufficient condition and obstruction](#statement) | Both parts, including canonical domains, quantitative bounds and normalized lifting failure. |
| argument | [Complete argument](#argument) | Sections 1-7, with strong convergence, Hilbert-Schmidt commutator limits and the explicit Fourier-matrix obstruction. |
| dependency | [Bare normal dual derivations](Yin_C_F0070_v1.md#statement) | Part A gives the bounded normalized right contractions, diffuse laws and exact starred values. |
| dependency | [Two-contraction criterion](Yin_C_F0072_v1.md#statement) | Actual vacuum, quantitative bound and both domains of the canonical closure once (6) is proved. |
| dependency | [Little Grothendieck inequality](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Exact finite-family commutative inequality with squared constant 4/pi, applied to b -> E_i(p b) on the marginal algebra. |

### Decision reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T14:11 |
| status | proved |
| reason | The complete fixed phase-coefficient proof and universal lifting obstruction passed independent review, including both normalizations. The square-sum coefficient hypothesis remains an additional condition; the finite atomic obstruction is not a rank-one dual counterexample. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sufficient condition and obstruction](#statement) | Both parts, including canonical domains, quantitative bounds and normalized lifting failure. |
| argument | [Complete argument](#argument) | Sections 1-7, with strong convergence, Hilbert-Schmidt commutator limits and the explicit Fourier-matrix obstruction. |
| dependency | [Bare normal dual derivations](Yin_C_F0070_v1.md#statement) | Part A gives the bounded normalized right contractions, diffuse laws and exact starred values. |
| dependency | [Two-contraction criterion](Yin_C_F0072_v1.md#statement) | Actual vacuum, quantitative bound and both domains of the canonical closure once (6) is proved. |
| dependency | [Little Grothendieck inequality](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Exact finite-family commutative inequality with squared constant 4/pi, applied to b -> E_i(p b) on the marginal algebra. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0139_v1.md#conclusion) | Exact fixed statement and complete argument, with actual source interfaces, review arrangement and unresolved scope disclosed. |

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:02 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Both parts, including canonical domains, quantitative bounds and normalized lifting failure. |
| argument | [Exact material](#argument) | Sections 1-7, with strong convergence, Hilbert-Schmidt commutator limits and the explicit Fourier-matrix obstruction. |
| dependency | [Exact material](Yin_C_F0070_v1.md#statement) | Part A gives the bounded normalized right contractions, diffuse laws and exact starred values. |
| dependency | [Exact material](Yin_C_F0072_v1.md#statement) | Actual vacuum, quantitative bound and both domains of the canonical closure once (6) is proved. |
| dependency | [Exact material](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Exact finite-family commutative inequality with squared constant 4/pi, applied to b -> E_i(p b) on the marginal algebra. |
| review | [Original finding](../audits/reviews/Yin_R_F0139_v1.md#conclusion) | Whole Sections 1–7 phase square-sum coefficient implementation, actual vacuum/canonical domains, exact Fourier matrix lifting obstruction and both normalizations; initial-context relationship unknown, not inferred self from C_F0072 dependency authorship. |

---
author: Yin
---

# Conjugation estimates for finite signed shells and excess kernel dimension

## Statement

Fix an individual torsion-free word-hyperbolic four-line group on the event giving two freely generating marked elements \(u,v\). [C59](Yin_C_A0059_v1.md#statement)
The conjugation estimates (1)–(3) also work in any finitely generated group containing such a pair for which the stabilizer of every \(g\ne e\) under conjugation by \(F=\langle u,v\rangle\) is amenable.
The four-line applications to trace integrality from spatial decay and to an operator-norm obstruction below use the additional inputs given there.
Write \(\mathsf P\) for averaging conjugation by \(u,u^{-1},v,v^{-1}\), \(\rho=\sqrt3/2\), and \(b=2\max(|u|,|v|)\).
All matrix traces are unnormalized, and the trace \(L^2\) norm is the coefficient square norm with the Hilbert–Schmidt norm at each group element.

1. For the finite signed sums of [C76](Yin_C_A0076_v1.md#statement), fix that claim's return hypothesis (2) and choices of \(\alpha,\beta,\kappa,L,z_j,N_j\).
   Let \(Q=I-A^*A/M\) be its positive contraction, and compute the ordinary finite polynomial
   \[
           K_j=(1-z_j)\sum_{l=0}^{N_j}z_j^l Q^l .
   \]
   Choose \(a>\beta/(2\log_2(1/\rho))\), set \(k_j=\lceil a(j+1)\rceil\), and write \(S_j=\{2^j\le |g|<2^{j+1}\}\).
   Enlarge this shell by \(bk_j\) in each radial direction and omit the identity to get \(S_j^+\).
   It suffices to estimate
   \[
             t_j=\|1_{S_j^+}(I-\mathsf P)\widehat K_j\|_2 .             \tag{1}
   \]
   For \(J\ge J_0\) there are constants \(C,\eta>0\), independent of \(J\), such that both the C76 finite-shell array and the actual kernel projection satisfy
   \[
     \max\big\{\|B_\bullet\|_{\beta,\,|g|\ge2^J},
                 \|\widehat p_A\|_{\beta,\,|g|\ge2^J}\big\}
       \le C\left(\sum_{j\ge J}2^{\beta j}t_j^2\right)^{1/2}
                   +C2^{-\eta J}.                                     \tag{2}
   \]
   The squared spatial norm has weight \((1+|g|)^\beta\).
   Each \(t_j\) uses a signed insertion of a single conjugation difference of the *original* Gram matrix into finite products.
   On the good four-line group, summability of these measured differences for \(\beta>3\) gives integral kernel trace. [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace)

2. A different finite estimate uses a fit of rows of the input and requires no positive spectral mass hypothesis.
   Let \(S\) be an \(m\)-by-\(m\) group-ring matrix boundedly invertible in the regular representation, possibly the identity, where \(A\) has \(m\) columns.
   Put \(C_0=AS\), \(T=C_0^*C_0\), \(T_0=\widehat T(e)\), and \(W=\bigcap_g\ker \widehat C_0(g)=\ker T_0\subset\mathbb C^m\).
   Suppose \(C_0\ne0\) and write \(\lambda>0\) for the smallest positive eigenvalue of the finite matrix \(T_0\).
   For words \(h\) drawn from the \(n\)-step uniform walk on the four free letters, choose any finite group-ring matrices \(X_h\) of the square output size and compute
   \[
        E^2=\mathbb E_h\|C_0 h-X_h C_0\|_2^2,\quad
        \delta_n=\|\mathsf P^nT-T_0\|_2
                         \le \rho^n\|T-T_0\|_2 .
   \]
   Right multiplication by \(h\) here means multiplication by the scalar diagonal matrix on the input coordinates.
   For \(z=(\dim_G\ker A-\dim W)^{1/2}\) one has
   \[
             0\le z\le\frac{\delta_n+\sqrt{\delta_n^2+4\lambda E^2}}
                                  {2\lambda}.                          \tag{3}
   \]
   Each least-squares fit with bounded word support for \(X_h\) is a finite ordinary Gram calculation over original group-product fibers.
   If these data give \(E\to0\) along \(n\to\infty\), the actual kernel projection has an exponentially weighted square sum and can be reconstructed from \(S,W\).
   This criterion makes no assumption of a closed-range group-ring matrix with the same kernel.
   For a nonzero scalar input and \(S=I\), a right-hand side in (3) strictly less than \(1/\sqrt s\) rules out every nonzero algebraic right annihilator with at most \(s\) terms anywhere in the group.

<a id="argument"></a>
## Conjugation on the nonidentity coefficients

For \(g\ne e\) the conjugation orbit of \(g\) under \(F\) is \(F/J\) with \(J=F\cap C_G(g)\).
In the stated hyperbolic group \(g\) has infinite order.
It acts on the boundary with two fixed points, and anything commuting with it preserves their pair.
An infinite maximal amenable subgroup containing \(g\) is the stabilizer of this pair and is virtually cyclic, so \(J\) is amenable. [Boutonnet–Carderi, Lemma 2.2(i) and its proof](../literature/pdf/BC15--arxiv-v2.pdf#page=6)

On each \(\ell^2(F/J)\) the one-step average over the four letters has norm at most \(\rho\), the upper bound for the corresponding average on the four-regular tree.
To check the comparison, lift a finitely supported vector on the cosets to the chosen representatives times a common finite Følner set in \(J\), dividing its values by the square root of the size of that set.
For its support and the four neighboring translates only finitely many transition elements in \(J\) occur.
The inner products with each of the four regular shifts then tend to the coset inner products by the Følner property, and the norm of the vector is unchanged.
For the trivial or a finite stabilizer the lift uses the whole stabilizer.
On the tree the sum of the four generator shifts has norm at most \(2\sqrt3\), by orienting it toward one end and bounding the form on each edge as in [C64](Yin_C_A0064_v1.md#the-row-map-and-its-kernel).
This proves the claimed bound on each coset space, and hence on their direct sum, with matrix coordinates left unchanged.
Each conjugation step changes word length by at most \(b\).

## Signed estimates on widened shells

For any square-summable coefficient array \(f\) on nonidentity elements, the exact identity
\[
      f=\sum_{l=0}^{k-1}\mathsf P^l(I-\mathsf P)f+\mathsf P^k f
\]
and the contraction just proved imply
\[
 \|1_{S_j} f\|_2
   \le (1-\rho)^{-1}\|1_{S_j^+}(I-\mathsf P)f\|_2+\rho^{k_j}\|f\|_2
\]
when \(k=k_j\).
Indeed every path of at most \(k_j\) conjugations ending in \(S_j\) starts within the enlarged shell, so the first term needs only the indicated coefficients.
Apply this with \(f=\widehat K_j\) off the identity.
The discarded identity is fixed by conjugation, and \(\|K_j\|_2\le\sqrt m\) by positivity and the geometric weights.
The signed difference can be computed before the nonlinear first-return recursions: for \(Q_h=h^*Qh\), the difference of the two order-\(l\) powers is
\[
               Q^l-Q_h^l=\sum_{k=0}^{l-1}Q^k(Q-Q_h)Q_h^{l-1-k}.
\]
Average this identity over the four letters, retain the endpoints in \(S_j^+\), and sum over \(l\) with the coefficients of \(K_j\) before taking the norm.

For real \(z=z_j\), the Abel coefficient of the signed first-return array is the real polarization of \(R_z=(1-z)(I-zQ)^{-1}\) divided pointwise by two padded probe factors, each at least \(1/2\).
The polarizations at phases \(1,\mathrm i\) give the squared modulus after summing the two squares on each entry of the selfadjoint matrix.
Moreover \(\|R_z-K_j\|_2\le\sqrt m\,z^{N_j+1}\).
The C76 bound for the time truncation of the signed Abel array on the entire group is at most \(\sqrt{128m}\,z^{N_j+1}/\sqrt{1-z^2}\). [C76, joint square bound](Yin_C_A0076_v1.md#the-joint-square-bound-across-time-and-endpoints)
These observations bound the shell norm of \(B_\bullet\) by four times the above bound for \(K_j\), plus the two time truncation errors with their respective constants.
The maximum square-root weight on the shell is at most \(2^{\beta(j+1)/2}\).
After squaring and summing, the \(\rho^{k_j}\) contribution is bounded by a geometric tail because \(2a\log_2(1/\rho)>\beta\).
The truncation errors give geometric tails by the time and \(L\) chosen in C76.
Finally the signed limiting coefficient differs from the shellwise finite array by the decaying exterior error in [C76, shell comparison](Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell), and bounds the true projection coefficient in square norm by C67.
This proves (2) with \(\eta=\min\{a\log_2(1/\rho)-\beta/2,(\kappa\alpha-\beta)/2\}\) and no factor counting the volume of a shell.
It reduces the remaining estimate to the signed conjugation differences on shells widened by \(O(j)\).

## A finite upper bound from row fits

The constant coefficient matrix is \(T_0=\sum_g\widehat C_0(g)^*\widehat C_0(g)\), so its kernel is precisely \(W\).
Let \(q\) project onto \(\ker C_0\) and \(e_W\) be the constant projection onto \(W\).
Since \(C_0e_W=0\), \(q\ge e_W\).
The invertible map \(S\) sends \(\ker C_0\) onto \(\ker A\), preserving its von Neumann dimension by polar decomposition of the restriction.
Therefore \(q'=q-e_W\) is a projection of trace \(z^2\).
Denote \(D_n=\mathsf P^nT=\mathbb E_h h^*Th\).
The offidentity contraction gives the stated estimate on \(\delta_n\).
Both \(D_n\) and \(T_0\) annihilate \(e_W\), since group translations commute with constant matrices.
For every fit one has
\[
       (C_0 h-X_h C_0)q=C_0 hq,\qquad
       \tau_m(q'D_n)=\mathbb E_h\|C_0 hq\|_2^2\le E^2 .
\]
The bound \(T_0\ge\lambda(I-e_W)\) and trace Cauchy–Schwarz yield
\[
          \lambda z^2\le\tau_m(q'T_0)\le E^2+\delta_n z.
\]
Solving this scalar inequality gives (3).
For a scalar \(C_0=A\ne0\), \(W=0\).
Any nonzero \(s\)-term annihilator has regular range dimension at least \(1/s\) by the coefficient norm bound \(\|b\|_2^2\le\|b\|_1^2\dim_G\overline{\operatorname{ran} b}\), and its range must lie in the kernel.

In the equality case \(z=0\), faithfulness gives \(q=e_W\).
Choose a constant isometry \(V\) onto \(W\), put \(K=SV\), and take the projection to be zero if \(W=0\).
Otherwise the kernel of \(A\) is the range of \(K\) and its projection is \(p_0=K(K^*K)^{-1}K^*\).
Since \(S\) is boundedly invertible, \(K^*K\) has a positive lower bound, and the finite range of its coefficients gives exponentially accurate, linearly propagating Neumann approximations to its inverse. [C58, rational inverse estimate](Yin_C_A0058_v1.md#bounded-rational-inverses-have-exponential-tails)
This proves the stated exponential Fourier tail.
For a single finite fit with \(z\) merely bounded, the same \(p_0\) projects into \(\ker A\).
One has \(\|p_A-p_0\|_2=z\), so outside any ball the unweighted coefficient norm of \(p_A\) is at most the computable upper bound on \(z\) plus the exterior norm of \(p_0\).
Under the C76 time hypothesis this also bounds each individual finite signed shell norm, using four times the corresponding projection shell norm and the C76 shell error.
A single unweighted error independent of radius does not imply a summable weighted exterior.

For fixed \(h\), the infimum of \(\|C_0h-X_h C_0\|_2\) over finite group-ring \(X_h\) is exactly \(\|C_0h q\|_2\).
For the upper bound use \(X_{h,t}=C_0 h(C_0^*C_0+tI)^{-1}C_0^*\).
Then \(X_{h,t}C_0\to C_0h(I-q)\) in trace \(L^2\) as \(t\downarrow0\), and for each fixed \(t\) one can approximate \(X_{h,t}\) in operator norm by finite group-ring matrices.
The preceding projection identity gives the reverse inequality.
Consequently vanishing residuals for some sequence \(n\to\infty\) are equivalent to \(q=e_W\): in that case \(C_0 hq=0\) for every averaging word and the finitely many fits at each \(n\) can be chosen as accurately as desired.
For example this criterion cannot give equality for [C64](Yin_C_A0064_v1.md#the-row-map-and-its-kernel), whose nonzero kernel contains no finitely supported vector.
Indeed an invertible finite group-ring matrix \(S\) would take a nonzero constant kernel coordinate supported at the identity to a nonzero finitely supported vector.
For the trace alone one can instead apply (3) to \(A^*\).
If \(A\) has \(r\) rows then \(\dim_G\ker A=m-r+\dim_G\ker A^*\) by polar decomposition.
In particular the adjoint fits with \(S=I\) can be made arbitrarily small at each \(n\) whenever \(A\) has dense range, even if the kernel of \(A\) lacks finitely supported vectors, as in C64.
Proving this fit convergence gives the nullity \(m-r\); control of the spatial tail of the original projection in that case still requires other information.

## Why operator norm fits fail at nonclosed range

Here use the additional rapid-decay estimate available on the fixed four-line group.
The finite matrix \(D_n-T_0\) has propagation at most \(w_T+bn\), where \(w_T\) is the propagation of \(T\).
By the matrix ball estimate and the conjugation contraction,
\[
      \|D_n-T_0\|\le K_G(1+w_T+bn)^{3/2}\rho^n\|T-T_0\|_2 .
\]
The matrix ball estimate follows from the scalar inequality entry by entry. [C56](Yin_C_A0056_v1.md#argument)
For each sufficiently large fixed \(n\) this upper bound is at most \(\lambda/2\).
Since both matrices annihilate \(e_W\), \(D_n\ge(\lambda/2)(I-e_W)\).
At any such \(n\) even the single finite family of fits gives \(z^2\le 2 E^2/\lambda\).
Formula (3), with \(n\) arbitrary, does not require a specified rapid-decay constant.

If \(A\) has nonclosed range then so does \(C_0\), since \(S\) is onto.
Take unit vectors \(\xi_i\) perpendicular to \(\ker C_0\) with \(\|C_0\xi_i\|\to0\).
The mean squared norm of \(C_0h\xi_i\) is at least \(\lambda/2\) by the preceding lower bound.
For any fixed collection of bounded \(X_h\), one has \(X_h C_0\xi_i\to0\) for all of the finitely many words.
Therefore
\[
       \mathbb E_h\|C_0 h-X_h C_0\|^2\ \ge\ \lambda/2 .
\]
Even when the trace-\(L^2\) residuals at this \(n\) tend to zero, the multipliers in such fits cannot stay uniformly operator-norm bounded.
Otherwise simultaneous weak-operator cluster points would solve all the equations exactly, since bounded matrices with trace-\(L^2\) convergence to zero converge weakly to zero in the regular representation.
This would contradict the operator-norm lower bound just proved.

## Finite fits for a full-group input of nonclosed range

Let \(P\) be the uniform group-ring probability on the identity and a finite symmetric generating set containing \(u,v\).
Put \(a=(8I+P)(1-u)\), \(V=1-v\), and take the row \(A=a(1,V)\).
The row takes values in precisely the range of \(a\), which is nonclosed since \(8I+P\) is invertible and \(1-u\) is the difference of an infinite cyclic shift and the identity.
The coefficients of \(a\) at both \(e\) and \(u\) are nonzero by the dominant term \(8(1-u)\).
If a subgroup carries \(a\), it contains \(u\).
Multiplying on the right by the inverse of \(1-u\) affiliated to that subgroup recovers the bounded operator \(8I+P\), so the subgroup contains the whole generating set. [Affiliated subgroup argument](Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group)
The identity coefficient also makes this full-group support obstruction persist under a left and a right translation of \(a\).

Use \(S=\left(\begin{smallmatrix}1&-V\\0&1\end{smallmatrix}\right)\).
Then \(C_0=(a,0)\) and \(W\) is the second constant coordinate.
For \(N\ge2\) take the finite polynomials
\[
 L_N=\sum_{j=0}^{N-1}(1-j/N)u^j,\quad
 J_k=\tfrac18\sum_{l=0}^{k-1}(-P/8)^l,\quad
 k=\lceil2\log_8(N+1)\rceil,\quad X_h=a hL_N J_k .
\]
The identity \(I-L_N(1-u)=N^{-1}\sum_{j=1}^Nu^j\) has trace-\(L^2\) norm \(N^{-1/2}\).
Also \(\|I-J_k(8I+P)\|\le8^{-k}\) and \(\|L_N\|\le N\).
These finite coefficient products give \(\|C_0h-X_h C_0\|_2\le\|a\|(N^{-1/2}+2N8^{-k})\), uniformly over all words in the fit.
Taking any \(n\) with \(\rho^n\le N^{-1/2}\) proves \(z=O(N^{-1/2})\) in (3) and hence \(z=0\) for this fixed input.
The resulting projection comes from the column \((-V,I)^t\) and has second diagonal entry \((3-v-v^{-1})^{-1}\).
Its Fourier series has positive coefficients on every power of \(v\), by the convergent geometric expansion in \((v+v^{-1})/3\).
Thus the polynomial fits identify an infinitely supported, exponentially localized projection.
The underlying row construction and its graph-kernel mechanism are those of [C57](Yin_C_A0057_v1.md#nonclosed-range-with-exponential-decay-after-canceling-an-injective-factor); here the scalar injective factor uses the full group and the fits and norm obstruction are explicit.

For C76 time decay, \(a a^*\le AA^*\le5 a a^*\).
By polar decomposition the positive spectral measures of \(aa^*\) and \(a^*a\) agree, and \(49(1-u)^*(1-u)\le a^*a\le81(1-u)^*(1-u)\).
Trace comparison of sublevel projections and the cyclic shift distribution give positive spectral mass comparable to \(t^{1/2}\) at zero, for any fixed allowed normalization.
Integration against the powers of \(Q\) then gives C76's return assumption with \(\alpha=1/2\). [Power estimate and trace comparison](Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group)
Consequently its finite signed shell arrays have the decaying exterior bound of C76 from the established exponential projection tail and time error.
For a general input, summable signed insertions in (1), or finite fits giving sufficiently small errors in (3), require their own proof.

## Assessment history

### Decision angular-shells-and-finite-fits

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:46 |
| status | proved |
| reason | Independent review verified the free-orbit norm, widened-shell estimate, finite-fit upper bound, reconstruction and the nonclosed-range limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite conjugation differences and trace certificates on the fixed group, including their assumptions and the separate adjoint trace conclusion. |
| argument | [Proof](#conjugation-on-the-nonidentity-coefficients) | Orbit norm, angular differences, measurable row fits and the example and obstruction at nonclosed range. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0116_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-angular-shells-and-finite-fits)

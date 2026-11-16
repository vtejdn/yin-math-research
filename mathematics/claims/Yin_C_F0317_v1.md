---
author: Yin
---

# Testing the normal converse near a free semicircular pair in operator norm

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Suppose the [universal implication](../tasks/Yin_T_F0011_v1.md#contract) \(\mathsf A\Rightarrow\mathsf S\) fails for finite normal tuples.
For every \(\varepsilon>0\) there is a common finite tracial algebra containing freely independent standard semicirculars \(T_0,T_1\) and a pair of normal operators \(W_0,W_1\) with the following properties.
The normal pair is exchanged by a trace-preserving involution of its generated algebra.
It has full actual starred conjugate variables \(\xi_0,\xi_1\) there and both original right slice costs are infinite; in particular the pair has no bare full-domain dual system.
In the common trace Hilbert space, with the operator norm taken in the same algebra,
\[
     \max_{j=0,1}\big(\|W_j-T_j\|+\|\xi_j-T_j\|_2\big)<\varepsilon .      \tag{1}
\]
The common law \(\mu\) of the \(W_j\) has the form \((1-t)\mu_{\rm sc}+t\mu_{\rm tail}\) with \(0<t<\varepsilon\), where \(\mu_{\rm tail}\) is supported in the \(\varepsilon\)-neighborhood of the right semicircular endpoint \(2\).
The joint probability \(\pi\) defined on rectangles by \(\pi(A\times B)=\tau(1_A(W_0)1_B(W_1))\) may simultaneously be required to satisfy
\[
            \pi=(1-b^2)\mu\otimes\mu+b^2\pi_*,\qquad 0<b^2<\varepsilon,   \tag{2}
\]
where \(\pi_*\) is another probability coupling of \(\mu\) to itself.

Consequently it would suffice to prove \(\mathsf A\Rightarrow\mathsf S\) in any one such neighborhood of the free standard semicircular pair, even with these further restrictions and model-dependent bounds.
The freely independent reference pair in (1) is required only in a tracial extension of the algebra of the normal pair.
The argument leaves existence of a separating pair open.

## Argument

### A freely perturbed projection close in norm to a free symmetry

Let \(J=J^*=J^{-1}\) be a centered symmetry in a tracial base \(R\), and let \(v=v^*\) be free from \(R\) with uniform probability law on \([-2,-1]\cup[1,2]\).
It has a scalar divided-difference vacuum \(g_v\in L^2\): the maximal linear density is bounded and the squared Menger curvature vanishes for this real law. [Scalar vacuum criterion](Yin_C_F0255_v1.md#statement)
Write \(s_0=\operatorname{sgn}v\), a centered symmetry free from \(R\).
For \(0<\lambda<1/2\) put \(Y=v+\lambda J\) and \(s=\operatorname{sgn}Y\).
Both signs are norm functional calculi of the same fixed continuous function equal to the sign outside \((-1/2,1/2)\) on the two spectra.
Thus \(\|s-s_0\|\to0\) as \(\lambda\downarrow0\), uniformly for these identically distributed free inputs, by polynomial approximation.

In \(B=W^*(J)\), the conditional mean of \(s\) is \(bJ\) for a real scalar \(b\), since the joint law of \(v,J\) is invariant under simultaneous negation.
In fact \(0<b\to0\).
Freeness gives \(\tau(Js_0)=0\), so \(b=\tau(Js)\to0\).
Also \(\tau(s_0Y)=\tau(|v|)\) and \(\tau(|Y|)>\tau(s_0Y)\).
For the strict inequality, equality would give
\(\tau(|Y|^{1/2}(1-\operatorname{Re}(s_0s))|Y|^{1/2})=0\).
Positivity, faithfulness and invertibility of \(|Y|\) would imply \(\operatorname{Re}(s_0s)=1\), hence \(s=s_0\).
This would give \([s_0,J]=0\) since \(s_0\) commutes with \(v\) and \(s\) commutes with \(Y\).
The two free centered symmetries have commutator of squared trace Hilbert norm \(2\), by expanding its Hilbert square into the two alternating centered words and the two unit terms.
Finally \(\tau(|Y|)=\tau(sv)+\lambda b\le\tau(|v|)+\lambda b\), proving strict positivity of \(b\).

The [conditional compression estimate](Yin_C_F0313_v1.md#compression-of-a-free-perturbation) holds with \(v\) as the independent factor: its two reduced-word projections in that proof use only freeness of the noise algebra.
For \(\mathbb E_B e=\tau(e)1\) it gives
\[
       \|b^{-1}ese-eJe\|\le 4\sqrt{\tau(e)}/b.                          \tag{3}
\]
Here \(\|s-bJ\|\le2\).
This permits recovering the old symmetry on arbitrarily small corners even for a fixed arbitrarily small \(b>0\).

### A semicircular main summand and summable distinguished vacua

Use the [sign-symmetric finite witnesses](Yin_C_F0311_v1.md#statement).
For each \(n\ge1\) take a model \(R_n=W^*(Z_n,J_n)\) with centered symmetry \(J_n\), \(\|Z_n\|\le1\), actual distinguished vacuum \(\zeta_n\) and a fixed polynomial contraction whose right slice norm exceeds \(4^n\|\zeta_n\|_2\).
Each model has a trace-preserving involution fixing \(Z_n\) and negating \(J_n\).
On the main summand use a standard semicircular \(A\) free from a centered symmetry \(J_0\).
The derivation at \(A\) killing \(J_0\) has vacuum \(A\), by the [semicircular pairing formula](../audits/literature/NS06/Yin_U004.md#ns06-u004) and [free vacuum extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
The sign change on \(J_0\) fixing \(A\) is trace preserving.

Fix a small \(d>0\) and a large \(L>1\).
Give the other summands trace weights \(t_n>0\), of sum \(t<1\), and put
\[
  \alpha_n=L2^n t_n^{3/2}\|\zeta_n\|_2,\qquad
  W_n=2+d2^{-n}+\alpha_n Z_n .
\]
In \(R=\prod_{n\ge0}R_n\) take \(W=A\) on the main summand of weight \(1-t\) and \(W=W_n\) elsewhere, and take \(J=(J_n)_{n\ge0}\).
Choose the \(t_n\) small enough that \(\alpha_n\le d2^{-n}/16\) and the right side of (3) lies below each corresponding [finite-witness perturbation tolerance](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses).
At the same time \(\sum_n4^nt_n\) can be made arbitrarily small, by taking an arbitrarily small summable majorant for \(4^nt_n\).
These upper bounds on positive \(t_n\) impose no conflicting lower bounds.
The bad disks are separated from each other and from \([-2,2]\); each individual disk is also separated in real part.
Their units \(e_n\) are therefore spectral cuts of \(W\), and \(W,J\) generate \(R\).
The symmetry \(J\) has conditional compression weights \(\mathbb E_B e_n=t_n1\) because \(\tau_n(J_n)=0\).

Use the [direct-sum derivative and gap kernel](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing).
Before the correction on mixed coarse summands, its diagonal vacuum is the vector \(\eta\) with main entry \((1-t)A\) and entries \(t_n\zeta_n/\alpha_n\).
The squared norm of the latter entries together equals \(\sum 4^{-n}/L^2\).
For \(d<1\) we have
\[
               \|\eta-W\|_2\le t+3\sqrt t+L^{-1}.
\]
On the distinct coarse summands the inner correction has kernel \(K(z,w)=1/(z-w)\).
Between a bad disk \(n\) and the main spectrum its absolute value is at most \(C2^n/d\), and between two bad disks it is at most \(C2^{\min(n,k)}/d\) with an absolute constant \(C\).
Summing against the block masses gives \(\|K\|_2^2\le C' d^{-2}\sum_n 4^nt_n\).
The corrected derivation \(D_0\) has unit value at \(W\), forced phase at its adjoint, vacuum differing from \(\eta\) in norm by at most \(2\|K\|_2\), and \(\|D_0J\|_2\le2\|K\|_2\).

Extend by zero on the free noise and insert \(-\lambda D_0J\) at \(v\).
The [free extension](Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) preserves the former vacuum, and the [arbitrary base tensor insertion](Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) has vacuum norm at most \(\lambda\|g_v\|_2\|D_0J\|_2\).
Their sum kills \(Y\), so it kills \(s\) on the bounded graph extension by the spectral gap.
Restriction to \(M=W^*(W,s)\) has intrinsic coarse values by the generator values, and projects the ambient vacuum onto \(L^2(M)\). [Graph restriction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator)
Its vacuum \(\xi\) satisfies
\[
        \|\xi-W\|_2\le t+3\sqrt t+L^{-1}
                     +2(1+\lambda\|g_v\|_2)\|K\|_2 .                    \tag{4}
\]
The product sign involution on \(R\) extended by \(v\mapsto-v\) fixes \(W\) and negates \(s\).

Exactly as in the [intrinsic corner comparison](Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign), insert \(e_n\) on both inner legs.
The scaled corner derivative differentiates \(Z_n\) to the unit tensor and kills \(b^{-1}e_nse_n\).
By (3) the original polynomial at this new coefficient has norm at most two and scaled normalized slice norm above \(4^n\|\zeta_n\|_2/2\).
If the target distinguished slice had finite original cost \(a\), its corner bound would imply \(4a\ge t_n^{3/2}4^n\|\zeta_n\|_2/(2\alpha_n)=2^{n-1}/L\) for every \(n\).
Thus the cost is infinite.
The [even-algebra formula](Yin_C_F0311_v1.md#statement) yields the actual pair \(W_0=W,W_1=sWs\), with vacua \(\xi,s\xi s\) and infinite right costs in its generated algebra.
The [normal bare-dual implication](Yin_C_F0070_v1.md#statement) excludes bare duals there.

### Coupling in operator norm and comparing two marginal blocks

Let \(Q\) be the quantile function of the standard semicircular probability on \([-2,2]\), continuously extended to \([0,1]\) with endpoint values \(-2,2\), and let \(G\) be its cumulative distribution function.
Define \(T_0=Q((1-t)G(A))\) on the main summand.
On each other summand take a uniform \([0,1]\) variable \(U_n\) in the diffuse abelian algebra \(W^*(Z_n)\), and take \(T_0=Q(1-t+tU_n)\) there.
Such a variable is obtained from nested dyadic equal-mass partitions of the nonatomic scalar law.
The distribution of the quantile argument in the direct product is exactly uniform on \([0,1]\), by combining the two intervals with weights \(1-t,t\).
Thus \(T_0\in R\) is standard semicircular.
In operator norm,
\[
 \|W-T_0\|\le \max\{\omega_Q(t),\ 2-Q(1-t)+d\} ,                       \tag{5}
\]
where \(\omega_Q\) is the modulus of uniform continuity.
On each bad block this follows by subtracting the scalar \(2\) and using \(\|W_n-2\|\le d\).
Set \(T_1=s_0T_0s_0\).
These two semicirculars are free: in an alternating product of centered terms from \(W^*(T_0)\) and \(s_0W^*(T_0)s_0\), expanding the conjugations gives a reduced free word in \(R\) and the centered symmetry \(s_0\).
It follows that
\[
          \|W_1-T_1\|\le\|W-T_0\|+4\|s-s_0\|,\qquad
          \|\xi_j-T_j\|_2\le\|\xi-W\|_2+\|W_j-T_j\|.
\]

For (2) let \(a=s-bJ\).
The conditional expectation onto \(R\) on \(W^*(J,v)\) is the expectation onto \(B\), as seen by expanding reduced words containing a noise letter.
Hence \(\mathbb E_R a=0\) and \(\mathbb E_R a^2=(1-b^2)1\).
For \(f\in W^*(W)\) one has \(\mathbb E_B f=\tau(f)1\), since the sign involution fixes \(f\).
Consequently \(\mathbb E_R(a(f-\tau f)a)=0\).
For reduced centered-over-\(B\) words in place of each \(a\), the two nearest optional \(B\)-letters multiply \(f-\tau f\) to an \(R\)-factor centered over \(B\), hence centered over the scalars.
The neighboring noise letters remain separated and the resulting reduced word has zero expectation onto \(R\).
Weak density and separate normality in the two words extend the identity to \(a\).
Expanding \(sfs\) now gives \(\mathbb E_R(sfs)=b^2JfJ+(1-b^2)\tau(f)1\).
Pairing with a spectral indicator of \(W\) gives (2) with \(\pi_*\) the two-block law of \(W,JWJ\).
This is a probability coupling by the commuting left and right marginal actions on the trace Hilbert space.

First make \(\lambda\) small enough to control \(\|s-s_0\|\) and \(b^2\).
Next make \(d,L^{-1}\) small, and finally choose the masses so small that (3) meets the witness tolerances, and (4) and (5) give (1).
The bad spectra then lie within the stated neighborhood of \(2\).
Every construction was conditional on failure of the general implication; conversely any resulting deficient pair is itself a counterexample.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:17 |
| status | open |
| reason | Fix the conditional construction near a free semicircular pair, including operator-norm coupling, Hilbert-space vacuum estimates and the independent component of the two-block law. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One actual deficient exchange pair in every stated neighborhood, with trace and spectral constraints. |
| argument | [Argument](#argument) | Sign of gapped free noise, small conditional regression, concentrated weights, intrinsic corner test, quantile coupling and exact marginal-block computation. |
| dependency | [Scalar vacuum criterion](Yin_C_F0255_v1.md#statement) | Actual scalar noise vacuum on a bounded real law with two separated intervals. |
| dependency | [Conditional compression](Yin_C_F0313_v1.md#compression-of-a-free-perturbation) | Reduced-word projection estimate for any free noise factor, as used on its sign. |
| dependency | [Sign and exchange transfer](Yin_C_F0311_v1.md#statement) | Arbitrarily large finite sign-symmetric tests and actual vacua and costs of the even algebra. |
| dependency | [Semicircular moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | The standard semicircular is its own scalar conjugate variable. |
| dependency | [Free vacuum extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Extension of the scalar main-summand derivative killing a free symmetry. |
| dependency | [Finite witnesses](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Stability of represented polynomial and normalized formal derivative in a larger corner. |
| dependency | [Direct-sum derivation](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Trace powers in the diagonal vacuum, mixed gap correction and derivative at the old symmetry. |
| dependency | [Free extension of the base derivative](Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) | Preservation of the base vacuum across an independent noise factor. |
| dependency | [Base tensor insertion](Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Insertion at the independent selfadjoint noise, with vacuum norm controlled by its scalar vacuum. |
| dependency | [Graph restriction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) | Killed spectral cut, intrinsic phase and projection of the vacuum to the generated algebra. |
| dependency | [Intrinsic comparison](Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) | Corner derivative and global bound on the separated cut in the new generated algebra. |
| dependency | [Bare dual obstruction](Yin_C_F0070_v1.md#statement) | Finiteness of the original slice cost under a bare system on a normal pair. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:31 |
| status | proved |
| reason | Adopt the operator-norm semicircular neighborhood reduction and the trace-coupling formula after independent review of the complete conditional construction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One actual deficient exchange pair in every stated neighborhood, with trace and spectral constraints. |
| argument | [Argument](#argument) | Sign of gapped free noise, small conditional regression, concentrated weights, intrinsic corner test, quantile coupling and exact marginal-block computation. |
| dependency | [Scalar vacuum criterion](Yin_C_F0255_v1.md#statement) | Actual scalar noise vacuum on a bounded real law with two separated intervals. |
| dependency | [Conditional compression](Yin_C_F0313_v1.md#compression-of-a-free-perturbation) | Reduced-word projection estimate for any free noise factor, as used on its sign. |
| dependency | [Sign and exchange transfer](Yin_C_F0311_v1.md#statement) | Arbitrarily large finite sign-symmetric tests and actual vacua and costs of the even algebra. |
| dependency | [Semicircular moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | The standard semicircular is its own scalar conjugate variable. |
| dependency | [Free vacuum extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Extension of the scalar main-summand derivative killing a free symmetry. |
| dependency | [Finite witnesses](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Stability of represented polynomial and normalized formal derivative in a larger corner. |
| dependency | [Direct-sum derivation](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Trace powers in the diagonal vacuum, mixed gap correction and derivative at the old symmetry. |
| dependency | [Free extension of the base derivative](Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) | Preservation of the base vacuum across an independent noise factor. |
| dependency | [Base tensor insertion](Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Insertion at the independent selfadjoint noise, with vacuum norm controlled by its scalar vacuum. |
| dependency | [Graph restriction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) | Killed spectral cut, intrinsic phase and projection of the vacuum to the generated algebra. |
| dependency | [Intrinsic comparison](Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) | Corner derivative and global bound on the separated cut in the new generated algebra. |
| dependency | [Bare dual obstruction](Yin_C_F0070_v1.md#statement) | Finiteness of the original slice cost under a bare system on a normal pair. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0325_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

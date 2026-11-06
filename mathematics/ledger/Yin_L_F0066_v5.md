---
author: Yin
---

# Bounded actual minors can retain a conditional singular atom

This ordinary proof-development finding was obtained for Yin on 2026-11-05 during the original-input quadratic investigation for [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract).
It fixes a failed uniform conditional-floor implication, with its complete model, evidence and scope, rather than resolving either unrestricted determinant Task.
It is not an independent review, an adopted Claim or a novelty claim.
The earlier [cofactor and Riccati-fiber](Yin_L_F0066_v1.md), [complex-orientation](Yin_L_F0066_v2.md), [transpose-pair](Yin_L_F0066_v3.md) and [fixed skew-probe](Yin_L_F0066_v4.md) obstructions retain their distinct fixed scopes.
The continuing [typical-minor coefficient test](../drafts/Yin_D_F0010.md#typical-minor-energy-matching) asks for probabilistic control beyond the guards refuted here and is not a logical input to this finding.

<a id="model-and-determinants"></a>
## Fixed two-channel pencil and scalar reduction

Set \(\alpha=\sqrt2\), \(T=\operatorname{diag}(1,\alpha)\) and \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).
For two independent real symmetric Wigner inputs \(A=W_1^{(N)}\), \(B=W_2^{(N)}\), with the fixed laws specified below and the normalization \(N^{-1/2}\), put
\[
 X_N=A+B,\qquad Y_N=A+\alpha B,\qquad
 L_N=J\otimes I_N+I_2\otimes A+T\otimes B
     =\begin{pmatrix}X_N&I_N\\I_N&Y_N\end{pmatrix},
 \qquad Q_N=Y_NX_N-I_N.
 \tag{Fixed-pencil}
\]
The scalar shift is \(K=1\) throughout.
The auxiliary size is two, the coefficient tuple is fixed with dimension, and all coordinate families are independent within each dimension before conditioning.
The calculations below concern one-size marginals and impose no independence between different dimensions.
Both noise coefficients are invertible, so their common left and right kernels vanish, including after fixed invertible changes of coefficient bases.
The distinct diagonal entries of \(T\) generate the diagonal matrix units, and multiplication by \(J\) produces the two off-diagonal matrix units, so the coefficient algebra is \(M_2(\mathbb C)\).
Nevertheless the frame constant
\[
 \chi=\inf_{\|u\|=\|v\|=1}
       \bigl(|u^*I_2v|^2+|u^*Tv|^2\bigr)
\]
is zero by \(u=e_1,v=e_2\), so the additional hypothesis of [C_F0187_v3](../claims/Yin_C_F0187_v3.md#statement) is unavailable.

Let \(P=\begin{pmatrix}0&I_N\\I_N&0\end{pmatrix}\).
Multiplying \(L_NP=\begin{pmatrix}I_N&X_N\\Y_N&I_N\end{pmatrix}\) on the left and right by unitriangular blocks eliminates \(Y_N\) and \(X_N\), leaving \(\operatorname{diag}(I_N,I_N-Y_NX_N)\).
Since \(\det P=(-1)^N\), this proves, without inverting \(X_N\) or \(Y_N\),
\[
 \det L_N=\det(Y_NX_N-I_N)=\det Q_N.
 \tag{Finite-block-determinant}
\]
For free variance-one semicircular \(s_1,s_2\) in a finite von Neumann algebra with faithful normal tracial state \(\tau\), write
\[
 x=s_1+s_2,\qquad y=s_1+\alpha s_2,
 \qquad \ell=\begin{pmatrix}x&1\\1&y\end{pmatrix},
 \qquad \tau_2=\operatorname{tr}_2\otimes\tau.
\]
The same bounded factorization, [ordinary bounded FK multiplicativity](../audits/literature/FK52/Yin_U001.md#fk52-u001), and the determinant-one unitriangular calculation in [C_F0186_v4](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) give
\[
 \log\Delta_{\tau_2}(\ell)=\tfrac12\log\Delta_\tau(yx-1),
 \tag{Free-block-determinant}
\]
including zero determinants and without an affiliated inverse.
Only those accepted bounded determinant interfaces are reused; their original source proofs are not re-audited here.
The free-target regularity proof below separately uses the stated C_F0119_v1 resolvent interface.

<a id="actual-minor-singular-atom"></a>
## Bounded actual minors can leave a conditional singular atom

Unlike the [earlier arbitrary-minor obstruction](../ledger/Yin_L_F0059_v1.md#schur-findings), every conditioned block below is an actual minor of a pencil with fixed admissible entry laws.
The obstruction survives uniformly bounded matrix and inverse norms and a separately established finite free logarithm.
It rules out uniformity over all actual conditioned minors; it does not rule out a bound outside a suitably controlled exceptional set of minors.

Let \(t\in(0,1)\) be the positive solution of
\[
 \alpha t^2+(1+\alpha)t=1.
 \tag{Border-atom}
\]
Let the first raw off-diagonal law be a symmetric sign.
For the second, put equal mass at the two points of each indicated pair, with the following total masses:
\[
 \mathbb P\{\xi_2\in\{-1,1\}\}=\tfrac14,\qquad
 \mathbb P\{\xi_2\in\{-t,t\}\}=\tfrac14,\qquad
 \mathbb P\{\xi_2\in\{-2,2\}\}=\frac{3-t^2}{16},\qquad
 \mathbb P\{\xi_2=0\}=p_0:=\frac{5+t^2}{16}.
 \tag{Fixed-atomic-background}
\]
These are positive probabilities summing to one, and
\[
 \mathbb E\xi_2=0,\qquad
 \mathbb E\xi_2^2=\tfrac14+\tfrac14t^2+4\frac{3-t^2}{16}=1.
\]
Both diagonal laws are identically zero.
Thus the two independent inputs satisfy the original fixed-law model, with bounded support; no distribution or coefficient varies with the dimension.

Fix \(N\ge2\), write \(n=N-1\), and choose any real symmetric \(n\)-by-\(n\) matrix \(C\) with zero diagonal and every strict upper entry in \(\{-1,1\}/\sqrt N\).
Expose the first physical row and column of \(A:=W_1\), and condition on the following event \(E_N(C)\), measurable in the whole independent input \(B:=W_2\) and the remaining principal minor of \(A\):
\[
 A=\begin{pmatrix}0&x^T\\x&C\end{pmatrix},\qquad
 B=\begin{pmatrix}0&b^T\\b&-C\end{pmatrix},\qquad
 b=\frac{t}{\sqrt N}e_1.
 \tag{Actual-conditioned-blocks}
\]
The condition fixes \(C\) and \(B\), but leaves \(x=(\varepsilon_1,\ldots,\varepsilon_n)^T/\sqrt N\) with independent symmetric signs.
Every specified atom has positive probability under the one fixed pair of laws.
In particular,
\[
 \mathbb P(E_N(C))
 =16^{-n(n-1)/2}\,\frac18\,p_0^{n-1}>0.
 \tag{Actual-atom-probability}
\]
The power of sixteen combines the probability \(1/2\) of each prescribed first-input minor sign with the probability \(1/8\) of its prescribed opposite second-input sign.

Put \(u=x+b\), \(v=x+\alpha b\), and \(D=(1-\alpha)C\).
Then
\[
 X=A+B=\begin{pmatrix}0&u^T\\u&0\end{pmatrix},\qquad
 Y=A+\alpha B=\begin{pmatrix}0&v^T\\v&D\end{pmatrix},\qquad
 YX-I_N=
 \begin{pmatrix}v^Tu-1&0\\Du&vu^T-I_n\end{pmatrix}.
\]
The rank-one determinant identity, or a basis beginning with \(v\) when \(v\ne0\), gives
\[
 \det(YX-I_N)=(-1)^N(v^Tu-1)^2.
 \tag{Actual-square-determinant}
\]
The same formula holds for \(v=0\) directly.
Here
\[
 v^Tu
 =\frac{N-1+(1+\alpha)t\varepsilon_1+\alpha t^2}{N}
 =\begin{cases}
 1,&\varepsilon_1=1,\\
 1-2(1+\alpha)t/N,&\varepsilon_1=-1.
 \end{cases}
\]
Consequently the original pencil and its scalar quadratic reduction satisfy
\[
 \mathbb P\{s_{\min}(L_N)=0\mid E_N(C)\}
 =\mathbb P\{s_{\min}(Q_N)=0\mid E_N(C)\}
 =\tfrac12.
 \tag{Actual-conditional-atom}
\]
This is an exact conditional probability, not just the possibility of a zero for one exposed row.
The surviving original row is still fully independent; the failure is therefore different from conditioning away all randomness in a mixed factor.

Deleting the first physical block from \(L_N\) gives the actual conditioned minor
\[
 \mathcal M_N=\begin{pmatrix}0&I_n\\I_n&D\end{pmatrix},\qquad
 \mathcal M_N^{-1}=\begin{pmatrix}-D&I_n\\I_n&0\end{pmatrix}.
 \tag{Actual-minor-inverse}
\]
In particular the minor is always invertible, with
\(\max\{\|\mathcal M_N\|,\|\mathcal M_N^{-1}\|\}\le1+\|D\|\).
To obtain dimension-independent guards along an infinite even subsequence, take \(N=2^k\), index the rows and columns of \(H_N\) by binary vectors \(a,b\in\{0,1\}^k\), and set
\[
 (H_N)_{ab}=(-1)^{a\cdot b}.
\]
The direct sum
\(\sum_b(-1)^{(a-a')\cdot b}=N\mathbf1_{a=a'}\)
shows that \(H_N\) is real symmetric and \(\|H_N\|=\sqrt N\).
Take any principal \(n\)-by-\(n\) submatrix, subtract its diagonal, and divide by \(\sqrt N\) to define \(C\).
Then \(C\) has precisely the required signs and
\[
 \|C\|\le1+N^{-1/2},\qquad
 \|B\|\le\|C\|+tN^{-1/2},\qquad
 \|A\|\le\|C\|+\sqrt{(N-1)/N}.
\]
These bounds and (Actual-minor-inverse) are uniform in every remaining exposed sign vector.
Thus even restricting to bounded actual minors, bounded actual inverses, bounded independent backgrounds and bounded full input matrices cannot make (Actual-conditional-atom) tend to zero.
For completeness, the physical border has the two-by-two corner \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) and off-diagonal block \(R=\operatorname{diag}(u^T,v^T)\).
Its exact Schur complement is
\[
 J-R\mathcal M_N^{-1}R^T
 =\begin{pmatrix}u^TDu&1-u^Tv\\1-u^Tv&0\end{pmatrix}.
\]
It is singular precisely when \(u^Tv=1\).
The same event makes the actual normalized physical-block distance singular, since graph normalization multiplies this Schur complement by invertible factors.

<a id="identity-direction-free-density"></a>
## A free-density certificate for the same obstruction

The finite free target in this example follows from a short consequence of the accepted [operator-valued Cauchy identity](../claims/Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness), specifically its equations (6)--(7) and retained MS17 cumulant interface.
Only that established semicircular resolvent identity is reused; no finite-size random-matrix conclusion or new source-proof inspection is inferred.
Its displayed noncrossing-pairing recursion uses selfadjoint coefficients and their covariance map; substituting the selfadjoint coefficients \(I_2,T\) and the drift below gives the same identity directly, without a requirement that these matrices have the source application's Hermitization block form.
Let
\[
 \ell=\begin{pmatrix}0&1\\1&0\end{pmatrix}\otimes1
        +I_2\otimes s_1+\operatorname{diag}(1,\alpha)\otimes s_2,
 \quad T:=\operatorname{diag}(1,\alpha),
 \quad G(z):=(\operatorname{id}_2\otimes\tau)((z-\ell)^{-1}).
\]
For \(z=u+iy\) with \(y>0\), put \(V=-\operatorname{Im}G(z)>0\).
The strict positivity follows from boundedness of \(\ell\) and the resolvent identity, exactly as at the cited interface.
Its covariance map is \(\eta(H)=H+THT\), so
\[
 G^{-1}=zI_2-\begin{pmatrix}0&1\\1&0\end{pmatrix}-G-TGT,
 \qquad
 V=G^*(yI_2+V+TVT)G\ge G^*VG.
\]
Therefore \(V^{1/2}GV^{-1/2}\) is a contraction.
Every eigenvalue of \(G\) has modulus at most one, and consequently
\[
 0<-\operatorname{Im}\operatorname{tr}_2G(z)
 \le|\operatorname{tr}_2G(z)|\le1.
 \tag{Free-Poisson-bound}
\]
If \(\mu_\ell\) is the scalar spectral law under \(\operatorname{tr}_2\otimes\tau\), integrating its Poisson transform over a finite interval and sending \(y\downarrow0\) gives
\(\mu_\ell((a,b))\le(b-a)/\pi\).
Indeed the integral kernel has limit \(\pi\) at each interior point, and Fatou applies to its nonnegative integral; the preceding bound controls that integral by \(b-a\).
Thus \(\mu_\ell\) has a density bounded by \(1/\pi\), and
\[
 \int_{|r|<1}-\log|r|\,d\mu_\ell(r)
 \le\frac2\pi\int_0^1-\log r\,dr=\frac2\pi.
\]
The positive logarithm is bounded because \(\ell\) is bounded.
Hence \(\log\Delta_{\operatorname{tr}_2\otimes\tau}(\ell)\) is finite, at the same \(K=1\) and coefficients as the conditional singular-atom construction.
This is a free-target regularity certificate; it gives no finite-size bottom-logarithm estimate.
The bounded block factorization in (Free-block-determinant) also makes the free logarithm of the scalar quadratic reduction finite.

<a id="actual-minor-allocation-boundary"></a>
## Consequence for the original-input route

For these one-time fixed coefficients and laws, there is no bound of the form
\[
 \sup_{\text{all admitted actual conditioning atoms}}
 \mathbb P\{s_{\min}(L_N)\le N^{-a}\mid B,A^{(1)}\}
 \le r_N,\qquad r_N\longrightarrow0,
\]
for any fixed \(a>0\), even after imposing the uniform norm and inverse guards just proved and even through the subsequence \(N=2^k\).
The displayed conditional probability is interpreted on the atom fixing the indicated values of \(B\) and the first-input minor \(A^{(1)}\).
The corresponding assertion for the scalar quadratic \(Q_N\) fails for the same reason.
This is stronger than failure of a uniform estimate over unrelated minors, and stronger than the projected-Gram failure in [C_F0187_v3](../claims/Yin_C_F0187_v3.md#actual-projected-block-failure): the present full pencil is actually singular on half of the fresh rows while the retained minor and inverse are well conditioned.

The conditioning atoms in (Actual-atom-probability) are exponentially rare in \(N^2\); their probabilities are summable and far smaller than every fixed inverse power.
Their existence therefore neither contradicts an unconditional polynomial floor with vanishing or summable failure nor supplies a counterexample to F0013 or F0014 under any cross-size coupling.
It instead identifies an indispensable new obligation: a successful original-input proof must control the probability of bad actual minors or retain further independent coordinates when conditioning.
It cannot obtain the needed estimate merely from actual-minor membership, bounded norm, bounded inverse, zero common noise kernels, full coefficient algebra and a finite free logarithm.
The useful next test is a probabilistic bound on the conditional singularity profile over the independent background and the first-input minor, with its exceptional set accounted for before row small-ball estimates are integrated.
The necessary middle-range or bottom-logarithm control remains separate from that floor question.

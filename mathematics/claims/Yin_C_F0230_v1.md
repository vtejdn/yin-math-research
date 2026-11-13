---
author: Yin
---
# Four-point geometry and strict polar phase loss for shifts of a normal coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=X_i\) be a coordinate of a finite bounded normal generating tuple with actual ACSY in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, and set \(N=W^*(X_j:j\ne i)\).
For \(b\in N\) set \(T=X-b=UP\), \(P=|T|\), and let \(\xi=\delta_i^*(1\otimes1)\).
By the [shifted singular-law theorem](Yin_C_F0229_v1.md#statement), \(U\) is unitary and the law \(\mu_P\) has no mass at zero.
Use \(\mathcal B=M\bar\otimes M^{\rm op}\) with product trace \(\tau_{\mathcal B}\).
Let \(k\in W^*(X)\bar\otimes W^*(X)^{\rm op}\) denote the unitary with symbol \(k(z,w)=(\bar z-\bar w)/(z-w)\) off the product-null diagonal of the diffuse trace law \(\mu_X\).
Put \(L=(1\otimes U^{\rm op})k(U\otimes1)\) and let \(m(v,w)\) be its conditional expectation onto the product spectral algebra of \(P\).
The full defect is
\[
    I_b=\iint\frac{1-\operatorname{Re}m(v,w)}{v+w}\,d\mu_P(v)d\mu_P(w)
            \le\|\xi\|_2 .
\]

1. For every nonzero bounded positive \(e=g(P)\) put \(f=UeU^*\), \(t=\tau(e)\), and \(\nu_j(B)=t^{-1}\tau(j1_B(X))\) for \(j=e,f\).
   Draw \(z_1,z_2\) independently from \(\nu_f\) and \(w_1,w_2\) independently from \(\nu_e\), with independent pairs.
   All four points are almost surely distinct.
   Put
   \[
     Q=\frac{(z_1-w_1)(z_2-w_2)}{(z_1-w_2)(z_2-w_1)},\qquad
     \Delta(e)=\mathbb E\sin^2(\arg Q),\qquad
     d(e)=\frac1{t^2}\iint g(v)g(w)(1-\operatorname{Re}m(v,w))\,d\mu_P(v)d\mu_P(w).
   \]
   Then \(\Delta(e)\le 2d(e)\), and
   \[
      \int_0^\infty \tau(e^{-sP})^2\Delta(e^{-sP})\,ds\le2I_b .
   \]
   If \(e=1_{[0,r]}(P)\) has positive trace and \(r>0\), then \(t^2\Delta(e)\le4r I_b\).
2. For every such weight, \(\Delta(e)=0\) if and only if a single generalized circle \(C\) carries both \(\nu_f\) and \(\nu_e\), where a generalized circle is a circle of positive radius or a straight line.
   In this case \(\operatorname{supp}(e),\operatorname{supp}(f)\le1_C(X)\), with supports taken as projections in \(M\).
   In particular this conclusion holds when \(d(e)=0\).
   If \(0<\eta\le1\) and every generalized circle has \(\mu_X\)-mass strictly less than \(\eta\), then \(\Delta(e)\) has a strictly positive lower bound for all shifts \(b\) and weights \(0\le e\le1\) with \(t\ge\eta\).
   If every straight line has \(\mu_X\)-mass strictly less than \(\eta\), then for each finite \(B\ge0\) the phase loss \(d(e)\) has a strictly positive lower bound over the same weights and \(\|b\|\le B\).
3. The full defect vanishes if and only if \(\mu_X\) is carried by a line with unit direction \(d\) and the actual polar unitary of \(X-b\) equals \(d1\) or \(-d1\).
   Some scalar shift attains zero whenever the marginal is carried by a line.
   If \(\mu_X\) is carried by no line, then for every finite \(B\ge0\)
   \[
                      \inf_{b\in N,\ \|b\|\le B} I_b>0 .
   \]
   When \(\mu_X\) is carried by no generalized circle, a lower bound is \(\Delta(1)/(4(\|X\|+B))\), where \(\Delta(1)\) uses four independent samples from \(\mu_X\).
   For every marginal the infimum over all scalar shifts is zero.

The behavior of \(d(e)\) on weights of vanishing trace remains relevant to the normal-tuple column obstruction.

## Argument

### Compression by the polar unitary and four-point minors

The two measures are probabilities, since \(\tau(f)=\tau(e)\), and are diffuse since each is dominated by \((\|e\|/t)\mu_X\).
Thus independence gives the asserted distinctness.
Let \(K:L^2(\nu_e)\to L^2(\nu_f)\) be the linear integral operator with kernel \(k(z,w)\).
It has Hilbert–Schmidt norm one because the two measures have mass one and its symbol has modulus one almost everywhere.
Let \(C_e=e^{1/2}\otimes(e^{1/2})^{\rm op}\).
Trace preservation and traciality give
\[
     1-d(e)=t^{-2}\operatorname{Re}\langle C_e,L C_e\rangle_{L^2(\mathcal B)} .
\]
Multiply both vectors on the left by \(1\otimes(U^*)^{\rm op}\).
Reversed multiplication in the opposite leg changes the inner product into
\[
 \langle b_1\otimes b_2^{\rm op},\ k(a_1\otimes a_2^{\rm op})\rangle,\qquad
 a_1=Ue^{1/2},\quad a_2=e^{1/2},\quad b_1=e^{1/2},\quad b_2=e^{1/2}U^* .
\]
Here each of the four leg vectors has \(L^2\)-norm \(\sqrt t\).
On the first leg \(\varphi\mapsto\varphi(X)a_1/\sqrt t\) is isometric from \(L^2(\nu_f)\), since \(a_1a_1^*=f\).
On the second leg \(\psi\mapsto(a_2\psi(X))^{\rm op}/\sqrt t\) is isometric from \(L^2(\nu_e)\), since \(a_2^*a_2=e\).
Testing these two isometries against \(b_1/\sqrt t\) and \(b_2^{\rm op}/\sqrt t\), respectively, gives Riesz representatives of norm at most one in the two scalar spaces.
For a rectangular simple multiplier the normalized inner product is exactly its kernel pairing against these representatives, with complex conjugation of the input representative if needed in the linear operator convention.
The identity extends to \(k\) by rectangular simple approximation in \(L^2(\nu_f\otimes\nu_e)\), which is precisely the weighted norm on the input tensor.
Consequently \(1-d(e)\le\|K\|\).

Write \(k_{ij}=k(z_i,w_j)\).
The two terms of its two-by-two determinant have modulus one and their ratio is \(\bar Q/Q\).
Expanding the square, the expectation of the cross term is the squared Hilbert–Schmidt norm of \(K^*K\), by integrating in the two independent \(z\)'s and then in the two independent \(w\)'s.
Therefore
\[
     4\Delta(e)=\mathbb E|k_{11}k_{22}-k_{12}k_{21}|^2
            =2\left(1-\operatorname{Tr}((K^*K)^2)\right).
\]
With \(s_0=\|K\|\le1\), we have \(\operatorname{Tr}((K^*K)^2)\ge s_0^4\) and \(1-s_0\le d(e)\).
The inequality \(1-s_0^4\le4(1-s_0)\) proves the first estimate.

Take \(e=e^{-sP}\) and use \(\int_0^\infty e^{-s(v+w)}ds=1/(v+w)\) for \(\mu_P^2\)-almost every \((v,w)\).
Since \(1-\operatorname{Re}m\ge0\), Tonelli gives the integrated estimate.
Its left integrand is measurable: norm continuity of \(e^{-sP}\) on bounded \(s\)-intervals gives total-variation continuity of each normalized weighted marginal, and the four-point test is bounded Borel with arbitrary values on coincidences.
Taking \(e=1_{[0,r]}(P)\) instead, \(v+w\le2r\) throughout the spectral square, except for the irrelevant zero denominator at the origin.
This gives \(t^2 d(e)\le 2r I_b\) and the asserted radius bound.

### The carrier when the angular loss vanishes

The cross ratio of four distinct finite points is real precisely when they lie on a generalized circle, as follows by sending three of the points to \(0,1,\infty\) by a Möbius map.
For three distinct points the generalized circle through them is unique, including the collinear case.
If \(\Delta(e)=0\), Fubini gives a typical triple \(z_1,z_2,w_1\) such that its generalized circle \(C\) carries \(\nu_e\).
For almost every other triple the same holds, and its circle must be \(C\), since two distinct generalized circles meet in at most two points and \(\nu_e\) is diffuse.
Thus \(\nu_f\) is carried by \(C\) as well.
The converse follows from the real cross ratio.
If \(\nu_e(C^c)=0\) then \(\|1_{C^c}(X)e^{1/2}\|_2^2=\tau(e1_{C^c}(X))=0\), so the support projection of \(e\) is at most \(1_C(X)\).
The same reasoning applies to \(f\).
This proves the claimed spectral localization, including projection weights.

### Weights with a common positive lower trace bound

For contractions with \(t\ge\eta\), the measures \(\nu_e,\nu_f\) are dominated by \(\mu_X/\eta\).
This is a weakly compact class of probabilities on the compact spectrum, since nonnegative continuous test functions preserve the domination at every subsequential weak limit.
The four-point integral of \(\sin^2(\arg Q)\) is continuous on pairs from this class.
Indeed their product probabilities converge weakly, as one sees by uniformly approximating continuous functions by sums of products, and the bounded four-point integrand is continuous off coincidences.
Those coincidences have zero mass under every limiting product because the limiting marginals are diffuse.
Equivalently one can cut off a closed neighborhood of the coincident points whose mass tends to zero under the dominating product measure.
The argument above for a real cross ratio used only independence and diffuseness, so it applies to any two such limiting probabilities.
If a sequence has \(\Delta(e_n)\to0\), a subsequence of its two weights has limiting laws carried by a common generalized circle \(C\), necessarily with \(\mu_X(C)\ge\eta\).
This proves the uniform angle assertion.

Now suppose \(\|b_n\|\le B\), \(t_n=\tau(e_n)\ge\eta\), and \(d(e_n)\to0\).
Use the preceding subsequence, since \(\Delta(e_n)\le2d(e_n)\), and write \(X-b_n=U_nP_n\), \(f_n=U_ne_nU_n^*\).
We show that the common carrier cannot be a circle of center \(c\) and radius \(\rho>0\).
Let \(W\) be the unitary phase of \(X-c\), defining its phase symbol to be one at \(c\), a \(\mu_X\)-null singleton.
Integration against the weights then gives
\[
  \|(|X-c|-\rho)e_n^{1/2}\|_2\longrightarrow0,\qquad
  \left\| k(z,w)+\overline{W(z)W(w)}\right\|_{L^2(\nu_{f_n}\otimes\nu_{e_n})}\longrightarrow0 .
\]
The squared first test is continuous on the spectrum.
The second squared test is bounded, continuous off the diagonal and the two exceptional slices at \(c\), and zero for distinct points of the limiting circle.
All these exceptional sets are null for the limiting product, so the same cutoff argument applies.
In the preceding two-leg pairing for \(1-d(e_n)\) the normalized input tensor sees precisely this product measure.
Replacing \(k\) there by \(-W^*\otimes(W^*)^{\rm op}\) incurs an error tending to zero by Cauchy–Schwarz, since the normalized output test vector has norm one.
Thus, with \(h_n=\tau(e_n W^*U_n)/t_n\),
\[
       d(e_n)=1+\operatorname{Re}(h_n^2)+o(1),\qquad |h_n|\le1 .
\]
For a sign \(\sigma_n\) agreeing with \(\operatorname{Im} h_n\) this gives
\[
     t_n^{-1}\|(U_n-\sigma_n iW)e_n^{1/2}\|_2^2
            =2-2|\operatorname{Im} h_n|\longrightarrow0 .
\]
Pass to a subsequence with a fixed sign \(\sigma\).
Put \(A_n=b_n-c\in N\), and write \(D_n\simeq F_n\) in this paragraph for \(\|(D_n-F_n)e_n^{1/2}\|_2\to0\).
This convergence is preserved by uniformly bounded left multipliers and by uniformly bounded right multipliers commuting with \(e_n\).
From \(X-c=W|X-c|\), \(U_n\simeq\sigma iW\) and \(U_n^*W\simeq-\sigma i\,1\) it follows that
\[
   A_n=X-c-U_nP_n\simeq W(\rho-\sigma iP_n),\qquad
   A_n^*W=|X-c|-P_nU_n^*W\simeq\rho+\sigma iP_n .
\]
Here \(P_n\) commutes with \(e_n\) and \(\|P_n\|\le\|X\|+B\).
Multiplying the first relation on the left by \(A_n^*\) and the second on the right by \(\rho-\sigma iP_n\) gives \(H_n=A_n^*A_n\simeq S_n=\rho^2+P_n^2\).
For a polynomial \(p\) the telescoping identity gives \(p(H_n)\simeq p(S_n)\), since powers of \(S_n\) commute with \(e_n\) and both sequences are bounded in operator norm.
Uniform polynomial approximation on their common compact spectral interval gives the same for the continuous function \(h(s)=(\rho-\sigma i\sqrt{(s-\rho^2)_+})^{-1}\).
Consequently
\[
    C_n=A_n h(H_n)\in N,\qquad C_n\simeq A_n h(S_n)\simeq W .
\]
The last step uses \(h(S_n)=(\rho-\sigma iP_n)^{-1}\), which commutes with \(e_n\) and has norm at most \(1/\rho\).
It follows that \(D_n=X-c-\rho C_n\simeq0\).
For every \(r>0\), the contraction bound on \(e_n\) and the spectral inequality \(|D_n|^2\ge r^2 1_{(r,\infty)}(|D_n|)\) give
\[
  \eta\le\tau(e_n)\le\tau(1_{[0,r]}(|D_n|))
           + r^{-2}\|D_ne_n^{1/2}\|_2^2
       \le \sqrt{\pi r\|\xi\|_2}+r^{-2}\|D_ne_n^{1/2}\|_2^2 .
\]
The final inequality uses the [shifted singular-law bound](Yin_C_F0229_v1.md#statement) with the omitted shift \(c+\rho C_n\).
First taking \(n\to\infty\) and then \(r\downarrow0\) contradicts \(\eta>0\).
The common carrier must therefore be a straight line of \(\mu_X\)-mass at least \(\eta\), proving the asserted lower bound on \(d(e)\).

### The global equality case and bounded shifts

Since \(P\) has zero kernel and \(1-\mathrm{Re}\,m\ge0\), \(I_b=0\) is equivalent to \(d(1)=0\).
The unitary \(L\) satisfies \(\|L-1\|_{2,\mathcal B}^2=2d(1)\).
Thus global equality is equivalent to \(k=U^*\otimes(U^*)^{\rm op}\).
By the preceding geometric argument at \(e=1\), the diffuse law \(\mu_X\) must then be carried by a generalized circle.
If it is a line with unit direction \(d\), its phase is the constant \(\bar d^{\,2}\).
The tensor equality forces \(U^*\) to be scalar, by applying a normal functional on the opposite factor nonzero at \((U^*)^{\rm op}\).
Thus \(U=\pm d\,1\), and either choice gives the tensor equality and \(I_b=0\).
For a line with offset \(c_0\) write \(X=c_0+dA\), \(A=A^*\), and choose \(b=c_0+d\gamma\) with real \(\gamma<\min\sigma(A)\) to realize \(U=d1\).

For bounded shifts fix \(B\ge0\) and put \(R=\|X\|+B>0\).
For \(\|b\|\le B\), \(P\le R\), whence \(2R I_b\ge d(1)\ge\Delta(1)/2\).
This gives the strictly positive quantitative bound whenever no generalized circle carries \(\mu_X\).

When no line carries \(\mu_X\), apply the macroscopic phase-loss bound with \(\eta=1\) and \(e=1\).
Its strictly positive lower bound for \(d(1)\) on this shift ball also bounds \(2R I_b\) below, completing the equality and bounded-shift conclusions in the remaining circular case.
For scalar \(b=s1\) with \(s>\|X\|\), we instead have \(P\ge(s-\|X\|)1\).
Since \(1-\operatorname{Re}m\le2\), this implies \(I_b\le(s-\|X\|)^{-1}\), proving the infimum over all scalar shifts.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:57 |
| status | open |
| reason | The angular and integrated bounds, the carriers and uniform phase-loss estimates for weights of positive lower trace, and the global equality cases are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Weighted four-point and integrated estimates, marginal carriers for local equality, uniform angle and phase gaps at a positive lower trace, global equality and scalar-shift behavior. |
| argument | [Argument](#argument) | Opposite-leg traces, weighted isometries, Hilbert–Schmidt minors, generalized-circle selection and weighted polynomial approximation excluding a circular limit on a positive-trace corner. |
| dependency | [Shifted singular-law identity](Yin_C_F0229_v1.md#statement) | Equations (1) and (2), giving unitary polar decomposition, the phase conditional expectation, the vacuum bound on the full defect, and the singular mass estimate for the newly reconstructed omitted shift. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Item 1, diffuse trace marginal and a.e. unimodular divided difference on its square. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:01 |
| status | proved |
| reason | Independent review verifies the two weighted spectral laws, the four-point constants and the reconstruction of an omitted shift that excludes a circular limit on any corner of uniformly positive trace. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Weighted four-point and integrated estimates, marginal carriers for local equality, uniform angle and phase gaps at a positive lower trace, global equality and scalar-shift behavior. |
| argument | [Argument](#argument) | Opposite-leg traces, weighted isometries, Hilbert–Schmidt minors, generalized-circle selection and weighted polynomial approximation excluding a circular limit on a positive-trace corner. |
| dependency | [Shifted singular-law identity](Yin_C_F0229_v1.md#statement) | Equations (1) and (2), giving unitary polar decomposition, the phase conditional expectation, the vacuum bound on the full defect, and the singular mass estimate for the newly reconstructed omitted shift. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Item 1, diffuse trace marginal and a.e. unimodular divided difference on its square. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0239_v1.md#whole-proof-finding) | All three conclusions, the exact equality case, the lower bounds for bounded shifts and the scalar-shift limit. |

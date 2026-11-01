---
author: Yin
---
# Dense-core dual systems: atomic counterexamples

User-directed preparation, 2026-10-14T12:00.
The user authorized completing, checking and fixing the counterexample and its mathematical materials.
This bounded follow-up does not reopen the completed T_F0001 contract.

The authoring agent completed the direct proofs; root fixed this candidate for a separately organized whole-argument review.
The selected decision below owns its assessment.

## Current assessment
[Selected decision](#decision-initial)

## Statement

### 1. Question, conventions and exact conclusions

Let \(M\) be a finite von Neumann algebra with faithful normal tracial state \(\tau\), \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P_\Omega f=\tau(f)\Omega\).
Write \([S,T]=ST-TS\), and use Hilbert inner products linear in the second variable.

The full-domain hypothesis considered here is the existence of complex-linear maps \(D_i:M\Omega\to H\) satisfying \([X_j,D_i]=\delta_{ij}P_\Omega\) on all \(M\Omega\).
It imposes no normality, closability or adjoint-domain assumption.
It implies maximal Delta by the [argument in C_F0024 Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors).

The two constructions below establish different boundaries.

1. There is a bounded selfadjoint generator \(X\) with a dense invariant polynomial domain \(\mathcal A\Omega\), and a linear map \(D:\mathcal A\Omega\to H\) such that \(D\Omega=0\) and \([X,D]=P_\Omega\), but \(\Delta(X)<1\).
   This \(D\) is not closable and \(\Omega\notin\operatorname{Dom}D^*\).
2. There is a bounded normal generator \(X\), with dense starred polynomial algebra \(\mathcal A=\mathbb C[X,X^*]\), and a linear map \(D:\mathcal A\Omega\to H\) such that
   \[
   D\Omega=0,\qquad [X,D]=P_\Omega,\qquad
   \Omega\in\operatorname{Dom}D^*,\qquad D\ \text{is closable},
   \tag{1.1}
   \]
   while \(\Delta(X)<1\).
   The closure still satisfies the dual relation on its invariant domain, but this domain excludes a specified bounded vector \(e\Omega\).
   No choice of a different full-\(M\Omega\) dual is possible for this \(X\).

Only the relation with \(X\) is prescribed in (1.1).
A bounded extension of \([X^*,D]\) is not assumed or obtained.

Thus even the simultaneous starred-polynomial-domain, normalization, vacuum-adjoint and closability conditions do not imply the full-domain hypothesis or its maximal-\(\Delta\) conclusion for normal generators.
This addresses the small-domain-to-full-domain direction.
It does not refute any converse starting from an actual full-domain dual.

## Argument

## 2. Reused inputs and distinctions from existing examples

The [disk-Cauchy calculation in C_F0003](Yin_C_F0003_v1.md#counterexample-normal-multiplication-on-the-disk) already proves the row/column integral bounds and the value of the transform on antiholomorphic monomials.
Its source relationship is fixed in [Xia23-U001](../audits/literature/Xia23/Yin_U001.md#xia23-u001).
The present \(C\) is the negative of the operator denoted \(D\) there.
The needed norm and vacuum calculations are reproduced below to keep the new normalization inspectable; no trace-class theorem is used.

[MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002), Section “Setting, Delta, and the Three Conditions”, supplies the accepted characterization
\[
\Delta(X)=1
\quad\Longleftrightarrow\quad
\{T\in\mathcal F(H):[T,X]=0\}=\{0\}.
\tag{2.1}
\]
It applies to bounded \(X\) without selfadjointness.
Its left/right conversion and finite-rank scope are retained there.
We use (2.1) only to show nonmaximality, not to calculate the exact value of \(\Delta\).

[C_F0036](Yin_C_F0036_v1.md#yin_c_f0036-p1) has an atomic obstruction on a nondense test module.
The domain in Section 3 below is dense, so that earlier example does not settle this question.
[C_F0026](Yin_C_F0026_v1.md#small-core-domain-obstruction) is a diffuse weighted-disk example concerning arbitrary bounded denominator domains.
It has no atomic finite-rank cycle and does not supply Section 4.

The source input for the elementary distribution identity used in Section 4.3 is identified in Section 6.
Standard polynomial approximation and the criterion that a densely defined operator is closable exactly when its adjoint is densely defined are used at their usual Hilbert-space scope; the latter is already recorded in [Bla06-U001](../audits/literature/Bla06/Yin_U001.md#bla06-u001).

## 3. Selfadjoint boundary: a dense algebraic dual need not be closable

### 3.1 The represented polynomial algebra

Put
\[
K=\{0\}\cup[1,2],\qquad
\mu=\tfrac12\delta_0+\tfrac12\,1_{[1,2]}(t)\,dt,\qquad
M=L^\infty(K,\mu),\quad X(t)=t.
\]
The interval measure has mass one.
Thus \(\mu\) is a probability measure and
\[
H=\mathbb C\oplus L^2([1,2],dt),\qquad
\|(a,f)\|_H^2=\tfrac12|a|^2+\tfrac12\|f\|_2^2,\qquad
\Omega=(1,1).
\]
The coordinate \(X=(0,t)\) is bounded and selfadjoint, and generates \(M\).

Let \(\mathcal A=\mathbb C[X]\).
A polynomial zero as a represented element vanishes almost everywhere on \([1,2]\), hence is the zero polynomial.
Evaluation is therefore injective.
Polynomial approximation on \([0,2]\), after extending a continuous function on \(K\) across the gap \((0,1)\), shows that \(\mathcal A\) is uniformly dense in \(C(K)\).
Consequently \(\mathcal A\Omega\) is dense in \(H\).
It contains \(\Omega\) and is invariant under \(X\).

For a polynomial \(p\), define its polynomial divided difference by
\[
Q_p(x,y)=
\begin{cases}
\dfrac{p(x)-p(y)}{x-y},&x\ne y,\\[4pt]
p'(x),&x=y.
\end{cases}
\]
This is an actual polynomial in the two variables.
Define
\[
(Dp)(x)=-\int_K Q_p(x,y)\,d\mu(y),
\qquad \operatorname{Dom}D=\mathcal A\Omega.
\tag{3.1}
\]
The right side is a polynomial in \(x\), hence is bounded and in \(H\); uniqueness of the represented polynomial makes \(D\) well-defined.

### 3.2 Normalization and the dual relation

Clearly \(D1=0\).
The polynomial identity
\[
Q_{tp}(x,y)=xQ_p(x,y)+p(y)
\]
gives
\[
D(Xp)=X(Dp)-\tau(p)\Omega,
\qquad [X,D]p=\tau(p)\Omega.
\tag{3.2}
\]
This calculation includes the atomic diagonal \(x=y=0\); discarding that diagonal would destroy (3.2).

Let \(e=1_{\{0\}}=(1,0)\in M\).
Multiplication by \(e\) is a nonzero rank-one orthogonal projection on \(H\), and commutes with \(X\).
Equation (2.1) gives \(\Delta(X)<1\).

### 3.3 Explicit failure of closability and of the vacuum adjoint

For \(n\ge1\), set
\[
p_n(t)=t(1-t/2)^n.
\]
Then \(p_n(0)=0\), \(p_n'(0)=1\), and, on \([1,2]\),
\[
|p_n(t)|\le 2^{1-n},\qquad
|p_n'(t)|\le 2^{-n}+n2^{1-n}.
\tag{3.3}
\]
In particular \(p_n\to0\) in \(H\).
At the atom, (3.1) gives
\[
(Dp_n)(0)
=-\tfrac12p_n'(0)-\tfrac12\int_1^2\frac{p_n(y)}y\,dy
\longrightarrow-\tfrac12.
\]
On the interval, the atomic contribution has absolute value at most \(2^{-n}\).
The interval divided difference is bounded by \(\sup_{[1,2]}|p_n'|\), by integration of the derivative along the real segment.
Hence
\[
\sup_{1\le x\le2}|Dp_n(x)|\longrightarrow0.
\]
Therefore
\[
p_n\longrightarrow0,\qquad Dp_n\longrightarrow-\tfrac12e\Omega\ne0
\quad\text{in }H.
\tag{3.4}
\]
This proves that \(D\) is not closable.
It also proves
\[
\langle\Omega,Dp_n\rangle=\tau(Dp_n)\longrightarrow-\tfrac14,
\]
so the functional \(p\mapsto\langle\Omega,Dp\rangle\) is not \(H\)-bounded and \(\Omega\notin\operatorname{Dom}D^*\).

The example establishes the algebraic dense-domain boundary only.
It does not contradict the selfadjoint closable-dual implication discussed in Section 5.

## 4. Strong normal example: the disk with an atom

### 4.1 Space, polynomial domain and Cauchy operator

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(d\nu=dA/\pi\), and
\[
\mu=\tfrac12\delta_0+\tfrac12\nu,\qquad
M=L^\infty(\mathbb D,\mu),\qquad X(z)=z.
\]
The atomic value at zero is independent of the \(\nu\)-equivalence class.
In coordinates,
\[
H=\mathbb C\oplus L^2(\mathbb D,\nu),\qquad
\|(a,f)\|_H^2=\tfrac12|a|^2+\tfrac12\|f\|_2^2,\qquad
\Omega=(1,1),\quad X(a,f)=(0,zf).
\tag{4.1}
\]
The faithful normal trace is \(\tau(a,f)=\frac12a+\frac12\int f\,d\nu\).
The bounded normal coordinate generates \(M\): its Borel functional calculus contains the atomic projection and all bounded coordinate functions modulo \(\mu\).

Set \(\mathcal A=\mathbb C[X,X^*]\), represented by \(p(z,\bar z)\mapsto(p(0),p)\).
A polynomial that vanishes \(\nu\)-almost everywhere vanishes everywhere on the disk by continuity, and is the zero real polynomial, hence the zero polynomial in the independent symbols \(z,\bar z\).
This makes every derivative in the construction independent of representatives.

The algebra \(\mathbb C[z,\bar z]\) is uniformly dense in the continuous functions on the closed disk, by Stone-Weierstrass.
Continuous functions are dense in \(L^2(\mu)\) for this finite Borel measure, including its atom.
Thus \(\mathcal A\Omega\) is dense in \(H\).
It contains \(\Omega\) and is invariant under both \(X\) and \(X^*\).

On \(L^2(\nu)\), define
\[
(Cf)(z)=\int_{\mathbb D}\frac{f(w)}{z-w}\,d\nu(w).
\tag{4.2}
\]
For fixed \(z\in\mathbb D\),
\[
\int_{\mathbb D}\frac{d\nu(w)}{|z-w|}
\le\frac1\pi\int_{|u|<2}\frac{dA(u)}{|u|}=4,
\]
and the same column bound holds.
Weighted Cauchy-Schwarz and integration give
\[
|Cf(z)|^2\le4\int_{\mathbb D}\frac{|f(w)|^2}{|z-w|}\,d\nu(w),
\qquad \|Cf\|_2^2\le16\|f\|_2^2.
\tag{4.3}
\]
Initially these formulas apply to bounded \(f\), and then define a unique bounded extension with \(\|C\|\le4\).
No principal value is used in (4.2).

For \(z=re^{i\theta}\ne0\), the angular average of \((z-\rho e^{i\phi})^{-1}\) is \(1/z\) when \(\rho<r\), and zero when \(\rho>r\).
The geometric expansions on these circles and absolute integrability of the original kernel give
\[
C1(z)=\frac1z\int_0^r2\rho\,d\rho=\bar z.
\tag{4.4}
\]
The formula at zero follows by angular integration.
Cancellation also gives, for polynomials \(p\),
\[
zCp-C(zp)=\left(\int_{\mathbb D}p\,d\nu\right)1.
\tag{4.5}
\]
Finally Fubini is justified by (4.3)'s absolute row/column bounds, and
\[
\int_{\mathbb D}Cp\,d\nu
=\int_{\mathbb D}p(w)
  \left(\int_{\mathbb D}\frac{d\nu(z)}{z-w}\right)d\nu(w)
=-\int_{\mathbb D}\bar w\,p(w)\,d\nu(w).
\tag{4.6}
\]

### 4.2 Definition and well-definedness of the dual

Use
\[
\partial_z=\tfrac12(\partial_x-i\partial_y),\qquad
\bar\partial=\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y).
\]
Choose a real \(\chi\in C_c^\infty(\mathbb D)\) equal to one on a neighborhood of zero.
Put
\[
q_0(z)=\frac{\bar z^3}{12z^2}+\frac{\bar z^4}{24z}\quad(z\ne0),
\qquad
q(z)=\chi(z)q_0(z),\quad q(0)=0.
\tag{4.7}
\]
Since \(|q_0(z)|\le |z|/12+|z|^3/24\), \(q\) is bounded, continuous at zero, and compactly supported in the disk.
It is smooth away from zero.

For \(p\in\mathcal A\), define \(Dp=(a(p),L(p))\) by
\[
a(p)=-\frac12\partial_zp(0)
      -\frac12\int_{\mathbb D}\frac{p(w)}w\,d\nu(w),
\tag{4.8}
\]
\[
L(p)(z)=q(z)\bar\partial^4p(z)
-\frac{p(z)-p(0)}{2z}
+\frac12\big(Cp(z)-\bar z\,p(z)\big),
\qquad \operatorname{Dom}D=\mathcal A\Omega.
\tag{4.9}
\]
The atomic integral is absolutely convergent because \(1/|w|\) is integrable on the disk.
For a fixed polynomial, \(|p(z)-p(0)|\le c_p|z|\) on the disk, so the middle term of (4.9) is bounded almost everywhere.
The first term is bounded, and the last term belongs to \(L^2(\nu)\) by (4.3).
Therefore \(D\) is a well-defined complex-linear map into \(H\).

Angular integration gives \(\int1/w\,d\nu=0\); (4.4) now gives \(D\Omega=0\).

For the continuous component, the first term commutes with multiplication by \(z\), since \(\bar\partial z=0\).
The middle term has commutator \(p(0)/2\), and (4.5) gives the commutator of the last term.
Thus
\[
zL(p)-L(zp)=\frac12p(0)+\frac12\int_{\mathbb D}p\,d\nu.
\]
For the atomic component, \(\partial_z(zp)(0)=p(0)\), so
\[
-a(zp)=\frac12p(0)+\frac12\int_{\mathbb D}p\,d\nu.
\]
Together these prove
\[
[X,D]p=\tau(p)\Omega=P_\Omega p
\qquad(p\in\mathcal A\Omega).
\tag{4.10}
\]

### 4.3 The fourth-order distribution identity

All distributions in this subsection are complex-linear distributions paired bilinearly with test functions and use ordinary planar area \(dA\), not \(\nu\).
In these conventions
\[
\bar\partial(1/z)=\pi\delta_0.
\tag{4.11}
\]
For clarity, the normalization has the following direct check.
For a compactly supported smooth test function \(\varphi\), write \(\bar\partial=\frac12e^{i\theta}(\partial_r+i r^{-1}\partial_\theta)\).
Integrating \(z^{-1}\bar\partial\varphi\) over \(|z|>\varepsilon\), the angular derivative integrates to zero and the radial derivative gives
\[
\int_{|z|>\varepsilon}\frac{\bar\partial\varphi(z)}z\,dA(z)
=-\frac12\int_0^{2\pi}\varphi(\varepsilon e^{i\theta})\,d\theta
\longrightarrow-\pi\varphi(0).
\]
Local integrability of \(1/z\) completes the distributional calculation.
Section 6 identifies a checked primary source for this standard identity.

One must not treat \(1/z^2\) alone as a locally integrable function.
Define instead
\[
T=-\partial_z(1/z)\in\mathcal D'(\mathbb C).
\]
It equals \(1/z^2\) away from zero and satisfies \(\bar\partial T=-\pi\partial_z\delta_0\).
For every integer \(m\ge1\), multiplication by \(\bar z^m\) yields the locally integrable function
\[
\bar z^mT=\bar z^m/z^2.
\tag{4.12}
\]
Indeed, apply the distribution derivative to \(\bar z^m\varphi\) and integrate by parts on \(|z|>\varepsilon\).
Since \(\partial_z\bar z^m=0\), the interior term is the displayed function.
The inner-circle boundary term is \(O(\varepsilon^m)\), so it tends to zero.

For \(m\ge1\), \(\bar z^m\partial_z\delta_0=0\), because both the value and the \(\partial_z\)-derivative of \(\bar z^m\) vanish at zero.
The product rule and (4.12) give
\[
\bar\partial(\bar z^3T)=3\bar z^2T,\qquad
\bar\partial^2(\bar z^3T)=6\bar zT,\qquad
\bar\partial^3(\bar z^3T)=6T.
\]
Consequently
\[
\bar\partial^4(\bar z^3/z^2)=-6\pi\partial_z\delta_0.
\tag{4.13}
\]
Similarly, \(\bar z^m\delta_0=0\) for \(m\ge1\), and repeated use of (4.11) gives
\[
\bar\partial^4(\bar z^4/z)=24/z.
\tag{4.14}
\]
Equations (4.13)-(4.14) imply
\[
\bar\partial^4q_0=-\frac{\pi}{2}\partial_z\delta_0+\frac1z.
\]
Applying the cutoff product rule gives
\[
\bar\partial^4q=-\frac{\pi}{2}\partial_z\delta_0+\frac1z+R,
\tag{4.15}
\]
where, on the punctured disk,
\[
R=\frac{\chi-1}{z}
+\sum_{k=1}^4\binom4k
   (\bar\partial^k\chi)(\bar\partial^{\,4-k}q_0).
\tag{4.16}
\]
All derivatives in the sum are ordinary derivatives on the support of derivatives of \(\chi\), which stays away from zero.
The first term vanishes near zero.
Thus \(R\) extends to a smooth bounded function on \(\mathbb D\), with \(R=0\) near zero and \(R=-1/z\) outside \(\operatorname{supp}\chi\).
Multiplication of \(\partial_z\delta_0\) by \(\chi\) introduces no extra term because \(\chi=1\) near zero.

Since \(q\) has compact support and \(1/z+R\) vanishes outside that support, (4.15) can be tested against an arbitrary polynomial using a smooth auxiliary cutoff equal to one near the support.
Dividing by \(\pi\), using \(d\nu=dA/\pi\) and \(\langle\partial_z\delta_0,p\rangle=-\partial_zp(0)\), gives the exact identity
\[
\int_{\mathbb D}q\,\bar\partial^4p\,d\nu
=\frac12\partial_zp(0)
 +\int_{\mathbb D}\frac pz\,d\nu
 +\int_{\mathbb D}Rp\,d\nu.
\tag{4.17}
\]

### 4.4 The actual vacuum adjoint

By (4.6), (4.9), (4.17), and \(\int1/z\,d\nu=0\),
\[
\begin{aligned}
\int_{\mathbb D}L(p)\,d\nu
&=\frac12\partial_zp(0)
 +\int\frac pz\,d\nu+\int Rp\,d\nu
 -\frac12\int\frac pz\,d\nu
 +\frac12\left(-\int\bar zp\,d\nu-\int\bar zp\,d\nu\right)\\
&=\frac12\partial_zp(0)
 +\frac12\int\frac pz\,d\nu
 +\int(R-\bar z)p\,d\nu.
\end{aligned}
\]
Adding the atomic component (4.8) and then applying the outer trace weight \(1/2\) yields
\[
\tau(Dp)=\frac12\int_{\mathbb D}(R-\bar z)p\,d\nu.
\tag{4.18}
\]
Thus, with the inner product fixed in Section 1,
\[
\Omega\in\operatorname{Dom}D^*,\qquad
D^*\Omega=(0,\overline R-z)\in H.
\tag{4.19}
\]
The derivative evaluation in the atomic output is not \(H\)-bounded by itself.
Its exact cancellation against the distributional derivative of \(q\) is essential in (4.18).
The factors \(1/2\) in both the operator and the trace have been retained.

### 4.5 A dense set of actual adjoint-domain vectors

Let \(\psi\in C_c^\infty(\mathbb D\setminus\{0\})\) and put \(h_\psi=(0,\psi)\in H\).
On its support \(q\) is smooth.
Four integrations by parts have positive sign and no boundary contribution, and give
\[
\begin{aligned}
\langle h_\psi,Dp\rangle_H
=\frac12\bigg[
&\frac{p(0)}2\int_{\mathbb D}\frac{\overline\psi}{z}\,d\nu\\
&+\int_{\mathbb D}
 \left\{\bar\partial^4(q\overline\psi)
  -\frac{\overline\psi}{2z}
  +\frac12\big(\overline{C^*\psi}-\bar z\,\overline\psi\big)\right\}
 p\,d\nu\bigg].
\end{aligned}
\tag{4.20}
\]
Every coefficient in the integral is in \(L^2(\nu)\): the differential and quotient terms are smooth with compact support away from zero, and \(C^*\) is bounded by (4.3).
The scalar \(p(0)\) is a bounded functional on \(H\) because its atomic weight is \(1/2\).
Equation (4.20) therefore proves \(h_\psi\in\operatorname{Dom}D^*\), and in fact
\[
D^*h_\psi=
\left(
\frac12\int_{\mathbb D}\frac{\psi}{\bar z}\,d\nu,\
\partial_z^4(\bar q\,\psi)-\frac{\psi}{2\bar z}
       +\frac12(C^*\psi-z\psi)
\right).
\tag{4.21}
\]

The space \(C_c^\infty(\mathbb D\setminus\{0\})\) is dense in \(L^2(\nu)\).
For example, first truncate an \(L^2\) function to compact annuli, whose complement has vanishing area, and then use ordinary smooth approximation on each annulus.
Hence the closure of the span of all \(h_\psi\) is \(\{0\}\oplus L^2(\nu)\).
Adding \(\Omega=(1,1)\), which belongs to the actual adjoint domain by (4.19), gives a dense subspace of \(H\).
Thus \(\operatorname{Dom}D^*\) is dense and \(D\) is closable.

This argument proves closability of the specified operator with domain exactly \(\mathcal A\Omega\), not merely existence of some unrelated closable implementer.

### 4.6 Nonmaximal Delta and exclusion of the bounded atomic vector

Let \(e=(1,0)=1_{\{0\}}(X)\in M\).
The bounded multiplication operator \(L_e\) has rank one and commutes with \(X\), so (2.1) gives
\[
\Delta(X)<1.
\tag{4.22}
\]

Let \(\overline D\) be the closure.
For \(v\in\operatorname{Dom}\overline D\), take \(p_n\in\mathcal A\Omega\) with \(p_n\to v\) and \(Dp_n\to\overline Dv\).
Equation (4.10) gives
\[
D(Xp_n)=X Dp_n-P_\Omega p_n
\longrightarrow X\overline Dv-P_\Omega v.
\]
Closedness and boundedness of \(X,P_\Omega\) imply
\[
X\operatorname{Dom}\overline D\subseteq\operatorname{Dom}\overline D,
\qquad
[X,\overline D]v=P_\Omega v.
\tag{4.23}
\]
Also \(\overline D\Omega=0\), and \((\overline D)^*=D^*\).

If \(e\Omega\in\operatorname{Dom}\overline D\), then \(Xe\Omega=0\), so (4.23) would imply
\[
X\overline D(e\Omega)=P_\Omega e\Omega=\tfrac12\Omega.
\tag{4.24}
\]
The atomic coordinate on the left is zero, while that on the right is \(1/2\).
This is impossible.
Therefore
\[
e\Omega\notin\operatorname{Dom}\overline D,\qquad
M\Omega\not\subseteq\operatorname{Dom}\overline D.
\tag{4.25}
\]
The same atomic-coordinate contradiction applies to any linear operator defined on a domain containing \(e\Omega\) and satisfying the dual relation there.
In particular there is no full-\(M\Omega\) dual for this \(X\), even after changing the operator entirely.

The closure itself is a normalized closed densely defined dual on an \(X\)-invariant domain, with the vacuum in its adjoint domain.
Thus requiring a closed operator on some dense invariant domain does not repair the normal-generator implication.

### 4.7 Why this does not satisfy the ACSY24 starred-commutator interface

[ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), Section 3, proves maximal Delta for a closable dual on a dense starred polynomial core if the adjoint-generator commutators also have bounded extensions.
The present example satisfies the other conditions and fails maximality.
Consequently its \([X^*,D]\) cannot have a bounded extension.

The obstruction is consistent with the formula: the continuous component of this commutator contains
\[
-4q\,\bar\partial^3p
+\frac{p(0)\bar z}{2z}
+\frac12\big(\bar z\,Cp-C(\bar z p)\big).
\tag{4.26}
\]
Its atomic component is \(\frac12\int(\bar w/w)p(w)\,d\nu(w)\).
The last two terms of (4.26) and that atomic component have bounded extensions; the differential term is not controlled by the unstarred dual relation.
We use the already established implication and (4.22), rather than an additional approximation argument, to conclude that the full starred commutator is unbounded.

There is therefore no conflict with ACSY24 Proposition 3.5: a dual operator alone need not induce a Hilbert-tensor-valued derivation on the represented starred algebra.
The stronger source premise controls all starred commutators.

## 5. Relation to the four domain combinations

The disk example satisfies both extra conditions simultaneously, on the starred polynomial domain:
\[
\Omega\in\operatorname{Dom}D^*
\quad\text{and}\quad
D\text{ closable}.
\]
It therefore supplies every weaker combination obtained by asking only one of these conditions, or by allowing an arbitrary dense invariant domain instead of that algebra.
Yet its atom forbids every full-domain dual.
This is a single witness for all four small-domain-to-full-domain nonimplications.

For selfadjoint tuples the closable case has a different outcome.
If a common dense \(X_j\)-invariant domain contains \(\Omega\), it contains \(\mathbb C\langle X_1,\ldots,X_d\rangle\Omega\).
Restricting a closable dual to that polynomial domain leaves it closable.
Since \(X_j^*=X_j\), the required adjoint-generator commutators are the same bounded rank-one operators.
The already fixed selfadjoint-block regularization in [ACSY24-U001, Section 3](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) then gives \(\Delta(X)=d\).
Section 3's explicit nonclosability is thus necessary to its example.

The alternative spectral-truncation input is fixed in [Shl06-U002](../audits/literature/Shl06/Yin_U002.md#shl06-u002), with its precise full-domain form-commutator convention.
Neither route is reconstructed as a new Claim here, and neither establishes an all-\(M\Omega\) domain merely from the small core.

## 6. Source check and proof-inspection limits

The needed external identity was the normalization of the Cauchy fundamental solution in (4.11).
The bounded reuse search inspected the existing disk-Cauchy Claim/source unit, the nearby weighted-disk domain example, and the local literature contents for distributional Cauchy/Pompeiu coverage.
No adequate fixed source check for this precise distribution identity was located.

A targeted primary-source search then located Alain Yger, *Distributions*, the author's Bordeaux course notes for the 2010–2011 MHT836 course, [author-hosted PDF](https://www.math.u-bordeaux.fr/~ayger/mht836.pdf), Example 2.18, equation (2.21), printed p.31 / PDF p.35.
The title/author/course description and the selected formula with its Cauchy-Pompeiu test-function interpretation were read in the parsed 98-page artifact on 2026-10-14.
The standard identity was accepted at statement and normalization scope; no whole-notes audit, original Cauchy-Pompeiu proof audit, or publisher-edition comparison is claimed.
Root registered this source as `Yge11` in the bibliography.
The bounded PDF acquisition attempt failed certificate verification; no local PDF is available.
The primary-text inspection and the local proof above do not claim a local artifact or a whole-source audit.
The direct polar computation in Section 4.3 also proves the identity in exactly the conventions used here.

The Schur estimate and disk Cauchy transform are already supported by C_F0003 and Xia23-U001; their stronger source conclusions are unused.
MSY23-U002 supplies only the finite-rank-cycle characterization of maximal Delta.
The ordinary distribution product rule, Hilbert adjoint criterion, smooth cutoff existence, and polynomial/smooth approximation are standard foundations at the explicit scopes above.

Author self-check reconstructed the commutator in both coordinates, the distribution extension of \(1/z^2\), the fourth-order coefficients, cutoff remainder, both probability weights, adjoint pairings, density and the atomic contradiction.
The selfadjoint example includes an explicit sequence establishing its two failures.
No unresolved mathematical input remains in these candidate proofs as written.
No numerical test, formal verification, independent review, novelty claim or new reverse implication is asserted.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T12:10 |
| status | open |
| reason | Complete explicit candidate proofs of the two atomic counterexamples, including actual adjoint domains, closability and exclusion of every full-domain replacement. Independent whole-artifact review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both existence statements and their exact operator/domain properties. |
| argument | [Argument](#argument) | Sections 2--6: definitions, distribution normalization, Hilbert adjoints, atomic obstruction and precise source boundaries. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Finite-rank characterization of maximal Delta for arbitrary bounded generators. |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Section 3 bounded starred-commutator regularization, used only for the explicit comparison and unboundedness conclusion. |
| dependency | [C_F0003](Yin_C_F0003_v1.md#counterexample-normal-multiplication-on-the-disk) | Existing disk-Cauchy calculation, rederived at the exact normalization here. |
| dependency | [Bla06-U001](../audits/literature/Bla06/Yin_U001.md#bla06-u001) | Densely defined adjoint and closability criterion. |

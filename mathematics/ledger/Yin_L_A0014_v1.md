---
author: Yin
---
# First amalgamated-atom tests: support degeneration, normalization and boundary scope

Date: 2026-11-11 (Asia/Hong_Kong).
This first exploration of [S_A0005](../strategies/Yin_S_A0005.md) tests the three interfaces identified in [L_A0013](Yin_L_A0013_v1.md#three-missing-interfaces-for-a-diffuse-cyclic-base).
The main agent and two development helpers derived the examples and their exact limits.
These are calibrations and useful failed strengthening attempts, not a new Atiyah permanence theorem.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0014_v1.md#whole-artifact-finding) covers the complete calculations and their stated limits, with the analytic foundations accepted at the recorded scope.

## Setting and accepted interfaces

Use the central cyclic amalgam
\[
G:=\langle u,a\mid [u,a]=1\rangle
 *_{\langle u\rangle}
 \langle u,b\mid [u,b]=1\rangle
 \cong\mathbb Z\times F(a,b),
\qquad B:=W^*(u).
\]
Both vertex groups are copies of \(\mathbb Z^2\).
The canonical expectation \(E_B\) kills group words outside \(\langle u\rangle\).
Write \(E^{(n)}:=\operatorname{id}_{M_n}\otimes E_B\) and
\[
\nu_n(T):=(\operatorname{Tr}_n\otimes\tau_G)(p_{\ker T}).
\]
The two vertex algebras are free over \(B\) by the reduced-word argument retained in L_A0013.
All displayed kernel dimensions below are computed directly, without an Atiyah premise for \(G\).

Use the [two-sided support formulas](../claims/Yin_C_F0181_v1.md#trace-conventions-and-square-support-cuts) only at their algebraic projection identities.
For an arbitrary base algebra, faithfulness still gives \(p_T\le q\), where \(q\) is the support of \(E^{(n)}(p_T)\), and
\[
p_{Tq}=p_T+(1-q).
\tag{1}
\]
The finite-dimensional implication from support to a bounded inverse is not imported.
The second accepted input is [BBL21 Theorem 3.5](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), at its general-base, boundedly invertible expected-kernel hypothesis.
Its analytic foundations retain the source unit's accepted-input status.

## Both support cuts can be ineffective

Set
\[
s:=u-1,\quad h:=s^*s,\quad
c:=\begin{pmatrix}s\\a\end{pmatrix},\quad
r:=\begin{pmatrix}s&b\end{pmatrix},\quad
T:=cr=
\begin{pmatrix}s^2&sb\\as&ab\end{pmatrix}.
\tag{2}
\]
The entries of \(c\) and \(r\) belong to the first and second vertex group rings, respectively.
The matrix \(T\) involves both vertices, including the mixed word \(ab\).
Since \(c^*c=rr^*=1+h\), the column \(c\) has a bounded left inverse and the row \(r\) has a bounded right inverse.
Thus \(\ker T=\ker r\), while \(\ker T^*=\ker c^*\).
Their projections are
\[
p_T=\frac1{1+h}
 \begin{pmatrix}1&-s^*b\\-b^*s&h\end{pmatrix},
\qquad
p_{T^*}=\frac1{1+h}
 \begin{pmatrix}1&-sa^*\\-as^*&h\end{pmatrix}.
\tag{3}
\]
Each has unnormalized trace one.
Conditional expectation gives
\[
E^{(2)}(p_T)=E^{(2)}(p_{T^*})
=\operatorname{diag}\left((1+h)^{-1},h(1+h)^{-1}\right).
\tag{4}
\]
Both have full support, since \(s\ne0\) almost everywhere on the circle.
Neither has a bounded inverse, because \(h\) tends to zero on neighborhoods of \(u=1\).
Consequently both successive support projections are \(I_2\), and the support-only procedure makes no change.
The selfadjoint hermitization has the same full-support, no-gap failure in both diagonal blocks of its expected kernel.

This is a failure of support-only repair on an actual two-vertex group-ring matrix.
It is not yet a failure on an additive affine pencil with separate vertex entries: the mixed word \(ab\) in (2) must be retained in that distinction.

### An exact affiliated normalization and its limits

The scalar \(s=u-1\) is injective by the Haar law and has its actual affiliated inverse, independently of the conjecture.
With
\[
D:=\operatorname{diag}(s^{-1},1),
\]
the affiliated product satisfies
\[
DTD=
\begin{pmatrix}1&b\\a&ab\end{pmatrix}
=\begin{pmatrix}1\\a\end{pmatrix}\begin{pmatrix}1&b\end{pmatrix}.
\tag{5}
\]
Both expected kernel projections of the resulting bounded matrix equal \(\tfrac12 I_2\).
Invertible affiliated multiplication preserves analytic nullity, so (5) repairs the expected-kernel gap for this example.
The unbounded factors are legitimate actual cyclic rational inverses, not bounded similarities.
This uses the existing cyclic-pivot mechanism, and the mixed word \(ab\) still prevents treating (5) directly as an additive two-vertex pencil.
Thus (4) does not establish impossibility of rational normalization or of every probabilistic reduction.

### Affine realization changes the support behavior

Consider
\[
P:=\begin{pmatrix}
0&0&s\\
0&0&a\\
s&b&-1
\end{pmatrix}
=\begin{pmatrix}0_2&c\\r&-1\end{pmatrix}.
\tag{6}
\]
This is affine in \(u,a,b\), with no mixed vertex word.
Its kernel and adjoint kernel are \((\ker r)\oplus0\) and \((\ker c^*)\oplus0\), respectively.
Both expected-kernel supports are
\(q:=\operatorname{diag}(I_2,0)\).
The right cut \(U:=Pq\) has kernel projection \(p_P+(1-q)\), so \(\nu_3(U)=2\).
Its adjoint kernel is exactly the first two coordinates, so its left support is again \(q\).
The subsequent left cut gives
\[
qPq=0,\qquad \nu_3(qPq)=3.
\]
The two corrections are each one, recovering \(\nu_3(P)=1\).
Although the intermediate expected right kernel still lacks a bounded inverse, the second cut gives the zero matrix and closes this example exactly.
Polynomial-level failure of support-only repair therefore cannot be transferred to this affine realization without checking its new kernels.

## An additive two-vertex model with an invertible expected kernel

Put
\[
t:=u+u^*,\qquad f:=t+a,\qquad
V:=\begin{pmatrix}f&1&0\\0&1&b\end{pmatrix},
\qquad H:=V^*V=Y_1+Y_2,
\tag{7}
\]
where
\[
Y_1:=
\begin{pmatrix}
f^*f&f^*&0\\
f&1&0\\
0&0&0
\end{pmatrix},
\qquad
Y_2:=
\begin{pmatrix}
0&0&0\\
0&1&b\\
0&b^*&1
\end{pmatrix}.
\]
The two positive selfadjoint group-ring matrices belong to the respective vertex algebras.
They are affine in \(a,a^*,b,b^*\) with central Laurent-polynomial coefficients, since
\(f^*f=t^2+1+t(a+a^*)\).
This is not a claim of degree one in the original tuple \(u,a,b\) with constant coefficients.
The BBL theorem itself applies directly to these bounded operators and does not require that degree restriction.

Solving \(Vx=0\) gives
\[
w:=\begin{pmatrix}1\\-f\\b^*f\end{pmatrix},\qquad
k:=(w^*w)^{-1}=(1+2f^*f)^{-1},\qquad
p:=p_{\ker H}=wkw^*.
\tag{8}
\]
The column \(wk^{1/2}\) is an isometry onto the kernel, so \(\nu_3(H)=1\).
Each row defining \(Y_j\) has a bounded right inverse, so \(\nu_3(Y_j)=2\).

Conditional expectation in the free Haar variables gives
\[
\xi:=E^{(3)}(p)=
\begin{pmatrix}
\alpha&-m&0\\
-m&\beta&0\\
0&0&\beta
\end{pmatrix},
\tag{9}
\]
with pointwise central functions
\[
\alpha:=(4t^4-4t^2+9)^{-1/2},
\quad
\beta:=\frac{1-\alpha}{2},
\quad
m:=\frac{1+(2t^2-3)\alpha}{4t}\quad(t\ne0),
\qquad m(0):=0.
\tag{10}
\]
Indeed, writing \(\tau_a\) for Haar integration in the \(a\) variable,
\[
\alpha=\tau_a(k)
=\frac1{2\pi}\int_0^{2\pi}
 \frac{d\theta}{3+2t^2+4t\cos\theta}
=\frac1{\sqrt{(3+2t^2)^2-16t^2}}.
\]
The elementary circle integral follows, for example, by the substitution \(x=\tan(\theta/2)\).
Next \(\beta=\tau_a(f^*fk)=(1-\alpha)/2\) and
\(m=\tau_a(kf^*)\) give (10).
For the latter identity, use
\(1=(3+2t^2)\alpha+4t\,\tau_a(ak)\).
At \(t=0\), \(k=1/3\) and \(m=0\).
The cross terms with a final \(b\) vanish under conditional expectation; conjugating \(fkf^*\) by \(b\) leaves its central expectation \(\beta\).

Since \(|t|\le2\) and \(\|f\|\le3\), one has \(k\ge1/19\).
The upper-left block of \(\xi\) consequently satisfies
\[
\begin{pmatrix}\alpha&-m\\-m&\beta\end{pmatrix}
\ge
\frac1{19}\begin{pmatrix}1&-t\\-t&t^2+1\end{pmatrix}
\ge\frac1{114}I_2.
\tag{11}
\]
The last Gram matrix has determinant one and trace at most six.
Also \(\beta\ge(t^2+1)/19\ge1/19\).
Thus
\[
\xi\ge\frac1{114}I_3.
\tag{12}
\]
This verifies the actual expected-kernel hypothesis without assuming a spectral gap for \(H\).

## The expected kernel leaves the cyclic rational field

The first diagonal entry of (9) is not in \(\mathbb C(u)\).
Indeed
\[
\alpha^{-2}
=u^{-4}Q(u),
\qquad
Q(u):=4u^8+12u^6+25u^4+12u^2+4.
\tag{13}
\]
If \(\alpha\) agreed almost everywhere on the circle with a rational function, squaring would make \(Q\) a rational square, hence a polynomial square over \(\mathbb C\).
Taking the leading coefficient of its hypothetical square root as \(2\), successive coefficients force the root to have the form
\(2u^4+3u^2+4\).
Its constant coefficient squared is \(16\), contradicting the constant coefficient \(4\) of \(Q\).
Thus \(\xi\notin M_3(\mathbb C(u))\), despite the group-ring input, full support, and uniform lower bound (12).
The rational identities used in this argument follow from almost-everywhere equality on the circle, since a nonzero rational function has only finitely many zeros there.

This refutes the strengthening that the whole expected kernel of every such pencil stays in the cyclic rational field.
It does not assert that \(\xi\) lies outside every larger algebraic extension or every vertex rational closure.
Its support is \(I_3\), so its support trace remains integer.

## The actual subordination boundary values are nevertheless zero

Apply BBL21 at \(b=0\) to the two operators in (7), using (12).
It supplies \(b_1,b_2\in M_3(B)_{\mathrm{sa}}\), with \(b_1+b_2=0\), and
\[
p=p_1\wedge p_2,\qquad p_j:=p_{\ker(Y_j-b_j)}.
\]
Positivity of the summands gives \(Y_jp=0\).
The inclusion \(p\le p_j\) also gives \((Y_j-b_j)p=0\), hence \(b_jp=0\).
Conditional expectation now yields \(b_j\xi=0\), and invertibility of \(\xi\) proves
\[
b_1=b_2=0.
\tag{14}
\]
The unnormalized source trace identity is exactly
\[
2+2=3+1.
\]
This argument applies to any positive two-summand zero-atom test meeting the source's invertible-expected-kernel premise.
Such tests cannot exhibit nonzero boundary shifts, even when their expected kernel is nonrational.

## Consequence for the next investigation

The first test establishes two different limitations: support-only repair can fail before linearization, and rationality of the full expected kernel is too strong even in an additive two-vertex model.
The explicit affine realization and positive model also show why neither limitation by itself refutes the atom-transfer route.
The scalar rational normalization (5) and the two support cuts in (6) use already controlled mechanisms.

The next boundary-coefficient test should be an indefinite decomposition or a non-bottom atom with an independently known nonzero kernel and invertible expected kernel.
Its summands must not separately annihilate that kernel; otherwise (14) remains decisive.
Adding opposite controlled base shifts to the positive example merely shifts the two boundary values and supplies no new coefficient phenomenon.
The target should be control of the boundary kernel traces, rather than rationality of the entire conditional expectation.

The base in this round is central.
No noncentral cyclic-edge theorem, universal support repair, or new Atiyah group class is established.
The exact calculations provide a first-round calibration and a sharper next target for S_A0005.

---
author: Yin
---
# Diagonal tensor tests for the surviving trinomial kernel

This development studies the actual regular group operator \(T=1+u-v\) in a torsion-free group \(G\), with \(u\ne e\), and its kernel projection \(p\in\mathcal N(G)\).
Write \(\delta=\tau_G(p)\).
The question is whether diagonal embeddings of the group into its direct powers impose a stronger constraint than the [coefficient-angle bound](../claims/Yin_C_A0009_v2.md#statement), using information unavailable in the [pairwise-Haar model](../ledger/Yin_L_A0025_v1.md).
The proposed inputs are \(\Delta_n(g)=g^{\otimes n}\), \(q_n=\Delta_n(p)\), and \(P_n=p^{\otimes n}\).
The task is to justify the exact tensor identity, all spectral and trace interfaces, and any intersection or quantitative-angle conclusion without applying an unbounded inverse to arbitrary Hilbert-space vectors.
No abstract replacement of the canonical regular group law, assumed Atiyah property, or inference from \(\delta+\delta^n\le1\) to \(\delta=0\) is permitted.
The conclusions concern these exact tensor tests and do not complete the Task.

## Actual setting and reused interfaces

Work in \(M=\mathcal N(G)\), with the canonical trace \(\tau(1)=1\), and in the actual product-group algebras \(M^{\bar\otimes n}=\mathcal N(G^n)\).
All operators used in the derivations below are bounded.
An affiliated inverse is mentioned only after injectivity has been proved and is never applied pointwise to an arbitrary Hilbert-space vector.
The [cyclic regular representation](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), [finite-trace rank convention](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness), and the bounded compression argument in [C_A0009_v2](../claims/Yin_C_A0009_v2.md#argument) are the reused interfaces.
The local A-line and foundational-input search supplied no retained diagonal-tensor estimate settling the present question.
The calculations below do not adopt an additional external theorem or assert historical novelty.

It suffices to consider distinct \(e,u,v\).
If \(u=e\), then \(T=2-v\) has a bounded inverse; if \(v=e\) or \(v=u\), then \(T=u\) or \(T=1\).
Those cases have \(p=0\).
For the distinct case put
\[
 N=\|T\|^2,\qquad 3\le N\le9.
\tag{1}
\]
The upper bound is the triangle inequality, and the lower bound follows from \(\tau(T^*T)=3\).
The elementary inequality already available before tensorization is
\[
 3=\tau(T^*T)\le N\tau(1-p)=N(1-\delta),
 \qquad \delta\le1-\frac3N.
\tag{2}
\]
When a separate operator-norm estimate makes (2) stronger than \(1/3\), that improvement is already present in this original one-copy inequality.
Only the universal bound \(N\le9\) yields \(\delta\le2/3\) from (2).

## The diagonal map and the exact tensor identity

The map \(g\mapsto(g,\ldots,g)\) identifies \(G\) with its diagonal subgroup in \(G^n\).
The restriction of the left regular representation of \(G^n\) to that subgroup decomposes on right cosets into copies of the regular representation of \(G\).
Consequently it induces an injective normal trace-preserving star homomorphism
\[
 \Delta_n:M\longrightarrow M^{\bar\otimes n},
 \qquad \Delta_n(g)=g^{\otimes n}.
\tag{3}
\]
It preserves operator norm and spectral kernel projections.
Thus, with
\[
 A_n=\Delta_n(T),\qquad q_n=\Delta_n(p),\qquad
 P_n=p^{\otimes n},
\]
one has
\[
 q_n=P_{\ker A_n},\qquad \tau_n(q_n)=\delta,
 \qquad \tau_n(P_n)=\delta^n,\qquad \|A_n\|^2=N.
\tag{4}
\]
Here \(\tau_n=\tau^{\otimes n}\) is a probability trace, not an unnormalized finite matrix trace.

Let \(u_i\) and \(v_i\) act in coordinate \(i\).
The bounded equation \(vp=(1+u)p\) gives the exact identity
\[
 \left(\prod_{i=1}^n v_i\right)P_n
 =\left(\prod_{i=1}^n(1+u_i)\right)P_n.
\]
Only operators in different coordinates have been commuted.
Therefore
\[
 A_nP_n=f_n(u_1,\ldots,u_n)P_n,
 \qquad
 f_n(z_1,\ldots,z_n)=1+\prod_{i=1}^nz_i-\prod_{i=1}^n(1+z_i).
\tag{5}
\]
For \(n\ge2\),
\[
 f_n(z_1,\ldots,z_n)
 =-\sum_{\varnothing\ne S\subsetneq\{1,\ldots,n\}}
       \prod_{i\in S}z_i
\tag{6}
\]
is a nonzero polynomial, since each singleton monomial has coefficient minus one.
In particular \(f_2=-z_1-z_2\).
The case \(n=1\) gives the zero polynomial and supplies no such conclusion.

Since \(u\) has infinite order, the coordinate elements \(u_1,\ldots,u_n\) generate an actual subgroup isomorphic to \(\mathbb Z^n\).
Their regular joint spectral measure is product Haar measure on \(\mathbb T^n\), by the same right-coset Fourier decomposition used in the cyclic input.
A nonzero Laurent polynomial has a Haar-null zero set on that torus.
One direct proof is induction on \(n\): regard it as a polynomial in the last coordinate, discard the common zero set of its finitely many coefficient polynomials using one nonzero coefficient and the induction hypothesis, and then use the finite zero set of each remaining one-variable polynomial and Fubini's theorem.
Multiplication by a monomial first removes negative exponents without changing the zero set.
Thus \(f_n(u_1,\ldots,u_n)\) is injective and has an actual affiliated inverse.
This certificate depends only on the displayed nonzero abelian polynomial, not on an inverse of \(T\).

If \(\xi\in q_n\mathcal H_n\cap P_n\mathcal H_n\), then (5) gives
\[
 0=A_n\xi=f_n(u_1,\ldots,u_n)\xi.
\]
The proved injectivity forces \(\xi=0\), without applying the affiliated inverse to \(\xi\).
Hence
\[
 \boxed{q_n\wedge P_n=0\quad(n\ge2).}
\tag{7}
\]
Equivalently, the bounded map \(A_nP_n\) is injective on \(P_n\mathcal H_n\); polar decomposition gives
\[
 \delta^n\le\operatorname{rank}(A_n)=1-\delta,
 \qquad \boxed{\delta+\delta^n\le1.}
\tag{8}
\]
For every \(0<\delta\le1/3\), all inequalities (8) hold with room to spare: \(\delta+\delta^n\le4/9\) for \(n\ge2\).
Letting \(n\) tend to infinity in (8) gives only \(\delta\le1\), not \(\delta=0\).
The independent invertibility of \(f_n\) proves the intersection statement; it does not make \(A_n\) invertible on the full ambient space.

## Uniform accretivity for every even tensor power

Write \(a=pup\) in the corner \(pMp\).
Taking the norm square of \(vp=(1+u)p\) gives
\[
 p(u+u^*)p=-p,
 \qquad a=-\frac12p+iH,
 \qquad H=H^*\in pMp.
\tag{9}
\]
Moreover
\[
 pvp=p+a=-a^*.
\tag{10}
\]
Compressing the bounded diagonal operator therefore gives
\[
 P_nA_nP_n
 =P_n+a^{\otimes n}-(-1)^n(a^*)^{\otimes n}.
\tag{11}
\]
For every even \(n\ge2\), its real part is exactly
\[
 \boxed{\operatorname{Re}(P_nA_nP_n)=P_n.}
\tag{12}
\]
Thus the proposed two-copy positive compression extends to all even copies, with the same constant one.
It does not produce a constant growing with \(n\).

For \(\xi=P_n\xi\), Cauchy--Schwarz and (12) give
\[
 \|\xi\|^2
 =\operatorname{Re}\langle A_n\xi,\xi\rangle
 \le\|A_n\xi\|\,\|\xi\|.
\]
Since \(A_nq_n=0\),
\[
 \|\xi\|\le\|A_n(1-q_n)\xi\|
 \le\sqrt N\,\|(1-q_n)\xi\|.
\]
It follows that
\[
 \boxed{P_nq_nP_n\le\left(1-\frac1N\right)P_n
 \le\frac89P_n\qquad(n\ge2\text{ even}).}
\tag{13}
\]
This is a uniform quantitative separation, stronger than (7) for those powers.
It is not a sequence of angles tending to orthogonality or of rank bounds tending to zero.

## Exact overlap traces and their limiting content

Coordinatewise complex conjugation of the regular basis fixes the real-coefficient operator \(T\) and its kernel, hence fixes \(p\).
Consequently all Fourier coefficients
\[
 c_g=\tau(pg^{-1}),\qquad
 p=\sum_{g\in G}c_g g\quad\text{in }L^2(M,\tau),
\]
are real, with
\[
 c_e=\delta,\qquad c_{g^{-1}}=c_g,
 \qquad \sum_g c_g^2=\delta.
\tag{14}
\]
In particular the traces of \(pu\) and \(pv\) are real.
Equations (9)--(10) and \(u^*vp=(1+u^*)p\) give
\[
 \tau(pu)=-\frac\delta2,
 \qquad\tau(pv)=\frac\delta2,
 \qquad\tau(pu^*v)=\frac\delta2.
\tag{15}
\]
Expanding \(A_n^*A_n\) and using the product trace now gives the exact formula
\[
 \tau_n(P_nA_n^*A_nP_n)
 =\left(3+2\frac{(-1)^n}{2^n}-\frac4{2^n}\right)\delta^n.
\tag{16}
\]
For even \(n\) the coefficient is \(3-2^{1-n}\); at \(n=2\) it is \(5/2\).
Since \(A_n^*A_n\le N(1-q_n)\), (16) yields
\[
 \boxed{\tau_n(q_nP_n)
 \le\left(1-\frac{3-2^{1-n}}N\right)\delta^n
 \qquad(n\ge2\text{ even}).}
\tag{17}
\]
At \(n=2\), this is at least as strong as the uniform-angle trace estimate:
\[
 \tau_2(q_2P_2)
 \le\left(1-\frac5{2N}\right)\delta^2
 \le\frac{13}{18}\delta^2.
\tag{18}
\]

The same overlap has an exact Fourier expression:
\[
 \boxed{\tau_n(q_nP_n)=\sum_{g\in G}c_g^{\,n+1}.}
\tag{19}
\]
Indeed \(q_n\) has Fourier coefficient \(c_g\) at \((g,\ldots,g)\), whereas the coefficient of \(P_n\) there is \(c_g^n\).
Their \(L^2\) pairing gives (19); absolute convergence follows from (14) and \(|c_g|\le\delta\).
The sum is nonnegative because it is the trace of a product of projections, even when its individual odd-power summands have different signs.

If \(\delta>0\) and \(g\ne e\), then
\[
 |c_g|<\delta.
\tag{20}
\]
To see the strictness, Cauchy--Schwarz in \(L^2(M,\tau)\) bounds \(|\tau(pg^{-1})|\) by \(\|p\|_2^2=\delta\).
Equality would make \(gp\) a unit-modulus scalar multiple of \(p\), as an equality of bounded operators.
Its nonzero range would supply eigenvectors for the infinite-order regular group unitary \(g\), contradicting its bilateral-shift spectral law.
Torsion-freeness is used for every nonidentity \(g\) in this step, beyond the single infinite-order condition needed in (5)--(7).

The square summability in (14) strengthens (20) to
\[
 s:=\sup_{g\ne e}\frac{|c_g|}{\delta}<1.
\tag{21}
\]
For example only finitely many coefficients can have absolute value above \(\delta/2\); their finite maximum is strictly below \(\delta\), and the remaining ones are at most \(\delta/2\).
This reasoning also applies to an uncountable discrete group because a square-summable coefficient family has countable support.
Equations (14) and (19) imply the explicit estimate
\[
 \left|\frac{\tau_n(q_nP_n)}{\delta^n}-\delta\right|
 \le(1-\delta)s^{n-1},
 \qquad
 \lim_{n\to\infty}\frac{\tau_n(q_nP_n)}{\delta^n}=\delta.
\tag{22}
\]
Along even \(n\), combining (17) and (22) returns exactly
\[
 \delta\le1-\frac3N,
\tag{23}
\]
which is the original inequality (2).
Thus this quantitative tensor limit does not strengthen the existing one-copy norm information.
Using only the uniform angle (13) instead would give the still weaker \(\delta\le1-1/N\le8/9\).

## Conditional expectations and a precise projection calibration

Let \(E_i:M^{\bar\otimes n}\to M\) be the trace-preserving conditional expectation onto one coordinate.
For \(n\ge2\), the diagonal Fourier expansion gives
\[
 E_i(q_n)=\delta\,1,
 \qquad \tau_n\bigl(q_n(p\otimes1\otimes\cdots\otimes1)\bigr)=\delta^2,
\tag{24}
\]
with the same statement in every coordinate.
These are genuine consequences of the diagonal group embedding.
For the conditional expectation onto the diagonal subgroup algebra, write
\[
 E_{\Delta_n(G)}(P_n)=\Delta_n(b_n),
 \qquad b_n=\sum_g c_g^n g\quad\text{in }L^2(M,\tau).
\tag{25}
\]
The operator \(b_n\) is bounded and positive because it is obtained by conditional expectation of a projection, and
\[
 \boxed{0\le b_n\le\delta^{n-1}1.}
\tag{26}
\]
There is a direct subgroup-expectation proof of this bound.
For \(n=2\), use \(P_2\le p\otimes1\) and \(E_{\Delta_2(G)}(p\otimes1)=\delta1\).
Inductively first expect \(P_n\) onto \(\Delta_{n-1}(G)\times G\), obtaining \(\Delta_{n-1}(b_{n-1})\otimes p\).
The induction bound makes this at most \(\delta^{n-2}1\otimes p\); expectation onto the nested full diagonal gives \(\delta^{n-1}1\).
These subgroup expectations are the positive trace-preserving compressions deleting Fourier coefficients outside the specified subgroup, so the nested expectations compose in the required order.
No positive-multiplier theorem or unbounded operation is needed for (26).

Taking the trace against \(p\) in (26) gives only \(\tau_n(q_nP_n)\le\delta^n\), which is weaker than (17).
The exact coordinate expectations in (24) do not make \(q_n\) independent of \(P_n\); replacing their overlap by \(\delta^{n+1}\) at a fixed \(n\) is unjustified.
Formula (22) gives that value only after its stated normalization and limit.

A concrete actual-group calibration isolates the weakness of the two-copy projection facts.
In \(\mathcal N(\mathbb Z)=L^\infty(\mathbb R/\mathbb Z)\), take
\[
 A=(1/3,2/3),\qquad p=1_A,
 \qquad q_2(x,y)=p(x+y),
\tag{27}
\]
where addition is modulo one.
Then \(\tau(p)=1/3\), both coordinate expectations of \(q_2\) are \((1/3)1\), and
\[
 q_2(p\otimes p)=0,
\tag{28}
\]
because \(A+A\) lies outside \(A\) modulo one, apart from irrelevant endpoints.
Thus the two-copy zero-intersection statement and uniform-coordinate expectations, even strengthened to orthogonality, do not by themselves imply a strict improvement on \(1/3\).
This calibration is an actual torsion-free abelian diagonal-coproduct model for those projection facts only.
It does not satisfy the trinomial kernel or compression equations, and it does not satisfy (7) for every \(n\); no counterexample to the original group-ring assertion or to the full tensor system is claimed.

## Outcome of this tensor test

The proposed polynomial reduction is valid for every \(n\ge2\), and every even power gives the stronger exact accretive compression (12).
The complete deductions here are the intersection bound (8), the uniform angle (13), the exact overlap estimates (16)--(19), the Fourier limit (22), and the expectation bounds (24)--(26).
The dimension inequality is weaker than the existing \(1/3\) bound, while the computed limiting trace inequality is precisely the original trace--norm bound.
No numerical restriction beyond those already available has been obtained from this tensor step.

This failure does not prove that every use of diagonal group information is insufficient.
The full canonical group law has supplied a legitimate diagonal map unavailable in the abstract [pairwise-Haar obstruction](../ledger/Yin_L_A0025_v1.md#the-explicit-failure-of-the-regular-joint-word-condition), but the displayed comparisons do not turn it into a vanishing-kernel argument.
A further argument would need an additional bound on the relative position or overlap of \(q_n\) and \(P_n\) that improves (17) after normalization, or a separate kernel-preserving construction with a genuinely shrinking defect.
Neither is established here.
The retained estimates do not supply that additional overlap bound or shrinking construction.

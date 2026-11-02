---
author: Yin
---

# Normal-domain shortcuts: exact failures and remaining possibilities

Context: the actual canonical bounded-vector domain question for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
In the actual operator statements, (M,tau) is finite tracial with a faithful normal tracial state, H=L2(M,tau), and the derivations on their stated represented starred cores take values in the outer bimodule H tensor_2 H.
Adjoints are actual Hilbert adjoints, and inner products are linear in the second variable.
These are developer-checked obstructions to specific proposed mechanisms, not counterexamples to the general normal A-to-S implication or new independent project reviews.
The sharp-vacuum tests were developed and self-checked by the original authoring main agent on 2026-10-16; the rank computation records the branch agent's derivation and root's separate development-context check.
The source-applicability and actual-domain limits of the geometry and weighted-forcing tests are retained below.

## Haar-Poisson score and vacuum

Retain the actual [C_F0057 model](../claims/Yin_C_F0057_v1.md#statement), write its generators as U,V and target algebras as N=W*(U) and B=alg(U*V,(U*V)*).
Let m be Haar measure, let 0<r<1, and put

\[
w_r(e^{i\theta})=\frac{1-r^2}{1-2r\cos\theta+r^2},\qquad
f_r(e^{i\theta})=-\frac{w_r'(\theta)}{w_r(\theta)}
=\frac{2r\sin\theta}{1-2r\cos\theta+r^2}.
\]

Here f_r is a bounded real function for each fixed r, with trace zero.
Ordinary integration by parts on the circle gives

\[
\tau(f_r(V)V^l)=i l r^{|l|}\quad(l\in\mathbb Z).
\tag{T1}
\]

The actual scalar difference-quotient conjugate vector for V is \(\xi_V=V(1+i f_r(V))\).
Testing every Laurent monomial with (T1) gives its full scalar vacuum identity; the vector is bounded.
Its extension to the free reference core is the actual free-product conjugate vector of C_F0057's construction.

For completeness its scalar squared norm is

\[
\sigma_r^2:=\|f_r(V)\|_2^2=\frac{2r^2}{(1-r^2)^2}.
\tag{T3}
\]

This can be checked without importing a Fisher-information formula.
Write D=1-2r cos(theta)+r squared.
The Poisson Fourier series gives integral D inverse dm=(1-r squared) inverse and integral D to the power -2 dm=(1+r squared)/(1-r squared) cubed.
Differentiation of the first identity gives integral cos(theta) D to the power -2 dm=2r/(1-r squared) cubed.
Integration by parts gives integral f_r squared w_r dm=integral f_r' w_r dm.
Substituting the derivative of 2r sin(theta)/D then gives twice the left side equal to 2r(1-r squared) integral cos(theta) D to the power -2 dm, proving (T3).
All differentiations and integrations are between bounded smooth functions at fixed r<1.


## Sharp fixed-vacuum and degree-growth failures

Here P is the represented starred core of the C_F0057 model, delta its actual U-coordinate outer derivation, xi=delta^*(1 tensor 1), and T=delta^*( . tensor 1).
The weaker quadratic proposal permits an unspecified finite constant C in
\[
 \|T(a)\|_2^2\le C\|T(a^2)\|_2\qquad(a=a^*\in P). \tag{R1}
\]
The sharp scalar fixed-vacuum domination does not extend even to selfadjoint mixed tests in the existing correlated-unitary model.
Take the actual C_F0057 model: U Haar, V free from U with Poisson law of parameter \(0<r<1\), and target coordinates \((U,U^*V)\).
This tuple has bounded duals and actual starred-core conjugate variables.
For its U-coordinate derivative delta,
\[
 \delta U=1\otimes1,\qquad
 \delta V=1\otimes U^*V,\qquad
 \delta V^*=-V^*\otimes U^*.
\]
Write \(\xi=\delta^*(1\otimes1)\), \(T=\delta^*(\,\cdot\,\otimes1)\), and set
\[
 w=U^{-2}V^2,\qquad a=w+w^*=a^*,\qquad \|a\|\le2.
\]
The complete-square identity in [C_F0158 v2, equation (Q13)](../claims/Yin_C_F0158_v2.md#argument), and the actual adjoint pairing give
\[
 \operatorname{Re}\langle T(a^2),\xi\rangle-\|Ta\|_2^2
 =-\operatorname{Re}(\tau\otimes\tau)((a\otimes U)\delta a).
 \tag{R2}
\]
Indeed the right side is norm(a) in L2 squared minus Re<Ta,aU>, after expanding delta(aU).
The actual Leibniz calculation is
\[
 \delta a=-U^{-1}\otimes U^{-2}V^2
 +U^{-2}V\otimes U^{-1}V
 -V^{-1}\otimes U^{-1}V^{-1}U^2
 +V^{-2}U\otimes1.
\]
Only its second term survives the trace pairing in (R2).
Haar gauge invariance kills the other second-leg traces, and \(\tau(aU^{-2}V)=\tau(V^{-1})=r\).
Consequently
\[
 \operatorname{Re}\langle T(a^2),\xi\rangle-\|Ta\|_2^2=-r^2<0.
 \tag{R3}
\]
The displayed four-term proof supplies the mathematical evidence.
The counterexample concerns the stronger fixed-vector bound with vector xi and constant one.
It neither refutes (R1) with an unspecified finite constant nor either endpoint estimate: these unitary coordinates already have bounded duals.
It also persists on strictly positive tests.
Since T1=xi, the defect \(\operatorname{Re}\langle T(a^2),\xi\rangle-\|Ta\|_2^2\) is unchanged under \(a\mapsto a+c1\) for real c, by expansion of both sides.
Thus \(b=3+w+w^*\ge1\) has exactly the same negative defect \(-r^2\).
In fact C_F0158 v2 implies the always valid unitary bound
\[
 \|Ta\|_2^2\le2\operatorname{Re}\langle T(a^*a),\xi\rangle,
\]
because adding the nonnegative term norm(a) in L2 squared to its completed-square identity replaces the vector 2xi-U by 2xi.

The same family also tests whether increasing mixed-word degree can make the obstruction diverge for one fixed actual law.
Let \(w_n=U^{-n}V^n\), \(a_n=w_n+w_n^*\), and \(n\ge1\).
The normalized U-coordinate vacuum in this model is
\[
 \xi=h(V)U,\qquad h=1+\mathrm i f_r,\qquad
 \|\xi\|_2^2=1+\frac{2r^2}{(1-r^2)^2},
\]
where the actual Poisson score f_r, its moments and its squared norm are retained in [the score calculation above](#haar-poisson-score-and-vacuum).
To check the target normalization, let E_U,E_V be the vacuum-normalized bounded canonical contractions of the free reference pair.
C_F0057's change of coordinates gives
\[
 E_A=E_U+E_V\rho(U^*V)-\rho(U^*),\qquad
 E_A^*1=\xi_VV^*U=h(V)U.
\]
The subtracted right multiplier is necessary because the unnormalized changed dual sends 1 to U*.
The actual adjoint formula and the same derivative expansion give
\[
 Ta_n=U^{-n}\left(V^nh(V)+\sum_{j=1}^{n-1}r^jV^{n-j}\right)U
       +V^{-n}U^nh(V)U.
 \tag{R4}
\]
The two displayed terms are orthogonal by Haar gauge invariance.
Put \(s_n=\sum_{j=1}^{n-1}r^jV^{n-j}\).
The identities \(\tau(h^*V^{-j})=(1-j)r^j\) and \(\|s_n\|_2^2=\sum_{j=1}^{n-1}(2j-1)r^{2j}\) show
\[
 \|Ta_n\|_2^2=2\|\xi\|_2^2+\sum_{j=1}^{n-1}r^{2j},
 \qquad
 \operatorname{Re}\langle T(a_n^2),\xi\rangle=2\|\xi\|_2^2.
 \tag{R5}
\]
For the second equality, (R2) applies to a_n; its surviving trace terms give the negative of the same geometric sum.
Also \(\langle Ta_n,\xi\rangle=0\) by gauge invariance.
Hence the strictly positive \(b_n=3+a_n\ge1\), of norm at most five, has
\[
 \|Tb_n\|_2^2=11\|\xi\|_2^2+\sum_{j=1}^{n-1}r^{2j},
 \qquad
 \operatorname{Re}\langle T(b_n^2),\xi\rangle=11\|\xi\|_2^2.
 \tag{R6}
\]
The sum is bounded by \(r^2/(1-r^2)\) for every fixed r.
Thus this degree-growth attempt does not furnish an unbounded canonical map for a single actual-A tuple.
Allowing r to approach one changes the tuple and makes its actual vacuum norm diverge faster than this defect; that family limit cannot be presented as a full-domain counterexample.


## Geometry and joint gluing

The original applicability check concerns Tol17 arXiv v2, Theorems 1.1 and 1.3 on pp.3--5, and Leg99's published Theorem 0.1 on p.831 and Proposition 1.2 on pp.835--836.
These are statement/applicability checks, not original-proof audits; the [Tol17](../audits/literature/Tol17/readme.md) and [Leg99](../audits/literature/Leg99/readme.md) notes own their exact source scopes.

1. **David–Léger is not an arbitrary-measure finite-curvature theorem.**
   Its principal statement uses H1 on a finite-length set.
   Its quantitative measure proposition keeps normalized mass, uniform linear growth and growth-dependent curvature smallness.
   Arbitrary actual scalar ACSY laws need not be arc-length measures; the planar scalar example already fixed in C_F0140 has zero one-dimensional density.
   This is an actual admissible example outside the rectifiability premise, although C_F0078 separately handles its planar growth.

2. **The additional Tolsa hypotheses remain additional.**
   Theorem 1.1 requires positive upper linear density and a density square-function condition.
   Theorem 1.3 requires uniform linear growth and uniform tests over all squares.
   Existing A-to-finite-curvature reasoning does not verify these tests.
   Tol17-U001's selected curvature identity also keeps linear growth; TV06-U001 retains square-integrability of maximal linear density.
   None is an implication from the supplied actual vacuum alone to the correlated lower form.
   This does not assert that every missing scalar hypothesis is false under A; it identifies what the proposed invocation has not proved.

3. **Geometry class and quantitative gluing are distinct.**
   A rectifiable piece is not automatically an analytic closed curve or a C3 spectral graph at the hypotheses of the accepted correlated geometry results.
   A zero-linear-density conclusion, if obtained from some further decomposition theorem, would not itself give a power bound with exponent greater than one.
   No checked theorem upgrades all pieces to C_F0078's precise exponent and no summable estimate for their domain constants has been supplied.
   In particular, C_F0143 is already an actual countable union of analytic circles with scalar vacua and finite total curvature; its auxiliary absolute contraction norm is unbounded and its fourth curvature power diverges.
   Merely listing good geometric pieces does not justify an absolute-norm gluing argument.

There is also an independent joint-algebra obstruction even if a satisfactory scalar decomposition were granted.
A spectral piece e=1_E(Z) belongs to W*(Z), but need not be central in the full correlated algebra.
Consequently:

- weighting the joint state by a positive bounded marginal density w generally destroys the trace.
  Indeed tau(wab)-tau(wba)=tau((wa-aw)b); vanishing for every a,b forces w central by faithfulness and the L2 pairing.
  The scalar positive-measure weighting argument therefore does not create a new tracial joint law for free;
- passing to eMe keeps a trace, but compression of another normal coordinate need not stay normal, and no theorem here proves inheritance of the original represented ACSY derivatives.
  The Borel projection e itself need not belong to the original star core or to any required derivative graph;
- estimates confined to the diagonal pieces epe do not control the off-diagonal pieces epf or the mixed-word derivative terms.
  The curvature kernel also contains triples with points in distinct scalar pieces, and its actual joint-vacuum measure is not determined by the marginal geometric decomposition.

These are failures of the proposed transfer, not counterexamples to A-to-S.
For example, the elementary fact that a compression of a normal operator can be nonnormal is only an algebraic warning here, not a claimed finite-dimensional ACSY model.
A legitimate reconstruction would need actual projection/multiplier graph rules, a trace-compatible treatment of the correlated coordinates, and a summable bound for cross-piece mixed quadratic terms involving the joint vacuum.

Finally, C_F0057 fixes both marginal laws to a single smooth Haar circle while its mixed negative quadratic form becomes arbitrarily negative across the correlated family.
Thus even the strongest regularity of those fixed marginals cannot supply a lower bound depending only on scalar geometry.
A possible successful estimate must still use joint data, as the square-root-vacuum question does.
None of the checked geometric statements supplies that missing joint term.

**Branch stopping conclusion.**
No usable theorem or completed reduction to full normal A-to-S was obtained from these source interfaces.
The precise unproved bridge is a joint, actual-domain gluing/lower-form estimate; a scalar rectifiability conclusion alone is insufficient.

## Scalar square-root multiplier failure

For masses m_i on three points, the symmetric jump operator is (L_g f)_i=sum_j m_j g_ij(f_i-f_j).
The proposed shortcut factors it through its positive square root L_b=sqrt(L_g) and seeks a universal pointwise bound for (z_i-z_j)b_ij.

The branch account records root's exact computation and a separate development-context recheck; no independent project finding is claimed.
Take three equilateral locations of curvature c, masses (t,t,r), r=1-2t and 0<t<1/2.
Their curvature kernel is g_12=r c squared and g_13=g_23=t c squared.
The scalar jump generator L_g has nonconstant eigenvectors
\[
 f_a=(1,-1,0),\quad\lambda_a=3tr c^2,
 \qquad
 f_s=(1,1,-2t/r),\quad\lambda_s=t c^2.
\]
The associated orthogonal projections on weighted L2 have ordinary matrix entries (P_a)_12=-1/2 and (P_s)_12=r/2.
These follow directly from ||f_a|| squared=2t and ||f_s|| squared=2t/r.
Consequently the symmetric kernel b for L_b=sqrt(L_g) has
\[
 b_{12}=-\frac{(\sqrt{L_g})_{12}}{m_2}
       =\frac{c(\sqrt{3r}-r)}{2\sqrt t}.
 \tag{U11}
\]
For a fixed equilateral triangle, |z_1-z_2| b_12 diverges as t tends to zero.
Thus the scalar square-root factorization used in this shortcut cannot provide a universal pointwise multiplier estimate ||(z-v)b||infinity.
This is not an actual joint-vacuum counterexample: the vector zeta may have additional constraints, and the calculation neither disproves a bound for S_b zeta in a realized normal law nor refutes the desired lower quadratic form.
The positive Gaussian correction in C_F0153 illustrates a mechanism bypassing this scalar-kernel obstruction.



## Rank obstruction for real and imaginary coordinates


The normal actual-vacuum assumptions and phase formula are those of [C_F0076, assertion 1](../claims/Yin_C_F0076_v1.md#statement).
Set \(A_i:=(X_i+X_i^*)/2\), \(B_i:=(X_i-X_i^*)/(2\mathrm i)\), and \(\partial_i^\#(a):=(\partial_i(a^*))^\dagger\).
The spectral law of X_i is diffuse, and the bounded coarse coefficient
\[
 k_i(z,w):=\frac{\bar z-\bar w}{z-w}
\]
has modulus one almost everywhere for the product spectral measure.
The two derivations take the following values on the two selfadjoint coordinates:
\[
 \begin{pmatrix}
  \partial_i A_i&\partial_i B_i\\
  \partial_i^\# A_i&\partial_i^\# B_i
 \end{pmatrix}
 =
 \begin{pmatrix}
  (1+k_i)/2&(1-k_i)/(2\mathrm i)\\
  (1+\bar k_i)/2&(\bar k_i-1)/(2\mathrm i)
 \end{pmatrix}.
\]
Here all entries belong to the commutative spatial tensor algebra generated by the two spectral copies of X_i.
Its second row is \(\bar k_i\) times its first row, and its determinant is \((|k_i|^2-1)/(2\mathrm i)=0\).
Thus this coordinate matrix has rank one almost everywhere and has no inverse even as a measurable matrix.
Taking invertible scalar combinations of the two derivations, including their realification, does not change this rank.

The obstruction also follows directly from the represented relation \([A_i,B_i]=0\).
A putative coordinate derivation with values \(\nabla A_i=1\otimes1\) and \(\nabla B_i=0\) would force \(1\otimes B_i-B_i\otimes1=0\), hence B_i scalar.
A second one with the reversed coordinate values would force A_i scalar.
Both cannot hold for the diffuse X_i under consideration.
Consequently one cannot replace the tuple by its 2d real and imaginary parts and invoke a theorem for 2d independent selfadjoint free difference quotients.
Choosing regions where either 1+k_i or 1-k_i is invertible selects one local direction; it does not provide the missing independent direction or remove the mixed defect already recorded above.
This rules out only this inverse-coordinate shortcut, not A implies S.
The branch agent supplied the matrix computation and root separately checked its entries, determinant and represented-relation argument; it remains a development finding without a new Claim acceptance.


## Weighted forcing and the uniform-trace shortcut

For the affine matrix L=A_0 tensor 1+sum_{i=1}^d A_i tensor X_i at issue, p denotes its kernel projection, C=(id tensor tau)(p), and B=sum_{i=1}^d A_i C A_i^*.
The positive compressed inverse Q and its minimum-norm solution criterion are those of [C_F0154](../claims/Yin_C_F0154_v1.md#statement); the scalar example below defines Q_t explicitly.

The small compression must also be compared with the actual right-hand side.
If p a=a and C=(id tensor tau)p, then for each scalar column v,

\[
 |v^*\tau(a)|=|\tau((p v)^*a)|
 \le(v^*Cv)^{1/2}\|a\|_{H^m}
 \le(v^*Cv)^{1/2}\|a\|_{M_{m,1}(M)}.
 \tag{124}
\]

Finite-dimensional Hilbert duality thus gives tau(a)=C^(1/2)b with ||b||<=||a||_column, using the inverse only on the support of C.
For B=sum_i A_i C A_i*>0, each B^-1/2 A_i C^1/2 is a contraction.
The affine forced vector A_i tau(a) therefore belongs to the B^1/2 ellipsoid of the same radius.
The actual polar solution in C_F0154 has the refined bound

\[
 \|z\|_2^2\le
   \|a\|_{\rm column}^2\,
   \operatorname{Tr}_n\bigl((\mathrm{id}\otimes\tau)(Q^{-1})B\bigr).
 \tag{125}
\]

Indeed write A_i tau(a)=B^1/2 c with ||c||<=||a||_column and apply the positive trace bound to c* B^1/2 (id tensor tau)(Q^-1) B^1/2 c.
The same argument applies to the nonzero compressed block of C_F0155.
This bound is finite for each fixed block by C_F0154.
It retains some forcing information, but the next calculation shows that a uniform bound on this sufficient weighted trace is not a necessary consequence of A or F.

### A law with divergent sufficient trace and controlled actual forcing

This diagnostic uses existing exact scalar interfaces, not a new source search.
Let M=L-infinity(mu), X(x)=x, with

\[
 d\mu(x)=\frac38|x|^{-1/4}1_{\{|x|<1\}}\,dx.
 \tag{126}
\]

The density integrates to one and belongs to L3 of Lebesgue measure.
[Voi98-U002, Proposition 3.5](../audits/literature/Voi98/Yin_U002.md#proposition-35-scalar-hilbert-transform-realization) supplies the actual L2 conjugate variable for this compactly supported selfadjoint law.
Thus A holds on its represented star core.
The adopted [C_F0055 scalar estimate](../claims/Yin_C_F0055_v1.md#statement) then gives the full canonical forward domain and F; its scalar hypotheses are exactly compact support, no atoms and the actual vacuum, all satisfied here.
Neither source asserts bounded density, and none is used.

For L_t=[X,t], put Q_t=X^2+t^2 and U_t=tau(Q_t^-1).
Direct substitution x=t y gives

\[
 U_t\asymp t^{-5/4},\qquad
 B_t=t^2U_t,\qquad
 U_tB_t=t^2U_t^2\asymp t^{-1/2}\longrightarrow\infty.
 \tag{127}
\]

Here f(t) asymp g(t) means their ratio is bounded above and below by positive constants for small t.
For the first comparison the rescaled integral tends to the positive finite integral of |y|^-1/4/(1+y^2) on the real line.
Thus the sufficient constant on the right of (125) cannot have a uniform bound even in an example with both A and F.

The exact forcing is smaller than the covariance ellipsoid bound.
In this commutative model every bounded kernel column is a=(t b,-Xb), and its operator column norm is at most one exactly when |b|<=Q_t^-1/2 almost everywhere.
Its forced scalar is tau(a_1)=t tau(b).
The largest possible absolute value is attained by b=Q_t^-1/2, which is bounded for each t>0.
Another rescaling gives

\[
 I_t:=\tau(Q_t^{-1/2})\asymp t^{-1/4},\qquad
 \sup\{ |\tau(a_1)|:L_ta=0,\ \|a\|_{\rm column}\le1\}
       =t I_t\asymp t^{3/4}.
 \tag{128}
\]

The rescaled integrand is |y|^-1/4/sqrt(1+y^2), integrable at zero and infinity.
For a fixed scalar c, the minimum Hilbert norm squared among solutions Xz_1+t z_2=-c is |c|^2 U_t: pointwise Cauchy--Schwarz gives the lower bound, and z=(-c X/Q_t,-c t/Q_t) attains it.
Consequently the worst minimum squared norm over the unit bounded kernel columns is exactly

\[
 t^2 I_t^2 U_t\asymp t^{1/4},
 \tag{129}
\]

which stays bounded and tends to zero.
This does not refute a uniform estimate sensitive to the full bounded-column geometry.
It shows why replacing the attainable forcing set by its C^1/2 ellipsoid, and then by the weighted trace in (125), loses information needed for that route.
The general finite-to-global implication remains open.

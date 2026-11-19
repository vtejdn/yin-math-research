---
author: Yin
---

# Discrete borders and matrix-evaluation residues for Wigner pencils

The 19 November 2026 exploration for [F0012](../tasks/Yin_T_F0012_v3.md#contract) tests replacements for the continuous small-ball steps in [Han's tensor-pencil argument](../audits/literature/Han26b/Yin_U001.md#han26b-u001).
Yin's main research agent and three bounded delegates derived the tests below.
They concern the original independent signs, except for explicitly identified deterministic algebraic witnesses.
The general summable terminal estimate remains open.
The [cyclic cutoff theorem](../claims/Yin_C_F0359_v2.md#clip) already controls the logarithms above every fixed polynomial cutoff; the unresolved target is its [integrated terminal loss](../claims/Yin_C_F0359_v2.md#equivalence).

<a id="density-obstructions"></a>
## Two failures of a direct density replacement

Let
\[
 A_1=2^{-1/2}\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad A_2=2^{-1/2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
They generate \(M_2(\mathbb C)\), both are invertible, and \(\sum_jA_jA_j^*=I_2\).
Nevertheless
\[
 \det(I+xA_1+yA_2)=1-(x^2+y^2)/2
\]
vanishes at every pair of independent fair signs, while the ambient gradient has norm \(\sqrt2\).
Thus irreducibility and a positive coefficient Gram do not imply a discrete relative-gradient estimate.
This finite conditional-statistic example does not refute an asymptotic Wigner assertion.

Replacing the derivative by Boolean differences does not suffice either.
For \(q\) independent signs and \(0<\delta<1\), put \(f_\delta=\delta+1+\prod_{i=1}^q\epsilon_i\).
Every one-bit flip changes its value by modulus two, but \(\Pr\{|f_\delta|=\delta\}=1/2\).
Each variable has degree one.
The number and size of these pivots therefore do not make the lower tail small.
The [earlier parity test](../drafts/Yin_D_F0044.md#squarefree) already rules out multiplying conditional success probabilities over disjoint fibers.

There are two separate interfaces to replace in the continuous proof.
Its bounded anchor sets give powers of the radius from a density; a fixed set of signs instead has atoms bounded below independently of that radius.
Even a separately established punctured-row frame would still leave the relative-gradient-to-probability step, which the first example disproves under its purely geometric hypotheses.

<a id="fresh-border"></a>
## What a conditional sign completion would provide

Fix an old physical block of a matrix-coefficient affine pencil of coefficient size \(m\), and append \(h\) physical sites.
Keep the final-size normalization fixed.
For any square determinant minor \(f\), its degree in all fresh raw variables is at most \(2mh\), independently of the old size.
Indeed a variable entry touches a new row or column, and a determinant term uses at most \(mh\) new rows and \(mh\) new columns.
Repeated appearances of one symmetric edge do not alter this degree bound.

Reduce \(f\) modulo \(\epsilon_e^2=1\), and suppose it is not identically zero on the fresh sign cube.
Write its Walsh expansion as \(\sum_Sc_S\epsilon_S\), choosing a nonzero coefficient of maximal degree.
No strict superset of this \(S\) occurs.
After conditioning on every fresh sign outside \(S\), its \(S\)-coefficient remains \(c_S\), so
\[
 2^{-|S|}\sum_{\epsilon_S}\epsilon_Sf(\epsilon)=c_S.
\]
At least one assignment on every such fiber has \(|f|\ge |c_S|\).
Consequently
\[
 \Pr\{|f|\ge |c_S|\mid\text{old block}\}\ge2^{-|S|}\ge2^{-2mh}.
 \tag{1}
\]
The minor and its coefficient can be selected measurably from the old data, with a fixed ordering for ties.
An actual conditional completion witness thus gives a positive one-step probability independent of the old dimension.
It gives no lower bound on \(|c_S|\).
The [global sign-support construction](../claims/Yin_C_F0354_v1.md#statement) supplies neither this conditional completion witness nor its coefficient size.

A single fresh border can miss the left and right kernels simultaneously.
For
\[
 D=\begin{pmatrix}1&1\\-1&-1\end{pmatrix},\qquad x\in\{-1,1\}^2,
\]
one has \(\det\left(\begin{smallmatrix}D&x\\x^{\mathsf T}&d\end{smallmatrix}\right)=x_1^2-x_2^2=0\) for every \(d\), and the enlarged rank is exactly two.
For \(h\) independent sign columns \(X\), \(t\ne0\), and \(s=\sum_{a=1}^hX_{1a}X_{2a}\), Schur complementation gives
\[
 \det\begin{pmatrix}D&X\\X^{\mathsf T}&tI_h\end{pmatrix}
 =t^{h-2}(h^2-s^2).
 \tag{2}
\]
Thus oversampling repairs this particular cancellation with probability \(1-2^{1-h}\).
It does not prove a conditional completion theorem for general Wigner exteriors.

Nor can successive rank gains be assumed to persist on every supported completion.
For a symmetric Sylvester Hadamard matrix \(H_N\), \(N=2^r\ge2\), put \(W=H_N/\sqrt N\).
The supported sign tuple has \(W^2=I\), and the fixed monic pencil
\[
 L(W)=\begin{pmatrix}I&W\\W&I\end{pmatrix}
\]
has corank \(N\).
After deleting one physical site, write \(W=\left(\begin{smallmatrix}W_0&b\\b^{\mathsf T}&d\end{smallmatrix}\right)\).
Then \(W_0^2+bb^{\mathsf T}=I\), \(W_0b=-db\), and \(d=\pm N^{-1/2}\).
On \(b^\perp\), \(W_0\) has eigenvalues in \(\{-1,1\}\); on \(b\) its eigenvalue is \(-d\).
Hence \(L(W_0)\) has corank \(N-2\), and the supported final border increases corank by two.
This rare example uses sign diagonals and excludes only deterministic persistence on all supported exteriors.
An averaged drift or a typical-exterior argument remains possible.

<a id="matrix-detector"></a>
## An invertible detector invisible to commuting substitutions

Take
\[
 A=E_{12}+E_{23},\qquad B=E_{21}-E_{32}.
\]
The generated algebra is \(M_3(\mathbb C)\): \(A^2=E_{13}\), \(B^2=-E_{31}\), their products give \(E_{11}\) and \(E_{33}\), and multiplication by \(A,B\) then gives every matrix unit.
Yet
\[
 \det(zI_3-xA-yB)=z^3
 \tag{3}
\]
for commuting scalar \(x,y\).
Such substitutions have no variable poles at any fixed \(z\ne0\).

Use the real symmetric two-dimensional evaluation
\[
 X=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 Y=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 K=XY=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 Q=A\otimes X+B\otimes Y.
\]
These matrices are algebraic witnesses, not modified samples of the Wigner model.
For arbitrary square \(X,Y\), eliminating the two outside channels gives the polynomial identity
\[
 \det(zI_{3N}-A\otimes X-B\otimes Y)
 =z^N\det(z^2I_N-(YX-XY)).
 \tag{4}
\]
At the displayed witness, the nonzero eigenvalues are \(\pm(1+i),\pm(1-i)\), each simple, and zero has multiplicity two.
In particular
\[
 Q^4=\begin{pmatrix}-2I&0&2K\\0&-4I&0\\-2K&0&-2I\end{pmatrix},
 \qquad
 \operatorname{Tr}_2(-Q^4/4)=\operatorname{diag}(1,2,1).
\]
The partial trace is unnormalized.
Summing all nonzero residues gives this invertible raw-resolvent detector, but an individual residue is needed below.

Fix \(\lambda=1+i\).
Let \(v=(1,-i)^{\mathsf T}\), \(\ell=(1,i)\), and
\[
 r=(Xv/\lambda,v,-Yv/\lambda)^{\mathsf T},\qquad
 l=(\ell Y/\lambda,\ell,\ell X/\lambda).
\]
Direct multiplication gives \(Qr=\lambda r\), \(lQ=\lambda l\), and \(lr=4\).
Thus \(P_\lambda=rl/4\) is its spectral projector.
The physical trace with the antisymmetric matrix \(K\) is
\[
 F_{ab}=\operatorname{Tr}_2(K(P_\lambda)_{ab}),\qquad
 F=\frac14\begin{pmatrix}i&0&1\\0&-2i&0\\-1&0&i\end{pmatrix}.
\]
The decisive auxiliary identity is
\[
                    BFA-AFB=\frac{i}{2}I_3.                  \tag{5}
\]

<a id="physical-detector"></a>
## The detector survives the actual Schur symmetry

Write \(R_z=(zI-A\otimes x-B\otimes y)^{-1}\).
For two fresh physical columns \(u,v\), the quadratic Schur term is
\[
 (A\otimes u^{\mathsf T}+B\otimes v^{\mathsf T})
 R_z(A\otimes u+B\otimes v).
\]
For its auxiliary entry \(a,b\), let
\[
 \mathscr M_{ab,z}=
 \begin{pmatrix}
 (AR_zA)_{ab}&(AR_zB)_{ab}\\
 (BR_zA)_{ab}&(BR_zB)_{ab}
 \end{pmatrix}.
\]
Only the transpose-symmetric part of this physical/color matrix is observed by the quadratic form in \(g=(u,v)\).
At the witness use
\[
 H=\begin{pmatrix}0&K\\-K&0\end{pmatrix},\qquad H^{\mathsf T}=H.
\]
Its diagonal is zero.
The functional therefore ignores diagonal-square contributions, and
\[
 \operatorname{Tr}_4(H\,\operatorname{sym}\mathscr M_{ab,z})
 =\operatorname{Tr}_2(K(BR_zA-AR_zB)_{ab}).
 \tag{6}
\]
Thus the antisymmetric physical test is retained through the symmetric cross-color observation.
The ordinary physical trace would miss the middle auxiliary direction.

Substitute \(x=tX,y=tY\), where the complex variable \(t\) is only a test of rational identities.
Then
\[
 \operatorname*{Res}_{t=z/\lambda}(zI-tQ)^{-1}=-P_\lambda/\lambda.
\]
For \(z\ne0\), applying \(-\lambda\) times this residue to (6) gives \(iI_3/2\).
It gives zero on scalar physical kernels and on every other node \(w\) when
\[
                 w/z\notin\{1,-1,i,-i\}.                    \tag{7}
\]
Require this for distinct members of the complete node list, including conjugates.
The excluded choices form a finite union of measure-zero real algebraic sets.

For clarity, any linear relation among the actual rational kernels modulo scalar kernels remains valid under the finite matrix substitution.
At \(t=z/\lambda\), the other nodes and scalar kernels are regular.
The residue therefore annihilates the relation and pairs its \(z\)-coefficient with \(iI_3/2\).
Finite-dimensional annihilator duality puts this node-supported matrix in the coefficient image of the joint kernel quotient, exactly as in the [joint-node argument](../claims/Yin_C_F0363_v4.md#quotient).
Complex relations can be realified by retaining the conjugate nodes.
The explicit functional supplies an algebraic detector; it does not itself give a random physical projection estimate.

The companion (4) reduces to a skew-self-adjoint commutator, whose spectral problem is already covered by thin-support methods.
Accordingly this is a positive test of the matrix-evaluation mechanism, not a new Brown-convergence class.
In particular the example does not prove that every irreducible pencil has such a legal detector.
For a general cyclic realization the [compatible trims and selected-volume conditions](../strategies/Yin_S_F0035.md#the-full-polynomial-as-one-spectral-problem) still need verification.

<a id="joint-covariance"></a>
## A precise covariance test before arithmetic estimates

There is an existing discrete input for oversampling a subspace measurable in an old block: [independent testing of both near-kernels](../claims/Yin_C_F0196_v5.md#restricted-small-ball).
For signs its \(k\)-column failure probability is at most \(4e^{-ck}\) when the two tested dimensions are at most a sufficiently small fixed multiple of \(k\).
The same fresh columns may be used on both sides.
Taking \(k\ge C(r_L+r_R+M\log N)\) gives any prescribed polynomial failure rate.
It must not be applied to a subspace depending on those same columns.

For a real symmetric old matrix \(B_0\) and an old-measurable complex orthonormal frame \(Q_0\), the paired observations of one raw sign column have coefficient matrix
\[
 T=\begin{pmatrix}Q_0^*\\Q_0^*B_0\end{pmatrix},\qquad
 TT^*=\begin{pmatrix}
 I&Q_0^*B_0Q_0\\Q_0^*B_0Q_0&Q_0^*B_0^2Q_0
 \end{pmatrix}.
\]
The Schur complement of the first identity block is exactly
\[
 Q_0^*B_0(I-Q_0Q_0^*)B_0Q_0
 =\big((I-Q_0Q_0^*)B_0Q_0\big)^*
   \big((I-Q_0Q_0^*)B_0Q_0\big).                             \tag{8}
\]
Writing \(C=Q_0^*B_0Q_0\), block triangular factorization shows that a lower bound \(\kappa^2I\) in (8) gives
\[
 TT^*\succeq \frac{\min(1,\kappa^2)}{(1+\|C\|)^2}I.
\]
Conversely a lower bound for \(TT^*\) gives one for (8) by testing vectors \((-Cu,u)\).
Whitening followed by the existing independent-column estimate therefore controls these joint observations once their old-block transverse singular values are controlled.
If \(B_0\) preserves \(\operatorname{ran}Q_0\), the covariance is singular, regardless of how many fresh columns are sampled.
One must quotient actual dependencies or select fewer directions.

For the [quartic border](Yin_L_F0070_v1.md#quartic), the relevant old maps include \(Y_0\) and \(X_0^2\).
The initial two trims and joint projected volumes remain open.
A commutator spectral gap for several old colors would bound aggregate leakage of a small subspace, but aggregate Hilbert--Schmidt leakage does not give the least transverse singular value for one specified map.
Nor can a color absent from the actual border be inserted as fresh determinant randomness.

<a id="continuation"></a>
## Selected continuation and search limits

The selected test is to carry (5)--(7) through an actual independent-panel polarization and a selected-volume Schur restoration, with every space measurable before its fresh signs are exposed.
Then test finite matrix residues for a genuinely unresolved repeated-variable polynomial whose commuting specialization vanishes, such as \([x,y]x\).
The separate quartic test should first establish or refute the transverse covariance and initial-trim requirements in (8), rather than repeat an unconditioned Gram-energy calculation.
The bounded fresh-border degree in (1) is useful only after a quantitative conditional completion coefficient and an amplification mechanism have been exhibited.
Neither per-fiber success nor deterministic corank monotonicity supplies that mechanism.

A second, conditional arithmetic route is retained in the [rectangular small-ball source inspection](../audits/literature/RV09/Yin_U001.md).
Its subspace least-common-denominator condition would have to be proved for the joint, decoupled Schur coefficients on the original law; no such assertion is established here.
The oversampled old-measurable subspace bound above is already available and should be used whenever its exposure and covariance hypotheses fit.

Public searches on 19 November used “random Kronecker matrices least singular value Bernoulli matrix coefficients linearization polynomial”, “free semicircular rectangular linear matrix invertibility strict Hall expansion spectral gap”, and “random Wigner matrices quantum expander commutator spectral gap Bernoulli”.
The tensor-pencil searches returned Han's density result and scalar iid invertibility results; their inspected scope supplies no direct discrete tensor-pencil application.
The quantum-expander lead [Lancien--Youssef, arXiv:2302.07772v4](https://arxiv.org/abs/2302.07772v4) concerns random Kraus operators and is retained as a possible source of expansion ideas.
Its Wigner-reflected, exposure-compatible applicability has not been verified, and no commutator-gap theorem from it is used.
This bounded search does not assert that a general discrete result is absent from the literature.

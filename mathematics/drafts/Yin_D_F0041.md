---
author: Yin
---

# Rank-one pole algebra for the two-sided product and its stable-background boundary

This development concerns the real-input finite-fourth-moment branch of \(AB+2BA-zI\), for fixed \(z\ne0\).
It complements the [physical distance average](../claims/Yin_C_F0196_v1.md#companion-average) and the [complete same-row quartic interface](../ledger/Yin_L_F0066_v19.md#two-sided-quartic-first-obligation).
The argument below has been checked during development but has not received independent review or Claim adoption.
It proves raw polynomial nonvanishing and quantitative coefficient bounds, not an original-law small-ball estimate.

<a id="rank-one-graph-polynomial"></a>
## A uniformly nonzero rank-one graph polynomial

Let \(A,B\) be linear maps on \(\mathbb C^n\), with \(\|A\|,\|B\|\le K\), and let \(u,r\in\mathbb C^n\).
For commuting coordinate variables \(x,y\), define
\[
 Q_{A,B,u,r,z}(x,y)
 =[(Ar)^Ty+2(Br)^Tx][x^TBu+2y^TAu]
  +z[(r^Tx)(u^Ty)+2(r^Ty)(u^Tx)].
 \tag{Graph-quadratic}
\]
Write it uniquely as \(x^TS_{xx}x+x^TM_{xy}y+y^TS_{yy}y\), with symmetric pure blocks.
These blocks are
\[
 S_{xx}=(Br)(Bu)^T+(Bu)(Br)^T,
 \qquad S_{yy}=(Ar)(Au)^T+(Au)(Ar)^T,
\]
\[
 M_{xy}=(Bu)(Ar)^T+4(Br)(Au)^T+z(ru^T+2ur^T).
 \tag{Graph-coefficients}
\]
For each fixed \(K\) and nonzero \(z\), there is \(c(K,z)>0\), independent of \(n\), such that
\[
 (\|S_{xx}\|_F^2+\|M_{xy}\|_F^2+\|S_{yy}\|_F^2)^{1/2}
 \ge c(K,z)\|u\|\|r\|.
 \tag{Uniform-graph-coefficient}
\]
No joint-gap assumption or symmetry of the two maps is required for this algebraic assertion.
The relation between this polynomial and the Wigner companion below uses real symmetric matrices.

Assume first that both roots are nonzero and that the polynomial vanishes.
For complex vectors \(v,w\), the identity \(vw^T+wv^T=0\) implies that one vector is zero.
Indeed, if \(v_i\ne0\), the diagonal entry forces \(w_i=0\), and the entries in that row then force every coordinate of \(w\) to vanish.
Consequently \(S_{xx}=0\) implies \(Br=0\) or \(Bu=0\), and \(S_{yy}=0\) implies \(Ar=0\) or \(Au=0\).
If both images of the same root vanish, the mixed block is \(z(ru^T+2ur^T)\), which is nonzero.
If \(u,r\) are independent, this last matrix has rank two, since its representation on the two root spans has an invertible off-diagonal coefficient matrix.
If they are proportional, it equals a nonzero multiple of \(uu^T\).

In either remaining crossed case, vanishing of the mixed block requires a matrix of rank at most one to equal \(-z(ru^T+2ur^T)\).
Independent roots therefore give a contradiction.
For proportional roots \(r=\lambda u\), the crossed zero-image conditions force both corresponding images to vanish, again leaving the nonzero mixed root term.
This proves nonvanishing.

For the uniform estimate, normalize both root norms to one.
Only the six vectors \(u,r,Au,Ar,Bu,Br\) enter the coefficient blocks, and their norms are bounded in terms of \(K\).
Their Hermitian Gram matrices form a compact set after taking closure.
Represent a convergent Gram sequence by columns of its positive square roots in \(\mathbb C^6\).
This preserves the Frobenius norms of the displayed tensor expressions, since the identifications on the vector spans are isometries and the tensors transform by congruence.
The inequalities
\[
 \|aAu+bAr\|\le K\|au+br\|,
 \qquad \|aBu+bBr\|\le K\|au+br\|
 \quad(a,b\in\mathbb C)
\]
pass to the limit.
They ensure that the limiting images define bounded linear maps on the span of the limiting roots, extended by zero on its orthogonal complement.
A sequence with coefficient norm tending to zero would therefore give two unit roots and two bounded maps whose graph polynomial vanishes, contradicting the preceding algebra.
Homogeneity in the two roots proves (Uniform-graph-coefficient).
This proof uses only elementary finite-dimensional rank and compactness, without a probabilistic or source-theorem premise.

<a id="exact-companion-pole"></a>
## Exact companion elimination and the ideal pole formula

Now take real symmetric \(A,B\), write \(M=AB+2BA-zI\), and assume \(M\) invertible.
For its physical principal companion \(Q\), direct elimination gives
\[
 Q^{-1}=T M^{-1}U+\operatorname{diag}(0,-I,-I),
 \qquad T=\begin{pmatrix}I\\B\\A\end{pmatrix},
 \quad U=\begin{pmatrix}I&A&2B\end{pmatrix}.
 \tag{Companion-inverse-identity}
\]
Use the same fresh real row vectors \(x,y\) in the two original inputs, and initially set the exposed diagonal coordinates to zero.
The Schur matrix is exactly
\[
 S=D+3(x^Ty)E_{11}-V M^{-1}W,
 \qquad D=\operatorname{diag}(-z,-1,-1),
\]
\[
 V=\begin{pmatrix}x^TB+2y^TA\\y^T\\x^T\end{pmatrix},
 \qquad W=\begin{pmatrix}Ay+2Bx&x&2y\end{pmatrix}.
 \tag{Physical-Schur-pole}
\]
In the formal rank-one specialization \(M^{-1}=qur^T\), put
\[
 C_2(x,y)=(r^Tx)(u^Ty)+2(r^Ty)(u^Tx).
\]
The rank-one determinant formula gives the exact identity
\[
 \det S=-z+3x^Ty-qQ_{A,B,u,r,z}(x,y)
                    +3q(x^Ty)C_2(x,y).
 \tag{Ideal-pole-determinant}
\]
This is a specialization of the algebraic formula, not an assertion that an inverse of dimension greater than one actually has rank one.

For original normalized independent real rows with finite fourth moments, bounded root norms imply
\[
 \mathbb E|x^Ty|^2=O(N^{-1}),\qquad
 \mathbb E|C_2(x,y)|^2=O(N^{-2}).
\]
Each term of \(C_2\) is a product of one linear form in each independent row; the displayed second-moment bound follows from independence and the covariance normalization.
Cauchy--Schwarz therefore gives
\[
 \mathbb E|(x^Ty)C_2(x,y)|=O(N^{-3/2}).
 \tag{Ideal-quartic-remainder}
\]
Thus this particular quartic correction is negligible in probability relative to the natural \(q/N\) quadratic scale.
This does not establish anticoncentration of the quadratic, whose coefficients can interact with atoms of the entry law.

<a id="actual-residual-background"></a>
## The actual residual has a nonvanishing stable background

For an actual decomposition \(M^{-1}=qur^T+E\), the same identity instead gives
\[
 S=G-q(Vu)(r^TW),\qquad
 G=D+3(x^Ty)E_{11}-VEW,
\]
\[
 \det S=\det G-q(r^TW)\operatorname{adj}(G)(Vu).
 \tag{Actual-pole-background}
\]
In particular, the ideal formula cannot discard \(E\) solely from dominance of its operator norm by \(q\).
Suppose, conditionally on the original minor, that \(\|E\|_F\le L\sqrt N\), and retain the original \(N^{-1/2}\) row normalization.
Define
\[
 c=N^{-1}\operatorname{Tr}E,\quad
 a=N^{-1}\operatorname{Tr}(EA),\quad
 b=N^{-1}\operatorname{Tr}(EB),\quad
 d=N^{-1}\operatorname{Tr}[E(A^2+B^2)].
\]
A direct covariance expansion yields
\[
 \mathbb E[VEW\mid A,B,E]
 =\begin{pmatrix}2d&b&4a\\a&0&2c\\2b&c&0\end{pmatrix}.
 \tag{Residual-mean}
\]
Every entry of \(VEW\) is a fixed sum of quadratic or bilinear forms.
For a deterministic complex matrix \(F\), independent centered normalized real rows with bounded fourth moments give
\[
 \mathbb E|x^TFx-N^{-1}\operatorname{Tr}F|^2
 \le C N^{-2}\|F\|_F^2,\qquad
 \mathbb E|x^TFy|^2=N^{-2}\|F\|_F^2.
\]
These follow by expanding the four coordinates: singleton indices vanish, the two pairings are bounded by the Frobenius square, and all-equal indices use the fourth moment.
The matrices here are products of \(E\) and at most two of \(A,B\), so their Frobenius norms are at most \(C_KL\sqrt N\).
Consequently \(G\) fluctuates by \(O_{\mathbb P}(N^{-1/2})\) around
\[
 K_E=\begin{pmatrix}-z-2d&-b&-4a\\-a&-1&-2c\\-2b&-c&-1\end{pmatrix}.
 \tag{Stable-background}
\]
The four normalized traces are merely bounded under the stated residual guard; they need not tend to zero.
The appropriate leading quadratic is therefore \((r^TW)\operatorname{adj}(K_E)(Vu)\), whose nonvanishing and original-law anticoncentration are additional obligations.
The proof of (Uniform-graph-coefficient) only treats the special background \(D\), and supplies no such result for all possible \(K_E\).
A residual with Frobenius norm \(o(\sqrt N)\) would remove this distinction, but that is not an available regime for a norm-bounded original \(M\): all its inverse singular values are at least \(1/\|M\|\), so removing one mode still leaves Frobenius norm of order at least \(\sqrt N\).

<a id="raw-degree-two-consequence"></a>
## A raw coefficient consequence and its exact limit

There is nevertheless a coefficient consequence for an isolated inverse pole of the full companion.
Write \(Q^{-1}=q w\ell^*+E_Q\), with unit singular vectors \(w,\ell\), so \(\|Qw\|=\|Q^*\ell\|=q^{-1}\).
Their last two block equations give approximate graphs
\[
 w=(u,Bu,Au)+O(q^{-1}),\qquad
 \ell=(\alpha,A\alpha,2B\alpha)+O(q^{-1}).
\]
The root norms are bounded below by constants depending on \(K\) when \(q\) is large.
Take \(r=\overline\alpha\), using that \(A,B\) are real.
The homogeneous degree-two part of \(\det(D-RQ^{-1}C)\) is linear in \(Q^{-1}\).
At its rank-one graph term it is \(-qQ_{A,B,u,r,z}\).
Its coefficient map on an arbitrary remainder has Frobenius operator norm bounded only in terms of the fixed three-channel matrices and \(z\); this follows by expanding the finitely many block contractions and symmetrizing their pure quadratic blocks.
The graph errors change that coefficient norm by \(O_{K,z}(1)\).
Therefore there are constants \(c_0,c_1>0\) such that, for sufficiently large \(q\),
\[
 \|E_Q\|_F\le c_0q
 \quad\Longrightarrow\quad
 \|\text{raw degree-two coefficient of }\det S\|_F\ge c_1q.
 \tag{Isolated-pole-raw-coefficient}
\]
Small exposed diagonal coordinates preserve this estimate, because the adjugate of their \(3\times3\) block varies continuously; the necessary smallness depends only on \(K,z\).
With raw row variables instead of the normalized rows, the coefficient scale is \(q/N\).
Finite-second-moment diagonal laws make these diagonal coordinates tend to zero in probability.

A large raw quadratic coefficient is not a complete lower bound for the multilinear polynomial obtained under an atomic two-copy representation.
Higher even powers may collapse to lower degrees, and the actual determinant normalization must still be controlled.
Nor does root incompressibility alone preserve graph consistency after removing coordinates with large load.
The exact stable background, robust tail coefficients and actual row-law small-ball probabilities remain the necessary continuation objects.
For Brown-relevant parameters, the [existing almost-everywhere singularity observation](../claims/Yin_C_F0186_v4.md#remaining-defect) already removes exact finite-size singularity almost surely after a countable union over dimensions and physical minors; it does not control their quantitative inverse scales.


<a id="inverse-tail-reservoir"></a>
## Uniform inverse-energy survival after deleting large-load coordinates

There is a separate useful consequence of the adopted C196 incompressibility result, without a rank-one approximation.
This subsection uses its full complex Hermitian input scope, while the preceding graph-polynomial calculations retain their real-input scope.
Work on a fixed parent norm guard and a bounded shift disk, and use both C196 for \((A,B,z)\) and its application to \((B,A,\overline z)\).
The combined exceptional probability is still \(Ce^{-cN}\).
The following statements concern the intersection with the norm guard; it is never conditioned into a fresh-row law.

Let \(L=\mathcal L_N(z)\) be the actual companion from C196, and group its three auxiliary coordinates at each physical position.
There exist fixed \(a_*,c_*,\delta_*>0\) such that, on this event, the right and left low-singular subspaces
\[
 V=\operatorname{Ran}\mathbf1_{[0,a_*^2]}(L^*L),\qquad
 U=\operatorname{Ran}\mathbf1_{[0,a_*^2]}(LL^*)
\]
satisfy, for every physical set \(S\) with \(|S|\le\delta_*N\),
\[
 \|P_{S^c}v\|\ge c_*\|v\|\quad(v\in V),\qquad
 \|P_{S^c}u\|\ge c_*\|u\|\quad(u\in U).
 \tag{Two-sided-low-space-restriction}
\]
Here \(P_{S^c}\) retains all three auxiliary coordinates over the remaining physical positions.

For the right space, every unit vector has residual at most \(a_*\), so the exact companion reduction gives a physical root of norm bounded below by a constant depending on the norm guard.
After normalizing that root, C196 excludes compressibility.
For any set of at most \(\delta N\) coordinates, a normalized vector with tail norm at most \(\rho/\sqrt2\) is within distance \(\rho\) of a unit vector supported there, by the normalized-truncation calculation used in C196.
Thus the root retains a fixed norm outside every such set, and so does the complete companion vector.
This reasoning is simultaneous over the entire low-singular subspace, rather than only over individual singular vectors.

For the left space, write the residual of \(L^*(\alpha,\beta,\gamma)^T\) as \((r_0,r_1,r_2)^T\).
The exact equations give
\[
 \beta=A\alpha-r_1,\qquad\gamma=2B\alpha-r_2,
\]
\[
 (BA+2AB-\overline z I)\alpha=r_0+Br_1+Ar_2.
\]
A unit companion vector with residual at most \(\varepsilon\le1/4\) has
\[
 \|\alpha\|\ge[2(1+3K)]^{-1},\qquad
 \|(BA+2AB-\overline z I)\alpha\|\le(1+2K)\varepsilon.
\]
Choose \(a_*\) sufficiently small and apply the swapped C196 assertion to \(\alpha/\|\alpha\|\).
This proves the left restriction bound and hence (Two-sided-low-space-restriction).
The argument also permits zero singular values.

Now let \(E\) be any matrix with range contained in \(V\) and range of its adjoint contained in \(U\).
Applying the right restriction bound to every column and then the left restriction bound to the rows gives
\[
 \|P_{S^c} E P_{S^c}\|_F\ge c_*^2\|E\|_F
 \qquad(|S|\le\delta_*N).
 \tag{Tail-inverse-energy-survival}
\]
This permits arbitrary weights on the low singular modes and removal of any selected modes; no independence of those weights is used.

For \(E\ne0\), define physical loads
\[
 \ell_i=\|P_iE\|_F^2+\|EP_i\|_F^2,
 \qquad\sum_i\ell_i=2\|E\|_F^2.
\]
For any \(\epsilon>0\), let \(S=\{i:\ell_i>\epsilon\|E\|_F^2\}\).
Its cardinality is at most \(2/\epsilon\).
For \(N\) large enough that \(2/\epsilon\le\delta_*N\), the truncated matrix \(E_T=P_{S^c}EP_{S^c}\) satisfies
\[
 \|E_T\|_F\ge c_*^2\|E\|_F,
 \qquad
 \max_i\frac{\|P_iE_T\|_F^2+\|E_TP_i\|_F^2}{\|E_T\|_F^2}
 \le c_*^{-4}\epsilon.
 \tag{Low-load-inverse-reservoir}
\]
The same conclusion holds for a deterministic sequence \(\epsilon_N\downarrow0\) whenever \(2/\epsilon_N\le\delta_*N\).
When \(E\) is itself selected measurably from the actual minor, the deletion and compression are minor-measurable before sampling the fresh border.
The deterministic restriction inequalities for arbitrary \(E\) do not assert measurability for a nonmeasurable choice.

For an actual inverse remainder whose Frobenius norm divided by \(\sqrt N\) diverges, its restriction to modes with singular value at most \(a_*\) carries asymptotically all that energy.
Indeed the complementary inverse piece has Frobenius norm at most \(\sqrt{3N}/a_*\), including after removal of finitely many modes.
Thus this reservoir is applicable to a high-residual branch.
It supplies inverse-matrix energy and load control, not a lower bound for the complete Schur determinant tensor or its normalized small-ball probability.
In particular, compressing all physical coordinates may destroy the exact graph identities needed by a separate determinant-nonvanishing argument; that remaining interface is not asserted here.

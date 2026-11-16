---
author: Yin
---
# Fixed local interactions and exceptional ranks on a torsion-free wreath product

The [wreath-product reduction for A0001](../claims/Yin_C_A0017_v2.md#consequence-for-a0001) turns a failure of integer rank into exact powers \(\alpha^n\) of a scalar nullity, where \(0<\alpha<1\).
Two realizations give different tests on a single group.
Finite paths keep the group support, local matrix blocks and operator norm bounded as the path grows.
A selfadjoint affine pencil keeps the matrix size and support fixed while its exceptional real parameters form a countable dense subset of \([-2,2]\).

## Common coefficient and trace

Assume that the [Task contract](../tasks/Yin_T_A0001_v1.md#contract) fails.
By [the finite-support reduction and actual division-closure criterion](../claims/Yin_C_A0017_v2.md#consequence-for-a0001), there is a nontrivial finitely generated torsion-free group \(K\) and a nonzero singular \(a\) in the scalar division closure \(D_K\) of \(\mathbb C K\) in its regular affiliated algebra.
Write \(W=K\wr\mathbb Z\), with \(t\) shifting the lamp at site zero to site one, and \(U=\mathcal U(W)\).
Use the canonical group trace and its unnormalized matrix extensions.
For a finite group-ring matrix \(M\), its regular Hilbert kernel dimension \(\nu(M)\) equals the dimension of the kernel on free right \(U\)-modules: both are given by the trace of the same kernel projection.
In particular invertible row and column operations over \(U\) preserve nullity.

The bounded positive element \(b=1-(1+a^*a)^{-1}\) of \(D_K\) has kernel projection \(p\) with trace \(\alpha=\nu(a)\in(0,1)\).
The projections \(t^jpt^{-j}\) at distinct sites commute, and traces of products of these projections and their complements at distinct sites factor by the product trace.
The [finite Schur realization](../claims/Yin_C_A0017_v2.md#group-ring-matrices-with-the-same-nullities) gives
\[
 b=d-cL^{-1}e,\qquad
 Q=\begin{pmatrix}d&c\\ e&L\end{pmatrix}\in M_{1+h}(\mathbb C K),
\]
where \(L\) has size \(h\) and is invertible in the affiliated matrix algebra.
One can append a unit block to choose \(h\ge1\).
The group-ring matrices below use only \(d,c,e,L\), their adjoints, constants and the height shift.

## A positive block Jacobi matrix at every path length

For \(n\ge1\), write \(w_j=(v_j,y_j)\in U\oplus U^h\), \(0\le j<n\).
Let \(B_n\) send \(w=(w_0,\ldots,w_{n-1})\) to the \(n\) vectors \(Qw_j\) together with the \(n-1\) scalars \(v_{j+1}-t^{-1}v_j\).
Then \(J_n=B_n^*B_n\) belongs to \(M_{n(h+1)}(\mathbb C W)\).
With \(P=\operatorname{diag}(1,0_h)\), its diagonal blocks for \(n\ge2\) are \(Q^*Q+P\) at the endpoints and \(Q^*Q+2P\) in the interior.
The upper and lower neighboring blocks are \(-tP\) and \(-t^{-1}P\), respectively, and the other blocks are zero.
For \(n=1\), \(J_1=Q^*Q\).
The coupling form satisfies \(\sum_j\|v_{j+1}-t^{-1}v_j\|^2\le4\sum_j\|v_j\|^2\), hence \(\|J_n\|\le\|Q\|^2+4\).
The block size, scalar entries available for these blocks, and group support of the entries are independent of \(n\).

On affiliated modules the cell equation gives \(y_j=-L^{-1}ev_j\) and \(bv_j=0\).
The edge equations give \(v_j=t^{-j}v_0\), so \(v_0\) ranges precisely over the common kernel of the \(t^jbt^{-j}\) for \(0\le j<n\).
These equations give an isomorphism of that right \(U\)-module onto \(\ker B_n\) with inverse projection onto \(v_0\).
The commuting kernel projections give its dimension by the product trace.
Since \(\ker(B_n^*B_n)=\ker B_n\), this yields
\[
                         \nu(J_n)=\alpha^n .
\]
Thus any strictly positive lower bounds \(\epsilon_n\) for the nonzero nullities of this particular family with \(\limsup_n\epsilon_n^{1/n}=1\) would exclude its hypothesized input.
The estimate needed here concerns finite intervals with a fixed local interaction and these endpoint conditions.

## A fixed Hermitian pencil

Put \(T=t+t^{-1}\).
For real \(\lambda\) consider on \(U^2\) the matrix
\[
 H(\lambda)=\begin{pmatrix}T-\lambda&b\\ b&0\end{pmatrix}.
\]
Define
\[
 M(\lambda)=\begin{pmatrix}T-\lambda&d\\ d^*&0\end{pmatrix},
 \qquad X=\begin{pmatrix}c&0\\0&e^*\end{pmatrix},
 \qquad D=\begin{pmatrix}0&L^*\\ L&0\end{pmatrix},
 \qquad A(\lambda)=\begin{pmatrix}M(\lambda)&X\\X^*&D\end{pmatrix}.
\]
This is a selfadjoint matrix over \(\mathbb C W\) of size \(2+2h\) with parameter coefficient \(-E_{11}\).
The upper right block of \(D^{-1}\) is \(L^{-1}\) and its lower left block is \((L^*)^{-1}\).
Eliminating \(D\) therefore gives \(M(\lambda)-XD^{-1}X^*=H(\lambda)\), so \(\nu(A(\lambda))=\nu(H(\lambda))\).

The equations \(bx=0\) and \(by=-(T-\lambda)x\) imply \(x\in pU\) and \(p(T-\lambda)px=0\).
Conversely, for each such \(x\), the second equation has all solutions \(y=-b^\dagger(T-\lambda)x+z\) with \(z\in pU\), where \(b^\dagger\) is the inverse on the support \(1-p\), extended by zero on \(p\).
This uses \(bb^\dagger=b^\dagger b=1-p\) in \(U\) and requires no bounded inverse on the support.
The resulting right \(U\)-module isomorphism shows that
\[
          \nu(A(\lambda))=\alpha+
          \tau\bigl(1_{\{\lambda\}}(pTp|_p)\bigr),
\]
where the corner trace is unnormalized.

The [commuting-path decomposition](../claims/Yin_C_A0005_v2.md#path-blocks-and-the-exact-kernel-dimension) and its [corner spectral measure, equation (11)](../claims/Yin_C_A0005_v2.md#actual-projections-and-boundary-residues) apply to this orbit of \(p\).
A path of \(\ell\) occupied sites starting at zero with both neighbors vacant has trace \((1-\alpha)^2\alpha^\ell\); the all-occupied projection has trace zero.
Every eigenline of the length-\(\ell\) Dirichlet path contributes one copy of that start projection to the corner spectral measure.
The path eigenvalues \(2\cos(\pi k/(\ell+1))\), \(1\le k\le\ell\), have multiplicity one by the finite sine basis.
For integers \(0<m<q\) with \(\gcd(m,q)=1\), the eigenvalue \(2\cos(\pi m/q)\) therefore occurs precisely at lengths \(\ell=jq-1,\ j\ge1\).
Summing the geometric series gives
\[
 \nu(A(\lambda))-\alpha=
 \begin{cases}
 \displaystyle\frac{(1-\alpha)^2\alpha^{q-1}}{1-\alpha^q},
       &\lambda=2\cos(\pi m/q),\quad 0<m<q,\quad \gcd(m,q)=1,\\[4pt]
 0, &\text{otherwise}.
 \end{cases}
\]
In particular \(\lambda=0\) and \(1\) have positive excess and \(\lambda=2\) has zero excess.
The exceptional parameters are dense in \([-2,2]\) and the excess decays exponentially in the reduced denominator along this same pencil.

## Relation to the universal question

If the contract holds, the actual division closure of every torsion-free group ring under consideration is a skew field.
For a matrix pencil varying only by \(-\lambda E_{11}\), eliminate all pivots of the constant block obtained by deleting the first row and column over that skew field.
The residual block is \(\left(\begin{smallmatrix}s-\lambda&u\\v&0\end{smallmatrix}\right)\) for a fixed scalar, row and column.
If \(u,v\) are both nonzero it has rank two, using a pivot in each; if exactly one is nonzero it has rank one.
When both vanish, the rank is one except possibly at the single scalar value \(s=\lambda\).
These ranks agree with regular dimensions because the same invertible row and column operations apply over \(U\).
Thus the contract implies that every such pencil has at most one real parameter of nullity above its minimum.
Conversely, under failure of the universal contract the fixed group-ring pencil just constructed has infinitely many such parameters.
The construction also preserves the class of amenable groups, since the wreath product of an amenable \(K\) by \(\mathbb Z\) is amenable.
An independent structural exclusion of the displayed rank behavior for these torsion-free groups remains open.

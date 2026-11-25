---
author: Yin
---

# Right polynomial relations and the zero spectral projection of a bordered pencil

On November 25, 2026, the investigation of [A0003](../tasks/Yin_T_A0003_v3.md#contract) considered polynomial relations among the columns \((B^*B)^jJ\).
Such a relation can give the last diagonal entry of the kernel projection by a scalar inversion, even when the compressed spectral measure has infinite support.
A pencil over the free group on two generators shows that these relations need not exist.
Regular specialization of the compressed resolvent gives an exact alternative for each pencil.

Write \(H=\ell^2(G)\), \(R=\mathbb CG\), \(U=L^0(\mathcal N(G))\) and \(D=\operatorname{Div}_U R\).
Take a bordered pencil
\[
 B=\begin{pmatrix}L&\beta\\ \alpha&0\end{pmatrix},
 \qquad A=B^*B,\qquad \pi=p_{\ker B},\qquad h=J^*\pi J,
\]
where \(L\) is an injective square affine pencil over \(R\), the row \(\alpha\) and column \(\beta\) are constant, and \(J\) is the last coordinate inclusion.
For a fixed marked group one can delete the local condition in the finite-rank criterion exactly when \(h\in D\) for every such pencil. [Reduction to one diagonal entry](Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil)

## A formula from right polynomial relations

Suppose \(\sum_{j=k}^m A^jJc_j=0\) for coefficients \(c_j\in R\), with \(b=c_k\ne0\).
If \(k=0\), left multiplication by \(\pi\) gives \(\pi Jb=0\), so put \(Y=0\).
If \(k\ge1\), put \(Y=\sum_{j=k}^m A^{j-k}Jc_j\).
Then \(A^kY=0\) and positivity gives \(\ker A^k=\ker A\), so \(Y=\pi Y=\pi Jb\).
In both cases every entry of \(Y\) lies in \(R\).
If \(b\) is an affiliated unit, this gives \(h=J^*Yb^{-1}\in D\).

More generally, take finitely many such relations, with possibly different lowest degrees and corresponding \(Y_i,b_i\).
If \(\sum_i b_ib_i^*\) has zero Hilbert kernel, positivity makes it an affiliated unit and
\[
 h=J^*\Big(\sum_iY_ib_i^*\Big)\Big(\sum_i b_ib_i^*\Big)^{-1}\in D .
\]
This follows by multiplying each identity \(\pi Jb_i=Y_i\) on the right by \(b_i^*\) and summing.

For an example with infinite spectral support take \(G=\mathbb Z\), let \(X\) be its generator, and use \(L=1+X\), \(\beta=1\), \(\alpha=0\).
Fourier transformation shows \(L\) is injective.
Put \(w=1+LL^*\), so \(A^2J=AJw\) and \(J^*AJ=1\).
The formula gives \(h=1-w^{-1}\).
In each Fourier fiber \(A\) has eigenvalues \(0\) and \(w=3+2\cos\theta\), and the weight of the last coordinate at the positive eigenvalue is \(w^{-1}>0\).
The compressed spectral measure therefore has positive spectrum supported on the entire interval \([1,5]\), precluding a nonzero scalar polynomial relation on \(J\).

## A free-group pencil with no right polynomial relation

Let \(G=F(x,y)\), \(d=y-1\), \(v=1+x\), and \(a=v^*v=2+x+x^{-1}\).
For any \(\lambda\in\mathbb C\) set
\[
 L=\begin{pmatrix}1&0\\d&v\end{pmatrix},
 \qquad \beta=\binom10,\qquad \alpha=(\lambda,0).
\]
The shift by \(x\) on each coset of \(\langle x\rangle\) is bilateral, so \(v\) and \(v^*\) have zero kernel.
It follows that \(L\) is injective and \(k=L^{-1}\beta=(1,-v^{-1}d)^t\).
The scalar \(\alpha L^{-1}\beta\) equals \(\lambda\).
If \(\lambda\ne0\), then \(B\) is an affiliated unit, so \(h=0\).
If \(\lambda=0\), the graph of the kernel gives \(h=(1+k^*k)^{-1}\), a nonzero affiliated unit in \(D\). [Kernel graph formula](Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil)

The family \(x^i d\), \(i\in\mathbb Z\), is right linearly independent over \(R\).
Indeed, the conjugates \(y_i=x^i yx^{-i}\) freely generate a free subgroup, as one sees by expanding a reduced product of nonzero powers with consecutive distinct indices into the reduced \(x,y\) word.
The graph on \(G\) with oriented edges \(g\longrightarrow y_i g\) is a disjoint union of trees.
A relation \(\sum_i(y_i-1)r_i=0\) over \(R\) gives a finitely supported edge chain with zero boundary in this graph.
A nonempty finite forest has a leaf, so all its edge coefficients vanish.
Since \(x^i d=(y_i-1)x^i\), the asserted independence follows.
In \(a^n\) the largest exponent of \(x\) is \(n\), with coefficient one.
It follows by considering the largest \(n\) in a relation that \(a^n d\), \(n\ge0\), are right linearly independent.
Commutation of \(a\) with \(v^*\) and injectivity of \(v^*\) give the same independence for \(a^n v^*d\).

Let \(t_j,b_j\) be the first and second entries of \(A^jJ\).
The second row of \(A\) is \((v^*d,a,0)\), and \(J=(0,0,1)^t\) gives \(AJ=(1,0,1)^t\).
Thus \(b_0=b_1=0\), \(b_2=v^*d\), and \(b_{j+1}=ab_j+v^*d\,t_j\).
For \(j\ge2\), induction gives \(b_j=a^{j-2}v^*d\) plus a right \(R\)-linear combination of the earlier \(a^i v^*d\).
In a relation \(\sum_{j=0}^m A^jJc_j=0\), the second entry therefore forces all \(c_j=0\) for \(j\ge2\).
The first and third entries of \(Jc_0+AJc_1=0\) then force \(c_0=c_1=0\).
For this prescribed pencil, rationality of its kernel coefficient coexists with right \(R\)-linear independence of all the columns \(A^jJ\), for every value of \(\lambda\).

## Regular specialization of the compressed resolvent

For real \(t>0\) set \(F(t)=tJ^*(A+tI)^{-1}J\).
Then \(h\in D\) if and only if there exists a scalar rational expression over \(R\) in the central real parameter \(t\) which equals \(F(t)\) for all sufficiently small \(t>0\) and is defined at \(t=0\).
Here being defined requires that every scalar to be inverted be a unit in \(U\), both at zero and throughout the specified positive interval.

For the forward direction write \(V=\binom{-L^{-1}\beta}{1}\).
The graph formula gives \(\pi=VhV^*\), so all entries of \(\pi\) belong to \(D\). [Kernel graph formula](Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil)
The matrix \(C(t)=A+\pi+t(I-\pi)\) is positive and has zero kernel for all \(t\ge0\) because it acts as the identity on \(\ker A\) and as \(A+tI\) on its orthogonal complement.
The spectral theorem gives
\[
 F(t)=h+tJ^*(I-\pi)C(t)^{-1}(I-\pi)J\qquad(t>0).
\]
The same order of scalar Gram pivots works for \(C(t)\) at every \(t\ge0\), since the leading Gram pivots for an injective square matrix are affiliated units. [Scalar pivots](../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Expanding the constant entries from \(D\) by their defining rational expressions gives the required expression over \(R\).

Conversely, evaluation of a rational expression defined for \(0\le t<\delta\) is continuous in measure at zero.
Sums and products are continuous in the measure topology of \(U\). [Affiliated measure topology](../audits/literature/FK86/Yin_U001.md#measure-topology-interface)
For the inversion step, if units \(Z_t\) converge in measure to a unit \(Z\), put \(Y_t=Z^{-1}Z_t\).
For every \(0<\epsilon<1/2\) and all sufficiently small \(t\), there is a projection \(q_t\) of trace at least \(1-\epsilon\) with \(\|(Y_t-I)q_t\|<\epsilon\).
The operator \(Y_tq_t\) is bounded below by \(1-\epsilon\) on \(q_t H\), so its range is closed and its range projection has the same trace as \(q_t\).
On that range \(Y_t^{-1}-I\) has norm at most \(\epsilon/(1-\epsilon)\), giving \(Y_t^{-1}\to I\) in measure and hence \(Z_t^{-1}\to Z^{-1}\) in measure.
This proves continuity of evaluation by induction on the expression.
Meanwhile \(t(A+tI)^{-1}\) converges strongly to \(\pi\) by spectral calculus and is uniformly bounded by one, so \(F(t)\to h\) in measure.
Uniqueness of the limit identifies \(h\) with the value at zero of the expression, which belongs to \(D\).

The free-group example rules out a proof of deletion that requires a right polynomial relation over \(R\) for every prescribed bordered pencil.
The remaining specialization question is whether every compressed resolvent from a finitely generated torsion-free group admits an expression defined at zero.

---
author: Yin
---

# Brown masses of unbounded rational matrices at stable kernels and on the resolvent chart

## Statement

Let \(Y\) be a \(k\)-square actual finite rational evaluation over \(\overline{\mathbb Q}G\) for a sofic group \(G\), as in the [logarithmic integrability result](Yin_C_A0347_v4.md#logarithmic-integrability-for-unbounded-evaluations).
Use the probability Brown measure and the matrix trace \(\tau=\operatorname{Tr}_G/k\).
The output and intermediate inverses may be unbounded.

* At an algebraic \(\lambda\), if two successive generalized kernels of \(T=Y-\lambda I\) have the same dimension at orders \(m,m+1\), \(m\ge1\), then
  \[
                 \mu_Y(\{\lambda\})=\tau(\operatorname{proj}\ker T^m)
                   =\lim_{j\to\infty}k^{-1}\dim_G\ker T^j .
  \]
  The complementary compression has a positive Fuglede--Kadison determinant computed below from the nonzero singular distributions of \(T^m,T^{2m}\).
* If the usual resolvent set of \(Y\) is nonempty, the same limit formula holds at every complex \(\lambda\), without a stabilization hypothesis.
  All atoms are algebraic and are exactly the ordinary eigenvalues.
* The formula also holds at every complex point if there are finitely many algebraic ordinary eigenvalues and their generalized kernels stabilize.
  In particular it holds for every such unbounded matrix on a torsion-free sofic group satisfying the complex strong Atiyah conjecture.
  In this case all atom masses lie in \(\{1/k,2/k,\ldots,1\}\).

The stable-kernel argument is valid in any finite tracial von Neumann algebra under a reduced logarithmic integral condition.
It does not require the ranges of \(T^j\) to be closed or their kernel projections to be expressible in any rational layer.

## The complementary compression at a stable kernel

Let \(T\in\mathcal M^\Delta\), the class of affiliated operators with \(\tau\log^+|T|<\infty\), for a finite von Neumann algebra with tracial state \(\tau\).
Regard generalized kernels as right modules over the affiliated algebra when taking compositions.
Equality of dimensions at consecutive orders implies equality of their kernel projections by inclusion and faithfulness.
Taking inverse images under \(T\) then proves equality at all following orders.
Write \(S=T^m\), \(p=\operatorname{proj}\ker S=\operatorname{proj}\ker S^2\), \(q=I-p\).
The closures of the ranges of \(S,S^2\) are equal: the second is contained in the first and both have trace \(\tau(q)\).
Denote their common projection by \(r\).
The Moore--Penrose inverse \(W^\dagger\) of an affiliated operator \(W\) is taken as an affiliated inverse between its support modules, extended by zero on the orthogonal complement of its image support.
By polar decomposition the positive-part logarithm of \(|W^\dagger|\) has integral equal to \(\int_{(0,\infty)}\log^-t\,d\mu_{|W|}(t)\).

Suppose the latter integral is finite for \(W=S^2\).
If \(q\ne0\), let \(C=qSq\), with the normalized trace on the \(q\)-corner.
Write \(Z=S|_q,\ Z_2=S^2|_q\) as affiliated isomorphisms from \(q\) to \(r\).
The equality \(Sp=0\) gives \(ZC=Z_2\), since \(S q S q=S^2q\).
Consequently \(C\) is invertible in the \(q\)-corner and \(C^{-1}=Z_2^\dagger Z\).
This inverse has positive-part logarithm integrable by the hypothesis on \(S^2\), the assumption \(S\in\mathcal M^\Delta\), and closure of that class under multiplication.
The rectangular factors may equivalently be viewed as operators on the full space supported on the specified corners.
Both \(C\) and \(C^{-1}\) belong to the logarithmic class of the \(q\)-corner, so \(0<\Delta_q(C)<\infty\).
The Brown measure of \(C\) has zero mass at zero by the logarithmic potential formula. [Haagerup and Schultz, Propositions 2.5 and 2.16 and Theorem 2.7](https://arxiv.org/pdf/math/0605251)

When both \(S\) and \(S^2\) have finite negative logarithmic integral on their strictly positive singular values, put
\[
   L_+(W)=\int_{(0,\infty)}\log t\,d\mu_{|W|}(t).
\]
Then the actual corner determinant is given by
\[
                  \tau(q)\log\Delta_q(C)=L_+(S^2)-L_+(S).
\]
Indeed if \(v\) is the polar partial isometry of \(S\), the two \(q\)-square operators \(v^*Z,v^*Z_2\) have the respective strictly positive singular distributions of \(S,S^2\) after normalization by \(\tau(q)\).
This uses the common final projection \(r=vv^*\).
Apply multiplicativity to \(v^*Z_2=(v^*Z)C\).

In the splitting \(p,q\) the first column of \(S\) is zero.
The [upper triangular determinant identity](Yin_C_A0347_v4.md#actual-eigenvectors-and-the-layer-criterion) gives \(\mu_S=\tau(p)\delta_0+\tau(q)\mu_C\), with the endpoint cases \(p=0,I\) interpreted directly.
Thus \(\mu_S(\{0\})=\tau(p)\).
Brown measure under the power \(T^m\) is the pushforward under \(z\mapsto z^m\), also for unbounded logarithmically integrable operators. [Haagerup and Schultz, Proposition 2.15](https://arxiv.org/pdf/math/0605251#page=16)
The power has only zero as a preimage of zero, so \(\mu_T(\{0\})=\tau(p)\).

For \(T=Y-\lambda I\) and \(\lambda\) algebraic, both \(T^m,T^{2m}\) are actual algebraic rational evaluations.
Their positive logarithms are integrable, and their negative logarithms on strictly positive singular values are integrable by the [sparse-system estimate without a bounded-output hypothesis](Yin_C_A0347_v4.md#logarithmic-integrability-for-unbounded-evaluations).
Translation of Brown measure proves the first assertion.

## An algebraic point in the resolvent

The usual resolvent set consists of those \(a\) for which \(Y-aI\) has a bounded everywhere-defined inverse.
It is open for a closed operator, by the Neumann series at any such point.
If it is nonempty take an algebraic \(a\) there and put \(Z=(Y-aI)^{-1}\).
This is a bounded actual algebraic rational matrix, so its Brown atom formula holds at every complex point by the [bounded evaluation theorem](Yin_C_A0347_v3.md#statement).
The operator \(Y-aI\) and its inverse belong to \(\mathcal M^\Delta\) by the rational integrability theorem.
In particular its negative logarithm is integrable and it has no kernel, so \(\log\Delta(Y-aI)>-\infty\) and \(\mu_Y(\{a\})=0\).
The Brown measure of \(Z\) is the pushforward of \(\mu_{Y-aI}\) under inversion. [Haagerup and Schultz, Proposition 2.16](https://arxiv.org/pdf/math/0605251#page=17)

For \(\lambda\ne a\) write \(\gamma=(\lambda-a)^{-1}\).
In the affiliated algebra one has
\[
                      Z-\gamma I=-\gamma Z(Y-\lambda I).
\]
The two nonconstant factors on the right commute and \(Z\) is an affiliated unit.
Taking any positive power therefore gives exactly the same kernel on the two sides as \((Y-\lambda I)^j\).
The Brown mass of \(Y\) at \(\lambda\) equals that of \(Z\) at \(\gamma\).
Transfer the bounded formula along these two equalities.
Inversion and translation by an algebraic point preserve algebraicity of the nonexceptional points, giving the asserted support of the atoms.

## Finitely many algebraic eigenvalues and the strong Atiyah case

Suppose \(Y\) has only finitely many algebraic ordinary eigenvalues.
There are then no transcendental Brown atoms, even before imposing stabilization at the algebraic ones.
To see this, fix a transcendental \(\lambda\) with proposed mass \(\alpha>0\).
Let \(l\) be the fixed coefficient-field degree in the [unbounded singular-logarithm estimate](Yin_C_A0347_v4.md#logarithmic-integrability-for-unbounded-evaluations), and choose \(n+1>2(l+1)/\alpha\).
The [complex pigeonhole construction](Yin_C_A0347_v1.md#transcendental-points-and-small-polynomial-values) gives nonzero integer polynomials of degree at most \(n\), height at most \(D\), and modulus at \(\lambda\) at most \(C_{n,\lambda}D^{1-(n+1)/2}\).
Remove all factors belonging to the primitive integral minimal polynomials of the finite algebraic eigenvalue list.
Gauss's lemma puts the quotient \(Q\) in \(\mathbb Z[z]\) even when these primitive factors are nonmonic.
With \(n\) fixed there are finitely many possible products removed.
Division by each is bounded on this finite-dimensional space of coefficient lists, and its value at \(\lambda\) is nonzero.
Thus the height of \(Q\) is \(O_n(D)\) and its small-value bound at \(\lambda\) has the same exponent.

No root of \(Q\) is an ordinary eigenvalue, since its roots are algebraic.
Factoring over the algebraic numbers makes \(Q(Y)\) an affiliated unit, and the singular-logarithm estimate gives \(\log\Delta(Q(Y))\ge-l\log D-O_n(1)\).
On the other hand, factorization, potential identities and determinant multiplicativity give
\[
                    \log\Delta(Q(Y))=\int\log|Q(z)|\,d\mu_Y(z).
\]
Use the small value at \(\lambda\) there, and elsewhere use \(\log^+|Q(z)|\le\log D+O_n(1)+n\log^+|z|\).
The positive logarithmic moment of \(\mu_Y\) is finite, so this gives at most \((1-\alpha(n+1)/2)\log D+O_{n,\lambda,Y}(1)\).
This contradicts the lower bound.
At any point where the Brown mass is zero, the [kernel lower bound](Yin_C_A0347_v4.md#actual-eigenvectors-and-the-layer-criterion) applied to \((Y-\lambda I)^j\) and the power pushforward show that the kernel dimensions vanish at all orders.
At each algebraic point either the first kernel is zero, in which case the kernels are stable, or the stabilization hypothesis for that eigenvalue applies.
This proves the all-points claim under the stated finite stabilized eigenvalue condition.

If \(G\) is torsion-free sofic and satisfies strong Atiyah over \(\mathbb C\), its scalar division closure is a skew field containing the entries of \(Y\). [Division-closure criterion](../tasks/Yin_T_A0001_v1.md#starting-references)
For every algebraic \(\lambda\), linear algebra over the skew field gives integral unnormalized kernel dimensions for all powers of \(Y-\lambda I\).
Indeed invertible elementary operations over the field also act invertibly on affiliated modules.
Strict inclusion increases these dimensions by at least one, and equality at one step implies stability, so the kernels stabilize by the \(k\)-th power.
Distinct algebraic eigenvalues have linearly independent eigenspaces in the sense of a direct sum of affiliated modules, by scalar polynomial interpolation.
Every nonzero one has unnormalized dimension at least one.
Hence there can be at most \(k\) algebraic ordinary eigenvalues, and the sufficient condition just proved applies.

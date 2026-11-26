---
author: Yin
---

# Exact Brown atoms of unbounded rational matrices from open finite time chains

## Statement

Let \(G\) be sofic and let \(Y\) be a \(k\)-square algebraic-coefficient rational evaluation in its regular affiliated algebra, with every inverse gate defined there.
All gates and the final matrix may be unbounded.
Use the probability Brown measure for the regular trace normalized by \(k\).
For every \(\lambda\in\mathbb C\) one has
\[
            \mu_Y(\{\lambda\})=\frac1k\lim_{m\to\infty}
                                   \dim_G\ker (Y-\lambda I)^m .
\]
The atoms are exactly the ordinary eigenvalues, and all are algebraic.
At every algebraic \(\lambda\) the integral of \(\log^-|z-\lambda|\) away from \(z=\lambda\) is finite after omitting the atom.
No resolvent or generalized-kernel stabilization condition is required.
This extends the [bounded formula](Yin_C_A0347_v3.md#statement) and [the stable-kernel and resolvent tests](Yin_C_A0347_v5.md#statement).
The inputs are actual evaluations, including mixed Schur complements with nonclosed pivot range.
The assertion does not establish integrality of their kernel dimensions.

More quantitatively, for a nonzero integer polynomial \(P\) of degree at most \(n\) and coefficient height at most \(D\ge1\), there is a fixed coefficient-field degree \(l\) and a constant \(C_n\) independent of \(P,D\) such that
\[
         \int_{P(z)\ne0}\log^-|P(z)|\,d\mu_Y(z)\le l\log D+C_n .
\]
In particular for each algebraic shift the Brown mass of the punctured disk of radius \(s<1\) about that point is \(O_\lambda(1/|\log s|)\).

## A bounded pencil for the logarithmic potential

All the actual rational matrices and their invertible auxiliary gates are in the [unbounded logarithmic class](Yin_C_A0347_v4.md#logarithmic-integrability-for-unbounded-evaluations), also for the inverse of an affiliated unit.
Restrict to the finitely generated subgroup supporting the expression; regular trace preservation gives the same determinants and Brown measure.
Represent a chosen output \(W\) as \(d-ca^{-1}b\), with \(a,b,c,d\) algebraic group-ring blocks and \(a\) square and invertible in the affiliated algebra.
Take either \(W=Y-\lambda I\) for algebraic \(\lambda\), or \(W=P(Y)\).
For the latter use the [sparse polynomial system](Yin_C_A0347_v3.md#sparse-repeated-systems-with-a-fixed-number-of-coefficient-dependent-rows) with one copy.
Its auxiliary matrix \(a\) computes the powers \(Y^i\) using only the original gates and identity connections.
Only its last \(k\) output rows in the full matrix involve \(P\), and \(a\) is independent of its coefficients for fixed \(n\).

Put \(F=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), \(E=\operatorname{diag}(0,I_k)\), and let \(h\) be the full number of matrix coordinates.
Write \(\mathcal L\) for the logarithmic determinant with unnormalized matrix trace and with the zero singular value included, so that a nonzero kernel gives \(-\infty\).
Then
\[
                  \mathcal L(F-wE)=\mathcal L(a)
                       +k\int\log|z-w|\,d\mu_W(z).
\]
Indeed the triangular Schur elimination factors have logarithmic class entries and inverses, and each elementary block shear has determinant one by its similarity to its square.
Determinant multiplicativity gives the formula even when the residual determinant is zero.
The auxiliary term is finite. [Unbounded determinant and potential](Yin_C_A0347_v4.md#actual-eigenvectors-and-the-layer-criterion)

## The singular product on an open time chain

Take \(m\) copies of \(F\) on the diagonal of \(L_m(r)\), with \(-rE\) immediately below the diagonal and zeros elsewhere, for \(0<r\le1\).
Its kernel at \(r=1\), as an affiliated module, is parametrized by the last \(k\)-column \(x_m\in\ker W^m\).
Indeed elimination gives \(Wx_1=0,\ Wx_i=x_{i-1}\) for \(2\le i\le m\), and each auxiliary coordinate vector is fixed by its input.
Thus its unnormalized kernel dimension \(\kappa_m=\dim_G\ker W^m\) is at most \(k\).
The weighted chain is its conjugate by the scalar block diagonal with layer weights \(1,r,\ldots,r^{m-1}\).

Take an \(N\)-site sofic model of the group-ring entries; denote the unit-weight and weighted finite chains by \(L_{m,N}(1)\) and \(L_{m,N}(r)\).
Let \(q_{m,N}\) be their common ordinary nullity and \(\Pi(B)\) the product of strictly positive singular values of a finite matrix \(B\), with empty product one.
For fixed \(m,W\), \(q_{m,N}/N\to\kappa_m\) along the sofic approximation by applying rank convergence to the whole bounded chain. [Jaikin-Zapirain, Theorem 1.3](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf#page=5)
This does not require the finite approximations of \(a\) to be invertible.

For a minor of maximal rank size \(hmN-q_{m,N}\), the exponent of \(r\) introduced by the diagonal similarity is the weight-index sum of its retained rows minus that of its retained columns.
It is equivalently the sum for its omitted columns minus that for its omitted rows.
Every index lies between zero and \(m-1\), so this exponent is at most \((m-1)q_{m,N}\).
By Cauchy--Binet the square of \(\Pi\) is the sum of the squared absolute values of all these maximal minors, hence
\[
             \Pi(L_{m,N}(r))\ge
                  r^{(m-1)q_{m,N}}\Pi(L_{m,N}(1)).
\]

For \(W=P(Y)\) one has the arithmetic lower bound
\[
     \frac{\log\Pi(L_{m,N}(1))}{mN}
                       \ge -(l-1)k\log D-C_n .
\]
For \(W=Y-\lambda I\) only a fixed constant is needed, by including \(\lambda\) in the number field and taking the input polynomial of degree one and height one for the shifted system.
For clarity, clear a common positive integer denominator on the whole finite matrix and use a Galois coefficient field of degree \(l\), stable under conjugation.
The product of the positive squared singular values of this integral matrix is a nonzero algebraic integer.
In each embedding its maximal-minor sum has at most \(4^{hmN}\) terms.
Only \(kmN\) rows have coefficient size dependent on \(D\), so each minor in either embedded factor of a squared minor is at most \(D^{kmN}C_n'{}^{hmN}\).
After dividing these rows by \(D\), the row and column sums are uniformly bounded by the fixed word expressions at each time step, including the extra time edge of weight one.
Apply the ordinary integer lower bound on the absolute field norm, take a square root and undo the denominator.
This proves the estimate with constants independent of \(m,N,D\).
It is valid even when a finite chain has additional zero singular values.

## Two limits and the exact logarithmic slope

Fix \(r\) and \(0<\eta<1\), and use \(f_\eta(t)=\log\max(t,\eta)\).
The preceding two estimates give, including the \(q_{m,N}\) zero values,
\[
 \frac1{mN}\operatorname{Tr} f_\eta(|L_{m,N}(r)|)
 \ge -C_n-(l-1)k\log D+
        \frac{(m-1)q_{m,N}}{mN}\log r
             +\frac{q_{m,N}}{mN}\log\eta .
\]
First let \(N\) tend along the sofic sequence at fixed \(m,r\).
The left side tends to the corresponding regular trace divided by \(m\), by finite word moments and the uniform finite norm at this fixed system.
Next let \(m\to\infty\).
The last term disappears since \(\kappa_m\le k\); the preceding coefficient tends to \(\kappa_\infty=\lim_m\kappa_m\).
On the left the limiting trace is the circle mean of \(\operatorname{Tr}_G f_\eta(|F-r e^{it} E|)\).
Indeed closing the chain by inserting its last-to-first edge changes rank by at most \(k\).
For fixed \(r,P\) both full systems have norm bounded independently of \(m\).
In the normalized trace of any fixed polynomial in the Gram operator, the difference tends to zero by expanding the difference and bounding the trace of each term by its rank times its norm, then dividing by \(m\).
Uniform polynomial approximation of the continuous function \(u\mapsto f_\eta(\sqrt u)\) on the bounded spectral interval gives the same conclusion for the cutoff.
The cyclic chain diagonalizes at the \(m\)-th roots by ordinary time Fourier transformation, and its mean converges to the circle integral by continuity.

Let \(\eta\downarrow0\) only after both limits.
Monotone convergence after subtraction from a uniform upper bound gives the circle mean of the actual logarithmic determinant.
Use the bounded-pencil identity and the scalar circular mean of \(\log|z-re^{it}|\) to conclude that for all \(0<r<1\),
\[
     k\int\log\max(r,|z|)\,d\mu_W(z)
                 \ge \kappa_\infty\log r-(l-1)k\log D-C_n'' .
\]
Here the auxiliary determinant is included in the constant and is independent of the polynomial coefficients at fixed \(n\).
The circle exchange of integrals is legitimate: the positive logarithm is bounded by \(\log(1+r)+\log^+|z|\), integrable against \(\mu_W\), and the scalar circle mean is bounded below by \(\log r\).

Divide by the negative number \(k\log r\) and let \(r\downarrow0\).
On the unit disk the normalized integrand is bounded between zero and one and tends to the indicator of zero.
Outside it the integrable positive log contributes a vanishing ratio.
This proves \(\mu_W(\{0\})\le\kappa_\infty/k\).
Conversely \(\mu_{W^m}(\{0\})=\mu_W(\{0\})\) by unbounded polynomial spectral mapping, while the [kernel corner inequality](Yin_C_A0347_v4.md#actual-eigenvectors-and-the-layer-criterion) bounds this mass below by \(\kappa_m/k\).
This proves equality for \(W\), in particular for every algebraic shift.
The power mapping here also follows by factoring the polynomial in the unbounded logarithmic potential. [Haagerup and Schultz, Proposition 2.15](https://arxiv.org/pdf/math/0605251)

## Removing exactly the zero mass

The equality just proved cancels the term \(\kappa_\infty\log r\) exactly from the last inequality.
Taking \(r\downarrow0\) on the remaining positive-radii part gives
\[
          \int_{z\ne0}\log|z|\,d\mu_W(z)\ge -(l-1)\log D-C_n''' .
\]
Its positive part is integrable, so its negative part away from zero is finite.
For \(W=P(Y)\), polynomial spectral mapping pushes \(\mu_Y\) forward to \(\mu_W\).
The positive logarithm of \(|P(z)|\) is bounded by \(\log D+\log(n+1)+n\log^+|z|\).
This proves the height-uniform punctured logarithmic estimate in the statement, with no restriction on the zeros of \(P(Y)\).
For the algebraic shift it gives the punctured-disk mass bound by Markov's inequality.

If a transcendental \(\lambda\) were an atom of mass \(\alpha>0\), use a nonzero integer polynomial of degree at most \(n\) and height at most \(D\) whose value at \(\lambda\) is at most \(C_{n,\lambda}D^{1-(n+1)/2}\) and is nonzero, by the [complex pigeonhole construction](Yin_C_A0347_v1.md#transcendental-points-and-small-polynomial-values).
Take \(n+1>2(l+1)/\alpha\) and let \(D\to\infty\).
The contribution of this one point to the punctured negative logarithm contradicts the bound just proved.
Ordinary kernels of all powers at a transcendental point are zero by the general kernel-mass lower bound applied to powers.
At algebraic points the increasing generalized-kernel limit is positive if and only if the first kernel is nonzero, proving the point-spectrum assertion.

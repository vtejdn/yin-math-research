---
author: Yin
---

# Brown atoms of algebraic group-ring matrices over sofic groups

## Statement

Let \(G\) be sofic and \(X\in M_k(\overline{\mathbb Q}G)\).
Use the probability Brown measure \(\mu_X\) with the regular trace normalized by \(k\).
For every \(\lambda\in\mathbb C\),
\[
       k\,\mu_X(\{\lambda\})
            =\lim_{j\to\infty}\dim_G\ker(X-\lambda I)^j .
\]
In particular the atoms are exactly the ordinary eigenvalues, all algebraic; for algebraic integer coefficients the atoms are algebraic integers.
For algebraic \(\lambda\) their masses are unchanged by embedding the coefficients and \(\lambda\) simultaneously into \(\mathbb C\).
No approximation of Brown measures by eigenvalue measures of finite models is required.
All the group von Neumann algebra quantities can first be computed in the finitely generated subgroup containing the support, since regular inclusion preserves its trace, singular distributions and logarithmic determinants.

For torsion-free sofic \(G\) the full complex-coefficient Atiyah conjecture on \(G\) is equivalent to the assertion that every atom of each such algebraic \(k\)-square matrix has mass in \(\frac1k\mathbb Z\), for all \(k\).
For a sofic group having scalar injectivity, every nonscalar \(x\in\overline{\mathbb Q}G\) (meaning \(x\notin\mathbb C e\)) has atomless Brown measure.
The assertions include nonnormal matrices and elements.

## Logarithmic tails for roots of all powers

First let \(Y\) be any \(k\)-square algebraic group-ring matrix.
Write \(\nu_j\) for the normalized singular distribution of \(|Y^j|^{1/j}\).
There are constants \(C\) and \(L\ge1\) such that the supports are contained in \([0,L]\) and
\[
    \int_{(0,\infty)}\log t\,d\nu_j(t)\ge-C,\qquad
    \nu_j((0,s])\le (C+\log L)/|\log s|\quad(0<s<1).
\]
These constants can be chosen from a fixed finite word expression and its algebraic coefficients, uniformly in any sofic marked quotient.
The bound on positive singular values excludes the atom at zero from the integral.

To see this choose an integer \(b\ge1\) making \(bY\) integral over the ordinary integers coefficientwise, and take a finite Galois number field containing all coefficients and their complex conjugates.
For \(Z_j=((bY)^j)^*(bY)^j\) use the determinant bound for positive matrices over the algebraic integer group ring. [Knebusch, Definitions 2.3 and 2.5 and Theorem 4.4](https://arxiv.org/pdf/0804.0530#page=6)
For every embedding the maximum number of nonzero entries in each regular row or column of the embedded \(Z_j\) and the maximum absolute coefficient are bounded exponentially in \(j\).
Indeed the support counts multiply under matrix multiplication, and the maximum absolute row and column sums are submultiplicative.
Bounds for the two separately embedded factors \(bY,(bY)^*\) suffice, without commuting the embedding and conjugation.
Use bounds on the free word lifts to allow collisions in a quotient.
The resulting logarithms of the finitely many \(\kappa(\sigma Z_j)\) in Knebusch's bound are \(O(j)\).
If \(Z_j=0\), the positive-singular-value integral is empty.
Otherwise its unnormalized integral of \(\log t\) on \(0<t<\infty\) is bounded below by \(-O(j)\).
Taking square roots, removing \(b^j\) and dividing by \(kj\) proves the first estimate.
The norm bound \(\||Y^j|^{1/j}\|\le\|Y\|\) and the upper bound \(\log L\) for the integral of the positive logarithm give the second.

The radial Brown-measure theorem gives weak convergence of \(\nu_j\) to the image of \(\mu_Y\) under \(z\mapsto|z|\). Its squared version is Theorem 2.2 of Haagerup and Schultz, who also explain the trace-preserving passage from finite algebras to a finite factor. [Haagerup and Schultz, Sections 1 and 2](https://www.numdam.org/article/PMIHES_2009__109__19_0.pdf)
The uniform estimate on \((0,s]\) gives convergence of the masses at zero by taking positive continuity radii down to zero.
Consequently
\[
                   \mu_Y(\{0\})=\lim_j k^{-1}\dim_G\ker Y^j .
\]
Apply this to \(Y=X-\lambda I\) for algebraic \(\lambda\), using translation of Brown measure.
A bounded operator is injective exactly when all its positive powers are injective, so positivity of the limiting mass is equivalent to a nonzero kernel because the kernels increase.
Rank invariance under coefficient embeddings for each of these powers gives the assertion about masses. [Jaikin-Zapirain, Corollary 1.7](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf)

## Transcendental points and small polynomial values

By multiplying \(X,\lambda\) by the same positive integer we can assume \(X\) has algebraic integer coefficients.
Let \(K\) be a finite Galois field containing its coefficients and their complex conjugates, of degree \(l\).
For each fixed \(n\) there are finitely many minimal polynomials over \(\mathbb Q\) of degree at most \(n\) that can vanish at an ordinary eigenvalue of \(X\).
Indeed Thom's algebraic eigenvalue theorem makes these eigenvalues algebraic integers. [Thom, Theorem 1.2](https://arxiv.org/pdf/math/0701294#page=1)
Every conjugate of such an eigenvalue is an eigenvalue of some conjugate matrix by the rank independence theorem applied to the shifted matrix.
The finitely many conjugate coefficient matrices have a common operator-norm bound.
The elementary symmetric functions of at most \(n\) conjugates therefore bound the integer coefficients of the monic minimal polynomials.

Fix a transcendental \(\lambda\).
For each sufficiently large integer \(D\) there is a nonzero \(P\in\mathbb Z[z]\) of degree at most \(n\), height at most \(D\) (maximum absolute coefficient), with
\[
                             |P(\lambda)|\le C_{n,\lambda}D^{1-(n+1)/2}.
\]
Evaluate the \((D+1)^{n+1}\) polynomials with coefficients between zero and \(D\) in a complex square of side \(O_{n,\lambda}(D)\).
Partition it into fewer than that many equal subsquares of side \(O_{n,\lambda}(D^{1-(n+1)/2})\).
The difference of a pair in one subsquare works.
Remove from \(P\) every irreducible factor in the preceding finite forbidden list, with its multiplicity, obtaining \(Q\in\mathbb Z[z]\).
Only finitely many products can be removed at this fixed degree, all taking nonzero values at \(\lambda\).
Division by these fixed monic factors on coefficient vectors is bounded at degree at most \(n\), by ordinary long division.
Thus \(Q\) still has height \(O_n(D)\) and satisfies the same small-value bound up to a fixed multiplier.
The operator \(Q(X)\) is injective since its scalar linear factors at all its roots are injective.

Knebusch's determinant bound for \(Q(X)^*Q(X)\) now uses a fixed support depending on \(n\), and coefficients \(O_n(D^2)\) in each embedding.
With trace normalized by \(k\) and upon taking the square root this yields
\[
                          \log\Delta(Q(X))\ge -(l-1)\log D-O_n(1).
\]
The logarithmic potential of Brown measure gives
\(\log\Delta(Q(X))=\int\log|Q(z)|\,d\mu_X(z)\), by factoring \(Q\) and multiplicativity of the determinant. [Haagerup and Schultz, Brown measure and its logarithmic potential](https://arxiv.org/pdf/math/0605251#page=10)
On the bounded spectral disk of \(X\) the polynomial has modulus \(O_n(D)\).
If \(\mu_X(\{\lambda\})=\alpha>0\), its small value at \(\lambda\) makes the last integral at most
\((1-\alpha(n+1)/2)\log D+O_{n,\lambda}(1)\).
Choose \(n+1>2l/\alpha\), then let \(D\to\infty\), contradicting the lower bound.
This excludes transcendental atoms. Thom's theorem excludes ordinary transcendental eigenvalues, so the kernel formula holds there too.

## Quantization and the scalar case

If the complex Atiyah conjecture holds for \(G\), the increasing unnormalized generalized-kernel dimensions in the formula are integers bounded by \(k\).
Their limit is an integer.
Conversely take \(X=A^*A\) for an arbitrary rectangular matrix \(A\) over \(\overline{\mathbb Q}G\).
The zero atom for this positive matrix is the normalized regular kernel dimension of \(A\).
Quantization therefore gives strong Atiyah integrality over \(\overline{\mathbb Q}\), and the sofic base-change theorem gives it over \(\mathbb C\). [Jaikin-Zapirain, Theorem 1.1](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf#page=4)
Finally a nonscalar \(x\) has \(x-\lambda e\ne0\) for all \(\lambda\).
Under scalar injectivity it has no ordinary eigenvalues, which gives the asserted absence of Brown atoms.

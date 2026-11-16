# Open mathematical problems in the F0012 manuscript

## Hypothesis of the added-coordinate estimate

In [the global lower-bound argument](sections/affine.tex), the paragraph beginning “For a map \(F\) on \(\mathbb R^p\) with empty zero set” asserts that \((x,y)\mapsto(yF(x),y(y-1))\) has degree at most three and uses the exponent \(3\cdot15^p\).
An empty zero set alone does not bound the degree: the argument uses the fact that \(F\) is one of the quadratic compressed maps \(F_{k,\ell}\).

## Fixed coefficients in the deterministic case

The opening of [the affine proof](sections/affine.tex) refers to “the random coefficients.”
The \(A_j\) are fixed matrices; the GUE inputs are random.
The deterministic branch uses \(A_1=\cdots=A_d=0\).

## Laplacian in the definition of Brown measure

The [definition of Brown measure](sections/introduction.tex) sets \(\mu_a^{\mathrm{Br}}=(2\pi)^{-1}\Delta u_a\) and says only that \(\Delta\) acts distributionally.
The name, sign and normalization of the operator are implicit until [the Brown-measure proof](sections/brown.tex) uses \(\Delta\log|z|=2\pi\delta_0\).
The intended convention is the planar Laplacian \(\Delta=\partial_x^2+\partial_y^2\) for \(z=x+\mathrm i y\).

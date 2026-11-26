---
author: Yin
---

# Brown atoms of bounded rational evaluations through arbitrary finite inverse layers

## Statement

Let \(G\) be sofic and let \(Y\) be a bounded \(k\)-square operator represented by a finite rational expression over \(\overline{\mathbb Q}G\) inside the regular affiliated algebra.
All inverses in the expression must exist at their actual gate sizes; intermediate inverses may be unbounded.
The final bound means \(Y\in M_k(\mathcal N(G))\).
Then for each \(\lambda\in\mathbb C\) its probability Brown measure satisfies
\[
         \mu_Y(\{\lambda\})=
            \lim_{j\to\infty}k^{-1}\dim_G\ker(Y-\lambda I)^j .
\]
All atoms are algebraic and coincide as a set with the ordinary eigenvalues.
In particular this covers a bounded Schur complement \(d-ca^{-1}b\) even when the nonzero pivot has nonclosed range, provided it is invertible in the affiliated algebra.
The conclusion concerns point masses; it does not claim approximation of Brown measures by spectra of finite matrices.

If the complex strong Atiyah conjecture holds on a torsion-free sofic \(G\), all these masses are multiples of \(1/k\).
In particular each bounded scalar in the actual rational closure of \(\overline{\mathbb Q}G\) is either a scalar constant or has atomless Brown measure.
Conversely quantization for all the bounded evaluations above implies the complex conjecture on \(G\) by the [polynomial case](Yin_C_A0347_v1.md#quantization-and-the-scalar-case).
The general formula requires no scalar-injectivity or integrality hypothesis.

## An actual linear system and its spectral comparison

Represent the input as \(Y=d-ca^{-1}b\), with rectangular block sizes compatible, \(a\) square and affiliated-invertible, and \(a,b,c,d\) matrices over the algebraic group ring.
Here and below the letters can denote enlarged blocks.
Every finite rational expression admits such a representation.
Associate to each intermediate vector its auxiliary unknowns and linear equations, with signs chosen so that elimination returns the expression.
For a group-ring operation on the input use its group-ring matrix directly.
For sums take both auxiliary systems in parallel; for a product add an unknown for the intermediate output, impose its output equation and feed it to the next system.
For inversion of a square output use its output equation with prescribed value as a new auxiliary equation and take the old input as the new output.
The old auxiliary system solves uniquely in the affiliated algebra, and the new input is uniquely determined by the assumed actual inverse.
Equivalently the enlarged block matrix of the preceding system is an affiliated unit by Schur elimination.
These steps give a square auxiliary system invertible in the affiliated algebra, and do not require bounded intermediate inverses.

For any bounded output \(F=d-ca^{-1}b\) compare it with its whole matrix \(T=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\).
Let \(n_S(I)\) denote the unnormalized regular trace of the spectral projection of \(|S|\) on \(I\).
For all \(t>0\),
\[
                n_F((0,t])\le n_T((0,t]),\qquad
                n_F(\{0\})=n_T(\{0\}).
\]
The kernel equality follows by affiliated Gaussian elimination, using dimensions of right modules.
For the inequality on \([0,t]\), lift \(x\) to \((-a^{-1}bx,x)\). Its norm is at least \(\|x\|\) and its output is \((0,Fx)\) on the domain of the lift.
In the spectral space of \(|F|\) on \([0,t]\), intersect with the spectral cutoff \(|a^{-1}b|\le l\).
On that intersection the graph map is bounded, has a bounded left inverse, and every graph vector satisfies \(\|T v\|\le t\|v\|\).
The dimension of this graph is at most \(n_T([0,t])\), by its trivial intersection with the complementary spectral space of \(|T|\).
Cutting off costs at most the trace of \(\mathbf1_{(l,\infty)}(|a^{-1}b|)\), tending to zero as \(l\to\infty\).
The bounded \(F\) agrees with the affiliated expression on these vectors, as the original coefficients are bounded.
Subtract the equal kernel dimensions to obtain the displayed estimate.

## Sparse repeated systems with a fixed number of coefficient-dependent rows

Fix \(n\ge1\) and an integer polynomial \(P\) of degree at most \(n\) and coefficient height at most \(D\), \(D\ge1\).
For each integer \(j\ge1\), form an auxiliary matrix \(T_j\) for \(P(Y)^j\).
In each of the \(j\) copies start with a vector \(x_0\), compute \(x_1=Yx_0,\ldots,x_n=Yx_{n-1}\) by the preceding fixed system, and impose the output \(\sum_{i=0}^nP_i x_i\).
Connect each output to the next copy's input by one identity equation, leaving the last output as the last \(k\) rows of the full matrix.
All inner auxiliary blocks are invertible by successive substitutions in the affiliated algebra.
The full number of coordinates is at most \(c_n j\), where \(c_n\) depends on the fixed system and \(n\).
Only \(k j\) rows carry coefficients depending on \(P\), namely the \(k\) output or connection rows in each copy.
There are uniformly bounded row and column counts of group-ring words for fixed \(n\), including at the interfaces between copies.
The coefficient number field and a common positive integer denominator \(b_0\) for all entries can be fixed independently of \(P,n,j,D\).

For this approximation one may restrict to the countable subgroup generated by the finite support of the expression.
Its inclusion preserves the trace and all actual gate operations, and its singular distributions determine the same logarithmic potentials.
Take the coefficient field to be Galois over \(\mathbb Q\), stable under conjugation, of degree \(l\).
Use a sofic approximation on \(N\) sites, replacing each word by its permutation on the sites and using transposes of the resulting matrices for adjoints in finite singular-value calculations.
Remove the common denominators by multiplying the finite matrix by \(b_0\), writing the resulting matrix as \(B\) of size \(m\le c_n j N\).
After dividing the \(kjN\) distinguished rows by \(D\), the norm is bounded by a constant \(C_n\ge1\) for every coefficient embedding, uniformly in \(j,N,P,D\).
Indeed both maximum absolute row and column sums admit such bounds by the sparse construction, also for the entrywise complex conjugates.
At a site where words coincide their absolute sums can only use the same original bounds.

Let \(r\) be the ordinary rank of \(B\).
The product of its nonzero squared singular values is the sum of the squared absolute values of all \(r\)-square minors by Cauchy--Binet, with value one at rank zero.
This is a nonzero algebraic integer.
For any embedding each factor of a squared minor becomes a determinant of an embedded matrix or of its separately embedded coefficientwise conjugate.
Row rescaling bounds each such determinant by \(C_n^m D^{kjN}\).
There are at most \(4^m\) minors.
The absolute field norm is a nonzero integer, giving
\[
      \sum_{\sigma_i(B)>0}\log\sigma_i(B)
                     \ \ge\ -(l-1)kjN\log D-O_n(jN).
\]
Here \(\sigma_i\) denote singular values. The sum of their positive logarithms is at most \(kjN\log D+O_n(jN)\).
Indeed the row-rescaled matrix has norm bounded by \(C_n\); the diagonal matrix restoring its rows has singular values \(D\) on at most \(kjN\) coordinates and one elsewhere.
Apply the exterior-power norm bound to the product of the largest singular values exceeding one.
Returning to the unscaled finite system changes the estimate by \(O_n(jN)\).
It follows that the sum of \(\log^-(s)=\max(0,-\log s)\) on its strictly positive singular values is at most \(lkjN\log D+O_n(jN)\).

For each fixed \(P,j\), sofic convergence of all finite word moments and uniform boundedness in \(N\) imply weak convergence of the singular distributions of the full systems, dividing finite traces by \(N\).
The nonnegative function equal to \(\log^-(s)\) for \(s>0\) and to zero at zero is lower semicontinuous.
The same integral bound with \(N\) removed holds for the actual \(T_j\).
By the spectral comparison of the preceding section, integration of the counts on \((0,t]\) passes it to \(P(Y)^j\).
Consequently the probability singular distribution \(\nu_j\) of \(|P(Y)^j|^{1/j}\) satisfies
\[
              \int_{(0,\infty)}\log^-(s)\,d\nu_j(s)
                            \ \le\ l\log D+C'_n .
\]
The coefficient of \(\log D\) is independent of the polynomial degree.
The constants \(C'_n\) may depend on the original rational expression and on \(n\).

## Passage to Brown measure at all complex points

For fixed \(P\), the positive mass in \((0,s]\) is \(O(1/|\log s|)\) for the distributions just estimated, uniformly in \(j\).
Their radial Brown limit therefore gives convergence of the atoms at zero as in the [algebraic polynomial proof](Yin_C_A0347_v1.md#logarithmic-tails-for-roots-of-all-powers).
For any algebraic \(\lambda\), enlarge the fixed number field and apply the construction to \(Y-\lambda I\) with \(P(z)=z\).
This proves the generalized-kernel formula there.

For arbitrary integer \(P\) pass the same logarithmic bound to the radial limit by lower semicontinuity and use polynomial spectral mapping of Brown measure.
One obtains
\[
       \int_{\{z:P(z)\ne0\}}\log^-|P(z)|\,d\mu_Y(z)\le l\log D+C'_n .
\]
This comparison omits polynomial zeros even if their Brown masses are positive.
If a transcendental \(\lambda\) had mass \(\alpha>0\), the [elementary complex pigeonhole construction](Yin_C_A0347_v1.md#transcendental-points-and-small-polynomial-values) would give nonzero polynomials \(P\) at each large height with
\[
       0<|P(\lambda)|\le C_{n,\lambda}D^{\,1-(n+1)/2}.
\]
Choose \(n\) with \(\alpha((n+1)/2-1)>l\), then let \(D\) grow.
The contribution of \(\lambda\) alone contradicts the preceding bound.
Thus no transcendental point is an atom. At every complex \(\lambda\) the radial limit for \(Y-\lambda I\) and the closed-set inequality give \(\mu_Y(\{\lambda\})\ge\limsup_j \dim_G\ker (Y-\lambda I)^j/k\), where the right side means the increasing normalized dimensions of the power kernels.
Hence these kernels are zero at transcendental points.
This finishes the formula at all points.

If \(G\) satisfies the complex strong Atiyah conjecture, the actual division closure of \(\mathbb CG\) in \(U(G)\) is a skew field.
Schur elimination over that field or matrix linearization gives integer unnormalized dimensions for kernels of matrices over its subfield of actual algebraic rational evaluations, including their algebraic shifts and powers. [Division-closure equivalence](../tasks/Yin_T_A0001_v1.md#starting-references)
The increasing dimensions in the atom formula therefore stabilize at integers.
For \(k=1\) any ordinary scalar eigenvalue must itself be algebraic by the atom formula, and a nonzero scalar in the skew field is an affiliated unit.
This proves the stated scalar dichotomy.

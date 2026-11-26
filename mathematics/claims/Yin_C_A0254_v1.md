---
author: Yin
---

# Local maps and paired half-rank increments for three traceless commutator equations

## Statement

Let \(G=\langle S\rangle\) have a finite generating list, \(H=L^2(\mathcal N(G),\tau)\), and \(U\) be its regular affiliated algebra.
Suppose a [traceless system of size two](Yin_C_A0243_v2.md#statement) is given with bounded vectors \(x_1,x_2,y_1,y_2\).
Put \(z_i=y_i^*\).
Choose any finite-rank witnesses on this same list for the three tensors \(x_1\otimes z_2,\ x_2\otimes z_1,\ x_1\otimes z_1-x_2\otimes z_2\).
Let \(V\) contain the \(x_i\) and the first legs of all witness tensors, and let \(W\) contain the \(z_i\) and the second legs, taking any finite-dimensional complex spaces in \(H\) with these properties.
Write \(V^+=V+\sum_{g\in S}Vg\), \(W^+=W+\sum_{g\in S}gW\).

Every complex-linear map \(\phi:V^+\to U\) with \(\phi(vg)=\phi(v)g\) on \(V\) satisfies
\[
                    (\phi(x_1),\phi(x_2))=(a x_1,a x_2)
\]
for a single affiliated multiplier \(a\).
Every such pair occurs.
Likewise the pairs \((\theta(z_1),\theta(z_2))\) for left-compatible maps on \(W^+\) are exactly \((z_1 b,z_2 b)\), \(b\in U\).

The linear relations in the two finite lists of first translates give rectangular affine polynomial matrices \(A,B\) and constant columns \(\alpha_1,\alpha_2\) and rows \(\beta_1,\beta_2\), respectively, with the following tests.

* On the original group translations, adjoining any single nonzero complex combination of the two columns to \(A\) increases regular rank by exactly \(1/2\).
  Adjoining both together still increases rank by exactly \(1/2\).
  The right kernels of the two individual columns modulo the image of \(A\) are complementary orthogonal support modules.
  The corresponding row assertions hold for \(B\).
* At an arbitrary choice of \(d\)-square complex matrices for the marked variables, form the spaces of all evaluated right and left local maps with values in rows and columns of length \(d\), respectively.
  Let \(a_d\) be the dimension spanned by their right-map values at \(x_1,x_2\), and \(b_d\) that spanned by their left-map values at \(z_1,z_2\).
  If \(d\) is odd, \(a_d+b_d\le2d-1\).
  In particular at scalar labels one entire side of output evaluations vanishes.
  The two dimensions are explicit differences of ordinary ranks below.
* For at least one of the two base matrices \(A,B\), the free polynomial inner rank exceeds the original group regular rank by at least \(1/2\).
  Thus two lower bounds strictly within \(1/2\) of the respective free inner ranks exclude the proposed witnesses.

For a torsion-free group the first-translate vectors satisfy a further orbit restriction on each side.
Choose a basis of \(V\) containing \(x_1,x_2\).
For each \(x_i\), some complex relation among this basis and its first right translates has a nonzero coefficient on its projective right orbit after proportional terms are combined.
If nonzero group-ring scalars act injectively, the same relation has a nonzero sum on directions outside this orbit.
The analogous assertion holds for \(W\) with a basis containing \(z_1,z_2\) and left translates.
There is also a two-sided obstruction using group-ring values under just the algebraic domain hypothesis below.

## What local maps can do on the two output directions

The ordinary finite-rank tensor identity writes each of the three displayed boundary tensors as a finite sum of \(ug\otimes v-u\otimes gv\) with \(u\in V,\ v\in W\).
It uses \(h\mapsto u\tau(vh)\) for an elementary tensor and right multiplication by \(g\) for the commutator. [Finite-rank correspondence](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
Applying \(\phi\) to the first leg and multiplying into \(U\) annihilates every balance.
Thus \(\phi(x_i)z_j=0\) for \(i\ne j\) and \(\phi(x_1)z_1=\phi(x_2)z_2\).
The identity map gives \(x_i z_i=h\) independent of \(i\).
Let \(p_i\) be the right support of \(x_i\) and the left support of \(z_i\).
These projections are orthogonal with sum one by the prescribed translate spans.
Consequently \(hU=x_iU=eU\) for a common projection \(e\), \(z_i=x_i^\dagger h\), and \(z_i h^\dagger=x_i^\dagger\), where daggers denote relative inverses in \(U\).
The four supports have regular traces \(\tau(p_1)=\tau(p_2)=\tau(e)=\tau(h^\dagger h)=1/2\). [Support reconstruction](Yin_C_A0243_v1.md#recovering-the-matrix-units-from-the-witnesses)

The off-diagonal identities give \(\phi(x_i)=\phi(x_i)p_i\) because \(z_jU=p_jU\).
Multiplying the diagonal equality on the right by \(h^\dagger\) gives a common \(a=\phi(x_i)x_i^\dagger\), so \(a x_i=\phi(x_i)\).
Every \(a\in U\) gives a local map by left multiplication.
For a left-compatible \(\theta\), one has \(x_i\theta(z_j)=0\) off the diagonal and \(x_i\theta(z_i)\) is independent of \(i\).
Hence \(p_i\theta(z_i)=\theta(z_i)\), and \(b=h^\dagger x_i\theta(z_i)\) gives \(z_i b=\theta(z_i)\).
Conversely right multiplication by \(b\) realizes these values.

## The original group-ring matrices

Use basis rows \(\mathbf v=(v_1,\ldots,v_m)\) of \(V\) and basis columns \(\mathbf w=(w_1,\ldots,w_n)^{\mathsf T}\) of \(W\).
Write \(x_i=\mathbf v\alpha_i,\ z_i=\beta_i\mathbf w\) with constant coefficients.
For a complex basis of all linear relations among the \(v_j,v_j g\) form a column of \(A\) for each relation.
Its \(j\)-th entry is the coefficient of \(v_j\) plus the sum of the coefficients of the \(v_jg\) times their formal variable \(X_g\).
Form a row of \(B\) from each relation among \(w_j,gw_j\) in the same way.
This finite construction also works for a repeated label by indexing the list positions.
After evaluation at the group, \(\mathbf v A=0,\ B\mathbf w=0\).
All rows \(l\) over \(U\) with \(lA=0\) parametrize the right local maps, and all columns \(r\) with \(Br=0\) parametrize the left local maps, by the defining completeness of the complex relations.

For \(u_1,u_2\in U\) one has
\[
        \alpha_1u_1+\alpha_2u_2\in\operatorname{im}A
               \quad\Longleftrightarrow\quad x_1u_1+x_2u_2=0 .
\]
Indeed membership on the left is equivalent to annihilation by all rows \(lA=0\), as witnessed by the rows of \(I-AA^\dagger\).
The pair \(l\alpha_1,l\alpha_2\) ranges exactly over the simultaneous multiples proved above.
The column map into the cokernel thus has the same kernel as \([x_1\ x_2]\), which has image \(eU\).
For constants \(c_1,c_2\) not both zero, \(x=c_1x_1+c_2x_2\) also has image \(eU\): multiplying by \(p_i\) gives \(c_i x_i\), whose image already fills \(eU\) when \(c_i\ne0\).
The image of the joint map, or of any such single column in the cokernel, therefore has dimension \(1/2\).
For \(\alpha_i\) alone its right kernel modulo \(\operatorname{im}A\) is \((1-p_i)U\).
The left-handed argument for the two rows uses all columns \(Br=0\) and the common initial support of \(z_i\).
It gives the same rank increments and the left kernels \(U(1-p_i)\) modulo the row space of \(B\).
All dimensions here use the unnormalized coordinate trace.

## Numerical labels and the free inner rank loss

For arbitrary complex \(d\)-square labels \(T_g\), substitution in \(A,B\) parametrizes the local maps into rows and columns: \(lA(T)=0,\ B(T)r=0\), with all constant matrices amplified by \(I_d\).
These maps obey \(\phi(vg)=\phi(v)T_g,\ \theta(gw)=T_g\theta(w)\).
Use a basis of each solution space and stack the rows \(\phi(x_i)\) into a matrix \(X_i\) and concatenate the columns \(\theta(z_j)\) into a matrix \(Y_j\).
Applying both maps to the two legs of each boundary identity and multiplying annihilates its balances.
It gives \(X_iY_j=0\) off the diagonal and \(X_1Y_1=X_2Y_2=D\).
Hence the product of the vertical stack of \(X_1,X_2\) and the horizontal concatenation of \(Y_1,Y_2\) is \(\operatorname{diag}(D,D)\).
The factors have ranks \(a_d,b_d\) and the intermediate space has dimension \(d\).
If both ranks equal \(d\), the product has rank \(d\), which must then be even.
More precisely \(a_d+b_d-d\le2\operatorname{rank}D\le\min(a_d,b_d)\).

Explicitly,
\[
\begin{split}
 a_d&=\operatorname{rank}\begin{pmatrix} A(T)&0&\alpha_1\\0&A(T)&\alpha_2\end{pmatrix}-2\operatorname{rank} A(T),\\
 b_d&=\operatorname{rank}\begin{pmatrix} B(T)&0\\0&B(T)\\\beta_1&\beta_2\end{pmatrix}-2\operatorname{rank} B(T).
\end{split}
\]
For the first formula, the kernel of the last column modulo the first two block columns consists of those vectors annihilated by both sets of evaluated rows.
For the second, restrict the last block row to the kernel of the top two block rows.
At the actual group translations the corresponding regular rank increments are both one, since the two column kernels are complementary and the values \(z_iU=p_iU\) of the left maps together span \(U\).

Over any division ring containing \(\mathbb C\) centrally, the scalar-label case of the same local-map calculation gives a sharper dichotomy.
If a right-map value and a left-map value are both nonzero, they must occur at the same index by the off-diagonal products.
The opposite diagonal product is then zero while the selected diagonal product is nonzero.
Thus on at least one side all output values vanish for every solution.
For the free skew field on the label variables, ordinary row and column duality over a division ring gives either \(\operatorname{rank}[A,\alpha_1,\alpha_2]=\operatorname{rank}A\) or \(\operatorname{rank}[B;\beta_1;\beta_2]=\operatorname{rank}B\), with semicolon notation for stacked rows.
Free-field rank equals inner rank over the free polynomial algebra, also for rectangular matrices by padding with zero rows or columns. [Free-field rank interface](../audits/literature/MSY23/Yin_U004.md#theorem-56-exact-equivalences)
Every polynomial factorization evaluates at the original group translations, so the regular rank of the selected enlarged matrix is at most this common integer.
At the group its rank exceeds that of the selected base matrix by \(1/2\), proving the lower bound on the loss.

## Group-ring values and relations on a projective orbit

If \(\mathbb CG\) is a domain, take right- and left-compatible local maps with values in \(\mathbb CG\) at the actual group generators.
The same two-sided product argument in the domain shows that, on at least one side, every such map annihilates both output directions.
In particular suppose there are multipliers \(a,b\in U\) with all \(ax_i,z_jb\) in the group ring and with some nonzero value on each side.
Already \( (ax_i)(z_jb)=\delta_{ij}ahb\) gives a contradiction in the domain.
The multipliers here need only clear the two output vectors on each side.

Finally let \(G\) be torsion-free and fix \(x=x_i\) in an adapted basis of \(V\).
In its projective right orbit every vector has a unique expression \(c x h\) with \(c\in\mathbb C^\times,\ h\in G\).
Indeed a nonidentity stabilizer up to scalar would give an eigenvector for right translation by an infinite-order element, impossible on its bilateral-shift orbits in \(\ell^2(G)\).
On the finite list of basis vectors and first translates, send \(c x h\) to \(c h\in\mathbb CG\), and send every other vector to zero.
If every relation of this list had zero evaluated sum, this assignment would give a linear map on \(V^+\).
It would be right-compatible, because being in this orbit is invariant under each right group translation.
Its value at \(x\) would be \(1\), whereas the local-map conclusion forces every value at \(x_i\) to have right support dominated by \(p_i\).
Thus there is a relation whose sum over the chosen orbit is \(x f\) with \(0\ne f\in\mathbb CG\), after gathering equal group terms.
Under regular scalar injectivity \(f\) is an affiliated unit, so \(xf\ne0\) and the sum outside that orbit is its nonzero negative.
The argument for \(z_i\) uses left translations and sends \(c h z_i\) to \(c h\); left-compatible values there have left support dominated by \(p_i\).

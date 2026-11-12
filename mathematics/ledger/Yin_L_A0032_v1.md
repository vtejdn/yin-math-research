---
author: Yin
---
# Testing zero cokernel classes against the ICC regular trace

This exploration of [A0001](../tasks/Yin_T_A0001_v1.md#contract) on 2026-11-13 tests the single-class implication in the [KLS17 audit](../audits/literature/KLS17/Yin_U001.md#why-condition-3-has-not-been-cleared).
Its positive constraint for the actual regular representation is recorded in the [ICC rank dichotomy](../claims/Yin_C_A0017_v1.md#statement).
The two models below were developed in parallel with the arithmetic argument.
Both realize a zero cokernel class through a single injective endomorphism of the coefficient module.
Neither model computes global cyclic generation for its new coefficient ring.

## Keeping the regular trace and changing the coefficient ring

Let \(G=\bigoplus_{j\ge1} F_2\), a torsion-free ICC group, and \(N=\overline{\bigotimes}_{j\ge1}\mathcal N(F_2)\) with its regular product trace.
A nonidentity element has a nonidentity coordinate whose conjugacy class in that factor is infinite.
Fix \(0<\alpha<1\) and let \(p_j=1-\alpha^{2^{-j}}\), so \(\prod_j(1-p_j)=\alpha\).
For a free generator \(u_j\) of each factor take a real smooth circle function \(0\le f_j\le1\) strictly positive on one arc of Haar measure \(p_j\) and zero off the arc.
Its Fourier coefficients are absolutely summable by the second derivative bound.
Choose \(0<\delta_j\le2^{-j}/(1+\|\widehat f_j\|_1)\) and set
\[
 x=\sum_{j\ge1}\delta_j f_j(u_j),\qquad
 B=\mathbb C\langle\mathbb C[G],x\rangle,\qquad D'=D(B,\mathcal U(G)).
\]
The sum belongs to the embedded \(\ell^1(G)\), is positive and has kernel trace \(\alpha\) by independence of the Haar coordinates.
We show \(xb=0\) for \(b\in D'\) forces \(b=0\).

Every element \(b\) of the scalar division closure has a finite expression using sums, products and actual scalar inverse gates.
Take \(n\) covering its group-ring coefficients and split \(x=y_n+x_n\) into its positive prefix and commuting positive tail.
The tail law \(\mu_n\) has an atom at zero and gives positive mass to every \((0,\epsilon)\).
Indeed, require just one sufficiently remote bump with \(\delta_j<\epsilon\) to be positive and all other tail bumps to vanish, an event of positive product probability.
Writing \(N_n=\overline{\bigotimes}_{j\le n}\mathcal N(F_2)\), work inside the affiliates of \(N_n\ \overline\otimes\ W^*(x_n)\).
This algebra contains the expression since affiliated operators of a von Neumann subalgebra are inverse-closed in the larger affiliated algebra, by the support criterion for invertibility.
Identify the second factor with \(L^\infty(\mu_n)\), so that \(x(s)=y_n+s\).
Decomposing the finitely many inverse gates into fibers shows all gates valid at the atom \(s=0\) and on one set of full \(\mu_n\)-measure, since an invertible affiliated operator has both kernel and cokernel projection zero.
On this set \(xb=0\) gives \(b(s)=0\) for \(s>0\) by positivity of \(y_n+s\).
Choose good \(s_i>0\) tending to zero.
A finite rational linearization for the given defined expression gives, on each good fiber including 0,
\[
                 r(b(s))=r(P(s))-h,
\]
with bounded polynomial block matrix \(P(s)\) over \(N_n\) and constant auxiliary block size \(h\). [Actual inverse gates and bordering](../claims/Yin_C_A0012_v2.md#rational-expressions-with-actual-defined-inverse-gates)
The polynomial block is norm continuous in \(s\) and its range dimension is lower semicontinuous by continuous cutoffs of \(P(s)P(s)^*\).
Thus \(r(b(0))\le\liminf_i r(b(s_i))=0\), proving \(b=0\) in all fibers up to a null set.

Left multiplication gives an exact sequence \(0\to D'\xrightarrow{x}D'\to D'/xD'\to0\) of right modules.
The cokernel has zero \(G_0(D')\) class and its regular affiliated dimension is \(\alpha\).
In the convention \(S=k-\dim\operatorname{coker}x_U\), its witness has \(k=0\) and \(S=-\alpha\).
The canonical \(D(\mathbb C[G],\mathcal U(G))\) lies in the union of the prefix affiliated algebras, since this directed union contains \(\mathbb C[G]\) and is inverse-closed.
The operator \(x\) lies in no prefix, since its independent tail has a nonconstant law and the intersection of the prefix and tail factors consists of scalars.
This explicitly locates the change of coefficient ring even though \(x\) is a norm limit of finite group-ring sums.

## Keeping the ICC group ring and changing its trace

Let \(\Gamma=\mathbb Z\wr\mathbb Z\) and \(R=\mathbb C[u_i^{\pm1}:i\in\mathbb Z][s^{\pm1};\sigma]\) with the shift automorphism.
Projection to the shift and torsion-freeness of the lamp subgroup give torsion-freeness of \(\Gamma\).
A nonzero lamp configuration has infinitely many distinct translates, while conjugating an element of shift \(k\ne0\) by lamps at \(i\) changes its configuration by the different vectors \(\delta_i-\delta_{i+k}\).
Thus \(\Gamma\) is ICC.
The algebra \(R\) has a classical Ore division ring \(Q\), by localizing the lamp coefficients to their fraction field and taking skew Laurent fractions.
Denominators of finitely many shifted coefficients can be cleared back in the commutative lamp ring on either side.

Put \(\mu_p=(p\delta_1+(1-p)m_{\mathbb T})^{\mathbb Z}\) for \(0\le p<1\) and \(M_p=L^\infty(\mu_p)\rtimes_\sigma\mathbb Z\).
The Bernoulli shift is essentially free and ergodic, so \(M_p\) with its crossed product trace is a finite factor.
The shifts and coordinate unitaries generate it, and the map from \(R\) is faithful because finite-coordinate Laurent coefficients are detected on the positive-weight product Haar component and the shift sectors are orthogonal.
For \(p=0\) the trace is regular, by evaluating its moments on group elements.
For \(p>0\) the trace of the nonidentity lamp \(u_0\) is \(p\).

Write \(r_p\) for affiliated matrix rank in \(M_p\).
For any finite \(W\) over \(R\), one has \(r_p(W)\le r_0(W)\).
Indeed, if its shift propagation is \(L\) and it has \(b\) input columns per site, arrange the shifts in \(n>2L\) residue classes modulo \(n\).
Restriction to the crossed product by \(n\mathbb Z\) represents \(W\) by an \(n\)-site block, whose ordinary matrix trace with the factor trace divided by \(n\) recovers the original trace.
This follows on a Fourier monomial by inspecting its diagonal entries and using shift invariance.
Dropping the wrap-around terms changes at most \(2Lb\) input columns and hence changes normalized rank by at most \(2Lb/n\).
The remaining block is a Laurent polynomial matrix in finitely many circle coordinates.
Its pointwise rank for every choice of those coordinates is at most its Haar-almost-sure generic rank, by a maximal nonzero minor.
Integrating over each law, using the two boundary estimates, and letting \(n\to\infty\) proves the comparison.

In the regular representation \(R\) has division closure \(Q\) by the torsion-free elementary amenable case of Linnell's theorem and the Ore description. [Lin93 audit](../audits/literature/Lin93/Yin_U001.md)
Let \(D_p=D(R,\mathcal U(M_p))\).
For any finite rational expression \(e\) defined at \(p\), all its inverse gates remain defined at 0 and \(r_p(e)\le r_0(e)\).
Induct on the expression and use bordered polynomial linearization as above, whose auxiliary blocks are units at both evaluations for already valid inner gates.
In an inverse step the just-compared scalar has full rank at \(p\), hence full rank at 0.
In particular \(e_0=0\) implies \(e_p=0\).
Conversely, common right denominators give \(t\in R\setminus\{0\}\) and \(r\in R\) with \(e_pt=r\) and \(e_0t=r\) in their respective representations.
For a sum choose a common right multiple of the two denominators.
For a product \(xy\), write \(x t_x=r_x\) and \(y t_y=r_y\) at both evaluations.
If \(r_y=0\), then \(y_0=y_p=0\) by the rank comparison.
Otherwise choose \(v,w\ne0\) with \(r_yv=t_xw\), obtaining \((xy)t_yv=r_xw\).
For an inverse use \(x^{-1}r_x=t_x\), with \(r_x\ne0\) since \(x_0\) is a unit.
It follows from faithfulness on \(R\) that \(e_p=0\) implies \(e_0=0\).
Applying both implications to differences proves that \(e_p\mapsto e_0\) embeds \(D_p\) into \(Q\).

For \(a=u_0-1\), multiplication is thus algebraically injective on \(D_p\).
The sequence \(0\to D_p\xrightarrow{a}D_p\to D_p/aD_p\to0\) again gives class zero, while the affiliated cokernel has trace \(p\), the coordinate atom.
With the regular trace on the very same ICC group and matrix, the kernel trace is zero.
The [earlier abelian model](../audits/literature/KLS17/Yin_U001.md#a-faithful-representation-detecting-both-failed-formal-steps) also computes global \(G_0\) generation, but its von Neumann algebra is abelian.

## Checks in genuine group representations

For the lamplighter quotient \(\mathbb Z\wr\mathbb Z\twoheadrightarrow C_q\wr\mathbb Z\), \(q\ge2\), the regular nullity of the single lamp \(u_0-1\) changes from 0 upstairs to \(1/q\) downstairs.
Indeed the regular kernel upstairs consists of square-summable functions constant on infinite lamp cosets, and downstairs the kernel projection is the average over the order-\(q\) cyclic subgroup.
The quotient also contains \(C_q^n\) for every \(n\), violating even the bounded-order hypothesis in the journal theorem.
Taking its free product with \(F_2\) preserves these subgroups and the restricted regular ranks by coset decomposition.
Neither operation yields a torsion-free regular example.
The same torsion obstruction applies to Grabowski's integral group-ring matrix with transcendental regular kernel dimension. [Gra16, Theorem 2, p. 796](../literature/pdf/Gra16.pdf#page=2)

A separate torsion-free candidate comes from a preprint whose Theorem 1.1 gives a projection in the reduced group \(C^*\)-algebra with regular trace strictly between zero and one half.
The introduction obtains the matrix projection by continuous functional calculus on a separated spectral band and subsequently compresses it to a scalar projection.
This identifies neither a finite group-ring matrix with that kernel dimension nor the \(G_0\) of the actual division closure.
This screening uses the theorem statement and construction outline on pp. 2–3. [Ope26e](../literature/pdf/Ope26e.pdf#page=2)

The two zero-class models and this quotient test leave open the simultaneous requirements of an actual group-ring division closure, canonical regular trace, condition (3), and a finite group-ring matrix of nonintegral rank.

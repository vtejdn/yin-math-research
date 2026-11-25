---
author: Yin
---

# Obstructions to group-algebra denominators and least-norm finite-rank witnesses

For [A0003](../tasks/Yin_T_A0003_v3.md#contract), the [common-denominator criterion](../claims/Yin_C_A0135_v1.md#statement) uses one bounded positive affiliated unit and an existential tuple of finite-rank operators.
On November 25, 2026 the two examples below were obtained by testing whether the denominator can always be chosen in the group algebra or the tuple can always be selected by minimizing its Hilbert–Schmidt norm.

## A rational positive operator with no group-algebra denominator

Suppose that \(G\) contains two elements \(g,h\) that freely generate a free subgroup of rank two.
Write \(A=\mathbb CG\), \(M=\mathcal N(G)\), \(U=L^0(M)\) and \(D_G=\operatorname{Div}_U A\).
For \(k=g,h\), put \(d_k=1-k\), identifying group elements with their left multipliers on \(\ell^2(G)\).
The action of \(k\) on each right coset of \(\langle k\rangle\) is a bilateral shift.
Consequently \(d_k\) and \(d_k^*\) have zero Hilbert kernel and are affiliated units.
Define the positive rational operator
\[
                     u=(d_gd_g^*)^{-1}+(d_hd_h^*)^{-1}\in D_G .
\]
For every \(d\in A\),
\[
                 d^*ud\in M
          \quad\Longleftrightarrow\quad d\in d_gA\cap d_hA.             \tag{1}
\]
Indeed \(d^*ud=\sum_{k=g,h}(d_k^{-1}d)^*(d_k^{-1}d)\), and the positive sum is bounded precisely when both factors \(d_k^{-1}d\) are bounded.
For each \(k\), if \(d_k^{-1}d\) is bounded, its value \(\eta\) on \(\delta_e\) lies in \(\ell^2(G)\) and satisfies \(d_k\eta=d\delta_e\).
On a right coset of \(\langle k\rangle\) this equation prescribes the first difference of a two-sided square-summable sequence.
Its right side has finite support, so the sequence is constant on each tail and both constants vanish by square summability.
On every coset disjoint from the support of \(d\) the whole sequence vanishes.
Only finitely many cosets remain, so \(\eta\) has finite support.
It gives \(a_k\in A\) with \(d=d_k a_k\), since group-ring elements agree when their values on \(\delta_e\) agree.
Conversely this algebraic factorization gives \(d_k^{-1}d=a_k\) in \(U\), proving (1).

The intersection in (1) is zero for the free pair.
In fact \(d_g a=d_h b\) makes a finitely supported chain with coefficients \(a,-b\) on the \(g,h\) edges of the left Cayley graph have zero boundary.
Its components on \(G\) are copies of the Cayley tree of the subgroup, indexed by its right cosets.
Removing leaves in the finite support gives \(a=b=0\). [Free-tree boundary argument](Yin_L_A0076_v1.md#a-bordered-pencil-over-a-free-group-without-a-finitely-supported-kernel-vector)
Thus \(ud\in M\) forces \(d^*ud\in M\) and \(d=0\).
If \(du\in M\), taking adjoints gives \(ud^*\in M\), with the same conclusion.
In particular \(u\) has neither a nonzero group-ring left denominator nor a nonzero group-ring right denominator even if the cleared product is only required to be bounded.
This applies to the torsion-free group \(F_2\) itself.

For arbitrary infinite-order \(g,h\), the same calculation (1) holds and its right-hand ideal is nonzero exactly when the natural map \(\langle g\rangle*\langle h\rangle\to\langle g,h\rangle\) has nontrivial kernel.
Indeed a shortest nonempty freely reduced relator gives a cycle with no repeated intermediate vertex in the marked Cayley multigraph, allowing parallel edges for different labels.
Its signed edge chain is nonzero and has zero boundary, hence again yields a relation \(d_g a=d_h b\).
The common value is nonzero because both difference operators are injective and the chain is nonzero.
The free case gives the reverse implication.
This last characterization concerns the bounded sandwich \(d^*ud\); only its necessity is used to exclude single-sided denominators in the free case.

## The least Hilbert–Schmidt norm solution on the two-torus

Take the standard marking of \(\mathbb Z^2\), identify \(H=L^2(\mathbb T^2)\) by Fourier transformation, and take \(u(z)=z_1\).
For any two bounded affiliated units \(s,t\) acting by multiplication, the fraction numerators are \(su,ut\).
There is a solution of the [unrestricted equation](../claims/Yin_C_A0131_v1.md#statement) with \(T_1=-sP_et\), \(T_2=0\), so the equation is soluble in the Hilbert space of pairs of Hilbert–Schmidt operators.
The unique solution minimizing \(\|T_1\|_{\mathrm{HS}}^2+\|T_2\|_{\mathrm{HS}}^2\) has infinite rank in its first component for every such \(s,t\).

Write \(K_j(z,w)\) for the integral kernel of a Hilbert–Schmidt solution and use Haar probability measure on \(\mathbb T^2\).
Multiplication by \(z_j\) has commutator kernel \((z_j-w_j)K_j(z,w)\), so the equation is
\[
                 \sum_{j=1}^{2}(z_j-w_j)K_j(z,w)
                     =-s(z)t(w)(z_1-w_1).
\]
Away from the null diagonal, the least Euclidean norm solution at \((z,w)\) is
\[
 K_j(z,w)=-s(z)t(w)
     \frac{\overline{z_j-w_j}(z_1-w_1)}
          {|z_1-w_1|^2+|z_2-w_2|^2}.
\]
These kernels are bounded and square integrable, and pointwise orthogonality to the homogeneous solutions gives the unique Hilbert–Schmidt minimizer.
For its first component put
\[
 k(\zeta)=\frac{|1-\zeta_1|^2}{|1-\zeta_1|^2+|1-\zeta_2|^2},
 \qquad K_1(z,w)=-s(z)\,k(zw^{-1})\,t(w).
\]
Convolution by \(k\) is diagonal on torus characters with eigenvalues the Fourier coefficients of \(k\).
Finite rank would force \(k\) to agree almost everywhere with a trigonometric polynomial.
On the punctured torus \(k\) is continuous, so this agreement would hold everywhere there, by full support of Haar measure.
Approaching \((1,1)\) along the two coordinate axes gives the limits zero and one, contradicting continuity of the polynomial.
Hence convolution by \(k\) has infinite rank.
Multiplication by \(t\) has dense range and multiplication by \(s\) is injective, so the sandwiched operator in the first component also has infinite rank.
Thus for \(u\) equal to one of the two standard generators of \(\mathbb Z^2\), every choice of fractions gives a least Hilbert–Schmidt norm solution with an infinite-rank component.

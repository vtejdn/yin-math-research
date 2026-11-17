---
author: Yin
---

# A winding obstruction to dissipative determinant linearizations of the Wigner quadratic test

<a id="statement"></a>
## Failure of a multiplicity-one realization

Fix \(P(x,y)=xy+2yx\) and any fixed \(z=\alpha+i\beta\) with \(\beta\ne0\).
Consider a putative finite-dimensional linearization \(D(X,Y)=H(X,Y)+iJ(X,Y)^*J(X,Y)\) on selfadjoint inputs.
Allow arbitrary fixed auxiliary dimensions, polynomial matrices \(H=H^*,J\), and any constant scalar rotation of \(D\).
In particular the model includes affine pencils with fixed semidefinite imaginary part.
The following obstruction already holds on real symmetric matrices of size two.

There is no such realization satisfying
\[
 |\det D(X,Y)| = g(X,Y)\,|\det(P(X,Y)-zI)|^r
 \tag{Modulus}
\]
locally on the real two-dimensional evaluation disk in the proof when \(r\) is a positive odd integer and \(g\) is continuous and strictly positive there.
In particular it excludes a universally valid ordinary Schur determinant linearization of multiplicity one with a regular nonvanishing auxiliary factor at the tested tuple.
If the complex determinant identity itself is prescribed, with a continuous complex factor extending without zeros over the disk, every positive integer multiplicity is excluded.
These obstructions persist for products or ratios with any regular nonvanishing auxiliary determinants on that disk.
They concern identities required on a full neighborhood of the evaluation.
They give no counterexample to the random-matrix convergence assertion of [F0014](../tasks/Yin_T_F0014_v1.md#contract).

<a id="argument"></a>
## A two-dimensional real evaluation and the determinant argument

Take
\[
 A=\operatorname{diag}(1,-1),\qquad
 B(t,s)=\begin{pmatrix}t/3&s\\s&-t/3\end{pmatrix}.
\]
Then \(AB+2BA=\left(\begin{smallmatrix}t&-s\\s&t\end{smallmatrix}\right)\), so its shifted determinant is \((t+is-z)(t-is-z)\).
Parameterize a circle by \(t=\alpha+\rho\cos\theta,\ s=\beta+\rho\sin\theta\) with \(0<\rho<|\beta|\).
The first factor winds once around zero, and the second extends without zeros over the disk.
Thus the shifted determinant has winding number one about zero.

Along any closed curve on which \(D\) is invertible, \((1-h)D+hiI\), \(0\le h\le1\), is an invertible homotopy to a constant.
For \(h>0\) the imaginary part dominates \(hI\).
Its complex determinant therefore has winding zero along the curve.
A constant rotation leaves that winding unchanged.
A continuous factor nonzero on the full disk has winding zero on its boundary by radial contraction.
This proves the complex-determinant obstruction for any positive multiplicity.

Write \(f(t,s)=\det D(A,B(t,s))\).
It is a polynomial in two real parameters with complex coefficients.
Under (Modulus) it has an isolated zero at the center and a nonzero leading homogeneous Taylor term \(f_k\) there.
For unit real vectors \(v=(\cos\theta,\sin\theta)\) we have
\[
 |\det(P(A,B((\alpha,\beta)+\rho v))-zI)|/\rho
 \longrightarrow 2|\beta|
\]
uniformly in \(\theta\), where \(B((t,s))\) means \(B(t,s)\).
Choosing a unit vector with \(f_k(v)\ne0\) and comparing powers in (Modulus) gives \(k=r\).
For every unit \(v\), the same comparison gives \(|f_r(v)|=g(A,B(\alpha,\beta))(2|\beta|)^r>0\).
The rescaled determinant loops \(\rho^{-r} f((\alpha,\beta)+\rho v)\) converge uniformly to \(f_r(v)\), so for sufficiently small \(\rho\) the two loops have the same winding by straight-line interpolation.
For odd \(r\), \(f_r(-v)=-f_r(v)\).
A continuous lift of its argument on \([0,2\pi]\) changes from \(\theta\) to \(\theta+\pi\) by an odd multiple of \(\pi\), constant in \(\theta\) by continuity.
The total winding is therefore odd.
This contradicts the dissipative homotopy, proving (Modulus) impossible for odd \(r\).

<a id="even-doubling"></a>
## Even multiplicity and the observation of a doubled pencil

For any square polynomial \(A\), set
\[
 H=\begin{pmatrix}0&A\\A^*&0\end{pmatrix},\qquad J=(I,0).
\]
The determinant modulus of \(H+iJ^*J\) is \(|\det A|^2\), by eliminating the top-left block \(iI\).
Its first two stacked observation rows are \(\operatorname{diag}(I,A)\), and each row \(JH^d\) is a polynomial left multiple of this diagonal matrix.
Indeed even powers give \(((AA^*)^l,0)\) and odd powers give \((0,(AA^*)^l A)\).
The rows of the larger stack \((H^{\mathsf T},J^{\mathsf T})^{\mathsf T}\), understood as vertical stacking of \(H\) and \(J\), generate the same left polynomial row module.
Its rows include \((I,0)\) and \((0,A)\), and the remaining block \((A^*,0)\) is a left multiple of the first.

This factor persists after adjoining a Hermitian polynomial block \(T\) with polynomial inverse to \(H\), extending \(J\) by zero on the new coordinates, and replacing the enlarged pair \((H',J')\) by \((S^*H'S,J'S)\) for any polynomially invertible square \(S\).
Left multiplication of the two raw row blocks by \(\operatorname{diag}(S^*,I)\) is reversible by polynomial operations.
Every square polynomial combination of the transformed raw stack consequently has the form
\[
 B=M\,\operatorname{diag}(I,A,I)\,S
 \tag{Stable}
\]
for a square polynomial \(M\) of the lifted size, with the last identity omitted in the absence of \(T\).
The same applies to polynomial combinations of the transformed observation rows, since all positive powers end in a right factor \(S^*H'S\).
One may choose a square raw-stack combination exactly equal to \(\operatorname{diag}(I,A,I)S\).
Iterating stabilization and congruence preserves the same form after a permutation and further enlargement of \(S\).

For the [Wigner logarithmic problem](../tasks/Yin_T_F0013_v1.md#contract), a witness (Stable) converging in probability along a given subsequence to its finite free log determinant already forces the corresponding probability limit for \(A\) along that subsequence.
Use total logarithms divided by physical dimension \(N\), so block embeddings add without scalar weights.
Their free versions use the unnormalized auxiliary trace times the free state, equivalently auxiliary size times the normalized FK logarithm.
Finite multiplicativity gives addition of the three factors, and [bounded FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) gives the same free identity.
A finite total free logarithm forces each of the three terms to be finite, since all free factors are bounded.
At finite size invertibility of \(B\) holds with probability tending to one and implies invertibility of all factors on that event.
The [upper bound for fixed polynomial logarithms](../ledger/Yin_L_F0061_v2.md#upper-limit) gives vanishing probability for any positive overshoot of any factor.
If the logarithm of \(A\) falls at least \(\eta>0\) below its target while both others overshoot by at most \(\eta/4\), the sum falls at least \(\eta/2\) below its target.
Probability convergence for the sum thus rules out that lower deviation of \(A\).

The calculation concerns the canonical even lift and its stated stabilizations.
The winding argument permits other even-multiplicity modulus realizations, and a direct probability estimate may exploit structure of a particular representation.

## Assessment history

### Decision winding-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:33 |
| status | proved |
| reason | The local winding proof, the odd-multiplicity modulus obstruction and the canonical even doubling were independently verified. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete stated conclusions under the specified hypotheses. |
| argument | [Proof](#argument) | Full mathematical argument for this version. |
| support | [Even multiplicities](#even-doubling) | The canonical doubling and the retained target factor. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0359_v1.md#winding) | Complete fixed statement, proof and applicability boundaries. |

## Current assessment

[Selected decision](#decision-winding-reviewed)

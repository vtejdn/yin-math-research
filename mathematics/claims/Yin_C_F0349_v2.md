---
author: Yin
---

# No multiplicity-one dissipative determinant realization of the quadratic test at any prescribed shift

<a id="statement"></a>
## Real and nonreal shifted determinants

Let \(P(x,y)=xy+2yx\), fix \(z\in\mathbb C\), and consider an exact determinant realization by a fixed square matrix polynomial \(D(X,Y)=H(X,Y)+iJ(X,Y)^*J(X,Y)\) with \(H=H^*\).
Any fixed scalar rotation of \(D\) is allowed.
For \(z\notin\mathbb R\) the [two-dimensional real symmetric disk](Yin_C_F0349_v1.md#argument) excludes the following modulus identity of any positive odd multiplicity \(r\).
For **every real** \(z\), including \(z=0\), the same exclusion holds on a real two-dimensional disk of **complex Hermitian** matrices of size three:
\[
 |\det D(X,Y)|=g(X,Y)\,|\det(P(X,Y)-zI)|^r,
 \tag{1}
\]
where \(g\) is continuous and strictly positive on that disk.
For identities of complex determinants with a continuous factor extending without zeros over the disk, every positive integer multiplicity is excluded.
A product or quotient with auxiliary determinants regular and nonzero throughout the disk is covered by these factor conditions.
For fixed \(z\), the disk can be embedded in every higher common matrix size.
These obstructions concern dissipative exact realizations at a fixed parameter of [F0014](../tasks/Yin_T_F0014_v1.md#contract).
The earlier [stable even-lift factorization](Yin_C_F0349_v1.md#even-doubling) remains at its stated class of representations.

<a id="argument"></a>
## Winding and modulus at a transverse real-parameter zero

For completeness suppose \(f:\mathbb R^2\to\mathbb C\) is smooth, \(f(0)=0\) and its real Jacobian \(T\) is invertible at zero.
On the circle \(\rho v\), \(|v|=1\), we have \(f(\rho v)=\rho T v+o(\rho)\) uniformly in \(v\), with \(\min_{|v|=1}|Tv|>0\).
For small \(\rho\) this loop is nonzero and has winding \(\operatorname{sign}\det_{\mathbb R}T\).
Indeed its linear approximation traces a nondegenerate ellipse with that orientation, and straight-line interpolation preserves nonvanishing.

Suppose a polynomial evaluation on this real parameter plane gives \(h=\det D\) with \(|h|=g|f|^r\), \(g(0)>0\) and \(g\) continuous.
The lowest nonzero homogeneous Taylor polynomial \(h_k\) of \(h\) has degree \(k=r\), by considering a ray where \(h_k\) is nonzero.
Moreover \(|h_r(v)|=g(0)|Tv|^r>0\) on the entire unit circle.
Small circles of \(h\) consequently have the winding of \(h_r\), by uniform approximation and straight-line interpolation.
For odd \(r\), \(h_r(-v)=-h_r(v)\), so the increment of a lifted circle argument on each half-circle is a constant odd multiple of \(\pi\).
The total winding is odd.
On the other hand, every invertible loop of dissipative matrices has determinant winding zero by the contractive homotopy \((1-t)D+tiI\) for \(0\le t\le1\), which is strictly dissipative for \(t>0\).
A fixed rotation of \(D\) does not alter the winding.
Thus the modulus identity is impossible for odd \(r\).
In the complex-determinant version the winding is \(r\operatorname{sign}\det_{\mathbb R}T\), since the factor extending invertibly over the disk has zero winding.
This yields the obstruction for every positive integer \(r\).

<a id="real-test"></a>
## Real shifts on a three-dimensional Hermitian evaluation

Fix real \(z\) and put \(d=1+|z|\).
Take
\[
 A=\operatorname{diag}(1,2,3),\qquad
 B(t,s)=
 \begin{pmatrix}
 t&1+is&1\\
 1-is&0&d\\
 1&d&0
 \end{pmatrix},
 \qquad t,s\in\mathbb R .
\]
Writing \(a_j=A_{jj}\), we have \(P(A,B)_{ij}=(a_i+2a_j)B_{ij}\).
The minor deleting row and column one of \(P(A,B)-zI\) has determinant \(z^2-56d^2\).
For \(f(t,s)=\det(P(A,B(t,s))-zI)\), the transposition terms involving \(B_{12},B_{21}\) depend on \(1+s^2\), and the two three-cycles give \(200d(1+is)\) and \(196d(1-is)\).
Equivalently, direct expansion yields
\[
 f(t,s)=(3t-z)(z^2-56d^2)+20z(1+s^2)+35z+396d+4ids .
\]
Set \(t_0=(z-(55z+396d)/(z^2-56d^2))/3\).
Then \(t_0\) is well-defined and real, \(f(t_0,0)=0\), and the two coordinate derivatives there are \(3(z^2-56d^2)\) and \(4id\).
These give an invertible real Jacobian with negative determinant.
The previous argument applies on every sufficiently small disk centered at \((t_0,0)\).
In particular at \(z=0\) the derivative in the imaginary direction stays nonzero.

<a id="larger-sizes"></a>
## Larger dimensions and the scope of the model

For \(z\notin\mathbb R\) the [real symmetric two-by-two test](Yin_C_F0349_v1.md#argument) gives a transverse zero with the opposite orientation for its stated circle.
It remains a Hermitian test.
Any of the disks extends to dimension \(N\) at least the dimension \(n\) of the test, by adjoining a common scalar pair \(A'=1,B'=b\) on each of \(N-n\) additional coordinates with \(3b-z\ne0,\ b\in\mathbb R\).
For example take \(b=0\) if \(z\ne0\), and take \(b=1\) when \(z=0\).
The target determinant gains the nonzero constant factor \((3b-z)^{N-n}\).
Restriction of the proposed identity to this enlarged disk again gives a contradiction, even when one only proposes the identities in all sufficiently large even dimensions.

At fixed real \(z\), restricting both inputs to real symmetric matrices would instead make their scalar shifted determinant real throughout the parameter plane.
The three-by-three test uses complex Hermitian off-diagonal entries, which the full Task permits.
For a polynomial identity with a globally continuous nonvanishing factor, equality almost surely under a within-size law of full Hermitian support would imply equality on the entire Hermitian space by continuity.
A complex Gaussian Wigner law supplies such support, also at arbitrarily large even sizes.
The result leaves modulus identities of even multiplicity and estimates specific to random original inputs as separate possibilities.

## Current assessment
[Selected decision](#decision-all-shift-winding-reviewed)

## Assessment history

### Decision all-shift-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:34 |
| status | open |
| reason | The three-dimensional Hermitian disk extends the winding obstruction to every real parameter under the unrestricted Hermitian input scope and awaits independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All prescribed shifts](#statement) | Odd modulus multiplicities and all positive complex multiplicities at real and nonreal shifts on the indicated input disks. |
| argument | [Transverse winding argument](#argument) | Uniform Taylor comparison and dissipative homotopy. |
| support | [Three-dimensional real-shift test](#real-test) | Exact Hermitian computation for every real shift. |
| dependency | [Nonreal two-dimensional test](Yin_C_F0349_v1.md#argument) | Real symmetric evaluation for each nonreal shift. |

### Decision all-shift-winding-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:40 |
| status | proved |
| reason | Every prescribed complex shift admits a transverse Hermitian test excluding the specified multiplicities. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete fixed statement and quantifiers. |
| argument | [Proof](#argument) | Complete fixed mathematical argument. |
| support | [Three-dimensional test for real parameters](#real-test) | Three-dimensional test for real parameters. |
| support | [Stabilization and full-support laws](#larger-sizes) | Stabilization and full-support laws. |
| dependency | [Nonreal shifts on the real symmetric disk](Yin_C_F0349_v1.md#argument) | Nonreal shifts on the real symmetric disk. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0359_v2.md#all-shifts) | All stated conclusions at the specified scope. |

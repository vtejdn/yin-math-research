---
author: Yin
---
# Three fixed diagonal perturbations detect fractional column rank

## Statement

Fix a discrete group \(G\), put \(R=\mathbb C[G]\), and use left convolution, the canonical trace and its unnormalized matrix extension as in the [Atiyah Task](../tasks/Yin_T_A0001_v1.md#contract).
Write \(\nu\) for regular kernel dimension and \(E=E_{11}\) in each square matrix size.
The following two properties of this one group are equivalent.

1. Every finite matrix over \(R\) has integer regular rank.
2. Every finite Hermitian matrix \(H\) over \(R\) satisfies
   \[
   \min\{\nu(H),\nu(H-E)\}\ \leq\ \nu(H-2E).
   \tag{1}
   \]

If adjoining a column \(v\) to an \(m\)-by-\(n\) matrix \(B\) increases its rank by \(d\in(0,1)\), the proof constructs a Hermitian matrix of size \(m+n+2\) over \(R\).
Above a common baseline its three nullities are \(d,1-d,0\).
For an arbitrary Hermitian pencil \(H-\lambda E\), measure excess nullity above the dimension of its common kernel on the hyperplane with first coordinate zero.
The sum of the excess nullities at distinct real parameters is at most one.

Restricting (1) to positive \(H\) with \(H_{11}\leq 1\) is equivalent to regular injectivity of every nonzero **scalar** in \(R\).
For amenable groups the [finite scalar descent](Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) identifies that property with item 1.

## Argument

Use the affiliated ring \(U=\mathcal U(G)\).
For a bounded matrix \(T\), its right-module kernel in \(U\) is \(1_{\ker T}U^n\), and its algebraic image in \(U^m\) is the module of its closed Hilbert range projection.
Indeed the inverse on the support from polar decomposition gives the affiliated Moore–Penrose inverse \(T^\dagger\), with \(TT^\dagger\) and \(T^\dagger T\) the range and initial projections.
These identities hold for affiliated matrices as well, using closed products. Dimension is additive on the resulting split finite projective modules.

### The atom formula

Write \(H=\left(\begin{smallmatrix} u&w^*\\w&D\end{smallmatrix}\right)\), \(P=1_{\ker D}\), \(e=1_{\ker(Pw)}\) and \(c=\dim_U(\ker D\cap\ker w^*)\), with the kernels in this formula taken over \(U\).
The lower equation \(wx+Dy=0\) requires \(x\in eU\), and all its solutions are \(y=-D^\dagger wx+z\) with \(z\in PU^{m-1}\), where \(m\) here denotes the size of \(H\).
As \(z\) varies, \(w^*z\) fills \((1-e)U\), by the range projection of \((Pw)^*\).
Thus the first coordinate of a solution may be any vector in the \(\lambda\)-eigenmodule of
\[
 S=e(u-w^*D^\dagger w)e\quad\text{in }eUe .
\]
The solutions with first coordinate zero have dimension \(c\).
Since \(S\) is selfadjoint in the affiliated corner, the excess \(\nu(H-\lambda E)-c\) is the trace of its spectral projection at \(\lambda\) **in that corner**.
The formula includes \(e=0\) with zero excess and the size-one case with \(c=0,e=1\).
Distinct real eigenprojections are orthogonal and their sum has trace at most \(\tau(e)\leq1\).
Under item 1, both \(\nu(H-\lambda E)\) and \(c\) are integers, since \(c\) is the nullity of the stacked group-ring matrix with rows \(D,w^*\).
At most one parameter can therefore have positive excess, proving (1).

### A witness over the original group ring

If some matrix has noninteger rank, adding its columns successively gives an increment strictly between zero and one: each increment is in \([0,1]\) by projection onto the orthogonal complement of the previous range.
Use the preceding columns as \(B\) and the new column as \(v\), allowing \(n=0\).
For \(Q=1_{\ker B^*}\), let \(p=1_{\ker(Qv)}\).
The decomposition of the augmented range over \(U\) gives \(d=\operatorname{rank}(Qv)=1-\tau(p)\).
In block sizes \(1,1,n,m\) take
\[
 H-\lambda E =
 \begin{pmatrix}
 -\lambda&1&0&0\\
 1&-1&0&v^*\\
 0&0&0&B^*\\
 0&v&B&0
 \end{pmatrix}.
 \tag{2}
\]
Its four equations on \((x,y,z,w)\) give \(y=\lambda x,\ x-y=-v^*w,\ B^*w=0,\ vy+Bz=0\).
The last equation is solvable in \(z\) precisely when \(y\in pU\).
The middle two equations are solvable in \(w\) precisely when \(x-y\in(1-p)U\), since \(\operatorname{im}(v^*Q)=(1-p)U\).
The orthogonal splitting of \(x\) thus forces \(y=px\), and every \(x\) with \(px=\lambda x\) lifts to a solution.
Projection onto \(x\) has kernel of dimension \(c_0=\nu(B)+\nu([v\ B]^*)\), independently of \(\lambda\).
At \(0,1,2\) the excess over \(c_0\) is respectively \(d,1-d,0\).
This contradicts (1) for a fractional increment.
In particular the violating matrices use only the original group-ring entries, their adjoints, signs, zero and one.

### Positive matrices with a bounded first diagonal entry

For \(0\le H\) with \(u\le1\), positivity forces \(Pw=0\): the quadratic form vanishes on \((0,P\xi)\), so \(H^{1/2}(0,P\xi)=0\).
The formula above now has \(e=1\). Completing the square over \(U\) gives \(S=u-w^*D^\dagger w\ge0\) by triangular congruence of \(H\) with \(\operatorname{diag}(S,D)\).
Since \(D^\dagger\ge0\), \(S\le u\le1\), and \(S\) is bounded.
Its eigenspace at one is \(\ker(1-u)\cap\ker w\): the two summands \(1-u\) and \(w^*D^\dagger w\) in \(1-S\) are positive, and \(w\) takes values on the support of \(D\).
The kernel identity follows by writing the second form as \(((D^\dagger)^{1/2}w)^*((D^\dagger)^{1/2}w)\) over \(U\).
If nonzero scalars over \(R\) act injectively, positive mass at one forces \(u=1\) and every entry of \(w\) to vanish.
Then \(S=1\) has no mass at zero. In all cases the endpoint test (1) holds.
Conversely, for a nonzero scalar \(a\in R\) of nullity \(\alpha>0\), faithfulness gives \(\alpha<1\).
Use the Gram matrix \(H=[1\ \ a]^*[1\ \ a]\).
Its lower block is \(a^*a\), its baseline is \(\alpha\), and \(S=1-a(a^*a)^\dagger a^*\) is the kernel projection of \(a^*\), of trace \(\alpha\).
The three nullities are \(1,2\alpha,\alpha\), which violate (1).

## Scope for the torsion-free problem

The unrestricted test keeps the group fixed and needs three evaluations of a single pencil.
The corresponding [wreath-product test](Yin_C_A0017_v2.md#statement) varies the ambient group and asks for a lower bound over all matrix sizes.
The spectral mass bound alone permits both \(d\) and \(1-d\) to be positive.
To establish (1) for every torsion-free group one must independently exclude their simultaneous occurrence for the group-ring inputs in (2).

## Assessment history

### Decision three-point

| Field | Value |
| --- | --- |
| date | 2026-11-16T23:23 |
| status | proved |
| reason | The independent review covers the complete fixed statement and proof at the indicated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Three-point rank comparison, the original-group witness and the positive normalized restriction. |
| argument | [Proof](#argument) | All parameter, rank, Gram and source interfaces in the statement. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0049_v1.md#whole-argument-finding) | Independent review of the complete claim, including its limits for A0001. |

## Current assessment

[Selected decision](#decision-three-point)

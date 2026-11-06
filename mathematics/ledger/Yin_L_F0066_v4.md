---
author: Yin
---

# Fixed skew probes cannot control a rank-three symmetric addition

This ordinary proof-development comparison was obtained for Yin on 2026-11-05 while investigating the remaining purely imaginary branch of [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract).
It strengthens the specific coordinate-pair obstruction in [C_F0194_v9](../claims/Yin_C_F0194_v9.md#rank-three-boundary) to every prescribed finite family of supported skew updates.
It is not an independent review, a novelty claim or a counterexample to the random Wigner floor.
The earlier [cofactor comparison](Yin_L_F0066_v1.md), [complex orientation boundaries](Yin_L_F0066_v2.md) and [transpose-pair mixed-moment obstruction](Yin_L_F0066_v3.md) retain their separate fixed scopes.
The elementary finite-rank determinant identity used below is the one proved in [C_F0194_v9](../claims/Yin_C_F0194_v9.md#finite-rank-identities); the new obstruction is calculated explicitly here.

<a id="finite-skew-probe-obstruction"></a>
## The failed deterministic implication

Fix any finite list of complex transpose-skew matrices \(B_1,\ldots,B_m\in M_3(\mathbb C)\), independently of the matrix to be tested.
There exist \(U\in M_{6,3}(\mathbb C)\) and an invertible complex transpose-skew \(A\in M_6(\mathbb C)\) such that
\[
 U^*U=I_3,\qquad \|A\|,\|A^{-1}\|\le2,
 \qquad A+UU^T\text{ is singular},
\]
while every \(A+UB_jU^T\) is invertible.
The same construction extends to every even order \(N\ge6\), preserving those bounds and positive lower bounds on the least singular values of the finitely many test matrices that depend only on the fixed list.
In particular, replacing the six coordinate-pair tests in C_F0194_v9 by another fixed finite list of skew forms cannot establish the corresponding deterministic invertibility implication.

Write
\[
 K(k)=\begin{pmatrix}0&k_1&k_2\\-k_1&0&k_3\\-k_2&-k_3&0\end{pmatrix},
 \qquad
 B(b)=\begin{pmatrix}0&b_1&b_2\\-b_1&0&b_3\\-b_2&-b_3&0\end{pmatrix}.
\]
Expansion of the two three-by-three determinants gives
\[
 \det(I_3+K(k))=1+k_1^2+k_2^2+k_3^2,
 \qquad
 \det(I_3+B(b)K(k))=(1-b_1k_1-b_2k_2-b_3k_3)^2.
 \tag{Probe-identities}
\]
For the second equality, the trace of \(BK\) is \(-2b\cdot k\), the sum of its two-by-two principal minors is \((b\cdot k)^2\), and its determinant vanishes because both skew factors have rank at most two.
These formulas use complex bilinear squares and no conjugation.

For a nonnegative integer \(t\), put
\[
 D(t)=1+t^2+t^4,\qquad
 k(t)=\frac{i}{D(t)}\bigl(2t,2t^2,1-t^2-t^4\bigr).
 \tag{Rational-witness}
\]
Direct expansion gives \(k_1(t)^2+k_2(t)^2+k_3(t)^2=-1\).
For a fixed \(b\), the equation \(1-b\cdot k(t)=0\) is equivalent to the vanishing of
\[
 P_b(t)=(1-i b_3)-2i b_1t+(1+i b_3-2i b_2)t^2+(1+i b_3)t^4.
\]
This polynomial is never identically zero: its constant and fourth-degree coefficients sum to two.
It therefore has at most four distinct roots, by repeated division by a linear factor.
Among the \(4m+1\) integers \(0,\ldots,4m\), choose one avoiding the roots of all \(P_{b_j}\).
For this \(t\), \(D(t)>0\), and every second determinant in (Probe-identities) is nonzero while the first is zero.
The case of an empty list permits \(t=0\).

Set \(K=K(k(t))\) and
\[
 U=\binom{I_3}{0},\qquad
 A=\begin{pmatrix}0&-I_3\\I_3&K\end{pmatrix},\qquad
 A^{-1}=\begin{pmatrix}K&I_3\\-I_3&0\end{pmatrix}.
\]
Multiplication verifies the inverse and transpose skewness.
Writing \(k=i r\), the vector \(r\) is real and has Euclidean norm one.
For the real skew matrix \(K(r)\), direct multiplication gives \(K(r)^*K(r)=I_3-vv^T\) with \(v=(r_3,-r_2,r_1)^T\), so \(\|K\|=1\).
Each displayed six-by-six matrix is a skew orthogonal block matrix of norm one plus one block of norm one, giving the asserted bounds of two.
The finite-rank determinant identity now yields
\[
 \det(A+UU^T)=\det A\det(I_3+K)=0,
 \qquad
 \det(A+UB_jU^T)=\det A\det(I_3+B_jK)\ne0.
\]
Taking direct sums with copies of \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) and padding \(U\) by zero rows proves the all-even-dimensional assertion.
For a fixed list, the finitely many invertible six-by-six matrices have a positive minimum least singular value; direct sum takes its minimum with one.

<a id="scope-and-next-step"></a>
## What the obstruction changes

The rank-two proof factors its small determinant into two linear factors, each detected by a fixed skew perturbation.
At rank three, arbitrary fixed supported skew probes detect only finitely many hyperplanes \(b\cdot k=1\), while the explicit curve above stays on the singular symmetric-addition locus and avoids them all.
Thus adding more fixed probes of this form does not repair that deterministic method.
A method using a dimension-growing family with quantitative mesh control, adaptive probes, additional random information about \(K=U^TA^{-1}U\), or a different identity is not ruled out here.
The construction supplies no small probability estimate for that random compression.
In particular, setting a shift equal to the constructed \(A-W_N\) would destroy its required independence from the Wigner input, so this calculation is no counterexample to any original Task or arbitrary-shift random theorem.
The viable remaining target is direct anti-concentration of \(\det(I_3+U^TA^{-1}U)\), or a genuinely different way to avoid that denominator, rather than a larger fixed list of the same skew tests.

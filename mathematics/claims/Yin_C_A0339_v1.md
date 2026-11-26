---
author: Yin
---

# A spectral radius test for the exceptional order-twenty transfers

## Statement

Consider the [normalized exceptional transfer](Yin_C_A0336_v1.md#a-circle-valued-scalar-square-of-the-transfer) of the noncyclic order-twenty marking, with its two actual generators \(g,h\).
Write \(M=PQ^{-1}\) for the complex two-square transfer, \(U=g^{-1}M(h)\) for the bounded operator in \(M_2(\mathcal N(H))\), and \(\operatorname{Tr}\) for the regular trace with unnormalized matrix trace.
Assume \(H\) is torsion-free with regular scalar group-ring injectivity.

If \(U\) is power bounded in the forward direction, the rectangle \(P(h)-gQ(h)\) cannot have nullity \(1/2\).
In particular this excludes the half kernel under [bounded similarity to a unitary or the constant positive form condition](Yin_C_A0336_v2.md#a-necessary-group-relation-for-a-unitary-twisted-transfer).

More generally, if the rectangle has a half kernel and the spectral radius of \(U\) is at most one, no integers \(i,j\ge0\) give \(g^{-1}h^i g^{-1}h^j=1\).
For every integer \(n\ge1\) one then has
\[
                       \operatorname{Tr}(U^{2n})=1+(-1)^n .
\]
In particular there is a four-step return \(\prod_{k=1}^4 g^{-1}h^{i_k}=1\) with \(i_k\ge0\), in the indicated order.
Thus a half kernel forces spectral radius strictly greater than one if a two-step return exists or if every four-step return is absent.
These restrictions apply also when the commutator subgroup is perfect.

## A central trace disk at spectral radius one

Assume a half kernel and write \(p\) for the orthogonal projection onto \(\ker(U^2-I)\).
The sign fixing \(h\) and negating \(g\) gives eigenspaces at \(1,-1\) each of dimension \(1/2\), and the two linear interpolation polynomials decompose this kernel, so \(\operatorname{Tr}(p)=1\).
In fact for every central projection \(c\in\mathcal N(H)\) one has \(\operatorname{Tr}(cp)=\tau(c)\), where \(\tau\) is the scalar regular trace.
Indeed the [group-ring multiple of \(U^2-I\)](Yin_C_A0330_v1.md#a-rank-one-matrix-with-no-polynomial-syzygies) has affiliated units on its two outside factors and a nonzero group-ring entry.
Its column containing this entry is injective from one coordinate by scalar injectivity, also upon restriction to \(c\).
Thus on \(c\) its rank is at least \(\tau(c)\).
The outside factors preserve affiliated rank on every such cut.
The same lower bound on \(1-c\), together with global rank one, gives equality on each cut and the assertion about \(p\).

Put \(q=I-p\) and \(T=qU^2q\) in its corner, whose unit \(q\) has trace one.
The block form of \(U^2\) relative to \(p,q\) is upper triangular with diagonal blocks \(p,T\).
In particular \(T^n=qU^{2n}q\) and its spectral radius is at most one under the stated radius hypothesis.
For \(\rho>1\) the norm-convergent positive operator \(D_\rho=\sum_{n\ge0}\rho^{-2n}T^{*n}T^n\), with zeroth term \(q\), is invertible in the corner.
The identity \(T^*D_\rho T=\rho^2(D_\rho-q)\) makes \(X_\rho=D_\rho^{1/2}TD_\rho^{-1/2}/\rho\) a contraction.

If \(C\le Z(H)\) is cyclic, let \(\Theta_C\) denote ordinary matrix trace followed by the trace-preserving expectation onto \(\mathcal N(C)\).
This map is tracial since the target is central and pairing with each target coefficient reduces to ordinary trace cyclicity.
The cut identity gives \(\Theta_C(p)=\Theta_C(q)=1\).
For a contraction \(X\) in the corner, positivity applied to \(\operatorname{Re}(e^{i\theta}X)\le q\) for all angles gives \(|\Theta_C(X)|\le1\).
Use \(X_\rho\), traciality and \(\rho\downarrow1\).
It follows that
\[
                              |\Theta_C(U^2)-1|\le1
\]
almost everywhere on the dual of \(C\).

## Central coefficients of two-step words

Suppose \(g^{-1}h^i g^{-1}h^j=1\) with \(i,j\ge0\).
Then \(a=g^{-1}h^i\) satisfies \(a^2=h^{i-j}\).
As \(a,h\) generate \(H\), this power is central.
If \(i=j\), torsion-freeness would give \(a=1\), making \(H\) cyclic contrary to its marked quotient.
Let \(r\) be the positive generator of \(\{k:h^k\in Z(H)\}\), and put \(C=\langle h^r\rangle\).
For any other return with integer exponents \(i+k,j+l\), its equation is \(ah^ka^{-1}=h^{-l}\).
Raising to the \(r\)-th power gives \(k=-l\), since \(h\) has infinite order.
Hence \(a\) commutes with \(h^k\), exactly when \(r\mid k\).
Conversely all \((i+kr,j-kr)\) return.
Interchanging \(i,j\) is also a return by cyclic permutation.
Consequently both belong to one residue class \(e\bmod r\), \(0\le e<r\), and \(i+j=2e+wr\) with \(w\ge1\), since \(w=0\) would give \(i=j=e\).

Write \(M(y)=\sum_{k\ge0}M_k y^k\) and \(F_e(z)=\sum_{k\ge0}M_{e+kr}z^k\).
These series converge absolutely on a neighborhood of the closed disk.
A word \(g^{-1}h^b g^{-1}h^d\) equals \(h^{vr}\) if and only if \((b,d-vr)\) returns.
By the preceding classification this happens precisely when \(b=e+kr,\ d=e+lr,\ v=k+l-w\), for integers \(k,l\).
Taking the expectation of the absolutely convergent product \(U^2\) and identifying \(h^r\) with the circle coordinate \(z\) therefore gives
\[
            \Theta_C(U^2)(z)=z^{-w}S_e(z),\qquad
            S_e(z)=\operatorname{tr}\big(F_e(z)^2\big).
\]
The trace disk now gives \(|S_e(z)-z^w|\le1\) everywhere on the circle by continuity.

Here \(M(y)^2=B(y)I\) and \(\operatorname{tr}M(y)=0\), with \(B\) the explicit degree-two Blaschke product of the normalized orientation.
Its two simple poles are the roots of \(\det Q\), both outside the closed disk.
The entries of \(M=P\,\operatorname{adj}(Q)/\det Q\) have numerator degree at most two, so \(M\) is bounded at infinity and has a partial fraction decomposition
\[
             M(y)=M_\infty+\frac{L_1}{1-d_1y}+\frac{L_2}{1-d_2y},
                         \qquad 0<|d_1|,|d_2|<1 .
\]
Each \(L_j\) is nonzero because \(B\) has a pole there, and \(L_j^2=0\) by the absence of a double pole in \(M^2\).
Also \(\operatorname{tr}(L_1L_2)\ne0\).
Indeed a nonzero square-zero two-square matrix has the same line as kernel and image.
Writing both as rank-one tensors shows that zero product trace forces these lines to agree, hence the matrices to be proportional.
Then \(M(y)\) takes values in a span of two constant matrices.
Normalize this span on the left by one invertible value of \(M\).
It then contains the identity and has a common eigenline by choosing an eigenvector of the other matrix, so \(M\) sends a fixed line into a fixed line.
The [constant point correspondence](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) excludes fractional rank.

For \(e>0\) it follows that
\[
 S_e(z)=\frac{2(d_1d_2)^e\operatorname{tr}(L_1L_2)}
                  {(1-d_1^rz)(1-d_2^rz)} .
\]
It has winding number zero on the circle, with no zeros or poles on the closed disk.
Yet \(z^{-w}S_e(z)\) takes nonzero values in the disk of radius one about one and therefore has winding number zero, forcing \(w=0\).
For \(e=0\) one has \(F_0(z)=M_\infty+\sum_j L_j/(1-d_j^r z)\), again bounded at infinity.
Now \(S_0(0)=\operatorname{tr}(M(0)^2)=2B(0)=1\).
The holomorphic function \(S_0(z)-z^w\) takes the value one at zero and has boundary modulus at most one.
It is identically one by the maximum principle.
The rational identity \(S_0(z)=1+z^w\) contradicts boundedness at infinity.
This excludes every two-step return.

## Moments without a two-step return

Without such a return, the Taylor series gives \(\operatorname{Tr}(U^2)=0\), hence \(\operatorname{Tr}(T)=-1\).
With the normalized corner trace \(\operatorname{Tr}|_{q}\) and its \(L^2\) norm, the contractions above satisfy
\[
                   \|X_\rho+q\|_2^2
                       \le 2+2\operatorname{Re}\operatorname{Tr}(X_\rho)
                       =2-2/\rho .
\]
For each fixed \(n\), telescoping the difference of the powers of \(X_\rho,-q\) bounds its \(L^2\) norm by \(n\|X_\rho+q\|_2\).
By tracial invariance under similarity, \(\operatorname{Tr}(T^n)=\rho^n\operatorname{Tr}(X_\rho^n)\).
Taking \(\rho\downarrow1\) gives \((-1)^n\).
The upper triangular form gives the stated moments of \(U\).
Absolute convergence of the four Taylor series and \(\operatorname{Tr}(U^4)=2\) force an actual four-step return.

Finally suppose \(\sup_{n\ge0}\|U^n\|<\infty\), which gives the spectral radius hypothesis.
The means \(A_N=N^{-1}\sum_{n=0}^{N-1}(-U^2)^n\) are uniformly bounded, and \((I+U^2)A_N\to0\) in norm by telescoping.
Every weak operator cluster point therefore has range in \(\ker(I+U^2)\).
This kernel splits by interpolation at \(i,-i\) and is zero by the [three-eigenspace budget](Yin_C_A0329_v1.md#statement), since the two eigenspaces at \(1,-1\) exhaust dimension one.
On the other hand the moment formula gives \(\operatorname{Tr}(A_N)\to1\), impossible since the regular matrix trace is a finite sum of vector functionals and the bounded means have a weak cluster point.

## Assessment history

### Decision central-trace-disks-and-spectral-radius-one

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:25 |
| status | proved |
| reason | The central trace and the two opposite geometric pole residues exclude the two-step word and force all the stated moments. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The central trace and the two opposite geometric pole residues exclude the two-step word and force all the stated moments. |
| argument | [A central trace disk at spectral radius one](#a-central-trace-disk-at-spectral-radius-one) | A central trace disk at spectral radius one. |
| argument | [Central coefficients of two-step words](#central-coefficients-of-two-step-words) | Central coefficients of two-step words. |
| argument | [Moments without a two-step return](#moments-without-a-two-step-return) | Moments without a two-step return. |
| review | [Central trace disks and spectral radius one](../audits/reviews/Yin_R_A0233_v1.md#central-trace-disks-and-spectral-radius-one) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-central-trace-disks-and-spectral-radius-one)

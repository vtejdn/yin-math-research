---
author: Yin
---

# Two simultaneous obstructions to sufficient packing tests for free Haar coordinates

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(U,Y\) be free Haar unitaries in their generated tracial von Neumann algebra \(M\), with normalized faithful trace \(\tau\), and write \(N=W^*(Y)\).
The pair satisfies actual ACSY with vacua \(U,Y\) and has strong duals in both orientations.
There is a fixed normal \(b\in N\) with exactly four spectral values such that the exact projections
\[
       e_r=1_{[0,r]}(|U-b|),\qquad t_r=\tau(e_r)
\]
have \(t_r>0\) for every \(r>0\) and \(t_r\to0\) as \(r\downarrow0\).
They satisfy both of the following assertions.

1. Uniformly in unitaries \(V,W\in N\),
   \[
      \inf\sigma(\operatorname{Re}(V^*(U-b)W))\le-1/4 .
   \]
   In particular no fixed \(\kappa\) fulfills the [omitted-unitary half-plane hypothesis](Yin_C_F0231_v1.md#statement) as \(r\downarrow0\).
2. For every \(r\) with \(t=t_r\le 1/2\), \(e=e_r\), and every \(c\in N\),
   \[
          \|(b-c)e\|_2+\|[c,e]\|_2
                \ge \tfrac14\sqrt{t(1-2t)} .                           \tag{1}
   \]
   In particular even \(\|[b,e_r]\|_2/(r\sqrt{t_r})\) diverges.
   For every finite-spectrum approximant \(c\in N\) and every spectral partition in the [locally finite-spectrum estimate](Yin_C_F0233_v1.md#statement), its quantities satisfy
   \[
            \frac{mR}{r}\ \ge\ 1+\frac{\sqrt{1-2t_r}}{4r}.
   \]
   Thus the best possible approximation criterion there fails along these exact projections.

As a separate example on the same free Haar pair, taking \(b_j=\lambda_jY\) with scalar \(|\lambda_j|=1\) gives orthogonal nonzero exact singular projections for suitable radii \(r_j\downarrow0\).
On this family the exact optimum \(\inf_c m_jR_j/r_j=1+1/r_j\) holds over all normal finite-spectrum approximants.
The fixed four-value example supplies simultaneous failure on nested projections, while this last family supplies orthogonal tests for the approximation obstruction.
Neither conclusion asserts divergence of the actual packing sum.

## Argument

### Free coordinates and the modulus of the shift

The [Haar factor and reduced-word vacuum computation](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) gives the actual vacua \(U,Y\).
Applying the [free normal estimate](Yin_C_F0162_v1.md#statement), part B, to the pair and its free Haar adjoints gives the bounded-vector domain duals in the two orientations.

Partition the circle of \(Y\) into four successive equal arcs.
Let \(q\in N\) indicate the first two arcs and let \(D_0\in N\) equal \(+1,-1,+1,-1\) on the four arcs respectively.
Then \(\tau(q)=1/2\), and the conditional expectation of \(D_0\) on \(B=\mathbb Cq+\mathbb C(1-q)\) is zero.
Set
\[
          l=\tfrac14,\qquad H=2,\qquad h=lq+H(1-q),\qquad b=D_0h .
\]
This is a selfadjoint four-value shift in \(N\), with \(\mathbb E_B b=0\).

For any unitary \(w\in N\), \(w^*U\) is Haar and free from \(N\), by the free-product Haar multiplication property.
To see it directly, test words in nonzero powers of \(w^*U\) alternating with centered elements of \(N\).
Expand each power into individual \(U,U^*\) letters with coefficients in \(N\).
At consecutive \(U,U^*\) of opposite signs, the intervening \(N\)-coefficient is either the original centered block or its unitary conjugate in \(N\), so it is centered.
At equal signs one may split intervening \(N\)-coefficients into scalars and centered parts.
A scalar deletion there joins group powers of the same sign; no nonzero \(U\)-power at a sign change can disappear.
Every resulting word has zero trace by freeness of \(U\) and \(N\), also allowing initial and terminal \(N\)-coefficients by their scalar and centered decomposition.
For a power with no alternating blocks all surviving powers have the same sign and the same conclusion holds.
This verifies the Haar and joint freeness assertions.

In particular \(V_0=D_0^*U\) is free Haar relative to \(N\) and \(M=W^*(N,V_0)\).
Writing \(A=W^*(B,V_0)\), we have \(|U-b|=|V_0-h|\) and \(e_r\in A\).
The [Haagerup–Larsen annular support theorem](../audits/literature/Miy26/Yin_U004.md#hl00-the-r-diagonal-brown-support-interface) applies to the nonconstant bounded invertible \(h^{-1}\) free from \(V_0\).
The resulting spectrum of \(V_0h^{-1}\) contains every point of the Brown annulus with radii \(\|h\|_2^{-1}<1<\|h^{-1}\|_2\).
Indeed \(\|h\|_2^2=65/32\) and \(\|h^{-1}\|_2^2=65/8\).
Thus \(1\in\sigma(V_0h^{-1})\), and \(V_0-h=(V_0h^{-1}-1)h\) is noninvertible.
If its modulus were bounded below, the polar isometry would be unitary by finiteness and the original element would be invertible.
Therefore zero belongs to the spectrum of \(|V_0-h|\), and faithfulness gives \(t_r>0\) for all \(r>0\).
The absence of kernel in the [omitted-shift singular-law theorem](Yin_C_F0229_v1.md#statement) gives \(t_r\downarrow0\) as \(r\downarrow0\).

### Numerical range with every omitted unitary

Conjugating by \(W\) reduces the real part of \(V^*(U-b)W\) to that of \(w^*(U-b)\) for \(w=VW^*\).
Put \(S=\operatorname{Re}(w^*U)\), which is centered, is free from \(N\), has variance \(1/2\), and has a law invariant under \(S\mapsto -S\).
Freeness gives the same sign symmetry for \(qSq\) with the normalized corner trace \(\tau_q=\tau/\tau(q)\), and
\[
      \tau_q((qSq)^2)=\tau(q)\tau(S^2)=1/4.
\]
For the equality expand the middle \(q\) in \(\tau(SqSq)\) into its scalar and centered parts, using freeness and \(\tau(S)=0\).
Hence the bottom of the spectrum of \(qSq\) in the \(q\)-corner is at most \(-1/2\), by symmetry and its second moment.
Since \(N\) is abelian and \(\|bq\|=1/4\), the compression of \(\operatorname{Re}(w^*b)\) to the same corner has norm at most \(1/4\).
Testing on this corner gives the claimed upper bound \(-1/4\) for the bottom of the full real part.

### Conditional moments of the exact input projections

Let \(\mathbb E_N,\mathbb E_B\) be the trace-preserving conditional expectations.
Every \(a\in A\) satisfies \(\mathbb E_N a=\mathbb E_B a\), by the scalar free-product reduced-word decomposition for \(M=N*W^*(V_0)\) and for \(A=B*W^*(V_0)\).
We also need the following joint moment: if \(a,a'\in A\) are bounded with \(\mathbb E_B a=\mathbb E_B a'=0\) and \(x\in N\) with \(\mathbb E_B x=0\), then
\[
                    \mathbb E_N(a x a')=0 .                            \tag{2}
\]
For dense finite reduced words from \(A\ominus B\), write each word with a nonzero \(V_0\)-power at both ends, up to exterior \(B\)-coefficients.
In the concatenated word the new middle \(N\)-coefficient is \(b_1 x b_2\) for \(b_1,b_2\in B\), which is centered because \(\mathbb E_B x=0\).
The intervening centered \(B\)-coefficients elsewhere also belong to centered \(N\).
The result has zero conditional expectation onto \(N\), since it contains a \(V_0\)-power in a reduced word, even with exterior \(N\)-coefficients.
To extend the identity, first fix one finite word and approximate the other bounded argument in \(L^2\).
Then fix that bounded argument and approximate the first, since left and right multiplication by each fixed bounded factor is continuous in \(L^2\).
The same reduced-word proof with \(x\) absent gives the asserted \(\mathbb E_N|_A\).

Write \(e=e_r\), \(t=\tau(e)\), \(k=\mathbb E_B e=\mathbb E_N e\).
Since \(B\) has two atoms each of trace \(1/2\), \(0\le k\le2t1\).
For \(x\in N\) with \(\mathbb E_Bx=0\), expanding \(e=k+(e-k)\) and applying (2) yields \(\mathbb E_N(e x e)=k x k\).
Consequently
\[
    \|e x e\|_2^2=\tau(x^* e x e)=\tau(x^* k x k)
            \le 2t\,\tau(x^*x k)=2t\,\|xe\|_2^2 .
\]
Here \(k,x\) commute in \(N\).
For \(c\in N\) put \(c_B=\mathbb E_Bc\), \(x=c-c_B\).
The vectors \(xe,c_Be\) are orthogonal, since \(\tau(c_B^*x k)=0\).
Their left \(e\)-compressions \(exe,ec_Be\) are also orthogonal, since \(\tau(c_B^* k x k)=0\).
It follows that \((1-e)xe\) is orthogonal to \((1-e)c_Be\).
The corner \((1-e)ce\) of the commutator therefore satisfies
\[
      \|[c,e]\|_2\ge\|(1-e)ce\|_2\ge\|(1-e)xe\|_2
                    \ge\sqrt{1-2t}\,\|xe\|_2
\]
when \(t\le1/2\).
Since \(\mathbb E_B b=0\), orthogonality applied to \(b-x\) gives \(\|(b-c)e\|_2\ge\|(b-x)e\|_2\).
Adding and using the triangle inequality proves (1), since \(|b|=h\ge l1\).
The [spectral approximation formula](Yin_C_F0233_v1.md#statement) now gives the lower bound for \(mR/r\) from \(m\ge1\).

### An orthogonal family with an exact optimum

Use \(V_1=Y^*U\), again free Haar relative to \(N\), and take \(b=\lambda Y\), \(|\lambda|=1\).
Then \(e=1_{[0,r]}(|V_1-\lambda|)\) belongs to \(W^*(V_1)\) and is free from \(N\).
It has trace \(t=(2/\pi)\arcsin(r/2)\) for \(0<r\le2\), by arc length.
For \(c_0=c-\tau(c)\) direct freeness gives
\[
       \|(b-c)e\|_2=\sqrt t\,\|b-c\|_2,\qquad
       \|[c,e]\|_2^2=2t(1-t)\|c_0\|_2^2 .
\]
For the second identity, the two square terms have trace \(t\|c_0\|_2^2\), and the mixed terms have trace \(t^2\|c_0\|_2^2\) by centering the two occurrences of \(e\).
For \(t\le1/2\), the sum of the two errors divided by \(\sqrt t\) is at least \(\|b-c\|_2+\|c_0\|_2\ge\|b\|_2=1\), since \(b\) is centered.
The scalar choice \(c=0\) attains this bound and \(m=1\), giving the stated optimum.
For example choose centers \(\lambda_j=\exp(i2^{-j})\) and angular half widths \(2^{-j-3}\), \(j\ge1\), with \(r_j=2\sin(2^{-j-4})\).
The corresponding closed arcs are pairwise disjoint, so their positive-trace projections are mutually orthogonal.
Here \(V=-b\), \(W=1\) give \(\operatorname{Re}(V^*(U-b))\ge0\), so the half-plane condition holds for this separate family.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:40 |
| status | open |
| reason | Both sufficient tests are excluded for exact shrinking projections of the same fixed four-value shift, and the orthogonal-family optimum is fixed for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The free Haar normal tuple and its four-value shift, nonzero shrinking projections, simultaneous numerical-range and approximation obstructions, separate orthogonal benchmark with exact optimum. |
| argument | [Argument](#argument) | Haar multiplication, spectral support, compressed numerical range, conditional reduced words, Hilbert space projection estimates and orthogonal arcs. |
| dependency | [Free Haar coordinates](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual Haar vacuum and its extension to the complete free-product starred core. |
| dependency | [Free normal duals](Yin_C_F0162_v1.md#statement) | Part B for the freely independent normal coordinates and their adjoints, giving the strong dual domains. |
| dependency | [Annular Brown support](../audits/literature/Miy26/Yin_U004.md#miy26-u004) | Only the HL00 interface, Haagerup–Larsen, Theorem 4.4, for a nonconstant positive bounded invertible modulus free from a Haar unitary, and inclusion of the annulus in the spectrum. |
| dependency | [Unconditioned shifted singular law](Yin_C_F0229_v1.md#statement) | Absence of kernel for the omitted shift in the free Haar tuple. |
| dependency | [Omitted-unitary half-plane condition](Yin_C_F0231_v1.md#statement) | The two-unitary numerical-range hypothesis whose tolerance is tested. |
| dependency | [Locally finite-spectrum packing](Yin_C_F0233_v1.md#statement) | Item 2 and its definitions of \(m,R\) for the approximating partition and shift. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:44 |
| status | proved |
| reason | Independent review verifies the annular support, the numerical range bound and the uniform approximation obstruction on the same exact singular projections. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The free Haar normal tuple and its four-value shift, nonzero shrinking projections, simultaneous numerical-range and approximation obstructions, separate orthogonal benchmark with exact optimum. |
| argument | [Argument](#argument) | Haar multiplication, spectral support, compressed numerical range, conditional reduced words, Hilbert space projection estimates and orthogonal arcs. |
| dependency | [Free Haar coordinates](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual Haar vacuum and its extension to the complete free-product starred core. |
| dependency | [Free normal duals](Yin_C_F0162_v1.md#statement) | Part B for the freely independent normal coordinates and their adjoints, giving the strong dual domains. |
| dependency | [Annular Brown support](../audits/literature/Miy26/Yin_U004.md#miy26-u004) | Only the HL00 interface, Haagerup–Larsen, Theorem 4.4, for a nonconstant positive bounded invertible modulus free from a Haar unitary, and inclusion of the annulus in the spectrum. |
| dependency | [Unconditioned shifted singular law](Yin_C_F0229_v1.md#statement) | Absence of kernel for the omitted shift in the free Haar tuple. |
| dependency | [Omitted-unitary half-plane condition](Yin_C_F0231_v1.md#statement) | The two-unitary numerical-range hypothesis whose tolerance is tested. |
| dependency | [Locally finite-spectrum packing](Yin_C_F0233_v1.md#statement) | Item 2 and its definitions of \(m,R\) for the approximating partition and shift. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0244_v1.md#whole-proof-finding) | All conclusions, including the orthogonal family optimum and the scope of the two distinct examples. |

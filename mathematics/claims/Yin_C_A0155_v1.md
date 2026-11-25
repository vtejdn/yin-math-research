---
author: Yin
---

# Rank error at ordinary parameters from a formal approximation at zero

## Statement

Let \(G\) be finitely generated and let \(U=L^0(\mathcal N(G))\) with the normalized group trace.
Use the unnormalized trace on matrices and denote affiliated rank by \(\operatorname{rk}\).
Consider a scalar transfer \(f=\alpha L(z)^{-1}\beta\) with constant complex border vectors, where \(L\) is a square polynomial matrix of size \(n\), degree at most \(d\), with entries over \(\mathbb CG\) and a Laurent inverse over \(U((z))\).
Let \(s\) be an ordinary complex parameter and call it admissible if \(L(s)\) is an affiliated unit.
All but countably many \(s\) are admissible.

For any \(u\in U\), if \(f-u\in z^NU[[z]]\) with \(N\ge1\), then every admissible \(s\) satisfies
\[
                   N\operatorname{rk}_G(f(s)-u)\le nd.             \tag{1}
\]
In particular, if a sequence of such approximations has \(n_Nd_N/N\to0\), with arbitrary group supports, then \(u\) lies in the rank-metric closure of \(D_G\) in \(U\).
Each admissible real specialization gives a rational approximant with the displayed error bound.

There is a sharper bound for \(u=0\).
If \(f\ne0\) and \(f\in z^NU[[z]]\), put \(r=\operatorname{rk}_G f(s)\) at a generic admissible parameter.
This common value outside a countable set is strictly positive.
For \(n\ge2\),
\[
                         Nr\le (n-2+r)d .                           \tag{2}
\]
In size two, vanishing to order greater than \(d\) forces the transfer to vanish identically, without a support restriction or a positive lower bound on ranks.
In size one a nonzero realization cannot vanish to positive order.

For \(x\in D_G\), put \(B=x^*x\) and \(p=p_{\ker x}\).
One can use the weaker conditions \(f(0)=p\) and \(f^2-f\in z^NU[[z]]\) for a regular \(f\).
At all but countably many real \(s\), the rational element
\[
              y_s=1-B(B^2+f(s)f(s)^*)^{-1}B
\]
then satisfies \(y_sp=py_s=p\) and
\[
                   \operatorname{rk}_G(y_s-p)\le (2n+1)d/N.       \tag{3}
\]
Thus approximate idempotents with \(n_Nd_N/N\to0\) give rational rank approximants to \(p\) even when the group elements in their coefficients vary with \(N\).
At fixed support and size, sublinear degree already implies exact recovery. [Degree criterion](Yin_C_A0151_v1.md#statement)

## Argument

### Rank of the truncation of a rational matrix

For a matrix power series \(A\) with affiliated coefficients, let \(T_N(A)\) act on columns of the first \(N\) coefficients by multiplication modulo \(z^N\).
Suppose \(A(s)\) has its series as its asymptotic expansion to every finite order in the measure topology outside a countable exceptional set.
If \(\operatorname{rk} A(s)\le b\) there, then
\[
                            \operatorname{rk}T_N(A)\le Nb.           \tag{4}
\]
To see this, identify polynomials of degree below \(N\) with their values at the \(N\) roots \(s\omega^j\) of \(s^N\), where \(\omega=\exp(2\pi i/N)\).
The change of basis on each coordinate is the scalar Fourier matrix times \(\operatorname{diag}(1,s,\ldots,s^{N-1})\).
Choose \(s\to0\) avoiding the exceptional sets at every root.
Conjugating the rectangular diagonal map with fibers \(A(s\omega^j)\) by the evaluation maps for source and target preserves its rank, at most \(Nb\).
Replace each fiber by its Taylor polynomial of degree \(N-1\) there.
The entries of the change in the conjugated matrix tend to zero in measure, because the remainders are \(o(s^{N-1})\) in measure and each entry is a finite linear combination involving powers of \(s\) no worse than \(s^{1-N}\).
For the Taylor polynomial the conjugated map is multiplication modulo \(z^N-s^N\), and its coefficients tend in measure to those for multiplication modulo \(z^N\).
This gives \(T_N(A)\) as the limit.
Rank is lower semicontinuous for convergence in measure.
Indeed on a spectral cut of the initial support where the limiting operator is bounded above and below by positive constants, intersect with a projection of arbitrarily small trace loss where the difference is uniformly small.
The approximating operator is bounded below on that intersection, whose trace tends up to the limiting rank.
This proves (4).

For polynomial \(C(z)\) of degree at most \(d\) over \(U\) with generic rank \(h\), the complementary bound is
\[
                   \operatorname{rk}T_N(C)\ge \max(N-d,0)h.          \tag{5}
\]
For \(N>d\), restrict inputs to degree below \(N-d\), whose products have degree below \(N\).
Evaluate them at \(N-d\) distinct complex points where \(C\) has rank \(h\).
On these inputs evaluation is a scalar vector-space isomorphism over the coefficients, and the evaluated products have dimension \((N-d)h\).
The original image has at least that dimension.
Generic polynomial rank for affiliated coefficients follows by the [one-variable rank bound](Yin_C_A0143_v1.md#full-rank-away-from-a-countable-set).

### The bordered matrices

These arguments apply as well to a transfer with polynomial pivot over \(U\) for which the pivot is Laurent-invertible.
Its evaluations and asymptotics in measure follow from the [polynomial pivot argument](Yin_C_A0143_v1.md#full-rank-away-from-a-countable-set) and the finite truncation identities in the same proof.
In particular an admissible parameter exists off a countable set.
Form the two matrices
\[
       H_u(z)=\begin{pmatrix}L(z)&-\beta\\ \alpha&-u\end{pmatrix},
       \qquad H_f(z)=\begin{pmatrix}L(z)&-\beta\\ \alpha&-f(z)\end{pmatrix}.
\]
When \(f-u\) has order at least \(N\), their truncations agree, and \(H_f\) has rank \(n\) at every admissible parameter by its zero Schur complement.
Formula (4) gives \(\operatorname{rk}T_N(H_u)\le nN\).
Denote the generic rank of \(H_u(s)\) by \(n+r_u\).
On the coefficient spaces of the truncation, compare multiplication modulo \(z^N\) with multiplication modulo \(z^N-c\), choosing \(c\ne0\) so all \(N\) roots of \(c\) have generic rank.
The cyclic matrix has rank \(N(n+r_u)\).
Only the first \(n\) rows of the original matrix can wrap, and their outputs differ only in the first \(\min(d,N)\) coefficient positions.
Thus \(Nr_u\le nd\).
At every admissible \(s\), Schur elimination gives \(\operatorname{rk}(f(s)-u)=\operatorname{rk}H_u(s)-n\le r_u\).
For group-ring coefficients the values belong to \(D_G\) by [matrix inverse closure](Yin_C_A0132_v1.md#argument).

For the sharper assertion take \(u=0\).
Generic \(r=r_0\) is positive for a nonzero formal transfer by [injective Laurent evaluation](Yin_C_A0143_v1.md#statement).
In size one, multiplying by the polynomial pivot contradicts positive order when the border scalars are nonzero.
In higher sizes, apply invertible scalar row and column changes to \(L\) so that the nonzero borders are both first-coordinate vectors.
Let \(C\) be the \((n-1)\)-square submatrix of the transformed pivot obtained by deleting its first row and column.
Two scalar unit pivots eliminate the last row and column and the two border coordinates of \(H_0\), giving a matrix equivalent to \(\operatorname{diag}(I_2,C)\) over \(U[z]\).
The same elimination is valid modulo \(z^N\).
Hence \(C\) has generic rank \(h=n-2+r\) and \(\operatorname{rk}T_N(C)\le (n-2)N\).
For \(N>d\), (5) gives \((N-d)(n-2+r)\le(n-2)N\), which proves (2).
When \(N\le d\), the claimed bound follows from \(n\ge2\).

### From nearly idempotent series to rank approximation

Use the coefficientwise involution fixing \(z\).
Inside \(U[[z]]/(z^N)\) the class of \(f\) is an idempotent with constant coefficient \(p\).
The factors with invertible constant terms have inverses in this quotient by finite geometric expansion, so the [kernel recovery factorization](Yin_C_A0147_v1.md#recovering-the-orthogonal-projection) applies.
Thus \(y(z)=1-B(B^2+ff^*)^{-1}B\) satisfies \(y-p\in z^NU[[z]]\).
The pivot \(B^2+ff^*\) is a formal unit because its constant coefficient \(B^2+p\) is an affiliated unit.

To apply (1) with a size bound, over \(U[z]\) form the block polynomial
\[
 K_+=\begin{pmatrix}
       L^*&0&-\alpha^*\\
       -\beta\beta^*&L&0\\
       0&\alpha&B^2
     \end{pmatrix}.
\]
The Schur complement after the first two diagonal blocks is \(B^2+ff^*\).
Its bottom-right inverse entry is \((B^2+ff^*)^{-1}\).
The degree is at most \(d\), the size is \(2n+1\), and all entries lie in \(D_G[z]\).
Use constant affiliated border vectors with bottom entries \(B\) to realize \(1-y\).
The proof of (1) also applies to these fixed borders, since their entries are constant in \(z\) and Schur elimination works over \(U\).
Applying (1) to \(1-y\) with residue \(1-p\) gives (3).
For real admissible parameters avoiding the auxiliary pivot exceptions, evaluation preserves the involution and gives precisely \(y_s\in D_G\).
Both identities with \(p\) follow from \(Bp=pB=0\).

## Assessment history

### Decision specialization-rank-error

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:50 |
| status | proved |
| reason | Cyclic evaluation and asymptotics in measure bound the rank of a formal truncation and give a uniform rank error at ordinary admissible parameters. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Specialization error for constant and idempotent jets, rank closure, and the sharper low-state zero test. |
| argument | [Argument](#argument) | Confluent evaluation in measure, the bordered ranks and a polynomial realization of the kernel recovery formula. |
| dependency | [Asymptotics in measure](Yin_C_A0143_v1.md#statement) | Generic polynomial ranks, Laurent inversion and all orders of asymptotic evaluation. |
| dependency | [Matrix inverse closure](Yin_C_A0132_v1.md#argument) | Rationality of the specialized matrix inverses. |
| dependency | [Kernel recovery](Yin_C_A0147_v1.md#recovering-the-orthogonal-projection) | The idempotent factorization modulo a power of the central variable. |
| dependency | [Sublinear-degree test](Yin_C_A0151_v1.md#statement) | Exact rationality under fixed support and matrix size. |
| review | [Rank at ordinary parameters](../audits/reviews/Yin_R_A0171_v1.md#rank-at-ordinary-parameters) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-specialization-rank-error)

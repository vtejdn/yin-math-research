---
author: Yin
---

# Rank-one elimination for real Wigner determinant pencils

<a id="statement"></a>
## Finite-dimensional floors and deterministic even sizes

Use independent real symmetric Wigner inputs with the fixed centered strict upper laws of variance one and fixed centered real diagonal laws of finite second moment in [F0013](../tasks/Yin_T_F0013_v1.md#input-model).
The upper triangular entries of each color are independent before reflection and scaled by \(N^{-1/2}\).
The dimensions may be coupled arbitrarily.
In particular all the raw entries may be Rademacher.
Fix complex matrices \(b,A_1,\ldots,A_g\) of size \(m\), let \(L=b+\sum_j A_j x_j\), and assume that all but at most one of its nonconstant coefficients have rank at most one.
There is no condition on the rank of \(b\).
Write \(L_N=L(W^{(N)})\) and \(u=\log\Delta_{\operatorname{tr}_m\otimes\tau}L(s)\) at a standard free semicircular system.

If \(L\) is full over the free polynomial algebra, there are \(C,H,N_0>0\) such that
\[
 \Pr\{s_{\min}(L_N)\le N^{-H}\}
 \le C\sqrt{\log(2+N)}\,N^{-1/18},\qquad N\ge N_0 . \tag{1}
\]
Fullness means that the matrix does not factor over this algebra through fewer than \(m\) columns.
Its free target \(u\) is then finite.
The ordinary normalized log \(U_N=(mN)^{-1}\log|\det L_N|\), with \(\log0=-\infty\), tends to \(u\) in probability on the full sequence.
For every coupling \(U_{2^k}\to u\) almost surely, and \(\limsup_N U_N=u\) almost surely.
Along \(N=2^k\) the loss below \(N^{-H}\) is eventually zero almost surely.
The events can depend on the fixed data and the coupling; the sequence of dimensions has no such dependence.
If \(L\) is nonfull, the ordinary logarithms and the free target are all \(-\infty\).

<a id="argument"></a>
## Eliminating an input with a rank-one coefficient

The [scalar shifted-Wigner floor](Yin_C_F0194_v5.md#in-probability-floor), in the [uniform normalization](Yin_C_F0186_v10.md#floor-input), permits an independent nonsymmetric complex shift.
For each fixed \(a>0\), the probability of a least singular value at most \(N^{-h(a)}\) for \(W_j+F\), conditionally on an independent \(F\) on its guard \(\max |F_{ij}|\le N^a\), is bounded by \(C N^{-2}+C\sqrt{\log(2+N)}N^{-1/18}\).
Use fixed tail power two in that statement.
Moreover \(\max_j\|W_j\|\le N^2\) with exception \(O(N^{-3})\) by the expected squared Hilbert--Schmidt norms.
These estimates need only within-size independence.
Below, a polynomial bound on a norm means \(N^C\) for some constant depending on the fixed pencil and laws, allowing \(C\) to increase by a fixed amount at successive steps.

We prove (1) for a full pencil by induction, removing zero coefficients and inducting in the number of active colors.
If none remains then the constant matrix is invertible.
If only one color remains, let \(f(t)=\det(b+tA)\).
Fullness makes \(f\) nonzero, since the free field on one generator is the ordinary field of rational functions.
The real symmetric \(W\) is orthogonally diagonalizable.
The shifted-Wigner floor for \(W-zI\) at each of the finitely many complex roots \(z\) of \(f\) bounds every \(|\lambda_i(W)-z|\) below by an inverse power of \(N\) outside the stated total error.
Then each \(|f(\lambda_i)|\) has a polynomial lower bound, including the constant-polynomial case.
The classical adjugate of \(b+\lambda_i A\) is bounded polynomially on the norm guard.
The resulting inverse bounds apply to all blocks of the diagonalized pencil and prove (1) in this base case.

With at least two active colors, choose one with rank one, called \(j\).
Fixed invertible scalar left and right changes of basis turn \(A_j\) into \(e_1e_1^{\mathsf T}\) and preserve the other rank bounds, fullness and polynomial inverse estimates.
In this coordinate system write
\[
 L(x)=\begin{pmatrix}x_j+d&r\\ c&E\end{pmatrix},\qquad
 L_0(x)=\begin{pmatrix}d&r\\ c&E\end{pmatrix}.
\]
All displayed blocks other than \(x_j\) omit the distinguished color.
At size \(m=1\) use the empty invertible matrix for \(E\), giving the direct shifted-Wigner floor.
For \(m>1\) there are two cases.

If \(E\) is full, each coefficient in it is a fixed rectangular compression of the corresponding coefficient of the original pencil.
Thus at most one variable coefficient can still have rank above one.
Apply the induction hypothesis to the smaller number of colors in \(E\).
With the stated failure bound, \(E_N^{-1}\) has polynomial norm.
On the norm guard for the colors other than \(j\) the Schur shift \(F=d_N-r_N E_N^{-1}c_N\) also has polynomial norm.
The guards on this shift depend only on the other colors, so the scalar conditional floor applies to \(W_j+F\).
The two triangular Schur factors and their inverses have polynomial norms on those guards.
Consequently \(L_N^{-1}\) has polynomial norm with the claimed error.

<a id="singular-complement"></a>
## Removing a color when its complementary pencil is nonfull

Let \(E\) be nonfull.
For the formal argument work over the free field in all the active generators.
The [inner-rank and free-field interfaces](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) identify fullness of \(L\) with invertibility there.
As \(E\) factors through at most \(m-2\) columns, choose a nonzero column \(y\) in its right kernel over the field.
Then \(L(0,y)^{\mathsf T}=(r y,0)^{\mathsf T}\), using the notation of stacked columns.
The entry \(ry\) is nonzero by injectivity of \(L\), hence invertible in the field.
Thus the first entry of \(L^{-1}e_1\) vanishes.
It follows that \(L^{-1}e_1 x_j e_1^{\mathsf T}\) squares to zero.
Factoring \(L_0=L(I-L^{-1}e_1 x_j e_1^{\mathsf T})\) proves that \(L_0\) is full even over the polynomial algebra omitting \(x_j\), since a factorization there through fewer columns would persist over the larger field.
Induction with one less active color gives the desired polynomial inverse estimate for \(L_{0,N}\).

There is a direct finite-matrix return which requires no evaluation of any free-field denominator.
The polynomial factorization of \(E\) gives \(\dim\ker E_N\ge N\) in every dimension.
On the event \(L_{0,N}\) is invertible, its first block row \(r_N\) maps \(\ker E_N\) injectively into \(\mathbb C^N\), so it maps onto that space.
For every \(v\in\mathbb C^N\) the preimage of \((v,0)^{\mathsf T}\) under \(L_{0,N}\) therefore has zero first component.
The entire \(N\)-by-\(N\) first diagonal block of \(L_{0,N}^{-1}\) vanishes.
With \(D=e_1e_1^{\mathsf T}\otimes W_j\) we have \((L_{0,N}^{-1}D)^2=0\) and
\[
 L_N^{-1}=(I-L_{0,N}^{-1}D)L_{0,N}^{-1}.
\]
The original norm guard and the inverse bound for \(L_{0,N}\) give the required bound on \(L_N^{-1}\).
Across finitely many induction steps the exceptional probabilities add, retaining the rate in (1).
An increase in the final power \(H\) yields the displayed weak inequality at its threshold.

<a id="logs"></a>
## Removing the polynomial cutoff on dyadic dimensions

For full \(L\), the [full-pencil free power estimate](Yin_C_F0352_v1.md#statement) at zero background gives \(u>-\infty\).
The [ordinary-law clipping argument](Yin_C_F0186_v40.md#determinant) before invoking (T) gives almost-sure convergence to \(u\) of
\[
 V_N=\int \log\max(s,N^{-H})\,d\nu_{|L_N|}(s)
\]
under every coupling.
It uses only second moments, the [original polynomial-window count](Yin_C_F0186_v40.md#argument), bounded-rank concentration and positive-log tail control.
Off the exceptional event in (1), \(U_N=V_N\).
This gives full-sequence convergence in probability.
The failure bound in (1) is summable on \(N=2^k\), so first Borel--Cantelli gives equality eventually there under every coupling.
Since \(U_N\le V_N\) in every dimension, the dyadic limit also gives the full dimension limsup.
If \(L\) is nonfull its factorization forces a kernel of dimension at least \(N\) at every finite evaluation and positive kernel trace at the free evaluation, giving the stated infinite logarithms.
No expectation of an ordinary logarithm with atomic input is needed.

<a id="scalar"></a>
## Scalar realizations with few occurrences of each variable

For disjoint collections of colors \(x_1,\dots,x_r\) and \(y_1,\dots,y_s\) take arbitrary fixed complex coefficients and a fixed shift \(z\).
Consider
\[
 P-z=d-z+\sum_i a_i x_i+\sum_j b_j y_j+\sum_{ij}q_{ij}x_i y_j .
\]
Writing \(x^\mathsf T=(x_1,\ldots,x_r)\), \(y=(y_1,\ldots,y_s)^\mathsf T\), and \(Q=(q_{ij})\), use the pencil
\[
 \begin{pmatrix}d-z+\sum_i a_i x_i+\sum_j b_j y_j&-x^\mathsf T\\ Qy&I_r\end{pmatrix}.
\]
Its Schur complement is \(P-z\).
Each \(x_i\) occurs only in the first row, and each \(y_j\) only in the first column, including their linear terms.
Hence all variable coefficients have rank at most one.
For nonconstant \(P\) this pencil is full, by the two unit triangular Schur operations over the free polynomial algebra and nonvanishing of \(P-z\) in its free field.
These operations preserve ordinary determinants and the [finite/free logarithmic normalization](../ledger/Yin_L_F0061_v2.md#linearization-transfer), multiplying the normalized pencil logs by \(r+1\) on both sides.
The inverse upper-left corner on nonsingular evaluations is \((P(W)-zI)^{-1}\), so the same polynomial floor transfers to the scalar matrix.

More generally let a scalar polynomial be given by a finite formula using addition, ordered multiplication, complex constants and variable leaves, with every color except possibly one occurring at most once in the formula.
Construct a finite acyclic directed graph with a distinct source and sink representing its sum of source-to-sink path weights, products taken in path order.
Represent a leaf by one labeled edge.
For a sum take disjoint copies of the two graphs, join a new source to both sources and both sinks to a new sink by edges of weight one.
For a product join the first sink to the second source by an edge of weight one and retain the outer source and sink.
The construction yields \(P\) and uses one labeled edge for each leaf occurrence.
In topological order the adjacency matrix \(T\) is strictly upper triangular, adding weights of any parallel edges.
If the source and sink indices are \(u,v\), then \(e_u^\mathsf T(I-T)^{-1}e_v=P\) by the finite path sum.
The affine pencil
\[
 \begin{pmatrix}-z&-e_u^\mathsf T\\e_v&I-T\end{pmatrix}
\]
has Schur complement \(P-z\) and a unit upper triangular auxiliary pivot.
Each variable coefficient has rank at most its number of labeled edges.
The theorem therefore proves the ordinary scalar determinant limit in probability through all dimensions, almost-sure convergence along \(2^k\) and the almost-sure limsup under every coupling for this class at every prescribed \(z\), including \(P(0)\).
The triangular factors are bounded invertible at bounded free inputs, and have ordinary determinant modulus one at finite size, giving again the exact finite/free transfer.
Constants have their deterministic logs directly.
A general polynomial can have several variables repeated in every available realization and the argument gives no rank-one pivot in that case.

## Current assessment

[Selected decision](#decision-rank-one-floor-candidate)

## Assessment history

### Decision rank-one-floor-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:51 |
| status | open |
| reason | Successive elimination of rank-one variable coefficients gives a polynomial floor using the original real Wigner law, including the singular-complement branch, and yields ordinary logarithms on fixed even dimensions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Floor and determinant limits](#statement) | All but one variable coefficient of rank at most one, every real finite-variance Wigner input, and arbitrary cross-size couplings. |
| argument | [Full complementary pencil](#argument) | Uniform independent scalar shift, one-color base and Schur conditioning. |
| support | [Nonfull complementary pencil](#singular-complement) | Formal removal of the fresh color and the finite nullity argument. |
| support | [Ordinary logarithms](#logs) | Polynomial cutoff, perturbation error and explicit even dimensions. |
| support | [Scalar realizations](#scalar) | Bipartite quadratic forms and scalar formulas with at most one multiply occurring color. |

---
author: Yin
---
# Bounded supports and the characteristic-zero obstruction

<a id="md26-u001"></a>

This inspection uses [arXiv v1](readme.md#yin), Section 8, printed and PDF pages 32–34.
On 21 November 2026 the argument of Theorem 8.1, Corollary 8.2 and Proposition 8.3 was checked in full, including the coefficient-field descent and the nonvanishing conditions in the last proposition.
The construction parameters and the definitions of the witnesses in Sections 6.1–6.3, Proposition 7.6 and Section 7.5 were read to determine which support bounds are supplied.
The probabilistic and geometric existence theorems are used here at their stated scope.
The inspection covers the written mathematics of these passages, with the weak Nullstellensatz, finite-dimensional linear algebra and Perron–Frobenius monotonicity accepted as standard inputs.
The whole-paper proof and the accompanying Lean development lie outside this inspection.

## Proposition 8.3 and its quantifiers

Suppose that for an infinite set of distinct primes \(p\) there are torsion-free groups \(G_p\), fields \(K_p\) of characteristic \(p\), and elements
\[
 0\ne\alpha_p,\beta_p\in K_p[G_p],\qquad \alpha_p\beta_p=0.
\]
Assume both cardinalities of the actual supports are bounded independently of \(p\).
Then, for infinitely many of these primes, the same group \(G_p\) admits nonzero zero divisors over \(\overline{\mathbb Q}\), and hence over \(\mathbb C\).
The groups and their presentations may vary with \(p\).
The assertion needs infinitely many distinct prime characteristics and simultaneous bounds for both factors.

### The partition of the support products

For each \(p\), enumerate the distinct support elements as \(x_{p,1},\ldots,x_{p,a_p}\) and \(y_{p,1},\ldots,y_{p,b_p}\).
After restricting to infinitely many primes, their cardinalities are fixed integers \(a,b\ge1\).
Define the partition \(\mathcal P_p\) of \([a]\times[b]\) by
\[
 (i,j)\sim_p(i',j')
 \quad\Longleftrightarrow\quad
 x_{p,i}y_{p,j}=x_{p,i'}y_{p,j'}.
\]
There are only finitely many partitions of this finite set.
An infinite subset of primes therefore realizes one partition \(\mathcal P\).
Each block records exactly one group element among the products of the two supports.

Write \(\alpha_p=\sum_i u_{p,i}x_{p,i}\) and \(\beta_p=\sum_j v_{p,j}y_{p,j}\), with every displayed coefficient nonzero.
The necessary coefficient equations are the fixed integral polynomials
\[
 f_C(X,Y)=\sum_{(i,j)\in C}X_iY_j\quad(C\in\mathcal P),
 \qquad
 f_0(X,Y,Z)=Z\prod_{i=1}^aX_i\prod_{j=1}^bY_j-1.
\]
They have a simultaneous solution in every selected \(K_p\), using the original coefficients and the inverse of their total product for \(Z\).
The equation \(f_0=0\) retains all support coefficients as nonzero.
The finite partition contains all multiplication data needed for these equations.

### Descent of the polynomial certificate

Suppose that the fixed equations have no solution over \(\mathbb C\).
The weak Nullstellensatz gives a polynomial identity
\[
 1=\sum_{C\in\mathcal P}H_C f_C+H_0f_0,
 \qquad H_C,H_0\in\mathbb C[X,Y,Z].
\]
Only finitely many monomials occur in the multipliers in this identity.
Keeping those monomial positions and treating their coefficients as unknowns turns the identity into a finite linear system over \(\mathbb Q\).
Row reduction over \(\mathbb Q\) shows that its consistency over \(\mathbb C\) implies consistency over \(\mathbb Q\).
Clearing the denominators of rational multipliers gives
\[
 0\ne D=\sum_{C\in\mathcal P}A_C f_C+A_0f_0,
 \qquad D\in\mathbb Z,\quad A_C,A_0\in\mathbb Z[X,Y,Z].
\]
Evaluating this identity at a solution in characteristic \(p\) forces \(D\cdot1_{K_p}=0\), and hence \(p\mid D\).
A nonzero integer has only finitely many prime divisors, contradicting the infinite set under consideration.
This evaluation works directly in any coefficient field \(K_p\) of characteristic \(p\).

For algebraic coefficients, run the same argument with the algebraically closed field \(\overline{\mathbb Q}\) in place of \(\mathbb C\).
It supplies one solution \(u_i,v_j,z\in\overline{\mathbb Q}\), with every \(u_i,v_j\ne0\).
For each \(p\) in the selected infinite set define
\[
 \alpha'_p=\sum_i u_i x_{p,i},\qquad
 \beta'_p=\sum_j v_j y_{p,j}.
\]
Distinctness within each support makes both elements nonzero, while the block equations give \(\alpha'_p\beta'_p=0\).
The same algebraic coefficients work in each selected \(G_p\).
Torsion-freeness is inherited from each existing group and is used to identify the resulting pairs as counterexamples to the conjecture.

The source proof of Proposition 8.3 is sound with these details made explicit.
Its phrase about solutions over \(\overline{\mathbb F}_p\) can also be justified by applying the weak Nullstellensatz to the proper ideal determined by a solution in \(K_p\).

## The rank obstruction in Theorem 8.1

### Type incidence and squared-turn matrix

Let \(T\) be a finite alphabet with a fixed-point-free involution \(t\mapsto\bar t\), and put \(N=|T|\).
Let \(S_a\subseteq T\) be a finite family of vertex types with probabilities \(\mu(a)>0\), \(\sum_a\mu(a)=1\).
Define
\[
 X_{at}=\mathbf1_{\{t\in S_a\}},\qquad
 \pi(t)=\sum_a\mu(a)X_{at},\qquad
 \jmath(s,t)=\sum_a\mu(a)X_{as}X_{at}.
\]
Assume \(\pi(t)>0\) and \(\pi(t)=\pi(\bar t)\) for every letter.
The squared-turn matrix is
\[
 M_{tu}=
 \begin{cases}
 \bigl(\jmath(\bar t,u)/\pi(\bar t)\bigr)^2,&u\ne\bar t,\\
 0,&u=\bar t.
 \end{cases}
\]
Theorem 8.1 states that \(\rho(M)<1\) implies \(\operatorname{rank}_{\mathbb R}X\ge N/2+1\).

### Proof check

Let \(D=\operatorname{diag}(\pi)\), \(C=D^{-1/2}(\jmath(s,t))D^{-1/2}\), \(S=C^{\circ2}-I\), and let \(R\) be the permutation matrix of the involution.
The matrix \(C\) is positive semidefinite, has unit diagonal, and has the same rank as \(X\), because \(\jmath=X^{\mathsf T}\operatorname{diag}(\mu)X\).
Entrywise calculation using \(\pi(t)=\pi(\bar t)\) gives \(M=D^{-1}RSD\).
The matrix \(S\) is entrywise nonnegative, so
\[
 f=(I-RS)^{-1}\mathbf1=\sum_{k\ge0}(RS)^k\mathbf1>0,
 \qquad Sf=Rf-\mathbf1<Rf.
\]
For \(F=\operatorname{diag}(f)\), put \(H=F^{1/2}CF^{1/2}\), and let \(Q\) be the orthogonal projection onto its range.
Since \(QHe_t=He_t\), Cauchy–Schwarz gives
\[
 H_{tt}^2\le Q_{tt}(H^2)_{tt},\qquad
 Q_{tt}\ge\frac{f_t}{f_t+(Sf)_t}>
 \frac{f_t}{f_t+f_{\bar t}}.
\]
Summing over an inverse pair gives \(Q_{tt}+Q_{\bar t,\bar t}>1\).
Consequently \(\operatorname{rank}X=\operatorname{tr}Q>N/2\), which gives the stated integral lower bound.

For Corollary 8.2, restrict both type families to the nonempty inverse-closed support \(U\) of a letter-weight vector \(c\).
The restricted squared-turn matrix is a principal submatrix, so its spectral radius remains below one.
Both restricted incidence matrices have rank at least \(|U|/2+1\).
Sylvester's inequality therefore gives
\[
 \operatorname{rank}_{\mathbb C}
 \bigl(X_A\operatorname{diag}(c)X_B^{\mathsf T}\bigr)
 \ge (|U|/2+1)+(|U|/2+1)-|U|=2.
\]
This excludes a factorization of the full weighted cross-intersection array as \(u_av_b\), whose rank is at most one.
The inverse-symmetric weights required by the signed cancellation pairing have inverse-closed support, so the corollary applies to them.

## What the existing constructions supply

The witnesses in Section 6 have the form
\[
 \alpha=\sum_{x\in A'}\sigma(x)g_x,\qquad
 \beta=\sum_{y\in B'}h_y^{-1},
\]
where \(A',B'\) are the root components and \(\sigma\) changes sign across each edge on the first side.
The integer cancellation identity is
\[
 \sum_{x,y}|S_x\cap S_y|\sigma(x)g_xh_y^{-1}=0.
\]
When all intersections are congruent to \(1\pmod p\), it gives \(\alpha\beta=0\) in characteristic \(p\).
Root protection verifies the identity coefficient and hence nonvanishing of each factor.

Definition 6.2 uses
\[
 e=2p-1,\qquad q=p^k\ge2e(e+2),\qquad v=q^2+q+1,
 \qquad n\in n_0\mathbb Z_{>0},\quad
 n_0=2\binom{2p-2}{p-1}v^2.
\]
Both whole sides have \(n\) vertices, and the existence theorem requires sufficiently large admissible \(n\).
The witnesses have at most \(n\) terms each before collecting repeated group labels.
Section 7 uses \(q=p^5\), \(v=q^2+q+1\), and a uniform family of \(p^2v^2\) vertices, repeated sufficiently many times and modified by corrections that are fixed for each \(p\).
Proposition 7.11 gives \(ab=1\) and \(ac=0\) from the resulting root-component sums.
Section 8 explicitly records that these constructions supply no support bound independent of \(p\).

The source's mechanism explains why a fixed alphabet cannot implement the same family of type identities.
In characteristic \(p\), every integer cross-intersection is \(1\pmod p\).
Corollary 8.2 excludes the matrix in which every intersection equals one, so some intersection is at least \(p+1\), forcing at least \(p+1\) letters.
For projective-plane types this dependence is visible in \(XX^{\mathsf T}=qI+J\), which becomes \(J\) modulo \(p\) and is positive definite over \(\mathbb R\).

The graph size, the alphabet size, and the actual support cardinality are different quantities.
For example, the coefficient of a group element \(g\) in \(\alpha\) is
\[
 \sum_{x\in A':\ g_x=g}\sigma(x)\in\mathbb F_p.
\]
Several vertex occurrences can have the same label, and their combined coefficient can vanish.
A growing graph-size lower bound therefore does not itself prove an unbounded lower bound for the collected supports.
The verified conclusion is that the present results supply no uniform bound, while the rank obstruction rules out the stated fixed-alphabet, full-type cancellation mechanism under the decay hypothesis.
It leaves open compression through additional coincidences for specially chosen matchings and constructions with a different geometric safeguard.

The [existing characteristic-two support calculation](../../../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) separately gives actual support sizes \(n-o(n)\) in probability for the original fixed type family.
That calculation has fixed characteristic and fixed type data as \(n\to\infty\), so it supplies no bound or obstruction uniform in the prime \(p\).
[Ivanov, Section 8.3, PDF p.12](../../../literature/pdf/Iva26--arxiv-v1.pdf#page=12) already records the coefficient transfer for one fixed group and fixed supports, and states that his construction supplies no such uniformity.
Proposition 8.3 removes the need to fix the whole group by using the finite partition of support products.

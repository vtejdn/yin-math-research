---
author: Yin
---

# MS24: Dependency Audit for the Integer Capacity Bound

<a id="integer-dependency-audit"></a>

Record: 2026-09-12, the integer-dependency reviewer, independent review of the upstream interfaces used in [MS24-U004](../audits/literature/MS24/Yin_U004.md#ms24-u004).
The finite-quotient proof below is a source-specialization reconstruction, self-checked in this assignment and independently reviewed by the coordinating agent within the scope recorded at the end.
It is not a new project Claim.

Scope: MS24 Theorem 4.1, printed/PDF pp. 15-16, in the registered local version.
This record checks rank non-decrease to Haar-model injectivity, then the ordinary determinant lower bound for that injective integral matrix.
The final normalization argument from the Haar model to capacity is included to expose the complete dependency chain.
The semicircular determinant formula is a separate input to the resulting Corollary 1.4.

Current complete proof homes, 2026-10-21: [Sch01-U001](../audits/literature/Sch01/Yin_U001.md#finite-quotient-determinant-proof) retains the complete injective free-group determinant proof, and [MS24-U004](../audits/literature/MS24/Yin_U004.md#complete-retained-algebra-and-haar-interfaces) retains the exact smaller rank/Haar interfaces alongside the sufficient existing capacity proof.
The original text remains the exact R_F0129 review input, with all fixed source and arithmetic limits preserved.

## Exact Chain and Conclusion

Let \(m,n\geq1\), \(a_1,\ldots,a_n\in M_m(\mathbb Z)\), and
\[
\eta(b)=\sum_{i=1}^n a_i b a_i^*,\qquad
A(x)=\sum_{i=1}^n a_i x_i.
\]
Let \(u_i=\lambda(g_i)\in L(F_n)\) be the left regular free-group generators, with canonical trace \(\tau\), and use the normalized state \(\varphi=\operatorname{tr}_m\otimes\tau\) on \(M_m(L(F_n))\).
The matrix
\[
T=A(u)=\sum_i a_i\otimes u_i
\]
is a bounded operator on \(\mathbb C^m\otimes\ell^2(F_n)\).

The sufficient chain is
\[
\begin{aligned}
\eta\text{ rank non-decreasing}
&\Longrightarrow A\text{ full over }\mathbb C\langle x\rangle\\
&\Longrightarrow \ker T=0\\
&\Longrightarrow \Delta_\varphi(T)\geq1\\
&\Longrightarrow \det\eta(b)\geq1
 \quad(b>0,\ \det b=1)\\
&\Longrightarrow \operatorname{cap}(\eta)\geq1.
\end{aligned}
\]
The third arrow uses integral coefficients and finite quotients of the free group in addition to injectivity.
Neither injectivity nor a positive determinant is a conclusion of integrality alone.

The conclusions are valid under the explicitly retained algebraic and operator-algebra foundations below.
The unresolved literal algorithm constants and complete quantitative continuity estimates in [GGOW20-U004](../audits/literature/GGOW20/Yin_U004.md#ggow20-u004) are not premises of this chain.

## Rank Non-Decrease to a Full Homogeneous Pencil

For \(V\subseteq\mathbb C^m\), let \(p_V\) be the orthogonal projection and put
\[
W=\sum_i a_iV.
\]
Positivity gives
\[
\operatorname{Ran}\eta(p_V)=W.
\]
More generally, if \(b\geq0\) has range \(V\), its restriction to \(V\) is invertible, so the same range identity holds with \(b\) in place of \(p_V\).
Thus rank non-decrease is exactly
\[
\dim\Big(\sum_i a_iV\Big)\geq\dim V
\quad\hbox{for every }V\subseteq\mathbb C^m.
\tag{1}
\]

A shrunk subspace, with \(\dim V=\ell\) and \(\dim W=r<\ell\), supplies scalar invertible changes of domain and range bases for which every \(a_i\) has a common zero block of size \((m-r)\)-by-\(\ell\).
Its row and column sizes sum to more than \(m\).
Such a hollow pencil factors through fewer than \(m\) coordinates, so it is not full.

Conversely, the linear hollow criterion puts every nonfull square linear pencil into a scalar-equivalent hollow form.
The corresponding column subspace maps under every coefficient matrix into the complementary row subspace, whose dimension is strictly smaller.
It violates (1).
Homogeneity ensures that the coefficients in this comparison are exactly the Kraus matrices \(a_i\); an omitted constant term would invalidate the comparison.

The precise algebraic input is MSY23 Theorem 2.10 and Proposition 2.11, printed pp. 10-11, with the citation repair proved and independently reviewed in [MSY23-U001](../audits/literature/MSY23/Yin_U001.md#msy23-u001).
The retained Cohn input is the matched-degree bound in the proof of Coh06 Lemma 5.8.7, printed pp. 316-317: a rank factorization of a degree-one matrix can be internally reduced so that each matched column/row degree sum is at most one.
Partitioning those factors into constant columns and constant rows yields the hollow form.
The book's cited Theorem 5.8.8 has different hypotheses and is not used.

This audit rechecked the block/range interface and the existing independent review.
It accepts that primary-source-checked degree-reduction theorem and the full-submatrix property of free-algebra matrices; the complete weak-algorithm foundations of the free algebra are not reproved here.
No invariant-theory characterization or operator-scaling algorithm is needed.

## Haar Evaluation: Actual Source Scope and a Smaller Sufficient Proof

MSY23 Corollary 6.4, printed/PDF p. 48 of [MSY23.pdf](../literature/pdf/MSY23.pdf), states that the division and rational closures of the canonical free group generators \(u_1,\ldots,u_n\) (without adjoining their inverses as additional formal variables) in the operators affiliated to \(L(F_n)\) are the free field.
Together with Theorem 5.6, pp. 30-34, this makes every full polynomial matrix invertible in the matrix algebra over \(U(L(F_n))\), hence injective in its bounded realization.

The actual ambient algebra in the corollary is \(U(L(F_n))\); it is not \(L(F_n)\).
There is no hypothesis \(n\geq2\), no factoriality hypothesis, and no requirement that the positive-generator polynomial algebra be strongly dense in \(L(F_n)\).
In fact that holomorphic density assertion would already be false for one Haar unitary.
The corollary does not treat the formal symbols \(x_i^*\) as additional independent generators.

For the homogeneous linear pencil required by MS24, the following shorter route proves injectivity without invoking the full rational-closure theorem.

1. Define \(V_j\in B(\ell^2(F_n))\) on reduced group words by deleting a terminal positive \(g_j\), and sending all other words, including the identity, to zero.
   This map sends distinct eligible basis vectors to distinct basis vectors, so its norm is one.
   Direct cancellation gives
   \[
   [u_i,V_j]=-\delta_{ij}P_e.
   \]
   At the identity, the left side is \(-\delta_{ij}e\).
   For any nonidentity reduced word the two operations agree; the whole-word left cancellation case is the one-letter word \(g_i^{-1}\), and both terms are then zero.
   Hence \(D_j=-V_j\) satisfies the source convention \([u_i,D_j]=\delta_{ij}P_e\).
   This corrects the sign in the prose of MSY23 Proposition 6.3; the published vacuum calculation itself has the minus sign.

2. Suppose finite-rank \(R_1,\ldots,R_n\in B(\ell^2(F_n))\) satisfy \(\sum_i[R_i,u_i]=0\).
   For \(Q_1,Q_2\in L(F_n)'\), ordinary trace cyclicity gives
   \[
   0=\operatorname{Tr}\!\left(\sum_i[R_i,u_i]Q_1D_jQ_2\right)
    =\operatorname{Tr}(R_jQ_1P_eQ_2).
   \]
   Every trace has a finite-rank factor and bounded remaining factors.
   The vectors \(Q_1e\) and \(Q_2^*e\) range independently through dense subspaces because right translations belong to the commutant.
   Therefore \(R_j=0\) for every \(j\).

3. The implication in MSY23 Theorem 3.1 from absence of nonzero finite-rank cycles to injectivity of full linear evaluations is reconstructed in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002), with independent review.
   Its mechanism is finite rank: kernel vectors for a linear matrix and its adjoint produce a cycle; independent component families force the coefficient matrix to vanish.
   An induction using full square submatrices rules out dependent components for a full pencil.
   Finite trace equates the traces of the two kernel projections and supplies the adjoint kernel.
   This argument applies to the unitary, generally nonselfadjoint tuple \(u\).

Thus \(A\) full implies \(\ker A(u)=0\).
This proof uses neither a group determinant theorem, nor free entropy/Fisher information, nor the original Linnell theorem.
The general von Neumann dimension theory used to name maximal \(\Delta\) can also be omitted: the actual premise of the linear-kernel argument is exactly the vanishing of finite-rank cycles proved in step 2.

For completeness, finite trace and polar decomposition imply that an injective \(T\in M_m(L(F_n))\) has dense range, since its initial and final support projections have equal trace.
Its spectral inverse is then a closed densely defined affiliated inverse.
This is the affiliated interpretation of injectivity, not a bounded inverse estimate.

The case \(n=1\) is especially transparent.
Rank non-decrease is equivalent to \(a_1\) being an invertible complex matrix; then \(T=a_1\otimes u_1\) is even boundedly invertible, and \(\Delta_\varphi(T)=|\det a_1|^{1/m}\geq1\).
The common proof above also works with \(F_1=\mathbb Z\).
The scalar matrix size \(m=1\) causes no exceptional case.

## Integral Free-Group Determinants by Finite Quotients

<a id="finite-quotient-determinant-proof"></a>

The exact needed input has a direct proof:

> If \(T\in M_m(\mathbb ZF_n)\), represented on \(\mathbb C^m\otimes\ell^2(F_n)\), is injective, then \(\Delta_\varphi(T)\geq1\).

This is the injective free-group specialization of [Sch01-U001](../audits/literature/Sch01/Yin_U001.md#sch01-u001).
The primary source's Lemma 6.8, p. 19, contains the finite integer characteristic-polynomial argument; Theorem 6.9, pp. 19-21, uses bounded spectral approximation.
Remark 6.10, p. 21, explicitly separates the resulting bound from convergence of determinants.
The following proof retains precisely that distinction and does not import a determinant approximation theorem.

### Finite quotients and uniform bounds

Choose finite-index normal subgroups \(N_k\lhd F_n\) with \(N_{k+1}\subseteq N_k\) and \(\bigcap_kN_k=\{e\}\), and let \(G_k=F_n/N_k\).

The finite quotients can be constructed directly.
On the finite word ball \(B_R\subset F_n\), the partial maps \(w\mapsto g_iw\), restricted to pairs whose endpoints lie in \(B_R\), are injective partial permutations.
Extend each to a permutation of \(B_R\), and use freeness to obtain a homomorphism \(F_n\to\operatorname{Sym}(B_R)\).
A reduced word of length at most \(R\) acts on \(e\) by the prescribed successive multiplications, since all intermediate suffixes lie in \(B_R\), and therefore a nonidentity such word does not fix \(e\).
Taking the intersections of the kernels of these homomorphisms for \(R\leq k\) gives the required nested family.
This also verifies directly the residual-finiteness input used in this specialization.

Let \(T_k\) be the image of \(T\) acting on \(\mathbb C^m\otimes\ell^2(G_k)\), and set
\[
B=T^*T,\qquad B_k=T_k^*T_k,\qquad d_k=m|G_k|.
\]
Every \(B_k\) is a positive semidefinite integer \(d_k\)-by-\(d_k\) matrix.
Write \(T=\sum_{g\in S}C_g\otimes\lambda(g)\) with finite \(S\) and \(C_g\in M_m(\mathbb Z)\).
Unitarity of both regular representations gives a common spectral bound
\[
\|T\|,\|T_k\|\leq\sum_{g\in S}\|C_g\|,
\qquad 0\leq B,B_k\leq K I,
\]
where \(K\geq1\) is fixed and may be chosen larger than the square of this sum.

### Spectral convergence and kernel masses

Let \(\mu\) be the probability spectral measure of \(B\) for \(\varphi\), and \(\mu_k\) the eigenvalue counting measure of \(B_k\) divided by \(d_k\).
For a fixed nonnegative integer \(r\), the group-ring matrix \(B^r\) has finite support.
Eventually no nonidentity group element in that support lies in \(N_k\), so
\[
\frac{1}{d_k}\operatorname{Tr}(B_k^r)
=\varphi(B^r)
\quad\hbox{for all sufficiently large }k.
\tag{2}
\]
Indeed the normalized trace of a finite-group regular permutation is one at the identity and zero elsewhere, exactly as for the infinite regular representation.
Polynomial approximation of continuous functions on \([0,K]\) now yields weak convergence \(\mu_k\Rightarrow\mu\).

Injectivity of \(T\) implies \(\mu(\{0\})=0\).
Put \(\alpha_k=\mu_k(\{0\})\).
Then \(\alpha_k\to0\).
For example, for each \(\delta>0\), a continuous function on \([0,K]\) that equals one at zero, decreases linearly to zero at \(\delta\), and vanishes above \(\delta\), bounds \(1_{\{0\}}\) from above.
Use weak convergence and then \(\delta\downarrow0\).
This argument needs no theorem asserting convergence of arbitrary group-ring kernel dimensions.
Some or all finite quotient matrices \(T_k\) may still be singular.

### Integer products and truncated logarithms

The product of the nonzero eigenvalues of \(B_k\) is, up to sign, the first nonzero coefficient of its integer characteristic polynomial.
Positivity makes this product a positive integer; if \(B_k=0\), the empty product is one.
Consequently
\[
J_k:=\int_{(0,K]}\log t\,d\mu_k(t)
=\frac{1}{d_k}\log\!\prod_{\lambda>0}\lambda
\geq0.
\tag{3}
\]

For fixed \(0<\varepsilon<1\), \(f_\varepsilon(t)=\log\max(t,\varepsilon)\) is continuous on \([0,K]\), and
\[
\int f_\varepsilon\,d\mu_k
=\alpha_k\log\varepsilon
  +\int_{(0,K]}\log\max(t,\varepsilon)\,d\mu_k(t)
\geq\alpha_k\log\varepsilon+J_k
\geq\alpha_k\log\varepsilon.
\tag{4}
\]
First let \(k\to\infty\).
Weak convergence and \(\alpha_k\to0\) imply
\[
\int f_\varepsilon\,d\mu\geq0
\quad\hbox{for every }0<\varepsilon<1.
\]
Next let \(\varepsilon\downarrow0\).
The functions \(\log K-f_\varepsilon\) are nonnegative and increase.
Monotone convergence gives
\[
\int\log t\,d\mu(t)
=\lim_{\varepsilon\downarrow0}\int f_\varepsilon\,d\mu
\geq0.
\]
In particular the negative logarithmic part is integrable.
By the definition of the ordinary normalized Fuglede-Kadison determinant,
\[
\log\Delta_\varphi(T)
=\frac12\int\log t\,d\mu(t)\geq0.
\tag{5}
\]

This proves the exact required lower bound.
The order of limits in (4) is essential.
Replacing \(\alpha_k\log\varepsilon\) by zero before taking \(k\to\infty\), or claiming that all \(T_k\) are invertible, would be incorrect.
Equations (2)-(5) do not assert \(J_k\to\int\log t\,d\mu(t)\), and no uniform estimate on the smallest nonzero eigenvalues is required.

### Normalization and the source erratum

Sch01 uses the unnormalized trace \(\operatorname{Tr}_m\otimes\tau\) and a logarithmic determinant that excludes the kernel.
For the present injective \(T\),
\[
\int_{(0,\infty)}\log t\,
 d[(\operatorname{Tr}_m\otimes\tau)(1_{[0,t]}(T^*T))]
=2m\log\Delta_\varphi(T).
\]
Both the square and the trace normalization are necessary.
If \(T\) has a kernel, its ordinary determinant is zero even when the kernel-removed logarithmic integral is nonnegative.
The finite-quotient proof above does not justify discarding that distinction.

Sch01's appended erratum restricts its broader amenable-extension argument to normal amenable extensions.
The proof retained here only uses finite quotient representations and the elementary truncation argument; it uses none of those extension steps.
Its conclusion is therefore unaffected by the cited erratum.
This is not an audit or repair of Sch01's entire closure theorem.

## Closing the Capacity Estimate

Fix \(b>0\) with \(\det b=1\).
Rank non-decrease makes \(\eta(b)>0\).
Define
\[
c_i=\eta(b)^{-1/2}a_i b^{1/2},
\qquad
\widetilde T=(\eta(b)^{-1/2}\otimes1)T(b^{1/2}\otimes1).
\]
Then \(\sum_i c_ic_i^*=I_m\).
The ordinary determinant multiplicativity interface in [MS24-U005](../audits/literature/MS24/Yin_U005.md#ms24-u005), applied to bounded factors, gives
\[
\Delta_\varphi(\widetilde T)
=\det(\eta(b))^{-1/(2m)}
  \Delta_\varphi(T)\det(b)^{1/(2m)}
\geq\det(\eta(b))^{-1/(2m)}.
\]
The scalar logarithmic arithmetic-mean inequality and \(\tau(u_i u_j^*)=\delta_{ij}\) give
\[
\Delta_\varphi(\widetilde T)^2
=\Delta_\varphi(\widetilde T\widetilde T^*)
\leq\varphi(\widetilde T\widetilde T^*)
=\operatorname{tr}_m\!\left(\sum_i c_ic_i^*\right)=1.
\]
Hence \(\det\eta(b)\geq1\), and taking the infimum proves the bound.
Every inverse factor in this step is a finite-dimensional positive matrix.
Neither an unbounded inverse of \(T\) inside a determinant product nor continuity of the determinant under weak convergence is invoked.

The rank-decreasing alternative \(\operatorname{cap}(\eta)=0\) belongs to the separate qualitative rank/capacity interface in [Gur04-U002](../audits/literature/Gur04/Yin_U002.md#gur04-u002).
The positive lower bound proved here does not depend on that alternative or on a prior positive lower bound from GGOW20.

## Dependency Boundary, Evidence, and Downstream Use

| Component | Retained evidence and boundary |
| --- | --- |
| Linear hollow and full-submatrix algebra | Exact MSY23/Coh06 interfaces and independent review in MSY23-U001; full weak-algorithm foundations remain accepted external algebra. The current attempt to reopen the online book returned an access/parsing error, so it supplies no new primary verification beyond the earlier recorded inspection. |
| Full linear Haar evaluation is injective | MSY23 published pp. 47-48 re-extracted directly; its actual sign and \(n=1\) scope checked. The finite-cycle proof and the forward linear-kernel induction were rechecked against MSY23-U002. General free-field evaluation is stronger than needed. |
| Integer determinant lower bound | Local reconstruction (2)-(5), using finite integer characteristic polynomials, compact-support spectral convergence and injectivity. Primary Sch01 Lemma 6.8/Theorem 6.9/Remark 6.10 read online on 2026-09-12. A rendered screenshot request failed, so the source access is parsed-primary-text access. |
| Ordinary determinant identities | The explicitly retained Fuglede-Kadison multiplicativity and scalar spectral-calculus interface in MS24-U005. Their broader historical proofs are not attributed to the finite-quotient argument. |
| Finite von Neumann algebra structure | Faithful trace, polar decomposition, spectral measures, and trace-class cyclicity; exact finite-rank and inverse consequences shown above. No entropy comparison is needed. |

There is no circular dependence on MS24's semicircular determinant formula, its integer capacity theorem, or GGOW's integral capacity lower bound.
The proof first establishes Haar injectivity by algebra and bounded duals, then obtains the determinant bound from integral finite quotient matrices, and only then estimates capacity.
The semicircular formula may subsequently use this completed capacity estimate for Corollary 1.4.

This supplement upgrades the exact Sch01 specialization consumed by MS24 from a statement-only accepted input to an explicit proof reconstruction.
It does not upgrade the whole Sch01 article, every Cohn foundation, the full quantitative GGOW algorithms, or the general determinant-convergence problem.
It does not prove a spectral gap or an \(L^2\) inverse estimate for a semicircular matrix.

No new PDF was retained, no source file was altered, and no numerical test or formal verification was used.
The scope is the two upstream arrows and their interface with the already recorded integer-capacity proof.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_F0129_v1.md#independent-review), with its original inspected scope and relationship.

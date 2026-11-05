---
author: Yin
---

# Haar determinant limits beyond rank-one regular-bulk Schur updates

This continuing investigation concerns the unrestricted dense-coefficient contract of [Task F0015](../tasks/Yin_T_F0015_v1.md#contract).
The first structural reductions are [proved in C_F0192_v1](../claims/Yin_C_F0192_v1.md#statement), at their reviewed two-position, sparse-cycle and triangular scopes.
The new complete [conditional Haar-additive and rank-one Schur candidate](../claims/Yin_C_F0193_v1.md#statement) fixes the regular-bulk mechanism and its original affine application.
It has an open candidate assessment pending separate review.
Its full fixed argument, source applicability, original coefficient checks, nonnormal free-target identification and positive-FK/unbounded-inverse example are retained there without repetition here.
The [HZ25 source unit](../audits/literature/HZ25/Yin_U001.md#hz25-u001) owns the inspected local-law and ultra-small-integral inputs and their actual source-proof inspection limits.

## Remaining original-contract gaps

A full-rank or higher-rank fresh auxiliary coefficient does not give the physical-size Haar perturbation used by C_F0193.
For a rank-k coefficient, the corresponding rectangular compression leaves a repeated block I_k tensor V_N rather than a Haar matrix on U(kN).
The current conditional local law therefore does not apply merely by replacing N with kN.
A genuine extension would have to preserve that repeated-input dependence or find a different determinant reduction.

The rank-one mechanism also requires a boundedly invertible free background and a boundedly invertible scalar compression.
If the background is singular or its inverse is unbounded, the finite compression is not controlled by the bounded rational approximation used in the fixed proof.
If the compression has no bounded inverse, the additive deformation D_N=C_N^{-1} lacks the eventual deterministic norm guard needed by the inspected local law.
The proved coefficient-position symmetry can change the candidate background, but it does not establish either inverse condition for an arbitrary tuple.

Finally the strict-bulk inequalities leave the boundary cases ||d||_2=1 or ||d^{-1}||_2=1 untreated by the new argument.
At such a boundary the finite positive imaginary subordination values needed by the fixed weak-neighborhood proof may fail.
Approaching the boundary through proved coefficients is not sufficient by itself, because the unregularized finite determinant can develop a negative logarithmic defect in that limit.
The next discriminating questions are a physical repeated-Haar block estimate for k=2, or a fixed-boundary logarithmic estimate retaining the original coefficient tuple.
No claim is made that these interfaces are necessary to every possible solution of F0015.

## Direct polynomial anti-concentration comparison

On 2026-11-05 a bounded search for Haar log-determinant variance and single-ring fixed-parameter bounds also inspected Fefferman, Ghosh and Zhan, [Anti-Concentration for the Unitary Haar Measure and Applications to Random Quantum Circuits](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.57/LIPIcs.ITCS.2026.57.html), Theorem 6 and Remark 8, in the ITCS 2026 primary publication.
Its displayed exponent is 1/(4n²d), with prefactor O(n³d), for a degree-d polynomial in the entries of a Haar U(n) matrix and its adjoint.
Directly inserting a determinant of degree proportional to N gives an exponent of order N^{-3}.
At a normalized logarithmic threshold exp(−cN), that bound does not force the failure probability to zero, so this direct invocation does not supply the missing aggregate logarithmic estimate.
This is a limit of that displayed quantitative bound in this application, rather than a refutation of other uses of Haar polynomial anti-concentration.
The successful rank-one argument instead compresses to a full physical Haar additive perturbation and imports a singular-value local law before integrating the logarithmic defect.

<a id="offdiagonal-pilot"></a>
## An off-diagonal pivot can bypass both singular one-input backgrounds

The fixed conditional Haar-additive candidate also suggests an application outside the bounded-background Schur hypotheses.
This continuation is a new proof draft, conditional on adoption of the generic part of [C_F0193_v1](../claims/Yin_C_F0193_v1.md#conditional-haar-additive-statement), and is not part of that Claim's frozen review scope.
Consider
\[
 M_N=\begin{pmatrix}I_N+aU_N&bV_N\\cU_N&I_N+dV_N\end{pmatrix},
 \qquad e=ad-bc,
\]
with b≠0, and suppose B(z)=d+ez has no zero on the unit circle.
Put A(z)=1+az and R=A/B.
Assume the modulus law of R is nonconstant and
\[
 \int|R|^2\,dm>1,\qquad\int|R|^{-2}\,dm>1,
\]
allowing the second integral to be infinite.
The ratio R is bounded because B is bounded away from zero, but R is not required to be invertible.

Swap the two block columns of M_N, and set T_N=I_N+aU_N, S_N=I_N+dV_N.
The upper-left pivot is now bV_N, which is uniformly boundedly invertible without any condition on a or d.
The Schur complement is
\[
 H_N=cU_N-S_N(bV_N)^{-1}T_N.
\]
Because S_N commutes with V_N,
\[
 bV_NH_N=bcV_NU_N-S_NT_N
 =-Q_N',\qquad
 Q_N'=I_N+aU_N+dV_N+eV_NU_N.
\]
The finite determinant magnitudes therefore satisfy |det M_N|=|det Q_N'|.
The same bounded Schur factorization and ordinary FK multiplicativity give 2logΔ(M)=logΔ(Q') freely, with no inverse of T or S used.
Now
\[
 Q_N'=A(U_N)+V_NB(U_N)
      =\bigl(R(U_N)+V_N\bigr)B(U_N),
\]
and the free identity has the same order.
Thus the generic conditional Haar-additive limit for R(U_N)+V_N, together with the bounded continuous logarithmic factor B(U_N), supplies the original two-by-two affine limit.
The normalized factor is 1/2, both finitely and freely.
Free-target identification uses ordinary joint Haar *-moment convergence for the polynomial and rational expressions, as in the fixed generic application; it does not assume that R(u) is positive.

For a concrete new test take
\[
 a=d=b=1,\qquad c=\tfrac12,\qquad e=\tfrac12.
\]
Then
\[
 M_N=\begin{pmatrix}I_N+U_N&V_N\\\tfrac12U_N&I_N+V_N\end{pmatrix},
 \qquad
 R(z)=\frac{1+z}{1+z/2}.
\]
The exact moments are ∫|R|²dm=4/3 and ∫|R|^{-2}dm=+∞.
The latter divergence comes from the single circle root z=−1, whose Haar measure is zero.
Each one-input background I_2+A_j⊗u has a diagonal Schur factor 1+u and hence no bounded inverse, so the fixed bounded-background rank-one corollary does not apply to this ordered tuple.
The off-diagonal unitary pivot remains boundedly invertible and closes the finite/free reduction despite those two failed background guards.
Regular bulk would give positive ordinary FK determinant and an unbounded inverse for this full pencil through the displayed bounded Schur factors.
The next action is to incorporate this distinct off-diagonal application after the shared generic conditional lemma has been reviewed, without changing its already frozen statement or proof.
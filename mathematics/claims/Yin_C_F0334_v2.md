---
author: Yin
---

# The dihedral law characterizes actuality of a normal coordinate over a two-point marginal algebra

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(A=W^*(Z)\) for a bounded normal coordinate of diffuse law \(\mu\) in a finite tracial von Neumann algebra with faithful probability trace \(\tau\).
Let \(a=a(Z)\) and \(s\) be selfadjoint unitaries with \(\tau(a)=\tau(s)=0\).
Set \(B=W^*(a)\), \(N=W^*(a,s)\), \(M=W^*(A,s)\), and assume \(A,N\) are free with amalgamation over \(B\) for the trace-preserving conditional expectation.
Let \(v=as\), write \(\lambda\) for its law on the unit circle and \(m\) for Haar probability, and put
\[
 J=\iint_{z\ne w}|a(z)-a(w)|^2 |z-w|^{-2}\,d\mu(z)d\mu(w).
\]
On the represented starred polynomial algebra of \(Z,s\), a distinguished derivation with \(\delta Z=1\otimes1,\ \delta s=0\) and actual vacuum \(\xi=\delta^*(1\otimes1)\) exists exactly under the following conditions.

1. The scalar marginal of \(Z\) has an actual vacuum \(\xi_\mu\).
2. \(\lambda=\rho m\) with \(\rho\in L^3(m)\).
3. Either \(\rho=1\) almost everywhere or \(J<\infty\).

Under these conditions \(v\) has an actual scalar vacuum \(\xi_v\).
The partial liberation vacuum at \(Z\) with the skew convention \(\eta=\gamma^*(1\otimes1)\) is
\[
     \eta=1-\xi_v v^*\ \in L^2(W^*(v)),\qquad
     \|\xi\|_2^2=\|\xi_\mu\|_2^2+\frac{\int\rho^3\,dm-1}{6}\,J .
\]
The last summand is zero for \(\rho=1\), including \(J=\infty\) in that case.
The [bounded-domain theorem for this model](Yin_C_F0334_v1.md#statement) gives both original relative domains and bounds both oriented right slices by \(C(\|\xi_\mu\|_2+(1+\|\eta\|_2)\sqrt J)\) in the non-Haar case, or by \(C\|\xi_\mu\|_2\) in the Haar case.
These assertions also hold with \(s=uau^*\) for a unitary free from \(A\), since the resulting two-symmetry algebra satisfies the specified conditional freeness.
The criterion tests the product law of \(as\) and requires no vacuum for \(u\).

## Argument

### Restricting the actual gradient to the rotation algebra

Assume first that the distinguished derivative and its vacuum exist.
The marginal restriction gives \(\xi_\mu=\mathbb E_A\xi\).
Use the [two-point restriction](Yin_C_F0334_v1.md#locating-the-liberation-vector-in-the-two-symmetry-algebra) to put \(\eta\) in \(L^2(N)\), with zero same-sign compressions, and to adjoin \(a\) to the liberation graph.
Write \(\operatorname{ad}x=x\otimes1-1\otimes x\).
On \(N_0=\operatorname{alg}^*(a,s)\), \(\gamma\) takes \(a\) to \(\operatorname{ad}a\) and kills \(s\).

From \(ava=v^*\), every word of \(N_0\) is a Laurent monomial of \(v\) or such a monomial followed by \(a\).
Every odd reflection word has zero trace, since by cyclic reduction it has the trace of \(a\) or of \(s\), both zero.
It follows that \(L^2(W^*(v))\) and \(L^2(W^*(v))a\) are orthogonal and span \(L^2(N)\).
Simultaneous negation of \(a,s\) preserves all their tracial moments and is a trace-preserving automorphism of \(N\).
It fixes the first of these spaces pointwise and acts by minus one on the second.
The generator formulas for \(\gamma|_{N_0}\) are equivariant, so its vacuum \(\eta\) is fixed and belongs to \(L^2(W^*(v))\).
The relation \(ava=v^*\) also shows that \(\lambda\) is conjugation invariant.

If \(p=1_{\{\lambda_0\}}(v)\ne0\), then \(\tau(pa)=\tau(sp)=0\) by the preceding orthogonality.
Apply the [kernel projection identity](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) to \(v-\lambda_0\) in the liberation graph on \(N_0\).
This application may use the Hilbert domain \(L^2(N)\), since the restricted derivation is closable there and has values in its coarse space.
As \(v-\lambda_0\) is normal, \(p\cdot\gamma(v)\cdot p=0\).
But \(\gamma v=a\otimes s-1\otimes v\), whose compressed double trace is \(-\lambda_0\tau(p)^2\ne0\).
Hence \(\lambda\) is diffuse, and Laurent polynomial values have their represented scalar divided difference.

Write \(m_k=\tau(v^k)\).
For \(n>0\), cutting \(v^n\) gives double trace \(-\sum_{k=0}^{n-1}m_k m_{n-k}\), since both legs of the \(a\otimes s\) term are reflection words.
For \(v^{-n}\), cutting with \(\gamma(v^*)=v^*\otimes1-s\otimes a\) gives \(+\sum_{k=0}^{n-1}m_{-(k+1)}m_{-(n-k-1)}\).
Both formulas are the negatives of the double traces for the scalar angular derivation \(\mathcal L v=1\otimes v\) with its inverse rule.
For a Laurent polynomial \(f\), the scalar identity \(w d_{f/v}(z,w)=d_f(z,w)-f(z)/z\), where \(d\) is divided difference, now shows
\[
        \iint d_f\,d\lambda^2
        =\langle 1-\eta,f(v)v^*\rangle
        =\langle(1-\eta)v,f(v)\rangle .
\]
This gives the actual scalar vacuum of \(v\) and \(\eta=-(\xi_v v^*-1)\).
The [unitary angular vacuum identity](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) gives \(\lambda=\rho m,\ \rho\in L^3(m)\) and \(3\|\eta\|_2^2=\int\rho^3\,dm-1\).
The latter vanishes precisely at \(\rho=1\) by strict convexity.
The spectral-density formula in v1 and its inverse-gap bound give condition 3.

### Constructing the represented derivations from the scalar data

Conversely suppose the three conditions hold.
The \(L^3\) circle density gives an actual scalar vacuum for \(v\), as can be seen directly from Laurent moments.
Put \(G=P_-\rho-P_+\rho\), where \(P_\pm\) are the strictly negative and positive Fourier projections.
Their [circle \(L^3\) bound](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) gives \(G\in L^3(m)\subset L^2(\lambda)\) by Holder.
For positive \(n\) the bilinear Fourier pairing gives
\[
 \int z^n G(z)\rho(z)\,dm(z)
      =\sum_{k=1}^{n}m_k m_{n-k};
\]
the negative-mode terms with index \(k>n\) cancel the positive-mode terms.
Indeed \(m_k=\widehat\rho(-k)\), and the two infinite product sums are absolutely convergent by Cauchy--Schwarz for the square-summable Fourier coefficients.
Conjugation gives the inverse-power calculation with its negative sign because \(G\) is purely imaginary.
The integral at \(n=0\) is zero.
Thus \(H=G^*\) represents the angular double trace and \((1+H)v\) represents the scalar divided-difference vacuum by the same \(f/v\) identity.
In particular \(H=\xi_vv^*-1\), with \(3\|H\|_2^2=\int\rho^3\,dm-1\).

Define on the sign words \(\Gamma_N a=\operatorname{ad}a\), \(\Gamma_N s=0\).
The two sign relations are respected by Leibniz.
There are no further represented polynomial relations: the normal form \(f(v)+g(v)a\) is orthogonal in its two summands, and the diffuse circle law makes a Laurent polynomial of norm zero identically zero.
The moment calculations for rotational words above give \(-H\) as vacuum on that subspace.
Odd reflection words give zero on both sides, by simultaneous negation, equivariance of \(\Gamma_N\) and invariance of \(H(v)\) under this grading.
Thus \(-H\) is the actual vacuum of \(\Gamma_N\) on \(N_0\), and \(\Lambda_N=\operatorname{ad}-\Gamma_N\) kills \(B\) with vacuum \(H\).

Define a formal derivation \(\Lambda\) on the algebraic amalgamated product of \(A,N_0\), taking \(\Lambda_N\) on \(N_0\) and zero on \(A\), with values in the represented outer coarse bimodule.
The prescriptions agree on \(B\); this defines the Leibniz calculation before any assumption on the kernel of evaluation.
For every formal input \(x\) its double trace is \(\langle H,\operatorname{ev}(x)\rangle\).
To check this, reduce into words centered over \(B\).
A reduced word with at least one centered \(A\)-letter is orthogonal to \(L^2(N)\) in the represented trace.
In each nonzero cut at an \(N_0\)-letter a nonempty prefix ending in a centered \(A\)-letter or suffix starting in one has zero conditional expectation onto \(N\).
Since both differentiated legs belong to \(N_0\), the double trace vanishes.
Pure \(A\)-words also pair to zero with \(H\): its \(B\)-projection vanishes since it is centered in \(W^*(v)\), orthogonal to \(a\).
The \(N_0\)-words give the verified scalar identity.

If \(\operatorname{ev}(x)=0\), test this identity on \(p^*xq^*\) for every pair of algebraic words \(p,q\).
The two outer product terms containing the undifferentiated \(x\) vanish, so \(\Lambda x\) is orthogonal to \(\operatorname{ev}(p)\otimes\operatorname{ev}(q)\) by the two trace pairings.
These simple tensors are total since the represented algebra is weakly dense.
Thus \(\Lambda x=0\), proving descent to every represented relation.
Now \(\Gamma=\operatorname{ad}-\Lambda\) on the restricted original core takes \(\operatorname{ad}\) on \(Z,Z^*\) and zero on \(s\) and has vacuum \(\eta=-H\).
On the full sign algebra \(-H\) has zero same-sign blocks, by the same compressed double-trace calculation as in the [two-point restriction](Yin_C_F0334_v1.md#locating-the-liberation-vector-in-the-two-symmetry-algebra).
Since \(\Gamma_N\) is realized and the restriction to \(N_0\) has the verified vacuum, that calculation needs no already constructed \(\delta\).
The conditional freeness computation there consequently gives
\[
       d\nu_\eta=2\|H\|_2^2 1_{\{a(z)\ne a(w)\}}\,d\mu^2 .
\]
This expression gives zero measure if \(\rho=1\), and otherwise has finite inverse-gap energy \(\|H\|_2^2J/2\) by condition 3.

Finally apply [divided-difference descent](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) and [the scalar adjoint reconstruction](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) to this relative core, as in the [projection version of the criterion](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries).
In detail, the formal divided difference at \(Z,Z^*\), with \(s\) killed, recovers \(\Gamma\) upon inner multiplication by \(z-w\).
This multiplier is injective on the coarse space by diffuseness.
Consequently the formal derivative descends; for its double trace the soft inverse gap converges on the liberation vacuum to \(S_{1/(\bar z-\bar w)}\eta\) by the finite inverse-gap energy, and its row/column correction converges weakly to \(\xi_\mu\) by scalar actuality.
These are the two orthogonal terms in the actual adjoint vacuum on all represented words.
Only the distinguished marginal is used in this reconstruction.
Taking squared norms proves the identity in the statement.
The [original domain result](Yin_C_F0334_v1.md#statement) and its [free conjugation instance](Yin_C_F0334_v1.md#the-opposite-sign-term-and-the-zero-vacuum-boundary) hence apply to exactly these scalar data.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:08 |
| status | open |
| reason | Fix the necessary and sufficient scalar criterion for the two-point amalgamated normal model and the exact vacuum norm for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalence of the three scalar conditions and actual relative vacuum, exact rotation gradient and cubic vacuum norm, with relative domain consequence. |
| argument | [Argument](#argument) | Dihedral parity, exclusion of atoms, angular double traces, scalar construction, descent through the represented amalgamated product and inverse-gap reconstruction. |
| dependency | [Two-point restriction](Yin_C_F0334_v1.md#locating-the-liberation-vector-in-the-two-symmetry-algebra) | Necessity of the sign algebra localization and direct conditional calculation of the two off-sign joint spectral measures. |
| dependency | [Two-point domain theorem](Yin_C_F0334_v1.md#statement) | Original canonical domains after actuality and the free conjugation instance. |
| dependency | [Kernel projection identity](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the graph derivative at a hypothetical atom of the unitary product. |
| dependency | [Circle angular identity](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) | Angular vacuum, Fourier projection bounds on \(L^3\), absolute continuity and cubic energy of an actual circle law. |
| dependency | [Divided-difference descent](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Injection by the marginal gap and descent of the formal normalized derivative. |
| dependency | [Actual adjoint reconstruction](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Orthogonal scalar and off-diagonal vacuum terms and their Hilbert norms. |
| dependency | [Relative sign criterion](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Applying the one-coordinate reconstruction with a killed atomic selfadjoint sign. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:20 |
| status | proved |
| reason | R_F0341 v2 checked the exact rotation-law criterion and vacuum norm, the Haar boundary, both directions on the represented relative core, the retained v1 inputs and all seven declared dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalence of the three scalar conditions and actual relative vacuum, exact rotation gradient and cubic vacuum norm, with relative domain consequence. |
| argument | [Argument](#argument) | Dihedral parity, exclusion of atoms, angular double traces, scalar construction, descent through the represented amalgamated product and inverse-gap reconstruction. |
| dependency | [Two-point restriction](Yin_C_F0334_v1.md#locating-the-liberation-vector-in-the-two-symmetry-algebra) | Necessity of the sign algebra localization and direct conditional calculation of the two off-sign joint spectral measures. |
| dependency | [Two-point domain theorem](Yin_C_F0334_v1.md#statement) | Original canonical domains after actuality and the free conjugation instance. |
| dependency | [Kernel projection identity](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the graph derivative at a hypothetical atom of the unitary product. |
| dependency | [Circle angular identity](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) | Angular vacuum, Fourier projection bounds on \(L^3\), absolute continuity and cubic energy of an actual circle law. |
| dependency | [Divided-difference descent](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Injection by the marginal gap and descent of the formal normalized derivative. |
| dependency | [Actual adjoint reconstruction](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Orthogonal scalar and off-diagonal vacuum terms and their Hilbert norms. |
| dependency | [Relative sign criterion](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Applying the one-coordinate reconstruction with a killed atomic selfadjoint sign. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0341_v2.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

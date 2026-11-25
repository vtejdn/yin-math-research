---
author: Yin
---

# What scalar moments determine about a rational kernel projection

## Statement

For a bounded rectangular matrix \(X\), the constant coefficient at zero of \(z(z+X^*X)^{-1}\) is the orthogonal projection \(p\) onto \(\ker X\).
How much of its rationality can one detect from the scalar moments of \(X^*X\)?
One fixed two-by-two input over the infinite cyclic group has a kernel of normalized trace \(1/2\), although every finite prefix of its moments also occurs at an invertible input arbitrarily close to it.
The two inputs even give different answers to rational recoverability from the single observable \(X^*X\).
If one can also exhibit rational matrices whose ranges lie in the kernel, the missing kernel dimension admits a two-sided estimate, and a sequence of such estimates can certify rationality over the full group algebra.

Let \(G\) be a discrete group, \(M=\mathcal N(G)\), \(U=L^0(M)\), and \(D_G\) the division closure of \(\mathbb CG\) in \(U\).
Take \(X\in M_{a,b}(D_G)\) with bounded entries, \(a,b\ge1\), and put \(B=X^*X\).
Let \(\tau_b\) be the normalized matrix trace extending the canonical group trace, \(\mu\) the probability spectral law of \(B\), \(m_j=\tau_b(B^j)\), and \(r\) affiliated matrix rank for the **unnormalized** matrix trace.
Write \(\lambda_d\) for the minimum of \(\int|q|^2\,d\mu\) over complex polynomials of degree at most \(d\) satisfying \(q(0)=1\).

1. Every \(Y\in M_b(D_G)\) satisfying \(XY=0\) gives the interval
   \[
       r(Y)/b\ \le\ \tau_b(p)\ \le\ \lambda_d,\qquad
       \lambda_d\downarrow\tau_b(p).
   \]
   Its upper endpoint uses only \(m_0,\ldots,m_{2d}\).
   If the positive spectrum of \(B\) lies in \([\eta,R]\), with \(0<\eta\le R\), then
   \[
       0\le\lambda_d-\tau_b(p)\le
       (1-\tau_b(p))(1-\eta/R)^{2d}\qquad(d\ge1).
   \]
   If an independent bound puts every positive value of \(\tau_b(p)-r(Y)/b\) for the witnesses under consideration at least \(\delta>0\), the single strict inequality \(\lambda_d-r(Y)/b<\delta\) certifies that \(Y\) exhausts the kernel and gives \(p\in M_b(D_G)\).
   For example, if \(r(p)\) and the permitted values of \(r(Y)\) are integers, one can take \(\delta=1/b\).

2. The condition \(p\in M_b(D_G)\) is equivalent to the existence of integer orders \(d_j\to\infty\) and matrices \(Y_j\) with \(XY_j=0\) and
   \[
                         \lambda_{d_j}-r(Y_j)/b\longrightarrow0
   \]
   such that \(Y_j=\alpha_j L_j^{-1}\beta_j\) for one fixed pivot size \(h\ge1\) and finite group support \(F\subset G\).
   Here \(L_j,\alpha_j,\beta_j\) have sizes \(h\times h,b\times h,h\times b\), all their entries are supported on \(F\) in \(\mathbb CG\), and \(L_j\) is invertible over \(U\).
   Their complex coefficients can vary with \(j\).
   Under these hypotheses a single \(Y\) of the same form exhausts the kernel.
   Equivalently, one may replace \(r(Y_j)/b\) by the ordinary normalized trace of \(t_jY_jY_j^*(I+t_jY_jY_j^*)^{-1}\) for suitable positive real numbers \(t_j\).

3. Over \(G=\mathbb Z\), one fixed \(X_0\in M_2(\mathbb C G)\) and, for each \(K\ge1\), invertible bounded operators \(X_K\in M_2(\mathbb C G)\) have the same moments \(m_0,\ldots,m_K\) for their respective positive matrices.
   Each \(X_K\) can be chosen arbitrarily close to \(X_0\) in norm, with both positive spectra contained in \([0,10]\).
   The projection for \(X_0\) has normalized trace \(1/2\) and lies outside the division closure of \(\mathbb C[X_0^*X_0]\) in \(M_2(U)\).
   The projection for each \(X_K\) is zero.
   Both projections have entries in \(\mathbb C G\).
   Thus even a choice of the last moment made from the observed moments cannot give a correct decision at every input if it terminates at \(X_0\).
   This applies to deciding whether the kernel is nonzero and to deciding its rational recoverability from its single positive observable.

4. With \(G,a,b\) fixed and the entries of **both** group-ring inputs supported on a prescribed finite set \(F\), there exists a finite \(K(G,a,b,F)\) such that equality through moment \(K\) implies equality of the entire scalar laws.
   This determines the kernel trace and rational recoverability from the single observable on that class, without giving an effective stopping order or a group-ring formula for the projection.

For a finitely generated group \(G\), the unrestricted finite-rank equation detects \(D_G\) for every affiliated element if and only if the two bounds in assertion 2 can be made to meet in the limit for every rectangular group-ring matrix \(X\).
The size \(h\) and support \(F\) may depend on \(X\).
Indeed the [matrix kernel criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) equates complete deletion with rationality of all these projections.

## Argument

### The two expansions of the resolvent

In the corner \(1-p\), \(B\) has an affiliated inverse \(B_+^{-1}\).
Splitting into the two corners gives the expansion at zero
\[
      z(z+B)^{-1}=p+\sum_{j\ge1}(-1)^{j-1}z^j B_+^{-j},
\]
where the inverse powers are extended by zero on \(p\).
This is a formal expansion with affiliated coefficients.
At infinity the trace has the norm-convergent expansion
\[
      \tau_b\bigl(z(z+B)^{-1}\bigr)
                =\sum_{j\ge0}(-1)^j m_j z^{-j},\qquad |z|>\|B\|.
\]
The moments in the statement are the coefficients at infinity.
At zero the operator \(p\) is also the formal residue of \((z+B)^{-1}\).
For positive real \(z\downarrow0\), integration of \(z/(z+t)\) against \(\mu\) gives the scalar limit \(\tau_b(p)=\mu(\{0\})\) by dominated convergence.

### The missing trace and an exact annihilator

The upper endpoint is the [Christoffel variational minimum](../audits/literature/Sim08/Yin_U001.md#christoffel-variational-principle).
Indeed, for \(q(t)=\sum_{i=0}^d c_i t^i\) its squared norm is \(\sum_{i,j}\overline{c_i}c_jm_{i+j}\), and the constraint is \(c_0=1\).
The finite-dimensional affine space of these polynomial classes in \(L^2(\mu)\) is closed, so the minimum exists even for a singular moment matrix.
Every admissible polynomial contributes \(\mu(\{0\})\) at zero.
Choose \(R>0\) with \(\|B\|\le R\).
The trial polynomials \((1-t/R)^d\) converge pointwise to \(1_{\{0\}}\) on \([0,R]\), with absolute value bounded by one.
Dominated convergence and the increasing trial spaces prove the claimed decreasing limit, including for finitely supported laws.
Bounding the same polynomials on \([\eta,R]\) gives the stated rate.
Earlier [polynomial localization estimates](Yin_C_A0014_v2.md#definition-christoffel-minima-at-the-target-point) use these minima to control spatial tails for scalar kernels.

Write \(e\) for the range projection of the affiliated matrix \(Y\).
The equation \(XY=0\) gives \(e\le p\), so \(r(Y)/b=\tau_b(e)\) is the lower endpoint.
Trace equality forces \(e=p\) by faithfulness.
In this case \(YY^*\) is supported on \(p\) and is invertible as an affiliated operator in that corner.
On \(1-p\) the restriction of \(B\) is an affiliated unit, so \(B+YY^*\) is an affiliated unit and
\[
                        p=YY^*(B+YY^*)^{-1}.
\]
The adjoint preserves \(D_G\) since it preserves \(\mathbb CG\) and carries legal inverses to legal inverses.
The displayed inverse has entries in \(D_G\) by [matrix inversion in the division closure](Yin_C_A0132_v1.md#argument).
The strict finite-order criterion follows by applying the independent separation bound to \(0\le \tau_b(p)-r(Y)/b\le\lambda_d-r(Y)/b\).

### Maximal rank with fixed group support and size

Suppose a sequence from assertion 2 is given, and use one complex affine space for all coefficients of \(L,\alpha,\beta\).
The entries of the matrices
\[
       J=\begin{pmatrix}L&\beta\\X\alpha&0\end{pmatrix},
       \qquad T=\begin{pmatrix}L&\beta\\\alpha&0\end{pmatrix}
\]
are polynomials in these complex coordinates with bounded operator coefficients.
The set \(V=\{r(J)\le h\}\) is [Zariski closed](Yin_C_A0128_v1.md#statement).
At an invertible \(L\), Schur elimination gives \(r(J)=h+r(XY)\) and \(r(T)=h+r(Y)\).
All the sequence points belong to \(V\).
Choose an irreducible component containing infinitely many of them.
On it the maximal ranks of \(L\) and \(T\) occur simultaneously outside the union of two countable families of proper closed sets, by the same rank theorem and the Baire argument in its proof.
The maximum rank of \(L\) is \(h\), as witnessed by any of these sequence points, so the selected \(L\) is an affiliated unit.
Membership in \(V\) gives \(XY=0\).
The interval in assertion 1 and the shrinking widths give \(r(Y_j)\to b\tau_b(p)\).
Maximality of \(r(T)\) thus gives \(r(Y)\ge b\tau_b(p)\), while \(XY=0\) gives the opposite bound.
The preceding formula recovers \(p\).
Conversely, if \(p\in M_b(D_G)\), take \(Y_j=p\) and combine [group-ring realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) for the finitely many entries of \(p\) into a single block diagonal pivot.
The upper endpoints then decrease to the constant lower endpoint.
For every witness \(Y\), the positive contractions \(C_t=tYY^*(I+tYY^*)^{-1}\) have entries in \(D_G\), satisfy \(XC_t=0\), and increase strongly to the range projection \(e\) as \(t\to\infty\).
This follows by applying \(s\mapsto ts/(1+ts)\) to the positive affiliated matrix \(YY^*\).
Thus \(\tau_b(C_t)\uparrow r(Y)/b\), and for the sequence of witnesses one can choose \(t_j\) with trace error less than \(1/j\).
Conversely the deficit with \(r(Y_j)/b\) is bounded above by the deficit with \(\tau_b(C_{t_j})\).
All ranks in this argument are taken in \(G\) itself, including for groups without a chosen family of finite models.

### Indistinguishable finite moments at one fixed cyclic-group input

Let \(h\) generate \(G=\mathbb Z\), put \(t=2+(h+h^*)/2\), and take \(X_0=\operatorname{diag}(0,t)\).
In the Fourier representation the scalar group trace \(\tau\) is normalized Haar integration on the circle, and \(t=2+\cos\theta\) has full support on \([1,3]\).
In particular \(p_0=\operatorname{diag}(1,0)\).
The positive part of the law of \(B_0=X_0^*X_0\) has support \([1,9]\).
Its Zariski closure contains zero, where the full law has mass \(1/2\), so the [single-observable rationality criterion](Yin_C_A0154_v1.md#statement) excludes \(p_0\) from the division closure generated by \(B_0\).

Fix \(K\) and real variables \(\varepsilon,c_1,\ldots,c_K\).
Set \(s_c=t+\sum_{j=1}^K c_jt^{2j-1}\) and \(X_{\varepsilon,c}=\operatorname{diag}(\varepsilon,s_c)\).
For \(1\le k\le K\) the moment difference is the real polynomial
\[
       H_k(\varepsilon,c)
          =\tfrac12\bigl(\varepsilon^{2k}+\tau(s_c^{2k})-\tau(t^{2k})\bigr).
\]
It vanishes at \((0,0)\), and its Jacobian in the \(c\) coordinates there is
\[
       \partial_{c_j}H_k(0,0)=k\,\tau(t^{2k-1}t^{2j-1}).
\]
After division of row \(k\) by \(k\), this is the Gram matrix of \(t,t^3,\ldots,t^{2K-1}\).
Every nonzero linear combination has positive squared norm because its polynomial is nonzero somewhere on the support interval.
Since \(H\) is a real polynomial map and \(D_cH(0,0)\) is invertible, the real implicit function theorem gives \(c(\varepsilon)\to0\) with all \(H_k(\varepsilon,c(\varepsilon))=0\) near zero and \(c(0)=0\). [De Oliveira, Theorem 5](../audits/literature/dO14/Yin_U001.md#do14-u001)
The perturbed symbols converge uniformly to \(t\) on the circle.
For all sufficiently small \(\varepsilon>0\), one has \(s_{c(\varepsilon)}>1/2\), \(\|s_{c(\varepsilon)}\|<\sqrt{10}\), and \(0<\varepsilon<1\).
These choices give the invertibility, spectral bounds and arbitrary norm proximity in assertion 3.
Any rule that reads finitely many scalar moments at \(B_0\) receives identical answers at one of these positive invertible examples, through the largest moment it requested.
The resulting obstruction concerns scalar spectral data even though both full group-ring projections are rational.
More quantitatively, take \(K=2d\) with \(d\ge1\).
The common value of \(\lambda_d\) exceeds \(1/2\), since a minimizer taking value one at zero cannot vanish on the whole interval \([1,9]\).
It is at most \(1/2+\tfrac12(8/9)^{2d}\) by assertion 1 at \(B_0\).
Thus the same moment bound approaches the true kernel trace exponentially fast at the fixed input while overestimating it by more than \(1/2\) at the invertible comparison inputs.

### Finite determination when the input support is prescribed

Parametrize the two matrices by the real and imaginary parts of their group coefficients on \(F\).
For each \(j\), extraction of the identity coefficient in the group-ring trace expresses the difference \(P_j\) of their \(j\)-th moments as a real polynomial in finitely many variables.
The polynomial ring in these finitely many variables is a finite type algebra over \(\mathbb R\), hence Noetherian by the Hilbert basis theorem, so the ascending chain of ideals \((P_1,\ldots,P_k)\) stabilizes. [The Stacks Project, Lemma 10.31.3](https://stacks.math.columbia.edu/tag/00FO), [source inspection](Yin_C_F0091_v1.md#reuse-and-accepted-source-inputs)
For such a stabilization index \(K\) every \(P_j\) lies in \((P_1,\ldots,P_K)\).
Equality of the first \(K\) moments therefore implies equality at all orders.
For any particular pair, both laws are supported in a common compact real interval, where polynomial approximation of continuous functions then gives equality of the measures.
The criterion for recovery from a single observable depends only on this law.
The cyclic comparison above allows the support to grow with the number of matched moments.

## Assessment history

### Decision moment-certificates

| Field | Value |
| --- | --- |
| date | 2026-11-25T13:19 |
| status | proved |
| reason | The Christoffel minimum and the range ranks of rational annihilators bound the kernel trace on both sides, and maximal rank on one algebraic component yields an exact rational projection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two trace bounds, the rationality criterion, the fixed cyclic example and finite determination on prescribed input support. |
| argument | [Argument](#argument) | Attainment on an algebraic rank locus, trace approximation, matched moments by the implicit function theorem and stabilization of the moment ideal. |
| dependency | [Christoffel variational principle](../audits/literature/Sim08/Yin_U001.md#sim08-u001) | Variational minimum and the atom limit for compactly supported measures, with singular moment matrices handled directly. |
| dependency | [Algebraic rank sublevels](Yin_C_A0128_v1.md#statement) | Simultaneous attainment of the generic ranks on an irreducible component. |
| dependency | [Matrix inversion](Yin_C_A0132_v1.md#argument) | Inversion of a full-rank matrix over the division closure. |
| dependency | [Group-ring realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Combining realizations of rational entries into a single pivot. |
| dependency | [Single-observable criterion](Yin_C_A0154_v1.md#statement) | Recovery of the kernel projection from the law of one positive observable. |
| dependency | [All-column criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) | The group-level equivalence for all rectangular group-ring matrices. |
| dependency | [Euclidean implicit function theorem](../audits/literature/dO14/Yin_U001.md#do14-u001) | Existence of a real solution preserving the prescribed finite moments. |
| dependency | [Noetherian polynomial rings](Yin_C_F0091_v1.md#reuse-and-accepted-source-inputs) | The Hilbert basis theorem over a field for the ideal generated by the moment differences. |
| review | [Spectral moments](../audits/reviews/Yin_R_A0172_v1.md#spectral-moments) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-moment-certificates)

---
author: Yin
---
# Rational kernel projection transport from finite abelian coefficients

Date: 2026-11-12 (Asia/Hong_Kong).
This route-six discriminator for [A0001](../tasks/Yin_T_A0001_v1.md#contract) starts with finite group-ring middle coefficients rather than an arbitrary measurable projection.
For torsion-free abelian coefficient groups, it proves finiteness and integer path weights for any commuting transport orbit of an input-derived kernel projection.
A concrete example exhibits a nonstationary two-cycle, so stationarity cannot replace the finite-orbit conclusion.
These are explicit abelian Fourier and path-formula consequences, with no new Atiyah group class.
It distinguishes spectral rational projections from the actual group-ring projection hypothesis in [C_A0005 v2](../claims/Yin_C_A0005_v2.md#augmentation-rigidity-for-abelian-group-ring-matrix-projections).
This is a substantive continuation of the same projection-transport problem as C_A0005 v2; that version retains its arbitrary von Neumann orbit and scalar Bernoulli comparisons.
The mathematical calculation is a direct abelian Fourier, cyclic and Gram application; no historical priority is claimed.

## Statement

Let \(N\) be torsion-free abelian, let \(\sigma\) be an automorphism, and let \(G=N\rtimes_\sigma\langle t\rangle\).
Take \(A\in M_{k,d}(\mathbb CN)\), put \(B=A^*A\), and let \(p\in M_d(\mathcal N(N))\) be its actual kernel projection.
Assume all the translates \(\sigma^j(p)\), \(j\in\mathbb Z\), commute.
Use \(p_j=\sigma^{-j}(p)\) and
\[
e_\ell=(I_d-p_{-1})p_0p_1\cdots p_{\ell-1}(I_d-p_\ell).
\tag{F1}
\]
Then the transport orbit is periodic, with a period \(m\le2^d\).
Every finite Boolean product of the \(p_j\) has integer unnormalized trace.
For the actual finite group-ring matrix
\[
\mathcal H_A=
\begin{pmatrix}(t+t^{-1})I_d&B\\ B&0\end{pmatrix}
\in M_{2d}(\mathbb CG),
\tag{F2}
\]
one has
\[
\boxed{\dim_G\ker\mathcal H_A
=(\operatorname{Tr}_d\otimes\tau_N)(p)
 +\sum_{\substack{1\le\ell<m\\ \ell\ {\rm odd}}}
   (\operatorname{Tr}_d\otimes\tau_N)(e_\ell)
\in\{0,1,\ldots,d\}.}
\tag{F3}
\]
For \(m=1\), the sum is empty.
The kernel projection \(p\) is not assumed to have finite group-ring support or an augmentation value.
The explicit example below has \(N=\mathbb Z^2\), nonstationary orbit \(\sigma(p)=I_2-p\), and a four-coordinate finite group-ring realization with unnormalized kernel dimension two.
Its projection is rational but has no Laurent-polynomial representative, and formula (11) gives the actual complete kernel projection.

## Argument

### Finite coefficient origin and the surviving finite-orbit certificate

To prove the actual coefficient assertion, write \(F=\operatorname{Frac}(\mathbb CN)\).
Every nonzero denominator has finite support in a free abelian subgroup and becomes a nonzero Laurent polynomial on a finite torus.
Its zero set is Haar null, by the standard iterated one-variable polynomial argument used in the retained abelian Fourier calibrations.
Thus \(F\) embeds in the actual affiliated algebra.
For any finite matrix over \(F\), its rank over \(F\) equals its pointwise Fourier rank almost everywhere: choose a nonzero maximal minor, exclude its null zero set and all denominator zero sets, and use the vanishing of larger minors.
The unnormalized affiliated rank is consequently that integer.
This is the elementary abelian rank calculation, not a new source theorem or an assumed Atiyah assertion for the semidirect product.

Choose a matrix \(V\) over \(F\) whose columns form a basis for \(\ker_F A\).
If that kernel is zero, \(p=0\).
Otherwise \(V\) has full column rank almost everywhere, so \(V^*V\) is invertible over \(F\) and
\[
p=V(V^*V)^{-1}V^*\in M_d(F).
\tag{F4}
\]
The Fourier formula is the actual orthogonal kernel projection almost everywhere.
All entries of each such calculation involve only a finitely generated subgroup of \(N\); the same reasoning therefore applies when \(N\) is not finitely generated, using the [coset trace comparison](../tasks/Yin_T_A0001_v1.md#reduction-to-finitely-generated-groups).
Automorphic translates and finite Boolean products of commuting projections remain in \(M_d(F)\).
Every nonzero such projection has positive integer trace, hence trace at least one.
Apply the already proved [Boolean lower-bound lemma](../claims/Yin_C_A0005_v2.md#a-trace-lower-bound-forces-a-finite-boolean-orbit) with total trace \(d\) and lower bound one.
It gives at most \(2^d\) members of the transport orbit; the invertible transport permutes this finite orbit, yielding the stated period \(m\).

The matrix \(B+p\) is an independently certified actual affiliated unit.
Indeed the actual Fourier decomposition gives \(B\) positive definite on the complementary fiber and the identity on the \(p\)-fiber.
Its inverse lies in \(M_d(F)\) by the same nonzero determinant argument.
Put
\[
X=(B+p)^{-1},\qquad J=\operatorname{diag}(I_d,X).
\]
Since \(B,p,X\) commute and \(Bp=0\), \(BX=XB=I_d-p\).
Consequently
\[
J\mathcal H_AJ=
\begin{pmatrix}(t+t^{-1})I_d&I_d-p\\I_d-p&0\end{pmatrix}.
\tag{F5}
\]
This is a closed affiliated congruence by already certified units, so it preserves rank and closed-kernel dimension.
The [commuting path calculation](../claims/Yin_C_A0005_v2.md#path-blocks-and-the-exact-kernel-dimension) applies verbatim in the matrix amplification with restricted unnormalized trace.
Its bounded kernel parametrization and component unitaries operate on \(p\ell^2(G)^d\); they do not require scalar-valued coefficients.
It gives the trace of \(p\) plus the odd finite-path start traces.
Periodicity implies \(e_\ell=0\) for \(\ell\ge m\): the retained factor \(p_{m-1}\) then equals the deleted neighbor \(p_{-1}\).
This proves the finite sum and its integrality.
Also the sum of all finite start projections is bounded by \(I_d-p_{-1}\), so the odd-path contribution is at most \(d-(\operatorname{Tr}_d\otimes\tau_N)(p)\), proving the range in (F3).
The all-open component remains injective by the independent cyclic \(t+t^{-1}\) test, as in the cited path argument.
The proof neither asserts all transport orbits commute nor treats noncommuting products as Boolean projections.

### Actual group and certified denominator

Let \(N=\langle x,y\mid[x,y]=1\rangle\cong\mathbb Z^2\), let \(\sigma(x)=y,\sigma(y)=x^{-1}\), and put \(G=N\rtimes_\sigma\langle t\rangle\), with \(t\) infinite order.
In particular \(txt^{-1}=y\) and \(tyt^{-1}=x^{-1}\).
An element of finite order projects trivially to the quotient \(\mathbb Z\), and then lies in the torsion-free subgroup \(N\); hence \(G\) is torsion-free.
Since \(\sigma^4=1\), the subgroup \(\langle x,y,t^4\rangle\cong\mathbb Z^3\) has index four.
This establishes the stated known virtually abelian coverage without using it in the calculation below.

Use the canonical trace and unnormalized matrix traces.
In \(\mathbb CN\), define
\[
a=x-x^{-1},\qquad b=y-y^{-1},\qquad
v=\binom a b,\qquad w=\binom b{-a},\qquad
s=a^*a+b^*b.
\tag{1}
\]
Both \(a,b\) are skew-adjoint and commute.
The scalar \(a\) is an independently certified actual affiliated unit by the infinite-order cyclic argument, since \(a=x(1-x^{-2})\).
The positive sum \(s\ge a^*a\) is therefore injective, with its affiliated inverse independently certified by the retained Gram/positive-kernel argument.
No use of the whole group's Atiyah theorem enters this certificate.
Moreover \(\sigma(a)=b,\sigma(b)=-a,\sigma(s)=s\), so \(s\) commutes with \(t\), as well as with \(\mathbb CN\).

### Actual spectral projection and its two-cycle

The direct identities are
\[
v^*v=w^*w=s,\qquad v^*w=0,\qquad vv^*+ww^*=sI_2.
\tag{2}
\]
Consequently
\[
p=vs^{-1}v^*,\qquad q=ws^{-1}w^*=I_2-p
\tag{3}
\]
are actual orthogonal projections in \(M_2(\mathcal N(N))\), also in the actual rational closure of \(M_2(\mathbb CN)\).
This bounded-projection assertion follows either from the Gram range projection or from the pointwise Fourier formula; it is not a claim that the entries of \(s^{-1}\) are bounded.
The column \(v\) has rank one because its first entry is a unit.
Thus \((\operatorname{Tr}_2\otimes\tau_N)(p)=1\), and likewise the trace of \(q\) is one.
Their actual transport satisfies
\[
\sigma(p)=q,\qquad \sigma(q)=p.
\tag{4}
\]
In particular the orbit commutes but is not stationary, and its overlap defect \(p\wedge\sigma^{-1}(I_2-p)\) equals \(p\).

The finite positive group-ring matrix
\[
B=ww^*=sq\in M_2(\mathbb CN)
\tag{5}
\]
has kernel projection exactly \(p\).
Its restriction to the \(q\)-corner has independently known affiliated inverse \(s^{-1}q\).
Thus the projection in (3) is derived from a specified finite group-ring matrix.

It is not itself a group-ring matrix.
For \(x=e^{i\theta},y=e^{i\phi}\), its upper-left entry is
\[
p_{11}(\theta,\phi)=
\frac{\sin^2\theta}{\sin^2\theta+\sin^2\phi}
\tag{6}
\]
away from the four common zeros.
It tends to one along \(\phi=0\) and to zero along \(\theta=0\) near the trivial character.
A Laurent-polynomial representative would be continuous and equal to this continuous rational function on the complement of those zeros, hence cannot have these incompatible limits.
Equality almost everywhere with a continuous representative implies equality on that open complement, so the null singular set cannot repair the obstruction.
There is therefore no augmentation value for this rational projection at the trivial character.
The earlier augmentation rigidity theorem has not been contradicted.

### Finite group-ring realization and exact kernel

Let \(T=(t+t^{-1})I_2\), and take the selfadjoint four-coordinate group-ring matrix
\[
H=\begin{pmatrix}T&B\\B&0\end{pmatrix}.
\tag{7}
\]
With the independently known actual unit \(J=\operatorname{diag}(I_2,s^{-1}I_2)\), affiliated multiplication gives
\[
JHJ=\begin{pmatrix}T&q\\q&0\end{pmatrix}=:H_p.
\tag{8}
\]
Both factors are invertible; the exact affiliated rank interface preserves rank and closed-kernel dimension.
Equation (4) implies \(Tp=qTp\), hence \(pTp=0\).
The bounded kernel equations for \(H_p\) are consequently
\[
\ker H_p=\left\{\binom{\xi}{-T\xi+\zeta}:
\xi,\zeta\in p\ell^2(G)^2\right\}.
\tag{9}
\]
The displayed parametrization is bounded and has bounded inverse given by the upper coordinate and the \(p\)-part of the lower coordinate.
It follows that
\[
\dim_G\ker H_p=2,\qquad
\dim_G\ker H=2,\qquad
\operatorname{rk}_G H=2,\qquad
\mu_H(\{0\})=\frac12.
\tag{10}
\]
The last atom uses the probability normalization by the full matrix size four; it is an allowed integer-rank atom.
The zero potential and matrix amplification use only the bounded kernel equations, not an assumed extension of a scalar source theorem.
In the matrix-amplified path language every retained component has length one: \(e_1=p\), all \(e_\ell\) for \(\ell>1\) vanish, and the two terms in the path formula each have unnormalized trace one.

An actual orthogonal projection for the original \(H\) can also be retained without applying \(s^{-1}\) to arbitrary Hilbert vectors.
Put \(F=\binom{sp}{-Tp}\), a bounded four-by-two operator, and \(C=p(s^2+T^2)p\) in the \(p\)-corner.
The scalar \(s\) commutes with \(T,p\), and \(T^2\) preserves the \(p\)-corner.
Thus \(C=F^*F\) is positive injective in that corner, since its first Gram summand is \(s^2p\).
With its affiliated corner inverse, the full orthogonal kernel projection is
\[
P_{\ker H}=FC^{-1}F^*+\begin{pmatrix}0&0\\0&p\end{pmatrix}.
\tag{11}
\]
Indeed \(HF=0\), the range closure of \(F\) has dimension one, and it is orthogonal to the lower \(p\)-coordinate because \(pTp=0\).
The sum in (11) is an orthogonal subprojection of the complete kernel with trace two; (10) and trace faithfulness give equality.
The expression \(FC^{-1}F^*\) is the bounded Gram range projection in the finite affiliated calculus.

## What this test changes and does not change

Finite group-ring coefficients do not force their rational spectral kernel projections to have stationary commuting transport.
Thus the actual-coefficient-origin requirement is realizable beyond the already proved stationary polynomial-projection case.
This example reaches a nonzero maximal overlap defect using only independently certified denominators.
It supplies no fractional unnormalized rank and no counterexample to A0001.
The coefficient field and the finite transport permutation remain fully controlled.
The general semidirect products in the statement are torsion-free abelian-by-cyclic and belong to the known elementary amenable coverage retained in the [Lin93 audit](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems).
Torsion-freeness follows directly by projecting a finite-order element to the quotient \(\mathbb Z\) and then using torsion-freeness of \(N\).
The next useful question is whether comparable input-derived projections can have noncommuting or genuinely uncontrolled intersection arithmetic, rather than whether the present nontrivial two-cycle exists.
Any broader inference must preserve the distinction between finite-support coefficients, rational spectral projections, their actual canonical traces and arbitrary measurable projections.

## Assessment history

### Decision reviewed-rational-transport

| Field | Value |
| --- | --- |
| date | 2026-11-11T16:31 |
| status | proved |
| reason | Independent complete review supports the rational finite-coefficient projection construction, finite commuting transport orbit, integer Boolean and path traces, exact kernel formula and nonstationary two-cycle example at their stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete hypotheses and conclusions (F1)--(F3), finite orbit bound and nullity range, plus the explicit finite group-ring example. |
| argument | [Argument](#argument) | Complete formulas (F4)--(F5) and (1)--(11), actual affiliated units, rational and Boolean rank arguments, matrix path interface, full kernel projection, known coverage and limitations. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0018_v3.md#finding-rational-kernel-transport) | Exact saved statement, whole argument, explicit example, source interfaces and final scope limitations. |

## Current assessment

[Selected decision](#decision-reviewed-rational-transport)


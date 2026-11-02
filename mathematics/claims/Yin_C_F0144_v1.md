---
author: Yin
---
# Actual ACSY vacua for a nonlinear free tuple with a non-L2 inverse

Human author: Yin.
The acsy_to_full_domain agent developed the letter-count adjoint estimate, graph-convergent inverse expansion and both actual target vacua.
Root identified the unbounded-inverse free nonlinear class as the next test and emphasized that the h-coordinate actual adjoint must be verified separately.
The developers are not independent reviewers; at the original candidate checkpoint this complete argument awaited independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let s_0,s_1 be standard variance-one free semicircular variables in their finite tracial von Neumann algebra (M,tau), with faithful normal probability trace.
Put H=L2(M,tau), Omega=1, and use inner products linear in the second variable.
For any real c>6, define
\[
 h=2+s_0,\qquad S=c+s_1,\qquad
 Y=ShS+\mathrm i hSh,\qquad A_X=\mathbb C\langle h,Y,Y^*\rangle.
 \tag{1}
\]
Then h is positive regular with unbounded inverse and h^-1 does not belong to L2(M), while the tuple X=(h,Y) generates M and satisfies the full ACSY condition A(X).

More precisely, use N=M bar tensor M^op and the unique target derivations of [C_F0142](Yin_C_F0142_v1.md#statement):
\[
 F=\partial_SY=Sh\otimes1+1\otimes(hS)^{\mathrm{op}}
           +\mathrm i h\otimes h^{\mathrm{op}},\quad
 \beta=F^{-1},\quad C=\partial_hY,
\]
\[
 \delta_Y(p)=(\partial_Sp)\beta,\qquad
 \theta_h(p)=\partial_hp-\delta_Y(p)C,\qquad p\in A_X.
 \tag{2}
\]
Both required actual adjoint domains are present:
\[
 1,C^*\in\operatorname{Dom}(\delta_Y:A_X\subset H\to L^2(N))^*.
 \tag{3}
\]
Their actual conjugate vectors are
\[
 v_Y=\partial_S^*(\beta^*),\qquad
 v_h=s_0-\partial_S^*(C^*\beta^*),
 \tag{4}
\]
where the reference adjoints in (4) really contain both displayed vectors.
The construction provides explicit convergent series for these adjoint values, as well as quantitative bounds below.

This is an actual A-positive nonlinear example with h^-1 not in L2.
It is not asserted to separate A and F.
In particular no conclusion is made about existence of arbitrary bare full-M duals, or about full M domains of the supplied canonical contractions or their adjoints.
Those remain distinct questions.

## Argument

### Reference hypotheses and the singular marginal

The checked [Miy22-U001 Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) supplies the standard free semicircular pair, its faithful trace, the full Fock word basis and the Chebyshev recurrence used below.
The word-cut formula (51), also for the letter 0, gives the actual conjugate variables s_0,s_1 for the shifted pair h,S: testing the vacuum tensor selects precisely the one-letter word.
Thus the original reference pair has a joint L2 conjugate system without an additional hypothesis.

The shifted semicircle h has spectrum [0,4] and probability density
\[
 d\mu(t)=\frac1{2\pi}\sqrt{t(4-t)}\,1_{(0,4)}(t)\,dt.
 \tag{5}
\]
There is no atom at zero, so h is regular.
Its spectrum reaches zero, making h^-1 unbounded, and the inverse-square integral diverges because the density is comparable to t^(1/2) near zero.
The other reference variable satisfies S>=(c-2)1>0.
Hence all reference assumptions of C_F0142 apply; that fixed result supplies generation, the actual represented target derivations, their uniqueness and the precise actual-adjoint criterion.
The remaining proof below verifies that criterion by reference adjoint graph convergence.

### Letter-count grading and the actual reference adjoint

Reuse the free Fock identification and word Chebyshev basis U_w from [Miy22-U001](../audits/literature/Miy22/Yin_U001.md#miy22-u001).
Let H_n be the closed span of all word vectors e_w having exactly n occurrences of the letter 1; the number of letter 0 is unrestricted.
These are mutually orthogonal and H is their Hilbert direct sum.
The source word recurrence and the Leibniz rule give
\[
 \partial_1U_w=\sum_{w=u1v}U_u\otimes U_v,
 \tag{51}
\]
where partial_1=partial_S.
For completeness, the recurrence is U_(iw)=s_i U_w-delta_(i,w_1)U_(tail w).
Differentiating it, its extra 1 tensor U_w term occurs exactly for i=1; the other terms group by the remaining letter-1 cuts and the same recurrence in the left word.
This proves (51) by induction from the empty word.
No scalar total-degree bound in s_0 is being used.

For j+k=n, concatenation with one inserted letter 1 defines a unitary
\[
 V_{j,k}:H_j\otimes_2H_k\longrightarrow H_{n+1},
 \qquad e_u\otimes e_v\longmapsto e_{u1v}.
\]
It is onto because every word with n+1 letters 1 has a unique cut at its (j+1)st occurrence of 1.
On
\[
 \mathcal K_n=\bigoplus_{j+k=n}H_j\otimes_2H_k,
\]
equation (51) and polynomial testing identify the ACTUAL Hilbert adjoint as
\[
 \partial_1^*\eta=\sum_{j+k=n}V_{j,k}\eta_{j,k},\qquad
 \|\partial_1^*\eta\|_2\le\sqrt{n+1}\,\|\eta\|_2.
 \tag{52}
\]
Indeed Cauchy--Schwarz bounds the displayed vector sum.
Its pairing against every polynomial is the adjoint pairing from (51), which proves actual domain membership for every vector in the closed space K_n.
Distinct n give output spaces H_(n+1), hence for K_<=n=sum_(r=0)^n K_r,
\[
 \mathcal K_{\le n}\subseteq\operatorname{Dom}\partial_1^*,
 \qquad
 \|\partial_1^*\eta\|_2\le\sqrt{n+1}\,\|\eta\|_2.
 \tag{53}
\]

Left and right multiplication by s_0 preserve each H_n: their creation/deletion actions change only letter 0.
Consequently every bounded element of W*(s_0), on either side, preserves these closed reducing spaces.
Left or right multiplication by s_1 sends H_n into H_(n-1) direct sum H_(n+1).
These facts also hold on each tensor leg.
In particular bounded functions of the two h variables preserve K_<=n; multiplication by s_1 in one leg increases the upper degree by at most one.

### The coarse inverse and its graph-convergent expansion

In N=M bar tensor M^op put
\[
 G=h\otimes1+1\otimes h^{\mathrm{op}},\qquad
 A=(h\otimes1)G^{-1},\qquad
 H_0=(h\otimes h^{\mathrm{op}})G^{-1}.
\]
These use the joint calculus of the two commuting h copies.
We have 0<=A<=1, I-A=(1 tensor h^op)G^-1, and ||H_0||<=||h||/2=2.
Also
\[
 g^2:=\|G^{-1}\|_2^2
   =\iint\frac{d\mu(s)d\mu(t)}{(s+t)^2}<\infty.
 \tag{54}
\]
To verify the last assertion directly, bound the density by pi^-1 sqrt(t).
With u=s+t, v=s/(s+t), the upper-bound integrand sqrt(st)(s+t)^(-2) ds dt becomes sqrt(v(1-v)) du dv on a subset of 0<u<8, 0<v<1.
Its integral is finite.
Thus the sum denominator is square integrable although each individual inverse is not.

Set
\[
 Z=(s_1\otimes1)A+(1\otimes s_1^{\mathrm{op}})(1-A)
       +\mathrm i H_0.
 \tag{55}
\]
Its norm is at most 2+2+2=6.
The opposite multiplication is essential for the second term: (1 tensor s_1^op)(1 tensor h^op)=1 tensor (h s_1)^op.
The original S-Jacobian satisfies exactly
\[
 F=(c+Z)G,\qquad
 \beta=F^{-1}=G^{-1}(c+Z)^{-1}.
 \tag{56}
\]
This is the same unique affiliated inverse as in C_F0142.
Since c>6, the second inverse has a norm-convergent Neumann series in N.
Let
\[
 \eta_n=c^{-n-1}(-Z^*)^nG^{-1},\qquad r=6/c<1.
\]
Then
\[
 \beta^*=\sum_{n\ge0}\eta_n\quad\hbox{in }L^2(N),\qquad
 \|\eta_n\|_2\le(g/c)r^n,\qquad
 \eta_n\in\mathcal K_{\le n}.
 \tag{57}
\]
For the degree assertion, approximate G^-1 in L2 by bounded joint functions of h.
These vectors belong to K_0.
Each left multiplication by Z* increases the degree by at most one, by the reducing-space observations above.
The L2 bound passes the approximation to eta_n, and the degree subspace is closed.

Equation (53) now gives
\[
 \sum_{n\ge0}\|\partial_1^*\eta_n\|_2
   \le(g/c)\sum_{n\ge0}\sqrt{n+1}\,r^n<\infty.
 \tag{58}
\]
Thus the partial sums converge in the graph norm of the closed actual adjoint partial_1*, and beta* belongs to its domain.

The coefficient C=partial_hY in C_F0142 is bounded and has total s_1-degree at most two.
Multiplying it on the left sends K_<=n into K_<=n+2.
Therefore
\[
 \|C^*\eta_n\|_2\le\|C\|(g/c)r^n,\qquad
 \|\partial_1^*(C^*\eta_n)\|_2
    \le\sqrt{n+3}\,\|C\|(g/c)r^n.
 \tag{59}
\]
The same graph convergence proves C*beta* in Dom partial_1*.
This second step explicitly checks the h-coordinate obstruction rather than inferring it from the vacuum test at 1.

### Transfer to the target core

For p in A_X, the fixed derivative is delta_Yp=(partial_1p)beta.
Tracial pairing in N gives
\[
 \begin{aligned}
 \langle1,\delta_Yp\rangle
   &=\langle\beta^*,\partial_1p\rangle
     =\langle\partial_1^*\beta^*,p\rangle,\\
 \langle C^*,\delta_Yp\rangle
   &=\langle C^*\beta^*,\partial_1p\rangle
     =\langle\partial_1^*(C^*\beta^*),p\rangle.
 \end{aligned}
 \tag{60}
\]
Every tensor pairing is legitimate because beta is L2, partial_1p and C are bounded, and the two graph-domain inclusions have been proved.
These are actual adjoint pairings on the dense target star algebra, not formal moments.
The C_F0142 criterion gives A(h,Y), with
\[
 v_Y=\partial_1^*\beta^*,\qquad
 v_h=s_0-\partial_1^*(C^*\beta^*).
 \tag{61}
\]
In particular their norms are bounded by the series in (58) and ||s_0||2 plus the series in (59).
This construction does not apply an unknown target derivation to S.
It starts with the reference partial_1 and then verifies the unique target restrictions.

The remaining full-domain question is genuine.
The estimates (52)-(59) control the actual vacuum vectors; they do not yet control (id tensor tau)delta_Y from the target operator norm into H.
The kernel-only finite-tensor estimate of C_F0139 cannot be applied to Z-dependent coefficients, since they involve s_1 itself.
No S or F conclusion for the unbounded-inverse tuple (1) is asserted in this section.


## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:01 |
| status | open |
| reason | Complete actual adjoint graph estimates prove the full ACSY condition for a concrete nonlinear free generating tuple with h^-1 not in L2. No bare full-domain implication or separation is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Concrete nonlinear ACSY example](#statement) | Every c>6, the singular marginal, generation, both actual conjugate vectors and the stated existential limits. |
| argument | [Complete proof](#argument) | Fock letter-count adjoint bound, coarse inverse integrability, two graph-convergent series and actual target pairings. |
| dependency | [Free Fock word model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Standard free semicircular normalization, trace, word Chebyshev basis and its recurrence. The partial letter-count estimate is proved here. |
| dependency | [Nonlinear target criterion](Yin_C_F0142_v1.md#statement) | Generation, unique represented coordinate derivations and equivalence with the two actual adjoint tests. No Hilbert--Schmidt-range statement from that Claim is needed. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:12 |
| status | proved |
| reason | Adopt the complete actual-vacuum construction after R_F0151 independently checked the relative Fock grading, both adjoint graph series, coefficient orders and exact target pairings. The presentation-only tuple reference is repaired as permitted by the review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Concrete nonlinear ACSY example](#statement) | Every c>6, the singular marginal, generation, both actual conjugate vectors and the stated existential limits. |
| argument | [Complete proof](#argument) | Fock letter-count adjoint bound, coarse inverse integrability, two graph-convergent series and actual target pairings. |
| dependency | [Free Fock word model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Standard free semicircular normalization, trace, word Chebyshev basis and its recurrence. The partial letter-count estimate is proved here. |
| dependency | [Nonlinear target criterion](Yin_C_F0142_v1.md#statement) | Generation, unique represented coordinate derivations and equivalence with the two actual adjoint tests. No Hilbert--Schmidt-range statement from that Claim is needed. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0151_v1.md#conclusion) | Entire statement and argument with both exact direct inputs; A-positive example only at this decision scope. |


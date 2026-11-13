---
author: Yin
---

# Phase spread after coordinate deletion for a nonreal Wigner product mode

<a id="statement"></a>
## Exact scope of phase spread

Use the real symmetric Wigner specialization and independent colors of [C196v1](Yin_C_F0196_v1.md#statement).
Fix \(z=x+iy\) with \(y\ne0\) and \(K\ge1\).
Write \(M=AB+2BA\), \(\Omega_K=\{\max(\|A\|,\|B\|)\le K\}\), and \(H=(M-xI)^2+y^2I\).
There exist positive constants \(\delta,\rho,a,b,d,c,C\) depending only on \(K,z\) and the two fourth-moment bounds with the following simultaneous assertions outside an event of probability \(Ce^{-cN}\), for all sufficiently large \(N\).
On \(\Omega_K\) every real unit vector within distance \(\rho\) of a real unit vector on at most \(\lfloor\delta N\rfloor\) coordinates satisfies \(\|Hv\|\ge a\).
On the same event every unit \(h\in\mathbb C^N\) with \(\|(M-zI)h\|\le b\) satisfies
\[
 \inf_{\theta\in\mathbb R,\ |D|\le\lfloor\delta N\rfloor}
 \|(\operatorname{Re}(e^{i\theta}h))_{D^c}\|\ge d.
 \tag{Deleted-phase-spread}
\]
Here \(D\) ranges over coordinate subsets.
Equivalently the real Gram matrix of \((\operatorname{Re}h)_{D^c},(\operatorname{Im}h)_{D^c}\) is bounded below by \(d^2 I_2\) for every such deletion.
The near-mode and the deletion may depend on all the entries of both matrices.
The probability estimate restricts the event to the fixed norm guard.

## Current assessment
[Selected decision](#decision-phase-spread-reviewed)

## Assessment history

### Decision phase-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T02:21 |
| status | open |
| reason | The four-rectangle difference and the simultaneous phase-spread conclusion are submitted for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Sparse exclusion for the real annihilating polynomial and deleted phase spread of every complex near-mode at a fixed nonreal shift. |
| argument | [Proof](#argument) | Independent rectangular differences, sparse covering and real phase transfer. |

### Decision phase-spread-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T02:30 |
| status | proved |
| reason | Independent review supports the uniform guarded sparse exclusion and the deletion bound for all phases of every approximate mode at the fixed nonreal shift. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Sparse real polynomial exclusion and simultaneous deleted phase spread. |
| argument | [Complete argument](#argument) | Four independent rectangles, corner difference, sparse net and phase transfer. |
| dependency | [Rectangular estimate](Yin_C_F0196_v1.md#affine-small-ball) | Fourth-moment bound and independent row count for nonzero real inputs after rescaling the entry differences. |
| review | [Whole-proof finding](../audits/reviews/Yin_R_F0203_v2.md#deleted-phase-spread-reviewed) | Fixed statement and argument including direct inspection of the rectangular dependency. |

<a id="argument"></a>
## Four independent differences

Fix \(S\) of size \(s=\lfloor\delta N\rfloor\), \(0<\delta<1/8\), and a deterministic real unit vector \(v\) supported in \(S\).
Choose disjoint \(T_1,T_2,T_3,T_4\) outside \(S\), each with \(\lceil N/5\rceil\) elements, and write \(T_0=S\).
The four off-diagonal rectangles indexed by \(T_j\times T_{j-1}\) have colors \(B,A,B,A\) as \(j\) increases.
Expose everything except the unordered entry pairs in these four rectangles.
In the conditional law write \(X_j^0,X_j^1\) for two independent copies of each rectangle with the transposed entries filled in by symmetry.
The eight random rectangles are independent.
For a choice \(\omega\in\{0,1\}^4\) let \(H^\omega\) denote the polynomial computed with \(X_j^{\omega_j}\).
If the conditional probability of \(\|(Hv)_{T_4}\|\le t\) is \(p\), the probability of this event at all sixteen corners is at least \(p^{16}\).
Indeed, starting with one indicator, double one of the as yet undoubled rectangle coordinates.
Conditional on every other variable, the mean of the product before this doubling is squared by taking two independent copies of that coordinate.
Jensen's inequality after integrating the other variables bounds the doubled expectation below by the square of the preceding expectation.
Four iterations give the assertion.
This iterates the [two-rectangle difference method](Yin_C_F0187_v19.md#quadratic-fixed-parameter-gap).

Put \(\Delta_j=X_j^1-X_j^0\), oriented from \(T_{j-1}\) to \(T_j\).
Up to a common sign the alternating sum of \((H^\omega v)_{T_4}\) is exactly
\[
 \Delta_4\Delta_3\Delta_2\Delta_1 v_S.
\]
To survive the four differences a matrix-entry monomial must contain a variable from each rectangle.
Its degree is at most four, hence it uses each rectangle once and has no other step.
The disjoint panels force the only walk from \(S\) to \(T_4\) visiting these four edges in four steps to traverse them in increasing order.
Of the four words in \(M^2\), only \(ABAB\) has the required colors read from the right, and its coefficient is one.
The terms of degree less than four cancel.
If all corner events hold, the displayed product has norm at most \(16t\).

Each difference has independent entries of variance \(2/N\).
After division by \(\sqrt2\), its raw entries have unit variance and uniformly bounded fourth moments.
By the [rectangular fourth-moment bound](Yin_C_F0196_v1.md#affine-small-ball), with zero center, a deterministic nonzero real input \(u\) has \(\|\Delta_j u\|\ge c_0\|u\|\) except with probability \(e^{-c_1N}\), for common \(c_0,c_1>0\).
Condition on the preceding differences in their product and apply this estimate at each step.
With probability at least \(1-4e^{-c_1N}\) the norm of the complete product is at least \(c_0^4\).
This estimate holds in every exposed background.
Taking \(t=c_0^4/32\), the sixteen-corner inequality gives \(p\le 4^{1/16}e^{-c_1N/16}\), uniformly in the support and the unit input.

## Sparse nets and all phases

On the guard \(\|H\|\le L=(3K^2+|x|)^2+y^2\).
Put \(\ell=\min(1/4,t/(4(1+L)))\).
Cover the real unit sphere of each support by an \(\ell\)-net of size at most \((1+2/\ell)^s\).
The number of supports is at most \((eN/s)^s\).
Choose \(\delta>0\) sufficiently small that the product of these two cardinalities is at most \(e^{c_1 N/32}\) for all sufficiently large \(N\).
By the fixed-vector estimate, except on an event of probability \(Ce^{-cN}\), every net point has \(\|Hv\|>t\).
Every unit vector within \(\rho=\ell\) of a sparse unit vector then satisfies \(\|Hv\|\ge a=t/2\) on the guard.
Supports of size less than \(s\) extend to size \(s\).

For a complex unit near-mode write \(u+iv=e^{i\theta}h\) and \(r=e^{i\theta}(M-zI)h\).
Reality of \(M\) gives \((M-xI)u+yv=\operatorname{Re}r\).
Consequently \( |y|\le |y|(\|u\|+\|v\|)\le (|y|+3K^2+|x|)\|u\|+\|r\|\).
If \(\|r\|\le |y|/2\), then \(\|u\|\ge d_0=|y|/(2(|y|+3K^2+|x|))\), uniformly in \(\theta\).
The identity \(H=(M-\bar z I)(M-zI)\) gives \(\|Hu\|\le(3K^2+|z|)\|r\|\) since \(H\) is real.
Choose \(b>0\) with \(b\le |y|/2\) and \((3K^2+|z|)b<a d_0\).
Thus \(u/\|u\|\) lies outside the real compressible set for every phase on the same good event.
For a real unit \(w\) and a deletion \(D\) with \(w_D\ne0\),
\[
 \|w-w_D/\|w_D\|\|^2=2(1-\|w_D\|)\le 2\|w_{D^c}\|^2
\]
where the truncated vector is embedded by zero extension.
When \(w_D=0\) the remaining mass is one.
Applying this observation to \(w=u/\|u\|\) gives (Deleted-phase-spread) with \(d=d_0\rho/\sqrt2\).
For each \(D\) the least eigenvalue of the indicated Gram matrix is the squared infimum over real phases.
No probability union over phases, near-modes or adaptive deleted sets is used.

---
author: Yin
---

# Local slope oscillation and curvature rows on Lipschitz spectral graphs

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra with faithful normal probability trace \(\tau\), satisfying the [actual starred conjugate-variable condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Suppose the law of \(X_i\) is \(h_*\mu\), where \(\mu\) is a probability on a compact real interval \(I\) of length \(D>0\), \(h(t)=t+\mathrm i g(t)\), and \(g\) is real and \(L\)-Lipschitz.
For \(x\in\operatorname{supp}\mu\) and \(j\ge0\) put \(r_j=2^{-j}D\), \(I_j(x)=I\cap[x-r_j,x+r_j]\), and
\[
 o_j(x)=\operatorname*{ess\,sup}_{I_j(x)}g'
         -\operatorname*{ess\,inf}_{I_j(x)}g',\qquad
 Q=\sup_{x\in\operatorname{supp}\mu}\sum_{j\ge0}
        \left(\frac{\mu(I_j(x))}{r_j}o_j(x)\right)^2 .
 \tag{1}
\]
The oscillation uses Lebesgue measure on the parameter interval.
If \(Q<\infty\), the canonical operator \(D_i=-\overline{(\mathrm{id}\otimes\tau)\delta_i}\) and its Hilbert adjoint have domains containing every bounded vector \(a\Omega\).
On these vectors \([X_k,D_i]=\delta_{ik}P_\Omega\), and the right slice on the original starred algebra has finite column cost.
The other normal coordinates can have arbitrary spectra and correlations.
In particular \(\mathsf A\) and \(\mathsf S\) are equivalent for tuples satisfying (1) at each coordinate.

For the graph \(g(t)=\operatorname{dist}(t,E)\) on \([0,1]\), where \(E\) is the middle-thirds Cantor set, let \(F\) be the union of \(E\) with the midpoints of its complementary gaps.
For \(\beta\ge0\) give the parameter the probability density
\[
 \rho_\beta(t)=c_\beta[\log(e/\operatorname{dist}(t,F))]^{-\beta}
                   \quad(t\in[0,1]\setminus F),\qquad \rho_\beta|_F=0.
 \tag{2}
\]
Then (1) and the uniform curvature-row bound of [C_F0078 v2](Yin_C_F0078_v2.md#statement) each hold exactly for \(\beta>1/2\).
For every \(\beta\) this is an actual scalar conjugate-variable law, and it also occurs in an explicitly correlated normal pair with actual conjugate variables.
The slope has infinite variation on every relative neighborhood of a Cantor point.
The threshold concerns the uniform curvature bound used to control arbitrary correlations.

## Argument

### Curvature estimates at one parameter point

Write \(\kappa(x,y,t)\) for the reciprocal circumradius of the three graph points \(h(x),h(y),h(t)\), with value zero for repeated or collinear triples.
For three distinct parameters \(a<b<c\), write \(m_{ab},m_{bc}\) for the corresponding secant slopes of \(g\).
The determinant of the two consecutive chord vectors has absolute value \((b-a)(c-b)|m_{ab}-m_{bc}|\).
In the formula for reciprocal circumradius, twice this determinant is divided by the product of the three chord lengths.
Bounding each length below by its horizontal projection gives
\[
 \kappa(a,b,c)\le \frac{2|m_{ab}-m_{bc}|}{c-a}.
 \tag{3}
\]
Both slopes are averages of the almost-everywhere derivative on subintervals of \([a,c]\), since \(g\) is Lipschitz.

For fixed \(x\) split \((y,t)\) by \(r_j/2<\max(|y-x|,|t-x|)\le r_j\).
All three points lie in \(I_j(x)\), and the extreme horizontal separation is greater than \(r_j/2\).
Thus (3) gives \(\kappa\le4o_j(x)/r_j\) on this shell, and integration proves
\[
    \sup_x\iint\kappa(x,y,t)^2\,d\mu(y)d\mu(t)\le16Q.                 \tag{4}
\]
For distinct \(x,y\) with \(s=|x-y|\), let \(r_k/2<s\le r_k\).
In the same shell partition with \(t\) variable only \(0\le j\le k\) can contribute.
Write \(a_j(x)=o_j(x)\mu(I_j(x))/r_j\) and \(H=\sqrt{1+L^2}\).
Since \(|h(x)-h(y)|\le Hs\) and \(o_j(x)\le2L\), the other required bound is
\[
 \begin{aligned}
 |h(x)-h(y)|\int\kappa(x,y,t)^2\,d\mu(t)
 &\le16H\sum_{j=0}^k \frac{s}{r_j}\,o_j(x)a_j(x)\\
 &\le64HL\sqrt Q .
 \end{aligned}                                                        \tag{5}
\]
Here \(s/r_j\le2^{j-k}\) and \(|a_j(x)|\le\sqrt Q\).
These estimates use only the product of the local mass density with the local slope oscillation.
For example, uniformly bounded parameter density and a continuous derivative with dyadically square-summable modulus of continuity imply (1).
The dyadic sum in (1) also allows the density to decrease where the slope oscillates.

Equations (4) and (5) are the two curvature hypotheses at the distinguished coordinate.
The [original canonical domain argument](Yin_C_F0078_v2.md#the-original-canonical-operators) only uses those bounds at this coordinate.
It bounds both original slices on the entire mixed starred algebra and extends the commutator to bounded vectors.
For the column conclusion apply the same argument to the tuple enlarged by two free Haar unitaries.
The [free enlargement and its column comparison](Yin_C_F0208_v1.md#statement) preserve the actual vacua and the old law, and the canonical slice of the enlarged tuple gives a finite single-coordinate witness there.
The reverse implication for the assertion at all coordinates follows from [the normal strong-to-actual implication](Yin_C_F0070_v1.md#statement).

### The logarithmic weight at the Cantor gaps

Distinct gaps are disjoint and only finitely many have length exceeding any fixed positive number.
Therefore every accumulation point of distinct gap midpoints belongs to \(E\), and \(F\) is closed.
It has Lebesgue measure zero.
The density in (2) is bounded and positive outside \(F\), so its normalizing constant is finite and its support is \([0,1]\).
On the two halves of each gap \(g'\) equals \(1\) and \(-1\), respectively.
Every relative neighborhood of a point of \(E\) contains a Cantor construction interval and hence infinitely many complete gaps.
On each complete gap any representative of the slope has variation at least two, as witnessed by one point of each open half outside the exceptional null set.
This proves the variation assertion and excludes a continuous representative of the derivative on the whole interval.

An interval \(I_j(x)\) disjoint from \(F\) lies in one affine half-gap and contributes zero to (1).
If \(I_j(x)\) meets \(F\), then \(\operatorname{dist}(t,F)\le 2r_j\) throughout the interval.
Consequently \(\mu(I_j(x))/r_j\le C_\beta(1+j)^{-\beta}\), using the bounded density at the first two scales and \(r_j=2^{-j}\) at the others.
Since \(o_j(x)\le2\), (1) holds for \(\beta>1/2\).

For the converse fix \(x=0\) and take \(r=3^{-n}\), \(n\ge1\).
The interval \((r,2r)\) is a complementary gap.
Consider its two subintervals
\[
        \mathcal U_r=[9r/8,5r/4],\qquad
        \mathcal V_r=[11r/8,23r/16].
\]
Both lie inside the rising half, so \(h(t)=(t,t-r)\) in plane coordinates there.
The distance from each subinterval to \(F\) is at least \(r/16\), as the nearest members of \(F\) in this half-gap are its left endpoint and the gap midpoint.
The probability mass of each interval is at least \(c'_\beta r(1+n)^{-\beta}\).
For \(y\in\mathcal U_r,\ t\in\mathcal V_r\) the determinant of \(h(y),h(t)\) is \(r(t-y)\).
Both lengths from \(h(0)=0\) are at most \(3r\), and the remaining chord has length \(\sqrt2(t-y)\).
The reciprocal circumradius is therefore at least \(2/(9\sqrt2\,r)\).
The rectangles for distinct \(n\) are disjoint, so the curvature row at \(0\) is bounded below by a positive multiple of \(\sum_{n\ge1}(1+n)^{-2\beta}\).
For \(\beta\le1/2\) it diverges, and (4) then forces \(Q=\infty\).

### Realization with an omitted correlated coordinate

For every \(\beta\ge0\), \(\rho_\beta\in L^3(dt)\), so the [scalar Lipschitz graph criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) gives actual conjugate variables for the real coordinate \(S(t)=t\) and the complex coordinate \(h(S)\) in their marginal algebras.
Take a variance-one semicircular \(T\) free from \(S\).
Extend their marginal derivations to the free product by the Leibniz rule and zero on the other factor.
The free product vacuum calculation on centered reduced words preserves the original vacua. [Free extension argument](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words)
The selfadjoint pair \((S,U)\), \(U=S+T\), generates the same algebra with the same starred polynomial core.
Its first derivative is \(\delta_S-\delta_T\) and its second is \(\delta_T\).
These have the prescribed generator values and actual vacua by linearity of the displayed real combinations.
The [Lipschitz graph transfer](Yin_C_F0244_v1.md#statement) now gives actual conjugate variables for \((h(S),U)\).
Since \(\operatorname{Re}h(S)=S\) and \(\tau((S-\tau(S))(U-\tau(U)))=\operatorname{Var}(S)>0\), the two coordinate algebras are correlated.
For \(\beta>1/2\), (1) applies to the first coordinate, and the real graph of zero slope applies to the second.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:18 |
| status | open |
| reason | The local slope and mass estimates give a criterion for correlated graph coordinates with a sharp curvature-row threshold on an explicit Cantor graph. A fixed-argument review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Local criterion for the canonical domains and columns, Cantor threshold, and realization with actual correlated coordinates. |
| argument | [Argument](#argument) | Two curvature bounds from one local square sum, disjoint flank rectangles giving divergence, and linear and graph substitutions on an actual free product. |
| dependency | [Curvature-row theorem](Yin_C_F0078_v2.md#the-original-canonical-operators) | Both canonical domains and the commutator from the two geometric bounds at the tested coordinate. |
| dependency | [Column comparison and free extension](Yin_C_F0208_v1.md#statement) | Downward estimate for the old column from an enlarged witness and preservation of free-factor vacuum pairings. |
| dependency | [Lipschitz graph transfer](Yin_C_F0244_v1.md#statement) | Scalar graph vacuum from a cubic density and availability of actual conjugates after graph relabelling of the mixed selfadjoint pair. |
| dependency | [Normal strong-to-actual implication](Yin_C_F0070_v1.md#statement) | Reverse implication for the class satisfying (1) at all coordinates. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:25 |
| status | proved |
| reason | The independent finding verifies the mixed-coordinate curvature hypotheses, canonical domain transfer and the sharp threshold for the Cantor curvature rows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Local criterion for the canonical domains and columns, Cantor threshold, and realization with actual correlated coordinates. |
| argument | [Argument](#argument) | Two curvature bounds from one local square sum, disjoint flank rectangles giving divergence, and linear and graph substitutions on an actual free product. |
| dependency | [Curvature-row theorem](Yin_C_F0078_v2.md#the-original-canonical-operators) | Both canonical domains and the commutator from the two geometric bounds at the tested coordinate. |
| dependency | [Column comparison and free extension](Yin_C_F0208_v1.md#statement) | Downward estimate for the old column from an enlarged witness and preservation of free-factor vacuum pairings. |
| dependency | [Lipschitz graph transfer](Yin_C_F0244_v1.md#statement) | Scalar graph vacuum from a cubic density and availability of actual conjugates after graph relabelling of the mixed selfadjoint pair. |
| dependency | [Normal strong-to-actual implication](Yin_C_F0070_v1.md#statement) | Reverse implication for the class satisfying (1) at all coordinates. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0295_v1.md#finding) | Both local curvature estimates, arbitrary omitted spectra, all four direct inputs and the correlated noise realization. |

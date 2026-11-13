---
author: Yin
---
# The least conjugate-vector norm and two orders of the finite word tests

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) generate a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Use \(H=L^2(M,\tau)\), \(G=(H\otimes_2H)^d\) and inner products linear in the second entry.
Fix an actual ACSY witness for coordinate \(i\) on the represented star algebra, with vacuum \(\xi_0\).
Let \(m_i\) be the infimum of the norms of the actual vacua for this coordinate, allowing all finite starred derivative values.
For formal star polynomials let \(Dp=(d_{y_j}p)_j\) be the evaluated outer cuts at the starred letters and \(\ell p=(\tau\otimes\tau)d_{x_i}p\) the trace of the unstarred cut.
Define closed subspaces
\[
  L=\overline{\{(p(X),Dp):p\text{ a formal star polynomial}\}}\subset H\oplus G,\qquad
  W=\{h:(h,0)\in L\},\qquad
  W_0=\overline{\{p(X):Dp=0\}}\subset H.
\]
The closures are Hilbert closures, including for tuples with represented relations.
Then \(m_i=\|P_W\xi_0\|_2\).
The unique vector of least norm in the closure of the set of actual vacua is \(P_W\xi_0\).
It is an actual vacuum precisely when the scalar identities of [C_F0201](Yin_C_F0201_v1.md#argument) for this vector admit one finite tuple of starred derivative values at all degrees.
If \(D\) descends to a closable operator on the represented core, \(W=\ker\overline D\).

For \(t>0\) let \(a_n(t)\) be the least constant in
\[
  |\ell p|\le a_n(t)(\|p(X)\|_2^2+t^{-2}\|Dp\|_G^2)^{1/2}
      \quad(\deg p\le n).
\]
The two orders of limits satisfy
\[
   \lim_{t\downarrow0}\sup_n a_n(t)=m_i,\qquad
   \sup_n\lim_{t\downarrow0}a_n(t)=\|P_{W_0}\xi_0\|_2.                    \tag{1}
\]
In particular, for a single generator the cutoff-free ratio criterion in [C_F0210](Yin_C_F0210_v1.md#statement) can use the first quantity as denominator, even if its infimum is not attained.

The two quantities in (1) can differ by an arbitrarily large factor even for a single normal generator of norm one with actual ACSY and both canonical full domains.
For \(0<\varepsilon<1/4\), take the scalar coordinate \(Z(z)=z\) with law one half normalized area on \(|z|\le\varepsilon\) plus one half normalized area on \(1/2\le |z|\le1\).
The first quantity is at least \(1/(2\varepsilon)\), and the second is \(1/\|Z\|_2\le\sqrt8\).
Every bounded \(E:M\to H\) satisfying \([E,Z]=P_1\) on bounded inputs has \(\|E\|\ge 1/(4\sqrt2\,\varepsilon)\), with any value at the unit.
Consequently the second quantity can give an unbounded dual-cost ratio on this scalar family even though the actual-vacuum ratio is uniformly bounded.

## Argument

### Vacua as projections of solutions

By the [word rule and represented-quotient argument](Yin_C_F0201_v1.md#argument), all actual witnesses correspond to solutions
\[
     \langle\xi,p(X)\rangle+\langle k,Dp\rangle=\ell p\quad\text{for every }p,
                                                                    \tag{2}
\]
with \(\delta_i(X_j^*)=-k_j^\sharp\), where \(\sharp\) takes the adjoint separately in each tensor leg.
The descent through every represented relation in that result applies to every solution of (2).
Thus for a fixed solution \((\xi_0,k_0)\) the full solution set is \((\xi_0,k_0)+L^\perp\).
If \(U=\operatorname{pr}_H L^\perp\), then \(U^\perp=W\), since \((h,0)\) is orthogonal to \(L^\perp\) exactly for \(h\in W\).
The closure of the actual vacua is therefore \(\xi_0+W^\perp\), giving the norm formula and the attainment assertion.
If \(D\) descends and is closable then \(L\) is its closed graph, giving the kernel assertion.

For fixed \(t>0\), Riesz representation on the closure of the pairs \((p(X),t^{-1}Dp)\) shows that \(\sup_n a_n(t)\) is the least joint norm
\[
        \big(\|\xi\|_2^2+t^2\|k\|_G^2\big)^{1/2}
\]
over solutions of (2), because their representing vectors in these coordinates are \((\xi,tk)\).
It is at least \(m_i\), and for each fixed solution its upper limit as \(t\downarrow0\) is at most that solution's vacuum norm.
Taking the infimum over solutions gives the first limit.
For one generator \(\langle\xi,Z\rangle=1\) for every witness, so \(m_i\ge1/\|Z\|_2>0\).
For each law choose an actual witness with norm less than \(2m_i\).
Unboundedness of the ratio with \(m_i\) then supplies unboundedness with actual witnesses as required in C_F0210.

At a fixed degree write \(V_n^0=\{p(X):\deg p\le n,\ Dp=0\}\).
The same Riesz and small-\(t\) argument gives the infimum of \(\|\eta\|_2\) over solutions at this degree alone.
Every such \(\eta\) agrees with \(\xi_0\) in pairings with \(V_n^0\).
Conversely, for any such \(\eta\) the functional \(Dp\mapsto\ell p-\langle\eta,p(X)\rangle\) is well defined on the finite-dimensional cut range of degree at most \(n\).
It has a representing \(k\in G\), so the least vacuum cost at this degree is \(\|P_{V_n^0}\xi_0\|_2\).
The increasing subspaces \(V_n^0\) have dense union in \(W_0\), proving the other order in (1).

### A radial law with separated limits

Write \(\mu\) for the indicated probability, \(F(r)=\mu\{|z|\le r\}\) and \(M=L^\infty(\mu)\).
The divided difference \(\delta f(z,w)=(f(z)-f(w))/(z-w)\) on represented star polynomials is a coarse-valued outer derivation with \(\delta Z=1\otimes1\), since the diagonal is null and these polynomials are Lipschitz on the disk.
The density of \(\mu\) is bounded for each fixed \(\varepsilon\), so the integral of \(1/|z-w|\) in \(w\) is uniformly finite for \(z\) in the unit disk by the planar polar integral over a disk of radius two.
Fubini and interchange of \(z,w\) give its actual vacuum
\[
      \overline{\xi(z)}=2\int\frac{d\mu(w)}{z-w}=\frac{2F(|z|)}{z}
               \quad(\mu\text{-almost everywhere}).
\]
Indeed the angular mean of \(1/(z-r e^{i\theta})\) is \(1/z\) for \(r<|z|\) and zero for \(r>|z|\), by the two geometric series, and individual circles have zero mass.
The vacuum is bounded for fixed \(\varepsilon\) and is the unique actual vacuum because the [forced starred phase](Yin_C_F0076_v1.md#statement) fixes the derivation on the full core.
In particular \(W=H\) by the solution-space description above.
Inside the small disk \(F(r)=r^2/(2\varepsilon^2)\), giving \(\xi(z)=z/\varepsilon^2\).
Its squared norm on this disk alone is \(\int_0^\varepsilon (r^2/\varepsilon^4)(r/\varepsilon^2)\,dr=1/(4\varepsilon^2)\).

If \(Dp=0\) in the coarse space, its polynomial in \(z,\bar z,w,\bar w\) is identically zero.
Indeed \(\mu^2\) has positive density on a product of open disks, and the change from real and imaginary parts to these four formal complex coordinates is invertible over \(\mathbb C\).
For the commutative image \(q\) of \(p\), telescoping a word gives the polynomial identity
\[
 q(z,u)-q(w,v)=(z-w)d_xp(z,u,w,v)+(u-v)d_yp(z,u,w,v).
\]
Setting \(w=z\) while keeping \(u,v\) independent shows that \(q\) depends only on \(z\).
Conversely every holomorphic polynomial has a lift with zero starred cut.
Thus \(W_0\) is the closed holomorphic polynomial span.
Rotational symmetry gives orthogonal monomials and \(\ell(Z^n)=0\) for \(n\ne1\), with value one for \(n=1\), by the word cut and the vanishing of all positive holomorphic moments.
Hence \(P_{W_0}\xi=Z/\|Z\|_2^2\), and \(\|Z\|_2^2\ge1/8\) by the mass on the outer annulus.

For \(e=1_{\{|Z|\le\varepsilon\}}\), any bounded-vector commutator witness gives
\[
   \tau(e)e=e E(Ze)-Ze E(e),\qquad
   \tau(e)^{3/2}\le2\varepsilon\|E\| .
\]
Here \(\|Ze\|_\infty\le\varepsilon\) and \(\tau(e)=1/2\), proving the lower bound.
The [scalar full-domain theorem](Yin_C_F0055_v1.md#statement) supplies both canonical full domains and a bounded witness with norm at most \((5+2\sqrt{27})\|\xi\|_2\) in each law.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:02 |
| status | open |
| reason | Fixed the vacuum-only word tests and an explicit scalar family on which exchanging the limits gives arbitrarily smaller costs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual vacuum infimum, ordered tests and their quantitative separation on a scalar normal family. |
| argument | [Argument](#argument) | Projected solution space, weighted Riesz tests, planar uniqueness, holomorphic kernel and compressed commutator. |
| dependency | [Word descent](Yin_C_F0201_v1.md#argument) | Equivalence of the scalar identities and actual witnesses through all represented relations. |
| dependency | [Uniform ratio criterion](Yin_C_F0210_v1.md#statement) | Unbounded bounded-dual cost divided by actual vacuum norm gives a general separating pair. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | The actual starred derivative and hence the vacuum are unique for the diffuse normal scalar coordinate. |
| dependency | [Scalar full domains](Yin_C_F0055_v1.md#statement) | Actual normal scalar vacuum controls the canonical bounded-input norm and gives both canonical full domains. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:05 |
| status | proved |
| reason | Adopt the vacuum infimum formulas and the radial separation of the two limit orders after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual vacuum infimum, ordered tests and their quantitative separation on a scalar normal family. |
| argument | [Argument](#argument) | Projected solution space, weighted Riesz tests, planar uniqueness, holomorphic kernel and compressed commutator. |
| dependency | [Word descent](Yin_C_F0201_v1.md#argument) | Equivalence of the scalar identities and actual witnesses through all represented relations. |
| dependency | [Uniform ratio criterion](Yin_C_F0210_v1.md#statement) | Unbounded bounded-dual cost divided by actual vacuum norm gives a general separating pair. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | The actual starred derivative and hence the vacuum are unique for the diffuse normal scalar coordinate. |
| dependency | [Scalar full domains](Yin_C_F0055_v1.md#statement) | Actual normal scalar vacuum controls the canonical bounded-input norm and gives both canonical full domains. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0222_v1.md#whole-proof-finding) | All-degrees descent, weighted and finite-degree limits, scalar vacuum, polynomial kernel and compressed cost. |

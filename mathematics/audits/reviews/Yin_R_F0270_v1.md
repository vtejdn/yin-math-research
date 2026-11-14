---
author: Yin
---

# Independent review of cubic concentration at accretive and nonpositive-phase shifts

For Yin I independently reviewed the complete [candidate dated 2026-11-14T12:29](../../claims/Yin_C_F0261_v1.md#decision-candidate) and its four declared dependency interfaces.
I took no part in developing the proof and received no development discussion, author explanation, exploration notes or prior finding on this candidate.

## Finding

At 2026-11-14T12:31 UTC I found both integral bounds valid for the stated families of shifts of a coordinate with an actual starred vacuum.
The proof permits a separate choice of shift at every radius because each test operator has its entire singular-value tail controlled by the same concentration function that occurs on the left.

### The nonlinear estimate at the endpoint

On the measure \(dr/r\), the \(3/2\)-power of \(F(r)^2r^{-4/3}\) integrates to \(I_\varepsilon\) on \(r\ge\varepsilon\).
After the substitution \(x=ry\), the translated function \(H(F(ry))/(ry)^{1/3}\) has \(L^{3/2}\) norm bounded by \(J_\varepsilon^{2/3}\), since its lower limit is \(\varepsilon y\ge\varepsilon\).
The integral of \(y^{-2/3}\) against \(dy/y\) over \(y\ge1\) gives the factor \(3/2\).
Both truncated quantities are finite by \(F\le1\) and \(H\le\|v\|_2\).

For a nondecreasing \(F\) the set \(\{r\ge\varepsilon:F(r)>t\}\) differs from the interval above \(Q_\varepsilon(t)\) by at most its endpoint.
Its integrals against \(dr/r^3\) and \(dr/r^{3/2}\) are \(1/(2Q_\varepsilon(t)^2)\) and \(2/\sqrt{Q_\varepsilon(t)}\), respectively, with both equal to zero for the empty set.
Applying these formulas to the derivatives \(3t^2\) and \((3/2)\sqrt{H(t)}v(t)\) proves the two layer identities even when \(F\) has jumps or \(H\) vanishes on an interval.
For the second integral, the factors \((t^2/Q_\varepsilon(t)^2)^{1/4}\), \(\sqrt{H(t)/t}\) and \(v(t)\) have \(L^4,L^4,L^2\) norms at most \((2I_\varepsilon/3)^{1/4}\), \(\sqrt{2\|v\|_2}\) and \(\|v\|_2\).
The middle estimate follows by integrating the dilation norm bound \(u^{-1/2}\|v\|_2\) for \(v(ut)\) over \(0<u<1\).
Substitution into \(I_\varepsilon\le(3L/2)^{3/2}J_\varepsilon\) gives \(I_\varepsilon\le(27/2)L^2\|v\|_2^2\) after division in the positive case.
The zero case and the increasing limit as \(\varepsilon\downarrow0\) give the full estimate.

### Vacuum pairing and the two singular-value tails

For a contraction \(x\) of right support trace at most \(m\), tracial Hölder gives \(|\tau(e_y U^*x)|\le\min(\tau(e_y),\|x\|_1)\le\min(\tau(e_y),m)\), where \(\xi=U|\xi|\) and \(e_y=1_{(y,\infty)}(|\xi|)\).
Integrating first over bounded \(y\), then passing to the limit by \(L^1\) truncation, gives \(|\langle\xi,x\rangle|\le H(m)\) for the rearrangement of \(|\xi|\).
For the polar decomposition \(K=S|K|\), each \(S1_{(y,\infty)}(|K|)\) is such a contraction, with the indicated level projection as its right support.
The bounded spectral layer integral for \(K\) and the substitution \(x=1/y\) therefore yield (4), with a finite bound also at the infinite end of the \(x\)-integral.

In the accretive case the omitted coefficients give zero derivative, so the closed inverse rule applied to \(R\) gives \(\langle\xi,VRW^*\rangle=-(\tau R)^2\).
Since \(\operatorname{Re}R=R^*(\operatorname{Re}(D+s))R\), its absolute pairing is at least \(g^2q^4\).
For \(e=1_{[0,r]}(|D|)\), \(R(D+s)e=e\) gives \(\tau(e)\le q(s+r)\sqrt{\tau(e)}\), including the zero projection.
Combining the bounds gives exactly \((s+r)^4/(g^2r^2)=(81/4)(1+\kappa)^2\).
The inverse has norm at most \(1/g\), and the trace law of its modulus equals that of \(|D+s|^{-1}\) by unitary polar decomposition.
Thus a strict inverse tail above \(y\) is bounded by the closed cutoff mass at \(1/y\) for \(b'=b-sVW^*\).
The same \(V,W\) exhibit \(\operatorname{Re}(V^*(Z-b')W)\ge g1\), so this shift is admissible at every tail radius, including when \(\kappa=0\).
Taking the supremum needs no maximizing or measurably selected shift, since \(F_\kappa\) is nondecreasing.

In the phase case, \(P\) and \(|(Z-b)^*|\) have the same trace law and the vanishing kernels give a unitary polar factor.
At \(s=r^2\) the two terms obtained by tracing the differentiated shifted resolvent are \(r^2\tau((P^2+r^2)^{-1})^2\) and the negative of the compressed phase integral against the two factors \(v/(v^2+r^2)\).
Multiplying the identity by \(r^2\) gives the candidate's \(\tau(h_r(P))^2\) on the left and \(r\operatorname{Re}\langle\xi,Ua_r(P)\rangle\) plus the radial phase integral on the right.
The assumed sign and \(h_r\ge1/2\) on \([0,r]\) give \(m_b(r)^2/r^2\le4|\langle\xi,U P(P^2+r^2)^{-1}\rangle|\).
The strict superlevel set of \(v/(v^2+r^2)\) above \(y>0\) is contained in \(0<v<1/y\), and the function is bounded by \(1/(2r)\).
The same shift \(b\) therefore bounds each tail by \(F_{\mathcal G}(1/y)\), including when the choice of \(b\) changes between applications of the test.
The fixed-family envelope is nondecreasing, and the empty family gives zero under the stated convention.
Taking real parts of the conditional phase integral uses its bounded kernel and the same two radial factors, so the integrated sign suffices.

The finite-column result supplies the interpretation of the cubic integral as a necessary test.
Each of the two restricted integrals is finite on the hypotheses checked above, while finiteness of the column cost and integrability over all omitted shifts remain outside this conclusion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0261_v1.md#decision-candidate) | Whole candidate at the stated revision, with both envelopes and all four dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0261_v1.md#statement) | Radius-dependent unitary rotations and shifts, integrated radial sign on a fixed family, uniform constants and the restriction of the column obstruction. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0261_v1.md#argument) | Truncated nonlinear estimate, level sets and rearrangement of the actual vacuum, both operator tails and the two suprema. |
| [Finding](#finding) | [Accretive inverse](../../claims/Yin_C_F0231_v1.md#the-inverse-in-the-closed-graph) | Invertibility, inverse norm, rotated vacuum pairing and singular mass compression at the specified radius. |
| [Finding](#finding) | [Shifted graph calculus](../../claims/Yin_C_F0229_v1.md#argument) | Closed-graph shifted resolvent differentiation, identical left and right singular laws and vanishing kernels for arbitrary omitted shifts. |
| [Finding](#finding) | [Compressed phase](../../claims/Yin_C_F0229_v1.md#the-integrated-phase-defect) | Trace-preserving conditional expectation and exact two-factor radial pairing before integration in radius. |
| [Finding](#finding) | [Uniform concentration test](../../claims/Yin_C_F0258_v1.md#statement) | Necessity of cubic integrability over the full envelope when the original column cost is finite. |

---
author: Yin
---
# Independent review of the least vacuum norm and the two orders of the word tests

## Whole-proof finding

At 2026-11-13T14:07 UTC, a separate agent outside proof development reviewed the entire statement and argument of Yin's C_F0214 v1 candidate dated 2026-11-13T14:02 and the four direct interfaces listed below.
The reviewer received the fixed material and the requested scope and consulted no development discussion, exploratory drafts, author explanations or previous finding on this candidate.
Both limit identities, their quantitative separation and the conclusions for the two dual-cost ratios hold.

With inner products linear in the second variable, the scalar contribution of the starred values \(K_j\) to the vacuum pairing is \(\sum_j\langle K_j^\sharp,d_{y_j}p\rangle\).
Taking \(K_j=-k_j^\sharp\) therefore gives exactly (2).
For any solution of (2), testing on \(urv\) for a represented relation \(r\) pairs its formal derivative with arbitrary evaluated polynomial simple tensors, since the two end terms in Leibniz' rule vanish.
Their density gives descent for that solution.
The vacuum projections of all solutions consequently form the affine space \(\xi_0+\operatorname{pr}_H L^\perp\).
The annihilator of its direction consists of \(h\) with \((h,0)\in (L^\perp)^\perp=L\).
Thus the affine closure has unique least-norm point \(P_W\xi_0\), and this point is realized exactly when it lifts to a solution with a single tuple \(k\) of finite Hilbert norm.
If the cut descends to a closable operator, the horizontal slice of its closed graph is its kernel.

For \(t>0\) the fixed witness bounds the scalar functional on the scaled graph, including at its null pairs.
All representatives have coordinates \((\xi,tk)\) with \((\xi,k)\) solving (2), and projection onto the closed scaled graph gives the least joint norm.
The norm of the functional is the supremum on the increasing degree subspaces.
It is bounded below by \(m_i\) for every \(t\), whereas any fixed solution gives a limiting upper bound \(\|\xi\|_2\).
At a fixed degree \(n\), the map \(Dp\mapsto\ell p-\langle\eta,p(X)\rangle\) factors through the cut range precisely when \(\eta\) agrees with \(\xi_0\) on \(V_n^0\).
The cut range is finite dimensional, so every such \(\eta\) lifts, including \(P_{V_n^0}\xi_0\).
Taking the increasing degree supremum then gives the norm of the projection onto \(\overline{\bigcup_n V_n^0}=W_0\).
For a single generator testing \(p=x\) yields \(m_i\|Z\|_2\ge1\).
Each law admits an actual vacuum of norm less than \(2m_i\), so unboundedness with denominator \(m_i\) passes to actual witnesses in the cutoff-free criterion even when the infimum is unattained.

The scalar measure has no atoms, has positive area density on an open disk and has essential spectral radius one.
The divided difference is a well-defined derivation on the represented core because changes on a null set affect a null set of pairs, and its polynomial kernels are bounded by the Lipschitz bound on the unit disk.
Bounded planar density and local integrability of \(|z-w|^{-1}\) justify splitting the double integral for the vacuum identity.
The two resulting integrals agree after swapping variables, and the angular integral gives \(\overline{\xi(z)}=2F(|z|)/z\) away from the origin.
On the inner disk the radial marginal is \(r\,dr/\varepsilon^2\) and \(\xi(z)=z/\varepsilon^2\), contributing \(1/(4\varepsilon^2)\) to its squared norm.
The vacuum is bounded on the rest of the support.
The normal phase fixes the one remaining generator value, so the derivation on all words and its actual vacuum are unique.
This identifies \(W=H\) and gives the asserted first lower bound.

Vanishing of the polynomial starred cut in \(L^2(\mu^2)\) implies vanishing on an open product in four real variables, hence a polynomial identity in the four independent complex variables \(z,u,w,v\) by an invertible linear change.
Setting \(w=z\) in the word telescoping identity then makes \(q(z,u)=q(z,v)\) with \(u,v\) free.
Conversely the holomorphic lift has zero starred cut, giving exactly the claimed closed span for \(W_0\).
Rotational invariance makes the holomorphic monomials orthogonal, and only the degree-one monomial has nonzero pairing with \(\xi\), of value one.
Thus the second limit is \(1/\|Z\|_2\).
Direct radial integration gives \(\|Z\|_2^2=5/16+\varepsilon^2/4\), which implies the stated lower bound \(1/8\).

Testing the commutator on the inner-disk projection \(e\) and multiplying on the left by \(e\) gives the vector \(\tau(e)e\).
The two terms have norms at most \(\varepsilon\|E\|\) each, since \(\|Ze\|_\infty\le\varepsilon\) and \(\|e\|_\infty=1\).
As \(\tau(e)=1/2\), every admissible map has norm at least \(1/(4\sqrt{2}\,\varepsilon)\), independently of \(E(1)\).
The verified scalar vacuum identity meets the premise for the original two-domain result for the canonical slice.
The polynomial commutator extends to the closed slice by graph approximation because multiplication by \(Z\) and the vacuum projection are bounded on \(H\).
Its restriction to bounded functions gives the upper bound \((5+2\sqrt{27})m_i\).
Hence the reversed-limit denominator yields an unbounded ratio on this family, while the true denominator gives a uniformly bounded ratio.

The existing findings for [word descent](Yin_R_F0209_v1.md#whole-proof-finding), [the cutoff-free criterion](Yin_R_F0218_v1.md#whole-proof-finding), [the normal phase](Yin_R_F0049_v1.md#conclusion) and [the scalar domain theorem](Yin_R_F0037_v1.md#scalar-findings) were used at the interfaces below.
The example separates the two tests and leaves the existence of an unbounded true dual-cost ratio open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0214_v1.md#statement) | Vacuum infimum and its attainment, kernel under closability, the two limit identities, ratio criterion and the normal scalar family with both canonical domains. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0214_v1.md#argument) | Descent, projected affine solutions, weighted and fixed-degree representatives, radial vacuum and uniqueness, polynomial identity and projection, and lower and upper dual bounds. |
| [Whole-proof finding](#whole-proof-finding) | [Word descent](../../claims/Yin_C_F0201_v1.md#argument) | Every solution of the all-degrees scalar identities gives a represented derivation with its stated starred values and actual vacuum, also in the presence of relations. |
| [Whole-proof finding](#whole-proof-finding) | [Cutoff-free criterion](../../claims/Yin_C_F0210_v1.md#statement) | An unbounded ratio using actual vacuum norms suffices, with each starred value finite and no common bound required. |
| [Whole-proof finding](#whole-proof-finding) | [Forced normal phase](../../claims/Yin_C_F0076_v1.md#statement) | The sole starred value is fixed in the scalar normal case, giving uniqueness of the derivation and its vacuum. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar full domains](../../claims/Yin_C_F0055_v1.md#statement) | Both original bounded-function domains and the canonical slice bound for the compact diffuse law with its actual vacuum. |

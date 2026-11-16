---
author: Yin
---

# Left and right singular states on regular inverse branches of a Borel shift

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z,Y\) be two distinct coordinates of a bounded normal generating tuple with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Let \(\mu\) be the trace law of \(Y\) on \(K=\sigma(Y)\), let \(f\) be a bounded complex Borel function on \(K\), and put \(T=Z-f(Y)=U|T|\).
The polar factor \(U\) is unitary by the [shifted singular-law theorem](Yin_C_F0229_v1.md#statement).
Use the compact support \(\Gamma\) of the image of \(\mu\) under \(y\mapsto(y,f(y))\) and its essential fibers \(K_z=\{y:(y,z)\in\Gamma\}\).
A point \(v\in K\) will be tested when \(f\) has a Lipschitz representative on a relative neighborhood of \(v\) and the two limits
\[
 d=\lim_{y,w\to v}\frac{f(y)-f(w)}{y-w}\ne0,\qquad
 d'=\lim_{y,w\to v}\frac{\overline{f(y)}-\overline{f(w)}}{y-w}
 \tag{1}
\]
exist for distinct \(y,w\in K\) using that representative.
The continuous representative on such a neighborhood is unique since \(\mu\) has support \(K\).

Put \(F(s)=\tau(1_{[0,s]}(|T|))\).
If \(\int_0^\infty F(s)^3\,ds/s^3=\infty\), there are \(s_n\downarrow0\), \(z_0\in\sigma(Z)\), and probabilities \(R,L\) on \(K_{z_0}\) with the following properties.
The [local secant spread](Yin_C_F0273_v1.md#statement) at \(z_0\) in \(\sigma(Z)\) is at least \(2(\sqrt{1+24^{-2}}-1)\).
For \(h_n=s_n^2/(|T|^2+s_n^2)\), \(h_n'=Uh_nU^*\), and \(H_n=\tau(h_n)\), the \(Y\)-marginals of \(h_n/H_n,h_n'/H_n\) converge weakly to \(R,L\), respectively.
For every \(v\in K_{z_0}\) satisfying (1),
\[
                         L(\{v\})R(\{v\})=0.                       \tag{2}
\]
If every point of this fiber satisfies (1), the fiber is finite, the supports of \(R,L\) are disjoint and nonempty, and the hard projections \(e_n=1_{[0,s_n]}(|T|)\), \(e'_n=Ue_nU^*\) satisfy
\[
                       \frac{\tau(e'_n e_n)}{\tau(e_n)}\longrightarrow0.
                                                                    \tag{3}
\]
In particular the integral is finite if for every \(z\in\sigma(Z)\) of at least the indicated spread the essential fiber is either empty or a singleton satisfying (1).
This condition allows \(f\) to be discontinuous away from the tested fibers.
At a simple root of a holomorphic polynomial shift, (1) holds when the marginal \(Y\) has just one limiting unoriented chord direction there.
Finiteness at this fixed shift does not control every omitted shift.

## Argument

### Local trace identities for a bounded Borel shift

Fix \(s>0\), put \(P=|T|\), \(h=s^2/(P^2+s^2)\), \(h'=UhU^*\), \(V=UsP/(P^2+s^2)\), and \(H=\tau(h)\).
For a bounded Borel test \(c\) on \(K\) write \(R_s(c)=\tau(c(Y)h)/H\), \(L_s(c)=\tau(c(Y)h')/H\), and \(G_s(c)=\tau(c(Y)V)/H\).
Let \(g\) be a real smooth bump on the plane with support compactly inside an open set on which \(f|_K\) has a Lipschitz representative.
Write \(D(y,w)=(f(y)-f(w))/(y-w)\) and \(D'(y,w)=(\overline{f(y)}-\overline{f(w)})/(y-w)\) on this patch.
All leg measures at fixed \(s\) are absolutely continuous with respect to \(\mu\), whose diffuseness makes the diagonal null for their products.
Writing \(g\otimes g\) for \(g(y)g(w)\), the quantities
\[
 \begin{aligned}
 &\int(g\otimes g)D\,d(L_s\otimes R_s)
       -\int(g\otimes g)D'\,d(G_s\otimes G_s),\\
 &\int(g\otimes g)D'\,d(R_s\otimes G_s)
       +\int(g\otimes g)D\,d(\overline{G_s}\otimes R_s)
 \end{aligned}                                                       \tag{4}
\]
equal \(-s\langle\eta_g,V\rangle/H^2\) and \(s\langle\eta_g,h\rangle/H^2\), respectively, with \(\eta_g=\delta_Y^*(g(Y)\otimes g(Y))\).
Here \(\overline{G_s}(c)=\overline{G_s(\bar c)}\).
Indeed the [normal starred symbols and adjoint formula](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) give graph approximations for \(g(Y)\) whose coarse derivatives converge in both orientations.
In detail, the [Lipschitz approximation on a marginal](Yin_C_F0257_v1.md#comparing-the-two-represented-cores-in-both-directions) gives uniformly converging starred polynomial approximants with bounded Lipschitz constants, whose divided differences converge in \(L^2(\mu^2)\) by dominated convergence.
Applying the tensor adjoint formula to the two polynomial legs gives convergence of their vacuum product and sliced derivative terms, hence membership of \(g(Y)\otimes g(Y)\) in the closed adjoint domain.

First take \(f\) globally Lipschitz on \(K\).
The same approximations give coarse graph values \(D,D'\) for \(f(Y),\overline f(Y)\) in the original \(\delta_Y\) graph.
All differentiated symbols are uniformly bounded in the marginal tensor algebra during approximation for this fixed Lipschitz function.
The [mixed resolvent calculation](Yin_C_F0287_v1.md#the-two-derivations-and-the-polar-resolvents) applies to \(T\), with \(\Phi(\delta_YT)=-D,\ \Phi(\delta_YT^*)=-D'\) in the opposite tensor representation.
Explicitly,
\[
 s\Phi(\delta_Y V)=-(h'\otimes h^{\mathrm{op}})D
                    +(V\otimes V^{\mathrm{op}})D',\qquad
 s\Phi(\delta_Y h)=(h\otimes V^{\mathrm{op}})D'
                    +(V^*\otimes h^{\mathrm{op}})D .
\]
These identities pass from polynomial approximants at fixed \(s\) by the inverse product rule or norm-convergent geometric inversion with differentiated tails, since the residual and its adjoint are uniformly bounded and their derivatives converge in the coarse Hilbert space.
Test each equality against the real tensor \(g(Y)\otimes g(Y)\).
Under the product trace the two tests commute with \(D,D'\) after cycling the trace, so the inserted scalar symbols have factors \(g(y)g(w)\).
Tracing the two outer legs gives (4).

For a merely Borel \(f\), select a smaller closed neighborhood of \(K\cap\operatorname{supp}g\) inside the Lipschitz patch and extend its Lipschitz representative boundedly to \(K\).
For example, for each real component one may use the infimum over the closed neighborhood of the value plus the Lipschitz constant times distance, and clip the extension to its original range.
Take bounded globally Lipschitz approximants converging to \(f\) in \(L^2(\mu)\) with a common supremum bound; continuous functions are dense for the finite Borel measure on the compact metric spectrum, and Lipschitz approximation and clipping give this choice.
Using a fixed Lipschitz bump equal to one on \(K\cap\operatorname{supp}g\) and supported inside the smaller neighborhood, glue the extension there to these approximants.
The resulting \(f_m\) are uniformly bounded, globally Lipschitz individually and converge in \(L^2(\mu)\) to \(f\).
In (4) their divided differences multiplied by \(g\otimes g\) are the same fixed bounded symbols for all \(m\).
For fixed \(s\) the resolvent tests \(h_m,h_m',V_m\) converge boundedly strongly-star to \(h,h',V\) since \(f_m(Y)\to f(Y)\) boundedly strongly-star and the regularized inverses have a common norm bound.
The two product traces with the fixed bounded symbols thus converge, as do the pairings with \(\eta_g\).
This proves (4) without putting \(f(Y)\) in the global derivation graph.

### Localization on the essential fiber

Apply the [two-resolvent scale selection at \(Z\)](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) and its [dyadic refinement](Yin_C_F0273_v1.md#concentration-of-the-complex-measures-in-total-variation-away-from-the-point) at the singleton shift \(f(Y)\).
Include in the countable test list the vectors \(\eta_g\) for a countable collection of smooth bump functions \(0\le g\le1\) on rational balls with rational inner radii, equal to one on the inner ball.
This collection admits shrinking supports about every point with the point in every inner ball.
The vectors depend only on \(g,Y,\delta_Y\), so they can be included before choosing the limiting point.
Also require \(F(s_n)>s_n^{3/4}\), which is possible because the integral on the discarded radii below one is at most \(\int_0^1 s^{9/4}ds/s^3<\infty\).
The scale choices give \(F/2\le H\le6F\), \(\|G_s\|_{\mathrm{TV}}\le24\), and the two errors in (4) tend to zero for each listed test.
The [two-resolvent point-mass argument](Yin_C_F0269_v1.md#the-common-limiting-point) and the [local cone estimate at \(Z\)](Yin_C_F0273_v1.md#the-two-scalar-trace-inequalities-in-a-local-cone) apply on this selection with the additional countably many tests.
Thus the \(Z\)-marginals for both positive weights converge to \(\delta_{z_0}\) with the required secant spread.

For the two normalized positive states, testing \(T^*T\) against \(h/H\) and \(TT^*\) against \(h'/H\) gives \(s^2(1-H)/H\to0\) by the extra lower bound on \(F\).
The state Hilbert seminorm triangle inequality, applied on the right to \(Z-f(Y)\) and on the left to its adjoint, and normality of \(Z,f(Y)\) show that both states take \(|f(Y)-z_0|^2\) to zero in the limit.
Restricting these states to \(C^*(Y,f(Y))=C(\Gamma)\), subsequence limits are supported on \(\Gamma\cap\{(y,z_0):y\in K\}\).
Their \(Y\)-marginals \(R,L\) thus have the asserted support, also for discontinuous \(f\).
Pass to the same subsequence for weak convergence \(G_s\to G\) on \(K\), using the uniform variation bound and compact metrizability.

### The diagonal equations at a regular point

Fix \(v\in K_{z_0}\) satisfying (1) and choose listed bumps \(g_j\) equal to one near \(v\) with supports tending to \(v\) inside the Lipschitz patch.
On each supporting square the supremum off the diagonal of \(|D-d|+|D'-d'|\) tends to zero as \(j\to\infty\).
Replacing the two symbols in (4) by their limits therefore has an error tending to zero uniformly over the chosen scales, since the factors are probabilities or have variation at most 24.
For fixed \(j\) first pass to the scale limit on the constant-symbol terms, then take \(j\to\infty\).
The integrals of \(g_j\) converge to the masses of \(\{v\}\) by dominated convergence for each of the fixed limiting measures.
Write \(L_v,R_v,G_v\) for these masses.
The two equations are
\[
 d L_v R_v=d'G_v^2,\qquad d'R_v G_v+d\,\overline{G_v}R_v=0 .
\]
If \(R_v>0\), multiply the second equality divided by \(R_v\) by \(G_v\) to get \(d L_vR_v=-d|G_v|^2\).
Since \(d\ne0\), both nonnegative quantities vanish.
This proves (2) for all such \(v\) on one sequence.

Every point satisfying (1) is isolated in \(K_{z_0}\): on a sufficiently small relative neighborhood the divided differences of \(f\) have modulus at least \(|d|/2\), so the representative is injective, and on the patch the essential graph is its graph by continuity and full support.
If all points of the compact fiber satisfy (1), it is consequently finite.
By (2) the two nonempty probability supports there are disjoint.
Choose a Borel neighborhood of the support of \(R\) whose closure misses the support of \(L\) and whose boundary misses both supports, and denote its \(Y\)-spectral projection by \(p\).
The soft marginals give \(R_s(1-p),L_s(p)\to0\), writing these functionals on the associated indicators.
Since \(e_n\le2h_n,\ e'_n\le2h'_n\) and \(H_n/\tau(e_n)\le6\), it follows that \(\|(1-p)e_n\|_2,\|e'_n p\|_2=o(\sqrt{\tau(e_n)})\).
Their sum bounds \(\|e'_ne_n\|_2\), whose square is \(\tau(e'_ne_n)\).
This proves (3), and a singleton fiber of the specified kind cannot carry two disjoint probabilities.
For a polynomial \(f\), its first divided difference approaches \(f'(v)\) at \(v\); the second equals the conjugate first divided difference times the chord phase of \(Y\), proving the stated simple-root application.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:30 |
| status | open |
| reason | Fix the local resolvent identities for Borel shifts and the necessary separation of their two singular states on regular inverse branches for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Concentration on the essential Borel fiber, disjoint atoms at regular points, vanishing overlap on a regular fiber and the singleton exclusion. |
| argument | [Argument](#argument) | Patchwise resolvent traces, uniform symbol tests, shared scale selection, diagonal equations and hard spectral projections. |
| dependency | [Shifted singular laws](Yin_C_F0229_v1.md#statement) | Zero singular kernels and unitary polar factors for all bounded omitted shifts. |
| dependency | [Starred symbols and the tensor adjoint](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuse marginal, divided differences, closability and vacuum pairing for bounded polynomial legs. |
| dependency | [Marginal graph approximation](Yin_C_F0257_v1.md#comparing-the-two-represented-cores-in-both-directions) | Uniform polynomial approximants to Lipschitz functions with bounded Lipschitz constants and graph convergence. |
| dependency | [Mixed residual differentiation](Yin_C_F0287_v1.md#the-two-derivations-and-the-polar-resolvents) | Opposite tensor convention, differentiated inverse with bounded derivatives and the two polar resolvent blocks. |
| dependency | [Spectral concentration](Yin_C_F0269_v1.md#argument) | Countable adjoint-test scale selection, soft mass and variation bounds and common marginal limit at the first coordinate. |
| dependency | [Local secant theorem](Yin_C_F0273_v1.md#argument) | Simultaneous dyadic cut estimates and the numerical spread restriction at the first coordinate. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:36 |
| status | proved |
| reason | Independent review verified the localized adjoint tests for Borel shifts and the separation of the two singular states on regular inverse branches. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Concentration on the essential Borel fiber, disjoint atoms at regular points, vanishing overlap on a regular fiber and the singleton exclusion. |
| argument | [Argument](#argument) | Patchwise resolvent traces, uniform symbol tests, shared scale selection, diagonal equations and hard spectral projections. |
| dependency | [Shifted singular laws](Yin_C_F0229_v1.md#statement) | Zero singular kernels and unitary polar factors for all bounded omitted shifts. |
| dependency | [Starred symbols and the tensor adjoint](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuse marginal, divided differences, closability and vacuum pairing for bounded polynomial legs. |
| dependency | [Marginal graph approximation](Yin_C_F0257_v1.md#comparing-the-two-represented-cores-in-both-directions) | Uniform polynomial approximants to Lipschitz functions with bounded Lipschitz constants and graph convergence. |
| dependency | [Mixed residual differentiation](Yin_C_F0287_v1.md#the-two-derivations-and-the-polar-resolvents) | Opposite tensor convention, differentiated inverse with bounded derivatives and the two polar resolvent blocks. |
| dependency | [Spectral concentration](Yin_C_F0269_v1.md#argument) | Countable adjoint-test scale selection, soft mass and variation bounds and common marginal limit at the first coordinate. |
| dependency | [Local secant theorem](Yin_C_F0273_v1.md#argument) | Simultaneous dyadic cut estimates and the numerical spread restriction at the first coordinate. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0306_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

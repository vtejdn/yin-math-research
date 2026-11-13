---
author: Yin
---
# Left-right quadratic adjoint estimates and a fixed-functional criterion

Task: [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
This continuing argument was developed on 2026-10-16 by the quadratic-abstract subagent for Yin, under root's existing execution coordination.
It is a developer-checked reduction and sufficient-condition analysis, with no independent review or general normal estimate claimed.
The main normal working material is [D_F0002](Yin_D_F0002.md).

## Exact question and reusable inputs

Let \(P\subset M\) be a weakly dense unital star algebra in a finite tracial von Neumann algebra, let \(H=L^2(M,\tau)\), and let
\[
 \delta:P\longrightarrow H\otimes_2H
\]
be an outer derivation with actual vacuum \(\xi=\delta^*(1\otimes1)\).
Inner products are linear in the second variable.
The actual tensor-adjoint formula in [Mai15-U001](../audits/literature/Mai15/Yin_U001.md#mai15-u001) places \(P\odot P\) in the adjoint domain.
Set
\[
 E_0=(\mathrm{id}\otimes\tau)\delta,\quad
 F_0=(\tau\otimes\mathrm{id})\delta,\quad
 T_\ell(a)=\delta^*(a\otimes1),\quad
 T_r(a)=\delta^*(1\otimes a).
\]
The proposed inequalities are
\[
 \|T_\ell(a)\|_2^2\le C_\ell\|T_\ell(a^*a)\|_2,\qquad
 \|T_r(a)\|_2^2\le C_r\|T_r(aa^*)\|_2.
 \tag{Q}
\]
D_F0002 already establishes automatic power growth and the implication from both estimates to both canonical bounded-vector domains.
Those arguments are not reproved here.
The actual adjoint-conjugation input is [C_F0073 Part A](../claims/Yin_C_F0073_v1.md#argument); the calculation below makes its effect on (Q) explicit.

## The maps are actual slice adjoints

For \(a,p\in P\), adjoint duality gives
\[
 \langle T_\ell(a),p\rangle
 =\langle a\otimes1,\delta(p)\rangle
 =\langle a,E_0p\rangle,
 \qquad
 \langle T_r(a),p\rangle
 =\langle a,F_0p\rangle.
\]
Consequently
\[
 P\subset\operatorname{Dom}E_0^*\cap\operatorname{Dom}F_0^*,
 \qquad T_\ell=E_0^*|_P,\quad T_r=F_0^*|_P.
 \tag{1}
\]
If \(E_0\) extends boundedly on all H, then \(T_\ell\) is bounded in the Hilbert norm with the same operator norm.
The analogous statement for \(T_r\) uses \(F_0\).
No boundedness of \(\xi\) as an element of M is needed for these statements.
Boundedness of just \(E_0\) does not by (1) establish boundedness of \(T_r\).

Suppose in addition that \(Y\in P\) satisfies \(\delta Y=1\otimes1\), and set
\[
 \sigma=\|Y-\tau(Y)1\|_2>0.
\]
For positive \(b\in P\), \(\delta1=0\) and adjoint duality give
\[
 \langle T_\ell(b),Y-\tau(Y)1\rangle
 =\langle T_r(b),Y-\tau(Y)1\rangle=\tau(b).
\]
Thus
\[
 \|T_\ell(b)\|_2,\ \|T_r(b)\|_2\ge\frac{\tau(b)}{\sigma}.
 \tag{2}
\]
In particular the denominators in (Q) are nonzero whenever \(a\ne0\).

If \(E_0\) is Hilbert-space bounded, (1)--(2) imply
\[
 \|T_\ell(a)\|_2^2
 \le\|E_0\|_{2\to2}^2\|a\|_2^2
 \le \sigma\|E_0\|_{2\to2}^2\|T_\ell(a^*a)\|_2.
 \tag{3}
\]
If \(F_0\) is Hilbert-space bounded, the right estimate follows with constant \(\sigma\|F_0\|_{2\to2}^2\), using \(\tau(aa^*)=\|a\|_2^2\).
These are sufficient hypotheses; neither the actual vacuum condition nor full bounded-vector domains supplies Hilbert-space boundedness.
The scalar uniform-interval example in D_F0002 already distinguishes those domain targets.

There is also a restricted estimate with no Hilbert boundedness assumption.
For every \(a\in P\) with \(\delta(a)=\delta(a^*)=0\), the actual adjoint formulas give \(T_\ell(a)=a\xi\) and \(T_r(a)=\xi a\).
Cauchy-Schwarz then gives both inequalities in (Q) with constant \(\|\xi\|_2\), because
\[
 \|a\xi\|_2^2=\langle\xi,a^*a\xi\rangle,\qquad
 \|\xi a\|_2^2=\langle\xi,\xi aa^*\rangle.
\]
For normal coordinate derivations this includes the starred polynomial algebra of the other coordinates.
It does not control mixed words.

## Adjoint conjugation exchanges the two correctly ordered estimates

Let \(J:H\to H\) be \(Ja=a^*\), let \(J_2(u\otimes v)=v^*\otimes u^*\), and define
\[
 \epsilon=J_2\delta J,\qquad
 \epsilon(a)=(\delta(a^*))^\dagger.
\]
These antiunitary maps give the actual adjoint-domain identity
\[
 \epsilon^*=J\delta^*J_2,\qquad
 \operatorname{Dom}\epsilon^*=J_2\operatorname{Dom}\delta^*.
 \tag{4}
\]
In particular \(\epsilon^*(1\otimes1)=\xi^*\), so both sides of the following formulas are actually defined on P:
\[
 T_\ell^\epsilon(a)=T_r^\delta(a^*)^*,\qquad
 T_r^\epsilon(a)=T_\ell^\delta(a^*)^*.
 \tag{5}
\]
For example, the left inequality for epsilon, evaluated at \(a^*\), reads exactly
\[
 \|T_r^\delta(a)\|_2^2
 \le C_\ell^\epsilon\|T_r^\delta(aa^*)\|_2.
\]
The reverse implication follows by applying the same calculation again, since \(\epsilon^\#=\delta\).
Consequently the least possible constants, allowing infinity, obey
\[
 C_\ell(\epsilon)=C_r(\delta),\qquad
 C_r(\epsilon)=C_\ell(\delta).
 \tag{6}
\]
This does not identify \(C_\ell(\delta)\) with \(C_r(\delta)\).

Now impose the Task's normal-coordinate assumptions and let \(P=\mathbb C\langle X,X^*\rangle\).
For the adjoint tuple \(X^*=(X_1^*,\ldots,X_d^*)\), the same P is the represented starred algebra and
\[
 \epsilon_i(X_j^*)=\delta_{ij}1\otimes1,\qquad
 \epsilon_i^*(1\otimes1)=\xi_i^*.
\]
Thus the class of all normal ACSY systems is stable under this transformation.
A theorem establishing the left inequality for every normal ACSY system would also establish the required right inequality for every such system, by applying it to the adjoint tuple.
This is a reduction of the universal proof target.
A left estimate for one fixed delta alone does not imply the right estimate for that same delta unless its conjugate system is separately covered.

## What a fixed positive-functional proof would require

For a complex-linear \(T:P\to H\), consider the following stronger finite-family condition with one nonnegative constant C:
\[
 \sum_{j=1}^n\|T(a_j)\|_2^2
 \le C\left\|T\left(\sum_{j=1}^n a_j^*a_j\right)\right\|_2
 \quad(n\ge1,\ a_j\in P).
 \tag{7}
\]
It is equivalent to the existence of one \(g\in H\), with \(\|g\|_2\le C\), such that
\[
 \|T(a)\|_2^2\le\operatorname{Re}\langle g,T(a^*a)\rangle
 \quad(a\in P).
 \tag{8}
\]
The implication (8) to (7) is summation and Cauchy-Schwarz.

For the converse, regard H as a real Hilbert space.
For a fixed finite list \(a_1,\ldots,a_n\), set \(h_j=T(a_j^*a_j)\), \(q_j=\|T(a_j)\|_2^2\).
The image K of the closed radius-C ball under \(g\mapsto(\operatorname{Re}\langle g,h_j\rangle)_j\) is compact and convex, because the map depends only on the finite-dimensional real span of the \(h_j\).
If K does not meet \(Q=\prod_j[q_j,\infty)\), choose a closest pair \(k\in K,o\in Q\).
Such a pair exists because K is compact and the Euclidean nearest point in Q is obtained by replacing each coordinate below \(q_j\) by \(q_j\).
Set \(\lambda=o-k\ne0\).
The nearest-point description gives \(\lambda_j\ge0\) and \(\lambda_j o_j=\lambda_j q_j\).
Minimality along every line segment in K gives \(\lambda\cdot(k'-k)\le0\) for \(k'\in K\).
Consequently \(\lambda\cdot q=\lambda\cdot o=\lambda\cdot k+\|\lambda\|^2>\sup_{k'\in K}\lambda\cdot k'\), or equivalently
\[
 \sum_j\lambda_j q_j
 >C\left\|\sum_j\lambda_j h_j\right\|_2.
\]
This contradicts (7) applied to \(\sqrt{\lambda_j}a_j\).
Therefore each finite collection of the closed half-space constraints in (8) meets the radius-C ball.

Here is a direct Hilbert-space passage to all constraints.
For each finite collection F, let \(g_F\) be the vector of least norm satisfying those constraints.
It exists by projecting to the finite-dimensional real span of their vectors \(h_j\), where a bounded minimizing sequence has a convergent subsequence.
Its norm is at most C.
For \(G\supset F\), minimality along the segment from \(g_F\) to \(g_G\) gives
\[
 \|g_G-g_F\|_2^2\le\|g_G\|_2^2-\|g_F\|_2^2.
\]
Let \(s=\sup_F\|g_F\|_2^2\le C^2\), and choose an increasing sequence of finite collections \(F_n\) whose minimum squared norms converge to s.
The displayed inequality makes \(g_{F_n}\) a Cauchy sequence, with a norm-at-most-C limit g.
For any one additional constraint k, apply the same inequality to \(G_n=F_n\cup\{k\}\).
It gives \(\|g_{G_n}-g_{F_n}\|_2^2\le s-\|g_{F_n}\|_2^2\to0\).
Thus the same limit g satisfies k, because its half-space is norm closed.
This proves (8) without invoking an uninspected infinite-dimensional separation or compactness theorem.
No normal phase positivity is assumed.

This is a self-contained domination calculation for the present route, not a claim of novelty.
Its standard finite-convex minimax interface is [Simons, Theorem 2.4, printed p.634](../audits/literature/Sim03/readme.md#yin), checked in the author-hosted published text.
That theorem states that for real convex functions f_1,...,f_n on a nonempty convex set A, some nonnegative weights summing to one satisfy inf_A max_j f_j=inf_A sum_j lambda_j f_j.
For the present use, A is the radius-C ball in the real Hilbert space and f_j(g)=q_j-Re<g,h_j>.
Condition (7), applied to sqrt(lambda_j)a_j, makes the infimum of every such weighted sum nonpositive; weak compactness of the ball and the finite-intersection property give one g for all constraints, using the [checked Hilbert-ball and FIP interfaces](../audits/literature/Keh25/Yin_U001.md#exact-accepted-interfaces).
This identifies the abstract domination mechanism and its exact hypotheses, rather than attributing the specific algebraic formulas (7)--(8) verbatim to Simons.
The direct finite-dimensional and least-norm argument above remains the self-contained proof used here; no new Claim or independently reviewed finding is created by this source comparison.
The existing Mai15 and C_F0073 source interfaces are used only at the specific adjoint and power-growth steps identified above; they are not cited as sources of (7)--(8).

The associated hermitian linear functional is
\[
 \phi_g(b)=\frac12\left(
   \langle g,T(b)\rangle+
   \overline{\langle g,T(b^*)\rangle}\right).
\]
It is nonnegative on every algebraic sum of squares and satisfies \(\|T(a)\|_2^2\le\phi_g(a^*a)\).
For an actual adjoint map T, (8) implies the original single-square inequality, and D_F0002's automatic growth then makes T bounded from the operator norm to H.
It follows that \(\phi_g\) is bounded on P and extends to a positive functional on its C*-completion.
No claim of normality is needed here.

The same argument for the right side uses \(\sum_j a_ja_j^*\) throughout.
The original single-square inequality has not been shown here to imply the finite-family strengthening (7).
In particular, a search for one fixed g, including the candidate \(g=\xi\), introduces an additional simultaneous domination obligation.
C_F0076 supplies actual tensor-leg domains and pure coassociativity, but no proof of (7) or (8).
C_F0057's mixed-defect negativity does not by itself refute either the single-square estimates or this fixed-functional mechanism.

## Present consequence and remaining question

The universal normal problem can be concentrated on the left inequality, provided the final theorem covers the entire adjoint-stable normal ACSY class.
Hilbert-space bounded slices give a direct positive subclass through (3); the other-coordinate algebra gives a different restricted subclass.
A fixed-functional proof would follow from the precisely stated finite-family inequality.
None of these reductions proves the left estimate for a general correlated normal system, gives a separating normal law, or changes the unresolved Task classification.

<a id="selfadjoint-tests-and-the-correlated-unitary-obstruction"></a>
## Selfadjoint tests and a correlated-unitary obstruction

On 2026-10-16 Yin resumed the arbitrary correlated normal endpoint question after the DGS21 source application.
The following calculations are development and self-checking by the original authoring main agent, with no independent review or change to a fixed Claim assessment.
[DGS21-U001](../audits/literature/DGS21/Yin_U001.md#dgs21-u001) identifies the two endpoint inequalities with the two actual canonical bounded-vector domains.

For either actual one-sided adjoint T, it is sufficient to establish
\[
 \|T(a)\|_2^2\le C\|T(a^2)\|_2\qquad(a=a^*\in P)
 \tag{R1}
\]
with a fixed finite C.
The already established power-growth bound applies to every positive power of a selfadjoint a.
Iterating (R1) on a,a squared,a to the fourth power gives \(\|T(a)\|_2\le C\|a\|\).
For arbitrary a, its real and imaginary parts have operator norm at most norm(a), and therefore \(\|T(a)\|_2\le2C\|a\|\).
Thus a proof need not begin with the stronger complex-input square-order estimates.
Both one-sided maps must still be covered, or one must prove a universal left theorem and apply adjoint-tuple conjugation.

In fact (R1) is needed only for positive b in P.
Power iteration first gives norm(Tb) in L2 at most C norm(b) for every such b.
For selfadjoint a with m=norm(a), the two elements \((m1+a)/2\) and \((m1-a)/2\) are positive elements of P of norm at most m.
Their difference is a, so the bound becomes \(\|Ta\|_2\le2C\|a\|\) on selfadjoint tests and \(\|Ta\|_2\le4C\|a\|\) on arbitrary tests.
Therefore a universal left positive-input quadratic theorem, applied also to the adjoint tuple, would prove both endpoint estimates without assuming a fixed-vector domination or a sharp constant.

The [fixed sharp-vacuum and degree-growth account](../ledger/Yin_L_F0055_v1.md#sharp-fixed-vacuum-and-degree-growth-failures) retains the complete R2--R6 calculations, including the strictly positive countertest and the bounded geometric-sum limit for a fixed actual law.
The score and actual normalized vacuum used there are fixed in the same account.
Those failures concern the sharp vector-xi constant-one inequality; they do not refute (R1) with an unspecified finite constant or either endpoint estimate.

The next bounded-model diagnostic is the normal coordinate change \(X=U+\lambda U^2\), \(Y=U^*V\), with real \(|\lambda|<1/2\).
Its inverse divided-difference multiplier is
\[
 g=(1+\lambda(U\otimes1+1\otimes U))^{-1}.
\]
The Neumann series is absolutely convergent in the projective tensor norm.
It gives an exact bounded dual by inserting the series into the already bounded U-coordinate dual, so this model cannot separate A from S.
Its use is to test whether the fixed-vacuum factor-two inequality survives correlated normal coordinates beyond circles.
Every finite series computation must retain its truncation status; numerical failure needs a tail bound before it is an exact inequality counterexample.

The original bounded U-coordinate canonical contraction is denoted E_A.
For a separated inner coefficient \(U^k\otimes U^l\), its inserted contraction is
\[
 p\longmapsto\bigl(E_A(pU^l)-pE_A(U^l)\bigr)U^k.
 \tag{R7}
\]
For all nonnegative integers l, the multiplier \(E_A(U^l)\) has norm at most one.
Consequently the Neumann tail after degree N has operator norm at most
\[
 (\|E_A\|_{2\to2}+1)\frac{(2|\lambda|)^{N+1}}{1-2|\lambda|}.
 \tag{R8}
\]
The continuous injective map \(u\mapsto u+\lambda u^2\) on the unit circle identifies U in W*(X), so (X,Y) still generates M.
The unchanged Y-coordinate dual and (R7) give an actual bounded dual system on H; the canonical closure agrees with it after vacuum normalization because the target star core is dense.
Its starred commutators are Hilbert--Schmidt, either by the same insertion series on the reference core or the actual normal-phase formula, and hence the actual conjugate-variable condition holds.
The coordinate-change family is therefore a test of stronger estimates only.

[J_F0009/normal_change.py](../computations/programs/Yin_J_F0009/normal_change.py) now computes the finite Neumann adjoints by exact rational free moments, including the actual Poisson score in xi.
At lambda=3/10, the runs (r,N)=(1/2,8),(1/2,12),(9/10,8) found the factor-two form positive definite on the real span of six specified selfadjoint mixed words, by exact rational LDL elimination.
The individual finite-truncation ratios ranged from approximately 0.671 to 1.056 in the first run and from approximately 0.997 to 1.006 in the last.
The N=8 and N=12 values for the first test at r=1/2 were approximately 1.0562741 and 1.0562674.
These are positive diagnostics only.
The infinite-series tail was not combined with a quantitative least-eigenvalue estimate, and no statement for all polynomials or arbitrary normal laws follows.

The endpoint problem remains unresolved in this round.
The specific new negative result is the strictly positive mixed-test obstruction to the sharp scalar fixed-vacuum identity.
The weaker positive-input estimate (R1) with an unspecified finite constant, or a full-domain counterexample for one fixed actual-A normal tuple, remains the mathematical continuation.

## Spectral cuts for the two contraction bounds

Fix one coordinate derivation \(\delta\) on the mixed starred core \(P\), and retain the actual vacuum and adjoint-domain hypotheses above.
Put \(G_0=E_0\) or \(F_0\), and set \(v_h=h\otimes1\) or \(1\otimes h\), respectively, for \(h\in H\).
The best constant on positive contractions is \(K_G^+=\sup_{a\in P,\,0\le a\le1}\|G_0a\|_2\), possibly infinite.
Since \(G_0(1)=0\), writing a selfadjoint contraction as \(2b-1\) and then taking real and imaginary parts gives \(\|G_0a\|_2\le4K_G^+\|a\|\) on the full core whenever \(K_G^+<\infty\).

For a positive contraction \(a\in P\), write \(e_a\) for its spectral measure.
Let \(Q_a\) be the joint spectral measure of left multiplication by \(a\) on the first coarse leg and right multiplication by \(a\) on the second.
For each \(h\), define a finite complex measure on \([0,1]^2\) by
\[
 \nu_{a,h}(B)=\langle v_h,Q_a(B)\delta a\rangle .
\]
Orthogonality for disjoint spectral sets and Cauchy--Schwarz give \(\|\nu_{a,h}\|_{\rm TV}\le\|h\|_2\|\delta a\|_2\).
The Leibniz rule gives \(\delta f(a)=f^{[1]}(Q_a)\delta a\) for each scalar polynomial, where the divided difference on the diagonal is \(f'\).

Here \(Q_a(\{s=t\})\delta a=0\), including when \(a\) has spectral atoms.
Indeed, faithfulness of the trace implies that the spectral measures of left and right multiplication on individual leg vectors are absolutely continuous with respect to \(\mu_a=\tau\circ e_a\).
On simple tensors the joint measures are products, so \(Q_a\) vanishes on the nonatomic part of the diagonal by density of their linear span.
For each atom \(c\) choose \(R>1\) and the polynomials \(p_n(t)=(t-c)(1-(t-c)^2/R^2)^n\).
They converge uniformly to zero on \([0,1]\), their derivatives are uniformly bounded there, \(p'_n(c)=1\), and \(p'_n(t)\to0\) elsewhere.
For the derivative bound use \(n u(1-u)^{n-1}\le1\) for \(0\le u\le1\), by the binomial expansion.
Consequently \(p_n^{[1]}\) are uniformly bounded and converge pointwise to the indicator of \((c,c)\).
The spectral theorem now gives \(\delta p_n(a)\to Q_a(\{(c,c)\})\delta a\) in the coarse Hilbert space.
The dense tensor-adjoint domain stated above makes \(\delta\) closable, so this limit vanishes.
Summation over the at most countably many atoms proves the assertion.

Define the scalar function for almost every \(0<x<1\) by
\[
 k_{a,h}(x)=\int_{s\ne t}
 \frac{{\bf1}_{\{\min(s,t)<x<\max(s,t)\}}}{|s-t|}\,d\nu_{a,h}(s,t).
 \tag{C1}
\]
The kernel has \(x\)-integral one off the diagonal, so \(\|k_{a,h}\|_{L^1(dx)}\le\|\nu_{a,h}\|_{\rm TV}\).
Integrating \(f'\) on the interval between \(s\) and \(t\) and applying Fubini against this total-variation bound gives
\[
 \langle h,G_0f(a)\rangle=\int_0^1 f'(x) k_{a,h}(x)\,dx .
 \tag{C2}
\]
Each endpoint admits the exact test
\[
 K_G^+=\sup_{\substack{a\in P,\ 0\le a\le1\\ \|h\|_2\le1}}
                \|k_{a,h}\|_{L^\infty(0,1)} .
 \tag{C3}
\]
Taking \(f(t)=t\) in (C2) proves that the left side is bounded by the right.
For the reverse bound, take \(\phi\ge0\) smooth with compact support in \((0,1)\) and integral one, and put \(f(t)=\int_0^t\phi(x)\,dx\).
Its real Bernstein polynomials \(f_n\) take values in \([0,1]\) there because their coefficients \(f(j/n)\) lie in \([0,1]\) and the Bernstein basis is a positive partition of unity.
Apply the [checked tensor Bernstein derivative approximation](../audits/literature/VV16/Yin_U001.md#vv16-u001) to \((s,t)\mapsto f(s)\) on the unit square.
Its polynomial is \(f_n(s)\), since the basis in \(t\) sums to one, so \(f_n'\to f'\) uniformly.
Thus \(f_n(a)\) are positive contractions in \(P\), and (C2) gives \(|\int\phi k_{a,h}|\le K_G^+\|h\|_2\).
Taking a nonnegative smooth approximate identity at Lebesgue points proves the asserted essential bound also for these complex-valued profiles.
This argument tests only core polynomials and never evaluates \(\delta\) at a discontinuous spectral projection.

For \(h\in\operatorname{Dom}G_0^*\), the actual adjoint gives a more explicit form,
\[
 k_{a,h}(x)=\langle G_0^*h,e_a((x,1])\Omega\rangle
 \quad\text{for almost every }x\in(0,1).
 \tag{C4}
\]
In fact the spectral theorem writes \(f(a)=f(0)1+\int_0^1 f'(x)e_a((x,1])\,dx\) weakly, and the constant term pairs to zero since \(G_0(1)=0\).
Comparing with (C2) for all polynomial derivatives identifies the two integrable functions, by uniform polynomial density in \(C[0,1]\).
In particular both legs have \(G_0^*\Omega=\xi\), hence \(|k_{a,\Omega}(x)|\le\|\xi\|_2\sqrt{\tau(e_a((x,1]))}\).
Both adjoint domains contain the dense starred core, so (C3) can be tested using only unit vectors \(h\in P\).
Indeed, a uniform bound on those vectors implies \(|\langle h,G_0a\rangle|\le K\|h\|_2\) by (C2), which then extends to all \(h\in H\) by density.
Thus a sufficient and necessary bound on one leg is uniform control of the pairings in (C4) by \(K\|h\|_2\) for core \(h\), all mixed positive core contractions \(a\), and almost every threshold \(x\).

The [Haar absolute-phase computation](../claims/Yin_C_F0054_v1.md#4-exact-haar-circle-failure-of-the-transformed-contraction-estimate) tests the loss of information in using the vacuum direction alone.
For that transformed derivation \(G_0=(\mathrm{id}\otimes\tau)\delta_0\) satisfies \(G_0z^{\pm n}=\mathrm i\lambda_n z^{\pm n}\), \(\lambda_n\to\infty\), and \(\xi=0\).
Take \(a_n=(1+\operatorname{Re}z^n)/2\) and \(h_n=\sqrt{2}\operatorname{Re}z^n\).
These are a positive core contraction and a unit core vector, with \(|\langle h_n,G_0a_n\rangle|=\lambda_n/(2\sqrt{2})\).
Equations (C2) and (C4) give \(\|k_{a_n,h_n}\|_\infty\ge\lambda_n/(2\sqrt{2})\) while every vacuum profile vanishes.
The prescribed coordinate identity \(\delta X=1\otimes1\) fails for this transformed derivation.
For an actual normal coordinate, the outstanding estimate is (C3) uniformly in the two mixed tests for a fixed tuple on each leg.
Finiteness for both legs restores the two canonical domains by [C_F0072, Part B](../claims/Yin_C_F0072_v1.md#statement).

### A sharp threshold on a fixed singular marginal

Use the [shrinking-circle law of C_F0143](../claims/Yin_C_F0143_v1.md#argument) for \(Z\), with radii \(r_n=2^{-n}\), weights \(p_n=(1-s)s^{n-1}\), \(s=2^{-b}\), \(b=3/4\), and normalized Haar measure on each circle.
This fixed law \(\mu\) has a scalar actual vacuum \(\xi_N\in L^2(N)\) for \(N=W^*(Z)\), even though the fourth composition of the marginal curvature kernel is infinite on a set of positive product measure.
Let \(S_0\) be standard semicircular and free from \(N\).
For \(\gamma>0,\ \beta\ge0\), set \(d_n=r_n^\gamma n^{-\beta}\), let \(h(z)=1+d_n\) on the \(n\)-th circle, and take \(Y=h(Z)S_0h(Z)\).
The normal pair \((Z,Y)\) generates \(M=W^*(N,S_0)\), since \(1\le h\le2\) gives \(S_0=h(Z)^{-1}Yh(Z)^{-1}\).
For \(B\in N\) the reference free law gives \(E_N(S_0 B S_0)=\tau(B)1\) by testing against \(N\) and centering the two \(N\) factors.
Hence \(E_N(Y^2)=\tau(h^2)h^2\) is nonconstant, so \(Y\) and \(N\) are dependent even in this second-moment test.

The kernel \(u(z,w)=h(z)h(w)\) in the [measurable Gaussian criterion C_F0157](../claims/Yin_C_F0157_v1.md#statement) is positive, bounded and has bounded reciprocal.
The ratio \(u(w,v)/u(z,w)=h(v)/h(z)\) eliminates the middle variable in its second integral.
That criterion gives \(\mathsf A(Z,Y)\Longleftrightarrow\mathsf S(Z,Y)\Longleftrightarrow I<\infty\), where
\[
 I=\iint\frac{|h(v)/h(z)-h(z)/h(v)|^2}{|z-v|^2}\,d\mu(z)\,d\mu(v).
 \tag{C5}
\]
The numerator vanishes for points on the same circle.
For \(z\) on circle \(n\) and \(v\) on circle \(m>n\), the separation satisfies \(r_n/2\le |z-v|\le3r_n/2\).
Moreover \(d_m/d_n\le2^{-\gamma}\) and the numerator before squaring equals \((d_n-d_m)(1/h(z)+1/h(v))\) in absolute value.
It thus lies between \((1-2^{-\gamma})d_n\) and \(2d_n\).
Summing the two orders of the circles and using \(\sum_{m>n}p_m=s^n\) gives two-sided comparison, with constants depending only on \(b,\gamma\),
\[
 I\asymp\sum_{n\ge1}p_n s^n\,d_n^2/r_n^2
 \asymp\sum_{n\ge1}2^{-2n(b+\gamma-1)}n^{-2\beta}.
 \tag{C6}
\]
Consequently both target hypotheses hold for \(\gamma>1/4\) and both fail for \(0<\gamma<1/4\).
At the critical exponent \(\gamma=1/4\), both hold exactly when \(\beta>1/2\).

In the finite regime \(I\) is the squared norm of the degree-two correction \(\chi\) to the marginal vacuum in the original target \(Z\) coordinate.
The [two reference-to-target contraction estimates of C_F0156](../claims/Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form) bound the right slice \(E_0\) and its adjoint-reversed slice \(p\mapsto(F_0(p^*))^*\) by \(K_0\|\xi_N\|_2+2\sqrt{2I}\), with \(K_0=\sqrt{4/\pi}(5+2\sqrt{27})\).
The involutions preserve both norms, so (C3) gives this bound on each \(Z\) leg for all mixed target tests despite the marginal curvature divergence.
Along \(\gamma=1/4\) the squared correction norm grows comparably to \((2\beta-1)^{-1}\) as \(\beta\downarrow1/2\), by (C6) and integral comparison.
This calculation determines the growth of the vacuum correction and supplies an upper bound on the cut norm.
Below the integrability threshold the pair fails the required antecedent \(\mathsf A\), so the unrestricted normal converse remains open.

<a id="first-output-layer-and-two-occurrence-inputs"></a>
## The first output layer and the full slice on two-occurrence inputs

Consider an arbitrary bounded normal ACSY tuple and distinguish coordinate \(i\).
Use \(N=W^*(X_j:j\ne i)\), \(x=X_i-\mathbb E_N X_i\), \(H_x=\overline{NxN}^{\,2}\) (closed linear span), \(A=N\bar\otimes N^{\rm op}\), and the polar data \(W,h\) of [C_F0217](../claims/Yin_C_F0217_v1.md#statement).
Let \(P_1\) be the Hilbert projection onto \(L^2(N)\oplus H_x\), and regard \(W^*:L^2(A)\to H_x\) as the isometry onto the coarse summand.
Write \(\delta=\delta_i\), \(\xi=\delta^*(1\otimes1)\), \(Ep=(\mathrm{id}\otimes\tau)\bar\delta p\), and \(\epsilon(a)=(\delta(a^*))^\dagger\), where \(\dagger\) flips and takes adjoints.
By the [normal phase formula](../claims/Yin_C_F0076_v1.md#statement), \(K=\bar\epsilon(x)=(\bar\delta x^*)^\dagger\) is in the abelian marginal tensor algebra and its phase has modulus one almost everywhere.
Here both closed derivations kill \(N\) and intertwine its left and right actions by the [omitted-algebra graph argument](../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra).
Map a Hilbert tensor into \(L^2(\mathcal B)\), \(\mathcal B=M\bar\otimes M^{\rm op}\), by the linear unitary \(\Phi(c\otimes d)=c\otimes d^{\rm op}\).
Set \(K_0=\Phi(K)^*\), which takes adjoints in both legs, with no additional flip.
On the abelian marginal tensor subalgebra \(\Phi\) preserves multiplication as well as the trace and the adjoint, so \(K_0\) is unitary in \(\mathcal B\).
With \(\mathbb E_A:\mathcal B\to A\) the product-trace-preserving conditional expectation, put
\[
                    V_p=\mathbb E_A\big((p\otimes1)K_0\big)\in A .
\]
For every bounded \(p\) which admits uniformly operator-bounded original core approximants converging strongly-star to \(p\) and in the graph of \(\bar\delta\), one has
\[
                 P_1 Ep=P_1(p\xi^*)-W^*\big(V_p h^{-1/2}\big).            \tag{L1}
\]
This includes every original starred polynomial.

To verify (L1), take \(q=\sum_j a_j\otimes b_j^{\rm op}\in N\odot N^{\rm op}\) and \(y=qx=\sum_j a_jxb_j\).
The bounded products \(y^*p\) belong to \(\operatorname{Dom}\bar\delta\) with the product rule.
Indeed bounded strong-star approximations to \(a_j,b_j,\mathbb E_NX_i\) by omitted-coordinate core polynomials have identically zero derivatives.
Such approximations exist by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001), using the norm density of the polynomials in their \(C^*\)-algebra.
They approximate \(y^*\) in its graph by the polynomial product rule, since bounded strong-star convergence of outer factors acts strongly on the coarse Hilbert space.
Multiplying by the stipulated approximants for \(p\) gives the stated product rule in the closure.
Pair the rule for \(y^*p\) with the vacuum tensor and use its actual adjoint.
For \(y=axb\) the resulting endpoint term \((\tau\otimes\tau)((\bar\delta y^*)p)\) equals \(\langle a\otimes b^{\rm op},(p\otimes1)K_0\rangle_{L^2(\mathcal B)}\), with the inner product linear in its second entry.
Indeed if \(K=c\otimes d\) then \(\bar\delta y^*=b^*d^*\otimes c^*a^*\), so the two factors after tracing are \(\tau(a^*p c^*)\) and \(\tau(b^*d^*)\).
The two sides are continuous in the Hilbert tensor \(K\) for these fixed bounded elements, giving the identity for the actual phase.
Summing and projecting onto \(A\) gives
\[
                 \langle qx,Ep\rangle=\langle qx,p\xi^*\rangle
                                        -\langle q,V_p\rangle_{L^2(A)} .
\]
By the cyclic-module formula \(W(qx)=q h^{1/2}\), where \(W\) vanishes on its kernel summand, and both \(h^{1/2},h^{-1/2}\) are in \(L^2(A)\).
Thus \(\langle qh^{1/2},V_p h^{-1/2}\rangle=\tau_A(q^*V_p)\), by tracial cycling of the two \(L^2\) factors and \(h^{-1/2}h^{1/2}=1\).
This proves (L1) against \(H_x\) by density, even when \(H_x\) contains a singular summand.
Testing instead against \(N\) gives \(\mathbb E_N(Ep)=\mathbb E_N(p\xi^*)\) by the same product rule with zero endpoint term.
Orthogonality proves (L1) against the full range of \(P_1\).

Conditional Schwarz, positivity of \(\mathbb E_A\), and unitarity of \(K_0\) give for any finite column
\[
 \sum_j V_{p_j}^*V_{p_j}
 \ \le\ \mathbb E_A\!\left(K_0^*\big((\textstyle\sum_j p_j^*p_j)\otimes1\big)K_0\right)
 \ \le\ \left\|\sum_j p_j^*p_j\right\|1_A .
\]
Pairing with the normal positive functional \(a\mapsto\langle h^{-1/2},a h^{-1/2}\rangle\) bounds the column of correction terms in (L1).
Projection is contractive and \(\sum_j\|p_j\xi^*\|_2^2\le\|\xi\|_2^2\|\sum_j p_j^*p_j\|\).
The Hilbert direct-sum triangle inequality therefore yields
\[
   \left(\sum_j\|P_1Ep_j\|_2^2\right)^{1/2}
    \le\big(\|\xi\|_2+\|h^{-1/2}\|_{2,A}\big)\left\|\sum_jp_j^*p_j\right\|^{1/2}
    \le 2\|\xi\|_2\left\|\sum_jp_j^*p_j\right\|^{1/2}.               \tag{L2}
\]
The last inequality is the actual inverse-density estimate in C_F0217.
Consequently the full [polynomial column cost](../claims/Yin_C_F0208_v1.md#statement) is finite exactly when the complementary cost for \((I-P_1)E\) is finite.

In particular (L2) bounds the entire slice on finite columns from the linear span of \(N,NxN,NxNxN\), allowing arbitrary bounded coefficients in \(N\).
The approximants above apply to each such word, since \(\bar\delta x=1\otimes1\), and also to every term in its finite product rule.
For \(a,b,d\in N\) one has \(E(axbxd)=a\,\tau(bxd)+axb\,\tau(d)=axb\,\tau(d)\), as \(\mathbb E_Nx=0\).
The slices on \(N\) and \(NxN\) lie in \(L^2(N)\).
Thus \(P_1\) fixes the full slice on all these inputs.
For unrestricted mixed words the new bound leaves only the component orthogonal to both the omitted algebra and its cyclic \(x\)-bimodule.
No estimate on that remaining component has been deduced here.

### The joint span of \(x\) and \(x^*\) under a phase gap

There is a further estimate on \(H_{x,x^*}=\overline{\operatorname{span}(NxN+Nx^*N)}^{\,2}\) when \(t=\mathbb E_A(k)\), \(k=\Phi(\bar\delta x^*)\), satisfies \(\|t\|<1\).
The scalar phase is symmetric in the two spectral variables, so \(k\) is unitary, \(\Phi(\bar\epsilon x)=k^*\), and \(K_0=k\) in (L1).
Write \(y=qx+rx^*\) for \(q,r\in N\odot N^{\rm op}\) and let \(\pi(a\otimes b^{\rm op})v=avb\) on \(L^2(M)\).
Taking \(\Phi\) of the two derivatives gives \(q+rk\) and \(qk^*+r\), respectively.
The actual vacuum \(\xi\) of \(\delta\) and the actual vacuum \(\xi^*\) of \(\epsilon\) therefore give
\[
 \langle y,\xi\rangle=\tau_A(q^*+t^*r^*),\qquad
 \langle y,\xi^*\rangle=\tau_A(tq^*+r^*) .
\]
Let \(P_{x,x^*}\) project onto this joint cyclic span and set \(\eta_1=P_{x,x^*}\xi,\ \eta_2=P_{x,x^*}\xi^*\).
On the closed joint cyclic span of \(\eta_1,\eta_2\) under \(\pi(N\odot N^{\rm op})\), the action extends normally to \(A\).
To check this without assuming a spatial tensor action on the whole ambient Hilbert space, close the restriction \(T:y\mapsto q+rk\) into \(L^2(\mathcal B)\).
It is a well-defined closable map by the graph of \(\bar\delta\), and the polar isometry intertwines the two \(N\)-actions from \((\ker T)^\perp\) into the left regular action on \(L^2(\mathcal B)\), by the unitary graph argument in C_F0217.
The latter action of \(A\subset\mathcal B\) is normal.
Its closed range subspace \(\overline{\operatorname{ran}T}\) reduces this action since it reduces both factor actions.
Thus the equivalent action \(\pi\) on \((\ker T)^\perp\) is normal on \(A\).
Both projected vacua lie there, since the two vacuum pairings against \(y\) are the pairings of \(Ty\) with \(1,k\), respectively, and hence extend to zero on \(\ker T\).

For a bounded \(p\) with the approximants used in (L1), write \(V_p=\mathbb E_A((p\otimes1)k)\) and \(U_p=\mathbb E_A(p\otimes1)\).
The two endpoint computations on \(qx\) and \(rx^*\) give
\[
 \langle y,p\xi^*-Ep\rangle=\tau_A(q^*V_p+r^*U_p).
\]
The \(x^*\)-term uses \(\bar\delta x=1\otimes1\) in \(\bar\delta((rx^*)^*)\).
Set
\[
 G=\begin{pmatrix}1&t\\t^*&1\end{pmatrix}\in M_2(A),\qquad
 \binom{a_p}{b_p}=G^{-1}\binom{V_p}{U_p}.
\]
This is a bounded inverse of norm at most \((1-\|t\|)^{-1}\) by the norm of its off-diagonal part.
For \(a,b\in A\) the vacuum pairings above give
\[
 \langle y,\pi(a)\eta_1+\pi(b)\eta_2\rangle
  =\tau_A\!\left(q^*(a+tb)+r^*(t^*a+b)\right).
\]
For algebraic coefficients this follows by moving their adjoints onto \(y\), and bounded ultraweak approximation proves it for all \(a,b\) using normality on the projected vacua and normal tracial pairings on \(A\).
Consequently \(P_{x,x^*}(p\xi^*-Ep)=\pi(a_p)\eta_1+\pi(b_p)\eta_2\).
For any finite column, conditional Schwarz gives \(\sum_j(V_{p_j}^*V_{p_j}+U_{p_j}^*U_{p_j})\le2\|\sum_j p_j^*p_j\|1_A\).
Applying \((G^{-1})^*G^{-1}\le(1-\|t\|)^{-2}I_2\) between each coefficient column and its adjoint gives
\[
 \sum_j(a_{p_j}^*a_{p_j}+b_{p_j}^*b_{p_j})
 \le 2(1-\|t\|)^{-2}\left\|\sum_jp_j^*p_j\right\|1_A .
\]
Since both projected vacua have norm at most \(\|\xi\|_2\), the same triangle and projection argument gives the joint projected column bound with constant \(\big(1+2\sqrt2/(1-\|t\|)\big)\|\xi\|_2\), including the orthogonal \(L^2(N)\)-summand.
This estimate controls the right slice on every original starred polynomial after projection to \(L^2(N)\oplus H_{x,x^*}\).
The phase gap is an additional assumption, and the estimate allows divergence of its constant as \(\|t\|\uparrow1\).

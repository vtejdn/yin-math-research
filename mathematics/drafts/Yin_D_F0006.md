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

<a id="weighted-phase-and-a-gapless-normal-factor"></a>
## A vacuum-weighted phase condition and a normal factor with no phase gap

The [weighted phase theorem](../claims/Yin_C_F0228_v1.md#decision-reviewed) fixes the joint projected estimate for an abelian omitted algebra and the example with an unbounded inverse phase weight.
It remains open whether the weighted norm of the projected vacua is finite on all normal pairs, or whether the joint projected cost can remain finite even when it is infinite.
For a nonabelian omitted algebra the endpoint system contains \(V_p-tU_p=C_p+[U_p,t]\), with \(C_p=\mathbb E_A((p\otimes1)(k-t))\) and phase defects \(1-tt^*\) and \(1-t^*t\) on different sides.
The proof in the fixed claim uses commutativity precisely to remove this extra term.

<a id="radial-phase-factorization-and-adjoint-orientation"></a>
## The two orientations of the shifted radial phase

Use the [shifted singular-law identity](../claims/Yin_C_F0229_v1.md#statement) for \(T=X_i-b=UP,\ b\in N\).
Write \(\nu,\mu\) for the spectral laws of \(X_i,P\) respectively, and \(k,m\) for the marginal and shifted radial phases of that identity.
Define \(A:L^2(\mu)\to L^2(\nu)\) by \(Af=\mathbb E_{W^*(X_i)}(U f(P))\) in spectral coordinates.
It is a contraction because \(U\) is unitary and conditional expectation is an orthogonal projection.
For bounded scalar functions \(f,g\) one has the bilinear identity
\[
 \iint f(v)g(w)m(v,w)\,d\mu(v)d\mu(w)
  =\iint (Af)(z)(Ag)(y)k(z,y)\,d\nu(z)d\nu(y).
 \tag{RF}
\]
Indeed for a product symbol \(k=\alpha(X_i)\otimes\beta(X_i)^{\rm op}\), the trace against \(f(P)\otimes g(P)^{\rm op}\) after the two polar multiplications is
\(\tau(f(P)\alpha(X_i)U)\tau(\beta(X_i)Ug(P))\).
Moving the first \(U\) by cyclicity gives exactly the two indicated conditional expectations, with the same \(U\) on both inputs.
Rectangular simple symbols approximate \(k\) in \(L^2(\nu^2)\), and multiplication by the polar tensor unitaries and bounded test functions is continuous there into the ambient \(L^2\) space.
The identity extends to \(f,g\in L^2(\mu)\) by the Hilbert–Schmidt kernel bound and contractivity of \(A\).
In particular \(m\) is symmetric almost everywhere because \(k\) is.

If \(K_k,K_m\) denote the integral operators with these kernels and \(J_\mu,J_\nu\) scalar conjugations, (RF) says \(K_m=(J_\nu A J_\mu)^*K_k A\).
In particular \(s_j(K_m)\le s_j(K_k)\) for every singular-value index, by composing rank-\(<j\) approximants with the two contractions.
The actual vacuum tested on \(U f(P)\) has radial representative \(\mathbb E_{W^*(P)}(U^*\xi)\), directly by the Hilbert pairing.
For \(e=1_B(P)\), (RF) uses \(a_e=\mathbb E_{W^*(X_i)}(Ue)\) on both legs.
The pointwise bound
\[
 |a_e|^2\le\mathbb E_{W^*(X_i)}(UeU^*)\mathbb E_{W^*(X_i)}(e)
\]
follows by applying the matrix-amplified expectation to the positive Gram block of the column \((Ue,e)^{\mathsf T}\) times its adjoint.
Integration and Cauchy–Schwarz give \(\|a_e\|_1\le\tau(e)\).

For the actual adjoint orientation take \(T^*=U^*P'\) with \(P'=UPU^*\) and conjugate derivation \(\epsilon(a)=(\delta_i(a^*))^\dagger\).
Its vacuum is \(\xi^*\), and its marginal phase is \(k^*\), since the flip-star of the symmetric symbol \(k\) is its conjugate. [Normal phase and conjugate derivation](../claims/Yin_C_F0076_v1.md#statement)
Put \(V=U\otimes(U^*)^{\rm op}\).
Conjugation by \(V\) transports the product spectral algebra of \(P\) to that of \(P'\) and intertwines their trace-preserving expectations.
Reversed multiplication on the opposite leg gives the exact identity
\[
 V^*(1\otimes(U^*)^{\rm op})\,k^*(U^*\otimes1)V
    = (U^*\otimes1)\,k^*(1\otimes(U^*)^{\rm op})
    = \big((1\otimes U^{\rm op})k(U\otimes1)\big)^* .
\]
Thus in the common radial variable the opposite compression is \(\overline{m(v,w)}\), including at atoms of the positive singular law.
The opposite radial vacuum, transported by \(U^*(\cdot)U\), is likewise \(\mathbb E_{W^*(P)}(\xi^*U)=\mathbb E_{W^*(P)}(U^*\xi)^*\).
Both orientations give exactly the same real defect on every radial rectangle.
These identities constrain the full compressed kernel but give no exponent improvement for a general omitted shift.

<a id="nonpositive-compressed-phase"></a>
## A two-thirds exponent at shifts with nonpositive radial phase pairing

In the setting and notation of the [uniform omitted-shift theorem](../claims/Yin_C_F0229_v1.md#statement), write \(T=X_i-b=UP\), with \(P=|T|\) and \(b\in N=W^*(X_j:j\ne i)\).
Use \(\xi=\delta_i^*(1\otimes1)\), \(\mu\) the law of \(P\), the actual phase \(k=\Phi(\delta_i X_i^*)\), and \(m\) the conditional expectation of \((1\otimes U^{\rm op})k(U\otimes1)\) onto the abelian two-leg algebra generated by \(P\).
For \(r>0\) define
\[
 V_r=rT(P^2+r^2)^{-1},\qquad h_r(v)=\frac{r^2}{r^2+v^2},\qquad
 A_r=\tau(h_r(P)),\qquad a_r(v)=\frac{rv}{r^2+v^2}.
\]
Suppose that for this shift and radius
\[
             \iint a_r(v)a_r(w){\rm Re}\,m(v,w)\,d\mu^2\le0 .        \tag{1}
\]
Then \(e=1_{[0,r]}(P)\) satisfies
\[
              \tau(e)^3\le8r^2\|\xi\|_2^2.                            \tag{2}
\]
In particular the pointwise sign \({\rm Re}\,m\le0\) suffices at every radius.

For a finite family of such shifts and radii denote their quantities by \(A_j,V_j,e_j\).
Define
\[
 B=\sup_{\|z\|_2=1}\sum_j
              |\langle z,V_j/\sqrt{A_j}\rangle|^2.
\]
If (1) holds for each test then
\[
             \sum_j\frac{\tau(e_j)^3}{r_j^2}\le 8B\|\xi\|_2^2.        \tag{3}
\]
Pairwise orthogonality of the regularized test vectors gives \(B\le1\), since their normalized norms are at most one.
The tests in (3) need no pairwise orthogonality.
To apply this estimate to the [general packing obstruction](../claims/Yin_C_F0211_v1.md#statement) requires sign and overlap control on the particular family.

### Resolvent pairing and overlap weights

The [closed resolvent formula](../claims/Yin_C_F0229_v1.md#argument) and its [polar trace calculation](../claims/Yin_C_F0229_v1.md#the-integrated-phase-defect) give the exact equality
\[
     A_r^2
      =r\,{\rm Re}\langle\xi,V_r\rangle
                +\iint a_r(v)a_r(w){\rm Re}\,m(v,w)\,d\mu^2 .
\]
Indeed multiply the differentiated formula at \(s=r^2\) by \(r^2\) before tracing.
The leading term is \(r^4\tau((P^2+r^2)^{-1})^2=A_r^2\).
The phase term uses \(V_r=Ua_r(P)\).
Since \(a_r^2=h_r(1-h_r)\le h_r\), one has \(\|V_r\|_2\le\sqrt{A_r}\).
By (1), \(A_r^{3/2}\le r\|\xi\|_2\).
The scalar bound \(1_{[0,r]}\le2h_r\) gives (2).
For a family retain the pairing with \(V_j/\sqrt{A_j}\) and square, giving
\(A_j^3/r_j^2\le|\langle\xi,V_j/\sqrt{A_j}\rangle|^2\).
The definition of \(B\) now proves (3).

A separate overlap bound is available for positive invertible weights \(w_j=w_j(P_j)\).
For \(z\in H\), traciality gives
\[
  |\langle V_j,z\rangle|
       \le \|V_jw_j^{-1/2}\|_2\,\|z w_j^{1/2}\|_2 .
\]
Thus \(B\le\sup_j[\tau(a_{r_j}(P_j)^2/w_j)/A_j]\,\|\sum_j w_j\|\).
The bound also holds with left weights in \(W^*(|T_j^*|)\) by the corresponding left factorization.
Pairwise orthogonality of the sharp small-value projections alone gives neither the orthogonality of the regularized vectors nor the displayed weighted bound.
In particular \(w_j=h_{r_j}(P_j)\) gives the quotient \((1-A_j)/A_j\); this can grow when the small-mass test is most sensitive.
For the [strict positive compressed phase countermodel](Yin_D_F0003.md#sharp-scalar-limits-of-radial-vacuum-tests-at-an-omitted-shift), the integral in (1) has the opposite sign, so its failure of exponent \(2/3\) is compatible with this calculation.

<a id="shifted-modulus-graph-and-phase-mismatch"></a>
## The two actual graph derivatives at the singular modulus

Let \(T=X_i-b=UP\) as in [C_F0229](../claims/Yin_C_F0229_v1.md#statement), let \(\delta=\delta_i\), and use \(G=L^2(M)\otimes_2L^2(M)\) with outer actions.
The unitary \(U\) need not belong to the domain of \(\bar\delta\).
In \(G\) write \(v,w\) for the commuting outer spectral coordinates given by \(P\) on the left and on the right.
Put \(L=U^*(1\otimes1)\), \(R=(\bar\delta T^*)U\), where the multipliers indicated outside the parentheses are outer.
Both vectors have norm one, since \(\Phi(\bar\delta T^*)=k\) is unitary and \(U\) is unitary.
Then
\[
      P\in\operatorname{Dom}\bar\delta,\qquad
      \bar\delta P=\frac{v}{v+w}L+\frac{w}{v+w}R .
\]
Indeed the polynomial product rule gives \(\bar\delta(P^2)=vL+wR\) using the bounded graph approximants to \(T,T^*\) from C_F0229.
For \(\eta>0\), approximate \(s\mapsto\sqrt{s+\eta}\) in \(C^1\) by polynomials on a fixed compact interval containing the spectrum of \(P^2\).
The derivatives converge by the joint spectral calculus for divided differences on \(G\).
The divided difference acting on \(vL+wR\) is \(1/(\sqrt{v^2+\eta}+\sqrt{w^2+\eta})\).
The resulting two scalar coefficients are bounded by one, so converge strongly on their respective vectors as \(\eta\downarrow0\).
The inputs converge in operator norm to \(P\); the zero spectral projection of \(P\) vanishes by C_F0229.
This proves the formula and the bound \(\|\bar\delta P\|_2\le2\).

There is a sharper constraint on the difference of the two data:
\[
 \big\|(v+w)^{-1/2}(L-R)\big\|_2^2
      =2\iint\frac{1-{\rm Re}\,m(v,w)}{v+w}\,d\mu(v)d\mu(w)
      \le 2\|\xi_i\|_2 .
\]
Here \(m\) is exactly the conditional expectation in C_F0229.
In the opposite tensor convention \(\Phi(L)=U^*\otimes1\), \(\Phi(R)=(1\otimes U^{\rm op})k\), both unitaries.
For each bounded nonnegative spectral multiplier \(g(v,w)\), taking the trace and cycling gives
\(\|g^{1/2}(L-R)\|_2^2=2\iint g(1-{\rm Re}\,m)\,d\mu^2\), with the order \(m=\mathbb E((1\otimes U^{\rm op})k(U\otimes1))\).
Monotone convergence of spectral truncations and the integrated phase identity prove the assertion for the unbounded multiplier.
In particular \((v+w)^{-1/2}(\bar\delta P-L)\) and \((v+w)^{-1/2}(\bar\delta P-R)\) both have norm at most \(\sqrt{2\|\xi_i\|_2}\).
An analogous statement for the reversed coordinate follows by applying the argument to the adjoint tuple and the shift \(b^*\).
One may also control the polar factor in the following weighted sense on the original Hilbert space.
Put \(U_\eta=T(P^2+\eta)^{-1/2}\).
These are contractions in the closed graph by the same \(C^1\) argument and converge to \(U\) strongly-star as \(\eta\downarrow0\).
For \(s_v=\sqrt{v^2+\eta}\), differentiating and multiplying by \(U^*\) on the outer left gives
\[
 U^*\bar\delta U_\eta=
 \frac{s_v s_w+\eta}{s_v s_w(s_v+s_w)}\,L
 -\frac{vw}{s_v s_w(s_v+s_w)}\,R .
\]
Indeed the derivative of \(T f(P^2)\), with \(f(a)=(a+\eta)^{-1/2}\), gives \(s_w^{-1}L+v f^{[1]}(v^2,w^2)(vL+wR)\), and \(f^{[1]}=-1/(s_vs_w(s_v+s_w))\).
Multiplication by \((v+w)^{1/2}\) gives actual weak Hilbert convergence to \((v+w)^{-1/2}(L-R)\), with a bound independent of \(b,\eta\).
To see uniform boundedness write \(t=\sqrt\eta\), \(h_t(v)=t^2/(v^2+t^2)\), and split the formula as \(c_\eta(L-R)+d_\eta L\), where \(c_\eta=vw/(s_vs_w(s_v+s_w))\).
The first coefficient is at most \(1/(v+w)\).
For the second one use \(1-vw/(s_vs_w)\le h_t(v)+h_t(w)\) and \(t^2/(s_vs_w)\le(h_t(v)+h_t(w))/2\).
Since \(s_v+s_w\ge(v+w+t)/2\), it follows that \(0\le d_\eta\le3(h_t(v)+h_t(w))/(v+w+t)\).
The scalar joint spectral law on the vector \(L\) is \(\mu\otimes\mu\) by traciality and unitarity of \(\Phi(L)\).
Consequently the squared norm of \((v+w)^{1/2}d_\eta L\) is at most
\[
 36\left(\int h_t(v)\,d\mu(v)\right)
    \left(\int\frac{d\mu(w)}{w+t}\right).
\]
Both factors can be bounded using \(\mu([0,r])\le C\sqrt r\), \(C=\sqrt{\pi\|\xi_i\|_2}\).
Indeed \(h_t(v)\le 2t/(t+v)\) and Tonelli gives
\(\int (w+t)^{-1}d\mu(w)=\int_0^\infty\mu([0,r])(r+t)^{-2}dr\le(\pi/2)C/\sqrt t\).
Their product is at most \(\pi^2 C^2/2\).
The weighted defect estimate controls the first term, so the entire weighted derivative is uniformly bounded.
On each spectral region \(v+w\ge c>0\), bounded convergence of the multipliers gives strong convergence of the projected vectors.
The union of those projected test spaces is dense because \(P\) has zero kernel, which proves weak convergence on the full coarse space.
Controlling the unweighted polar gradient would involve the second inverse power of \(v+w\).

<a id="two-point-modulus-matrix-encoding"></a>
## A rank obstruction to algebraically encoding the two-point modulus by normal coordinates

The [fixed matrix-unit argument](../claims/Yin_C_F0232_v1.md#matrix-units-and-coarse-derivation-parameters) gives \(d\le1+(2k^2)^{-1}\) for normalized coarse derivations at a star-generating list of the matrix-amplified two-point modulus algebra.
The [normal-encoding argument](../claims/Yin_C_F0232_v1.md#normal-encodings-and-moment-perturbations) excludes uniformly bounded vacua under vanishing moment perturbations of the real–imaginary and polar pairs, including at zero modulus.
A remaining construction could use a proper represented star subalgebra with the same von Neumann closure, or introduced randomness whose effect persists in the limiting joint law.
Either route requires constructing the actual derivations on the new represented core.

For example, the subgroup generated by \(u\) and \(sus\) is free on these two generators.
A reduced word in their alternating nonzero powers remains a nonempty reduced group word after replacing \((sus)^n\) by \(su^ns\).
Their traces therefore give the two free Haar laws, and their star algebra is proper since it lies in the even kernel of the homomorphism sending \(s\) to the generator of \(\mathbb Z_2\) and \(u\) to zero.
The free normal estimate applies to this pair. [Free normal bounds](../claims/Yin_C_F0162_v1.md#statement)

The midpoint representation of the nonnormal coordinate gives a different pair of unitaries, \(A=u(h+i\sqrt{1-h^2})\) and \(B=u(h-i\sqrt{1-h^2})\), with \((A+B)/2=uh\).
Its relative unitary \(A^*B\) has two atoms of mass \(1/2\), since it is \((h-i\sqrt{1-h^2})^2\) at the two values \(h=\varepsilon,1\) with \(0\le\varepsilon\le1/2\).
For a candidate actual normal tuple with unitary coordinates \(A',B'\), let \(W=(A')^*B'\).
The [omitted-unitary transport](../claims/Yin_C_F0226_v1.md#transport-at-the-distinguished-coordinate) gives a normalized actual derivation at the twisted \(B'\) coordinate with vacuum \((A')^*\xi_{B'}\).
On the scalar star algebra of \(W\), its values lie in the scalar coarse space by the inverse rule for \(W^*=W^{-1}\), and its actual vacuum is the projection of \((A')^*\xi_{B'}\) to \(L^2(W^*(W))\).
For \(0<r\le1/2\), \(\lambda\in\mathbb T\), \(\rho=1-r\) and \(R=(1-\rho\bar\lambda W)^{-1}\), the geometric series and its differentiated series converge in the graph.
The derivative \(\rho\bar\lambda R\otimes R\) gives \(\rho|\tau R|^2\le\|\xi_{B'}\|_2\|R\|_2\).
The identity \(|1-\rho\bar\lambda W|^2=r^2+\rho|W-\lambda|^2\) gives
\[
 m_r=\tau(1_{[0,r]}(|W-\lambda|))\le(1+\rho)r^2\|R\|_2^2,\qquad
 \operatorname{Re}\tau R=\tfrac12(1+(1-\rho^2)\|R\|_2^2).
\]
Combining these estimates yields \(m_r^{3/2}/r\le4\|\xi_{B'}\|_2/(\rho\sqrt{1+\rho})\le8\|\xi_{B'}\|_2\).
Suppose a projection \(e\) of trace \(m>0\) in a common ambient tracial algebra satisfies \(\|(W-\lambda)e\|_2\le\eta\sqrt m\), where \(0<\eta\le1/4\).
Then \(m_{2\eta}\ge3m/4\) by testing \(|W-\lambda|^2\ge4\eta^2 1_{(2\eta,\infty)}(|W-\lambda|)\) against \(e\).
In particular \(\|\xi_{B'}\|_2\ge (3m/4)^{3/2}/(16\eta)\), independently of which star algebra the perturbed pair generates.
Thus perturbing the two midpoint unitaries while retaining either approximate half-trace atom cannot give the bounded vacua required in a separating sequence.

<a id="positive-phase-concentration-integral"></a>
## Cubic concentration with a small positive radial phase

Keep the actual normal tuple, distinguished vacuum \(\xi\), and fixed family of omitted shifts \(\mathcal G\) from the [cubic concentration theorem](../claims/Yin_C_F0261_v1.md#statement).
Write \(Z-b=U_bP_b\), let \(\mu_b\) be the law of \(P_b\), and set \(F(r)=\sup_{b\in\mathcal G}\mu_b([0,r])\).
Take the empty supremum to be zero.
With \(a_s(v)=sv/(v^2+s^2)\) and the [compressed marginal phase](../claims/Yin_C_F0229_v1.md#the-integrated-phase-defect) \(m_b\), suppose that a single \(\rho\ge0\) satisfies
\[
  \operatorname{Re}\iint a_s(v)a_s(w)m_b(v,w)\,d\mu_b(v)d\mu_b(w)
       \le \rho\left(\int a_s(v)\,d\mu_b(v)\right)^2
          \qquad(b\in\mathcal G,\ s>0).                                           \tag{P1}
\]
Define
\[
    k(y)=\frac{y^2-1}{(1+y^2)^2}\quad(y\ge1),\qquad
    K=\int_1^\infty k(y)y^{2/3}\,dy,\qquad B_\lambda=(1+\lambda^{-2})\lambda^{2/3}
                        \quad(\lambda\ge1).
\]
If \(B_\lambda K\sqrt\rho<1\), there is an absolute \(C\) such that
\[
     \int_0^\infty F(r)^3\,\frac{dr}{r^3}
       \le C\left(\frac{B_\lambda}{1-B_\lambda K\sqrt\rho}\right)^4\|\xi\|_2^2 . \tag{P2}
\]
The condition includes \(\rho<1/36\) at \(\lambda=1\), since \(k(y)<y^{-2}\) gives \(K<3\).
The factor \(B_\lambda=\lambda^{2/3}+\lambda^{-4/3}\) reaches its minimum on \([1,\infty)\) at \(\lambda=\sqrt2\), by differentiation.
The bound \(K<3\) alone then includes \(\rho<4/(81\sqrt[3]{4})\).

For the proof put \(v=|\xi|^*\), the decreasing rearrangement of the singular values of \(\xi\), \(H(t)=\int_0^t v(u)\,du\), and \(D(s)=\int_s^\infty H(F(x))\,dx/x^2\).
For each shift the [original vacuum resolvent identity](../claims/Yin_C_F0261_v1.md#nonpositive-radial-phase-on-a-fixed-shift-family) has left side \((\int h_s\,d\mu_b)^2\), where \(h_s(t)=s^2/(s^2+t^2)\).
Its first term is \(s^2\operatorname{Re}\langle\xi,U_bP_b(P_b^2+s^2)^{-1}\rangle\).
The test has operator norm at most \(1/s\), and the trace of its singular values above \(y>0\) is at most \(F(1/y)\).
The [vacuum rearrangement bound](../claims/Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) bounds this term above by \(s^2D(s)\).
Estimate the second term by (P1), take a square root, and put \(s=\lambda r\).
Since \(h_{\lambda r}\ge(1+\lambda^{-2})^{-1}\) on \([0,r]\), this gives
\[
 \mu_b([0,r])\le(1+\lambda^{-2})\left(s\sqrt{D(s)}
                      +\sqrt\rho\int a_s\,d\mu_b\right).
\]
One has \(\int_t^\infty k(y)\,dy=t/(1+t^2)\) for \(t\ge1\).
Hence \(\int_1^\infty k(y)1_{\{v\le sy\}}dy=a_s(v)\) for \(v\ge s\), and equals \(1/2\ge a_s(v)\) for \(v\le s\).
Integration against \(\mu_b\), followed by the supremum over shifts, yields
\[
 F(r)\le(1+\lambda^{-2})\left(\lambda r\sqrt{D(\lambda r)}
               +\sqrt\rho\int_1^\infty k(y) F(\lambda r y)\,dy\right).         \tag{P3}
\]

For \(\varepsilon>0\), write \(I_\varepsilon=\int_\varepsilon^\infty F(r)^3\,dr/r^3\) and \(J_\varepsilon=\int_\varepsilon^\infty H(F(r))^{3/2}\,dr/r^{3/2}\).
These are finite as \(F\le1\) and \(H\le\|\xi\|_2\).
In \(L^3([\varepsilon,\infty),dr/r)\) the norm of \(r^{-2/3}F(r)\) is \(I_\varepsilon^{1/3}\).
For any \(c\ge1\) the norm of \(r^{-2/3}F(cr)\) there is \(c^{2/3}I_{c\varepsilon}^{1/3}\le c^{2/3}I_\varepsilon^{1/3}\).
Minkowski therefore bounds the scaled integral term of (P3) by \(B_\lambda K\sqrt\rho\,I_\varepsilon^{1/3}\).
For the first term use
\[
 s^{2/3}D(s)=\int_1^\infty u^{-2/3}\frac{H(F(su))}{(su)^{1/3}}\,\frac{du}{u}.
\]
Minkowski in \(L^{3/2}([\lambda\varepsilon,\infty),ds/s)\) bounds the norm of this expression by \((3/2)J_\varepsilon^{2/3}\), since \(su\) ranges only over radii at least \(\varepsilon\).
Taking the square root gives the first term of (P3), after scaling by \(r^{-2/3}\), a norm at most \(\sqrt{3/2}\,B_\lambda J_\varepsilon^{1/3}\).
The [layer and Hardy calculation](../claims/Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) for these same \(F,v\) gives \(J_\varepsilon\le 3(2I_\varepsilon/3)^{1/4}\sqrt2\,\|\xi\|_2^{3/2}\), independently of the radial phase.
Thus \((1-B_\lambda K\sqrt\rho)I_\varepsilon^{1/3}\le C_1B_\lambda I_\varepsilon^{1/12}\|\xi\|_2^{1/2}\) with an absolute \(C_1\).
For \(I_\varepsilon>0\) division and the fourth power yield (P2) at the truncated lower limit, and monotone convergence gives the full result.

The [scalar radial models](Yin_D_F0003.md#sharp-scalar-limits-of-radial-vacuum-tests-at-an-omitted-shift) also quantify a limitation of this proof.
For \(1/2<\alpha<2/3\) those laws have \(F(r)=r^\alpha\) on \((0,1)\) and constant compressed phase \(\rho_\alpha=(B_\alpha-A_\alpha)/(B_\alpha+A_\alpha)\), with the integrals defined there.
In fact \(B_\alpha=\pi/\sin(\pi\alpha)\) and \(A_\alpha=-\pi\cot(\pi\alpha)\).
To see both signs, integrate \(z^{\alpha-1}/(1+z)\) on a positively oriented slit annulus about the positive real axis with \(\arg z\in(0,2\pi)\).
The two bank integrals converge to \((1-e^{2\pi i\alpha})B_\alpha\), the inner and outer circles vanish, and the residue at \(-1\) gives \(2\pi i e^{i\pi(\alpha-1)}\).
With \(1-z\) in the denominator instead, indent the banks at \(1\) by clockwise semicircles of radius \(\epsilon\), excluding the pole and enclosing no others.
The small arcs on the two banks contribute \(i\pi(1+e^{2\pi i\alpha})\) in the limit.
The principal value \(I=\operatorname{pv}\int_0^\infty t^{\alpha-1}/(1-t)\,dt\) therefore satisfies \((1-e^{2\pi i\alpha})I+i\pi(1+e^{2\pi i\alpha})=0\), yielding \(I=\pi\cot(\pi\alpha)\).
Inversion above one gives \(I=-A_\alpha\); replacing the lower cutoff \(1-\epsilon\) by \(1/(1+\epsilon)\) changes the integral by \(O(\epsilon)\).
Consequently \(\rho_\alpha=\cot^2(\pi\alpha/2)\downarrow1/3\) as \(\alpha\uparrow2/3\).
The cubic integral for these abstract tests diverges since \(3\alpha-3<-1\).
Thus a uniform allowance \(\rho>1/3\) in (P1) permits abstract radial data with all the stated radial vacuum pairings and divergent cubic concentration.
These data have no established realization by an actual normal tuple and omitted shift.
For arbitrary actual shifts the positive phase has only its contraction bound; (P1) with the smaller quantitative coefficient remains an additional assumption.
The [sharp uniform estimate](../claims/Yin_C_F0261_v2.md#decision-reviewed) subsequently extends this absorption argument to every coefficient strictly below \(1/3\) by averaging the signed kernels over scales.
At equality its scalar endpoint example represents all \(C^1\) radial tests while the integral diverges logarithmically.

<a id="weak-fourth-moment-gaussian-density"></a>
## The weak fourth-moment endpoint for the mixed Gaussian column

Consider the two-disk pair of [C0259](../claims/Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square).
Write \(N=W^*(Z)\), \(D=W^*(T)\), \(q=\mu(D_1)=3/8\), \(f=1_{D_1}\), \(e_r=1_{\{|z|\le r\}}\), and \(m(z)=\sqrt{|z|}/2\) on \(D_0\).
The [full-algebra density](../claims/Yin_C_F0263_v1.md#right-creation-and-the-explicit-density) \(d_*=(\xi^2+h)/(2\|\xi\|_2^2)\), \(h=\mathbb E_N(\xi^2)\), dominates the canonical right slice \(E=(\mathrm{id}\otimes\tau)\delta_T\) on every original mixed column.
On this fixed pair \(d_*\) belongs to weak \(L^4(M)\), and every density \(d\) with \(\|Ep\|_2^2\le C^2\tau(dp^*p)\) on the polynomial core satisfies
\[
 \inf_{0<t\le 3/32}t^{-3/4}\int_0^t\mu_d(u)\,du
       \ \ge\ \frac{5q^2}{8C^2}(32/3)^{3/4}.                           \tag{W1}
\]
Here \(\mu_d\) is the decreasing rearrangement of \(d\ge0\) for the normalized trace.

To prove (W1), set \(B_r=fT e_r T f\) and \(s_r=\int_{e_r}m\,d\mu=r^{5/2}/4\), by polar integration for \(0<r\le1\).
The [two compressed creation bounds and original polynomial tests](../claims/Yin_C_F0263_v1.md#the-two-disk-pair-and-its-cutoffs) give
\[
 \tau(B_r)=q s_r,\qquad
 \|e_rTf\|\le\sqrt{s_r}+\sqrt{q\sqrt r/2}\le r^{1/4},\qquad
 C^2\tau(dB_r)\ge q^2(5/8)r^2 .
\]
For \(V=B_r/\sqrt r\) one therefore has \(0\le V\le1\) and \(\tau(V)=(3/32)r^2\).
Integrating \(\tau(1_{(y,\infty)}(d)V)\le\min(\tau(1_{(y,\infty)}(d)),\tau(V))\) over \(y>0\) gives \(\tau(dV)\le\int_0^{\tau(V)}\mu_d(u)\,du\), which proves (W1).
In particular a dominating density cannot satisfy \(u^{1/4}\mu_d(u)\to0\) at zero, since this would make the integral in (W1) \(o(t^{3/4})\).
This excludes all \(L^{4,j}\) with \(1\le j<\infty\), since monotonicity bounds \(u^{j/4}\mu_d(u)^j\) by a constant times \(\int_{u/2}^u(v^{1/4}\mu_d(v))^j\,dv/v\).

For the endpoint upper bound, the [reciprocal-kernel decomposition](../claims/Yin_C_F0263_v1.md#integrability-of-the-full-algebra-density) gives \(\xi=K+gSf+fSg\), with \(K\) bounded, \(S\) standard semicircular and \(g=1_{D_0}m^{-1/2}\).
The projection \(P_L=1_{\{g>L\}}\) has trace at most \(10L^{-8}\), by \(g=\sqrt2|z|^{-1/4}\) on \(D_0\).
Replacing \(g\) by \(g1_{\{g\le L\}}\) leaves a bounded part of norm at most \(\|K\|+4L\).
The two discarded terms each have right support of trace at most \(\tau(P_L)\), since the first has left support under \(P_L\), the second has right support under \(P_L\), and polar decomposition equates the two support traces.
On the intersection of their kernels the original \(\xi\) is thus bounded by \(\|K\|+4L\).
The spectral projection of \(|\xi|\) strictly above this bound has trace at most \(2\tau(P_L)\), since any projection of larger trace meets that intersection nontrivially.
This proves \(\tau(1_{(\lambda,\infty)}(\xi^2))=O(\lambda^{-4})\) at infinity.
The same bound holds for \(h\) because it is bounded on \(D_1\) and at most \(1+q/m\) on \(D_0\).
Intersect the spectral cutoffs of \(\xi^2\) and \(h\) at level \(\lambda\).
On this intersection their sum has norm at most \(2\lambda\), with complementary trace \(O(\lambda^{-4})\), proving \(d_*\in L^{4,\infty}(M)\).

There is also a uniform obstruction for products of marginal weights.
For \(v\in L^2(N)\), \(w\in L^1(D)_+\), let \(d_{v,w}=yy^*\) with \(y=v\sqrt w\in L^2(M)\).
The relative Wick basis \(U_n(T)\) of \(L^2(D)\) lies in degree \(n\), so \(\mathbb E_D(u)=\tau(u)1\) for bounded \(u\in N\) by orthogonality to every positive degree.
By truncation, \(\mathbb E_D(|v|^2)=\|v\|_2^2 1\).
For bounded \(v\in N\), \(b\in D\) the trace identity gives \(\|vb\|_2=\|v\|_2\|b\|_2\).
Applying it to differences of bounded truncations of either factor gives the stated \(L^2\) product as their joint limit, with \(\tau(d_{v,w})=\|v\|_2^2\tau(w)\).

For bounded \(v\), put \(j=fv\).
The degree-zero and degree-two projections of \(j^*T e_r Tj\) onto \(L^2(D)\) give
\[
 \mathbb E_D(j^*T e_r Tj)=A+B(T^2-1),\qquad
 A=s_r\int_{D_1}|v|^2\,d\mu,\qquad
 B=\left(\int_{e_r}m^2\,d\mu\right)\left|\int_{D_1}v\,d\mu\right|^2 .
\]
Indeed the scalar coefficient integrates \(|j(z)|^2a(z,x)^2e_r(x)\), and pairing the two-edge path \(\overline{j(z)}a(z,x)e_r(x)a(x,y)j(y)\) with \(U_2(T)\) replaces both edge factors by \(a^2\).
On the two cross rectangles each squared edge equals \(m(x)\).
Since \(m\le1\) and \(|\int_{D_1}v|^2\le q\int_{D_1}|v|^2\), one has \(0\le B\le A\).
The spectrum of \(T^2-1\) lies in \([-1,3]\), giving \(\tau(d_{v,w}B_r)\le4s_r\tau(d_{v,w})\), first for bounded factors and then by the \(L^2\) product convergence and boundedness of \(B_r\).
The normalized states from these products include every probability density in either marginal by taking \(v=1\) or \(w=1\).
Their closed convex hull in \(\sigma(M^*,M)\) still satisfies \(\varphi(B_r)\le4s_r\) for each fixed \(r\).
Even a singular state in this hull fails on the original polynomial core.
Indeed take a continuous \(0\le u_r\le e_r\) equal to one on \(e_{r/2}\), so \((u_rTf)^*(u_rTf)\le B_r\).
Both \(u_r\) and \(f\) are continuous on the compact two-disk support and hence uniformly approximable by starred polynomials in \(Z\).
For the approximants \(p_n=u_nTv_n\), the outputs \(Ep_n=u_n\tau(v_n)\) converge in norm to \(q u_r\), and \(p_n^*p_n\) converges in norm to \((u_rTf)^*(u_rTf)\), allowing testing against any state.
Domination on the core would force \(q^2(5/32)r^2\le C^2\varphi(B_r)\le4C^2s_r=C^2r^{5/2}\) at every scale.

<a id="radial-disk-weights"></a>
## Radial dominating weights on a disk and its free extensions

For normalized area measure \(\mu=dA/\pi\) on the unit disk, let \(E\) be the right slice of the normal coordinate \(Z(z)=z\).
The [disk indicator estimate](../claims/Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) forces logarithmic growth in the mass of a dominating weight near the origin.
The full test on radial weights requires a stronger exponent.
For \(D(|z|)\in L^1(\mu)_+\), there is a finite \(C\) with
\[
                  \|Ep\|_2^2\le C^2\int|p|^2D\,d\mu
                   \qquad(p\in\mathbb C[Z,Z^*])
\]
if and only if, for some \(a>0\),
\[
   D(r)\ge a r^2\quad\text{almost everywhere},\qquad
   H_D:=\sup_{0<r<1}\log(1/r)\int_0^r\frac{s}{D(s)}\,ds<\infty .        \tag{D1}
\]
In particular \(D_\alpha(r)=r^2(\log(e/r))^\alpha\) dominates exactly for \(\alpha\ge2\).

Write \(\mathcal C f(z)=\int f(w)/(z-w)\,d\mu(w)\) for the unbarred Cauchy transform.
On the original core one has \(E f=\bar z f-\mathcal C f\) by the disk calculation in C0267.
The kernel \(1/|z-w|\) has uniformly bounded integrals in either variable, so \(\mathcal C\) extends continuously on ordinary \(L^2(\mu)\) by Cauchy–Schwarz in the integration variable followed by Fubini.
The pointwise multiplier necessity in [C0267](../claims/Yin_C_F0267_v1.md#localizing-the-multiplier-part) gives \(D\ge C^{-2}r^2\) for any dominating \(D\).
With this condition, multiplication by \(\bar z\) is bounded from \(L^2(D\mu)\) to \(L^2(\mu)\), so the remaining question is boundedness of \(\mathcal C\) between the same spaces.
To test (or extend) the core inequality on bounded Borel functions one can approximate by starred polynomials in \(L^2((1+D)\mu)\), using both operator bounds and the ordinary \(L^2\) realization just given.

For a bounded angular mode \(f(se^{it})=h(s)e^{int}\), geometric-series integration in \(t\) gives a single output mode \(e^{i(n-1)\phi}\) at \(z=re^{i\phi}\).
Its radial coefficient is
\[
 \begin{cases}
  \displaystyle\frac{2}{r}\int_0^r (s/r)^{-n}h(s)s\,ds, & n\le0,\\[4pt]
  \displaystyle-2\int_r^1 (r/s)^{n-1} h(s)\,ds, & n\ge1 .
 \end{cases}                                                            \tag{D2}
\]
The expansions are valid for each \(s\ne r\), and the original disk kernel is absolutely integrable for each \(z\) and bounded input.
Distinct input modes thus give orthogonal output modes.
In absolute value each nonpositive mode is dominated by the radial Hardy operator of mode zero applied to \(|h|\).
Each positive mode is dominated by \(2\int_r^1 |h(s)|\,ds\).
Writing \(F(r)=\int_r^1 |h(s)|\,ds\), integration by parts for bounded \(h\) gives
\[
 \int_0^1 F(r)^2r\,dr=\int_0^1 r^2F(r)|h(r)|\,dr
 \le\left(\int_0^1 F^2 r\,dr\right)^{1/2}
     \left(\int_0^1 |h|^2r^3\,dr\right)^{1/2}.
\]
The first condition in (D1) therefore handles all positive modes.

For mode zero put \(V(r)=\int_0^r s/D(s)\,ds\).
Dropping the fixed numerical factors in (D2) and the area measure leaves the inequality
\[
    \int_0^1\left|\int_0^r h(s)s\,ds\right|^2\frac{dr}{r}
             \le K\int_0^1 |h(s)|^2D(s)s\,ds .                          \tag{D3}
\]
For \(h(s)=1_{\{s<r_0\}}\min(D(s)^{-1},m)\), the left side is at least \(\log(1/r_0)(\int_0^{r_0}h(s)s\,ds)^2\), whereas the input norm squared is at most \(\int_0^{r_0}h(s)s\,ds\).
Letting \(m\) tend to infinity proves \(H_D\le K\).

Conversely, suppose \(H_D<\infty\).
Then \(0<V(r)<\infty\) for \(0<r<1\), \(V\) tends to zero at zero, and \(V'(s)=s/D(s)\) almost everywhere.
Cauchy–Schwarz gives
\[
 \left(\int_0^r |h(s)|s\,ds\right)^2
 \le 2\sqrt{V(r)}
       \int_0^r |h(s)|^2D(s)s\sqrt{V(s)}\,ds ,
\]
since \(\int_0^r V'(s)/\sqrt{V(s)}\,ds=2\sqrt{V(r)}\).
The bound \(V(r)\le H_D/\log(1/r)\) gives, for \(0<s<1\),
\[
 \int_s^1\sqrt{V(r)}\,\frac{dr}{r}
 \le 2\sqrt{H_D\log(1/s)}\le \frac{2H_D}{\sqrt{V(s)}} .
\]
Interchanging the nonnegative integrals proves (D3) with \(K=4H_D\).
These estimates control all finite angular sums by orthogonality since \(D\) is radial, in particular every starred polynomial.
For \(D_\alpha\), one has \(V(r)=\int_{\log(e/r)}^\infty u^{-\alpha}du\).
It is infinite for \(\alpha\le1\) and otherwise equals \((\log(e/r))^{1-\alpha}/(\alpha-1)\).
Thus \(H_{D_\alpha}<\infty\) precisely for \(\alpha\ge2\), and those weights also satisfy the pointwise condition.

Adjoin any finite family of freely independent actual normal coordinates free from \(Z\), including for example one Haar unitary.
For the expanded tuple and the distinguished coordinate \(Z\), each original mixed starred polynomial \(p\) has the finite orthogonal right-module expansion \(p=\sum_u u b_u\).
The [right-module decomposition](../claims/Yin_C_F0160_v1.md#2-right-modules-and-the-actual-adjoint) gives \(E_{\rm mixed}p=\sum_u u E b_u\) and \(\mathbb E_{W^*(Z)}(p^*p)=\sum_u |b_u|^2\).
Therefore
\[
       \|E_{\rm mixed}p\|_2^2=\sum_u\|E b_u\|_2^2
                    \le C^2\sum_u\int D|b_u|^2\,d\mu
                    = C^2\tau(Dp^*p).
\]
Restriction to marginal polynomials recovers the scalar inequality with the same constant.
Thus the least constant for a given marginal weight agrees on both cores, and (D1) and the \(\alpha=2\) endpoint characterize these radial weights even on the full mixed core.
For a general correlated actual tuple with this disk marginal, a mixed weight whose conditional expectation onto the disk is radial must still satisfy (D1) after compression by the pure polynomial tests.

<a id="mixed-spectral-localization-at-divergent-shifts"></a>
## Mixed tests at the spectral concentration point

Suppose the cubic envelope diverges for a fixed family of omitted shifts at the normal coordinate \(Z\), in the setting of the [two-resolvent concentration theorem](../claims/Yin_C_F0269_v1.md#statement).
Along a suitable sequence of nearly maximizing shifts, both marginal spectral distributions of \(a_s(P)\), before and after polar conjugation, have asymptotically all their mass near the same point \(z_0\).
These distributions are normalized by \(H=\tau(h_s(P))\), and their total mass need not be one.
This stronger localization permits arbitrary bounded tests from the ambient algebra on either side of a fixed function of \(Z\).

To choose the scales, set \(J(s)=\int_1^\infty F(su)du/u^2\) and use the probability proportional to \(F(s)^3ds/s^3\) on \([\varepsilon,\infty)\) from the [simultaneous scale selection](../claims/Yin_C_F0269_v1.md#simultaneous-choice-of-scales).
Its mass is normalized by \(I_\varepsilon\to\infty\).
For every integer \(j\ge0\),
\[
 \frac1{I_\varepsilon}\int_\varepsilon^\infty
                  \frac{J(2^js)^3}{s^2}\,\frac{ds}{s}\le 27\,2^{2j},
\]
by the same Minkowski estimate followed by the dilation \(s\mapsto2^js\).
Fix \(2/3<\beta<1\).
The probability that \(J(2^js)>C2^{\beta j}F(s)\) for at least one \(j\ge0\) is bounded by \(27 C^{-3}\sum_{j\ge0}2^{(2-3\beta)j}\).
Choose \(C\) large enough that this probability is less than \(1/4\).
The probability of \(F(s)\le s^{3/4}\) on \(s<1\) tends to zero since its unnormalized mass is at most \(\int_0^1 s^{1/4}ds/s<\infty\).
The simultaneous choice of scales for finitely many adjoint tests at each stage still works under both extra conditions, by taking \(\varepsilon\) sufficiently small.
Thus along a decreasing sequence \(s\to0\) one has the two limiting point masses of that theorem together with
\[
          H\ge F(s)/4>s^{3/4}/4,\qquad
          J(2^js)\le C2^{\beta j}F(s)\quad(j\ge0).
\]
The change of the numerical upper bound at \(j=0\) only changes the uniform variation constant in its compactness proof.

For \(v\le2^m s\) one has \(a_s(v)=(v/s)h_s(v)\le 2^m h_s(v)\).
For \(v>2^ms\) use \(a_s(v)\le s/v\) and sum over the dyadic bands \(2^j s<v\le2^{j+1}s\).
Writing \(P=|Z-b|\), this gives
\[
 \frac{\tau(a_s(P)1_{\{P>2^ms\}})}{H}
   \le \frac{1}{H}\sum_{j\ge m}2^{-j}F(2^{j+1}s)
   \le 4 C 2^\beta\sum_{j\ge m}2^{-(1-\beta)j}.
\]
Here \(F(t)\le J(t)\) by monotonicity.
The same tail estimate holds after conjugation by the polar \(U\) of \(Z-b\).
For each fixed \(m\) the first band is bounded by a constant times the corresponding \(h_s\) marginal measure at \(Z\), which converges after normalization to \(\delta_{z_0}\).
Taking \(m\) to infinity establishes concentration of the normalized positive measures for \(a_s(P)\) and \(Ua_s(P)U^*\) outside every neighborhood of \(z_0\).
Since the total masses \(\tau(a_s(P))/H\) are bounded, a subsequence gives the same multiple of \(\delta_{z_0}\) for their two weak limits.

Regard \(R_s(p)=\tau(ph_s(P))/H\) and \(L_s(p)=\tau(pUh_s(P)U^*)/H\) as states on \(M\), and put \(G_s(p)=\tau(pUa_s(P))/H\).
For every \(c\in C(\sigma(Z))\) put \(c_0=c(z_0)\).
For \(\Lambda_s=R_s,L_s,G_s\) the preceding localization yields
\[
 \sup_{\|p\|\le1}\big|\Lambda_s((c(Z)-c_0)p)\big|\longrightarrow0,\qquad
 \sup_{\|p\|\le1}\big|\Lambda_s(p(c(Z)-c_0))\big|\longrightarrow0.
\]
For the two positive states this follows by Cauchy–Schwarz since \(\Lambda_s(|c(Z)-c_0|^2)\to0\).
For \(G_s\), write \(a=a_s(P)\) and \(G_s(p)=H^{-1}\langle\sqrt a,pU\sqrt a\rangle\).
The difference on the left edge is bounded by
\((\tau(a|c(Z)-c_0|^2)/H)^{1/2}(\tau(a)/H)^{1/2}\).
The bound on the right edge uses \(UaU^*\) in the first factor instead.
These bounds follow from the Hilbert norms of the two polar vectors, uniformly over the operator unit ball.
Consequently the limiting functionals on any fixed separable \(C^*\)-subalgebra containing \(Z\), obtained by subsequence compactness, evaluate spectral functions at \(z_0\) at either edge of a mixed product.

There is a further restriction for a fixed shift \(b\).
Use the \(C^*\)-algebra generated by the original tuple and \(b\), and write \(\Lambda_R,\Lambda_L\) for any limits of \(R_s,L_s\) on this algebra along the selected sequence.
Since \(P^2 h_s(P)=s^2(1-h_s(P))\),
\[
 R_s((Z-b)^*(Z-b))=L_s((Z-b)(Z-b)^*)=s^2(1-H)/H\longrightarrow0 .
\]
The Hilbert seminorm triangle inequality in the two states and convergence of their \(Z\)-marginals now give
\[
  \Lambda_R((b-z_0)^*(b-z_0))=0,\qquad
  \Lambda_L((b-z_0)(b-z_0)^*)=0.
\]
In particular \(z_0\in\sigma(b)\), since invertibility would bound the first tested positive element below by a strictly positive scalar.
For normal \(b\), both limiting states therefore evaluate spectral functions of \(b\) at the same point at both edges of mixed products, by Cauchy–Schwarz and continuous functional calculus.
These bounds concern each endpoint of a product; an intervening arbitrary operator may move the tested vectors into other spectral regions.
The [disk pair with a common character](../claims/Yin_C_F0275_v1.md#statement) realizes this edge condition at the origin with every marginal secant direction, while the chosen nonnormal residual has singular mass asymptotic to the square of the radius.

<a id="local-critical-shell-integrals"></a>
## Cubic concentration restricted to the singular shells at one marginal point

Let \(Z\), the family of shifts, \(F,H,A\), and the local angular spread \(e(z)\) have the meanings of the [local secant theorem](../claims/Yin_C_F0273_v1.md#statement).
If the full cubic integral diverges, there is a single \(z_0\) with \(e(z_0)\ge 2(\sqrt{1+24^{-2}}-1)\) such that for every neighborhood \(O\) of \(z_0\) and every \(d>0\) the integral still diverges on radii admitting a shift with both normalized hard marginal projection masses at least \(1-d\) on \(O\) and original singular mass at least \(F(s)/2\).
More precisely the restricted radii contain Borel sets of divergent cubic integral.
This strengthens the [single-sequence conclusion](../claims/Yin_C_F0269_v1.md#statement) to an integral on each neighborhood of the same point.

For \(y\in K=\sigma(Z)\), an open neighborhood \(O\) of \(y\) and \(d>0\), call a radius admissible for \((O,d)\) if it meets the two hard mass conditions just stated.
No measurability of a supremum over shifts is needed.
A set of radii is called negligible in this argument if it is contained in a Borel set of finite measure for \(\nu(ds)=F(s)^3ds/s^3\) on \((0,1)\).
Fix the positive constant \(e_*=2(\sqrt{1+24^{-2}}-1)\).
Suppose that each point \(y\) with \(e(y)\ge e_*\) has some \(O_y,d_y\) whose admissible radii are negligible.
The set \(C=\{y:e(y)\ge e_*\}\) is compact.
Indeed, if \(e(y)<a\) then there is a unit scalar \(\lambda\) and a neighborhood where every chord phase has distance strictly below \(a\) from \(\lambda\) with a uniform gap; the same bound holds at every point of a smaller neighborhood.
Compactness of the phase circle proves this assertion by taking successively smaller balls as in the proof of the local secant theorem.
Cover \(C\) by finitely many such \(O_y\), and discard from \((0,1)\) the finite union of their Borel supersets of finite \(\nu\)-measure.
The remaining Borel set still has infinite \(\nu\)-measure.
Run the [simultaneous scale selection](../claims/Yin_C_F0269_v1.md#simultaneous-choice-of-scales) including the [dyadic tail requirements](../claims/Yin_C_F0273_v1.md#concentration-of-the-complex-measures-in-total-variation-away-from-the-point).
The discarded radii have probability tending to zero under the original normalized truncated measure, so all chosen radii may be taken in the remainder.
The resulting concentrating point lies in \(C\) by the same local trace proof.
For an open set of the finite cover containing this point, both hard probabilities eventually exceed \(1-d_y\), contradicting the choice of the remaining radii.
The case \(C=\varnothing\) is already excluded by the local secant theorem.
It follows that for some \(z_0\in C\) every one of its indicated admissible sets fails to be negligible.

For completeness these admissible sets contain measurable subsets of infinite integral.
The fixed family of shifts need not be Borel.
Use intervals immediately to the right of each admissible radius for relaxed mass requirements.
For fixed \(b\), the right hard projections decrease strongly to the projection at \(s\) as the radius decreases to \(s\), and polar conjugation gives the same convergence for the left hard projections.
The mass \(F\) is monotone and hence has at most countably many discontinuities.
At a continuity radius with a witness having trace at least \(F(s)/2\), the trace need not exceed half the envelope strictly.
Use the selection above with the stronger near-maximality level \(3F(s)/4\), possible whenever \(F(s)>0\) and leaving all bounds unchanged.
Likewise use neighborhood error \(d/2\) before relaxing to \(d\).
The same finite-cover argument gives a single point for which every stronger admissibility set fails to be negligible.
Removing the countable set of discontinuities preserves this property.
For each remaining stronger radius there is a nontrivial half-open interval to its right on which the same witness fulfills the relaxed conditions.
The interior of their union is a countable union of open intervals.
Every included point outside the interior is the left endpoint of an interior component, so the entire union is Borel.
Thus the relaxed admissible set contains a Borel superset of the stronger set of radii, which by construction has infinite \(\nu\)-measure.
The argument needs only monotonicity and right continuity of the hard spectral measures for each shift.

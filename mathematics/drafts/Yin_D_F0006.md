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
The actual tensor-adjoint formula in [Mai15-U001 v2](../audits/literature/Mai15/Yin_U001.md#mai15-u001) places \(P\odot P\) in the adjoint domain.
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

For a complex-linear \(T:P\to H\), consider the following stronger finite-family condition with one constant C:
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
Primary-source attribution for the abstract finite-family domination equivalence has not been checked and remains outstanding before any fixed reusable Claim publication.
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

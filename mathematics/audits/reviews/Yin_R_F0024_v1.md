---
author: Yin
---

# Independent review: measurable angular densities

Date/reviewer: 2026-09-11, the reviewing agent.

Target: [measurable-density continuation](../../claims/Yin_C_F0049_v1.md).


**Outcome: pass.**
The complete frozen artifact was read and independently recomputed.
No correction was requested.
This audit assigns no Claim ID or Role.

Preliminary collaboration: root proposed investigating measurable necessity and relayed the author's annular mechanism.
The reviewer checked that outline and sent normalization, graph-limit and vacuum-pairing observations before reading the complete artifact.
The author reports that this confirmation reached it after freezing.
The present audit includes the subsequent full review; prior interaction is disclosed.

## 1. Scope and dependencies

The result retains assumptions \(0<m\le b\le B\), angular mean one, compact radial support, and no atom at the origin.
Radius atoms are permitted.
It proves that the actual vacuum-adjoint condition is equivalent to \(A=(F_-+a/2)/r\) belonging to L2, with the constants in equations (4)--(5).
The C1 condition on b has been removed.

Only the measurable sufficient direction of [Yin_C_F0048](../../claims/Yin_C_F0048_v1.md#yin_c_f0048) is used on annuli.
[Yin_C_F0047](../../claims/Yin_C_F0047_v1.md#yin_c_f0047) makes its radial hypothesis automatic there.
[VV16-U001](../literature/VV16/Yin_U001_v1.md#vv16-u001) is used for C1 approximation of smooth cutoffs times polynomials, with the statement-level source inspection already recorded in the [Yin_C_F0048 review](Yin_R_F0022_v1.md).
No new external theorem, full source-proof audit, or Hilbert norm equivalence argument for transferring adjoints is introduced.

## 2. Finite measures and actual annular operators

For t=nu(V)>0, angular mean one gives mu(V)=t.
Normalizing both finite measures by this same t preserves the density b.
The normalized radial midpoint quantity is bounded by 1/a, since all radii in V exceed a.
The local premise does not depend on the unknown global L2 quantity being finite.

The unnormalized operator is t times its probability counterpart.
Its adjoint is likewise t times the probability adjoint; scaling the inner product by t does not otherwise change the adjoint or the domain.
Thus local bounded functions lie in both actual domains.
No uniform estimate as a tends to zero is needed.

For bounded f, uniformly bounded polynomial approximants converging in L2, followed by an almost-everywhere convergent subsequence, establish
\[
 F_{\mu,V}f=F_{\nu,V}(fb)-fF_{\nu,V}b.
\]
Both operator-output limits are identified by their own closed graphs.
The multiplication term converges strongly by dominated convergence.
Equivalent norms also allow comparison of the weak vector limits; they are not used to identify Hilbert adjoints.
This checks equation (8) for rough bounded f, beyond the polynomial identity.

## 3. Cutoffs and the original global graph

The smooth cutoff h has compact support K strictly inside V, hence positive distance d from V^c.
Both global and local actual operator values on hp equal their canonical integrals by the existing C1 graph approximation.
The original closure exists from the assumed global vacuum condition, without using the desired infinity-to-2 estimate.

\[
 E_\mu(hp)|_V=F_{\mu,V}(hp)+hp\,c_{\mu,V^c}
\]
and the exterior negative integral have the asserted signs.
The local bound and separated cross kernels yield equation (10).
In the multiplication term, c is only evaluated on K.
The exterior integral kernel is bounded on V^c times K and is therefore Hilbert--Schmidt as a map between the finite L2 spaces.

Uniformly bounded polynomials converging to f make hp_n converge strongly to hf.
Weak closedness of the original global graph gives hf in Dom(E_mu).
The internal local outputs converge weakly to their actual local value, while both cross maps converge strongly.
This identifies the full formula (9) for hf.
In particular the cutoff, not the rough f, is differentiated.
Choosing h=1 on the support of phi puts psi=φ/b into the original graph without approximating derivatives of b or 1/b.

## 4. Rotation of an actual closed graph

For \(R_s f(z)=f(e^{is}z)\), direct substitution verifies
\[
 F_{\nu,V}R_s=e^{is}R_sF_{\nu,V}.
\]
The sign is correct; polynomial-core invariance extends both the domain invariance and this identity to the actual closure.
It sends the frequency-one φ to a radial output.

Because b belongs to the actual annular domain, its rotated graph vectors are continuous in the graph norm: their two components are rotations of fixed L2 vectors.
Their Bochner average remains in the closed graph.
The input average is 1, and its operator value is zero.
Pairing against φ commutes with this average, and the phase cancellation makes the pairing independent of s.
Therefore
\[
 \int\phi F_{\nu,V}b\,d\nu_V=0.
\]
This verifies equation (15) without claiming a pointwise divided-difference formula for rough b or any weak-star continuity assertion.

The bounded-function transfer now proves the actual internal vacuum identity (16).
No global radial vacuum adjoint is assumed.

## 5. Cross terms, atomic midpoint and norm bound

In the integrated global formula, interchanging the separated exterior variables cancels its initial minus sign.
Hence the two cross contributions add, giving the factor 2 in equation (17).
The identity psi b=φ changes its outer measure to nu.

Simultaneous rotation preserves V and V^c.
The phase of φ cancels the kernel phase, and the angular average of b is one.
The distance d provides an absolutely integrable bound, so Fubini is legitimate.
Thus the global vacuum test equals the full radial integral of δφ.

That radial integral exists because φ is C1.
Its frequency-one calculation gives \(2\int A\chi\,d\sigma\), including the radius-atom contribution; it does not require A in L2 beforehand.
The actual global vacuum pairing now gives
\[
 2\left|\int A\chi\,d\sigma\right|
 \le m^{-1/2}\|\xi_\mu\|_\mu\|\chi\|_\sigma.
\]
Smooth annular tests are dense in L2(sigma), also for atomic sigma.
Local boundedness of A and exhaustion prove equation (4).
Substitution into Yin_C_F0048 sufficiency gives exactly equation (5), its vacuum formula and both original bounded-function domains.
There is no circular appeal to the desired necessity statement.

## 6. Positive tests and the retained boundary

The positive-kernel expression in equation (20) is checked.
For nonnegative chi increasing on the radial support interval, both terms in its numerator are nonnegative.
Smooth extensions outside that interval may be used for the C1 graph test.

The proposed cone does not detect the full L2 condition.
For sigma=beta r^(beta-1)dr with 1/2<beta<=2/3, A=r^(beta-1) belongs to L1 but not L2.
Its L1 norm is beta/(2beta-1).
Opposite monotonicity, justified also by bounded truncations, yields the stated cone estimate even in this case.
This is a failure of the test cone, not a counterexample satisfying the global vacuum premise.

The successful conclusion still requires the stated uniform angular comparison and angular mean condition.
The Yin_C_F0045 free-product consequence remains conditional on freeness.
General singular angular laws, correlated normal tuples and bounded rational reconstruction remain outside the conclusion.

## Actual review arrangement

Root relayed the author annular mechanism to this reviewer before the complete artifact was read; the reviewer sent normalization, graph-limit and vacuum-pairing observations after checking that mathematical outline. Shared substantive target development context makes the later full finding self-reviewed even though the author reports receiving the confirmation after freezing.
The original 2026-09-11 date, full mathematical findings, source depths and exact boundaries remain unchanged.
This maintenance performs no new mathematical review or context-isolation certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#6-positive-tests-and-the-retained-boundary) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#6-positive-tests-and-the-retained-boundary) | [C_F0049 statement](../../claims/Yin_C_F0049_v1.md#statement) | Whole six-section measurable angular-density vacuum equivalence and quantitative original-domain theorem: finite-measure annular normalization, rough inverse-density graph cutoffs, rotation of actual closed graph, midpoint identity with radius atoms and failure of the positive test cone. Exact uniform density comparison and freeness limits retained. |
| [Original finding](#6-positive-tests-and-the-retained-boundary) | [C_F0049 argument](../../claims/Yin_C_F0049_v1.md#2-canonical-operators-on-a-fixed-annulus) | Whole six-section measurable angular-density vacuum equivalence and quantitative original-domain theorem: finite-measure annular normalization, rough inverse-density graph cutoffs, rotation of actual closed graph, midpoint identity with radius atoms and failure of the positive test cone. Exact uniform density comparison and freeness limits retained. |

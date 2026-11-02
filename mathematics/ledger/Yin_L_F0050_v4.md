---
author: Yin
---
# Left contractions of bare normal duals: adjoint stability, normal L1 realizations and phase bounds

Date: 2026-10-14.
Human author Yin.
This fixed continuation follows the explicit request to prioritize the left-contraction bound for general normal generating tuples.
Root coordinated the separate mathematical branches and their fixed reviews.
This comparison is self-checked; the individual accepted arguments and their actual finding-specific review relationships are linked below.
The [previous comparison](Yin_L_F0050_v3.md) retains the earlier equivalence classes, and [v2](Yin_L_F0050_v2.md) retains the dense-domain comparison and earlier candidates.

## Target and retained inputs

Let (M,tau) be finite tracial, H=L2(M,tau), Omega=1, P=P_Omega, and let X=(X_1,...,X_d) be normal bounded generators.
Write A=C<X,X*>.

F(X) means existence of complex-linear D_i:M Omega -> H with [X_j,D_i]=delta_ij P on all bounded vectors, with no continuity or adjoint premise.
A(X) means the complete starred Hilbert-tensor derivation and actual-vacuum hypothesis of ACSY24 Proposition3.5.
The common maximal-Delta conclusions are retained in [C_F0024 Section3](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) and [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).

Assume F(X).
[C_F0069](../claims/Yin_C_F0069_v1.md#statement) and [C_F0070](../claims/Yin_C_F0070_v1.md#statement) already give unique starred derivations delta_i and bounded right contractions
\[
 R_i=(\mathrm{id}\otimes\tau)\delta_i:A\to H.
\]
The current target is boundedness of
\[
 L_i=(\tau\otimes\mathrm{id})\delta_i:A\to H
\]
for the operator norm on A.
[C_F0072](../claims/Yin_C_F0072_v1.md#statement) then gives the actual vacuum and both canonical full bounded-vector domains without a reality hypothesis.

This continuation establishes the exact reductions and sufficient conditions below.
It does not prove the left bound for every normal tuple, and supplies no rank-one dual counterexample.

## Exact algebraic reformulation: adjoint stability

[C_F0073](../claims/Yin_C_F0073_v1.md#statement), checked in the unknown-relationship [R_F0046 finding](../audits/reviews/Yin_R_F0046_v1.md#conclusion), proves under F(X)
\[
 \boxed{
 \text{all }L_i\text{ are bounded}
 \ \Longleftrightarrow\
 \exists R_i^{right}:M\Omega\to H,\
       [R_i^{right},\rho(X_j)]=\delta_{ij}P
 \ \Longleftrightarrow\ \mathsf F(X^*).
 }
\]
Thus the remaining estimate is exactly stability of the full-domain condition under taking the adjoint of every coordinate.

The algebraic conversion is delta_i#(a)=(delta_i(a*))^dagger, with (u tensor v)^dagger=v* tensor u*.
Its right contraction is J L_i J, and its left contraction is J R_i J.
Uniqueness of the starred derivation for a normal tuple gives one direction; C_F0072 and actual graph extension give the other.

Directly conjugating a supplied map by J gives a RIGHT dual for X*, rather than the needed right dual for X.
This is why the formal J operation alone does not settle the question.
The right normalization is R^0(a)=R(a)-R(1)a.

Separately, A(Y) if and only if A(Y*) holds for every bounded generating tuple, normal or not.
The actual vacuum transforms as xi -> xi*.
This symmetry of A is not a proof of the corresponding unresolved symmetry of F.

## Exact analytic reformulation: a specified normal L1 map

[C_F0132](../claims/Yin_C_F0132_v1.md#statement), checked in the unknown-relationship [R_F0138 finding](../audits/reviews/Yin_R_F0138_v1.md#conclusion), supplies a second formulation with an explicit map on all of M.

First one can choose UNIQUE normalized normal bounded maps E_i:M -> H with
\[
 E_i1=0,\qquad [E_i,X_j]=\delta_{ij}P,\qquad E_i|A=R_i.
\]
Here normal means ultraweak-to-weak continuity of the map, not merely normality of the generators.
The proof takes the normal bidual summand of an arbitrary supplied bounded map, then normalizes it.
The exact primary interface is retained in [Bla06-U002](../audits/literature/Bla06/Yin_U002.md#bla06-u002).
Uniqueness follows from the homogeneous normal-generator Fuglede argument, equality on the star core and normality.

For N_i=W*(X_j:j neq i), these representatives satisfy E_i(ba)=bE_i(a) and E_i(b)=0 for b in N_i.
This extra module property is legitimately extended from the polynomial core because these representatives are normal.

Define the actual L1 preadjoint by
\[
 \tau((E_i^\flat b)^*a)=\langle b,E_i(a)\rangle,
 \qquad \xi_i=E_i^\flat1\in L^1(M),
\]
and define on ALL of M
\[
 \boxed{G_i(b)=b\xi_i-E_i^\flat b.}
\]
Then G_i is normal and bounded M -> L1, vanishes at 1, and satisfies
\[
 [G_i,X_j^*]=\delta_{ij}P,\qquad
 [G_i,X_j]=\delta_{ij}K_i^*
\]
as L1 equalities.
On the star core it equals (L_i(b*))*, so its core values already lie in L2.

The complete proof gives
\[
 \boxed{
 \text{all }L_i\text{ are bounded}
 \ \Longleftrightarrow\
 G_i(M)\subseteq L^2(M)\ \text{for every }i
 \ \Longleftrightarrow\
 G_i:M\to L^2(M)\text{ is bounded for every }i.
 }
\]
For the range-to-bound direction, the L1 continuity makes the graph in M times L2 closed.
Thus it is enough to prove pointwise L2 membership on all bounded inputs; a quantitative norm estimate need not be supplied first.
The reverse direction uses the actual C_F0072 closures and uniqueness of normal representatives, not an arbitrary extension of the core.

As an elementary further reduction for continuation, testing every unitary input suffices for the range assertion.
Each bounded element is a finite complex linear combination of unitaries: split real and imaginary parts, scale to selfadjoint contractions b, and write b=(u+u*)/2 with u=b+i(1-b squared)^{1/2}.
Linearity then gives all bounded inputs; closed graph gives the uniform bound afterward.
This observation does not establish L2 membership for those unitary tests.

## A sufficient phase condition using bounded square sums

[C_F0131 PartA](../claims/Yin_C_F0131_v1.md#statement), checked in the unknown-relationship [R_F0139 finding](../audits/reviews/Yin_R_F0139_v1.md#conclusion), proves a usable general sufficient condition.

For the normal marginal law mu_i, write k_i(z,w)=(conjugate z-conjugate w)/(z-w).
Suppose
\[
 \overline{k_i(z,w)}=\sum_n a_{in}(z)b_{in}(w)
 \quad\text{almost everywhere},
\]
where a_in,b_in belong to W*(X_i), with
\[
 A_i^2=\left\|\sum_n|a_{in}|^2\right\|_\infty<\infty,
 \qquad
 B_i^2=\left\|\sum_n|b_{in}|^2\right\|_\infty<\infty.
\]
No uniform-norm decay of the square-sum tails is required.
Then, with C_i=||E_i||_{infinity to 2},
\[
 \|L_i(p)\|_2\le\frac4{\sqrt\pi}C_iA_iB_i\|p\|.
\]
In particular A(X) and both canonical domains follow.

The proof applies the accepted commutative little Grothendieck inequality to the map b -> E_i(p b) on the marginal algebra.
It makes the input vector sequence square summable.
The bounded output row of right multipliers then makes
\[
 Q_i(p)=\sum_n E_i(p b_{in})a_{in}
\]
strongly convergent in H for each p in M, with norm at most 2 C_i A_i B_i ||p||/sqrt(pi).
This is not operator-norm convergence of the finite maps.
Dominated convergence of the corresponding marginal HS kernels verifies both generator commutators.
Normalizing at 1 identifies the conjugate derivation on the entire star core.

This extends the earlier projectively summable coefficient mechanism of [C_F0039](../claims/Yin_C_F0039_v1.md#yin_c_f0039-p1), removes its closability premise and gives an actual L2 vacuum.
The exact difference is the countable coefficient/convergence condition, not an unsupported claim of inequivalence between finite commutative tensor norms.
The condition is not asserted to hold for every normal spectrum.

## A second sufficient condition: reversal symmetry

C_F0073 also proves that a trace-preserving complex-linear star antiautomorphism sigma:M -> M fixing every X_j supplies the left bound with the same constant as the right contraction.
Its Hilbert implementation conjugates left generator multiplication to right generator multiplication.
The resulting normalized right dual agrees with L_i on the star core.

The reduced-word reversal of a free product of the abelian marginal algebras gives this symmetry for freely independent normal coordinates.
Thus F(X) implies A(X) for every free normal tuple satisfying F(X), without a geometric spectral restriction.
This does not claim that arbitrary free normal laws have full-domain duals.

The general correlated case need not possess the required symmetry.
The result is a verified sufficient condition, not a general reversal construction from normality alone.

## Two shortcuts have been ruled out at their actual scope

### Arbitrary phase lifting on M-to-L2 maps

C_F0131 PartB gives finite commutative models with
\[
 \|E_n\|_{\infty\to2}\le\pi/\sqrt2,\qquad
 \|Q_{k_{x_n}}E_n\|_{\infty\to2}
 \ge\frac3{5\sqrt2}H_{n-1}\longrightarrow\infty.
\]
The spectrum consists of positive-real and positive-imaginary geometric sequences.
Its cross-block phase turns the uniformly bounded discrete Hilbert matrix into harmonic row sums.
The complete Fourier multiplier proof and normalized counting trace are fixed in the Claim.

The divergence persists after normalizing the input at 1 and normalizing the lifted output at 1.
Consequently a universal estimate based only on ||E||_{infinity to 2} and the modulus-one phase is false in the actual Banach norm relevant here.
This is stronger than importing the older B(H) Schur obstruction from [L_F0034](Yin_L_F0034_v1.md).

The finite atomic models do not satisfy the rank-one dual identities and are NOT counterexamples to F(X) implies A(X).

### Normality and a general HS commutator

C_F0132 PartD gives a diffuse commutative dyadic averaging operator E with E1=0, normal M-to-L2 boundedness, a closable polynomial restriction and an HS generator commutator.
Its induced polynomial derivation has bounded right contraction and an L1 vacuum density outside L2.
Its full-M conjugate implementation takes a particular bounded sign function outside L2.

The defining block lengths are ell_n=2^{-n}, epsilon_n=ell_n squared, and E f on I_n is the average of f on J_n minus f.
The actual density has block L2 square 1-ell_n, while the HS commutator has total squared norm bounded by sum ell_n.
These exact calculations separate the two requirements.

Here delta(x) is an HS kernel, not 1 tensor 1.
Therefore the example rules out replacing the special generator identities by general HS commutators.
It neither separates F from A nor supplies an atomic or nonclosable counterexample to the actual target.

## Remaining research obligation

The priority question remains unresolved for arbitrary correlated normal tuples.
The current exact target is to use the special rank-one commutators, normality and the other-coordinate module structure to prove
\[
 G_i(u)\in L^2(M)\qquad\text{for every unitary }u\in M.
\]
The range criterion then supplies the full uniform left-contraction bound and ACSY condition.

Equivalently, a direct construction of full-domain duals for the adjoint tuple would settle the same target.
Merely conjugating the original maps by J, using a generic bounded phase lift, invoking normality of a general M-to-H map, or invoking a general HS automatic-continuity theorem before proving H-valuedness does not complete it.
The two negative mechanisms above explain precisely why those shortcuts are insufficient, without disproving the rank-one problem.

The three new fixed Claims remain adopted as proved at their stated scopes; their R_F0046, R_F0138 and R_F0139 findings retain unknown initial-context relationships.
The broader normal-tuple implication and a genuine separating counterexample remain open in this comparison.
Prior positive classes and their distinct reverse implications remain as recorded in v3; no stronger reverse implication is inferred from this continuation.

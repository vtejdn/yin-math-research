---
author: Yin
---
# ACSY-to-full-domain exploration for general bounded tuples

Task: [T_F0011, general-tuple implication](../tasks/Yin_T_F0011_v1.md#objective-2-arbitrary-tuples-and-maximal-delta).
This rolling draft retains the continuing A-to-F branch.
Fixed free-model mathematics is at [C_F0134](../claims/Yin_C_F0134_v1.md#statement); its assessment is owned there.
Fixed results below retain the assessments at their linked Claims.
Unfixed arguments are explicitly retained at developer-checked scope.

## Exact unresolved target

For a bounded generating tuple X in a finite tracial von Neumann algebra, A(X) is existence of outer Hilbert-space-tensor derivations on the represented star algebra C<X,X*> with prescribed values on X and actual vacuum adjoints.
F(X) is existence of arbitrary linear maps D_i:M Omega to L2(M) satisfying [X_j,D_i]=delta_ij P on every bounded vector.
S(X) adds all bounded vectors to the actual adjoint domains.
Failure of a selected canonical candidate does not by itself refute the existential condition F.

The implication A(X) implies F(X) for arbitrary bounded generating tuples remains unresolved.
The converse is already refuted by [C_F0133](../claims/Yin_C_F0133_v1.md#statement), which is a separate branch.

## Existing failures and fixed positive range

[L_F0049](../ledger/Yin_L_F0049_v1.md) excludes the inverse-not-L2 singular tuple and the diffuse Jordan tuple as separating examples: their represented starred derivation conditions already fail.
[C_F0128 v2](../claims/Yin_C_F0128_v2.md#statement) has weaker small-domain premises.
The uniform singular sandwich in L_F0047 fails the actual vacuum condition.
None establishes A true and F false.

The complete free semicircular left-transport argument now belongs to [C_F0134](../claims/Yin_C_F0134_v1.md#argument), including the weighted-creation estimate, actual domains, actual vacua and necessity for every witness.
Its conclusion is A(h,hS) iff F(h,hS) iff S(h,hS) iff h^{-1} in L2, under its stated scalar-conjugate and freeness hypotheses.
The free model is therefore no longer a possible separating example; its proof is not duplicated here.

## Fixed weighted criterion and current continuation

The complete correlated-reference criterion formerly developed here is now fixed at [C_F0135](../claims/Yin_C_F0135_v1.md#statement), with its actual assessment owned there.
It assumes a selfadjoint finite-Fisher reference pair and Hilbert-space boundedness only of the normalized canonical S-contraction.
The fixed proof covers A iff inverse in L2, and the equivalence of F, S and the weighted polynomial bound.
It includes every actual domain and all-witness necessity argument, so that proof is not duplicated here.

The stronger kernel-weight estimate is proved and independently reviewed in C_F0136.
C_F0138 uses it, together with the input-weight estimate, to remove the Hilbert-space bounded S-contraction premise from the one-sided actual-vacuum result.
The remaining search concerns nonlinear coefficients outside the reference derivation kernel or an arbitrary reference tuple.

## Right transport remains positive in the sufficient direction

Under the reference assumptions of C_F0135, with b=h^{-1} in L2, put Z=Sh and define on all M

\[
 F_Z(a)=B_S(ab),\qquad
 F_h(a)=B_h(a)-\rho(S)F_Z(a).
 \tag{15}
\]

These are genuine H-valued maps because B_S is bounded on H.
The norm bound for F_Z is ||B_S||||b||2||a||.
Since [B_S,Sh]=Ph,

\[
 [F_Z,Sh](a)=\tau(hab)1=\tau(a)1,\qquad [F_Z,h]=0.
 \tag{16}
\]

The trace identity is legitimate for bounded h,a and L2 b, using tracial cyclicity and bh=1.
Moreover [B_h,Sh]=SP and [rho(S)F_Z,Sh]=rho(S)P=SP, while the correction commutes with left h.
Thus (15) gives F(h,Sh).
The position of rho(S) in (15) is essential; putting it on the other side would give P rho(S)=PS rather than SP.

This proves only h^{-1} in L2 implies F(h,Sh) under the reference hypotheses.
It does not prove the converse bare-full-domain implication or all-M actual adjoint domains for (15).
For the stronger current existence conclusion in the left orientation see [C_F0138](../claims/Yin_C_F0138_v1.md#statement).
Under the present bounded-B_S assumptions its criterion holds, so S(h,hS) exists; taking the negatives of the actual adjoints on M also gives S(h,Sh), with both domains justified by the original adjoint pairings.
This does not prove the bare converse F(h,Sh) implies h^{-1} in L2 or adjoint invariance of arbitrary F systems.

## The limitation of the earlier counterexample search

The earlier search required a correlated finite-Fisher reference pair with bounded normalized canonical B_S, b=h^{-1} in L2 and failure of the weighted bound.
C_F0135 proves why such failure would exclude every full-domain witness.
The accepted kernel-weight estimate C_F0136 forces that bound throughout this class.
This counterexample route is closed at those hypotheses.

The normalization premise remains important.
An arbitrary bounded raw dual on H need not remain bounded on H after subtracting a -> a E1, because E1 might only lie in L2.
For a bounded extension B_S of the normalized canonical contraction, B_S+B_S* commutes with the selfadjoint generators, hence is right multiplication by the bounded selfadjoint xi_S.
This is why b in L2 already makes b xi_S belong to L2 in C_F0135's narrower premise.

## A concrete unbounded-inverse marginal available for the free class

The allowed inverse need not be bounded.
Let h have probability law

\[
 d\mu(t)=w(t)\,dt,\qquad
 w(t)=30t^2(1-t)^2\,1_{(0,1)}(t).
 \tag{17}
\]

Then h is positive regular and diffuse, tau(h^{-2})=10, but h^{-1} is unbounded (indeed not in L4).
It also has a bounded scalar conjugate variable.
For 0<t<1 put

\[
 C_w(t)=\operatorname{PV}\int_0^1\frac{w(s)}{t-s}\,ds
 =w(t)\log\frac{t}{1-t}
  -30\left(\frac1{12}+\frac t3-\frac32t^2+t^3\right).
 \tag{18}
\]

The right side is bounded.
To check that xi_h=2C_w is the actual scalar conjugate variable, truncate the integral at |s-t|>epsilon.
Writing w(s)=w(t)+(w(s)-w(t)), the second part is uniformly bounded by ||w'||_infinity, while the constant part is

\[
 w(t)\log\frac{\max(t,\epsilon)}
                    {\max(1-t,\epsilon)}.
\]

For 0<epsilon<=1 this is bounded uniformly in t and epsilon by w(t)(|log t|+|log(1-t)|).
Therefore dominated convergence applies.
Symmetrizing the truncated double integral gives, for every polynomial p,

\[
 2\int p(t)C_w(t)\,d\mu(t)
 =\iint\frac{p(t)-p(s)}{t-s}\,d\mu(t)d\mu(s).
 \tag{19}
\]

The polynomial divided difference is bounded on [0,1]^2, so the diagonal cutoff disappears by dominated convergence.
Equation (19) is the actual conjugate-variable identity and its representing vector is bounded.
Freely adjoining a standard semicircular S puts this explicit h in the hypotheses of C_F0134 with an unbounded L2 inverse.
This elementary example is developer-checked here; it has not been included in C_F0134's fixed statement or independent review scope.

## Fixed actual-vacuum criterion and the next coefficient class

The complete argument without a Hilbert-space bounded reference contraction is now fixed at [C_F0138](../claims/Yin_C_F0138_v1.md#statement), whose actual assessment is owned there.
It proves A(h,hS) iff S(h,hS) iff h^{-1} and h^{-1}xi_S belong to L2, and implies F(h,hS), for a finite-Fisher selfadjoint reference pair.
The actual-vacuum necessity, input-weight estimate, both unbounded products, quantitative adjoint bound and S-to-A reconstruction are all retained there rather than duplicated here.

The output kernel-weight mechanism is proved and independently reviewed in [C_F0136](../claims/Yin_C_F0136_v1.md#statement).
Its finite kernel-tensor extension and Sylvester example are proved and independently reviewed in C_F0139; the still-unfixed structural explanation and weak-cluster variant are retained separately below.


## Fixed kernel-tensor theorem and Sylvester corollary

The finite-kernel energy identity, exact nonunitary error, core adjoint formula, simultaneous-measure extension and Sylvester-coordinate corollary are now fixed together at [C_F0139](../claims/Yin_C_F0139_v1.md#statement).
Its assessment and independent review scope are owned there.
Root developed the energy mechanism, and this branch developed the graph extension and corollary; neither developer is its independent reviewer.
The complete proof is not duplicated here.

Root also identified a structural explanation for finite coefficients.
For beta in B tensor B, delta_beta=I_beta delta annihilates B and takes the distinguished reference generator to beta, all others to zero.
Its coassociativity defect is an outer triple derivation and vanishes on the reference generators, because every tensor factor of beta is in its kernel.
Thus delta_beta is algebraically coassociative.
The coefficients (beta+beta#)/2 and (beta-beta#)/(2i) give two real coassociative derivations, with actual vacua (v+v*)/2 and i(v-v*)/2.
A general real-coassociative contraction theorem would give an alternative existence proof; applying the two separate 4-times bounds yields 4 sqrt(2)||v||, while C_F0139 directly retains 4||v||.
This explanation does not modify the fixed proof or import an uninspected general source theorem.
In particular Mai's general real-coassociative statement is only a source lead at present.

## Next failure mechanism: singular coefficients outside the kernel

The finite-kernel theorem above closes the most direct way of producing a counterexample by a coefficient singularity living entirely in the other-coordinate algebra.
A remaining possibility is an inverse-Jacobian coefficient involving the differentiated coordinate itself.
Its actual vacuum includes derivative corrections; those may cancel even when the transported contraction has no infinity-to-L2 bound.
No example satisfying the full A premise and excluding every F witness has yet been obtained by this route.

A simple nonkernel trial with a spectral gap also remains positive.
For positive selfadjoint h,S, the change Y=S h S+i S has S-Jacobian F=Sh tensor 1+1 tensor hS+i 1 tensor 1.
Both Sh and hS have nonnegative real spectra.
Explicitly Sh=(S h^(1/2))h^(1/2), whose reverse product is the bounded positive h^(1/2) S h^(1/2).
The nonzero-spectrum AB/BA identity treats every nonzero spectral point, and zero is real.
For z nonreal the actual bounded resolvent is
(z-Sh)^(-1)=z^(-1)+z^(-1) S h^(1/2)(z-h^(1/2) S h^(1/2))^(-1)h^(1/2).
No inverse of h occurs.
The same argument applies to hS.
The spectra of Sh and -hS-i are separated.
The usual Sylvester contour resolvents therefore give an inverse of F in the Banach projective tensor algebra.
The existing [projective inverse-Jacobian mechanism](../claims/Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma) is consequently the applicable positive interface; this is not a singular inverse-Jacobian test.
A useful future test needs absence of that projective inverse and an actual integrable vacuum, rather than merely a nonnormal polynomial expression.

The existing [C_F0054](../claims/Yin_C_F0054_v1.md#statement) gives a real derivation with actual zero vacuum and an unbounded contraction, but it cannot simply be declared an ACSY coordinate derivation.
In that model
delta f(z,w)=i(f(z)-f(w))/|z-w|,
so every value is antisymmetric under interchange of z,w.
A value equal to 1 tensor 1 is impossible on a nonatomic probability space, because that vector is symmetric and nonzero.
Adding this bad derivation to a good witness would likewise only exhibit a bad chosen witness, not the failure of every F system.

More generally, if a derivation is real and its values on every unstarred generator are the scalar tensors delta_ij 1 tensor 1, reality fixes the same values on the starred generators.
The algebraic coassociativity defect is a derivation into the triple tensor bimodule and vanishes on those generators, so it vanishes on the whole represented star algebra whenever the indicated algebraic tensor domains are available.
Thus a real derivation with the exact ACSY coordinate values cannot be used as an uncontrolled-coassociativity shortcut to a counterexample.
The unresolved freedom is in genuinely nonreal starred values and their analytic domains.

## A weaker weighted graph can suffice for full-domain existence

This is a new continuing candidate, not part of C_F0139's stated Hilbert-coefficient theorem.
Let the original finite-Fisher reference pair be (h,S), with h selfadjoint, B=C[h], and xi=xi_S.
Let F(s,t)=sum a_j(s)b_j(t) be a polynomial separated coefficient and Y=sum a_j(h)S b_j(h).
Assume X=(h,Y) generates M and F is nonzero mu tensor mu almost everywhere.
Let nu_xi be the same joint vector measure as in C_F0139.

Suppose beta=1/F belongs to L2(nu_xi), with a specified measurable value on any zero set invisible to the inverse.
It need not belong to L2(mu tensor mu).
The finite measure
|F|^2(mu tensor mu)+nu_xi
has beta in its L2 space, since F beta=1 in the coarse measure.
Polynomial density provides beta_n in C[h] tensor C[h] such that

\[
 F\beta_n\to1\text{ in }L^2(\mu\otimes\mu),\qquad
 v_n=\overline{\beta_n}(L_h,R_h)\xi\to
 v=\overline\beta(L_h,R_h)\xi\text{ in }H.
 \tag{44}
\]

For each finite beta_n, C_F0139 supplies operators T_n and T_n* on all M with uniform bounds 4||v_n|| and 5||v_n|| from operator norm to H.
Use the checked [Keh25 product and weak Hilbert-ball interfaces](../audits/literature/Keh25/Yin_U001.md#exact-accepted-interfaces) directly for the bounded maps from M, with its operator norm, to H.
For a fixed bound K, place each coordinate T(a) in the weakly compact closed H-ball of radius K||a||, indexed by every a in M.
The product is compact, and the equations T(alpha a+beta b)=alpha T(a)+beta T(b) are weakly closed finite-coordinate conditions.
Their closed intersection is exactly the set of complex-linear maps with ||T(a)||_2<=K||a|| for every a; no reflexivity of M or of a tensor product is assumed.
Apply this construction to both bounds 4 sup_n||v_n|| and 5 sup_n||v_n|| and take the product of the two compact sets.
It gives one simultaneous subnet of the pairs (T_n|M,T_n*|M) converging pointwise weakly to maps (T,U), without a sequential compactness or separability assumption.

The uniform bounds pass to the limits.
For a,q in M, pass to the limit in
<q,T_n a>=<T_n* q,a>.
This gives <q,T a>=<Uq,a> for every a in the dense domain M.
Hence each q in M is in the actual Hilbert adjoint domain of the domain-M operator T, and T*q=Uq.
Thus T has both actual M domains.

All finite T_n commute with h.
Their Y commutators are the Hilbert--Schmidt operators Theta(F beta_n).
By (44) these converge in Hilbert--Schmidt norm to P.
Passing to the pointwise weak limits gives [T,h]=0, [T,Y]=P on M.
If C=partial_h Y is the finite original polynomial tensor, the finite right-coefficient implementation Q_C(T)=sum rho(c_left)T rho(c_right) is defined on M with actual adjoint domain M.
Its commutator with Y is Theta(C), while its h commutator is zero.
Therefore B_h-Q_C(T), together with T and the generator-first negation, gives S(h,Y).

This is an existence construction through uniformly controlled maps, rather than a claim that beta defines a Hilbert-valued derivation on the original A_0.
It can remain meaningful when beta is not in the coarse L2 space.
The compactness used here is precisely the source-checked product of weak Hilbert balls and its closed linearity constraints; the candidate requires no projective-tensor dual identification.
The weighted-graph construction remains a working candidate at the scope stated above, distinct from the accepted target-core theorem below.

## Fixed target-core linear-coordinate theorem

The complete actual-vacuum bridge, three-measure target-core approximation, pseudoinverse removal of an unnecessary H-injectivity premise, and identification of both supplied canonical closures are now fixed and independently reviewed at [C_F0141](../claims/Yin_C_F0141_v1.md#decision-reviewed).
Its actual assessment is owned there.
Generation and coarse nonvanishing remain explicit.
That proof restores the target canonical domains without assuming 1/F is coarse L2, without a weak-cluster choice, and without applying a target derivation to reference coefficients outside its domain.
The complete proof is not duplicated here.


## An exact integrability criterion retained for reuse

Root observed that C_F0141's construction also proves a useful converse sufficient test at the same reference, generation and coarse-nonvanishing assumptions.
It is retained here without another Claim allocation.
Define F#(s,t)=overline{F(t,s)} and let nu_xi be the joint left/right spectral vector measure at the original xi_S.
The conditions are

\[
 F^\#/F\in L^2(\mu\otimes\mu),\qquad
 \nu_\xi(\{F=0\})=0,\qquad
 1/F\in L^2(\nu_\xi).
 \tag{45}
\]

The explicit zero-mass clause specifies that 1/F is a genuine inverse on this vector measure, rather than assigning a harmless zero value on a set of positive nu_xi mass.
Under A these conditions are necessary by C_F0141 Sections 2-3.

Conversely (45) places beta=1/F in the three-measure space of that proof.
Finite polynomial beta_n then have target generator derivatives converging respectively to 0,1,F#/F and actual vacua converging to overline(beta)(L_h,R_h)xi_S.
Leibniz expansion gives limits on every target polynomial.
The limits are well-defined on the represented A_X: an expression representing zero is already zero in A_0, and every finite delta_(beta_n) sends it to zero.
The actual vacuum pairing passes to the limit.
Thus the Y-coordinate derivation and its actual vacuum exist.

The same two contraction limits and adjoint pairings give its closed canonical dual with both M domains.
The h correction of C_F0141 Section 5 then constructs the h-coordinate derivation with an actual vacuum and both canonical domains.
Hence (45) is sufficient for A and S, and the existence of just the Y-coordinate actual-vacuum derivation already supplies the whole system in this linear reference class.
This statement is not an F-to-A converse and does not address nonlinear inverse Jacobians.

The standard diffuse-polynomial simplification remains available: if mu is diffuse and F is a nonzero polynomial, its zero set is mu tensor mu null by Fubini and finiteness of the roots of each nonzero one-variable specialization.
It does not remove the separately stated generation hypothesis.

## Fixed nonlinear target reduction and exact remaining tests

The complete nonlinear construction for Y=ShS+i hSh is fixed at [C_F0142](../claims/Yin_C_F0142_v1.md#statement), with its assessment owned there.
The fixed candidate contains generation, the affiliated Cayley construction of both represented starred derivations, uniqueness among all L0(M bar tensor M^op)-valued coordinate derivations, and the exact equivalence of A(h,Y) with the two actual adjoint conditions

    1,C* in Dom(delta_Y|A_X)*,
    C=partial_h Y,
    delta_Y(p)=(partial_S p)(partial_S Y)^(-1).

The complete proof, including the target relation hWZ=ZWh and its regular coefficient K, is retained there and not duplicated here.
The separate positive-S Hilbert--Schmidt range proof is also fixed there.
Root developed the necessary equation for arbitrary bare witnesses; this branch developed the nonlinear reduction and range formula.
The developers are not independent reviewers of this result.

The next exact obligations remain:

1. Determine whether the two actual-adjoint conditions hold for a concrete finite-Fisher reference pair with h^{-1} unbounded, or find an exact criterion in such a class.
   The bounded target derivative delta_Y(Y*) is a Cayley unitary even if the inverse Jacobian is not coarse L2.
   Non-L2 of that inverse alone cannot reject A.
2. Determine whether an arbitrary bare E:M->H with [E,h]=0 and [E,Y]=P is forced to have the same useful core/inverse-domain behavior.
   Its commutators are maps M->H, so regularity of K in the coarse affiliated algebra does not act on them automatically.
   Hilbert--Schmidt uniqueness is not bare-witness uniqueness.
3. The positive-S weighted Hilbert--Schmidt solution does not settle the unweighted map h^{-1/2}U h^{-1/2}; sign-changing S also retains the inhomogeneous weighted range problem.
   The finite diagnostics below distinguish these questions without resolving them.

## A special positive projective integral and a genuine sufficient regime

This uses the particular Q of C_F0142, not a universal symmetry assertion.
Assume S>=c1 for c>0 and retain h bounded positive regular.
Set
\[
 q_0=S^{-1/2}h^{-1}S^{-1/2},\qquad
 G=S^{1/2}\otimes(S^{1/2})^{\mathrm{op}}.
\]
Then q_0 is positive affiliated and q_0>=(||h||||S||)^(-1)1, while Q=G(q_0 tensor 1+1 tensor q_0^op)G.
For t>0 the map t->exp(-t q_0) is operator-norm continuous, also for unbounded q_0, by the uniform scalar estimate on the positive half-line.
The elementary tensor integrand is therefore norm continuous in the Banach projective tensor algebra on (0,infinity), and its norm is at most exp(-2t/(||h||||S||)).
Consequently the Bochner integral
\[
 Q^{-1}=G^{-1}
   \left[\int_0^\infty e^{-tq_0}\otimes(e^{-tq_0})^{\mathrm{op}}\,dt\right]
   G^{-1}
 \tag{46}
\]
belongs to M tensor_pi M^op.
Its image in the spatial tensor algebra is the claimed inverse by the joint scalar Laplace identity.
The projective norm bound is
\[
 \|Q^{-1}\|_\pi\le
 \eta:=\frac{\|S\|\|h\|}{2c^2}.
 \tag{47}
\]
Both outside factors have projective norm at most 1/c; retaining both is necessary for this constant.
This remains valid for unbounded h^{-1}.

If eta<1, the explicit projective Neumann series yields R=(Q+i)^(-1)=Q^(-1)(1+iQ^(-1))^(-1), with projective norm at most eta/(1-eta).
If h^{-1} is also bounded, then
\[
 \beta=(h^{-1}\otimes(h^{-1})^{\mathrm{op}})R
   \in M\widehat\otimes_\pi M^{\mathrm{op}},\qquad
 \|\beta\|_\pi\le\|h^{-1}\|^2\frac{\eta}{1-\eta}.
 \tag{48}
\]

These explicit extra assumptions do prove A(h,Y), S(h,Y), and F(h,Y), with full actual canonical domains.
Here are the domain details, so this is not merely a proposed projective shortcut.
Let E and B_h be the normalized canonical reference contractions.
The checked selfadjoint finite-Fisher interface gives E,E*,B_h,B_h* on all M with operator-norm-to-H bounds.
The projective coefficient implementation of [C_F0130, Section 5](../claims/Yin_C_F0130_v1.md#5-projective-corrections-on-all-bounded-vectors) is Q_(a tensor b)(E)=rho(a) E rho(b).
For a projective expansion beta=sum a_n tensor b_n with sum ||a_n||||b_n|| finite, put
\[
 Kp=\sum_n E(p b_n)a_n,\qquad
 K^*q=\sum_n E^*(q a_n^*)b_n^*,\qquad p,q\in M.
 \tag{49}
\]
Both series converge in H by the two reference bounds.
Termwise Hilbert pairing proves that the displayed second expression is the actual adjoint of the domain-M first map at q, not a formal transpose.
The same estimates prove both operator-norm-to-H bounds.
Commutator identities pass through these absolutely convergent series.
In particular [K,h]=0, [K,Y]=Theta(F beta)=P, and [K,Y*]=Theta(k) on M.
On finite tensors this is exactly the right-coefficient identity of C_F0130; projective continuity supplies the completed case without assuming that E is bounded on H.

For C=partial_hY, put L=B_h-Q_C(K).
The finite right-coefficient correction has actual adjoint on M by the same calculation, and [L,h]=P, [L,Y]=0, [L,Y*]=Theta(C_- -kC).
Thus -L,-K give S and hence F.
For p in A_X their full-domain commutators give exactly the two derivations fixed in C_F0142, by Leibniz expansion and the three generator values.
Every domain-M operator T with actual adjoint at 1 satisfies
\[
 \tau_N(\Theta^{-1}[T,p])
   =\langle T^*1-(T1)^*,p\rangle_H.
\]
This is the elementary vacuum pairing: [T,p]1=Tp-pT1 and tracial cyclicity identifies the second term.
Applying it to K,L proves both actual vacua and hence A.
Moreover the canonical contractions on A_X are K-rho(K1) and L-rho(L1).
Their actual adjoints contain M, their operator-norm-to-H bounds hold on all M, and bounded polynomial approximation with the weakly closed graph puts M in their original Hilbert closures.
Thus the sufficient regime genuinely restores both specified canonical domains.

For unbounded h^{-1}, (46)-(47) and the projective R still hold under eta<1, but (48) does not follow.
The singular outside factors in beta are exactly the unremoved difficulty; a projective Cayley phase alone supplies neither of the two vacuum tests.

Root also observed a bounded-operator extension of the independent positive-S HS formula.
With A=h^(1/2)Sh^(1/2), its J is the completely positive map J(V)=integral_0^infinity exp(-tA)h^(1/2)Vh^(1/2)exp(-tA) dt on B(H), interpreted through its bounded Stinespring integral.
Indeed A>=ch gives J(1)<=1/(2c), by integrating exp(-tA)h exp(-tA)<=c^(-1) exp(-tA)A exp(-tA).
The map C_0(V)=h^(1/2)J(V)h^(1/2) has selfadjoint Kraus operators and norm at most ||h||/(2c).
When that bound is below one, its Neumann resolvent also acts on B(H).
This does not remove the h^(-1/2) unweighting and does not extend such maps to arbitrary B(M,H) inputs by itself.

## Fixed free nonlinear actual-vacuum example and the remaining contraction issue

The complete actual-vacuum proof for h=2+s_0, S=c+s_1, c>6, and Y=ShS+i hSh is fixed at [C_F0144](../claims/Yin_C_F0144_v1.md#statement), with its exact assessment owned there.
It proves A(h,Y) although h^{-1} is unbounded and not in L2.
The fixed proof contains the letter-1 count grading with unrestricted letter-0 count, the actual reference-adjoint norm bound, the coarse sum-denominator inverse, both graph-convergent series and the actual target pairings.
None of that necessary proof is duplicated here.

The full-domain issue for this concrete example is resolved by C_F0145 below.
A useful exact primitive formula follows from the same Fock basis.
For beta=U_r tensor U_t and a word w,

    E_beta U_w = U_u U_r if w=u 1 reverse(t), and zero otherwise.

Here E_beta=(id tensor tau) I_beta partial_1.
The formula follows because tau(U_t U_v) is one precisely when v=reverse(t), and zero otherwise.
It selects one suffix cut, but multiplication U_u U_r still includes cancellations, so an operator-norm bound does not follow merely from deleting a suffix.

The complete finite-letter-count and summable-coefficient contraction argument is now fixed at [C_F0145](../claims/Yin_C_F0145_v1.md#statement), with its actual assessment owned there.
Root developed the suffix-cut H-to-L1 estimate, duality and summation; this branch supplied the primitive formula and checked its tensor contractions and nonlinear application during development.
These checks are not an independent review.
The complete proof is not duplicated here.

C_F0145's independently reviewed result restores both target canonical domains for the geometric beta series of C_F0144, including the h-coordinate correction, and therefore gives S and F for that concrete example.
Its selected decision adopts the complete independent review R_F0152.
The continuing question concerns an arbitrary integrable inverse Jacobian without this summable relative-degree expansion.
The abstract coefficient obstruction below shows why actual reference adjoint membership by itself is insufficient.

## Coarse inverse integrability for every positive shift: no new domain conclusion

For the same free h=2+s_0 and S=c+s_1, the affiliated inverse beta of C_F0142 belongs to coarse L2 for every c>2, not only c>6.
This is a bounded additional reduction; the actual-adjoint and full-domain extension beyond the geometric regime is not claimed.

Write d=c-2>0, G=h tensor 1+1 tensor h^op, and g=||G^-1||2<infinity as proved in C_F0144.
Put A=h^(1/2)Sh^(1/2), A'=S^(1/2)hS^(1/2), D=A' tensor 1+1 tensor (A')^op, and K=S^(1/2) tensor (S^(1/2))^op.
Then A>=d h, while A and A' have the same trace spectral law, by cyclicity of every polynomial moment and continuous functional calculus.
One must NOT assert A'>=d h, which need not hold.

For bounded positive A>=d h, differentiating the scalar trace function f(r)=tau exp[-t(d h+r(A-d h))] and using the Duhamel derivative with tracial cyclicity gives f'(r)=-t tau((A-d h)exp[-t(d h+r(A-d h))])<=0.
The positivity of the trace of a product of two bounded positives proves the sign.
Consequently tau(exp(-tA'))=tau(exp(-tA))<=tau(exp(-tdh)).
Tonelli and the scalar Laplace formula x^-2=integral_0^infinity t exp(-tx)dt now give

    ||D^-1||2^2
      = integral_0^infinity t [tau(exp(-tA'))]^2 dt
      <= d^-2 g^2.

The exact bounded similarity is F_0=Sh tensor 1+1 tensor (hS)^op=K D K^-1.
Hence F_0^-1 is L2 with norm at most ||S||g/d^2.
In the C_F0142 notation, F_0=QB and Q>=2d/||h||.
Therefore

    beta=F_0^-1(1+iQ^-1)^-1,
    ||beta||2<=||S||g/d^2,

because Q^-1 is bounded positive and the last factor has norm at most one.
These estimates use the trace comparison, not an invalid operator comparison or a projective inverse claim.
They do not establish beta* in Dom partial_1* or full-domain contraction bounds for 2<c<=6.

## An actual reference adjoint does not control the contraction

The following adapts the already fixed absolute-phase mechanism of [C_F0054](../claims/Yin_C_F0054_v1.md#statement) to the exact free Fock reference used here.
It is retained to distinguish the new finite-letter-count sufficient condition from an actual-vacuum condition alone.
It is not an A-to-F counterexample.

Let s=s_1 be standard semicircular and keep the freely independent s_0.
Identify W*(s) tensor W*(s) with the product semicircle measure.
Put
\[
 \beta_0(s,t)=\mathrm i\operatorname{sign}(s-t),\qquad
 \beta_1=1+\beta_0.
 \tag{50}
\]
Both are bounded coarse tensors.
Beta_1 is boundedly invertible, with beta_1^-1(s,t)=(1-i sign(s-t))/2 off the null diagonal.
Nevertheless
\[
 \beta_0^*,\beta_1^*\in\operatorname{Dom}\partial_1^*,\qquad
 \partial_1^*\beta_0^*=0,\quad
 \partial_1^*\beta_1^*=s,
 \tag{51}
\]
and their transported contractions fail every operator-norm-to-L2 bound.

First verify (51) on the FULL mixed polynomial core.
For a polynomial f(s),
\[
 \langle\beta_0^*,\partial_1 f\rangle
 =\mathrm i\iint\frac{f(s)-f(t)}{|s-t|}\,d\mu(s)d\mu(t)=0.
 \tag{52}
\]
The numerator is Lipschitz, so the kernel is bounded and antisymmetry justifies the interchange.
A Fock word involving a letter 0 has, in every letter-1 cut, at least one tensor leg containing a letter 0.
Such a tensor is orthogonal to beta_0*, which is supported on the two s-only Fock spaces.
Thus (52) also vanishes for every mixed word; words containing no letter 1 have zero derivative.
The functional is identically zero on the entire dense mixed core, proving actual adjoint membership, not merely a scalar marginal identity.
Adding the vacuum tensor gives the second equation in (51).

For scalar f the contraction is
\[
 E_{\beta_0}f(s)
   =\mathrm i\int\frac{f(s)-f(t)}{|s-t|}\,d\mu(t).
 \tag{53}
\]
Let u_n(s)=exp(i n s).
Its scalar divided-difference kernel is bounded, so (53) defines an H vector.
Symmetrization gives the real nonnegative energy
\[
 \langle u_n,-\mathrm iE_{\beta_0}u_n\rangle
  =\iint\frac{1-\cos(n(s-t))}{|s-t|}\,d\mu(s)d\mu(t).
 \tag{54}
\]
The semicircle density is at least m=sqrt(3)/(2pi) on [-1,1].
Restrict to s in [-1/2,1/2] and t=s+r with 0<r<1/2; both variables stay in that interval of density control.
For n>=2 the energy is therefore at least
\[
 m^2\int_{1/n}^{1/2}\frac{1-\cos(nr)}r\,dr
 \ge m^2\bigl(\log(n/2)-3\bigr).
 \tag{55}
\]
The final bound follows after u=nr: integration by parts bounds the absolute value of integral_1^R cos(u)/u du by 3 uniformly in R>=1.
Since ||u_n||2=||u_n||infinity=1, Cauchy--Schwarz bounds ||E_beta0 u_n||2 below by (55).

This can be returned to the ORIGINAL polynomial core.
For each n choose a complex polynomial p_n approximating u_n and its derivative uniformly on [-2,2] to error at most one, using its convergent exponential Taylor series.
Then ||p_n||infinity<=2, and the mean-value bound on the error gives ||E_beta0(p_n-u_n)||2<=1.
Thus ||E_beta0 p_n||2 tends to infinity while ||p_n|| stays bounded.
The canonical reference E_1 is the bounded right-annihilation operator, of Hilbert norm one; hence ||E_beta1 p_n||2 also tends to infinity.
This proves the failure for the bounded invertible coefficient beta_1 with nonzero actual vacuum s.

The extra finite coefficient test in C_F0142 does not by itself remove this abstract obstruction.
For any eta in Dom partial_1* and any fixed algebraic outer coefficient C in A_0 tensor A_0, C eta belongs to Dom partial_1*.
To check this directly, write C as a finite sum of a tensor b and apply the Leibniz rule to a* p b* in the adjoint pairing.
The two error terms contain bounded polynomial derivative tensors; their trace contractions are L2 vectors bounded by a finite constant times ||eta||2||p||2.
The main term is controlled by ||partial_1*eta||2 and the bounded a,b.
Thus C*beta_j* is in the actual adjoint domain for j=0,1.
Merely knowing both such reference graph conditions cannot substitute for coordinate integrability.

### Why the bounded invertible bad coefficient cannot be an inverse Jacobian

The preceding tensor does not satisfy the missing coordinate condition.
In fact no Y in the actual domain of the closed reference partial_1 can have partial_1Y=beta_1^-1.
The word-cut formula identifies that closed domain explicitly: if Y=sum_w a_w U_w, then

    Y in Dom closed partial_1 iff sum_w (# of letters 1 in w)|a_w|^2<infinity,
    partial_1Y=sum_(w=u1v) a_w U_u tensor U_v.

Finite word truncations prove this domain characterization.
Different cuts with the same left/right count occupy orthogonal tensor word bases, and the pair (u,v) determines w=u1v uniquely, so no coefficient cancellation is possible at a fixed output pair.

If partial_1Y belongs to H(W*(s)) tensor H(W*(s)), every coefficient of a mixed word containing both 0 and 1 must vanish: any of its cuts leaves a 0 in one leg, outside that tensor subspace.
Hence Y=f(s)+g(s_0) in H, with f in the scalar closed derivative domain and g in its kernel.
The derivative of f is symmetric in s,t, because scalar polynomial divided differences are symmetric and that symmetry subspace is L2 closed.
But beta_1^-1(s,t) is not symmetric.
This is the contradiction.

Since right multiplication by beta_1 is bounded and boundedly invertible on the coarse Hilbert space, the closure of I_beta1 partial_1 has exactly the reference closed-derivation domain.
Thus even allowing the closure cannot produce a bounded coordinate Y with derivative equal to the vacuum tensor.
This precisely excludes the tempting normalization of a bad coefficient into an ACSY coordinate.
It neither excludes nor constructs every dual for an unrelated tuple.

The useful remaining question is whether the additional condition that beta is an actual inverse Jacobian, together with its actual vacua, prevents such high-degree cancellations.
A failure of the coefficient estimate without this integrability condition does not resolve the Task.

## Algebraic module splitting does not erase the range obstruction

This section tests a different existential route: producing an arbitrary bare full-domain dual by algebraic extension, without first extending the canonical contraction.
The relevant local search found no adopted module-splitting theorem giving that conclusion.
The registered tensor-algebra source does give the exact length-one resolution: [Wei94-U002](../audits/literature/Wei94/Yin_U002.md#wei94-u002) records the directly inspected Proposition 9.1.6, printed pp.303–304, and its precise field specialization.
The following adaptation and its limits are developer-checked here.

Let A=C<x_1,...,x_d> be the formal free algebra, V=M as a complex vector space with left action x_j a=X_j a, and H=L2(M) with the same left action.
No injectivity of the evaluation map is needed for these module definitions.
For a fixed index i define an A-module W_i=H direct-sum V by prescribing its free-generator actions

\[
 x_j(\eta,a)=(X_j\eta+\delta_{ij}\tau(a)1,\ X_j a).
 \tag{56}
\]

Because A is free, these linear maps define an A-action.
The sequence
0 -> H -> W_i -> V -> 0 is exact.
It splits as A-modules if and only if there is a linear E_i:V->H with

\[
 E_i(X_j a)-X_jE_i(a)=\delta_{ij}\tau(a)1
 \quad(a\in M).
 \tag{57}
\]

Indeed a linear section of the projection has the form a mapped to (E_i(a),a), and A-linearity on the free generators is exactly (57).
Thus D_i=-E_i is the required generator-first bare dual.
This equivalence concerns a genuinely H-valued section; it does not impose continuity or actual adjoint domains.

Tensor the inspected bimodule resolution over its right A-action with V.
Right-A splitting of the original short exact sequence preserves exactness.
With e_1,...,e_d the standard basis, the resulting free left-A resolution is

\[
0\longrightarrow A\otimes\mathbb C^d\otimes V
 \mathop{\longrightarrow}^{d}A\otimes V
 \mathop{\longrightarrow}^{\varepsilon}V\longrightarrow0,
\qquad
d(a\otimes e_j\otimes v)=a x_j\otimes v-a\otimes X_jv.
 \tag{58}
\]

Here all tensor products are algebraic over C.
Applying Hom_A(-,H), using freeness of the displayed modules, gives the explicit cokernel

\[
 \operatorname{Ext}_A^1(V,H)
 \cong
 \operatorname{Hom}_{\mathbb C}(V,H)^d\big/
 \{(X_jE-E X_j)_{j=1}^d:E\in\operatorname{Hom}_{\mathbb C}(V,H)\}.
 \tag{59}
\]

The extension (56) splits precisely when its rank-one coordinate class vanishes in this cokernel; the overall sign is immaterial for vanishing.
The resolution bounds projective dimension by one.
It does not make the displayed cokernel zero.
In particular neither a Hamel basis nor the absence of degree-two homology proves (57).

### Maximal Delta only gives an algebraic-dual-valued extension by this argument

The [maximal-Delta finite-rank-cycle interface](../audits/literature/MSY23/Yin_U002.md#msy23-u002) says that Delta(X)=d is equivalent to injectivity of

\[
 b:\mathcal F(H)^d\longrightarrow\mathcal F(H),
 \qquad b(T_1,\ldots,T_d)=\sum_j[X_j,T_j].
 \tag{60}
\]

Consequently the functional ell_i(b(T))=Tr(P T_i) is well-defined on the range of b.
Extend it algebraically to all finite-rank operators by a vector-space complement.
With inner product linear in its second variable and R_(a,b)z=a<b,z>, put

\[
 \mathcal E_i(a)(b)=\ell_i(R_{a,b}),\qquad a,b\in H.
 \tag{61}
\]

For fixed a this is a conjugate-linear algebraic functional of b, with no continuity assertion.
Since
[X_j,R_(a,b)]=R_(X_j a,b)-R_(a,X_j^* b), formula (60) yields

\[
 \mathcal E_i(X_j a)(b)-\mathcal E_i(a)(X_j^* b)
   =\delta_{ij}\langle b,Pa\rangle.
 \tag{62}
\]

Thus there is a formal dual with values in the full algebraic conjugate dual of H.
A value belongs to H under the Riesz embedding only when that functional is Hilbert-norm continuous.
Algebraic extension gives no such pointwise continuity, even for a in M.
This is the exact missing step in using maximal Delta to produce a bare Hilbert-valued dual.

### Explicit scalar falsification of Delta implying F

The complete arcsine vacuum-adjoint obstruction, together with its liberation-dual consequence and a shorter monomial proof, is now fixed in [C_F0080](../claims/Yin_C_F0080_v1.md#argument), with the recorded self-review [R_F0053](../audits/reviews/Yin_R_F0053_v1.md#whole-proof-finding).
The ordinary-dual comparison below retains its additional C_F0069 input.

The missing step cannot hold in general.
Let M=L-infinity(mu) for the arcsine probability measure

\[
 d\mu(t)=\frac{1_{(-1,1)}(t)}{\pi\sqrt{1-t^2}}\,dt,
 \qquad x(t)=t.
 \tag{63}
\]

This scalar law is diffuse, so no nonzero finite-rank operator commutes with multiplication by x.
In fact its finite-dimensional range would be x-invariant and would contain an eigenvector of x, contradicting diffuseness.
The interface (60) therefore gives Delta(x)=1.

The [fixed Chebyshev calculation](../claims/Yin_C_F0080_v1.md#the-original-chebyshev-calculation) proves that no vector in H represents the actual divided-difference vacuum functional.
The independently reviewed [scalar converse C_F0069](../claims/Yin_C_F0069_v1.md#statement) implies that any bare full-domain dual would supply precisely this actual vacuum.
Therefore F(x) is false.
This example refutes Delta=d implying F even for an absolutely continuous scalar law.
It does not refute A implying F, since A already fails here.
The vacuum calculation has its self-contained fixed home in C_F0080; the substantive automatic-continuity implication is imported only at C_F0069's stated scope.

## A row-kernel obstruction excluding every bare full-domain witness

The complete general row obstruction and the concrete common-left-factor tuple are fixed at [C_F0147](../claims/Yin_C_F0147_v1.md#statement), with its assessment owned there.
For h=2+s_0 and three free semicircular reference coordinates, X=(hS_1,hS_2) generates its target algebra N=W*(X), has Delta_N(X)=2, but neither coordinate admits any bare full-domain dual.
The proof uses bounded columns of the target row-kernel projection and the failure of 1 to belong to hL2 of the ambient reference algebra.
It also proves star algebraic freeness and excludes every L2-valued derivation lift to the full reference algebra.
Its selected reviewed decision adopts the complete independent [R_F0154](../audits/reviews/Yin_R_F0154_v1.md#conclusion).
The subsequent [C_F0148](../claims/Yin_C_F0148_v1.md#statement), with complete self-review [R_F0155](../audits/reviews/Yin_R_F0155_v1.md#conclusion), excludes both actual target coordinate vacua as well.
Thus this example has maximal Delta while A and F both fail, and the proposed A-to-F separation route is closed.
These complete proofs are not duplicated.

The fixed reference-lifting obstruction alone could not decide target A because h,S_j were not in any verified target derivation domain.
C_F0148 resolves it directly through target polynomial Neumann approximations and actual vacuum pairings.
Parent root and this branch developed C_F0147; neither is its independent reviewer.
This branch checked C_F0148 at the self-reviewed relationship recorded in R_F0155, with its exact prior-summary and related-development disclosures.

### The natural holomorphic-core dual fails on one starred generator

Root supplied the following exact boundary during development, retained here as a continuation mechanism rather than an addition to the fixed Claim.
Use the standard right annihilation operator r_i* for S_i in the [free Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001).
It is bounded on the ambient H and satisfies

\[
 [r_i^*,S_j]=\delta_{ij}P,\qquad [r_i^*,h]=0,
 \qquad r_i^*1=0.
 \tag{73}
\]

Let rho(h^-1) denote closed right multiplication by the affiliated inverse and set E_i=rho(h^-1) r_i* on its actual composition domain.
This domain contains the target holomorphic polynomial algebra C<X_1,X_2>, and E_i there satisfies [E_i,X_j]=delta_ij P.
To verify actual membership inductively, the vacuum is in the domain, and

\[
 r_i^*(X_j a)=X_jr_i^*a+\delta_{ij}\tau(a)h.
 \tag{74}
\]

If r_i*a has its right h^-1 product in H, bounded left multiplication by X_j preserves the domain of right h^-1 multiplication.
Both terms in (74) therefore lie in that domain, and applying rho(h^-1) gives X_j E_i a+delta_ij tau(a)1.
This proves the recursion on every holomorphic word.
It does not assert that the holomorphic core is Hilbert dense in L2(N), and the constructed values are initially in the ambient H.

Already for one starred generator the actual domain fails:

\[
 r_i^*(X_i^*)=r_i^*(S_i h)=\tau(h)1=2\,1,
 \qquad
 \rho(h^{-1})r_i^*(X_i^*)=2h^{-1}\notin H.
 \tag{75}
\]

Thus this natural reference annihilation construction cannot be used on the required target star core.
The rank-one commutator recursion uniquely fixes every normalized coordinate map on holomorphic polynomials, but does not specify its values on all additional starred vectors.
Equation (75) alone did not exclude a different extension with compatible starred values.
C_F0148 now excludes every such actual target-A extension by a separate target-only argument.
The calculation is retained as the exact failure of the natural holomorphic-core construction, not as the proof of universal nonexistence.

The continuing general A-to-F problem must move beyond this example.
C_F0148 makes every bounded vector belong to the actual row range under full A with at least two generators.
The subsequent [C_F0155](../claims/Yin_C_F0155_v1.md#statement) removes every finite holomorphic polynomial-relation range obstruction.
What remains is coherent infinite compatibility or an estimate yielding a full-domain dual, not an unresolved finite-relation obstruction of that form.

Root's bounded source search for the next step covered the registered literature/audits by free Fisher matrices and minimization, then external primary-source leads by products of semicircular variables and common multiplicative factors.
It did not supply an external theorem deciding this target tuple; C_F0148 subsequently resolved it by the local target-resolvent argument.
The surfaced general operator-valued Fisher and free Stein topics are not adopted inputs.
This retains the useful search boundary without an absence or novelty claim.

### Scope of the earlier bounded-regularization route

Root checked the following interface during the common-factor investigation.
It is a necessary condition under a hypothetical target A.
C_F0148 now rules out that hypothesis for the specific tuple; this calculation remains a useful record of why bounded regularization did not itself provide a reference-domain extension.
Reuse is the exact bounded regularization in [ACSY24-U001, Section 3](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), already inspected in this investigation.

Suppose the target tuple of C_F0147 had an actual ACSY witness for coordinate i.
Its canonical contraction has bounded regularizations D_t on L2(N) such that, in Hilbert-Schmidt norm,

\[
 [D_t,X_j]\longrightarrow\delta_{ij}P,\qquad
 [D_t,X_j^*]\longrightarrow K_{ij},
 \tag{76}
\]

where K_ij is the actual Hilbert-Schmidt starred commutator supplied by that witness.
The source's block-resolvent calculation applies to X_j* as well as X_j; both required commutator blocks are Hilbert-Schmidt.
No full bounded-vector domain is inferred.

Let Q_N be the orthogonal projection from ambient L2(tilde M) onto L2(N), and extend D_t by zero on its orthogonal complement.
Left multiplication by every N element reduces L2(N), so (76) persists on the ambient space with K_ij extended by zero.
The rank-one P is the same ambient vacuum projection.
This extension permits use of the bounded ambient h even though h is not asserted to belong to N.

Put T_j,t=[D_t,X_j], U_j,t=[D_t,X_j*], and B_t=[D_t,h] for these ambient bounded operators.
The concrete identity X_j h=h X_j* and the commutator product rule give exactly

\[
 X_jB_t-B_tX_j^*=hU_{j,t}-T_{j,t}h.
 \tag{77}
\]

The right sides have uniformly bounded Hilbert-Schmidt norms as t decreases to zero, with limits hK_ij-delta_ij P h.
Each B_t is bounded, but neither a uniform operator bound nor a Hilbert-Schmidt bound for B_t is available.
In particular, this calculation does not produce the L2 reference derivative excluded in C_F0147.
No quantitative bound on these B_t was proved by this route.
Passing B_t to a Hilbert limit or replacing it by a coarse tensor without an estimate would reintroduce the invalid reference-domain assumption.
The target-resolvent proof in C_F0148 bypasses this unavailable passage.

## Positive congruence coordinates at the weaker inverse-half integrability

The following comparison is a direct specialization of the accepted measurable-kernel theorem [C_F0139](../claims/Yin_C_F0139_v1.md#statement).
It explains why unbounded similarity alone cannot transfer the current domain conclusions.
Let s_0,S_1,S_2 be the same free semicircular reference family as in C_F0147, h=2+s_0, c=h^(1/2), b=h^(-1/2), and

\[
 Y_j=cS_jc,\qquad P_Y=W^*(Y_1,Y_2),
 \qquad m=\tau(h^{-1})=1.
 \tag{78}
\]

The value m follows by integrating sqrt((4-t)/t)/(2 pi) over (0,4), or by substituting t=4 sin^2 theta.
Thus b belongs to ambient L2 although h^-1 does not.
The target algebra P_Y is not asserted to equal the ambient reference algebra or N=W*(hS_1,hS_2).

Fix i and use the reference free derivative partial_i with actual vacuum S_i.
Put beta=b tensor b, a real symmetric measurable coefficient in the kernel algebra W*(h).
Freeness gives, first for bounded functions a,d of h,

\[
 \|aS_i d\|_2^2=\|a\|_2^2\|d\|_2^2.
 \tag{79}
\]

More generally its polarized form identifies the entire joint spectral vector measure of L_h,R_h at S_i with mu_h tensor mu_h.
Thus beta belongs to both measures required in C_F0139(S3), and

\[
 v_i=\partial_i^*\beta=bS_i b,\qquad
 \|\beta\|_2=\|v_i\|_2=m.
 \tag{80}
\]

The adjoint value in (80) is actual.
One can see the graph convergence directly: bounded spectral approximations b_n to b, converging in L2, give beta_n=b_n tensor b_n converging to beta.
The bounded-kernel adjoint formula gives partial_i*beta_n=b_n S_i b_n.
Equation (79), applied to the two differences, shows convergence to bS_i b in L2.
Bounded functions of h in this formula can be approximated by polynomials for the corresponding kernel and joint vector measures, exactly as in C_F0139's spectral-approximation proof.
Closedness of partial_i* yields (80); it is not merely a formal product identity.

C_F0139 now gives the original closed kernel contraction K_i and its actual adjoint on all bounded ambient vectors, with

\[
 \|K_i a\|_2\le4m\|a\|,\qquad
 \|K_i^*a\|_2\le5m\|a\|,\qquad a\in\widetilde M,
 \quad K_i1=0,\quad K_i^*1=v_i.
 \tag{81}
\]

On the reference polynomial core the commutator identities are [K_i,h]=0 and [K_i,S_j]=delta_ij Theta(beta).
They extend to every bounded ambient vector by bounded polynomial approximation: input vectors converge in L2, the images have the bounds (81), and weak closedness of the original Hilbert graph identifies every weak image cluster with the actual K_i value.
Norm approximation of c by polynomials in h similarly gives [K_i,c]=0 on all bounded vectors.
Since every intermediate input in the following product is bounded, all operator domains are legitimate, and

\[
 [K_i,Y_j]=c[K_i,S_j]c
  =\delta_{ij}\,c\Theta(b\otimes b)c
  =\delta_{ij}P.
 \tag{82}
\]

The last equality uses cb=bc=1 in the affiliated algebra, with the two rank-one vectors c b equal to the actual bounded vacuum.
It does not require b to be bounded.

For the target algebra let Q_Y:L2(tilde M)->L2(P_Y) be the trace-preserving conditional-expectation projection and define T_i a=Q_Y K_i a for a in P_Y.
Every element of P_Y reduces Q_Y, so (82) compresses to [T_i,Y_j]=delta_ij P on P_Y.
For a,q in P_Y, the ambient actual adjoint pairing shows that q is in Dom T_i* and

\[
 T_i^*q=Q_YK_i^*q,\qquad T_i1=0,
 \qquad T_i^*1=Q_Yv_i.
 \tag{83}
\]

Consequently -T_i gives a target dual with both actual bounded-vector domains.
The commutator on the target star polynomial core is Hilbert-Schmidt and is the represented ordinary free derivative of the selfadjoint Y tuple.
Its actual vacuum is Q_Yv_i: pairing [T_i,p]1 with 1 uses (83) and T_i1=0.
Thus A(P_Y;Y) holds.
The original canonical restriction p mapped to (id tensor tau)partial_(Y_i)p is exactly T_i on this core.
Bounded Kaplansky approximation, the bounds (81) and the weakly closed graph of its Hilbert closure put every a in P_Y in that original closure; pairing against the dense P_Y vectors through (83) identifies its value with T_i a.
Its actual adjoint also contains P_Y by (83).
Therefore both specified canonical domains hold, in addition to existence of S and F.

The connection with the C_F0147 tuple is exact only at the following scope:

\[
 X_j=cY_jc^{-1}\quad\text{in }L^0(\widetilde M),
 \qquad
 \tau(p(X_1,X_2))=\tau(p(Y_1,Y_2))
 \tag{84}
\]

for every holomorphic polynomial p.
The trace equality follows by cyclically moving the bounded factors in each word: Y words have outside factors c and inside factors h, whereas X words begin with h.
The affiliated similarity implements the displayed polynomial identity but is unbounded, does not preserve adjoints, and supplies no target-star-core Hilbert or actual-adjoint estimate.
The all-F nonexistence for X and the positive result here are therefore compatible.
The holomorphic vacuum functional agrees for X and Y, but its target H norms and starred corrections remain different.

The exact target-only graph-norm feasibility criterion, independently developed by the reviewer branch, is retained at [D_F0005](Yin_D_F0005.md#an-exact-target-only-functional-reduction), together with its CN21 source interface.
Its full proof is not duplicated here.
The present congruence comparison supplies no estimate for that graph norm on the X target core.

## One hidden factor: actual A and the full forward domain

The complete construction is fixed and independently reviewed in [C_F0150](../claims/Yin_C_F0150_v1.md#statement), with its complete [R_F0156](../audits/reviews/Yin_R_F0156_v1.md#conclusion).
For h=2+s_0 and a free standard semicircular S, the single coordinate X=hS in N=W*(X) has an intrinsic actual target ACSY witness.
Its reference coefficients are

\[
 \alpha(u,v)=\frac{v}{u^2+v^2},\qquad
 \beta(u,v)=\frac{u}{u^2+v^2},\qquad
 \|\alpha\|_2^2+\|\beta\|_2^2\le1.
 \tag{85}
\]

C_F0150 retains the full separated-leg actual-adjoint proof, both reference generator values, the actual whole-star-core vacuum of norm at most sqrt(2), and conditional-expectation compression to the intrinsic target coefficient module.
None of those proofs is duplicated here.
In contrast to the two-coordinate row example, the single-column kernel trace is zero, so C_F0148 gives no obstruction.
The full-N dual and actual forward canonical domain are proved with the recorded self-review in [C_F0152](../claims/Yin_C_F0152_v1.md#statement), adopted with [R_F0160](../audits/reviews/Yin_R_F0160_v1.md#conclusion).
Thus this example satisfies both A and F and is no longer a separating candidate.

Root's bounded-selfadjoint-factorization automatic-continuity argument and exact projective-functional formulation are now adopted at [C_F0151 v2](../claims/Yin_C_F0151_v2.md#statement), with its selected review and assessment owned there.
Version 2 corrects the concrete diffuseness interface.
During development this was the interface in D_F0005.
It constrains every possible bare witness rather than just the supplied canonical contraction; no claim of F existence follows from this constraint.

### The coefficient expansion and the limit of degree summation

Set q(u)=(sqrt(u^2+4)-u)/2, so 1-q(u)^2=u q(u) and 0<q(u)<1 for u>0.
The complete coupled Chebyshev expansion, its coarse Hilbert convergence and the exact finite-output annihilation formula are fixed in [C_F0152 Section 1](../claims/Yin_C_F0152_v1.md#1-the-square-summable-coefficient-expansion-and-exact-contraction).
Its formula (8) performs the indicated right q multiplication after the annihilations.
These proofs are not duplicated here.

Near u=0, q(u)=1-u/2+O(u^2) and dmu_h(u) is comparable to sqrt(u)du.
Consequently ||q(h)^n||2 is comparable to n^(-3/4) for large n: split the integral at a fixed small u, compare q(u)^(2n) with exp(-c n u), and rescale u by n.
The outside interval decays exponentially.
Neither the unweighted sum of these coefficient norms nor C_F0145's sqrt(degree)-weighted sum is finite.
The new cancellation argument of C_F0152 is therefore not an application of that previous summation theorem term by term.

There is also extra integrability: for every 2<p<5/2, alpha,beta belong to Lp(mu_h tensor mu_S).
Their absolute values are bounded by (u^2+v^2)^(-1/2); integrating its pth power in v against the bounded semicircle density gives at most C_p u^(1-p), which is integrable against sqrt(u)du in this range.
No finite-p multiplier theorem is needed in C_F0152.

### Why arbitrary separated-leg vacua are insufficient for a full-domain estimate

C_F0150's adjoint isometries do not give a universal infinity-to-L2 contraction bound for all coefficients in H_h tensor H_S.
Here is a fixed-coefficient obstruction.
Put x=s_0 and choose

\[
 a(2+x)=\frac{1_{\{0<|x|<1/2\}}}
                 {\sqrt{|x|}\log(e/|x|)}.
 \tag{92}
\]

The marginal semicircle density is bounded above and below near x=0, so a is in L2(W*(h)).
The coefficient eta=a(h) tensor 1 belongs to C_F0150's oriented tensor space and has actual reference vacuum partial_h*eta of norm ||a||2.
Its right contraction on scalar polynomials f(x) is

\[
 E_\eta f=(E_h f)a(h),\qquad
 E_h f(x)=\int\frac{f(x)-f(t)}{x-t}\,d\mu_{s_0}(t).
 \tag{93}
\]

Take f_epsilon(x)=x/sqrt(x^2+epsilon^2).
It is increasing and bounded by one.
For |x|<=epsilon/2 and 2epsilon<=t<=1, f_epsilon(t)-f_epsilon(x) is bounded below by 1/sqrt(5), and t-x is at most 5t/4.
The positive divided-difference integral therefore gives E_h f_epsilon(x)>=c log(1/(2epsilon)) for a constant c>0.
The integral of |a(2+x)|^2 over |x|<=epsilon/2 against the semicircle measure is comparable to 1/log(1/epsilon).
Consequently

\[
 \|a E_h f_\varepsilon\|_2^2
      \ge c'\log(1/\varepsilon)\longrightarrow\infty.
 \tag{94}
\]

Choose polynomial approximants to f_epsilon and its derivative on [-2,2] with uniform errors at most one.
Such approximants follow by approximating the continuous derivative uniformly and integrating, with a harmless rescaling of the error.
Their operator norms are at most two, while the divided-difference error in E_h is uniformly at most one.
Multiplication by the fixed L2 a adds only a bounded error to (94).
Thus the original polynomial contraction fails every infinity-to-L2 bound despite its actual vacuum.
The unbounded reference coefficient eta does not normalize a target coordinate and is not an A-to-F counterexample.

The actual alpha,beta of (85) are more regular than this obstruction and are coupled by the normalization equation.
In particular alpha has zero second-leg mean, so E vanishes on the h-only scalar core.
Neither the generic failure nor the square-summable series alone decides F for X; C_F0152 uses their coupled cancellation and an additional partial-block column estimate.

### Complementary one-sided bounds from unique suffix cuts

The following partial bounds use the cut-to-projective-tensor argument of [C_F0145](../claims/Yin_C_F0145_v1.md#argument), with a unique suffix instead of a sum over relative degrees.
Root identified the alpha cut; this branch checked the reverse beta cut and the actual adjoint identities.
They are development checks, not independent review.

Write E_(eta,j)=(id tensor tau) I_eta partial_j on the full reference Wick core.
Let eta lie in H_0 tensor H_1 and j=0.
Cutting a word at a 0 with only 1's after it selects its last 0, so there is at most one such cut.
Consequently the map C_0 from H into H tensor H_1 which retains that prefix and suffix is a contraction: different input words give different prefix/suffix pairs.
If eta=sum_n a_n tensor U_n(S), the contraction is

\[
 E_{\eta,0}p=\sum_n (r_0^*r_1^{*n}p)a_n.
 \tag{95}
\]

The Hilbert tensor C_0 p and the Hilbert tensor eta compose as two Hilbert--Schmidt maps, giving a projective Hilbert tensor of norm at most ||p||2 ||eta||2.
Explicitly, the coefficient map sending e_n to r_0*r_1*^n p and that sending e_n to a_n are Hilbert--Schmidt; their product, with the usual conjugate-Hilbert identification, has trace norm at most the product of their Hilbert--Schmidt norms.
Multiplication H tensor_pi H -> L1(M) has norm at most one by Holder.
Therefore

\[
 \|E_{\eta,0}p\|_1\le\|\eta\|_2\|p\|_2.
 \tag{96}
\]

Initially this is proved for finite expansions; Hilbert convergence of eta and the same bound give it for all eta.
For a fixed polynomial p the cut formula has finitely many suffix degrees, and agrees with the original coarse contraction.
Pairing (96) with every bounded a proves actual, rather than formal, adjoint membership

\[
 M\subset\operatorname{Dom}E_{\eta,0}^*,\qquad
 \|E_{\eta,0}^*a\|_2\le\|\eta\|_2\|a\|.
 \tag{97}
\]

This applies in particular to alpha.
Its codes 0 1^(2k+1) in C_F0152 formula (8) are suffix-free, and the square sum in C_F0152 formula (6) is exactly the coefficient norm in (96).

Interchanging 0 and 1 proves (96)--(97) for eta in H_1 tensor H_0 and j=1, since one cuts at the last 1 before a pure 0 suffix.
Put eta-dagger=flip(eta*) and v_eta=partial_j*(eta*) whenever this is an actual adjoint value.
On the reference core the usual real-reference integration-by-parts identity, checked first for polynomial tensor coefficients, is

\[
 E_{\eta,j}^*a=a v_\eta-E_{\eta^\dagger,j}a.
 \tag{98}
\]

For the separated-leg coefficients used here, their componentwise adjoints and flipped adjoints have actual reference vacua: the insertion-word isometries of C_F0150 apply also with the two labels reversed.
Approximation in those isometric adjoint graphs extends (98) to the present coefficients, on every polynomial a.
In particular v_(beta-dagger)=v_beta* and ||v_beta||2=||beta||2.
Applying (97) to beta-dagger in H_1 tensor H_0 and solving its version of (98) for E_(beta,1) gives

\[
 \|E_{\beta,1}p\|_2
 \le\|p v_\beta^*\|_2+
       \|E_{\beta^\dagger,1}^*p\|_2
 \le2\|\beta\|_2\|p\|.
 \tag{99}
\]

Thus the beta forward contraction has an operator-norm-to-Hilbert bound, whereas the alpha adjoint has the bound (97).
The statement (99) is on the original reference core.
Its closability follows from (98), since the polynomial core belongs to its actual adjoint domain.
Bounded Kaplansky approximation, (99), and the weakly closed graph of that closure put all of M in its actual closure domain, with the same bound.
This is the usual original-core closure argument, not an arbitrary extension.
These estimates alone did not control alpha's forward map.

For the supplied sum E=E_(alpha,0)+E_(beta,1), these preliminary bounds isolated alpha forward and beta adjoint as the missing estimates.
The additional C_F0152 argument now bounds E forward and hence, by subtraction using (99), bounds alpha forward as well.
The beta adjoint estimate remains separate; together with (97) it is exactly what would be needed for the supplied sum's full bounded-vector adjoint domain.
No failure of that estimate has been proved.

### An exact weighted right-annihilation bound at the semicircular edge

The special edge weight h^-1/2 has a useful property that does not hold for arbitrary L2 coefficients such as (92).
Set H_0=rho(h)=2+r_0+r_0* on the full Fock space.
It is positive and injective.
The right creation isometry satisfies the exact bounded identity

\[
 r_0^*H_0r_0=H_0.
 \tag{100}
\]

Define V initially on the dense range of H_0^(1/2) by V(H_0^(1/2)z)=H_0^(1/2)r_0z.
Equation (100) makes V isometric, so it extends to an isometry on H.
The bounded identity V H_0^(1/2)=H_0^(1/2)r_0 and its adjoint give H_0^(1/2)V*=r_0*H_0^(1/2).
Since Dom H_0^(-1/2)=Ran H_0^(1/2), this proves actual domain invariance and

\[
 \|\rho(h^{-1/2})r_0^*z\|_2
 \le\|\rho(h^{-1/2})z\|_2,
 \qquad z\in\operatorname{Dom}\rho(h^{-1/2}).
 \tag{101}
\]

Every bounded p belongs to that domain, with ||p h^-1/2||2<=||p|| since tau(h^-1)=1.
Hence the weighted annihilation itself has an infinity-to-L2 bound.
This proves the actual product-domain assertion in (101), rather than just a quadratic-form estimate.

A related bound is uniform in a single pure-S suffix length.
Let b in L2(W*(h)), and n>=1.
The isometry relation for r_1 gives the finite identity

\[
 r_1^{*n}=\rho(U_n(S))-r_1\rho(U_{n-1}(S)).
 \tag{102}
\]

The map rho(b)r_1 is bounded on all H with norm ||b||2: appending a 1 and then the pure-0 expansion of b gives orthogonal concatenated words, with squared norm ||b||2^2 times the input norm.
For bounded functions of h this formula follows first for polynomials, then by uniformly bounded functional-calculus approximation in L2.
For arbitrary b, use its bounded spectral truncations b_R=b 1_(|b|<=R).
The operators rho(b_R)r_1 converge in operator norm by the same formula.
The spectral-truncation characterization of the closed multiplication operator rho(b) therefore puts every r_1 z in its actual domain and identifies this operator-norm limit with rho(b)r_1.
For bounded p, (102), freeness, and ||U_n(S)||2=1 imply

\[
 \|\rho(b)r_1^{*n}p\|_2\le2\|b\|_2\|p\|.
 \tag{103}
\]

Indeed the first term is p U_n(S)b, whose norm is at most ||p|| ||b||2 by freeness, and the second term is bounded by ||b||2 ||p U_(n-1)(S)||2.
Thus both terms give genuine Hilbert products.
Neither (101) nor the individual bound (103) supplies a uniform weighted column estimate for all suffix lengths simultaneously; summing their constants would diverge.
C_F0152 resolves the required forward estimate by a different column and cancellation argument, without asserting this stronger weighted-column statement.

### A nonreal normalized coefficient choice

The same separated-leg domain theorem permits a different coupled pair.
With gamma(u,v)=1/(u+i v), put alpha'=i gamma and beta'=gamma.
These are Hilbert coefficients by (4) of C_F0150 and satisfy alpha' v+u beta'=1.
Their componentwise adjoints are still in H_0 tensor H_1, so both actual reference adjoints and the target compression work exactly as there.
The canonical contraction on each Wick polynomial is the finite-output series

\[
 E'=\sum_{n\ge0}(-i)^n\rho(q^{n+1})
          (i r_0^*r_1^{*n}+r_1^{*(n+1)}).
 \tag{104}
\]

Its n=0 h-only term has bounded coefficient q.
This is an alternative actual-A witness with potentially different cancellation, not a proof of a full-domain bound or a telescoping identity.
The order of q multiplication is again fixed as in C_F0152 formula (8).

### Fixed full forward-domain result

The complete-block cancellation, centered partial-block bound, exact mean sum and actual closure/compression arguments are fixed in [C_F0152](../claims/Yin_C_F0152_v1.md#argument).
Together they give ||Ep||2<=(sqrt(2)+1+2||beta||2)||p|| on the full reference core and place every bounded vector in the actual forward canonical closure.
The proof then constructs the intrinsic dual on N=W*(hS).
Its selected decision owns the mathematical assessment and exact review adoption; R_F0160 owns the self-reviewed relationship, and the full proof is not retained twice.

The auxiliary one-sided estimates, weighted right-annihilation argument, and alternate nonreal coefficients above are not used to fill an unproved step in C_F0152.
They retain separate useful scope.
In particular the present forward result does not establish a full bounded-vector adjoint domain.
That extra domain is not required for the A-to-F task.
The adopted positive result closes this separating candidate; the general implication still requires a different route.

### Bounded source search for the free-product estimate

A primary-source search led to [MR17, exact inspected scope](../audits/literature/MR17/readme.md).
Its finite-p first/last-factor projection bounds and column estimates are useful neighboring mechanisms.
The source interface sought concerned collapse or replacement of the final free blocks with an h-dependent kernel, not merely a first/last-factor projection multiplier.
No source theorem was verified to give that estimate; C_F0152 instead supplies a direct Fock proof for the specific coupled coefficients.
The existing RX06 inspection concerns fixed-length Khintchine estimates and does not by itself supply a length-uniform bound for this series.
The naive triangle estimate fails by the n^(-3/4) coefficient norms.

The general A-to-F obligation remains outside this concrete positive result.
C_F0151's all-witness bounded-functional criterion remains available for other tuples satisfying its factorization hypotheses.
The reverse canonical bound for this example is separate from the full forward domain established by C_F0152.

## Finite polynomial relations and a weighted row-range target

The next route returns to arbitrary tuples satisfying A.
Let A_0=C<X,X*> and let delta_i be one of its actual ACSY derivations.
For a holomorphic polynomial row P=[P_1(X),...,P_m(X)], write Q=PP*, let p be its matrix kernel projection, and put zeta_j=delta_i P_j.
The latter are finite algebraic tensors with bounded holomorphic polynomial legs, because delta_i X_k=delta_ik 1 tensor 1.
Right matrix multiplication below means the outer right module action, so

\[
 V_k=(\zeta\mathbin{\cdot}p)_k
       =\sum_j\zeta_j\mathbin{\cdot}p_{jk}.
 \tag{115}
\]

Every bounded column a=(a_j) with Pa=0 satisfies a=pa.
Its forced commutator right-hand side is

\[
 g_i(a)=(\mathrm{id}\otimes\tau)
              \sum_j\zeta_j\mathbin{\cdot}a_j.
 \tag{116}
\]

Indeed any full-domain E_i with [E_i,X_k]=delta_ik P obeys E_i(P_j a_j)=P_j E_i(a_j)+Theta(zeta_j)a_j, by the finite holomorphic product rule.
Summing gives P(E_i(a_j))=-g_i(a).
This identity imposes an actual row-range requirement on every possible witness, not only on a chosen canonical contraction.
The entries a_j are not assumed to lie in Dom delta_i.

Here is a sufficient weighted-tensor condition for that one finite relation family.
Suppose Q is regular and

\[
 W_k=(Q^{-1/2}\otimes1)V_k
       \quad\hbox{belongs to }H\otimes_2H
       \quad(k=1,\ldots,m).
 \tag{117}
\]

This is an actual left multiplication domain statement, not yet a conclusion from A.
It implies g_i(a) belongs to Dom Q^-1/2, with

\[
 Q^{-1/2}g_i(a)
 = (\mathrm{id}\otimes\tau)\sum_kW_k\mathbin{\cdot}a_k,
 \qquad
 \|Q^{-1/2}g_i(a)\|_2
 \le\left\|\sum_ka_k^*a_k\right\|^{1/2}
       \left(\sum_k\|W_k\|_2^2\right)^{1/2}.
 \tag{118}
\]

To justify the actual domain, use bounded spectral truncations of Q^-1/2 in the first tensor leg.
They commute with id tensor tau, and their applied V columns converge in the coarse Hilbert space to W.
The bounded outer-right column operator has norm ||sum a_k*a_k||^(1/2), so the truncated images in (118) converge in H.
The spectral-truncation domain characterization gives (118).
If P=Q^(1/2)U is its polar decomposition, U is a coisometry by regularity of Q.
The vector U*Q^-1/2 g_i(a) is in H^m, has image g_i(a) under P, and obeys the same bound.
Thus (117) removes this row's finite obstruction.

The stronger unproved assertion is whether an actual ACSY vacuum forces (117).
The contracted range implication (118) is now obtained by the separate C_F0155 reduction without assuming (117); neither route yet builds one coherent E_i.
Even all separate finite row-range conditions would not automatically supply a single Hilbert-valued extension or the uniform projective bound in C_F0151.
No compactness or injectivity argument filling that step is claimed.
Moreover (117) is deliberately stronger than individual contracted range membership; no necessity of this Hilbert-tensor condition has been proved.

A stronger sufficient interface is actual Sobolev membership of the kernel projection: if each entry of p belongs to Dom closure(delta_i), then (117) follows.
The actual tensor-adjoint formula in [ACSY24-U003, Lemma 3.3](../audits/literature/ACSY24/Yin_U003.md#derivation-adjoint-and-compression) makes delta_i closable without a reality premise.
Take core graph approximants p_n entrywise for p.
Since each zeta_j is a finite sum of bounded polynomial tensor legs, the map zeta_j dot a is bounded from a in H to the coarse Hilbert space.
Thus zeta dot p_n converges to zeta dot p, while P dot delta_i p_n converges to P dot closure(delta_i)p.
The Leibniz identity and Pp_n->Pp=0 in H give, by closability,

\[
 \zeta\mathbin{\cdot}p+
       P\mathbin{\cdot}\overline{\delta_i}(p)=0.
 \tag{118a}
\]

For P=Q^(1/2)U, closed left multiplication by Q^-1/2 then yields W=-U dot closure(delta_i)(p), which is Hilbert.
This proves the conditional implication with actual domains and does not require uniformly bounded graph approximants.
It does not prove the required projection membership.
General spectral projections need not belong to the graph domain of a closed derivation; no functional-calculus argument covering these bounded rational kernel projections has been verified here.
The source's Lemma 3.3 supplies closability only, not that missing domain assertion.

The local reuse pass checked the fixed row obstruction C_F0147, the actual resolvent proof C_F0148, the projective-functional criterion C_F0151 and retained polynomial-matrix/source entries.
No fixed input supplied (117).
A bounded external primary-source search by conjugate variables, polynomial-matrix kernels, free Fisher information, inverse integrability and derivation resolvents located neighboring Stein/Jacobian formulations but no verified weighted-kernel estimate.
No new external theorem is adopted.
The resulting matrix-resolvent and scalar-block route is now fixed in C_F0154 and C_F0155 below; the uncontracted domain condition (117) is a separate, stronger unresolved assertion.

### Fixed positive-compression matrix criterion

The complete matrix affine-pencil theorem and proof are proved and independently reviewed at [C_F0154](../claims/Yin_C_F0154_v1.md#statement), adopted with [R_F0162](../audits/reviews/Yin_R_F0162_v1.md#conclusion).
For L=A_0+sum_i A_i X_i, Q=LL* regular and p=ker L, the sufficient condition is strict positivity of the scalar matrix B=sum_i A_i (id tensor tau)(p) A_i*.
Under that hypothesis the proof gives (Tr tensor tau)(Q^-1)<infinity and an actual Hilbert right inverse on every bounded column.
Its complete original-core matrix Neumann argument, all index contractions, normalized weak tensor proof and polar range formula are not duplicated here.
Root and this branch co-developed it.

For singular B the scalar normalization need not dominate the unweighted inverse trace U_epsilon.
The starred-derivative error retains two unweighted resolvent-column legs, so merely replacing U_epsilon by a weighted trace does not reproduce the estimate.
C_F0155 supplies a scalar-block reduction for the contracted finite-relation right-hand sides and removes that finite obstruction without proving (117).
The stronger uncontracted weighted-domain assertion remains separate.

### Fixed finite polynomial-relation result

The complete scalar-null block reduction, rectangular finite-rank-cycle and trace argument, actual compressed polar inverse, and bounded polynomial-linearization transfer are proved with the recorded unknown-relationship review at [C_F0155](../claims/Yin_C_F0155_v1.md#statement), adopted with [R_F0163](../audits/reviews/Yin_R_F0163_v1.md#conclusion).
For every holomorphic polynomial matrix P and bounded column a with Pa=0, it supplies a Hilbert column z with Pz=-g_i(P,a).
For fixed P,i this choice is bounded and linear in a.
The complete proof is not duplicated here.

This contracted range result bypasses the unproved weighted-tensor assertion (117).
It does not assign compatible values across different matrices or bound their constants uniformly.
Thus a separating example, if one exists under A, cannot be explained by a single finite polynomial-relation range obstruction of this form.

### Finite-rank interpolation of all finite commutator tests

C_F0155 yields a precise finite-to-global interface without a compactness conclusion.
Fix a finite set F of bounded vectors in M.
Make one finite list a_1,...,a_m containing 1, F, and every X_j a for a in F and j=1,...,d.
Include a basis of all complex scalar linear relations among this list as constant rows of a polynomial matrix P.
Also include for each requested product X_j a=a_k the affine row encoding X_j a-a_k=0.
Thus P a=0 holds exactly.

For a fixed i, C_F0155 supplies output vectors z_1,...,z_m obeying Pz=-g_i(P,a).
Its constant rows force every scalar linear relation among the a_k to hold among the z_k.
Its product rows give z_(X_j a)-X_j z_a=delta_ij tau(a)1.
Let eta be the output assigned to the listed vector 1 and replace every z_k by z_k-a_k eta.
All scalar and affine equations remain valid because Pa=0, and the new output at 1 is zero.

The resulting assignment defines a complex-linear map on the finite-dimensional Hilbert subspace V_F=span{a_1,...,a_m} in H.
It is bounded for the Hilbert norm because its domain is finite dimensional.
Extend it to H by composing with the orthogonal projection onto V_F.
This gives a bounded finite-rank Hilbert operator E_(i,F) with
\[
 E_{i,F}1=0,\qquad
 [E_{i,F},X_j]a=\delta_{ij}\tau(a)1
       \quad(a\in F,\ j=1,\ldots,d).
 \tag{119}
\]
The construction is simultaneous in every scalar relation among the listed inputs, rather than independently prescribing inconsistent values.
For all i one repeats the construction using the same list and relation matrix.
Directed by inclusion of finite F, the commutator values on each fixed bounded vector are eventually exactly correct.

The norms of E_(i,F), whether on H or from M in operator norm to H, are not controlled uniformly by this argument.
If a uniform M-to-H bound were obtained, the exact bounded-functional criterion of [C_F0151 v2](../claims/Yin_C_F0151_v2.md#statement) would give a bounded full-domain witness: any finite projective-tensor test uses finitely many input vectors, so select one F covering them and estimate its forced functional by that common bound.
The present finite interpolation gives no such estimate.
In particular eventual exactness of the commutators does not imply convergence, or even pointwise boundedness, of E_(i,F)a itself.

There is an elementary one-operator module caution.
On H=ell2(N), let T e_n=2^(-n)e_n.
Consider the equations
\[
 (T-2^{-n}I)y_n=x-e_n\qquad(n\ge1).
 \tag{120}
\]
Every finite subsystem is solvable: take x to be the sum of the corresponding basis vectors, and invert T-2^(-n) on e_n-perp for each requested n.
This inverse is bounded on that subspace because the remaining eigenvalues stay a positive distance from 2^(-n).
But the full system forces the nth coordinate of x to equal 1 for every n, impossible for x in ell2.
Thus finite consistency over the one-generator algebra C[t] does not itself give a Hilbert-valued solution.
This is an atomic example, not an ACSY example or a counterexample to A implies F; H is not asserted to be finitely generated as a C[t]-module.

The next exact bare-domain obligation is joint finite feasibility with one fixed choice of pointwise finite radii, as the equivalence below makes precise.
A bounded projective-functional estimate is a stronger sufficient route.
Neither follows from the separate finite-result constants.
No new unrelated example or additional adjoint-domain requirement is needed for this step.

### An exact pointwise-radius criterion for bare full-domain duals

This reduction applies to any bounded finite tuple X in a finite tracial algebra M; it needs neither normality nor the actual ACSY premise.
Identify M with M Omega inside H=L2(M).
The bare full-domain condition F is equivalent to the following statement:

There are functions r_i:M->[0,infinity), finite at every a, such that for every finite subset F_0 of M there are bounded finite-rank Hilbert operators E_(i,F_0):H->H satisfying
\[
 E_{i,F_0}1=0,\qquad
 [E_{i,F_0},X_j]a=\delta_{ij}\tau(a)1
       \quad(a\in F_0,\ 1\le j\le d),
 \qquad
 \|E_{i,F_0}a\|_2\le r_i(a)\quad(a\in F_0).
 \tag{130}
\]
The radii are fixed before the finite sets are selected.
They may depend arbitrarily on the individual input a; no inequality r_i(a)<=C_i||a||, no common bound on operator norms, and no Hilbert-space continuity of the eventual witness is required.

**Necessity.** Given a bare generator-first dual D_i:M->H, normalize
\[
 E_i(a)=-D_i(a)+aD_i(1),\qquad E_i(1)=0,\qquad
 [E_i,X_j]a=\delta_{ij}\tau(a)1.
 \tag{131}
\]
The bounded left multiplication of the Hilbert vector D_i(1) is defined for every a in M, and this right-multiplier correction commutes with each left X_j.
Set r_i(a)=||E_i(a)||2, which is finite pointwise without a continuity assertion.
For fixed finite F_0, take V=span({1} union F_0 union all X_j F_0) inside H.
The restriction E_i|V is a linear map on a finite-dimensional Hilbert space, hence bounded.
Its composition with the orthogonal projection H->V is a bounded finite-rank Hilbert operator.
It agrees with E_i on every a and X_j a needed in (130), and at 1.
Thus (130) holds with the same fixed radii, indeed with equality of its listed values to E_i(a).

**Sufficiency.** For each pair (i,a), let K_(i,a) be the weakly closed Hilbert ball of radius r_i(a).
Form
\[
 \mathcal K=\prod_{i=1}^d\prod_{a\in M}K_{i,a}
 \tag{132}
\]
with its product of weak topologies.
Each factor is nonempty and compact, and the full product is compact.
The exact standard interfaces are [Keh25-U001](../audits/literature/Keh25/Yin_U001.md#keh25-u001): arbitrary compact products, closed-set finite intersection, and weak compactness of Hilbert balls through Banach--Alaoglu and the already checked Hilbert representation.
No separability or sequential compactness is assumed.

For a point y=(y_(i,a)) in this product, impose all the following equations:

- y_(i,1)=0;
- y_(i,lambda a+mu b)=lambda y_(i,a)+mu y_(i,b), for every a,b in M and lambda,mu in C;
- y_(i,X_j a)-X_j y_(i,a)=delta_ij tau(a)1, for every a in M and all i,j.

Each is a closed condition in K.
It involves only finitely many coordinate projections, complex linear combinations are weakly continuous, and left multiplication by a bounded X_j is weakly continuous on H.
Equality with a fixed vector is weakly closed because the Hilbert weak topology is Hausdorff.

These closed conditions have the finite intersection property.
For any finite collection of them, collect every input appearing as a coordinate into a finite set G.
In particular include all the specific a,b,lambda a+mu b and X_j a that occur, and 1 if necessary.
Apply (130) with F_0=G.
Set y_(i,a)=E_(i,G)a for a in G, and set every coordinate outside G equal to zero.
The radius bound in (130) puts the entire assignment in K, including the zero coordinates.
Since the Hilbert operators are genuinely complex linear, all requested linearity equations hold; normalization and the requested commutators hold by (130).
Enlarging G does not require closure under every scalar combination, only inclusion of the finitely many combinations in the chosen constraint collection.

Compactness now supplies a point satisfying all these equations simultaneously.
Define E_i(a)=y_(i,a).
The full family of scalar relations makes E_i a complex-linear map on all M, its value at 1 is zero, and its all-bounded-vector commutators are exactly those in (131).
Moreover ||E_i(a)||2<=r_i(a).
Taking D_i=-E_i proves bare F.
No closure, adjoint, or norm continuity is inferred.

This equivalence separates what C_F0155 already gives from what is missing: C_F0155 proves (130) with no prescribed radii, allowing the output sizes to change with the finite test set.
To conclude bare F it suffices, and is necessary, to choose pointwise finite radii which work for every finite set.
A uniform M-to-H estimate is a stronger sufficient specialization, corresponding to r_i(a)=C_i||a||, and is not the exact target for arbitrary tuples.

The requirement is joint: for each finite set, one family of interpolating operators must satisfy every one of its prescribed radius bounds simultaneously.
Separate per-vector infimum bounds, obtained from different feasible operators for different vectors, do not establish this finite intersection property and are not substituted for it.

There is no application of uniform boundedness to upgrade the pointwise-radius condition.
The finite interpolating operators need only satisfy the radius at a when a belongs to the selected finite set, and their operator norms may vary without bound.
The compact product constructs a possibly discontinuous algebraic map with the stated pointwise bounds.
The necessity argument itself shows why replacing those bounds by a uniform norm estimate would impose an additional condition beyond the bare formulation.

### An equivalent estimate on every affine relation

The pointwise criterion has the following exact dual formulation.
This is a self-checked development, proposed by root and checked here, with no ACSY-to-F implication asserted.
Let X be any bounded finite tuple in a finite tracial von Neumann algebra M and H=L2(M); neither normality nor generation is needed for this equivalence.
Inner products are linear in the second variable.

Bare F holds if and only if there exist functions r_i:M->[0,infinity), finite at every bounded a and satisfying r_i(1)=0, such that the following estimate holds simultaneously for every i, all positive integers n,m, every scalar-coefficient affine pencil L=A_0+sum_j A_j X_j of size n by m, every bounded column a=(a_l) in M^m with La=0, and every eta in H^n:

\[
 \left|\left\langle\eta,A_i\tau(a)\right\rangle\right|
 \le \sum_{\ell=1}^m
          r_i(a_\ell)\,\|(L^*\eta)_\ell\|_2 .
 \tag{133}
\]

Here tau(a) is the scalar column of entrywise traces, embedded in H^m by the vacuum, and L and L* act by bounded left multiplication.
The radii are chosen once, before the pencil, column, or test vector.
The same radius is used whenever the same bounded element appears in different relations.
No norm bound on r_i is required.

For necessity normalize a bare witness as in the preceding criterion, obtaining E_i1=0 and [E_i,X_j]a=delta_ij tau(a)1 on M, and put r_i(a)=||E_i a||2.
Apply E_i entrywise to La=0.
Its complex linearity and the commutator identities give

\[
 L(E_i a_\ell)_{\ell=1}^m=-A_i\tau(a).
 \tag{134}
\]

Pairing with eta and applying Cauchy--Schwarz separately in each coordinate gives (133).
This proof uses neither continuity nor an adjoint of E_i.

For sufficiency first fix L,a,i and put c=-A_i tau(a).
Let

\[
 K=\prod_{\ell=1}^m
       \{z_\ell\in H:\|z_\ell\|_2\le r_i(a_\ell)\},
 \qquad \mathcal K=L(K)\subset H^n .
 \tag{135}
\]

Each factor of K is weakly compact by the Hilbert-ball interface already inspected in [Keh25-U001](../audits/literature/Keh25/Yin_U001.md#keh25-u001).
The bounded map L is weakly continuous, so cal K is nonempty, weakly compact, convex and balanced.
Its real support function is exactly

\[
 \sup_{k\in\mathcal K}\operatorname{Re}\langle\eta,k\rangle
 =\sum_{\ell=1}^m r_i(a_\ell)\|(L^*\eta)_\ell\|_2 .
 \tag{136}
\]

Indeed the pairing separates into independent ball coordinates.
For a nonzero coordinate (L*eta)_l the maximum is attained by z_l=r_i(a_l)(L*eta)_l/||(L*eta)_l||2; a zero coordinate contributes zero.
Thus the formula also covers zero radii and complex Hilbert spaces.

If c were outside cal K, the weakly lower semicontinuous function k mapped to ||c-k||2 would attain its minimum at some k_0 in cal K.
Its minimum would be positive.
Convexity and differentiation along the segment from k_0 to k show, for eta=c-k_0, that Re<eta,k-k_0><=0 for every k in cal K.
Consequently

\[
 \operatorname{Re}\langle\eta,c\rangle
 =\operatorname{Re}\langle\eta,k_0\rangle+\|\eta\|_2^2
 >\sup_{k\in\mathcal K}\operatorname{Re}\langle\eta,k\rangle .
 \tag{137}
\]

But (133), unchanged by the minus sign in c, says that the absolute value of <eta,c> is at most (136), a contradiction.
Therefore c lies in cal K.
In particular (134) admits one solution z with all bounds ||z_l||2<=r_i(a_l) simultaneously.
This is an actual Hilbert-valued solution; no closure of the range L H^m is substituted for that range.

It remains to verify that this family of bounded solutions yields the finite interpolants in the preceding criterion.
Given a finite F subset M, list 1, the elements of F, and every X_j a with a in F as a finite column b=(b_1,...,b_m), with b_1=1.
Repeated entries cause no problem.
Include as constant rows of an affine pencil every member of a basis of the finite-dimensional scalar relation space {lambda in C^m:sum_l lambda_l b_l=0}.
For each a in F and each j, include the row with X_j at the selected position of a and -1 at the selected position of X_j a.
Combining these finitely many rows gives an affine pencil L with Lb=0.
A zero row may be added when needed to make its row size positive.

Apply the solution conclusion of (133) to this one pencil and the column b.
Its constant rows force the assigned z_l to respect all scalar linear relations among the b_l.
Its other rows give z_(X_j a)-X_j z_a=delta_ij tau(a)1.
Since ||z_1||2<=r_i(1)=0, the assignment defines a normalized complex-linear map on span{b_l}.
Extend it to H by composing with the orthogonal projection onto this finite-dimensional span.
The resulting operator is bounded and has finite rank, satisfies every required commutator on F, and has ||E_(i,F)a||2<=r_i(a) for all a in F.
Perform this construction for each i.
The preceding pointwise-radius compactness proof now gives a bare full-domain dual.
This establishes the equivalence, including joint feasibility and normalization.

Estimate (133) is the next exact forcing estimate to seek from actual ACSY data.
[C_F0155](../claims/Yin_C_F0155_v1.md#statement), using [C_F0154](../claims/Yin_C_F0154_v1.md#statement) on the relevant scalar compression, supplies a Hilbert solution for every fixed affine relation and a bound that can depend on its pencil.
A fixed solution gives a support estimate with its own coordinate norms, but does not furnish one choice of r_i(a) valid for all pencils and all bounded relation columns.
[L_F0055, equations (124)–(129)](../ledger/Yin_L_F0055_v1.md#weighted-forcing-and-the-uniform-trace-shortcut) further show why replacing the actual forcing geometry by a uniform weighted inverse-trace bound loses necessary information.
Criterion (133) retains the exact coordinate radii and is equivalent to bare F; it does not impose a global operator-norm estimate, and it has not yet been deduced from A.

### Simultaneous solutions on finitely generated holomorphic modules

Under the actual ACSY hypothesis, [C_F0200](../claims/Yin_C_F0200_v1.md#statement) gives a normalized \(E_i:V_b\to H\) for every finite or countable list of bounded inputs containing \(1\), where \(R=\mathbb C\langle X\rangle\) and \(V_b=\sum_k Rb_k\).
For a fixed \(i\), write \(E=E_i\) and use \(g_i(p,b)=(\mathrm{id}\otimes\tau)((\partial_i p)\cdot b)\) as in its [finite-module construction](../claims/Yin_C_F0200_v1.md#finite-modules-and-all-their-polynomial-relations).
On this module the pointwise radii \(\|E(v)\|_2\) satisfy (133) simultaneously for all relation columns with entries in \(V_b\), irrespective of the word lengths.

There is a domain on which these local solutions glue uniquely.
Take all bounded columns \(u\in M^k\) such that \(Pu=q\) for some holomorphic polynomial matrix \(P(X)\) injective on \(H^k\) and some polynomial column \(q(X)\).
Let \(V\) be the left \(R\)-module generated by all entries of all such columns and by \(1\).
For each finite list of columns, apply the finite-module theorem to all of their entries together with \(1\).
On the polynomial algebra every normalized solution has the prescribed value \(E(p)=g_i(p,1)\).
On each listed column the identity \(P E(u)=g_i(q,1)-g_i(P,u)\) follows by the product rule.
Injectivity prescribes \(E(u)\) uniquely among Hilbert columns.
Any two normalized local solutions therefore agree on the left module generated by the columns common to their lists, by the polynomial commutator recursion.
Any two representations of one element of \(V\) can be compared in the module for the union of their finite lists.
This gives a single normalized solution on \(V\).
For example, \(V\) contains every bounded \(p(X)^{-1}q(X)\) with \(p(X)\) regular and \(p,q\in R\), even when \(p(X)^{-1}\) is unbounded.

For general inclusions \(V_b\subset V_{b'}\), restricting normalized solutions from the larger module need not yield every normalized solution on the smaller one.
This already occurs for one standard semicircular \(X\) with law \(\mu\) and \(M=L^\infty(\mu)\).
It has actual conjugate variable \(X\) and a global normalized solution \(E_0\) by the [semicircular conjugate interface](../audits/literature/Voi98/Yin_U003.md#voi98-u003) and [C_F0022](../claims/Yin_C_F0022_v1.md#statement).
Put \(e=1_{(0,\infty)}(X)\) and take \(V_b=R1+R(Xe)\subset V_{b'}=R1+Re\).
Both displayed sums are direct because restriction to the negative open half of the support first kills the polynomial coefficient of \(1\), and restriction to the positive open half then kills the second coefficient.
On \(V_b\) add to \(E_0\) the \(R\)-linear map \(h\) specified by \(h(1)=0\) and \(h(Xe)=1\).
If the resulting normalized solution extended to \(V_{b'}\), the difference \(h'\) from \(E_0\) there would satisfy \(X h'(e)=1\).
The semicircular density is positive near zero, so \(\int |x|^{-2}\,d\mu(x)=\infty\) and this equation has no Hilbert-space solution.
Affiliated multiplication does produce \(X^{-1}\), illustrating the loss of the required Hilbert-valued range when attempting to glue arbitrary choices through the skew field.
The global \(E_0\) itself still exists in this example.

### Stabilization of the closed restriction images on a fixed finite column

[C_F0200](../claims/Yin_C_F0200_v1.md#closed-restriction-images) proves stabilization on each fixed finite column and constructs compatible solutions throughout any one countably generated module.
Its [arcsine example](../claims/Yin_C_F0200_v1.md#diffuse-scalar-laws-and-the-arcsine-obstruction) admits such solutions on every countably generated module and excludes a full-domain dual.
For the actual ACSY tuple the unresolved step in (133) is to choose radii on all of \(M\) simultaneously.

### Finite-degree growth of both tests for the arcsine law

Consider the arcsine coordinate \(X=\cos\theta\) with \(d\theta/\pi\) on \((0,\pi)\).
The two optimal tests of [C_F0201](../claims/Yin_C_F0201_v1.md#statement) already detect the obstruction at a quantitative rate in degree.
Use \(T_m(\cos\theta)=\cos(m\theta)\), with the normalized polynomial dual \(E_0(T_m)=U_{m-1}\) and \(\|U_{m-1}\|_2=\sqrt m\) from [C_F0200](../claims/Yin_C_F0200_v1.md#diffuse-scalar-laws-and-the-arcsine-obstruction).
For \(n\ge1\) one has
\[
 \alpha_{1,n}^2=2\lceil n/2\rceil+1,
 \qquad \beta_{1,2m}\ \ge\ \sqrt m/2\quad(m\ge1).
\]
Indeed the vacuum pairing of the ordinary scalar difference quotient on \(T_m\) is \(\tau(U_{m-1})\), equal to one for odd \(m\) and zero for even \(m\).
For the latter evaluation, the exponential expansion of \(U_{m-1}\) pairs opposite frequencies to cosines, each with zero integral except for the constant.
On the holomorphic degree-\(n\) tests the formal starred cuts vanish, so (1) in C_F0201 tests precisely this functional on \((V_n,\|\cdot\|_2)\).
Its Riesz vector is \(\xi_n=2\sum_{1\le m\le n,\ m\ {\rm odd}}T_m\) by cosine orthogonality, and \(\|\xi_n\|_2^2=2\lceil n/2\rceil\).
These holomorphic tests force the projection of any representing vacuum vector onto \(V_n\) to equal \(\xi_n\).
The formal degree-one relation \(y-x\) has zero evaluated value, unstarred cut \(-1\otimes1\) and starred cut \(1\otimes1\).
Its vacuum identity forces the starred derivative vector to pair to one with \(1\otimes1\), giving squared norm at least one in the other, orthogonal Hilbert summand.
Finite-dimensional Riesz representation on the degree-\(n\) image in (1) therefore gives the sum of these lower bounds for \(\alpha_{1,n}^2\).
For an arbitrary formal star word of degree at most \(n\), identifying both letters with \(X\) turns its ordinary scalar derivative into the sum of its two evaluated word cuts.
Consequently \(\xi_n\) and the starred derivative value \(1\otimes1\) obey the finite vacuum identity, giving the upper bound.

For the second test take any feasible finite map \(T\) in C_F0201 (2) at level \(2m\) and a vector \(h\in V_{m-1}\).
For any one-variable polynomial \(p\) of degree at most \(m\), iterating (2) gives
\[
 \langle h,T(p(X))\rangle
 =\langle p(X)^* h,T(1)\rangle+\langle h,E_0(p(X))\rangle.
\]
For a monomial each application removes one factor \(X\) from its argument and transfers that factor to the test vector.
During the iteration its degree stays at most \(2m-1\), so the weak relations and every inner product used are within the finite test.
Extend by complex linearity, retaining the adjoint on the first leg.
Choose \(p=T_m\) and \(h=U_{m-1}/\sqrt m\).
As \(\|p(X)\|_M=1\) and \(\|h\|_2=1\), the two terms involving \(T\) each have absolute value at most its norm from \(V_{2m+1}\) with the operator norm into \(H\).
The remaining pairing is \(\sqrt m\), proving the claimed lower bound for the infimum with unrestricted \(T(1)\).
Thus this law fails both uniform tests even though all of its countably generated modules have algebraic solutions.

### Why a fixed finite-tensor approximation does not give uniform absorption

Root proposed approximating the fixed starred derivative tensors K_ij=delta_i X_j* by finite sums of bounded elementary tensors.
The exact matrix expression makes the remaining conditioning visible.
In C_F0154's notation put M_i=V_epsilon A_i*.
Its entire starred error can be grouped as

\[
 \sum_{i,j}\left\langle K_{ij}^*,
        \sum_{r,b}(M_j)_{rb}\otimes(M_i)_{br}\right\rangle.
 \tag{121}
\]

This follows by substituting delta_i(L_bl*)=sum_j conjugate(A_j[bl]) K_ij into C_F0154 formula (4) and summing the constant coefficients.
For finite elementary approximants with Hilbert errors e_ij, Cauchy--Schwarz in the matrix entries gives the rigorous tail estimate

\[
 |\mathrm{tail}_\varepsilon|
 \le \sum_{i,j}e_{ij}\|M_j\|_2\|M_i\|_2
 \le U_\varepsilon\sum_{i,j}e_{ij}\|A_i\|\|A_j\|.
 \tag{122}
\]

The comparison T_epsilon>=lambda_min(B) U_epsilon therefore permits absorption only after the coefficient-weighted error sum is small relative to lambda_min(B).
Density of bounded elementary tensors gives such approximants for each fixed pencil.
It does not give one fixed approximation sufficient for every pencil.

This loss already occurs for fixed dimensions and uniformly bounded pencil norms.
In the one-coordinate situation choose L_t=[X-z,t], 0<t<=1.
Its derivative coefficient is [1,0] of norm one; Q_t is boundedly invertible, while its scalar compression is

\[
 B_t=\tau((p_t)_{11})
     =t^2\tau\bigl(((X-z)^*(X-z)+t^2)^{-1}\bigr)
       \longrightarrow0
 \tag{123}
\]

whenever X-z is regular.
The latter follows under A from its maximal-Delta affine-polynomial interface.
The displayed limit is bounded spectral convergence to the kernel projection, which is zero.
Therefore a fixed strictly positive Hilbert approximation error cannot satisfy the absorption threshold for all t.
This only diagnoses (122): it is not failure of a global dual or a proof that all refined approximation arguments fail.
If the starred tensors are themselves finite elementary sums, the approximation tail is zero and this particular issue does not arise.

### The forcing vector retains a covariance weight

The [fixed weighted-forcing account](../ledger/Yin_L_F0055_v1.md#weighted-forcing-and-the-uniform-trace-shortcut) retains the ellipsoid estimate and the exact scalar law where the sufficient weighted trace diverges while the worst minimum solution norm stays controlled.
It does not refute an estimate sensitive to the full bounded-column forcing set; the general finite-to-global implication remains unresolved.

## Corrected projective-symmetry source and the separate extension limit

A bounded search for inverse-closed projective tensor algebras found Kumar--Rajpal, *Symmetry and quasi-centrality of operator space projective tensor product*, [registered KR12 source and inspection](../audits/literature/KR12/readme.md), arXiv:1205.1679v1, 8 May 2012.
Its universal symmetry assertion cannot be used: the later primary [LSW24b-U001 correction](../audits/literature/LSW24b/Yin_U001.md#lsw24b-u001), verified by root, gives symmetry of the Banach projective tensor product of two C*-algebras exactly when at least one factor is type I.
Thus the general projective-symmetry justification for inverting this Q+i is unavailable, even when h^{-1} is bounded.

The original concrete concern was the use of a two-sided-ideal lemma in an abbreviated proper-left-ideal argument.
That concern triggered the correction search; it is no longer recorded as an unresolved search for the validity of the universal assertion.
Nonsymmetry alone does not decide projective invertibility of the particular Q+i in C_F0142.
That special inverse, the two actual vacuum tests, and the arbitrary bare-F question remain separate.
C_F0142 uses none of the invalid universal theorem.

A second search for derivation extension to affiliated operators found Thom, *L2-cohomology for von Neumann algebras*, [registered Tho08 source and inspection](../audits/literature/Tho08/readme.md), arXiv:math/0601447v2, 15 March 2006.
Definition 5.3 on p.10 and Theorem 5.8 on p.13 were read together with Theorems 4.3-4.5 and the extension's stated target.
Its closability is from operator norm to convergence in measure, and the target is the algebra M_A generated by the specified matrix-level abelian weak-closure procedure.
Hilbert-space closability of an ACSY derivation does not immediately verify this norm-to-measure hypothesis: a sequence of derivative values can converge in measure without a bounded Hilbert norm.
Thus the source does not currently extend an arbitrary ACSY witness through h^{-1}, and no theorem from it is used.
The target polynomial relation in C_F0142 resolves uniqueness here without that extension.

## Finite inverse probe and its limits

[Computation J_F0008](../computations/programs/Yin_J_F0008/readme.md) retains the complete seeded complex128 probe, native program and output for 30 finite coefficient-algebra cases, with n=8,12,16,24,32, h quantile powers 0.8,1,1.2, and S a centered or +3 shifted GUE sample.
All original and weighted equation residuals were below 6.2e-14; all 15 positive-S norm controls passed.

For centered S and power 1.2, the normalized weighted U norm changed from approximately 1.19 to 1.52 between n=8 and n=32, whereas the unweighted V norm changed from approximately 8.82 to 54.25.
This supports testing the unweighting separately from the weighted range, but proves neither an infinite-size divergence nor any free-limit transfer.
The finite matrix inputs have atoms and are not admissible actual free-difference-quotient or full-domain-dual examples.
In particular a large finite inverse norm does not show failure of C_F0142's target vacuum tests, whose generator values remain bounded by the exact resolvent identity.

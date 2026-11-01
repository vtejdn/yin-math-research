---
author: Yin
---
# Independent review of actual-vacuum and strong-domain equivalence for a singular coordinate change

Review performed and recorded: 2026-10-14T17:45.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0138 v1](../../claims/Yin_C_F0138_v1.md).
Root assigned the fixed candidate and disclosed the author's preparation and root's input-weight suggestion.
No author D material, preparation discussion or informal derivation was read.
The reviewer read the complete fixed candidate selected by its initial decision dated 2026-10-14T17:37 and the exact three direct dependency interfaces before forming this conclusion.
The reviewer earlier independently reviewed C_F0136; its accepted fixed output-weight theorem is reused here at that actual scope, while the new input-weight argument and the complete assembly are checked separately below.

This finding covers the whole statement and all six proof sections, including necessity for arbitrary A witnesses, the actual weighted polynomial approximation, both unbounded reference-product domains, the output and input estimates, restoration of K and its actual adjoint on M, the two coordinate corrections, and reconstruction of A from arbitrary S witnesses.
It is not a proof of a converse from F or a general nonnormal A-to-F theorem.

Dab10-U002 is used for its stated selfadjoint reference operators, actual domains and core-adjoint identities; C_F0136 supplies the accepted output estimate and the exact core-energy/analytic-series mechanism.
Only the universal Hilbert--Schmidt tensor identification is taken from C_F0070.
Its normal-tuple inference is not invoked for the nonnormal target.
The accepted inputs retain their original source-inspection limits; no new original-PDF or recursive predecessor-proof audit is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0138 statement](../../claims/Yin_C_F0138_v1.md#statement) | Exact finite-Fisher selfadjoint reference assumptions and positive regular h; A iff S iff b and b xi_S in L2, implication to F only, explicit actual vacua, both K-domain bounds and the supplied coordinate operators. |
| [Conclusion](#conclusion) | [C_F0138 argument](../../claims/Yin_C_F0138_v1.md#argument) | Complete Sections 1-6, including all-witness star-relation necessity, weighted polynomial approximation, actual E/E* product graphs, input/output estimates, two-domain restoration and arbitrary-strong-witness tensor reconstruction. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Sections 1-3 at the joint selfadjoint conjugate premise: represented real free difference quotients, their specified canonical closures, core adjoint identity and both actual M domains for E and B_h with operator-norm-to-L2 bounds. No bounded-H extension is required. |
| [Conclusion](#conclusion) | [C_F0136](../../claims/Yin_C_F0136_v1.md#statement) | Positive affiliated kernel-output estimate with both product integrability assumptions, and its exact core energy identity/first-derivative analytic-unitary passage used to derive the new input estimate. |
| [Conclusion](#conclusion) | [C_F0070 tensor interface](../../claims/Yin_C_F0070_v1.md#statement-and-interfaces) | Only the universal unitary map from H tensor H to Hilbert--Schmidt operators and its outer-action/vacuum compatibility. The normality-dependent theorem and phase formulas are not imported. |

## Reference operators, generation and one weighted approximation

The bounded selfadjoint generating pair with actual joint L2 conjugates satisfies the Dab10-U002 premises.
It supplies the represented algebraic difference quotients, the specified closures E and B_h, the actual domains of each operator and adjoint containing M, and the full-M commutators in (6).
Their extension from the reference polynomial core uses the retained bounded-set weak continuity.
Neither reference operator is assumed bounded on H.
The actual core formula E*q=q xi_S-Eq has its correct right-contraction order.

Generation of the target tuple is independent of inverse integrability: the bounded cuts c_n=h inverse 1_[1/n,infinity)(h) satisfy c_nY=e_nS and e_n tends strongly to 1.
Thus W*(h,Y)=M and A_X is dense in H.
Positivity and regularity ensure the inverse exists in the finite affiliated algebra and the zero spectral projection vanishes.

The simultaneous approximation in Section 1 is valid even for unbounded xi_S.
The positive normal functional with L1 density xi_S squared restricts to a finite positive measure nu on the spectral algebra of h.
For bounded real spectral f,

\[
\|\xi_S f(h)\|_2^2=\int |f|^2\,d\nu.
\]

For the unbounded inverse this identity extends by its bounded spectral cuts and the actual product-domain condition.
Selfadjointness gives (b xi_S)*=xi_S b and equality of the L2 norms, so the two assumed conditions place 1/t in L2(mu+nu).
Neither measure has an atom at zero, because the corresponding spectral projection is zero.
Real polynomials are dense for this finite compactly supported real measure; they may be chosen to approximate 1/t simultaneously in both measures.

Consequently the same selfadjoint c_n in C[h] converges to b in H and satisfies xi_S c_n tending to xi_S b in H.
Taking the tracial adjoint gives c_n xi_S tending to b xi_S.
No uniform operator-norm bound on c_n is needed or used in the later graph passages.
The argument never cyclically permutes an uncontrolled product of two unbounded operators.

## Necessity for every ACSY witness

Take any Y-coordinate derivation delta of an A(X) witness, with actual vacuum v.
Its values on h and Y are fixed.
Differentiating the represented relation Yh=hY* gives

\[
(h\otimes1)\delta(Y^*)=1\otimes h.
\]

Slicing the second tensor factor against h is a bounded Hilbert slice.
The resulting w in H satisfies h w=norm(h)_2 squared times 1.
The scalar is nonzero because h is positive regular.
Thus regularity forces b in H.
The first-leg operator h tensor 1 is injective on H tensor H, so the relation uniquely determines delta(Y*)=b tensor h.
There is no step applying an unbounded tensor inverse without first establishing its image as a Hilbert tensor.

The bounded inner map I_(h tensor 1) commutes with both outer actions.
Its composite with delta agrees with partial_S on h,Y,Y*: its respective values are zero, h tensor 1 and 1 tensor h.
These elements generate the represented A_X, so the derivations agree on that whole algebra.

For every p in A_X, delta(hp)=h dot delta(p).
The actual vacuum pairing therefore gives

\[
\langle h\otimes1,\delta(p)\rangle
=\langle v,hp\rangle=\langle hv,p\rangle.
\]

This proves actual membership of h tensor 1 in Dom delta* and its value hv.
Pairing the derivative equality with the vacuum then identifies hv with xi_S on the dense A_X.
Hence v=b xi_S is an actual H vector.
This derives both integrability requirements from every possible A witness.
It uses neither functional-calculus extension of delta nor a prior full-domain dual.

## Integrability gives actual reference and target vacua

For the simultaneous polynomials c_n, the reference derivative and contraction vanish, and the core adjoint formula gives E*c_n=c_n xi_S.
Both graph coordinates converge by the joint approximation.
Closedness of E* therefore proves b in Dom E* and E*b=b xi_S for the original adjoint, independently of the later input-weight estimate.

The insertion u tensor v mapped to u b tensor v is defined on the finite polynomial derivative values, because u is bounded and b is L2.
It commutes with the outer actions.
The insertion eta tensor v mapped to eta tensor S v has the same compatibility and is bounded.
Composing these with the represented reference derivatives gives the two actual derivations in (13).
Their restrictions to A_X respect its relations; hb=1 verifies the prescribed coordinate values.

Their actual right contractions are K_0p=(Ep)b and B_hp-K_0(pS)+pb.
The second formula follows from the product rule and cyclicity of the scalar trace on the second tensor leg; its final sign is positive.
Pairing K_0p against 1 equals pairing Ep against b, now known to lie in Dom E*.
Its actual vacuum is therefore b xi_S.
The other contraction has vacuum xi_h-(b xi_S)S+b.
All vectors belong to H because S is bounded.
Equality of derivative and contraction vacuum pairings gives the actual two target adjoint-vacuum conditions, proving A(X).

## Input-weight estimate and the actual E and E* product domains

C_F0136's core identity with weight 1 applies to the reference partial_S.
For fixed selfadjoint c in C[h], let u be the analytic-core unitary obtained from a selfadjoint strict contraction a in A_0.
Its polynomial truncations u_n and their adjoints converge uniformly with first derivatives converging in the Hilbert tensor norm.
Set z_n=u_n c.
Since partial_S c=0,

\[
\partial_S(z_n^*z_n)
=c\cdot\partial_S(u_n^*u_n)\cdot c\longrightarrow0.
\]

Both multipliers here are bounded.
The derivative of z_n also converges, so its contraction converges in H and the original closed graph identifies the limit as E(uc).
In the energy identity, the main term pairs E z_n in L2 with z_n xi_S in L2; uniform convergence of z_n makes that pairing converge even when xi_S is unbounded.
The last term tends to zero against the fixed tensor 1 tensor xi_S.
No second-operator domain at uc is asserted.

The resulting norm squared is 2 Re of the pairing of E(uc) with uc xi_S.
Left multiplication by u is isometric, so it gives norm(E(uc))_2 at most 2 norm(c xi_S)_2.
Repeating for u*, taking their average, scaling a strict contraction, and splitting arbitrary p into real and imaginary parts gives exactly

\[
\|E(pc)\|_2\le4\|c\xi_S\|_2\|p\|.
\]

This is an input-weight estimate.
No equality E(pc)=(Ep)c is asserted.

Now fix p in A_0 and take the same c_n from the joint approximation.
The finite tensor formula

\[
E(pc_n)=(\mathrm{id}\otimes\tau)(\partial_Sp\cdot c_n)
\]

has a strong H limit because each second-leg trace is continuous in c_n's L2 norm and there are finitely many bounded first-leg coefficients.
Also pc_n tends to pb in H.
Closedness gives actual membership pb in Dom E and exactly the formula and constant-4 bound of (17).
This passage does not need uniform boundedness of c_n.

For E*, its core identity at pc_n has output pc_n xi_S-E(pc_n).
The first term converges in H because c_n xi_S converges and p is bounded; the second was just shown to converge.
The closed E* graph therefore gives actual membership pb in Dom E*, value pb xi_S-E(pb), and the constant-5 bound.
These actual graph limits justify the later pairing with E*(qb); a formal product E*rho(b) is never substituted for them.

## Output bound and restoration of both K domains

Apply C_F0136 to B=C[h], which is a delta-zero star algebra for partial_S, and to the positive affiliated inverse b.
Its two L2 hypotheses hold by the assumed integrability and adjoint symmetry.
This gives the constant-4 estimate for K_0p on A_0.

For p,q in A_0, positivity of b and the actual product domain established above give

\[
\langle q,K_0p\rangle
=\langle qb,Ep\rangle
=\langle E^*(qb),p\rangle.
\]

Thus A_0 is contained in the actual Dom K_0*, with value E*(qb) there.
The constant-5 input estimate controls that core-adjoint value.
Density proves K_0 closable, so K=closure(K_0) and K*=K_0* are definite closed operators.

Uniformly operator-norm-bounded Kaplansky approximants to a in M have bounded K_0 images and bounded K_0* images by these separate estimates.
Weakly convergent graph subsequences lie in the corresponding weakly closed graphs.
This puts M in both domains; the approximation tolerance tending to zero gives exactly the two quantitative bounds (5).
Neither domain is obtained from a mere formal adjoint-product identity.

The polynomial commutators [K_0,h]=0 and [K_0,S]=bP have bounded right sides.
Their extension to M follows from the stated weak-graph approximation.
Equivalently, the invariant polynomial graph core and bounded bP allow the usual closed-graph commutator extension.
Thus [K,hS]=P on M.

The domain-M choices E_Y=K|_M and E_h=(B_h-K rho(S))|_M are well-defined, since aS is bounded for bounded a.
Their actual adjoint values on M are K* and B_h* minus rho(S)K*.
The undesired Y-commutator cancels because [B_h,hS]=PS and [K rho(S),hS]=P rho(S)=PS, with the latter equality obtained from trace cyclicity.
Negation gives the required generator-first S witnesses.

## Every strong witness reconstructs the actual starred derivations

This direction needs only the coordinate setup h positive regular, S bounded selfadjoint, and generation.
Start from arbitrary S(X) witnesses, change the sign and restrict to M for normalization.
Subtracting a mapped to a eta preserves every left commutator.
Its actual adjoint on bounded q is q eta*, by the bounded-L2 trace pairing, so the normalized operators retain M in their actual adjoint domains and vanish at 1.

For E_Y, h[E_Y,S]=P and normalization give h E_Y(S)=1, so b belongs to H.
Applying the full-M commutator product rule to Yh=hY* then yields

\[
h[E_Y,Y^*]=Ph,\qquad
h[E_h,Y^*]=YP-PY^*.
\]

Injectivity of h on H identifies the respective solutions as bPh and SP-bPY*.
The latter uses hS=Y and hb=1 with the displayed order; it does not commute b past S.
Each solution is a bounded finite-rank, hence Hilbert--Schmidt, operator because b is an H vector and the tested functionals have bounded coefficients.

The map Theta(u tensor v)(a)=u tau(v a) is the universal rank-one identification: tau(v a)=<v*,a>, so its Hilbert--Schmidt norm is norm(u)_2 norm(v)_2.
It extends to the unitary H tensor H identification and respects the outer left/right actions and the vacuum slice.
No normality of Y or phase theorem is needed for this fact.

All generator and adjoint-generator commutators therefore extend to Hilbert--Schmidt operators.
Finite product expansions give the same property for every element of A_X.
An actual represented zero has zero commutator on dense M, so the extension is unique and does not depend on a word presentation.
Taking Theta inverse defines a represented outer derivation with the required h and Y values.
Normalization identifies its right contraction on A_X with the supplied E_i.
Since 1 lies in the actual Dom E_i*, its vacuum pairing is represented by E_i*1 on the dense A_X.
This proves A(X) for every strong witness, not just for the constructed K system.

## Dependency and scope boundaries

The output estimate from C_F0136 and the local input estimate have separate roles and both stated product assumptions have been checked.
The actual conjugate-variable and core-adjoint input from Dab10 is used at its selfadjoint scope; neither reference contraction is assumed bounded on H.
The C_F0070 citation supplies only the universal tensor identification, rechecked above, and imports none of its normal-coordinate conclusions.

The proof is acyclic: arbitrary A gives the integrability conditions by the represented star relation and an actual vacuum pairing; those conditions give both actual vacua and the two-domain construction; arbitrary S gives A by a separate Hilbert--Schmidt reconstruction.
F is only a consequence.
No failure of a selected operator is used as an existential obstruction.
There is no numerical, proof-assistant or priority claim.

## Conclusion

The complete fixed statement and all six proof sections of C_F0138 v1 pass this independently organized review with no required mathematical correction.
The three direct dependency interfaces are adequate at their declared scopes.
This finding supports proved / independently reviewed for the candidate if adopted by its responsible Claim decision.

For the stated correlated finite-Fisher selfadjoint reference pair, A(h,hS), S(h,hS), and the two actual inverse-weight integrability conditions are equivalent.
The explicit vacuum vectors, specified K closure, both full-M actual domains and the constants 4 and 5 are established.
Each equivalent condition implies F.
No converse from F and no general nonnormal A-to-F theorem is part of this finding.

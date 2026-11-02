---
author: Yin
---
# Independent complete review of canonical domains for measurable Gaussian kernels

Review performed and recorded: 2026-10-14T21:16.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and inspected scope

The complete fixed [C_F0156 v1](../../claims/Yin_C_F0156_v1.md), initial decision dated 2026-10-14T21:10, and all seven exact declared dependency interfaces were read.
This review covers the entire statement and argument: actual target moment extraction, positive correction, soft adjoint and parameterized integration by parts, bounded Gaussian construction, weak reference commutator transfer, original target domains and complete vacua, the other coordinate and generation, constants and exact analytic-unitary energy.

Root proposed the quadratic-test and soft-kernel ideas; the normal branch developed the proof.
This reviewer did not participate in M1--M8 or the measurable-kernel extension, and did not read D_F0002 development.
The assignment disclosed the intended interfaces.
This reviewer previously independently reviewed C_F0153 and developed different normal tests in D_F0004 and nonnormal tests in D_F0005; those developments supply no missing premise here.
The new calculations were reconstructed from the fixed candidate.

During review the author explicitly defined delta_N as the scalar free-reference derivation on C<Z,Z*,S>, zero on S, with actual vacuum xi_N and the already declared C_F0045 free-lift bound.
This reviewer reread the sentence.
It makes explicit the reference already used, changing no formula, premise, conclusion or dependency.
The reviewed text includes it.
No mathematical repair was supplied by this reviewer.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0156 statement](../../claims/Yin_C_F0156_v1.md#statement) | Complete measurable positive Gaussian result under actual target A: generation, complete vacua and Hilbert coefficients, both original canonical domains, all-bounded commutators, constants and analytic-unitary lower form. No maximal/minimal-domain equality or general correlated-normal conclusion. |
| [Conclusion](#conclusion) | [C_F0156 argument](../../claims/Yin_C_F0156_v1.md#argument) | Entire moment, soft-adjoint, tensor-test, approximation, weak commutator, target comparison, generation and quantitative proof, including initial identification only of vacuum projections and their later exhaustion. |
| [Conclusion](#conclusion) | [C_F0153 statement](../../claims/Yin_C_F0153_v1.md#statement) | Arbitrary abelian-base Wick representation and degree-zero/one weighted derivative estimates with actual vacua and both original reference domains. Its finite-block application is not a measurable extension theorem. |
| [Conclusion](#conclusion) | [C_F0055 statement](../../claims/Yin_C_F0055_v1.md#statement) | Actual scalar vacuum, forward and reverse bound with constant 5+2 sqrt(27), and C1 graph approximation for the smooth marginal tests. |
| [Conclusion](#conclusion) | [C_F0055 soft bound](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform soft-Cauchy L2 bound only. Weak convergence and algebraic-tensor integration by parts are checked anew; no principal-value or maximal-domain theorem is imported. |
| [Conclusion](#conclusion) | [C_F0045 statement](../../claims/Yin_C_F0045_v1.md#statement) | Normalized scalar free extension on the complete reference core, its actual vacuum and contraction bounds with squared Grothendieck constant 4/pi. Freeness applies only to N and S. |
| [Conclusion](#conclusion) | [C_F0072 statement](../../claims/Yin_C_F0072_v1.md#statement) | Actual core-adjoint formula and weak graph restoration for the original contractions after both bounds are established; no closure-of-sum equality. |
| [Conclusion](#conclusion) | [C_F0070 tensor interface](../../claims/Yin_C_F0070_v1.md#statement-and-interfaces) | Coarse Hilbert--Schmidt identification, outer compatibility, matrix-element convention and diffuse normal spectral-difference injectivity forcing the starred phase. Its general bare-dual theorem is not used in place of this proof. |
| [Conclusion](#conclusion) | [C_F0078 Section 6](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual normal mixed energy, phase tensor-leg graphs and final-identity analytic limits before any growth estimate. |

## 1. Actual moment tests and the correction coefficient

The diffuse diagonal spectral projection of outer left Z minus outer right Z vanishes on the entire coarse Hilbert space.
Elementary outer spectral measures are absolutely continuous with respect to mu squared, and Hilbert density extends this to all tensors.
Differentiating normality therefore forces the stated Z* values.
The marginal restriction is the scalar divided difference with actual vacuum E_N xi.

The actual vacuum gives the usual algebraic-tensor adjoint formula and closability.
C1 approximation of the smooth endpoint functions converges in the original marginal derivative graph and in operator norm.
Finite products with bounded T pass through the outer Hilbert actions and vacuum pairing.
Thus the separated-endpoint tests are legitimate without applying the supplied derivation to S.

The degree-zero term of f0 T f1 T f2 is f0 eta_a(f1) f2 and vanishes by disjoint support.
Its degree-two path coefficient is precisely f0(z)a(z,w)f1(w)a(w,v)f2(v).
The middle derivative has zero double trace because each leg contains one centered T.
The first endpoint contributes a(w,v) squared/(z-v), the last minus a(z,w) squared/(z-v); the coincident endpoint products vanish.
This independently reproduces M1.

The H2 projection of the already supplied xi is a Hilbert vector.
On separated endpoint sets its coefficient multiplied by bounded a(z,w)a(w,v) is L1.
Smooth endpoint and polynomial middle tests determine that finite measure.
Countably many separated neighborhoods cover the complement of the product-null endpoint diagonal.
Positivity of the adjacent a factors yields M2 almost everywhere.
Thus chi is L2 because it is an existing vacuum projection, not because a formal quotient has been asserted integrable.

The two real correction numerators r inverse-1 and 1-r have the same sign.
Their coarse components are orthogonal, but their actual partial_S adjoints concatenate into the same H2 path.
C_F0153 therefore gives ||beta||2<=||chi||2 and partial_S*(beta*)=chi.
The independently constructed reference derivation has vacuum xi_N+chi.
At this stage those are only orthogonal components of the supplied vacuum; the later target comparison is needed to exclude other components.

## 2. Soft adjoints and precisely limited integration by parts

Antisymmetry gives the polynomial pairing of 2 conjugate(C_epsilon) with p.
The bounded polynomial divided differences justify dominated convergence.
The C_F0055 uniform L2 bound and polynomial density then give weak convergence of the whole family to xi_N, without choosing a subsequence or invoking principal values.

Direct adjoint expansion gives

    D_epsilon*(b tensor c)(z)
      = b(z) integral c(v) conjugate(K_epsilon(z-v)) dmu(v)
        + c(z) integral b(v) conjugate(K_epsilon(z-v)) dmu(v).

Rewriting the integrals proves M5, including coefficient 2 on bc conjugate(C_epsilon), both minus signs and the absence of conjugates on b,c in the resulting adjoint value.
The two reverse difference terms converge strongly for polynomial b,c; bounded multiplication preserves weak convergence of the vacuum term.
Testing this limit against original polynomials identifies it with the actual algebraic tensor adjoint D*(b tensor c).

For bounded f with D_max f in L2, its soft difference is D_max f multiplied by a uniformly bounded scalar tending to one off the null diagonal.
Strong Hilbert convergence follows.
Pairing the soft adjoint identity against the fixed f proves M6.
This requires neither membership of f in the original closed derivative domain nor algebraic-tensor core density for the entire adjoint.

The parameterized version is valid: tensor the fixed adjoint test with a fixed polynomial in the extra variable, preserving weak convergence, and pair against the fixed two-variable kernel in L2.
Strong convergence of the leg differences follows by the same domination.
Finite sums suffice for the later polynomial Wick projections.
No conclusion for arbitrary full-adjoint-domain tests is inferred.

## 3. Bounded Gaussian elements and the formal leg tensor

The relative creation operator prepends a(z0,z1); integrating in the new variable bounds its norm by ||a||infinity.
For a Hermitian kernel its adjoint is the finite-kernel annihilation operator.
Their sum has norm at most twice that bound and vacuum vector a.
Uniformly bounded almost-everywhere approximation gives strong convergence of both parts, first on finite-degree vectors and then on H.
Finite kernels give actual free-product elements, so the strong limit lies in M.

Bounded continuous approximation on the compact spectral product, polynomial approximation and real/symmetric averaging give the a_n used here; a subsequence gives almost-everywhere convergence with the same bound.
No derivative bound is needed.

The two formal tensor-leg differences of a equal minus beta multiplied by a at the external endpoints.
For example the coefficient at z tensor w S v is (a(z,v)-a(w,v))/(z-w), while beta has (a(w,v)/a(z,v)-1)/(z-w).
This checks the external multiplication and its sign; the other component has the corresponding endpoint order.
Hence bounded a and Hilbert beta give the actual tensor G_a.
This is a formal divided-difference Hilbert vector, still not a claim that a lies in the original closed leg graph.

## 4. Weak polynomial tests and full-domain commutators

Only the degree-zero/one patterns of a reference polynomial tensor test pair with delta_N T_n.
Their Wick components have polynomial marginal factors.
Each such algebraic tensor is in the actual reference adjoint domain.
Moving delta_N to the fixed test and using T_n tending to T_a in L2 proves that the limit in M7 exists even if the derivative norms are unbounded.
The parameterized M6 identifies it with G_a.
Other degree patterns are identically orthogonal.
This is convergence on the specified tests, not a claim of weak convergence of a uniformly bounded derivative family.

Insertion into partial_S T_n is the outer multiplier J_a_n beta.
The two explicit degree-one coefficients have external measures absolutely continuous with respect to mu squared.
Uniform boundedness and almost-everywhere convergence of a_n thus give strong convergence to J_a beta=-G_a.
Consequently M7 and M8 cancel on every fixed algebraic tensor test.

E' is the original reference contraction closure.
Its actual vacuum and both contraction bounds give all bounded-vector forward and adjoint domains by C_F0072.
Uniformly bounded strong polynomial approximation and weakly closed graphs identify bounded-vector values with the sum of the previously constructed contractions; this does not presume a closure-of-sum theorem.

The matrix-element test is correctly u tensor v*: Theta(x tensor y)v=x tau(yv).
For reference-core u,v, M7--M8 give limit zero.
Meanwhile the actual full adjoint domain supplies

    <u,[E',T_n]v>
       = <E'^*u,T_n v>-<T_n* u,E'v>.

The uniformly bounded selfadjoint T_n converge strongly, so this tends to the matrix element of [E',T_a].
Density in u proves vanishing for reference-core v.
Uniformly bounded core approximation in v passes both E'v and E'T_a v weakly through their original graphs, establishing the commutator on every bounded vector.
This never assumes that the algebraic tensor tests form a core for the entire derivation adjoint.
The Z and starred normal commutators pass through the corresponding bounded graph limits.

## 5. Generation and identification of the original target operators

Generation is independent of the derivative construction.
For q_n=min(n,1/a), choose finite marginal tensor approximants with the same bound and symmetry.
Multiplication of their kernels by a gives finite outer N combinations of T_a, hence elements of W*(N,T_a).
Uniformly bounded strong limits give T_(a q_n) in this algebra.
Since 0<a q_n<=1 and a q_n tends almost everywhere to one, creation and annihilation converge strongly to S.
Thus W*(Z,T_a)=M, and the target core is Hilbert dense.
No derivative of q_n or supplied-target differentiation of S is used.
Its later placement in the written proof creates no circularity.

E' and the supplied canonical Z contraction kill 1 and have identical commutators with Z,Z*,T on the target core.
Word induction gives equality of their values.
For bounded p, the actual reference adjoint identity already gives a bounded Hilbert pairing against every target-core input.
Thus p is also in the actual target adjoint domain with that same value.
In particular the supplied vacuum equals xi_N+chi by target density, eliminating all higher-chaos components.

The reference identity E'^*p=p(xi_N+chi)-F'p extends to bounded p by bounded graph approximation; multiplication of uniformly bounded strong approximants by the fixed L2 vacuum converges strongly.
Comparison with the target core-adjoint formula identifies its reversed contraction with F' there.
The two target bounds and the actual adjoint estimate are therefore justified.
Target Kaplansky approximants and their own weakly closed graphs place all M in the ORIGINAL target closure and adjoint; equality of unbounded closures from mere core agreement is not assumed.

For the T coordinate, the actual vacuum tests on f T_a g give the H1 identity.
Since a is bounded, a conjugate(psi_H1) is L2.
Dense polynomial tensor tests force it to equal one; positivity gives psi_H1=1/a and proves its L2 integrability.
The reference degree-zero coefficient 1/a then has actual vacuum Psi(1/a) and both full domains.
Its derivative at T_n is a_n/a, converging strongly to one by dominated convergence against the finite measure |1/a| squared dmu squared.
The same actual-adjoint matrix-element argument gives commutator P at T_a and zero at Z,Z*.
Word induction and target density identify the entire supplied psi with Psi(1/a), not only its first-chaos projection, and restore both original target domains.

## 6. Quantitative bounds and normal energy

The scalar free term contributes K0||xi_N|| and the correction contributes at most 2 sqrt(2)||chi|| to both forward and reversed contractions.
The two coefficients are initially orthogonal vacuum projections and later exhaust xi.
Cauchy--Schwarz therefore gives K squared=K0 squared+8 with the stated norm of xi.
The actual adjoint formula adds exactly ||xi||.
For the T coordinate the degree-zero insertion is isometric onto its vacuum, yielding exactly the constants 2||psi|| and ||psi||.

C_F0078 Section 6 applies its actual normal energy before any growth bound.
The present normal pair, actual target derivations and vacua, and generation satisfy that interface.
The analytic-unitary limit uses the final identity and first-derivative series, without a new second-iterate domain at the unitary.
The two vacuum pairings contribute at worst minus 4K||xi|| squared, and the two squared contraction norms at worst minus 2K squared||xi|| squared.
This gives the claimed lower form.
No absolute C_g estimate or Hilbert-kernel assumption on g is introduced.

## Source and verification limits

All seven exact fixed interfaces were read or reread and their applicability checked.
Their established scalar, free-lift, finite-degree, tensor and phase-domain results retain their recorded source inspection limits; the full external texts behind those accepted inputs were not newly audited.
The new soft-adjoint, parameterized test, weak commutator and target-domain steps were checked directly.
No maximal/minimal domain theorem, adjoint-core density theorem, principal-value assertion, numerical experiment or formal verification is used.

## Conclusion

**Pass: complete fixed C_F0156 v1 independently reviewed.**
The entire statement, complete proof and all seven direct interfaces are covered above.
No mathematical correction was found.
The added explicit reference-derivation definition is included at the unchanged scope recorded in the arrangement.

The supported result is actual A implying both specified original canonical domains, hence S and F, for the bounded positive symmetric measurable Gaussian-kernel class.
It includes the complete forced vacua, constants and analytic-unitary lower form.
It does not establish maximal/minimal-domain equality, an exact converse criterion, arbitrary phase coefficients or the unrestricted correlated-normal implication.
This is not a Task completion review.

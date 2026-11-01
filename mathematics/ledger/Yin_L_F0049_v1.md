---
author: Yin
---
# Nonnormal tests for ACSY24 versus full-domain duals

Date: 2026-10-14.
Human author Yin.
The acsy_full_counterexample agent developed this bounded subtask under the user's explicit continuation request.
The audit_acsy_nonnormal agent independently checked the complete arguments below after root corrected the order of the one-sided starred relation.
Both tested constructions fail ACSY24 and the full-domain dual premise; no separating counterexample has been obtained.

## Current proof home

The complete original argument and its original dates, local-check statements and earlier review descriptions remain below.

## Question and reused inputs

Fixed-material review: [R_F0134, failed-test conclusion](../audits/reviews/Yin_R_F0134_v1.md#failed-test-conclusion) independently checks the complete corrected arguments below, including the three-block automatic-continuity step.
Review accepted for this exact exploration scope on 2026-10-14T11:20; no separating example is claimed.

Does the existence of normalized starred-core derivations with actual L2 vacua in ACSY24 Proposition 3.5 imply existence of any linear dual system on all M Omega?
The source assumptions, including absence of normality, are retained in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
The exact normal-case comparison and prior failed sandwich test are retained in [C_F0070](../claims/Yin_C_F0070_v1.md#statement) and [L_F0047](Yin_L_F0047_v1.md).
The present draft tests nonnormal variations, where normal uniqueness and automatic continuity cannot simply be imported.

## One-sided singular transport cannot use a non-L2 inverse

Let h be bounded positive, injective, with dense range in a finite tracial M, let S=S* be bounded, and put Y=hS.
Consider X=(h,Y), with starred polynomial algebra A.
Suppose a derivation partial_Y:A -> L2(M) tensor_2 L2(M) satisfies partial_Y h=0 and partial_Y Y=1 tensor 1.
Since h=h*, it also vanishes on h*.
The actual relation Y h=hY* gives

    h (partial_Y Y*) = 1 tensor h.

Left multiplication by h in the first tensor leg is injective.
Its affiliated inverse therefore forces

    partial_Y Y* = h^{-1} tensor h.

This vector is in the Hilbert tensor product only if h^{-1} is in L2(M).
More explicitly, contract the second leg against h/||h||2^2; a Hilbert-vector solution would produce v in L2(M) with hv=1, forcing v=h^{-1}.
Thus the uniform-(0,1) choice from C_F0068 does not meet even the Hilbert-valued starred derivation condition.
This excludes a tempting nonnormal repair of the failed selfadjoint sandwich example, before any vacuum calculation.

For comparison, a full-domain dual E with [E,h]=0 and [E,Y]=P gives h[E,S]=P on M Omega.
Applying to Omega forces a vector v in L2 with hv=1, so again h^{-1} must be L2.
This shared necessary condition does not decide the case h^{-1} in L2 but unbounded.

## A diffuse Jordan operator also fails the starred derivation premise

Let M=M2(L-infinity(0,1)) with product probability trace, let s be the coordinate function times I2, let N=e12, and put x=s+N.
Then x generates M as a von Neumann algebra.
Indeed [x,x*]=e11-e22, so

    N=(1/2)[[x,x*],x],  s=x-N

belong to A=C<x,x*>.
Matrix units and the scalar coordinate therefore belong to its generated von Neumann algebra.
The diffuse diagonal law avoids the elementary scalar eigenvalue obstruction, but is not sufficient for ACSY24.

Suppose delta:A -> H tensor_2 H is a derivation with delta x=1 tensor 1.
Write beta=delta N, alpha=delta s=1 tensor 1-beta, and let K be the bounded coarse operator N acting on the first leg minus N acting on the right of the second leg.
Differentiating sN=Ns yields

    ((s-t)I+K) beta = K(1 tensor 1).

Here t denotes the second scalar coordinate.
The coarse space is L2((0,1)^2) tensor (M2 tensor M2), and K^3=0.
Off the product-null diagonal s=t, multiplication by (s-t)I+K is invertible.
Thus any Hilbert-vector solution is forced to be

    beta(s,t) = (N tensor I-I tensor N)/(s-t)
                + 2 N tensor N/(s-t)^2.

The two displayed matrix tensors are orthogonal for the normalized product trace.
The first has squared Hilbert norm 1.
Consequently

    ||beta||2^2 >= integral_0^1 integral_0^1 |s-t|^{-2} ds dt = infinity,

a contradiction.
This rules out the normalized Hilbert-valued starred derivation before asking for its vacuum adjoint.

### The Jordan operator also excludes a bare full-domain dual

The following continuation uses the accepted [Lau88 interface](../audits/literature/Lau88/Yin_U001.md#lau88-u001) and the proof mechanism in [C_F0069](../claims/Yin_C_F0069_v1.md#argument).
The audit_acsy_nonnormal agent independently verified the complete argument, including the source hypotheses and pinching estimate; its fixed review record is attached separately.

Suppose E:M -> L2(M) is an arbitrary complex-linear map satisfying [E,x]=P on all M.
For scalar f in L-infinity(0,1), set

    F(f)=(E(f e11))22,  G(f)=(E(f e11))12.

Since x(f e11)=sf e11 and the matrix trace is normalized, the 22 and 12 coefficients of the commutator identity respectively give

    F(sf)-sF(f)=(1/2) integral f,   G(sf)-sG(f)=F(f).       (J1)

Thus F and G are everywhere-defined algebraic maps L-infinity -> L2, with [F,s]=P0/2 and [G,s]=F, where P0(f)=(integral f)1.

First these identities imply that G is bounded L-infinity -> L2.
Let T be scalar multiplication by s on L-infinity, let N0 be multiplication by s on L2, and on Y=L2 direct-sum L2 direct-sum L-infinity set

    R = [[N0, I, 0], [0, N0, P0/2], [0, 0, T]],
    J(f)=(G(f),F(f),f).

Equation (J1) says RJ=JT.
For a smooth scalar function phi on the real line define k1_phi(s,t)=(phi(s)-phi(t))/(s-t) and

    k2_phi(s,t)=(phi(t)-phi(s)-phi'(s)(t-s))/(t-s)^2.

Use their continuous diagonal values.
Let K1_phi and K2_phi be the corresponding Hilbert-Schmidt integral operators, restricted to L-infinity for the third-column entries.
Define

    Phi(phi) = [[phi(N0), phi'(N0), K2_phi/2],
                [0, phi(N0), K1_phi/2],
                [0, 0, phi(T)]].

The first and second divided-difference product identities make Phi a unital homomorphism.
Explicitly,

    k1_(phi psi)(s,t)=phi(s)k1_psi(s,t)+k1_phi(s,t)psi(t),
    k2_(phi psi)(s,t)=phi(s)k2_psi(s,t)
                     +phi'(s)k1_psi(s,t)+k2_phi(s,t)psi(t).

Both kernels are bounded on [0,1]^2 by the first and second derivative bounds, and Phi(s)=R.
Its spectrum is contained in [0,1] by triangular inversion outside that interval.
Smooth partitions of unity and the local reciprocal phi(s)=(s-lambda)^{-1}, exactly as in C_F0069's two-block argument, show R is super-decomposable.
For a two-set cover of the complex plane, choose the partition near [0,1]; for any lambda outside one partition support, a smooth reciprocal near that support supplies the inverse on the closed range of its Phi image.

R has no eigenvalues by taking the three coordinate equations in reverse order.
It has no nonzero algebraically divisible subspace: project a divisible subspace successively to the last coordinate and the second coordinate, embedding the L-infinity coordinate into L2.
Each image is a divisible subspace for the bounded normal multiplication operator N0 and is zero by the elementary spectral-measure argument proved in C_F0069; the first coordinate then vanishes as well.
T is decomposable via interval spectral projections.
Thus Lau88 Proposition 3.7 and Theorem 4.1 apply to (R,T), and J is continuous.
In particular ||G(f)||2 <= C ||f||infinity for some finite C.

Now (J1) gives [[G,s],s]=P0/2.
Partition (0,1) into n equal intervals with indicators e_j and midpoints lambda_j; set r_j=(s-lambda_j)e_j.
Applying the pinched identity to 1 gives

    (1/(2n))1 = sum_j [ e_j G(r_j^2) - 2 r_j G(r_j) + r_j^2 G(e_j) ].

For independent symmetric signs sigma_j, each sum on the right is a sign average of the form (sum sigma_j a_j) G(sum sigma_j b_j).
Since the supports are disjoint,

    ||sum sigma_j e_j||infinity=1,
    ||sum sigma_j r_j||infinity <=1/(2n),
    ||sum sigma_j r_j^2||infinity <=1/(4n^2).

Consequently the right side has L2 norm at most C/n^2, whereas the left side has norm 1/(2n).
Taking n>2C gives a contradiction.
Hence no bare full-domain dual exists for this Jordan x either.
It therefore separates neither set of hypotheses: both fail for concrete, distinct reasons.

## Current boundary

Neither candidate gives an ACSY24 example.
A valid nonnormal counterexample must retain an actual Hilbert-valued derivation on every starred polynomial and its L2 vacuum; maximal Delta, lack of scalar eigenvalues, or a formal holomorphic derivative alone are insufficient.
The preceding arguments are direct relation tests and use no unverified extension theorem.
The general implication remains unresolved in this subtask.

## Search boundary

After the local C/U/L checks, a bounded primary-source web search used the phrases dual system non-self-adjoint free probability conjugate variables; conjugate variables Dabrowski nonselfadjoint derivation bounded; and derivation coassociative real Dabrowski inequalities.
It surfaced the known selfadjoint/real contraction estimates and generalized almost-coassociative leads, not a verified theorem covering the present arbitrary-nonnormal implication.
No novelty or literature-absence claim is made.

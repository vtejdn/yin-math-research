---
author: Yin
---

# Three monomials suffice to test the one-third coordinate threshold

## Statement

Let \(G\) be a discrete ICC group, \(p\) a projection of trace \(\alpha\) in its regular von Neumann algebra, \(q=1-p\), and \(z\) an affiliated scalar.
For \(\alpha=1/2\), there is a sum \(v\) of at most three integer multiples of group elements such that
\[
                           \operatorname{rk}(q(z+v)p)>1/3 .
\]
Each of the three coefficients before collecting equal terms can be taken in \(\{1,\ldots,256\}\).
For a two-by-two Schur input this is the excess \(b-h\) of the [original column shear](Yin_C_A0257_v1.md#statement).
If \(G\) has a free pair whose centralizers of all nonidentity elements of \(G\) are cyclic or trivial inside the pair's free group, all three monomials can be chosen among the freely reduced words of length exactly ten in those two generators.
The original coefficients may use the two free generators.

For each finitely generated torsion-free ICC group, strong Atiyah holds if and only if the supremum of \((b-h)_+\) is strictly less than \(1/3\) on the following restricted family.
Take an arbitrary finite polynomial kernel, select one coordinate \(x_i\), add one input \(y\) and the single equation \(y=v x_i\), and use \(x_i,y\) for the two distinguished coordinates.
Only sums of at most three monomials with the same integer bound need be tested.
A failure produces an individual test with \(b-h\ge1/3\).
With the specified free pair the tests may use only the length-ten sphere for \(v\); in particular this restriction on \(K*F_2\) is sufficient for the conjecture across all torsion-free groups.
The length-free equivalence also holds for torsion-free groups with scalar center-valued ranks on their scalar regular-closure projections, as in the [virtual-character and amenable cases](Yin_C_A0260_v1.md#statement).

The final example distinguishes three terms from two at **strict** excess \(1/3\) for arbitrary half-trace projections on a fixed free sphere.
It makes no assertion of optimality for hypothetical torsion-free polynomial counterexamples.

## Improving one coefficient at a time

Start with \(v=0\) and set \(r=\operatorname{rk}(q(z+v)p)\).
Let \(P\le p\) be the residual kernel on \(p\) and \(E\le q\) the orthogonal complement of the range within \(q\).
Write \(u=\alpha-r,\ w=1-\alpha-r\) for their traces.
For any group element \(g\),
\[
 \sup_{\lambda\in\mathbb C}\operatorname{rk}(q(z+v+\lambda g)p)
       \ \ge\ r+\operatorname{rk}(EgP)
       \ \ge\ r+\tau(EgPg^*).
\]
For the first inequality use the [rescaled triangular perturbation](Yin_C_A0270_v1.md#what-maximal-rank-on-a-fixed-support-forces) at the present \(v\), without assuming a maximum; right regularization transports the restricted kernel to \(PU\).
For the second, \(EgP\) is a contraction and its squared \(L^2\)-norm is bounded by its image rank.
The [finite-parameter estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) shows that a single integer \(1\le\lambda\le256\) achieves at least \(255/256\) of the line supremum, losing at most \(1/512\) since the ranks are bounded by \(\min(\alpha,1-\alpha)\le1/2\).

In a factor the closed \(L^2\)-convex hull of the conjugates of \(P\) contains \(u1\).
Hence \(\sup_g\tau(EgPg^*)\ge uw\), also when all the relevant projections have scalar center-valued rank. [Conjugation averaging](Yin_C_A0125_v2.md#reduction-of-the-defect-with-one-more-group-element)
In particular for \(\kappa=2/81\) one can choose an actual \(g\) satisfying
\[
               \tau(EgPg^*)\ \ge\ uw-\kappa\sqrt{u(1-u)w(1-w)} .
\]
When the square root is positive the bound uses a strict allowance below the supremum; for zero residual kernel or target one may stop at the maximal rank.
The cases \(\alpha=0,1\) are not needed.

For the prescribed free pair there is a stronger choice restricted to a fixed finite sphere.
Write \(C\) for uniform conjugation on the four free letters and \(S_n\) for uniform conjugation on the words of reduced length \(n\).
Then \(S_0=I,\ S_1=C,\ CS_n=(3S_{n+1}+S_{n-1})/4\) for \(n\ge1\), by counting initial cancellation.
The [orbit estimate](Yin_C_A0264_v1.md#two-fixed-choices-in-the-marked-group) and the modulus argument for the [two-sided norm](Yin_C_A0270_v1.md#signed-averages-on-the-two-free-generators) give \(\|C\|\le\theta=\sqrt3/2\) on the centered subspace.
Using the Chebyshev polynomials of the first and second kinds gives
\[
      S_n=3^{-n/2}\big(U_n(C/\theta)+T_n(C/\theta)\big)/2 .
\]
Both sides have the same first two values and the same three-term recurrence.
On the centered subspace \(\|S_n\|\le(1+n/2)3^{-n/2}\).
For \(n=10\) this is \(2/81\).
Unlike a signed polynomial average, \(S_{10}\) is a convex combination on that sphere itself.
Centering \(P,E\) therefore gives the displayed lower bound for at least one such word.

Put \(c=\alpha(1-\alpha)\).
One has \(uw=c-r+r^2\) and
\[
    u(1-u)w(1-w)=(c+r^2)^2-r^2\le(1/4-r^2)^2,
\]
since \(c\le1/4\).
The new rank after adding the selected integer multiple is consequently at least
\[
             c-1/162-1/512+(83/81)r^2 .
\]
This is an increasing function of \(r\ge0\).
If the maximal rank is reached early, take no further term; all quantitative lower bounds below are also bounded by that maximum for the selected traces.

## Three improvements and the original-group test

For \(8/17\le\alpha\le1/2\), one has \(c\ge72/289\) and \(c-1/162-1/512>241/1000\).
From any starting \(r\ge0\) the first improvement gives at least \(241/1000\), the second at least \(601/2000\), and the third strictly more than \(1/3\).
For the last two comparisons substitute these rational lower bounds into \(241/1000+(83/81)r^2\).
This includes the asserted half-Schur case.

When \(\alpha\ge2/5\) and \(\alpha\le1/2\), the constant term is at least \(6/25-1/162-1/512>231/1000\).
Three iterations then exceed \(4/13\): the second exceeds \(285/1000\), and \(231/1000+(83/81)(285/1000)^2>4/13\).
At \(\alpha=1/3\) already the first lower bound is positive.

If strong Atiyah fails in the ICC group, use the [corner alternatives](Yin_C_A0259_v1.md#statement) for its scalar star-regular closure \(R\).
If it has no minimal projection choose \(p\in R\) of trace in \([8/17,1/2]\).
In \(R=M_n(D)\) take trace \(\lfloor n/2\rfloor/n\) for \(n\ge2\).
For even \(n\) or \(n\ge17\) this is in the first range.
For \(n=5,7,9,11,13,15\), the largest possible \(1/n\)-multiple strictly less than \(1/3\) is at most \(4/13\); the second estimate therefore gives rank at least \(1/3\).
For \(n=3\) any positive rank already suffices.
Using \(z=0\), each rank so measured is a multiple of \(1/n\) in this Artinian case.
Every selected \(p\) is the coordinate image of an actual group-ring kernel by the [polynomial graph construction](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix).
The new equation has joint coordinate dimension \(\alpha\) and separate dimension \(\alpha+\operatorname{rk}(qvp)\).
In a skew field every positive part of this coordinate excess is zero. [Coordinate criterion](Yin_C_A0255_v1.md#statement)
For the scalar center-valued case the packing alternatives are unchanged, and \(z=0,\ p,v\in R\) ensure that the residual projections used in averaging lie in \(R\).
The free-product reduction uses the same regular subgroup inclusion as the [radius-five criterion](Yin_C_A0270_v1.md#a-restricted-test-for-the-whole-group).

## Two shifts on a Bernoulli lamp projection

Take \(G=\mathbb Z\wr F_2\) and for \(p\) take a half-circle spectral projection of the lamp translation at the identity.
This torsion-free group has the required centralizer property: a nonidentity shift projection has cyclic free-group centralizer, and a nonempty finite lamp support has trivial stabilizer under left translations by the torsion-free free group.
In the group von Neumann algebra the shifted \(p\)'s are independent fair bits and the free shifts act by translating sites, as seen from their product trace and zero trace at each nonidentity shift. [Bernoulli lamp model](Yin_C_A0127_v1.md#the-bernoulli-representation-of-the-translated-projections)
For \(z=0\) take two distinct free words \(x,y\) of the same positive length with nonzero complex coefficients \(c_1,c_2\).
Put \(w=x^{-1}y\).
Then \(x\notin\langle w\rangle\).
Otherwise \(x=w^m,\ y=w^{m+1}\), and the lengths of two consecutive powers of a nontrivial free word differ, by cyclic reduction (also when one power is the identity).

In the equivariant Bernoulli fibers each input chain \(w^j\) is matched to the separate output chain \(xw^j\); an input at \(w^j\) can reach \(xw^j\) and \(xw^{j+1}\).
These chains have disjoint site sets.
More generally the input chains are right translates of \(\langle w\rangle\) and their output chains are the corresponding right translates of \(x\langle w\rangle\); distinct input chains have disjoint output chains.
On the chain through the identity, live input coordinates and live output rows are two independent sequences of fair bits.
A connected block of \(\ell\ge1\) live columns gives one component of the kernel precisely when all its \(\ell-1\) interior rows are live and both boundary rows are absent.
Indeed the interior equations propagate one free scalar via the two nonzero coefficients; a live boundary row with a dead adjacent column pins it to zero.
Equivalently split all runs at absent rows, and pin the ends next to dead columns when the bordering row is live.
The qualifying intervals are disjoint, and no infinite component occurs almost surely.
Their start probability is \((1/2)^\ell(1/2)^{\ell-1}(1/2)^2=2^{-(2\ell+1)}\).
Summing the diagonal of each normalized kernel line over its \(\ell\) possible positions in the trace gives restricted nullity \(\sum_{\ell\ge1}2^{-(2\ell+1)}=1/6\).
Thus \(\operatorname{rk}((1-p)(c_1x+c_2y)p)=1/3\).
For just one nonidentity shift the rank is \(1/4\) by independence.
This computation concerns an ambient projection and does not assert that it is a Schur kernel over this torsion-free group.

## Assessment history

### Decision three-integer-monomials-and-the-fixed-sphere

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Independent full review confirmed three-term sufficiency, the original-group quantifiers, integer bounds and the sharp ambient two-shift calculation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The three-term shear, quantized one-third test and limits of the Bernoulli example. |
| argument | [Improving one coefficient at a time](#improving-one-coefficient-at-a-time) | Residual rank increment, integer loss, spherical walk and the lower recurrence. |
| argument | [Three improvements and the original-group test](#three-improvements-and-the-original-group-test) | The three rational iterations and all exceptional denominator cases. |
| argument | [Two shifts on a Bernoulli lamp projection](#two-shifts-on-a-bernoulli-lamp-projection) | Disjoint input and output chains and the exact multiple-term comparison. |
| review | [Three integer monomials and the fixed sphere](../audits/reviews/Yin_R_A0206_v1.md#three-integer-monomials-and-the-fixed-sphere) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-three-integer-monomials-and-the-fixed-sphere)

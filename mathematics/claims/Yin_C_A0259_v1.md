---
author: Yin
---

# The possible sizes of matrix-algebra corners over an ICC group

## Statement

Let \(G\) be a discrete group whose group von Neumann algebra \(N\) is a factor, and let \(R\) be the actual star-regular closure of \(\mathbb CG\) in \(\mathcal U(G)\).
Write \(\mu_d\) for the supremum of the traces of projections \(e\in R\) such that \(eRe\) contains a unital algebraic \(M_d(\mathbb C)\), including zero in the supremum.
For each fixed \(d\ge2\) there are two cases.

* If \(R\) contains a nonzero minimal projection, then \(R\) is isomorphic as a ring to \(M_n(D)\) for a division ring \(D\).
  Every minimal projection has trace \(1/n\), and \(\mu_d=d\lfloor n/d\rfloor/n\), attained when positive.
* If \(R\) has no nonzero minimal projection, then \(\mu_d=1\).
  It contains actual \(d\)-square matrix algebras on corners whose traces are arbitrarily close to one.

Minimality here means absence of a proper nonzero subprojection in \(R\).
The second conclusion is a supremum and does not assert a unital \(M_d\) on the whole identity.
With \(h,b\) the [two coordinate increments](Yin_C_A0255_v1.md#statement) of polynomial matrices and distinct coordinate rows, \(d\sup_L(b-(d-1)h)_+=\mu_d\).

For a finitely generated torsion-free ICC group, complex strong Atiyah therefore holds if and only if
\[
                           \sup_L(b-h)_+<1/3\quad(d=2).
\]
More precisely this supremum can only be \(0\), \(k/(2k+1)\) for an integer \(k\ge1\), or \(1/2\).
If strong Atiyah fails, a test exists in the original group with \(b=2h\ge2/3\).
If an original polynomial matrix has irrational regular rank, there are tests in that group with \(b=2h\) arbitrarily close to one.
The numerical alternatives describe implications of the ring structure, without supplying any torsion-free counterexample.

## Packing a minimal projection

For nonzero projections \(p,q\in R\) some \(qgp\) with \(g\in G\) is nonzero.
Indeed the join of all conjugates of \(p\) by group elements is central in \(N\), hence equals one in the factor.
If \(p\) is minimal, the initial projection of that nonzero compression is a nonzero subprojection of \(p\) in \(R\), so equals \(p\).
The image projection and the Moore–Penrose inverse then exhibit an equivalent copy of \(p\) inside \(q\).

Apply this to the remaining complement after each placement of a copy of \(p\).
Each placement uses exactly \(\tau(p)>0\), so the procedure is finite and its terminal complement must be zero.
One obtains \(n\) orthogonal equivalent copies summing to the identity, with \(n\tau(p)=1\).
Any nonzero element of \(pRp\) has nonzero initial and final projections in \(pRp\); minimality makes both equal to \(p\), so its relative inverse is its two-sided inverse in this corner.
Thus \(D=pRp\) is a division ring.
The \(n\) equivalences with \(p\) yield a ring isomorphism \(R\simeq M_n(D)\) by writing every entry between two of these summands.

Every idempotent over \(M_s(R)\) then has unnormalized regular rank equal to its ordinary \(D\)-rank divided by \(n\).
In fact it is conjugate over \(M_{sn}(D)\) to an identity block and a zero block, and each single \(D\)-coordinate corresponds to a copy of \(p\).
Every polynomial matrix has image projection over the matrix regular closure, so its rank also has this denominator bound.
For a \(d\)-square system on a projection \(e\) in the scalar ring the \(D\)-rank of \(e\) is divisible by \(d\), since its \(d\) diagonal summands are equivalent.
Conversely, take \(d\lfloor n/d\rfloor\) of the orthogonal coordinates and divide them into \(d\) equal groups.
When this number is nonzero their scalar corner carries unital \(d\)-square matrix units.
This proves the first value of \(\mu_d\), also giving zero when \(d>n\).

## Packing without minimal projections

For projections \(p,q\in R\), the supremum of \(\operatorname{rk}(qvp)\) over \(v\in\mathbb CG\) equals \(\min(\tau(p),\tau(q))\).
For the lower bound compare the two projections in the factor, choose a partial isometry with that rank between them, and approximate it in \(L^2\) by group-ring entries.
On the initial support of the partial isometry the kernel of \(qvp\) has dimension at most the squared approximation error. [Comparison and polynomial approximation](Yin_C_A0239_v1.md#the-exact-original-infimum)
For each polynomial choice the resulting initial and final projections belong to \(R\).

In the absence of minimal projections, \(R\) has projections of arbitrarily small strictly positive trace.
Split any nonzero projection using a proper nonzero subprojection in \(R\), then keep a smaller of the two pieces in trace and repeat.
To approach a target \(s\in(0,1)\) from below, fix such a small \(p\) with trace \(a<s\).
Starting with an empty sum of pieces of total trace \(u\), while \(s-u\ge a\) apply the comparison above with \(q\) the unused complement.
Since \(\tau(q)\ge a\), one obtains an image in \(q\) of trace at least \(a/2\) and at most \(a\).
Finitely many such placements give a projection of trace in \((s-a,s]\).
In particular choose \(P\in R\) with trace \(c\le1/d\) as close to \(1/d\) as desired.

For any \(\eta>0\) successively choose \(x_i=(1-Q_{i-1})v_iP\), \(v_i\in\mathbb CG\), \(1\le i\le d\).
Here \(Q_{i-1}\) is the sum of the preceding mutually orthogonal image projections.
It has trace at most \((i-1)c\), so its complement has trace at least \(c\).
Each \(x_i\) can therefore be chosen with rank at least \(c-\eta\).
The intersection \(F\) of their initial projections lies in \(R\), is dominated by \(P\), and has trace at least \(c-d\eta\) by subadditivity of the losses inside \(P\).
For \(c>d\eta\), the restrictions \(x_iF\) are injective on \(F\), with mutually orthogonal images equivalent in \(R\) by their relative inverses.
The sum of these images carries unital \(d\)-square matrix units and has trace \(d\tau(F)\ge dc-d^2\eta\).
Let \(c\) approach \(1/d\) and then \(\eta\) approach zero.
All the corners so obtained belong to the original group and use only finitely many operations.

## Detecting a failure with two coordinates

The [polynomial realization of each corner](Yin_C_A0255_v1.md#realizing-a-corner-by-polynomial-equations) gives two-coordinate tests at \(b=2h=\tau(e)\) whenever \(e\) carries the matrix units.
Its converse bounds \(2(b-h)_+\) by the supremum of the corner traces for all tests.
Thus in the minimal case the supremum is \(\lfloor n/2\rfloor/n\), and without minimal projections it is \(1/2\).
For \(n=1\) the regular closure is a division ring; conversely when the complex strong conjecture holds the actual division closure is a star-closed skew field and equals the regular closure.
Every \(n\ge2\) gives an attained \(2\lfloor n/2\rfloor/n\ge2/3\) for the corner trace.
Without minimal projections the trace can be made greater than \(2/3\).
These facts prove the strict threshold and the claim for irrational regular ranks, which cannot occur in the minimal case.

## Assessment history

### Decision sizes-of-corners-in-a-factor

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:07 |
| status | proved |
| reason | Whole-proof review verified the two packing arguments, possible values, strict threshold and original-group claims. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The possible corner suprema, the original-group threshold and the irrational case. |
| argument | [Packing a minimal projection](#packing-a-minimal-projection) | The finite decomposition into equivalent minimal summands and exact division-ring rank. |
| argument | [Packing without minimal projections](#packing-without-minimal-projections) | Trace approximation, positive steps and simultaneous restriction of the initial supports. |
| argument | [Detecting a failure with two coordinates](#detecting-a-failure-with-two-coordinates) | The attained two-thirds corner and the one-third gap. |
| review | [Sizes of corners in a factor](../audits/reviews/Yin_R_A0203_v1.md#sizes-of-corners-in-a-factor) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-sizes-of-corners-in-a-factor)

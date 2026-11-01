---
author: Yin
---

# Yin_C_F0010: Independent Review of Bounded Dual Action on Rational States

Date: 2026-09-09.
Reviewer: the reviewing agent.
Reviewed artifact: [Yin_C_F0010 proof](../../claims/Yin_C_F0010_v1.md#yin_c_f0010).

This reviewer did not author the probe argument or its written artifact.
The interval normalization obstruction had previously been discussed by this reviewer; its written calculation and exact primary input were checked again here.
The proof of parts 1-3 was independently reconstructed.

**Verdict:** all three stated conclusions are valid under their displayed hypotheses.
The full inverse has L1 entries unconditionally within the lemma's assumptions; the L2 upgrade retains its separate bounded-probe hypothesis, and the selfadjoint/bounded-vacuum condition is a valid sufficient condition for those probes.
Both boundary examples are correct.
No bounded inverse or scalar division conclusion is supplied by this lemma.


## Review relationships

| Review | Relationship |
| --- | --- |
| [Actual complete finding](#bounded-probe-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Actual complete finding](#bounded-probe-finding) | [C_F0010 statement](../../claims/Yin_C_F0010_v1.md#statement) | Complete bounded probe identity, unconditional whole-inverse L1 consequence, conditional L2 upgrade, selfadjoint bounded-vacuum sufficient probes, exact interval nonnormalizability and Haar probe boundary. Retains the actual Tao06 primary-text inspection depth; no Lp-to-bounded or scalar elimination conclusion. |
| [Actual complete finding](#bounded-probe-finding) | [C_F0010 argument](../../claims/Yin_C_F0010_v1.md#1-a-probe-identity-in-h-then-in-u) | Complete bounded probe identity, unconditional whole-inverse L1 consequence, conditional L2 upgrade, selfadjoint bounded-vacuum sufficient probes, exact interval nonnormalizability and Haar probe boundary. Retains the actual Tao06 primary-text inspection depth; no Lp-to-bounded or scalar elimination conclusion. |

<a id="bounded-probe-finding"></a>
The reviewer explicitly records having previously discussed the interval normalization obstruction, which is a substantive component of this same complete finding.
Its full finding therefore has shared substantive mathematical context; separate reconstruction of Parts 1-3 does not make this whole account independently reviewed under the current rule.
The original inspection date, computations, source limits and independent wording remain historical facts; this declaration maintenance performs no new review and does not infer a relationship from C's retired aggregate field.

## 1. Hilbert-Space Identity and Affiliated Multiplication Order

For a bounded probe a, every h_j a is L2, so the column ha is in H^n.
The polynomial matrix L acts boundedly on H^n.
Applying the diagonal bounded D_i to L(ha)=va is legitimate before any affiliated inverse is used.
Because the constant matrices commute with the diagonal D_i and [D_i,X_j]=delta_ij P, the exact sign is [D_i,L]=-A_iP.
Therefore

\[
L D_i(ha)=vD_i(a)+A_i\tau(ha).
\]

After this Hilbert-space equality is obtained, every vector is identified with its canonical measurable-operator column.
Multiplication by L^{-1} then takes place in the associative matrix algebra over U(M).
In particular,

\[
L^{-1}(vD_i(a))=(L^{-1}v)D_i(a)=hD_i(a),
\]

in that order.
This proves the stated probe identity as an affiliated identity.
It does not presume that D_i acts on arbitrary affiliated elements or that hD_i(a) is already in H.

The latter product has L1 entries by noncommutative Holder, since h_j and D_i(a) are both L2.
The other summand D_i(h_j a) is L2 and hence L1 because tau(1)=1.
More explicitly,

\[
\|D_i(h_ja)\|_1\le\|D_i\|\|h_j\|_2\|a\|_\infty,
\qquad
\|h_jD_i(a)\|_1\le\|h_j\|_2\|D_i\|\|a\|_2.
\]

Their sum is exactly the displayed estimate (3).
No missing coefficient norm or state-index sum occurs: the left side is the indicated row of L^{-1}A_i tau(ha), already fixed by the probe identity.

## 2. Bounded Probes Separate Every Constant State Direction

The map T(a)=tau(ha) is complex-linear on M.
If a scalar row c annihilates its range, k=sum_j c_jh_j satisfies tau(ka)=0 for every bounded a.
Bounded elements are dense in L2, so choose a_m tending to k* in L2.
Holder continuity gives tau(kk*)=0.
Faithfulness implies k=0, and the stated independence of the h_j gives c=0.

Since the target is finite dimensional, trivial annihilator means T(M)=C^n.
Thus one can choose finitely many bounded a_k with T(a_k)=e_k, not merely a dense set of approximate directions.
The probe identity places each column L^{-1}A_i e_k in L1.
The algebraic identity

\[
L^{-1}=I_n+\sum_i (L^{-1}A_i)X_i
\]

follows from L^{-1}L=I with the correct multiplication order.
Bounded right multiplication preserves L1, so every entry of L^{-1} is L1.
No left-state hypothesis or minimal representation theorem is needed for this local deduction; Yin_C_F0007 supplies the needed independent right states in its research application.

## 3. Exact Scope of the L2 Upgrade

For the stronger probes of part 2, D_i(a_k) belongs to M.
Consequently h_jD_i(a_k) belongs to L2, and the probe identity puts L^{-1}A_i T(a_k) in L2.
Inverting the finite scalar matrix of probe columns recovers every column of L^{-1}A_i in L2.
The same right-multiplication identity recovers the whole inverse in L2.

Under part 3's additional assumptions, Yin_C_F0002's polynomial vacuum formula gives D_i(p(X))=p(X)eta_i+(id tensor tau)(partial_i p)(X).
Both terms are bounded if eta_i is bounded.
Selfadjoint generators make their polynomial algebra a unital star algebra dense in L2(M); repeating the annihilator argument using only these polynomial probes therefore produces a finite basis of trace columns.
This proves the sufficient condition without assuming any L2 density of holomorphic polynomials for a merely normal tuple.
Boundedness of eta_i alone was correctly not promoted to an unconditional general-normal conclusion.

## 4. Primary Hilbert-Transform Input and the Interval Obstruction

The reviewer reopened [Tao06, Lecture Notes 4](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf), a 30-page primary PDF.
Page 1 defines the normalized kernel; Proposition 1.2 on p. 3 gives the multiplier -i sgn; p. 4 gives its isometric L2 extension and states L2 convergence of symmetric kernel truncations.
The general truncation theorem is stated there without its full proof and is retained as an accepted standard input.
Parsed primary text was inspected; no successful rendered-page inspection or full Calderon-Zygmund audit is claimed.

With that convention, D=-pi E*HE has kernel 1/(y-x) on the interval and norm at most pi.
The commutator with X(x)=x has positive kernel (y-x)/(y-x)=1, giving [D,X]=P first on smooth compactly supported functions and then on H by boundedness.
The vacuum vector is log((1-x)/x).
For 0<epsilon<1/2, the truncated integral agrees with it on (epsilon,1-epsilon); the difference on (0,epsilon) is log(x/epsilon), whose squared integral is 2 epsilon, and the other endpoint contributes the same amount.
This independently confirms the stated L2 representative, including its sign and endpoint behavior.

The logarithm is essentially unbounded.
Any difference D'-D of bounded duals commutes with the selfadjoint multiplication operator X, hence with its spectral algebra.
In the multiplicity-one standard representation this commutant is M, so the difference is multiplication by a bounded function.
Adding that function cannot remove the logarithm's essential unboundedness.
The asserted nonexistence of a bounded dual with bounded vacuum image, in particular one annihilating Omega, follows.
This is an obstruction to the normalization step, not to the already proved Yin_C_F0004 criterion.

## 5. Haar Probe Check and Final Boundaries

For the stated Haar dual, D kills every nonpositive Fourier basis vector.
The norm-convergent expansion h=-sum_{m>=1}2^{-m}U^{-m} therefore gives Dh=0 and tau(h)=0; all further D iterates vanish.
This does not say that [D,h]=0.
The bounded probe a=U has tau(hU)=-1/2, so varying probes detects the nonzero state exactly as required by the proof.

The result controls additional entries of the inverse in an explicitly stated Lp class.
It does not turn L1 into L2 without the stronger probes, or L2 into L-infinity, and does not supply bounded scalar elimination.
The finite-tracial Lp/affiliated-operator foundation and the stated Hilbert-transform interface are retained at their declared scopes.
No numerical experiment, proof assistant, external human review, publication or novelty assessment was performed.

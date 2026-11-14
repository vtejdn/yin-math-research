---
author: Yin
---

# Single-input bounds and finite columns on the original correlated tuple

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, satisfying [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix \(i\), put \(H=L^2(M,\tau)\), \(P=\mathbb C\langle X,X^*\rangle\), \(N=W^*(X_j:j\ne i)\), \(C=N'\cap M\), and write \(E_0=(\mathrm{id}\otimes\tau)\delta_i\) on \(P\).
Let \(a=\sup_{p\in P,\ \|p\|\le1}\|E_0p\|_2\) and let \(c\) be the [finite-column cost](Yin_C_F0208_v1.md#statement), allowing infinity.

If \(a<\infty\), \(E_0\) extends uniquely to a normal bounded map \(E:M\to H\) of norm \(a\), where normal means ultraweak-to-weak continuous.
There are positive densities \(h\in L^1(M)\) and \(k\in L^1(C)\), each of trace at most one, such that for every \(x\in M\)
\[
          \|Ex\|_2^2\le a^2\big(\tau(hx^*x)+\tau(kxx^*)\big).                 \tag{1}
\]
For \(C=\mathbb C1\) this gives
\[
                          a\le c\le\sqrt2\,a.                                \tag{2}
\]
In particular (2) holds for every coordinate of every such tuple with \(d\ge3\), in the extended reals, and for its adjoint tuple.
If an original column cost is infinite in this dimension, the original tuple already has no bare full-domain dual system.
For \(d\ge3\) the cubic concentration of the distinguished coordinate against all omitted shifts obeys
\[
      \int_0^\infty
      \left(\sup_{b\in N}\tau(1_{[0,r]}(|X_i-b|))\right)^3\frac{dr}{r^3}
             \ \le\ 48 a^2 .                                                 \tag{3}
\]

For \(d\ge2\) with \(a<\infty\) the projections \(q_R=1_{[0,R]}(k)\) for \(R>0\) give maps \(q_RE\) satisfying
\[
 \|q_RE(x)\|_2^2\le a^2\tau((h+R1)x^*x),\qquad
                  \|(1-q_R)E\|_{M\to H}\longrightarrow0.                   \tag{4}
\]
Thus even for a normal pair every bounded slice is an operator-norm limit of maps of finite column cost.
When \(a<\infty\) but \(c=\infty\), for every \(R\) the remaining map \((1-q_R)E\) still has infinite column cost on \(P\).
Equations (2) and (4) concern full mixed words of arbitrary length.
They do not establish finiteness of \(a\) from the vacuum hypothesis.

## Argument

### A normal extension and two normal densities

Extend \(E_0\) in operator norm to \(A=C^*(X)\).
Write \(e\) for the central support summand of the represented algebra in \(A^{**}\) and \(j:M\to eA^{**}\) for its normal identification, using the [bidual summand theorem](../audits/literature/Bla06/Yin_U002.md#bla06-u002).
The bidual of the extended map takes values in the reflexive Hilbert space and is ultraweak-to-weak continuous.
The [ACSY Hilbert adjoint theorem](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) makes \(\operatorname{Dom}E_0^*\) dense.
For each \(v\) in this domain the pairing with \(E_0p\) is the normal vector functional \(\langle E_0^*v,p1\rangle\) on \(P\).
It extends by continuity to \(A\) and its normal extension to \(A^{**}\) vanishes on \((1-e)A^{**}\).
Density makes the entire bidual map vanish there, as in the [normal summand argument for column states](Yin_C_F0211_v1.md#removing-the-singular-part-of-an-optimal-state).
Restriction along \(j\) gives \(E\) with norm at most \(a\), and the core forces equality.
Normality and ultraweak density of the core give uniqueness.

Apply [Pisier, Theorem 8.1](../audits/literature/Pis12/Yin_U002.md#pis12-u002) to the map \(A\to H\).
Its column and row states \(f,g\) need not initially be normal for \(M\).
For any \(y\) in the unit ball of \(A^{**}\), take a bounded net from \(A\) converging strong-star to \(y\) in the universal representation, by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001).
The two positive products converge ultraweakly to \(y^*y\) and \(yy^*\), and the images converge weakly to the bidual image.
Weak lower semicontinuity therefore extends the squared two-state bound to all of \(A^{**}\), with the normal bidual extensions of the states.
Setting \(y=j(x)\) yields the same inequality on \(M\) with two normal positive functionals of mass at most one.
The [finite tracial predual identification](../audits/literature/AP18/Yin_U003.md#l1-predual-interface) writes their densities as \(h,k_0\in L^1(M)_+\).

### Averaging over the omitted algebra

The forced values of \(\delta_i\) on both omitted generators and their adjoints give \(E(np)=nEp\) for omitted polynomials \(n\) and \(p\in P\), by the product rule.
Separate normal continuity extends this to \(n\in N,\ p\in M\).
For \(u\) unitary in \(N\), apply the two-density estimate to \(ux\).
The left side stays fixed, as does the column term, and the row density is replaced by \(u^*k_0u\).
Every convex average of such densities gives the same bound.

The trace-preserving conditional expectation \(k=\mathbb E_C k_0\) belongs to the \(L^1\)-closed convex hull of these conjugates.
Indeed for a bounded positive truncation \(l\) of \(k_0\), the closed Hilbert-space convex hull of its unitary conjugates has a unique element of minimum norm.
It is invariant under every such conjugation, and its projection onto the invariant subspace agrees with that of \(l\).
The invariant subspace in \(L^2(M)\) is \(L^2(C)\), since the polar part and spectral projections of an affiliated invariant vector commute with \(N\).
Hence the minimum is \(\mathbb E_C l\).
Hilbert approximation implies \(L^1\) approximation, and conjugation, its convex averages and conditional expectation are all contractions on \(L^1\).
Truncating with arbitrarily small \(L^1\) error proves the assertion for \(k_0\).
Pass to this norm limit at fixed \(xx^*\) to obtain (1).

If \(C\) is scalar, \(k=\tau(k)1\).
The trace then turns its row term into a column term.
Sum (1) over any finite column and use \(\tau(h)+\tau(k)\le2\) to get (2).
Its lower bound uses one-element columns, including when \(a=\infty\).
With at least two omitted coordinates their [scalar relative commutant](Yin_C_F0202_v1.md#statement) implies \(C=\mathbb C1\).
The actual hypothesis passes to the adjoint tuple by the [adjoint derivation theorem](Yin_C_F0073_v1.md#statement).
A bare system on \(X\) would give boundedness of every normalized right slice on \(P\) by [the normal bare-dual theorem](Yin_C_F0070_v1.md#statement).
Thus (2) rules it out at an infinite original cost for \(d\ge3\).
The [uniform cubic concentration bound](Yin_C_F0258_v1.md#statement) is \(24c^2\) whenever \(c<\infty\), yielding (3).

### Row cutoffs for a normal pair or a longer tuple

For \(d\ge2\) choose a diffuse abelian algebra \(D=W^*(X_j)\) of one omitted coordinate using the [normal starred symbol theorem](Yin_C_F0076_v1.md#statement).
All bounded multipliers in \(D'\cap M\) commute with \(E\) on \(M\).
To verify this single-coordinate use of the [compact commutator argument](Yin_C_F0202_v1.md#averaging-the-compact-polynomial-commutators-of-a-bare-witness), take a Haar unitary \(u\in D\).
For \(p\in P\) the slice identity on \(P\), \([E,L_p]=\Theta(\delta_i p)\), gives a Hilbert–Schmidt commutator, with \(\Theta(s\otimes t)x=s\tau(tx)\).
Both sides extend from \(P\) to \(M\) by normality.
There is no nonzero Hilbert–Schmidt operator commuting with \(L_u\), because its positive square would have a nonzero finite-dimensional invariant eigenspace and \(L_u\) has no eigenvectors in the tracial representation.
Consequently Cesàro averages under conjugation by \(L_u\) tend to zero in Hilbert–Schmidt norm, by the Hilbert-space mean ergodic argument.

Given \(b\in D'\cap M\), take bounded \(p_j\in P\) converging strong-star to \(b\) by Kaplansky density and polynomial norm approximation.
For each \(j\), average sufficiently many \(u^t p_j u^{-t}\) to obtain \(r_j\) with commutator Hilbert–Schmidt norm tending to zero, since \(E\) commutes with the omitted \(u,u^*\).
These \(r_j\) stay uniformly bounded and \(\|r_j-b\|_2\le\|p_j-b\|_2\), so \(r_j\to b\) strongly and ultraweakly.
For \(x\in M\), normality of \(E\) and strong convergence on \(Ex\) pass \([E,L_{r_j}]x\to0\) to \([E,L_b]x=0\).
In particular this applies to the spectral projections of \(k\), since \(C\subset D'\cap M\).

It follows that \(q_RE(x)=E(q_Rx)\).
Apply (1) to \(q_Rx\), use \(x^*q_Rx\le x^*x\) and \(kq_R\le R1\), and cycle the trace to obtain the first estimate of (4).
For \(s=1-q_R\) and \(\|x\|\le1\), (1) on \(sx\) gives
\[
   a^{-2}\|sE(x)\|_2^2
     \le \tau(hx^*sx)+\tau(ks)
     \le L\tau(s)+\tau((h-L1)_+)+\tau(ks) \qquad(L>0).
\]
Here \(\tau(x^*sx)\le\tau(s)\) and \(x^*sx\le1\).
The slice takes \(X_i\) to \(1\), so \(a>0\).
Let \(R\to\infty\) at fixed \(L\), then \(L\to\infty\), to get norm convergence.
The first estimate gives finite column cost for \(q_RE\) on the original core, so if the complementary map also had finite column cost their sum would as well.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:34 |
| status | open |
| reason | Fix the full-word column reduction on the original tuple, the normal two-state domination and the norm localization for two coordinates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Tuple-wise comparison of one-input and column costs, original separation, cubic bound and normal-pair tail localization. |
| argument | [Argument](#argument) | Normal two-state compression, omitted-unitary averaging, commutation with relative-commutant projections and trace-tail approximation. |
| dependency | [Two-state inequality](../audits/literature/Pis12/Yin_U002.md#pis12-u002) | Existence of states for a bounded map on the generated C*-algebra, with constant one on each squared term. |
| dependency | [Bidual summand](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Normal central summand for the tracial representation. |
| dependency | [ACSY adjoint and Hilbert–Schmidt commutators](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Dense adjoint domain of the sliced core operator and polynomial commutator identity. |
| dependency | [Central compression of a bounded slice](Yin_C_F0211_v1.md#removing-the-singular-part-of-an-optimal-state) | The bounded slice's bidual vanishes on the singular summand by its dense Hilbert adjoint domain. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation in the universal and trace representations. |
| dependency | [Trace densities](../audits/literature/AP18/Yin_U003.md#ap18-u003) | The additional L1 interface identifies normal positive functionals with positive integrable densities. |
| dependency | [Relative commutant and compact averaging](Yin_C_F0202_v1.md#argument) | Scalar relative commutant of two distinct coordinates and the compact-commutator averaging argument for a single diffuse omitted coordinate. |
| dependency | [Adjoint stability](Yin_C_F0073_v1.md#statement) | Actual conjugate variables transfer to the adjoint tuple. |
| dependency | [Normal bare duals](Yin_C_F0070_v1.md#statement) | Every bare dual system yields normalized bounded slices on the represented starred core. |
| dependency | [Uniform concentration](Yin_C_F0258_v1.md#statement) | Cubic integral at most 24 times the squared finite column cost. |
| dependency | [Forced normal symbols](Yin_C_F0076_v1.md#statement) | Diffuse marginals, zero starred and unstarred derivatives at omitted coordinates. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:41 |
| status | proved |
| reason | The independent finding verifies the single-input comparison in the original tuple, spectral cutoffs, normal density averaging and the cubic estimate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Tuple-wise comparison of one-input and column costs, original separation, cubic bound and normal-pair tail localization. |
| argument | [Argument](#argument) | Normal two-state compression, omitted-unitary averaging, commutation with relative-commutant projections and trace-tail approximation. |
| dependency | [Two-state inequality](../audits/literature/Pis12/Yin_U002.md#pis12-u002) | Existence of states for a bounded map on the generated C*-algebra, with constant one on each squared term. |
| dependency | [Bidual summand](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Normal central summand for the tracial representation. |
| dependency | [ACSY adjoint and Hilbert–Schmidt commutators](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Dense adjoint domain of the sliced core operator and polynomial commutator identity. |
| dependency | [Central compression of a bounded slice](Yin_C_F0211_v1.md#removing-the-singular-part-of-an-optimal-state) | The bounded slice's bidual vanishes on the singular summand by its dense Hilbert adjoint domain. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation in the universal and trace representations. |
| dependency | [Trace densities](../audits/literature/AP18/Yin_U003.md#ap18-u003) | The additional L1 interface identifies normal positive functionals with positive integrable densities. |
| dependency | [Relative commutant and compact averaging](Yin_C_F0202_v1.md#argument) | Scalar relative commutant of two distinct coordinates and the compact-commutator averaging argument for a single diffuse omitted coordinate. |
| dependency | [Adjoint stability](Yin_C_F0073_v1.md#statement) | Actual conjugate variables transfer to the adjoint tuple. |
| dependency | [Normal bare duals](Yin_C_F0070_v1.md#statement) | Every bare dual system yields normalized bounded slices on the represented starred core. |
| dependency | [Uniform concentration](Yin_C_F0258_v1.md#statement) | Cubic integral at most 24 times the squared finite column cost. |
| dependency | [Forced normal symbols](Yin_C_F0076_v1.md#statement) | Diffuse marginals, zero starred and unstarred derivatives at omitted coordinates. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0285_v1.md#finding) | All eleven direct inputs, two-state normal compression, the original bare exclusion and operator-norm convergence of the cutoffs. |

---
author: Yin
---

# A signed count of short cycles for the four-binomial obstruction

## Statement

Let the nine entries of a three-square monomial matrix over a torsion-free group have moduli that positive row and column gauges can make equal to one.
Take such gauges, use the actual regular bipartite graph of the [finite path test](Yin_C_A0276_v1.md#statement), and assume it has girth at least ten, allowing infinite girth.
For \(\ell=10,12,14,16\), let \(c_\ell\) be the sum over deck-translation orbits of unoriented simple \(\ell\)-cycles of the real part of the phase around the cycle.
Each phase is the product of the magnetic adjacency entries traversed around the cycle, using conjugate phases in the reverse direction.
These sums are finite since every orbit contains a cycle through a vertex in the six-vertex fundamental domain.
A regular nullity of at least \(1/2\) requires
\[
                     -40c_{10}+27c_{12}-7c_{14}+4c_{16}\ \ge\ 224 .
\]
For positive real coefficients after removing phases by vertex gauges, the four numbers are ordinary cycle-orbit counts.
In this case at least one of lengths twelve and sixteen must occur, even if there are many cycles of lengths ten and fourteen.
For arbitrary phases and girth at least sixteen, nullity at least \(1/2\) needs at least 56 distinct deck orbits of simple sixteen-cycles.

## The nonbacktracking polynomial

Let \(T\) be the Hermitian bipartite adjacency with lower and upper off-diagonal blocks \(A,A^*\) in the order column, row.
Define polynomials \(b_0=1,\ b_1=X,\ b_2=X^2-3,\ b_{k+1}=Xb_k-2b_{k-1}\) for \(k\ge2\).
Then \(b_k(T)\) sums phased nonbacktracking walks of length \(k\) between its endpoints.
For a step followed by its inverse the two phases multiply to one.
Removing such a pair gives three ways to extend the empty path and two ways to extend each nonempty reduced path at its end, which gives precisely the recurrence.

Put \(L=\sum_{j=0}^4(-1/2)^j b_{2j}(T)\) and denote by \(\operatorname{Tr}_{\rm col}\) the sum of the three group trace diagonals at the columns.
Since \(b_{2j}(T)\) acting on a column root uses the conjugate of the phase in the [root row recursion](Yin_C_A0276_v1.md#testing-the-three-column-roots), \(L\delta_o=v_o\) there.
In particular \(\operatorname{Tr}_{\rm col}(L^2)\ge49\dim_G\ker A\).
To record the integer coefficients explicitly, expansion by the displayed recurrence gives
\[
  256L^2=1792 b_0(T)-768 b_2(T)+352 b_4(T)-144 b_6(T)+64 b_8(T)
       -24 b_{10}(T)+10 b_{12}(T)-3 b_{14}(T)+b_{16}(T).
\]
For instance the polynomial squared on the left before multiplication by 256 is
\((b_0-b_2/2+b_4/4-b_6/8+b_8/16)^2\); the monic recurrence determines each coefficient successively from the highest power.
The constant contributes \(3\cdot1792\) to the column trace.
The terms of lengths two through eight have zero column trace by the girth hypothesis.
Thus nullity at least \(1/2\) requires the remaining four trace terms on the right to contribute at least \(256\cdot49/2-3\cdot1792=896\).

## Counting the tails of a closed walk

Any nonbacktracking closed walk of length at most sixteen has a unique maximal initial tail canceled by the terminal reversed tail, leaving a nonempty cyclically reduced closed walk.
Its cyclic core is a simple cycle: a repeated interior vertex would split the circular walk into two nonempty closed segments with nonbacktracking interiors, each containing a simple cycle of length at least ten.
This would give length at least twenty.
The phase of the two tails cancels.

Fix an unoriented simple \(\ell\)-cycle with phase \(\varphi\).
For a tail of length zero there are \(\ell/2\) attachment vertices of column type.
For a positive tail length \(h\), exactly \(\ell/2\) attachment vertices have the type making the final tail endpoint a column.
From each such vertex the first outward tail edge has one choice, since the vertex has degree three and two edges run along the cycle.
Every later step has two choices.
The maximal-tail decomposition recovers the pointed cycle, the tail and the orientation uniquely from the closed walk.
Translations stabilizing the finite cycle form a finite group, since they act faithfully on its vertex set by the free deck action.
Torsion-freeness makes this stabilizer trivial.
Consequently after moving the tail endpoint to its chosen fundamental-domain representative the two orientations contribute together \(\ell\operatorname{Re}\varphi\) at length \(\ell\), and \(\ell\,2^{h-1}\operatorname{Re}\varphi\) at length \(\ell+2h\) for \(h\ge1\).

In the combination of lengths ten through sixteen the resulting coefficients of \(c_{10},c_{12},c_{14},c_{16}\) are respectively
\[
    10(-24+10-6+4)=-160,\quad
    12(10-3+2)=108,\quad
    14(-3+1)=-28,\quad
    16 .
\]
Dividing the threshold 896 by four gives the asserted inequality.
If the girth is at least sixteen only \(4c_{16}\) survives; each cycle orbit contributes at most one to \(c_{16}\), proving the final count.

## Assessment history

### Decision signed-traces-of-closed-cycles

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | The exact nonbacktracking polynomial and the free action on cycles give the signed count on the original graph. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [The nonbacktracking polynomial](#the-nonbacktracking-polynomial) | Independent expansion and the unnormalized trace threshold. |
| argument | [Counting the tails of a closed walk](#counting-the-tails-of-a-closed-walk) | The cyclic core, tail multiplicities and conjugate phases. |
| review | [Signed traces of closed cycles](../audits/reviews/Yin_R_A0209_v1.md#signed-traces-of-closed-cycles) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-signed-traces-of-closed-cycles)

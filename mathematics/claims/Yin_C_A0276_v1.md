---
author: Yin
---

# Short closed paths forced by a half-dimensional four-binomial kernel

## Statement

Let \(A=(a_{ij}g_{ij})_{1\le i,j\le3}\) be the monomial matrix associated with the [four-binomial obstruction](Yin_C_A0266_v3.md#the-only-three-row-pattern-left), with all \(a_{ij}\in\mathbb C^\times\).
Its regular bipartite graph has vertices \((j,h)\) at the columns and \((i,g_{ij}h)\) at the rows, joined for every \(i,j,h\) with edge coefficient \(a_{ij}\).
Use the unnormalized trace \(\operatorname{Tr}_G\) and put \(\delta=\dim_G\ker A\).
All conclusions below hold for any discrete labeling group, including groups for which no scalar injectivity hypothesis is available.

Suppose positive row and column scalings make the nine moduli equal to one.
In the resulting matrix put \(D_m=1+3m/2\) for each positive integer \(m\).
For each of the three column roots \(o=(j,1)\), form all nonbacktracking paths of even length at most \(2m\) starting at \(o\), including the empty path.
Give a path of length \(2k\) a coefficient of modulus \(2^{-k}\), with the signed phase specified below.
Let \(v_o\) be the vector obtained by adding the coefficients of paths with the same column endpoint.
Then
\[
    \delta\le D_m^{-2}\sum_o\|v_o\|^2 .
\]
If \(\delta\ge1/2\), at \(m=4\) the signed cross terms between distinct paths in these three sums total at least \(7/2\).
In particular there are at least seven unordered same-endpoint pairs, counted with their column roots, and a nonempty reduced closed path of length at most sixteen.
This condition uses the actual group products and complex phases.

There is also a coefficient-independent test for arbitrary nonzero complex entries.
Given \(0<d\le1\), put \(n=\lceil 12^{6/d}\log(12/d)\rceil\).
If \(\delta\ge d\), the regular graph has a nonempty reduced closed path of length at most \(2n\).
More precisely, after the scaling below the sum of the signed trace terms of \((I-A^*A/3)^n\) coming from closed walks which lift to open walks on the universal tree is at least \(d/4\).
The large bound in this statement has no dependence on the sizes, phases or arithmetic nature of the coefficients.

## Testing the three column roots

Positive invertible row and column scalings preserve the module dimension of the kernel, since the right column gauge gives an invertible map of kernels.
Work with the scaled matrix and write \(p\) for its kernel projection.
At a step from a column \(y\) through row \(r\) to column \(z\), use the phase \(a_{rz}/a_{ry}\), reading the coefficients from their base positions.
For a nonbacktracking path \(\gamma\) let \(u(\gamma)\) be the product of these phases.
For \(f\in\ker A\) the row equation divided by its coefficient at the parent gives that the sum of the two phased child values is the negative of the parent value.
Thus for paths of length \(2k\) starting at \(o\),
\[
        \sum_{\gamma} u(\gamma) f(\operatorname{end}\gamma)
                    =(-1)^k\,3\,2^{k-1}f(o)\qquad(k\ge1).
\]
There are three choices of first row, two at each subsequent column, and two choices of child at each intervening row.
This induction counts paths with multiplicities also when vertices coincide.

The vector \(v_o\) uses coefficient \((-1/2)^k\overline{u(\gamma)}\) and the empty coefficient one.
With scalar product linear in its second slot the identity gives \(\langle v_o,f\rangle=D_m f(o)\), hence \(p v_o=D_m p\delta_o\).
Bounding \(\|p v_o\|\) by \(\|v_o\|\) and summing the three root diagonals proves the estimate.
The sum of the individual squared moduli for each root is \(D_m\), since the number at level \(k\ge1\) is \(3\cdot2^{2k-1}\).
At \(m=4\) the excess over these diagonal terms is therefore at least \(7^2/2-3\cdot7=7/2\).
Two nonempty paths contribute a cross term at most \(2(1/2)^2=1/2\).
A nonempty path returning to the empty endpoint has length at least four because a two-step nonbacktracking path changes its base column, so its cross term also contributes at most \(1/2\).
Any same-endpoint pair gives a closed walk by going out along one path and back along the other.
Its reduction is nonempty because the two paths are distinct and reduced, and its length is at most \(4m\).

## Scaling and an exposed matching on the universal tree

For arbitrary coefficients choose positive row and column scalings so \(p_{ij}=|a_{ij}|^2\) is doubly stochastic.
For existence, minimize \(\sum_i\log(\sum_j |a_{ij}|^2 e^{x_j})-\sum_jx_j\) on \(\sum_jx_j=0\).
There the objective is bounded below by \(3\max_j x_j+\sum_i\log\min_j|a_{ij}|^2\), so it attains a minimum.
Normalize each row of the rescaled table to sum one.
The critical equations give equal column sums, hence also one; taking square roots gives the claimed gauges.
Both the free and the actual \(A\) now have norm at most \(\sqrt3\) by the row and column sum test applied to the moduli.

There is a matching with \(p_{i\sigma(i)}\ge1/4\) in every row.
Indeed if \(r\) rows had fewer than \(r\) neighbors at this threshold, the mass on the complement of some \(r-1\) columns in those rows would be at least one.
It would be strictly less than \(r(4-r)/4\le1\), a contradiction.
Hall's theorem supplies \(\sigma\).

Take the universal covering tree of the base \(K_{3,3}\), represented by putting identity labels on a spanning tree and the four free generators on its chords.
Its deck group is the free group of rank four.
On that tree let \(B(z)=D+zO\), where \(D\) retains the chosen matching and \(O\) retains every other edge.
For each \(|z|=1\), its weighted operator is unitarily gauge equivalent to \(B(1)\): root the tree and define the vertex phases successively along the unique paths so as to absorb the edge phases.
The row and column gauges multiply each root basis vector by a phase, so all root diagonals of the corresponding continuous functions of \(B(z)^*B(z)\) agree with those at \(z=1\).

For \(\epsilon>0\) write \(Q=B^*B+\epsilon I,\ R=BB^*+\epsilon I\).
The differentiable trace \(f_\epsilon(z)=\operatorname{Tr}_{F_4}\log Q\) is subharmonic.
Indeed cyclicity and the resolvent formula for \(\log\) give \(\partial\operatorname{Tr}\log Q=\operatorname{Tr}(Q^{-1}B^*O)\).
Differentiating in \(\bar z\), using \(I-BQ^{-1}B^*=\epsilon R^{-1}\), gives
\[
       \bar\partial\partial f_\epsilon
              =\epsilon\operatorname{Tr}_{F_4}(Q^{-1}O^*R^{-1}O)\ge0 .
\]
The last trace is the squared trace norm in \(L^2\) of \(R^{-1/2}OQ^{-1/2}\), times the displayed \(\epsilon\) in the derivative.
The mean value inequality and the circle equivalence give \(f_\epsilon(1)\ge f_\epsilon(0)=\sum_i\log(p_{i\sigma(i)}+\epsilon)\).
Monotone passage to \(\epsilon\downarrow0\) gives \(\int\log x\,d\mu(x)\ge-3\log4\), where \(\mu\) is the unnormalized trace spectral measure of \(B(1)^*B(1)\).
In particular it has no mass at zero; it has total mass three and support in \([0,3]\).

## Detecting closed walks at one finite moment

The logarithmic bound implies \(\int\log(3/x)\,d\mu(x)\le3\log12\).
Choose \(\eta=3\cdot12^{-6/d}\).
Then \(\mu([0,\eta])\le d/2\) and
\[
    \int (1-x/3)^n\,d\mu(x)
             \le d/2+3\exp(-n\eta/3)\le 3d/4 .
\]
The same positive polynomial on the actual graph dominates its kernel projection, so its unnormalized trace is at least \(d\).
Every term in either trace is a weighted walk from a column root, with at most \(2n\) edges.
The terms of walks closing on the universal tree occur with the same coefficients in the actual graph by the covering map, including all choices of identity factors.
The excess of the actual trace is exactly the sum asserted in the statement.
Positive excess forces a closed walk of the specified length whose reduction is nonempty on the tree, which proves the result.

## Assessment history

### Decision endpoint-path-sums-and-the-universal-tree

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | The finite signed path sums and the universal-tree logarithmic estimate bound the actual group kernel. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [Testing the three column roots](#testing-the-three-column-roots) | The level recursion, finite norm and signed collision threshold. |
| argument | [Scaling and an exposed matching on the universal tree](#scaling-and-an-exposed-matching-on-the-universal-tree) | The matching threshold and regularized trace logarithm. |
| argument | [Detecting closed walks at one finite moment](#detecting-closed-walks-at-one-finite-moment) | An explicit degree and the excess from actual relations. |
| review | [Endpoint path sums and the universal tree](../audits/reviews/Yin_R_A0209_v1.md#endpoint-path-sums-and-the-universal-tree) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-endpoint-path-sums-and-the-universal-tree)

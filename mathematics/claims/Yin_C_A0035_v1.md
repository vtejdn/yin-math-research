---
author: Yin
---
# Three coupled fibers without fixed internal ratios on a twelve-by-twelve four-coset table

## Statement

Use the Nielsen–Soelberg sets \(A=\{a_1,\ldots,a_8\}\), \(B=\{b_1,\ldots,b_8\}\) in \(G_3\), and \(w=yxy\) in the notation of [the two cyclic covers](../ledger/Yin_L_A0042_v1.md#the-two-covers).
Enlarge the supports to \(A\cup wA\) and \(B\cup Bw\), retaining the four right and four left cosets of \(\langle w\rangle\) respectively.
In this Claim the original eight elements on each side retain their original indices.
In order, the additional row elements \(9,10,11,12\) are \(w a_1,w a_3,w a_6,w a_7\), and the additional column elements are \(b_2 w,b_3 w,b_6 w,b_7 w\).
This differs from the interleaved order on the one-sided extension in the [eight-by-twelve calculation](../ledger/Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation).
Write \(U_i,V_j\) for the nonzero complex coefficients and call \((i,j)\) a cell of the fiber indexed by its group product.

The 37 two-term cancellation equations, after normalizing \(U_1=V_1=1\), define a single torus of dimension six.
Among the larger actual fibers, fifteen have all within-fiber ratios nonconstant on this torus.
The following three are among those fifteen:
\[
\begin{split}
 F&=\{(1,12),(3,11),(12,10)\},\\
 G&=\{(3,12),(6,3),(7,2)\},\\
 T&=\{(1,2),(2,3),(3,1),(5,12),(12,5)\}.
\end{split}                                                            \tag{1}
\]
Any two of their coefficient equations admit a full-support rational solution satisfying all 37 two-term equations.
The three equations together admit no solution even after retaining only the following five of the two-term equations:
\[
\begin{array}{c|c}
 (6,2)&(7,1)\\
 (1,1)&(2,2)\\
 (3,5)&(6,1)\\
 (2,1)&(5,5)\\
 (2,11)&(5,10).
\end{array}                                                             \tag{2}
\]
Every row in (2) lists one entire two-element fiber.
These eight fibers therefore exclude a zero product over any commutative domain on any actual table containing them with their stated multiplicities and the indicated common row and column labels.
Other labels and other product fibers may be present.

## An identity using five double fibers

Work in the fraction field of the coefficient domain and normalize \(U_1,V_1\) to one by independent scalar rescalings.
The first two doubles in (2) give \(U_6V_2=-U_7\) and \(U_2V_2=-1\), so \(U_6/U_7=U_2\).
The next two give \(U_3/U_6=-1/V_5\) and \(U_2/U_5=-V_5\), hence \(U_3/U_7=U_5\).
Finally \(U_2 V_{11}=-U_5V_{10}\) gives \(V_{10}/V_{11}=V_5\).
For any fiber \(D\), denote its coefficient by \(P_D=\sum_{(i,j)\in D}U_iV_j\).
Using these three identities in (1) gives
\[
\begin{aligned}
 P_G/U_7 &= U_5V_{12}+U_2V_3+V_2,\\
 P_F/V_{11} &= V_{12}/V_{11}+U_3+U_{12}V_5,\\
 P_T &= V_2+U_2V_3+U_3+U_5V_{12}+U_{12}V_5 .
\end{aligned}
\]
Consequently
\[
                  P_G/U_7+P_F/V_{11}-P_T=V_{12}/V_{11}\ne0 .            \tag{3}
\]
This deduction uses the whole coefficient equations as written, so it also proves the statement about additional labels outside these eight fibers.

## The true fibers and all binary solutions

The [faithful integer model](../ledger/Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation) gives the original group labels and preserves equality of all their products.
It therefore applies to the translated labels as well.
The [exact product-table verifier](../computations/programs/Yin_J_A0003/readme.md) uses integer group multiplication to enumerate these fibers.
The complete table on the enlarged supports has 37 fibers of size two, ten of size three, five of size four and four of size five.
In the following table a row pair \((i,k)\) and a column arrow \(j\to l\) designate the actual double \(\{(i,j),(k,l)\}\).
Thus the required ratio is \(V_l/V_j=-U_i/U_k\).
The last column is expressed in the parameters introduced below.

| Row pair | Column arrows | Common ratio |
| --- | --- | --- |
| \(1,2\) | \(1\to2,\ 4\to5,\ 6\to7,\ 11\to12\) | \(z/y\) |
| \(2,5\) | \(1\to5,\ 6\to3,\ 8\to7,\ 11\to10\) | \(x/y\) |
| \(3,6\) | \(5\to1,\ 7\to8,\ 10\to11\) | \(y/x\) |
| \(4,7\) | \(1\to5,\ 6\to3,\ 11\to10\) | \(x/y\) |
| \(5,8\) | \(1\to2,\ 4\to5,\ 6\to7,\ 9\to10,\ 11\to12\) | \(z/y\) |
| \(6,7\) | \(2\to1,\ 5\to4,\ 7\to6,\ 10\to9,\ 12\to11\) | \(y/z\) |
| \(9,10\) | \(5\to4,\ 7\to6,\ 10\to9,\ 12\to11\) | \(y/z\) |
| \(10,11\) | \(3\to6,\ 5\to1,\ 7\to8,\ 10\to11\) | \(y/x\) |
| \(11,12\) | \(2\to1,\ 5\to4,\ 7\to6,\ 10\to9,\ 12\to11\) | \(y/z\) |

Use six independent nonzero coefficient parameters
\[
          (a,b,c,x,y,z):=(U_7,U_{12},V_8,V_{10},V_{11},V_{12}).
\]
Here \(x,y\) denote field elements only in the coefficient formulas.
Then the normalized solutions to all the doubles are precisely
\[
\begin{aligned}
(U_1,\ldots,U_{12})={}&
\left(1,-\frac y z,\frac{a y^2}{xz},-\frac{a x}{y},
       \frac{y^2}{xz},-\frac{a y}{z},a,-\frac{y^3}{xz^2},
       -\frac{b y^3}{xz^2},\frac{b y^2}{xz},-\frac{b y}{z},b\right),\\
(V_1,\ldots,V_{12})={}&
\left(1,\frac z y,\frac{c x^2}{yz},\frac x z,\frac x y,
       \frac{c x} z,\frac{c x} y,c,\frac{xy}{z},x,y,z\right).
\end{aligned}                                                          \tag{4}
\]
For necessity, the \(11\to12\) and \(1\to2\) arrows for rows \(1,2\) first give \(U_2,V_2\).
The \(12\to11\) arrow for \(6,7\) gives \(U_6\), and \(10\to11\) for \(3,6\) gives \(U_3\).
The \(5\to1\) arrow for \(3,6\) gives \(V_5\), then \(5\to4\) for \(6,7\) gives \(V_4\).
The two \(1\to5\) and \(1\to2\) arrows for \(2,5\) and \(5,8\) give \(U_5,U_8\).
The \(11\to10\) arrow for \(4,7\) gives \(U_4\), and \(10\to9\) for \(6,7\) gives \(V_9\).
Use \(7\to8\) for \(3,6\), \(6\to7\) for \(1,2\), and \(6\to3\) for \(2,5\) to obtain \(V_7,V_6,V_3\) in that order.
The last three row coefficients to be determined are \(U_{11},U_{10},U_9\), from \(12\to11\) for \(11,12\), \(10\to11\) for \(10,11\), and \(12\to11\) for \(9,10\).
This gives (4) without imposing any condition on the six parameters.
Conversely substitution into (4) gives both row and column ratios in the last column of the table for every displayed arrow.
The parametrization and its inverse, projection to the six designated coordinates, are regular on the tori.

## Nonconstant ratios and proper subsystems

Substitution of (4) gives
\[
\begin{aligned}
 P_F &= z+a x^{-1}y^3z^{-1}+b x,\\
 P_G &= a x^{-1}y^2-a c x^2z^{-2}+a y^{-1}z,\\
 P_T &= y^{-1}z-c x^2z^{-2}+a x^{-1}y^2z^{-1}
                              +x^{-1}y^2+bxy^{-1}.
\end{aligned}
\]
The exponent vectors in each displayed line are pairwise distinct.
Since all six parameters are free, no ratio between two terms in any one of the three fibers is fixed by the binary equations.
Applying the same comparison before collecting terms in every larger fiber gives eight triples, five quadruples and two quintuples with pairwise distinct exponent vectors.
This is a test on representations in each actual fiber; replacing two equal exponents by their summed coefficient before testing could lose a forced ratio.

For \(a=x=y=z=1\) the three equations become \(2+b=0,\ 2-c=0,\ 3+b-c=0\), respectively.
The pairs \((b,c)=(-2,2),(-2,1),(-1,2)\) solve respectively \((F,G),(F,T),(G,T)\).
All coefficients in (4) remain nonzero at these rational points.
Thus retaining the binary equations and any proper subset of the three selected larger equations permits cancellation on that subsystem.
Imposing all three fails by (3), hence so does imposing the entire collection of fifteen fibers with no fixed internal ratio.
This excludes these supports for [A0001](../tasks/Yin_T_A0001_v1.md#contract) directly from their coefficients, without a regular-rank hypothesis.

The eight equations in (1)–(2) form an inclusion-minimal inconsistent subsystem over \(\mathbb Q\) and over \(\mathbb C\).
To check deletion of the \(k\)-th double in (2), set \(V_2=2\), use row \(k\) below, and put every unspecified vertex coefficient equal to one.
\[
\begin{array}{c|rrrrrrrr|r}
 k&U_2&U_3&U_5&U_6&U_{12}&V_3&V_{10}&V_{12}&P_{\mathrm{omitted}}\\ \hline
 1&-1/2&1&1/2&-1&-2&3&1&1&-1\\
 2&-1/4&1/2&1/4&-1/2&-3/2&5&1&1&1/2\\
 3&-1/2&-1/2&1/2&-1/2&-1/2&3&1&1&-1\\
 4&-1/2&1/2&-1/6&-1/2&5/6&6&-3&2&-2/3\\
 5&-1/2&1/2&1/2&-1/2&-1/2&5&3&1&1
\end{array}
\]
Substitution gives zero in the other four doubles and all three of \(F,G,T\) in every row, as the [exact rational verifier](../computations/programs/Yin_J_A0003/verify_coupling.py) also checks.
The preceding three specializations handle deletion of \(F,G\) or \(T\), completing all eight cases.

## Assessment history

### Decision coupled-three-fiber-identity

| Field | Value |
| --- | --- |
| date | 2026-11-17T01:30 |
| status | proved |
| reason | The independent review checked the actual group fibers, the complete binary solution family and the witnesses for each deletion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The twelve-by-twelve table and the eight-equation obstruction on any table carrying its exact labeled fibers. |
| argument | [Proof](#an-identity-using-five-double-fibers) | The Laurent identity, variable ratios on the full binary solution family, and inclusion-minimality over the rationals and the complex numbers. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0066_v1.md#whole-argument-finding) | Independent verification of the proof and every proper-deletion witness. |

## Current assessment

[Selected decision](#decision-coupled-three-fiber-identity)

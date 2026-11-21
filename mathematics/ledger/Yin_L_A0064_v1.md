---
author: Yin
---
# Overlap and basis certificates for sparse-alphabet cone outputs

## Scope and the exact alphabet law

Fix one tuple and the complete covering family from [C92](../claims/Yin_C_A0092_v1.md#statement), including every cone configuration needed at its bounded-cone cutoff.
Let \(\mathcal A\) be its complete inclusion-minimal nonempty family of neutral label supports, retaining sizes at most \(s=62\).
Write \(D=8252\), let \(S\) be a uniformly chosen \(s\)-subset of the neutral inverse-pair types, and put
\[
 E_A=\{A\subseteq S\},\qquad
 E=\bigcup_{A\in\mathcal A}E_A,\qquad
 q_t=\frac{\binom{s}{t}}{\binom{D}{t}}
     =\frac{(s)_t}{(D)_t},
                                                                    \tag{1}
\]
with \(q_0=1\) and \(q_t=0\) for \(t>s\).
For every finite family \(A_1,\ldots,A_j\),
\[
             \Pr(E_{A_1}\cap\cdots\cap E_{A_j})
                      =q_{|\bigcup_i A_i|}.                  \tag{2}
\]
Thus all probabilities below are for the actual fixed-size sampling law.
They do not replace it by independent Bernoulli sampling.

C92 proves
\[
 \Pr\{\operatorname{rk}_{K_S}R_{S,H}\ge1/128\}\le\Pr(E).
                                                                    \tag{3}
\]
Any upper bound \(\Pr(E)\le1/4000\) therefore excludes the erasure event in [C91](../claims/Yin_C_A0091_v1.md#statement).
The new bounds below improve the union bound using verified overlap or finite row-basis information.
No assertion is made that an original safeguarded four-line tuple supplies the required information.
An upper bound on finite sparse-output existence is used throughout; finite ordinary dimension is not identified with regular module dimension.

## A forest bound and common-core caps

Let \(\mathcal F\) be any forest with vertex set \(\mathcal A\).
Then
\[
 \Pr(E)\le
       \sum_{A\in\mathcal A}q_{|A|}
          -\sum_{\{A,B\}\in E(\mathcal F)}q_{|A\cup B|}.
                                                                    \tag{4}
\]
For a fixed alphabet, mark precisely those vertices \(A\) for which \(A\subseteq S\).
The number of marked vertices minus the number of forest edges joining marked vertices is the number of components of the induced marked forest.
It is zero when no vertex is marked and at least one otherwise.
Taking expectations proves (4).
No independence, sign of correlation, or geometric realizability assumption enters this probability identity.

One can choose a maximum-weight spanning forest with edge weight \(q_{|A\cup B|}\).
A simpler safe greedy procedure orders the sets and, for each new set, subtracts its intersection probability with one chosen earlier parent.
The resulting edges form a forest, so (4) remains valid whether or not the choice is optimal.
Subtracting every pairwise intersection without the forest restriction would instead be a lower Bonferroni bound and is not a valid upper certificate.

If a cluster \(\mathcal C\subseteq\mathcal A\) has a common contained set \(C\subseteq\bigcap_{A\in\mathcal C}A\), then
\[
              \Pr\Bigl(\bigcup_{A\in\mathcal C}E_A\Bigr)
                              \le q_{|C|}.                    \tag{5}
\]
Partitioning the family into clusters gives a safe capped bound: for each cluster use the smaller of (5) and its forest bound, then sum over clusters.
Greedy cluster selection affects sharpness, not validity.
This can handle a large number of minimal supports sharing a small fixed core.

For instance, \(m\) distinct triples sharing one pair \(C\) have probability at most \(q_2\), regardless of \(m\).
If their remaining labels are \(m\) distinct labels outside \(C\), the probability is exactly
\[
 q_2\left(1-
        \frac{\binom{D-2-m}{s-2}}{\binom{D-2}{s-2}}\right).
                                                                    \tag{6}
\]
Condition first on selecting the core and then require at least one of those \(m\) labels.
This example is an antichain calculation; its occurrence as a complete covering antichain of an original four-line tuple is not established.

## A strict improvement at the required threshold

Take 619 triples on 621 distinct neutral labels:
\[
                 A_i=\{i,i+1,i+2\},\qquad1\le i\le619.
\]
Their common intersection is empty, so there is no common pair-core.
Consecutive triples have union size four.
Using the path with edges \(\{A_i,A_{i+1}\}\) in (4) gives
\[
 \Pr(E)\le619q_3-618q_4<\frac1{4000},\qquad
 619q_3-618q_4\approx0.0002482740457743743,
                                                                    \tag{7}
\]
whereas their union bound is
\[
 619q_3>\frac1{4000},\qquad
 619q_3\approx0.0002500596787727072.
\]
Both comparisons were made using the exact rational quantities (1).
Thus overlap data can cross the actual C91 threshold without a common-core simplification.

For a separate exact check, count subsets of the 621 active labels containing no three consecutive labels.
Let \(a_{n,k,r}\) count binary strings of length \(n\), with \(k\) ones and final run length \(r\in\{0,1,2\}\), containing no run of three ones.
Start at \(a_{0,0,0}=1\), use
\[
 a_{n+1,k,0}=\sum_{r=0}^2a_{n,k,r},\qquad
 a_{n+1,k+1,1}=a_{n,k,0},\qquad
 a_{n+1,k+1,2}=a_{n,k,1},
\]
and set inadmissible indices to zero.
The exact bad probability is
\[
 1-\frac{\displaystyle
      \sum_{k=0}^{62}\sum_{r=0}^2
               a_{621,k,r}\binom{8252-621}{62-k}}
          {\binom{8252}{62}}
       \approx0.0002482478064683776.
                                                                    \tag{8}
\]
The exact rational comparison also verifies that (8) is at most (7).
The sliding-triple family is a probability diagnostic, not a claimed full-cone realization in the original construction.

## Fractional covers by contained cores

Choose finitely many nonempty cores \(C\), and nonnegative rational weights \(w_C\), satisfying
\[
                    \sum_{C\subseteq A}w_C\ge1
                          \qquad(A\in\mathcal A).
                                                                    \tag{9}
\]
Then
\[
                          \Pr(E)\le\sum_C w_C q_{|C|}.        \tag{10}
\]
Indeed, if \(A\subseteq S\), every core contained in \(A\) is also contained in \(S\), so the sum \(\sum_{C\subseteq S}w_C\) is at least one.
Take expectations.
Using only the cores \(C=A\) with weight one recovers the union bound; a shared core recovers (5).
The constraints (9) must cover the complete minimal-support family, not only the supports seen in one-, two-, or three-cone calculations.

In particular, a fractional cover by pair-cores with total weight at most \(9/2\) is sufficient:
\[
 \frac92 q_2<\frac1{4000},\qquad
 \frac92 q_2\approx0.0002499586853644791.
                                                                    \tag{11}
\]
The exact allowed total pair weight is
\[
                 \frac{1}{4000q_2}
                    \approx4.500743786356425.
\]
The bound (11) is sufficient and can be verified by a rational linear certificate.
It does not assert that such a cover exists for the source antichain.

An ordinary vertex fractional transversal used only through its first moment cannot achieve this threshold.
If \(w_i\ge0\) and \(\sum_{i\in A}w_i\ge1\) for every bad set, Markov's inequality gives
\[
                 \Pr(E)\le\frac{s}{D}\sum_iw_i.
\]
For a nonempty family, \(\sum_iw_i\ge1\), while \(s/D>1/4000\) and \(s/D\approx0.0075133301\).
This is a limitation of that first-moment estimate, not of every weighted-transversal method.
For integer weights \(k_i\ge0\) and a positive threshold \(K\) with \(\sum_{i\in A}k_i\ge K\), the full weighted hypergeometric tail is instead the valid bound
\[
 \Pr(E)\le
 \frac{[z^{62}y^{\ge K}]
                  \prod_{i=1}^{8252}(1+zy^{k_i})}
      {\binom{8252}{62}}.
\]
Rational weights can be scaled to integers.
The coefficient notation sums the \(y\)-degrees at least \(K\).
This finite computation retains the weight distribution that the first moment loses.

## A grouped row-basis certificate

This test can avoid enumerating the minimal support antichain.
For each covering configuration, first restrict its full output space to vectors supported only on neutral edges; nonneutral edge coordinates must be zero for every sampled alphabet.
Take the direct sum \(V\) of these restricted finite output spaces, retaining separate copies of coordinates from different configurations.
Group its coordinate rows by their neutral inverse-pair label.
The event \(E\) is exactly that \(V\) contains a nonzero vector supported on the blocks with labels in \(S\).
Taking a direct sum, rather than adding outputs in one shared edge space, introduces no new cross-configuration cancellations.

Suppose pairwise label-disjoint sets \(B_1,\ldots,B_t\) each contain enough coordinate rows to give an injective projection on the whole \(V\):
\[
       \operatorname{rank}\bigl(V\longrightarrow
                   \text{coordinates with labels in }B_j\bigr)
                              =\dim V,\qquad1\le j\le t.
                                                                    \tag{12}
\]
A full row basis can be retained as a finite certificate for each equality.
If \(S\) misses any \(B_j\), every vector supported on \(S\) has zero projection there and hence is zero.
Therefore a bad \(S\) must meet every \(B_j\).
Writing \(b_j=|B_j|\), this gives the exact sufficient bound
\[
 \Pr(E)\le
 \frac{\displaystyle\sum_{J\subseteq\{1,\ldots,t\}}
          (-1)^{|J|}
          \binom{D-\sum_{j\in J}b_j}{s}}
      {\binom Ds}
 \ \le\ \left(\prod_{j=1}^t b_j\right)q_t.
                                                                    \tag{13}
\]
The first expression is one minus the inclusion-exclusion probability of missing at least one block.
For the second, choose one sampled label from each block and use the union bound on these \(t\)-element transversals; the blocks being disjoint makes all chosen labels distinct.
If \(t>s\), hitting all the blocks is impossible.

For example, three disjoint common basis-label sets, each with at most eight labels, suffice:
\[
 \Pr(E)\le512q_3<1/4000,\qquad
 512q_3\approx0.0002068345000510922.
\]
Two such sets of size at most two give \(4q_2<1/4000\); four of size at most seventeen give \(17^4q_4<1/4000\).
All three numerical comparisons use exact rational arithmetic.
Each basis must work for the entire covering direct sum, not just one selected cone or one selected cycle.
For a nonzero \(V\), the sets \(B_j\) are nonempty.
If \(V=0\), the bad probability is already zero.

Because one label can contain many coordinate rows, the label rank function is a representable polymatroid in general, not an ordinary matroid with one row per label.
An ordinary matroid circuit-packing assertion cannot be transferred to these label blocks without proof.
Condition (12) is stated directly in finite linear algebra and remains valid with arbitrary block sizes and folds.

## Necessary restrictions and the limits of local contact tests

Five distinct two-label minimal supports already make the probability that some covering configuration has a nonzero sparse output larger than the allowed threshold.
For any such five sets, their pairwise unions have at least three labels, so
\[
 \Pr(E)\ge5q_2-10q_3>1/4000,\qquad
 5q_2-10q_3\approx0.0002736921362980761.
                                                                    \tag{14}
\]
This is the second Bonferroni inequality and uses \(q_{|A\cup B|}\le q_3\).
Thus any certificate of \(\Pr(E)\le1/4000\) must globally leave at most four two-label minimal supports.
It does not follow that the regular-rank event in (3) has probability above the threshold; (3) is only a one-way inclusion.

Minimum support size three and bounded label incidence alone are also insufficient.
For 619 disjoint triples, each label has incidence one, but
\[
 \Pr(E)\ge619q_3-\binom{619}{2}q_6>1/4000,\qquad
 619q_3-\binom{619}{2}q_6\approx0.0002500328184603465.
                                                                    \tag{15}
\]
This contrasts with the 619 sliding triples in (7), which have the same individual probabilities and a successful upper bound.
The disjoint-triple pattern is realizable by triangular cone cycles with disjoint alphabets and relators \(a_i b_i c_i\).
Each relator eliminates its own \(a_i\), so the resulting presentation complex retracts to a graph and its group is free.
The minimal label sets for the selected cycle spaces are precisely those disjoint triples.
This supplies an aspherical torsion-free cone calibration with label incidence one.
It is not an original four-line tuple and has triangle girth, not the source's logarithmically increasing girth.

There is a separate four-cone obstruction to relying only on two- and three-cone rank tests.
The outside matrix
\[
 O=\begin{pmatrix}
 1&-1&0&0\\
 0&1&-1&0\\
 0&0&1&-1\\
 -1&0&0&1
 \end{pmatrix}
\]
has kernel spanned by \((1,1,1,1)\), whereas every proper subset of its four columns is independent.
Appending four distinct inside rows \(I_4\) makes the full columns independent.
Every outside row meets just two columns, and the contact graph has degree two, but the full four-column sparse output survives.

This contact pattern has an actual elementary cone realization.
Use generators \(a_i,c_i\), \(1\le i\le4\), with cyclic indices, and four triangular relators
\[
                         a_i c_i c_{i+1}^{-1}.
\]
Each unique \(a_i\) can be eliminated, leaving the free group on \(c_1,\ldots,c_4\); the associated cone complex retracts to that rose.
Take the \(i\)-th lifted triangle based at \(x_i=c_1c_{i+1}^{-1}\).
Its \(a_i\)-edge runs to \(x_{i-1}=c_1c_i^{-1}\), followed by the \(c_i\)-edge to the common center \(c_1\), and then the inverse \(c_{i+1}\)-edge back to \(x_i\).
The outside \(c_i\)-spokes cancel in the sum of the four cycles, leaving the four inside \(a_i\)-edges.
Up to row and column permutation, this is exactly the displayed matrix.
Selecting any proper subfamily leaves an outside anchor and no nonzero sparse combination.
Again, this verifies generic aspherical torsion-free realizability, not occurrence in the original four-line population and pattern safeguards.

These examples show that low incidence or verification of subfamilies with at most three cones need not supply the global inputs to (4), (9), or (12) in general cone configurations.
The C92 covering cutoff permits configurations with more than three cones; this bound does not establish that any specific four-line tuple requires such a configuration.
The probability law also retains dependence even for disjoint label supports: for disjoint nonempty \(A,B\), \(q_{|A|+|B|}<q_{|A|}q_{|B|}\) whenever both can fit in the sample.
Thus a dependency graph that declares such events independent is not valid for the fixed-size draw.
The forest, core, and basis bounds above avoid that issue by using exact containment probabilities or pointwise certificates.

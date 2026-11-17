---
author: Yin
---

# How many product fibers must merge when a vertex color disappears?

Take a connected Ope26f matching on \(n\) vertices on each side with the prescribed types and girth at least three.
Write \(J\) for the number of ordered vertex pairs whose group-product fiber contains more than one simultaneous-step component.
Let \(r_A,r_B\) count vertices on each side with a group label also carried by a different vertex on that side.
These counts include even repetitions that disappear in the binary group algebra and odd repetitions that still leave a coefficient one.

## A lower bound on each row and column

Put \(p=129/16513\) and \(\beta=126p(1-2/129-3p)>0.9459\).
Every vertex carries \(129\) ordinary letters; at most three of those letters are paired with extras.
For each of its at least \(126\) ordinary letters \(t\) with ordinary inverse, the [minimum-degree estimate](../claims/Yin_C_A0046_v1.md#isolated-edges-and-their-bipartite-graphs) gives at least \(np(1-2/129-3p)\) choices of the opposite vertex for which the pair lies on an isolated simultaneous edge of label \(t\).
That estimate applies to either orientation of the edge.
The choices belonging to distinct \(t\) are disjoint since the pair then has just one available common step.
Consequently every row and every column contains at least \(\beta n\) pairs on isolated edges.

If \(g_x=g_{x'}\) for \(x'\ne x\), then \((x',y)\) has the same product as \((x,y)\) for every \(y\).
When \((x,y)\) belongs to an isolated edge, its only other component member has a different second coordinate since the second graph has no loops.
Thus \((x',y)\) belongs to another component, and \((x,y)\) is counted by \(J\).
Interchanging the coordinates gives the column assertion.
For arbitrary subsets of \(u\) repeated row vertices and \(v\) repeated column vertices, counting the two sets of certified pairs and subtracting at most \(uv\) for their intersection yields
\[
 J\ \ge\ \max\{\beta n r_A,\ \beta n r_B,\ \beta n(u+v)-uv\}.
\]
This test counts all occurrences in merged fibers and uses no probabilistic assumptions.

## Consequences for a sparse quotient

An erased color contributes every one of its vertices to \(r_A\) or \(r_B\).
If there are at least two distinct pairs of nonzero letter increments and only the four desired odd colors survive on each side, the [neighbor count](../claims/Yin_C_A0043_v1.md#passing-from-vertices-to-the-two-actual-supports) gives at least \(n/(3\cdot16513)\) such repeated vertices per side.
Already a single side forces \(J/n^2\ge\beta/(3\cdot16513)>0.000019\).
The row and column bounds can be checked separately when outside occurrence counts differ.

For a tuple with many outside occurrences there is a second estimate.
At least \(1-(1-r_A/n)(1-r_B/n)\) of the rectangle has a repeated coordinate.
The [global isolated-edge fraction](../claims/Yin_C_A0047_v1.md#the-fixed-graph-walk) shows that fewer than \(0.009 n^2\) pairs fail to be on isolated edges.
Therefore
\[
 \frac J{n^2}\ \ge\ 1-(1-r_A/n)(1-r_B/n)-0.009 .
\]
For example, erasure of three colors of size \(n/7-4\) per side forces more than \(66\%\) of the occurrence rectangle into merged product fibers for all sufficiently large \(n\).
This distinguishes a proposed construction with a macroscopic number of erased vertices from the [two-root estimate](../claims/Yin_C_A0049_v1.md#statement), which gives \(J/n^2\to0\) in probability in its two matching laws.
It does not exclude a particular exceptional matching with that many mergers.

## A fourth moment for repetitions on both sides

Fix any subsets of the two vertex lists, for instance just the occurrences in the colors proposed for erasure.
Attach independent complex random variables uniform on the unit circle to every vertex of both lists.
Keep the matching and all group labels fixed.
For a product \(w\) write \(Z_w\) for its random group-ring coefficient and \(M_w\) for its number of vertex-pair occurrences.
If \(r_g,s_h\) count the two lists' occurrences of actual factor labels \(g,h\), then
\[
 \sum_w\left(\mathbb E|Z_w|^4-2M_w^2+M_w\right)
   =8\left(\sum_g\binom{r_g}{2}\right)
       \left(\sum_h\binom{s_h}{2}\right).
\]
Indeed the occurrence fiber at \(w\) is a disjoint union of rectangles of sizes \(r_g\) by \(s_h\) over \(gh=w\).
Different rectangles in that fiber have disjoint rows and columns by group cancellation.
The contribution of one rectangle is the product of independent sums of \(r_g\) and \(s_h\) phases.
A sum of \(r\) independent phases has second moment \(r\) and fourth moment \(2r^2-r\), by matching indices in the two conjugate pairs.
Distinct rectangle contributions are independent and invariant under multiplication by any unit complex number.
Expanding the fourth moment of their sum gives \(2M_w^2\) plus the sum of their individual fourth moments minus twice the squares of their individual second moments.
Adding \(M_w\) now leaves \(2r_gs_h(r_g-1)(s_h-1)\) for each rectangle.
Summing over \(w\) proves the identity without any independence between coefficients at different products.

In particular if both selected lists disappear entirely after binary collection, each of their multiplicities is even.
For list sizes \(N_A,N_B\) the displayed excess is then at least \(2N_A N_B\), since \(\binom r2\ge r/2\) for positive even \(r\).
A smaller exact value certifies failure of simultaneous erasure.
The second moments \(\mathbb E|Z_w|^2=M_w\) can also supply the baseline: an independent repeat of the phase experiment gives \(M_w^2=\mathbb E(|Z_w|^2|\widetilde Z_w|^2)\).
Application requires access to coefficients in the original group, or in a verified quotient that still separates enough labels.
If the selected lists erase in the original group, all their multiplicities in any quotient are still even, so a smaller excess in that quotient also excludes erasure.
In \(C_7\) itself the bins are the prescribed colors and the test loses the distinctions within them.
A positive excess measures repeated pairs of labels and does not certify that every multiplicity is even.

---
author: Yin
---

# Alternating translations and the intersection of two graph planes

## Statement

Let \(s,t\) belong to a discrete group \(G\), let \(P\in{\rm GL}_{4}(\mathbb C)\), and let
\[
 L_s=\{(x,sx):x\in U(G)^2\},\qquad
 L_t=\{(y,ty):y\in U(G)^2\},\qquad d=\dim_G(L_s\cap P L_t).
\]
Here a translation acts diagonally on each two-coordinate block, \(U(G)\) is the regular affiliated algebra, and dimensions use the unnormalized matrix trace.
These are exactly the two full coefficient planes in the [four-column reduction](Yin_C_A0184_v1.md#statement), after a constant normalization of the first plane.
Their concatenated pencil has rank \(4-d\).

Write
\[
 A=\begin{pmatrix}0&s^{-1}I_2\\sI_2&0\end{pmatrix},\qquad
 B=P\begin{pmatrix}0&t^{-1}I_2\\tI_2&0\end{pmatrix}P^{-1}.
\]
Let \(\mathcal W_q\) consist of the empty word and the two alternating words of each length from \(1\) to \(q\) in the formal letters \(A,B\).
For the corresponding actual matrices write \(H_w=w(A,B)\).
For any complex numbers \(\lambda_w\) with \(\sum_w\lambda_w=1\),
\[
 d \ \le\ \sum_{v,w}\overline{\lambda_v}\lambda_w\,\operatorname{Tr}(H_v^*H_w).
 \tag{1}
\]
The coefficients of this positive form are finite sums computed using just the actual group endpoints of the words.

Suppose the endpoint sets for distinct words of \(\mathcal W_q\) are disjoint, where each occurrence of \(A\) contributes \(s^{\pm1}\) and each \(B\) contributes \(t^{\pm1}\).
For example this holds when no nonempty freely reduced word of length at most \(2q\) in the marked letters \(s,t\) represents the identity.
Writing \(b(w)\) for the number of occurrences of \(B\) and \(\kappa=\|P\|\|P^{-1}\|\) for its Euclidean condition number, one has
\[
 d\le\left(\sum_w \frac1{\operatorname{Tr}(H_w^*H_w)}\right)^{-1}
   \le \frac4{\sum_w\kappa^{-2b(w)}}.
 \tag{2}
\]
For a scalar multiple of a unitary \(P\), this gives \(d\le4/(2q+1)\).
In particular the marked ball test through length eight excludes \(d=1/2\) for \(q=4\).
The same conclusion holds for any \(P\) satisfying \(2+4\kappa^{-2}+3\kappa^{-4}>8\) under that ball test.
The hypotheses make no scalar injectivity or character assumption.

## Testing the common fixed vectors

The involutions \(A,B\) have fixed modules \(L_s,P L_t\).
If \(F\in M_4(\mathcal N(G))\) is the orthogonal projection onto the intersection, then \(H_w F=F\) for every \(w\).
For \(D=\sum_w\lambda_w H_w\) this gives \(DF=F\), and trace cyclicity gives
\[
 \operatorname{Tr}F=\operatorname{Tr}(D F D^*)
       \le\operatorname{Tr}(D D^*)=\operatorname{Tr}(D^*D).
\]
Expanding proves (1), including in the presence of collisions.
Writing \((H_v)_g\) for the complex matrix coefficient at \(g\), each Gram entry is
\(\sum_g\operatorname{tr}_4((H_v)_g^*(H_w)_g)\).
In particular cancellation at identical endpoints is included before taking the trace.

Under the stated disjointness assumption the Gram matrix is diagonal.
The diagonal entries are positive since each \(H_w\) is invertible.
Choosing weights proportional to their reciprocals proves the first bound in (2).
Since \(A\) is unitary and \(B\) is similar by \(P\) to a unitary, \(\|H_w\|\le\kappa^{b(w)}\).
Thus \(\operatorname{Tr}(H_w^*H_w)\le4\kappa^{2b(w)}\), proving the second bound.
For \(q=4\) the respective numbers of words with zero, one and two occurrences of \(B\) are \(2,4,3\).
If two different formal words have a common endpoint, a signed spelling of one followed by the inverse spelling of the other gives an identity of length at most \(2q\).
Its free reduction is nonempty because the original signed spellings are reduced and have different alternating generator patterns.
This proves the marked ball criterion.

## A calibration with both separating characters absent

Fix \(q\ge1\), let \(N>2q\) be an integer, and use the torsion-free group
\[
  G_N=\langle a,b\mid b a^N b^{-1}=a^{N+1}\rangle,\qquad s=b,\quad t=ab .
\]
The [cyclic HNN normal form and torsion argument](Yin_C_A0181_v1.md#finite-windows-and-characters) apply.
The marked elements generate \(G_N\) since \(a=t s^{-1}\).
In its abelianization \([a]=0\), so \([s]=[t]\).
Consequently every circle-valued character which is trivial on one marked label is trivial on both.

A nonempty freely reduced word of length at most \(2q\) on \(s,t\) becomes a nonempty freely reduced word in \(a,b\) after substitution and free reduction, since the inverse substitution is \(b=s,\ a=ts^{-1}\) in the free group.
There are at most \(2q\) occurrences of \(a^{\pm1}\) before reduction.
If the reduced word has stable letters \(b^{\pm1}\), neighboring stable letters of opposite signs have a nonzero intervening power of \(a\) of absolute exponent at most \(2q<N\).
Neither \(N\) nor \(N+1\) divides that exponent, so there is no HNN pinch.
The word is therefore nonidentity.
A reduced word with no stable letters is a nonzero power in the embedded base group.
This proves the required marked ball test for all the indicated \(N\), e.g. \(N=9,q=4\).
It gives a half-rank exclusion for every graph pair satisfying the displayed condition on \(P\) in this marking, independently of both character tests.
For arbitrary \(P\) or additional collisions, failure of the numerical bound to drop below one half leaves the intersection open.

## Assessment history

### Decision alternating-graph-equations

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:23 |
| status | proved |
| reason | The independent review verified the full argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite Gram bound, sufficient girth and condition number. |
| argument | [Testing the common fixed vectors](#testing-the-common-fixed-vectors) | Trace calculation and optimization of weights. |
| argument | [A calibration with both separating characters absent](#a-calibration-with-both-separating-characters-absent) | The changed HNN marking. |
| review | [Alternating graph equations](../audits/reviews/Yin_R_A0179_v1.md#alternating-graph-equations) | Independent review of the stated result and its argument. |

## Current assessment

[Selected decision](#decision-alternating-graph-equations)

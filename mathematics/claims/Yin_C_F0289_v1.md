---
author: Yin
---

# A single free projection detects original slice domains along its unitary orbit

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a finite bounded normal generating tuple in a tracial von Neumann algebra \(M\) with faithful normal probability trace and [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix an old coordinate with right slice \(E=(\mathrm{id}\otimes\tau)\delta\) on the represented starred polynomial algebra \(P\), and set \(a=\sup_{\|p\|\le1,p\in P}\|Ep\|_2\).
Adjoin one independently free Haar unitary \(Y\), denote the resulting actual tuple's old-coordinate right slice by \(\widehat E\), and put \(H=L^2(M)\).
Choose any projection \(f\in W^*(Y)\) of prescribed trace \(0<t<1\), set \(\sigma=\sqrt{t(1-t)}\), and write
\[
               q(u)=u f u^*,\qquad u\in\mathcal U(M).
\]
With \(J_u h=\sigma^{-1}u(f-t)h\), an isometry from \(H\) into the enlarged Hilbert space, one has the equivalences
\[
\begin{aligned}
 q(u)\in\operatorname{Dom}\overline{\widehat E}
 &\ \Longleftrightarrow\ u^*\in\operatorname{Dom}\bar E,
 &\quad \overline{\widehat E}q(u)&=\sigma J_u\bar E(u^*),\\
 q(u)\in\operatorname{Dom}\widehat E^*
 &\ \Longleftrightarrow\ u^*\in\operatorname{Dom}E^*,
 &\quad \widehat E^*q(u)&=t\xi+\sigma J_u E^*(u^*) ,
\end{aligned}                                                     \tag{1}
\]
where \(\xi=E^*1\), and the two terms in the second value are orthogonal.
The same identities apply to the opposite orientation.
For the original and augmented [normal cutoff maps](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) at every \(r>0\),
\[
               \widehat E_r q(u)=\sigma J_u E_r(u^*) .             \tag{2}
\]
No polynomial or graph-domain assumption is placed on the old unitary.

Let \(\mathcal O=\{q(u):u\in\mathcal U(M)\}\), with its trace Hilbert metric, and take any prescribed \(r_n>0\) tending to zero.
Counting the norm as infinite outside the forward domain, put
\[
 K=\sup_{q\in\mathcal O}\|\overline{\widehat E}q\|_2,\qquad
 B=\sup_{q\in\mathcal O,n}\|\widehat E_{r_n}q\|_2 .
\]
Then
\[
                  K=\sigma a,\qquad K\le B\le3K.                   \tag{3}
\]
If \(a=\infty\), a dense \(G_\delta\) in this orbit is outside the augmented forward domain and has unbounded cutoff outputs.
In particular bounded cutoff sequences on a nonmeagre subset *of the orbit* imply the entire original forward domain.
Testing both orientations at every original coordinate on the same orbit decides the full strong condition on the original tuple, by the [normal domain comparison](Yin_C_F0075_v1.md#statement).
The orbit tests the original single-input cost regardless of dimension.
In dimension at least three its supremum also detects the original finite column cost by the [single-input comparison](Yin_C_F0276_v1.md#statement).

## Argument

Use the [old-factor decomposition](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) with the other factor \(W^*(Y)\).
The [single free extension](Yin_C_F0278_v1.md#free-extension-of-a-slice) preserves the two actual vacua, in particular the old vacuum \(\xi\).
There is a Hilbert decomposition \(\widehat H=\mathcal K\otimes H\) with a basis of \(\mathcal K\) consisting of the empty word and centered alternating basis words ending in the new factor.
Choose the centered orthonormal bases by taking finite linear combinations of core polynomials, exhausting each polynomial space by their finite spans.
The enlarged polynomial algebra is exactly the algebraic sum of these basis copies of \(P\): each product \(w b\) with \(b\in P\) belongs to the core, and every enlarged polynomial has a finite expansion in such products.
On that algebra the right slice is the direct sum of copies of \(E\), by the cited reduction of the traced suffix of a differentiated word.
Consequently its closure is the Hilbert direct sum of the closed copies of \(\bar E\) and its adjoint the direct sum of copies of \(E^*\).
For the closure this follows by first truncating to finite sums and then approximating their individual coordinates in graph norm.
For the adjoint, testing finite vectors identifies each coordinate and the squared sum of their output norms is the required Hilbert boundedness condition.

The vacuum coordinate is \(1\otimes H\), with \(1\) denoting the empty word.
The vector \(u(f-t)/\sigma\) corresponds to a unit vector \(k_u\in\mathcal K\) perpendicular to that empty word, tensored with the old vacuum.
Indeed split \(u\) into its trace and old centered part and approximate the centered factors in their Hilbert spaces.
The resulting reduced words end with the centered new-factor letter and have norm \(\|u\|_2\|f-t\|_2/\sigma=1\).
Right multiplication by a bounded old \(h\) corresponds to the coefficient \(h\) on the last \(H\), so that \(J_u h=k_u\otimes h\), extending by density to every \(h\in H\).
Now \(q(u)=t1+\sigma J_u(u^*)\).
The two direct-sum graphs give (1) since \(E1=0\) and \(E^*1=\xi\).

For fixed \(r\) the old inner cutoff acts on the final differentiated coefficient in exactly the same way as on the old core.
Cuts before an intervening centered new-factor suffix still have zero right trace: insertion of bounded separated old marginal multipliers on the inner legs preserves that property, and bounded separated approximations to the continuous cutoff converge on each fixed coarse derivative tensor.
Thus on polynomials \(w b\) the augmented cutoff is \(w E_r b\), and the formula also holds when \(w\) is a finite combination of centered old/new prefixes ending in the new factor.
To pass to \(u(f-t)u^*\), approximate \(u,u^*\) and \(f-t\) in their factors strongly-star on bounded balls by polynomials, centering the new-factor letter exactly.
At each stage the norm of the output is determined by the Hilbert tensor of the prefix and the output on the old last coefficient.
The old cutoff is normal, hence maps the bounded approximating coefficients to a weakly convergent bounded net.
The coefficient vectors in \(\mathcal K\) converge in norm by the reduced tensor decomposition, so the tensor products converge weakly.
The augmented cutoff is normal as well and its value at the unit is zero, proving (2) by uniqueness of the weak limit.

For a bounded linear map \(L:M\to H\), the supremum of \(\|Lu\|\) over unitaries equals its norm.
Here is an elementary proof at the required scope.
For at least two coordinates the algebra is a factor by [two-coordinate rigidity](Yin_C_F0202_v1.md#statement).
The complementary initial and final projections of a partial isometry have equal scalar trace and hence are equivalent in the finite factor, so the polar factor of a contraction extends to a unitary. [Anantharaman and Popa, Corollary 2.4.11](../audits/literature/AP18/Yin_U004.md#ap18-u004)
For one coordinate the algebra is abelian and the extension takes the value one on the zero set.
For a contraction \(x=v|x|\) with unitary \(v\), \(x\) is the average of \(v(|x|\pm i\sqrt{1-|x|^2})\), both unitary.
The same argument holds for a linear subspace containing all unitaries and a linear map on it.
If \(a<\infty\), the [original bounded extension](Yin_C_F0276_v1.md#statement) agrees with the graph of \(\bar E\) on \(M\): bounded strong approximation from the core and weak graph closure give this identification.
Its norm is \(a\).
Conversely finite \(K\) puts all old unitaries in that graph and bounds their outputs by \(K/\sigma\), hence controls the entire core ball by the preceding average.
This proves \(K=\sigma a\) in the extended reals.
For the cutoffs the same average applies separately for each \(n\); their values on core vectors converge to \(E\), while their norms are at most \(3a\) if \(a<\infty\) by the [single-input cutoff comparison](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra).
This proves (3).

Finally freeness gives
\[
       \|q(u)-q(v)\|_2^2=2\sigma^2(1-|\tau(u^*v)|^2).
\]
Indeed for \(x=u^*v\) the trace of \((f-t)x(f-t)x^*\) is \(\sigma^2|\tau(x)|^2\) by centering and freeness.
The orbit is therefore a complete metric space: its metric is equivalent to the quotient metric \(\inf_{|\lambda|=1}\|u-\lambda v\|_2\), whose square is \(2(1-|\tau(u^*v)|)\).
In a quotient Cauchy sequence pass to a subsequence of summable successive distances, choose phases successively to get a Hilbert Cauchy sequence, and use completeness of the unitaries for the tracial Hilbert metric (bounded convergence of products and adjoints).
The original sequence then converges in the quotient.
Sublevels for the forward graph are closed by weak compactness and weak graph closure; simultaneous cutoff sublevels are closed by normality on bounded sets.
If either sublevel had interior, its preimage under \(u\mapsto q(u^*)\) would contain a neighborhood of some unitary \(v\).
By (1) or (2), respectively, all the old unitary values in that neighborhood would be bounded by a common constant.
For any selfadjoint contraction \(h\) and small fixed \(\epsilon>0\), the two unitaries \(v(\sqrt{1-\epsilon^2h^2}\pm i\epsilon h)\) belong to this neighborhood, uniformly over \(h\) by operator-norm proximity to \(v\).
Subtracting their values and dividing by \(2i\epsilon\) gives a common bound for \(v h\), with graph inclusion for the original forward operator.
Splitting \(v^*x\) into real and imaginary parts gives the bound on the entire unit ball for either the graph or every cutoff, contradicting \(a=\infty\) by the core limits.
The countable union of integer sublevels for each condition is consequently meagre if \(a=\infty\), and the Baire theorem proves the stated simultaneous assertion.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:58 |
| status | open |
| reason | Fix the exact free projection orbit test on original unitaries, including both unbounded graph equivalences and the quantitative category conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact domains and cutoff values at every orbit point, quantitative bounds and the intrinsic category alternative. |
| argument | [Argument](#argument) | Free right-module graph direct sums, a fixed-radius normal limit, unitary averages and complete orbit geometry. |
| dependency | [Free right module](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Algebraic reduced-word coefficient expansion, orthogonality and right-slice identity before closure. |
| dependency | [Single free extension](Yin_C_F0278_v1.md#free-extension-of-a-slice) | Actual distinguished vacua and corresponding decomposition with one freely adjoined scalar factor. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normality of the bounded fixed-radius maps, convergence on the core and the uniform bound in the bounded-slice case. |
| dependency | [Bounded original map](Yin_C_F0276_v1.md#statement) | The original normal bounded extension, its norm and the column comparison when the tuple has at least three coordinates. |
| dependency | [Factoriality](Yin_C_F0202_v1.md#statement) | The original normal algebra is a finite factor for at least two coordinates. |
| dependency | [Finite projection comparison](../audits/literature/AP18/Yin_U004.md#ap18-u004) | Corollary 2.4.11, printed page 39 of the retained Anantharaman and Popa notes, for equivalence of equal-trace projections in a finite factor. |
| dependency | [Both normal orientations](Yin_C_F0075_v1.md#statement) | Equivalence between the two original forward domains and the existential strong normal condition. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T16:06 |
| status | proved |
| reason | Independent review verified the two direct-sum domains, fixed-radius identities, orbit cost and category result, with both orientations tested at every old coordinate for the strong condition. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact domains and cutoff values at every orbit point, quantitative bounds and the intrinsic category alternative. |
| argument | [Argument](#argument) | Free right-module graph direct sums, a fixed-radius normal limit, unitary averages and complete orbit geometry. |
| dependency | [Free right module](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Algebraic reduced-word coefficient expansion, orthogonality and right-slice identity before closure. |
| dependency | [Single free extension](Yin_C_F0278_v1.md#free-extension-of-a-slice) | Actual distinguished vacua and corresponding decomposition with one freely adjoined scalar factor. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normality of the bounded fixed-radius maps, convergence on the core and the uniform bound in the bounded-slice case. |
| dependency | [Bounded original map](Yin_C_F0276_v1.md#statement) | The original normal bounded extension, its norm and the column comparison when the tuple has at least three coordinates. |
| dependency | [Factoriality](Yin_C_F0202_v1.md#statement) | The original normal algebra is a finite factor for at least two coordinates. |
| dependency | [Finite projection comparison](../audits/literature/AP18/Yin_U004.md#ap18-u004) | Corollary 2.4.11, printed page 39 of the retained Anantharaman and Popa notes, for equivalence of equal-trace projections in a finite factor. |
| dependency | [Both normal orientations](Yin_C_F0075_v1.md#statement) | Equivalence between the two original forward domains and the existential strong normal condition. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0298_v1.md#finding) | Complete fixed statement and argument, the seven declared dependencies, adjoint orthogonality, and the coordinate and orbit quantifiers. |

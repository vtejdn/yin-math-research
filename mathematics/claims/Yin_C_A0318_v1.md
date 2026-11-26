---
author: Yin
---

# Fourier coefficient level sets at a bounded four-position endpoint

## Statement

Let \(s,t\) belong to a discrete group, put \(t_j=s^jts^{-j}\) and write \(C_j=\langle t_j\rangle\).
Suppose \(t\) has infinite order, \(C_0\cap C_1=1\), and \(\langle t_1,t_2\rangle\) is nonamenable.
Let \(M(z)=P(z)Q(z)^{-1}\) for regular complex two-square pencils \(P=Az+B,\ Q=Cz+D\) with invertible assembly \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\).
Assume that both transfers are regular on the circle, that neither determinant is a Laurent monomial, and that \(M\) sends no constant input line to a constant output line over \(\mathbb C(z)\).
If \((s^{-1}M(t))^4=I\), the two determinants have precisely one common finite nonzero root, each with multiplicity one there and with no other nonzero finite roots.
The residues of the two transfers at this point are proportional nonzero square-zero matrices, and \(\det M=c z^k\) with \(c\ne0,\ k\in\{-1,0,1\}\).
The pole location is off the unit circle.
This argument treats the original group and imposes no assumption on its abelianization.

## Possible tails of the Laurent coefficients

Write \(M_i\) for the matrix Laurent coefficient at \(z^i\).
There can be no removable determinant zero at a finite point: the three coefficients of \(N=P\,{\rm adj}\,Q\) are independent, since an invertible rational matrix in a constant span of dimension at most two admits a constant point correspondence by normalizing at one invertible value and choosing an eigenline.
In particular \(N(z)\ne0\) for every finite \(z\), and the same holds for \({\rm adj}\,N(z)\).
The inverse transfer is \({\rm adj}\,N/\det P\).
Thus no root of either determinant lies on the unit circle.

For either transfer \(L\), with its own numerator and denominator, the following alternatives cover all possibilities.

* If the denominator has two nonzero finite roots counted with multiplicity on the same side of the unit circle, there is one sign \(\sigma\) for which all \(L_{\sigma n}\), \(n\ge1\), are invertible and
  \[
                   |\det L_{\sigma n}|=b r^n,\qquad b>0,\quad 0<r<1 .
  \]
  The coefficients on the other open half-line vanish.
* Otherwise, outside a finite set each open half-line is zero or has the form
  \[
                  L_{\sigma n}=d_\sigma r_\sigma^n R_\sigma ,
             \qquad 0<|r_\sigma|<1,\quad d_\sigma\ne0,\quad
                          {\rm rank}\,R_\sigma=1 .
  \]
  The nonzero tails correspond exactly to the simple nonzero finite denominator roots, with \(R_\sigma\) their residues up to nonzero scalar.

For the first alternative invert the parameter if necessary to put both roots outside the circle.
In the notation of \(M\), both \(C,D\) are invertible.
The cyclic expansion \(M(z)=BD^{-1}+Vz(I+zT)^{-1}D^{-1}\), with \(T=D^{-1}C,\ V=A-BT\), has \(V,T\) invertible by the assembly.
The coefficients at \(n\ge1\) are \(V(-T)^{n-1}D^{-1}\), and both eigenvalues of \(T\) have modulus less than one, including the repeated-root case.
The absolute determinants have the stated form with \(r=|\det T|\).
For the other alternative there is at least one nonzero finite root by nonmonomiality.
There is either one simple nonzero finite root or two distinct simple ones on opposite sides.
The constant, polynomial and zero-pole parts give only finitely many Fourier coefficients, and expansion of each nonzero simple fraction gives exactly one geometric half-line.
At a simple root the pencil kernel has dimension one and the numerator is injective there by assembly, so the residue has rank one.
These explanations also apply to \(M^{-1}\) with the pencils exchanged.

## Two independent translations of the same finite set

The [quartic product calculation](Yin_C_A0186_v1.md#cutting-the-ordered-product) gives
\[
       W=M(t_1)M(t_0)=M(t_2)^{-1}M(t_3)^{-1}s^4 .
\]
All Fourier comparisons below are in the group convolution algebra, since the matrix functions are rational without circle poles.
Write \(L_i=M_i,\ L'_i=(M^{-1})_i\).
The coefficient of \(W\) at \(t_1^i t_0^j\) is \(L_i L_j\), since these labels are distinct for all \((i,j)\).
Likewise in the right expression its coefficients are the individual \(L'_i L'_j\) at distinct \(t_2^i t_3^j s^4\).
Outside the respective product set all coefficients vanish.

If one transfer has an infinite tail of invertible blocks, the other does as well: infinitely many coefficients of \(W\) are invertible, and two invertible factors are necessary for each invertible product on either side.
Thus both transfers are of the first type.
For real \(R\) tending to infinity, form the finite set \(S_R\) of group labels where the absolute determinant of the coefficient of \(W\) is at least \(e^{-R}\).
There are at least a constant times \(R^2\) such labels for large \(R\), by all the pairs \((\sigma n,\sigma m)\) with \(n,m\ge1\) and \(n+m\) bounded by a sufficiently small positive multiple of \(R\).
For each fixed \(j\) the accepted \(i\)'s form an interval on the nonzero determinant tail, possibly with the exceptional index zero added.
Only \(O(R)\) indices \(j\) occur, by exponential decay and boundedness of all the coefficients.
Since left translation by \(t_1\) increments \(i\) by one, \(|t_1 S_R\triangle S_R|=O(R)\).
In the right-hand coordinates the identical interval argument gives \(|t_2 S_R\triangle S_R|=O(R)\).

Such sets imply amenability of \(\langle t_1,t_2\rangle\).
Indeed normalize their indicators to probability measures and, in each orbit of the subgroup's left action on the ambient group, identify that orbit equivariantly with the subgroup.
The sums of the transported measures have mass one and variation under each generator tending to zero.
A weak-star limit of the associated means gives an invariant mean on the subgroup.
This contradiction rules out the first type on either side.

For the remaining two transfers use the level set of the Hilbert-Schmidt norm of the actual coefficient of \(W\), again at threshold \(e^{-R}\).
If two nonzero tail matrices on one side satisfy \(R_\sigma R_\tau\ne0\), the products for large \(n,m\) have norm \(c|r_\sigma|^n |r_\tau|^m\) at their corresponding labels for some \(c>0\).
They give at least a constant times \(R^2\) accepted labels for large \(R\).
For fixed \(j\) on either side, as \(i\) runs over a nonzero half-line tail the norm of \(L_iL_j\), or of \(L'_iL'_j\), is zero or a positive constant depending on \(j\) times a decreasing geometric sequence.
The accepted \(i\)'s are therefore the union of a bounded number of intervals and singletons, with a bound independent of \(j,R\).
Again only \(O(R)\) different \(j\)'s occur in either coordinate system, by uniform exponential decay.
The very same two symmetric differences are \(O(R)\).
Nonamenability forces
\[
                  R_\sigma R_\tau=0
\]
for every ordered pair of nonzero tails, on either side separately.
This argument uses the scalar magnitude of the actual group coefficient as a common threshold even when the two presentations of its label have different exponents.

## A single finite pole for each side

For two nonzero finite roots on opposite sides, the rank-one residues have independent ranges.
Indeed the right kernels of \(Q\) at the two roots are independent, being distinct eigenspaces of \(D^{-1}C\) (both corners are invertible).
If \(P(\alpha)v_\alpha+P(\beta)v_\beta=0\) with \(v_i\) in those kernels, applying the assembly to \((\alpha v_\alpha+\beta v_\beta,v_\alpha+v_\beta)\) gives zero, whence \(v_\alpha=v_\beta=0\).
The residue image at each root is precisely that image of its kernel.
A nonzero residue cannot kill both ranges.
Consequently the second type must have exactly one simple nonzero finite denominator root on each side, and its residue squares to zero.

Let \(R,S\) be the residues of \(M,M^{-1}\) at these respective points \(\alpha,\beta\).
Choose a nonzero constant row \(\ell\) and column \(v\) with \(\ell R=0,\ Rv=0\).
Both \(\ell M(z)\) and \(M(z)v\) are Laurent polynomials, having removed their only possible finite nonzero pole.
Thus the group Fourier support of \(\ell Wv\) is finite.
Since \(W^{-1}=s^{-2}Ws^{-2}\), the same holds for \(\ell W^{-1}v=\ell M(t_0)^{-1}M(t_1)^{-1}v\).
If \(\ell S\ne0\), the vectors \(L'_jv\) span two dimensions, since otherwise \(M^{-1}(z)v\) would stay on a constant line and a constant point correspondence for the inverse reverses for \(M\).
Choose \(j\) with \(\ell S L'_jv\ne0\).
All sufficiently large indices along the unique inverse tail then produce distinct nonzero group coefficients of the compressed product, impossible.
The same argument on the other side gives \(Sv=0\), using that the rows \(\ell L'_j\) span the dual space; otherwise taking kernels would give a constant point correspondence for \(M^{-1}\).
Thus \(R,S\) have the same image and kernel and are proportional.

Finally \(N(\alpha)\) is proportional to \(R\) and \({\rm adj}\,N(\beta)\) is proportional to \(S\).
Square zero makes the adjugate of either residue its negative.
Hence \(N(\alpha)\) is proportional to \(N(\beta)\), which by independence of the three coefficients and comparison of \(1,z,z^2\) implies \(\alpha=\beta\).
Beyond this one simple root the determinants can only have a factor of \(z\), of multiplicity at most one, and a nonzero constant multiplier.
This proves the asserted monomial determinant ratio.

## Assessment history

### Decision level-sets-of-the-bounded-middle-product

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:50 |
| status | proved |
| reason | The common level sets force all tail residue products to vanish, leaving a single common pole and a monomial determinant. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The common level sets force all tail residue products to vanish, leaving a single common pole and a monomial determinant. |
| argument | [Possible tails of the Laurent coefficients](#possible-tails-of-the-laurent-coefficients) | Possible tails of the Laurent coefficients. |
| argument | [Two independent translations of the same finite set](#two-independent-translations-of-the-same-finite-set) | Two independent translations of the same finite set. |
| argument | [A single finite pole for each side](#a-single-finite-pole-for-each-side) | A single finite pole for each side. |
| review | [Level sets of the bounded middle product](../audits/reviews/Yin_R_A0223_v1.md#level-sets-of-the-bounded-middle-product) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-level-sets-of-the-bounded-middle-product)

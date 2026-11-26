---
author: Yin
---

# A nonsummable second pivot and a spectral test on every compressed block

## Statement

Assume a half kernel in the [noncyclic order-twenty marking](Yin_C_A0344_v2.md#statement).
Let \(N\) be the common sign subgroup, \(R\) its four-square commutator matrix, and call a marking character \(\psi\) visible if \(r_\psi=\operatorname{rank}\psi(R)\ge3\).
There are \(k\) visible characters, \(1\le k\le5\).
For every nonzero constant input and output fiber pair use the two-square compressed block \(D=U_w R V_v\) of the [two-plane construction](Yin_C_A0344_v2.md#two-dimensional-input-and-output-spaces).
Its actual affiliated inverse never belongs to \(M_2(\ell^1(N))\).
This holds even for pairs at which a visible numerical block is singular.

If \(D\) is selected to be numerically invertible at all visible characters, two further unimodular integer coordinate changes can put a nonsummable scalar at the exact position of the inverse of the second Schur pivot.
Both pivots still have nonzero formal values at all visible characters.
Among at most \(2(k+2)\) specified choices at least one has this property.
For its scalar inverse there is a sequence of explicit finite-support regularizations whose \(\ell^1\) norms tend to infinity.

For every block \(D\) above, also after arbitrary invertible constant changes of its two input and output coordinates, one has
\[
                \inf\sigma(|D|)\le(\sqrt3-1)\|D\|
\]
in the regular representation.
If \(D\) has a bounded regular inverse and detects all visible characters, it furnishes a concrete matrix in the kernel of the maximal-to-reduced group \(C^*\)-algebra map whose value at each \(\psi\) has rank \(r_\psi-2\).
These assertions only use the actual half-kernel construction, with no additional hypothesis on traces of \(\ell^1\) idempotents.

## An obstruction shared by the entire family of blocks

For pairs making every \(\psi(D)\) invertible, extend the coordinates of \(D\) to the full matrix \(\left(\begin{smallmatrix}D&E\\F&G\end{smallmatrix}\right)\).
The [actual Schur identity](Yin_C_A0344_v2.md#two-actual-inverses-and-the-formal-remainder) gives \(G=FD^{-1}E\) in the affiliated algebra, whereas \(G(\psi)-F(\psi)D(\psi)^{-1}E(\psi)\) has positive numerical rank \(r_\psi-2\).
If \(D^{-1}\) had absolutely summable entries, the identity and both inverse equations would hold in the faithful convolution algebra and could be evaluated at \(\psi\), a contradiction.
The same reasoning shows that neither \(D^{-1}E\) nor \(FD^{-1}\) has all entries absolutely summable.
For the former use the two actual equations \(D(D^{-1}E)=E,\ F(D^{-1}E)=G\); for the latter use \((FD^{-1})D=F,\ (FD^{-1})E=G\).

All compressed blocks are affiliated units.
The simultaneous numerical conditions on the two constant vectors form a dense open set: they require finitely many nonzero bilinear forms not to vanish, as in the [finite character selection](Yin_C_A0344_v2.md#simultaneous-numerical-rank-for-the-same-input-and-output-spaces).
The map from the pair to \(D\) is continuous in matrix convolution norm since its support is fixed and finite.
Invertibility is open in this Banach algebra.
Consequently no pair gives a convolution inverse, and constant invertible coordinate changes preserve this obstruction.

## Selecting and approximating one actual scalar inverse

Fix a block \(D\) invertible at every visible character and write \(Q=D^{-1}\) for its actual inverse.
In the complex vector space \(U(N)/\ell^1(N)\) at least one of the four entries of \(Q\) has nonzero class.
On the span of those four classes choose a linear functional nonzero on one, and apply it to the four entries to obtain a nonzero numerical matrix \(M\).
Choose \(\nu=(1,j)^{\mathsf T}\), \(j=0\) or \(1\), with \(M\nu\ne0\).
The vectors \(M\nu,\psi(D)^{-1}\nu\) for the visible characters are all nonzero.
For at least one \(i\in\{0,\ldots,k+1\}\), the row \(\omega=(1,i)\) annihilates none of them, since each excludes at most one value.
It follows that \(\omega Q\nu\notin\ell^1(N)\) and every ordinary \(\omega\psi(D)^{-1}\nu\ne0\).

Set \(S_j=\left(\begin{smallmatrix}0&1\\1&j\end{smallmatrix}\right)\) and \(D'=S_j^{-1}D S_i^{-1}\).
The bottom-right entry of its actual inverse is \(\omega Q\nu\).
Its formal numerical value computed by inverting the numerical block is nonzero at every visible character.
The numerical two-square cofactor formula therefore gives \(\psi(a)\ne0\) for \(a=D'_{11}\).
The first pivot is an affiliated unit by scalar injectivity.
The next Schur pivot \(b=D'_{22}-D'_{21}a^{-1}D'_{12}\) is an affiliated unit by invertibility of \(D'\).
Its inverse equals \(\omega Q\nu\) by block inversion.
The numerical value of the displayed expression for \(b\) is \(\det\psi(D')/\psi(a)\ne0\).
The two extra coordinate changes preserve the total eight-label support.

Choose \(L\) larger than both the regular norm of \(D\) and its norms at all the selected characters.
For every \(n\ge1\) form the finite-support scalar
\[
 Z_n=\omega\left(\frac1{L^2}\sum_{j'=0}^{n-1}(I-D^*D/L^2)^{j'}D^*\right)\nu .
\]
Its character values converge to the nonzero values \(\omega\psi(D)^{-1}\nu\).
In the finite-trace measure topology the matrix between the outside constants converges to \(Q\): in the polar decomposition it is the inverse multiplied on the output side by \(I-(I-|D|^2/L^2)^n\).
Equivalently, on the input spectral space \(\mathbf 1_{[a,L]}(|D^*|)\) the inverse error is bounded by \(a^{-1}(1-a^2/L^2)^n\), and the complementary trace tends to zero as \(a\downarrow0\) because \(D^*\) is injective.
Compression by the fixed constants preserves convergence in measure.
If a subsequence of \(Z_n\) had bounded \(\ell^1\) norm, it would have uniformly bounded regular operator norm.
Its limit in measure would be bounded by that same constant, and convergence of this subsequence would hold in regular \(L^2\): split its difference from the limit at any positive singular cutoff and use the uniform bound above that cutoff.
Termwise convergence of group coefficients and Fatou's lemma would now give \(\omega Q\nu\in\ell^1(N)\).
Thus \(\|Z_n\|_1\to\infty\), with no boundedness assumption on \(Q\).

## The growth of the eight group labels

Up to the common left translation \(m=(st)^{-1}\), the entries of \(D\) are supported on the symmetric set \(V\) of the eight words \(s^{\pm1}t^{\pm1},t^{\pm1}s^{\pm1}\).
Write
\[
        a=st,\qquad b=st^{-1},\qquad c=s^{-1}t,\qquad e=s^{-1}t^{-1}.
\]
Then \(V\) consists of these four elements and their inverses, and \(ac^{-1}eb^{-1}=1\).
The number of elements of word length at most \(n\) in these four generators has exponential growth rate at most \(\rho=3+2\sqrt3\).
It suffices to prove the upper bound in the group presented by the four symbols and this single relation, since its map to the subgroup generated by \(V\) is onto.

In the Cayley two-complex of this presentation each unoriented edge is in one lifted square: its label appears once in the attaching word and the lift at that occurrence is fixed by the edge.
Each vertex is in at most four squares, one for each position along the relation.
The lifted squares have four distinct vertices and sides, as is also seen by mapping the symbols to the indicated words in the free group on \(s,t\).
A shortest path takes at most two consecutive edges within one square.
A nonempty segment there has two possible adjacent endpoints at distance one, and one opposite endpoint at distance two.
On leaving a square there are at most three new choices of square.
Thus an upper counting series for endpoints by the length of such paths, with each two-step segment counted by its endpoint, is
\[
              1+4(2z+z^2)\sum_{\ell\ge0}\big(3(2z+z^2)\big)^\ell .
\]
Overcounting between different segment lists can only increase the upper bound.
The positive radius of this series is \(1/(3+2\sqrt3)\), which gives the asserted bound also for the balls.

If the regular singular spectrum of \(D\) is in \([\alpha,\beta]\) with \(0<\alpha<\beta=\|D\|\), let \(f_n\) be the [Chebyshev residual](Yin_C_A0349_v1.md#the-size-of-a-positive-regular-gap) equal to one at zero and of modulus at most \(2\theta^n\) on \([\alpha^2,\beta^2]\), where \(\theta=(\beta-\alpha)/(\beta+\alpha)\).
Then \(p_{n-1}(z)=(1-f_n(z))/z\) is a polynomial.
The matrices \(p_{n-1}(D^*D)D^*\) approximate \(Q\) in regular operator norm with error at most \(2\theta^n/\alpha\).
Their supports lie in the ball of radius \(2n-1\) in \(V\), followed by \(m^{-1}\), because \(D\) has support in \(mV\).
The difference of successive approximants has regular \(L^2\) norm \(O(\theta^n)\).
Cauchy--Schwarz over all supported matrix entries bounds its total convolution norm by a constant times this \(L^2\) norm times the square root of the ball size at \(2n+1\).
If \(\theta\rho<1\), these differences are summable, giving an \(\ell^1\) inverse, already excluded.
Therefore \(\alpha/\beta\le(\rho-1)/(\rho+1)=\sqrt3-1\).
The case \(\alpha=\beta>0\) would give the finite-support inverse \(D^*/\beta^2\); a zero spectral infimum already satisfies the bound.
The same argument uses unchanged supports after invertible numerical coordinate changes.

## A maximal group-algebra witness when the block is bounded below

If \(D\) has a bounded regular inverse and \(\psi(D)\) is invertible at each visible character, choose a positive number \(\lambda\) below the minimum of the regular and these finite lower singular bounds squared.
Take a continuous real function \(f\) on \([0,\|D\|_{\max}^2]\) equal to \(1/t\) for \(t\ge\lambda\), with a finite value at zero.
The positive operator \(D^*D\) admits this continuous functional calculus in \(M_2(C^*_{\max}(N))\).
In that algebra put
\[
                            W=G-F f(D^*D)D^* E .
\]
Its image in the reduced algebra is zero by the actual Schur identity.
Every visible character sends it to the numerical Schur remainder, of rank \(r_\psi-2\).
In particular at least one matrix entry is a nonzero element of the kernel of the maximal-to-reduced map.

## Assessment history

### Decision selecting-a-scalar-inverse-outside-absolutely-summable-convolution

| Field | Value |
| --- | --- |
| date | 2026-11-26T19:16 |
| status | proved |
| reason | A common visible block and finitely many integer coordinate choices locate a nonsummable second inverse and a quantitative singular-spectrum obstruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A common visible block and finitely many integer coordinate choices locate a nonsummable second inverse and a quantitative singular-spectrum obstruction. |
| argument | [An obstruction shared by the entire family of blocks](#an-obstruction-shared-by-the-entire-family-of-blocks) | An obstruction shared by the entire family of blocks. |
| argument | [Selecting and approximating one actual scalar inverse](#selecting-and-approximating-one-actual-scalar-inverse) | Selecting and approximating one actual scalar inverse. |
| argument | [The growth of the eight group labels](#the-growth-of-the-eight-group-labels) | The growth of the eight group labels. |
| argument | [A maximal group-algebra witness when the block is bounded below](#a-maximal-group-algebra-witness-when-the-block-is-bounded-below) | A maximal group-algebra witness when the block is bounded below. |
| review | [Selecting a scalar inverse outside absolutely summable convolution](../audits/reviews/Yin_R_A0240_v1.md#selecting-a-scalar-inverse-outside-absolutely-summable-convolution) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-selecting-a-scalar-inverse-outside-absolutely-summable-convolution)

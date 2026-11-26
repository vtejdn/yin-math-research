---
author: Yin
---

# Annular moment bounds force a bounded-length positive return without a unitary similarity

## Statement

Consider a torsion-free group \(H=\langle g,h\rangle\) with \(h\) of infinite order and a sign character negating \(g\) and fixing \(h\).
Let \(M(y)\) be a two-square rational matrix such that \(M(y)\) and \(L(y)=M(y^{-1})^{-1}\) are holomorphic on a neighborhood of the closed unit disk.
Write \(U=g^{-1}M(h)\), and let \(\delta\) be the dimension of its \(+1\) eigenspace with unnormalized matrix trace.
For \(R>1\) assume the spectrum of \(U^2\) in the bounded regular algebra is contained in \(R^{-1}\le |z|\le R\).
It suffices that both spectral radii of \(U\) and \(U^{-1}\) be at most \(\sqrt R\).

If \(R=4\) and no word
\[
                  g^{-1}h^{i_1}\cdots g^{-1}h^{i_{2j}}=1,
                  \qquad i_\ell\ge0,\quad 1\le j\le5
\]
occurs in the group, then \(\delta<49/100\).
For \(\delta=1/2\) at least one such word occurs with every exponent bounded by a finite number computable from the coefficients.
This applies to the [two exceptional order-twenty prototypes](Yin_C_A0336_v1.md#a-circle-valued-scalar-square-of-the-transfer), for example whenever a constant change of basis gives \(\max_{|y|=1}\|M(y)\|\le2\).
Their boundary determinants have modulus one, so the same norm bound holds for their inverses by the two singular values.
The annular condition concerns spectral radii only and allows nonnormal operators.

More generally, if there is no such word for any \(j\), then
\[
           \delta\le\left(1+4\sum_{j=1}^{\infty}
                                      \frac{1}{R^j+R^{-j}}\right)^{-1}.
\]
The estimates also apply to the nullity of \(P(h)-gQ(h)\) when \(M=PQ^{-1}\) and \(Q(h)\) is an affiliated unit, by the transfer coordinate change.
The general result needs neither a prior half kernel nor regular scalar group-ring injectivity.

## Positive real parts tested by a finite trace

For a normalized finite von Neumann algebra trace \(t\), one has \(|t(X)|\le r(X)\) for every bounded \(X\), where \(r\) is the spectral radius.
Indeed for \(a>r(X)\) the norm-convergent series \(D=\sum_{k\ge0}(X^*)^kX^k/a^{2k}\) satisfies \(D\ge I\) and \(X^*DX=a^2(D-I)\).
Consequently \(\|D^{1/2}XD^{-1/2}\|\le a\), and the trace is invariant under this similarity.
Let \(a\) decrease to \(r(X)\).
If the spectrum of \(X\) has nonnegative real parts, apply the inequality to \(cI-X\) for positive real \(c\).
The squared spectral radius there is at most \(c^2+\|X\|^2\), giving \({\rm Re}\,t(X)\ge0\) on letting \(c\) tend to infinity.
This reasoning also applies to each normalized nonzero corner.

Use normalized two-coordinate trace \(t=(\operatorname{Tr}_2\otimes\tau_H)/2\) and put \(T=U^2\).
The range of \(p=\operatorname{proj}\ker(T-I)\) is the direct sum of the eigenspaces of \(U\) at \(1,-1\) by polynomial interpolation on that range.
The sign character interchanges the eigenspaces, so \(t(p)=\delta\).
In the orthogonal splitting by \(p\), \(T\) is upper triangular with identity in the first diagonal block and an operator \(T_0\) in the other.
For \(\lambda\ne1\) the first block of \(T-\lambda I\) is invertible, so invertibility reduces to that of \(T_0-\lambda I\).
It follows that \(T_0\) has spectrum in the same annulus.
For any Laurent polynomial \(F\) with real \(F(1)\) and nonnegative real part on that annulus, the corner trace bound, spectral mapping and the triangular form give
\[
                        {\rm Re}\,t(F(T))\ \ge\ \delta F(1).
\]
This includes a zero complement directly.

## Positive Laurent tests on the two boundary circles

For a real nonzero list \(v_0,\ldots,v_N\) let \(c_j=\sum_{k=0}^{N-j}v_kv_{k+j}/\sum_{k=0}^N v_k^2\) and set
\[
              F(z)=1+2\sum_{j=1}^N \frac{c_j(z^j+z^{-j})}{R^j+R^{-j}} .
\]
On either boundary circle its real part is \(\big|\sum_{k=0}^N v_ke^{ik\theta}\big|^2/\sum_k v_k^2\).
The harmonic minimum principle gives nonnegative real part on the entire annulus.
Thus the exact traces satisfy
\[
  \delta\left(1+4\sum_{j=1}^N\frac{c_j}{R^j+R^{-j}}\right)
       \le 1+2\sum_{j=1}^N\frac{c_j\,{\rm Re}\,t(U^{2j}+U^{-2j})}{R^j+R^{-j}} .
\]

The coefficients of \(M\) are absolutely summable in nonnegative powers of \(h\).
For \(U^{-1}\) expand \(M(h)^{-1}=L(h^{-1})\) in nonpositive powers.
Only words equal to the identity contribute to either trace, and the contributing coefficients can have either sign or be complex.
The inverse of each word for \(U^{-2j}\) has the positive-return form in the statement with the indices reversed.
Hence absence of all returns through \(2N\) factors gives zero moments on the right.
Taking \(v_k=1\) gives \(c_j=1-j/(N+1)\); passage to the limit yields the infinite bound.
For \(R=4\) use the six entries \((2,3,4,4,3,2)\), giving \(58(c_0,\ldots,c_5)=(58,52,40,25,12,4)\).
Direct rational addition yields \(F(1)>100/49\), proving the ten-factor bound.

## A finite search in the original word ball

Write \(M(y)=\sum A_i y^i,\ L(y)=\sum B_i y^i\).
Use \(S_+=\sum\|A_i\|,\ S_-=\sum\|B_i\|\) and \(T_\pm(l)\) for their tails at indices greater than \(l\).
If none of the words in the stated finite list with exponents between zero and \(l\) returns to the identity, absolute convergence gives
\[
                |t(U^{\pm 2j})|\le 2j S_\pm^{2j-1} T_\pm(l).
\]
Indeed every surviving product must contain at least one coefficient from the tail, and the normalized numerical trace is bounded by the product of the coefficient norms.
With the preceding positive coefficients choose \(l\) so that
\[
  2\sum_{j=1}^5\frac{2j\,c_j}{4^j+4^{-j}}
      \left(S_+^{2j-1}T_+(l)+S_-^{2j-1}T_-(l)\right)
               <F(1)/2-1 .
\]
A half kernel then forces a returning word of length at most \(10(l+1)\) in the original marks.
For effective bounds choose any rational \(r>1\) within both disks of analyticity and explicit upper bounds \(K_\pm\) for the matrix norms on \(|y|=r\).
Cauchy's estimate allows \(S_\pm\le K_\pm/(1-r^{-1})\) and \(T_\pm(l)\le K_\pm r^{-l-1}/(1-r^{-1})\).
For the normalized order-twenty prototypes both denominators can be taken as \(2-\sigma\sqrt5\,y+y^2\), including after reversal for \(L\).
Use \(r=5/4\) and the denominator modulus bound \((\sqrt2-r)^2\) to compute each \(K_\pm\) directly from the numerator coefficient norms.

## Assessment history

### Decision annular-trace-inequalities-and-finite-group-returns

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:25 |
| status | proved |
| reason | A positive Laurent test on the annulus and both Taylor expansions give a uniform bound below forty-nine hundredths when there is no short return. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A positive Laurent test on the annulus and both Taylor expansions give a uniform bound below forty-nine hundredths when there is no short return. |
| argument | [Positive real parts tested by a finite trace](#positive-real-parts-tested-by-a-finite-trace) | Positive real parts tested by a finite trace. |
| argument | [Positive Laurent tests on the two boundary circles](#positive-laurent-tests-on-the-two-boundary-circles) | Positive Laurent tests on the two boundary circles. |
| argument | [A finite search in the original word ball](#a-finite-search-in-the-original-word-ball) | A finite search in the original word ball. |
| review | [Annular trace inequalities and finite group returns](../audits/reviews/Yin_R_A0233_v1.md#annular-trace-inequalities-and-finite-group-returns) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-annular-trace-inequalities-and-finite-group-returns)

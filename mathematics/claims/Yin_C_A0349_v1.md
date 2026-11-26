---
author: Yin
---

# A character rank excess forces connected Banach spectrum and bounds the regular spectral gap

## Statement

Let \(G\) be a torsion-free discrete group and \(\pi:G\to U(t)\) a finite-dimensional unitary representation.
Assume that every idempotent matrix over \(\ell^1(G)\) has the same unnormalized regular trace as the numerical rank of its image under \(\pi\) divided by \(t\).
Let \(R\) be a finite group-ring matrix with \(k\) columns, and suppose
\[
               r=\operatorname{rk}_G R < t^{-1}\operatorname{rank}\pi(R).
\]
Put \(A=R^*R\).
The connected component of zero in \(\sigma_{M_k(\ell^1(G))}(A)\) contains at least \(t(k-r)\) eigenvalues of \(\pi(A)\), counted with multiplicity.
At least one of them is strictly positive.
The orthogonal regular kernel projection of \(R\) has a matrix entry outside \(\ell^1(G)\).

If all entries of \(R\) together have group support of size \(m\ge2\) and \(R\) has nonzero regular spectrum, then
\[
              \frac{\inf(\sigma(|R|)\setminus\{0\})}{\|R\|}
                        \le \frac{m-2}{m}
\]
in the regular representation, with the infimum zero when the positive spectrum accumulates at zero.
The bound applies after any invertible constant changes of input and output coordinates.

For the [four-square matrix on the common sign subgroup](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator), a hypothetical half kernel at the noncyclic order-twenty marking gives \(r=2\) and a scalar character \(\psi\) of rank three or four by [the character theorem](Yin_C_A0343_v1.md#statement).
Under the trace hypothesis for that subgroup and \(\psi\), each such matrix with its at most eight labels therefore has regular positive singular infimum at most \(3\|R\|/4\).
Constant coordinate changes can arrange \(\psi(A)\) to be a projection.
The Banach spectrum then has zero and one in the same component.
Every circle \(|z|=a\), \(0<a<1\), meets this spectrum, including inside any open gap of the regular spectrum.

## Exact trace assumptions

For torsion-free \(G\), support of the \(\ell^1\) Hattori--Stallings trace on finite-order conjugacy classes implies the stated trace equality for every finite-dimensional unitary \(\pi\).
Indeed the normalized numerical trace is obtained by summing the conjugacy-class coefficients of the diagonal trace, weighted by the normalized character of \(\pi\).
Absolute convergence justifies grouping by conjugacy classes.
Only the identity class contributes under the support condition, and its coefficient is the regular trace.
The numerical matrix is idempotent, so its ordinary trace equals its rank.

The published Theorems 1.3 and 1.4 of Berrick, Chatterji and Mislin give this condition for countable groups with rationally surjective degree-zero Bost assembly, including countable groups with the Haagerup property. [BCM04, source statement and applicability](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace).
Theorem 1.1 of the OpenAI preprint of 5 October 2026 states the trace-support theorem for every discrete group. [Ope26h, inspected statement](../audits/literature/Ope26h/Yin_U001.md#trace-support).
The extension of the present conclusions to all torsion-free groups using that preprint is conditional on its theorem; its general proof has not been independently checked here.
The published range and the arguments below do not depend on that extension.

## Spectral components and finite-support tests

If the regular kernel projection \(P\) belongs to \(M_k(\ell^1(G))\), the equalities \(P^2=P\) and \(RP=0\) hold in the convolution algebra by faithfulness of the regular representation.
The trace hypothesis gives \(\operatorname{rank}\pi(P)=t(k-r)\).
Its range lies in \(\ker\pi(R)\), whose dimension is strictly smaller, a contradiction.
In particular, for any \(L>\|A\|\) the finite-support matrices \((I-A/L)^n\) have entrywise total \(\ell^1\) norm tending to infinity.
They converge strongly to \(P\) by the positive regular spectral calculus and their coefficients converge pointwise.
A bounded subsequence in the entrywise total norm would put \(P\) in the convolution algebra by Fatou's lemma.

Write \(X=\sigma_{M_k(\ell^1(G))}(A)\).
Both the regular spectrum and the finite representation spectrum lie in this compact set by the corresponding unital algebra maps.
The regular kernel has positive dimension, so \(0\in X\).
If \(C_0\) is the connected component of zero, take a relatively open and closed subset \(B\) of \(X\) containing \(C_0\) and omitting all eigenvalues of \(\pi(A)\) outside it.
Such a subset exists since a component of a compact Hausdorff space is the intersection of its clopen neighborhoods, and only finitely many eigenvalues need to be omitted.
Apply holomorphic functional calculus to the function identically one on a neighborhood of \(B\) and zero on a disjoint neighborhood of \(X\setminus B\).
Its value is an idempotent in \(M_k(\ell^1(G))\).
In the regular algebra its image is the orthogonal spectral projection of the positive operator \(A\) onto its spectrum in \(B\); its trace is at least \(k-r\).
In the finite representation it is the ordinary projection onto exactly the eigenvalues in \(C_0\).
Trace equality gives the asserted count.
The eigenvalue zero alone has multiplicity \(tk-\operatorname{rank}\pi(R)<t(k-r)\).

For a detecting scalar character, constant invertible row and column changes take its numerical matrix to rectangular diagonal form with a rank-size identity block.
After these changes \(\pi(A)\) is a projection and \(1\in C_0\).
The modulus function takes every value between zero and one on the component.
For an explicit finite-support consequence choose \(L>\max(1,\|A\|)\), \(E_n=(I-A/L)^n\).
Whenever \((1-1/L)^n\le1/2\), polynomial spectral mapping gives
\[
                       r_{M_k(\ell^1(G))}(E_n-E_n^2)\ \ge\ 1/4 .
\]
Indeed \((1-z/L)^n\) maps the component to a connected set containing one and a real number at most \(1/2\).
It takes a value \(v\) of real part \(1/2\) there, with \(|v(1-v)|\ge1/4\).
In the regular algebra \(E_n-E_n^2\) instead converges strongly to zero.

## The size of a positive regular gap

Put \(b=\|R\|>0\), and suppose the regular positive singular spectrum lies in \([a,b]\), where \(a>0\).
For \(0<a<b\) use the ordinary Chebyshev polynomial \(T_n\) to set
\[
       f_n(z)=\frac{T_n((b^2+a^2-2z)/(b^2-a^2))}
                         {T_n((b^2+a^2)/(b^2-a^2))},\qquad
            \theta=\frac{b-a}{b+a}.
\]
It has \(f_n(0)=1\) and supremum at most \(2\theta^n\) on \([a^2,b^2]\), by the cosine formula on \([-1,1]\) and \(2T_n((u+u^{-1})/2)=u^n+u^{-n}\) at \(u=\theta^{-1}\).
Consequently \(f_n(A)\) converges to \(P\) in regular operator norm at this rate.

Let \(D\) be the support of \(R\), and let \(B_n=(D^{-1}D)^n\).
The identity belongs to \(D^{-1}D\) and \(f_{n+1}(A)-f_n(A)\) has support in \(B_{n+1}\).
Products for \(B_n\) are alternating inverse and direct letters from \(D\).
Delete adjacent equal labels with opposite signs until none remains.
Any nonempty remaining string has even length \(2j\le2n\), starts with an inverse, and has at most \(m(m-1)^{2j-1}\) choices.
It follows that \(\limsup |B_n|^{1/(2n)}\le m-1\), including \(m=2\).
For a \(k\)-square matrix \(F\) supported in \(B_n\), Cauchy--Schwarz on all its coefficients gives
\[
           \sum_{i,j}\|F_{ij}\|_1
                  \le k\sqrt{|B_n|}\,\|F\|_{2,\operatorname{Tr}}
                  \le k^{3/2}\sqrt{|B_n|}\,\|F\| .
\]
If \((m-1)\theta<1\), the successive polynomial differences are absolutely summable in this matrix convolution norm.
Their sum gives \(P\) in \(M_k(\ell^1(G))\), already excluded.
Thus \(\theta\ge1/(m-1)\), equivalent to \(a/b\le(m-2)/m\).
If \(a=b>0\), the projection \(I-A/b^2\) itself has finite support, giving the same contradiction.
When \(m=1\) each matrix entry is a constant times one common group translation and a character excess is already impossible.
Invertible numerical coordinate changes preserve both ranks and do not enlarge the support.

## Assessment history

### Decision character-excess-in-the-banach-spectrum

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:53 |
| status | proved |
| reason | The trace comparison forces a spectral component containing a positive character value and bounds the relative regular singular gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The trace comparison forces a spectral component containing a positive character value and bounds the relative regular singular gap. |
| argument | [Exact trace assumptions](#exact-trace-assumptions) | Exact trace assumptions. |
| argument | [Spectral components and finite-support tests](#spectral-components-and-finite-support-tests) | Spectral components and finite-support tests. |
| argument | [The size of a positive regular gap](#the-size-of-a-positive-regular-gap) | The size of a positive regular gap. |
| review | [Character excess in the Banach spectrum](../audits/reviews/Yin_R_A0237_v1.md#character-excess-in-the-banach-spectrum) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-character-excess-in-the-banach-spectrum)

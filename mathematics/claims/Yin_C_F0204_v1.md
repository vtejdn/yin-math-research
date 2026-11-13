---
author: Yin
---
# A central holomorphic polynomial forces an ACSY generator to be normal

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a bounded generator of a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\), and write \(H=L^2(M,\tau)\).
Assume the [actual one-coordinate ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Thus the represented unital star algebra \(\mathcal A=\mathbb C\langle X,X^*\rangle\) has an outer-bimodule derivation \(\delta:\mathcal A\to H\otimes_2 H\) with \(\delta X=1\otimes1\) and \(1\otimes1\in\operatorname{Dom}\delta^*\).
If \(Y=p(X)\) lies in \(Z(M)\) for a nonconstant complex polynomial \(p\), then \(X\) is normal and \(M\) is abelian.
In particular \(X\) admits a complex-linear map \(D:M\to H\) with \(XD(a)-D(Xa)=\tau(a)1\) for all \(a\in M\).

The normality assertion also holds if the actual ACSY condition is replaced by the existence of the displayed Hilbert-valued derivation with \(\delta X=1\otimes1\) and the explicit assumption that the spectral law of the central \(Y\) charges no critical value of \(p\).

## Argument

### Central spectral law and fiber Hilbert spaces

Under actual ACSY, [ACSY24 Proposition 3.5](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) gives \(\Delta(X)=1\).
The [MSY23 free-field equivalence](../audits/literature/MSY23/Yin_U001.md#exact-introductory-interfaces) then makes every nonzero holomorphic polynomial in \(X\) invertible in the algebra of affiliated operators.
In particular \(Y-s\) has zero kernel for every \(s\in\mathbb C\), since \(p-s\) is a nonzero polynomial.
Thus the spectral law \(\mu\) of the central normal \(Y\) is diffuse.
In the weaker assertion we only need \(\mu\) to vanish on the finite set \(\{p(\lambda):p'(\lambda)=0\}\).

Here are the precise fibers used below.
Identify \(N=W^*(Y)\) with \(L^\infty(\mu)\) by spectral calculus and write \(E_N\) for the trace-preserving conditional expectation.
For a formal star polynomial \(v\), write \(v(X)\) for its evaluation at \(X,X^*\).
Choose simultaneous measurable representatives of \(E_N(w(X))\) for the countably many star words \(w\).
Outside a single null set, the assignment \(w\mapsto E_N(w(X))(s)\) extends to a positive tracial state \(\tau_s\) on the formal polynomial algebra, with bounded GNS generator \(X_s\) of norm at most \(\|X\|\).
Indeed normalization and traciality are countably many word identities.
For every polynomial \(v\) with rational complex coefficients apply positivity of \(E_N\) to \(v^*v\), \(v^*(\|X\|^2-X^*X)v\), and \(v^*(\|X\|^2-XX^*)v\), using represented values in \(M\).
These countably many inequalities extend coefficientwise to complex polynomials and give the two multiplication bounds in GNS.
Centrality of \(Y\) and the \(N\)-module property give
\(\tau_s(v^*(p(X_s)-s)^*(p(X_s)-s)v)=0\) for every word \(v\), by expanding the product and evaluating the central factors.
Consequently \(p(X_s)=s1\) on the fiber Hilbert space \(H_s\).
The trace vector in \(H_s\) separates the represented fiber algebra, since right multiplication by words is bounded by traciality and has cyclic orbit.

The sections \(w(X_s)1\) form a countable total family on each fiber.
For finite sums of sections \(f(s)w(X_s)1\), with \(f\) bounded measurable, integration of the fiber inner products gives exactly the Hilbert inner product of the corresponding vectors \(f(Y)w(X)1\) in \(H\).
Their span is dense in \(H\) by the generating hypothesis and dense in the measurable direct integral by the total family construction.
This identifies \(H\) with \(\int^\oplus H_s\,d\mu(s)\).
Scalar multiplication on the fibers represents \(Y\) on the left and on the right.
The Hilbert tensor product similarly identifies with the direct integral of \(H_s\otimes_2 H_t\) over \(\mu\times\mu\), as follows first on tensors of the total sections and measurable rectangles and then by density.

### The diagonal value of the differentiated central relation

Write \(p(u)=\sum_{k=0}^m c_k u^k\) and set
\[
 B_{s,t}=\sum_{k=1}^m c_k\sum_{a=0}^{k-1}X_s^a\otimes X_t^{k-1-a}.
\]
Bounded fiber operators occurring as Hilbert vectors in these tensors are applied to their trace vectors.
The word rule identifies \(B_{s,t}\) with the section of \(\delta Y\).
For a star word \(w\), put \(w_s=w(X_s)\).
Differentiating the represented relation \(Yw=wY\) gives, for product-almost every \((s,t)\),
\[
 (s-t)(\delta w)_{s,t}=G_w(s,t),\qquad
 G_w(s,t)=(w_s\otimes1)B_{s,t}-B_{s,t}(1\otimes w_t).
\]
The displayed multiplication on the second leg is on the right.
The explicit polynomial tensor \(G_w(s,t)\) also specifies a diagonal value \(G_w(s,s)\) from the fiber moments, even for a diffuse \(\mu\).
We prove \(G_w(s,s)=0\) for \(\mu\)-almost every \(s\).

For an atom \(s\), the product point \((s,s)\) has positive measure and the equation gives this vanishing directly.
Restrict now to the nonatomic part.
The scalar \(g(s,t)=\|G_w(s,t)\|_2^2\) is a continuous polynomial expression \(F(m(s),m(t))\) in finitely many bounded complex word moments and their conjugates, by expanding the finite tensor inner product.
Suppose \(g(s,s)\ge\varepsilon>0\) on a set of positive nonatomic measure.
Uniform continuity of \(F\) on the bounded closed moment box gives a finite partition into cells so small that \(|F(m(s),m(t))-F(m(s),m(s))|<\varepsilon/2\) whenever \(m(s)\) and \(m(t)\) are in the same cell.
Intersect the positive-measure set with one such cell to obtain a positive-measure \(A\) on whose product \(g(s,t)\ge\varepsilon/2\).

For \(\nu=\mu|_A\), compact support in the plane allows a cover by \(O(r^{-2})\) disjoint grid cells of diameter at most \(r\), for \(0<r\le1\).
Cauchy--Schwarz gives \((\nu\times\nu)\{|s-t|\le r\}\ge c\,r^2\nu(A)^2\) by summing their squared masses.
The diagonal has zero product measure.
Integrating this bound against \(2r^{-3}\,dr\) over \((0,1)\) proves \(\iint|s-t|^{-2}\,d\nu(s)d\nu(t)=\infty\) by Tonelli.
This contradicts \(\delta w\in H\otimes_2H\) in the differentiated relation.
Thus the claimed diagonal vanishing holds.
Taking a countable intersection makes it valid for every star word on the same conull set.
At each such \(s\) it then holds for every complex linear combination of those words.

### Simple roots force the fiber adjoint into the polynomial algebra

Fix a point in this conull set away from the critical values of \(p\).
The polynomial \(p(u)-s\) has distinct roots and annihilates \(X_s\).
Lagrange interpolation therefore gives \(X_s=\sum_\ell \lambda_\ell P_\ell\), where the nonzero polynomial idempotents \(P_\ell\) sum to \(1\) and \(P_\ell P_j=0\) for \(\ell\ne j\).
Their Hilbert vectors are linearly independent, by multiplication by individual idempotents and separation by the trace vector.
The divided difference of \(p\) at two distinct roots is zero and at a repeated argument \(\lambda_\ell\) it equals \(p'(\lambda_\ell)\).
Substituting the idempotents in \(B_{s,s}\) gives
\[
 B_{s,s}=\sum_\ell p'(\lambda_\ell)P_\ell\otimes P_\ell,\qquad
 p'(\lambda_\ell)\ne0 .
\]

Let \(V_s=\operatorname{span}\{P_\ell\}\).
The second term in \(G_w(s,s)\) has first leg in \(V_s\).
Applying the orthogonal projection onto \(V_s^\perp\) on the first leg of the first term, and using independence of the second legs, yields \(w_sP_\ell\in V_s\) for every \(\ell\).
The separating vector converts this Hilbert-vector inclusion into the same inclusion of represented operators.
Summing over \(\ell\) gives \(w_s\in V_s\), in particular \(X_s^*\in V_s\).
As \(X_s\) also lies in the commutative algebra \(V_s\), it is normal.
Integration gives \(\|[X,X^*]\|_2^2=\int\|[X_s,X_s^*]\|_2^2\,d\mu(s)=0\), so faithfulness proves normality in \(M\).
The single normal generator generates an abelian algebra.
Under the stated actual ACSY hypothesis, [C_F0071 Part C](Yin_C_F0071_v2.md#statement) now gives the bare full-domain dual with the asserted generator-first sign.

## Provenance and scope

This project argument concerns the single-generator branch of [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The fixed [bounded-similarity example](Yin_C_F0133_v1.md#statement) has central \(X^2\) and fails the starred derivation premise.
The proof here treats arbitrary degrees, spectral laws and fiber multiplicities under the stated assumptions.
The planar energy step is the critical two-dimensional Riesz-energy divergence, with its grid proof above.
For comparison, Brauchart and Grabner discuss infinite Riesz energy in the hypersingular regime in [Section 3.3, p. 26 of the authors' edition](https://www.math.tugraz.at/~grabner/Publications/Energy-Designs.pdf).
The theorem leaves open the implication from ACSY to full-domain duals when the generator is nonnormal and its holomorphic polynomial algebra contains no nonconstant central polynomial in the generator.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T10:29 |
| status | open |
| reason | The complete central-polynomial argument and its scalar full-domain consequence are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normality under a central nonconstant holomorphic polynomial, the weaker Hilbert-derivation variant with no critical mass, and the ACSY full-domain consequence. |
| argument | [Argument](#argument) | Moment fibers, differentiated central identities, critical planar energy, simple-root idempotents and scalar application. |
| dependency | [ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The actual starred derivation and vacuum give maximal Delta. |
| dependency | [Affiliated free field](../audits/literature/MSY23/Yin_U001.md#msy23-u001) | Maximal Delta makes each nonzero univariate polynomial regular and thus removes critical atoms of the central law. |
| dependency | [Scalar normal case](Yin_C_F0071_v2.md#statement) | Part C turns the actual ACSY hypothesis for the resulting single normal generator into a bare full-domain dual. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:22 |
| status | proved |
| reason | Adopt the single-generator central-polynomial theorem and its full-domain consequence after whole-proof review of the corrected scalar citation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normality under a central nonconstant holomorphic polynomial, the weaker Hilbert-derivation variant with no critical mass, and the ACSY full-domain consequence. |
| argument | [Argument](#argument) | Moment fibers, differentiated central identities, critical planar energy, simple-root idempotents and scalar application. |
| dependency | [ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The actual starred derivation and vacuum give maximal Delta. |
| dependency | [Affiliated free field](../audits/literature/MSY23/Yin_U001.md#msy23-u001) | Maximal Delta makes each nonzero univariate polynomial regular and thus removes critical atoms of the central law. |
| dependency | [Scalar normal case](Yin_C_F0071_v2.md#statement) | Part C turns the actual ACSY hypothesis for the resulting single normal generator into a bare full-domain dual. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0212_v1.md#whole-proof-finding) | Both hypotheses, the fiber argument and the bare-dual conclusion, including all three direct inputs. |

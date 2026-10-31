---
author: Yin
---

# TV06-U001: Cauchy-transform norms with square-integrable maximal density

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected artifact: the publicly accessible [publisher PDF](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf), 16 PDF pages, with the title, authors, volume, year and printed page range visible in its extracted opening text. |
| source-locator | The selected text was successfully read on printed pp.480--481, physical PDF pages 2--3: maximal-density and curvature definitions, the preceding principal-value discussion, and Theorem 2. |
| inspection | Method: the research subagent developing the consumer read the selected primary theorem statement and checked its application. |

Source-interface inspection: 2026-09-16T13:29.
Human record author: Yin.
Method: the research subagent developing the consumer read the selected primary theorem statement and checked its application.
This is a separate source-interface document, not an independent review of that subagent's mathematical proof.

<a id="tv06-u001"></a>
## Source, artifact and inspection depth

Xavier Tolsa and Joan Verdera, *May the Cauchy transform of a non-trivial finite measure vanish on the support of the measure?*, **Annales Academiae Scientiarum Fennicae Mathematica 31** (2006), 479--494.
Work status: published research paper.
Inspected artifact: the publicly accessible [publisher PDF](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf), 16 PDF pages, with the title, authors, volume, year and printed page range visible in its extracted opening text.

The author-site endpoint did not open in this inspection; the publisher endpoint did.
The selected text was successfully read on printed pp.480--481, physical PDF pages 2--3: maximal-density and curvature definitions, the preceding principal-value discussion, and Theorem 2.
No PDF was retained, no source-byte hash is claimed, and no registered local PDF or rendered-page inspection is implied.
The theorem's full proof and the proofs of its earlier rectifiability inputs were not audited.
Acceptance depth here is exact statement, hypothesis and application inspection of an established result.

The earlier repository source-search note in [Yin_S_F0011](../../../strategies/Yin_S_F0011.md) had already excluded this theorem as a way to deduce geometric hypotheses from an arbitrary polynomial vacuum functional.
The present consumer keeps those hypotheses explicitly and uses the theorem only in that sufficient direction.

## Definitions, hypotheses and exact consumed bound

For a finite positive Radon measure lambda on the plane, use

\[
 C_\epsilon\lambda(z)=\int_{|z-w|>\epsilon}\frac{d\lambda(w)}{z-w},
 \qquad
 M_1\lambda(z)=\sup_{r>0}\frac{\lambda(B(z,r))}{r}.
\]

Let `c(z,w,v)` be the reciprocal circumradius for three distinct noncollinear points, zero for collinear triples, and put

\[
 c^2(\lambda)=\iiint c(z,w,v)^2\,d\lambda(z)d\lambda(w)d\lambda(v).
\]

Theorem 2 assumes

\[
 c^2(\lambda)<\infty,
 \qquad \int(M_1\lambda)^2\,d\lambda<\infty.
\]

Under these assumptions it identifies the finite limit of `||C_epsilon lambda||_(L2(lambda))^2` with a fixed positive linear combination of the squared one-dimensional-density integral and total curvature, and with the squared norm of the principal-value transform.
The limiting density is bounded by the maximal density.
Consequently the precise interface consumed here is: there is an absolute constant `K_0>0`, independent of lambda, such that

\[
 \limsup_{\epsilon\downarrow0}
 \|C_\epsilon\lambda\|_{L^2(\lambda)}^2
 \le K_0\left(c^2(\lambda)+\int(M_1\lambda)^2\,d\lambda\right).
 \tag{S}
\]

The consumer needs this inequality only; it assigns no numerical value to K_0 and does not use a density-normalization coefficient from the exact identity.
Finite `M_1` square integral excludes atoms, since an atom makes `M_1` infinite on a set of positive lambda measure.
The source accepts arbitrary finite positive measures satisfying the displayed energy assumptions; no uniform linear-growth constant or probability normalization is imposed by (S).

## Application check and limits

Consumer: [maximal-density-cauchy-core-transfer.md](../../../claims/Yin_C_F0053_v1.md#maximal-density-cauchy-core-transfer).
For a compactly supported probability mu with finite

\[
 G(\mu)=c^2(\mu)+\int(M_1\mu)^2\,d\mu,
\]

the consumer applies (S) first to mu and then to `lambda_f=(1+f/2)mu`, for real measurable f with sup norm at most one.
Positivity and `mu/2<=lambda_f<=3mu/2` give `G(lambda_f)<=27G(mu)/8`, so every application meets the source's full hypotheses.
Changing the output norm from `L2(lambda_f)` to `L2(mu)` uses `mu<=2lambda_f`.
These are direct weighted-measure checks, independent of any original vacuum assumption.

The positive-weight subtraction, infinity-to-L2 estimate, actual vacuum construction, original closed-graph recovery and free-product consequence are the consumer's mathematical deductions and require their own proof review.
This source document does not independently certify them.

The source does not derive `G(mu)<infinity` from convergence of polynomial pairings of Cauchy truncations, nor from the existence of an actual L2 vacuum adjoint.
It is not used as a T1 theorem on every square and supplies no correlated noncommutative tuple result.
No source registration, canonical assessment, literature-index edit, whole-paper audit, formal verification or novelty claim is performed by this document.

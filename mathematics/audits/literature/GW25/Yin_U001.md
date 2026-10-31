---
author: Yin
---

# GW25: The Classical Polynomial Runge Interface

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published work read by the consuming-proof author; the coordinator used [arXiv:2507.13182v1](https://arxiv.org/html/2507.13182v1) and Debray’s [Math 116 notes](https://www.math.purdue.edu/~adebray/lecture_notes/116notes.pdf), dated 21 August 2015. |
| source-locator | Published Theorem 2, §3; preprint Theorem 2.1, §2; Debray Theorem 6.4, p.16. |
| inspection | After the publisher fetch failed, the coordinator independently checked the same classical statement in the two named alternatives. |

The numbering differs between versions.

The proof author read the published statement.

No full version comparison or whole-paper audit.

<a id="gw25-u001"></a>
## GW25-U001: Polynomial Approximation on a Filled Jordan Domain

Date/reviewers: 2026-09-11; the polynomial-core research agent and the coordinating agent.
The source is Adi Glucksam and Benjamin Weiss, *Measurable Entire Functions II*, IMRN 2025(21), rnaf330.
Bibliographic metadata is corroborated by the [authors' institution](https://cris.huji.ac.il/en/publications/measurable-entire-functions-ii/) and the [publisher](https://academic.oup.com/imrn/article/2025/21/rnaf330/8307121).

The author of the consuming proof read published Theorem 2 in Section 3.
The coordinating agent's subsequent publisher fetch failed, so the coordinating agent independently checked the same classical statement in [arXiv:2507.13182v1](https://arxiv.org/html/2507.13182v1), Theorem 2.1 in Section 2, and in Arun Debray's [Math 116 notes](https://www.math.purdue.edu/~adebray/lecture_notes/116notes.pdf), dated 21 August 2015, Theorem 6.4 on p. 16.
The different theorem/section numbers refer to different versions.
No full version comparison or whole-paper audit was performed.

The accepted statement is the polynomial form of Runge's theorem: if K is a compact subset of C with connected complement and h is holomorphic on a neighborhood of K, polynomials approximate h uniformly on K.
The historical theorem is retained as an established external input; neither source is claimed to be its original proof.
In particular the incidental date printed in the arXiv statement is not used for historical attribution.

The [analytic-arc proof](../../../claims/Yin_C_F0042_v1.md) applies this to the image of a filled ellipse under a holomorphic injective map, which is a filled Jordan domain.
Its inner Cauchy contour gives uniform divided-difference approximation on the spectral arc.
That derivative estimate, the enlarged operator graph and the domain reconstruction are project deductions, not results imported from GW25.
The Debray notes are a corroborating instructional source; the source author's course provenance is Stanford Math 116, taught by Steve Kerckhoff in Fall 2014.

This exact statement and hypothesis match are accepted.
The original Runge proof and the unrelated measurable-entire-function construction were not audited.
The source-search scope and geometric construction are retained in Section 2 of the consumer.

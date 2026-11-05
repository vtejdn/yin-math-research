---
author: Yin
---

<a id="ngu12a-u001"></a>
# Vector-valued progressions and concentration conventions

The selected edition and original-theorem inspection limits are recorded in [Ngu12a source notes](readme.md).
The definitions below were read in arXiv:1105.5733v1, PDF pp. 1--3.
They use Euclidean coefficient space and real scalar random variables; the consuming complex case identifies \(\mathbb C\) with \(\mathbb R^2\).
No originality or equivalence with an uninspected edition is asserted.

<a id="progression-conventions"></a>
## Definition: generalized arithmetic progressions

For vectors \(g_0,\ldots,g_r\in\mathbb R^d\) and integer endpoints \(K_i\le K_i'\), a generalized arithmetic progression is
\[
 Q=\{g_0+\sum_{i=1}^r k_i g_i: k_i\in\mathbb Z,\ K_i\le k_i\le K_i'\}.
\]
Its displayed rank is \(r\), its generators are the \(g_i\), and its volume is \(\prod_i(K_i'-K_i+1)\).
Its size is its actual cardinality, which can be smaller than that volume.
It is proper when the integer-box map is injective.
It is symmetric in this source convention when \(g_0=0\) and \(K_i=-K_i'\).
A vector is \(\delta\)-close to a set if its Euclidean distance to some point of that set is at most \(\delta\).
The local counting proof also uses nonproper progressions, retaining an explicit bound on their displayed integer boxes; the source inverse theorem itself supplies proper symmetric progressions.

<a id="concentration-conventions"></a>
## Definition: linear and quadratic concentration

Let \(\xi_1,\ldots,\xi_n\) be independent copies of a real law \(\xi\), and let \(\beta>0\).
For \(A=(a_i)\) with \(a_i\in\mathbb R^d\), define
\[
 \rho_{\beta,\xi}(A)=\sup_{v\in\mathbb R^d}
 \mathbb P\{\|\sum_i a_i\xi_i-v\|_2\le\beta\}.
\]
For a symmetric array \(A=(a_{ij})\) of vectors in \(\mathbb R^d\), the source's quadratic concentration is
\[
 \rho_{\beta,\xi}(A)=\sup_{v,b_1,\ldots,b_n\in\mathbb R^d}
 \mathbb P\{\|\sum_{i,j}a_{ij}\xi_i\xi_j+\sum_i b_i\xi_i-v\|_2\le\beta\}.
\]
The quadratic convention includes a supremum over linear terms, and differs from fixing those terms in advance.
The local proof's particular quadratic form is bounded by this supremum.
The two uses of \(\rho\) are distinguished by their coefficient arrays.

The inverse-theorem statements and actual local deduction are used in [C_F0188_v2](../../../claims/Yin_C_F0188_v2.md#argument).
The source proof itself remains an accepted external input at the inspection depth stated in the source notes.

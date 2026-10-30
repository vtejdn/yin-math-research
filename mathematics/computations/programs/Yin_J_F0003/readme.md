---
author: Yin
---
# ms23-dual-combinatorics

Context: [MS23-U002](../../../audits/literature/MS23/Yin_U002_v1.md#ms23-u002); [original integration finding](../../../audits/reviews/Yin_R_F0057_v1.md#ms23-integration-review-finding); [original proof and rerun finding](../../../audits/reviews/Yin_R_F0057_v1.md#ms23-u002-proof-finding); [MS23 source units](../../../audits/literature/MS23/readme.md).

## Question and scope

Exact q-polynomial recursive-versus-partition dual checks, crossing controls and the Example3.1 missing-q correction; no all-degree or analytic boundedness certification.

Targets: [MS23-U002](../../../audits/literature/MS23/Yin_U002_v1.md#ms23-u002), Proposition 4.5 and its cancellation steps, and Proposition 3.3 and Example 3.1 in the same supplied 36-page published edition.

### Scope and Mathematical Reduction

The script implements q-Gaussian action on algebraic word tensors, recursively derives the normalized dual from its commutator relation and independently enumerates Proposition 4.5's partitions and polygonal crossings.
It compares integer polynomials in q, including complete output words, and directly checks commutators.
A separate geometric implementation counts crossings between horizontal pair segments and vertical segments of higher pairs/singletons.
It compares these with $\sum_a(p_a-k)+\operatorname{inv}(p)$ and the singleton-deletion and pair-insertion exponent differences.
Thus the drawing check is independent of the closed formula used in the proof.

Inputs exhaust binary words through length 8 and ternary words through length 6, with all dual and Gaussian indices.
Drawing checks cover $B(n+1)$ for $1\le n\le10$; insertion checks use partitions on up to 13 vertices.
Direct commutators may increase input degree by one; no intermediate support cutoff is imposed.
The one-variable check expands $P_q(n-k,k-1)$ as a product of q-integers and compares Proposition 3.3 with the independent recursion for $0\le n\le32$.
For $D e_6$, the $e_3$ coefficient is compared with corrected $-q(1+q+q^2+q^3)$ and published $-q(1+q^2+q^3)$.
Visual inspection of printed/PDF p. 11 confirmed that the discrepancy is in the source, not text extraction.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact finite-check program. |

## Reproduction

From the repository root:

```powershell
python mathematics/computations/programs/Yin_J_F0003/main.py
```

Use Python 3.10+ and the standard library, with no external input files.
The source is the supplied 36-page published MS23 artifact identified in MS23-U002.
All enumerations are deterministic with exact integer coefficients indexed by q-degree and output word, without floating evaluation or tolerance.
The command uses a suitable available Python interpreter and is a present reproduction instruction, not a newly recorded run.
The program prints its finite result; no saved output or input dataset is required.

## Results and limits

All stated comparisons passed:

| Check | Count |
| --- | ---: |
| Drawing versus closed crossing formula | 512 |
| Singleton-deletion exponent | 1,257 |
| Pair-insertion exponent | 1,978 |
| Partition versus recursive dual | 4,301 |
| Direct commutator | 11,881 |
| Negative/boundary controls | 3 |
| One-variable cases n=0–32 | 33 |

The $B(n+1)$ counts for n=1–10 are `[1,1,2,3,6,11,24,51,122,291]`.
The pairing $(0,3),(1,5),(2,4)$ has ordinary crossing count 2 but prescribed drawing count 4.
The two endpoint controls give nonzero images of quotient-null tensors at q=1 and q=-1; quotient-nullness is the separate symmetric/antisymmetric Fock-space fact in MS23-U002.
Independent recursive and closed formulas confirm Example 3.1's missing q: the $e_3$ coefficient is $-q-q^2-q^3-q^4$.
The universal multivariable proof remains the partition-bijection argument in MS23-U002.
Infinite degree, norm estimates, adjoint-domain membership, convergence and boundedness remain outside this finite coefficient, sign, order and exponent check.
No proof-assistant verification occurred.

## Inspection summary

The finite result was recorded for Yin on 2026-09-09; this record does not identify the execution operator.
Actual separate review remains at its responsible source/review material.

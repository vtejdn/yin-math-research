---
author: Yin
---
# miy26-quadratic

Context: [Observable spectrum](../../../audits/literature/Miy26/Yin_U008.md); [Quadratic spectra](../../../audits/literature/Miy26/Yin_U007.md); [readme.md](../../../audits/literature/Miy26/readme.md)

## Question and scope

Exact Gaussian-rational finite recurrence checks, seed and word cutoff, Schur missing-factor witness (-7/5 versus17/5) and cyclic-subspace control; preserve all limitations.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | program |


## Reproduction

From the repository root, using Python with its standard library:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0007/main.py
```

This program uses only the standard library and prints its finite result; no saved output or input dataset is required.
The mathematical account below specifies exact inputs, arithmetic and actual checking scope.
This is a present reproduction command, not a claim of a new run.

## Results and limits

All 14,355 checks passed over 48 Gaussian-rational cases with seed 260319528 and word cutoff seven.
The exact Schur witness gives -7/5 versus the printed 17/5.
Separate reruns used the same implementation; the cyclic-subspace control is not a Miy26-form counterexample.

<a id="retained-mathematical-account"></a>
## Mathematical account

### Exact finite checks for the quadratic spectrum recurrence

Script: [main.py](main.py).
Targets: [Miy26-U007](../../../audits/literature/Miy26/Yin_U007.md#miy26-u007), Theorem 4.6, and [Miy26-U008](../../../audits/literature/Miy26/Yin_U008.md#miy26-u008), Remark 4.7.
The source artifact is the registered exact arXiv v2 of [Miy26](../../../literature/pdf/Miy26.pdf).

#### Scope and reduction

Truncated free-word geometric-series multiplication forms formal inverse coefficients independently of the printed six-state matrix, against which squared-length and mixed coefficients are compared.
Words retain concatenation order; distinct noncommutative words remain distinct.
Every coefficient through word length seven is retained: the polynomial has no constant term, so powers above seven cannot contribute.

The 48 cases comprise twelve boundary/figure examples and 36 reproducible random integer-complex cases.
They include the zero and linear polynomials, a pure quadratic, complex nonsymmetric coefficients, a rank-one symmetric endpoint, a nilpotent coefficient matrix, distinct positive eigenvalues of \(\overline AA\), and a real skew-symmetric example with repeated negative eigenvalues of that product.
All four Figure 1 coefficient cases are included, and each case uses nonzero Gaussian-rational \(\lambda\).

Each case checks six state components at \(n=0,\ldots,6\), every word recursion equation at lengths 1–7 and \(\det Q=-\operatorname{Tr}(B^*B)|\det B|^2\).
The full determinant is compared with an independently evaluated Schur expression at x=7,11 when the four-by-four block is nonsingular; all 96 chosen instances are nonsingular.
Three further examples check the degenerate left eigenvector, the missing-factor discrepancy and the danger of replacing cyclic spectral radius by full spectral radius.
The illustrative \(\operatorname{diag}(0,2)\) is not Miy26-form and is not a counterexample to the unrestricted Miy26 replacement.

#### Observed execution output

All 14,355 stated checks passed, without a failed assertion:

| Check | Count |
| --- | ---: |
| State components | 2,016 |
| Coefficient equations | 12,192 |
| Determinants | 48 |
| Schur complements | 96 |
| Boundary examples | 3 |

These count checked components, equations and examples, not independent theorems.
The missing-factor witness \(A=\operatorname{diag}(-2,1)\), \(b=(3,0)\), \(\lambda=1\), x=3 gives actual/corrected Schur value -7/5 and printed value 17/5.
This expected failure of the uncorrected source expression remains a checked discrepancy.
The source units supply the infinite-order recurrence, exponential-decay implication, analytic inverse and restricted spectral-radius equivalence.
Finite data establish neither infinite summability nor an unrestricted \(r(Q)\) criterion, spectral-boundary numerical stability, random-matrix convergence or formal verification.

#### Inspection summary

On 2026-09-08 the circular-section agent read and independently reran the same script; root separately read the complete script and reproduced the same counts and discrepancy.
These reproductions check the same retained implementation, not separately implemented algorithms.

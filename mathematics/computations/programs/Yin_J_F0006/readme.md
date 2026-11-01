---
author: Yin
---
# miy26-circular

Context: [Circular examples](../../../audits/literature/Miy26/Yin_U006.md); [Circular resolvents](../../../audits/literature/Miy26/Yin_U005.md); [readme.md](../../../audits/literature/Miy26/readme.md)

## Question and scope

Finite circular Wick words, resolvent/characteristic/Perron identities and degenerate-parameter controls; retain exact counts without an analytic-limit or Brown-measure claim.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | program |


## Reproduction

From the repository root, using Python with its standard library:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0006/main.py
```

This program uses only the standard library and prints its finite result; no saved output or input dataset is required.
The mathematical account below specifies exact inputs, arithmetic and actual checking scope.
This is a present reproduction command, not a claim of a new run.

## Results and limits

All 193,363 finite checks passed, including coefficient/shell, determinant-grid and zero/unit-radius controls.
Root reproduced the same implementation; no analytic-limit or Brown-measure conclusion follows.

<a id="retained-mathematical-account"></a>
## Mathematical account

### Exact circular-word and product-resolvent checks

Script: [main.py](main.py).
Targets: [Miy26-U005](../../../audits/literature/Miy26/Yin_U005.md#miy26-u005) and [Miy26-U006](../../../audits/literature/Miy26/Yin_U006.md#miy26-u006).

#### Scope and mathematical reduction

The word checks independently evaluate the finite Wick sum and right-annihilation commutator, then compare with [Miy26-U005's residual formula](../../../audits/literature/Miy26/Yin_U005.md#lemma-41-repaired-proof-and-exact-coefficient-identity).
Alphabet sizes are d=1,2, mixed operator lengths 0–4 and input lengths 0–3.
All intermediate actions are exact and untruncated; positive-word inputs separately check the creation restriction.

For Example 4.5, prefix recursion is compared with the increasing-run coefficient formula for k=1–4, lengths 1–6, rational lambda in {-2,-1,0,1/2,2} and t in {-1,0,1/2,2}.
Independently summed coefficient squares are compared with the transfer-matrix shell formula.
Exact Gaussian elimination checks `(1-a) det(xI-M(a))=(x-1+a)^k-a*x^k` for k=1–6, a=0,…,k+1 and x=0,…,k.
For each checked k, polynomial degree bounds make this grid sufficient to identify both sides as polynomials in a,x; it proves no formula for all k.
The a=1 specialization is checked separately against `x^(k-1)(x-k)`.
Eigenvectors use a=b^k for b in {0,1/2,1,2}.
At a=0, powers m=0–10 check `1^T M^m 1=binomial(m+k,k-1)`.

#### Execution and interpretation

All 193,363 checks passed:

| Check | Count |
| --- | ---: |
| Mixed-word commutator | 58,435 |
| Holomorphic restriction | 485 |
| Random-walk coefficients | 133,680 |
| Random-walk shells | 480 |
| Characteristic grid | 166 |
| Characteristic unit radius | 27 |
| Perron eigenvectors | 24 |
| Zero-parameter Jordan growth | 66 |

These tests detect label reversal, prefix orientation and zero/unit-radius errors.
Universal coefficient identities, affiliated inverse existence, convergence, spectral equality, R-diagonality and Brown-measure identification require the units' analytic arguments and dependencies.
This is finite exact computation, not formalization or a numerical spectrum plot.

#### Inspection summary

On 2026-09-08 root read the complete script and record, reran the same implementation and reproduced all category totals without a failed case.
Root checked Wick action, prefix recursion, determinant-grid degree bounds and degenerate branches.
The original execution also reported no failed case.
This reproduction does not extend the finite scope or supply a separately implemented algorithm.

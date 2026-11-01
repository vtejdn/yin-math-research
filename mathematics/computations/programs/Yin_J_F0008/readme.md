---
author: Yin
---
# Finite matrix probes for the nonlinear weighted Hilbert–Schmidt inverse

Context: [T_F0011](../../../tasks/Yin_T_F0011_v1.md#objective-2-arbitrary-tuples-and-maximal-delta) and the nonlinear operator/domain statements in [C_F0142](../../../claims/Yin_C_F0142_v1.md#statement).

## Question and scope

For positive diagonal h and Hermitian Gaussian S, form A=h^(1/2)S h^(1/2) and K=A tensor I+I tensor A^T+i h tensor h^T.
Solve K U=h^(1/2) tensor h^(1/2), then compare normalized Hilbert–Schmidt norms of U and V=(h^(-1/2) tensor h^(-1/2))U across sizes.
This is a floating-point weighted-inverse/unweighting probe, not a computation of actual ACSY derivations.
Finite matrix inputs have atoms and do not satisfy the free-difference-quotient hypotheses.
No finite solution is a full-domain dual system or an A-to-F counterexample; growing dimensions/GUE inputs certify no asymptotic or infinite-dimensional conclusion.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Seeded dense complex128 calculation and residual/positive-S controls. |
| `../../outputs/Yin_J_F0008/results.json` | Historical output location for the complete 30-case run; no payload is retained here. |

## Reproduction

From the repository root, with NumPy in the shared Python environment:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0008/main.py
```

Output resolves to `mathematics/computations/outputs/Yin_J_F0008/results.json`, independently of the caller's directory.
Default sizes are 8,12,16,24,32; h quantile powers are 0.8,1,1.2; shifts are 0,3; the base seed is 20261015.
Each row uses seed base+n, and arithmetic is complex128.
NumPy supplies the dense linear algebra; no SciPy is required.
Use `--output control.json` or another distinct filename for changed/smaller scopes.
Parameters and mathematical rows remain in the result, without execution timestamps or a mandatory progress archive.
The complete result is published atomically only after all selected checks pass.
A clone can lack generated output; these instructions do not execute it automatically.

Checks use the relative equation residual and the proved bound ||U||HS<=1/(2 min spectrum(S)) when S is positive.
Normalized HS norm is Frobenius norm divided by n because the coefficient algebra M_n tensor M_n^op has probability trace.
Both K U=D and the independently assembled F V=I are checked on complex Hermitian samples, testing transpose/opposite-algebra and unweighting order.

## Results and limits

The `acsy_to_full_domain` agent completed the default 30-case calculation; both equation checks and all 15 positive-S controls passed.
For centered S and power 1.2, weighted U norms were approximately 1.19 at n=8 and 1.52 at n=32; unweighted V norms were approximately 8.82 and 54.25.
The other two powers also changed substantially more in V than in U over this finite range.
Positive-shift controls obeyed the bound with much smaller norms.
These observations motivate distinguishing weighted range from subsequent unweighting; they certify no convergence/divergence, free-limit transfer or existence/nonexistence of ACSY vacuum or full-domain duals.
No external analytic theorem is claimed by this computation.

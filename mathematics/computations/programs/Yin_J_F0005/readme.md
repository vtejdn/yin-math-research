---
author: Yin
---
# free-poisson-wick

Context: [All-positive-rate proof review](../../../audits/reviews/Yin_R_F0110_v1.md#original-f0044-account); [Yin_C_F0096_v1.md](../../../claims/Yin_C_F0096_v1.md)

## Question and scope

Exact finite recursive-versus-normal-ordered Wick and commutator checks; preserve the negative-parameter sign control as algebraic scope beyond the adopted positive family.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | program |


## Reproduction

From the repository root, using Python with its standard library:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0005/main.py
```

This program uses only the standard library and prints its finite result; no saved output or input dataset is required.
The mathematical account below specifies exact inputs, arithmetic and actual checking scope.
This is a present reproduction command, not a claim of a new run.

## Results and limits

All 1,953 Wick columns and 3,906 commutator columns passed at the stated finite lengths.
The negative parameter is an algebraic sign control outside the nonnegative Poisson family.
The all-word and analytic claims remain in the responsible Claim.

<a id="retained-mathematical-account"></a>
## Mathematical account

### Exact Free-Poisson Word Checks

Script: [main.py](main.py).
Target: [Yin_C_F0096](../../../claims/Yin_C_F0096_v1.md#yin_c_f0096).

The script compares recursive polynomial action with the normal-ordered Wick formula, then the right-annihilation commutator with the corrected residual formula.
It uses two letters, parameters \(a=(2/3,-1/2)\), all polynomial words of lengths 0–5 and all test words of lengths 0–4.
The negative second parameter exercises algebraic signs outside Yin_C_F0096's stated nonnegative Poisson family.
No intermediate support is truncated and no random sampling is used.
Arithmetic is exact `fractions.Fraction`, with memoized recursive word actions.

#### Results and limits

All 1,953 Wick columns and 3,906 commutator columns passed.
These finite checks detect preservation terms, word reversal, suffix orientation and sign errors.
They do not replace the all-word identities, affiliated-domain argument, finite residual proof or norm-convergence theorem in Yin_C_F0096.
No numerical approximation, human peer review or formal verification is claimed.

#### Inspection summary

The finite result was recorded for Yin on 2026-09-11; the execution operator is not identified in this record.
No additional independent checking arrangement is inferred.

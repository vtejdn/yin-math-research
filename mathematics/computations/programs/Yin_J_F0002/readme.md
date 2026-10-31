---
author: Yin
---
# miy22-commutators

Context: [Miy22-U003](../../../audits/literature/Miy22/Yin_U003.md#miy22-u003); [Miy22 source units](../../../audits/literature/Miy22/readme.md).

## Question and scope

Finite exact Fock word actions and adjoint-sign comparisons without intermediate support truncation; the universal identities, closure and analytic scope remain in source audits.

Target: [Miy22-U003](../../../audits/literature/Miy22/Yin_U003.md#miy22-u003), Lemmas 3.2–3.3 and the signs in Remark 3.10.

### Scope and Mathematical Reduction

The algebraic full Fock space uses finite dictionaries from words to integer coefficients.
The empty tuple is the vacuum word; the empty dictionary is the zero vector.
Left creation prepends a letter, left annihilation deletes a matching first letter, right creation appends a letter and right annihilation deletes a matching last letter.

The operator `s_i` is left creation plus left annihilation.
The recurrence `U_0=1`, `U_1=s_i`, `U_(k+1)=s_i U_k-U_(k-1)` is evaluated directly on vectors.
Consecutive runs of a general word determine the ordered polynomial product.
This action supplies the left sides independently of the suffix formula.
No vector support is cut off, including at intermediate steps.

| Check | Finite scope over alphabet {1,2} | Equalities |
| --- | --- | ---: |
| Vacuum `U_v Omega=e_v` | Every v of length 0–4 | 31 |
| `[r_i^*,s_j] e_w=delta_ij P_Omega e_w` | Both i,j; every w of length 0–4 | 124 |
| Lemma 3.2 rank-one sum for `[r_i^*,U_k(s_j)] e_w` | Both i,j; k=1–6; every w of length 0–4 | 744 |
| Lemma 3.3 removal of `i reverse(w)` from v | Both i; every v,w of lengths 0–4 | 1,922 |
| Creation sign `[r_i,U_v] e_w=-[r_i^*,U_v] e_w` | Both i; every v,w of lengths 0–4 | 1,922 |
| Adjoint `[r_i^*,U_v]^*=[r_i^*,U_reverse(v)]` | Both i; every v and matrix input/output word of lengths 0–4 | 59,582 |

The suffix comparison returns zero when the suffix is absent and the vacuum vector when it removes all of v.
Empty words, repeated runs and non-palindromic words test the reversal order.
The universal argument in Miy22-U003 uses Leibniz and Lemma 3.2 to obtain one term `U_p P_Omega U_q` for each cut `v=p i q`.
Since `U_q^*=U_reverse(q)`, the term survives on `e_w` exactly when `q=reverse(w)`.
The recurrence uses `U_-1=0` at the boundary.
The creation sign follows from `[r_i+r_i^*,a]=0` in the left von Neumann algebra; the adjoint sign also uses `[A,B]^*=-[A^*,B^*]`.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact finite-check program. |

## Reproduction

From the repository root:

```powershell
python mathematics/computations/programs/Yin_J_F0002/main.py
```

Only the standard library is needed; fixed inputs are in the script.
The enumeration uses exact integers without floating tolerances or Fock-space truncation.
The source specification is the journal edition identified in [Miy22-U003](../../../audits/literature/Miy22/Yin_U003.md#miy22-u003), Lemmas 3.2–3.3 on pp. 9–10 and Remark 3.10 on p. 18.
The command uses a suitable available Python interpreter and is a present reproduction instruction, not a newly recorded run.
The program prints its finite result; no saved output or input dataset is required.

## Results and limits

All 64,325 exact dictionary or matrix-entry equalities passed, with no failed check in this scope.
Universal induction, von Neumann algebra commutation, bounded inverse closure, norm estimates and Theorem 3.1 remain outside the computation.
It proves no all-word identity or rationality criterion.

## Inspection summary

The finite result was recorded for Yin on 2026-09-08; the execution operator is not identified here.
A separate audit agent reconstructed the universal commutator argument and bounded closure direction from the identified source pages, as recorded in Miy22-U003.
The computation is supplementary evidence, not that source proof or formal verification.

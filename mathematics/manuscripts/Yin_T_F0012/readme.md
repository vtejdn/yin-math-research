# Brown Measure Convergence for Polynomials in Independent GUE Matrices

Responsible author: Yin (Sheng Yin).
This manuscript presents the proof selected for [Task F0012 v2](../../tasks/Yin_T_F0012_v2.md#decision-almost-sure-completed).
It establishes almost-sure weak convergence to Brown measure for every fixed scalar polynomial in independent normalized GUE matrices, with arbitrary coupling across sizes.
It also presents the associated almost-sure and mean convergence results for affine determinants.

- [Paper sources and build instructions](paper/readme.md)
- [Organization](organization.md) and [writing conventions](conventions.md)
- [Citation map](citation.md) and [manuscript review](paper/review.md)

## Mathematical provenance

| Manuscript result | Responsible argument |
| --- | --- |
| Theorem `thm:brown` | [C_F0186 v3, linearization transfer](../../claims/Yin_C_F0186_v3.md#linearization-transfer) and [one-event planar limit](../../claims/Yin_C_F0186_v3.md#brown-as), using the [v1 scalar probability limit](../../claims/Yin_C_F0186_v1.md#polynomial-application). |
| Theorem `thm:affine` | [C_F0186 v3, strengthened affine argument](../../claims/Yin_C_F0186_v3.md#argument), including the [v2 rank](../../claims/Yin_C_F0186_v2.md#generic-rank) and [resolvent](../../claims/Yin_C_F0186_v2.md#logarithmic-tail) inputs. |
| Theorem `thm:pencil` and Lemma `lem:gaussian-tube` | [C_F0186 v1, monic pencil argument](../../claims/Yin_C_F0186_v1.md#tubes) with the [v3 Gaussian tube estimate](../../claims/Yin_C_F0186_v3.md#tube-without-floor) and [summable norm bound](../../claims/Yin_C_F0186_v3.md#norm-tail). |
| Proposition `prop:distance` | [C_F0186 v2, affine compression and Hermitian lifting](../../claims/Yin_C_F0186_v2.md#affine-repair). |

[R_F0190 v3](../../audits/reviews/Yin_R_F0190_v3.md#independent-strong-proof) independently reviewed the fixed strengthened argument and its application to the Task v2 contract.
The [manuscript-local review](paper/review.md) records checks of its current exposition.

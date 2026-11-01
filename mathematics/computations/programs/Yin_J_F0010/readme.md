---
author: Yin
---

# One-Kraus affine determinant adversarial screen

## Question and exact scope

This is the existing [L_F0029 source-candidate screen](../../../ledger/Yin_L_F0029_v1.md#numerical-adversarial-check-with-a-noncommuting-drift), originally executed on 2026-09-13 with Python 3.13.15 and the standard library.
The retained native program is [main.py](main.py).
It tests a necessary universal comparison for the strict-domain candidate that was subsequently proved in [C_F0124](../../../claims/Yin_C_F0124_v1.md#statement).
This floating-point search is consistency evidence; that theorem's proof does not depend on it.
No new execution was performed while retaining this program in its responsible J home.

## Reproduction and mathematical inputs

From the repository root, run:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0010/main.py
```

Only random, math and cmath from Python's standard library are used.
The original seed is 83925 and the loop has 200000 draws, skipping abs(p*q)<1e-5.
For selfadjoint B=diag(p,q) and real-symmetric A=[[a,z],[z,d]], the quadratic determinant roots reduce the potential to the explicit scalar semicircular formula.
A diagonal unitary makes the off-diagonal drift real after diagonalizing the one selfadjoint noise coefficient, so these inputs include noncommuting one-Kraus size-two pencils.
The source candidate and its strict-domain repair retain their exact definition in L_F0029/C_F0124; negative Hilbert--Schmidt directions pq<0 are included.
This is finite ordinary floating-point arithmetic, with no interval enclosure or exhaustive theorem over the real parameters.
The program prints its worst residual and input tuple; it writes no output file.

## Retained actual outcome and limits

The original 200000-draw screen found no violation.
Its largest residual was -3.2285730582892747e-6 at k=59790, p=-0.6276111874414962, q=0.7787443888517115, a=0.5943016407731344, d=-0.6839372533367548 and z=0.4610325177001209.
The potential was -0.15598734721283608 and the proposed upper bound was -0.1559841186397778.
Inputs near zero determinant make the numerical comparison delicate.
No certified residual sign, independent program review, arbitrary coefficient-size theorem or new mathematical Task decision follows from the screen.
The current maintenance inspected the complete original program and preserved it literally, with a static Python syntax parse only.

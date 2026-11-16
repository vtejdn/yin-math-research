---
author: Yin
---
# Six triples remain compatible with all binary equations on the eight-by-twelve support

Use precisely the row and column order and the ten numbered multiterm fibers in the [eight-by-twelve table](Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation).
The original torsion-free group has finite abelianization, and the two supports occupy the same [four exterior cyclic cosets](Yin_L_A0042_v1.md#the-two-covers) as before thickening.
The following calculation treats a family satisfying all thirty-two double equations.

## A family inside the binary equations

For three independent nonzero complex parameters \(c,e,r\), take
\[
\begin{aligned}
u&=(1,-r,-r^{-1},1,1,1,-r^{-1},-r),\\
v&=(1,c,r^{-1},er^2,cr^3,er,r^2,cr^2,r,cr,e,e/r).
\end{aligned}
\]
Substitution of \(u_i v_j\) in each double fiber of the [faithful table](../computations/programs/Yin_J_A0003/verify.py) gives opposite copies of one Laurent monomial.
For example, the coefficient at the identity is \(u_1v_1+u_2v_3=1-r/r=0\).
The [symbolic verifier](../computations/programs/Yin_J_A0003/verify_eight.py) checks all thirty-two identities using signed integer exponents.
It also gives the following expressions for the remaining coefficients.

| Fiber | Coefficient after substitution |
| --- | --- |
| 1 | \(c-er^3+r^{-1}\) |
| 2 | \(e/r-cr^4\) |
| 3 | \(r^2-c/r\) |
| 4 | \(cr^3-r^{-2}+er^2\) |
| 5 | \(c-(1+e)r^3\) |
| 6 | \(cr^3-(1+e)/r^2\) |
| 7 | \(-r^3\) |
| 8 | \(-e/r^2\) |
| 9 | \((1+e)r^2-c/r\) |
| 10 | \((1+e)/r-cr^4\) |

## Solving the triples with variable ratios

In each of fibers \(1,4,5,6,9,10\), the original three signed terms have distinct exponent vectors in \((c,e,r)\).
Thus the ratio of every two terms in each of these six fibers varies even after **all** the double equations have been imposed.
The other four multiterm fibers each contain an opposite pair on this family, as their uncombined terms in the verifier show.

Within this family all six triples vanish exactly when
\[
             r^4=-1,\qquad c=(1+e)r^3,\qquad e\ne0,-1 .
\]
Indeed fibers 5 and 1 give the displayed formula for \(c\) and \(r^3+r^{-1}=0\).
Substituting these identities into fibers 4, 6, 9 and 10 gives zero, using \(r^8=1\).
For instance one may take \(e=1,\ r=\exp(\pi\mathrm i/4),\ c=2r^3\).
Hence the thirty-two binary equations together with six coupled triples whose internal ratios all vary do have full-support complex solutions.
At these points the coefficient of fiber 7 is \(-r^3\ne0\), so they do not give zero products or branches to which the [rank sampling theorem](../claims/Yin_C_A0030_v1.md#statement) applies.
This calculation fixes one family inside the binary equations and makes no classification of their other solutions.

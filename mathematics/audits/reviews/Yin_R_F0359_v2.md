---
author: Yin
---

# Transverse determinant zeros for the quadratic Hermitian test at every shift

An agent acting for Yin independently examined the working-tree version [C349v2](../../claims/Yin_C_F0349_v2.md#statement) at 2026-11-17T06:38 UTC.
The reviewer did not participate in proof development and received the fixed objects and scope without development dialogue, exploration notes or explanations from the proposing agent.
The reviewer consulted the [prior finding for C349v1](Yin_R_F0359_v1.md#winding) for its unchanged hypotheses and its separate result on the doubled pencil.

<a id="all-shifts"></a>
## Whole-proof finding for the fixed-shift obstruction

For \(A=\operatorname{diag}(1,2,3)\), the rows of \(AB+2BA-zI\) are
\[
 (3t-z,5(1+is),7),\qquad
 (4(1-is),-z,8d),\qquad (5,7d,-z).
\]
Expansion in the first row gives the linear coefficient \(3(z^2-56d^2)\) in \(t\), the terms \(20z(1+s^2)+35z\), and the oriented cycles \(200d(1+is)+196d(1-is)\).
At \(d=1+|z|\) the coefficient in \(t\) is strictly negative and the imaginary part is \(4ds\).
Thus \(s=0\) and the displayed \(t_0\) in the Claim give a zero with real Jacobian determinant \(12d(z^2-56d^2)<0\).
In particular \(z=0\) gives \(t_0=33/14\) and Jacobian determinant \(-672\).
For the two-by-two evaluation at \(z=\alpha+i\beta\) with \(\beta\ne0\), the determinant in centered coordinates \((u,v)\) is \((u+iv)(-2i\beta+u-iv)\).
Its derivative is complex multiplication by \(-2i\beta\), so its real Jacobian determinant is \(4\beta^2>0\).

For either zero the rescaled target on the unit circle converges uniformly to its invertible real derivative applied to the unit vector.
Straight-line interpolation then gives the sign of the real Jacobian as its local winding number.
In a local identity of complex determinants with a factor nonzero throughout the disk, taking a positive power \(r\) multiplies that winding by \(r\), and the factor contributes zero winding.
In the modulus identity put \(h=\det D\) on the affine parameter plane.
Its first nonzero homogeneous term exists because \(h\) is polynomial and nonzero on a punctured neighborhood.
Along a ray where that term is nonzero, the strictly positive radial limit of \(|h|/\rho^r\) forces its degree to be \(r\).
The same limit along every ray makes the homogeneous term nonzero in every unit direction.
Uniform convergence of \(\rho^{-r}h\) on the circle identifies its winding with that of the leading term.
For odd \(r\) the change of a lifted argument over a half turn is an odd multiple of \(\pi\), constant as the start angle varies by continuity.
Doubling that increment gives an odd winding.
Each proposed determinant loop is invertible on the boundary, and interpolating its dissipative matrix to \(iI\) gives strictly positive imaginary part for positive interpolation time.
Its winding is therefore zero, also after a fixed scalar rotation.
Regular auxiliary factors and their reciprocals have zero boundary winding and continuous positive modulus.

Adjoining the scalar pair \((1,b)\) on each extra coordinate multiplies the target by \((3b-z)^{N-n}\), which is nonzero for the indicated real choices of \(b\).
This preserves transversality and its orientation since nonzero complex scalar multiplication has positive real Jacobian determinant.
The same contradiction applies in each \(N\ge n\), in particular in every sufficiently large even dimension, with any auxiliary size allowed in that dimension.
The full Hermitian input space contains the complex Hermitian three-by-three slice.
At a real shift on real symmetric inputs the target determinant is real, so the real-shift construction genuinely uses the larger input space.
Independent complex Gaussian off-diagonal entries of nondegenerate real and imaginary parts and nondegenerate real Gaussian diagonal entries have full support at every size and admit the Task's normalization.
For such a model, an almost-sure equality of continuous functions with the stipulated globally nonvanishing factor is an equality throughout the support.

This verifies the entire fixed-shift obstruction of C349v2.
The modulus argument covers odd positive powers, and the complex determinant argument covers every positive power.
The earlier even-modulus construction and its restricted row-module and probability implications retain the scope of their prior finding.
The finite-dimensional obstruction gives no probability estimate for the logarithm of the original random quadratic determinant.

## Review relationships

| Review | Relationship |
| --- | --- |
| [All shifts](#all-shifts) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [All shifts](#all-shifts) | [Statement](../../claims/Yin_C_F0349_v2.md#statement) | Complex identities for all positive powers and modulus identities for positive odd powers at each fixed shift. |
| [All shifts](#all-shifts) | [Argument](../../claims/Yin_C_F0349_v2.md#argument) | Transverse zeros, polynomial leading form, parity, disk factors and dissipative contraction. |
| [All shifts](#all-shifts) | [Real-shift evaluation](../../claims/Yin_C_F0349_v2.md#real-test) | Exact three-by-three determinant, center, Jacobian and zero shift. |
| [All shifts](#all-shifts) | [Larger sizes](../../claims/Yin_C_F0349_v2.md#larger-sizes) | Nonzero scalar blocks, even sizes, real-input limitation and full-support extension of a continuous identity. |
| [All shifts](#all-shifts) | [Nonreal-shift evaluation](../../claims/Yin_C_F0349_v1.md#argument) | Centered determinant factors and positive local degree for every nonreal shift. |
| [All shifts](#all-shifts) | [Earlier even lift](../../claims/Yin_C_F0349_v1.md#even-doubling) | Unchanged canonical even lift and its specified stabilizations, at the scope of the earlier finding. |
| [All shifts](#all-shifts) | [Earlier review](Yin_R_F0359_v1.md#winding) | Prior reviewed scope of the even lift and its conditional probability implication. |
| [All shifts](#all-shifts) | [Input model](../../tasks/Yin_T_F0013_v1.md#input-model) | Within-size full-support Gaussian example allowed by the Wigner assumptions. |
| [All shifts](#all-shifts) | [Scalar Task](../../tasks/Yin_T_F0014_v1.md#contract) | Separation of the exact identity obstruction from the requested random determinant upper-limit equality. |

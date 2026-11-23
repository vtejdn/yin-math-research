---
author: Yin
---

# Integer canonical trace on the algebraic projective classes

<a id="ope26g-u001"></a>
## Theorem 1.1 and Corollary 1.2(i)

The [author's preprint](readme.md) defines the Hattori-Stallings trace of a finitely generated projective right module represented by an idempotent \(e\in M_q(\mathbb CG)\) as the class of \(\sum_i e_{ii}\) modulo additive commutators.
Under the identification in equation (1.1), its coefficient at a conjugacy class is the sum of the coefficients of the diagonal trace on that class. [Page 2](../../../literature/pdf/Ope26g.pdf#page=2)

Theorem 1.1 asserts that for every discrete group this trace vanishes on every infinite-order conjugacy class.
For a torsion-free group Corollary 1.2(i) identifies the unnormalized canonical trace of \(e\) with the ordinary rank of the complex matrix obtained by applying augmentation to its entries. [Page 3](../../../literature/pdf/Ope26g.pdf#page=3)

The deduction in equation (10.1) uses the support assertion from Theorem 1.1.
The canonical trace is the coefficient at the identity class, the only surviving class for a torsion-free group.
All entries have finite group support, so summing their diagonal coefficients over all classes gives exactly the augmented matrix trace.
The augmented matrix is idempotent, hence its trace equals its rank.
Passing to differences gives integer trace for every class in \(K_0(\mathbb CG)\), and the free module of rank one supplies the generator of \(\mathbb Z\). [Section 10, page 30](../../../literature/pdf/Ope26g.pdf#page=30)

For a matrix idempotent the positive similarity used in Section 10 identifies its canonical trace with the von Neumann dimension of its projective image.
Thus Corollary 1.2(i), if used with its stated theorem input, excludes \(1/2\) from the trace image of \(K_0(\mathbb CG)\) inside an actual affiliated scalar inverse layer.
Remark 10.1 restricts the analogous conclusion for the reduced group \(C^*\)-algebra to the image of the algebraic classes. [Pages 30-31](../../../literature/pdf/Ope26g.pdf#page=30)

This inspection verifies the deduction and its trace conventions against the author PDF and the [Section 10 source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/build/sections/10-torsion-free.tex).
The support theorem from Sections 2-9 remains an external preprint input whose proof was outside the inspection.
The [two-layer unit-class test](../../../claims/Yin_C_A0129_v1.md#a-positive-matrix-over-the-original-group-ring) would still require control of new projective classes over \(D_2(G)\), where the algebraic augmentation has no general extension.

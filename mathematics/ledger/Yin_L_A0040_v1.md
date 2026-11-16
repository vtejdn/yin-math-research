---
author: Yin
---
# Projective dimension tests on a component of the cancelling coefficient table

Let \(G\) be torsion-free and let \(A,B\) be the fixed nonempty supports of the two factors.
In \(\mathbb P^{|A|-1}\times\mathbb P^{|B|-1}\) impose the original bihomogeneous coefficient equations \(\sum_{xy=w}a_x b_y=0\).
Choose an irreducible component of the exact-support locus and let \(X\) be its projective closure.
Let \(Y_A,Y_B\) be its two projections; projectivity makes these images closed.
These varieties depend only on the finite table of actual group-element products.

Suppose the component contains a zero product with both regular ranks \(1/2\).
By the [componentwise rank bound](../claims/Yin_C_A0030_v1.md#components-and-exact-support), every pair on the component has both individual ranks at most \(1/2\).
The same upper bounds hold throughout \(X\): in local projective charts coefficient convergence gives operator-norm convergence and rank is lower semicontinuous.
The exact-support part is Zariski open dense in its closure and hence dense in the usual complex topology there.
Consequently every coefficient vector in \(Y_A\) has rank at most \(1/2\), and similarly on the other side.

Take \(S\subset A\) nonempty such that **every** nonzero element supported in \(S\) has rank strictly above \(1/2\).
Then \(Y_A\) misses the coordinate subspace \(\mathbb P(\mathbb C^S)\).
The projective dimension theorem over \(\mathbb C\) gives
\[
        \dim Y_A \le |A|-|S|-1 .                                         \tag{1}
\]
Indeed two projective subvarieties in \(\mathbb P^{|A|-1}\) whose dimensions sum to at least \(|A|-1\) intersect.
The corresponding bound holds for \(Y_B\).
Possible \(S\) include any set of at most [four group elements](../claims/Yin_C_A0027_v1.md#four-point-rank) and all support points lying on at most [two cyclic cosets](../claims/Yin_C_A0019_v1.md#consequences-for-group-ring-products) of either orientation.
Thus if \(A\) occupies four cosets, \(\dim Y_A\) is strictly smaller than the combined occupancies of the two smallest, regardless of their Laurent coefficients.
A component whose projection exceeds any of these bounds cannot contain a half pair, even when every integer grading of the entire table is constant.

If the half-rank pair on this component is primitive for the [four right-coset and four left-coset covers](../claims/Yin_C_A0020_v1.md#primitivity-and-coefficient-collisions), the annihilator supported in \(A\) of its fixed \(b\) is exactly the line \(\mathbb Ca\).
This includes coefficient vectors whose support is a proper subset of \(A\).
Thus the projective fiber of \(X\to Y_B\) over \([b]\) is a single point. The same argument applies to the fiber over \([a]\).
The fiber dimension theorem for a dominant morphism of irreducible varieties gives \(\dim X=\dim Y_A=\dim Y_B\), since each nonempty fiber has dimension at least the difference of the dimensions.
For this primitive situation (1) is therefore a bound on the dimension of the entire component.
This argument supplies no exclusion for a low-dimensional component whose projections avoid all the indicated coordinate subspaces; a point component is allowed by the dimension test.

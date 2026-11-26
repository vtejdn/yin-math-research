---
author: Yin
---

# Descending four simultaneous kernels to the index-four sign subgroup

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity.
Suppose the sign map onto \(C_2^2\) takes \(s,t\) to its two basis elements, and put \(N\) for its kernel.
Suppose \(K=P(t)-sQ(t)\) for two-square linear pencils has regular nullity \(1/2\).
There is a four-square group-ring matrix \(R\) over the actual subgroup \(N\), supported on at most eight group elements, with regular rank two, and no nonzero left or right group-ring syzygy even after extension to \(\mathbb CH\).
Write \(E\) for the orthogonal kernel projection of \(R\) and \(p\) for that of \(K\).
Without any closed-range assumption one has
\[
                   E\in M_4(C_r^*(N))\quad\Longleftrightarrow\quad
                   p\in M_2(C_r^*(H)).
\]
The finite character group acting on \(H\) makes all four signed rectangle kernels have the same properties.

There is an additional alternative inside the original index-four subgroup.
Either its first scalar inverse layer contains a scalar of regular rank strictly between zero and one, or there are two-square matrices \(V_s,V_t\) invertible over its second scalar inverse layer such that
\[
  V_s\,{}^s V_s=s^{-2} I_2,\qquad
  V_t\,{}^t V_t=t^{-2} I_2,\qquad
  V_s\,{}^s V_t\,([s,t] I_2)=V_t\,{}^t V_s ,
\]
where \({}^gX=gXg^{-1}\) entrywise and \([s,t]=st(ts)^{-1}\).
Both matrices are expressed using the same basis of the rank-two kernel over \(N\).
These simultaneous identities are necessary in the absence of the fractional scalar in the first alternative.
Their solvability in general is unresolved.

## Two involutions with a polynomial commutator

Let \(T=\left(\begin{smallmatrix}A&B\\ C&D\end{smallmatrix}\right)\) for \(P(z)=Az+B,\ Q(z)=Cz+D\).
The [four-column reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) makes \(T\) invertible.
On the four-coordinate module define bounded group-ring involutions
\[
 J=\begin{pmatrix}0&sI_2\\s^{-1}I_2&0\end{pmatrix},\qquad
 L=T\begin{pmatrix}0&tI_2\\t^{-1}I_2&0\end{pmatrix}T^{-1},\qquad
 R=((st)^{-1}I_4)(JL-LJ).
\]
Each term of \(JL-LJ\) has the same binary degree as \(st\).
The support of \(R\) is thus contained in the eight points \((st)^{-1}s^{\pm1}t^{\pm1},(st)^{-1}t^{\pm1}s^{\pm1}\) of \(N\).

The commutator kernel is invariant under \(J,L\): the commutator anticommutes with each involution.
On it the restrictions commute, so the polynomial operators
\[
             B_{\epsilon\eta}=(I+\epsilon J)(I+\eta L)/4,
                  \qquad \epsilon,\eta\in\{1,-1\},
\]
restrict to complementary bounded idempotents onto the four joint eigenspaces.
The \(J\)-plane at \(\epsilon\) is the graph column \(\binom{\epsilon s I_2}{I_2}\), and the \(L\)-plane at \(\eta\) is the image of \(C_\eta=T\binom{\eta t I_2}{I_2}\).
Each \(C_\eta\) has a bounded group-ring left inverse from the last two rows of \(T^{-1}\).
Consequently their intersection is \(C_\eta\ker(P(\eta t)-\epsilon sQ(\eta t))\), isomorphically.
The four sign characters of \(H\) give dimension \(1/2\) to every such intersection.
Their direct sum thus has dimension two, equal to the regular nullity over \(N\) by subgroup trace preservation.

If a nonzero group-ring column were killed by \(R\), one of its four polynomial components \(B_{\epsilon\eta}\) would give a nonzero group-ring column inside a half-dimensional module.
This contradicts scalar injectivity.
For a left syzygy, an invertible group translation reduces to the adjoint commutator, formed by \(J^*,L^*\).
Its two \((\epsilon,\eta)\)-planes are the orthogonal complements of the opposite planes for the original involutions, since each kernel at one sign is the range of the corresponding linear factor at the other sign.
Their intersection has dimension \(4-(2+2-1/2)=1/2\), using the closure of the sum of the opposite planes.
The same polynomial splitting excludes a nonzero polynomial column for the adjoint.
This proves both syzygy assertions.

## Recovering the fractional projection from an integral kernel

If \(E\in M_4(C_r^*(N))\), the bounded idempotent \(B_{\epsilon\eta}E\) belongs to \(M_4(C_r^*(H))\) and has range the corresponding joint eigenspace.
It is idempotent since that range is contained in \(E\) and \(B_{\epsilon\eta}\) is idempotent on \(E\).
The orthogonal range projection of a bounded idempotent in a unital \(C^*\)-algebra belongs to that algebra, by applying a spectral cut to the idempotent times its adjoint at its closed range.
The group-ring left inverse of \(C_\eta\) recovers the signed rectangle kernel from this closed subspace.
Its restriction is an isomorphism onto the kernel, with bounded inverse \(C_\eta\).
Hence the product of the left inverse and the joint range projection has closed range, and its orthogonal range projection is in \(M_2(C_r^*(H))\).

Conversely, if \(p\in M_2(C_r^*(H))\), all four signed kernel projections lie there by the sign automorphisms.
Applying \(C_\eta\) gives four closed-range maps since these columns are bounded below.
Their joint range projections \(P_{\epsilon\eta}\) belong to \(M_4(C_r^*(H))\).
Their sum of ranges is precisely \(E\)'s range and is closed: the maps \(B_{\epsilon\eta}\) give bounded coordinates there.
For example the row with the four orthogonal projections as blocks maps onto \(E\)'s range and has bounded right inverse on it given by stacking \(B_{\epsilon\eta}\) on this range.
Its range projection \(E\) therefore lies in \(M_4(C_r^*(H))\).
It already belongs to \(M_4(\mathcal N(N))\) by the kernel formula for \(R\).
The subgroup trace-preserving expectation takes reduced group-algebra polynomials to their coefficients in \(N\) and is norm contractive, so it takes \(C_r^*(H)\) into \(C_r^*(N)\).
It fixes \(E\), proving the converse.
In particular closed range for \(R\) is a sufficient condition for the original fractional projection to belong to the reduced algebra even when \(K\) has nonclosed range.

## Two compatible norms over the same subgroup

Assume every nonzero scalar in the first inverse layer of \(N\) is an affiliated unit.
A nonzero entry of \(R\) is an affiliated unit by scalar injectivity.
After row and column permutations use it as a pivot.
The residual three-square Schur matrix over the first layer has rank one by ordinary block elimination in the affiliated algebra.
At least one of its entries is nonzero.
If such an entry has fractional rank we obtain the first alternative.
Otherwise use an invertible entry as a second pivot.
All eliminations then use entries in the second inverse layer, and the remaining two-square block, of rank zero, is zero.
Solving these two row equations yields a four-by-two matrix \(Z\) over that layer with two identity coordinate rows, whose image is the kernel of \(R\).
The identity rows recover the parameters.
Column permutations in this calculation simply permute the original four coordinates back.
Equivalently it suffices for this construction that one invertible second pivot is available.

Since \(J,L\) preserve the kernel, the last two parameters of \(JZ,LZ\), read at the identity rows, determine the whole matrices.
The matrix \(J(s^{-1}I_4)\) has coefficients in \(\mathbb CN\), since its degree is the first binary basis vector before multiplication.
Likewise \(L(t^{-1}I_4)\) has coefficients in \(\mathbb CN\).
Conjugation by \(s,t\) preserves \(N\) and its inverse layers.
Thus
\[
               JZ=Z V_s(sI_2),\qquad LZ=Z V_t(tI_2)
\]
where \(V_s,V_t\) are obtained by reading the identity rows of \(J(s^{-1}I_4){}^s Z\) and \(L(t^{-1}I_4){}^t Z\).
Squaring these equations and reading the identity rows yields the two norm identities.
Each gives a right inverse in the same layer, necessarily the inverse in the finite affiliated matrix algebra.
Finally \(JLZ=LJZ\) gives \(V_s\,{}^s V_t(st I_2)=V_t\,{}^t V_s(ts I_2)\).
Multiplication on the right by \((ts)^{-1}I_2\) proves the compatibility with the actual commutator in \(N\).

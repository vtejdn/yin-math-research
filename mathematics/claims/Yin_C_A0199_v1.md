---
author: Yin
---

# A rank-one companion remainder and an odd-dimensional norm over the kernel group

## Statement

Let \(T\in M_l(A)\), where \(l\ge2\), \(A=\mathbb CH\), and every nonzero element of \(A\) is a unit of the regular affiliated algebra \(U(H)\).
Fix \(m\ge1\).
Suppose \(R=T^m-I_l\) has regular rank one and every eigenspace of \(T\) at an \(m\)-th root of unity has dimension strictly less than one, with the unnormalized matrix trace.
Then no nonzero group-ring column is killed by \(R\), and no nonzero group-ring row kills \(R\).
Every entry of \(R\) is nonzero.
Its entries in each row freely generate a complex associative algebra and are right-linearly independent over \(A\); those in each column freely generate an algebra and are left-linearly independent over \(A\).

Choose a column \(v\) and a row \(r\) of \(R\) meeting at \(a\).
The action \(Tv=v c\) on the remainder image has \(c\) transcendental over \(\mathbb C\), with every nonzero polynomial in \(c\) an affiliated unit.
The scalar \(\ell=rv\in A\) is nonzero.
There is a projection in the algebraic sense with image \(R U(H)^l\) along \(\ker R\), namely \(p=v\ell^{-1}r\).
The spectral idempotents of \(T\) on \(\ker R\), extended by zero on \(pU(H)^l\), all have formulas over the first actual scalar inverse layer using just the same denominator \(\ell\).

In particular let \(H=\langle s,t\rangle\) be torsion-free with the stated scalar hypothesis and a cyclic quotient of order 26.
If a four-site matrix \(B_0+At-s(D+Ct)\) with constant two-by-two coefficients has rank \(3/2\), one can choose a quotient \(\chi:H\to C_{26}\) with the same kernel as the given one and a fourteen-dimensional companion as below.
Write \(N=\ker\chi\), \(J=\ker(\chi\bmod 13)\), choose \(g\in H\) with \(\chi(g)=13\), and put \(\alpha=\operatorname{Ad}_g\) on \(U(N)\).
The rank-one remainder can be expressed over \(\mathbb CN\), and the two matrices \(L-I_{14},L+I_{14}\) over \(\mathbb CJ\) then have regular nullity \(13/2\) each and product equal to this remainder.
There is an actual
\[
                  V\in{\rm GL}_{13}(D_1(N)),\qquad
                          V\alpha(V)=g^{-2}I_{13}.
\]
Consequently an integer rank theorem for these two matrices on the odd-index subgroup \(J\), or a valid obstruction to this specific odd-dimensional norm over \(D_1(N)\), excludes the four-site input.
All groups used here are subgroups of the original group.
The construction imposes the norm and does not by itself exclude a solution.

## Syzygies and the single denominator

Put \(U=U(H)\).
On \(\ker R\) the interpolation polynomials \(E_\omega=m^{-1}\sum_{j=0}^{m-1}\omega^{-j}T^j\) for \(\omega^m=1\) separate the right eigenspaces and sum to the identity there.
For a nonzero \(w\in A^l\) with \(Rw=0\), some \(E_\omega w\) would be a nonzero polynomial column in the corresponding eigenspace.
Such a column has image of dimension one because a nonzero coordinate is an affiliated unit.
This contradicts the assumed eigenspace bound.
For \(T^*\) the bound also holds at the conjugate roots, by polar decomposition of the square matrices \(T-\omega I_l\).
Taking adjoints therefore excludes nonzero polynomial left syzygies of \(R\).

In particular every row and column of \(R\) is nonzero.
Any one row \(r\) has rank one, so \(\ker R=\ker r\): inclusion and equality of trace dimensions give equality of their kernel projections.
Similarly the left kernel of any column equals the left kernel of \(R\).
It follows that each row is right-linearly independent over \(A\) and each column is left-linearly independent over \(A\), proving in particular that every entry is nonzero.
The [augmentation and initial-letter argument](Yin_C_A0113_v1.md#the-two-by-two-schur-complement) works with all \(l\) entries.
Indeed \(r A^l\) is a proper right ideal; otherwise injectivity yields \(A^l\simeq A\), incompatible with augmentation for \(l\ge2\).
The constant term of any polynomial relation in the entries must therefore vanish.
Grouping its remaining monomials by their first letter and using right independence gives relations of smaller degree, proving algebraic freeness by induction.
The last-letter argument proves the column assertion.
For a finite nonempty \(Y\subset H\), if \(S_r\) is the union of the supports in a row and \(S_v\) the union for a column, independence on finite coefficient spaces gives \(|S_r Y|\ge l|Y|\) and \(|Y S_v|\ge l|Y|\).
In particular two entries of a single row cannot have a common nonzero right multiple, and columns give the left-handed test.

For the chosen \(v,r\), the unit entry \(a=v_i\) identifies the rank-one range of \(R\) with \(vU\), since the latter is contained in that range and has the same dimension.
Reading coordinate \(i\) gives \(R=v a^{-1}r\).
The ranges here are affiliated modules, equal to their support modules by the relative inverse.
Since \(T\) commutes with \(R\), it acts on this range by \(Tv=v c\), with \(c=a^{-1}(Tv)_i\).
For any scalar \(\lambda\), the expression \(c-\lambda\) is \(a^{-1}\) times a polynomial group-ring entry, so it is zero or a unit.
If \(c=\lambda\) and \(\lambda^m=1\), the whole range \(vU\) would be in a forbidden eigenspace.
If \(c=\lambda\) and \(\lambda^m\ne1\), then \(R^2=(\lambda^m-1)R\) and \(I_l-(\lambda^m-1)^{-1}R\) is a nonzero group-ring idempotent with range in \(\ker R\), contradicting the absence of polynomial kernel columns.
Thus every \(c-\lambda\) is a unit, giving the transcendence and the embedded field \(\mathbb C(c)\).

Now \(Rv=v(c^m-1)=v a^{-1}rv\), so \(\ell=rv=a(c^m-1)\ne0\).
Consequently \(p=v\ell^{-1}r\) is an idempotent with image \(vU\) and kernel \(\ker r=\ker R\).
Both summands are invariant under \(T\), hence \(p\) commutes with \(T\).
The required idempotents on the full module are \(E_\omega(I_l-p)\).
For any chosen entry \(a=r_j\) the right ideals \(\ell A\) and \(aA\) have zero intersection: an equality \(\ell d= a e\) gives \(\sum_k r_k(v_kd-\delta_{kj}e)=0\), and at least one nonzero \(v_k\) has \(k\ne j\).
Right independence and scalar injectivity force \(d=e=0\).
In particular \(c^m\) cannot commute with \(a\), since otherwise the two nonzero scalars \(\ell\) and \(a\) would commute.
Rectangular rows of analytic rank one can themselves admit no polynomial kernel: \((x_1-1,\ldots,x_l-1)\) in the free group ring has this property since the boundary of a finite nonzero edge chain in the free Cayley tree cannot vanish.
Thus rank one alone does not contradict these independence tests.

## The two extreme coefficients at order 26

Assume the four-site rank is \(3/2\).
The [short-lift bound](Yin_C_A0197_v1.md#short-marked-lifts) and the [finite-phase deficit bound](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter) force a shortest lift of width exactly seven: the first bounds it by \(\lfloor\sqrt{52}\rfloor=7\) and the second excludes width at most six.
A shortest axial lift of length seven is impossible because the axial period divides 26.
Thus the weights \((a,b)\) are both nonzero, with \(|a|+|b|=7\), and are relatively prime.
Their multiple of the marked character modulo 26 has order 26 since its two residues generate \(C_{26}\).
Use this quotient generator to define \(\chi(s)=a,\ \chi(t)=b\bmod26\).

Shift the rectangle deformation \(B_0+z^bAt-z^as(D+z^bCt)\) by \(z^{-\mu}\), where \(\mu=\min(0,a,b,a+b)\).
The polynomial \(Q(z)=\sum_{j=0}^7Q_j z^j\) has maximum rank two and deficit \(1/2\) at each of the 26 roots by the same finite-phase result.
The [polynomial inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) on the projective line also counts both extreme coefficients as the evaluations at zero and infinity.
Indeed homogenize to degree seven and make an invertible linear change of the two scalar variables sending a point outside the finite set of evaluations to the new infinity.
Dehomogenization is a polynomial of degree at most seven with the same maximum rank, since the old generic maximum holds off a countable set.
The ranks at the specified projective points are unchanged up to nonzero scalar factors.
Their total deficit is at most fourteen.
The 26 roots already contribute thirteen, so \(Q_0,Q_7\) cannot both have rank at most one.
Both endpoints are single group elements times constant matrices, since \(ab\ne0\).
Thus at least one endpoint is invertible over \(\mathbb CH\).
Use the reversal \(z^7Q(1/z)\) and replace \(\chi\) by \(-\chi\) if required so the leading coefficient is invertible over the group ring.
Reversal preserves the root nullities and changes the additive constant in the grading of the coefficients.

The usual monic block companion \(T\) of \(Q_7^{-1}Q(z)\) has two-dimensional blocks, identity superdiagonal, and last row blocks \(-Q_7^{-1}Q_j\) for \(0\le j<7\).
As in the [companion calculation](Yin_C_A0197_v1.md#the-companion-and-a-column-over-the-original-group-ring), each root eigenspace is identified by its first block with the corresponding polynomial kernel and has dimension \(1/2\).
Their direct sum equals \(\ker(T^{26}-I)\) by interpolation.
The dimension of this kernel is thirteen, so \(T^{26}-I\) has rank one.

## Subgroup coordinates and the odd-dimensional norm

In the chosen orientation every nonzero group element in \(Q_j\) has the same \(\chi\)-degree \(j+\beta\) for a fixed \(\beta\bmod26\); initially \(\beta=\mu\), and after reversal it is \(-7-\mu\) for the negative character.
The nonzero monic coefficient blocks thus have degree \(j-7\), with the inverse of the single-site leading coefficient of opposite degree to that coefficient.
The \((i,j)\) block of the companion has degree \(-1-i+j\), with \(0\le i,j<7\).
Choose \(h_i\in H\) with \(\chi(h_i)=i\), and conjugate by the diagonal with blocks \(h_i I_2\) on the left and \(h_i^{-1}I_2\) on the right.
The resulting matrix \(T'\) is entrywise homogeneous of degree \(-1\).
Hence \(R'=T'^{26}-I\in M_{14}(\mathbb CN)\), and all its nonzero entries remain scalar affiliated units.
The preceding independence, support and one-denominator formula for its range projection hold already for the chosen coefficients \(v,r,\ell\) over \(N\) and their affiliated images there by coset replication.
The group element \(g\) of degree 13 has \(g^2\in N\) and normalizes \(N\).

Put \(L=T'^{13}\), a matrix over \(\mathbb CJ\) with entries of degree 13.
The kernels of \(L-I\) and \(L+I\) are the sums of the thirteen eigenspaces of \(T'\) for the roots of \(z^{13}-1\) and \(z^{13}+1\), respectively.
Both have dimension \(13/2\) over \(H\) and hence over \(J\), while \((L-I)(L+I)=R'\).

Choose a row \((a_0,r')\) of \(R'\), where \(a_0\ne0\).
A basis for its affiliated kernel, also the kernel of \(R'\), is the matrix of columns
\[
                 Z=\binom{-a_0^{-1}r'}{I_{13}} .
\]
These entries lie in \(D_1(N)\) and the bottom thirteen coordinates recover the parameter vector uniquely.
Write \(L=L_0(gI_{14})\) with \(L_0\in M_{14}(\mathbb CN)\).
The matrix \(L\) maps this kernel to itself because it commutes with \(R'\), and \(L^2\) acts as the identity there.
Consequently
\[
                LZ=Z V(g I_{13}),
\]
where \(V\) consists precisely of the bottom thirteen rows of \(L_0\alpha(Z)\), with \(\alpha\) applied entrywise.
This gives \(V\in M_{13}(D_1(N))\).
Squaring the displayed relation on the invariant module gives \(Z=Z V\alpha(V)(g^2 I_{13})\), proving the claimed norm.
It also gives the right inverse \(\alpha(V)(g^2I_{13})\) over this layer.
The square matrix \(V\) is therefore invertible in the finite affiliated algebra, and its unique inverse belongs to the same first layer.
This locates the obstruction on \(N\) without requiring its division closure to be a skew field.

## Assessment history

### Decision rank-one-remainder-and-the-odd-dimensional-norm

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite support, the shared inverse and the norm over the index-26 kernel. |
| argument | [Syzygies and the single denominator](#syzygies-and-the-single-denominator) | Left and right equations, algebraic freeness and the commuting projection. |
| argument | [The two extreme coefficients at order 26](#the-two-extreme-coefficients-at-order-26) | A primitive nonaxial lift and an invertible group-ring endpoint. |
| argument | [Subgroup coordinates and the odd-dimensional norm](#subgroup-coordinates-and-the-odd-dimensional-norm) | The actual subgroup matrices and the first scalar inverse layer. |
| review | [Rank-one remainder and the odd-dimensional norm](../audits/reviews/Yin_R_A0185_v1.md#rank-one-remainder-and-the-odd-dimensional-norm) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-rank-one-remainder-and-the-odd-dimensional-norm)

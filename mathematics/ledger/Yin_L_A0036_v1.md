---
author: Yin
---
# Joint Fourier overlap for the two factors of a putative zero product

Let \(a,b\ne0\) in the complex group ring of a torsion-free discrete group, and suppose \(ab=0\).
Let \(p,q\) be the range projections of left convolution by \(a^*,b\), of traces \(u,v\).
Then \(pq=0\).
Cover \(\operatorname{supp}a^*\) and \(\operatorname{supp}b\) by their respective occupied left cosets of infinite cyclic subgroups, with counts \(k,l\) and set stabilizers \(L_1,L_2\) as in the [cyclic-coset bound](../claims/Yin_C_A0019_v1.md#statement).
The first cover here is of the adjoint support because the two ranges must lie in orthogonal subspaces.
Write \(J=L_1\cap L_2\), and write \(E_H\) for the trace-preserving conditional expectation onto the group von Neumann algebra of a subgroup \(H\).

## The overlap inequality

The Fourier projections \(E_{L_1}\) and \(E_{L_2}\) commute on \(L^2\) and have product \(E_J\), since they restrict the coefficient sequence to the indicated subgroups.
Consequently
\[
\tau(E_Jp\,E_Jq)
\le \sqrt{(ku-1)v(1-v)}+\sqrt{(lv-1)u(1-u)}. \tag{1}
\]
Indeed \(\langle p,q\rangle=0\), while \(\langle E_{L_1}p,E_{L_2}q\rangle=\langle E_Jp,E_Jq\rangle\).
Their difference is the sum of \(\langle p-E_{L_1}p,q\rangle\) and \(\langle E_{L_1}p,q-E_{L_2}q\rangle\).
In the first inner product subtract \(v1\) from the second argument, and in the second subtract \(u1\) from the first.
Cauchy–Schwarz, the contraction property of conditional expectation and the [two leakage estimates](../claims/Yin_C_A0019_v1.md#compression-to-the-occupied-cosets) give (1).

If \(J\) is trivial the left side is \(uv\).
Since \(u\ge1/k,\ v\ge1/l\) and \(x(1-x)\le1/4\), a necessary condition for a zero product is
\[
        (ku-1)+(lv-1)\ \ge\ 2u^2v^2\ \ge\ \frac{2}{k^2l^2}. \tag{2}
\]
This positive separation from the two simultaneous endpoints is uniform in the sizes of the supports.
For two and three cosets with both stabilizers trivial, the individual [trivial-stabilizer bounds](../claims/Yin_C_A0019_v1.md#statement) already exclude a zero product, since \((\sqrt5-1)/2+(\sqrt2-1)>1\).
That last consequence only uses the individual ranks and also works with the left support of \(a\) in place of the left support of \(a^*\).

## Nontrivial intersection and the remaining gap

For infinite \(J\), the stabilizer theorem makes \(J\) infinite cyclic.
Normalize \(z=a^*/\|a^*\|_1\) and \(w=b/\|b\|_1\), and regard them as left convolution operators of norm at most one.
Then \(p\ge zz^*,\ q\ge ww^*\).
Decompose \(z=\sum_t f_t t\) along right cosets \(Jt\); taking \(E_J(zz^*)\) gives precisely \(\sum_t |f_t|^2\) on the Fourier circle because cross-coset products have no coefficient in \(J\).
The analogous expression for \(w\) gives a lower function for \(E_Jq\).
Each sum has a nonzero Laurent polynomial summand and is positive almost everywhere, so the left side of (1) is strictly positive.
For explicit support bounds, if \(z,w\) have respectively \(s,h\) terms, choose one coset in each decomposition carrying a coefficient of modulus at least \(1/s,1/h\).
Put \(c_j=(2j)^{-1}(1/8)^{2^{j-1}-1}\).
The [circle estimate](../claims/Yin_C_A0019_v1.md#a-coefficient-independent-estimate-on-the-circle) with exceptional measure \(1/4\) shows that the two chosen moduli exceed \(c_s,c_h\) simultaneously on a set of measure at least \(1/2\).
Thus the left side of (1) is at least \(c_s^2c_h^2/2\).

For larger counts these restrictions still permit complementary fractional ranks.
For instance the numerical constraints \(k=l=4,\ u=v=1/2\) satisfy (1) when \(J\) is trivial, (2), \(u+v\le1\), and the individual trivial-stabilizer bounds.
These numbers test the estimates only.
A proof for arbitrary finite supports would require additional restrictions on the Fourier coefficients or the convolution equations themselves.

---
author: Yin
---

# Small positive Schur defects and an exact exchange in one scalar-injective representation

## Statement

Let \(\Gamma=F_3*\mathbb Z^2\), with \(t,v\) the commuting generators of \(\mathbb Z^2\).
There is a faithful unitary representation of this torsion-free group in a finite tracial von Neumann algebra in which every nonzero element of \(\mathbb C\Gamma\) is injective.
A single two-by-two matrix over the distinguished \(\mathbb CF_3\) has an affiliated-unit first pivot and a Schur complement \(S\) with kernel projection \(P\) of trace \(1/2\).
Put \(d(h)=\tfrac12-\operatorname{rk}((1-P)hP)\) for the represented trace.
With \(h_m=t^{-m}(1+t)^{2m}\), this representation satisfies
\[
 2^{-(2m+1)}\le d(h_m)\le\frac{1}{2\sqrt{m+1}}\quad(m\ge1),
 \qquad vPv^{-1}=1-P,\qquad d(v)=0 .
\]
The second scalar inverse layer of the represented \(\mathbb C\Gamma\) contains matrix units for a unital copy of \(M_2(\mathbb C)\) with first diagonal unit \(P\).
In particular its unit class is twice the class of \(P\) in algebraic \(K_0\).
The representing trace differs from the regular trace.

On restriction to \(F_3*\langle t\rangle\), every finite-support \(h\) has \(d(h)>0\), while the same fixed matrix and the same sequence \(h_m\) retain the displayed bounds.

## The representation and its group-ring scalars

Let \(\Omega=\{0,1\}^{\mathbb Z}\) with independent fair bits \(\omega_i\).
For each \(k=(i,j)\in\mathbb Z^2\) take five standard semicircular elements \(s_k,r_k,z_{k,1},z_{k,2},z_{k,3}\), freely independent across all labels.
Write \(M_0\) for their tracial von Neumann algebra and \(M=L^\infty(\Omega)\,\overline\otimes\,M_0\) with its product trace.
Let \(t\) shift the coordinate functions by \(\omega_i\mapsto\omega_{i+1}\), and let \(v\) act on them by \(\omega_i\mapsto1-\omega_i\).
On the free semicircular family \(t\) and \(v\) translate the site indices by \((1,0)\) and \((0,1)\) respectively.
Write \(t,v\) also for the canonical implementing unitaries in the tracial crossed product of \(M\) by these commuting trace-preserving automorphisms.

At site \(k=(i,j)\) set \(\varepsilon_k=\omega_i\) for even \(j\) and \(\varepsilon_k=1-\omega_i\) for odd \(j\).
Choose \(X_k=(r_k^2,r_ks_kr_k,r_ks_k^2r_k)\) on \(\varepsilon_k=1\) and \(X_k=(z_{k,1},z_{k,2},z_{k,3})\) on its complement.
These are bounded self-adjoint triples in \(M\), carried into successive sites by conjugation with \(t,v\).
Represent the three generators of the distinguished \(F_3\) by the Cayley unitaries \(\phi(X_{(0,0),l})\), where \(\phi(x)=(1+ix)(1-ix)^{-1}\), and use the stated implementing unitaries for the other factor.
Reduced group words identify the kernel of \(\Gamma\to\mathbb Z^2\) with the free product of all the \(\mathbb Z^2\)-translates of this \(F_3\).
Indeed conjugated nonidentity syllables with different successive indices have nonidentity \(\mathbb Z^2\)-syllables between them after expansion in \(F_3*\mathbb Z^2\), and moving all quotient syllables to the right gives the converse generation.
Thus \(\Gamma\) is the semidirect product of this base free group by the indicated translations.

Fix a nonzero element of the complex group ring of the base group.
It uses only a finite set of sites.
For each of their possible bit patterns its evaluation is a rational expression in one finite free semicircular family, in the [realized free skew field](../audits/literature/MSY23/Yin_U004.md#theorem-56-exact-equivalences) of that family.
The formal expansion of the element under the Cayley substitution in distinct indeterminates for all site generators is nonzero by the [maximal syllable argument](Yin_C_A0126_v1.md#cayley-generators-and-scalar-injectivity).
That argument uses only finitely many syllables and applies to every finite number of free generators.
In each pattern the variables at all sites are jointly algebraically free because the three words \(r_k s_k^l r_k\), \(l=0,1,2\), are uniquely decodable, the \(z\) variables are single letters, and different sites use disjoint alphabets.
The free field has the automorphism scaling \(r_k\) by \(\lambda\) at sites using the first triple and every \(z_{k,l}\) by \(\lambda^2\) at sites using the second triple, for nonzero real \(\lambda\).
It scales all the chosen variables by \(\lambda^2\).
For sufficiently small \(\lambda\) the Cayley expressions and their inverses admit norm-convergent expansions, whose first nonzero homogeneous coefficient survives by joint algebraic freeness.
Consequently the element is nonzero in this field and is an affiliated unit for every occurring pattern.
The finite partition by the chosen bits gives an affiliated inverse in the base algebra.

Every nonzero element of \(\mathbb C\Gamma\) now has a nonempty group-algebra Fourier sum \(\sum_{k\in E} b_k u_k\) over a finite set of indices in \(\mathbb Z^2\), with \(u_{(i,j)}=t^iv^j\) and all \(b_k\) nonzero base elements.
Choose an integer linear form \(\ell\) separating \(E\), and let \(k_0\) uniquely minimize it.
The bounded operator polynomial \(\sum_k z^{\ell(k)-\ell(k_0)} b_k u_k\) has an affiliated-unit constant coefficient.
By the [one-parameter polynomial rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) its rank is one outside a countable set.
For \(|z|=1\) the crossed-product gauge automorphism multiplies \(u_k\) by \(z^{\ell(k)}\) while fixing the base algebra, so all those ranks agree, including at \(z=1\).
This proves scalar injectivity on the whole group ring and faithfulness of the representation.
Its distinguished first generator has trace with positive imaginary part by the [one-site trace calculation](Yin_C_A0126_v1.md#cayley-generators-and-scalar-injectivity), whereas its regular trace is zero.

## The two behaviors of the fixed Schur kernel

Use the [Cayley group-ring matrix](Yin_C_A0126_v1.md#a-matrix-over-the-group-ring-and-its-half-kernel) on the original three generators.
Its pivot is a unit in the affiliated algebra.
Its Schur complement is zero on the first kind of site and an affiliated unit on the other kind, so the original kernel projection is precisely \(P=\omega_0\).
Its translates \(t^iPt^{-i}=\omega_i\) are independent fair bits, and the crossed-product trace vanishes on each nonzero translation power multiplied by a bounded bit function.
Consequently the algebra of the bits and \(t\) has exactly the [Bernoulli representation used for the shift polynomials](Yin_C_A0127_v1.md#the-bernoulli-representation-of-the-translated-projections).
Its [positive minors](Yin_C_A0127_v1.md#positive-minors-of-the-shift-polynomial) and [finite-block rank bound](Yin_C_A0127_v1.md#from-finite-blocks-to-the-trace-rank) give the stated upper and lower bounds on \(d(h_m)\).

For the subgroup generated by the distinguished \(F_3\) and \(t\), any group element conjugates \(P\) to one of the bits \(\omega_i\), since the base coefficients commute with all bits.
For each finitely supported \(h\), the intersection of \(P\) and \(g^{-1}Pg\) over \(g\in\operatorname{supp}h\) has strictly positive trace by independence of the finitely many distinct bits involved.
This intersection is annihilated by \((1-P)hP\).
In the full group the unitary \(v\) exchanges \(P\) and \(1-P\), so \((1-P)vP=vP\) has initial support \(P\).

For the scalar inverse layers starting at the represented group ring, \(x=S^*S\) belongs to \(D_1\).
The positive operators \(x\) and \(y=v^*xv\) have complementary supports \(1-P\) and \(P\).
Hence \(x+y\) is an affiliated unit and \(y(x+y)^{-1}=P\in D_2\).
The four elements \(P,1-P,vP,Pv^{-1}\) are matrix units in the order \(e_{11},e_{22},e_{21},e_{12}\).
The two projective summands of the unit are consequently isomorphic over \(D_2\), giving \([1]=2[P]\).
The half-kernel comparison uses a nonregular trace on the stated torsion-free group and leaves the [regular-trace question](../tasks/Yin_T_A0001_v1.md#contract) open.

## Assessment history

### Decision comparison-with-a-nonregular-trace

| Field | Value |
| --- | --- |
| date | 2026-11-23T07:16 |
| status | proved |
| reason | Independent inspection verified the complete statement, its arguments and the stated limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar injectivity of the whole represented group ring and both behaviors for one matrix. |
| argument | [The representation](#the-representation-and-its-group-ring-scalars) | Semidirect normal form, joint free-field argument and gauge rank. |
| argument | [Fixed Schur kernel](#the-two-behaviors-of-the-fixed-schur-kernel) | Bernoulli estimates, the flip and complementary projective modules. |
| review | [Independent finding](../audits/reviews/Yin_R_A0164_v1.md#comparison-with-a-nonregular-trace) | Whole argument at the stated scope. |

## Current assessment

[Selected decision](#decision-comparison-with-a-nonregular-trace)

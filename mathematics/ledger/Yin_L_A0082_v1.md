---
author: Yin
---

# Complex Atiyah integrality for the lifted triangle examples

This comparison for Yin on 26 November 2026 applies Linnell's theorem to the perfect groups in the two-generator phase estimate.

## The surface subgroup and its central extension

For \(r=12n+11\), \(n\geq0\), write \(H_r=\langle s,t\rangle\) for the [perfect marking](../claims/Yin_C_A0194_v1.md#an-explicit-perfect-marking) in the full lift of the hyperbolic triangle group \(\Delta=\Sigma(2,3,r)\).
Projection to \(\Delta\) restricts to a surjection \(\pi:H_r\to\Delta\), since \(s,t\) project to the first two vertex rotations and the third is the inverse of their product.
Its kernel \(C_r=H_r\cap\langle c_0\rangle\) is infinite cyclic and central, since the full covering kernel is \(\langle c_0\rangle\cong\mathbb Z\) and \(s^2=c_0^{\,r-6}\ne e\). [Mil75, Lemma 3.1](../audits/literature/Mil75/Yin_U001.md#lifted-triangle-presentation)

The triangle group is a finitely generated linear group in characteristic zero, via the faithful adjoint representation of \({\rm PSL}_2(\mathbb R)\).
Selberg's lemma and passage to the normal core give a torsion-free normal subgroup \(\Delta_0\) of finite index.
Fox's theorem gives this subgroup directly for triangle groups.
The free cocompact action of \(\Delta_0\) on the hyperbolic plane identifies it with the fundamental group of a closed orientable surface of genus at least two. [Mil75, Theorem 2.7 and its consequences, pp. 183–184](../literature/pdf/Mil75.pdf#page=9)

Choose a surjection \(\eta:\Delta_0\to\mathbb Z\) using the surface abelianization.
The infinite cyclic cover corresponding to \(F=\ker\eta\) is a noncompact surface, so \(F\) is a free group. [Mil75, p. 184](../literature/pdf/Mil75.pdf#page=10)
Write \(P=\pi^{-1}(\Delta_0)\) and \(K=\pi^{-1}(F)\).
Lifting a free basis of \(F\) defines a section of \(K\to F\), and centrality of \(C_r\) makes \(K\cong F\times C_r\).
Linnell's class \(\mathcal C\) contains free groups and is closed under extension by elementary amenable quotients.
Thus \(K\) belongs to \(\mathcal C\) by projection onto its infinite cyclic factor.
Next \(P/K\cong\mathbb Z\) and \(H_r/P\cong\Delta/\Delta_0\) is finite, so successively \(P,H_r\in\mathcal C\). [Lin93, Theorem 1.5 and the definition of the class](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems)

Since \(H_r\) is torsion-free, Linnell's theorem gives integral regular kernel dimension for every finite rectangular matrix over \(\mathbb C H_r\), with the unnormalized matrix trace.
The closure of the range has integer dimension by rank-nullity. [Complex-coefficient theorem and rank convention](Yin_L_A0001_v1.md#known-positive-results)

## What the phases give on other marked groups

The [two-generator estimate](../claims/Yin_C_A0194_v1.md#statement) applies to a rectangle \(B+At-s(D+Ct)\) with complex \(h\)-by-\(h\) coefficients when \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) is invertible.
The [exact count](../claims/Yin_C_A0195_v1.md#finite-relators-and-the-exact-count) is \(8(n+1)\) phases for the specified spectra on \(H_r\).
Consequently its nullity is at most \(h/(8(n+1))\) by the representation argument alone.
On \(H_r\) the known all-matrix theorem further makes this nullity integral, so every such rectangle has full rank when \(h<8(n+1)\).

For any marked group \(H\) surjecting onto \((H_r,s,t)\) with generators respected, composing the quotient map with the displayed representations of \(H_r\) supplies the same \(8(n+1)\) phases on \(H\).
More generally it suffices that \(H\) realize those generator spectra and at least that many phases.
The unnormalized regular nullity on \(H\) then satisfies the same numerical bound by applying the phase argument directly to \(H\).
This implication needs no integrality theorem for \(H\), no scalar injectivity hypothesis and no identification of a regular representation with that of a quotient.
The all-matrix question for an arbitrary torsion-free \(H\) remains the [original contract](../tasks/Yin_T_A0001_v1.md#contract).

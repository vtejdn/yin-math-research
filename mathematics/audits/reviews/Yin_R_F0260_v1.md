---
author: Yin
---

# Independent review of the rectangular liberation cuts in the correlated Haar pair

An independent agent for Yin examined the entire [candidate decision dated 2026-11-14T11:28](../../claims/Yin_C_F0251_v1.md#decision-candidate) and the direct mathematical inputs identified below.
The reviewer did not participate in developing this candidate and received its fixed locator and scope without development dialogue, exploration notes, author explanations or previous findings on it.

## Finding

At 2026-11-14T11:30 UTC the reviewer found that all three assertions hold, including the exact joint vacuum measure, both ordered slice formulas, their asymptotic growth and the sign and coefficient in the diagonal energy estimate.
The finding supports acceptance of the full candidate for \(0<r<1\), arbitrary base spectral projections \(e,f\) and the specified words \(p_n=V^n\), \(n\ge1\).

The reference pair is a free pair with \(\tau(V^j)=r^{|j|}\).
The bounded duals for the correlated pair have full Hilbert adjoint domains and can be negated to match the generator-first convention of the normal vacuum corollary.
The identities \(V=X_1X_2\) and \(X_2=U^*V\) identify the represented starred core with the free Laurent core, so computations on that core apply to the claimed inputs.
On the \(V\) factor, the \(n\) positive cuts of \(L(V^n)\) and the inverse-rule negative cuts give \((\tau\otimes\tau)L(V^j)=j r^{|j|}\) for all integers \(j\).
Integration by parts with the inner product linear in the second variable gives \(H=-i(w_r'/w_r)(V)\).
Its centered free extension represents the vacuum on the entire core because a centered reduced word of length at least two leaves a centered neighboring factor on one of the trace legs at every cut.
The same calculation gives zero vacuum for the reference liberation.
The circle change of variables has argument derivative \(w_r\), hence sends \(w_r\,dm\) to Haar measure and gives \(\|H\|_2^2=2r^2/(1-r^2)^2\).

On \(V\) the correlated derivation equals \(U\otimes U^*V-1\otimes V\), and the inverse rule determines its value on \(V^*\).
Trace cyclicity moves the insertion in the double trace of \(L\) to conjugation of the polynomial by \(U\), giving the actual vacuum \(U^*HU-H\).
For \(a,b,c,d\in N\), freeness gives \(\langle aHb,cHd\rangle=\|H\|_2^2\tau(a^*c)\tau(b^*d)\).
In this joint spectral representation the vacuum has coefficient \(\bar z w-1\), proving (1) and the compression formula \(\|e\eta f\|_2^2=\|H\|_2^2\int_{e\times f}|z-w|^2\,dm(z)dm(w)\), including overlaps.

For the cut with prefix \(V^k\) the two second-leg traces are \(\bar\lambda_f r^{n-k}\) and \(s r^{n-k}\).
Keeping the resulting \(V^k\) on the left of \(e(U\bar\lambda_f-s)\) yields (2) in the stated order, and exchanging the two projections gives the reverse cut.
Freeness splits its squared norm into the two claimed factors.
The number of ordered pairs \((\ell,m)\) with \(1\le\ell,m\le n\) and \(\max(\ell,m)=j\) is \(2j-1\).
Summing their weights \(r^{2j}\) gives the limiting squared norm \(r^2(1+r^2)/(1-r^2)^2\) for \(P_{r,n}\).
This is at most \(\|H\|_2^2\), so Cauchy–Schwarz on the \(f\) integration gives precisely the prefactor \(\sqrt{s}\) in (3).
The exchanged estimate has prefactor \(\sqrt{t}\).
For fixed nonzero \(e,f\), strict inequality \(|\lambda_f|<s\) gives a positive \(r\)-independent norm for the first marginal factor, and likewise for the reversed cut.
Thus the supremum over \(n\) of each norm is proportional to \((1-r)^{-1}\) as stated.

For \(k=e\) or \(f\) the two factors in the pairing with \(p_n\) are \(S_n\) and \(|\lambda_k|^2-\tau(k)^2\), giving (4).
The same integer \(n\) works for both negative forms since \(S_n\uparrow r^2/(1-r^2)\).
For nonzero projections write \(\alpha=\lambda_e/t,\ \beta=\lambda_f/s\) and \(J=2ts(1-\operatorname{Re}(\alpha\bar\beta))\).
The difference \(2(1-\operatorname{Re}(\alpha\bar\beta))-(1-|\alpha|^2)=1-|\beta|^2+|\alpha-\beta|^2\) is nonnegative.
Adding the two weighted estimates gives \(-s q_e-t q_f\le(s+t)S_n J\).
Inserting the above bound on \(S_n\) and the exact compression gives the coefficient \((s+t)(1-r^2)/2\) in (5).
The zero-projection cases vanish, and this inequality uses no disjointness.
For disjoint projections the composition square is \(s e\otimes e+t f\otimes f\).
Equations (B0c) and (B0d) of the finite-kernel input give its energy term \(-\operatorname{Im}\langle p_n,i(sG_{ee}+tG_{ff})p_n\rangle=-s q_e-t q_f\), since \(p_n\) is an actual polynomial unitary.
This checks the interpretation of (5) on the stated family of words.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0251_v1.md#decision-candidate) | Whole fixed candidate in the indicated correlated Poisson–Haar family. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0251_v1.md#statement) | Exact vacuum measure, both ordered outputs, norm bounds and growth, negative diagonal forms, overlap and disjoint energy scopes. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0251_v1.md#argument) | Actual free-coordinate vacuum, compressed measure, cut and moment summations, both projection estimates and their limits. |
| [Finding](#finding) | [Free reference laws](../../claims/Yin_C_F0057_v1.md#2-a-free-reference-pair-with-bounded-duals) | Haar base, bounded positive Poisson density, moments for all integer powers and free reference pair. |
| [Finding](#finding) | [Correlated Haar coordinates](../../claims/Yin_C_F0057_v1.md#3-correlated-haar-coordinates-retain-bounded-duals) | Haar marginal of \(U^*V\), equality of generated cores and bounded dual system for the changed coordinates. |
| [Finding](#finding) | [Actual normal ACSY](../../claims/Yin_C_F0070_v1.md#statement) | Parts A and C with the signs of the bounded duals adjusted, including their actual adjoints at the vacuum. |
| [Finding](#finding) | [Finite-kernel energy](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | The composition-square term in (B0c) enters (B0d) with a minus sign on the actual core unitaries \(V^n\). |

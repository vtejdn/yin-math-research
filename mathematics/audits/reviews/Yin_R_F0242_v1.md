---
author: Yin
---
# Independent review of singular-projection packing with local spectral approximations

## Whole-proof finding

At 2026-11-13T17:29 UTC the reviewer independently examined both parts of the [statement](../../claims/Yin_C_F0233_v1.md#statement) and the complete [argument](../../claims/Yin_C_F0233_v1.md#argument) fixed at the [candidate decision](../../claims/Yin_C_F0233_v1.md#decision-candidate) of 2026-11-13T17:28.
The reviewer had used the singular-projection obstruction and examined other mass bounds for omitted shifts in separate work.
The reviewer did not participate in the development of the present weighted marginal bound or spectral partition proof and consulted no exploration draft, development discussion or earlier finding for this candidate.
Both parts hold with the stated \(K\), the same choice of marginal density for every application, and the stated approximation and commutator terms.

**From the marginal to a single normal density.**
C_F0076, Part 1, gives diffuseness and the starred generator derivative in the marginal coarse space.
The represented scalar star polynomials therefore have derivatives in that space by Leibniz, and the Hilbert projection of the original vacuum to \(L^2(B)\) gives their actual adjoint identity against \(1\otimes1\).
This proves precisely the one-coordinate hypothesis required by C_F0208.
Starting from this marginal algebra, adjoining its two freely independent Haar factors gives a freely independent three-coordinate normal tuple with the original marginal vacuum \(\zeta\).
C_F0162, Part B, applies to this enlarged tuple.
In particular (S5) gives \(3\|\zeta\|_2\) as the core operator-norm-to-Hilbert bound, and (S6) gives the generator commutators on bounded inputs with the appropriate change of sign for the operator-first convention.
For clarity, the same norm bound on the full bounded inputs follows by approximating each bounded \(a\) in \(L^2\) by star-core elements of norm at most \(\|a\|+o(1)\) using Kaplansky density and norm density in the generated \(C^*\)-algebra.
Their images are bounded in the Hilbert ball of radius \(3\|\zeta\|_2(\|a\|+o(1))\), and a weak cluster point lies in the weakly closed canonical graph over \(a\).
This yields the required bound on the enlarged optimum \(\beta\).
The lower bound \(c/4\le\beta\) of C_F0208, (2), gives \(c\le12\|\zeta\|_2\) for the original marginal.
The finite attainment in C_F0211, (2), is therefore applicable to \(W^*(X)\) by itself, providing a single faithful normalized \(d\) with \(d^{-1}\in L^1(B)\) and the stated rank-one commutator on all of \(L^2(B)\).
An optimal density may be chosen there before considering any ambient weight or center.

**Positive ambient weights.**
Tracial cyclicity and trace-preserving conditional expectation give
\(\|(X-\lambda)a^{1/2}\|_2^2=\tau(w|X-\lambda|^2)\) for \(w=\mathbb E_Ba\), with \(0\le w\le1\) and \(\tau(w)=t\).
Because the spectral singleton at \(\lambda\) has trace zero, this quantity is positive for \(t>0\).
With the candidate's \(\sigma\), the mass of \(w\) outside radius \(2\sigma\) is at most \(t/4\).
Hence the truncated \(h\) has mass \(t'\ge3t/4\).
Compression by \(L_{\sqrt h}\) makes the rank-one norm \(\sqrt{t'}\,\|\sqrt h d^{-1/2}\|_2\).
The two terms of the compressed commutator with \(L_{X-\lambda}\) each have norm at most \(2c\sigma\) because \(\sqrt h\) and \(X-\lambda\) commute.
The Cauchy–Schwarz pairing of \(\sqrt h d^{-1/2}\) and \(\sqrt h d^{1/2}\) is defined by the two integrability conditions and equals \(t'\).
Combining gives \(t'^3\le16c^2\sigma^2\tau(dh)\).
As \(h\le w\), positivity and truncation of \(d\) give \(\tau(dh)\le\tau(dw)=\tau(da)\), also for positive ambient \(a\) which do not commute with \(d\).
Using \(\sigma^2=\|(X-\lambda)a^{1/2}\|_2^2/t\) yields the constant \(16(4/3)^3c^2\le(1024/27)(12\|\zeta\|_2)^2\).
Summation over positive weights of sum at most one uses the same normal state for every center.
For \(\sigma\le R\), the bound gives \(t\le K^{1/3}R^{2/3}\).
Moreover \(\tau(da)\le Ct+\tau((d-C)_+)\) for all such weights, first testing the positive and bounded spectral parts against \(a\).
Letting \(R\downarrow0\) and then \(C\uparrow\infty\) makes the state mass uniformly small, which proves the claimed little-order bound.

**Spectral partition and packing.**
For a finite spectral partition, each \(a_l=e q_l e\) is a positive contraction and \(\sum_l a_l=e\), with \(t_l=\tau(e q_l)\ge0\).
The identity \((e q_l)(e q_l)^*=a_l\) gives \(v_l^2=\|(X-\lambda_l)a_l^{1/2}\|_2^2\), including when \(e\) and \(q_l\) do not commute.
If \(t_l=0\), faithfulness gives \(a_l=0\) and \(e q_l=0\).
Otherwise the positive scalar denominator just proved applies to \(v_l\).
Cauchy–Schwarz on \(t_l^2/v_l\) and \(v_l\) yields \((\sum_l t_l^2)^2/\sum_l v_l^2\le\sum_l t_l^4/v_l^2\le K\tau(de)\).
Expanding the three terms in the candidate's identity leaves \(Xe q_l-e c q_l=(X-\lambda_l)e q_l\), so the commutator is indeed \([c,e]q_l\).
For any bounded \(z\), \(\sum_l\|zq_l\|_2^2=\|z\|_2^2\) by traciality and the partition of one.
The direct-sum triangle inequality thus bounds \(\sum_l v_l^2\) by \(tR^2\) with exactly the two additive errors stated in \(R\).
Since \(\sum_l t_l^2=t^2/m\), this yields \(t^3/(m^2R^2)\le K\tau(de)\).
Pairwise orthogonality gives the asserted sum by normality of the state, and finite partial sums also cover countable families.
Multiplication of each summand by \((m_jR_j/r_j)^2\le L^2\) proves the original packing estimate.
In the commuting finite-spectrum case \(R=r\) and \(m\) is at most the number of positive-mass spectral values by scalar Cauchy–Schwarz.
An exact spectral projection \(e=1_{[0,r]}(|X-b|)\) always meets the required Hilbert error bound.
The decomposition uses no normality of \(b\) and applies as stated to its chosen normal approximants.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0233_v1.md#statement) | Both weighted estimates, their constants and uniformity, summability, individual approximation errors and the claimed special cases. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0233_v1.md#argument) | Scalar ACSY restriction, free enlargement, full bounded-input witness, rank-one compression and spectral partition. |
| [Whole-proof finding](#whole-proof-finding) | [Normal coordinate phases](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, diffuseness and marginal coarse values on the scalar star core. |
| [Whole-proof finding](#whole-proof-finding) | [Two-Haar column criterion](../../claims/Yin_C_F0208_v1.md#statement) | Free enlargement with old vacuum and the factor-four lower bound for enlarged bounded-dual cost in (2). |
| [Whole-proof finding](#whole-proof-finding) | [Free normal estimate](../../claims/Yin_C_F0162_v1.md#statement) | Part B, (S5) and (S6), for the canonical contraction and its commutators at every bounded input of the enlarged algebra. |
| [Whole-proof finding](#whole-proof-finding) | [Optimal scalar density](../../claims/Yin_C_F0211_v1.md#statement) | Attainment of (2), faithful normalized density with integrable inverse, full Hilbert-space rank-one commutator and the referenced orthogonal tests (3). |

---
author: Yin
---

# SW20: finite-support spectral invariance and its structural boundary

<a id="sw20-u001"></a>
## Source and inspection scope

The source is [arXiv v4](readme.md#arxiv-v4).
Definition 1.3 on p. 2, the group definitions on pp. 1 and 9, Theorem 4.7 and Corollary 4.8 on p. 13, and Remark 4.9 and Corollary 4.11 on p. 14 were read directly.
The spectral-invariance theorem is accepted as an established published input at its statement and applicability scope; its interpolation proof and the Barnes–Hulanicki foundation were not audited end to end.
The short free-semigroup argument was checked locally, including the notation corrections below.
Corollary 4.11's application of the external structure theorem for elementary amenable groups was read but that external proof was not re-audited.

<a id="spectral-definitions"></a>
## Hermitian, quasi-Hermitian and quasi-symmetric: discrete specialization

Let \(G\) be a discrete group, let \(A=\ell^1(G)\) with convolution and involution \(f^*(g)=\overline{f(g^{-1})}\), and identify \(\mathbb CG\) with its finitely supported subalgebra.
Write \(\sigma_A(f)\) and \(r_A(f)=\sup\{|z|:z\in\sigma_A(f)\}\) for the Banach-algebra spectrum and spectral radius.
The regular representation gives the inclusion in \(C_r^*(G)\).

The group is Hermitian when \(\sigma_A(f)\subset\mathbb R\) for every \(f=f^*\in A\).
It is quasi-Hermitian when the same requirement is imposed only on \(f=f^*\in\mathbb CG\).
It is quasi-symmetric when \(\sigma_A(f^*f)\subset[0,\infty)\) for every \(f\in\mathbb CG\).
The first convention is on p. 1, the second is Definition 1.3 on p. 2, and the third is the beginning of Section 4 on p. 9.
The source treats locally compact groups with \(C_c(G)\subset L^1(G)\); these are precisely the discrete specializations needed here.
The finite-support and full \(\ell^1\) quantifiers must not be identified.

<a id="finite-support-spectral-invariance"></a>
## Theorem 4.7 and amenability

Theorem 4.7 on p. 13 states that the following are equivalent, in its more general locally compact setting and hence for every discrete \(G\):

1. \(G\) is quasi-symmetric.
2. \(G\) is quasi-Hermitian.
3. \(r_{\ell^1(G)}(f)=r_{C_r^*(G)}(f)\) for every \(f=f^*\in\mathbb CG\).
4. \(\sigma_{\ell^1(G)}(f)=\sigma_{C_r^*(G)}(f)\) for every \(f\in\mathbb CG\).

Part (4) has no self-adjointness restriction on \(f\).
Its support restriction remains essential: the statement is not an assertion of spectral equality for every element of \(\ell^1(G)\).
Corollary 4.8 gives amenability as a consequence of these equivalent properties.
It supplies no converse from amenability.

The opening proof paragraph of Theorem 4.7 repeats the arrow (iii) implies (iv), once with the Barnes–Hulanicki attribution and once as the clear remaining implication.
The omitted closing implication (iv) implies (i) follows directly because the regular image of \(f^*f\) is positive.
This typographical repetition does not change the stated equivalence; the substantial interpolation argument proving (ii) implies (iii) remains an accepted external input.

<a id="free-semigroup-obstruction"></a>
## Remark 4.9: free semigroups obstruct quasi-Hermitianity

Remark 4.9 on p. 14 states that a discrete group containing a free subsemigroup on two generators is not quasi-Hermitian, and attributes the original finitely supported self-adjoint witness to Jenkins.
Thus under that structural hypothesis some \(x=x^*\in\mathbb CG\) has \(\sigma_{\ell^1(G)}(x)\not\subset\mathbb R\).
This is stronger than merely knowing that \(\ell^1(G)\) has a non-Hermitian element with infinite support.

The rendered preprint's short proof calls a polynomial in \(\delta_s\) Hermitian, whereas it is only required to be normal, and later changes the third block \(s^2t\) to \(st^2\).
The proof works with the first block convention throughout.
The following check makes both corrections explicit without claiming any change to the source theorem.

Let \(s,t\) freely generate a subsemigroup and put \(P(z)=(1+z-z^2)/3\).
The triangle inequality gives \(|P(z)|\le1\) on the unit circle.
Equality would force \(1,z,-z^2\) to have the same phase, which is impossible, so compactness gives \(\rho:=\sup_{|z|=1}|P(z)|<1\).
The element \(P(\delta_s)\) is normal in the reduced group \(C^*\)-algebra because it is a polynomial in one unitary.
Hence, for
\[
v=P(\delta_s)\delta_t
=\frac{\delta_t+\delta_{st}-\delta_{s^2t}}3,
\]
one has \(\|v\|_{C_r^*(G)}\le\rho<1\).
Every product of \(n\) blocks from \(\{t,st,s^2t\}\) is a different group element: in the free positive word, successive occurrences of \(t\) delimit blocks with respectively zero, one or two copies of \(s\).
Therefore \(v^n\) has \(3^n\) distinct coefficients of absolute value \(3^{-n}\), so \(\|v^n\|_{\ell^1}=1\) for every \(n\).
The spectral-radius formula gives \(r_{\ell^1}(v)=1>\|v\|_{C_r^*}\ge r_{C_r^*}(v)\).
This contradicts Theorem 4.7(4) if \(G\) were quasi-Hermitian and verifies the stated structural obstruction.

<a id="elementary-amenable-growth"></a>
## Corollary 4.11: the elementary amenable boundary

Corollary 4.11 on p. 14 states that a discrete elementary amenable group is quasi-Hermitian if and only if it has subexponential growth.
The source uses the local convention in which subexponential growth holds on every finitely generated subgroup.
For finitely generated groups this is the usual word-growth condition.

The forward obstruction uses the cited elementary amenable structure theorem: if the group is not of subexponential growth, it contains a finitely generated subgroup of exponential growth and a free subsemigroup on two generators.
The source then invokes Remark 4.9.
The other direction uses the subexponential-growth result stated as Proposition 4.1 on p. 9.
Those growth theorems are accepted at the source's stated scope, without a new audit of their original proofs.

In particular, every torsion-free finitely generated elementary amenable group of exponential growth fails the finite-support real-spectrum property.
No search for a particular group or numerical probing is needed for this class-level conclusion.
The source does not assert that every amenable group is quasi-Hermitian, does not classify all amenable groups by this property, and gives no group-ring zero-divisor conclusion.

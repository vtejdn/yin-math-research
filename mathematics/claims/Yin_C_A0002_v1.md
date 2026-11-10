---
author: Yin
---
# Spectral-chain tensor injectivity for affiliated operators

This argument supplies the domain-sensitive completion of JZ19 Lemma 9.10(2), printed pp. 526–527, in the [retained journal edition](../audits/literature/JZ19/readme.md#journal-edition).
It uses distinct spectral parameters and the full Hilbert tensor product as the codomain.
The source's intended centralizer lower bound is retained; no new Atiyah group-class assertion is made.

## Statement

Let \(H\) be a countable group acting freely on a set \(X\) with finitely many orbits, let \(\mathcal H=\ell^2(X)\), and let \(\mathcal M\) be the finite von Neumann algebra of bounded \(H\)-equivariant operators on \(\mathcal H\).
Its trace is the group-module trace, with \(\operatorname{tr}(1)=|H\backslash X|\).
Let \(A\) be a closed densely defined operator affiliated with \(\mathcal M\).
Products and powers in \(\mathcal U(\mathcal M)\) mean their closed affiliated products; ordinary successive application to a vector is specified separately below.

For \(\lambda\in\mathbb C\), set
\[
N_\lambda=A-\lambda,\quad
K_{\lambda,r}=\ker N_\lambda^r,\quad K_{\lambda,0}=0,\quad
E_{\lambda,j}=K_{\lambda,j+1}\ominus K_{\lambda,j},\quad
d_{\lambda,j}=\dim_H E_{\lambda,j}.
\]
Use \(K^*_{\lambda,r}=\ker(A^*-\bar\lambda)^r\) and
\(E^*_{\lambda,j}=K^*_{\lambda,j+1}\ominus K^*_{\lambda,j}\).

Let \(\lambda_1,\ldots,\lambda_k\) be pairwise distinct complex numbers and let \(m_1,\ldots,m_k\) be nonnegative integers.
For every \(\varepsilon>0\), one can choose closed invariant subspaces
\[
U^\varepsilon_{i,j}\subseteq E_{\lambda_i,j},\qquad
V^\varepsilon_{i,j}\subseteq E^*_{\lambda_i,j}
\quad(1\le i\le k,\ 0\le j\le m_i)
\]
such that each dimension is at least \(d_{\lambda_i,j}-\varepsilon\), all successive applications through order \(j+1\) exist, and \(A\), respectively \(A^*\), is bounded on every image in the corresponding chain through order \(j\).

For any such choices, define on elementary tensors
\[
T_{i,j}(\bar v\otimes u)
=\sum_{r=0}^{j}
\overline{(A^*-\bar\lambda_i)^{j-r}v}
 \otimes (A-\lambda_i)^r u.
\]
The resulting map
\[
T^\varepsilon:
\bigoplus_{i=1}^{k}\ \bigoplus_{j=0}^{m_i}
\overline{V^\varepsilon_{i,j}}\ \widehat\otimes\
U^\varepsilon_{i,j}
\longrightarrow
\overline{\mathcal H}\ \widehat\otimes\ \mathcal H,
\qquad
(z_{i,j})\longmapsto\sum_{i,j}T_{i,j}z_{i,j},
\]
is bounded, \(H\times H\)-equivariant and injective.
Here the tensor products and the finite direct sum are Hilbert completions.

Writing \(W^\varepsilon=\overline{\operatorname{ran}T^\varepsilon}\), one has the exact identity
\[
\dim_{H\times H}W^\varepsilon
=
\sum_{i=1}^{k}\sum_{j=0}^{m_i}
\dim_H V^\varepsilon_{i,j}\,\dim_H U^\varepsilon_{i,j},
\]
and consequently
\[
\lim_{\varepsilon\downarrow0}\dim_{H\times H}W^\varepsilon
=\sum_{i=1}^{k}\sum_{j=0}^{m_i}d_{\lambda_i,j}^{\,2}.
\]

Under the Hilbert–Schmidt identification, \(W^\varepsilon\) lies in the denominator-cleared centralizer of \(A\).
Thus Proposition 9.9 follows:
\[
\dim_{H\times H} C_{HS}(A)
\ge \sum_{\lambda\in\sigma_p(A)}\sum_{j\ge0}d_{\lambda,j}^{\,2}.
\]
A sum of nonnegative terms is understood as the supremum of its finite subsums.
The same statements apply to matrices by replacing \(X\) with \(X\times\{1,\ldots,n\}\); the trace is unnormalized in that matrix factor.

## Current assessment

[Selected decision](#decision-reviewed-tensor-completion)

## Assessment history

### Decision reviewed-tensor-completion

| Field | Value |
| --- | --- |
| date | 2026-11-10T15:28 |
| status | proved |
| reason | Independent whole-argument review checks the explicit chain cutoffs, completed tensor injectivity, dimension limit, centralizer inclusion and matrix amplification under the declared standard foundations; spectral distinctness and the full tensor codomain are explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Distinct-parameter finite-family tensor injectivity, arbitrary admissible cutoffs, dimension limit, Proposition 9.9 consequence and unnormalized amplification. |
| argument | [Complete argument](#argument) | All actual-domain, bounded-denominator, tensor-completion, trace and closure interfaces. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0003_v1.md#whole-argument-finding) | Independently reviewed full statement and argument, including the literal repeated-parameter counterexample and corrected source-use scope. |
| dependency | [Accepted source foundations](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Exactly Section 3.2's finite affiliated algebra and Section 9.1/Proposition 9.1's Hilbert-module, Hilbert–Schmidt and weak-exact dimension interfaces; neither Lemma 9.10(2), Proposition 9.9 nor the later coefficient-change conclusions supply a premise. |

The source attribution and repair origin are JZ19 Lemma 9.10(2), printed pp. 526–527.
The source unit's link back to this completion records that repair, not a reverse logical dependency on the repaired conclusion.

## Argument

### Foundations and conventions

Operators in this proof act on the left, unlike the right-operator notation on JZ19 pp. 526–527.
The Hilbert inner product is linear in its first variable, and
\[
\bar v\otimes u\ \longmapsto\
K_{v,u},\qquad K_{v,u}(\xi)=\langle\xi,v\rangle u,
\]
extends to the Hilbert–Schmidt identification.
The first tensor factor has the conjugate \(H\)-action, and the second has the given action.

The accepted foundations are the closed affiliated-operator algebra, spectral calculus, polar decomposition, and finite Hilbert-module dimension.
In particular, a bounded equivariant map has domain dimension equal to its kernel dimension plus its closed-image dimension.
Polar decomposition identifies the traces of the initial and final support projections.
For exterior Hilbert tensor products, the product trace gives
\(\dim_{H\times H}(\bar V\widehat\otimes U)=\dim_H V\,\dim_H U\).
These are the precise finite-module and affiliated interfaces in JZ19 Section 3.2, Section 9.1 and Proposition 9.1, recorded in the [source unit](../audits/literature/JZ19/Yin_U001.md#hilbert-schmidt-mechanism).
The source's Lemma 9.10(2), Proposition 9.9 and later coefficient-change theorems are not proof inputs here.

If \(B\) is affiliated, there is a bounded injective \(d\in\mathcal M\) such that \(dB\), initially defined on \(\operatorname{dom}B\), has a bounded extension \(c\in\mathcal M\).
One concrete choice is
\[
d=(1+BB^*)^{-1/2},\qquad
c=\overline{dB}.
\]
Polar decomposition and \(t/\sqrt{1+t^2}\le1\) give \(\|c\|\le1\); the strictly positive spectral multiplier makes \(d\) injective.
The equality \(c\xi=dB\xi\) is used only for \(\xi\in\operatorname{dom}B\).
No unbounded tensor extension of \(B\) will be applied to an arbitrary tensor-completion vector.

### Adjoint layers have equal dimension

For \(r\ge1\), apply polar decomposition to the affiliated operator \(N_\lambda^r\).
Its adjoint is \((A^*-\bar\lambda)^r\) as a closed affiliated product.
The two support projections have equal finite trace, and hence
\[
\dim_H K_{\lambda,r}=\dim_H K^*_{\lambda,r}.
\]
Subtracting the equalities for \(r=j+1\) and \(r=j\) gives
\[
\dim_H E_{\lambda,j}=\dim_H E^*_{\lambda,j}=d_{\lambda,j}.
\]
Kernels of the affiliated powers are nested because the affiliated identity \(N_\lambda^r p=0\) implies \(N_\lambda^{r+1}p=0\) for their kernel projection \(p\).

### Explicit chain cutoffs

Fix \(j,\lambda,\varepsilon\), and let \(P\) be the projection onto \(E_{\lambda,j}\).
Choose the spectral projection
\[
e=\mathbf1_{[0,L]}(|A|)
\]
with \((j+1)\operatorname{tr}(1-e)<\varepsilon\).
Such \(L\) exists because \(e\uparrow1\) and the trace is finite.
The range of \(e\) lies in \(\operatorname{dom}A\), and \(B=Ae\) is bounded with norm at most \(L\).

Define the bounded equivariant map
\[
Q:E_{\lambda,j}\longrightarrow
\bigoplus_{r=0}^{j}(1-e)\mathcal H,\qquad
Q u=\bigl((1-e)B^r u\bigr)_{r=0}^{j},
\]
where \(B^0=1\), and put \(U^\varepsilon=\ker Q\).
Then \(U^\varepsilon\) is closed, invariant, and contained in \(E_{\lambda,j}\).
Dimension additivity gives
\[
\dim_H U^\varepsilon
\ge d_{\lambda,j}-(j+1)\operatorname{tr}(1-e)
> d_{\lambda,j}-\varepsilon.
\]

For \(u\in U^\varepsilon\), each \(B^r u\), \(0\le r\le j\), lies in \(e\mathcal H\).
Induction gives the actual successive applications
\[
A^r u=B^r u\quad(0\le r\le j+1).
\]
Indeed \(A B^r u=AeB^r u=B^{r+1}u\) whenever \(r\le j\).
Moreover \(A\) is bounded by \(L\) on every \(A^rU^\varepsilon\), \(0\le r\le j\), since all those spaces lie in \(e\mathcal H\).
This proves exactly the chain-boundedness required by the source.

Since \(u\in K_{\lambda,j+1}\) and the classical iterate exists, that iterate agrees with the closed affiliated power and satisfies \(N_\lambda^{j+1}u=0\).
The finite span of \(u,N_\lambda u,\ldots,N_\lambda^j u\) is contained in \(\operatorname{dom}A\) and is stable under \(A\).
Thus all higher ordinary polynomial applications are also defined on this vector, and they agree with the affiliated polynomial.
The same construction for \(A^*\) supplies \(V^\varepsilon\), with the required dimension by the previous paragraph.

Membership in the kernel of a closed affiliated power alone would not have supplied this chain-domain assertion.
The explicit cutoff construction is what supplies it.

### Boundedness and the actual codomain

Suppress \(\varepsilon\) in the rest of the proof.
On each chosen \(U_{i,j}\), every \(N_{\lambda_i}^r\), \(0\le r\le j\), is a bounded map to \(\mathcal H\); the same holds for the adjoint powers on \(V_{i,j}\).
Consequently each term in \(T_{i,j}\) is a tensor product of bounded maps and extends uniquely to the completed Hilbert tensor product.
There are only finitely many terms and summands, so \(T^\varepsilon\) is bounded and equivariant.

The vectors \(N_{\lambda_i}^r u\) belong to \(K_{\lambda_i,j+1-r}\), but need not belong to any of the chosen cutoff spaces.
Likewise for the adjoint factor.
The justified codomain is the full \(\overline{\mathcal H}\widehat\otimes\mathcal H\), followed by the closed-image target \(W^\varepsilon\).
No invariance or closedness of the sum of the cutoff layers is assumed.

### Injectivity for one spectral parameter

Fix \(\lambda\) and an upper level \(m\).
Suppose
\[
\sum_{j=0}^{m}T_j z_j=0,\qquad
z_j\in\overline{V_j}\widehat\otimes U_j.
\]
Let \(P_m\) be the orthogonal projection onto \(E_{\lambda,m}\).
Apply the bounded operator \(1\otimes P_m\) to the equality.

Every second factor from a level \(j<m\) lies in \(K_{\lambda,m}\), so it is annihilated.
At level \(m\), the terms with \(r\ge1\) also lie in \(K_{\lambda,m}\).
The term with \(r=0\) survives unchanged, giving
\[
\left(\overline{(A^*-\bar\lambda)^m|_{V_m}}
 \ \widehat\otimes\ \iota_{U_m}\right)z_m=0.
\]
The first bounded map is injective: its kernel is
\(V_m\cap K^*_{\lambda,m}=0\), because \(V_m\subseteq E^*_{\lambda,m}\).
The inclusion \(\iota_{U_m}:U_m\to\mathcal H\) is also injective.

The tensor product of two bounded injective Hilbert-space maps is injective.
Indeed both adjoints have dense range, so the range of the tensor-product adjoint contains a dense algebraic tensor product.
Thus \(z_m=0\).
Descending through the finitely many levels gives \(z_j=0\) for every \(j\).
All projections and tensor maps in this argument are bounded on their entire Hilbert domains.

### Separation of distinct spectral parameters with bounded maps

Choose Chinese-remainder polynomials \(p_i\in\mathbb C[t]\) satisfying
\[
p_i(t)\equiv1\pmod{(t-\lambda_i)^{m_i+1}},
\qquad
p_i(t)\equiv0\pmod{(t-\lambda_\ell)^{m_\ell+1}}
\quad(\ell\ne i).
\]
The distinctness hypothesis makes these polynomials exist.

For every elementary second factor \(h=N_{\lambda_\ell}^r u\) occurring in \(T_{\ell,j}\), the chain-domain result proves that the ordinary polynomial \(p_i(A)h\) exists.
Polynomial division on that finite nilpotent chain gives
\[
p_i(A)h=
\begin{cases}
h,&\ell=i,\\
0,&\ell\ne i.
\end{cases}
\]
This is also the value of the closed affiliated polynomial \(p_i(A)\) on \(h\).

Choose bounded \(d_i,c_i\in\mathcal M\) with \(d_i\) injective and \(c_i=\overline{d_i p_i(A)}\), by the bounded-denominator construction above.
On elementary tensors the preceding identity becomes
\[
(1\otimes c_i)T_{\ell,j}
=\begin{cases}
(1\otimes d_i)T_{i,j},&\ell=i,\\
0,&\ell\ne i.
\end{cases}
\]
Both sides are bounded maps on the same completed source tensor product.
Their equality therefore extends by continuity from elementary tensors to the whole Hilbert completion.
This passage uses neither an unbounded tensor-domain assumption nor a bounded spectral projection onto a nonnormal primary component.

If \(\sum_{\ell,j}T_{\ell,j}z_{\ell,j}=0\), apply \(1\otimes c_i\).
It gives
\[
(1\otimes d_i)\sum_{j=0}^{m_i}T_{i,j}z_{i,j}=0.
\]
Since \(d_i\) and hence \(1\otimes d_i\) are injective, the inner sum is zero.
The single-parameter argument now gives every \(z_{i,j}=0\).
Doing this for all \(i\) proves injectivity of \(T^\varepsilon\).

### Dimension equality and the cutoff limit

The bounded injective map \(T^\varepsilon\) has dense range in its declared target \(W^\varepsilon\).
Polar decomposition and the product trace give
\[
\dim_{H\times H}W^\varepsilon
=\sum_{i,j}\dim_H V^\varepsilon_{i,j}\,\dim_H U^\varepsilon_{i,j}.
\]
For each level both factors lie in
\([\max(0,d_{\lambda_i,j}-\varepsilon),d_{\lambda_i,j}]\).
Therefore
\[
\sum_{i,j}\max(0,d_{\lambda_i,j}-\varepsilon)^2
\le \dim_{H\times H}W^\varepsilon
\le \sum_{i,j}d_{\lambda_i,j}^{\,2}.
\]
The finite squeeze proves the asserted limit without requiring nested cutoffs.
If the source's notation uses the sum of the separately closed images \(W_{i,j}^\varepsilon\), its closure equals \(W^\varepsilon\).
The dimension convention already uses that closure; a nonclosed finite sum is not asserted to be a Hilbert-module codomain.

### Centralizer inclusion and amplification

For an elementary chain pair \(v,u\), the corresponding finite-rank operator is
\[
D=\sum_{r=0}^{j}K_{(N_\lambda^*)^{j-r}v,N_\lambda^r u}.
\]
Its range lies in \(\operatorname{dom}A\), so \(AD\) is everywhere defined and bounded.
Because each first-factor vector lies in \(\operatorname{dom}A^*\), \(DA\), initially defined on \(\operatorname{dom}A\), has a bounded extension.
The two extensions agree: subtraction telescopes to
\[
K_{v,N_\lambda^{j+1}u}
-
K_{(N_\lambda^*)^{j+1}v,u}=0.
\]

To pass to Hilbert–Schmidt closures, take bounded denominators with
\[
A=B_1^{-1}C_1=C_2B_2^{-1}.
\]
One may choose \(B_2=(1+A^*A)^{-1/2}\), so \(B_2\mathcal H\subseteq\operatorname{dom}A\), and \(C_2=AB_2\).
Take \(B_1=(1+AA^*)^{-1/2}\) and \(C_1=\overline{B_1A}\).
The commutation just proved implies
\[
C_1DB_2=B_1DC_2.
\]
The map \(D\mapsto C_1DB_2-B_1DC_2\) is bounded on Hilbert–Schmidt space.
Its kernel therefore contains the closure of all these finite-rank combinations, namely the image of \(W^\varepsilon\).
This is the source's denominator-cleared centralizer.
Taking the finite-family dimension limit and then the supremum over finite spectral families and levels proves Proposition 9.9.

Replacing \(X\) by \(X\times\{1,\ldots,n\}\) handles an affiliated \(n\)-by-\(n\) matrix.
The Hilbert–Schmidt identification becomes \(HS(\mathcal H^n)=M_n(HS(\mathcal H))\).
The ambient module dimension is \(n|H\backslash X|\); no normalized matrix trace is introduced.

## Source corrections and scope

The printed Lemma 9.10(2) does not explicitly require distinct \(\lambda_i\).
If repeated parameters are allowed, its formula is false.
Take the trivial group, \(X\) a singleton, \(A=0\), \(k=2\), \(\lambda_1=\lambda_2=0\), and \(m_1=m_2=1\).
For \(0<\varepsilon<1\), each level-zero cutoff must equal \(\mathbb C\), while all higher layers vanish.
The left side is the dimension of one copy of \(HS(\mathbb C)\), namely \(1\), whereas the printed right side is \(2\).
The corrected distinct-parameter version is exactly what the sum over different eigenvalues in Proposition 9.9 needs.

The source's proposed cutoff-space codomain is not justified by its stated cutoff hypotheses.
The proof above replaces that codomain by the full tensor product and proves bounded injectivity there.
It also supplies the missing construction of chain cutoffs and the adjoint-layer dimension equality.

This result addresses the selected analytic step and its immediate centralizer consequence.
It neither re-audits all of JZ19's other inputs nor resolves the complex Atiyah conjecture for arbitrary torsion-free groups.

## Derivation context

On 10 November 2026, Yin requested a concentrated reconstruction of Lemma 9.10(2), followed by independent review if a complete argument could be supplied.
The coordinating agent developed the argument above.
A separate source-reading helper checked the literal cutoff conditions, the omitted distinctness wording, the dimension conventions and the amplification passages, without developing this proof.

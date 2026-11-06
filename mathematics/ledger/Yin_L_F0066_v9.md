---
author: Yin
---

<a id="nonreal-center-corank-one-obstruction"></a>
# A complete-numerator atom on a corank-one high-matching background

This ordinary mathematical investigation by an agent representing Yin, dated 2026-11-06, tests whether a nonreal spectral parameter and the true first-row center exclude conditional atoms of the complete numerator for the [finite-variance Brown Task](../tasks/Yin_T_F0012_v3.md#contract).
The derivation and the fixed-law realization received ordinary authoring self-checks, not a formal proof review.
It retains a failed implication, not a new adopted small-ball theorem.
The [fixed low-matching comparison](../ledger/Yin_L_F0066_v7.md#accepted-branch-comparison) and [normalized coefficient theorem](../claims/Yin_C_F0194_v15.md#statement) are reused at their stated scopes.
The construction below has high matching, a nonzero cofactor denominator, and a polynomially guarded actual product-inverse shift, yet its complete normalized numerator has a conditional zero atom of order \(N^{-1}\).
Its realization uses fixed bounded atomic off-diagonal laws and fixed unbounded diagonal laws with every finite moment.
It therefore lies inside the finite-second-moment Task but does not refute the pilot in which the diagonal laws are also bounded.
The conditioning backgrounds have exponentially small probability, so this is not a counterexample to the averaged high-concentration target or to Brown convergence.

<a id="actual-model-and-target"></a>
## Actual model and conditional target

Let \(A,B,C\) be the three independent real symmetric Wigner inputs, normalized by \(N^{-1/2}\), with fixed centered off-diagonal laws of variance one and fixed centered real diagonal laws of finite second moment.
Within each matrix, the strict upper-triangular coordinates are independent copies of its off-diagonal law, independent of the independent diagonal coordinates.
Their laws do not depend on \(N\), and no cross-size independence is required.
The particular laws realizing the construction are specified below.
On the invertibility event for \(B,C\), define
\[
 M:=A-zC^{-1}B^{-1}
   =\begin{pmatrix}
       \mu&(x+f)^T\\
       x+g&D
     \end{pmatrix},\qquad
 MBC=ABC-zI_N.
 \tag{Center-probe-complete-block}
\]
Here \(x:=\xi/\sqrt N\) is the first off-diagonal border of \(A\), \(A_0:=A_{\widehat1,\widehat1}\), \(S_0:=(C^{-1}B^{-1})_{\widehat1,\widehat1}\), and \(D=A_0-zS_0\).
The vectors \(f,g\) are the actual shifted row and column, transposed as in the displayed block, and \(\mu\) is its actual shifted diagonal.
All transposes in polynomial identities are ordinary transposes; \(u^*\) below denotes conjugate transpose.
Define
\[
 \mathcal F_1:=\sigma(A_0,A_{11},B,C),\qquad
 T:=\operatorname{adj}D,\qquad Q:=\operatorname{sym}T=(T+T^T)/2.
\]
Conditioning on \(\mathcal F_1\) retains the independent original coordinates of \(\xi\).
On \(T\ne0\), put
\[
 Z_1(\xi):=
 \frac{\mu\det D-f^TTg
       -(Tg+T^Tf)^T\xi/\sqrt N-\xi^TQ\xi/N}
      {\|T\|_F}
 =\frac{\det M}{\|T\|_F},\qquad
 \kappa_1(\tau):=\mathbb P\{|Z_1(\xi)|\le\tau\mid\mathcal F_1\}.
 \tag{Center-probe-complete-normalization}
\]
For \(h>0\), let \(\mathcal H_1(h,r)\) require \(T\ne0\) and a matching of at least \(r\) edges in the graph with edges \(j\ne k\) satisfying \(|Q_{jk}|\ge h\|T\|_F\).
The other indices use the analogous definitions.
The continuing probability objective is to make the mean probability of high-matching backgrounds with \(\kappa_i(N^{-T_*})>N^{-B_*}\) of order \(N^{-B_*}\), for suitable fixed \(T_*>0\) and \(B_*>1\), on the existing polynomial guards.
The construction tests the stronger proposed uniform conditional bound and explains why actual background probabilities cannot be omitted.

<a id="invertible-minor-and-sign-boundary"></a>
## The invertible-minor rank calculation and its precise limit

For a real symmetric \(m\)-by-\(m\) matrix \(A_0\), a real \(m\)-by-\(m\) matrix \(S_0\), and \(z\notin\mathbb R\), suppose
\[
 D:=A_0-zS_0
\]
is invertible.
Put \(H:=\operatorname{sym}D=A_0-z\operatorname{sym}S_0\), with ordinary transpose in the symmetrization.
Then
\[
 \operatorname{sym}D^{-1}=D^{-T}HD^{-1},\qquad
 A_0=\frac{\bar z H-z\bar H}{\bar z-z}.
 \tag{Center-probe-invertible-rank-identities}
\]
The first identity follows by multiplying out the two terms in \(H=(D+D^T)/2\), and the second uses the reality of \(A_0,S_0\).
Consequently
\[
 \operatorname{rank}(\operatorname{sym}D^{-1})
 =\operatorname{rank}H
 \ge\frac12\operatorname{rank}A_0.
 \tag{Center-probe-invertible-rank}
\]
If \(\operatorname{rank}A_0\ge5\), the complete first-row polynomial before reducing any powers cannot factor over \(\mathbb C\) into two nonconstant polynomials.
Indeed its homogeneous quadratic matrix is a nonzero scalar multiple of \(\operatorname{sym}D^{-1}\), of rank at least three, whereas a product of two affine linear forms has homogeneous quadratic matrix \((ab^T+ba^T)/2\), of rank at most two.
Every nontrivial factorization of a degree-two polynomial would be of this affine-linear type.
This is only a statement about polynomial factorization on the invertible-minor branch.
It supplies no quantitative small-ball estimate and does not exclude a large collection of unrelated lattice zeros.

For a two-point first-entry law, that raw polynomial conclusion does not even exclude a factorization of its values on the support.
For Rademacher coordinates, an arbitrary diagonal quadratic matrix contributes only to the constant after using \(\xi_j^2=1\).
For example, with two equal even-sized coordinate groups \(I,J\), the polynomial
\[
 F(\xi):=\sum_{j\in I\cup J}(\xi_j^2-1)
       +\left(\sum_{j\in I}\xi_j\right)
        \left(\sum_{j\in J}\xi_j\right)
 \tag{Center-probe-sign-quotient}
\]
has a raw quadratic matrix of rank at least \(|I|+|J|-2\), because it is the identity plus a matrix of rank at most two.
On the sign cube it is exactly the displayed product of sums.
For independent fair signs and group size \(k:=|I|=|J|\), its zero probability is \(2b_k-b_k^2\), where \(b_k:=2^{-k}\binom{k}{k/2}\asymp k^{-1/2}\) for even \(k\).
Indeed the two group sums are independent and the product vanishes when either sum vanishes; the binomial estimate follows from the Stirling input specified below.
This example concerns the logical difference between raw and reduced polynomials, not an asserted actual cofactor realization.
For a general two-point support \(\{a,b\}\), the corresponding identity is \(\xi_j^2=(a+b)\xi_j-ab\), so diagonal changes also alter the effective linear coefficient.
With at least three support points, separate degree at most two in each coordinate gives a unique polynomial representative on the product support, by repeated one-variable interpolation; even then, irreducibility alone gives no concentration bound.

More fundamentally, the target also includes corank-one \(D\), where the preceding inverse argument is unavailable.
If \(\operatorname{adj}D=\gamma uv^T\ne0\), then its exact full numerator is
\[
 \det M=-\gamma\bigl((x+f)^Tu\bigr)
                       \bigl(v^T(x+g)\bigr),\qquad x:=\xi/\sqrt N.
 \tag{Center-probe-corank-factorization}
\]
Here the full \(\mu\det D\) term vanishes identically, rather than being discarded or replaced by a convenient center.
The next construction realizes this branch with many large normalized graph edges.

<a id="actual-high-matching-background"></a>
## An explicit actual background and its complete normalized numerator

Take an even integer \(n\ge4\), put \(N:=2n+1\), \(m:=2n\), and fix \(z:=i\).
Split the \(m\) retained coordinates into two groups of size \(n\), and let \(p,q\in\mathbb R^m\) be their normalized indicator vectors.
Thus \(p,q\) are orthonormal, each nonzero coordinate is \(n^{-1/2}\), and their supports are disjoint.
Define
\[
 P:=pp^T+qq^T,\qquad
 R:=I_m-P+qp^T-pq^T,
\]
\[
 B_0:=I_m-2qq^T,\qquad
 C_0:=I_m-P+pq^T+qp^T.
 \tag{Center-probe-background-matrices}
\]
Both \(B_0,C_0\) are real symmetric orthogonal matrices.
On \(\operatorname{span}\{p,q\}\), the first fixes \(p\) and negates \(q\), the second interchanges \(p,q\), and both are the identity on its orthogonal complement.
It follows directly that \(C_0^{-1}B_0^{-1}=C_0B_0=R\), with \(Rp=q\), \(Rq=-p\).
Use the full real symmetric inputs
\[
 B:=\operatorname{diag}(1,B_0),\qquad
 C:=\operatorname{diag}(1,C_0),\qquad
 A:=\begin{pmatrix}\alpha&x^T\\x&I_m\end{pmatrix},
 \tag{Center-probe-full-inputs}
\]
where \(\alpha\in\mathbb R\) and the original first border \(x\) remain arbitrary for the algebraic calculation.
Then \(C^{-1}B^{-1}=\operatorname{diag}(1,R)\), so the shifted first row and column have \(f=g=0\), the shifted diagonal is \(\mu=\alpha-i\), and
\[
 D=I_m-iR.
\]
Writing \(u:=(p+iq)/\sqrt2\), the restriction of \(D\) to the span of \(p,q\) has eigenvalues zero and two, with kernel \(\mathbb C u\); on the orthogonal complement it is \((1-i)I\).
Therefore \(D\) has corank exactly one and
\[
 T:=\operatorname{adj}D=\gamma uu^*,\qquad
 \gamma:=2(1-i)^{m-2},\qquad
 \|T\|_F=|\gamma|,
\]
\[
 Q:=\operatorname{sym}T=\frac\gamma2(pp^T+qq^T).
 \tag{Center-probe-exact-adjugate}
\]
In particular the denominator is nonzero, and the exact complete normalized numerator is
\[
 Z(x)=\frac{\det(A-iC^{-1}B^{-1})}{\|T\|_F}
     =-\frac{\gamma}{2|\gamma|}
         \bigl((p^Tx)^2+(q^Tx)^2\bigr).
 \tag{Center-probe-full-normalized-numerator}
\]
This keeps the actual center and every lower-degree term: the center vanishes because \(\det D=0\), and the linear term vanishes because \(f=g=0\).
The formula is valid for every real \(\alpha,x\), with no sign-power reduction.

For any two distinct coordinates in the same group,
\[
 \frac{|Q_{jk}|}{\|T\|_F}=\frac1{2n}=\frac1{N-1},
\]
and the other off-diagonal entries are zero.
Thus the normalized graph is the disjoint union of two complete \(n\)-vertex graphs and has matching number \(n\).
For every fixed \(H>1\), it lies in \(\mathcal H_1(N^{-H},\lfloor\sqrt N\rfloor)\) for all sufficiently large \(N\) in this sequence.
Both full factors and their displayed principal blocks have inverses of norm one, \(\|A_0\|=1\), and \(s_{m-1}(D)=\sqrt2\), with singular values ordered decreasingly.
The guards relevant to this index in the normalized coefficient theorem therefore hold with fixed bounds; that theorem still concerns coefficient energy rather than this conditional probability.

<a id="fixed-laws-and-background-probability"></a>
## Fixed entry laws and the size of the conditioning event

For the first off-diagonal law take
\[
 \mathbb P\{\xi=0\}=\tfrac12,\qquad
 \mathbb P\{\xi=\sqrt2\}
 =\mathbb P\{\xi=-\sqrt2\}=\tfrac14.
 \tag{Center-probe-first-law}
\]
It is centered with variance one, and has the representation \(\xi=(\varepsilon+\eta)/\sqrt2\) for independent fair signs.
For each even \(n\ge4\), set \(a_n:=\sqrt{2n+1}/n\) and \(t_n:=2^{-n-20}\).
Define one fixed symmetric second-and-third off-diagonal law by assigning mass \(t_n/4\) to each of \(a_n,-a_n,2a_n,-2a_n\), adding masses when locations coincide.
Let \(v:=\sum_{n\ge4,\ n\ {\rm even}}(5/2)t_na_n^2<1\) be their total second moment, add mass \((1-v)/8\) at each of \(2,-2\), and put the remaining probability at zero.
This gives a fixed bounded centered law of variance one with positive mass at every required off-diagonal value.
Its definition is independent of the matrix dimension.

Use a fixed symmetric diagonal law that, for each even \(n\ge4\), assigns mass \(t_n/6\) to each of the six listed signed values
\[
 \pm\sqrt{2n+1},\quad
 \pm(1-1/n)\sqrt{2n+1},\quad
 \pm(1-2/n)\sqrt{2n+1},
 \tag{Center-probe-diagonal-support}
\]
again adding masses at coincident locations, and puts the remaining mass at zero.
The exponential decay of \(t_n\) shows directly that every absolute moment of this law is finite.
It is centered and unbounded, and may be used for all three diagonal families.

At size \(N=2n+1\), condition on the event \(\Gamma_N\) that the first principal block is \(A_0=I_m\), its exposed diagonal is \(\alpha=0\), and the full second and third factors are exactly \(B,C\) in (Center-probe-full-inputs).
This event is measurable in the \(\mathcal F_1\) defined above and leaves the first off-diagonal border independent with its unchanged law.
Every entry is in the stated normalized support: the off-diagonal entries of \(B_0,C_0\) are \(0,-2/n,-1/n,1/n\), and their diagonal entries are \(1,1-2/n,1-1/n\).
The fixed diagonal support also realizes the diagonal entries of \(A_0\) and the two full-factor first entries.
Hence \(\mathbb P(\Gamma_N)>0\).
Moreover, there are constants \(c,C>0\), independent of this even \(n\), such that
\[
 e^{-CN^3}\le\mathbb P(\Gamma_N)\le e^{-cN^2}.
 \tag{Center-probe-background-probability}
\]
For the upper bound, the \(m(m-1)/2\) first-principal off-diagonal entries must all equal zero, each with probability \(1/2\).
For the lower bound, at most \(3N(N+1)/2\) specified independent coordinates are used, and each required atom has mass at least a fixed constant times \(2^{-n-20}\).
These estimates are deliberately only bounds, not an assertion of an exact exponential asymptotic.

Conditionally on \(\Gamma_N\), the sums over the two first-border groups are independent, and each vanishes with probability
\[
 q_n:=4^{-n}\binom{2n}{n}
     =\frac{1+O(n^{-1})}{\sqrt{\pi n}}.
\]
The exact formula follows from the representation of \(\xi\) as two fair signs.
For its asymptotic, the original [NIST DLMF Eq. 5.11.1](https://dlmf.nist.gov/5.11.E1) and [Eq. 5.11.3](https://dlmf.nist.gov/5.11.E3), in §5.11(i), were read on 2026-11-06; the existing bibliography entry is DLM26, with display key DLMF.
These are the logarithmic and multiplicative Stirling expansions as the argument tends to infinity in \(|\arg z|\le\pi-\delta\).
The positive arguments \(n+1\) and \(2n+1\) satisfy this sector condition, and substitution gives
\[
 \log q_n=-n\log4+\log\Gamma(2n+1)-2\log\Gamma(n+1)
          =-\tfrac12\log(\pi n)+O(n^{-1}).
 \tag{Center-probe-Stirling-application}
\]
Exponentiating gives the stated relative \(O(n^{-1})\) error.
The source inspection covered these formula statements, their stated sector and this applicability calculation; it did not inspect the original proofs or adopt any external random-matrix result.
Since the two squares in (Center-probe-full-normalized-numerator) are nonnegative real numbers, \(Z=0\) if and only if both group sums vanish.
Consequently
\[
 \mathbb P\{Z=0\mid\Gamma_N\}=q_n^2
     =\frac{1+O(n^{-1})}{\pi n}\asymp N^{-1},
\]
\[
 \kappa_1(N^{-T_*})\ge q_n^2>N^{-B_*}
 \quad\text{on }\Gamma_N
 \tag{Center-probe-conditional-atom}
\]
for every fixed \(T_*>0\), \(B_*>1\), and all sufficiently large sizes in the sequence.
The first inequality even holds for a zero window.
Thus nonreal \(z\), actual full-numerator normalization, strong factor guards and high matching do not imply a summable uniform conditional bound over all legal finite-variance backgrounds.

<a id="scope-and-continuation"></a>
## Consequence for the high-concentration allocation

The earlier [common-factor graph atom](../ledger/Yin_L_F0066_v7.md#common-factor-full-numerator) had a large full numerator at nonreal parameters, but that exclusion is specific to its background.
The present construction instead gives a complete-numerator atom on an actual high-matching background, and the exact corank-one factorization explains why the true center does not remove it.
The two findings are compatible.
Because (Center-probe-background-probability) is summable, this new background remains compatible with the averaged high-concentration target stated above.
It does not show that the target is false, that typical backgrounds have this atom, or that the bounded-diagonal pilot fails.

Any attempt to use nonreal-center irreducibility must therefore distinguish invertible and corank-one minors and, for two-point laws, raw polynomials from their reduced representatives.
Even on the invertible branch, a raw-rank argument alone supplies no arithmetic concentration estimate.
For the current full target, excluding dangerous corank-one or nearly corank-one backgrounds with sufficient probability, or estimating their actual affine factors jointly, remains a separate obligation.
No such estimate is supplied by this construction.
The only external asymptotic used here is the precisely inspected Stirling input above.

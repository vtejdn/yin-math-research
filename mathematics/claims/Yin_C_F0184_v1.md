---
author: Yin
---

# An L1 liberation gradient with a nonquadratic exponential remainder

Context: authorized repair of the [Voi99 Corollary 5.7 remainder issue](../audits/literature/Voi99/Yin_U003.md#exponential-remainder-limit).
Provenance: project deduction from the source definitions and two-projection representation, without a novelty claim.
This construction concerns the actual liberation gradient, rather than an arbitrary L1 generator.

## Statement

Put \(a=1/2\), \(b=3/4\), \(L=1/4\), \(\alpha=2/5\), and \(c=(1-\alpha)L^{\alpha-1}\).
Consider the probability measure and finite von Neumann algebra with faithful normal tracial state
\[
 d\mu(x)=c(x-a)^{-\alpha}1_{(a,b)}(x)\,dx,
 \qquad
 (N,\tau)=\left(M_2(L^\infty(\mu)),\frac12\int\operatorname{Tr}_2(\,\cdot\,)\,d\mu\right).
\]
Define bounded projections and their unital *-algebras by
\[
 s(x)=\sqrt{x(1-x)},\quad
 p=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 q(x)=\begin{pmatrix}x&s(x)\\s(x)&1-x\end{pmatrix},\quad
 A=\mathbb Cp+\mathbb C(1-p),\quad B=\mathbb Cq+\mathbb C(1-q).
\]
Then \(A,B\) are algebraically free, \(W^*(A,B)=N\), and \(\tau(p)=\tau(q)=1/2\).
The principal value \(g(x)=\operatorname{pv}\int(x-y)^{-1}\,d\mu(y)\) exists on \((a,b)\), and the actual liberation gradient is
\[
 j:=j(A:B)=-[p,q]g\in L^1(N,\tau)\setminus L^2(N,\tau).
 \tag{1}
\]
Here the actual liberation gradient satisfies the full polynomial trace identity
\[
 \tau(jm)=(\tau\otimes\tau)(\delta_{A:B}m),\quad
 m\in P:=\operatorname{Alg}(A,B),\qquad
 \delta_{A:B}(a_0)=a_0\otimes1-1\otimes a_0,\quad
 \delta_{A:B}(b_0)=0
\]
for \(a_0\in A\), \(b_0\in B\), with the outer bimodule action.

Let \(U(t)\) be a unitary free Brownian motion in a tracial free-product extension, free from \(N\), normalized by \(\tau(U(t))=e^{-t/2}\).
Set
\[
 F(t)=\tau(e^{tj/2}p e^{-tj/2}q),\quad
 \Lambda(t)=\tau(U(t)pU(t)^*q),\quad
 D=\frac14-\frac12\int x\,d\mu(x)=-\frac3{64}.
\]
There are constants \(c_0>0\), \(C_0<\infty\), \(t_0>0\) such that
\[
 F(t)-F(0)-tD\geq c_0t^{3/2}-C_0t^2\quad(0<t<t_0),
 \qquad
 \Lambda(t)=F(0)+tD+O(t^2).
 \tag{2}
\]
Consequently \(\Lambda(t)-F(t)\ne O(t^2)\) as \(t\downarrow0\).
This disproves the L1-only quadratic exponential comparison printed in Voi99 Corollary 5.7 for the fixed word \(a_1=p,b_1=q\).

## Current assessment
[Selected decision](#decision-reviewed-adoption)

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-02T05:01 |
| status | open |
| reason | Complete actual-gradient candidate; isolated independent correction review is pending before adopting the counterexample or disposing of the source issue. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit two-projection actual L1 gradient and failure of the original quadratic exponential comparison. |
| argument | [Candidate argument](#candidate-argument) | Cutoff convergence, whole-word gradient verification, Brownian moment and fractional lower bound. |
| dependency | [Voi99-U003](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | Definitions 5.3-5.5 and the skewadjoint trace-pairing convention; the disputed Corollary 5.7 exponential estimate is not used. |
| dependency | [Voi99-U002](../audits/literature/Voi99/Yin_U002.md#voi99-u002) | Existence of the free Brownian process in a free extension and its mean e^(-t/2); original construction remains an accepted external input. |


### Decision reviewed-adoption

| Field | Value |
| --- | --- |
| date | 2026-11-02T05:11 |
| status | proved |
| reason | Adopt the unchanged complete counterexample after R_F0186's independent whole-proof review found no mathematical gap at the actual Definition 5.4 and Corollary 5.7 hypotheses. The source's L1-only quadratic exponential comparison fails already for the fixed projection word; the preceding Brownian first-order formula and sufficient L2 quadratic comparison remain unaffected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact probability measure, algebraically free projection algebras, actual L1 but non-L2 gradient and failure of the original-normalization quadratic exponential comparison. |
| argument | [Complete argument](#candidate-argument) | Unchanged equations (1)-(13), including symmetric cutoffs, whole-word gradient verification, exact Brownian moment and positive fractional-order lower bound. |
| dependency | [Voi99-U003](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | Definitions 5.3-5.5 and skewadjoint trace-pairing convention, excluding the disputed final exponential assertion of Corollary 5.7. |
| dependency | [Voi99-U002](../audits/literature/Voi99/Yin_U002.md#voi99-u002) | Accepted unitary free Brownian motion in a free tracial extension and mean exp(-t/2), without re-auditing its original construction. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0186_v1.md#whole-candidate-finding) | Entire exact statement, complete unchanged argument and source interfaces; review act 2026-11-02T05:09 UTC, with the finding's actual primary-source and accepted-construction limits. |

## Source interfaces and scope

The repairing agent for Yin directly read the published Voi99, Definitions 5.3-5.5 and Corollary 5.7, printed pp.115-118, and Sections 12.1-12.7, printed pp.155-159, on 2026-11-02.
The [edition entrance](../audits/literature/Voi99/readme.md#yin-edition) identifies the inspected source.
Section 12.1 supplies the generic two-projection representation and the infinite-support criterion for algebraic freeness.
Lemma 12.2 and Sections 12.3-12.4 supply the diagonal/off-diagonal and moment mechanisms, which are verified directly below for this example.
Proposition 12.7 assumes an L3 Lebesgue density and obtains an L2 gradient.
Our density is not in L3, so that proposition is not invoked to establish (1); the full singular-density gradient identity is instead proved below.
This is a local source-interface deduction, not a claim that Voi99 already proves this extension.
A bounded source search on 2026-11-02 used two-projection liberation-gradient, Hilbert-transform, L1 and L3 terminology and led back to this primary-source interface.
No broader literature absence or priority conclusion is asserted.

## Candidate argument

### Actual represented algebras

The matrices are selfadjoint idempotents, and
\[
 xI_2=1-p-q+pq+qp,\qquad pq(1-p)=s e_{12}.
\]
The first identity generates the central \(L^\infty(\mu)\) algebra by functional calculus.
Since \(s\) is bounded away from zero on \([a,b]\), the second identity then gives all constant matrix units, proving \(W^*(p,q)=N\).
The measure has support \([a,b]\), an infinite set.
The criterion stated in Voi99 Section 12.1 therefore makes \(A,B\) algebraically free, so both liberation derivations below are well-defined on the represented algebra \(P\).

### Principal values and symmetric cutoffs

Write \(x=a+u\), \(0<u<L\), and \(\rho(u)=cu^{-\alpha}\).
For \(\varepsilon>0\), set
\[
 g_\varepsilon(a+u)=\int_{\substack{0<v<L\\|u-v|>\varepsilon}}
                  \frac{\rho(v)}{u-v}\,dv.
\]
The principal value exists at every interior point because \(\rho\) is smooth there.
Uniformly in \(\varepsilon\),
\[
 |g_\varepsilon(a+u)|\leq
 \begin{cases}
 Cu^{-\alpha},&0<u\leq L/2,\\
 C(1+|\log(L-u)|),&L/2\leq u<L.
 \end{cases}
 \tag{3}
\]
For the first bound, split at \(u/2\) and \(3u/2\).
On the middle interval, subtract \(\rho(u)\), whose symmetric cutoff integral is zero.
The derivative bound \(|\rho'(v)|\leq Cu^{-\alpha-1}\) bounds the remainder by \(Cu^{-\alpha}\).
The left part is bounded by \((2/u)\int_0^{u/2}\rho(v)dv\leq Cu^{-\alpha}\).
On the right, \(v-u\geq v/3\), so the bound follows from \(\int_{3u/2}^L v^{-\alpha-1}dv\leq Cu^{-\alpha}\).
For the second line, the part \(0<v<L/4\) has denominator bounded away from zero.
On \([L/4,L]\), subtract \(\rho(u)\); the density is Lipschitz there, so the divided remainder is bounded.
The constant-density integral has only a logarithmic boundary term at \(L-u\), also when the cutoff removes one of its sides entirely.

The bound (3) is integrable against \(d\mu(a+u)=cu^{-\alpha}du\), since \(2\alpha<1\).
It follows that \(g_\varepsilon\to g\) in \(L^1(\mu)\).
For every \(f\in C^1([a,b])\), symmetry of the cutoff kernel and then dominated convergence give
\[
 \begin{aligned}
 \int f g_\varepsilon\,d\mu
 &=\frac12\iint_{|x-y|>\varepsilon}
     \frac{f(x)-f(y)}{x-y}\,d\mu(x)d\mu(y),\\
 \int f g\,d\mu
 &=\frac12\iint
     \frac{f(x)-f(y)}{x-y}\,d\mu(x)d\mu(y).
 \end{aligned}
 \tag{4}
\]
The right integrand is bounded by \(\|f'\|_\infty\), and the diagonal has product measure zero.

There is also the exact scaling formula
\[
 g(a+u)=cu^{-\alpha}I(L/u),\qquad
 I(R)=\operatorname{pv}\int_0^R\frac{z^{-\alpha}}{1-z}\,dz.
\]
The tail at infinity is integrable because \(\alpha>0\).
Substitution \(z=1/r\) in the portion above one gives
\[
 I(\infty)=\int_0^1\frac{z^{-\alpha}-z^{\alpha-1}}{1-z}\,dz<0.
\]
The integrand is integrable at zero and one and is strictly negative since \(\alpha<1/2\).
Hence, for some \(\kappa>0\),
\[
 g(a+u)=-\kappa u^{-\alpha}(1+o(1))\quad(u\downarrow0).
 \tag{5}
\]
Thus \(g\in L^1(\mu)\setminus L^2(\mu)\), since \(2\alpha<1<3\alpha\).
On each \([a+u_0,b)\), \(u_0>0\), (3) gives membership in every finite \(L^r(\mu)\) space.

### Gradient identity for all algebra words

Write \(\lambda(m)=(\tau\otimes\tau)(\delta_{B:A}m)\), \(m_k=\int x^k d\mu(x)\), \(m_0=1\), and \(j_0=[p,q]g\).
The matrix \(j_0\) is skewadjoint with zero diagonal corners relative to \(p\), and \(|j_0|=s|g|I_2\).
In particular it belongs to L1 and not L2.
For every integer \(n\geq1\), the Leibniz rule gives
\[
 \delta_{B:A}((pq)^n)
 =\sum_{k=0}^{n-1}\left((pq)^{k+1}\otimes(pq)^{n-1-k}
             -(pq)^kp\otimes q(pq)^{n-1-k}\right).
\]
Taking traces, using \(\tau((pq)^r)=m_r/2\) for \(r\geq1\) and \(\tau(p)=\tau(q)=1/2\), gives
\[
 \begin{aligned}
 \lambda((pq)^n)
 &=\frac{m_n}{2}+\frac14\sum_{k=1}^{n-1}m_km_{n-k}
                  -\frac14\sum_{k=0}^{n-1}m_km_{n-1-k}\\
 &=\frac14\iint
  \frac{(x^{n+1}-x^n)-(y^{n+1}-y^n)}{x-y}\,d\mu(x)d\mu(y)\\
 &=\frac12\int g(x)(x^{n+1}-x^n)d\mu(x)
 =\tau(j_0(pq)^n).
 \end{aligned}
 \tag{6}
\]
This includes \(n=1\) with an empty first sum, without assuming a gradient exists.
The third line is (4), and the last equality is direct matrix multiplication.

For the remaining words, put \(r=pqp\).
Since \(\delta_{B:A}r=pq\otimes p-p\otimes qp\), direct expansion gives
\[
 \lambda(r^n)=\frac14\sum_{k=0}^{n-1}
       (m_{k+1}m_{n-1-k}-m_km_{n-k})=0\quad(n\geq1).
 \tag{7}
\]
The sums differ only by equal endpoint terms, and \(\lambda(p)=0\).
Replacing \(p\) by \(1-p\) proves the same assertion for \((1-p)q(1-p)\), with the moments of \(1-x\).
Reducing words by \(p^2=p,q^2=q\) shows that the two diagonal corners of \(P\) are spanned by these powers and their corner identities.
Thus both \(\lambda\) and pairing with \(j_0\) vanish on every diagonal corner.

The upper off-diagonal corner is spanned by
\[
 p(pq)^n(1-p)=x^{n-1}s e_{12},\qquad n\geq1,
\]
and the lower corner is its adjoint.
Indeed reducing alternating projection words leaves polynomial multiples of \(s e_{12}\) in the upper corner, and the displayed powers span them.
This also agrees with the exact basis reduction in Voi99 Section 12.3.
Subtracting the diagonal part from (6) proves the identity on the upper corner.
Anti-reality gives \(\lambda(m^*)=-\overline{\lambda(m)}\), and skewadjointness of \(j_0\) gives the same identity for its pairing, proving the lower-corner identity.
All four corners therefore give
\[
 \tau(j_0m)=(\tau\otimes\tau)(\delta_{B:A}m)\quad(m\in P).
 \tag{8}
\]
Finally \(\delta_{A:B}+\delta_{B:A}\) is the inner derivation \(m\mapsto m\otimes1-1\otimes m\), whose trace pairing is zero.
Therefore \(j(A:B)=-j_0\), establishing the full actual-gradient assertion (1).

### Exact Brownian moment and the matching coefficient

For a unitary \(V\) free from \(N\), expansion into centered factors and freeness give
\[
 \tau(VpV^*q)=|\tau(V)|^2\tau(pq)
            +(1-|\tau(V)|^2)\tau(p)\tau(q).
\]
The term with four alternating centered factors has trace zero, as do the terms containing a single centered factor from the unitary algebra.
Thus the source normalization gives the exact formula
\[
 \Lambda(t)=e^{-t}\frac{m_1}{2}+(1-e^{-t})\frac14
 =\frac{m_1}{2}+tD+O(t^2).
 \tag{9}
\]
Applying (4) to \(f(x)=x(1-x)\) gives
\[
 \int s^2g\,d\mu=\frac12-m_1,\qquad
 \frac12\tau([j,p]q)=\frac12\int s^2g\,d\mu=D.
 \tag{10}
\]
Here \(m_1=a+(1-\alpha)L/(2-\alpha)=19/32\), so \(D=-3/64\).

### Nonquadratic exponential remainder

Put \(h=sg\).
The actual generator \(j=-[p,q]g\) gives
\[
 e^{tj/2}=\begin{pmatrix}\cos(th/2)&-\sin(th/2)\\
                         \sin(th/2)&\cos(th/2)\end{pmatrix}.
\]
Direct multiplication yields
\[
 F(t)=\frac12\int\left[x+\frac{1-2x}{2}(1-\cos(th))+s\sin(th)\right]d\mu.
\]
By (10), \(F(t)-F(0)-tD=R_c(t)+R_s(t)\), where
\[
 R_c(t)=\frac14\int(1-2x)(1-\cos(th))d\mu,\qquad
 R_s(t)=\frac12\int s(\sin(th)-th)d\mu.
 \tag{11}
\]
Since \(1-2x=-2u\) and \(1-\cos z\leq z^2/2\),
\[
 |R_c(t)|\leq\frac{t^2}{4}\int u h^2d\mu=O(t^2).
 \tag{12}
\]
The last integral is finite: at zero its Lebesgue integrand is bounded by \(Cu^{1-3\alpha}\), with \(3\alpha<2\), and at the other endpoint only a logarithm is squared.

By (5), there are \(A_0,B_0,u_0>0\) such that
\[
 A_0u^{-\alpha}\leq-h(a+u)\leq B_0u^{-\alpha}\quad(0<u<u_0).
\]
On this interval \(\sin(th)-th\geq0\) for \(t>0\).
For small \(t>0\), restrict to \(t^{1/\alpha}\leq u\leq2t^{1/\alpha}<u_0\).
Then \(-th\) lies in the fixed compact interval \([A_0 2^{-\alpha},B_0]\subset(0,\infty)\).
The continuous function \(z-\sin z\) has a positive minimum there, and \(s\) has a positive lower bound.
The contribution of this interval to \(R_s\) is consequently at least
\[
 c_1\int_{t^{1/\alpha}}^{2t^{1/\alpha}}u^{-\alpha}du
 =c_2 t^{(1-\alpha)/\alpha}=c_2t^{3/2},\qquad c_2>0.
 \tag{13}
\]
The rest of \((0,u_0)\) contributes nonnegatively.
On \([u_0,L)\), (3) gives \(h\in L^3(\mu)\); the inequality \(|\sin z-z|\leq|z|^3/6\) therefore bounds the remaining contribution in absolute value by \(Ct^3\).
Hence \(R_s(t)\geq c_2t^{3/2}-Ct^3\).
Combining this with (12) proves the first assertion of (2).
Subtracting (9) gives \(F(t)-\Lambda(t)\geq c_2t^{3/2}-Ct^2\), so its quotient by \(t^2\) is unbounded as \(t\downarrow0\).
This proves the asserted failure for the fixed original-normalization word.

## Review and reliance boundary

The repairing agent for Yin developed and algebraically checked this argument.
The [independent whole-proof finding](../audits/reviews/Yin_R_F0186_v1.md#whole-candidate-finding), review act 2026-11-02T05:09 UTC, found no mathematical gap in the exact statement, complete argument and source interfaces.
The selected proved decision adopts that unchanged mathematical content while preserving the original candidate decision.
The safe L1 o(t) and sufficient L2 O(t^2) interfaces in Voi99-U003 remain valid.
The review does not re-audit the original free Brownian construction, the whole source, C_F0082/C_F0083, manuscripts or Task completion, and makes no novelty claim.

---
author: Yin
---
# An ergodic shift with a positive log-integrable weight admits an ACSY derivation exactly for constant weight

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(T\) be an invertible ergodic measure-preserving transformation of a probability space \((Y,\mu)\).
Write \(A=L^\infty(Y,\mu)\), \(\alpha(f)=f\circ T\), and let \(u\) implement \(ufu^*=\alpha(f)\) in the tracial crossed product \(P=A\rtimes_\alpha\mathbb Z\).
Suppose \(h\in A\) is bounded, strictly positive almost everywhere, and satisfies \(\log h\in L^1(Y,\mu)\).
Put \(X=uh,\ M=W^*(X)\subset P\), and give \(M\) the restricted canonical trace.
The weight \(h\) is almost everywhere constant if and only if \(X\) has the [actual ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Both are also equivalent to the existence of a complex-linear outer-bimodule derivation on the represented star algebra with
\[
  \delta:\mathbb C\langle X,X^*\rangle\longrightarrow L^2(M)\otimes_2 L^2(M),
  \qquad \delta X=1\otimes1.                                             \tag{1}
\]
The last condition allows arbitrary values on \(X^*\) and imposes no adjoint-domain or closability hypothesis.

There is an explicit nonconstant weight of diffuse law for which \(M=P\) is a \(\mathrm{II}_1\) factor and some bounded operator \(D\) on all of \(L^2(M)\) satisfies
\[
                 [L_X,D]=P_\Omega,\qquad P_\Omega(a)=\tau(a)1
                    \quad(a\in M).
\]
Thus the [full operator-and-adjoint domain and bare-domain conditions](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) both hold in this factor, while actual ACSY fails.

## Argument

### The derivatives forced by the two commuting squares for diffuse weight

Work in \(N=P\bar\otimes P^{\mathrm{op}}\), with product probability trace.
The linear isometry \(a\otimes b\mapsto a\otimes b^{\mathrm{op}}\) embeds the coarse bimodule of \(M\) into \(L^2(N)\), first on bounded elementary tensors and then by completion.
In this identification the two outer actions are left multiplication by \(\lambda_a=a\otimes1\) and \(\rho_b=1\otimes b^{\mathrm{op}}\), respectively.
Thus \(\rho_b\rho_c=\rho_{cb}\) and the two copies commute.
Let \(S_a=\lambda_a-\rho_a\), and view \(L^2(N)\) inside the [finite affiliated algebra](../audits/literature/MSY23/Yin_U004.md#ambient-algebra-domains-and-foundational-inputs) of \(N\).
All products of affiliated operators below are taken in this algebra.

First suppose (1) holds and the distribution of \(h\) is diffuse.
Put \(B=X^*X=h^2\), \(C=XX^*=\alpha(h^2)\).
The elements \(B,C\) commute and have the same diffuse law.
The differences \(\lambda_B-\rho_B,\ \lambda_C-\rho_B,\ \lambda_B-\rho_C\) are all invertible in the affiliated algebra.
Indeed each difference is the difference of independent selfadjoint variables in the two tensor legs, and the product of their diffuse laws gives zero mass to equality.
Its kernel projection consequently has trace zero, and [injectivity gives an affiliated inverse](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
Set \(K=S_B^{-1}\delta B\).
The map \(a\mapsto S_aK\) is an affiliated-valued outer derivation because \(S_{ab}=\lambda_a S_b+\rho_b S_a\).
Subtract it from \(\delta\) and call the resulting derivation \(d\), so \(dB=0\).
Differentiating \(BC=CB\) gives \(S_B dC=0\) and therefore \(dC=0\).
Differentiating \(XB=CX\) gives \((\lambda_C-\rho_B)dX=0\).
Likewise \(X^*C=BX^*\) gives \((\lambda_B-\rho_C)d(X^*)=0\).
The inverses just proved yield \(dX=d(X^*)=0\).
Writing \(S=S_X\) and \(b=\delta(X^*)\in L^2(N)\), we obtain
\[
                            SK=1,\qquad b=S^*K .
\]
The first identity makes \(S\) invertible by [direct finiteness of the affiliated algebra](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
Equivalently, the projection onto \(\ker S^*\) annihilates \(SK=1\), so the range support of \(S\) is one and its initial support is also one by the finite trace.
Thus \(KS=1\) and the necessary equation for the Hilbert vector \(b\) is
\[
                                   bS=S^*.                              \tag{2}
\]

### The itinerary of an arbitrary positive weight

For the general case put \(h_j=\alpha^j(h)\) for \(j\in\mathbb Z\).
The measurable itinerary \(y\mapsto(h_j(y))_{j\in\mathbb Z}\) has a shift-invariant ergodic law, being a factor of the original action.
This is a Borel probability on a countable product of bounded real intervals.
If it has a point atom, all points along that orbit have the same positive mass.
The orbit must then be finite and has full measure by ergodicity.
Otherwise two independent itineraries agree on a product-null set by Fubini, also after shifting either one by any fixed integer.

Suppose first that the itinerary law has no atoms.
The represented star algebra contains the commuting positive observables
\[
       B_k=(X^k)^*X^k=\prod_{j=0}^{k-1}h_{-j}^2,\qquad
       C_k=X^k(X^k)^*=\prod_{j=1}^k h_j^2,\qquad k\ge1.
\]
Also write \(B_0=C_0=1\).
The formulas follow by moving functions across \(u\), and consecutive ratios of the \(B_k\)'s and \(C_k\)'s recover every \(h_j^2\) since all the factors are positive almost everywhere.
Thus equality of every observable in this list at two points is equivalent to equality of the two itineraries off a fixed null set.
We again obtain (2), now using the whole list to replace the one diffuse observable in the preceding argument.

Enumerate the list as \(a_1,a_2,\ldots\) and set \(L_i=S_{a_i}\in A\bar\otimes A^{\mathrm{op}}\).
The supports of the \(L_i\) cover the unit of \(N\) because independent itineraries almost surely differ.
Choose disjoint projections \(p_i\) in this abelian product, given by the first index with \(L_i\ne0\) pointwise.
Choose positive scalars \(\gamma_i\) so that \(\sum_i\gamma_i(\|a_i\|+\|\delta a_i\|_2)<\infty\), for instance \(\gamma_i=2^{-i}/(1+\|a_i\|+\|\delta a_i\|_2)\).
Form
\[
          q=\sum_i\gamma_i p_iL_i,\qquad
          y=\sum_i\gamma_i p_i\delta a_i,\qquad K=q^{-1}y .
\]
The series for \(q\) converges in operator norm in the abelian base algebra, and \(q=\gamma_i L_i\ne0\) almost everywhere on each \(p_i\).
Thus \(q^{-1}\) exists in the affiliated algebra.
The series for \(y\) converges in \(L^2(N)\), with every cutoff to the left of its derivative.
Differentiating \(a_i a_j=a_j a_i\) gives \(L_i\delta a_j=L_j\delta a_i\).
Hence \(q\delta a_j=L_j y\) by the two convergent series and commutation of \(L_j\) with all \(p_i\).
Multiplying by \(q^{-1}\) from the left gives \(L_jK=\delta a_j\) for every \(j\).

As above, the affiliated-valued derivation \(d(a)=\delta a-S_aK\) now vanishes on every \(B_k,C_k\).
For each listed \(a\), both \(\alpha(a)\) and \(\alpha^{-1}(a)\) are ratios of strictly positive products of listed observables, by
\[
 \alpha(B_k)=C_1B_{k-1},\qquad \alpha(C_k)=C_{k+1}/C_1,\qquad
 \alpha^{-1}(C_k)=B_1 C_{k-1},\qquad \alpha^{-1}(B_k)=B_{k+1}/B_1 .
\]
To differentiate \(Xa=\alpha(a)X\), write \(\alpha(a)=n/v\) as displayed, taking \(v=1\) when no denominator occurs.
The represented polynomial identity \(vXa=nX\) only involves core elements and \(d\) kills \(v,a,n\).
Differentiating and canceling the injective \(\lambda_v\) in the affiliated algebra gives \((\rho_a-\lambda_{\alpha(a)})dX=0\).
Likewise \(X^*a=\alpha^{-1}(a)X^*\) gives \((\rho_a-\lambda_{\alpha^{-1}(a)})d(X^*)=0\) after clearing its displayed denominator.
The supports of the first differences cover the unit, since the itinerary at \(Ts\) and the independent itinerary at \(t\) agree with probability zero.
The same holds for the differences with \(T^{-1}s\).
Thus \(dX=d(X^*)=0\), with no differentiation of a measurable quotient.
The same argument from \(S K=1\) again gives \(bS=S^*\).

Suppose instead the itinerary law is supported on a finite orbit of period \(p\).
Then \(h_{j+p}=h_j\) almost everywhere for all \(j\), and the positive product \(\prod_{j=0}^{p-1}h_{-j}=a\) is constant by ergodicity.
Consequently \(X^p=a u^p\) with \(a>0\), and \(u^p\) commutes with \(u,h\) and their adjoints.
The central \(X^p\in W^*(X)\) has no mass at any critical value of \(z\mapsto z^p\), since for \(p>1\) the only such value is zero and \(a u^p\) is invertible.
The [central holomorphic polynomial theorem](Yin_C_F0204_v1.md#statement), in its Hilbert-derivation form, now makes \(X\) normal under (1).
Normality says \(h^2=\alpha(h^2)\), hence \(h\) is constant by positivity and ergodicity.

### The forced Fourier coefficients

Set \(h_j=h\circ T^j\), \(U=u\otimes1\), \(V=1\otimes u^{\mathrm{op}}\), and let \(s,t\) denote the two base variables.
Conjugation by \(U\) applies \(T\) to the first argument of a base function, and conjugation by \(V\) applies \(T^{-1}\) to its second argument.
Indeed \(u^{\mathrm{op}}a^{\mathrm{op}}(u^*)^{\mathrm{op}}=(u^*au)^{\mathrm{op}}\).
With both base coefficients written on the left this gives
\[
 S=h_1(s)U-h_0(t)V,\qquad
 S^*=h_0(s)U^{-1}-h_1(t)V^{-1}.                                        \tag{3}
\]
In the crossed-product trace the powers of the implementing unitary give orthogonal Fourier summands, with squared norm of \(a u^k\) equal to \(\int |a|^2\,d\mu\).
Finite Fourier sums are dense in the trace Hilbert space by the crossed-product construction.
Tensoring these decompositions gives the orthogonal expansion of \(b\) in coefficients times \(U^iV^j\), with sum of squared coefficient norms equal to \(\|b\|_2^2\).
Let \(f_k(s,t)\) be its coefficient at \(U^kV^{-2-k}\).
Since \(S\) is bounded and homogeneous of total degree \(1\), only this total-degree \(-2\) part of \(b\) contributes to the coefficients in (2) of total degree \(-1\).
For \(l\in\mathbb Z\) the coefficient at \(U^lV^{-1-l}\) gives
\[
 f_{l-1}(s,t)h_l(s)-f_l(s,t)h_{l+2}(t)
     =\mathbf1_{l=-1}h_0(s)-\mathbf1_{l=0}h_1(t).                     \tag{4}
\]
The first term comes from moving \(h_1(s)\) through \(U^{l-1}\), and the second from moving \(h_0(t)\) through \(V^{-2-l}\).
All equations hold simultaneously off one null set by countability.
Tonelli also gives \(\sum_k|f_k(s,t)|^2<\infty\) almost everywhere.

### An elementary recurrence argument on the product space

Write \(\phi=\log h\), \(\Theta(s,t)=(Ts,Tt)\), and \(F(s,t)=\phi(s)-\phi(T^2t)\).
For every \(\Theta\)-invariant measurable set \(E\) the two marginal densities of \(\mathbf1_E\,d(\mu\otimes\mu)\) are \(T\)-invariant by change of variables.
Ergodicity of \(T\) makes each density constant with value \((\mu\otimes\mu)(E)\).
It follows that \(\int_E F\,d(\mu\otimes\mu)=0\), including when \(\Theta\) itself is not ergodic.

We use the following elementary consequence of zero integrals on invariant sets.
Let \(Q\) be invertible and probability-preserving and \(F_0\) integrable with \(\int_E F_0=0\) for every \(Q\)-invariant set \(E\).
Then the sums \(S_nF_0=\sum_{j=0}^{n-1}F_0\circ Q^j\) tend to \(-\infty\) on a set of measure zero.
Indeed the set where that limit holds is invariant modulo null sets.
If it has positive measure, restrict to it with its normalized probability measure and let \(G=\sup_{n\ge0}S_n F_0\), including \(S_0F_0=0\).
Then \(G\) is finite, nonnegative and \(J=G-G\circ Q\ge F_0\).
In particular \(J^-\le F_0^-\) is integrable.
The difference \((G\wedge m)-(G\circ Q\wedge m)\) has mean zero by invariance, and each of its positive and negative parts increases to the corresponding part of \(J\).
Monotone convergence gives \(\int J^+=\int J^-<\infty\), so \(\int J=0=\int F_0\) and \(J=F_0\) almost everywhere.
This gives \(S_nF_0=G-G\circ Q^n\).
The claimed escape would imply \(G\circ Q^n\to+\infty\) almost everywhere on this restricted space, contradicting its fixed distribution and the finiteness of \(G\).

For \(l\ge1\), (4) gives
\[
   f_l=f_0\exp\!\left(\sum_{j=1}^l F\circ\Theta^j\right).
\]
The recurrence argument with \(Q=\Theta,\ F_0=F\), followed by the measure-preserving shift by \(\Theta\), excludes convergence of that exponent to \(-\infty\) almost everywhere.
Pointwise square summability of the coefficients would force that convergence on \(\{f_0\ne0\}\).
Hence \(f_0=0\) almost everywhere.
For \(n\ge1\) the homogeneous equations at \(l\le-2\) similarly give
\[
   f_{-2-n}=f_{-2}\exp\!\left(-\sum_{j=-n-1}^{-2}F\circ\Theta^j\right).
\]
Apply the same argument at \(\Theta^{-2}(s,t)\) with \(Q=\Theta^{-1}\) and \(F_0=-F\).
The inverse transformation has the same invariant sets, so the negative tail forces \(f_{-2}=0\) almost everywhere.
All divisions implicit in these recursions are legitimate since every translate of \(h\) is strictly positive and finite almost everywhere.

Now (4) at \(l=-1,0\) gives
\[
              -f_{-1}h_1(t)=h_0(s),\qquad
                f_{-1}h_0(s)=-h_1(t).
\]
These imply \(h_0(s)^2=h_1(t)^2\) for product-almost every \((s,t)\).
Two independent copies of a real random variable can agree almost surely only if its law is a point mass.
Indeed for every measurable value set of mass \(p\), the probability that the first value is in the set and the second is outside is \(p(1-p)\).
Thus the square of \(h\), and hence \(h\), is constant almost everywhere.
This is incompatible with a diffuse itinerary and completes necessity in all cases.

### Constant weights

When \(h=a>0\) is constant, \(X=au\) and \(W^*(X)=W^*(u)\) has the Haar circle model \(u(z)=z\).
The represented star polynomials are the Laurent polynomials in \(u\).
Set \(\delta p(z,w)=(p(z)-p(w))/(a(z-w))\) off the null diagonal.
The Laurent divided differences are bounded there, satisfy Leibniz, and \(\delta X=1\otimes1\).
The product Haar integral of \((z^k-w^k)/(z-w)\), for \(k\in\mathbb Z\), is zero except at \(k=1\) where it is one.
For \(k\ge1\) this follows from the finite geometric sum, and for \(k\le0\) from its negative-power version or simultaneous rotation of both variables.
Thus \(u/a\in L^2(W^*(u))\) represents the vacuum pairing on every Laurent polynomial with the inner product linear in its second entry.
This gives actual ACSY and proves sufficiency.

### A factor example with a bounded dual

Take \(Y=\mathbb R/\mathbb Z\) with Lebesgue probability measure and \(T(s)=s+\theta\) for an irrational \(\theta\).
For \(\varepsilon>0\) set \(g(s)=\exp(\varepsilon\cos(2\pi s))\),
\[
                    h=\alpha^{-1}(g)g^{-1},\qquad X=uh=gug^{-1}.
\]
Here \(g,g^{-1},h,h^{-1}\) are bounded and positive.
The function \(\log h=\varepsilon(\cos(2\pi(s-\theta))-\cos(2\pi s))\) is a nonzero first-harmonic sinusoid, with finite level sets, so \(h\) has diffuse law.
The action is ergodic because every nonconstant Fourier coefficient of an invariant function must vanish.
The obstruction just proved applies.

In fact \(X\) generates all of \(P\).
Its positive modulus is \(h\) and its polar unitary is \(u=Xh^{-1}\).
Then \(W^*(X)\) contains both \(\log h\) and \(\alpha(\log h)\).
These span the real linear space generated by \(\cos(2\pi s)\) and \(\sin(2\pi s)\), since \(2\pi\theta\) is not an integer multiple of \(\pi\).
Hence \(v(s)=e^{2\pi i s}\) belongs to \(W^*(X)\) and generates the entire base algebra.
For completeness, commuting with \(v\) forces the Fourier coefficient of a central element at \(u^k\) to vanish for every \(k\ne0\), by \(u^k v u^{-k}=e^{2\pi i k\theta}v\).
The remaining base coefficient must be invariant under \(T\), hence scalar.
Thus the generated algebra is a finite factor containing a diffuse abelian algebra, and so is of type \(\mathrm{II}_1\).

Let \(H=L^2(P)\) and \(H_0=L^2(W^*(u))\).
The powers \(u^n\), \(n\in\mathbb Z\), form an orthonormal basis of \(H_0\).
For the generator-first sign use the negative of the [positive-word deletion operator](../audits/literature/MSY23/Yin_U005.md#proposition-63-the-haar-example-and-its-sign), namely \(D_u(u^n)=-\mathbf1_{n\ge1}u^{n-1}\).
It has norm one and \(L_uD_u-D_uL_u=P_\Omega\) on \(H_0\) by the basis formula.
Extend \(D_u\) by zero on \(H_0^\perp\).
Both subspaces reduce \(L_u\), so the same identity holds on \(H\).
Use the [trace-preserving similarity on the trace Hilbert space](Yin_C_F0203_v1.md#transfer-of-the-holomorphic-moment-functional) given by \(W(a)=gag^{-1}\).
This operator and its inverse have norm at most \(\|g\|\|g^{-1}\|\), \(WL_uW^{-1}=L_X\), and \(WP_\Omega W^{-1}=P_\Omega\) since \(W1=1\) and conjugation preserves the trace.
Consequently \(D=WD_uW^{-1}\) is bounded on all of \(H\) with \([L_X,D]=P_\Omega\), and its actual adjoint has domain \(H\) as well.

## Provenance and scope

This argument addresses the single nonnormal generator in [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The obstruction uses only the represented relations of \(X\), its two squares, and the Fourier representation of the ambient crossed product.
The weighted-rotation model \(uf(v)\) is studied by Zhu, Fang and Shi in [arXiv:1411.0342v1](https://arxiv.org/abs/1411.0342v1).
The generation, factoriality and dual statements needed for this example were proved above.
The elementary recurrence argument supplies precisely the one-sided nonescape for the product action, including its possibly nonergodic case.
The factor example extends the [finite type I full-dual separation](Yin_C_F0133_v1.md#statement) to a different ambient type.
It leaves the general implication \(\mathsf A\Rightarrow\mathsf F\) open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:46 |
| status | open |
| reason | The classification for all positive log-integrable weights and the single-generator factor separation are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalence between constant weight, a normalized represented coarse derivation and actual ACSY, and a type II factor example with a bounded full-Hilbert-space dual. |
| argument | [Argument](#argument) | Diffuse-square and diffuse-itinerary implementers, finite-cycle centrality, necessary right equation, Fourier recurrence, two-sided nonescape, constant-weight vacuum, generation, factoriality and actual dual domains. |
| dependency | [Central polynomial theorem](Yin_C_F0204_v1.md#statement) | Its Hilbert-derivation conclusion under absence of mass at critical values, applied to the central monomial on a finite itinerary orbit. |
| dependency | [Finite affiliated inverses](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | The finite affiliated algebra, kernel criterion, equality of initial and final trace supports, and direct finiteness. |
| dependency | [Bounded Haar dual](../audits/literature/MSY23/Yin_U005.md#msy23-u005) | The rank-one commutator with its explicit generator-first sign on the one-unitary Fourier space. |
| dependency | [Trace-preserving similarity](Yin_C_F0203_v1.md#transfer-of-the-holomorphic-moment-functional) | The conjugation operator on the trace Hilbert space preserves the vacuum projection and transports a bounded commutator. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T15:09 |
| status | proved |
| reason | Adopt the ergodic weight classification and the factor example after the independent whole-proof check. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalence between constant weight, a normalized represented coarse derivation and actual ACSY, and a type II factor example with a bounded full-Hilbert-space dual. |
| argument | [Argument](#argument) | Diffuse-square and diffuse-itinerary implementers, finite-cycle centrality, necessary right equation, Fourier recurrence, two-sided nonescape, constant-weight vacuum, generation, factoriality and actual dual domains. |
| dependency | [Central polynomial theorem](Yin_C_F0204_v1.md#statement) | Its Hilbert-derivation conclusion under absence of mass at critical values, applied to the central monomial on a finite itinerary orbit. |
| dependency | [Finite affiliated inverses](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | The finite affiliated algebra, kernel criterion, equality of initial and final trace supports, and direct finiteness. |
| dependency | [Bounded Haar dual](../audits/literature/MSY23/Yin_U005.md#msy23-u005) | The rank-one commutator with its explicit generator-first sign on the one-unitary Fourier space. |
| dependency | [Trace-preserving similarity](Yin_C_F0203_v1.md#transfer-of-the-holomorphic-moment-functional) | The conjugation operator on the trace Hilbert space preserves the vacuum projection and transports a bounded commutator. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0227_v1.md#whole-proof-finding) | All four inputs, atomic and nonatomic itinerary branches, affiliated patching, Fourier tails and the full-domain factor example. |

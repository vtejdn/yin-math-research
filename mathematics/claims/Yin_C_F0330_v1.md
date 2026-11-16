---
author: Yin
---

# Exact free mixed moments up to prescribed alternating length with small liberation gradients

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

For every integer \(N\ge2\) and \(0<r<1/2\) there is an exchange-symmetric actual pair of Haar unitaries \(X,Y\) such that every alternating product of fewer than \(2N\) centered bounded Borel marginal functions has trace zero, whereas
\[
                            \tau((XY)^N)=r.                             \tag{1}
\]
In particular the two marginal algebras have product two-block trace.
All Gram inner products between linear combinations of words of at most \(N-1\) marginal blocks agree with those of two free Haar unitaries under the same marginal functions.
The joint liberation gradients \(\eta_j\) satisfy \(\|\eta_j\|_\infty\le4r\) and their left-right marginal spectral measures satisfy \(\nu_{\eta_j}\le8r^2 m^2\), where \(m\) is Haar probability.
In the same algebra there is a free Haar pair \(X,Y_f\) with \(\|Y-Y_f\|\le2r/N\).

On each one of these fixed pairs, evaluating the same Laurent words in the actual and the free pair gives no finite Hilbert norm comparison in either direction, with explicit polynomial norm ratios exponential in the number of factors.
Moreover, take the free first-coordinate right slice, or its [soft cutoff](Yin_C_F0245_v1.md#free-right-slices-at-a-fixed-cutoff) at any fixed positive radius, and evaluate its output words at the actual pair.
The resulting map, and its difference from the true slice at the same cutoff, are unbounded from the represented polynomial operator norm to the actual trace Hilbert norm.
The true slice and its cutoffs have uniform column bounds on these examples.

The same initial mixed moments can be realized with both marginal laws standard semicircular, the same liberation gradient bounds relative to their common law, and \(\|\xi_j-Z_j\|_2\le2\sqrt2\,r\) for the actual conjugate variables of that pair.
The two-sided failure of a Hilbert norm comparison persists on its ordinary starred polynomial core.
The calculation of the transported right slice concerns the Haar generators.

## Argument

### The first nonfree alternating product

Let \(X\) be Haar and free from a unitary \(V\) with circle law \(\rho\,dm\), where \(\rho(e^{i\theta})=1+2r\cos(N\theta)\), and put \(Y=X^*V\).
Then \(\tau(V^k)\) vanishes except for \(k=0,\pm N\), with \(\tau(V^{\pm N})=r\).
The smooth strictly positive density has an actual scalar divided-difference vacuum by the [scalar geometric criterion](Yin_C_F0255_v1.md#statement), since it has bounded maximal linear density and finite squared curvature.
The [Haar exchange calculation](Yin_C_F0315_v1.md#actuality-of-the-product-law) gives the Haar law of \(Y\) and the exchanging involution.
The [phase criterion](Yin_C_F0265_v1.md#statement) gives full actuality, since here the phase \(h(X)=X\) has divided-difference energy one.
In particular the two true right column costs in both orientations are uniformly bounded relative to their vacuum norms by the [uniform phase theorem](Yin_C_F0320_v1.md#statement).

First consider alternating nonzero powers of \(X\) and \(Y\), with fewer than \(N\) blocks of powers of \(Y\).
Substitute \((X^*V)^k\) for \(Y^k\) at \(k>0\) and \((V^*X)^{-k}\) at \(k<0\).
Within any such block, successive copies of \(V\) or \(V^*\) are separated by a nonzero \(X\)-power.
At a boundary \(Y^{k_1}X^lY^{k_2}\), \(l\ne0\), combine all adjacent \(X\)-powers.
For opposite signs of \(k_1,k_2\), the combined intervening exponent is \(l\), so opposite \(V\)-letters cannot cancel.
For two positive signs it is \(l-1\), and for two negative signs it is \(l+1\).
An empty intervening power in either case joins equal signs.
Consequently each joined \(V\)-power has nonzero exponent of absolute value at most the number of \(Y\)-blocks, since a single joined run uses at most one letter from each block.
After deleting empty initial or final \(X\)-powers, the remaining expression is a reduced product of centered powers in the free factors of \(X,V\), and has trace zero.
When there are no \(Y\)-letters the same assertion is the Haar trace identity.
Exchange proves the same vanishing whenever there are fewer than \(N\) blocks of \(X\).
An alternating word of length less than \(2N\) satisfies at least one of the two conditions.

Centered trigonometric polynomials follow by multilinearity.
For each fixed bounded centered Borel letter its Fejér means in the Haar marginal are centered, uniformly bounded and converge in trace Hilbert norm.
Telescoping a product with uniformly bounded other factors passes the trace identity to those letters.
For unrestricted bounded letters, successively splitting off scalar means and merging adjacent same-marginal factors shows that the free and actual traces agree through that block length.
This gives the Gram assertion after multiplying one word's adjoint by the other.
Equation (1) follows from \(XY=V\).

For the angular vacuum \(H=\xi_V V^*-1\), the [Fourier formula](Yin_C_F0316_v1.md#a-fourier-decomposition-of-the-terminal-derivative) gives \(H^*=r(V^{-N}-V^N)\).
Thus \(\|H\|_\infty\le2r\) and \(\|H\|_2^2=2r^2\), since \(\tau(V^{2N})=0\).
The [phase liberation formula](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) gives \(\eta_0=X^*HX-H\) and \(d\nu_{\eta_0}=\|H\|_2^2|z-w|^2dm^2\).
Exchange handles the second gradient, and the same phase criterion gives joint vacuum norm \(\sqrt{1+2r^2}\) at either Haar generator.
The increasing angular transformation
\[
                  \theta\longmapsto\theta+(2r/N)\sin(N\theta)
\]
has derivative \(\rho(e^{i\theta})\), so it sends \(\rho\,dm\) to Haar measure.
Writing \(V_f\) for the transform of \(V\) gives \(\|V-V_f\|\le2r/N\).
It is free from \(X\), and \(Y_f=X^*V_f\) is Haar free from \(X\) by [Haar absorption](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core).

### Word norms and the transported slice

In formal unitary variables \(a,b\) put \(v=ab\), \(w_j=a^j v^N a^{-j}\) for \(j\ge1\).
The Laurent word algebras in the free and actual representations are both faithful copies of the algebraic group algebra of two free generators.
Indeed the change \((a,b)\leftrightarrow(a,v)\) is invertible there, and the two Laurent factors of \(X,V\) are faithful by their infinite supports and embedded freely by their centered reduced-word representation.
The conjugate subalgebras \(a^j W^*(v)a^{-j}\) for distinct \(j\) are freely independent in each representation, by expanding centered alternating products with the intervening nonzero powers of the free Haar \(a\).
These are the [free conjugates used for word comparisons](Yin_C_F0245_v1.md#the-correlated-and-free-word-norms).

For \(0<d<1\) and either sign form a product of the \(n\) contractions \((1\pm d\,\operatorname{Re} w_j)/(1+d)\) in increasing order of \(j\).
Distinct free factors make its squared Hilbert norm the product of their squared Hilbert norms, by cycling off the square of the last factor under the trace and factoring across the preceding algebra.
The squared norm ratio of actual to free is consequently
\[
           \left(\frac{1\pm2dr+d^2/2}{1+d^2/2}\right)^n.
\]
The two signs preclude a uniform Hilbert norm comparison in either direction on the full word core.

Let \(P_n=n^{-1}\sum_{j=1}^n w_j\) and \(x_n=a(P_n-r)\).
The centered free-conjugate sum estimate in the cited word comparison is \(2\sqrt n\|x\|_2+\|x\|\) for the sum of \(n\) centered copies of \(x\).
It gives \(P_n(X,Y)\to r\) in operator norm and \(P_n(a,b)\to0\) in the free pair's operator norm.
Hence \(\|x_n(X,Y)\|\to0\).

At cutoff radius \(\epsilon>0\) write the Fourier coefficients of \(|z-w|^2/(|z-w|^2+\epsilon^2)\), a function of \(z/w\) on the unit circle, as \(d_l\).
They are absolutely summable, \(d_{-l}=d_l,\ d_0>0\) and \(\sum_l d_l=0\).
A first-coordinate cut of a group word in the free pair with suffix \(t\) contributes at index \(l\) only if \(t=a^l\), by the [free trace formula](Yin_C_F0245_v1.md#free-right-slices-at-a-fixed-cutoff).
In \(aw_j=a^{j+1}(ab)^N a^{-j}\) every cut before the final \(b\) has a reduced suffix containing \(b\), so none contributes.
For each negative cut in the final \(a^{-j}\), the selected \(l\) supplies the remaining power of \(a\), leaving the same output word \(w_{j+1}\) with a minus sign.
Thus word evaluation of the free cutoff slice at \(x_n\) gives
\[
         -n^{-1}\sum_{j=1}^n\left(\sum_{l=1}^j d_{-l}\right)w_{j+1}
                 -r d_0\,1 .
\]
Its trace in the actual pair tends to \(-r d_0/2\) because \(\tau(w_{j+1})=r\) and the partial coefficient sums tend to \(-d_0/2\).
For the unregularized slice the multiplier is one, and the output at \(x_n\) is exactly \(-r1\).
The finite Fourier selection for each cut makes the re-evaluated output a Laurent polynomial in both cases.
The actual right slice has finite column cost by (1) of the uniform phase theorem, and the [cutoff bound](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) costs at most three times the true column norm.
It follows that the corresponding actual slices send \(x_n(X,Y)\) to zero.
This proves both unboundedness assertions for each specified cutoff with the pair held fixed.

### Semicircular marginal coordinates

Let \(G\) be the cumulative distribution function of the standard semicircular law \(\mu_{\rm sc}\), and set \(S(e^{2\pi i t})=G^{-1}(t)\) on \(0<t<1\), with any endpoint value in \([-2,2]\).
The measurable inverse on conull sets is \(h(s)=e^{2\pi iG(s)}\), which is continuous and Lipschitz on \([-2,2]\) with Lipschitz constant at most two by the semicircular density.
Put \(Z_0=S(X),\,Z_1=S(Y)\).
Both marginal algebras and their centered elements are unchanged, so the finite-depth identities, exchange and the first nonfree cycle in their marginal unitaries persist.
Test polynomials in \(X,Y\) can be approximated in both operator norms by the same polynomials in \(Z_0,Z_1\), since \(h\) admits uniform polynomial approximation.
The Hilbert norm inequalities that fail on the Haar model would pass to these limits if they held for all ordinary polynomials in the semicircular marginal coordinates.

The scalar semicircular vacuum is \(Z_0\), and the phase energy of \(h\) is at most four.
The measurable phase criterion gives an actual distinguished derivative on \((Z_0,Y)\) with vacuum \(\xi_0\) projecting to \(Z_0\) on its marginal and satisfying \(\|\xi_0-Z_0\|_2^2=\|H\|_2^2J_\mu(h)\le8r^2\).
Restrict to \((Z_0,Z_1)\) by bounded strong-star approximation of \(S(Y)\) with omitted marginal polynomials killed by this derivation.
The resulting word values have the prescribed coarse derivatives by the product rule, on a core generating the same algebra, and the same vacuum represents the pairing.
Exchange gives actuality and the vacuum estimate at the second coordinate.
The [original-core transfer](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) and the uniform phase bound apply to this pair as well.
Its partial liberations still act by the inner difference on one marginal algebra and vanish on the other, by bounded marginal graph approximation, so their vacua are the same vectors as before.
Pushing the two-variable spectral measures forward by \(S\) on each leg preserves the stated domination with \(m^2\) replaced by \(\mu_{\rm sc}^2\).
This provides exact agreement with the free law at every prescribed finite alternating depth along with small bounded liberation gradients.
It leaves open whether small gradients suffice for the original unrestricted normal slice bounds.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:10 |
| status | open |
| reason | Fix the exact block-depth moment agreement and the full-core norm and transported-slice obstructions with arbitrarily small bounded liberation gradients. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact free moment depth, first nonfree cycle, small bounded gradients, exponential word norm differences, transported cutoffs and the semicircular marginal variant. |
| argument | [Argument](#argument) | Free-factor normal form, extension to bounded Borel letters, conjugate products and averages, every traced cutoff and the measurable marginal change. |
| dependency | [Scalar vacuum criterion](Yin_C_F0255_v1.md#statement) | Actuality of the diffuse product unitary with smooth positive density. |
| dependency | [Exchange of the Haar pair](Yin_C_F0315_v1.md#actuality-of-the-product-law) | Haar absorption, exchange automorphism and liberation on Borel marginal graph extensions. |
| dependency | [Phase criterion](Yin_C_F0265_v1.md#statement) | Actuality, strong domains and exact joint vacuum norm after the measurable scalar phase. |
| dependency | [Angular Fourier identity](Yin_C_F0316_v1.md#a-fourier-decomposition-of-the-terminal-derivative) | Actual centered angular vacuum of the specified density from its positive and negative Fourier modes. |
| dependency | [Liberation vacuum and law](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | The skew vacuum and its exact marginal spectral measure. |
| dependency | [Haar absorption](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | A free Haar variable multiplied on the left by a base unitary is Haar free from that base. |
| dependency | [Uniform true column cost](Yin_C_F0320_v1.md#statement) | Both true coordinate orientations in the phase model and the common Borel reparametrization. |
| dependency | [Free conjugate averages](Yin_C_F0245_v1.md#the-correlated-and-free-word-norms) | Faithful word comparison, free conjugate copies and their centered operator-norm sum bound. |
| dependency | [Free right-slice cutoffs](Yin_C_F0245_v1.md#free-right-slices-at-a-fixed-cutoff) | Fourier selection of the terminal suffix, symmetry and the coefficient sum for positive cutoff radii. |
| dependency | [True cutoff estimate](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Uniform boundedness of the true soft slices given finite true column cost. |
| dependency | [Core transfer](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Original represented cores and vacuum when replacing the omitted Haar generator by a generating Borel function. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:39 |
| status | proved |
| reason | Adopt the finite-depth moment and word-norm obstructions after complete independent review, including the exact scope of the fixed-radius computation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact free moment depth, first nonfree cycle, small bounded gradients, exponential word norm differences, transported cutoffs and the semicircular marginal variant. |
| argument | [Argument](#argument) | Free-factor normal form, extension to bounded Borel letters, conjugate products and averages, every traced cutoff and the measurable marginal change. |
| dependency | [Scalar vacuum criterion](Yin_C_F0255_v1.md#statement) | Actuality of the diffuse product unitary with smooth positive density. |
| dependency | [Exchange of the Haar pair](Yin_C_F0315_v1.md#actuality-of-the-product-law) | Haar absorption, exchange automorphism and liberation on Borel marginal graph extensions. |
| dependency | [Phase criterion](Yin_C_F0265_v1.md#statement) | Actuality, strong domains and exact joint vacuum norm after the measurable scalar phase. |
| dependency | [Angular Fourier identity](Yin_C_F0316_v1.md#a-fourier-decomposition-of-the-terminal-derivative) | Actual centered angular vacuum of the specified density from its positive and negative Fourier modes. |
| dependency | [Liberation vacuum and law](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | The skew vacuum and its exact marginal spectral measure. |
| dependency | [Haar absorption](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | A free Haar variable multiplied on the left by a base unitary is Haar free from that base. |
| dependency | [Uniform true column cost](Yin_C_F0320_v1.md#statement) | Both true coordinate orientations in the phase model and the common Borel reparametrization. |
| dependency | [Free conjugate averages](Yin_C_F0245_v1.md#the-correlated-and-free-word-norms) | Faithful word comparison, free conjugate copies and their centered operator-norm sum bound. |
| dependency | [Free right-slice cutoffs](Yin_C_F0245_v1.md#free-right-slices-at-a-fixed-cutoff) | Fourier selection of the terminal suffix, symmetry and the coefficient sum for positive cutoff radii. |
| dependency | [True cutoff estimate](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Uniform boundedness of the true soft slices given finite true column cost. |
| dependency | [Core transfer](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Original represented cores and vacuum when replacing the omitted Haar generator by a generating Borel function. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0336_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

---
author: Yin
---

# Exact energy criterion for a normal coordinate coupled to a free unitary by a Borel phase

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(A=W^*(Z)=L^\infty(\mu)\) for a bounded normal generator \(Z\) with compactly supported probability law \(\mu\) on the plane.
Let \(B=W^*(V)\) be free from \(A\) in their tracial free product \(M\), where \(V\) is a unitary with diffuse law and actual scalar divided-difference vacuum \(\xi_V\).
For any Borel \(h\) with \(|h|=1\) \(\mu\)-almost everywhere write \(h=h(Z)\), \(Y=h^*V\), and \(X=(Z,Y)\).
The tuple generates \(M\), since \(V=hY\) in its von Neumann algebra.
Use the represented starred polynomial core \(P_X\) and the [generator-first strong dual and actual ACSY conditions](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Then
\[
 \mathsf S(X)\ \Longleftrightarrow\ \mathsf A(X)\
 \Longleftrightarrow\
 \left\{\begin{array}{l}
 Z\text{ has an actual scalar divided-difference vacuum }\xi_\mu
 \text{ with diffuse law},\\[2pt]
 V\text{ is Haar, or }\displaystyle J_\mu(h):=\int_{z\ne w}
       \frac{|h(z)-h(w)|^2}{|z-w|^2}\,d\mu(z)d\mu(w)<\infty .
 \end{array}\right.                                                     \tag{1}
\]
In this case
\[
       \|\xi_{X,1}\|_2^2=\|\xi_\mu\|_2^2+
                      \int_{z\ne w}\|H\|_2^2
             \frac{|h(z)-h(w)|^2}{|z-w|^2}\,d\mu(z)d\mu(w),
                 \qquad H=\xi_V V^*-1 .                                \tag{2}
\]
The right contraction \(C\partial_i=(\mathrm{id}\otimes\tau)\partial_i\) has finite column cost at both coordinates and also for \(X^*=(Z^*,Y^*)\).
The column cost is the supremum of \((\sum_j\|C\partial_i p_j\|_2^2)^{1/2}\) over finite core columns satisfying \(\|\sum_jp_j^*p_j\|\le1\).
The negative closures on the original core give the strong duals.
The displayed criterion allows arbitrary measurable level sets of \(h\).
For example, the Poisson law \(w_r\,dm\) on the circle, with Haar probability \(m\), \(0<r<1\), and \(w_r(v)=(1-r^2)/|1-rv|^2\), gives \(\|H\|_2^2=2r^2/(1-r^2)^2\).
This gives genuinely correlated tuples for every nonconstant \(h\), since \(\mathbb E_A(Y)=r h^*\).
The previous [smooth triangular twist theorem](Yin_C_F0058_v1.md#1-a-precise-sufficient-class) treated \(C^1\) phases for actual unitary laws by placing the phase in both free derivative graphs.
Here the partial liberation formula tests all Borel phases, and the terminal estimate applies simultaneously to arbitrary finite columns.

At the second coordinate alone there is an actual normalized derivative with vacuum \(h^*\xi_V\) for every such \(Z,h\), where \(\xi_V\) is the scalar vacuum of \(V\).
Its original right slice has finite column cost even when the conditions at \(Z\) fail.
If the scalar right slice at \(V\) is Hilbert-space bounded, as for the Poisson law, the same holds for the original right slice at \(Y\).

## Argument

### The rotated unitary coordinate

Use the algebraic free product \(\mathcal Q\) of all bounded elements of \(A\) and the Laurent polynomials of \(V\).
It embeds in \(M\) by the orthogonal centered reduced-word representation and contains \(P_X\).
On \(\mathcal Q\) extend the ordinary scalar divided difference at \(V\) by zero on \(A\), denoting it by \(\partial_V^0\).
The scalar right slice \(E_V\) satisfies \(\|E_Vb\|_2\le a_V\|b\|\) on Laurent polynomials for some finite \(a_V\) by the [actual scalar theorem](Yin_C_F0055_v1.md#statement).
On \(\mathcal Q\) its free extension \(C\partial_V^0\) acts by copies of \(E_V\) on right-module coefficients.
Indeed, group each centered word by its prefix \(q\) ending in \(A^\circ=L^2(A)\ominus\mathbb C1\) or empty and its final, possibly scalar, \(B\)-factor \(b\).
Earlier \(V\)-cuts leave a nonempty centered suffix starting and ending outside \(B\) before \(b\), whose conditional expectation onto \(B\) is zero.
Thus \(C\partial_V^0(qb)=qE_V b\) by the [right-module decomposition](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core).
For a finite column of such inputs choose a common orthonormal prefix basis with finite expansions \(p_j=\sum_q q b_{jq}\), by orthonormalizing the finitely many bounded centered blocks in each factor and using their reduced products.
The conditional module identity gives \(\sum_{j,q}b_{jq}^*b_{jq}=\mathbb E_B(\sum_j p_j^*p_j)\).
The [commutative finite-family inequality](Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input), applied to the operator-norm extension of \(E_V\) on \(C^*(V)\), bounds \(\sum_{j,q}\|E_V b_{jq}\|_2^2\) by \(\kappa a_V^2\|\sum_j p_j^*p_j\|\), with \(\kappa=4/\pi\).
In particular the free vacuum is the same \(\xi_V\), by projection onto the vacuum-prefix summand.

For inner multiplication write \(I_{a\otimes b}(v\otimes w)=va\otimes bw\).
Set \(\partial_2=I_{h\otimes1}\partial_V^0\) on the target core.
The inner action commutes with both outer actions.
The assigned values are zero at \(Z,Z^*\), \(1\otimes1\) at \(h^*V\), and \(-Y^*\otimes Y^*\) at \(V^*h\), by the inverse rule.
In particular the normalization at \(Y\) uses the inner factor \(h\).
For every \(p\in P_X\) we have
\[
 C\partial_2 p=(C\partial_V^0p)h,\qquad
 (\tau\otimes\tau)\partial_2p=(\tau\otimes\tau)\partial_V^0(hp)
                    =\langle h^*\xi_V,p\rangle .
\]
The second equality uses cyclicity of the first-leg trace and \(\partial_V^0h=0\).
Here inner products are linear in their second argument.
Right multiplication by \(h\) is unitary, so the original right column cost is at most \(\sqrt\kappa a_V\).
If \(E_V\) is bounded on \(L^2(B)\), the orthogonal sum bound gives the same Hilbert norm upper bound \(\|E_V\|_{2\to2}\) on \(L^2(M)\).
The [Poisson density calculation](Yin_C_F0057_v1.md#2-a-free-reference-pair-with-bounded-duals) supplies this stronger bound for \(w_r\,dm\).
Restriction to Laurent polynomials in \(Y\) and projection of its vacuum give a scalar actual derivative at \(Y\), so its law is diffuse by [normal diffuseness](Yin_C_F0076_v1.md#statement).

### The base-coordinate vacuum and its inverse-gap energy

For this part assume \(\mu\) diffuse.
On \(\mathcal Q\) let \(\gamma^0\) take \(a\in A\) to \(a\otimes1-1\otimes a\) and kill the Laurent factor.
Let \(L\) kill \(A\), with \(L(V)=1\otimes V,\ L(V^*)=-V^*\otimes1\).
These are represented outer derivations by the free product and the Laurent inverse rule.
On the Laurent factor \(L=I_{1\otimes V}\partial_V^0\) by the generator values, whence
\[
             D b:=CL(b)=E_V(bV)-b,\qquad
             \tau(Db)=\langle \xi_V,bV\rangle-\tau(b)=\langle H,b\rangle .
\]
Here \(\tau(H)=0\), since \(D1=0\).
On \(\mathcal Q\) we have
\[
 (\gamma^0)^*(1\otimes1)=0,\qquad L^*(1\otimes1)=H,\qquad
 H=\xi_V V^*-1.
\]
Indeed the single-block identities follow from the preceding calculation and the zero double trace of an inner difference.
Each cut on a centered word of length at least two leaves a centered free segment on a trace leg.
This works for all bounded \(A\)-letters.
For the Poisson law the [explicit angular vacuum](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) is \(H=r(W-W^*)/(1-r^2)\), where \(W=(V-r)(1-rV)^{-1}\) is Haar, giving the stated norm.
More generally \(H=0\) if and only if \(V\) is Haar.
Writing \(m_n=\tau(V^n)\), one has \((\tau\otimes\tau)L(V^n)=\sum_{\ell=0}^{n-1}m_\ell m_{n-\ell}\) for \(n>0\).
Its vanishing gives \(m_n=0\) by induction, since \(m_0=1\).
Conversely for a Haar unitary both the positive and negative nonzero power double traces vanish by the Laurent rule, which proves \(H=0\) by density.

Define \(\gamma=\gamma^0+(I_{h\otimes h^*}-1)L\).
It has the prescribed inner difference at each base letter and kills \(h^*V\), since \(\gamma V=h\otimes h^*V-1\otimes V\).
The inverse rule gives \(\gamma Y^*=0\) as well.
Its restriction is therefore represented partial liberation on \(P_X\).
Cyclicity changes the double trace of \(I_{h\otimes h^*}L(p)\) to that of \(L(hph^*)\), giving \(\eta=\gamma^*(1\otimes1)=h^*Hh-H\) on the dense target core.
The map \(a\otimes b\mapsto aHb\) scales the coarse \(A\)-bimodule norm by \(\|H\|_2\), since freeness and centering give \(\langle aHb,a'Hb'\rangle=\|H\|_2^2\tau(a^*a')\tau(b^*b')\), first for centered bounded truncations of \(H\) and then by their \(L^2\) limit.
The left-right spectral measure of \(\eta\) is consequently \(\|H\|_2^2|h(z)-h(w)|^2\,d\mu(z)d\mu(w)\).
The [inverse-gap criterion](Yin_C_F0238_v1.md#statement) now proves the equivalence for \(\mathsf A\) and (2), since both marginals are diffuse and the second vacuum was established above.
In the necessary direction full actuality forces \(\mu\) diffuse as well.

### A global square-integrable kernel estimate for mixed columns

For \(k\in L^\infty(\mu^2)\) the inner spectral multiplier \(I_k\) is bounded on the coarse Hilbert space.
On \(\mathcal Q\), with \(D=CL|_B\), we prove
\[
 \left(\sum_j\|CI_k L(p_j)\|_2^2\right)^{1/2}
 \le L_V\|k\|_{L^2(\mu^2)}
               \left\|\sum_jp_j^*p_j\right\|^{1/2}.                    \tag{3}
\]
One may take \(L_V=2\sqrt\kappa(a_V+1)+2\|H\|_2\).
If \(D\) is Hilbert-space bounded one may instead take \(L_V=\|D\|_{2\to2}+2\|H\|_2\).
Thus the sliced map also has a column-norm limit for every \(L^2\) kernel by completion.
For such a kernel this statement defines a sliced limit and requires no unbounded coarse multiplier on arbitrary inputs.
The formula \(Db=E_V(bV)-b\) gives \(\|D:C^*(V)\to L^2(B)\|\le a_V+1\) and supplies the Hilbert bound whenever \(E_V\) has one.
Also \(\tau(Db)=\tau(bH^*)\).

Let \(\mathcal P_A\) denote the closed span of the empty word and the reduced words ending in \(A^\circ\), and let \(P_A\) be its orthogonal projection.
All words containing a \(B\)-block have the orthogonal tensor description
\[
                 \mathcal P_A\otimes B^\circ\otimes L^2(A),
                  \qquad q\otimes b\otimes a\longmapsto qba ,
\]
where \(B^\circ=L^2(B)\ominus\mathbb C1\).
Splitting \(a\) into mean and centered parts proves the identification by reduced words.
Its orthogonal complement is \(L^2(A)\).
Write \(O_k a(z)=\int k(z,w)a(w)\,d\mu(w)\), with \(\|O_k\|_{2\to2}\le\|k\|_2\).
For bounded reduced input blocks the last \(B\)-cut gives
\[
                     CI_k L(qba)=q(Db)(O_k a),\qquad CI_k L(a)=0.       \tag{4}
\]
For \(k=v\otimes e\), an earlier \(B\)-cut retains, after its right-leg \(B\)-coefficient, an alternating centered suffix starting in \(A^\circ\) and containing another centered \(B\)-block.
Its trace after left insertion of \(e\) and terminal multiplication by \(a\) vanishes by splitting the right-leg coefficient and the terminal \(a\) into mean and centered parts and using freeness, with trace cyclicity to combine the end \(A\)-factors.
At the last \(b\) the right trace on a \(B\)-coefficient \(d\) is \(\tau(e d a)=\tau(d)\tau(ae)\).
This proves (4) first for separated symbols.

Split \(Db=R b+\tau(Db)1\), with \(Rb=(Db)^\circ\).
When \(D\) is Hilbert-space bounded the centered output in (4) acts on the displayed tensor decomposition by \(\mathrm{id}\otimes R\otimes O_k\), and therefore has Hilbert norm at most \(\|D\|\|k\|_2\).
This bounds its column cost by the same constant since \(\sum_j\|p_j\|_2^2=\tau(\sum_jp_j^*p_j)\).

For general \(V\) take a finite separated kernel \(k(z,w)=\sum_{\ell=1}^N v_\ell(z)e_\ell(w)\) with bounded functions and \((e_\ell)\) orthonormal in \(L^2(A)\).
Finite bounded separated sums take this form by orthonormalizing second factors.
We apply the [triangular correction estimate](Yin_C_F0058_v1.md#4-the-triangular-correction-is-a-bounded-contraction) simultaneously to a finite column.
In the right \(B\)-module decomposition \(L^2(M)=\mathcal P_A\otimes L^2(B)\), let \(P_B\) retain the empty word and words ending in \(B^\circ\).
If \(p_j e=\sum_q q c_{jq}\) in an orthonormal reduced prefix basis, \(P_B\) replaces each \(c_{jq}\) at \(q\ne1\) by \(c_{jq}-\tau(c_{jq})\), leaving the coefficient at \(q=1\) intact.
For \(e\in A\) and a unit column \((p_j)\), the full coefficient column obeys
\[
    \sum_{j,q} c_{jq}^*c_{jq}=\mathbb E_B\!\left(e^*
                   \sum_j p_j^*p_j\,e\right)\le \|e\|_2^2 1 .
\]
Here \(\mathbb E_B(e^*e)=\tau(e^*e)1\) by freeness.
For bounded \(e\) the required expansion is finite using bases adapted to the finitely many input blocks.
The column of the removed scalar means has norm at most \((\sum_{j,q}\tau(|c_{jq}|^2))^{1/2}\le\|e\|_2\).
Hence the coefficients \(c'_{jq}\) of \(P_B(p_j e)\) have column norm at most \(2\|e\|_2\).
Apply \(R\) to every such terminal coefficient to form
\[
                  T_p e=\left(\sum_q q R(c'_{jq})\right)_j .
\]
This definition is independent of basis by the right-module identification and linearity of \(R\).
It takes values in the direct sum of \(m\) copies of the space of words ending in \(B^\circ\).
The finite-family inequality for \(R:C^*(V)\to B^\circ\) applied to all \(j,q\) shows
\(\|T_p e\|_2^2=\sum_{j,q}\|R(c'_{jq})\|_2^2\le4\kappa(a_V+1)^2\|e\|_2^2\).
It therefore extends boundedly from \(L^2(A)\).
For \(p_j=qba\), multiplication by \(e\) and the projection \(P_B\) retain \(qb\tau(ae)\).
For \(p_j\in A\) the projected scalar is killed by \(R1=0\).
The centered output of (4) is thus \(\sum_\ell(T_p e_\ell)v_\ell\).
Multiplication by the trailing \(A\)-variable is an isometry from the space of words ending in \(B^\circ\) tensored with \(L^2(A)\), by the right \(A\)-module representation.
The displayed sum consequently has norm at most \(\|T_p\|\|\sum_\ell e_\ell\otimes v_\ell\|_2\le2\sqrt\kappa(a_V+1)\|k\|_2\).

The scalar output on an arbitrary input \(p\in\mathcal Q\) is exactly
\[
                       \sum_{\ell=1}^N P_A(p e_\ell H^*)\,v_\ell.        \tag{5}
\]
Indeed for \(p=qba\), the centered part of \(a e_\ell\) leaves a word ending in the centered \(B\)-letter \(H^*\), which the projection kills.
The mean of \(a e_\ell\) leaves \(q bH^*\), with projection \(q\tau(bH^*)\).
For \(p\in A\) the projection also gives zero.

We bound (5) simultaneously for a column \(p=(p_j)_{j=1}^m\) with \(\|\sum p_j^*p_j\|\le1\).
Let \(K\) be the span, closed in the free Hilbert space, of the empty word and all centered reduced words ending in \(B^\circ\).
Right multiplication identifies \(L^2(M)=K\otimes L^2(\mu)\) by appending an uncentered \(A\)-block.
In this representation \(K=\mathbb C1\oplus K_0\), and
\[
               (P_A g)(z)=g(z)-P_{K_0}\int g(t)\,d\mu(t).               \tag{6}
\]
Indeed the discarded words are precisely \(K_0\otimes\mathbb C1\).
Freeness gives
\[
 \mathbb E_A\big((e_\ell H^*)^*(e_n H^*)\big)
       =\mathbb E_A(H e_\ell^* e_n H^*)=\|H\|_2^2\delta_{\ell n}1 ,
\]
by decomposing \(e_\ell^*e_n\) into its mean and centered part and using \(\tau(H)=0\).
For an unbounded \(H\in L^2(B)\) this identity holds in \(L^1(A)\) by centered bounded truncations and \(L^2\times L^2\) continuity into \(L^1\).
The same approximation gives (5) for every bounded input \(p\).
Hence the map \((f_\ell)_\ell\mapsto(\sum_\ell p_j e_\ell H^* f_\ell)_j\) on \(L^2(\mu;\mathbb C^N)\) has norm at most \(\|H\|_2\).
This follows by first multiplying into \(L^2(M)\) with norm \(\|H\|_2\) from the expectation identity and then applying the normalized left column.
In right-module coordinates its \(\ell\)-th column is the \(K^m\)-valued function \((p_j e_\ell H^*)_j(z)\).
The resulting matrix \(T(z):\mathbb C^N\to K^m\) has norm at most \(\|H\|_2\) almost everywhere.
To see this, test the integral bound on a constant vector times the indicator of an arbitrary measurable set and use a countable dense set of constant vectors.
Its average \(\int T(t)\,d\mu(t)\) has the same norm bound.
Applying (6) to each matrix column, the whole output (5) has fiber
\[
       \left(T(z)-P_{K_0^m}\int T(t)\,d\mu(t)\right)
                     (v_1(z),\ldots,v_N(z))^{\mathsf t}.
\]
Its \(L^2\) norm is at most \(2\|H\|_2\|k\|_2\) by orthonormality of the second factors.
This proves (3) for finite separated kernels.
For bounded Borel \(k\), conditional expectations on increasing finite rectangle partitions generating the spectral square give bounded separated kernels converging almost everywhere and in \(L^2(\mu^2)\).
The inner spectral measures on fixed coarse vectors are absolutely continuous with respect to \(\mu^2\), by the [coarse spectral measure calculation](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core).
Bounded convergence therefore identifies their sliced limit with \(CI_kL(p)\) on each original \(p\), proving (3) as asserted.

### Removing the cutoff on the target polynomial core

First suppose \(V\) is Haar.
The pair \(Y=h^*V,A\) then consists of a Haar generator free from the entire \(A\), for arbitrary measurable \(h\).
For a nonzero power of \(Y\) all intervening \(V\)-exponents have the same sign, so expanding the \(A\)-coefficients into means and centered parts gives zero trace.
For a cyclically alternating product of nonzero powers of \(Y\) separated by centered \(A\)-blocks, write \(Y=h^*V\), \(Y^{-1}=V^*h\).
At each change of sign the intervening \(A\)-coefficient is the centered separator or its conjugate by \(h\), hence has zero mean.
Within a power and at equal-sign junctions expanding the \(A\)-coefficients can only merge equal-sign \(V\)-exponents, which yields centered nonzero powers.
The trace of each expanded word vanishes by freeness, also when every intervening coefficient is scalar and all signs agree.
Cyclicity and centering of an end product reduce general alternating tests to these cyclic tests by induction on the number of blocks.
Thus the free actual estimates apply directly to \(X\) and its adjoint orientation if the base has an actual scalar vacuum, independently of \(J_\mu(h)\).

For non-Haar \(V\) suppose the two conditions on the right of (1) hold, and let \(\partial_1\) be the actual derivative just obtained.
Write \(u=z-w\), \(t_\epsilon=\bar u/(|u|^2+\epsilon^2)\), \(a_\epsilon=|u|^2/(|u|^2+\epsilon^2)\), \(k=(h(z)\overline{h(w)}-1)/u\) off the diagonal.
Then \(\|k\|_2^2=J_\mu(h)\).
On the target core we have \(\gamma=I_u\partial_1\), by the forced starred values and the product rule, so
\[
 CI_{a_\epsilon}\partial_1p
    =CI_{t_\epsilon}\gamma^0p+CI_{a_\epsilon k}L(p).
                                                                         \tag{7}
\]
Both symbols on the right are bounded for each fixed \(\epsilon>0\), since \(|h|=1\).
The second term has cost at most \(L_V\sqrt{J_\mu(h)}\) by (3).

For the first term start on the free reference core \(P_0=\mathbb C\langle Z,Z^*,V,V^*\rangle\), where \(\gamma^0=I_u\partial_Z^0\).
Extending the scalar vacua freely gives actual derivatives on this core by the [centered-word vacuum calculation](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
The reference right column cost \(c_0\) at \(Z\) is finite, with \(c_0\le12\|\xi_\mu\|_2\), by the [free estimate](Yin_C_F0162_v1.md#statement), part B, after [two-Haar column encoding](Yin_C_F0208_v1.md#statement).
The [uniform soft-cutoff estimate](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) gives cost at most \(3c_0\) for \(CI_{t_\epsilon}\gamma^0=CI_{a_\epsilon}\partial_Z^0\) there, independently of \(\epsilon\).

We transfer this bound for fixed \(\epsilon\) to \(P_X\).
Take uniformly bounded \(Z,Z^*\)-polynomials converging strongly-star to \(h\), using Kaplansky density and uniform approximation within \(C^*(Z)\).
Their \(\gamma^0\)-values converge in the coarse Hilbert norm to \(h\otimes1-1\otimes h\), and likewise for the adjoints.
Replacing \(h,h^*\) in \(Y,Y^*\) and applying the outer product rule gives entrywise bounded strong-star and \(\gamma^0\)-graph convergence on every target column and its adjoints.
For a unit column \(b\), write \(b_\lambda\) for these approximants and \(S_\lambda=b_\lambda^*b_\lambda\), \(S=b^*b\).
As in the [mixed-core column cutoff](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple), take a smooth real \(g\) equal to one near \([0,1]\) with \(\sqrt{s}|g(s)|\le1+\sigma\) for \(s\ge0\), for any fixed \(\sigma>0\).
The \(S_\lambda\) converge boundedly strongly-star with their graph values to \(S,\gamma^0 S\).
Approximate \(g\) in \(C^1\) on a fixed compact interval of spectra by polynomials.
Their outer divided differences acting on \(\gamma^0 S_\lambda\) compute the derivatives by the product rule, uniformly up to the first-derivative error.
For each fixed approximating polynomial the outer actions converge strongly, and \(g^{[1]}\) vanishes on \([0,1]^2\).
Consequently the approximations to \(b_\lambda g(S_\lambda)\) in \(P_0\) converge to \(b\) in the entrywise \(\gamma^0\)-graph with limsup column norm at most \(1+\sigma\).
Apply the reference estimate along these columns using boundedness of \(I_{t_\epsilon}\), then let \(\sigma\) decrease to zero.
This gives the first term of (7) cost at most \(3c_0\) on \(P_X\).
The argument only approximates \(h\) for the inner difference \(\gamma^0\).
Since \(a_\epsilon\to1\) off the diffuse diagonal, \(I_{a_\epsilon}\partial_1 p\to\partial_1 p\) strongly on each fixed coarse input.
Taking this limit on each finite target column gives
\[
     c_1(X)\le 3c_0+L_V\sqrt{J_\mu(h)}.                                  \tag{8}
\]

### Adjoints and the strong duals

Conjugating the entire adjoint tuple by the unitary \(h\) fixes \(Z^*\) and sends \(Y^*=V^*h\) to \(hV^*\).
With base \(Z^*\), take the phase \(\widetilde h(z)=\overline{h(\bar z)}\) and the free unitary \(V^*\), whose scalar vacuum is \(\xi_V^*\) by flip-adjoint conjugation.
Then \(\widetilde h(Z^*)^*V^*=hV^*\), and its phase energy against the conjugated measure equals \(J_\mu(h)\).
The scalar adjoint-coordinate vacuum is \(\xi_\mu^*\) by flip-adjoint conjugation.
The preceding bounds therefore apply to the original right contractions in the adjoint orientation as well, since inner conjugation is a trace-preserving spatial isomorphism.
On \(P_X\), the adjoint-orientation derivative is \(\epsilon_i(p)=(\partial_i(p^*))^\dagger\), where \((a\otimes b)^\dagger=b^*\otimes a^*\).
This follows from the [forced normal generator values](Yin_C_F0076_v1.md#statement) and the Leibniz rule.
Thus a one-input bound on \(C\epsilon_i\) also bounds the original left contraction \((\tau\otimes\mathrm{id})\partial_i\).
The [two-contraction domain theorem](Yin_C_F0072_v1.md#statement) now places \(M1\) in the domains of the original closure of \(C\partial_i\) and its Hilbert adjoint.
On the core its commutator with left multiplication by \(X_j\) is \(\delta_{ij}P_1\) in operator-first order by the product rule.
For any vector in the closure domain, graph approximation and boundedness of \(X_j,P_1\) extend this commutator identity, in particular on \(M1\).
Negating the closures gives the generator-first commutators in \(\mathsf S\).
Conversely [the normal strong-to-actual implication](Yin_C_F0070_v1.md#statement), part C, gives \(\mathsf A\) from \(\mathsf S\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:07 |
| status | open |
| reason | Fix the Borel-phase criterion and the square-integrable terminal-kernel column estimate for independent proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both original conditions for the phase-rotated pair, its base vacuum norm, the unitary-coordinate conclusions and the two orientations. |
| argument | [Argument](#argument) | Free marked terminal block, conditional right-module compression, uniform soft-cutoff transfer and canonical full domains. |
| dependency | [Poisson marginal](Yin_C_F0057_v1.md#2-a-free-reference-pair-with-bounded-duals) | Poisson moments and the Hilbert-bounded scalar right slice at the unitary. |
| dependency | [Free right-module decomposition](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Orthogonal free prefixes with an uncentered terminal marginal and their conditional inner products. |
| dependency | [Commutative finite-family inequality](Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input) | The little Grothendieck estimate on the unitary marginal for all finite families of terminal coefficients. |
| dependency | [Actual scalar estimate](Yin_C_F0055_v1.md#statement) | Operator-norm-to-Hilbert bound for the right slice of an arbitrary actual scalar unitary. |
| dependency | [Triangular terminal correction](Yin_C_F0058_v1.md#4-the-triangular-correction-is-a-bounded-contraction) | The centered coefficient and deletion-of-the-last-block argument, here applied to all input entries simultaneously. |
| dependency | [Poisson phase vacuum](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Tangential derivative and its bounded centered marginal vacuum with exact norm. |
| dependency | [Normal starred values](Yin_C_F0076_v1.md#statement) | Marginal diffuseness, the original forced phases and flip-adjoint orientation. |
| dependency | [Inverse-gap criterion and cutoff](Yin_C_F0238_v1.md#statement) | Represented liberation, scalar and joint vacuum norm, product-law domination and the uniform reference bound for soft cutoffs. |
| dependency | [Free actual column control](Yin_C_F0208_v1.md#statement) | Free preservation of the vacuum and reduction of old column tests to one input. |
| dependency | [Free one-input estimate](Yin_C_F0162_v1.md#statement) | Part B on the augmented free reference with the old base vacuum. |
| dependency | [Graph column cutoff](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Smooth normalization of bounded strong-star column approximants in an outer derivation graph. |
| dependency | [Canonical domain theorem](Yin_C_F0072_v1.md#statement) | Both original bounded-vector domains from the two contraction estimates. |
| dependency | [Normal strong-to-actual theorem](Yin_C_F0070_v1.md#statement) | Converse from a supplied generator-first dual system with the vacuum in its adjoint domains. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:15 |
| status | proved |
| reason | The independent review verifies the equivalence on the entire Borel-phase family and both original canonical domains. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both original conditions for the phase-rotated pair, its base vacuum norm, the unitary-coordinate conclusions and the two orientations. |
| argument | [Argument](#argument) | Free marked terminal block, conditional right-module compression, uniform soft-cutoff transfer and canonical full domains. |
| dependency | [Poisson marginal](Yin_C_F0057_v1.md#2-a-free-reference-pair-with-bounded-duals) | Poisson moments and the Hilbert-bounded scalar right slice at the unitary. |
| dependency | [Free right-module decomposition](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Orthogonal free prefixes with an uncentered terminal marginal and their conditional inner products. |
| dependency | [Commutative finite-family inequality](Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input) | The little Grothendieck estimate on the unitary marginal for all finite families of terminal coefficients. |
| dependency | [Actual scalar estimate](Yin_C_F0055_v1.md#statement) | Operator-norm-to-Hilbert bound for the right slice of an arbitrary actual scalar unitary. |
| dependency | [Triangular terminal correction](Yin_C_F0058_v1.md#4-the-triangular-correction-is-a-bounded-contraction) | The centered coefficient and deletion-of-the-last-block argument, here applied to all input entries simultaneously. |
| dependency | [Poisson phase vacuum](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Tangential derivative and its bounded centered marginal vacuum with exact norm. |
| dependency | [Normal starred values](Yin_C_F0076_v1.md#statement) | Marginal diffuseness, the original forced phases and flip-adjoint orientation. |
| dependency | [Inverse-gap criterion and cutoff](Yin_C_F0238_v1.md#statement) | Represented liberation, scalar and joint vacuum norm, product-law domination and the uniform reference bound for soft cutoffs. |
| dependency | [Free actual column control](Yin_C_F0208_v1.md#statement) | Free preservation of the vacuum and reduction of old column tests to one input. |
| dependency | [Free one-input estimate](Yin_C_F0162_v1.md#statement) | Part B on the augmented free reference with the old base vacuum. |
| dependency | [Graph column cutoff](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Smooth normalization of bounded strong-star column approximants in an outer derivation graph. |
| dependency | [Canonical domain theorem](Yin_C_F0072_v1.md#statement) | Both original bounded-vector domains from the two contraction estimates. |
| dependency | [Normal strong-to-actual theorem](Yin_C_F0070_v1.md#statement) | Converse from a supplied generator-first dual system with the vacuum in its adjoint domains. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0274_v1.md#finding) | The free end-module estimate, both orientations, the Haar exception and the thirteen declared input interfaces. |

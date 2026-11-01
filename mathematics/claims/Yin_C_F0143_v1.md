---
author: Yin
---
# An actual normal vacuum can coexist with divergent curvature compositions

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

There is a compactly supported nonatomic scalar normal probability law \(\mu\), with its full-star-algebra actual ACSY vacuum in \(L^2(\mu)\) and both canonical bounded-vector domains, for which the total Menger curvature is finite but the associated nonnegative symmetric kernel
\[
 g(z,v)=\int\mathfrak c(z,w,v)^2d\mu(w)
\]
has the following properties.

1. Its integral operator has no bounded \(L^2(\mu)\) extension; no positive integer composition power has uniform row \(L^1\) or row \(L^2\) bounds.
2. Its fourth composition \(g^{\circ4}\) is infinite on a set of positive \(\mu^2\) measure.
3. Although \(g\notin L^2(\mu^2)\), the weighted difference \((z-v)g\) is a Hilbert tensor.
   The real derivation \(\beta_g f(z,v)=\mathrm i(f(z)-f(v))g(z,v)\) on the original star polynomial core is closable and has actual vacuum zero.
4. The contraction
\[
 C_0f(z)=\int(f(z)-f(v))g(z,v)d\mu(v)
\]
is a positive symmetric densely defined operator on that core, but has no bound from its operator norm to \(L^2(\mu)\).
Neither its original closure nor its actual adjoint has domain containing all of \(L^\infty(\mu)\).

These statements use the radius-atom model already constructed in C_F0047, at the specific parameter \(b=3/4\).
They do not separate the normal actual-vacuum and strong-domain conditions: the original normal canonical operators have both all-bounded-vector domains.
The obstruction concerns automatic raw-curvature iteration and absolute bounds for the auxiliary weighted contraction.
Its positive quadratic form has the favorable sign in the scalar normal mixed-energy identity.

## Argument

The following obstruction reuses the already reviewed radius-atom model of [C_F0047, Section 7](Yin_C_F0047_v1.md#7-a-countable-haar-circle-example-with-an-unbounded-hilbert-dual).
A targeted local search for shrinking/disjoint circles, curvature composition and kernel powers found that exact existing model; no new joint law or independent source theorem is needed.
Its consequence below concerns the curvature method, not failure of the Task.

Fix \(b=3/4\), \(s=2^{-b}\), \(r_n=2^{-n}\), and \(p_n=(1-s)s^{n-1}\), \(n\ge1\).
Let \(\sigma_n\) be normalized Haar measure on the circle of radius \(r_n\), and
\[
 \mu=\sum_{n\ge1}p_n\sigma_n,\quad
 M=L^\infty(\mu),\quad Z(z)=z.
\]
The compact support includes the accumulation point zero but has no atom there.
C_F0047 gives the actual scalar ACSY vacuum
\[
 \xi(r_ne^{i\theta})
 =\frac{(1+s)s^{n-1}}{r_n}e^{i\theta},
 \qquad
 \|\xi\|_2^2=
 \frac{4(1-s)(1+s)^2}{1-4s^3}<\infty,
\]
and both original canonical bounded-vector domains.
The denominator is positive because \(b>2/3\).
The full-star-algebra outer derivative is the scalar divided difference normalized by \(\delta Z=1\otimes1\).
The actual vacuum and C_F0055's soft Cauchy argument also give finite total Menger curvature: \(\int\mathfrak c^2\,d\mu^3<\infty\).
Thus this is an actual scalar model with the relevant domain/vacuum assumptions, not an arbitrary abstract spectral weight.

Put
\[
 g(z,v)=\int\mathfrak c(z,w,v)^2d\mu(w),\qquad
 \lambda_n=p_n^2/r_n^2.
\]
For almost every pair \(z,v\) on circle n, all distinct triples from that same circle have curvature \(1/r_n\), so
\[
 g(z,v)\ge p_n/r_n^2.
 \tag{O1}
\]
Consequently the nonnegative integral kernel \(T_g\) has \(\langle p_n^{-1/2}1_{\{|z|=r_n\}},T_g(p_n^{-1/2}1_{\{|z|=r_n\}})\rangle\ge\lambda_n\).
Here \(\lambda_n\) tends to infinity because \(b<1\).
The form is well-defined as a nonnegative extended integral; the lower bound alone rules out a bounded L2 integral operator.
More generally, for every integer \(k\ge1\), Tonelli and integration with all intermediate variables on circle n give
\[
 g^{\circ k}(z,v)\ge
 (p_n/r_n^2)^k p_n^{k-1}\quad(z,v\text{ on circle }n).
 \tag{O2}
\]
Its row integral over circle n is at least \(\lambda_n^k\).
Hence no fixed composition power has a uniform row-L1 or row-L2 bound.

There is a stronger divergence statement.
Choose two closed angular arcs A and B of positive angular measure on the outer circle, centered for example at \(r_1\) and \(\mathrm i r_1\), and sufficiently small that every triangle with one point in A, one in B and third point zero is noncollinear.
By continuity and compactness, there exist \(c_0>0\) and \(\varepsilon>0\) such that \(\mathfrak c(z,t,w)^2\ge c_0\) for \(z\in A,t\in B,|w|\le\varepsilon\).
Here all three points remain uniformly distinct.
Therefore
\[
 g(z,w)\ge c:=p_1\sigma_1(B)c_0>0
 \quad(z\in A,\ w\text{ on circle }n,\ n\ge n_0).
 \tag{O3}
\]
Symmetry gives the same lower bound with the arguments reversed.
For \(z,v\in A\), restrict each of the three intermediate variables of \(g^{\circ4}(z,v)\) to the same circle n.
These product regions are disjoint as n varies.
Equations (O1) and (O3) imply
\[
 g^{\circ4}(z,v)
 \ge c^2\sum_{n\ge n_0}(p_n/r_n^2)^2p_n^3
 =c^2\sum_{n\ge n_0}p_n\lambda_n^2=\infty.
 \tag{O4}
\]
The summands are a fixed positive constant times \(2^{(4-5b)n}\); at \(b=3/4\) this exponent is \(1/4>0\).
Hence the fourth composition is infinite on the positive-\(\mu^2\)-measure set \(A\times A\), even though the original total curvature is finite.
This disproves automatic smoothing or finiteness of raw curvature powers from the actual scalar vacuum/finite-curvature premise.

### The actual weighted contraction is unbounded but its quadratic form is positive

The same example also separates an absolute contraction bound from the lower quadratic bound needed in the normal mixed-energy argument.
In the scalar algebra \(M=N\), the unweighted liberation derivation is the full inner one and its vacuum is zero.
The curvature weight need not be Hilbert:
\[
 \int g^2d\mu^2\ge\sum_n p_n^4/r_n^4=\infty.
\]
However \(h(z,v)=(z-v)g(z,v)\) belongs to \(L^2(\mu^2)\).
Indeed conditional Jensen and \(|z-v|\mathfrak c(z,w,v)\le2\) give
\[
 \|h\|_2^2
 \le\int |z-v|^2\mathfrak c(z,w,v)^4d\mu^3
 \le4\int\mathfrak c^2d\mu^3<\infty.
 \tag{O5}
\]
Thus on the original star polynomial core
\[
 \beta_g f(z,v)=\mathrm i(f(z)-f(v))g(z,v),\qquad
 C_0f(z)=\int(f(z)-f(v))g(z,v)d\mu(v)
 \tag{O6}
\]
are actual Hilbert-space operators, with \(\beta_g\) an outer real derivation and \(E_{g,0}=\mathrm iC_0\) its right contraction.
Polynomial Lipschitz constants and (O5) prove their Hilbert values.
Symmetry makes every vacuum pairing vanish, so \(1\otimes1\in\operatorname{Dom}\beta_g^*\) with actual vacuum zero.
The standard real-derivation pairing therefore proves closability and \(E_{g,0}^*f=-E_{g,0}f\) on the core.

For real f in this core the actual scalar pairing is
\[
 \langle f,C_0f\rangle
 =\tfrac12\int|f(z)-f(v)|^2g(z,v)d\mu(z)d\mu(v)\ge0.
 \tag{O7}
\]
All integrals are finite, by boundedness/Lipschitz continuity and finite total curvature.

For each n choose a real smooth plane function \(f_n\), supported in an annulus meeting no circle other than n, whose restriction there is \(\cos\theta\).
It is zero on all other circles, so \(\|f_n\|_{L^\infty(\mu)}=1\) and \(\|f_n\|_2^2=p_n/2\).
Uniform C1 polynomial approximation on a rectangle containing the support, together with (O5), places this function in the original closure of \(\beta_g\) and \(C_0\), with precisely the integral values (O6).
This uses the same accepted VV16 C1 approximation interface as C_F0055; alternatively the elementary Bernstein construction retained there supplies these approximants.

The same pairing formula and the same-circle lower bound give
\[
 \langle f_n,\overline{C_0}f_n\rangle
 \ge\frac{p_n^3}{2r_n^2},\qquad
 \|\overline{C_0}f_n\|_2
 \ge\lambda_n\sqrt{p_n/2}\longrightarrow\infty.
 \tag{O8}
\]
The square of the latter lower bound is \(p_n^5/(2r_n^4)\), again growing as \(2^{(4-5b)n}\).
Consequently \(C_0\) has no operator-norm-to-L2 bound even on its original polynomial core: such a bound would pass to each \(f_n\) through the uniform/C1 graph approximants.
Neither its original closure nor its actual adjoint can contain all of \(M\), since either inclusion would imply a Banach closed-graph bound from \(M\) with its operator norm to \(H\), and the adjoint restricts to \(C_0\) on the core.

The scalar normal canonical operators themselves still have their established all-M domains.
The weighted mixed-defect contraction \(C_0\) is positive in the sense (O7), so it has the favorable sign in the normal energy identity despite being unbounded from the operator norm to L2.
Thus the general remaining target should not demand an absolute bound for this weighted contraction: a lower bound for its negative quadratic part can be strictly weaker and is the relevant unresolved correlated estimate.
The example is a counterexample to the proposed automatic curvature-composition/contraction method, not to \(\mathsf A\Rightarrow\mathsf S\).


## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:44 |
| status | open |
| reason | Complete actual scalar obstruction to automatic curvature composition and absolute weighted-contraction bounds, with the original normal full-domain conclusion explicitly preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact scalar actual-vacuum model, divergent fourth kernel composition and unbounded positive auxiliary contraction; no separation of the normal hypotheses. |
| argument | [Argument](#argument) | Radius-law specialization, same-circle lower bounds, disjoint fourfold integration regions, actual weighted vacuum and graph-core tests. |
| dependency | [Radius-atom model](Yin_C_F0047_v1.md#7-a-countable-haar-circle-example-with-an-unbounded-hilbert-dual) | At b=3/4, the exact compact scalar law, actual L2 vacuum and both original canonical bounded-vector domains. |
| dependency | [Soft Cauchy estimate](Yin_C_F0055_v1.md#statement) | Section 5 actual scalar vacuum implies finite total marginal Menger curvature; the whole-star premise is supplied by C_F0047. |
| dependency | [C1 polynomial approximation](../audits/literature/VV16/Yin_U001.md#vv16-u001) | Uniform function and first-derivative approximation on a rectangle, used only to put the smooth annular tests in the original weighted contraction graph. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:51 |
| status | proved |
| reason | Adopt the complete actual scalar obstruction after R_F0150 checked all kernel lower bounds, actual original-core domains, the positive unbounded contraction, and the explicit nonseparation boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact scalar actual-vacuum model, divergent fourth kernel composition and unbounded positive auxiliary contraction; no separation of the normal hypotheses. |
| argument | [Argument](#argument) | Radius-law specialization, same-circle lower bounds, disjoint fourfold integration regions, actual weighted vacuum and graph-core tests. |
| dependency | [Radius-atom model](Yin_C_F0047_v1.md#7-a-countable-haar-circle-example-with-an-unbounded-hilbert-dual) | At b=3/4, the exact compact scalar law, actual L2 vacuum and both original canonical bounded-vector domains. |
| dependency | [Soft Cauchy estimate](Yin_C_F0055_v1.md#statement) | Section 5 actual scalar vacuum implies finite total marginal Menger curvature; the whole-star premise is supplied by C_F0047. |
| dependency | [C1 polynomial approximation](../audits/literature/VV16/Yin_U001.md#vv16-u001) | Uniform function and first-derivative approximation on a rectangle, used only to put the smooth annular tests in the original weighted contraction graph. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0150_v1.md#conclusion) | Whole statement and argument with all three direct inputs; this rejects the indicated auxiliary estimates, not the normal A-to-S implication. |


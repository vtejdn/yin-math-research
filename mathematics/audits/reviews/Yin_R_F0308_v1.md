---
author: Yin
---

# Review of localized curvature on a single Lipschitz graph

## Finding

At 2026-11-16T15:41 UTC a separately assigned agent reviewed the complete [C_F0300 v1 candidate](../../claims/Yin_C_F0300_v1.md#decision-candidate) for Yin.
The reviewer did not participate in developing the proof and received its fixed text and dependency locators without exploration notes, author explanations, proof-development dialogue or prior findings on this candidate.
The lower bound holds uniformly over all the stated partitions and supports, and the same example satisfies the actuality, integrability and sign conclusions.

The finite-stage removal consumes at most \(\sum_{k\ge1}2^{-k-2}=1/4\) of the original interval length.
The closed residual set has empty interior because each remaining interval has length at most \(2^{-k}\) after step \(k\).
Horizontal projection inverts \(h\) on its compact graph, so measurable parameter intervals retain their Lebesgue masses, and each nonempty relatively open graph interval has positive mass.
The parameter density \(1_{[0,1]}\) belongs to \(L^3\), and \(g\) extends constantly beyond each endpoint as a real Lipschitz function.
The scalar graph theorem therefore gives the actual vacuum, and the scalar geometric criterion then gives finite squared curvature and both scalar canonical domains.

The deficit \(x\mapsto |(x-r,x+r)\setminus F|\) is measurable.
Among the centers in \(F\cap[1/8,7/8]\), the finite-stage boundary neighborhoods remove at most \(2r\) times the number of endpoints.
Of the remaining centers at most \(80|F_k\setminus F|\) in measure fail (1), by integrating the normalized deficit and applying Markov's inequality.
Taking \(k\) large and then \(r\) small leaves mass at least \(1/4\) at every such \(r\).
A maximal \(3r\)-separated set is finite and its covering by intervals of length \(6r\) gives at least \(1/(24r)\) centers.

For a point of \(W_l\) and either endpoint in \(V_l\), the squared distance in units of \(r^2\) lies between \((21/32)^2\) and \((3/4)^2+(1/40)^2<1\).
Two points of \(V_l\) are within \(\sqrt{2}r/32\).
For distinct endpoints on the open slope-one subsegment, twice the height above their common line is at least \(\sqrt{2}(21/32-1/40)r\).
The two remaining side lengths are each at most \(r\), giving a common curvature bound \(c_1/r\) with \(c_1=\sqrt{2}(21/32-1/40)>0\).
The subsegment has positive product measure for the endpoints after omitting the null diagonal.
Thus a single cell's mass \(a_l\) in the central window forces the stated essential supremum even when the subsegment is short.

The reciprocal circumradius extended by zero on degenerate triples is measurable, and its square is bounded by \(16/r^2\) on the shell.
For completed measurable cells one may take Borel representatives modulo null sets before applying Fubini.
For every \(v\in h(V_l)\) and \(w\in h(W_l)\) the secant has slope at most \((1/40)/(21/32)<1\), and so meets the slope-one segment in at most a single point.
When \(a_l>0\), Fubini gives strictly positive \(q_{r,A}\) for almost every endpoint pair in \(h(I_l)\times h(V_l)\).
Positive mass of \(h(I_l)\) and the support assumption force \(\mu(h(V_l)\setminus B_A)=0\).
Consequently \(m_A\) disjoint remote windows require \(\mu(B_A)\ge m_A r/32\).
For \(m_A\ge1\), \(m_A^2\max_l a_l\ge\sum_l a_l\), and countable additivity over the partition recovers the mass \(r/16\) of each central window.
The resulting lower bound is \(c_1^2/(32^2\cdot384)\).
The half-open grid gives a valid upper bound at any radius since its fivefold squares contain both endpoints of every eligible triple and project to intervals of length \(5r\).
Summing the resulting bound \(400\mu(A)\) gives \(400\).
These estimates imply linear growth over \(N\) small dyadic radii even if every choice varies with the scale.

Disjoint shells have total curvature mass at most \(\int\kappa^2\,d\mu^3\) by Tonelli.
With the scalar liberation difference, exchanging the endpoint variables in the real part gives one half the integral of \(|u(z)-u(v)|^2g_\mu(z,v)\).
Boundedness of \(u\) and integrability of \(g_\mu\) justify the exchange.
For finite shell sums the signed form of C_F0297 has this real-part convention since the inner product is linear in its second argument.
For their increasing limit, Jensen and \(|z-v|\kappa\le2\) give \(|z-v|^2 g_\mu^2\le4g_\mu\) almost everywhere, justifying the gap-tensor limit on the analytic core independently of localized-cost summability.
The obstruction concerns the absolute majorant based on one third-point partition and one supporting square \(B_A^2\) per cell.
The accepted dependency interfaces were checked at their stated uses.
The individual proofs of those earlier theorems and the implication for unrestricted correlated tuples lie beyond this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0300_v1.md#statement) | Uniform optimized shell bounds, linear multiscale cost, actual scalar law with integrable curvature, and the scalar signed form. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0300_v1.md#argument) | Entire graph construction, all-small-radius packing, measurable partition and support estimates, grid upper bound and sign identification. |
| [Finding](#finding) | [Lipschitz graph theorem](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Actual scalar vacuum for the compact uniform parameter density and real Lipschitz graph. |
| [Finding](#finding) | [Geometric criterion](../../claims/Yin_C_F0255_v1.md#statement) | Necessity of finite total squared curvature and the two canonical scalar domains under actuality. |
| [Finding](#finding) | [Localized kernel](../../claims/Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) | Partial liberation and signed analytic-core energy with the second-variable-linear tracial pairing. |
| [Finding](#finding) | [Diameter shells](../../claims/Yin_C_F0297_v1.md#summing-by-triangle-diameter) | The localized cost, squared curvature bound, grid supports and identification of the limit via gap tensors. |

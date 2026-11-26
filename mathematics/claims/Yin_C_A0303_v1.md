---
author: Yin
---

# A four-site matrix of regular rank three halves has no cyclic quotient of order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and assume that every nonzero scalar in \(\mathbb C H\) acts injectively in its regular representation.
If \(H\) admits a cyclic quotient of order \(24\), no complex two-by-two four-site matrix \(K=B+At-s(D+Ct)\) has regular rank \(3/2\).
In particular the [equivalent four-column pencil](Yin_C_A0184_v1.md#statement) on these two generators has no half-dimensional column increment.
The exclusion concerns a quotient of this two-generator label group with this four-site input.

Suppose otherwise.
Use the [normalization at order 24](Yin_C_A0241_v1.md#statement), giving \(H_{\rm ab}=C_{24}\) with degrees \(3,4\) at \(s,t\), after the allowed changes to the marking and the matrix.
Let \(P(z)=Az+B,\ Q(z)=Cz+D,\ M(z)=P(z)Q(z)^{-1}\).
Write \(t_j=s^jts^{-j},\ g=s^4,\ W=M(t_1)M(t_0)\).
We use the [middle identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) \(W^{-1}=s^{-2}W s^{-2}\) and the [trivial intersection of neighboring cyclics](Yin_C_A0290_v1.md#applying-the-four-step-identity).

## The two residues occur at the same point

By the [weak trace tail theorem](Yin_C_A0302_v1.md#statement), \(M\) and \(M^{-1}\) each have a unique boundary pole; both are simple and both residues are nonzero of square zero.
By the [bounded scalar compression](Yin_C_A0301_v1.md#one-pole-on-a-side-bounds-all-residue-lines), the residues are proportional.
The two determinants have only simple unit-circle zeros and every such zero produces an actual pole on its respective side by the [adjugate calculation](Yin_C_A0301_v1.md#one-pole-on-a-side-bounds-all-residue-lines).

Write \(N(z)=P(z){\rm adj}\,Q(z)=N_0+N_1z+N_2z^2\).
The three constant matrices \(N_j\) are linearly independent: if they spanned at most two dimensions, left normalization by an invertible value would give a pencil spanned by the identity and at most one other matrix, hence a constant eigenline.
That would give a [constant point correspondence](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) for the original transfer.
Thus \(N(\alpha),N(\beta)\) are proportional at two finite points only when \(\alpha=\beta\), by comparing their respective coefficients \(1,z,z^2\).

Let \(\alpha\) be the pole of \(M=N/\det Q\) and \(\beta\) the pole of \(M^{-1}={\rm adj}\,N/\det P\); the second formula uses the linear two-by-two adjugate and \({\rm adj}({\rm adj}\,Q)=Q\).
The first residue is a nonzero multiple of \(N(\alpha)\), and the second a nonzero multiple of \({\rm adj}\,N(\beta)\).
The adjugate of a square-zero two-by-two matrix is its negative.
Therefore \(N(\alpha)\) and \(N(\beta)\) are proportional, giving \(\beta=\alpha\).

## A matrix entry with absolutely summable coefficients

After constant similarity the common residue direction is \(e_{12}\).
Write
\[
             M(z)=\begin{pmatrix}f(z)&b(z)\\h(z)&j(z)\end{pmatrix},
      \qquad m(z)=\det M(z)=p(z)/q(z),\quad
      \det P(z)=(z-\alpha)p(z),\quad \det Q(z)=(z-\alpha)q(z).
\]
The polynomials \(p,q\) have degree at most one and no unit-circle zeros.
In particular \(m\) and \(m^{-1}\) are bounded on the circle.
The three entries \(f,j,h\) have numerators of degree at most one over \(q\), because their numerators over \(\det Q\) vanish at \(\alpha\).
Also \(h(\alpha)=0\), since \(fj-bh=m\) stays bounded at the simple pole of \(b\).
The function \(h\) is nonzero since \(h\equiv0\) would give a constant invariant line.
Thus \(h\) is a nonconstant fractional linear function vanishing at \(\alpha\).
The inverse transfer has corresponding three regular entries \(j/m,f/m,-h/m\), including its lower left entry.

Each of these six regular entries is rational and holomorphic on an annulus about the circle, so its Laurent coefficients are absolutely summable.
The lower left entries
\[
  W_{21}=h(t_1)f(t_0)+j(t_1)h(t_0),\qquad
  (W^{-1})_{21}=-(h/m)(t_0)(j/m)(t_1)-(f/m)(t_0)(h/m)(t_1)
\]
therefore belong to \(\ell^1(F)\) for \(F=\ker(\chi\bmod4)\), where \(\chi:H\to C_{24}\) is the marking.
They satisfy \((W^{-1})_{21}=g^{-1}s^2 W_{21}s^{-2}\) there, by faithfulness of the regular representation on \(\ell^1(F)\).
Now apply the six actual characters of \(F\) induced by \(\chi/4\).
They send each \(t_i\) to \(\zeta\) and \(g\) to \(\zeta^3\) for \(\zeta^6=1\); conjugation by \(s^2\) preserves them.
This gives
\[
         h(\zeta)\,{\rm tr}M(\zeta)\big(m(\zeta)^2+\zeta^3\big)=0
                  \qquad(\zeta^6=1).
\]
Here \({\rm tr}M=f+j\) denotes its regular extension through \(\alpha\); the displayed identity only evaluates regular entries.

## A cross-ratio forces zero trace

If the trace is not identically zero, it vanishes at at most one circle point since its numerator has degree at most one.
The same bound applies to \(h\).
At least four sixth roots would therefore satisfy \(m(\zeta)^2=-\zeta^3\).
A constant \(m\) can do so at at most three points.
A nonconstant \(m=p/q\) is a fractional linear map and is injective, so exactly four points would map onto the four points \(1,-1,i,-i\).
The source set would contain two even and two odd powers of \(\exp(\pi i/3)\), because squaring the image gives opposite signs on the two parities.

This mapping of four points is impossible by the cross-ratio.
Use \((z_1-z_3)(z_2-z_4)/((z_1-z_4)(z_2-z_3))\) in cyclic order.
The two omitted sixth roots have opposite parities and are therefore either neighbors or antipodes.
Up to dihedral symmetry and a choice of starting point, the remaining exponents are \((0,1,2,3)\) or \((1,2,4,5)\); the respective cross-ratios are \(3/2\) and \(4/3\), using the half-angle sine formula.
The four square vertices in any order have cross-ratio in \(\{-1,1/2,2\}\).
No source tuple can therefore be carried to the square vertices by a fractional linear map.
It follows that \({\rm tr}M\equiv0\).

## The Fourier support cannot be translated as required

Put \(u_0=h(t_0),\ u_1=h(t_1)\) in this paragraph, and let \(w=h/m\).
Since \(h\) has linear numerator vanishing at \(\alpha\), whereas \(q(\alpha)\ne0\), the two polynomials \(q\) and \(qh\) form a basis of the polynomials of degree at most one.
Thus \(f=A_0+B_0 h,\ m=m_0+m_1h\), with \(A_0=f(\alpha)\), \(m_0=m(\alpha)\ne0\).
In fact \(A_0\ne0\): otherwise the first column of \(M\) would be \(h(B_0,1)^{\mathsf T}\), a constant point correspondence.
Since \(j=-f\), the forward entry becomes \(W_{21}=A_0(u_1-u_0)\), with the two mixed products cancelling in their original order.
Likewise \(f/m=A_0/m_0+(B_0-A_0m_1/m_0)w\) gives
\[
       s^{-2}\big(h(t_1)-h(t_0)\big)s^{-2}
                       =-m_0^{-1}\big(w(t_1)-w(t_0)\big).
\]
The functions \(h\) and \(w\) are nonconstant fractional linear functions regular on the circle, each with its only zero at \(\alpha\).
For either function the nonconstant Fourier exponents consist of all positive integers, all negative integers, or a singleton \(\{1\}\) or \(\{-1\}\).
Indeed a finite nonzero pole off the circle gives a geometric series from the inside or the outside with every coefficient on the corresponding half-line nonzero.
A pole at zero or infinity gives an affine function of \(z^{-1}\) or \(z\), respectively.
Constant coefficients cancel in each difference.
The cyclic groups \(C_i=\langle t_i\rangle\) have trivial consecutive intersection, so no exponent in either difference cancels with the other cyclic summand.

If the exponents of \(h\) form an infinite half-line, the displayed identity forces
\[
                      t_{-1}^{\,n}\in C_0s^4\ \cup\ C_1s^4
\]
for every \(n\) on that half-line: translate the nonzero coefficient at \(t_1^n\) on the left by \(s^{-2}\) on both sides, then move \(s^{-4}\) to the right.
At most one such element can belong to \(C_0s^4\), since the quotient of any two would be in \(C_{-1}\cap C_0=\{1\}\).
Choose consecutive exponents with both powers in \(C_1s^4\).
Their quotient gives \(t_{-1}\in C_1\), hence \(s^4\in C_1\).
Conjugating by \(s^{-1}\) gives \(s^4\in C_0\) as well, impossible since \(s\) has infinite order.

It remains that the support of the difference for \(h\) has just two elements, one in each cyclic subgroup.
The same equality forces precisely two for \(w\), so its nonconstant exponent is likewise \(1\) or \(-1\).
In \(C_{24}\) the two labels on the left have common degree \(4\epsilon-12\) with \(\epsilon\in\{1,-1\}\), whereas those on the right have common degree \(4\epsilon'\) with \(\epsilon'\in\{1,-1\}\).
The possible residues are \(16,8\) on the left and \(4,20\) on the right.
Their supports cannot be equal.
This also rules out both affine cases and proves the assertion.

## Assessment history

### Decision exclusion-at-order-twenty-four

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:54 |
| status | proved |
| reason | The six evaluations of the summable coordinate force zero trace, which the support identity in the original group excludes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The six evaluations of the summable coordinate force zero trace, which the support identity in the original group excludes. |
| argument | [The two residues occur at the same point](#the-two-residues-occur-at-the-same-point) | The two residues occur at the same point. |
| argument | [A matrix entry with absolutely summable coefficients](#a-matrix-entry-with-absolutely-summable-coefficients) | A matrix entry with absolutely summable coefficients. |
| argument | [A cross-ratio forces zero trace](#a-cross-ratio-forces-zero-trace) | A cross-ratio forces zero trace. |
| argument | [The Fourier support cannot be translated as required](#the-fourier-support-cannot-be-translated-as-required) | The Fourier support cannot be translated as required. |
| review | [Exclusion at order twenty-four](../audits/reviews/Yin_R_A0216_v1.md#exclusion-at-order-twenty-four) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-exclusion-at-order-twenty-four)

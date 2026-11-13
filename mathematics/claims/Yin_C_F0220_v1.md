---
author: Yin
---
# Brown-measure energy obstructs coarse Sylvester equations and normalized derivations on cyclic two-by-two generators

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(A\in M_1\), \(B\in M_2\) be bounded elements of finite von Neumann algebras with faithful normal probability traces, and let \(\nu_A,\nu_B\) denote their Brown measures.
On \(L^2(M_1)\otimes_2 L^2(M_2)\) use the outer left and right actions.
If a coarse vector \(k\) satisfies \(Ak-kB=1\otimes1\), then
\[
        I(\nu_A,\nu_B):=\int_{\mathbb C^2}|z-w|^{-2}\,
                     d\nu_A(z)d\nu_B(w)\le\|k\|_2^2 .                 \tag{1}
\]
In particular the two Brown measures must be mutually singular.
For \(A=B\) in a single algebra there is never such a vector, even for nonnormal \(A\).
Equivalently, on the tracial Hilbert space of that algebra there is no Hilbert--Schmidt \(T\) with \(L_A T-TL_A=P_\Omega\).

Let a represented star algebra containing \(X\in M\) be Hilbert dense in a finite tracial \(M\), with a closable outer derivation \(\delta\) into the coarse space such that \(\delta X=1\otimes1\).
If \(p=p^*=p^2\in\operatorname{Dom}\bar\delta\) commutes with \(X\), \(t=\tau(p)\in(0,1)\), and \(q=1-p\), let \(X_p=pXp,\ X_q=qXq\) carry their normalized corner traces.
Then
\[
       2t(1-t) I(\nu_{X_p},\nu_{X_q})\le\|\bar\delta p\|_2^2 .       \tag{2}
\]
In particular these corner Brown measures are mutually singular.
The condition applies to a replicated or mixed direct sum when its separating central projection belongs to the closed derivation domain.
A central projection in the generated \(C^*\)-algebra satisfies that domain condition on the generating star-polynomial core.

For any bounded \(b\) in a finite tracial von Neumann algebra, put
\[
                      Y=\begin{pmatrix}0&1\\ b&0\end{pmatrix}
\]
with the product of the normalized matrix trace and the given trace, and work on \(L^2(W^*(Y))\).
If \(1\notin\sigma(bb^*)\), or more generally if \(e_{11}\) has an operator-norm convergent graph approximation on the represented star core for a proposed normalized derivation, there is no closable outer derivation there with \(\delta Y=1\otimes1\).
In particular every \(\|b\|<1\) is covered, including \(b=\varepsilon c\) for a standard circular \(c\) and \(0<\varepsilon<1/\|c\|\).
All these exclusions hold for actual ACSY, since its adjoint vacuum implies closability.

## Argument

### Brown measure of the outer difference

Put \(\mathcal N=M_1\bar\otimes M_2^{\rm op}\) with the product probability trace.
The linear isometry \(s\otimes t\mapsto s\otimes t^{\rm op}\) identifies the coarse space with \(L^2(\mathcal N)\), since cyclicity gives the same second-leg inner product.
The two outer multipliers become left multiplications by \(A\otimes1\) and \(1\otimes B^{\rm op}\).
Hence the hypothesized vector corresponds to an affiliated \(K\in L^2(\mathcal N)\) satisfying \(DK=1\) for \(D=A\otimes1-1\otimes B^{\rm op}\).
The left support of \(D\) is one, since its complementary projection annihilates \(DK\).
The right support has the same trace by polar decomposition, hence also equals one.
Thus \(D\) has an affiliated two-sided inverse by spectral calculus and \(K=D^{-1}\).
Moreover \(\int\log^-s\,d\mu_{|D|}(s)<\infty\), since \(|D|^{-1}\) has finite second moment by polar decomposition.

For every \(\lambda\), the singular laws of \(B^{\rm op}-\lambda\) and \(B-\lambda\) coincide.
Indeed their squared moduli correspond to \((B-\lambda)(B-\lambda)^*\) and \((B-\lambda)^*(B-\lambda)\), of equal spectral law by the trace and polar decomposition.
The logarithmic potentials defining Brown measure therefore give \(\nu_{B^{\rm op}}=\nu_B\).
They also show that tensor amplification \(S\mapsto S\otimes1\) preserves the Brown measure of \(S\), including when the first algebra is a corner with its normalized trace.

For a Borel set \(E\subset\mathbb C\), the Haagerup--Schultz projection of \(A\otimes1\) for \(E\) equals \(P(A,E)\otimes1\).
Indeed this is invariant, and the two nonzero normalized diagonal compressions are tensor amplifications of the corresponding compressions of \(A\), whose Brown measures are concentrated on \(E\) and its complement respectively.
Uniqueness of the projection with these two properties yields the equality, also for a zero or full projection.
The same argument applies to \(1\otimes B^{\rm op}\).
Their two projections commute, so the trace of their meet is the product of the two marginal masses.
By the rectangle formula and the linear-polynomial pushforward theorem at the [joint Brown-measure source interface](#joint-brown-input), the joint law is \(\nu_A\times\nu_B\) and \(\nu_D\) is its image under \((z,w)\mapsto z-w\).

The [inverse and \(L^p\) Brown-measure inequalities](#inverse-brown-input) give
\[
       \int |\lambda|^{-2}\,d\nu_D(\lambda)
           =\int |u|^2\,d\nu_{D^{-1}}(u)\le\|D^{-1}\|_2^2.
\]
The pushforward just computed proves (1).
If the measures are not mutually singular, take their densities with respect to their sum and let \(\gamma\) have density the minimum of the two.
Then \(0<\gamma(\mathbb C)<\infty\) and \(\gamma\) is dominated by both measures.
Every such compactly supported planar \(\gamma\) has infinite self-energy.
For \(0<r\le1\), partition a containing square into at most \(C r^{-2}\) cells of diameter at most \(r\), with disjoint boundary conventions.
Summing squared cell masses and applying Cauchy--Schwarz gives \((\gamma\times\gamma)\{|z-w|\le r\}\ge C^{-1}r^2\gamma(\mathbb C)^2\).
Tonelli with \(2r^{-3}\,dr\) gives the divergence, including atoms, by the [planar energy argument](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation).
Consequently finite cross energy forces mutual singularity.
For \(A=B\), the standard tracial isometry \(s\otimes t\mapsto[h\mapsto s\tau(th)]\) onto the Hilbert--Schmidt operators intertwines the two outer actions with left and right composition by \(L_A\).
It takes \(1\otimes1\) to \(P_\Omega\), proving the commutator assertion.

<a id="joint-brown-input"></a>
#### Joint Brown-measure source interface

Charlesworth, Dykema, Sukochev and Zanin, *Simultaneous upper triangular forms for commuting operators in a finite von Neumann algebra*, supply the uniqueness characterization of the one-coordinate projection in §2.4 (PDF page 8), the rectangle meet in Definition 4.1 (PDF page 14), the measure extension in Proposition 5.5 and Definition 5.6 (PDF page 21), and the holomorphic pushforward in Theorem 11.2 (PDF page 49).
Here the commuting pair is bounded in the finite algebra \(\mathcal N\), the masses on rectangles use its product trace, and the function \(z-w\) is an entire polynomial.
Only these stated source results are used. [Authors' edition](https://arxiv.org/pdf/1703.05695)

<a id="inverse-brown-input"></a>
#### Inversion and second moments

Haagerup and Schultz, *Brown measures of unbounded operators affiliated with a finite von Neumann algebra*, Proposition 2.16 (PDF pages 17–18), give pushforward by inversion from finite negative logarithmic moment of the singular law.
Their Theorem 2.19 (PDF page 19) bounds the absolute \(p\)-th Brown moment by the \(p\)-th tracial norm for \(0<p<\infty\).
Here \(D\) is bounded and \(D^{-1}\in L^2(\mathcal N)\) under the solution hypothesis, giving the stated logarithmic hypothesis and allowing \(p=2\) for the inverse. [Authors' edition](https://arxiv.org/pdf/math/0605251)

### Compressing the derivative of a commuting projection

Write \(K=\bar\delta p\) and take graph approximants \(p_n\) on the original core.
Since \([p_n,X]\to0\) in \(L^2\), the product rule, the bounded outer actions of \(X\), and \(\delta X=1\otimes1\) give
\[
    \delta[p_n,X]\longrightarrow KX-XK+p\otimes1-1\otimes p .
\]
Closability makes this limit zero.
This step only requires Hilbert convergence of \(p_n\), since \(p_n\) multiplies the prescribed unit tensor here.
Let \(Q_p:H\to L^2(pMp,\tau|_{pMp})\subset H\) and \(Q_q\) be the orthogonal compressions \(h\mapsto php\) and \(h\mapsto qhq\), with inherited norms.
They commute with left and right multiplication by \(X\), since \(pX=Xp\).
Applying \(Q_p\otimes Q_q\) and \(Q_q\otimes Q_p\) gives equations with right sides \(p\otimes q\) and \(-q\otimes p\) for the respective differences \(X_p k-kX_q\) and \(X_q k-kX_p\).
In intrinsic probability norms (1) bounds \(I\) by the square of each of these solutions, changing the sign of the second.
The inherited squared norm in each mixed tensor is \(t(1-t)\) times its intrinsic squared norm.
The two compressions have orthogonal ranges, which proves (2).
This proof applies also when \(p\) is noncentral.
The [central \(C^*\)-cutoff and closability argument](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) supplies the stated domain sufficiency for central \(p\) and closability under the actual adjoint-vacuum hypothesis.

### The two-by-two cyclic relation

Work in \(M_2(W^*(b))\) in its given tracial representation, and put \(p=e_{11}\), \(s=2p-1\).
If \(1\notin\sigma(bb^*)\), then \(YY^*=\operatorname{diag}(1,bb^*)\) gives \(p=1_{\{1\}}(YY^*)\) by the spectral gap.
A smooth real cutoff on the real line equal to one near \(1\) and zero near \(\sigma(bb^*)\) has this value at \(YY^*\).
As in the [selfadjoint polynomial cutoff calculation](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff), approximate the function in \(C^1\) on a containing interval by real polynomials.
Their values converge in operator norm and their derivatives converge in coarse norm, by uniform divided-difference convergence on the two commuting selfadjoint outer multipliers of \(YY^*\).
This establishes the stronger graph approximation on the star core for this specific projection.
The alternative hypothesis gives it directly.
In either case \(e_{12}=pY\) and \(e_{21}=e_{12}^*\) are generated, and \(e_{12}Y=e_{11}b\) supplies \(b\) in the first matrix corner.
Thus \(W^*(Y)=M_2(W^*(b))\), with exactly its given trace and coarse tensor coordinates.

Suppose now that such a closable normalized derivation exists, and take core approximants \(s_n\to s\) in operator norm with \(\delta s_n\to K=\bar\delta s\).
The identity \(sY+Ys=0\) gives by closability
\[
                  KY+YK=-(s\otimes1+1\otimes s).
\]
Indeed the inputs \(s_nY+Ys_n\) tend to zero in norm and their derivatives converge to the sum of the two sides moved to the left.
For a coarse tensor take its matrix coefficients on the first leg at \((i,j)\) and on the second at \((m,n)\), extending continuously as \(K_{ij;mn}\in L^2(W^*(b))\otimes_2 L^2(W^*(b))\).
Each matrix tensor unit has inherited Hilbert norm \(1/2\), so the extraction gives finite intrinsic norms.
Fix inner indices \(j=m=1\), and denote \(U=K_{11;12}\), \(V=K_{21;11}\).
The coefficients at the two outer diagonal positions \((i,n)=(1,1)\) and \((2,2)\) of the displayed equation are
\[
                     V+U b=-2(1\otimes1),\qquad bU+V=0 .
\]
At the second position the right side is zero because the two fixed inner indices are one.
Subtracting gives \(bU-Ub=2(1\otimes1)\), contradicting (1) for \(A=B=b\) after division by two.
This rules out the proposed derivation independently of any bound or value on \(Y^*\).
For \(b=\varepsilon c\) the corresponding unscaled difference with \(c\) on both sides has right side \(2\varepsilon^{-1}(1\otimes1)\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:45 |
| status | open |
| reason | The Brown-measure cross-energy estimate, graph-domain corner consequence and cyclic matrix exclusion are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Mixed coarse lower bound, universal identical-operator obstruction, commuting projection trace factors and the cyclic two-by-two model. |
| argument | [Argument](#argument) | Opposite algebra, affiliated inverse, tensor Brown law, inverse moment, planar divergence, graph compression and two matrix coefficients. |
| dependency | [Joint Brown-measure theorems](#joint-brown-input) | Single-coordinate projection uniqueness, product rectangle masses and polynomial pushforward in a finite tracial algebra. |
| dependency | [Inverse Brown measure and Weyl bound](#inverse-brown-input) | Affiliated inverse Brown pushforward and the second absolute Brown moment bounded by its Hilbert norm squared. |
| dependency | [Planar critical energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Disjoint grids and the divergent layer integral for the self-energy of a compactly supported nonzero planar measure. |
| dependency | [Closed graph and spectral cutoff](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Actual adjoint-domain closability, central projection sufficiency and the selfadjoint divided-difference graph approximation. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T15:09 |
| status | proved |
| reason | Adopt the Brown-measure energy obstruction, corner estimate and cyclic matrix exclusion after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Mixed coarse lower bound, universal identical-operator obstruction, commuting projection trace factors and the cyclic two-by-two model. |
| argument | [Argument](#argument) | Opposite algebra, affiliated inverse, tensor Brown law, inverse moment, planar divergence, graph compression and two matrix coefficients. |
| dependency | [Joint Brown-measure theorems](#joint-brown-input) | Single-coordinate projection uniqueness, product rectangle masses and polynomial pushforward in a finite tracial algebra. |
| dependency | [Inverse Brown measure and Weyl bound](#inverse-brown-input) | Affiliated inverse Brown pushforward and the second absolute Brown moment bounded by its Hilbert norm squared. |
| dependency | [Planar critical energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Disjoint grids and the divergent layer integral for the self-energy of a compactly supported nonzero planar measure. |
| dependency | [Closed graph and spectral cutoff](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Actual adjoint-domain closability, central projection sufficiency and the selfadjoint divided-difference graph approximation. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0228_v1.md#whole-proof-finding) | Tensor Brown measures and inverse moments, opposite-leg conventions, corner trace factors, cyclic coefficients and all declared inputs. |

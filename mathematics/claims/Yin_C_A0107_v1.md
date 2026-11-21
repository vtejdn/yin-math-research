---
author: Yin
---
# Complex biradial ranks and affiliated splitting obstructions in the Gardam group

## Statement

Let
\[
 \Gamma=\langle a,b,c,d,e,f,g\mid
 acb,\ add,\ afg,\ bbf,\ cef,\ cdg,\ eeg\rangle,
 \qquad M=\mathcal N(\Gamma),
 \tag{1}
\]
with canonical trace \(\tau(1)=1\), and put
\[
 H=a+b+c+d+e+f+g,\qquad S_0=H+H^*.
 \tag{2}
\]
These are unnormalized sums: the positive-step averaging operator is \(H/7\), and the symmetric averaging operator is \(S_0/14\).
Let \(S_{m,n}\) be the elements with \(m\) positive and \(n\) inverse generators in a minimal seven-generator word.
Write
\[
 \mu_{m,n}=\frac1{|S_{m,n}|}\sum_{x\in S_{m,n}}x,\qquad
 \mathcal A=\operatorname{span}_{\mathbb C}\{\mu_{m,n}:m,n\ge0\}.
 \tag{3}
\]
Thus finite biradial coefficients are constant on each such displacement class.
The classes are not the two-generator word spheres.

The following assertions hold without an Atiyah assumption on \(\Gamma\) or any of its direct powers.

1. The operators \(H,H^*\) commute and are algebraically independent over \(\mathbb C\), and
   \[
       \mathcal A=\mathbb C[H,H^*]\cong\mathbb C[X,Y].
       \tag{4}
   \]
   Every nonzero element of \(\mathcal A\) is an affiliated unit.
   The field
   \[
       \mathcal F=\mathbb C(H,H^*)\subset U(M)
       \tag{5}
   \]
   is consequently well defined.
   For every \(m,n\ge1\) and every \(P\in M_{m,n}(\mathbb C(X,Y))\), evaluation in this field satisfies
   \[
   \operatorname{rk}_M P(H,H^*)
      =\operatorname{rank}_{\mathbb C(X,Y)}P=r,\qquad
   \dim_M\ker P(H,H^*)=n-r.
   \tag{6}
   \]
   Matrix ranks and dimensions use the unnormalized matrix trace.
   This covers arbitrary complex coefficients, arbitrary finite radius, and arbitrary matrix size.
   In particular a nonzero finite biradial coefficient has no nonzero left or right zero-divisor partner in \(\mathbb C[\Gamma]\), even if that partner is not biradial.

2. The actual regular-representation spectrum and trace moments of \(S_0\) are
   \[
     \sigma(S_0)=[-6,12],\qquad
     \tau(S_0)=0,\quad \tau(S_0^2)=14,\quad \tau(S_0^3)=42.
     \tag{7}
   \]
   If \(p=1_{(6,12]}(S_0)\), then
   \[
                         \tau(p)\ge\kappa,\qquad
                \kappa=\frac7{147456\pi^2}>0.
     \tag{8}
   \]

3. For every \(k\ge1\) and every \(V\in M_k(U(M))\), an equality
   \[
                       V(S_0I_k)=-(S_0I_k)V
     \tag{9}
   \]
   in the affiliated algebra forces
   \[
           pI_k\le \operatorname{proj}_{\ker V},\qquad
           \operatorname{rk}_M V\le k(1-\kappa).
     \tag{10}
   \]
   In particular \(V\) cannot be an affiliated unit.

4. Let \(t,c\in\mathbb R\), \(t\ne0\), and \(S=tS_0+cI\).
   For every \(k\ge1\), \(\alpha\in\mathbb C^\times\), and \(\beta\in\mathbb C\), there is no \(V\in M_k(U(M))\) satisfying both
   \[
       (SI_k)V+V(SI_k)=0,\qquad
       S^2I_k+\alpha V^2=\beta I_k.
       \tag{11}
   \]
   The second input may be unbounded and nonbiradial.
   The same conclusion holds when \(S\) is replaced by any nonzero complex scalar multiple of \(S\), in particular by \(iS\).

For affiliated matrices, \(\operatorname{rk}_M A\) means the trace dimension of the closure of the image, equivalently the number of input columns minus the trace of the kernel projection.
All products and inverses in \(U(M)\) use closed affiliated operators.
The claims concern the actual canonical regular trace.

The development source is [L67](../ledger/Yin_L_A0067_v1.md).
The external harmonic-analysis input is Cartwright--Młotkowski, CM94, in the [registered published edition](../audits/literature/CM94/readme.md).
The matrix consequence and the affiliated obstruction are proved below; they are not attributed as original results of CM94.

## Argument

### Applicability and normalization of the spherical theorem

The seven oriented triangle boundaries in (1) are those of [Gar21c, slide 12](../literature/pdf/Gar21c.pdf#page=12).
Their identification with Gardam's two-generator presentation is proved in [C105v2](Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
The incidence sets obtained from their cyclic permutations are
\[
\begin{array}{c|ccccccc}
x&a&b&c&d&e&f&g\\ \hline
\lambda(x)&cdf&abf&bde&adg&efg&bcg&ace.
\end{array}
\tag{12}
\]
Each row has three points; any two rows meet in one point.
Together with uniqueness of the third entry in a cyclic triple, these are the triangle-presentation conditions of CM94, Section 1, pp. 348--349, for the projective plane of order \(q=2\).
The building construction recalled there gives a simply transitive, type-rotating action of \(\Gamma\) on its vertices.
Its sector displacement classes are exactly \(S_{m,n}\).
The intrinsic minimal-word counts also follow from the source's normal forms, Section 6, equation (6.1), p. 374.

CM94, Corollary 2.2 and Proposition 2.3, pp. 352--354, give
\[
 \begin{split}
 |S_{0,0}|&=1,\\
 |S_{m,0}|=|S_{0,m}|&=7\,4^{m-1}\quad(m\ge1),\\
 |S_{m,n}|&=42\,4^{m+n-2}\quad(m,n\ge1).
 \end{split}
 \tag{13}
\]
They also show that the span of the normalized displacement sums is a commutative algebra generated by \(\mu_{1,0}=H/7\) and \(\mu_{0,1}=H^*/7\).
The source formulates this using averaging operators.
The unitary inversion of the group variable identifies its right averaging convention with left convolution, preserving the identity vector and its trace.
This proves the algebra-generation and commutation assertions in (4).

Let
\[
 \mathbb T_2=\{(s_1,s_2,s_3)\in\mathbb T^3:s_1s_2s_3=1\},
 \qquad s_3=(s_1s_2)^{-1},
 \tag{14}
\]
with normalized Haar measure \(ds=d\theta_1\,d\theta_2/(2\pi)^2\).
CM94, Proposition 3.1, p. 360, and Proposition 5.1, pp. 370--371, identify the spherical transforms and trace as follows:
\[
 \begin{split}
 h(s)&=2(s_1+s_2+s_3),\\
 h^\#(s)&=2(s_1^{-1}+s_2^{-1}+s_3^{-1}),\\
 \tau(F(H,H^*))&=\int_{\mathbb T_2}F(h(s),h^\#(s))\,w(s)\,ds,\\
 w(s)&=\frac7{16}
       \prod_{i<j}\left|\frac{s_i-s_j}{s_i-\tfrac12s_j}\right|^2.
 \end{split}
 \tag{15}
\]
Initially \(F\) is a polynomial; spectral calculus extends the identity to bounded Borel functions.
The source coordinate of \(H/7\) is \(h/7\).
The density coefficient is
\((q+1)(q^2+q+1)/(6q^3)=7/16\) at \(q=2\), and the measure in (15) has total mass one.
The denominator factors never vanish on the torus.
The numerator vanishes only when two coordinates coincide, a Haar-null set.
Thus \(w(s)\,ds\) and Haar measure have exactly the same null sets, and this measure has full support.

These are accepted external results at the stated passages.
No singular-MASA or normalizer assertion is a premise of the argument.

### Laurent minors and rational evaluation

A nonzero Laurent polynomial in \(s_1,s_2\) has a Haar-null zero set on \(\mathbb T^2\).
Clear negative powers and expand in \(s_2\).
The set of \(s_1\) for which all coefficient polynomials vanish is finite, unless all coefficients are zero.
Outside that exceptional set the polynomial has finitely many zeros in \(s_2\).
Fubini's theorem proves the assertion; (15) gives the same conclusion for the spherical measure.

The substitution
\[
 \mathbb C[X,Y]\longrightarrow
 \mathbb C[s_1^{\pm1},s_2^{\pm1}],\qquad
 (X,Y)\longmapsto(h,h^\#)
 \tag{16}
\]
is injective.
Indeed for arbitrary \(x,y\in\mathbb C\), the roots of
\[
                       T^3-\tfrac{x}{2}T^2+\tfrac{y}{2}T-1
\]
are nonzero, have product one, and their sum and sum of inverses are \(x/2,y/2\).
Consequently a polynomial identity after (16), evaluated on the complex torus, would vanish at every \((x,y)\).
It is the zero polynomial.
Combining injectivity with the preceding zero-set fact proves algebraic independence in (4) and shows that every nonzero polynomial in \(H,H^*\) has zero kernel.
It is normal, so its range is also dense.
It is therefore invertible in \(U(M)\).
The commuting inverses define the field (5).

Now let \(P\in M_{m,n}(\mathbb C[X,Y])\) have rank \(r\) over \(\mathbb C(X,Y)\).
If \(r>0\), some \(r\)-minor is nonzero, while all larger minors vanish identically.
The chosen minor remains a nonzero Laurent polynomial after (16); it is nonzero almost everywhere for (15).
Hence the numerical matrix \(P(h,h^\#)\) has rank \(r\) almost everywhere.
The assertion is immediate for \(r=0\).

The kernel projection of \(P(H,H^*)\) belongs to \(M_n(W^*(H))\), as the spectral projection at zero of \(P^*P\).
The restriction of the canonical trace to this abelian algebra is (15).
Taking the ordinary numerical kernel dimension in each spectral fibre therefore gives
\[
 \begin{split}
 (\operatorname{Tr}_n\otimes\tau)
      (\operatorname{proj}_{\ker P(H,H^*)})
 &=\int_{\mathbb T_2}
       \dim_{\mathbb C}\ker P(h(s),h^\#(s))\,w(s)\,ds\\
 &=n-r.
 \end{split}
 \tag{17}
\]
This proves (6) for polynomials.
For a matrix of rational functions choose a common nonzero scalar polynomial denominator.
Its evaluation is an affiliated unit, so multiplication by it preserves the kernel dimension and algebraic rank.
This proves (6) in full.
Equivalently any nested rational expression or matrix inverse formed from biradial entries, when defined in the affiliated algebra, evaluates in this field: a square matrix over the field that is singular over the field cannot become affiliated-invertible, by its nonzero field kernel vector.

Each matrix uses finitely many minors, regardless of its coefficients or degree.
The exceptional null set may depend on the matrix; no common null set for all complex coefficient choices is asserted.
An affiliated scalar unit has no nonzero annihilator on either side, proving the final scalar assertion in part 1.

### The actual spectrum and moment counts

By (15),
\[
                     \widehat S_0(s)=4\operatorname{Re}(s_1+s_2+s_3).
 \tag{18}
\]
Put \(r=(\theta_1+\theta_2)/2\) and \(d=(\theta_1-\theta_2)/2\).
Then
\[
 \operatorname{Re}(s_1+s_2+s_3)
       =2\cos r\cos d+2\cos^2r-1.
 \tag{19}
\]
For \(x=|\cos r|\), the right side is at least \(2x^2-2x-1\ge-3/2\) and at most \(2x^2+2x-1\le3\).
Both endpoints are attained.
Its range is the whole interval by connectedness.
The spherical measure has full support, so its essential range is the same interval.
The spectral calculus of the actual operator then gives \(\sigma(S_0)=[-6,12]\).

The canonical trace extracts the identity coefficient.
There is no length-one identity word and there are fourteen length-two inverse pairs.
The type homomorphism \(\Gamma\to\mathbb Z/3\mathbb Z\), sending every positive generator to one, excludes any length-three identity word with mixed signs.
The all-positive length-three identity words are precisely the cyclic permutations of the seven triangles.
For completeness, a positive pair is shortened by a triangle exactly when its second point lies on the incidence line of its first point.
Otherwise it is a length-two geodesic positive word and cannot equal the inverse of a generator.
If it is shortened, uniqueness of the third entry forces that entry as the final generator in a length-three return.
This gives \(7\cdot3=21\) positive returns and twenty-one inverse returns.
Consequently
\[
 \tau(H)=0,\quad
 \tau(H^3)=\tau((H^*)^3)=21,\quad
 \tau(H^2H^*)=\tau(H(H^*)^2)=0,
 \tag{20}
\]
and (7) follows.
These word facts can also be checked by the already retained [J5 normal forms](../computations/programs/Yin_J_A0005/readme.md); the proof here uses the complete triangle normal-form input, not a finite quotient.

### Positive spectral mass

The trace of \(p=1_{(6,12]}(S_0)\) is
\[
 \tau(p)=
 \int_{\{\operatorname{Re}(s_1+s_2+s_3)>3/2\}} w(s)\,ds.
 \tag{21}
\]
Consider the torus box
\[
 \theta_1=\pi/3+t_1,\qquad
 \theta_2=-\pi/3+t_2,\qquad
 |t_1|,|t_2|\le1/12,\qquad
 \theta_3=-t_1-t_2.
 \tag{22}
\]
Using the Lipschitz bound for cosine, the real part of the sum is at least \(2-4/12=5/3\).
Thus the box lies inside the set in (21).
The pairwise chord lengths at its center are \(1,1,\sqrt3\).
The perturbation of each difference angle is at most \(3/12\), so each chord has length at least \(3/4\) throughout the box.
Each denominator \(|s_i-\tfrac12s_j|\) in (15) is at most \(3/2\).
Therefore
\[
                       w(s)\ge\frac7{16}(1/2)^6=\frac7{1024}
 \tag{23}
\]
on the box.
Its normalized Haar measure is
\[
                     \frac{(2/12)^2}{(2\pi)^2}
                        =\frac1{144\pi^2}.
 \tag{24}
\]
Multiplying (23) and (24) proves (8).
The constant is an explicit lower bound, not an asserted exact evaluation of (21).

### Bounded transforms of affiliated intertwiners

We use an elementary finite-von-Neumann-algebra observation with its domain convention made explicit.
Let \(A=A^*\) be bounded in a finite von Neumann algebra \(N\), and let \(V\in U(N)\) satisfy \(VA=-AV\) as an equality of closed affiliated products.
Taking adjoints and multiplying in \(U(N)\) gives
\[
                       (V^*V)A=A(V^*V).
 \tag{25}
\]
Commutation with the bounded resolvent of the positive selfadjoint operator \(V^*V\) gives commutation with all its spectral projections.
In particular
\[
                T=V(1+V^*V)^{-1/2}\in N
 \tag{26}
\]
is bounded, has exactly the same kernel as \(V\), and satisfies \(TA=-AT\).
Here \(T^*T=d/(1+d)\), \(d=V^*V\), so the assertion about its kernel follows directly from spectral calculus.
Bounded spectral intertwining gives, for every Borel set \(E\subset\mathbb R\),
\[
                       T1_E(A)=1_{-E}(A)T.
 \tag{27}
\]
One obtains (27) first for continuous functional calculus and then for spectral projections by bounded strong limits.

Apply this observation in \(N=M_k(M)\) to \(A=S_0I_k\).
For \(E=(6,12]\), the projection \(1_{-E}(A)\) is zero by (7).
Thus \(T(pI_k)=0\), and the equality of the kernels of \(T,V\) proves the projection inclusion in (10).
Taking the unnormalized trace and using (8) proves its rank bound.

If \(V\) is an affiliated unit, its polar decomposition \(V=W|V|\) has a unitary \(W\in N\).
Equation (25) implies that \(|V|\) commutes with \(A\).
Cancelling the affiliated unit \(|V|\) in \(W|V|A=-AW|V|\) gives
\[
                             WAW^*=-A.
 \tag{28}
\]
Hence all odd moments of \(A\) vanish under any finite trace of \(N\).
Only the bounded unitary \(W\), not the unbounded similarity \(V\), is moved through that trace.

### Exclusion of the constant-square relations

Fix \(t,c,\alpha,\beta,k\) as in part 4, and suppose (11) holds.
The polynomial
\[
                     \beta-\bigl(t(X+Y)+c\bigr)^2
 \tag{29}
\]
is nonzero because \(t\ne0\).
Part 1 makes \(\beta-S^2\) an affiliated unit.
The second equation in (11) therefore makes \(V^2\) an affiliated unit, and hence makes \(V\) one.
For example \(V\) commutes with \(V^2\) and its inverse, and \(V(V^2)^{-1}\) is a two-sided inverse of \(V\).
Thus invertibility of the unknown second input is forced by (11); it has not been assumed via a division-ring conjecture.

Apply (28) to \(A=SI_k\).
With \(\operatorname{Tr}_k\otimes\tau\), its first trace moment must vanish, so \(kc=0\) and \(c=0\).
Its third moment would then be
\[
              (\operatorname{Tr}_k\otimes\tau)((tS_0I_k)^3)
                            =42kt^3\ne0,
 \tag{30}
\]
contradicting (28).
This proves (11) has no solution.
If \(S\) is replaced by \(\zeta S\), \(\zeta\in\mathbb C^\times\), divide the anticommutation relation by \(\zeta\) and the square relation by \(\zeta^2\).
The already proved case applies with coefficients \(\alpha/\zeta^2,\beta/\zeta^2\).

## Scope

The all-complex matrix theorem restricts its entries to the biradial field (5), with arbitrary radius and rational complexity.
It does not put a radius bound on arbitrary coefficients of \(\mathbb C[\Gamma]\), and does not establish general Atiyah integrality for this group.
The splitting obstruction has a different scope: its first input is the stated affine adjacency operator, while its second input is completely arbitrary affiliated.
It excludes that input family in particular from the equations in [C104v2](Yin_C_A0104_v2.md#statement), without requiring C104's rational-square premise.
The normalizer and sign-symmetric-direction questions retained in L67 are not premises or conclusions of this Claim.

## Assessment history

### Decision biradial-rank

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:24 |
| status | proved |
| reason | The independent review checks the spherical theorem at the source, the Laurent minors and the arbitrary affiliated-matrix argument. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All complex biradial rational matrix ranks, the spectrum and moments of the adjacency, the forced kernel mass and the affine splitting exclusion. |
| argument | [Proof](#argument) | Triangle-building hypotheses, normalized spherical measure, ranks, spectral mass and polar intertwiners. |
| review | [Whole finding](../audits/reviews/Yin_R_A0144_v1.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Gardam presentation](Yin_C_A0105_v2.md#decision-exact-balls) | The identification of the two-generator and seven-triangle presentations. |

## Current assessment

[Selected decision](#decision-biradial-rank)

---
author: Yin
---
# Biradial ranks and a spectral obstruction in the Gardam group

This 21 November 2026 investigation connects the actual Gardam group with [A0001](../tasks/Yin_T_A0001_v1.md#contract) and the complex zero-divisor question of [A0002](../tasks/Yin_T_A0002_v1.md#contract).
The accepted external input is Cartwright--Młotkowski, CM94, in the [published edition](../audits/literature/CM94/readme.md).
Its spherical Plancherel theorem gives an unconditional, arbitrary-radius subclass with all-complex matrix ranks.
The further spectral calculation below excludes an affine biradial input in the anticommutation and constant-square equations even when the other input is an arbitrary affiliated operator.
These are source consequences and development deductions, without a selected Claim assessment or an independent review.

## The group and the biradial convention

Use the seven-generator presentation
\[
 \Gamma=\langle a,b,c,d,e,f,g\mid
 acb,\ add,\ afg,\ bbf,\ cef,\ cdg,\ eeg\rangle.
 \tag{1}
\]
The oriented triangles are those in [Gar21c, slide 12](../literature/pdf/Gar21c.pdf#page=12).
Their identification with Gardam's two-generator presentation is established in [C105v2](../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
The [J5 normal forms](../computations/programs/Yin_J_A0005/readme.md) provide the existing exact word-comparison context.
The radii used here refer to the seven generators and their inverses and are different from the two-generator ball radii in J5.

For clarity, the point-line incidence sets obtained from the cyclic permutations of the seven triples are
\[
\begin{array}{c|ccccccc}
x&a&b&c&d&e&f&g\\ \hline
\lambda(x)&cdf&abf&bde&adg&efg&bcg&ace.
\end{array}
\tag{2}
\]
Each row has three points and each pair of rows meets in one point.
Thus these rows give the projective plane of order \(q=2\), and the cyclic triples satisfy the triangle-presentation conditions in CM94, Section 1, pp. 348--349.
The triangle-building construction recalled there applies to (1): \(\Gamma\) acts simply transitively and type-rotatingly on the vertices.
This is the geometric input used here; a finite quotient alone would not supply it.

Let \(S_{m,n}\subset\Gamma\) denote the elements whose minimal words contain \(m\) positive generators and \(n\) inverse generators.
These numbers are intrinsic; equivalently they are the two coordinates of the vertex displacement in a sector of the building.
They agree with the positive-then-negative normal form of CM94, Section 6, equation (6.1), p. 374.
Put
\[
 N_{m,n}=|S_{m,n}|,\qquad
 \mu_{m,n}=\frac{1}{N_{m,n}}\sum_{x\in S_{m,n}}x.
 \tag{3}
\]
CM94, Corollary 2.2, pp. 352--353, gives
\[
 N_{0,0}=1,\quad
 N_{m,0}=N_{0,m}=7\,4^{m-1}\ (m\ge1),\quad
 N_{m,n}=42\,4^{m+n-2}\ (m,n\ge1).
 \tag{4}
\]
A finite biradial coefficient is a finite complex linear combination of the \(\mu_{m,n}\); equivalently its Fourier coefficients are constant on each \(S_{m,n}\).
The biradial algebra is
\[
 \mathcal A=\operatorname{span}_{\mathbb C}\{\mu_{m,n}:m,n\ge0\}
           =\mathbb C[H,H^*],
 \qquad H=a+b+c+d+e+f+g.
 \tag{5}
\]
It is commutative, \(H\) is normal, \(\mu_{1,0}=H/7\), and \(\mu_{0,1}=H^*/7\).
These assertions are CM94, Proposition 2.3, pp. 353--354, transported from averaging operators to left convolution.
Concretely inversion of the group variable gives the required unitary identification of the source's right averaging convention with left convolution.
The canonical trace is always
\(\tau(x)=\langle x\delta_1,\delta_1\rangle\), with \(\tau(1)=1\).

## The precise spherical measure

Write
\[
 \mathbb T_2=\{(s_1,s_2,s_3)\in\mathbb T^3:s_1s_2s_3=1\},
 \qquad
 s_3=(s_1s_2)^{-1},
 \tag{6}
\]
and give it normalized Haar measure \(ds=d\theta_1\,d\theta_2/(2\pi)^2\).
CM94, Proposition 3.1, p. 360, and Proposition 5.1, pp. 370--371, give
\[
 \widehat H(s)=h(s)=2(s_1+s_2+s_3),\qquad
 \widehat{H^*}(s)=h^\#(s)=2(s_1^{-1}+s_2^{-1}+s_3^{-1}),
 \tag{7}
\]
and
\[
 \tau(F(H,H^*))
 =\int_{\mathbb T_2}F(h(s),h^\#(s))\,w(s)\,ds,
\qquad
 w(s)=\frac7{16}
       \prod_{i<j}\left|\frac{s_i-s_j}{s_i-\tfrac12s_j}\right|^2
 \tag{8}
\]
for polynomials \(F\), and consequently for bounded Borel functional calculus.
The constant \(7/16\) is
\((q+1)(q^2+q+1)/(6q^3)\) at \(q=2\), not a normalization of \(H\) to a Markov operator.
In the source the spectral coordinate of \(\mu_{1,0}\) is \(h/7\).
The weight (8) has total integral one.
Its denominators never vanish on the torus, and its only zeros occur where two coordinates coincide.
It is therefore positive Haar-almost everywhere, with full support.
In particular it has the same null sets as Haar measure.

The six permutations of the \(s_i\), complex conjugation, and common multiplication \(s_i\mapsto\omega s_i\), \(\omega^3=1\), preserve \(w(s)\,ds\).
Permutation invariance of each modulus in (8) follows from
\(|s_i-\tfrac12s_j|=|s_j-\tfrac12s_i|\) on the unit circle.
The other two invariances follow directly from (8).
They are symmetries of the spherical measure; they are not asserted to be inner automorphisms of \(\mathcal N(\Gamma)\).

## Arbitrary-radius complex matrix ranks

Every nonzero Laurent polynomial in \(s_1,s_2\) vanishes on a Haar-null subset of \(\mathbb T^2\).
Indeed, after clearing negative exponents, expand in one variable.
Outside the null set on which all its coefficient polynomials vanish, the resulting one-variable polynomial has finitely many zeros.
The one-variable zero fact and Fubini's theorem prove the assertion.
The same conclusion holds for the measure (8).

The substitution
\[
 \mathbb C[X,Y]\longrightarrow
 \mathbb C[s_1^{\pm1},s_2^{\pm1}],
 \qquad (X,Y)\longmapsto(h,h^\#)
 \tag{9}
\]
is injective.
To verify this algebraically, for any \(x,y\in\mathbb C\) take the roots of
\[
 T^3-\tfrac{x}{2}T^2+\tfrac{y}{2}T-1.
\]
They are nonzero, have product one, and their sum and sum of inverses are \(x/2,y/2\).
Thus a polynomial identity in the Laurent variables would vanish at every \((x,y)\in\mathbb C^2\).
This proves injectivity, independently of an inference from a finite numerical sample.

Let \(P\in M_{m,n}(\mathbb C[X,Y])\), with arbitrary \(m,n\) and arbitrary degrees, and put
\[
 r=\operatorname{rank}_{\mathbb C(X,Y)}P.
 \tag{10}
\]
If \(r>0\), some \(r\)-minor is a nonzero polynomial.
Its pullback under (9) is a nonzero Laurent polynomial, so that minor is nonzero almost everywhere for (8).
Every larger minor is identically zero.
Hence the numerical matrix \(P(h,h^\#)\) has rank \(r\) almost everywhere.
The zero matrix case has \(r=0\) directly.

Let \(\operatorname{Tr}_n\) be the unnormalized matrix trace.
The kernel projection of \(P(H,H^*)\) lies in \(M_n(W^*(H))\), by spectral calculus of \(P^*P\).
The restricted canonical trace is exactly (8), so
\[
 \dim_{\mathcal N(\Gamma)}\ker P(H,H^*)=n-r,\qquad
 \operatorname{rk}_{\mathcal N(\Gamma)}P(H,H^*)=r.
 \tag{11}
\]
The trace in (11) is \(\operatorname{Tr}_n\otimes\tau\); dividing it by \(n\) would change the assertion.
No irreducible-representation multiplicity is inserted into this calculation: it takes place in the actual commutative subalgebra with the restricted regular trace.

By (5), (11) covers every finite matrix of finite biradial coefficients, with no bound on radius, matrix size or complex coefficient field.
Each individual matrix uses finitely many Laurent minors, so no countability restriction on its complex coefficients is involved.
The exceptional null set may depend on the matrix; no single null set is claimed to work for all complex matrices at once.
For a scalar nonzero biradial coefficient the operator has zero kernel and dense range.
It therefore has neither a left nor a right zero-divisor partner in \(\mathbb C[\Gamma]\), or indeed in the affiliated algebra.
This scalar conclusion permits an arbitrary, nonbiradial partner.

Every nonzero polynomial in \(H,H^*\) is invertible as an affiliated operator, and these commuting inverses identify an actual subfield
\[
 \mathcal F=\mathbb C(H,H^*)\subset U(\mathcal N(\Gamma)).
 \tag{12}
\]
The same rank formula holds for every matrix over \(\mathcal F\).
For example, multiply all entries by a common nonzero polynomial denominator; this central multiplier is an affiliated unit and preserves kernel dimension and algebraic rank.
This is a direct matrix consequence of the known Plancherel formula.
It does not establish the Atiyah conjecture for arbitrary matrices over \(\mathbb C[\Gamma]\).

## The selfadjoint adjacency spectrum and odd moments

Use the unnormalized selfadjoint operator
\[
 S=H+H^*.
 \tag{13}
\]
Its transform is
\[
 \widehat S(s)=4\operatorname{Re}(s_1+s_2+s_3).
 \tag{14}
\]
The range of the real part on \(\mathbb T_2\) is exactly \([-3/2,3]\).
For example, on writing \(r=(\theta_1+\theta_2)/2\) and \(d=(\theta_1-\theta_2)/2\), it becomes
\[
 2\cos r\cos d+2\cos^2r-1.
\]
Its minimum for fixed \(|\cos r|=x\) is \(2x^2-2x-1\ge-3/2\), and its maximum is at most \(3\).
Both endpoints are attained, and connectedness gives the whole interval.
Full support of (8) then gives the actual operator spectrum
\[
                    \sigma(S)=[-6,12].
 \tag{15}
\]
In particular this spectrum is not symmetric about zero.

The type homomorphism \(\Gamma\to\mathbb Z/3\mathbb Z\), sending all seven positive generators to one, rules out identity words of length three with both signs.
The positive length-three identity words are exactly the three cyclic permutations of each of the seven triangles.
One can see their completeness either from the triangle incidence condition or the source's geodesic normal forms.
Their inverse words give the other orientation.
Thus
\[
 \tau(H)=0,\qquad
 \tau(H^3)=\tau((H^*)^3)=21,\qquad
 \tau(H^2H^*)=\tau(H(H^*)^2)=0.
 \tag{16}
\]
These are finite word counts in the actual presentation; they agree with the existing J5 normal-form calculation.
Consequently
\[
       \tau(S)=0,\qquad \tau(S^2)=14,\qquad \tau(S^3)=42.
 \tag{17}
\]
For a nonzero \(\gamma\in\mathbb C\), the more general selfadjoint direction
\[
 S_\gamma=\gamma H+\overline\gamma H^*
 \tag{18}
\]
satisfies
\[
            \tau(S_\gamma)=0,\qquad
            \tau(S_\gamma^3)=42\operatorname{Re}(\gamma^3).
 \tag{19}
\]
It is nonconstant, and every level set has measure zero by the Laurent-polynomial argument.
Thus \(S_\gamma\) has no scalar spectral atoms.

## Affiliated anticommutators and an explicit lost-rank bound

Here is the operator argument needed to use these spectral data without cyclically moving an unbounded inverse through a trace.
Let \(M\) be a finite von Neumann algebra, \(u=u^*\in M\), and \(v\in U(M)\) satisfy
\[
                            vu=-uv.
 \tag{20}
\]
Taking adjoints and multiplying in the affiliated algebra shows that \(d=v^*v\) commutes with \(u\).
Commutation with the resolvent of \(d\) then gives commutation with its spectral calculus.
Therefore the bounded transform
\[
              T=v(1+v^*v)^{-1/2}\in M
 \tag{21}
\]
has the same kernel as \(v\) and satisfies \(Tu=-uT\).
The bounded selfadjoint intertwining theorem, obtained first for polynomials and then for bounded Borel functions by spectral calculus, gives
\[
              T\,1_E(u)=1_{-E}(u)\,T.
 \tag{22}
\]
If \(v\) is an affiliated unit, its polar partial isometry \(w\) is unitary.
Since \(|v|\) commutes with \(u\), cancellation on its full support gives
\[
                         wuw^*=-u.
 \tag{23}
\]
Thus the canonical spectral distribution of \(u\) must be symmetric about zero.
For bounded \(u\), all its odd trace moments must vanish.
This argument uses bounded unitary conjugacy for the trace conclusion, not a trace identity for unbounded similarity.

Apply (22) to \(u=S\) and \(E=(6,12]\).
By (15), \(1_{-E}(S)=0\), and hence every affiliated solution of \(vS=-Sv\), whether invertible or not, satisfies
\[
 p\le1_{\{0\}}(|v|),\qquad p=1_{(6,12]}(S).
 \tag{24}
\]
The trace of this forced kernel is
\[
 \delta=\tau(p)
 =\int_{\{\operatorname{Re}(s_1+s_2+s_3)>3/2\}}w(s)\,ds>0.
 \tag{25}
\]
An explicit elementary lower bound is available.
Take
\[
 \theta_1=\pi/3+t_1,\quad
 \theta_2=-\pi/3+t_2,\quad
 |t_1|,|t_2|\le1/12,\quad
 \theta_3=-t_1-t_2.
 \tag{26}
\]
The real part of the sum is at least \(2-4/12=5/3>3/2\).
At the center the three pairwise chord lengths are \(1,1,\sqrt3\); on this box each is at least \(1-3/12=3/4\).
Each denominator chord in (8) has modulus at most \(3/2\).
Thus \(w\ge(7/16)(1/2)^6=7/1024\) throughout the box.
Its normalized Haar area is \(1/(144\pi^2)\), so
\[
 \delta\ge\frac7{147456\pi^2},\qquad
 \operatorname{rk}_{M}(v)\le1-\frac7{147456\pi^2}.
 \tag{27}
\]
This lower bound is deliberately elementary, not an assertion that it is the exact positive spectral mass.
For a matrix \(v\in M_k(U(M))\) anticommuting with \(S I_k\), the same argument forces the kernel \(p I_k\), with unnormalized trace at least \(7k/(147456\pi^2)\).
In particular no such \(v\) can be an affiliated unit.

## An unconditional exclusion for one input in the splitting equations

Suppose
\[
 u=c+S_\gamma,\qquad
 c\in\mathbb R,\quad\gamma\ne0,
 \tag{28}
\]
and ask for an arbitrary \(v\in U(\mathcal N(\Gamma))\) satisfying
\[
               uv+vu=0,\qquad u^2+\alpha v^2=\beta,
 \qquad \alpha\in\mathbb C^\times,\quad\beta\in\mathbb C.
 \tag{29}
\]
There is no such \(v\) whenever
\[
                    c\ne0\quad\hbox{or}\quad
                    \operatorname{Re}(\gamma^3)\ne0.
 \tag{30}
\]
In particular this excludes every real nonconstant affine input \(u=tS+c\).

To prove this, \(\beta-u^2\) is a nonzero polynomial in \(H,H^*\), since \(u\) is a nonconstant affine polynomial in two algebraically independent variables.
By (11)--(12), it is an affiliated unit.
Equation (29) makes \(v^2\), and hence \(v\), an affiliated unit.
No hypothesis that the entire rational division closure of \(\mathbb Q[\Gamma]\) is a division ring has been used.
The polar argument (23) now applies.
Its first-moment consequence forces \(\tau(u)=c=0\).
Its third-moment consequence then contradicts (19) if \(\operatorname{Re}(\gamma^3)\ne0\).
This proves the exclusion with a completely unrestricted, possibly unbounded and nonbiradial second input.
Multiplying \(u\) by a fixed nonzero complex scalar gives the same exclusion after dividing the square relation by that scalar squared.
In particular the corresponding skew-adjoint inputs \(i(tS+c)\) are covered.

There is a precise limit to the odd-moment test.
When \(c=0\) and \(\operatorname{Re}(\gamma^3)=0\), the distribution of \(S_\gamma\) actually is sign symmetric.
Writing \(\gamma=|\gamma|e^{i\theta}\), the condition implies that \(-e^{-2i\theta}\) is a cube root of unity.
The measure-preserving map \(s_i\mapsto\omega\overline{s_i}\) for this cube root sends the transform in (18) to its negative.
Thus vanishing of the odd moments in these directions is not missing a higher odd moment of the same scalar distribution.
It does not prove the existence of an intertwining affiliated unit, an inner implementation of this torus symmetry, or a solution of (29).

More generally, let \(u\in\mathcal F\) be nonconstant and selfadjoint, allowing an unbounded rational function.
Every level set of its rational transform is null after clearing denominators.
Hence \(\beta-u^2\) is again an affiliated unit for every scalar \(\beta\).
Any solution of (29) would force unitary conjugacy of \(u\) and \(-u\), by the same affiliated polar calculation.
Here algebraic commutation of the selfadjoint affiliated operators \(u\) and \(v^*v\) gives commutation of their bounded resolvents and hence of their spectral calculi, which justifies the unbounded extension of that calculation.
Thus failure of sign symmetry of its canonical spectral distribution is a further sufficient exclusion.
For unbounded \(u\), this last test is phrased using spectral projections and bounded Borel functions, rather than assuming finite odd moments.

## What the MASA result adds, and what remains open

CM94, Theorem 6.1, p. 374, proves that an \(\ell^2(\Gamma)\) function commuting by convolution with both \(\mu_{1,0}\) and \(\mu_{0,1}\) is biradial.
As explained in the source, this implies that
\[
                       \mathcal B=W^*(H)
 \tag{31}
\]
is maximal abelian in \(\mathcal N(\Gamma)\).
For instance a bounded operator commuting with \(\mathcal B\) has a biradial coefficient vector, and its trace-preserving conditional expectation onto \(\mathcal B\) has the same vector, hence is that operator.
For an affiliated operator commuting with both \(H\) and \(H^*\), bounded transforms of it and of its adjoint give the corresponding affiliated commutant statement.

The source theorem does not identify the normalizer of \(\mathcal B\) as \(\mathcal B\), and no singular-MASA claim is being inferred from maximal abelianness.
Moreover commuting with a single selfadjoint direction \(S_\gamma\), or with its square, has not been identified here with commuting with the whole biradial algebra.
Those distinctions matter in the sign-symmetric exceptional directions above.

The matrix result (11) and the scalar no-zero-divisor consequence require no rational Atiyah assumption on \(\Gamma\) or its powers.
They restrict one coefficient or every matrix entry to the explicitly defined biradial algebra; they do not restrict arbitrary group-ring coefficients merely by their word radius.
The splitting obstruction (29)--(30) goes further in a different direction: only the first input has the stated affine biradial form, while the second input is arbitrary affiliated.
Neither result settles arbitrary complex coefficients for this group or the original all-group objectives.

---
author: Yin
---

# Testing the normal converse on exchange-symmetric pairs with product two-marginal law

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(K_{\rm proj}\) be the [trace-half projection supremum](Yin_C_F0308_v1.md#statement) of the single-input right slice-to-vacuum ratio.
For \(K_{\rm ind}\) use instead the [exchange-symmetric actual normal pairs](Yin_C_F0311_v1.md#statement) \(W_0,W_1\) with the additional property
\[
     \tau(f(W_0)g(W_1))
           =\tau(f(W_0))\,\tau(g(W_1))                                  \tag{1}
\]
for every two bounded Borel functions on the common marginal spectrum.
Take the supremum at the first coordinate over all represented starred polynomial contractions, dividing by the Hilbert norm of its actual vacuum.
Write \(K_{\rm ind,mix}\) for the same supremum after projecting the output orthogonally off \(L^2(W^*(W_0))\).
In the extended nonnegative reals,
\[
 K_{\rm ind}\le K_{\rm proj}\le2\sqrt2 K_{\rm ind},\qquad
 K_{\rm ind,mix}\le K_{\rm ind}\le\sqrt{K_{\rm ind,mix}^2+(1+\sqrt2)^2}.
                                                                         \tag{2}
\]
Every finite witness in a trace-half projection model transfers to one pair satisfying (1) with ratio at least the old ratio divided by \(2\sqrt2\), up to arbitrarily small additive error.
The [universal normal implication](../tasks/Yin_T_F0011_v1.md#contract) \(\mathsf A\Rightarrow\mathsf S\) is therefore equivalent to finiteness of either new supremum.
The conclusion concerns uniform estimates and finite witnesses, and leaves open whether one pair satisfying (1) can have infinite cost.

## Argument

### A symmetry with exact product traces

The coordinating agent proposed balancing two matrix halves with a free symmetry and retaining the old coefficient on a cycle of four off-diagonal entries.
Take an input \(R=W^*(Z,J)\), with \(J=J^*=J^{-1}\), \(\tau(J)=0\); its projection coefficient is \((1+J)/2\).
The relative actual derivative \(\delta\) takes \(Z\) to \(1\otimes1\) and kills \(J\).
Write \(\xi\) for its vacuum and \(x=x(Z,J)\) for the chosen polynomial contraction, with right-slice Hilbert norm \(b\).
Replacing the projection by its affine expression in \(J\) represents the same witness.
Form \(R'\) by freely adjoining seven freely independent standard semicirculars \(S_2,\ldots,S_8\) to \(R\), put \(A=M_4(R')\), and take \(N=A*W^*(D)\) where \(D\) is a centered symmetry freely independent of \(A\).
Equip \(\mathcal M=M_2(N)\) and its subalgebra \(M_2(A)=M_8(R')\) with normalized matrix traces and use \(e_i\) for the eight diagonal slot projections, each of trace \(t=1/8\).
For \(\alpha>0\) with \(\alpha\|Z\|\le1\), put
\[
 W=e_1\alpha Z+\sum_{i=2}^8 e_i(10i+S_i),\qquad
 U=\tfrac12\begin{pmatrix}
 1&1&1&1\\1&J&-1&-J\\1&-1&1&-1\\1&-J&-1&J
 \end{pmatrix}\in A,\qquad
 s_0=\tfrac1{\sqrt2}\begin{pmatrix}D&U\\U^*&-U^*DU\end{pmatrix}.
\]
The row and column inner products give \(UU^*=U^*U=1\) using \(J^*=J\) and \(J^2=1\).
Matrix multiplication gives \(s_0^2=1\) with zero off-diagonal entries, and \(s_0\) is selfadjoint and centered.

Write \(f(W)=\operatorname{diag}(f_A,f_B)\) in the two outer halves, and similarly for \(g\), temporarily denoting the bottom half by a subscript \(B\).
The trace of \(f(W)s_0g(W)s_0\) is one fourth of the sum of the normalized internal traces of
\[
               f_A D g_A D,\quad f_A U g_B U^*,\quad
               f_B U^* g_A U,\quad f_B(U^*DU)g_B(U^*DU).
\]
The first and fourth traces factor into the separate traces of the displayed diagonal inputs, since each of \(D,U^*DU\) is a centered symmetry free from \(A\) in the scalar trace.
For the second trace the matrix expansion gives \(1/16\) times the sum, over \(i\le4<j\), of the \(R'\) traces of \(f_i u_{ij}g_j u_{ij}^*\); here each \(u_{ij}\) is \(1,-1,J\), or \(-J\), with the factor \(1/2\) already included in the prefactor.
The variable \(g_j\) belongs to the algebra of its own padding semicircular, which is free from the algebra containing \(f_i\) and \(u_{ij}\).
Cyclicity gives \(\tau_{R'}(f_i u_{ij}g_j u_{ij}^*)=\tau_{R'}(f_i)\tau_{R'}(g_j)\).
The third trace factors by the same expanded computation with the test functions interchanged.
Thus, for bounded Borel tests,
\[
          \tau(f(W)s_0g(W)s_0)=\tau(f(W))\tau(g(W)),\qquad
          \tau(f(W)s_0)=0.                                               \tag{3}
\]
The second equality follows from the two centered free diagonal blocks.
The sign change of \(D\) fixing \(A\), applied entrywise in \(M_2(N)\) and composed with conjugation by \(\operatorname{diag}(1,-1)\), is a trace-preserving involution fixing \(W\) and negating \(s_0\).
This grading needs no symmetry of the input pair \(Z,J\).

### Making the sign a relative coefficient

On the base core in \(R'\) let \(d_1\) extend \(\delta\) by zero on all padding factors, and for \(i\ge2\) let \(d_i\) differentiate \(S_i\), killing the other factors.
The [free extension and matrix lift](Yin_C_F0306_v1.md#matrix-derivations-and-the-off-diagonal-correction) give actual vacua \(\xi_1=\xi,\ \xi_i=S_i\).
For each \(i\) lift \(d_i\) to \(A\) in the inner matrix slot \(r=1+((i-1)\bmod4)\): an entry contribution \(d_i x_{ab}=h\otimes k\) is inserted as \(E_{ar}h\otimes E_{rb}k\), extended linearly and continuously on Hilbert tensor values.
Extend this lifted derivation to the algebraic free-product core in \(N\) by killing \(D\); the centered reduced-word argument preserves its vacuum.
Lift once more into \(M_2(N)\) at outer slot \(1\) for \(i\le4\) and \(2\) otherwise.
Both lifts obey the matrix-entry product rule and kill the corresponding matrix units.
The two trace scalings \(1/4\) and \(1/2\) give final vacuum \(t e_i\xi_i\) of norm \(t^{3/2}\|\xi_i\|_2\); the free extension between them is trace-isometric on the base.
In particular all lifts kill \(s_0\), since they kill \(D\), all matrix units and the entries \(1,J\) used in \(U\).
Sum the lifts, dividing the first one by \(\alpha\), to obtain \(L W=\sum_i e_i\otimes e_i\) and \(L s_0=0\).
The vacuum norm is at most \(t^{3/2}\|\xi\|_2/\alpha+t^{3/2}\sqrt7\).

The eight slot spectra are separated by gaps greater than one.
As in the matrix lift proof, add the outer inner derivation \(a\mapsto a\cdot K-K\cdot a\), where \(K(v,w)=1/(v-w)\) on distinct pieces of the spectrum of \(W\) and zero otherwise, with \(\|K\|_2\le1\).
The resulting \(L'\) takes \(W\) to \(1\otimes1\), has vacuum cost at most two more and satisfies \(\|L's_0\|_2\le2\).
The value at \(W^*\) is the normal marginal phase since \(W\) has diffuse spectral law. [Forced phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability)
Here the input marginal is diffuse by restriction of the actual distinguished vacuum to the scalar normal coordinate.

Adjoin a standard semicircular \(S\) freely to \(\mathcal M\), let \(T=s_0+\epsilon S\), \(0<2\epsilon<1/4\), and set \(s=\operatorname{sgn}T\).
Extend \(L'\) by zero at \(S\) and add the free noise derivative with insertion \(-L's_0/\epsilon\) at \(S\), which has vacuum norm at most \(2/\epsilon\). [Free-noise correction](Yin_C_F0306_v1.md#making-the-coefficient-an-actual-selfadjoint-coordinate)
The sum kills \(T\), hence also \(s\) on the bounded graph extension by uniform polynomial approximation on its gapped spectrum.
The same continuous function equal to the sign on both spectra shows \(\|s-s_0\|\to0\); these elements are independent of \(\alpha\).
Extending the grading by \(S\mapsto-S\) negates \(s\) and fixes \(W\).
Restricting to the generated \(M'=W^*(W,s)\) gives an actual relative derivative \(\delta'\), since the unit and phase at \(W,W^*\) and the zero at \(s\) lie in its intrinsic coarse space.
Projection of the ambient vacuum supplies the relative vacuum \(\xi'\) with
\[
              \|\xi'\|_2\le t^{3/2}\|\xi\|_2/\alpha
                              +t^{3/2}\sqrt7+2+2/\epsilon .               \tag{4}
\]

The exact two-block law survives taking the sign.
Let \(B_0=\operatorname{span}\{1,s_0\}\).
By the grading and freeness, \(\mathbb E_{\mathcal M}s=\mathbb E_{B_0}s=c s_0\) for a real \(c\); indeed on \(W^*(B_0,S)\) the first expectation agrees with the second by reduced words.
For \(g=g(W)\), (3) gives \(\mathbb E_{B_0}g=\tau(g)1\).
The [conditional two-block calculation](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) applied with this base symmetry gives
\[
               \mathbb E_{\mathcal M}(s g s)=c^2s_0g s_0+(1-c^2)\tau(g)1 .
\]
In detail \(d=s-cs_0\) has zero conditional mean and \(\mathbb E_{\mathcal M}d^2=(1-c^2)1\).
In \(d(g-\tau(g))d\), the neighboring \(B_0\) coefficients of reduced centered-over-\(B_0\) words multiply \(g-\tau(g)\) into a base factor centered over \(B_0\), hence scalar-centered.
The neighboring noise letters stay separated, giving zero conditional mean onto \(\mathcal M\); weak density and separate normality extend this computation to \(d\).
The two linear terms in \(d\) have zero conditional mean by bimodularity.
Pairing the displayed equality with \(f(W)\) and using (3) proves \(\tau(f(W)s g(W)s)=\tau(f(W))\tau(g(W))\).

### Recovering the finite witness and passing to the even algebra

Let \(e=e_1\) and define the selfadjoint corner coefficient
\[
               J_\epsilon=64\,\operatorname{Re}(e_1s e_5s e_2s e_6s e_1).
\]
At \(s_0\) the four entries along the indicated cycle are respectively \(1,1,J,1\) times \(1/\sqrt8\).
The resulting element is \(e_1J\) after the factor 64.
Consequently \(\|J_\epsilon-e_1J\|\to0\) in the common ambient corner independently of \(\alpha\).
Each slot projection is a smooth function of \(\operatorname{Re}W\) constant on neighborhoods of its eight disjoint spectral pieces.
The [cut projection and graph comparison](Yin_C_F0308_v1.md#direct-comparison-of-the-original-and-compressed-slices) therefore applies: approximation in \(C^1\) gives joint norm and coarse convergence with derivative \((e_i(v)-e_i(w))/(v-w)\).
Restrict the inner legs by \(\theta=I_{e\otimes e}\delta'\).
All slot projections and \(s\) are killed by \(\theta\), so \(\theta J_\epsilon=0\).
On \(eWe/\alpha=e_1 Z\), \(\alpha\theta\) takes value \(e\otimes e\), while on its adjoint it is the original scalar phase in the normalized corner.

Evaluate \(x(Z,J)\) at \(eWe/\alpha,J_\epsilon\) with unit \(e\), calling the result \(x_\epsilon\).
The previous norm and graph extension justifies its product rule and approximation from the relative model's original core.
The represented input norm tends to \(\|x\|\), and the normalized corner slice of \(\alpha\theta x_\epsilon\) tends in the ambient corner Hilbert norm to the old right slice embedded in slot one.
Indeed the product rule has finitely many terms with unchanged normalized base tensors and operator-norm convergence of all coefficient letters.
The normalized trace on the ambient corner restricts to the input trace on the embedded \(R\); the test in the generated algebra uses \(J_\epsilon\), so no membership of the old \(e_1J\) there is required.
These comparisons after scaling depend on \(\epsilon\) alone.

Let \(a'\) be the relative core cost at \(W\) in \(M'\).
For a corner graph test \(y=eye\), the same cut comparison gives
\[
     t^{3/2}\|(\mathrm{id}\otimes\tau_e)\theta y\|_{2,\tau_e}
           =\|(E'(ye)-yE'(e))e\|_2\le2a'\|y\|,\qquad
     E'=(\mathrm{id}\otimes\tau)\delta',\quad\tau_e=\tau/t.
\]
This is the traced product rule with the inner cut on each leg; the factor is \(t\) from the trace and \(\sqrt t\) from the first Hilbert leg.
The bound holds on graph limits by norm approximation when \(a'<\infty\).
For any \(\eta>0\) first choose \(\epsilon\) so that \(\|x_\epsilon\|\le1+\eta\) and its scaled corner slice norm is at least \(b-\eta\).
Combining the last inequality with (4) and then taking \(\alpha\) sufficiently small gives \(a'/\|\xi'\|_2\) at least \(b/(2\|\xi\|_2)\) up to arbitrarily small additive error, also if \(a'=\infty\).
The two vacuum norms are positive by the unit derivative at the normal generator.

Apply the [even-algebra transfer](Yin_C_F0311_v1.md#derivations-on-the-even-algebra) to the graded relative model \(W,s\).
The fixed algebra \(W^*(W,sWs)\) has an exchanging trace-preserving involution, actual vacua of norm \(\|\xi'\|_2\) at both coordinates, and first-coordinate cost at least \(a'/\sqrt2\).
Its second marginal evaluates \(g(sWs)=s g(W)s\), so the exact product traces just proved give (1) for all bounded Borel \(f,g\).
Selecting a polynomial from the cost supremum with arbitrarily small additional loss gives the finite-witness assertion and the upper bound for \(K_{\rm proj}\) in (2).
The reverse inequality follows by the [crossed-product realization](Yin_C_F0311_v1.md#realizing-each-exchange-symmetric-pair) of any such exchange pair as a trace-half projection model, preserving its first slice on the even core.
The [marginal projection bound](Yin_C_F0311_v1.md#the-output-outside-the-marginal) is pointwise over exchange pairs, so restricting its orthogonal square estimate gives the second comparison in (2).
The universal equivalence follows from the projection criterion.
The product law fixes the ordered two-marginal traces; higher mixed words are still admitted as inputs to the tests.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:31 |
| status | open |
| reason | Fix the matrix sign construction and finite-witness reduction with exactly product two-marginal law for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite ratio transfer with loss \(2\sqrt2\), product traces on all Borel rectangles, mixed-output comparison and uniform criterion. |
| argument | [Argument](#argument) | Eight-slot trace computation, two matrix lifts, independent noise correction, exact conditional smoothing, four-entry cycle, and even-algebra transfer. |
| dependency | [Projection reduction](Yin_C_F0308_v1.md#argument) | Trace-half characterization, spectral cut approximants and the factor-two direct corner estimate. |
| dependency | [Matrix and free-noise construction](Yin_C_F0306_v1.md#argument) | Entrywise pivot lifts with normalized vacuum cost, cross-spectrum correction, and insertion at a free semicircular. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Intrinsic adjoint-generator derivative in the diffuse marginal coarse space. |
| dependency | [Conditional two-block formula](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Conditional mean of a centered perturbation and the quadratic expectation over the base. |
| dependency | [Exchange and mixed output](Yin_C_F0311_v1.md#argument) | Actual even pair, cost loss \(\sqrt2\), crossed-product converse and pointwise bound for the marginal output. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:39 |
| status | proved |
| reason | Adopt the finite-test reduction to product two-marginal traces after independent verification of the matrix construction and its five inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite ratio transfer with loss \(2\sqrt2\), product traces on all Borel rectangles, mixed-output comparison and uniform criterion. |
| argument | [Argument](#argument) | Eight-slot trace computation, two matrix lifts, independent noise correction, exact conditional smoothing, four-entry cycle, and even-algebra transfer. |
| dependency | [Projection reduction](Yin_C_F0308_v1.md#argument) | Trace-half characterization, spectral cut approximants and the factor-two direct corner estimate. |
| dependency | [Matrix and free-noise construction](Yin_C_F0306_v1.md#argument) | Entrywise pivot lifts with normalized vacuum cost, cross-spectrum correction, and insertion at a free semicircular. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Intrinsic adjoint-generator derivative in the diffuse marginal coarse space. |
| dependency | [Conditional two-block formula](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Conditional mean of a centered perturbation and the quadratic expectation over the base. |
| dependency | [Exchange and mixed output](Yin_C_F0311_v1.md#argument) | Actual even pair, cost loss \(\sqrt2\), crossed-product converse and pointwise bound for the marginal output. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0329_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

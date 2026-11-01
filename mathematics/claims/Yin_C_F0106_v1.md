---
author: Yin
---

# Finite-dimensional tracial free factors satisfy bounded division-closure equality

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Bounded Division Closure for Finite-Dimensional Free Factors

<a id="statement"></a>
<a id="yin_c_f0106"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Record kind: substantive continuation of [Yin_T_F0007](../tasks/Yin_T_F0007_v1.md#yin_t_f0007).
Assessment at creation: complete candidate, awaiting independent mathematical review.
This file assigns no Claim ID or mathematical Role.
The [reviewed projection proof](Yin_C_F0105_v1.md) is retained unchanged.

**Outcome.**
The projection mechanism extends to finitely many arbitrary finite-dimensional tracial star-algebra factors, including matrix factors and arbitrary faithful central trace weights.
The new obligations are the complex structure constants in the commutator columns and a matrix-valued diagonal action in the homogeneous estimate.
Both are proved below.
The bounded resolvent and finite bounded scalar inverses then follow from the already reviewed reconstruction argument.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0106** after [complete independent review](../audits/reviews/Yin_R_F0116_v1.md#8-coordinated-wording-correction-and-verification-record).
The exact finite-dimensional-factor equality and finite-spectrum normal application below are accepted.
This dated assessment supersedes the initial candidate labels; no Role, lemma extraction or manuscript designation is assigned.
Yin_T_F0007 retains its diffuse and proper non-star input questions.

## 1. Exact statement and scope

Let \(\mathcal B_1,\ldots,\mathcal B_s\) be finite-dimensional complex unital C*-algebras, with faithful tracial probability states \(\tau_i\).
Form their tracial von Neumann free product, namely the von Neumann closure of the reduced C*-free product in its trace representation:
\[
 (\mathcal M,\tau)=*_{i=1}^s(\mathcal B_i,\tau_i),
 \qquad
 A=\operatorname{alg}_{\mathbb C}(1,\mathcal B_1,\ldots,\mathcal B_s)
          \subseteq\mathcal M.
 \tag{1}
\]
Here \(A\) contains the full canonical copies of the factor algebras; in particular it is a star algebra.
The candidate conclusion is
\[
 \operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M
       =\operatorname{Div}_{\mathcal M}A.
 \tag{2}
\]
Both closures use scalar inverses in their stated ambient algebras.
Neither is assumed to be a division ring.

This includes every finite family of freely independent normal variables with finite spectra, with arbitrary nonzero atom weights: their spectral projections are polynomials in the original normal variables, as checked in Section 8.
It also includes free products of full matrix algebras and finite direct sums thereof, with arbitrary faithful tracial weights.

The statement does not replace each \(\mathcal B_i\) by an arbitrary proper non-star subalgebra that merely generates it as a von Neumann algebra.
Such a replacement would change the polynomial algebra whose bounded scalar inverses must be reconstructed.
Thus this is a substantial sufficient case of Yin_T_F0007, not its full permanence assertion.

## 2. Reuse and source boundary

The current goal, the [free-projection reconstruction](Yin_C_F0105_v1.md) and its [independent review](../audits/reviews/Yin_R_F0115_v1.md#original-f0046-account) were read before this continuation.
That proof supplies the following reusable mathematical steps:

- Yin_C_F0034 gives the affiliated-to-bounded finite-commutator implication for any finite bounded auxiliary family with finite-rank generator commutators.
- The accepted Miy22 finite-residual theorem supplies a minimal representation, whose matrix entries are finite linear combinations of shifted scalar coefficients.
- Square-summable minimal state entries give an exponentially decaying positive-map energy.
- A homogeneous operator estimate and vanishing state products on forbidden words give a bounded finite matrix resolvent.
- Positive Schur complements reconstruct every entry of that bounded matrix inverse by finitely many bounded scalar inverses in a star algebra.

The exact supporting interfaces remain [Yin_C_F0034, assertion 4](Yin_C_F0034_v1.md#yin_c_f0034) and [Miy22-U002](../audits/literature/Miy22/Yin_U002.md#miy22-u002).
The last three steps are reused from Sections 6–7 of the reviewed projection proof, with their hypotheses checked again in Section 7 below.
This is proof dependence on those arguments, not a claim that the present conclusion was already covered by their projection statement.

Local searches for finite-dimensional free-factor closure, matrix factors, centered orthonormal bases and the registered RX06 source found no already recorded extension establishing (2).
A bounded follow-up primary search for rational closures of finite-dimensional reduced free products found no verified ready-made replacement for this proof.
No novelty or exhaustive literature claim follows.

The selected primary [Ricard–Xu version arXiv:math/0505302v2](https://arxiv.org/pdf/math/0505302), 2016-02-27, 25 pages, was revisited at Section 1, PDF pp. 2–3, and the upper-bound proof of Theorem 2.5, PDF pp. 6–7.
These passages give the general reduced free-product Hilbert representation and the decomposition into creation, annihilation and a single diagonal action; finite-dimensional commutativity is not a premise there.
Publication metadata and the retained inspection boundary are in the [literature registry](../literature/readme.md) under RX06 and the [projection source table](Yin_C_F0105_v1.md#1-precise-statement-and-reuse-boundary).
No new acquisition or whole-source audit is claimed.
The exact scalar constant and complex coefficient identity needed here are proved directly below.

## 3. Selfadjoint centered bases and the actual multiplication constants

Write \(m_i=\dim_{\mathbb C}\mathcal B_i-1\).
A scalar factor has \(m_i=0\) and can be omitted.
If all factors are scalar, (2) is immediate.
For every remaining factor choose a selfadjoint basis
\[
 x_{i,1},\ldots,x_{i,m_i}
       \quad\text{of }\mathcal B_i^0=\ker\tau_i
\]
such that
\[
 \tau_i(x_{i,a}x_{i,b})=\delta_{ab}.
 \tag{3}
\]
To justify the choice, the selfadjoint centered part is a real vector space on which \((a,b)\mapsto\tau_i(ab)\) is real, symmetric and positive definite.
Traciality gives symmetry and reality; faithfulness gives positive definiteness.
Real Gram–Schmidt therefore yields a selfadjoint orthonormal real basis.
Taking real and imaginary parts of any centered element shows that the same family is a complex basis of \(\mathcal B_i^0\).

The multiplication constants are defined by
\[
 x_{i,b}x_{i,c}
    =\delta_{bc}1+\sum_{a=1}^{m_i}\gamma^{\,i,a}_{bc}x_{i,a},
 \qquad
 \gamma^{\,i,a}_{bc}
    =\tau_i(x_{i,a}x_{i,b}x_{i,c}).
 \tag{4}
\]
They need not be real.
In particular
\[
 \overline{\gamma^{\,i,a}_{bc}}
       =\gamma^{\,i,a}_{cb},
 \tag{5}
\]
by taking adjoints and cycling the trace.
None of the coefficient calculations below replaces a \(\gamma\) by its conjugate without taking an adjoint.

Use the finite alphabet
\[
 \mathscr L=\{(i,a):1\leq i\leq s,\ 1\leq a\leq m_i\},
\]
and let \(\operatorname{fac}(i,a)=i\).
A word in this alphabet is called reduced if consecutive letters have different factors.
Let \(\mathcal W\) include all such words and the empty word.
For \(w=t_1\cdots t_n\in\mathcal W\), put
\[
 x_w=x_{t_1}\cdots x_{t_n},\qquad
 e_w=x_w\Omega,\quad \Omega=1.
 \tag{6}
\]
The free-product Hilbert representation supplies an orthonormal basis \((e_w)_{w\in\mathcal W}\) of \(H=L^2(\mathcal M,\tau)\).
All letters are selfadjoint, so
\[
 x_w^*=x_{w^{\mathrm{rev}}},
 \qquad \tau(x_v^*x_w)=\delta_{v,w}.
 \tag{7}
\]
No conjugation of a word label is required when it is reversed.

For left multiplication by a letter, the only nontrivial case is a word whose first factor agrees:
\[
 x_{i,b}e_{(i,c)v}
       =\delta_{bc}e_v
            +\sum_a\gamma^{\,i,a}_{bc}e_{(i,a)v}.
 \tag{8}
\]
If the word is empty or starts in another factor, multiplication creates the letter \((i,b)\).

## 4. Bounded end deletion and the finite-rank boundary defect

For \(t=(i,a)\) define \(R_t\) on the orthonormal basis by
\[
 R_t e_{wt}=e_w,\qquad
 R_t e_w=0\ \text{when }w=\varnothing
                          \text{ or its terminal letter is not }t.
 \tag{9}
\]
This is a partial isometry of norm at most one.
Write \(P=P_\Omega\).

For letters \((i,a)\) and \((j,b)\), the exact identity is
\[
 [R_{i,a},x_{j,b}]=
 \begin{cases}
 0,&i\ne j,\\[2mm]
 \displaystyle
 \delta_{ab}P+\sum_{c=1}^{m_i}\gamma^{\,i,a}_{bc}P x_{i,c}
                   -x_{i,b}P x_{i,a},&i=j.
 \end{cases}
 \tag{10}
\]
Indeed (8) and end deletion commute on words of length at least two.
On the vacuum the commutator is \(\delta_{ab}\Omega\) for the same factor and zero otherwise.
On the one-letter vector \(e_{i,c}\) it is
\[
 \gamma^{\,i,a}_{bc}\Omega-\delta_{ac}e_{i,b}.
 \tag{11}
\]
It vanishes on the one-letter vectors from every other factor.
Since \(P x_{i,c}e_{j,d}=\delta_{ij}\delta_{cd}\Omega\), these values give exactly (10).
Its range is contained in \(\operatorname{span}\{\Omega,e_{i,b}\}\), so the rank is at most two even when the factor has many basis letters.

The absence of a conjugate in the middle term is important.
For normalized-trace \(M_2(\mathbb C)\), take the selfadjoint Pauli basis
\[
 x_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 x_2=\begin{pmatrix}0&-\mathrm i\\\mathrm i&0\end{pmatrix},\quad
 x_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Then \(x_1x_2=\mathrm i x_3\), and (11) gives \([R_3,x_1]e_2=\mathrm i\Omega\).
Conjugating \(\gamma^3_{12}\) in (10) would give the wrong sign.
This direct finite-dimensional check records the coefficient convention, not a separate theorem or numerical experiment.

Apply Yin_C_F0034 with the finitely many bounded operators \(D_{t,0}=R_t\) and with both its domain module and all adjoint test modules equal to \(H\).
All its hypotheses hold: the modules are dense left \(\mathcal M\)-modules, and \(R_t,R_t^*\) are everywhere bounded.
Formula (10) supplies finite-rank commutators with a finite generating basis of \(A\).
Thus
\[
 f\in\operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M
 \quad\Longrightarrow\quad
 [R_t,f]\in\mathcal F(H)\quad(t\in\mathscr L).
 \tag{12}
\]
The affiliated inference uses cleared bounded fractions in Yin_C_F0034.
No undefined commutator with an unbounded rational expression is evaluated directly.

## 5. The selected columns still give all residuals

Expand a bounded \(f\) as
\[
 f\Omega=\sum_{v\in\mathcal W}\beta_v e_v,
 \qquad\sum_{v\in\mathcal W}|\beta_v|^2<\infty.
 \tag{13}
\]
Define \(\beta_v=0\) on nonreduced words of the full free monoid on \(\mathscr L\).

For \(t=(i,a)\) and reduced \(w\) that is empty or whose terminal factor differs from \(i\), the identity needed for reconstruction is
\[
 [R_t,f]e_w
       =\sum_{u\in\mathcal W}\beta_{u t w^{\mathrm{rev}}}e_u.
 \tag{14}
\]
A restriction only on the terminal letter, as opposed to its factor, would not be sufficient.

Here is the full polynomial cut computation.
For reduced \(v\), the Leibniz rule gives a sum over all cuts \(v=u(i,b)q\), with \(b\) varying over the \(i\)-factor letters.
At such a cut, (10) contributes
\[
\begin{aligned}
 &\delta_{ab}\,\mathbf1_{\{w=q^{\mathrm{rev}}\}}e_u\\
 &\quad+\sum_c\gamma^{\,i,a}_{bc}\,
        \mathbf1_{\{w=q^{\mathrm{rev}}(i,c)\}}e_u
       -\mathbf1_{\{w=q^{\mathrm{rev}}(i,a)\}}e_{u(i,b)}.
\end{aligned}
 \tag{15}
\]
To check these pairings, \(x_{i,c}x_q\) and \(x_u x_{i,b}\) are reduced products at the cut.
Equation (7) therefore says that \(P x_{i,c}x_q e_w\) is the indicated Kronecker delta times \(\Omega\).
The scalar \(\gamma^{\,i,a}_{bc}\) remains unchanged because it multiplies an operator applied linearly to the input; no adjoint is being taken.
This explains every coefficient and conjugation in (15).

For the columns allowed in (14), both the second and third lines of (15) vanish.
The first line retains the unique cut with \(b=a\) and \(v=u t w^{\mathrm{rev}}\), proving (14) for polynomial \(f\).

For general bounded \(f\), its finite Fourier sums converge in \(L^2\).
For each fixed \(w\), right multiplication by \(x_w\) is bounded on \(L^2\), and \(R_t e_w\) is zero or another fixed reduced word vector.
Thus the commutator columns converge in \(H\).
Their residual columns converge as well, because \(u\mapsto u t w^{\mathrm{rev}}\) is injective.
This gives (14) without assuming norm convergence of the Fourier sums.

Every nonempty reduced suffix is \(tq\) with \(q\) empty or its first factor different from \(\operatorname{fac}(t)\).
Put \(w=q^{\mathrm{rev}}\) in (14).
The residual vector \((\beta_{utq})_u\) is then a column of \([R_t,f]\).
Nonreduced suffixes have zero residuals.
By (12), the right residual space of the full coefficient series is finite dimensional.

The accepted Miy22 finite-residual and minimality interfaces now give
\[
 \beta_w=\lambda\mu(w)\gamma,\qquad
 \mu(w)=\mu_{t_1}\cdots\mu_{t_n}
          \in M_N(\mathbb C),
 \tag{16}
\]
with a minimal finite representation.
Each matrix entry of \(\mu(w)\) is a fixed finite linear combination of coefficients \(\beta_{p w q}\), so
\[
 \sum_{w\in\mathscr L^*}\|\mu(w)\|_{\mathrm{HS}}^2<\infty.
 \tag{17}
\]
Minimality also converts the forbidden adjacent-factor relations into actual matrix zero products:
\[
 \mu_{i,a}\mu_{i,b}=0
       \quad(1\leq a,b\leq m_i).
 \tag{18}
\]
Indeed \(\beta_{p(i,a)(i,b)q}=0\) for all \(p,q\); the observable rows \(\lambda\mu(p)\) and reachable columns \(\mu(q)\gamma\) span the dual state space and state space, respectively.
Hence the middle matrix is zero.
This is stronger than vanishing only after the outer \(\lambda,\gamma\) multiplication.

## 6. The homogeneous estimate with a matrix diagonal action

Define partial left creation operators by
\[
 L_t e_w=
 \begin{cases}
 e_{tw},&w=\varnothing\text{ or its first factor differs from }\operatorname{fac}(t),\\
 0,&\text{otherwise}.
 \end{cases}
\]
Let \(Q_i\) project onto words whose first factor is \(i\), and set
\[
 T_{i,a}=Q_i x_{i,a} Q_i.
 \tag{19}
\]
This is the bounded centered multiplication, or diagonal, part.
Its norm is at most \(\|x_{i,a}\|\), and (8) gives
\[
 x_{i,a}=L_{i,a}+L_{i,a}^*+T_{i,a}.
 \tag{20}
\]
For letters \(t,z\) in different factors,
\[
 L_t^*L_z=L_t^*T_z=T_tL_z=T_tT_z=0.
 \tag{21}
\]
This uses different-factor support, not orthogonality of the individual \(T_{i,a}\) within one factor.

For a reduced word \(w=t_1\cdots t_n\), expansion of (20) therefore gives
\[
\begin{aligned}
 x_w
 &=\sum_{k=0}^n
     L_{t_1}\cdots L_{t_k}
     L_{t_{k+1}}^*\cdots L_{t_n}^*\\
 &\quad+\sum_{k=1}^n
     L_{t_1}\cdots L_{t_{k-1}}T_{t_k}
     L_{t_{k+1}}^*\cdots L_{t_n}^*.
\end{aligned}
 \tag{22}
\]
The zero products in (21) exclude every order except creation followed by annihilation, with at most one diagonal action between them.

Let
\[
 C_0=\max_i\left(\sum_{a=1}^{m_i}\|T_{i,a}\|^2\right)^{1/2}<\infty.
 \tag{23}
\]
For coefficients \(c_w\) on reduced words of length \(n\), we claim
\[
 \left\|\sum_{|w|=n}c_wx_w\right\|
   \leq(n+1+nC_0)
                  \left(\sum_{|w|=n}|c_w|^2\right)^{1/2}.
 \tag{24}
\]

For each fixed length, the creation operators \(L_u\) have mutually orthogonal ranges and are contractions.
Their row map and its adjoint column map have norm at most one.
At a fixed cut in the first line of (22), the middle coefficient matrix is
\[
 C_{u,v}=c_{u v^{\mathrm{rev}}},
\]
with zero for nonreduced concatenations.
Its operator norm is at most its Hilbert–Schmidt norm, equal to \((\sum_w|c_w|^2)^{1/2}\).
Inserting the creation row and annihilation column contractions gives the same bound for that cut.

At a fixed diagonal cut the middle operator matrix is
\[
 \sum_{i,a} C_{i,a}\otimes T_{i,a},\qquad
 (C_{i,a})_{u,v}=c_{u(i,a)v^{\mathrm{rev}}},
 \tag{25}
\]
where \(|u|=k-1\), \(|v|=n-k\).
The supports \(Q_i\) are orthogonal, so this matrix is the direct sum over \(i\) of its factor blocks, and is zero on the vacuum part.
Within a factor one must estimate the full sum over its letters.
Triangle inequality and Cauchy–Schwarz give
\[
\begin{aligned}
 \left\|\sum_a C_{i,a}\otimes T_{i,a}\right\|
 &\leq \sum_a\|C_{i,a}\|\,\|T_{i,a}\|\\
 &\leq
    \left(\sum_a\|T_{i,a}\|^2\right)^{1/2}
    \left(\sum_a\|C_{i,a}\|_{\mathrm{HS}}^2\right)^{1/2}\\
 &\leq C_0\left(\sum_{|w|=n}|c_w|^2\right)^{1/2}.
\end{aligned}
 \tag{26}
\]
The coefficient indices at a fixed cut are unique, so the last square sum is a subset of the indicated full word coefficient sum.
Multiplication by the row and column contractions preserves this bound.
Summing the \(n+1\) creation/annihilation cuts and the \(n\) diagonal cuts proves (24).

Thus the matrix factors introduce only the finite constant \(C_0\).
No exponential dependence on \(n\), no commutativity of the factors, and no reality of the structure constants is needed.

## 7. Reusing the bounded resolvent and scalar-pivot reconstruction

All hypotheses of Sections 6–7 of the reviewed projection argument now hold with the finite alphabet \(\mathscr L\), the homogeneous constant in (24), and the forbidden products (18).
For clarity, the resulting finite data and inverses are as follows.

Define
\[
 \Phi(S)=\sum_{t\in\mathscr L}\mu_t S\mu_t^*,\qquad
 Q=\sum_{n\geq0}\Phi^n(I_N).
 \tag{27}
\]
Equation (17) ensures convergence in matrix norm, \(Q\geq I_N\), and \(\Phi(Q)=Q-I_N\).
Unless every \(\mu_t\) is zero, the number \(c=1-\|Q\|^{-1}\) lies in \((0,1)\), and
\[
 \sum_{|w|=n}\|\mu(w)\|_{\mathrm{HS}}^2
       =\operatorname{Tr}\Phi^n(I_N)
       \leq c^n\operatorname{Tr}Q.
 \tag{28}
\]
The zero-state case gives a constant element.

Form
\[
 V=\sum_{t\in\mathscr L}\mu_t\otimes x_t\in M_N(A).
 \tag{29}
\]
By (18), every nonreduced word has zero state product.
Hence
\[
 V^n=\sum_{\substack{w\in\mathcal W\\|w|=n}}
                       \mu(w)\otimes x_w.
 \tag{30}
\]
There is no contribution from reducing a nonreduced operator word, since its matrix coefficient was already zero.
Applying (24) to the scalar entries and (28) yields
\[
 \|V^n\|\leq N(n+1+nC_0)
                \sqrt{\operatorname{Tr}Q}\,c^{n/2}.
 \tag{31}
\]
Thus \(B=I_N-V\) is boundedly invertible and \(B^{-1}=\sum_{n\geq0}V^n\) in matrix operator norm.

This inverse has entries obtained by the finite scalar procedure, not by treating the series as a rational expression.
Namely \(G=B^*B\) belongs to \(M_N(A)\) and is at least \(\delta I_N\), where \(\delta=\|B^{-1}\|^{-2}>0\).
For a successive positive block matrix
\[
 G_0=\begin{pmatrix}a&b\\b^*&D\end{pmatrix}\geq\delta I,
 \qquad S=D-b^*a^{-1}b,
 \tag{32}
\]
the scalar pivot \(a\geq\delta1\) has a bounded inverse and \(S\geq\delta I\).
The latter follows by testing \(G_0\) on \((-a^{-1}by,y)\).
The block formula
\[
 G_0^{-1}=
 \begin{pmatrix}
 a^{-1}+a^{-1}bS^{-1}b^*a^{-1}&-a^{-1}bS^{-1}\\
 -S^{-1}b^*a^{-1}&S^{-1}
 \end{pmatrix}
 \tag{33}
\]
recursively uses only finitely many bounded scalar inverses and ring operations.
Since \(A\) is a star algebra, every entry involved stays in \(\operatorname{Div}_{\mathcal M}A\).
Consequently
\[
 B^{-1}=G^{-1}B^*\in M_N(\operatorname{Div}_{\mathcal M}A).
 \tag{34}
\]

Finally set
\[
 g=\lambda B^{-1}\gamma
     =\lambda G^{-1}B^*\gamma
       \in\operatorname{Div}_{\mathcal M}A.
 \tag{35}
\]
For each finite cutoff the identity (16) gives
\[
 \lambda\left(\sum_{n=0}^L V^n\right)\gamma
     =\sum_{\substack{w\in\mathcal W\\|w|\leq L}}\beta_w x_w.
 \tag{36}
\]
The left side converges to \(g\) in norm; the right side applied to \(\Omega\) converges to \(f\Omega\) by (13).
Thus \(g\Omega=f\Omega\), and the faithful trace gives \(g=f\).
This proves the nontrivial inclusion in (2).
The opposite inclusion holds because each bounded scalar inverse is also its affiliated inverse.

The same proof shows that, for the fixed auxiliary family (9), bounded elements of \(\operatorname{Div}_{\mathcal M}A\) are exactly those \(f\in\mathcal M\) having \([R_t,f]\in\mathcal F(H)\) for all letters.
The forward implication follows from (10) and the bounded product/inverse commutator identities; the reverse implication is Sections 5–7.
This is not a normalized dual-system statement for atomic generators.

## 8. Applications in the original coordinates and remaining boundary

For a finite-spectrum normal \(X_i\), write its distinct spectral values as \(\lambda_{i,1},\ldots,\lambda_{i,k_i}\).
Its spectral projection at \(\lambda_{i,a}\) is exactly
\[
 p_{i,a}
   =\prod_{b\ne a}
          \frac{X_i-\lambda_{i,b}1}{\lambda_{i,a}-\lambda_{i,b}}.
 \tag{37}
\]
It follows that \(\mathbb C[X_i]=W^*(X_i)\) is the full finite-dimensional abelian star algebra.
In particular \(X_i^*=\sum_a\overline{\lambda_{i,a}}p_{i,a}\) is already a polynomial in \(X_i\).
If these variables are freely independent, (2) therefore reads
\[
 \operatorname{Div}_{L^0(\mathcal M)}
       \mathbb C\langle X_1,\ldots,X_s\rangle\cap\mathcal M
  =\operatorname{Div}_{\mathcal M}
       \mathbb C\langle X_1,\ldots,X_s\rangle.
 \tag{38}
\]
No adjoints have been added to their original polynomial algebra.
All atom weights are arbitrary positive real numbers; scalar coordinates are harmless.

More generally, each finite-dimensional factor can be
\[
 \mathcal B_i=\bigoplus_r M_{n_{ir}}(\mathbb C),\qquad
 \tau_i=\sum_r t_{ir}\operatorname{tr}_{n_{ir}},
 \quad t_{ir}>0,\quad\sum_r t_{ir}=1.
 \tag{39}
\]
Here \(\operatorname{tr}_{n}\) is normalized matrix trace.
Any selfadjoint finite generating tuple for \(\mathcal B_i\) generates it already as a polynomial star algebra, because every linear subspace of a finite-dimensional algebra is closed.
Hence the reconstructed scalar expressions can be written in such original generators.
They need not be freely independent within a factor; the factors are the freely independent objects.

In Yin_T_F0007's notation, this establishes the permanence equality when each input coordinate algebra is its full finite-dimensional star factor.
The input equalities are then automatic, since \(L^0(\mathcal B_i)=\mathcal B_i\).
For a proper non-star coordinate subalgebra, the proof has not shown descent of the scalar expressions from the whole factor algebra.

Diffuse factors remain outside this argument.
Their centered \(L^2\) spaces are infinite dimensional; a finite orthonormal alphabet spanning them is unavailable, and finite generators do not by themselves give the required finite residual space in a reduced-word basis.
Neither norm approximation nor a rational expression in a larger auxiliary algebra replaces reconstruction in the specified original algebra.

## 9. Review and continuation

Self-review checked the real Gram–Schmidt construction, the generally complex coefficients in (4), the exact adjoint-free pairing leading to (15), and the distinction between terminal letter and terminal factor.
It also checked that the forbidden state products are all same-factor pairs, that the diagonal blocks are orthogonal only across factors, and that the finite scalar-pivot reconstruction uses the actual original star algebra.

No frozen proof or shared index was modified by this subtask.
No new computation evidence, proof-assistant validation, external human review or novelty conclusion is asserted.
Adoption requires independent mathematical review of the finite-dimensional extension and the invocation of the already reviewed reconstruction.
The general diffuse and non-star-input portions of Yin_T_F0007 remain open.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:33 |
| status | proved |
| reason | Adopt the exact original finding at its disclosed unknown initial-context relationship. Preserve the mathematical statement, status, selected argument, dependencies and all historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#4-bounded-end-deletion-and-the-finite-rank-boundary-defect) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0116_v1.md#8-coordinated-wording-correction-and-verification-record) | Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#4-bounded-end-deletion-and-the-finite-rank-boundary-defect) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0116_v1.md#current-isolated-finding) | Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#4-bounded-end-deletion-and-the-finite-rank-boundary-defect) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0116_v1.md#8-coordinated-wording-correction-and-verification-record) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0116_v1.md#8-coordinated-wording-correction-and-verification-record).

Material covered by that review: [Exact material](Yin_C_F0106_v1.md).

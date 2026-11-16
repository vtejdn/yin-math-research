---
author: Yin
---

# A single deficient pair with exactly independent marginal traces near free semicirculars

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

The [general normal implication](../tasks/Yin_T_F0011_v1.md#contract) \(\mathsf A\Rightarrow\mathsf S\) holds if and only if every exchange-symmetric actual normal pair \(W_0,W_1\) with
\[
              \tau(f(W_0)g(W_1))=\tau(f(W_0))\tau(g(W_1))                \tag{1}
\]
for all bounded Borel \(f,g\) has finite original right slice cost at the first coordinate.
No uniform bound across pairs is required in this test.

In fact, if the general implication fails, then for each \(\varepsilon>0\) one such pair has infinite original right slice costs at both coordinates and no bare full-domain dual system.
In a common finite tracial algebra there are freely independent standard semicirculars \(T_0,T_1\) such that the actual conjugate variables \(\xi_0,\xi_1\) of the pair satisfy
\[
          \max_{j=0,1}\big(\|W_j-T_j\|+\|\xi_j-T_j\|_2\big)<\varepsilon. \tag{2}
\]
Thus (1), (2) and exchange symmetry can be imposed together on the same hypothetical counterexample.
Equation (1) specifies only products of one function from each marginal.
The existence of a counterexample remains open.

## Argument

### Conditional expectations of the four matrix corners

Use the [eight-slot matrix symmetry](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces).
Here are the parts of that construction needed with a varying primary slot.
Start with a tracial base \(R'\) containing a centered symmetry \(J\), write \(B=W^*(J)\), \(A=M_4(R')\), and let \(N=A*W^*(D)\) with \(D\) a centered free symmetry.
Inside \(M_2(N)\) write \(e_1,\ldots,e_8\) for the diagonal matrix units of \(M_8(R')\) in their natural order.
The unitary \(U\in M_4(B)\) is one half times the matrix with rows
\((1,1,1,1),(1,J,-1,-J),(1,-1,1,-1),(1,-J,-1,J)\).
Put
\[
        s_*=\frac1{\sqrt2}\begin{pmatrix}D&U\\ U^*&-U^*DU\end{pmatrix},
        \qquad B_*=W^*(s_*).
\]
It is a centered symmetry.
There is a trace-preserving grading fixing \(A\), sending \(D\) to \(-D\), and conjugating the outer two-by-two matrix by \(\operatorname{diag}(1,-1)\).
It fixes the diagonal slots and negates \(s_*\).

Let \(v\) be the free selfadjoint noise of [the semicircular neighborhood construction](Yin_C_F0317_v1.md#a-freely-perturbed-projection-close-in-norm-to-a-free-symmetry), of uniform law on \([-2,-1]\cup[1,2]\), now free from \(M_2(N)\).
Write \(s_f=\operatorname{sgn}v,\ s=\operatorname{sgn}(v+\lambda s_*)\) for \(0<\lambda<1/2\).
The cited strict trace argument gives \(\mathbb E_{B_*}s=b s_*\) with \(b>0\) depending only on \(\lambda\) and the fixed free laws.
Also \(\|s-s_f\|\to0\) as \(\lambda\downarrow0\).
Put
\[
                  H=64\,\operatorname{Re}(e_1s e_5s e_2s e_6s e_1).
\]
The conditional expectation onto \(M_8(R')\) satisfies
\[
                        \mathbb E_{M_8(R')} H=e_1(a+b^4 J)              \tag{3}
\]
for a real scalar \(a\), identifying \(J\) in the first slot.

For clarity, if \(C\) is a von Neumann subalgebra of a tracial base \(\mathcal R\) and a noise algebra \(V\) is freely adjoined, then \(\mathcal R\) and \(C\vee V\) are free over \(C\) in their generated algebra for the trace-preserving expectation.
Indeed centered-over-\(C\) words of \(C\vee V\) are weakly spanned by scalar reduced words with at least one centered \(V\)-letter and optional initial and terminal \(C\)-letters.
Inserting \(x\in\mathcal R\) with \(\mathbb E_Cx=0\) between such words leaves the intervening \(\mathcal R\)-factor centered even after multiplication by the two optional \(C\)-letters.
This gives zero expectation onto \(\mathcal R\) for an alternating word with such interior \(\mathcal R\)-factors and at least one centered-over-\(C\) noise word, also with arbitrary outer \(\mathcal R\)-factors.
Weak density and separate normality extend the identity.

Apply this with \(\mathcal R=M_2(N), C=B_*, V=W^*(v)\).
In the conditional expectation onto \(\mathcal R\) of \(s e_5s e_2s e_6s\), the term using \(\mathbb E_{B_*}s\) four times is \(b^4s_*e_5s_*e_2s_*e_6s_*\).
Every other surviving term lies in the span of words of \(B_*\)-factors interspersed with an ordered subsequence of at most two of the three tags.
To see this, split each noise-side factor into its \(B_*\) mean and its centered part.
A single centered factor gives zero.
With two or more centered factors, center each intervening base run over \(B_*\); if all are centered the expectation vanishes by the preceding paragraph.
Taking the \(B_*\) mean of any such run removes at least one tag and merges the adjacent noise factors into one.
Induction on the number of tags gives the stated span, leaving outer base runs intact.

In the \(e_1\) compression two surviving distinct tags require \(s_*\) at both ends and between the tags, by orthogonality of the four distinct slot projections.
The resulting word is odd under the grading, hence its expectation onto \(M_8(R')\) vanishes in the first diagonal slot where the grading acts trivially.
One surviving tag \(e_j\) gives only \(e_1s_*e_js_*e_1\).
For a lower slot its first entry is \(1/8\) by unitarity of the corresponding entry of \(2U\); for the upper slot \(e_2\), expectation of \(D e_2 D\) onto \(A\) is \(\tau_A(e_2)1\), again giving \(1/8\).
The zero-tag compression has scalar expectation since \(B_*=\operatorname{span}\{1,s_*\}\) and \(e_1s_*e_1\) has mean zero onto \(A\).
The full four-step path uses \(U_{11}, U_{21}^*, U_{22}, U_{12}^*\) with the four factors \(1/\sqrt2\) from the symmetry, so it gives \(J/64\) in the first slot.
Taking real parts proves (3).

### Uniform recovery on small primary pieces

Let \(p\in R'\) be a projection with \(\mathbb E_Bp=t1\), and set \(P=I_8p\).
We claim that
\[
              \|e_1P(H-e_1(a+b^4 J))Pe_1\|\le512\sqrt t .                \tag{4}
\]
The [free-product compression proof](Yin_C_F0313_v1.md#compression-of-a-free-perturbation) works for every \(C\subset\mathcal R\) in the preceding paragraph and every projection \(P\in\mathcal R\) with \(\mathbb E_CP=t1\).
In the free-product Hilbert space its projection onto the words beginning with an optional \(L^2(C)\)-letter followed by a centered noise letter satisfies \(QPQ=tQ\).
For \(x\in C\vee V\) centered over \(C\), \((1-Q)x(1-Q)=0\) by the same reduced-word calculation, with \(C\) preserving \(L^2(\mathcal R)\ominus L^2(C)\) under multiplication.
It follows that \(\|PxP\|\le2\sqrt t\|x\|\).

First put \(C_1=M_4(B)\vee W^*(D)\subset N\) and \(C_2=M_2(C_1)\).
The conditional expectation of \(I_4p\) onto \(C_1\) equals \(t1\): testing against the \(M_4(B)\)-words uses entrywise conditional expectation, and all reduced words with a centered \(D\)-letter are orthogonal to \(A\).
Hence \(\mathbb E_{C_2}P=t1\).
As \(H\in C_2\vee W^*(v)\), its conditional expectation onto \(M_2(N)\) equals its expectation onto \(C_2\), by reduced words.
The first compression error is at most \(2\sqrt t\cdot 128\), since \(\|H\|\le64\).
This conditional expectation is supported in \(e_1\).
Its upper-left outer matrix entry belongs to \(C_1\) and has norm at most 64.
Apply the same estimate to that entry using \(M_4(B)\subset A\) and the free factor generated by \(D\); now the projection \(I_4p\) again has conditional mean \(t1\).
The additional compressed error is at most \(256\sqrt t\).
The expectation left after these two operations is the one in (3), proving (4).

### Placing bad tests in the top semicircular interval

Assume the general implication fails.
Use the [finite projection witnesses](Yin_C_F0308_v1.md#statement), choosing \(\|Z_n\|\le1\), centered symmetries \(J_n=2P_n-1\) in \(R_n=W^*(Z_n,J_n)\), distinguished actual vacua \(\zeta_n\), and fixed mixed polynomial contractions with right slice norm \(>4^n\|\zeta_n\|_2\).
Choose the tolerance \(h_n>0\) of each witness so that perturbing its symmetry by at most \(h_n\) in a larger corner keeps its norm at most two and its formal slice norm above \(4^n\|\zeta_n\|_2/2\). [Finite witness continuity](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses)

Split standard semicircular probability into its eight consecutive quantile intervals of mass \(1/8\), numbered from left to right by \(j=0,\dots,7\).
Translate interval \(j\) by \(j\delta\) for \(0<\delta<1/16\), and use on it the translated conditional probability of its original interval.
Each conditional law has bounded real density and therefore an actual scalar vacuum by the [scalar criterion](Yin_C_F0255_v1.md#statement).
Slot one uses the top interval and the seven other slots use the seven lower intervals in any fixed order.
In the primary tracial base \(R=\prod_{n\ge0}R_n\) the main summand of weight \(1-t\) carries the translated conditional top-interval variable and an independent free centered symmetry, with the first actual vacuum extended freely across the symmetry.
Here and below \(t=\sum_{n\ge1}t_n\).
On every bad summand \(n\ge1\) of weight \(t_n\), put
\[
 W^{(n)}=2+7\delta+d\,2^{-n}+\alpha_n Z_n,\qquad
 u_n=t_n/8,\qquad \alpha_n=L2^n u_n^{3/2}\|\zeta_n\|_2
\]
with \(0<d<1/4\) and \(L>1\).
The primary coefficient \(J\) is the direct sum of its centered symmetries, so \(\mathbb E_B1_n=t_n1\) for the summand units.
Obtain \(R'\) by adjoining the seven padding variables freely to \(R\) and each other.
Let \(W\) be the eight-slot diagonal normal operator with the variables just specified.
For fixed \(\delta,d,L,\lambda\), select all \(t_n\) small enough for \(\alpha_n<d2^{-n}/16\), \(512\sqrt{t_n}/b^4<h_n\), and \(\sum 4^nt_n\) as small as needed.
All these restrictions are upper bounds on the masses.
The primary bad pieces and each whole slot are individually isolated by cuts in \(\operatorname{Re}W\).
The good part of the primary slot may contain an accumulation point of bad pieces.

We describe the derivation on the ambient matrix algebra before restriction.
On the primary product base use only the diagonal-coarse derivatives from [the direct-sum construction](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing), namely \(D_n/\alpha_n\) on the bad pieces and the normalized scalar derivative extended by zero on the free symmetry on the main piece.
These diagonal derivatives kill \(J\), respect represented relations, have summable generator tensors and admit a vacuum, by the trace weights in the cited construction.
The vacuum on the main piece is the scalar vacuum for that translated conditional law with the block weight.
Take also the seven free scalar derivatives at the padding variables.
The [two matrix lifts and free extension](Yin_C_F0321_v1.md#making-the-sign-a-relative-coefficient) give their sum \(L_0\) on the matrix core, killing all matrix units, \(D\), \(J\) in the entries and \(s_*\).
Only the scalar vacuum of each padding variable is used in extending its derivative.
The value \(L_0W\) is \(\sum_i E_i\otimes E_i\), where \(E_i\) ranges over the seven padding units, the good primary piece and each separate bad primary piece.
At \(W^*\) the corresponding diagonal values are its marginal phases on those squares.
The vacuum on piece \(i\) is its global trace weight times its normalized local vacuum, including the scale \(1/\alpha_n\) on a bad piece.

Add the inner derivation of the mixed spectral kernel \(K=(z-w)^{-1}\) on distinct \(E_i,E_j\), zero on their diagonal squares.
The part \(K_{gg}\) between distinct good intervals has norm bounded by \(1/\delta\) in the coarse space.
Between a bad piece \(n\) and any good piece, the inverse gap is at most \(C2^n/d\); the same bound with \(\min(n,k)\) applies between distinct bad pieces.
Hence \(\|K-K_{gg}\|_2^2\le C'd^{-2}\sum 4^nt_n\).
The corrected \(L\) has the full unit value and normal phase, with \(\|Ls_*\|_2\le2\|K\|_2\).
The fixed-kernel inner vacuum has norm at most \(2\|K\|_2\).
Extend \(L\) freely by zero on \(v\), and insert \(-\lambda Ls_*\) at \(v\).
As in [the gapped-noise construction](Yin_C_F0317_v1.md#a-semicircular-main-summand-and-summable-distinguished-vacua), this changes the vacuum by at most \(2\lambda\|g_v\|_2\|K\|_2\), where \(g_v\) is the actual scalar noise vacuum.
It kills \(v+\lambda s_*\), hence also its sign on the norm and derivation graph extension.

### The good vacuum and its approximation to the coordinate

Let \(\nu\) be the normalized real marginal law on all good pieces, of total mass \(c=1-t/8\).
The vector made up of the good diagonal vacua and the inner vacuum of \(K_{gg}\) is exactly the function \(c\xi_\nu\) of the coordinate on the good pieces, zero elsewhere.
Indeed the good diagonal vacua are scalar marginal functions and the vacuum of the inner kernel is given by the difference of its two marginal trace contractions with the appropriate adjoints, so is also in the marginal Hilbert space and supported there.
On a scalar polynomial the good diagonal and good–good cross differences together give the divided difference on the full good square.
The ambient vacuum pairing is thus \(c^2\) times the normalized scalar double trace, identifying the vector by polynomial density on the good spectrum.
This calculation uses no graph assertion about the projection onto the union of good pieces.

Write \(w_g(x)\,dx=c\,d\nu(x)\) on the real line and \(A_g\) for \(W\) restricted to these pieces.
The [real-line case of the directional formula](Yin_C_F0318_v1.md#statement) and \(\langle\xi_\nu,x\rangle_\nu=1\) give the global trace Hilbert square
\[
       \|c\xi_\nu-A_g\|_{2,g}^2
       =\frac{4\pi^2}{3}\int w_g^3\,dx-2c^2+\int x^2 w_g(x)\,dx.         \tag{5}
\]
On the translated octiles \(w_g\) is the translate of the standard semicircular density, multiplied on the top octile only by \(1-t\).
As \(t\to0\) the cubic integral tends to the unshifted semicircular cubic integral, since the translated intervals are disjoint.
As \(\delta,t\to0\), the second moment tends to one.
The semicircular vacuum is the coordinate itself. [Semicircular moments](../audits/literature/NS06/Yin_U004.md#ns06-u004)
Consequently (5) can be made arbitrarily small by choosing \(\delta\) small and then \(t\) small.

The rest of the diagonal vacuum has norm at most \(L^{-1}\) by \(\sum u_n^3\|\zeta_n\|_2^2/\alpha_n^2=\sum4^{-n}/L^2\).
The bad coordinate has trace Hilbert norm \(\|W1_{\rm bad}\|_2\le3\sqrt{t/8}\) for \(\delta,d\) as above.
After sign restriction to the generated algebra, the intrinsic vacuum \(\xi\) differs from \(W\) by at most
\[
 \|c\xi_\nu-A_g\|_{2,g}+L^{-1}+3\sqrt{t/8}
       +2\|K-K_{gg}\|_2+2\lambda\|g_v\|_2\|K\|_2.                        \tag{6}
\]
Projection of the ambient vacuum is contractive and fixes \(W\).
Restriction is valid because the values on \(W,W^*,s\) belong to the target coarse space, and its sign involution fixes \(W\).

### The bad mixed tests, trace independence and the reference pair

For each \(n\) let \(E_n=e_1 I_8 1_n\) now denote its bad primary slot projection.
It has global mass \(u_n\).
The spectral cuts \(E_n,e_1,e_2,e_5,e_6\) are bounded norm and graph limits using \(C^1\) approximants of functions of \(\operatorname{Re}W\) constant on the respective pieces.
In the derivation with \(E_n\) inserted at both inner legs their gradients vanish, as do those of \(s,H\).
Thus \(\alpha_n I_{E_n\otimes E_n}\delta\) has the normalized values at \(Z_n,Z_n^*\) and zero at \(b^{-4}E_n(H-a e_1)E_n\) in the normalized corner.
The latter coefficient approximates \(J_n\) within \(h_n\) by (4).
The [corner slice comparison](Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) now gives \(4a_0\ge u_n^{3/2}4^n\|\zeta_n\|_2/(2\alpha_n)=2^{n-1}/L\) if \(a_0\) is the finite distinguished cost on the original polynomial unit ball.
This is impossible.
The [even-algebra formula](Yin_C_F0311_v1.md#statement) gives the pair \(W_0=W,W_1=sWs\), with vacua \(\xi,s\xi s\), exchange symmetry and infinite costs at both coordinates, excluding bare duals by the [normal dual implication](Yin_C_F0070_v1.md#statement).

Before smoothing the sign, (1) holds for \(W,s_*Ws_*\) by the four matrix-block trace computation in the [eight-slot construction](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces).
In a cross-color trace, the lower padding entry is freely independent of the entire primary entry, the old \(J\), and every other padding entry.
In a same-color trace the free centered \(D\) separates the two matrix factors.
The same argument gives \(\tau(f(W)s_*)=0\).
The [conditional expectation of the smoothed symmetry](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) therefore gives
\(\mathbb E_{M_2(N)}(s f(W)s)=b^2s_*f(W)s_*+(1-b^2)\tau(f(W))1\).
Both terms yield the same product trace against any \(g(W)\), giving exact equality in (1) for the final pair.

Take \(T_0\) equal to the unshifted coordinate on the seven lower octiles.
In the primary slot redistribute the conditional top semicircular law using its continuous quantile on \([0,1]\): use the lower probability portion \(1-t\) of that conditional law on the good primary piece and the upper probability portion \(t\) on all bad pieces, using a uniform variable in each diffuse bad marginal.
On the good primary piece the quantile argument is \((1-t)\) times the continuous cumulative distribution of its variable.
This is the [quantile coupling](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) for the top conditional law.
Then \(T_0\) in \(M_2(N)\) is standard semicircular and
\[
                 \|W-T_0\|\le 7\delta+d+\omega(t)
\]
for the modulus of continuity \(\omega\) of the top conditional quantile.
The other reference coordinate \(T_1=s_f T_0 s_f\) is a free standard semicircular because \(s_f\) is centered and free from \(M_2(N)\).
As in that coupling, \(\|W_1-T_1\|\le\|W-T_0\|+4\|s-s_f\|\) and \(\|\xi_j-T_j\|_2\le\|\xi-W\|_2+\|W_j-T_j\|\).

Choose \(\delta,d,L^{-1}\) small first.
An a priori restriction \(\sum4^nt_n\le d^2\) bounds \(\|K\|_2\) in terms of \(\delta\) and absolute constants before the masses are fixed.
Choose \(\lambda>0\) sufficiently small in (6) and in \(\|s-s_f\|\), fixing \(b>0\).
Finally choose all masses to satisfy the finite tolerances and to make \(t,\|K-K_{gg}\|_2\) as small as required.
These choices give (2); the converse in the statement follows because each such deficient actual pair is itself a counterexample.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:36 |
| status | open |
| reason | Fix the simultaneous single-law independence and semicircular neighborhood construction for complete review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Qualitative equivalence with exactly independent marginal traces, simultaneous strong coupling and both infinite costs on one exchange pair. |
| argument | [Argument](#argument) | Four-step coefficient after smoothing, double small-corner compression, global weighted vacuum, eight octiles, bad tests and quantile coupling. |
| dependency | [Flat matrix construction](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces) | The eight slots, odd symmetry, trace factorization and first-slot matrix entries. |
| dependency | [Lifted derivations](Yin_C_F0321_v1.md#making-the-sign-a-relative-coefficient) | Two matrix lifts through the free symmetry and trace normalization at the eight slots. |
| dependency | [Gapped sign](Yin_C_F0317_v1.md#a-freely-perturbed-projection-close-in-norm-to-a-free-symmetry) | Positive sign coefficient for arbitrarily small coupling and proximity to the independent symmetry. |
| dependency | [Free-product compression](Yin_C_F0313_v1.md#compression-of-a-free-perturbation) | Two reduced-word projections used with arbitrary base subalgebras at two nested free stages. |
| dependency | [Finite projection witnesses](Yin_C_F0308_v1.md#statement) | Unbounded normalized tests using one trace-half coefficient if the universal implication fails. |
| dependency | [Finite test continuity](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Perturbed coefficients in a larger normalized corner. |
| dependency | [Scalar actuality](Yin_C_F0255_v1.md#statement) | Bounded real densities on the translated conditional octiles. |
| dependency | [Diagonal-coarse derivatives](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Diagonal sum without differentiating the symmetry and subsequent inverse-gap correction. |
| dependency | [Free noise correction](Yin_C_F0317_v1.md#a-semicircular-main-summand-and-summable-distinguished-vacua) | Actual ambient adjustment at gapped free noise, graph restriction and projected vacuum. |
| dependency | [Directional Cauchy formula](Yin_C_F0318_v1.md#statement) | Exact cubic density normalization for the good real-line law. |
| dependency | [Semicircular law](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Standard probability, variance and scalar vacuum for the reference cubic integral. |
| dependency | [Cost of corner tests](Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) | Graph cuts, both inner legs and the twice-cost estimate on a bad slot. |
| dependency | [Even algebra](Yin_C_F0311_v1.md#statement) | Exchange-symmetric actual coordinates and transfer of infinite cost. |
| dependency | [Bare obstruction](Yin_C_F0070_v1.md#statement) | No bare dual system on the resulting actual normal pair. |
| dependency | [Quantile coupling and sign regression](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Projection of smoothed conjugations to the base and a standard semicircular reference in the ambient algebra. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:43 |
| status | proved |
| reason | Adopt the simultaneous single-pair construction with exact two-marginal trace independence and semicircular approximation after review of all fifteen direct interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Qualitative equivalence with exactly independent marginal traces, simultaneous strong coupling and both infinite costs on one exchange pair. |
| argument | [Argument](#argument) | Four-step coefficient after smoothing, double small-corner compression, global weighted vacuum, eight octiles, bad tests and quantile coupling. |
| dependency | [Flat matrix construction](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces) | The eight slots, odd symmetry, trace factorization and first-slot matrix entries. |
| dependency | [Lifted derivations](Yin_C_F0321_v1.md#making-the-sign-a-relative-coefficient) | Two matrix lifts through the free symmetry and trace normalization at the eight slots. |
| dependency | [Gapped sign](Yin_C_F0317_v1.md#a-freely-perturbed-projection-close-in-norm-to-a-free-symmetry) | Positive sign coefficient for arbitrarily small coupling and proximity to the independent symmetry. |
| dependency | [Free-product compression](Yin_C_F0313_v1.md#compression-of-a-free-perturbation) | Two reduced-word projections used with arbitrary base subalgebras at two nested free stages. |
| dependency | [Finite projection witnesses](Yin_C_F0308_v1.md#statement) | Unbounded normalized tests using one trace-half coefficient if the universal implication fails. |
| dependency | [Finite test continuity](Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Perturbed coefficients in a larger normalized corner. |
| dependency | [Scalar actuality](Yin_C_F0255_v1.md#statement) | Bounded real densities on the translated conditional octiles. |
| dependency | [Diagonal-coarse derivatives](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Diagonal sum without differentiating the symmetry and subsequent inverse-gap correction. |
| dependency | [Free noise correction](Yin_C_F0317_v1.md#a-semicircular-main-summand-and-summable-distinguished-vacua) | Actual ambient adjustment at gapped free noise, graph restriction and projected vacuum. |
| dependency | [Directional Cauchy formula](Yin_C_F0318_v1.md#statement) | Exact cubic density normalization for the good real-line law. |
| dependency | [Semicircular law](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Standard probability, variance and scalar vacuum for the reference cubic integral. |
| dependency | [Cost of corner tests](Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) | Graph cuts, both inner legs and the twice-cost estimate on a bad slot. |
| dependency | [Even algebra](Yin_C_F0311_v1.md#statement) | Exchange-symmetric actual coordinates and transfer of infinite cost. |
| dependency | [Bare obstruction](Yin_C_F0070_v1.md#statement) | No bare dual system on the resulting actual normal pair. |
| dependency | [Quantile coupling and sign regression](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Projection of smoothed conjugations to the base and a standard semicircular reference in the ambient algebra. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0330_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

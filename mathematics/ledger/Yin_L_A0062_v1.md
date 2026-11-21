---
author: Yin
---
# Residual representatives with a controlled extreme coefficient

This 21 November 2026 development examines the spectral test in [C_A0039_v3](../claims/Yin_C_A0039_v3.md#a-rational-eigenvalue-in-the-subgroup-of-the-residual-element), for [A0001](../tasks/Yin_T_A0001_v1.md#contract) and its connection to [A0002](../tasks/Yin_T_A0002_v1.md#contract).
The work below is development and comparison, not an independent review or a change to a selected Claim.
No actual Mghirbi--Douglas graph outcome and its complete collected product table have been supplied for these tests.
The contribution is an explicit residual-representative test, its integer feasibility calculation, and limitations that follow from the source's actual occurrence coefficients.

## The fixed residual class and its spectral meaning

Let \(a,b\in\mathbb F_p[G]\) satisfy \(ab=1\ne ba\), and let \(A,B\in\mathbb Z[G]\) be fixed lifts.
For \(W\in\mathbb Z[G]\), set
\[
 D=\frac{1-AB}{p},\qquad
 B_W=B+pW,\qquad D_W=D-AW,\qquad
 f_W=AB_W=1-pD_W.
 \tag{1}
\]
Every expression here is an actual finite group-ring element.
The [fixed-input argument in C39](../claims/Yin_C_A0039_v3.md#a-rational-eigenvalue-in-the-subgroup-of-the-residual-element) gives
\[
 \nu_G(f_W)\ge\nu_G(A),\qquad
 \nu_G(f_W)=\nu_{\langle\operatorname{supp}D_W\rangle}(1-pD_W).
 \tag{2}
\]
Thus absence of the eigenvalue \(1/p\) for even one residual representative excludes the analytic kernel of the fixed \(A\).
It also excludes every finitely supported complex right annihilator of \(A\).
The arguments use regular representations, so their kernel statements are stronger than exclusion of finite vectors.

The converse should not be inferred for \(A\) alone.
The product \(f_W\) can have a kernel because \(B_W\) does.
If \(f_W\) has a nonzero analytic kernel, its scalar nullity is strictly between zero and one, so it violates the scalar analytic integrality assertion.
Nevertheless \(f_W\equiv1\bmod p\) excludes every nonzero finite complex left or right annihilator, by rational row reduction and a primitive integral solution.
This would supply an analytic obstruction, not a finite zero product for this particular \(f_W\).
These distinctions are already part of the cited C39 result.

There is a uniform obstruction to a small-residual Neumann argument.
Every \(D_W\) is nonzero: \(D_W=0\) would give \(AB_W=1\), and direct finiteness over \(\mathbb C[G]\) would give \(B_WA=1\), contradicting \(ba\ne1\) on reduction.
Since its coefficients are integers,
\[
 \|D_W\|\ge\|D_W\|_2\ge1.
 \tag{3}
\]
In particular \(\|D_W\|<1/p\) is impossible throughout the permitted integral residual class.
This does not exclude other resolvent or extreme-coefficient tests.

## What the actual occurrence lifts supply

For odd \(p\), [Mghirbi--Douglas, Proposition 7.11, printed/PDF p.30](../literature/pdf/MD26.pdf#page=30), defines its two factors using the same rooted component \(\mathcal A'\):
\[
 a=\sum_{x\in\mathcal A'}\sigma(x)g_x,\qquad
 b=-\sum_{x\in\mathcal A'}g_x^{-1}
 \quad\text{in }\mathbb F_p[G].
 \tag{4}
\]
The signs are the two vertex colors.
The theorem's root protection supplies a nonzero right annihilator \(c\), and hence \(ba\ne1\).
The geometric existence and torsion-freeness inputs are used at their [retained source scope](../audits/literature/MD26/Yin_U001.md#md26-u001).

For these particular integer occurrence lifts, put
\[
 P_+=\sum_{\sigma(x)=1}g_x,\qquad
 P_-=\sum_{\sigma(x)=-1}g_x,\qquad S=P_++P_-.
\]
Then
\[
 A=P_+-P_-,\qquad B=-S^*,\qquad
 pD=I+AS^*
 =I+P_+P_+^*-P_-P_-^*+P_+P_-^*-P_-P_+^*.
 \tag{5}
\]
Consequently
\[
 p\,\operatorname{Re}D=I+P_+P_+^*-P_-P_-^*,\qquad
 p\,\operatorname{Im}D=\frac{P_+P_-^*-P_-P_+^*}{i}.
 \tag{6}
\]
These identities do not assert positivity, selfadjointness or normality of \(D\).
The real part is a difference of two positive terms and the imaginary part need not vanish.

Repeated group labels must be collected.
If \(n_g^\pm\) are their two occurrence multiplicities and \(N_\pm=\sum_gn_g^\pm\), then
\[
 A_g=n_g^+-n_g^-,\qquad S_g=n_g^++n_g^-,
\]
\[
 D_h=\frac{\mathbf1_{\{h=1\}}+
       \sum_{uv^{-1}=h}(n_u^+-n_u^-)(n_v^++n_v^-)}p,
 \tag{7}
\]
\[
 D_1=\frac{1+\sum_g((n_g^+)^2-(n_g^-)^2)}p,\qquad
 \varepsilon(D)=\frac{1+(N_+-N_-)(N_++N_-)}p.
 \tag{8}
\]
The divisibility in these expressions follows from the actual equality \(ab=1\).
Its augmentation gives
\((N_+-N_-)(N_++N_-)\equiv-1\bmod p\).
The cardinalities here refer to the selected component, not automatically to all vertices in the construction.
Neither the two color classes nor the actual collected supports may be replaced by distinct generic group elements.
The source's type frequencies and turn estimates do not specify the coefficients in (7) without the actual label equalities.

## One injective extreme coefficient: a bounded-window proof

The scalar conclusion needed here is already covered by the
[ordered-quotient theorem quoted in C4v3](../claims/Yin_C_A0004_v3.md#ordered-quotient-source).
The adjacent [finite-layer argument](../claims/Yin_C_A0004_v3.md#height-layer-certificate) was written with a bounded inverse for an outer coefficient.
The following local-kernel argument explains why mere injectivity is sufficient, including for finite matrix coefficients.
It uses bounded internal constraints rather than a claimed bounded inverse or a global two-sided recurrence.

Let \(L=N\rtimes\langle u\rangle\), with \(\sigma=\operatorname{Ad}u\), and let
\[
 T=\sum_{j=0}^{d}T_j u^j\in M_r(\mathcal N(L)),
 \qquad T_j\in M_r(\mathcal N(N)),
 \tag{9}
\]
have finite bandwidth, with \(T_0\) injective on \(\ell^2(N)^r\).
All the coefficients are bounded.
Then \(T\) is injective.
For \(d=0\) this is the subgroup decomposition, so suppose \(d>0\).

Write a vector as \(\xi=\sum_{l\in\mathbb Z}\xi_lu^l\), with
\(\xi_l\in\ell^2(N)^r\).
The equation \(T\xi=0\) says
\[
 \sum_{j=0}^{d}T_j\sigma^j(\xi_{l-j})=0
 \quad(l\in\mathbb Z).
 \tag{10}
\]
For an interval of \(m>d\) slices indexed by \(0,\ldots,m-1\), let \(K_m\) be the kernel of the bounded internal constraint map consisting of (10) only for
\(l=d,\ldots,m-1\).
It is a closed right \(N\)-module.
The action on slice \(l\) is the \(\sigma^l\)-twisted regular right action, and every such slice has \(N\)-dimension \(r\).
The constraints respect these actions.

Restriction from \(K_m\) to its first \(d\) slices is bounded, \(N\)-equivariant and injective.
Indeed, if those slices vanish, the equation at \(l=d\) gives \(T_0\xi_d=0\), hence \(\xi_d=0\).
The remaining equations successively force every other slice in the interval to vanish.
The polar decomposition of this restriction gives
\[
 \dim_N K_m\le rd.
 \tag{11}
\]
Its range need not be closed, and no bounded inverse for \(T_0\) is used.

Let \(e=P_{\ker T}\) and let \(\chi_m\) be the interval cut.
Every restricted global kernel vector satisfies the internal constraints.
Their closure therefore lies in \(K_m\), since the constraint map is bounded.
The positive contraction \(\chi_m e\chi_m\) is supported on \(K_m\), so
\[
 m\,\operatorname{Tr}_{r,L}(e)
 =\operatorname{Tr}_{rm,N}(\chi_m e\chi_m)
 \le \dim_N K_m\le rd.
 \tag{12}
\]
The equality follows because right translation makes the diagonal trace on every height slice equal to the group trace of \(e\).
Letting \(m\) tend to infinity proves \(e=0\).
Only the finite interval is determined by its first \(d\) slices in this argument.
We do not claim that these slices determine an entire bi-infinite solution when the opposite outer coefficient is not injective.

## Residual tests with a controlled zero layer

Fix one integral \(W\) in (1), and set \(L=\langle\operatorname{supp}D_W\rangle\).
Suppose there is an epimorphism \(\phi:L\to\mathbb Z\) such that
\[
 \operatorname{supp}D_W\subseteq\{\phi\ge0\}.
 \tag{13}
\]
A nonzero homomorphism to \(\mathbb Z\) can be rescaled to an epimorphism onto its image.
Let \(N=\ker\phi\) and let \((D_W)_0\in\mathbb Z[N]\) be the height-zero coefficient.
If
\[
 1-p(D_W)_0\quad\hbox{is independently known to be injective on }\ell^2(N),
 \tag{14}
\]
then (9)--(12), applied to \(f_W=1-pD_W\), prove
\[
 \nu_L(f_W)=0,\qquad \nu_G(A)=0.
 \tag{15}
\]
The finite tracial rank inequality for \(AB_W\) supplies the second implication.
Equivalently, the closed range of \(AB_W\) lies in the closed range of \(A\), and polar decomposition equates initial and final support traces.
Injectivity of the product also gives injectivity of \(B_W\).
Both factors have dense range by finite tracial polar decomposition.
In particular the fixed \(A\) has no finite complex left or right annihilator.

There are two directly useful forms of (14).

1. If every residual support element has strictly positive height, then \((D_W)_0=0\) and the coefficient in (14) is the identity.
   No group-class hypothesis on \(N\) or \(L\) is needed.
2. If the support of \((D_W)_0\) lies in a sofic subgroup \(K\le N\), the integer operator \((D_W)_0\) has no eigenvalue \(1/p\), by the exact [Thom interface already used in C39](../claims/Yin_C_A0039_v3.md#a-rational-eigenvalue-in-the-subgroup-of-the-residual-element).
   Decomposition into right \(K\)-cosets gives (14) on \(N\).
   Only the zero layer requires this certificate; the positive layers may generate a group whose soficity is unknown or false.

More generally, any independently verified injective extreme coefficient may replace (14).
Reversing the height or translating the lowest nonzero height to zero gives the same test.
The [singleton-extreme and indicable-support tests](Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) already cover the case of a scalar group unit at that extreme.
No new general theorem for all indicable groups or all their matrices is asserted.

The weaker subgroup requirement has a concrete calibration.
Let \(K\) be any finitely generated group with generators \(g_1,\ldots,g_s\), take \(L=K*\langle u\rangle\), and put
\[
 D^\circ=u+\sum_{i=1}^s g_i u.
 \tag{16}
\]
Its support generates \(L\), and all its terms have height one under the retraction to \(\langle u\rangle\).
Thus \(1-pD^\circ\) is analytically injective regardless of the group \(K\).
Taking \(K\) to be a torsion-free nonsofic group supplied by MD gives a torsion-free nonsofic support subgroup in this example.
This is an actual finite group-ring operator showing that the height certificate does not require the whole support subgroup to be sofic.
It has not been realized as the residual of a specific MD pair with \(ab=1\ne ba\).

## Integer feasibility on a fixed support

For a finite search, it suffices to choose a verified homomorphism \(\phi:G\to\mathbb Z\) and a finite candidate support \(T\subseteq G\) for \(W\).
This ambient-character version is sufficient, although the preceding theorem permits a character defined only on the residual subgroup.
Write \(W=\sum_{t\in T}w_t t\), with unknown \(w_t\in\mathbb Z\), and set
\[
 U=\operatorname{supp}D\ \cup\ (\operatorname{supp}A)T,\qquad
 U_-=\{g\in U:\phi(g)\le0\}.
 \tag{17}
\]
Define the finite integer matrix and right-hand side by
\[
 M_{g,t}=A_{gt^{-1}}\quad(g\in U_-,\ t\in T),\qquad
 d_g=D_g.
 \tag{18}
\]
Then
\[
 Mw=d\quad\text{over }\mathbb Z
 \tag{19}
\]
is exactly the condition that \(D-AW\) has no nonpositive-height coefficient.
The set \(U\) includes every possible output, so there is no omitted coefficient condition.
Its entries must be computed using actual equality of the group labels, rather than a formal occurrence table in a free group.

If \(P M Q\) is a Smith form with nonzero diagonal entries \(s_1,\ldots,s_r\), existence of an integral solution is equivalent to
\[
 s_i\mid(Pd)_i\quad(1\le i\le r),\qquad
 (Pd)_i=0\quad(i>r).
 \tag{20}
\]
Here \(P,Q\) are unimodular integer matrices of the appropriate sizes.
A solution supplies an explicit \(W\), and the strict version of (13)--(15) excludes the analytic kernel of \(A\).
The test does not change the reduction \(b\), since \(B_W=B+pW\).
Failure of (20) excludes this chosen finite support \(T\), not all possible residual representatives.

One can instead clear only negative-height coefficients and retain a specified zero layer whose injectivity has a separate certificate.
The same finite linear calculation then gives the coefficient constraints; the analytic certificate for the retained layer is an additional input.
This version must not silently replace (14) by the mere nonvanishing of its integer group-ring element.

## What remains unresolved

The pure norm-smallness test fails for the structural reason (3).
The strict height test fails for a particular residual support whenever zero belongs to the convex hull of its images in the real abelianization; in particular an identity coefficient or a zero abelianization image prevents strict separation.
If the residual subgroup has no nonzero real character, there is no such height to use.
Changing \(W\) may change these facts, but solving a fixed finite system does not prove eventual success of that search.
At a surviving zero layer, unknown injectivity is a genuine remaining spectral problem.

The MD source fixes signed occurrence sums and proves the modular identities.
It does not, by those assertions alone, give residual normality, a positive moment representation, a small residual norm, an appropriate character, or the integer solution in (19).
Without an actual chosen graph, its path labels and the verified equalities among their products, no one of these spectral exclusion tests has been applied to a source witness.
The new use of the established height mechanism is to test the entire permitted residual class by finite coefficient equations while isolating the zero-layer hypothesis.
The bounded-window proof also makes explicit the analytic justification when only that one coefficient is injective.

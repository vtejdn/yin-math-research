---
author: Yin
---
# Commutation corrections: nonbacktracking determinants and residue obstructions

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation advances [S_A0006](../strategies/Yin_S_A0006.md) through the commutation model and uses [S_A0007](../strategies/Yin_S_A0007.md) to test the arithmetic carried by return words.
It completes the all-orders comparison begun in [L_A0015](Yin_L_A0015_v1.md#a-geometric-index-mechanism-beyond-algebraicity), retaining the limits of the resulting atom information.
The main agent and two development helpers derived the formulas and checked their direct interfaces.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0016_v1.md#whole-artifact-finding) covers formulas (1)--(21), their arguments, source applicability and the stated strategy limits, with no substantive gap found at that scope.
The results are exact calibrations and useful failed implications, not a new group case of [A0001](../tasks/Yin_T_A0001_v1.md#contract).

## Setting and inspected sources

Use the same four-letter alphabet \(\mathcal A=\{u,u^{-1},v,v^{-1}\}\) in
\[
G_T=F(u,v),\qquad
G_Z=\langle u,v\mid [u,v]=e\rangle\cong\mathbb Z^2,
\qquad
A_G=u+u^{-1}+v+v^{-1}.
\]
All traces \(\tau_G\) are canonical group traces.
Write \(\mu_G\) for the scalar probability law of \(A_G\) and
\[
g_G(z)=\tau_G((z-A_G)^{-1}),\qquad
\Phi_G(z)=\exp\int\log(z-x)\,d\mu_G(x),\quad z\in\mathbb C^+.
\tag{1}
\]
The logarithm in (1) is the principal logarithm, with argument in \((0,\pi)\).
Thus \(\Phi_G'/\Phi_G=g_G\) and \(\Phi_G(z)/z\to1\) at infinity.
Near \(t=0\), put
\[
D_G(t)=\exp\left(-\sum_{k\ge1}\tau_G(A_G^k)\frac{t^k}{k}\right),
\quad
\mathcal R(t)=D_Z(t)/D_T(t),
\quad
\mathcal C(z)=\Phi_Z(z)/\Phi_T(z).
\]
The normalized germs obey \(D_G(t)=t\Phi_G(1/t)\) and
\(\mathcal R(t)=\mathcal C(1/t)\), initially where the indicated branches overlap.

The source comparison used a bounded search for the square-lattice Green function, periodic Ihara determinant and elliptic boundary asymptotics.
The exact inspected interfaces are:

- [Gut10, arXiv:1004.1435v1](https://arxiv.org/html/1004.1435v1), Section 1, equations (4), (6), (8), (10): square-lattice normalization and return counts.
- [GIL07, arXiv:math/0605753v3](https://arxiv.org/html/math/0605753v3), Lemma 4.2, Theorem 6.5 and Lemma 7.1(ii): periodic nonbacktracking zeta and analytic determinant, with one fundamental vertex and degree four.
- [BBGSS23](https://arxiv.org/html/2309.00437v1), Theorem 2.1, equation (2.6): the tree vertex-edge product, with the opposite resolvent sign in that source.
- [DLMF 19.12.1](https://dlmf.nist.gov/19.12.E1): the logarithmic asymptotic of the complete elliptic integral.

These source statements and conventions were checked; their complete source proofs were not independently audited.
The selected formulas have direct derivations below.
In particular the determinant convention here is an analytic trace-log germ, not an unrestricted global identification with a positive Fuglede--Kadison determinant.

## Exact tree and lattice transforms

Choose
\[
m(z)=\frac{z-\sqrt{z^2-12}}6,\qquad
\sqrt{z^2-12}\sim z
\]
off the tree spectral interval \([-2\sqrt3,2\sqrt3]\).
Deleting the root of a forward branch gives
\(m=(z-3m)^{-1}\), while the original root has four branches.
Consequently
\[
g_T(z)=\frac1{z-4m}
=\frac{m}{1-m^2}
=\frac3{z+2\sqrt{z^2-12}},
\qquad
\Phi_T(z)=\frac1{m(1-m^2)}
=\frac1{g_T(z)(1-m^2)^2}.
\tag{2}
\]
For the determinant formula, differentiate the displayed expression using
\(z=m^{-1}+3m\) and fix its multiplicative constant by \(\Phi_T(z)\sim z\).
This is the one-vertex, two-geometric-edge version of the tree vertex-edge product.
The source uses \((A-z)^{-1}\) and \(\log(x-z)\); at one vertex both source quantities change sign relative to (1).

Fourier transformation on \(\mathbb Z^2\) gives
\(A_Z(\theta,\phi)=2\cos\theta+2\cos\phi\).
Its moments are
\[
\tau_Z(A_Z^{2n})=\binom{2n}{n}^{\!2},
\qquad
\tau_Z(A_Z^{2n+1})=0.
\tag{3}
\]
Indeed, a returning word of length \(2n\) uses each horizontal direction \(k\) times and each vertical direction \(n-k\) times, so its count is
\[
(2n)!\sum_{k=0}^n\frac1{k!^2(n-k)!^2}
=\binom{2n}{n}\sum_{k=0}^n\binom nk^2
=\binom{2n}{n}^2.
\]
Use the modulus convention
\[
K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta.
\]
Expanding this integral at \(k=0\) and matching (3) proves
\[
g_Z(z)=\frac2{\pi z}K(4/z),
\qquad
M_Z(t):=\tau_Z((1-tA_Z)^{-1})=\frac2\pi K(4t).
\tag{4}
\]
The first equality is initially obtained for \(|z|>4\) and then continued on the physical branch characterized by \(g_Z(z)\sim1/z\).
Gut10's nearby hypergeometric display uses an ambiguous argument; the explicit integral above and its moment expansion fix the modulus convention independently.

Set \(f(t)=\sqrt{1-12t^2}\), \(f(0)=1\).
Equation (2) similarly gives
\[
M_T(t)=\frac3{1+2f(t)},\qquad
D_T(t)=\frac{3(1+f(t))^2}{4(1+2f(t))}.
\]
The complete correction is therefore fixed by
\[
\frac{\mathcal C'(z)}{\mathcal C(z)}
=\frac2{\pi z}K(4/z)-\frac3{z+2\sqrt{z^2-12}},
\qquad
\frac{\mathcal R'(t)}{\mathcal R(t)}
=\frac{M_T(t)-M_Z(t)}t,
\quad \mathcal R(0)=1.
\tag{5}
\]
This gives more than finitely many moment corrections.

## What root deletion actually changes

Delete the origin of the square lattice and compress the resolvent
\((z-A_Z^{(0)})^{-1}\) to the four neighbors of that origin.
By square symmetry, write \(d(z)\) for a diagonal entry, \(a(z)\) for an entry between adjacent neighbors, and \(o(z)\) for an entry between opposite neighbors.
The exact Schur complement is
\[
g_Z(z)=\frac1{z-4d(z)-8a(z)-4o(z)}.
\tag{6}
\]
For the tree the branches disconnect, giving \(d=m\) and \(a=o=0\).

The first path counts in the deleted lattice give
\[
d=z^{-1}+3z^{-3}+O(z^{-5}),\qquad
a=z^{-3}+O(z^{-5}),\qquad
o=2z^{-5}+O(z^{-7}).
\]
A neighbor has three remaining adjacent vertices.
Two adjacent root-neighbors are joined by one two-step path around the missing root, and opposite neighbors by two four-step paths.
It follows that the self-energy in (6) is \(4z^{-1}+20z^{-3}+O(z^{-5})\), while the tree value is \(4m=4z^{-1}+12z^{-3}+O(z^{-5})\).

Let \(R=(z-A_Z)^{-1}\), put \(g_0=R_{00}\), \(g_1=R_{0,e_1}\), \(g_2=R_{0,2e_1}\), and \(g_{\rm diag}=R_{0,e_1+e_2}\).
The rank-one deletion formula gives
\[
d=g_0-g_1^2/g_0,\qquad
a=g_{\rm diag}-g_1^2/g_0,\qquad
o=g_2-g_1^2/g_0.
\tag{7}
\]
These are analytic squares, not absolute squares.
The resolvent equations imply
\(4g_1=zg_0-1\) and \(zg_1=g_0+g_2+2g_{\rm diag}\).
Substituting them into (6) yields only \(g_0=g_0\).
Thus (6) identifies the missing off-diagonal transport, while a repair expressed solely through the unknown full Green function supplies no new rank constraint.

## A finite nonbacktracking determinant correction

Index four-dimensional matrices by \(\mathcal A\).
Let \(U=\operatorname{diag}(u_a)\), let \(J_{a,b}=1_{\{b=a^{-1}\}}\), let \(e\) be the all-ones column and \(r=(u_a)\) the corresponding row.
Define
\[
B_G=(ee^T-J)U,\qquad
(B_G)_{a,b}=1_{\{b\ne a^{-1}\}}u_b,
\qquad
N_G(s)=\exp\left(-\sum_{k\ge1}
(\operatorname{Tr}_4\otimes\tau_G)(B_G^k)\frac{s^k}{k}\right).
\tag{8}
\]
The edge trace in (8) is unnormalized.
The norm of \(ee^T-J\) is three and \(U\) is unitary, so the series converges for \(|s|<1/3\).
Its coefficients count identity words with no backtracking, including at the cyclic last-to-first join.

The degree-four periodic Bass identity takes the exact form
\[
N_G(s)=(1-s^2)\exp\tau_G\log(1-sA_G+3s^2).
\tag{9}
\]
For a direct verification near zero, put \(R=JU\).
Then \(R=R^*\), \(R^2=I\), and
\((\operatorname{Tr}_4\otimes\tau_G)(R)=0\), so
\[
\det_{\operatorname{Tr}_4\otimes\tau_G}(I+sR)=(1-s^2)^2.
\]
Also \(B_G=er-R\) and
\[
1-sr(I+sR)^{-1}e
=1-\frac{s(A_G-4s)}{1-s^2}
=\frac{1-sA_G+3s^2}{1-s^2}.
\]
Multiplicativity near the identity and the rectangular Sylvester identity for the analytic trace-log determinant give (9).
These identities follow by differentiating trace logarithms using cyclicity and by
\(\operatorname{Tr}(XY)^k=\operatorname{Tr}(YX)^k\), with value one at zero.
No global multiplicativity assertion for arbitrary logarithm branches is needed.
The same identity on \(|s|<1/3\) is the inspected GIL07 regular-graph interface; here its quotient has one vertex and two geometric edges, so the exponent of \(1-s^2\) is one.

There is no nonempty cyclically nonbacktracking identity word in \(F_2\), hence \(N_T(s)=1\).
With
\[
t=\frac{s}{1+3s^2}
\]
equation (9) gives the germ identity
\[
\boxed{\mathcal R\!\left(\frac{s}{1+3s^2}\right)=N_Z(s).}
\tag{10}
\]
On larger regions it is read by analytic continuation, not by substituting outside the convergence domain of a power series.
Taking \(s=m(z)\) yields the corrected vertex-edge formula and its resolvent derivative:
\[
\boxed{
\Phi_Z(z)=\frac{N_Z(m(z))}{m(z)(1-m(z)^2)},
\qquad
g_Z(z)-g_T(z)
=m'(z)\frac{N_Z'(m(z))}{N_Z(m(z))}.
}
\tag{11}
\]
These identities first hold near infinity and then on the physical continuation.
The notation \(N_Z(m(z))\) in (11) denotes that continuation where the cycle series itself does not converge.
The correction is a finite matrix operator determinant over the actual group algebra, not a finite product of scalar algebraic cavity factors.

The distinction matters at the tested atom.
The spectral edge \(z=4\) corresponds to \(m=1/3\), but \(z=0+i0\) corresponds to \(m=-i/\sqrt3\), outside \(|s|<1/3\).
Along \(z=i\eta\), one has \(m=-ir\), \(0<r<1/\sqrt3\), and
\[
1-sA_Z+3s^2=(1-3r^2)I+irA_Z
\]
has strictly positive real part.
Thus (9) supplies an actual continuous analytic-log branch along that path.
Termwise boundary evaluation of the cycle series at \(-i/\sqrt3\) is not justified.

## Primitive returns and their critical growth

The two torsion-free identity languages use the same full alphabet, and free returns are a subset of commuting returns.
Cancelling the primitive products of [L_A0015](Yin_L_A0015_v1.md#torsion-free-cycle-arithmetic-and-its-obstruction) gives
\[
\mathcal R(t)=
\prod_{\substack{[w]\ {\rm primitive\ cyclic\ alphabet\ class}\\
w=e\ {\rm in}\ \mathbb Z^2,\ w\ne e\ {\rm in}\ F_2}}
(1-t^{|w|}).
\tag{12}
\]
Primitivity in (12) is primitivity in the full free monoid; backtracking is allowed.
Both identity languages are closed under primitive roots, since the respective groups are torsion-free.

Put \(\Delta m_k=\tau_Z(A_Z^k)-\tau_T(A_T^k)\).
The number \(c_n\) of new primitive classes of length \(n\) is
\[
c_n=\frac1n\sum_{d\mid n}\mu_{\rm Mob}(d)\Delta m_{n/d}
\in\mathbb Z_{\ge0},
\qquad
\mathcal R(t)=\prod_{n\ge1}(1-t^n)^{c_n}.
\tag{13}
\]
These are coefficientwise identities and absolutely convergent analytic identities for \(|t|<1/4\).
The first even moment pairs from (2)--(4) are
\[
\begin{array}{c|rrrr}
k&2&4&6&8\\ \hline
\tau_T(A_T^k)&4&28&232&2092\\
\tau_Z(A_Z^k)&4&36&400&4900
\end{array}
\]
and hence
\[
\log\mathcal R(t)=-2t^4-28t^6-351t^8+O(t^{10}),
\qquad
(c_4,c_6,c_8)=(2,28,350).
\tag{14}
\]
Substituting the rational change of variable in (10) gives
\[
\log N_Z(s)=-2s^4-4s^6-27s^8+O(s^{10}).
\]
Thus the cyclically nonbacktracking counts are \(b_4=8,b_6=24,b_8=216\), and their primitive counts are \(2,4,26\).
This records the exact resummation of the backtracking attachments, rather than identifying the two kinds of primitivity.

Stirling's formula in (3), the bound
\(\tau_T(A_T^{2n})\le12^n\), and exponentially smaller proper-divisor terms in (13) give
\[
c_{2n}\sim\frac{16^n}{2\pi n^2},\qquad c_{2n+1}=0.
\tag{15}
\]
In particular
\[
\log\mathcal R(1/4)
=-\sum_{n\ge1}\frac{\Delta m_{2n}}{2n\,16^n}>-\infty,
\qquad
\mathcal R(1/4)>0.
\]
The bound \(\Delta m_{2n}\le\binom{2n}{n}^2\) and its \(n^{-1}\) asymptotic justify convergence.
Nevertheless (4)--(5) imply
\[
t\frac{\mathcal R'(t)}{\mathcal R(t)}
=\frac1\pi\log(1-16t^2)+O(1)\quad(t\uparrow1/4).
\tag{16}
\]
Thus the derivative is logarithmically singular while the product has zero local power exponent.
The singularity also shows that the return correction radius is exactly \(1/4\).
The nonbacktracking radius is exactly \(1/3\), since the change of variable is regular there, with derivative \(3/8\).
Individual integer cycle counts alone do not explain this critical behavior; their growth matters.

## Boundary residues and failure of an algebraic cavity repair

DLMF 19.12.1 gives
\[
K(k)=\log(4/k')+O(k'^2\log(1/k')),
\qquad k'=\sqrt{1-k^2}\downarrow0.
\]
Applying it to (4), for \(\delta\downarrow0\),
\[
g_Z(4+\delta)
=\frac1{4\pi}\log\frac{32}{\delta}
 +O(\delta\log(1/\delta)),
\qquad
g_T(4+\delta)=\frac38+O(\delta).
\tag{17}
\]
Consequently \(q(z):=\mathcal C'(z)/\mathcal C(z)\) has a nonzero logarithmic leading term at \(z=4\).
It is not algebraic over \(\mathbb C(z)\).

Here is a direct justification of that last assertion.
If \(\sum_j a_j(z)q(z)^j=0\) with polynomial coefficients, choose the least order \(v\) of vanishing of a nonzero coefficient at four and the largest index \(j_0\) attaining that order.
Divide the relation at \(z=4+\delta\) by \(\delta^v q^{j_0}\).
The \(j_0\) term tends to a nonzero constant.
Terms with the same order and smaller index tend to zero, and terms of higher order also tend to zero because any positive power of \(\delta\) dominates every power of \(\log(1/\delta)\).
This is a contradiction.

An algebraic nonzero function has algebraic logarithmic derivative, by implicit differentiation in characteristic zero.
More generally, every finite product \(\prod_j f_j(z)^{\alpha_j}\) of nonzero algebraic functions with fixed complex exponents has algebraic logarithmic derivative.
Thus neither \(\mathcal C\) nor the complete vertex-edge correction can have that form.
In particular \(\mathcal C\), \(\mathcal R\) and \(N_Z\) are not algebraic germs.
For the last statement, an algebraic \(N_Z\) would make
\(\mathcal R(t)=N_Z(m(1/t))\) algebraic.
This excludes a finite algebraic-factor repair, not finite formulas with transcendental factors or a residue-only index argument.

The interior point zero gives a different useful test.
The Haar covering
\((\alpha,\beta)\mapsto(\alpha+\beta,\alpha-\beta)\) replaces \(A_Z\) by \(4\cos\alpha\cos\beta\).
Integration in one coordinate gives
\[
g_Z(i\eta)
=-\frac{2i}{\pi\sqrt{\eta^2+16}}\,
K\!\left(\frac4{\sqrt{\eta^2+16}}\right)
\sim-\frac{i}{2\pi}\log\frac{16}{\eta},
\qquad
g_T(i\eta)\longrightarrow-\frac{i\sqrt3}{4}.
\tag{18}
\]
Write \(F_Z=1/g_Z\) for the reciprocal Cauchy transform.
Therefore
\[
\lim_{\eta\downarrow0}i\eta\,g_Z(i\eta)=0,\qquad
F_Z(i\eta)\to0,\qquad
\frac{F_Z(i\eta)}{i\eta}
\sim\frac{2\pi}{\eta\log(16/\eta)}\to\infty.
\tag{19}
\]
The commutation relation creates a logarithmic divergence and a zero reciprocal boundary value, but no finite atom slope.

In fact both laws are atomless without an Atiyah premise.
For the lattice, each level set
\(2\cos\theta+2\cos\phi=\lambda\) has Haar measure zero by Fubini, since each fixed-\(\theta\) fiber has at most two \(\phi\)-values.
For the tree, (2) has finite boundary values everywhere on its support, including its square-root endpoints, so the boundary-residue criterion excludes every atom.
The correction in (11) therefore has zero atom residue at every real point.
This is a relation-specific calibration, not a general estimate for other group matrices.

## Even cyclic root closure and positive moments do not suffice

The fractional-law example in L_A0015 admits a stronger return-language version.
Let
\[
\mu_*=\tfrac12\delta_0+\tfrac12\delta_4,\qquad
D_*(t)=\sqrt{1-4t}.
\]
Its Catalan expansion puts it in \(1+t\mathbb Z[[t]]\).
Every series in that ring has a unique Euler factorization
\(\prod_{n\ge1}(1-t^n)^{a_n}\) with integer \(a_n\), obtained by successively cancelling the lowest remaining coefficient.
Taking a logarithmic derivative and applying divisor inversion here gives
\[
a_n=\frac1{2n}\sum_{d\mid n}\mu_{\rm Mob}(d)\,4^{n/d}.
\tag{20}
\]
Twice \(a_n\) is the number of primitive necklaces of length \(n\) on four letters, so \(a_n\ge0\).
Thus positive integer multiplicities coexist with local exponent one half.
In contrast with (15), these multiplicities grow as \(a_n\sim4^n/(2n)\).

There is an actual cyclic root-closed language with these aggregate moments.
For every \(n\), choose exactly half of the primitive four-letter necklaces of length \(n\), which is possible by the integrality just proved.
Let \(L\) contain the empty word and all rotations and positive powers of the selected primitive words.
Membership depends only on the primitive necklace, so
\[
uv\in L\iff vu\in L,\qquad
w^r\in L\iff w\in L\quad(r\ge1).
\]
A selected primitive necklace of length \(d\mid k\) contributes \(d\) distinct length-\(k\) words.
Consequently
\[
|L\cap\mathcal A^k|
=\sum_{d\mid k}d\,a_d
=4^k/2\quad(k\ge1),
\tag{21}
\]
and together with the zeroth moment one, these are precisely the positive scalar moments of \(\mu_*\).

This language cannot be an identity language under any assignment of its four letters to a group.
Its length-one count is two, so two letters would represent the identity and the remaining two would represent nonidentity elements \(x,y\).
Root closure excludes \(x^2=e\) and \(y^2=e\).
At length two, the identity letters contribute four words, mixed identity/nonidentity words contribute none, and only \(xy,yx\) can contribute further words.
The total is at most six, contrary to the length-two count eight in (21).
Without root closure, the same aggregate law is realized by the labels \(e,e,g,g\) in the two-element group, with \(g^2=e\).

Thus cyclicity, primitive-root closure, positive integer primitive counts and positivity of the aggregate scalar moments still do not force integer atoms.
The example supplies no positive-definite full joint distribution satisfying group multiplication and unitary inverse relations.
Its role is to identify the additional group-identity compatibility that an S_A0007 argument must actually use, not to refute A0001.

## Consequence for the two strategies

The commutation pilot has produced an exact all-orders correction and a finite nonbacktracking operator realization.
The full correction is transcendental, so S_A0006 should no longer require it to collapse into finitely many algebraic tree-cavity factors.
A meaningful next target is a direct control of the atomic part of the correction, allowing a transcendental continuous part.
Writing the correction through the unknown full resolvent remains tautological unless an independent geometric or analytic estimate is obtained.

S_A0007 must retain more than generic cyclic root closure or positive Euler multiplicities.
The proposed route will therefore retain the full compatible group-word distribution together with analytic control through the relevant boundary continuation; this does not rule out a weaker sufficient compatibility condition.
The matrix in (8) retains the actual group algebra and therefore does not remove the original rank difficulty merely by having size four.
The tree and abelian cases used here are known Atiyah settings; no new group class, general residue quantization or solution of the full complex-coefficient Task is claimed.

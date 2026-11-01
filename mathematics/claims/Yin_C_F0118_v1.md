---
author: Yin
---

# Negative dual kernels and exact finite-polynomial holomorphic tests

## Current assessment
[Selected decision](#decision-isolated-original-whole-review-adoption-20261022)

## Statement

Fix finite d>=1 and real -1<q<1 in the canonical 2d-dimensional variance-one q-Gaussian tracial model.
Put c_j=(x_j+i y_j)/sqrt(2), let H_+ be the closed span of positive raw q-Fock words, and use the bounded normalized signed duals D_j^+,D_j^- constructed from C_F0023 by the displayed complex linear change of coordinates below.
They have the exact positive/negative coordinate commutators and annihilate the vacuum.
For every q in this interval,
\[
 H_+\subsetneq\bigcap_{k=1}^d\ker D_k^-.
\]
Indeed (c_i^*c_j-delta_ij)Omega=f_i tensor e_j is a norm-one vector orthogonal to H_+ and killed by every negative dual, while its full negative-dual commutator is nonzero.
For the closed subspace
\[
 K_{\rm iter}=\bigcap_{k,m,j_1,\ldots,j_m}
 \ker(D_k^-D_{j_m}^+\cdots D_{j_1}^+),\qquad m\ge0,
\]
all products are bounded, H_+ is contained in K_iter, and
\[
 K_{\rm iter}\cap\mathcal F_{\rm alg}
 =\operatorname{span}\{e_w:w\text{ is a positive word}\}.
\]
At q=0 the same tests give K_iter=H_+ on the whole Hilbert space.
For nonzero q only the finite-polynomial equality is proved; the exact equivalent adjoint-range totality problem below remains unresolved.
No all-q holomorphic rational inverse or rational boundedness theorem is asserted.

## Provenance and accepted inputs

The complete finite calculation and polynomial-kernel proof below were authored on 2026-09-11 by another AI agent.
The existing [original finite-calculation finding](../audits/reviews/Yin_R_F0106_v1.md#5-independent-finite-calculation-review) actually checked these entire sections, including the q=0 whole-space case and exact nonzero-q limitation.
The proof accepts [C_F0023's bounded normalized duals](Yin_C_F0023_v1.md#statement), the actual [MS23 q-Fock/Wick conventions](../audits/literature/MS23/Yin_U006.md#ms23-u006), and the relevant C_F0020 degree diagnostic at their disclosed scopes.
The [source comparison with Miy26](../ledger/Yin_L_F0022_v1.md#4-what-miy26-actually-uses) remains outside the retained finite-calculation review's certification; it is not an extra input to the theorem below.

## Argument

### 1. Inputs and conventions

The inputs inspected before this calculation are [Yin_C_F0023, Equations (2) and (7)](Yin_C_F0023_v1.md#yin_c_f0023), the cubic q-dual calculation [in Yin_C_F0020, Equation (13)](Yin_C_F0020_v1.md), [MS23-U006](../audits/literature/MS23/Yin_U006.md#ms23-u006), and the complete mixed-word argument in [Miy26-U005, Lemma 4.1](../audits/literature/Miy26/Yin_U005.md#miy26-u005).
The intended application is the actual holomorphic-state premise of [the q-rational evaluation interface, Section 3](Yin_C_F0103_v1.md).
These local inputs suffice for the finite calculations; no additional external result is claimed or required here.

Fix a finite d>=1 and real -1<q<1.
Let x_1,y_1,...,x_d,y_d be the canonical variance-one selfadjoint q-Gaussian tuple, and put
\[
c_j=(x_j+\mathrm i y_j)/\sqrt2,
\qquad c_j^*=(x_j-\mathrm i y_j)/\sqrt2.
\]
The associated one-particle vectors e_j,f_j are all orthonormal, with
\[
c_j=\ell_q(e_j)+\ell_q(f_j)^*,\qquad
c_j^*=\ell_q(f_j)+\ell_q(e_j)^*.
\]
Write H=L2(M,tau), Omega=1, P=P_Omega.
Let H_+ be the closed span of the positive raw words e_w, and let F_alg be the algebraic q-Fock space, equivalently the starred-polynomial vector space.
Let H_n denote the n-particle subspace.
Different degrees are orthogonal; raw words in one degree are a basis but generally are not orthogonal.

Let B_xj,B_yj be the bounded normalized duals furnished by Yin_C_F0023, and define
\[
D_j^+=(B_{x_j}-\mathrm i B_{y_j})/\sqrt2,
\qquad
D_j^-=(B_{x_j}+\mathrm i B_{y_j})/\sqrt2.
\tag{1}
\]
Complex linearity of the commutator gives, on all H,
\[
\begin{array}{ll}
[D_k^+,c_j]=\delta_{kj}P,&[D_k^+,c_j^*]=0,\\
[D_k^-,c_j]=0,&[D_k^-,c_j^*]=\delta_{kj}P,
\end{array}
\qquad D_k^\pm\Omega=0.
\tag{2}
\]
On polynomial vectors, D_k^+ and D_k^- are respectively (id tensor tau) applied to the algebraic free difference quotients in c_k and c_k^*.
These formulas follow directly from Yin_C_F0023 under the displayed invertible complex change of coordinates.
In particular, every D_k^- kills H_+: first use (2) on positive polynomials, then boundedness and density in H_+.

### 2. The degree-two obstruction to the simple common kernel

For any i,j, put
\[
\xi_{ij}=(c_i^*c_j-\delta_{ij}1)\Omega=f_i\otimes e_j.
\tag{3}
\]
The equality follows by applying the q-annihilator to the one-particle vector e_j.
It is independent of q.
Since f_i and e_j are orthogonal, the two-particle q-symmetrizer $I+q\Sigma$, where $\Sigma$ flips the two factors, gives ||xi_ij||_q=1.
This vector is orthogonal to H_+: the symmetrizer permutes letters and cannot change a negative letter into a positive one.

Nevertheless, (2) and tau(c_j)=0 give, for every k,
\[
D_k^-\xi_{ij}
=\delta_{ki}P c_j\Omega=0.
\tag{4}
\]
Consequently
\[
H_+\subsetneq\bigcap_{k=1}^d\ker D_k^-
\qquad(-1<q<1).
\tag{5}
\]
This is a counterexample to the proposed vector-kernel characterization, not to holomorphicity of a rational inverse under its other hypotheses.
In particular, the polynomial c_i^*c_j-delta_ij does not commute with all negative duals: its k-th commutator is delta_ki P c_j, which is a nonzero operator when k=i even though its vacuum column vanishes.

### 3. Iterated tests characterize finite holomorphic polynomials

Define the closed subspace
\[
K_{\mathrm{iter}}
=\bigcap_{\substack{1\leq k\leq d,\ m\geq0\\j_1,\ldots,j_m\in\{1,\ldots,d\}}}
\ker\bigl(D_k^-D_{j_m}^+\cdots D_{j_1}^+\bigr),
\tag{6}
\]
where k ranges from 1 to d and the product after D_k^- is the identity when m=0.
Each finite product is bounded.
Then
\[
H_+\subseteq K_{\mathrm{iter}},\qquad
K_{\mathrm{iter}}\cap F_{\mathrm{alg}}
=\operatorname{span}\{e_w:w\text{ is a positive word}\}.
\tag{7}
\]

Here is the finite proof, with the degree issue explicit.
Label e_j by j and f_j by bar(j).
If z_a is respectively c_j or c_j^*, the Wick polynomial W(u_1 tensor ... tensor u_n) has leading monomial z_1...z_n and only lower terms of degrees n-2,n-4,... .
This follows from the creation/annihilation action: multiplication changes particle degree by one, and its highest-degree term is literal creation.
All odd moments of the centered q-Gaussian tuple vanish, by the same parity decomposition.

For a polynomial monomial z_1...z_n, the normalized derivative is a sum over occurrences of its designated letter of
\[
z_1\cdots z_{r-1}\,\tau(z_{r+1}\cdots z_n)\Omega.
\]
Only the last-letter occurrence can have degree n-1.
A nonempty suffix of length one has zero trace, and a longer nonzero-trace suffix has even length at least two.
The lower Wick terms likewise contribute degree at most n-3.
Thus on a raw word u_1 tensor ... tensor u_n with n>=1,
\[
D_k^\pm(u_1\otimes\cdots\otimes u_n)
=\begin{cases}
u_1\otimes\cdots\otimes u_{n-1},&u_n\text{ has the matching signed label},\\
0,&\text{otherwise}
\end{cases}
\quad\bmod\!\bigoplus_{r\leq n-3}H_r.
\tag{8}
\]
An empty or negative degree range means zero.
At q=0 there are no lower corrections; for general q the cubic correction in Yin_C_F0020 is already an example of the remainder in (8).

On positive polynomials each D_j^+ is exactly terminal positive-letter deletion, because every nonempty positive suffix has zero vacuum expectation.
It therefore preserves positive polynomials and, by boundedness, H_+.
This proves the first inclusion in (7).

Now let xi in K_iter intersect F_alg have highest nonzero particle degree N.
Every degree-N word containing a negative letter has a unique presentation
\[
w=a\,\overline{k}\,j_m\cdots j_1
\]
in which bar(k) is its rightmost negative letter.
Apply D_k^- D_jm^+ ... D_j1^+ and project onto H_(N-m-1).
Formula (8) shows that this projection is precisely the terminal-deletion residual of the degree-N component.
Lower input degrees and lower corrections cannot contribute to this output degree.
The coefficient of the raw word a in that projection is therefore the coefficient of w in xi.
Since the test vanishes, that coefficient is zero.
Independence of the raw-word basis suffices; orthogonality within H_n is not used.

All mixed words in the top component vanish.
Subtract that positive homogeneous component, which itself belongs to K_iter, and repeat at the next highest degree.
Finite descent proves the second assertion in (7).
For example, (3) is now detected by
\[
D_i^-D_j^+\xi_{ij}=D_i^-(c_i^*\Omega)=\Omega.
\tag{9}
\]

For q=0 the same residual tests characterize H_+ on all H, since each test is exact terminal deletion without corrections.
For nonzero q, (7) does not prove K_iter=H_+.
There is no highest input degree for a general L2 vector, and arbitrarily high degrees can feed a fixed output degree through the lower terms.
Boundedness permits applying each test to an L2 limit, but does not make particle truncations remain in its kernel.

An exact remaining Hilbert-space interface is the totality assertion
\[
H_+^\perp
=\overline{\operatorname{span}}\left\{
(D_{j_1}^+)^*\cdots(D_{j_m}^+)^*(D_k^-)^*\eta:
\eta\in H,\ m\geq0,\ k,j_1,\ldots,j_m\in\{1,\ldots,d\}
\right\}.
\tag{10}
\]
Taking orthogonal complements makes (10) equivalent to K_iter=H_+.
The finite calculation establishes no such density statement for nonzero q, nor does it establish that every proposed affiliated state satisfies all tests in (6).

## Assessment history

### Decision registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:47 |
| status | open |
| reason | Register the complete retained finite proof in C before adopting its applicable original actual review finding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact all-q common-kernel obstruction, finite-polynomial iterated criterion, q=0 full-space case and nonzero-q unresolved boundary. |
| argument | [Argument](#argument) | Complete original Sections 1-3 calculation and proof, with accepted normalized-dual and q-Fock inputs. |

### Decision retained-complete-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:47 |
| status | proved |
| reason | Adopt the actual complete original finite-calculation finding for the exact unchanged retained proof. Its original date and genuinely unestablished context relationship remain explicit; this current adoption creates no new or redated review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire exact finite-polynomial criterion, common-kernel obstruction, q=0 case and unresolved nonzero-q whole-space boundary. |
| argument | [Argument](#argument) | Complete original Sections 1-3 and accepted dual/q-Fock interfaces, without the later source comparison. |
| review | [Original complete finding](../audits/reviews/Yin_R_F0106_v1.md#5-independent-finite-calculation-review) | Complete finite-calculation and polynomial proof reviewed on 2026-09-11, preserving its actual scope and unknown initial-context arrangement. |


### Decision isolated-original-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:47 |
| status | proved |
| reason | Adopt the separately assigned isolated complete reconstruction of this fixed original mathematics and its actual necessary interfaces. The reviewer supplied no target development or repair and completed the initial finding before old target verdicts. Preserve all exact hypotheses, original graphs and closures, source-depth limits, historical decisions and original UNKNOWN relationship facts. The current finding creates no generalization beyond the stated theorem and no research Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire exact finite-polynomial criterion, common-kernel obstruction, q=0 case and unresolved nonzero-q whole-space boundary. |
| argument | [Argument](#argument) | Complete original Sections 1-3 and accepted dual/q-Fock interfaces, without the later source comparison. |
| review | [Isolated complete original mathematical finding](../audits/reviews/Yin_R_F0106_v1.md#current-signed-q-finite-tests) | Complete actual fixed mathematical statement and original argument at the exact retained scope, necessary accepted interfaces, disclosed first-pass review-existence/scope descriptions and all source, closure and nontransfer limits; initial finding2026-10-22T21:41 precedes old target verdict comparison. |


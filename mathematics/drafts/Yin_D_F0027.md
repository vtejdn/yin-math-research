---
author: Yin
---

# Complex Hermitian laws: full-adjugate matching and the remaining linear interface

This continuing preparation concerns the complex Hermitian laws in the original [F0012](../tasks/Yin_T_F0012_v3.md#contract), [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract) contracts.
The complete phase-line least-value argument and its auxiliary proofs have their fixed home in [the independently reviewed C_F0194_v6](../claims/Yin_C_F0194_v6.md#decision-phase-line-floor-reviewed).
In particular the [fixed complex-distance assertion](../claims/Yin_C_F0194_v6.md#complex-distance), [finite-phase count](../claims/Yin_C_F0194_v6.md#phase-envelope-count), and [phase-line assembly](../claims/Yin_C_F0194_v6.md#in-probability-floor) retain their exact distinct scopes there.
The purely imaginary odd-size obstruction is retained completely in [that fixed boundary example](../claims/Yin_C_F0194_v6.md#odd-skew-obstruction); it refutes an all-law all-size least-value floor, not the original determinant limsup.
The unique mixed-orientation obstruction and new non-line modules remain below.
This is development, not an independent review or an adopted general-complex least-value theorem.

<a id="transpose-noncancellation-failure"></a>
## The transpose coefficient has a real algebraic failure

For xi=i epsilon, zero diagonal and zero shift, as in the fixed odd-size example, the symmetric part sym W_N=(W_N+W_N^T)/2 is identically zero.
For an invertible even-dimensional realization D of a skew-symmetric matrix, D^(-1) is skew-symmetric and therefore
\[
 A=\operatorname{adj}D=(\det D)D^{-1}\ne0,
 \qquad Q=\operatorname{sym}A=0.
\]
This conditional algebraic statement does not assert that every even random realization is invertible.
It shows that both the symmetric-part floor and the noncancelling sym-adjugate graph used in the real-input proof can disappear in the complex-input model.
For example D=diag(J,...,J), with J=[[0,i],[-i,0]], is an invertible Hermitian skew-symmetric matrix with these properties.
The graph based on Q then has no edges at any positive threshold although A is nonzero.
This failure concerns the real-input transpose mechanism, not merely a weaker exponent in its inverse-concentration input.

<a id="mixed-orientation-cancellation"></a>
## Cancellation remains possible with positive real-part variance

Let c=(1+i)/sqrt(2), xi=c epsilon, and consider two internal coordinates with opposite orientations:
\[
 z=(c\epsilon_1,\bar c\epsilon_2)^T,
 \qquad
 R=\begin{pmatrix}0&1-i\\1+i&0\end{pmatrix},
 \qquad B=R/2.
\]
Since R^2=2I, this B is exactly R^(-1).
Its norm is 1/sqrt(2), and
\[
 \operatorname{sym}B=\frac12\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad s_{\min}(\operatorname{sym}B)=1/2.
\]
For E=diag(1,-1), S=[[0,1],[1,0]] and T=[[0,-i],[i,0]], one has iTE=-S.
Here Phi(z)=(Rz+R^T bar z)/2.
As x=(epsilon_1,epsilon_2)^T/sqrt(2) and y=Ex,
\[
 \Phi(z)=Sx+iTEx=0
\]
for every pair of signs.
Thus a floor for sym B, a bound for ||B||, and a positive variance of Re xi do not imply any positive singular rank for the complex internal-row random map at a general index.
Direct sums of these paired blocks give the same cancellation in arbitrary even internal dimension when the two orientation groups have equal size.
This is an exact obstruction to that deterministic bridge, with bounded well-conditioned B and sym B.

The two-coordinate configuration occurs at the middle index j=2 of a three-dimensional Hermitian Wigner matrix, with zero diagonal law and N=3: its internal column has orientations xi and conjugate xi.
Set the two internal diagonal shifts to zero and choose the internal off-diagonal deterministic shifts so that the event epsilon_13=1 makes the internal matrix equal to the displayed B.
Explicitly use F_13=(1-i)/2-c/sqrt(N) and F_31=(1+i)/2-bar(c)/sqrt(N); this is even a Hermitian bounded shift.
The event has probability 1/2 and is independent of the exposed two signs.
This realizes the failed conditional map within an actual minor, rather than using an impossible coefficient matrix.
The construction at one fixed dimension and the direct-sum coefficient example do not show nonvanishing asymptotic failure probability for a full random Wigner minor.
Excluding their higher-dimensional analogues probabilistically would require new information about the actual internal minor.

<a id="inverse-count-interface"></a>
## The accepted inverse-counting input has a separate real-scalar boundary

The inspected [Ngu12a conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) and [edition-specific source notes](../audits/literature/Ngu12a/readme.md) concern real scalar random variables with vector-valued coefficients.
Their coefficient dimension two permits complex coefficients multiplying a real scalar; it does not replace the scalar random variable by a complex entry with dependent components.
The original Condition 1 and Theorem 1.3 were already inspected at PDF pp. 2--3 of the retained arXiv v1, and the quadratic theorem at p. 5.
This preparation reuses that exact accepted scope and makes no new claim about their original proofs or a different edition.

At a fixed deterministic coefficient vector, ordinary upper-row exposure still works for a complex Hermitian matrix: every newly exposed strict upper entry has law xi, while lower entries already exposed enter the center.
The difficulty is the structural inverse theorem and the subsequent permutations in the [full profile count](../claims/Yin_C_F0194_v1.md#structured-vector-counting).
For a general complex law there is no declared accepted input here converting large concentration of sum u_j xi_j into the same bounded-rank rational progression description.
Moreover a candidate-dependent reservoir permutation changes some upper entries from xi to conjugate xi.
Unless the law is conjugation invariant, it does not preserve the identical scalar law used to define the common monotone tail concentrations and to rerun the post-permutation profile count.
Even when the law is conjugation invariant, the real-scalar inverse-theorem boundary still has to be addressed.

The exact two-copy representation of a complex xi by a fair real sign is valid after freezing two complex samples.
It then gives random complex coefficients depending on those frozen samples, not the fixed coefficient structure used by the accepted count.
No conditional progression entropy bound or uniform orientation-aware profile argument has been established by that representation alone.
Consequently the [one-omitted-row kernel estimate](../claims/Yin_C_F0194_v5.md#one-row-kernel-ac), the isolated-minor branch and the matching branch cannot be cited unchanged for arbitrary complex laws.
The real-input Claim remains at its exact accepted scope.


<a id="comparison-and-return"></a>
## Parity comparison and the surviving objective

The [earlier real commutator obstruction](../ledger/Yin_L_F0061_v1.md#real-affine-obstruction) creates a skew-symmetric polynomial or affine pencil from real symmetric inputs.
The purely imaginary entry-law obstruction already occurs in one complex Hermitian Wigner matrix, with scalar polynomial P(x)=x and shift zero.
The parity mechanism is the same, but the input class and the purported intermediate floor are different.
Neither obstruction refutes the original dimension-limsup contract.
Even-size or suitable-subsequence estimates remain separate possible objectives for the pure-imaginary law.
The non-line preparation below addresses a different law class and keeps its generic linear inverse input explicit.

<a id="nonline-full-adjugate-scope"></a>
## Full-adjugate matching for a non-line complex law

This new preparation considers a fixed centered complex law xi with E|xi|^2=1 whose support is not contained in a real line through zero.
In this module W_N has independent strict upper entries xi/sqrt(N), conjugate lower entries and independent real diagonal entries zeta/sqrt(N), for a fixed finite-second-moment law zeta; the diagonal and upper families are independent.
An offset F is deterministic and complex with no symmetry requirement, unless an independent random-offset form is stated explicitly.
It does not import the phase-line inverse-counting argument for this new scalar law.
The bounded result is a complete quadratic matching estimate using the full adjugate, together with a low-matching actual-minor ratio implication that needs no symmetric-part floor.
The needed complex-distance estimate is the [reviewed fixed-cutoff auxiliary assertion](../claims/Yin_C_F0194_v6.md#complex-distance), whose scope includes arbitrary centered variance-one complex laws and coordinatewise conjugation.
The matching source is [MNV16-U001](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) at its exact original real-coefficient fair-sign degree-two scope, with its recorded source-proof inspection limits.
All new support, coefficient, column-exposure and probability arguments are supplied below as development, without a new Claim or independent review.

<a id="nonline-difference-edge"></a>
## Two noncollinear difference values control every ordered coefficient pair

Let delta=xi-xi' for independent copies.
There are a,b in its topological support such that a is nonzero and Im(bar a b) is nonzero.
Indeed, if the support of delta were contained in a real line L, the real orthogonal projection of xi-xi' onto L^perp would vanish almost surely.
Independence and finite second moment would then give zero variance for that projection of xi.
Centering would make the projection zero, implying xi belongs to L almost surely, contrary to the hypothesis.
Thus the difference support is not contained in any real line, which supplies such a,b.

There are fixed kappa,p>0, depending only on xi, with the following uniform assertion.
Let delta_s and delta_t be independent, each having either the law of delta or its conjugate, in any fixed orientations s,t.
For all u,v in C,
\[
 \mathbb P\{|\bar\delta_s u\delta_t
                 +\bar\delta_t v\delta_s|
                  \ge\kappa\max(|u|,|v|)\}\ge p.
 \tag{Full-edge-survival}
\]
To prove this, put alpha=s(a), beta_1=t(a), beta_2=t(b), where each orientation is either identity or conjugation.
The two coefficient forms at these support values have matrix
\[
 L_{s,t}=\begin{pmatrix}
 \bar\alpha\beta_1&\bar\beta_1\alpha\\
 \bar\alpha\beta_2&\bar\beta_2\alpha
 \end{pmatrix},
 \qquad
 \det L_{s,t}=|a|^2(\beta_1\bar\beta_2-\beta_2\bar\beta_1)\ne0.
\]
The determinant has absolute value 2|a|^2|Im(bar a b)| in all four orientation cases.
Consequently, with kappa_0=min_(s,t) s_min(L_s,t)/sqrt(2)>0 and M=max(|u|,|v|), at least one of the two forms has modulus at least kappa_0 M.
Choose a fixed sufficiently small epsilon>0 so that replacing alpha and beta_l by points within epsilon changes that form by at most kappa_0 M/2.
For example the error is bounded by 2epsilon(|a|+max(|a|,|b|)+epsilon)M.
Both support-ball probabilities p_a=P(|delta-a|<epsilon) and p_b=P(|delta-b|<epsilon) are positive.
The event of the selected pair of balls has probability at least p_a min(p_a,p_b), uniformly in the orientations and in u,v.
Take kappa=kappa_0/2 and p=p_a min(p_a,p_b).
The case M=0 also satisfies the displayed assertion.
This proves the bound without a density, an atom-size bound or independence of the real and imaginary parts.

<a id="nonline-full-matching"></a>
## The actual complex border has a full-adjugate matching estimate

Let M=W_N+F be the normalized Hermitian Wigner matrix with fixed upper law xi and an arbitrary deterministic complex shift.
Fix one omitted index i, condition on its actual principal minor D_i and exposed diagonal a_i, and write A_i=adj D_i.
After placing i first the raw lower column z has independent xi/conjugate-xi coordinates and is independent of this conditioning.
The bordered determinant identity is
\[
 \det M=a_i\det D_i-(z^*/\sqrt N+f^T)
                           A_i(z/\sqrt N+g),
\]
where f,g are arbitrary fixed complex offsets under the conditioning.
Its quadratic part is -z^*A_i z/N.
The identity holds for singular minors by polynomial continuity.

For h>0 define an undirected graph on the minor coordinates by an edge jk, j!=k, when
\[
 \max(|(A_i)_{jk}|,|(A_i)_{kj}|)\ge h\|A_i\|_F.
 \tag{Full-adjugate-graph}
\]
Let H_i^(full)(h,r) require A_i nonzero and a matching of at least r edges.
The Frobenius norm here is that of the full actual adjugate; no symmetric-part normalization is substituted.
There are c_*,C>0, depending only on xi, such that for every r>=2,
\[
 \mathbb P\left\{
    |\det M|/\|A_i\|_F\le c_*h/N
                \;\middle|\;D_i,a_i\right\}
 \le C\left[e^{-c_*r}+\sqrt{\log(2+r)}\,r^{-1/9}\right]
 \tag{Full-adjugate-matching}
\]
on H_i^(full)(h,r), uniformly over the conditional minor, diagonal, center and offsets.

Here is the complete reduction to the accepted real-sign theorem.
Choose a deterministic lexicographically first r-edge matching in the graph, conditional on D_i.
For every raw oriented coordinate take two independent copies z_j^(0),z_j^(1) and an independent fair sign epsilon_j, with all these families independent, and write
\[
 z_j=\frac{z_j^{(0)}+z_j^{(1)}}2
                +\frac{\delta_j}2\varepsilon_j,
 \qquad \delta_j=z_j^{(0)}-z_j^{(1)}.
\]
This represents the original independent coordinate law exactly.
For an edge jk the coefficient of epsilon_j epsilon_k in the determinant is
\[
 -\frac{\bar\delta_j(A_i)_{jk}\delta_k
               +\bar\delta_k(A_i)_{kj}\delta_j}{4N}.
 \tag{Full-sign-coefficient}
\]
The factor 1/4 comes from the two half-differences, and 1/N from normalized Wigner entries.
The difference orientations are precisely those in (Full-edge-survival).
Hence each selected edge has coefficient modulus at least kappa h||A_i||_F/(4N) with probability at least p.
These survival events are independent across the disjoint edges, since they use disjoint two-copy endpoint pairs.
A Chernoff bound leaves at least pr/2 surviving edges outside probability C exp(-cr), with fixed positive c, for sufficiently large r.

Conditional on all two-copy values, choose a common projection pi equal to real part or imaginary part that retains at least half the surviving edges at modulus loss at most sqrt(2).
This choice depends on the two-copy values, not on the remaining fair signs.
The projected determinant is a real polynomial of those independent signs.
Every diagonal term is affine in its single sign, since epsilon_j^2=1, including when its original coefficient was complex.
It is therefore multilinear of degree at most two, with at least pr/4 disjoint quadratic monomials of modulus at least
\[
 \lambda_N=\frac{\kappa h\|A_i\|_F}{4\sqrt2 N}.
\]
Choose c_*<kappa/(16sqrt(2)), decreased also to fit the survival exponent.
The event |det M|<=c_*h||A_i||_F/N places pi(det M)/lambda_N in an interval of length strictly less than one.
The exact MNV16 degree-two theorem then gives C sqrt(log(2+r))r^(-1/9), with unrestricted lower-degree terms and center.
The finitely many small r and the requirement that the retained source rank be at least two are absorbed by increasing C.
Integrating the two-copy values and adding their exponential failure proves (Full-adjugate-matching).
This conditional estimate uses the non-line hypothesis only through (Full-edge-survival).

<a id="full-adjugate-low-matching"></a>
## Low full-adjugate matching excludes a large uncovered diagonal

The next lemma holds for every fixed centered variance-one complex law, including line-supported laws.
The non-line hypothesis is unnecessary for this low-matching half.
Let D be an actual m-by-m shifted Hermitian Wigner minor normalized by sqrt(N), with m in [N/2,N], fixed independent real diagonal law of finite second moment, and an arbitrary deterministic complex shift.
For this local lemma the shift need not have a prescribed bound; retain the event ||D||<=N^K for a fixed K>=0.
Write A=adj D and use the full-adjugate graph (Full-adjugate-graph).
Fix J>=0 and H>J+K+1, and let r_N>=2 have r_N log(N)=o(N).
There are fixed c,C>0 such that the probability is at most C exp(-cN) that some I subset of [m], |I|<2r_N, and some j outside I satisfy
\[
 \begin{split}
 &A\ne0,\quad\|D\|\le N^K,\qquad
       |A_{jj}|\ge N^{-J}\|A\|_F,\\
 &|A_{ab}|<N^{-H}\|A\|_F
            \quad(a\ne b,\ a,b\notin I).
 \end{split}
 \tag{Full-large-diagonal}
\]
The constants are independent of the deterministic shift and of m,N, and the sufficiently large N may depend on the fixed exponents and the sequence r_N.
There is no symmetric-part guard or exceptional polynomial-floor term in this bound.

Fix I,j and condition on B=D with row and column j removed.
The event in question requires det B=A_jj nonzero and ||B||<=N^K; otherwise it is empty.
The exact adjugate column formula, valid polynomially before division, gives
\[
 \frac{A_{-j,j}}{\det B}
       =-B^{-1}(z/\sqrt N+g),
\]
where z has independent raw xi/conjugate-xi coordinates and is independent of B, and g is the fixed lower-column shift.
The exposed upper row, its possibly different shift, and the diagonal at j do not enter this identity.
Put R=B^(-1); then s_min(R)=1/||B||>=N^(-K).
For U=[m] minus (I union {j}), p=|U|=m-|I|-1, the principal block R_UU has at least p-|I| singular values at least N^(-K).
Indeed ker R_IU has dimension at least p-|I|, and on that kernel the full-column lower bound for R is the lower bound for its U-row projection.
For large N, p>=N/3 and p-|I|>=p/2.

Condition also on z_I.
The remaining z_U retain their independent oriented law, and the large-diagonal and small-column conditions force
\[
 \left\|R_{UU}z_U+w\right\|
       \le\sqrt{Np}\,N^{J-H},
\]
for a fixed conditional center w, after multiplying by sqrt(N).
Take at least p/2 left singular directions with singular values at least N^(-K), project the center onto them, and divide their coordinates by the corresponding singular values.
These directions and the affine center may be chosen Borel by the spectral projection above that fixed threshold and its pseudoinverse; ties may all be retained.
The event then forces z_U to lie within
\[
 \sqrt p\,N^{J-H+K+1/2}
\]
of a fixed complex affine subspace of codimension at least p/2.
Since H>J+K+1, this is below the fixed c sqrt(p) distance threshold eventually.
The [reviewed complex fixed-cutoff distance estimate](../claims/Yin_C_F0194_v6.md#complex-distance) bounds its conditional probability by C exp(-cp), uniformly over B,z_I and the center.
The norm and adjugate conditions were used only to imply this linear event and need not hold on the larger event to which the distance estimate is applied.
Integrate the conditioning, including the unused exposed diagonal, and union the at most N^(2r_N+2)=exp(o(N)) choices of I,j.
This proves the exponential assertion.

<a id="full-adjugate-hub-ratio"></a>
## A hub approximation now needs only D times adj D

On the complement of the last exceptional event, suppose A is nonzero, ||D||<=N^K and the full-adjugate graph at h=N^(-H) has matching size less than r_N.
The endpoints I of a maximal matching give |I|<2r_N and all uncovered off-diagonal entries of A smaller than N^(-H)||A||_F.
Every uncovered diagonal is smaller than N^(-J)||A||_F by (Full-large-diagonal).
Split A=A_hub+E, where A_hub equals A on all rows or columns in I and is zero elsewhere.
Then
\[
 \operatorname{rank}A_{\rm hub}\le2|I|<4r_N<m,
 \qquad
 \|E\|_F\le e_N\|A\|_F,
 \quad e_N=\sqrt m\,N^{-J}+mN^{-H}.
\]
No fixed central strip is added and no symmetry of A or D is assumed.
The exact identity DA=(det D)I implies, at the first singular-value index beyond rank(D A_hub),
\[
 |\det D|\le\|DE\|
       \le N^K e_N\|A\|_F.
\]
Consequently
\[
 \rho_D:=\frac{|\det D|}{\|A\|_F}
       \le N^K\bigl(\sqrt m\,N^{-J}+mN^{-H}\bigr),
 \qquad s_{\min}(D)\le\sqrt m\,\rho_D.
 \tag{Full-low-ratio}
\]
For invertible D the last inequality follows from rho_D=(sum_l s_l(D)^(-2))^(-1/2).
For singular D with A nonzero both sides in that last inequality are zero.
This argument uses neither s_min(sym D) nor any other floor for a symmetric part.

For any prescribed T_0>0 choose
\[
 J>K+T_0+1,\qquad
 H>\max\{J+K+1,\ K+T_0+2\}.
 \tag{Full-threshold-order}
\]
Then rho_D<=N^(-T_0) eventually on the retained norm and low-matching events, outside probability C exp(-cN).
The choice is made after the desired precision and the norm exponent; there is no new floor exponent to be chosen first.
For all N actual principal minors D_i in one full matrix these implications hold simultaneously outside C exp(-c'N), by a further union over the omitted index.
They are uniform over deterministic shifts; conditioning on an independent random shift within this dimension gives the same norm-guarded assertions.

<a id="nonline-full-adjugate-return"></a>
## What the new matching module removes and what remains

For the non-line law, the high-matching and low-matching parts now use the same full-adjugate graph.
The high part has (Full-adjugate-matching), and the low part forces an arbitrarily fine actual-minor ratio by (Full-low-ratio).
The latter is already an exponential-probability actual-minor deduction for every centered variance-one complex law.
It does not assert that the small minor direction is isolated.

For clarity the exact remaining full-matrix probability event can be retained in the same many-index normalization.
Fix K>=0 and use the norm/rank-restricted events E_N(K,epsilon),G_i(K,epsilon) of the [fixed event definitions](../claims/Yin_C_F0194_v6.md#phase-line-remaining-event), now for this complex-law matrix.
Those definitions involve only adjugates, singular values, ||M|| and rank, and the complex fixed-distance proof gives the same rectangular spread and pointwise cofactor average.
Let h_N=N^(-H), choose H by (Full-threshold-order), and require
\[
 C_1N^{2K+1}\varepsilon_N\le c_*h_N/N.
\]
For example epsilon_N=N^(-A) works eventually for any A>H+2K+2.
Writing H_i^(full)=H_i^(full)(h_N,r_N), the complete new reduction is
\[
 \begin{split}
 \mathbb P(E_N(K,\varepsilon_N))
 &\le C\psi(r_N)+C e^{-cN}\\
 &\quad+\frac C N\sum_{i=1}^N
 \mathbb P\{G_i(K,\varepsilon_N)\cap
        (H_i^{\rm full})^c\cap\{\rho_{D_i}\le N^{-T_0}\}\},\\
 \psi(r)&=e^{-cr}+\sqrt{\log(2+r)}\,r^{-1/9}.
 \end{split}
 \tag{Nonline-full-adjugate-reduction}
\]
This is pointwise usable-index averaging followed by the conditional matching estimate and the simultaneous low-ratio implication.
It introduces no factor N in front of psi(r_N).
The terminal event and the rank-at-least-N-1 restriction are not removed by this module.
For a polynomially bounded deterministic shift the elementary finite-second-moment norm guard can be added with arbitrary polynomial failure; for an independent random shift add or retain its guard as appropriate.

The finite-phase envelope count applies to a real scalar amplitude with finitely many deterministic phases, and cannot be cited for a generic non-line complex scalar law.
A valid generic complex inverse/profile-counting interface, its omitted-row and near-kernel consequences, and the associated rank, second-value and isolated-minor probability deductions remain necessary for a full least-value assembly along this route.
No such probability inputs or general complex-law floor are asserted here.
The pure-imaginary odd-size counterexample remains outside the high-matching hypothesis on the law and is not contradicted.

<a id="generic-linear-input"></a>
## The precise remaining linear input

The following interface is an explicit hypothesis for the deductions in the next sections, pending the separate generic complex profile count.
The [continuing D30 source and count preparation](Yin_D_F0030.md) is intended to supply it; a development address or a source abstract is not treated as its proof.
The interface is stated in a slightly weaker probability form than exponential failure, since arbitrarily high polynomial failure already suffices for the terminal deductions.

Fix a cutoff exponent kappa>0 and put xi_N=(xi conditioned on |xi|<=N^kappa).
For an independent xi_N vector and any coefficient vector u in C^m define the orientation envelope
\[
 \mathcal R^{(N)}_J(u,t)=
 \max_{e\in\{\mathrm{id},\mathrm{conj}\}^{J}}
 \sup_{w\in\mathbb C}
 \mathbb P\left\{\left|\sum_{j\in J}u_j e_j(\xi_{N,j})-w\right|\le t\right\}.
 \tag{Generic-envelope}
\]
The copies in this definition are separate from the matrix.
No centering or variance renormalization of xi_N is imposed.

Here is the hypothesis, denoted Linear(q,b,K,kappa,s0).
For every fixed q,b,K>0 and fixed integer s0>=0 there are finite a,L,C,N0, depending only on these data and xi, such that the following holds uniformly for N>=N0 and m in [N/4,N].
Take any deterministic Hermitian orientation table for the independent unordered off-diagonal xi_N samples: its upper entry may be either xi_N or conjugate xi_N and its lower entry is the conjugate of that same sample.
Add an arbitrary deterministic complex offset, with deterministic diagonal values, inside a common polynomial entry bound m^K for the complete matrix D; enlarge K in applications so this bound follows from the cutoff and offset guard.
For each such fixed orientation table and offset there is a D-measurable event Omega with P(Omega^c)<=C m^(-q) such that on Omega, simultaneously for all row sets R with |R|>=m-s0 and all unit u,
\[
 \max_{j\in R}|(Du)_j|\le m^{-L}
       \quad\Longrightarrow\quad
 \mathcal R^{(N)}_{[m]}(u,m^{-a})\le m^{-b}.
 \tag{Generic-linear-interface}
\]
Require the same assertion for D^T, with the failure bound enlarged by a fixed factor if its separate exceptional event is unioned.
Only s0=0 and s0=1 will be needed.
Uniformity is over any fixed orientation pattern; one common event controlling all possible orientation tables is not required.
An exponential exception C exp(-cm), uniform in the same parameters, is more than sufficient.
The fine exponents a,L may depend arbitrarily on the fixed q,b,K,kappa,s0, but not on N,m or the actual offset.

The cutoff is fixed before K and the fine precision.
Comparable dimensions must use the same law xi_N, not a newly truncated law xi_m.
Uniformity over this family is part of the hypothesis; one-coordinate total-variation convergence alone does not prove a uniform m-coordinate matrix assertion.
Any needed stability of source controlled-moment or small-ball parameters must therefore be verified in the count supplying the interface.
The conditional mean of xi_N only changes deterministic centers in its linear forms and is not a reason to impose an unproved conditional independence of its real components.

<a id="generic-rank-conditional"></a>
## Conditional generic corank tails

Assume (Generic-linear-interface) for s0=0, for all required fixed parameters.
Then for raw Hermitian Wigner X_n with upper law xi and independent fixed real finite-second-moment diagonal law, every gamma,B>0 admits C,n0 such that
\[
 \sup_{\max|F_{jk}|\le n^\gamma}
 \mathbb P\{\operatorname{rank}(X_n+F)\le n-2\}
       \le Cn^{-B},\qquad n\ge n0.
 \tag{Generic-rank-conditional}
\]
The offset is complex and may be nonsymmetric.
This conclusion remains conditional on the stated linear hypothesis.

Choose kappa>(B+6)/2 and discard the event that any raw off-diagonal or diagonal variable has modulus greater than n^kappa.
Its probability is at most Cn^(2-2kappa)<=C_B n^(-B-4).
Conditional on the complement the unordered off-diagonal samples remain independent with the single law xi_n; fix the bounded diagonal values by conditioning.
Use one leading-principal chain M_k of this same physical matrix for floor(n/3)<=k<=n.
Because k>=n/4 eventually, a fixed entry exponent K, selected after gamma,kappa, works throughout the chain after a fixed exponent slack.
Apply the linear hypothesis to each current block and its transpose with q,b>B+5.

For a singular block D of size k choose Borel unit vectors u in ker D and v in ker D^T by the rank-stratified, lexicographically first maximal-minor construction of [C_F0194_v2](../claims/Yin_C_F0194_v2.md#border-rank).
The new raw border has row r^T and column d, with
\[
 r_j=\bar z_j+f_j,\qquad d_j=z_j+g_j,
\]
where z_j are independent xi_n/conjugate-xi_n variables, independent of D.
The actual orientation of the row is the opposite of the column orientation and is also included in the envelope.
Outside the linear exceptional event,
\[
 \mathbb P\{r^Tu=0\mid D\}\le k^{-b},\qquad
 \mathbb P\{v^Td=0\mid D\}\le k^{-b}.
\]
The two forms share the z_j; only their union bound is used.
When both are nonzero the deterministic bordered-rank calculation raises rank by two, independently of the exposed diagonal.
Thus the failure at one singular step is at most 2k^(-b)+Ck^(-q).
Union the at most n steps.
On the good event the deficiency d_k=k-rank M_k falls by one when positive and stays in {0,1} once it reaches that set.
Starting with deficiency at most floor(n/3), enough steps remain to end with corank at most one.
Adding Cn^(1-b)+Cn^(1-q) and the raw cutoff failure proves (Generic-rank-conditional).
The normalized version follows from sqrt(n)(W_n+F), with shift exponent at most gamma+1; rank is unchanged.

<a id="generic-second-conditional"></a>
## Conditional generic second-smallest floor without a gauge

Assume the linear interface for s0=1.
For every gamma,B>0 there is a finite A_2>0 for which
\[
 \sup_{\max|F_{jk}|\le n^\gamma}
 \mathbb P\{s_{n-1}(X_n+F)\le n^{-A_2}\}\le Cn^{-B}
 \tag{Generic-raw-second-conditional}
\]
in raw scaling, and the analogous assertion holds for W_n+F with another fixed exponent.
Here singular values are in decreasing order, so this is the second-smallest value.

Take kappa>(B+6)/2, condition on all independent raw cutoffs and then on the bounded diagonal values, and choose K after gamma,kappa to bound all entries of size-(n-1) principal blocks by (n-1)^K.
Use the linear interface at q,b>B+5 and its fixed precision a.
Let M=X_n+F and let B0 consist of its first n-1 rows.
For a retained row i delete coordinate i from it and from the other retained rows, obtaining z_i and C_i.
Then C_i is D_i=M[[n] minus {i}] with the row of original index n omitted.
The row z_i has only off-diagonal xi_n/conjugate-xi_n samples plus its deterministic shift and is independent of D_i; their mirrored partners were all in the deleted coordinate i.
There is no need to rotate z_i to a real row or to transform the other rows.

Choose a Borel bilinear unit normal u_i to C_i using rank strata, a lexicographically first maximal nonzero minor, the first free coordinate, and normalization.
At rank zero use a coordinate vector.
Then (D_i u_i)_j=0 on all but its one omitted row, exactly within the s0=1 interface.
Outside its D_i-measurable exceptional event, conditioning on D_i gives
\[
 \mathbb P\{|z_i u_i|\le n^{-a}\mid D_i\}
       \le(n-1)^{-b},
\]
because n^(-a)<=(n-1)^(-a) and the row's actual pattern is one allowed orientation assignment in the envelope.
The arbitrary complex offset is a center in that envelope.
For a bilinear normal u_i, the Hilbert-space normal is bar u_i and Cauchy--Schwarz yields
\[
 \operatorname{dist}(z_i,\operatorname{rowspan}C_i)\ge|z_i u_i|.
\]
Coordinate deletion is a contraction, so the same lower bound applies to the full retained row's distance from the other retained rows.
Its failure probability is at most (n-1)^(-b)+C(n-1)^(-q).
Union the n-1 retained rows.

On their good event B0 has full row rank, and its Gram inverse gives
\[
 \sum_{j=1}^{n-1}s_j(B0)^{-2}
    =\sum_{i=1}^{n-1}\operatorname{dist}((B0)_i,
                      \operatorname{rowspan}(B0)_{-i})^{-2}
    \le n^{2a+1}.
\]
Thus s_(n-1)(B0)>=n^(-a-1/2).
Adding the final row is a positive-semidefinite Gram perturbation, so s_(n-1)(M) has the same bound.
Choose A_2>a+1/2 and restore the cutoffs; q,b>B+5 give the claimed arbitrary-power error.
For normalized scaling, multiply W_n+F by sqrt(n), use raw shift exponent gamma+1, and divide singular values by sqrt(n).
The resulting statement applies to every actual principal minor by the comparable-dimension conversion and a probability margin for their union.

<a id="generic-isolated-conditional"></a>
## Conditional generic isolated-minor estimate with the correct conjugate forms

Assume the linear interface for s0=0.
For raw size n, fixed gamma,B>0 and arbitrary complex shift entries bounded by n^gamma, there are finite A_0,L_iso>0 for which the probability is at most C_B n^(-B) that some actual minor D_i has nonzero adjugate, the full ratio satisfies
\[
 |\det M|/\|\operatorname{adj}D_i\|_F\le n^{-A_0},
\]
and D_i is either exactly corank one or is invertible with
\[
 t_1(D_i)\le n^{-L_{\rm iso}},\qquad
 t_1(D_i)/t_2(D_i)\le n^{-L_{\rm iso}}.
 \tag{Generic-isolated-conditional}
\]
Here t_1<=t_2 are the two smallest values.

Choose kappa>(B+6)/2, then K bounding the diagonal, both shifted raw border norms and every entry on the independently truncated event.
Use q,b>B+5 in the linear interface, producing a_lin,L_ker uniformly for size m=n-1, D_i and D_i^T with the same law xi_n.
Choose a0>a_lin+1, set A_0=2a0, and then choose
\[
 L_{\rm iso}>\max\{L_{\rm ker}+1,\ 2a0+2K+3\}.
\]
All these exponents are fixed before the actual minor or border is exposed.

For clarity, the singular-vector directions can be checked explicitly over C.
For invertible D_i=U diag(t_1,...,t_m)V^*, set u=Ve_1 and v=bar Ue_1.
Then
\[
 D_i u=t_1Ue_1,\qquad D_i^Tv=t_1\bar Ve_1,
 \qquad
 \frac{\operatorname{adj}D_i}{\|\operatorname{adj}D_i\|_F}
       =\alpha uv^T+E,
\]
where
\[
 |\alpha|=\left(1+\sum_{j\ge2}(t_1/t_j)^2\right)^{-1/2}\ge1/2,
 \qquad \|E\|_F\le\sqrt m\,t_1/t_2,
 \qquad\rho_{D_i}\le t_1.
\]
The amplitude bound holds for sufficiently large n under the isolation hypothesis.
For exactly corank-one D_i, its normalized adjugate has exact rank one, take |alpha|=1,E=0, and u in ker D_i, v in ker D_i^T.
There is no assertion that the two singular vectors have overlapping coordinate mass or that a transpose-left vector equals a Hermitian left vector.

In the raw bordered determinant formula the rank-one contribution is
\[
 -\alpha\,[u^T(\bar z+f)]\,[v^T(z+g)],
 \tag{Generic-two-forms}
\]
where z has independent xi_n/conjugate-xi_n coordinates and f,g are arbitrary deterministic shifts.
The first form uses the opposite scalar orientation from the second, and both are covered by the full orientation envelope.
After division by the minor adjugate norm, its error is at most
\[
 n^K t_1+n^{2K}\sqrt m\,t_1/t_2
\]
in the invertible branch and zero in the exactly singular branch.
The choice of L_iso makes the error at most n^(-2a0-1) eventually.
Hence the tiny-full-ratio event forces at least one of the two factors in (Generic-two-forms) to have modulus at most 2n^(-a0).

Their vectors satisfy the right and transpose-right near-kernel conditions of the linear input, with residual at most n^(-L_iso), hence below m^(-L_ker).
Outside the minor's linear exceptional events, their conditional concentrations at radius 2n^(-a0)<=m^(-a_lin) are each at most m^(-b).
They use the same raw samples and may be strongly dependent; the union bound gives conditional probability at most 2m^(-b).
For each fixed minor this bound is uniform over every admissible singular-vector choice, so no random vector is being fixed before its matrix is exposed.
Equivalently a Borel SVD selection may be used.
Integrate the exceptional probability C m^(-q), union n indices, and restore the global cutoff event.
This proves the conditional isolated-minor estimate, with no quadratic inverse theorem and no independence assumption inside one entry.

<a id="generic-floor-conditional"></a>
## Full non-line in-probability floor conditional on the linear input

Assume (Generic-linear-interface) for the fixed non-line law xi, every required fixed cutoff exponent, s0=0,1, and all requested b,q,K.
Then for every gamma,B>0 there are fixed A,C_B,C,N0 such that, for the original normalized Hermitian model,
\[
 \sup_{\max|F_{jk}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}\,N^{-1/18},
       \qquad N\ge N0.
 \tag{Generic-floor-given-linear}
\]
This is a conditional theorem with the explicit linear hypothesis above, not an unconditional assertion that this hypothesis is established.
The offset is arbitrary deterministic complex and may vary with N; for an independent random offset the same estimate holds on its polynomial entry guard, adding the guard failure for an unconditional event.
Only within-size independence is used.
No summability, full-sequence almost-sure floor or original Task completion is claimed.

Here is the complete parameter order.
First choose the raw cutoff kappa>(B+6)/2 and a fixed norm exponent K>max{kappa+1/2,gamma+1}, enlarged to absorb constants.
The ordinary finite-second-moment cutoff gives P(||M||>N^K)<=C_B N^(-B-2), with M=W_N+F.
The conditional rank theorem at failure exponent B+2, applied to sqrt(N)M, makes rank M>=N-1 outside the same order of polynomial failure.
The reviewed [complex fixed-distance input](../claims/Yin_C_F0194_v6.md#complex-distance) and the deterministic [row-adjugate, rectangle and spread proof](../claims/Yin_C_F0194_v3.md#spread-and-average) therefore give the usable-index average for the remaining event.
This step uses the original untruncated centered law xi for its rectangular distance bound; the separate rank, second-value and isolated modules restore their own cutoff failures.

Apply the conditional second-value theorem to all raw actual principal minors sqrt(N)D_i, whose shifts are bounded by N^(gamma+1/2)<= (N-1)^(gamma+2) eventually.
Choose its failure exponent with margin for the N-minor union.
There is a fixed L_2>0 outside probability C_B N^(-B-1) on which t_2(D_i)>=N^(-L_2) for every i.
Choose A_0,L_iso from the conditional raw isolated-minor theorem with shift exponent gamma+1 and failure exponent B+2.
These are chosen before the fine full-adjugate graph threshold.

Now choose
\[
 T_0>L_{\rm iso}+L_2+2,\qquad
 J>K+T_0+1,\qquad
 H>\max\{J+K+1,\ K+T_0+2\},
\]
and put h_N=N^(-H),r_N=floor(sqrt(N)).
The full-adjugate low-matching proof holds simultaneously for all actual minors outside C exp(-cN), since r_N log(N)=o(N).
On the retained norm guard, a nonzero-adjugate low-matching minor has rho_Di<=N^(-T_0), hence t_1(D_i)<=sqrt(N-1)N^(-T_0).
If it is invertible, the raw isolation thresholds follow from
\[
 t_1(\sqrt N D_i)\le N^{-T_0+1},\qquad
 \frac{t_1(\sqrt N D_i)}{t_2(\sqrt N D_i)}
      \le N^{-T_0+1/2+L_2}\le N^{-L_{\rm iso}}
\]
eventually, and the first bound is also at most N^(-L_iso).
If it is singular with nonzero adjugate, it is exactly corank one and already lies in the singular isolated branch.
No symmetric-part floor, Riccati inversion or left-right support comparison enters this deduction.

Finally choose A>max{H+2K+2,A_0+2K+2,1} and epsilon_N=N^(-A).
The usable-index event G_i bounds the normalized full ratio by C_1N^(2K+1-A), which is within the full-adjugate matching radius c_*h_N/N eventually.
For the raw isolated-minor event its exact ratio is
\[
 \frac{|\det(\sqrt N M)|}
      {\|\operatorname{adj}(\sqrt N D_i)\|_F}
      =N\frac{|\det M|}{\|A_i\|_F}
      \le C_1N^{2K+2-A}\le N^{-A_0}
\]
eventually.
The factor is N, because the raw numerator has degree N and the raw minor adjugate has degree N-2.

Split the usable-index average into H_i^(full)(h_N,r_N) and its complement.
The high-matching contribution is at most C psi(r_N) by the new complete two-copy matching estimate, with no factor N.
On the norm, second-value and low-matching guards, every remaining G_i forces one of the conditional raw isolated-minor events.
The probability of the union of those events is at most C_B N^(-B-2), and their mean probability is no larger than this union bound.
Adding all rank, norm, second-value and low-matching failures yields
\[
 \mathbb P\{s_{\min}(M)\le N^{-A}\}
       \le C_BN^{-B}+C\psi(\lfloor\sqrt N\rfloor),
\]
which is (Generic-floor-given-linear).
All constants and all precision exponents are fixed after the laws and requested exponents, before N or the offset realization, and no independence between different dimensions was used.

Thus the precise remaining mathematical gap in this assembled non-line route is (Generic-linear-interface), including its orientation and truncation-family uniformity.
The full-adjugate matching, low-matching ratio, correct complex SVD forms and the conditional terminal deductions above require no additional scalar-independence or covariance hypothesis.
Any later unconditional candidate must actually supply that generic linear argument and its source interfaces; this conditional assembly does not promote the current source/count preparation to a proved input.

---
author: Yin
---
# Relative Fock degree bounds restore weighted canonical domains

Human author: Yin.
Root developed the suffix-cut L1 estimate, its dual actual-domain argument and the summable-coefficient theorem.
The general-branch author supplied the elementary Wick-word contraction formula and checked the cut maps and nonlinear application during development.
Neither developer is the independent reviewer of this candidate.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(s_0,s_1\) be standard free semicircular generators of a finite tracial von Neumann algebra \(M\), with \(H=L^2(M,\tau)\), \(\Omega=1\), and inner products linear in the second variable.
Write \(\mathcal A_0=\mathbb C\langle s_0,s_1\rangle\), \(\partial=\partial_1\), and use the Wick basis \(U_w\Omega=e_w\).
Let \(H_j\) be the closed span of words with exactly j letters 1, allowing arbitrarily many letters 0, and put
\[
 \mathcal K_{\le n}
   =\bigoplus_{j+k\le n}H_j\otimes_2H_k.
\]
For a Hilbert tensor \(\beta\), insertion means
\[
 I_\beta(a\otimes b)=a\cdot\beta\cdot b,
 \qquad
 \delta_\beta(p)=I_\beta\partial p,\qquad
 E_{\beta,0}p=(\mathrm{id}\otimes\tau)\delta_\beta(p)
 \quad(p\in\mathcal A_0).
 \tag{1}
\]
In \(N=M\bar\otimes M^{\mathrm{op}}\), this is \(\delta_\beta(p)=(\partial p)\beta\); the coefficients of the finite algebraic tensor \(\partial p\) act boundedly, so (1) is defined even if \(\beta\) is unbounded affiliated.

If \(\beta\in\mathcal K_{\le n}\), then its actual vacuum is
\[
 v_\beta=\partial^*(\beta^*),\qquad
 \|v_\beta\|_2\le\sqrt{n+1}\|\beta\|_2.
 \tag{2}
\]
The contraction is closable and its original closure and actual adjoint obey
\[
 M\Omega\subseteq
 \operatorname{Dom}\overline{E_{\beta,0}}
 \cap\operatorname{Dom}E_{\beta,0}^*,
 \tag{3}
\]
\[
 \|\overline{E_{\beta,0}}p\|_2
       \le2\sqrt{n+1}\|\beta\|_2\|p\|,\qquad
 \|E_{\beta,0}^*p\|_2
       \le\sqrt{n+1}\|\beta\|_2\|p\|
 \quad(p\in M).
 \tag{4}
\]
In addition the core map \(E_{\beta,0}\) has a bounded extension \(H\to L^1(M)\) of norm at most \(\sqrt{n+1}\|\beta\|_2\).
This is a different mapping assertion from boundedness on H.

The same conclusions hold if
\[
 \beta=\sum_{n\ge0}\beta_n,\qquad
 \beta_n\in\mathcal K_{\le n},\qquad
 W=\sum_{n\ge0}\sqrt{n+1}\|\beta_n\|_2<\infty.
 \tag{5}
\]
Then the constants in (2) and the adjoint estimate in (4) are W, and the first constant in (4) is 2W.
The vacuum in (2) is still the actual reference-adjoint value.

As an application, every nonlinear tuple from [C_F0144](Yin_C_F0144_v1.md#statement),
\[
 h=2+s_0,\quad S=c+s_1,\quad c>6,\quad
 Y=ShS+\mathrm i hSh,\quad X=(h,Y),
 \tag{6}
\]
satisfies \(\mathsf S(X)\), hence \(\mathsf F(X)\), as well as its already established \(\mathsf A(X)\).
Both specified target canonical operators
\[
 -\overline{(\mathrm{id}\otimes\tau)\theta_h},
 \qquad -\overline{(\mathrm{id}\otimes\tau)\delta_Y},
 \qquad
 \operatorname{Dom}\theta_h=\operatorname{Dom}\delta_Y
       =\mathbb C\langle h,Y,Y^*\rangle\Omega
 \tag{7}
\]
and their actual adjoints contain all \(M\Omega\).
Thus this concrete A-positive example with \(h^{-1}\notin L^2(M)\) is not an A-but-not-F counterexample.
No assertion for all bounded tuples or all Hilbert kernels is made.

## Argument

### 1. Inputs and the exact contraction problem

The prior kernel estimate [C_F0139](Yin_C_F0139_v1.md#statement) assumes coefficients in the kernel algebra of the differentiated reference coordinate.
It does not apply to the coefficients involving \(s_1\) here.
The actual reference-adjoint estimate and nonlinear inverse series are already fixed in [C_F0144, letter-count grading](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) and its following inverse-expansion section.
We reuse those precise statements, not an unproved full-domain conclusion from that Claim.

The [Miy22-U001 Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) fixes the word normalization and reversal.
Its source uses the other inner-product convention; the coordinate and trace formulas below use the convention stated here.
Local searches by suffix, relative degree, chaos and weighted contraction found no existing full-domain theorem at this scope.
A bounded external search for free difference quotients, finite chaos and free Malliavin contraction bounds did not verify an exact applicable theorem.
No outside stochastic-calculus theorem or novelty claim is used.
The new estimate below is a direct word-cut and Cauchy--Schwarz argument.

We use the finite right-coefficient identities from [C_F0130 Section 5](Yin_C_F0130_v1.md#5-projective-corrections-on-all-bounded-vectors) only for the finite h-coordinate correction in the application.
The coefficient beta need not be projective.
The actual canonical graph restoration is the bounded-core mechanism of [C_F0072](Yin_C_F0072_v1.md#statement), with its hypotheses verified below and the sharper adjoint bound proved directly.

### 2. A suffix cut gives an H-to-L1 estimate

For each \(k\ge0\) define a bounded map
\[
 C_k:H\longrightarrow H\otimes_2H_k
\]
on the orthonormal word basis as follows.
If a word has at least \(k+1\) letters 1, cut it at the unique letter 1 leaving exactly k such letters in the suffix:
\[
 C_ke_{u1v}=e_u\otimes e_v,\qquad
 \#_1(v)=k.
 \tag{8}
\]
Words with at most k letters 1 go to zero.
The map on the other basis vectors is injective into an orthonormal tensor basis, because the pair (u,v) reconstructs the word.
In fact it is onto that tensor basis.
In particular \(\|C_k\|\le1\), with no bound on the number of zeros.

First let beta be a finite tensor of Wick polynomials, and decompose it by the degree of its second leg:
\[
 \beta=\sum_k\beta^{(k)},\qquad
 \beta^{(k)}=\sum_{\#_1(v)=k}a_v\otimes U_v^*.
\]
For a polynomial q write
\[
 C_kq=\sum_{\#_1(v)=k}x_v\otimes U_v.
\]
Orthogonality and word reversal give
\[
 \sum_v\|a_v\|_2^2=\|\beta^{(k)}\|_2^2,\qquad
 \sum_v\|x_v\|_2^2=\|C_kq\|_2^2.
\]
The exact cut formula \(\partial U_w=\sum_{w=u1v}U_u\otimes U_v\) from C_F0144 now gives
\[
 E_{\beta^{(k)},0}q=\sum_vx_va_v.
 \tag{9}
\]
Indeed the trace in the second leg is \(\tau(U_v^*U_{v'})=\delta_{v,v'}\).
The product in (9) is the ordinary product of L2 vectors, taking values in L1; it is not a bounded multiplication map from the Hilbert tensor product into L2.

Noncommutative L2 Holder and scalar Cauchy--Schwarz give
\[
 \left\|\sum_vx_va_v\right\|_1
 \le\sum_v\|x_v\|_2\|a_v\|_2
 \le\|C_kq\|_2\|\beta^{(k)}\|_2
 \le\|q\|_2\|\beta^{(k)}\|_2.
 \tag{10}
\]
If the second leg of beta has degree at most n, summing over k and using orthogonality proves
\[
 \|E_{\beta,0}q\|_1
 \le\sqrt{n+1}\|\beta\|_2\|q\|_2.
 \tag{11}
\]

For general beta in that closed degree subspace, approximate it by finite Wick tensors without changing the degree bound.
For fixed polynomial q, insertion into its finite derivative and partial tracing are continuous from the beta Hilbert norm to H.
Thus the values converge in H and in L1 and (11) passes to the actual expression (1).
Polynomial density then extends that expression uniquely to a bounded map \(H\to L^1(M)\).
Alternatively, the series in (9) converge absolutely in L1 by (10).
These statements do not assert that the extension is H-valued at every H vector.

### 3. The actual adjoints and the reverse bound

Now take \(\beta\in\mathcal K_{\le n}\).
The involutions
\[
 \beta^*=\sum a^*\otimes b^*,\qquad
 \beta^\dagger=\sum b^*\otimes a^*
\]
extend isometrically to the Hilbert tensor product and preserve this total-degree subspace.
C_F0144's actual insertion-adjoint estimate therefore gives beta* in Dom partial* and (2).
Testing the finite expression (1) gives
\[
 \langle1,\delta_\beta p\rangle
   =\langle\beta^*,\partial p\rangle
   =\langle v_\beta,p\rangle
 \quad(p\in\mathcal A_0).
 \tag{12}
\]
This proves an actual vacuum, and the conjugate derivation is \(\delta_\beta^\#=\delta_{\beta^\dagger}\), with vacuum \(v_\beta^*\).

The Leibniz rule, tracial pairings and (12) give the actual core adjoint formula
\[
 E_{\beta,0}^*q=qv_\beta-E_{\beta^\dagger,0}q
 \quad(q\in\mathcal A_0).
 \tag{13}
\]
For clarity, expanding \(\delta_\beta(q^*p)\) identifies \(\langle q,E_{\beta,0}p\rangle\) with the pairing of p against the right side of (13).
Both terms on that side are H vectors for polynomial q.
Thus the core belongs to the actual adjoint domain, so E_beta,0 is closable.
The same argument works for beta-dagger.

There is a stronger domain conclusion directly from (11).
For every p in M and q in the original polynomial domain,
\[
 |\langle p,E_{\beta,0}q\rangle|
 \le\|p\|\|E_{\beta,0}q\|_1
 \le\sqrt{n+1}\|\beta\|_2\|p\|\|q\|_2.
\]
Riesz representation is exactly the actual Hilbert adjoint test.
Hence
\[
 M\subseteq\operatorname{Dom}E_{\beta,0}^*,\qquad
 \|E_{\beta,0}^*p\|_2
 \le\sqrt{n+1}\|\beta\|_2\|p\|.
 \tag{14}
\]
Apply (14) to beta-dagger.
Its core formula is \(E_{\beta^\dagger,0}^*p=pv_\beta^*-E_{\beta,0}p\).
Together with (2), this gives
\[
 \|E_{\beta,0}p\|_2
 \le2\sqrt{n+1}\|\beta\|_2\|p\|
 \quad(p\in\mathcal A_0).
 \tag{15}
\]
This argument uses the actual adjoint of the other contraction; it does not infer an H bound from the L1 bound (11).

The same estimate holds for E_beta-dagger, so both right and left contractions of delta_beta have operator-norm-to-H bounds.
The generic bounded-core graph argument of C_F0072 applies.
Explicitly, uniformly bounded polynomial approximants to any p in M converge strongly and in H to p.
Their images in (15) have a weakly convergent subnet; the weakly closed graph of the original Hilbert closure identifies its limit.
This puts p in that closure with (15)'s bound.
The actual adjoint inclusion (14) was proved separately.
Equations (3)-(4) follow for the original closure, not a chosen extension.

### 4. Summable relative-degree coefficients

Assume (5).
Hilbert convergence defines beta.
The actual reference-adjoint estimates give
\[
 \sum_n\|\partial^*(\beta_n^*)\|_2\le W,
\]
so beta* belongs to Dom partial* by closedness of that actual adjoint, with vacuum the sum.
The same applies to beta-dagger.

For each fixed polynomial p, the finite derivative in (1) makes insertion continuous in the Hilbert beta norm.
Thus the contraction values of partial sums converge in H to precisely E_beta,0 p.
Equations (11), (14) and (15), summed with their absolutely summable constants, pass to give respectively
\[
 \|E_{\beta,0}q\|_1\le W\|q\|_2,\quad
 \|E_{\beta,0}^*p\|_2\le W\|p\|,\quad
 \|E_{\beta,0}p\|_2\le2W\|p\|.
\]
For the middle assertion, one can either pass actual adjoint pairings or repeat the Riesz test using the first bound; no formal sum-adjoint equality is required.
The same core formula (13) and weakly closed-graph argument establish both original domains.
This proves the full summable theorem.

### 5. Application to the singular nonlinear free example

Use the exact coefficient notation in C_F0144:
\[
 G=h\otimes1+1\otimes h^{\mathrm{op}},\quad
 F=\partial_SY=(c+Z)G,\quad
 \|Z\|\le6,\quad g=\|G^{-1}\|_2<\infty,\quad r=6/c<1.
\]
Its inverse has the fixed expansion
\[
 \beta=F^{-1}=\sum_{n\ge0}\beta_n,\qquad
 \beta_n=c^{-n-1}G^{-1}(-Z)^n.
 \tag{16}
\]
Taking adjoints in C_F0144's degree argument proves \(\beta_n\in\mathcal K_{\le n}\) and
\[
 \|\beta_n\|_2\le(g/c)r^n,\qquad
 W\le(g/c)\sum_{n\ge0}\sqrt{n+1}\,r^n<\infty.
 \tag{17}
\]
Thus the operator \(K=\overline{E_{\beta,0}}\) has both bounded-vector domains.
Its core commutators are
\[
 [K,h]=0,\qquad [K,S]=\Theta(\beta),
 \tag{18}
\]
where \(\Theta(a\otimes b)(p)=a\tau(bp)\) is the Hilbert-tensor/Hilbert--Schmidt identification.
These are identities on the polynomial core first, obtained from (1) and the Leibniz rule.

They pass to all M.
Choose bounded polynomial approximants for p and use the bounded commutator on the right together with weak graph limits for p and the bounded-generator products.
The graph limits are the already defined values of K at those bounded vectors.
This proves (18) on M without assuming operator-norm density of the polynomial algebra or Hilbert-space boundedness of K.

The polynomial product rule in (18), followed by the exact affiliated coefficient identities of C_F0142, gives
\[
 [K,Y]=\Theta(F\beta)=P,\qquad
 [K,Y^*]=\Theta((F-2\mathrm i h\otimes h^{\mathrm{op}})\beta)
        =\Theta(k)
 \quad\text{on }M.
 \tag{19}
\]
The products are actual Hilbert tensors because beta is L2 and the left factors are bounded; \(F\beta=1\) and the unitary k are the fixed C_F0142 identities.

Let \(B_h=r_0^*\) be right annihilation in the Fock model.
Direct word deletion gives \([B_h,h]=P,[B_h,S]=0\); it and its adjoint are bounded on H.
Put
\[
 C=\partial_hY=\sum_\ell a_\ell\otimes b_\ell,\qquad
 L=B_h-\sum_\ell\rho(a_\ell)K\rho(b_\ell).
 \tag{20}
\]
This is an operator on domain M.
Both its own values and its actual adjoint values at every q in M exist: the finite correction-adjoint expression is \(\sum_\ell\rho(b_\ell^*)K^*\rho(a_\ell^*)q\).
Direct pairing proves actual adjoint membership.
Both maps have operator-norm-to-H bounds by (4) and boundedness of the finite coefficients.

The exact finite coefficient identities of C_F0130 Section 5 give
\[
 [L,h]=P,\quad [L,Y]=0,\quad
 [L,Y^*]=\Theta(C_- -kC)
 \quad\text{on }M,
 \tag{21}
\]
with \(C_-=\partial_hY^*\) as in C_F0142.
Here the order kC is the right-coefficient order, not Ck.
Consequently \(-L,-K\), restricted to M, already supply the existential generator-first strong system.

It remains to identify the specified target canonical closures.
On \(\mathcal A_X=\mathbb C\langle h,Y,Y^*\rangle\), the commutators in (19)-(21) and the Leibniz rule identify exactly the two target derivations of C_F0142.
Evaluating at 1 gives
\[
 (\mathrm{id}\otimes\tau)\delta_Y(p)=Kp,\qquad
 (\mathrm{id}\otimes\tau)\theta_h(p)=Lp-pL1,
 \tag{22}
\]
since K1=0.
Right multiplication \(p\mapsto pL1\) has actual adjoint \(q\mapsto q(L1)^*\) on all M, with both operator-norm-to-H bounds.
Thus the two domain-M maps in (22) have both actual bounded-vector domains and bounds.

Their target-core restrictions are precisely the unclosed canonical contractions.
The target algebra generates M by C_F0142.
Bounded Kaplansky approximants from that target core, the established bounds and weak closed graphs therefore place M in each original target-core closure.
Their actual adjoints already contain M by the domain-M pairing.
Negation gives (7) with \([X_j,D_i]=\delta_{ij}P\).
No equality of unrelated larger closed domains is inferred.

## Scope

The result relies on summability in the relative Fock grading of a free semicircular reference.
An arbitrary Hilbert coefficient need not satisfy (5), and a general ACSY tuple need not admit this representation.
The concrete nonlinear example now has all three conditions; it does not decide the general A-to-F implication.
The full normal comparison is also unaffected.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:07 |
| status | open |
| reason | Complete suffix-cut L1 and actual-adjoint argument restores both canonical domains for summable relative-degree kernels and the concrete singular nonlinear ACSY example; independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite and summable relative-degree contraction estimates, actual original domains, and both target canonical domains for the nonlinear free tuple. |
| argument | [Argument](#argument) | Five sections: exact suffix cuts and L1 estimate, actual adjoints and reverse bound, summation, full-M commutators and target-core identification. |
| dependency | [Relative grading and inverse expansion](Yin_C_F0144_v1.md#argument) | Exact word-cut and actual reference-adjoint bounds, reducing degree spaces, and the concrete beta series/integrability. Its text supplies no full-domain conclusion being presumed. |
| dependency | [Free Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Word basis, reversal, standard semicircular normalization and bounded right creation/annihilation for B_h. |
| dependency | [Two-contraction graph mechanism](Yin_C_F0072_v1.md#statement) | The actual core-adjoint and bounded Kaplansky weak-graph mechanism, after both contraction estimates and the sharper direct adjoint bound are proved here. |
| dependency | [Nonlinear target identities](Yin_C_F0142_v1.md#statement) | Exact represented target derivations, generation, F inverse, starred k and C_- minus kC identities; no all-bare-witness uniqueness is imported. |
| dependency | [Finite coefficient implementation](Yin_C_F0130_v1.md#5-projective-corrections-on-all-bounded-vectors) | Only finite Q_C corrections on B(M,H), reversed composition order and commutator identities; beta itself is not assumed projective. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:18 |
| status | proved |
| reason | The complete fixed argument and all five direct dependency scopes passed the independent review R_F0152. This adopts the relative Fock degree estimates and both specified target canonical domains for the displayed nonlinear free tuple; no unrestricted implication is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite and summable relative-degree contraction estimates, actual original domains, and both target canonical domains for the nonlinear free tuple. |
| argument | [Argument](#argument) | Five sections: exact suffix cuts and L1 estimate, actual adjoints and reverse bound, summation, full-M commutators and target-core identification. |
| dependency | [Relative grading and inverse expansion](Yin_C_F0144_v1.md#argument) | Exact word-cut and actual reference-adjoint bounds, reducing degree spaces, and the concrete beta series/integrability. Its text supplies no full-domain conclusion being presumed. |
| dependency | [Free Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Word basis, reversal, standard semicircular normalization and bounded right creation/annihilation for B_h. |
| dependency | [Two-contraction graph mechanism](Yin_C_F0072_v1.md#statement) | The actual core-adjoint and bounded Kaplansky weak-graph mechanism, after both contraction estimates and the sharper direct adjoint bound are proved here. |
| dependency | [Nonlinear target identities](Yin_C_F0142_v1.md#statement) | Exact represented target derivations, generation, F inverse, starred k and C_- minus kC identities; no all-bare-witness uniqueness is imported. |
| dependency | [Finite coefficient implementation](Yin_C_F0130_v1.md#5-projective-corrections-on-all-bounded-vectors) | Only finite Q_C corrections on B(M,H), reversed composition order and commutator identities; beta itself is not assumed projective. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0152_v1.md#conclusion) | Entire statement, five proof sections and all five direct dependency scopes; reviewer disclosed prior development of C_F0072 but did not develop this result. |


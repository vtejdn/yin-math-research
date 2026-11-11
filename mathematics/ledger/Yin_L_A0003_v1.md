---
author: Yin
---
# An actual index-two crossed product and rational norm descent

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route four](../strategies/Yin_S_A0004.md) and its [finite-extension probe](../strategies/Yin_S_A0001.md).
The main research agent and two development helpers derived and checked the explicit specializations below for Yin.
The finite-extension closure theorem and the positive group-class coverage are established source results, not new project theorems.
The purpose is to complete the requested actual-realization and norm-equation test, including a case where the simplest parity valuation cannot work.
The [independent whole-argument finding](../audits/reviews/Yin_R_A0005_v1.md#whole-argument-finding) covers the complete mathematical argument, accepted-input scope and appended candidate screening.

## Results and source scope

For \(H\triangleleft G\) of index two with \(D_{\mathbb C}(H)\) a division ring, the actual crossed product is faithfully embedded in \(\mathcal U(G)\) and equals both the division and rational closures of \(\mathbb CG\).
It is a division ring exactly when the equation \(\alpha(b)b=h\) has no solution in \(D_{\mathbb C}(H)\).
A hypothetical solution gives scalar affiliated rank \(1/2\) and an explicit finite group-ring matrix construction with kernel dimension \(1/2\).
These conclusions require no prior Atiyah assumption for \(G\).

The selected concrete extension is
\[
G=\langle x,y,z\mid x^2y^2z^2=1\rangle,\qquad
H=\ker(w:G\longrightarrow C_2),\quad w(x)=w(y)=w(z)=1.
\]
An explicit free-by-cyclic realization proves torsion-freeness and shows that both groups are already covered by Linnell's class \(\mathcal C\).
The character \(w\) does not lift to an integer-valued homomorphism, and no \(\alpha\)-invariant integer valuation can give \(h=z^2\) odd value.
Nevertheless a different cyclic quotient produces a leading-coefficient constraint on every rational norm solution, reducing it to an impossible norm equation in an actual free-group division ring.
This supplies a complete calibration, not new group-class coverage.

The source inputs are [Lin93, Lemma 2.1, Lemmas 4.1--4.3 and Theorems 1.3 and 1.5](../audits/literature/Lin93/Yin_U001.md#routine-lemmas-and-induction), with the [free-group input](../audits/literature/Lin93/Yin_U001.md#free-group-proof) and its recorded foundations.
The matrix-inverse description of rational closure is [Lin06, Section 3, published pp. 45--47](../audits/literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures).
The general equivalence with the Task is [MSY23, Theorem 5.25](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence).
The subgroup and Artinian-closure arguments below reconstruct their requested index-two interfaces explicitly.
The norm factorization, the presentation calculation and the residue calculation are direct specializations; no priority claim is made for them.
The accepted analytic foundations are the finite affiliated algebra, bounded Ore denominators, polar decomposition and invariance of affiliated rank under invertible row and column operations, at the scope recorded in the Lin93 audit.
No arbitrary unbounded product below is interpreted as an everywhere-defined pointwise operator.

## Actual affiliated embedding

Write \(D=D_{\mathbb C}(H)=\operatorname{Div}_{\mathcal U(H)}(\mathbb CH)\) and assume it is a division ring.
Choose \(t\in G\setminus H\), set \(h=t^2\in H\), and put \(\alpha(d)=tdt^{-1}\).
Conjugation preserves \(\mathbb CH\), its affiliated ambient ring and its division closure, so \(\alpha\) is an automorphism of \(D\), \(\alpha(h)=h\), and \(\alpha^2=\operatorname{Ad}_h\).

The inclusion \(\mathcal U(H)\subseteq\mathcal U(G)\) is the extension of the normal subgroup inclusion of von Neumann algebras.
On the orthogonal right-coset decomposition \(\ell^2(G)=\bigoplus_{Hg}\ell^2(Hg)\), an element of \(\mathcal U(H)\) is the direct sum of its affiliated operator on each copy of \(\ell^2(H)\).
Its kernel projection is the corresponding direct sum; hence invertibility in \(\mathcal U(H)\) is equivalent to invertibility of its image in \(\mathcal U(G)\).
Its inverse, when it exists, has the same direct-sum description.
This also proves compatibility of subgroup division closures with the actual embeddings.

Define
\[
A=D+Dt\subseteq\mathcal U(G).
\]
The relations \(td=\alpha(d)t\) and \(t^2=h\) show that this is a unital subring.
It remains necessary to check that the displayed sum is direct in the actual ambient ring.
Given \(a+ct=0\), choose a common bounded left denominator \(q\in\mathcal N(H)\), invertible in \(\mathcal U(H)\), such that \(qa,qc\in\mathcal N(H)\).
Such a denominator exists by the bounded Ore fraction description of \(\mathcal U(H)\).
The bounded identity \(qa+(qc)t=0\), applied to \(\delta_e\), has its two summands in the orthogonal spaces \(\ell^2(H)\) and \(\ell^2(Ht)\).
Thus \(qa\delta_e=0\) and \(qc\delta_t=0\).
The first equality gives \(qa=0\) because \(\delta_e\) is separating for \(\mathcal N(H)\).
The second gives \(qc=0\) by the same fact on the right-coset copy, using that left convolution commutes with right translation.
Multiplying by \(q^{-1}\) proves \(a=c=0\).
Consequently \(A=D\oplus Dt\) is the faithful crossed product, with dimension two over \(D\) on either side.
The same bounded-denominator proof works for any finite set of distinct cosets, and will also justify the Laurent ring used below.

For an explicit matrix model, use the unitary
\[
V:\ell^2(H)\oplus\ell^2(H)\longrightarrow\ell^2(G),\qquad
V(\xi,\eta)=\xi+t\eta.
\]
Conjugation by \(V\) identifies the normal inclusion and its affiliated extension with
\[
\rho(d)=
\begin{pmatrix}d&0\\0&\alpha^{-1}(d)\end{pmatrix},\qquad
\rho(t)=
\begin{pmatrix}0&h\\1&0\end{pmatrix},
\]
and therefore
\[
\rho(a+ct)=
\begin{pmatrix}a&ch\\ \alpha^{-1}(c)&\alpha^{-1}(a)\end{pmatrix}.
\]
These are identities in \(M_2(\mathcal U(H))\), obtained by extending the bounded representation; they do not prescribe a common pointwise domain for arbitrary unbounded entries.
For bounded \(T\in\mathcal N(G)\), the two diagonal coefficients have traces \(\tau_G(T)\) and \(\tau_G(t^{-1}Tt)=\tau_G(T)\).
Hence
\[
(\operatorname{Tr}_2\otimes\tau_H)(\rho(T))=2\tau_G(T).
\]
The normal representation preserves kernel and support projections, so the same factor of two applies to affiliated ranks.

## Division and rational closure comparison

Put \(D_G=\operatorname{Div}_{\mathcal U(G)}(\mathbb CG)\) and \(R_G=\operatorname{Rat}_{\mathcal U(G)}(\mathbb CG)\).
Every scalar inverse used to generate \(D\) is also an allowed inverse in \(\mathcal U(G)\).
Thus \(D\subseteq D_G\), and \(t\in\mathbb CG\) gives \(A\subseteq D_G\).

Conversely, for every \(n\geq1\), \(M_n(A)\) is a finite-dimensional right \(D\)-vector space.
If \(X\in M_n(A)\) is invertible in \(M_n(\mathcal U(G))\), left multiplication by \(X\) on \(M_n(A)\) is injective and right \(D\)-linear.
Finite dimension makes this map surjective, so \(XY=I_n\) for some \(Y\in M_n(A)\).
In the ambient ring \(Y=X^{-1}\).
Thus \(A\) is closed under all ambient matrix inverses, even when \(A\) is not a division ring.
It contains \(\mathbb CG\), so \(D_G\subseteq R_G\subseteq A\).
Combining the inclusions gives
\[
\boxed{D_G=R_G=A=D\oplus Dt.}
\]
This is the index-two instance of the Artinian finite-extension closure argument in Lin93.
No integrality for \(G\), semisimplicity assertion, scalar Ore condition on \(\mathbb CG\), or abstract-to-analytic identification is being assumed.

## Complete norm criterion and the half-rank witness

For \(b\in D\), set
\[
\Delta_b=h-b\alpha^{-1}(b),\qquad
\delta_b=h-\alpha(b)b=\alpha(\Delta_b).
\]
Direct multiplication gives both identities
\[
(t+b)(t-\alpha^{-1}(b))=\Delta_b,\qquad
(t-\alpha(b))(t+b)=\delta_b.
\]
If \(\delta_b\ne0\), both right sides are units in \(D\), and the resulting right and left inverses agree:
\[
(t+b)^{-1}
 =(t-\alpha^{-1}(b))\Delta_b^{-1}
 =\delta_b^{-1}(t-\alpha(b)).
\]
If \(\delta_b=0\), then \(\Delta_b=0\), and the two displayed factors annihilating \(t+b\) are nonzero by coset independence.
Thus \(t+b\) is not a unit and is a nonzero zero divisor in the actual affiliated ring.

Every nonzero \(a+ct\) with \(c=0\) is already a unit of \(D\).
For \(c\ne0\), write \(a+ct=c(t+b)\), where \(b=c^{-1}a\).
The preceding alternatives prove the full equivalence
\[
\boxed{A\text{ is a division ring}
\quad\Longleftrightarrow\quad
\nexists\,b\in D:\alpha(b)b=h.}
\]
Together with the closure comparison and the fixed-ambient Atiyah equivalence, this is also equivalent to the complex-coefficient Atiyah conclusion for \(G\).
If \(b\in H\), the norm equation yields \((b^{-1}t)^2=1\), with \(b^{-1}t\notin H\); torsion-freeness rules out these group-element solutions.
That argument alone says nothing about the remaining \(b\in D\).

For a hypothetical rational solution \(b\), necessarily \(b\ne0\), and
\[
\rho(t+b)=
\begin{pmatrix}b&h\\1&\alpha^{-1}(b)\end{pmatrix}
=
\begin{pmatrix}b\\1\end{pmatrix}
\begin{pmatrix}1&\alpha^{-1}(b)\end{pmatrix}.
\]
The equality uses \(\Delta_b=0\).
Invertible row and column operations over \(D\) reduce this matrix to \(\operatorname{diag}(1,0)\).
They remain invertible over \(\mathcal U(H)\); the trace comparison therefore gives
\[
\operatorname{rank}_G(t+b)=\tfrac12,\qquad
\dim_G\ker(t+b)=\tfrac12.
\]
This avoids identifying a possibly unbounded graph on an unjustified Hilbert-space domain.

The half-rank witness can be transferred to a finite matrix over \(\mathbb CG\).
Since \(b\in D\subseteq R_H\), the matrix-inverse description of rational closure supplies some \(Q\in M_n(\mathbb CH)\), invertible in \(M_n(\mathcal U(H))\), and indices \(i,j\) with \(b=e_i^TQ^{-1}e_j\).
The actual subgroup embedding preserves that invertibility.
Then
\[
\mathcal B=
\begin{pmatrix}
t&e_i^T\\
-e_j&Q
\end{pmatrix}
\in M_{n+1}(\mathbb CG)
\]
has Schur complement \(t+b\), so
\[
\operatorname{rank}_G(\mathcal B)=n+\tfrac12,\qquad
\dim_G\ker\mathcal B=\tfrac12.
\]
This is a conditional extraction formula, not an exhibited counterexample: no such \(b\) has been found, and the chosen example below excludes all of them.

## Concrete group and existing coverage

Take \(G=\langle x,y,z\mid x^2y^2z^2=1\rangle\) and the index-two kernel \(H=\ker w\) specified above.
The relation has even parity, so \(w\) is well defined and onto.
Set \(a=xy\).
The presentation becomes
\[
G=\langle x,a,z\mid xax^{-1}az^2=1\rangle.
\]
Let \(F\) be the free group on \(a\) and \(z_i\), \(i\in\mathbb Z\).
Define
\[
\beta(a)=z_0^{-2}a^{-1},\qquad \beta(z_i)=z_{i+1}.
\]
The assignments
\[
\gamma(a)=a^{-1}z_{-1}^{-2},\qquad \gamma(z_i)=z_{i-1}
\]
satisfy \(\beta\gamma=\gamma\beta=\mathrm{id}\) on every free generator.
Thus \(\beta\) is an automorphism.
In \(F\rtimes_\beta\langle x\rangle\), eliminate the generators \(z_i=x^iz_0x^{-i}\); the sole remaining conjugation relation is \(xax^{-1}=z_0^{-2}a^{-1}\).
This is exactly the displayed presentation of \(G\), with inverse substitution \(y=x^{-1}a\).
Consequently the homomorphism
\[
\psi:G\longrightarrow\mathbb Z,\qquad
\psi(x)=1,\quad\psi(y)=-1,\quad\psi(z)=0
\]
has free kernel \(K=F\).
A finite-order element has trivial image in \(\mathbb Z\) and then lies in the torsion-free free group \(F\), proving that \(G\) is torsion-free.

Let \(L=K\cap H\).
Since \(z\in K\) has odd \(w\)-value, \(L\) has index two in \(K\) and is free by the subgroup theorem for free groups.
The element \(s=xz\in H\) has \(\psi(s)=1\), so \(\psi|_H\) is onto and
\[
H=L\rtimes\langle s\rangle.
\]
Thus \(G\) and \(H\) are free-by-infinite-cyclic, and \(K,L\) are free.
Lin93 Theorem 1.3 already gives the actual division closures for \(G\) and \(H\), and the free-group theorem gives them for \(K,L\).
Equivalently these are torsion-free members of \(\mathcal C\); the same coverage is recorded in [LL18 Theorem 2.3(3)--(4), arXiv v3 p.10](https://arxiv.org/pdf/1602.06906v3#page=10).
No original proof of the Task for this group is claimed.
More generally, because \(\mathcal C\) is closed under elementary amenable quotients, a torsion-free finite extension of any \(H\in\mathcal C\) is already covered.
Thus selecting such an \(H\) can test a mechanism but cannot by itself establish new coverage.

For the actual index-two extension choose \(t=z\), \(h=z^2\), and \(\alpha=\operatorname{Ad}_z\) on \(D(H)\).
These specify the extension and its twisting without choosing a surface-group normal form.
The preceding algebraic construction, rather than an uninspected surface-classification assertion, verifies every group property needed below.

## Why an invariant parity valuation cannot settle this example

There is no homomorphism \(\chi:G\to\mathbb Z\) whose reduction modulo two is \(w\).
Indeed \(\chi(x),\chi(y),\chi(z)\) would all be odd, whereas the relator forces
\[
\chi(x)+\chi(y)+\chi(z)=0.
\]
An odd sum of three odd integers cannot be zero.

This also excludes the usual proposed valuation obstruction on the full rational division ring.
Suppose \(\nu:D(H)^\times\to\mathbb Z\) is a multiplicative-group homomorphism invariant under \(\alpha\).
Its restriction to \(H\) is a group homomorphism invariant under conjugation by \(z\).
If \(\nu(h)\) were odd, define \(\chi(u)=2\nu(u)\) for \(u\in H\), and \(\chi(z)=\nu(h)\).
The relations \(zuz^{-1}=\alpha(u)\) and \(z^2=h\) show that this defines a homomorphism \(G\to\mathbb Z\).
Its reduction modulo two is \(w\), a contradiction.
Therefore every such \(\nu\), including every invariant integer-valued division-ring valuation, satisfies \(\nu(h)\in2\mathbb Z\).
The argument does not exclude valuations with additional residue information or valuations not invariant under \(\alpha\).

## A leading-coefficient constraint on every rational solution

Use the different cyclic quotient \(\psi\) above, and put \(E=D_{\mathbb C}(L)\).
For this part the positive inputs are only that \(D(H)\), \(D(K)\) and \(E\) are actual division rings; the already-known division property of \(D(G)\) is not used.
Conjugation by \(s=xz\) induces an automorphism \(\sigma\) of \(E\).
The ring generated by \(E\) and \(s\) in \(\mathcal U(H)\) is faithfully the skew Laurent polynomial ring
\[
B=E[s,s^{-1};\sigma],\qquad se=\sigma(e)s.
\]
Faithfulness follows by the same common-denominator and distinct-coset argument as before.
It is a domain and has its ordinary skew fraction division ring \(Q(B)\), by the left and right Euclidean algorithms for skew polynomials over a division ring.
Since \(D(H)\) is a division ring, the actual embedding of \(B\) extends to an embedding of \(Q(B)\) in \(D(H)\).
Conversely \(Q(B)\) contains \(\mathbb CH\) and is a division subring of \(\mathcal U(H)\), so minimality of the actual division closure gives
\[
D(H)=Q(B).
\]
This is the division-ring specialization of the skew Laurent localization used in Lin93 Lemma 4.3.

Embed \(Q(B)\) in the formal skew Laurent series division ring \(E((s;\sigma))\).
An element is a series \(\sum_{j\geq m}e_js^j\), with \(m\in\mathbb Z\); multiplication uses \(s^je=\sigma^j(e)s^j\).
For each fixed exponent the convolution has finitely many terms.
A nonzero series is a nonzero leading monomial times \(1+u\) with strictly positive lowest degree, and the geometric series for \((1+u)^{-1}\) is well defined coefficient by coefficient.
This proves it is a division ring and that the embedding extends from \(B\) to \(Q(B)\).
The resulting valuation \(v\) is the lowest exponent, with \(v(pq)=v(p)+v(q)\).
On the valuation ring \(v\geq0\), taking the coefficient of \(s^0\) is a ring homomorphism onto \(E\), and it is nonzero on elements of value zero.
These are formal series calculations, with no assertion of norm convergence in a Hilbert space.

Conjugation by \(z\) preserves \(L\) and hence \(E\); denote its restriction by \(\theta\).
Also
\[
\alpha(s)=zs z^{-1}=u s,\qquad
u=zs z^{-1}s^{-1}\in L.
\]
The membership \(u\in L\) follows from \(\psi(u)=0\) and \(w(u)=0\).
Thus \(\alpha\) preserves the Laurent degree, sends every nonzero leading coefficient to a nonzero coefficient in the same degree, and extends to a degree-preserving automorphism of the formal series division ring.
For negative powers this follows by expanding the inverse monomial, which still has a single exponent.
The covariance with \(\sigma\) follows from the actual relation \(se=\sigma(e)s\); substitution therefore respects multiplication.
It agrees with actual conjugation on \(D(H)=Q(B)\), since both maps agree on \(E\) and \(s\).
On the residue division ring of this valuation, its induced map is exactly \(\theta\).

Suppose \(b\in D(H)\) satisfies \(\alpha(b)b=h=z^2\).
Since \(h\in L\subset E^\times\), its value is zero, while \(v(\alpha(b))=v(b)\).
It follows that \(2v(b)=0\), so \(v(b)=0\).
Write the formal expansion
\[
b=c+\sum_{j>0}c_js^j,\qquad c\in E^\times.
\]
Taking the coefficient of degree zero in the norm equation gives the additional necessary condition
\[
\boxed{\theta(c)c=z^2,\qquad c\in D_{\mathbb C}(L)^\times.}
\]
This constraint applies to arbitrary rational complexity, not merely Laurent polynomials or expressions of bounded depth.

The residue equation is impossible.
The inclusions \(L\triangleleft K\), \([K:L]=2\), \(z\in K\setminus L\), and the actual subgroup embeddings put
\[
E\oplus Ez\subseteq D_{\mathbb C}(K).
\]
Coset independence makes \(z-\theta(c)\) and \(z+c\) nonzero.
But the residue equation gives
\[
(z-\theta(c))(z+c)=z^2-\theta(c)c=0,
\]
contradicting the known actual division-ring property for the free group \(K\).
Hence no rational solution \(b\in D(H)\) exists.
The complete criterion proves \(A=D(H)\oplus D(H)z\) is a division ring, and the closure comparison identifies it with both actual closures of \(\mathbb CG\).

## Consequences and remaining research boundary

The first finite-extension probe now has a complete actual-ambient realization, matrix-level closure comparison, necessary-and-sufficient norm criterion and conditional finite-matrix obstruction.
For the selected example the rational norm equation has been excluded for every rational element by a justified residue reduction.
The absence of a lift of \(w\) shows why the first parity test fails, while the independent quotient \(\psi\) supplies the extra structure that succeeds.

This uses the established free-by-cyclic setting and the familiar skew Laurent mechanism; it is not a new permanence theorem or a reduction of all torsion-free groups to this case.
The finite-extension criterion alone leaves the full difficulty in excluding rational norm solutions.
The residue mechanism requires an actual cyclic decomposition and known division of its coefficient and residual subgroup closures.
Torsion-freeness by itself supplies neither that quotient nor the required residual division input.
Further investment aimed at new coverage must first select an \(H\) and extension outside already applicable finite-extension results, or find a different actual-rational invariant when this cyclic reduction is unavailable.
Repeating the same argument for more free-by-cyclic or virtually abelian examples would provide additional calibration only.

## Retained candidate beyond the ambient cyclic-quotient test

A possible later calibration is the Promislow group
\[
P=\langle a,b\mid b^{-1}a^2b=a^{-2},\ a^{-1}b^2a=b^{-2}\rangle.
\]
[Gar21, arXiv v4, Section 3.1, pp. 4--5](../literature/pdf/Gar21--arxiv-v4.pdf#page=4) explicitly derives torsion-freeness and the normal subgroup
\(N=\langle X=a^2,Y=b^2,Z=(ab)^2\rangle\cong\mathbb Z^3\), with quotient \(C_2^2\), action and cocycle.
Only these passages and the bibliographic identity were inspected; the paper's unit-conjecture construction is not an input to this investigation.
Its normal forms and action give, for \(\omega(a)=1,\omega(b)=0\),
\[
H_P=\ker\omega=\langle X,Z,b\rangle
 \cong\mathbb Z^2\rtimes_{-I}\mathbb Z.
\]
For the representative \(t=a\), the twisting data are
\[
h=X,\qquad
\alpha(X)=X,\quad\alpha(Z)=Z^{-1},\quad\alpha(b)=XZb^{-1}.
\]
The last equality follows from \(Z=abab\) and \(b^{-1}X^{-1}=Xb^{-1}\).
The defining relators abelianize to \(4a=4b=0\) with no further relation, so \(P_{\mathrm{ab}}\cong C_4\oplus C_4\).
Consequently \(P\) has no nonzero homomorphism to \(\mathbb Z\).
This prevents direct reuse of the selected example's ambient cyclic quotient, while \(\alpha\) reverses the Laurent degree of \(b\) in \(H_P\).
Both \(P\) and \(H_P\) are virtually abelian and already in \(\mathcal C\).
The rational norm analysis for this second pair is not carried out here; its value would be testing a mechanism without an ambient cyclic quotient, not obtaining a new positive group class.

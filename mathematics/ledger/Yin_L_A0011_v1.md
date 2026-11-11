---
author: Yin
---
# Noncyclic path addition under Schur elimination: two certificates and their limits

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation for [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) seeks a preserved structure that controls noncyclic path addition and certifies the next scalar pivot before its inverse is used.
One complete sufficient class preserves a semidefinite real part and a positive injective imaginary compression on its specified zero coordinates.
Its explicit noncommuting group-ring example escapes the earlier original-pencil full-rank real-part and cyclic Laurent gauge conditions.
A second inverse-difference identity certifies a noncommutative two-path Schur sum from six independently known difference units.
With central column parameters it preserves a shape under rational conjugation, but a concrete torsion-free collision shows that the remaining row-separation condition needs separate control.
When the row labels lie in one component over an independently known division coefficient ring normalized by a known unit, that control is preserved and gives a complete conditional induction with row mergers.
A finite-tracial comparison isolates why individual Haar laws and an abstract torsion-free generated group do not replace the joint regular trace.
These are explicit refinements and applications of known energy, Schur, cyclic and spectral mechanisms, with no historical-novelty claim or new positive Atiyah group class.
All products are closed products in the actual finite affiliated algebra, and all matrix ranks use unnormalized matrix traces.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0013_v1.md#whole-artifact-finding) covers the complete investigation, including the conditional normalized-coefficient induction, with the exact source and foundational limits retained in that review.

## A pair of conditions preserved by scalar elimination

Let \(M\) be a finite von Neumann algebra with a faithful normal tracial state, let \(U=\mathcal U(M)\), and let \(R\subset U\) be the actual rational closure of a unital star subalgebra.
Use unnormalized matrix traces and the corresponding affiliated ranks.
Suppose \(L=H+iK\in M_n(R)\), with \(H=H^*\), \(K=K^*\), and a specified coordinate decomposition
\[
H=\operatorname{diag}(0_r,H_+),
\quad H_+\ge0,
\quad \operatorname{rk}H_+=n-r,
\quad K_{00}\ge0,
\quad \operatorname{rk}K_{00}=r,
\tag{D1}
\]
where \(K_{00}\) is the leading \(r\)-square compression of \(K\).
The principal case is \(0<r<n\); \(r=0\) is the already retained injective-real-part class, while \(r=n\) is an injective positive imaginary part.
All inequalities are inequalities of actual selfadjoint affiliated operators.
No spectral gap, commutation between entries, or Atiyah hypothesis is assumed.
The zero block of \(H\) is given explicitly; the criterion does not assume an arbitrary kernel projection can be put into this coordinate form by an already available rational unit.

For \(r>0\), separate the first coordinate and write
\[
K=\begin{pmatrix}k&b\\b^*&K_1\end{pmatrix},
\qquad
H=\begin{pmatrix}0&0\\0&H_1\end{pmatrix},
\qquad
H_1=\operatorname{diag}(0_{r-1},H_+).
\]
The scalar \(k\) is positive and has rank one before the Schur complement is formed.
Indeed, \(K_{00}^{1/2}\) is an actual unit and
\[
k=(K_{00}^{1/2}e_1)^*(K_{00}^{1/2}e_1).
\]
The column \(K_{00}^{1/2}e_1\) has rank one, so the Gram-rank identity gives \(\operatorname{rk}k=1\).
The actual finite-affiliated polar and Gram identities are precisely the [retained foundations and local consequences](../ledger/Yin_L_A0009_v1.md#another-closed-class-injective-positive-real-part).
Thus \(k\) and the actual pivot \(ik\) are independently invertible, with \((ik)^{-1}=-ik^{-1}\).
Inverse closure puts their inverses in \(R\).

The scalar Schur complement is
\[
\begin{aligned}
L_1
&=H_1+iK_1-(ib^*)(-ik^{-1})(ib)\\
&=H_1+i\bigl(K_1-b^*k^{-1}b\bigr).
\end{aligned}
\tag{D2}
\]
The last parenthesis is selfadjoint, with the displayed noncommutative order.
In particular, the real part is exactly \(H_1\), rather than merely a positive operator with an uncontrolled kernel.
Writing \(b=(b_0,b_+)\) according to the remaining zero block and positive block, the new imaginary compression on the zero block is
\[
K_{00}^{(1)}=K_{00,1}-b_0^*k^{-1}b_0.
\tag{D3}
\]
For \(r>1\), set \(V_0=\binom{-k^{-1}b_0}{I_{r-1}}\).
The exact identity
\[
K_{00}^{(1)}=V_0^*K_{00}V_0
=(K_{00}^{1/2}V_0)^*(K_{00}^{1/2}V_0)
\]
shows positivity.
The bottom identity block is a left inverse witness for \(V_0\), so it has rank \(r-1\).
The invertibility of \(K_{00}^{1/2}\) and the Gram-rank identity give \(\operatorname{rk}K_{00}^{(1)}=r-1\).
For \(r=1\), the empty compression simply disappears.
Thus (D1) is preserved with \((n,r)\) replaced by \((n-1,r-1)\), and every new entry stays in \(R\).

The [exact actual Schur equivalence](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) gives at every step
\[
\operatorname{rk}L=1+\operatorname{rk}L_1,
\qquad \dim_M\ker L=\dim_M\ker L_1.
\tag{D4}
\]
After \(r\) such pivots, the remaining real part is the original injective \(H_+\).
The already retained positive-real-part argument certifies all remaining scalar pivots and gives full rank \(n-r\).
Therefore \(L\) is an actual affiliated unit of rank \(n\), with its inverse in the actual rational closure.
All calculations take place in the closed finite-affiliated star algebra; none asserts that an unbounded inverse acts pointwise on every Hilbert-space vector.
The argument explicitly certifies the next pivot from the preserved pair, rather than assuming the invertibility of the original \(L\) or of an arbitrary nonzero rational entry.

## A noncyclic positive rational sum produced by the first pivot

Let \(G\) be torsion-free and choose \(g,h,k,l\ne e\).
Write \(\Delta_s=2-s-s^{-1}=(1-s)^*(1-s)\), and set
\[
A=\Delta_g,\quad B=\Delta_h,\quad C=\Delta_k,\quad D=\Delta_l.
\]
The [cyclic regular-representation argument](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) makes all four positive operators injective and affiliated invertible, independently of any Atiyah premise for \(G\).
Define
\[
Q=\begin{pmatrix}A+B&B\\B&B+C\end{pmatrix},
\qquad u=\binom{1}{1},
\qquad
L=\begin{pmatrix}
i(A+B)&iB&i\\
iB&i(B+C)&i\\
i&i&D
\end{pmatrix}.
\tag{D5}
\]
Here \(H=\operatorname{Re}L=\operatorname{diag}(0,0,D)\) and \(K=\operatorname{Im}L=\left(\begin{smallmatrix}Q&u\\u^*&0\end{smallmatrix}\right)\).
The identity
\[
Q=\operatorname{diag}(A,C)+\binom{1}{1} B\begin{pmatrix}1&1\end{pmatrix}
\]
proves \(Q\ge0\) and \(\operatorname{rk}Q=2\).
For the rank assertion, a kernel projection of this positive sum is killed by both positive summands; its being killed by the injective \(\operatorname{diag}(A,C)\) forces it to be zero.
This is an application of properness and does not use the invertibility of \(L\).

Let \(a=A+B\).
The first pivot is \(ia\), independently invertible because \(a\ge A\ge0\) and \(A\) is injective.
Its Schur complement is
\[
L_1=\begin{pmatrix}iq&iv\\iv^*&D-ia^{-1}\end{pmatrix},
\quad
q=C+B-Ba^{-1}B,
\quad
v=1-Ba^{-1}.
\tag{D6}
\]
The next pivot is not assumed cyclic or confined to a common commutative field.
Its independent positive certificate can be written in two equivalent ways.
The compression argument (D3) already proves that \(q\) is positive injective.
More explicitly, ordered multiplication gives
\[
B-B(A+B)^{-1}B
=B(A+B)^{-1}A
=(A^{-1}+B^{-1})^{-1}.
\tag{D7}
\]
Indeed the inverse of \(B(A+B)^{-1}A\) is \(A^{-1}(A+B)B^{-1}=B^{-1}+A^{-1}\).
All inverses in this verification have already been independently justified.
The sum \(A^{-1}+B^{-1}\) is positive injective, so its inverse is positive injective as well.
One direct affiliated verification writes that sum as the Gram product of \(\binom{A^{-1/2}}{B^{-1/2}}\), whose first entry is an actual unit and hence makes the column have rank one.
Consequently
\[
q=C+(A^{-1}+B^{-1})^{-1}\ge C\ge0
\tag{D8}
\]
is independently injective before \(q^{-1}\) is used.
This explicitly controls the sum of noncommuting parallel contributions, with no commutation of \(A\) and \(B\).
The parallel-sum identity is classical: Anderson and Duffin, [AD69](https://www.sciencedirect.com/science/article/pii/0022247X69902005), state the invertible-matrix formula in the published abstract and in the abstract and introduction of their [27 May 1968 report](../literature/pdf/AD69--report-1968.pdf#page=2).
The report's title page, abstract and opening introduction, PDF pp. 1--4, were inspected, including its explicit finite-dimensional restriction.
The report was obtained from the [CMU repository](https://doi.org/10.1184/R1/6479477.v1), and the published work's identity and formula were checked against the publisher's record.
This is source attribution for the known algebraic operation, not a source proof of the unbounded affiliated claims here; the ordered algebra and positive-injectivity checks above establish that interface directly.
No full audit of AD69 or comparison of the complete report and journal text is claimed or needed for this use.

The second pivot \(iq\) is now justified, and the final scalar is
\[
s=D-i\bigl(a^{-1}+v^*q^{-1}v\bigr).
\tag{D9}
\]
Its real part is exactly \(D\), hence is independently injective.
The positive-real-part lemma therefore certifies \(s\) as an actual affiliated unit.
The entire chain gives
\[
\operatorname{rk}_G L
=1+\operatorname{rk}_G L_1
=2+\operatorname{rk}_G s=3,
\qquad
\dim_G\ker L=\dim_G\ker L_1=\dim_G\ker s=0.
\tag{D10}
\]
The real part keeps rank one during the first two eliminations; positivity of the additional imaginary compression certifies precisely the pivots that the real part alone cannot certify.

## A screen excluding every direct full-rank constant-weight real part

For a concrete nonindicable choice, use the [retained Promislow group](../ledger/Yin_L_A0010_v1.md#group-and-selected-pencil) and take
\[
g=a_P,\qquad h=b_P,\qquad k=a_Pb_P,\qquad l=a_P.
\tag{D11}
\]
The subscripts distinguish the group generators from the positive pivot \(a=A+B\).
All four are nonidentity and infinite order, and \(a_P,b_P\) do not commute.
The positive path coefficients \(A=\Delta_{a_P}\) and \(B=\Delta_{b_P}\) themselves do not commute either.
With \(X=a_P^2,Y=b_P^2,Z=(a_Pb_P)^2\), the retained normal forms give
\[
\begin{aligned}
(a_P+a_P^{-1})(b_P+b_P^{-1})
&=(1+X^{-1})(1+Y)a_Pb_P,\\
(b_P+b_P^{-1})(a_P+a_P^{-1})
&=(1+X^{-1})(1+Y)Z^{-1}a_Pb_P.
\end{aligned}
\]
Hence
\[
[A,B]=(1+X^{-1})(1+Y)(1-Z^{-1})a_Pb_P\ne0,
\]
since \(X,Y,Z\) freely generate the abelian translation subgroup.
The original coefficient support generates \(P\), which has no nonzero integer character.
Moreover the first diagonal entry has support \(\{e,a_P,a_P^{-1},b_P,b_P^{-1}\}\).
If group-monomial diagonal row and column factors carried this entry into one cyclic Laurent ring, comparing the identity term to the \(a_P\) and \(b_P\) terms would put simultaneous conjugates of \(a_P,b_P\) into one cyclic subgroup, a contradiction.
Thus the explicit cyclic Laurent gauge condition of L_A0010 is unavailable for this pencil.

The following stronger real-part screen holds:
\[
T:=\operatorname{Re}(\gamma WL)\ge0,
\quad \gamma\ne0,
\quad W\in M_3(\mathbb C),\ W>0
\quad\Longrightarrow\quad
\operatorname{rk}_P T\le1.
\tag{D12}
\]
In particular, no such original constant-weight phase has an injective positive real part.
This does not assert that positive semidefinite real parts are absent: \(\gamma=1,W=I\) gives \(T=H\) of rank one.

To prove (D12), use the explicit [four-coset Følner vectors](../ledger/Yin_L_A0010_v1.md#direct-test-screen) for the trivial character of \(P\).
They show that positivity of a bounded matrix over \(\mathbb CP\) implies positivity of its augmentation evaluation, without treating augmentation as a normal map on \(\mathcal N(P)\).
All four Laplacians vanish under augmentation, so
\[
\epsilon(L)=iJ,
\qquad J=\begin{pmatrix}0_2&u\\u^*&0\end{pmatrix}.
\]
The real symmetric \(J\) has eigenvalues \(\sqrt2,-\sqrt2,0\).
Testing \(\operatorname{Re}(i\gamma WJ)\ge0\) on eigenvectors for its two nonzero eigenvalues forces \(\operatorname{Im}\gamma=0\), because \(W\) is positive definite.
Thus \(\gamma\) is nonzero real.
The positive evaluated matrix \(\gamma i(WJ-JW)/2\) has zero trace, hence is zero, so \(WJ=JW\).

Write \(W=\left(\begin{smallmatrix}W_{00}&w\\w^*&w_{33}\end{smallmatrix}\right)\).
The top-left block of the commutation identity is \(wu^*=uw^*\).
The leading two-square compression of the actual \(T\) is therefore
\[
T_{00}=\frac{\gamma i}{2}(W_{00}Q-QW_{00}).
\]
Its unnormalized canonical trace is zero by traciality.
Since \(T\ge0\), its compression \(T_{00}\) is positive, and trace faithfulness gives \(T_{00}=0\).
For the coordinate projection \(p_0=\operatorname{diag}(I_2,0)\), the identity \(p_0Tp_0=0\) implies \(T^{1/2}p_0=0\), hence \(Tp_0=0\).
Thus \(\dim_P\ker T\ge2\), proving (D12).

The same matrix has a whole-row-three-monomial stabilization by the [identity-pivot construction](../ledger/Yin_L_A0010_v1.md#an-elementary-row-splitting-step).
In the displayed expanded rows of (D5), the term counts for (D11) are \(9,9,5\), giving fourteen auxiliary variables and a seventeen-square matrix with unchanged kernel dimension.
The added identity pivots recover (D5), after which the three pivots above apply.
The statement (D12) concerns the original three-square pencil; no claim is made that an arbitrary chosen stabilization has the same direct energy-screen behavior.

## Scope, prior mechanisms and the remaining obligation

The pair (D1) retains more information than the rank or sign of \(\operatorname{Re}L\) alone.
It permits a strict scalar induction through a nonzero kernel of the real part and certifies the new noncyclic sum (D8) before its inverse is used.
The exhibited matrix therefore escapes the earlier original-pencil full-rank real-part test and cyclic Laurent gauge test, while remaining accessible to this explicit semidefinite-energy refinement.
Its group instance is already virtually abelian, and the proof of (D1) works in any finite affiliated algebra with the stated positivity data.
There is no new positive Atiyah group class, no claim of historical novelty, and no implication that torsion-freeness produces the decomposition (D1) for arbitrary group-ring matrices.
If the compressed imaginary part is merely selfadjoint with an uncontrolled zero spectral projection, positivity of the remaining real part does not certify the next pivot.
That missing compression certificate is the precise remaining obligation beyond this class.

For source comparison, a bounded primary-source search on 2026-11-11 found Candan Güdücü, Jörg Liesen, Volker Mehrmann and Daniel B. Szyld, *On non-Hermitian positive (semi)definite linear algebraic systems arising from dissipative Hamiltonian DAEs*, [arXiv:2111.05616v3](https://arxiv.org/abs/2111.05616v3), revised 4 August 2022.
The inspected [GLMS22, arXiv v3](../literature/pdf/GLMS22--arxiv-v3.pdf#page=9), Section 4, Lemma 4.2 and Corollary 4.3, printed/PDF pp. 9--10, treats finite complex matrices using staircase and Schur reductions and records preservation of a semidefinite Hermitian part.
This is related prior work for the mechanism, not a proof input establishing the affiliated inverses, trace ranks or unbounded-domain assertions here.
Its relevant statements and preceding Schur calculation were inspected; the full paper and its external proof foundations were not audited.
The actual affiliated deductions above use the fixed local Schur, positivity and Gram interfaces explicitly cited in their proofs.

## A relative-path certificate and its missing premise

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(U=\mathcal U(M)\).
If \(P,Q\in U^\times\) are independently certified units, then
\[
P+Q=P(1+T),\qquad T=P^{-1}Q.
\tag{R1}
\]
Consequently \(\operatorname{rk}(P+Q)=\operatorname{rk}(1+T)\), with the same closed-kernel dimension.
This identity alone supplies no new invertibility information.

An independent sufficient premise is an exhibited actual unit \(C\), scalar \(\zeta\ne0\), and nonidentity infinite-order group element \(g\) such that
\[
T=C^{-1}\zeta\lambda(g)C.
\]
Then \(1+T=C^{-1}(1+\zeta\lambda(g))C\) is a unit by the [cyclic regular-representation input](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions).
The conjugating unit need not be bounded, but its invertibility must be independently known before the identity is used.
This is transported cyclic coverage, not an argument that an arbitrary relative path admits this representation.

If instead \(T\in M\) is unitary, a usable analytic premise is
\[
\tau(T^n)=0\quad\text{for every integer }n\ne0.
\tag{R2}
\]
To check the needed conclusion directly, let \(p\) be the kernel projection of \(1+T\) and put \(F_m=m^{-1}\sum_{k=0}^{m-1}(-T)^k\).
Then \(F_mp=pF_m=p\), and (R2) gives \(\tau(F_m^*F_m)=1/m\).
Consequently \(0\le\tau(p)\le1/m\) for every positive integer \(m\), so \(p=0\) by trace faithfulness.
Thus \(1+T\) is injective and hence an actual affiliated unit.
The certificate (R2) concerns the relative path, not the spectral laws of \(P\) and \(Q\) separately.
No finite subset of these moments is asserted to be sufficient.
Neither (R1) nor (R2) is claimed to be preserved by arbitrary later Schur elimination.

## Individual diffuse path laws do not suffice

Let \(F_2=\langle g,h\rangle\), let \(z\) denote the coordinate unitary in \(L^\infty(\mathbb T)\), and choose \(0<\theta<1\).
Use
\[
M=L^\infty(\mathbb T)\oplus\mathcal N(F_2),
\qquad
\tau=\theta\tau_{\mathbb T}+(1-\theta)\tau_{F_2},
\]
and define
\[
u=(z,\lambda(g)),\qquad v=(-z,\lambda(h)).
\tag{R3}
\]
Both are Haar unitaries: every nonzero integral moment vanishes in each direct summand.
The homomorphism from \(F_2\) sending its generators to \(u,v\) is faithful because its second component is the faithful regular group representation.
Thus the abstract subgroup generated by \(u,v\) is noncommutative and torsion-free.
Nevertheless,
\[
u+v=(0,\lambda(g)+\lambda(h)),
\]
and its second component is injective because
\(\lambda(g)+\lambda(h)=\lambda(g)(1+\lambda(g^{-1}h))\) has an independently certified cyclic factor.
Hence
\[
\dim_M\ker(u+v)=\theta.
\tag{R4}
\]
The relative unitary is
\[
u^*v=(-1,\lambda(g^{-1}h)),\qquad \tau(u^*v)=-\theta,
\]
so its spectral measure has an atom of mass \(\theta\) at \(-1\).
This representation is not the group regular representation with its canonical trace, as that nonzero trace on the nonidentity word \(g^{-1}h\) already shows.
The example is therefore not an Atiyah counterexample.
It refutes only the proposed inference from individual Haar laws, relative unitarity and abstract torsion-freeness to invertibility of a path sum.

## One inverse-difference Schur step

Let \(x_1,x_2,y_1,y_2\in U\), and suppose every cross difference \(x_i-y_j\) is an independently certified unit.
Set
\[
K=\begin{pmatrix}
(x_1-y_1)^{-1}&(x_1-y_2)^{-1}\\
(x_2-y_1)^{-1}&(x_2-y_2)^{-1}
\end{pmatrix}.
\]
Its first pivot is already a unit.
The remaining scalar is
\[
S=(x_2-y_2)^{-1}
 -(x_2-y_1)^{-1}(x_1-y_1)(x_1-y_2)^{-1}.
\tag{C1}
\]
The following exact factorization does not require any commutation:
\[
\boxed{
S=(x_2-y_1)^{-1}(y_2-y_1)(x_2-y_2)^{-1}
  (x_1-x_2)(x_1-y_2)^{-1}.}
\tag{C2}
\]
To verify it, multiply (C1) on the left by \(x_2-y_1\) and on the right by \(x_1-y_2\).
Writing \(D=x_2-y_2\), \(B=y_2-y_1\), and \(F=x_1-y_2\), the result is
\[
(D+B)D^{-1}F-(F+B)
=BD^{-1}(F-D)
=(y_2-y_1)(x_2-y_2)^{-1}(x_1-x_2).
\]
Multiplying by the two already justified outside inverses proves (C2).

If the two same-side differences \(x_1-x_2\) and \(y_2-y_1\) are independently units as well, (C2) certifies \(S\) as a unit before any use of \(S^{-1}\).
The [actual Schur rank identity](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) then gives
\[
\operatorname{rk}K=1+\operatorname{rk}S=2,
\qquad \dim\ker K=\dim\ker S=0.
\tag{C3}
\]
All six difference-unit premises hold when the four parameters are distinct regular group elements of a torsion-free group: every difference is a group unit times a nonzero cyclic binomial.
This gives a genuine certification after the two noncommuting terms in (C1) have been combined.
The algebraic constraint is that the inverse entries come from the same additive rectangle \(x_i-y_j\); no theorem asserting injectivity of an arbitrary sum is used.

For a nonindicable calibration, take the [Promislow group](../ledger/Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test), and choose
\[
x_1=1,\quad x_2=a,\quad y_1=b,\quad y_2=ab.
\]
The four distinct cosets of its abelian translation subgroup show these group elements are distinct.
Its remaining scalar is
\[
S=(a-ab)^{-1}-(a-b)^{-1}(1-b)(1-ab)^{-1}
\]
and (C2) gives the certified factorization
\[
S=(a-b)^{-1}(ab-b)(a-ab)^{-1}(1-a)(1-ab)^{-1}.
\tag{C4}
\]
In particular its inverse is the independently defined product
\[
S^{-1}=(1-ab)(1-a)^{-1}(a-ab)(ab-b)^{-1}(a-b).
\]
The proof works in every torsion-free group for four distinct selected parameters, not merely in this already known virtually abelian example.
No complete exclusion of all possible positive-real-part transformations of this rational realization is claimed.

## A shape invariant with central column parameters

Now consider an \(n\)-square array \(K_{ij}=(x_i-\lambda_j)^{-1}\), where the column parameters \(\lambda_j\) are central in \(U\).
Assume every displayed cross difference, every \(x_1-x_i\) for \(i>1\), and every \(\lambda_j-\lambda_1\) for \(j>1\) is independently a unit.
The same calculation, entry by entry, gives the first Schur complement
\[
S_{ij}=(x_i-\lambda_1)^{-1}(\lambda_j-\lambda_1)
 (x_i-\lambda_j)^{-1}(x_1-x_i)(x_1-\lambda_j)^{-1},
\quad i,j>1.
\tag{C5}
\]
Put
\[
c_i=x_1-x_i,
\qquad x_i'=c_i^{-1}x_i c_i,
\]
\[
U_i=(x_i-\lambda_1)^{-1}c_i,
\qquad V_j=(\lambda_j-\lambda_1)(x_1-\lambda_j)^{-1}.
\]
The centrality of the column parameters gives the exact identity
\[
\boxed{S_{ij}=U_i(x_i'-\lambda_j)^{-1}V_j.}
\tag{C6}
\]
The row and column factors are independently units under the stated premises.
Each transformed cross difference is independently a unit as well, because
\[
x_i'-\lambda_j=c_i^{-1}(x_i-\lambda_j)c_i.
\tag{C7}
\]
Thus the smaller matrix is again an inverse-difference array up to known unit row and column factors, and its next displayed scalar entry is independently invertible.
The row parameters stay in their actual similarity orbits; central column parameters are retained.
This shape invariant is stronger than merely remembering that entries are rational expressions.

It does not certify the next differences \(x_i'-x_k'\).
Those differences are needed to repeat the factorization into units at the following stage.
They can be zero, as the next example proves, and an arbitrary nonzero such rational difference has not been independently certified here.
The unresolved obligation is exactly a zero-or-unit test for these new row separations, not existence of the first two scalar pivots.
Assuming that every nonzero new separation is a unit would reintroduce the unknown division-closure assertion.

For a three-square array, assume in addition that \(\lambda_3-\lambda_2\) is independently a unit.
Then the shape identity gives an exact expression for the remaining obstruction.
After the first elimination and removal of its known row and column factors, the remaining two-square inverse-difference array has row parameters \(x_2',x_3'\) and central column parameters \(\lambda_2,\lambda_3\).
Every cross difference is still an independently known unit by (C7), and the additional same-side unit premise is retained.
Applying the factorization (C2) without assuming that \(x_2'-x_3'\) is a unit gives
\[
\operatorname{rk}K=2+\operatorname{rk}(x_2'-x_3'),
\qquad
\dim\ker K=\dim\ker(x_2'-x_3').
\tag{C7a}
\]
Indeed every other factor in that last scalar Schur complement is an already certified unit.
This isolates a possible fractional defect in one explicit difference of rational conjugates rather than concealing it in a formally nonzero quasideterminant.

## A complete conditional invariant in one normalized coefficient component

There is a useful sufficient condition under which the missing zero-or-unit separation test is preserved through the entire inverse-difference induction.
Let \(\mathscr D\subset U\) be an actual division subring whose division property has been independently established, and let \(t\in U^\times\) be an independently known unit satisfying
\[
t\mathscr D t^{-1}=\mathscr D,
\qquad \alpha(d)=tdt^{-1}.
\tag{N1}
\]
Suppose the row parameters of an \(m\)-by-\(n\) array lie in the same component
\[
x_i=d_i t,\qquad d_i\in\mathscr D,
\]
and the column parameters \(\lambda_j\) are central in \(U\).
Assume every initial cross difference \(x_i-\lambda_j\) and every difference \(\lambda_j-\lambda_k\) for \(j\ne k\) is independently a unit.
No independence of powers of \(t\), integer grading of the ambient group, or division property of the ring generated by \(\mathscr D,t\) is assumed.
The condition is on an exhibited coefficient division ring and a normalizing unit, not on the unknown full rational closure.

Equal \(d_i\) give identical rows in the inverse-difference array.
Subtract one such row from another by a bounded elementary row unit, obtain a zero row, and remove that zero output coordinate; rank and kernel dimension are unchanged.
For the remaining distinct parameters, every difference \(x_1-x_i=(d_1-d_i)t\) is independently a unit because its nonzero coefficient belongs to the already known division ring.
The calculations (C5)--(C7) also hold for rectangular arrays, with one row and one column removed at each pivot.
Set \(e_i=d_1-d_i\), so \(c_i=e_i t\).
The transformed parameter satisfies the ordered identity
\[
\begin{aligned}
x_i'
&=(e_i t)^{-1}(d_i t)(e_i t)\\
&=t^{-1}e_i^{-1}d_i\alpha(e_i)t^2\\
&=\bigl[\alpha^{-1}(e_i^{-1}d_i)e_i\bigr]t.
\end{aligned}
\tag{N2}
\]
Thus \(d_i'=\alpha^{-1}(e_i^{-1}d_i)e_i\in\mathscr D\), even when the coefficients do not commute.
Every new row separation is
\[
x_i'-x_k'=(d_i'-d_k')t,
\]
which is exactly zero or an independently known unit.
All remaining cross differences stay units by actual similarity in (C7), and the column-separation premises persist when a column is removed.
After removing the known unit row and column factors in (C6), the smaller array therefore satisfies precisely the same hypotheses.
When such factors are present, remove them before subtracting duplicate rows; this uses their already certified actual inverses and does not presume a bounded Hilbert-space kernel map.

At every nonempty stage choose a displayed cross entry as pivot, merge any coincident rows, and repeat.
Each pivot removes one row and one column and adds one to the rank; merging removes only zero output rows after an invertible row operation.
The process terminates at an array with no rows or no columns.
If \(q\) pivots have occurred, the exact rank and closed-kernel dimension are
\[
\operatorname{rk}K=q,\qquad \dim_M\ker K=n-q.
\tag{N3}
\]
This gives a complete conditional integer-rank induction, including singular outcomes caused by actual row mergers.
It asserts no uniform procedure for deciding arbitrary equality in \(\mathscr D\); in a displayed cyclic rational field the coefficient identities can be checked directly.
If the coefficient ring, normalizing unit and column parameters lie in the actual rational closure under consideration, all entries and certified inverses used in this induction stay there.

For example, the following Klein bottle calibration has \(\mathscr D=\mathbb C(g)\), the independently known actual cyclic field, and \(t\) normalizes it by \(g\mapsto g^{-1}\).
Its row labels \(tg^i=g^{-i}t\) lie in \(\mathscr D t\), while its central column labels \(t^{2j}\) need not lie in \(\mathscr D\).
The closure in (N2) controls their noncommutative additions without requiring all entries to lie in one cyclic field.
This is a sufficient extension based on already controlled coefficient division, not a proof that an arbitrary torsion-free group supplies such a coefficient ring or normalizing structure.
Its concrete group coverage remains within known cyclic or finite-extension mechanisms.

## An actual torsion-free collision after one step

Take the Klein bottle group
\[
G=\langle t,g\mid tgt^{-1}=g^{-1}\rangle,
\qquad z=t^2.
\]
It is the semidirect product \(\mathbb Z\rtimes_{-1}\mathbb Z\).
In pair coordinates its multiplication is
\((n,m)(r,s)=(n+(-1)^m r,m+s)\).
If a positive power of such a pair is the identity, its second coordinate first forces \(m=0\), after which the first forces \(n=0\); hence it is torsion-free.
The element \(z\) is central and has infinite order.

Choose three row parameters and three central column parameters
\[
x_i=tg^i\quad(i=0,1,2),
\qquad \lambda_j=z^j\quad(j=1,2,3).
\tag{C8}
\]
All six are distinct group elements by their pair coordinates.
Every cross difference and every same-side difference is therefore independently a unit by the torsion-free cyclic test.
Moreover \(x_i^2=z\), so
\[
(x_i-\lambda_j)^{-1}
=(x_i+\lambda_j)(z-\lambda_j^2)^{-1}.
\tag{C9}
\]
The denominator is \(z(1-z^{2j-1})\), an independently known unit.
Consequently the three-square inverse-difference matrix factors as a three-by-two matrix times a two-by-three matrix:
\[
K=
\begin{pmatrix}x_0&1\\x_1&1\\x_2&1\end{pmatrix}
\begin{pmatrix}
(z-\lambda_1^2)^{-1}&(z-\lambda_2^2)^{-1}&(z-\lambda_3^2)^{-1}\\
\lambda_1(z-\lambda_1^2)^{-1}&\lambda_2(z-\lambda_2^2)^{-1}&\lambda_3(z-\lambda_3^2)^{-1}
\end{pmatrix}.
\tag{C10}
\]
Thus \(\operatorname{rk}_G K\le2\), while any two-by-two submatrix is a unit by (C2), so
\[
\operatorname{rk}_G K=2,\qquad \dim_G\ker K=1.
\tag{C11}
\]
This is an allowed integer defect, not a counterexample to Atiyah.

The shape calculation identifies the precise collision.
Use \(x_0=t\) as the first row parameter, so \(c_i=t(1-g^i)\) for \(i=1,2\).
Then
\[
\begin{aligned}
c_i^{-1}x_i c_i
&=(1-g^i)^{-1}g^i t(1-g^i)\\
&=(1-g^i)^{-1}g^i(1-g^{-i})t=-t.
\end{aligned}
\tag{C12}
\]
The two transformed row parameters coincide, and the final Schur pivot is exactly zero.
Thus original pairwise binomial invertibility does not preserve separation after the rational conjugations in (C6).
Any useful induction must allow and detect such exact mergers while also ruling out a proper nonzero analytic kernel for a nonzero transformed separation.
The group has already known virtually abelian Atiyah coverage, but no such theorem was used to compute (C11).

## Source attribution and remaining scope

The exact block elimination and affiliated rank conventions are reused from [L_A0009](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step), with the cyclic unit input from [L_A0002](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions).
A bounded primary-source search on 2026-11-11 for noncommutative Cauchy matrices, inverse differences and quasideterminants found the general framework in Gelfand, Gelfand, Retakh and Wilson, *Quasideterminants*, Adv. Math. 193 (2005), 56--141, DOI [10.1016/j.aim.2004.03.018](https://doi.org/10.1016/j.aim.2004.03.018).
The inspected [arXiv v4](../literature/pdf/GGRW05--arxiv-v4.pdf#page=9), Examples 1.2.3(a), Definition 1.2.5 and Proposition 1.2.6, printed/PDF pp. 9--10, gives the two-square Schur expression and the actual-ring invertibility premise for its general form.
These passages provide attribution and a compatible framework, not a source theorem asserting (C2) or injectivity for the present group evaluation.
The exact factorization (C2), shape calculation and collision above are checked directly in the actual ring.
The search did not locate the precise inverse-difference factorization; this limited search establishes no priority claim or absence of an earlier source.
The survey's later free-field, genericity and Vandermonde results are not imported.
No unresolved source theorem is needed for the displayed deductions, and no full audit of the survey is claimed.

The positive result is a constrained additive cancellation with independently certified factors, followed by a shape invariant whose next missing premise is explicit.
The normalized-coefficient-component condition supplies that premise throughout the induction, while leaving its actual coefficient division property and normalizing structure as independently required hypotheses.
It supplies neither a universally preserved zero-or-unit separation condition nor a reduction of arbitrary rational path sums to this array.
The relative-unitary counterexample shows what a weaker spectral substitute would miss: joint relative-word information retained by the actual regular trace.

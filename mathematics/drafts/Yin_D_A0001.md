---
author: Yin
---
# Degenerate real-part certificates for noncyclic Schur path addition

This investigation develops an explicit invariant for [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract): positivity of the real part together with positive injective imaginary compression on its specified zero block.
It certifies each successive pivot independently, including a noncyclic rational sum produced after the first elimination.
A concrete Promislow-group example has no injective positive real part after any constant positive left weight and scalar phase, so the original-pencil hypothesis of [L_A0009](../ledger/Yin_L_A0009_v1.md#another-closed-class-injective-positive-real-part) does not already apply.
The proof is an explicit semidefinite-energy and Schur refinement, not a new Atiyah group class or an assertion that torsion-freeness creates this structure in an arbitrary matrix.
The main agent is responsible for fixed retention, source registration and any formal review.

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
The parallel-sum identity is classical; its source attribution is to be supplied by the main agent's coordinated inspection, not claimed as new here.

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

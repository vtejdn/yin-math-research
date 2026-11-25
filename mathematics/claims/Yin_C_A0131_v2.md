---
author: Yin
---

# Finite-rank criteria for the division closure of a group algebra

## Statement

Let \(G=\langle g_1,\ldots,g_d\rangle\) be a finitely generated discrete group and \(X_j=\lambda(g_j)\) its marked left translations.
Write \(A=\mathbb CG\), \(M=\mathcal N(G)\), \(H=\ell^2(G)=L^2(M,\tau)\), and \(U=L^0(M)\), where \(\tau\) is the group trace.
The division closure \(D_G\) of \(A\) in \(U\) is obtained by ring operations and inversion of individual elements that are units in \(U\).
Write \(\rho_j\xi=\xi X_j\) for right multiplication and \(P_e\) for the orthogonal projection onto \(\mathbb C\delta_e\).
Identify \(M\subset H\subset U\) using \(x\mapsto x\delta_e\) for bounded elements.

For \(u\in U\), the following conditions are equivalent.

1. \(u\in D_G\).
2. There are \(n\ge1\), an affine pencil \(L=L_0+\sum_{j=1}^d L_j X_j\) with \(L_j\in M_n(\mathbb C)\) and \(\ker_{H^n}L=0\), a scalar row \(\alpha\) and a scalar column \(\beta\) of length \(n\) such that \(u=\alpha L^{-1}\beta\) in \(U\).
3. There are \(s,a,b,t\in M\) with \(s,t\in U^\times\), \(u=s^{-1}a=bt^{-1}\), and finite-rank \(T_1,\ldots,T_d\in B(H)\) satisfying the F0001 equation
   \[
       \sum_{j=1}^d[\rho_j,T_j]=sP_e b-aP_e t. \tag{1}
   \]
   For the same witnesses there are an injective pencil \(L\) and a scalar row \(\alpha\) as in condition 2, and a row \(\eta=(\eta_1,\ldots,\eta_n)\in H^{1\times n}\) satisfying
   \[
       \eta L=s\alpha,\qquad
       \sum_{j=1}^d\operatorname{Ran}T_j
         \ \subseteq\ W=\operatorname{span}_{\mathbb C}\{\eta_1,\ldots,\eta_n\}. \tag{2}
   \]

The row equation uses right multiplication on \(H\) and the vector \(s\delta_e\) on the right-hand side.
The variables in (1) and (2) range over bounded operators, Hilbert space vectors and finite scalar matrices.
The rank of each \(T_j\) is its ordinary complex rank.

If \(D_G\) is a division ring, (1) alone with the stated existential quantifiers characterizes \(D_G\).
In particular this holds for torsion-free groups satisfying the strong Atiyah conjecture over \(\mathbb C\). [Linnell and Lück, Theorem 2.3(3)](../ledger/Yin_L_A0001_v1.md#formulation-and-algebraic-interface)
The [unrestricted equation](Yin_C_A0131_v1.md#statement) characterizes the algebraic \(*\)-regular closure in general.
For an arbitrary torsion-free group, equivalence with (1) alone requires the additional kernel-projection property established there as the exact condition.

## Argument

### Linear pencils for scalar rational operations

Every element of \(D_G\) has a finite expression in the \(X_j\), scalars, sums, products and inverses of affiliated units, since \(X_j^{-1}\) recovers each inverse generator.
Constants have constant pencils, and \(X_j\) is the upper right entry of the inverse of \(\left(\begin{smallmatrix}1&-X_j\\0&1\end{smallmatrix}\right)\).
For realizations \(\alpha L^{-1}\beta\) and \(\gamma K^{-1}\nu\), block diagonal sum gives addition.
The upper right block of the inverse of \(\left(\begin{smallmatrix}L&-\beta\gamma\\0&K\end{smallmatrix}\right)\) gives their product after contraction with \(\alpha,\nu\).
If \(u=\alpha L^{-1}\beta\) is a unit, the Schur complement of \(L\) in \(\left(\begin{smallmatrix}0&\alpha\\-\beta&L\end{smallmatrix}\right)\) is \(u\), so the enlarged pencil is invertible over \(U\) and its upper left inverse entry is \(u^{-1}\).
All pencils constructed this way are invertible over \(U\) at the given tuple and hence injective on \(H^n\). [Mai, Speicher and Yin, Section 4](../audits/literature/MSY23/Yin_U003.md#msy23-u003)

Conversely, suppose \(L\) is an injective pencil as in condition 2.
Each leading principal block \(H_k\) of \(L^*L\) is the Gram matrix of the first \(k\) columns of \(L\).
These columns define an injective bounded map \(H^k\to H^n\), so \(H_k\) is injective and hence a unit in \(M_k(U)\) by finiteness of the trace. [Affiliated matrix invertibility](../audits/literature/MSY23/Yin_U004.md#msy23-u004)
The entries of \(H_k\) lie in \(A\), which is closed under adjoints.
Inductively, \(H_1^{-1}\in D_G\), and if \(H_k^{-1}\in M_k(D_G)\), write \(H_{k+1}=\left(\begin{smallmatrix}H_k&w\\w^*&h\end{smallmatrix}\right)\).
Block elimination shows that \(h-w^*H_k^{-1}w\in D_G\) is a unit in \(U\), since both \(H_{k+1}\) and \(H_k\) are units in their matrix rings over \(U\).
Scalar division closure gives the inverse of this Schur complement in \(D_G\).
Reversing the elimination gives \(H_{k+1}^{-1}\in M_{k+1}(D_G)\).
Consequently \(L^{-1}=H_n^{-1}L^*\in M_n(D_G)\), proving condition 1 from condition 2.

### Constructing the finite-rank operators

Given \(u=\alpha L^{-1}\beta\), choose a common bounded left denominator \(s\) for \(u\) and the entries of \(\alpha L^{-1}\), and a common bounded right denominator \(t\) for \(u\) and the entries of \(L^{-1}\beta\).
Both denominators are units in \(U\).
Set \(a=su\), \(b=ut\), \(\eta=s\alpha L^{-1}\) and \(z=L^{-1}\beta t\), all with bounded entries. [Simultaneous denominator clearing in F0001](Yin_C_F0068_v1.md#argument)
Then \(\eta L=s\alpha,\ Lz=\beta t,\ \eta\beta=a,\ \alpha z=b\).
Define
\[
     T_j=\sum_{p,q=1}^n (L_j)_{pq}\,\eta_p P_e z_q.
\]
Their ranges lie in \(W\).
For \(v,w\in M\), the trace identity gives \([\rho_j,vP_e w]=(vX_j)P_e w-vP_e(X_jw)\).
The contributions of the scalar matrix \(L_0\) cancel, so
\[
    \sum_j[\rho_j,T_j]
      =\sum_q(\eta L)_qP_e z_q-\sum_p\eta_pP_e(Lz)_p
      =sP_e b-aP_e t .
\]
This proves (1) and (2) for one common choice of the fractions.

### Recovering division-closure membership from the ranges

Conversely, let (1) and (2) hold.
Right multiplication of \(\eta L=s\alpha\) by \(L^{-1}\) in affiliated matrices gives \(s^{-1}\eta=\alpha L^{-1}\in D_G^{1\times n}\) by the Gram argument.
Thus \(s^{-1}W\subset D_G\).
The range of the left side of (1) lies in \(W+\sum_j W X_j\).
Apply (1) to \(t^*\delta_e\) and use \(\tau(tt^*)>0\).
The right side is \(s\tau(bt^*)-a\tau(tt^*)\) as a vector in \(H\), so
\[
      a\in\mathbb C s+W+\sum_j W X_j.
\]
Multiplying on the left by \(s^{-1}\) in \(U\) gives \(u\in D_G\), since every \(X_j\) belongs to \(D_G\).

### The original equation over a division ring

Suppose \(D=D_G\) is a division ring.
The finite-rank tensor identification and cancellation of the two denominators in (1) give \(u\otimes_A1=1\otimes_Au\), hence \(u\otimes_D1=1\otimes_Du\) in the ordinary algebraic tensor product. [Balancing and ordinary finite rank](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
Extend \(1\) to a right \(D\)-basis of \(U\) and let \(f:U\to D\) take its coefficient.
Applying \(f\otimes_D\mathrm{id}\) gives \(f(u)=u\), so \(u\in D\).
The construction above supplies (1) in the other direction.

## Assessment history

### Decision division-closure-criterion

| Field | Value |
| --- | --- |
| date | 2026-11-25T07:08 |
| status | proved |
| reason | Injectivity of the column Gram blocks gives the scalar inverses for a pencil realization, and the common row condition recovers division-closure membership from the range of the finite-rank equation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The pencil criterion and the finite-rank criterion with a common row equation for every finitely generated group, and the unrestricted criterion when the division closure is a division ring. |
| argument | [Argument](#argument) | Scalar Schur elimination, finite-rank witnesses from a pencil, reconstruction from their ranges and the division-ring specialization. |
| dependency | [Affine realizations](../audits/literature/MSY23/Yin_U003.md#msy23-u003) | Evaluated block realizations for scalar rational operations in Section 4. |
| dependency | [Affiliated matrices](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Injectivity and invertibility over a finite affiliated matrix algebra. |
| dependency | [F0001 fractions](Yin_C_F0068_v1.md#argument) | Simultaneous bounded denominators on the left and right. |
| dependency | [Unrestricted equation](Yin_C_A0131_v1.md#argument) | Balancing from a finite-rank solution and the kernel-projection condition for the unrestricted equation. |
| dependency | [Strong Atiyah property](../ledger/Yin_L_A0001_v1.md#formulation-and-algebraic-interface) | Linnell and Lück, Theorem 2.3(3), for a torsion-free group with complex coefficients. |
| review | [Self-review](../audits/reviews/Yin_R_A0165_v2.md#division-closure-criterion) | The statement and both directions, including unbounded inverses and the scope of the division-ring argument. |

## Current assessment

[Selected decision](#decision-division-closure-criterion)

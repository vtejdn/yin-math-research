---
author: Yin
---
# The affine matrix inverse-trace criterion: complete independent review

Date: 2026-10-14T20:56.
Human record author: Yin.
This separately organized review covers the complete [C_F0154 v1](../../claims/Yin_C_F0154_v1.md#statement), its whole argument and exact C_F0148 Sections 1--2 input.
The reviewer did not develop this matrix result.
Earlier T_F0011 work on normal contractions and independent reviews of other row/domain claims are related background, not development of the matrix normalization or proof.
The assignment supplied the claimed criterion and requested verification targets; no D_F0003 new development, proof-generation dialogue or earlier C_F0154 review conclusion was consulted.
The fixed claim and exact dependency were read before the following calculations were independently reconstructed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0154 statement](../../claims/Yin_C_F0154_v1.md#statement) | Inverse trace and actual bounded-column range under explicit Q regularity and strictly positive scalar B, with unnormalized matrix trace, right-inverse norm and absence of a coherent-dual conclusion. |
| [Conclusion](#conclusion) | [C_F0154 argument](../../claims/Yin_C_F0154_v1.md#argument) | Whole proof: original-core matrix Neumann tests, exact matrix indices and starred tensor terms, positive compression, normalized weak limits, contradiction, polar-domain conclusion and singular-B scope. |
| [Conclusion](#conclusion) | [C_F0148 argument](../../claims/Yin_C_F0148_v1.md#argument) | Sections 1--2 only: actual polynomial-resolvent graph approximation and weak normalized-tensor method. No full-system regularity theorem, maximal-Delta input or special tuple application is imported. |

## Findings

### 1. The scalar compression is positive at the normalization used

The matrix L*R_epsilon L is a positive contraction and increases strongly to the initial polar projection I_m-p.
Entrywise application of the trace is a positive unital matrix map.
Thus C_epsilon decreases in scalar matrix order to C, and B_epsilon is at least B.
Strict positivity of B supplies c>0 with B_epsilon>=c I_n.
Since tau(R_epsilon) is a positive scalar matrix, finite-matrix trace order gives T_epsilon>=c U_epsilon>0.
The two scalar matrices need not commute; cyclicity of their finite trace suffices.

This check uses regularity of Q only where the statement explicitly supplies it.
No rectangular rank conclusion is inferred from the derivation hypothesis.
If B is singular, this normalization need not dominate U_epsilon, exactly as the final scope paragraph explains.

### 2. All resolvent pairings come from the original star core

For fixed epsilon, the Neumann series has a matrix operator-norm ratio theta<1.
Each matrix entry of a partial sum is a target star polynomial.
The matrix Hilbert bimodule has bounded left and right matrix actions, so the kth derivative has the stated k theta^(k-1) bound times the fixed derivative norm.
The series converges in both the operator norm and derivative Hilbert norm.
Multiplication by L A_i* and finite diagonal summation preserve both convergences.

The actual vacuum identity therefore passes to each displayed f_i without assuming that the initial domain contains an inverse.
This use only requires convergence of the scalar tests and their derivative values; it does not silently use a closed inverse rule or prescribe delta_i(L*) in terms of delta_i L.

### 3. The matrix indices and tensor conjugations in equation (4) agree

Write f_i=sum_(r,s,k) R_(rs)L_(sk) conjugate(A_i[r,k]).
Differentiating L gives R A_i tensor 1 and hence Tr(tau(R)A_i A_i*).
In the constant part of delta_i Q, the entry (a,b) is sum_l (A_i)_(al) tensor L_(bl)*.
After inserting the inverse derivatives and summing b,s, this gives

\[
 -\sum_{r,k,l}(\tau(R)A_i)_{rl}
       \tau((L^*RL)_{lk})\overline{(A_i)_{rk}}
 =-\operatorname{Tr}(\tau(R)A_iD_\varepsilon A_i^*).
\]

The two constant pieces combine to the claimed C_epsilon term.
The remaining part of delta_i Q has entry sum_l L_(al) dot K_(i,b,l).
The adjacent R and L factors sum to V_(rl) and V_(bk), leaving precisely

\[
 -\sum_{r,b,k,l}\overline{(A_i)_{rk}}
  (\tau\otimes\tau)\bigl(V_{rl}\cdot K_{i,b,l}\cdot V_{bk}\bigr).
\]

For elementary K=x tensor y, cyclicity makes this last double trace tau(x V_rl) tau(y V_bk), which is <K*, V_rl tensor V_bk> with componentwise adjoint and the inner product linear in its second variable.
Hilbert approximation extends the equality to every fixed K.
No flip, extra adjoint on V, or conjugation of the scalar coefficient is missing.

### 4. The divergence contradiction uses weak, not norm, tensor convergence

Traciality yields sum_(r,l)||V_rl||2 squared=Tr tensor tau(Q R_epsilon squared)<=U_epsilon.
Hence each normalized column has norm at most one.
Its high-Q-spectral part tends to zero in norm at fixed positive cutoff, bounded by ||L e_l||2 divided by the cutoff times sqrt(U_epsilon).
Its low-spectral pairing is bounded by ||e_t z||2.
Regularity of Q makes e_t decrease strongly to zero as t decreases to zero.
Taking epsilon to zero first and then t to zero proves weak convergence of every normalized column and entry.

Products of two such entries are uniformly bounded Hilbert tensors.
Their pairings against elementary tensors tend to zero, and density extends this to every fixed K*.
Multiplication by the bounded scalar U_epsilon/T_epsilon preserves convergence to zero.
Thus all finitely many starred error terms in the sum of equation (4), divided by T_epsilon, vanish.

The Hilbert--Schmidt coefficient estimate gives ||f_i||2<=||A_i||HS sqrt(U_epsilon).
Each fixed vacuum pairing divided by T_epsilon is consequently bounded by a constant times U_epsilon^(-1/2), which tends to zero.
The sum of the constant terms divided by T_epsilon is exactly one.
This gives the claimed contradiction.
Spectral monotone convergence justifies U_epsilon tending to infinity under the negated conclusion.

### 5. The polar formula has the asserted actual domain and norm

The positive trace of Q inverse is finite after the contradiction.
For a bounded column a, apply positive trace order to bounded spectral truncations of Q inverse and aa*<=||a|| squared I_n.
Monotone convergence gives the finite norm in equation (7), so a is in the actual domain of Q inverse square root.
Rectangular polar decomposition gives L=Q^(1/2)W and WW*=I_n, since Q is regular.
Therefore W*Q^(-1/2)a is an actual Hilbert column, has the asserted norm bound, and its image under L is a by the spectral identity Q^(1/2)Q^(-1/2)a=a.

The proof never requires Q inverse applied to a to be a Hilbert vector.
The norm on the bounded column is the matrix C*-norm, and the matrix trace throughout is unnormalized.
For n=1 and the full coordinate row, the polar support trace makes the scalar B equal d-1; this agrees with the reused row mechanism.
It does not supply a conclusion for singular B or a construction of coordinate dual maps satisfying all required commutators.

## Source and scope limits

The complete C_F0154 proof and exact C_F0148 Sections 1--2 were checked.
The scalar prototype's separate maximal-Delta and common-left-factor applications were read as context but are not premises of this matrix theorem.
No new external source input, formal verification or numerical evidence is asserted.
Standard bounded matrix spectral calculus, Hilbert weak convergence and rectangular polar decomposition are used at their stated finite-tracial scope.

## Conclusion

The exact statement and entire argument of C_F0154 v1 pass this independent review, with its declared direct dependency applicable and no remaining mathematical gap or source correction found.
This supports a `proved` and `independently reviewed` assessment upon adoption.
The strict B>0 and Q-regular assumptions remain essential to the verified argument; no all-bare-dual existence or unrestricted finite-module range criterion is included.

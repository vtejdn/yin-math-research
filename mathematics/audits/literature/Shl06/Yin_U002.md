---
author: Yin
---

# Shl06: Spectral Truncation of Hilbert--Schmidt Commutators

## Shl06-U002

Source: [Abel Symposium preprint](../../../literature/pdf/Shl06--abel-preprint.pdf), Section 2, Theorem 3, pp. 4--5.
Direct AI review for Yin, 2026-10-10; self-review only.

### Spaces and necessary domain convention

H0 is the HS-norm closure of tuples ([Y,Xj]) with Y bounded and all commutators Hilbert--Schmidt.
H1 is the closed complex span of the corresponding tuples from selfadjoint, possibly unbounded implementers with Omega in their domains.
Selfadjoint means equality to the Hilbert-space adjoint, not merely symmetry on polynomials.
Interpret [A,Xj]=Kj as a bounded form commutator on Dom A (equivalently here, Xj preserves Dom A and the commutator there extends to Kj).
An identity solely on a dense non-core polynomial domain does not supply this interpretation.

H0 is contained in H1: decompose a bounded implementer into its real and imaginary parts; since the Xj are selfadjoint, both resulting commutators are Hilbert--Schmidt.
To prove the other inclusion it suffices to treat one selfadjoint A.
Factors i may be inserted consistently, but the source drops i midway through the p. 5 display; this does not change the norm-convergence argument.

### Reconstructed truncation proof

Choose smooth real f_R equal to x on [-R,R], bounded by R+1 and with |f_R'|<=2.
Such a function is obtained by smoothly decreasing the derivative from 1 to 0 over an interval of length one on each side.
Let g_R(s,t)=(f_R(s)-f_R(t))/(s-t), setting g_R(s,s)=f_R'(s).
Then |g_R|<=2 and g_R=1 on [-R,R]^2, including its diagonal.

Left and right spectral multiplication by A commute on HS, so bounded measurable functions g(s,t) act there with norm at most ||g||infty.
For K=[A,X] in HS the needed identity is

\[
 [f_R(A),X]=g_R(L_A,R_A)K. \tag{1}
\]

The source's claim that it suffices to test polynomials in A on C<X> is not justified: those vectors need not be in Dom A^m.
The following fills that step without imposing such domains.
Set $E_N=1_{[-N,N]}(A)$, A_N=A|E_NH and X_N=E_N X E_N.
The domain/form hypothesis gives [A_N,X_N]=E_N K E_N.
For a polynomial p, telescoping proves [p(A_N),X_N]=g_p(L_A_N,R_A_N)E_N K E_N.
Approximate f_R and f_R' uniformly on [-N,N] by polynomials (approximate its derivative and integrate); their divided differences converge uniformly as well.
The left sides converge in operator norm and the right sides in HS norm, proving the compressed version of (1).

Now E_N tends strongly to 1, E_N K E_N tends to K in HS norm, and ||g_R||infty<=2.
The compressed left side is E_N[f_R(A),X]E_N and converges strongly to that bounded commutator.
The right side converges in HS norm to g_R(L_A,R_A)K.
This proves (1).
Finally bounded dominated convergence for the joint spectral representation on HS gives

\[
 \|[f_R(A),X]-[A,X]\|_{HS}
 =\|(g_R-1)(L_A,R_A)K\|_{HS}\longrightarrow0.
\]

Apply this to finitely many Xj with the same f_R.
Each f_R(A) is bounded, hence the tuple lies in H0 and converges to the original tuple.
Thus H1 is contained in H0, proving Theorem 3 with the explicit domain convention above.

### Limits and downstream use

This is HS approximation of commutator tuples, not operator-norm convergence of A or preservation of finite rank.
It does not construct a bounded dual system whose commutators remain exactly P, nor does it prove that all bounded vectors belong to the dual operators' and their adjoints' domains.
If the source is read as allowing commutation only on an unspecified non-core dense subspace, the proof does not cover that broader interpretation.
No such interpretation is adopted.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Shl06, registered nine-page Abel Symposium preprint.

Passages: Section 2, definitions of H0/H1 and Theorem 3, pp. 4--5.

Inspection: 2026-10-10: statement and full proof read; pp. 4--5 visually checked; spectral-cutoff and C1 approximation repair reconstructed. Audited within the bounded form-commutator convention. The literal polynomial-domain shortcut is insufficient; the weaker-domain interpretation is not verified. No formal or independent review.

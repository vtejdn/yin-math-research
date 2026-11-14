---
author: Yin
---

# Word transport of the free Haar right slice at fixed positive cutoffs

On 2026-11-14T10:38 UTC an agent for Yin independently inspected all conclusions and the whole proof of the [C_F0245 v1 candidate](../../claims/Yin_C_F0245_v1.md#decision-candidate).
The reviewer took no part in developing this argument and received no substantive development discussion, exploration notes, separate author explanation or prior finding about it.

## Finding

For every \(0<s<1\) the word-transported free slice is unbounded on single correlated inputs, both at the unregularized endpoint and at every fixed \(\epsilon>0\).
Subtracting it from the corresponding correlated slice gives an unbounded correction in the same norms.
The finite-column and inverse-gap assertions and both nonclosability statements hold for the specified pair.

**Word identification and witness norms.**
The Poisson density has full support and first moment \(s\).
In the reduced free product the centered Laurent spaces from the two factors inject into their marginal Hilbert spaces, and their alternating algebraic tensors inject into the corresponding mutually orthogonal reduced-word summands.
Thus the only word identifications are the unitary relations, and \(A=U,\ B=U^{-1}V\) is an invertible group substitution with \(V=AB\).
The corresponding substitution in the free Haar representation takes nonidentity words to nonidentity words, so \(a,ab\) are also free Haar generators.
For successively distinct indices, centered conjugates from \(A^kW^*(V)A^{-k}\) have trace zero by cyclicity and reduction with nonzero intervening powers of \(A\).
This includes equal first and last indices, since the reduced product after cyclic permutation may start and end in the \(V\) factor without losing its centered alternating form.

In the representation of the free conjugate factors, multiplication by a centered element \(x_k\) on words not starting in factor \(k\) prepends \(x_k\Omega\), with norm \(\|x_k\|_2\).
These creation ranges are orthogonal, the adjoint calculation for \(x_k^*\) bounds the annihilations, and the remaining diagonal operators act on mutually orthogonal subspaces with norm at most \(\|x_k\|\).
The faithful trace transfers the resulting bound \(2\sqrt n\,\|x\|_2+\|x\|\) to the ambient algebra.
On taking \(x=V-s1\) or \(x=ab\), respectively, the averages \(P_n\) converge in operator norm to \(s1\) or zero.
Thus \(q_n(A,B)=A(P_n(A,B)-s1)\) tends to zero in the required operator norm.
The graph of \(\iota\) has \((0,s1)\) in its closure by \(P_n\), and the graph of \(\iota^{-1}\) has \((0,-s1)\) in its closure by \(P_n-s1\), in the respective Hilbert norms.

**Cutoff trace and the unregularized endpoint.**
The identity \(\gamma=I_{z-w}\delta\) in the cutoff theorem gives inner insertion of \(f_\epsilon=|z-w|^2/(|z-w|^2+\epsilon^2)\) on the coarse tensor before slicing.
On the Haar marginal this is a smooth, even circle function of \(z/w\), with absolutely summable Fourier coefficients, \(d_0>0\) by positive integral, and \(d_0+2\sum_{\ell\ge1}d_{-\ell}=0\) by its value at \(1\).
Termwise insertion into a cut \(h\otimes t\) is valid in the coarse space by absolute convergence and contributes \(d_m h a^m\tau_0(a^{-m}t)\).
Each group suffix \(t\) selects at most one exponent, so the output admits algebraic evaluation at \(A,B\).
The positive \(a\)-cuts of \(a^{k+2}ba^{-k}\) leave one \(b\) in the suffix and give zero.
In the negative tail the \(j\)-th suffix selects \(m=-(k-j+1)\) and the prefix becomes \(a^{k+2}ba^{-(k+1)}=w_{k+1}\) with a minus sign.
Also the free cutoff applied to \(a\) gives \(d_0 1\).
Every evaluated \(w_{k+1}\) has trace \(s\), and Cesàro convergence of the partial sums of the negative Fourier coefficients gives \(\tau(F_\epsilon q_n)\to -s d_0/2\).
For the constant multiplier \(1\), the negative coefficients vanish and \(Fq_n=-s1\) exactly.
These lower bounds use \(|\tau(x)|\le\|x\|_2\) in the correlated representation after evaluation of the output.

**Correlated costs and scope.**
The bounded dual of C_F0057 has \([D_A,A]=P_\Omega,\ [D_A,B]=0\), the commutator orientation of the normalized right slice \(E^{\rm c}\).
Right multiplication by \(D_A1\) is defined on polynomial inputs even when \(D_A1\) is only in \(L^2\).
Subtracting it fixes the vacuum value at zero and preserves both generator commutators and their inverse relations, which proves equality with \(E^{\rm c}\) on words.
The two terms of \((E^{\rm c}p_j)_j\) have direct-sum Hilbert norms at most \(\|D_A\|\|\sum p_j^*p_j\|^{1/2}\) and \(\|D_A1\|_2\|\sum p_j^*p_j\|^{1/2}\), by the probability trace and the left action of the positive sum on \(D_A1\).
The actual coordinate vacuum for these represented unitary generators also follows by taking the vacuum pairing in that equality and using boundedness of \(D_A\) on \(L^2\).
The Haar marginals are diffuse, so C_F0238 yields finite inverse-gap energy and \(\sup_{\epsilon>0}c(E^{\rm c}_\epsilon)\le3c(E^{\rm c})\).
Consequently both intrinsic slices send the witness inputs to zero, proving unboundedness of each stated difference.
The positive-cutoff lower bound depends on \(s,\epsilon\).
The obstruction concerns word evaluation of the free comparison and is compatible with the finite intrinsic column bounds above.
The inspection used the cited project results and source passages at their invoked interfaces without recursively auditing their full proofs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0245_v1.md#statement) | Both nonclosability statements, original costs and energy, and unbounded transport and subtraction for each fixed law and cutoff. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0245_v1.md#argument) | Whole proof through free-conjugate norms, Fourier cuts, correlated trace limits and intrinsic column bounds. |
| [Finding](#finding) | [Correlated pair](../../claims/Yin_C_F0057_v1.md#3-correlated-haar-coordinates-retain-bounded-duals) | Haar marginals and bounded Hilbert duals with the normalized generator commutators. |
| [Finding](#finding) | [Poisson input](../../claims/Yin_C_F0057_v1.md#2-a-free-reference-pair-with-bounded-duals) | Positive full-support density and first moment at the selected \(s\). |
| [Finding](#finding) | [Free-product Hilbert representation](../literature/Voi98/Yin_U005.md#voi98-u005) | Faithfulness on algebraic reduced words and left-end action. |
| [Finding](#finding) | [Ricard–Xu passage](../../claims/Yin_C_F0105_v1.md#1-precise-statement-and-reuse-boundary) | Source identification for the creation, annihilation and diagonal decomposition used in the local length-one proof. |
| [Finding](#finding) | [Liberation cutoff](../../claims/Yin_C_F0238_v1.md#statement) | Inner regularization, inverse-gap necessity and uniform original column estimate under actual ACSY. |

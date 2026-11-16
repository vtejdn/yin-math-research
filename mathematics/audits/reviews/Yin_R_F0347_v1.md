---
author: Yin
---

# Review of the signed Cauchy Gram criterion on finite lattices

## Finding

Review time (UTC) 2026-11-16T19:27.
I independently examined the complete C_F0342 candidate dated 2026-11-16T19:24, including the finite atomic energy calculation, both directions of the universal criterion and the dependence on the number of labels.
I had previously reviewed the lattice reduction C_F0339, was outside development of C_F0342, and received no development dialogue, separate author explanation or preceding finding on C_F0342.
The two identities and both quantitative implications hold as stated.

On this finite label algebra the liberation derivative has algebraic tensor values on core words, and insertion of \(e_i\otimes e_i\) kills each generator.
The endpoint terms in the vacuum pairing at \(e_i p e_i\) cancel, so the diagonal vacuum block vanishes as well.
For real \(x=\sum x_i e_i\) the vacuum of the rank-one insertion on \(i\gamma\) is \(x\zeta x\), with row-minus-column correction zero.
The row of \(x\otimes x\) is \((\tau x)x\); its composition square is \(\|x\|_2^2 x\otimes x\).
The finite-kernel energy and rank-one identities use only the marginal inner difference, the killed coefficient, the actual vacuum and the product rule on this algebra.
The strict binomial series passes their final first-derivative expressions to \(u\), since the derivative of the \(m\)-th power of the strict contraction costs at most \(m\|a\|^{m-1}\) times the first derivative norm.
This step requires neither diffuseness of the partition nor a second derivative evaluation at \(u\).

Write \(V_{ij}=iG_{ij}-u e_j\zeta e_i\), whose right support lies under \(e_i\).
The real part of its pairing with \(iu e_i\) is \(f_{ij}\) off the diagonal, because the trace of \(e_j\zeta e_i\) vanishes.
Splitting the rank-one energy by these right supports gives the quartic polynomial (3), including its positive row correction.
In its coefficient of \(x_i^3x_j\) the norm side is zero.
The terms on the other side are \(-t_i(f_{ij}+f_{ji})+2t_i f_{ij}\), giving symmetry because \(t_i>0\).
The \(x_i^2x_j^2\) coefficient yields the sum of the two ordered norm squares, with vacuum contribution \(2\nu_{ij}\) and row contribution \(2(t_i+t_j)f_{ij}\).
For three distinct indices the \(x_i^2x_jx_\ell\) coefficient on the norm side is twice the real inner product of \(V_{ij},V_{i\ell}\).
On the other side it is \(-2t_i f_{j\ell}+2t_\ell f_{ij}+2t_j f_{i\ell}\), proving (5).

For a real antisymmetric \(b\), summing (4) on unordered pairs with weights \(b_{ij}^2\) gives the diagonal contribution \(\sum b_{ij}^2\nu_{ij}+2\sum t_j b_{ij}^2 f_{ij}\).
The two positive terms from the ordered distinct-index cross sum in (5) combine to \(2\sum b_{ij}(m_i-t_j b_{ij})f_{ij}\).
The negative term is the Gram pairing \(-\sum f_{j\ell}\sum_i t_i b_{ij}b_{i\ell}\), with repeated indices contributing zero.
The terms containing \(t_jb_{ij}^2\) thus cancel, while subtraction of \(i m_i u e_i\) in the row norm cancels the remaining linear term and adds \(t_i m_i^2\).
Distinct ordered vacuum blocks are mutually orthogonal in the trace Hilbert space and orthogonal to the full label diagonal.
Hence the positive scalar budget in that identity is exactly \(\|A_b\|_2^2\).
Summing the identities for the two real components gives the mass-weighted real column Gram matrix and \(Q_c\), with no further mass factors in \(f_{ij}\).
Its quadratic form is the sum of \(t_\ell\) times modulus squares for real inputs, and the nonnegative norm sum in (1) proves \(F_K(u)\le Q_c\).

All budgets \(B_c\) are positive because \(M_i\ge t_i/h\).
A uniform lower bound on \(F_K/B_c^2\) controls the direct-sum norm of the two \(G\) components by \((1+\sqrt{1+d_{\rm G}})B_c\) from (1).
Passing to their complex combination costs \(\sqrt2\), averaging the two analytic signs recovers each strict selfadjoint test, and norm scaling and splitting real and imaginary parts cost at most another factor two.
In reverse, the finite-label word algebra and the analytic test are identical under reflection of the lattice.
The energies \(M_i,\ |H_i|\) and the inverse-gap weights are preserved, while the kernel changes to \(\bar k\).
The original and reflected bounds at that same \(u\) control \(G_{\operatorname{Re} k}+iG_{\operatorname{Im} k}\) and \(G_{\operatorname{Re} k}-iG_{\operatorname{Im} k}\).
Here the unit-ball estimate passes to \(u\) by binomial graph convergence, rescaling each approximating input by its norm when necessary.
The parallelogram law bounds the direct-sum norm by \(K_{\rm lat}B_c\).
Using \(\sum_b\|A_b\|_2^2=Q_c\le B_c^2\) in (1) now yields \(d_{\rm G}\le(K_{\rm lat}+1)^2\).
The two finite-case implications give the extended-real comparison, and the lattice reduction transfers finiteness to the unrestricted normal implication.

Finally (4), after expansion, gives \(Y_{ij}^2\le2\sqrt{2\nu_{ij}}\,Y_{ij}+2(t_i+t_j)|f_{ij}|\).
Symmetry of \(f\) and the two right supports give \(|f_{ij}|\le\min(\sqrt{t_i},\sqrt{t_j})Y_{ij}\).
For \(Y_{ij}>0\) division and squaring are justified, and \((t_i+t_j)^2\min(t_i,t_j)\le2t_it_j(t_i+t_j)\).
Summing the scalar terms on unordered pairs is exactly the ordered sum \(\sum_i t_i^2\sum_{j\ne i}t_j|k_{ij}|^2\).
Dyadic annuli at distances \(2^\ell h\) contribute at most \(2^{1-\ell}M_i/h\) to the inner sum, and \(t_i/h\le M_i\).
Cauchy–Schwarz over at most \(n-1\) indices within each orthogonal right support costs \(n-1\) in the squared norm.
This proves the stated \(C\sqrt{n-1}\) estimate, also covering zero \(Y_{ij}\); the singleton kernel vanishes.
Uniformity as \(n\) varies is the remaining mathematical question.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0342_v1.md#decision-candidate) | Complete candidate dated 2026-11-16T19:24 and all four declared direct dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0342_v1.md#statement) | Two exact norm identities, signed Gram criterion in both directions, general equivalence and bound for each label count. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0342_v1.md#argument) | Full quartic coefficient comparison, row correction, two real components, reflected estimates, analytic tests and annular counting. |
| [Finding](#finding) | [Lattice reduction](../../claims/Yin_C_F0339_v1.md#statement) | Universal lattice problem on the single-input unit ball and its equivalence to the unrestricted normal converse. |
| [Finding](#finding) | [Diagonal labels](../../claims/Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Diagonal insertions kill the core and diagonal liberation-vacuum blocks vanish. |
| [Finding](#finding) | [Uncentered square](../../claims/Yin_C_F0331_v1.md#the-uncentered-square) | Exact rank-one signed identity, composition coefficient, vacuum and row correction before taking bounds. |
| [Finding](#finding) | [Finite-kernel energy](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Actual adjoint and core formulas (B0a)–(B0e), and first-derivative analytic limits for the finite partition. |

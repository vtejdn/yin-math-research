---
author: Yin
---

# Ordinary spectral shifts of cyclic linearizations of scalar polynomials

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance Brown convergence](../tasks/Yin_T_F0012_v3.md#contract) | Full-sequence almost-sure weak convergence for a general fixed polynomial and every permitted cross-size coupling. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | For longer unequal-length words, prove the principal trims and the joint physical corner estimates needed by the single-flag exterior. |

## The full polynomial as one spectral problem

The [cyclic construction](../claims/Yin_C_F0359_v1.md#construction) puts each monomial on a path of the same length, padding with identity blocks and retaining every repeated occurrence of an original matrix.
Closing the paths produces one fixed affine pencil with ordinary spectral parameter \(tI\).
The [finite and free law identity](../claims/Yin_C_F0359_v1.md#statement) recovers the entire scalar Brown measure after the map \(t\mapsto t^D\) and removal of the deterministic zero mass.
The full-sequence weak convergence events are identical for each coupling.
The [earlier corner-parameter linearization](../ledger/Yin_L_F0061_v2.md#linearization-transfer) remains appropriate for transfer of an ordinary determinant at a specified shift.
Its dimension limsup alone does not provide this route's full-sequence probabilistic conclusion.

## A planar test away from the structural zero

For a prescribed disk \(|w|\le R\), take \(\lambda=4(R+1)\) and construct the cyclic pencil \(T\) for \(1+P/\lambda\).
Use the principal branch of \(t=(1+w/\lambda)^{1/D}\).
Its image is compact and stays away from zero and the branch cut.
For a finite or free evaluation use \(U\) for the normalized ordinary logarithmic potential.
Subtracting the free identity from the finite one gives
\[
 U_{P_N}(w)-U_p(w)
 =m\bigl[U_{T_N}(t)-U_{T(s)}(t)\bigr].
\]
The physical area factor is \(dA(w)=\lambda^2D^2|t|^{2D-2}dA(t)\), bounded above and below on this compact set.
This removes the deterministic zero from the parameter region in which the terminal probability estimate is needed.

For nonconstant \(P\), every pencil in this compact set is full: its Schur complement at nonzero \(t\) is a nonzero multiple of a nonzero free polynomial.
The [finite-variance polynomial-window estimate](../claims/Yin_C_F0186_v40.md#argument) supplies the count down to an inverse polynomial at fixed parameters.
The [uniform cutoff theorem](../claims/Yin_C_F0359_v2.md#clip) proves summability of every fixed positive deviation of the \(N^{-B}\)-clipped logarithms uniformly over the whole test region.
It uses the compact-family free count, the shift Lipschitz constant \(N^B\), and row-rank bounded differences after an upper clip of variation \(O(\log N)\).
The remaining target is summability of fixed positive deviations of the integral below \(N^{-B}\),
\[
 \int_{\Omega_R}\frac1{mN}\sum_j
       \log^+\frac{N^{-B}}{s_j(tI-T_N)}\,dA(t),
 \qquad \Omega_R=\{(1+w/\lambda)^{1/D}:|w|\le R\}.
\]
An area estimate must allow the exact finite roots inside the region.
The [terminal equivalence](../claims/Yin_C_F0359_v2.md#equivalence) shows that summability of the positive deviations of these integrals is necessary and sufficient for the all-coupling almost-sure scalar weak limit.
Any one fixed \(B>0\) suffices.
The [unequal-length cubic](../claims/Yin_C_F0359_v1.md#example) provides a test with repeated colors, a constant term, and a nonzero structural atom in the original cyclic realization.
For \(P=1+x^2y+yx\), the [principal-minor theorem](../claims/Yin_C_F0362_v1.md#statement) controls the ordinary scalar potential after deleting just \(h_N\) or \(2h_N\) bottom singular values, \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\), under two real finite-variance input laws.
Its independent-row estimate excludes a vector and its \(Y\)-image from lying nearly in the same two thin spectral windows of \(X\).
Exposing new \(Y\)-columns in the [first physical compression](../ledger/Yin_L_F0069_v1.md#compression) gives two dependent columns per site.
Their [projected area](../ledger/Yin_L_F0069_v2.md#energy) has positive coefficient energy at a nonreal shift, yet on certain deterministic old blocks that area vanishes for every equal-modulus sign column.
Fixing \(Y\) and exposing \(X\) instead gives the [one-direction initial compression](../claims/Yin_C_F0362_v2.md#exterior) and the [three-direction restoration](../claims/Yin_C_F0362_v2.md#restoration).
The [six-panel probability bound](../claims/Yin_C_F0363_v1.md#statement) closes the scalar terminal series.
The [real-axis rectangular test](../claims/Yin_C_F0362_v3.md#statement) also gives the ordinary determinant limsup for every prescribed complex point of this cubic.

For a new cyclic realization, first identify a fresh physical color and a lower-dimensional initial exterior whose full determinant is comparable with the retained product.
Then test whether the physical corner coefficient span contains an invertible matrix after the known scalar and rank errors are removed.
The [fixed-dimensional restoration lemma](../claims/Yin_C_F0363_v3.md#statement) supplies the joint probability estimate when the projected spread, Fourier and actual conditional product hypotheses hold.
The padded constant column in the seven-channel cyclic example has zero variable coefficient, so these hypotheses require an actual reduction of the deterministic directions.
For \(1+x^q y+yx\) with any fixed integer \(q\ge2\), the [longer-word calculation](../ledger/Yin_L_F0069_v3.md#partial) exhibits an exterior with only one initial scalar direction per independent background column.
At every \(w\ne1\) a [sum of scalar pole residues](../ledger/Yin_L_F0069_v3.md#residues) yields an invertible matrix in the tested coefficient directions.
For \(q>2\) the principal trims and joint spread of the actual corner kernels remain to be established.
No terminal estimate for a general cyclic pencil has been deduced from this calculation.

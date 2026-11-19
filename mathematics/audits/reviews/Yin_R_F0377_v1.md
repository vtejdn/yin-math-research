---
author: Yin
---

# Review of the discrete-border matrix detector and covariance test

## Arrangement and fixed inputs

The review was performed at 2026-11-19T16:16 UTC by a separately assigned agent outside the substantive development of the inspected argument.
No proof-development dialogue, author explanation or prior review finding for this argument was supplied or consulted before forming the findings.
The input was [L70v3](../../ledger/Yin_L_F0070_v3.md), in its 19 November 2026 revision, at the five exact sections bound below.
The reviewer read the stated rational-quotient interface and the independent-column argument where they were invoked, but did not re-audit their external source proofs.
This is a bounded mathematical review, not acceptance of the F0012 contract or of an unproved random-matrix extension.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Matrix detector](#matrix-detector-review) | independently reviewed |
| [Covariance test](#covariance-review) | independently reviewed |
| [Elementary border tests](#border-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Matrix detector](#matrix-detector-review) | [Matrix evaluation](../../ledger/Yin_L_F0070_v3.md#matrix-detector) | Generated algebra, characteristic identity, spectrum, projector, partial traces and identity (5). |
| [Matrix detector](#matrix-detector-review) | [Physical Schur detector](../../ledger/Yin_L_F0070_v3.md#physical-detector) | Transpose and color symmetry, scalar quotient, residue scaling, node separation including conjugates, and the algebraic coefficient-image conclusion. |
| [Matrix detector](#matrix-detector-review) | [Joint quotient interface](../../claims/Yin_C_F0363_v4.md#quotient) | Only the finite-dimensional annihilator-duality argument and its realification with conjugate nodes. |
| [Covariance test](#covariance-review) | [Joint covariance](../../ledger/Yin_L_F0070_v3.md#joint-covariance) | Equivalence of covariance and transverse bounds, realification for complex frames, and the stated old-measurability restriction. |
| [Covariance test](#covariance-review) | [Independent subspace tests](../../claims/Yin_C_F0196_v5.md#restricted-small-ball) | The local conditional argument, dimension requirement, normalization and simultaneous use of the same columns; the external small-ball theorem is accepted at its stated scope. |
| [Elementary border tests](#border-review) | [Density obstructions](../../ledger/Yin_L_F0070_v3.md#density-obstructions) | The two finite sign examples and their limited negative implications. |
| [Elementary border tests](#border-review) | [Fresh borders](../../ledger/Yin_L_F0070_v3.md#fresh-border) | Determinant degree, Walsh-fiber bound, two-row border example and Hadamard corank example. |

<a id="matrix-detector-review"></a>
## The detector is valid at the claimed algebraic scope

No gap was found in the displayed algebra.
The products of \(A^2=E_{13}\) and \(B^2=-E_{31}\), followed by multiplication with \(A,B\), recover all matrix units.
Eliminating the first and third channels for nonzero spectral parameter gives identity (4), and its polynomial form extends it to zero.
At the stated symmetric witness, \(YX-XY=-2K\), with eigenvalues \(2i,-2i\), gives the four distinct nonzero eigenvalues of \(Q\).
Its zero eigenspace has dimension two, so the stated fourth-power expression also gives the sum of the nonzero spectral projectors.
The left and right eigenvectors, the normalization \(lr=4\), the \(K\)-weighted partial trace \(F\), and \(BFA-AFB=iI_3/2\) were checked directly.

The test matrix \(H\) is symmetric under the ordinary transpose, although \(K\) is antisymmetric.
Consequently \(\operatorname{Tr}(H\operatorname{sym}\mathscr M)=\operatorname{Tr}(H\mathscr M)\), and block multiplication gives precisely the difference in (6), with no missing factor of two.
Its zero diagonal removes all diagonal-square terms.
The functional also vanishes on physical scalar blocks, since \(\operatorname{Tr}K=0\).
Replacing the cross-color physical test by the identity instead yields the sum of the two cross-color products; at this residue its middle auxiliary diagonal entry vanishes.
Thus the antisymmetric physical test is compatible with the actual symmetric quadratic observation and has a substantive role.

For \(z\ne0\), the pole at \(t=z/\lambda\) has residue \(-P_\lambda/\lambda\), so multiplication by \(-\lambda\) gives the stated invertible detector \(iI_3/2\).
Another node has a pole there exactly when its ratio to \(z\) belongs to \(\{1,-1,i,-i\}\).
Applying this exclusion to the complete finite node list, including conjugates, removes only a finite union of real algebraic null sets.
The substitution \(x=tX,y=tY\) respects transpose reversal because \(X,Y\) are symmetric; it tests rational identities and makes no claim that the substituted matrices are samples of the random model.
Taking the residue of a relation in the joint rational-kernel quotient therefore annihilates its scalar part and every other node and pairs the selected node with \(iI_3/2\).
The finite-dimensional annihilator argument then gives the stated coefficient-image membership, and retaining conjugates permits realification.

Here the quotient is the quotient of formal rational kernels by scalar physical kernels.
The review does not interpret it as the quotient of numerical matrices at a fixed realized exterior, where additional accidental relations can occur.
The argument gives neither a random physical-corner lower bound nor an independent-panel polarization estimate, selected-volume restoration, initial-trim theorem or general irreducible-pencil detector theorem.
The thin-support comparison is only contextual; no new Brown-convergence class is certified by this finding.

<a id="covariance-review"></a>
## The covariance reduction respects the exposure restriction

The block covariance, its Schur complement (8), and its identification with the square of the transverse map are correct for a real symmetric \(B_0\) and a complex orthonormal frame \(Q_0\).
Writing \(S\) for that Schur complement, one has
\[
 TT^*=\begin{pmatrix}I&0\\C&I\end{pmatrix}
       \begin{pmatrix}I&0\\0&S\end{pmatrix}
       \begin{pmatrix}I&C\\0&I\end{pmatrix},
 \qquad C=C^*.
\]
The norm bound for the inverse triangular factor is at most \(1+\|C\|\), which gives exactly the stated lower bound.
Testing a covariance lower bound on \((-Cu,u)\) gives the claimed converse, with no loss needed for \(S\succeq\eta I\) when \(TT^*\succeq\eta I\).

For complex frames and real signs, the independent-column estimate is applied through the real span of the real and imaginary parts of the coefficient subspace.
Its real dimension is at most twice its complex dimension; this is the realification already used in the cited local argument.
Whitening does not justify treating the real and imaginary coordinates as independent.
Under old-block measurability and the stated small dimension-to-column ratio, the conditional estimate and union bound give \(4e^{-ck}\) for the two spaces, even when the same columns are used on both sides.
Thus the stated choice of \(k\) gives the advertised polynomial rate, subject to the availability of that many fresh columns.
If \(B_0\) preserves the frame range, then \(S=0\), so oversampling cannot repair the covariance deficiency.
Nothing in this calculation permits a tested space to depend on the same fresh columns or permits absent colors to be added as fresh randomness.

<a id="border-review"></a>
## The elementary examples have the stated limited consequences

The normalized two-by-two coefficient example generates the full matrix algebra and has identity coefficient Gram, while its determinant vanishes at all four sign pairs with gradient norm \(\sqrt2\).
The parity example has one-bit changes of modulus two and mass one half at its smaller value.
Both negative conclusions are finite conditional-statistic obstructions and do not refute an asymptotic Wigner theorem.

Every fresh variable in a determinant term meets a new row or column, giving the bound \(2mh\) before Boolean reduction and hence afterwards.
A nonzero Walsh coefficient of maximal degree has no strict-superset contribution after conditioning on outside signs.
The resulting fiber average proves (1), but provides no coefficient-size bound or repetition/amplification theorem.
For the two-row example, \(XX^{\mathsf T}=\left(\begin{smallmatrix}h&s\\s&h\end{smallmatrix}\right)\) gives (2), and singularity is exactly the event that the \(h\) independent row-products are all equal.
The one-column enlargement has rank exactly two for every indicated sign column and every \(d\).
Finally, the Sylvester-Hadamard identities put \(N-2\) eigenvalues of \(W_0\) in \(\{1,-1\}\), with its remaining eigenvalue \(-d\), so the coranks are exactly \(N-2\) and \(N\) as claimed.
This rules out deterministic corank persistence on all supported completions without excluding an averaged or typical-exterior argument.

The optional arithmetic route, RV09 source claims, public-search conclusions, and the proposed continuation were not reviewed.

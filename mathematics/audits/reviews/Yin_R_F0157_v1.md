---
author: Yin
---
# Independent review of the finite curvature triangle bound and all-degree Wick action

Review performed and recorded: 2026-10-14T20:27.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and exact inputs

The reviewer first read the complete fixed C_F0149 v1 and all three direct inputs, reconstructed every calculation, and then checked the exact change to [C_F0149 v2](../../claims/Yin_C_F0149_v2.md).
The latter initial decision is dated 2026-10-14T20:26.
The mathematical difference is deletion of one inaccurate final vacuum-coefficient comparison; statement, displayed formulas and all other proof steps are unchanged.
The historical v1 assertion is retained and assessed below.

The normal-branch author developed the triangle inequality and full Wick calculation; root proposed the finite-model diagnostic.
The reviewer received their assignment summaries but did not develop this construction and did not read its D10 development.
Earlier reviewer contributions to the different Haar/Poisson tests in D13 and the target resolvent obstruction C144 are development, not independent review of those results.
They are not inputs to this finite semicircular triangle theorem.
C142's unchanged realized-model construction, previously independently reviewed by this agent, is reused only at its exact declared scope.

The normalization issue below was found after reconstructing the formulas.
The author then clarified that the intended vacuum was that of the gamma contraction, acknowledged the action-coefficient distinction, and issued v2 after root required preservation of v1.
That clarification is disclosed, not used as mathematical evidence.
The normalization is independently computed below.
The corrected version deletes a nonessential assertion; it does not add a proof supplied by this reviewer.

## Current relationship clarification

The retained arrangement says the reviewer received the developers’ assignment summaries, but does not retain their actual content sufficiently to distinguish fixed target/proof information from additional substantive author-development summaries.
Both the v1 normalization finding and v2 whole-proof conclusion therefore have an unknown current initial-context relationship.
This is not inferred self from the word summary or from earlier work on other proofs.
The subsequent author explanation of the intended vacuum, given after the initial normalization calculations, remains disclosed at its actual point in the sequence and does not establish the missing initial isolation.
V2 deletes an unused inaccurate comparison and supplies no new reviewer-authored proof; this record does not establish a repaired theorem chain requiring a separate repair finding.
Original mathematical calculations, negative v1 scope, passing v2 scope and dates remain unchanged.

## Review relationships

| Review | Relationship |
| --- | --- |
| [V1 normalization finding](#v1-normalization-finding) | unknown |
| [Conclusion](#conclusion) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [V1 normalization finding](#v1-normalization-finding) | [C_F0149 v1 argument](../../claims/Yin_C_F0149_v1.md#argument) | The final comparison between the S-path lowering action coefficient and the actual weighted liberation vacuum; the phase and path-mass distinction requires correction. |
| [Conclusion](#conclusion) | [C_F0149 v2 statement](../../claims/Yin_C_F0149_v2.md#statement) | Actual finite tracial model for every n, positive entrywise symmetric coefficients, complex first-Wick vectors, uniform constant-one curvature estimate, exact full-degree core action, and all stated nonclaims. |
| [Conclusion](#conclusion) | [C_F0149 v2 argument](../../claims/Yin_C_F0149_v2.md#argument) | Complete substitution/vacuum, D3 positive semidefiniteness, D4--D6 trace factors and operator-norm control, relative Wick normalization, D7--D10 including degrees zero through three, and precise remaining all-unitary limitations. |
| [Conclusion](#conclusion) | [C_F0146 argument](../../claims/Yin_C_F0146_v1.md#argument) | Actual finite-coefficient reciprocal substitution and bounded-vacuum prototype. The extension to all n and the present coefficients is checked locally rather than imported from its three-block special case. |
| [Conclusion](#conclusion) | [ACSY24-U004](../literature/ACSY24/Yin_U003.md#acsy24-u003) | Equation (1), actual tensor-adjoint domain for finite bounded core factors, after checking both free-reference vacua. No other assertions or uncertainties of that unit are used. |
| [Conclusion](#conclusion) | [NS06-U003](../literature/NS06/Yin_U004.md#ns06-u004) | Exact semicircular mixed-moment equation (14.5), conditional second/fourth moments and derivation of the relative Wick recurrence. The local Wick formulas are not represented as a separately printed theorem in the source. |

## V1 normalization finding

The final displayed S-path action coefficient is correct.
Set

\[
 d_{aij}=a_{ij}/a_{ai}-a_{ai}/a_{ij},\qquad
 \eta_g=(i\gamma)^*g=S_g\zeta.
\]

The correct vacuum relation is

\[
 C_g^*1=\gamma^*g=S_g[R,T]=i\eta_g.
\]

In the second S-Wick expansion the coefficient of C_g*1 is g_aj d_aij, whereas the lowering action coefficient is m_i m_j times that number.
The coefficient of eta_g has the additional factor -i.
Thus v1's unqualified identification with the actual weighted liberation vacuum is not an exact assertion under its stated normalization.
It does not affect D1--D10 or the theorem, because no proof step uses that comparison, but it is mathematical content and is not silently rewritten as wording maintenance.

V2 deletes only that comparison.
The exact physical diff was checked: the only other changes are its initial assessment date and revision explanation.
This resolves the finding without altering any estimate or action formula.
V1 retains this limitation; the passing conclusion below applies to v2.

## Actual represented model and the vacuum

Entrywise reciprocal substitution is inverse to the N-linear block substitution S to T: multiplying by p_i and p_j recovers each block separately.
Symmetry of the real coefficients preserves adjoints.
Faithfulness of the reduced free-product representation supplies the algebraic reference core; no extra relations are presumed absent after an unchecked quotient.
Thus gamma is represented on precisely the common N,S and N,T core.

The free-reference liberation has zero vacuum, while the semicircular derivative has actual vacuum S.
Reduced centered words and the scalar semicircular word-cut pairing give these identities on the entire reference core.
Inserting Q and applying the exact tensor-adjoint formula yields gamma*1=RT-TR.
Its scalar correction terms cancel after summing m_i p_j-m_j p_i.
Multiplication by -i gives the stated bounded real vacuum zeta.
The argument works for every finite n and requires no positive-semidefinite hypothesis on the coefficient matrix a.

Every finite marginal tensor lies in the actual adjoint domain by that same formula.
For real symmetric g the marginal row/column correction vanishes.
Diagonal blocks of [R,T] are zero since a_ik=a_ki.
Off diagonal, its coefficients are minus kappa_i(u,v); division by the nonzero spectral gaps therefore gives D1 and the bounded formal vector xi.
This vector is not an actual conjugate variable for the atomic coordinate.

## Triangle inequality and the uniform first-degree estimate

For D3, twice the quadratic-form matrix is exactly H: each vertex first has diagonal coefficient 2, while adding half the opposite ratio difference squared changes it to s_vw squared divided by 2.
Each off-diagonal matrix coefficient is -s_uv/2.
Hence H represents twice the full expression, also for complex B.

The ratio identity x squared+y squared+z squared-xyz=4 follows by expanding the six ratios.
Each of x,y,z is at least 2, and yz>=x, xz>=y, xy>=z give all two-by-two principal minors.
The direct determinant is x squared y squared z squared minus x to the fourth minus y to the fourth minus z to the fourth minus 2xyz.
Substituting the ratio identity gives the displayed 2 pair-sum minus 10 square-sum plus 24.
Writing the three squares as 4+d turns it into 6 times the d-sum plus 2 times the d-pair-sum.
Thus every principal minor is nonnegative and H is positive semidefinite.
This proves the inequality without assuming that B is real or has any sign.

For off-diagonal endpoints u,v, the fourth-moment pairing of the paths p_u S p_i S p_v is delta_ik m_u m_i m_v.
The other noncrossing-pairing term vanishes because p_u p_v=0.
This proves D4, including its ordered-pair convention.
Direct differentiation of p_i S p_j gives D4a: the first projection term has centered trace zero, the last projection term cancels the constant part of the inserted gamma S term, and the remaining ratio is a_iu/a_ij in the stated order.
Pairing against V and symmetrizing g gives D5 with its factor one half.

Inserting the curvature weight and grouping one unordered triple counts its three unordered edges exactly once.
D3 assigns the negative coefficient to the opposite edge before any term is discarded.
The elementary Menger estimate c_uvw squared<=4/|z_v-z_w| squared therefore gives the factor 2 in D6.
The ordered-pair norm in D4 is twice its unordered-pair sum, so the final constant is exactly one.

Finally, the free conditional second moment gives E_N(VV*)=sum_i(sum_u m_u|b_iu| squared)p_i.
Positivity and contractivity bound its largest coefficient by ||V|| squared, including nonselfadjoint V with arbitrary complex coefficients.
This proves the entire stated first-Wick estimate.
Collinear configurations and fewer than three atoms give zero curvature and are covered without division by curvature.

## Relative Wick normalization and all boundary degrees

The source pairing recursion gives the stated Wick paths, their orthogonality, and squared norm equal to the product of all path masses.
For degree two, the only subtraction is delta_(i0,i2) m_i1 p_i0; the general displayed recurrence inserts this same first-edge contraction.
Induction leaves only complete matching of the indices in an inner product of equal-degree Wick paths, while different degrees are orthogonal.
The triangular leading terms ensure that these paths span the full core.

Rescaling by the product of adjacent a coefficients yields D7.
Its annihilation coefficient is m_i0 a_i0i1 squared because the two occurrences of the first edge have equal coefficients by symmetry.
At degree zero only creation occurs.
This checks the covariance normalization rather than assuming chaos invariance of the proposed operator.

R_g and K_g preserve the initial projection in every positive degree, including when K_g reaches degree zero.
The Hilbert--Schmidt commutator Theta(I_g gamma(p_l)) vanishes on all positive Wick degrees by orthogonality to N.
On degree zero, direct substitution into D8 gives precisely that commutator.
Also R_g1=0 and K_g1=0.

The remaining commutator is checked at each boundary:

- Degree zero: final-index replacement commutes with the creation sum in T, and K_g vanishes before and after this single creation.
- Degree one: the degree-zero annihilation term produces exactly m_i m_j sum_u g_uj(a_iu squared-a_ij squared)p_u in [R_g,T].
  Applying K_g to the degree-two creation terms produces its negative; T K_g is zero.
- Degree two: R_g commutes with both first-edge terms.
  K_g after creation agrees coefficient by coefficient with creation after K_g; K_g after first-edge annihilation is zero, and multiplication of its degree-zero output has no annihilation part.
- Degree three: the two annihilation orders both give the product of m_i0 a_i0i1 squared and the same final-two-edge deletion coefficient.
  Their common surviving path is the degree-zero projection at the second vertex.
  Creation also commutes.
  Higher degrees have the same first/last-edge computation with no new boundary.

Thus [R_g+K_g,T]=0 on the entire core.
Its commutators with N and its value at 1 agree with the actual contraction.
Induction on words in the generating N,T algebra proves D10.
No boundedness on H, extension to all M, or invariant-chaos assumption was inserted.

Dividing the T-path scaling factors gives the final displayed S-path lowering coefficient, including m_i m_j and the ratio difference in the stated order.
R_g correspondingly has the same final-edge ratio matrix as D5.
Neither observation controls the cross-degree K_g pairing on arbitrary analytic unitaries.
The statement correctly leaves that issue open.
For a selfadjoint first-Wick V, centeredness removes the linear scalar term in the small analytic-unitary expansion, and anti-reality removes the extra real quadratic vacuum term; this only identifies the second variation and does not imply an all-parameter bound.

## Source limits and conclusion

The three exact inputs were read at their declared scopes.
The retained NS06 passages had also been directly read during this agent's preceding C142 review; that reading and U003 supply the mixed-moment interface, not a new audit of the complete book proof.
ACSY's exact tensor-adjoint formula is reused at U004's recorded scope.
No new source acquisition, numerical experiment or formal verification is claimed.

## Conclusion

**The complete C_F0149 v2 statement and argument pass independent review, with all three direct dependency scopes covered.**
V1 retains the normalization finding above.
The proven result is the uniform first-relative-Wick curvature estimate together with the exact all-degree algebraic action, not an all-unitary estimate or an actual normal ACSY theorem.
No mathematical change beyond the recorded v2 deletion is required for this scope.

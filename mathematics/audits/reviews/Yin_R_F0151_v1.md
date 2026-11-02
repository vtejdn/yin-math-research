---
author: Yin
---
# Independent review of the nonlinear free ACSY example with a non-L2 inverse

Review performed and recorded: 2026-10-14T19:06.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0144 v1](../../claims/Yin_C_F0144_v1.md).
Root assigned the fixed candidate and disclosed the general-branch author's development of the letter-count adjoint estimate, inverse expansion and both target vacua.
The complete candidate selected by its initial decision dated 2026-10-14T19:01 and both exact direct inputs were examined.
No general-branch D12 or proof-generation discussion was read, and no concurrently developed contraction lemma was used.

Immediately before this review, this agent developed a separate weighted-liberation test in D_F0004 for the correlated Haar/Poisson family.
That work is not independent review and disqualifies this agent from independently reviewing its own resulting proof.
It is disjoint from the present semicircular relative-letter adjoint construction and is not an input here.
This distinction is disclosed rather than inferring independence from the agent role alone.

This review covers every statement and argument section of C_F0144: exact free normalization and reference vacua, singular marginal integrability, relative Fock grading with unrestricted zero letters, actual adjoint domains on complete degree sectors, coarse inverse factorization and integrability, both graph-convergent series, their coefficient order, all target adjoint pairings and the explicit A-only scope.
The accepted C_F0142 criterion, previously independently reviewed by this agent, is reused unchanged.
Miy22-U001 is reused at its recorded source-foundation and inspection boundary; no new source PDF or proof-assistant verification is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0144 statement](../../claims/Yin_C_F0144_v1.md#statement) | Every real c>6, positive regular h with unbounded non-L2 inverse, generation of the nonlinear tuple, actual A witnesses and both explicit conjugate vectors, without a selected F or S conclusion. |
| [Conclusion](#conclusion) | [C_F0144 argument](../../claims/Yin_C_F0144_v1.md#argument) | Complete reference and density calculation, letter-count actual adjoint estimate, bounded coefficient actions, coarse inverse integration and order, both reference adjoint graph series and transfer to the dense target core. |
| [Conclusion](#conclusion) | [Miy22-U001](../literature/Miy22/Yin_U001.md#miy22-u001) | Variance-one free semicircular Fock model, faithful trace, word Chebyshev orthonormal basis, creation/deletion actions and recurrence. The new partial-letter adjoint estimate is checked below, not attributed to the source as a printed theorem. |
| [Conclusion](#conclusion) | [C_F0142](../../claims/Yin_C_F0142_v1.md#statement) | Generation and the unique represented target restrictions, with existential A exactly equivalent to actual target-adjoint membership of 1 and C*. Its separate Hilbert-Schmidt range result is not used. |

## Reference pair and singular marginal

The source Fock model has variance one, so each semicircle has support [-2,2] and the shifted density in (5) is the stated probability density on [0,4].
It has no atom at zero and has support reaching zero.
Thus h is positive regular and h inverse is unbounded.
Near zero its density is comparable to the square root of t; multiplication by t to the power -2 makes the inverse-square integral diverge.
In contrast S is bounded below by c-2>0.

The word-cut formula for either letter puts the tensor vacuum in the actual adjoint domain: pairing a word derivative against the tensor vacuum selects precisely the word consisting of that single letter.
Its representing Hilbert vector is s_i.
This checks the actual reference conjugate system for the shifted pair, not only a formal Gaussian assertion.
The shifts do not change the polynomial algebra or either difference quotient.
Hence every reference hypothesis of C_F0142 is satisfied, and that accepted result supplies generation and the exact target derivation/adjoint criterion used later.

## Relative letter grading and actual adjoint domains

The recurrence U_(iw)=s_i U_w-delta_(i,w_1) U_(tail w) follows from the source word basis and the left creation/deletion action.
Differentiating that recurrence groups the terms at every occurrence of letter 1; the additional leading term appears exactly when i=1.
This verifies (51) by induction, including words with no letter 1 and arbitrary runs of letter 0.

For each fixed j+k=n, the map e_u tensor e_v to e_(u1v) is a bijection of orthonormal bases onto H_(n+1): every output word has a unique cut at its (j+1)st letter 1.
Thus V_(j,k) is an onto unitary even though each source and target space permits unrestricted zero letters.
No bound on total word length is needed.

Testing an arbitrary vector in K_n against each polynomial and using (51) gives the candidate adjoint value as the sum of its n+1 V_(j,k) images.
Cauchy--Schwarz bounds this vector by sqrt(n+1) times the norm of the input.
The bound makes the pairing a genuine bounded H functional, proving actual adjoint membership for every vector of the complete closed K_n, not merely for finite word combinations.
Outputs of different n lie in orthogonal H_(n+1).
Summing those estimates proves (53) on K_<=n with exactly the same maximal constant.

Left and right multiplication by s_0 only create or delete a zero letter.
Their selfadjoint actions therefore reduce each H_n, and bounded spectral calculus in s_0 preserves these spaces as well.
Left or right multiplication by s_1 changes the number of ones by exactly plus or minus one whenever the term is nonzero.
Under the opposite-algebra identification, left multiplication on the second opposite factor is right multiplication on the original second H factor; the same count bound applies.
Bounded joint functions of the two h copies consequently preserve K_<=n, while one occurrence of s_1 in either leg raises its maximum index by at most one.

## Coarse denominator and exact inverse order

The two copies of h are commuting positive regular operators in N.
Their sum G is positive regular, and its inverse is the joint multiplier 1/(s+t).
Bounding each shifted density by pi inverse times the square root of its variable gives an integrable upper bound for the squared norm of G inverse.
Under u=s+t and v=s/(s+t), the Jacobian is u, so the integrand square-root(st)/(s+t) squared times ds dt becomes square-root(v(1-v)) du dv.
Its domain lies in 0<u<8 and 0<v<1, proving (54).
This does not imply square integrability of either individual inverse.

The ratios A=s/(s+t), 1-A=t/(s+t) are bounded between zero and one, and H_0=st/(s+t) has norm at most two.
Each s_1 has norm two.
Therefore the sufficient estimate norm(Z)<=6 is valid.
Multiplication of (55) by G on the right gives s_1 h tensor 1, 1 tensor (h s_1) opposite and i h tensor h opposite.
The second product has that order because of opposite multiplication.
Adding cG yields precisely the displayed F, so

\[
F=(c+Z)G,\qquad F^{-1}=G^{-1}(c+Z)^{-1}.
\]

This is an equality in the finite affiliated algebra and identifies the same inverse as C_F0142.
Since c>6, the resolvent factor has its norm-convergent Neumann series.
Taking the adjoint reverses the order: its terms are c to the power -n-1 times (-Z*) to the power n, followed on the right by G inverse.
This is exactly eta_n in (57).

## Both actual reference-adjoint graph series

Bounded joint spectral truncations approximate G inverse in L2(N), and all belong to K_0.
Left multiplication by Z* consists of one s_1 multiplication followed or preceded by bounded h functions, plus a zero-degree term.
Hence each application raises the maximal relative degree by at most one.
Passing the bounded truncations to their L2 limit puts eta_n in the closed K_<=n.
Its norm is at most (g/c)r to the power n, with r=6/c<1.

Equation (53) therefore gives actual adjoint values with the bound sqrt(n+1)(g/c)r to the power n.
Both the input series and the image series converge absolutely in their Hilbert norms.
The actual reference adjoint is closed, so the partial sums give a graph limit and beta* belongs to its domain.
This uses its full actual adjoint graph, not a merely formal application of the word formula to an infinite series.

The coefficient C and its adjoint have at most two occurrences of s_1 in each elementary tensor term in total; all intervening h coefficients have zero relative degree.
Left multiplication by C* sends K_<=n into K_<=n+2 and has norm at most norm(C).
Applying (53) again gives exactly the sqrt(n+3) bound in (59).
Thus the second series converges in the same actual adjoint graph, with limit C*beta*.
This step independently verifies the h-coordinate test and is not inferred from the first vacuum test.

The proof only requires fixed c>6, so all geometric series converge even though their constants may grow as c decreases toward six.
No endpoint c=6, optimal threshold, or bound in total s_0-degree is asserted.

## Actual target pairings and conclusion A

Every target polynomial lies in the reference polynomial algebra.
Its reference derivative and C are bounded, while beta is in L2(N).
Cyclicity of the finite trace with one L2 factor therefore gives both pairings in (60).
In particular

\[
\langle C^*,(\partial_1p)\beta\rangle
 =\tau(C(\partial_1p)\beta)
 =\tau(\beta C(\partial_1p))
 =\langle C^*\beta^*,\partial_1p\rangle.
\]

The order C*beta* is essential and is the one whose actual graph membership was proved.
The two reference adjoint values represent bounded H functionals on the dense target star algebra.
Hence 1 and C* truly belong to the actual target adjoint domain, with exactly the stated values.
C_F0142 now supplies the full existential A conclusion and the unique conjugate vectors in (61).
Their norm bounds are the displayed absolutely convergent series, plus norm(s_0)_2 for the h coordinate.

This construction never differentiates S with an unknown target derivation and never assumes that beta is bounded.
It also uses no contraction theorem for coefficients depending on s_1.
The present estimates establish the two actual vacuum vectors; they do not establish operator-norm-to-H bounds for the target contractions or a full-M dual system.

## Local reference correction and limits

The final paragraph of the proof refers to the unbounded-inverse tuple as (50), but the tuple in this fixed candidate is numbered (1).
This is a stale display-number reference, not a mathematical change.
Replacing (50) by (1) in that sentence is meaning-preserving locator maintenance and requires no new mathematical version or whole-proof recheck.

Both direct inputs are matched to their exact scopes.
The Miy22 word and trace interfaces retain the foundational source boundaries recorded in U001.
C_F0142 is used only for generation, represented restrictions and the exact two actual-adjoint tests; its independent Hilbert-Schmidt range conclusion is irrelevant to this proof.
The disjoint normal weighted-liberation development in D_F0004 and root's pending relative-degree contraction work are not inputs.

## Conclusion

The complete mathematical statement and argument of C_F0144 v1 pass this independently organized review.
No mathematical gap, missing direct input, degree-count error, coefficient-order error or actual-adjoint-domain mismatch was found.
The single stale equation reference above should be corrected as presentation maintenance.
This finding supports proved / independently reviewed when adopted by the responsible Claim decision.

The supported result is the actual ACSY-positive nonlinear free tuple for every c>6, with h inverse not in L2 and both explicit actual conjugate vectors.
No F or S conclusion, separation of conditions or general goal completion is included.

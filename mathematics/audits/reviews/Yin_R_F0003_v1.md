---
author: Yin
---

# Yin_C_F0004: Independent Review of the One-Normal-Generator Proof

Reviewer: the reviewing agent, 2026-09-08.
Reviewed artifact: the complete proof and one-coordinate compression corollary now in [Yin_C_F0004](../../claims/Yin_C_F0004_v1.md#yin_c_f0004).
The independent review originally inspected the mathematical text before registry headers were added; the root checked that the canonical proof and corollary are unchanged.
This reviewer did not author that proof.
This is an internal AI mathematical review, not formal verification, external peer review, or a novelty assessment.

**Result:** the reverse implication and the asserted degree bound are valid under the stated Yin_C_F0001 hypotheses; no unresolved proof gap was found.
Together with the existing Yin_C_F0002 forward implication, the proof establishes the complete d=1 case and the stated corollary for f in a single W*(X_j) inside a general tuple.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original one-generator finding](#decisive-checks) | unknown |
| [Exact-rank refinement finding](#independent-review-of-the-exact-rank-refinement-2026-09-09) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original one-generator finding](#decisive-checks) | [C_F0004 Statement](../../claims/Yin_C_F0004_v1.md#statement) | Original one-normal-generator reverse implication, upper rational-degree bound and coordinate-compression corollary; this first finding does not establish the later exact-rank equality. |
| [Original one-generator finding](#decisive-checks) | [C_F0004 Proof](../../claims/Yin_C_F0004_v1.md#proof) | Original four proof steps and coordinate corollary with nonatomic law, L2 kernel, rational columns and bounded denominator; no claim about arbitrary multivariable f. |
| [Exact-rank refinement finding](#independent-review-of-the-exact-rank-refinement-2026-09-09) | [C_F0004 Statement](../../claims/Yin_C_F0004_v1.md#statement) | Added exact rank=max(deg p,deg q) for reduced nonconstant scalar rational functions, including the pole at infinity and separate constant case. |
| [Exact-rank refinement finding](#independent-review-of-the-exact-rank-refinement-2026-09-09) | [C_F0004 Proof](../../claims/Yin_C_F0004_v1.md#proof) | Compatibility with the unchanged original finite-rank/kernel proof used in the refinement; this contributor finding is not a fresh independent review of that older proof. |
| [Exact-rank refinement finding](#independent-review-of-the-exact-rank-refinement-2026-09-09) | [C_F0004 exact refinement](../../claims/Yin_C_F0004_v1.md#exact-rank-refinement-and-the-kronecker-comparison) | Complete polynomial separation and reduced-quotient uniqueness argument; coordinate compression retains only its original upper bound. |

The original 2026-09-08 finding records a separate nonauthor reviewer, but does not establish whether the relevant substantive development context was inherited.
Its relationship is therefore unknown under the current isolated-context rule; the old independent description, actual date and mathematical checks remain historical facts.
The 2026-09-09 refinement reviewer authored the original one-generator argument used in the refinement and therefore shared relevant substantive mathematical context.
That finding is self-reviewed under the current rule, without changing its actual date, calculations, accepted result or original limit concerning the older proof.
This declaration maintenance performs no new mathematical review and does not infer either relationship from C's retired aggregate field.

## Decisive checks

1. Since X is normal and M=W*(X), the spectral theorem genuinely gives an abelian multiplicity-one tracial representation L-infinity(S,mu) on L2(S,mu).
   Faithfulness makes S=supp(mu) the operator spectrum; boundedness makes S compact.
   No assumption that holomorphic polynomials are L2 dense is used.
2. An atom gives a nonzero spectral projection E with E[D,X]E=0, whereas EPE has eigenvalue mu({lambda}) on E Omega.
   Therefore the measure is nonatomic.
   This also justifies nullity of the diagonal and of every finite set later removed.
3. The commutator sign in `TX+fP=Pf+XT` is correct.
   Hence `[T,X]=[P,f]`.
   Its Hilbert-Schmidt kernels are `(w-z)K(z,w)` and `f(w)-f(z)`, so the displayed divided-difference kernel has the correct sign.
4. Only T is finite rank or Hilbert-Schmidt; D is not assumed to admit a kernel.
   A finite-rank operator has a finite L2 tensor kernel with conjugates absorbed into the b_j factors.
   Equality of operators implies equality of these L2 kernels because the kernel/Hilbert-Schmidt map is injective.
5. Fubini gives one full-measure set of column parameters on which all finitely many kernel factors and f have finite values and the required L2 column equality holds.
   Nonatomicity guarantees r+1 distinct choices.
   A finite intersection of the corresponding full-measure sets of row parameters is still full measure, so the chosen linear dependence can be multiplied by the common polynomial denominator.
6. The polynomial B is nonzero: evaluating at any selected w_i with c_i nonzero kills all other terms and leaves a nonzero product.
   This is the decisive nondegeneracy check; no point-evaluation of the original almost-everywhere identity is taken.
7. Cancellation does not increase either degree and gives a reduced scalar rational function.
   A genuine pole at any support point forces unbounded modulus on a punctured neighborhood.
   That neighborhood has positive mu measure because it meets the support and the center has no atom; removal of the almost-everywhere exceptional set cannot restore essential boundedness.
   Consequently the reduced denominator is zero-free on the entire compact spectrum, and its inverse is bounded in M.
   The argument reaches exactly the original scalar division closure, with no matrix or affiliated substitution.
8. Rank zero is correctly treated separately by `[P,f]=0`, which implies f Omega=tau(f) Omega.
   In the abelian standard representation this gives scalar f; the written argument is valid.
   The zero-function convention avoids an unnecessary degree-of-zero-polynomial assertion.
9. In the corollary, L2(N_j) reduces the left action of N_j because both a and a* preserve it.
   Its projection therefore commutes with X_j and f.
   Compression preserves the rank-one dual relation and cannot increase commutator rank.
   The restricted trace is faithful normal finite and N_j=W*(X_j), so the one-generator theorem applies with all hypotheses.
   The resulting inverse in N_j remains the inverse in M.
   Yin_C_F0002 supplies the converse for every i, completing the claimed equivalence on each coordinate subalgebra.

## Limits retained

The calculation `[T,X]=[P,f]` uses fX=Xf and does not establish a multi-generator converse for arbitrary f.
The degree statement is an upper bound only, as recorded.
No kernel for the original dual, no polynomial graph-core result, no boundedness of arbitrary L2 factors, and no claim about the adjoint-adjoined variant enter the proof.

## Artifact Integration

Goal [Yin_T_F0001](../../tasks/Yin_T_F0001_v1.md#yin_t_f0001) remains open; this proof settles only its stated special case.
No numerical computation, proof assistant, or external human review was performed.

## Independent Review of the Exact Rank Refinement, 2026-09-09

Reviewer: another AI agent.
Reviewed artifact: [the current Yin_C_F0004 proof](../../claims/Yin_C_F0004_v1.md#yin_c_f0004).
The scope of this independent review is the strengthened rank statement and the new section "Exact Rank Refinement and the Kronecker Comparison," authored by the coordinating agent.
This reviewer authored the original one-generator argument, so this is not presented as an independent review of that older argument.
Direct text comparison confirms that its four proof steps and coordinate-compression corollary remain unchanged.

**Result:** the refinement is valid.
For a nonconstant reduced quotient f=p/q with q zero-free on the spectrum, rank[D,f]=max(deg p,deg q).
This supersedes the earlier **upper-bound-only limitation** in this audit; the preceding dated assessment and both historical inspection scopes remain records of the versions inspected.

The decisive checks are as follows.

1. The existing forward implication makes r=rank[D,f] finite before the older degree estimate is invoked.
   If its constructed reduced quotient and the given p/q agree mu-almost everywhere, their polynomial cross-product vanishes identically: otherwise its finite zero set would have full measure, contradicting nonatomicity.
   Uniqueness of reduced one-variable quotients then gives max(deg p,deg q)<=r.
   No pointwise identity on every support point is assumed.
2. With n=max(deg p,deg q), the numerator p(z)q(w)-p(w)q(z) is divisible by z-w.
   The quotient is polynomial, of degree at most n-1 in z.
   It is symmetric in z,w, so it has the same degree bound in w.
   Expanding in the n powers 1,z,...,z^(n-1) gives the displayed separation into at most n factors.
   Since q has no zero on compact S, every divided factor is bounded and therefore belongs to L2(mu).
3. The older identity (w-z)K=f(w)-f(z), together with nullity of the diagonal, uniquely identifies the finite-rank commutator's Hilbert-Schmidt kernel.
   Consequently the new separated expression is the actual kernel of [D,f], not an unrelated operator with a similar difference identity.
   It yields r<=n for every bounded dual covered by the statement; no explicit kernel of D is required.
4. Cancellation is performed before degrees or poles are counted.
   The argument covers polynomial functions, proper rational functions, and rational functions with polynomial parts.
   Constants, including zero, are separately assigned rank zero.
   For a reduced nonconstant quotient, the finite poles have total multiplicity deg q and the pole at infinity has order max(deg p-deg q,0), so the total is n.
   In particular, f=X has rank one despite having no finite pole.
   The comparison with Miy22's strictly proper Laurent convention retains this distinction.

No change to Yin_C_F0001's multi-generator scope or to its original scalar division closure follows from the refinement.
The coordinate corollary retains its asserted upper degree bound relative to the uncompressed commutator; this addition does not silently replace that compression inequality by an unproved equality.
This was a mathematical review plus a text-preservation check, not a numerical proof, formal verification, external human review, or novelty assessment.

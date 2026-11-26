---
author: Yin
---

# All simple twenty-sixth cyclotomic markings through the finite cutoff

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{26}\) with marked images \(1,10\), respectively, and suppose \(s\) has infinite order.
Put \(N=[H,H]\), \(M=N_{\rm ab}\), \(S=\operatorname{Ad}_s\) on \(M\), and \(M_{26}=M/\Phi_{26}(S)M\).
Suppose \(M_{26}\) has a simple quotient of prime characteristic \(p\le725547\).
Then for complex two-by-two corners \(A,B,C,D\) all invertible with \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible, the regular nullity of \(B+At-s(D+Ct)\) is at most \(217/442<1/2\), using the unnormalized coordinate trace.
The bound tests the indicated finite quotients under these coefficient assumptions and does not assume regular scalar injectivity.

## Genuine orbit exponents

By the [cyclic commutator calculation](Yin_C_A0230_v1.md#simple-quotients-and-their-marked-characters), the quotient by \([N,N]\) is \(M\rtimes C_{26}\) and \(u=ts^{-10}\) generates \(M\) as a cyclic module.
For a simple quotient \(E\) write \(\alpha\) for the inverse of the multiplier of \(S\).
If \(p\ne2,13\), then \(\alpha\) is a primitive twenty-sixth root in the field \(E=\mathbb F_p(\alpha)\), of degree \(d=\operatorname{ord}_{13}(p)=\operatorname{ord}_{26}(p)\).
At \(p=2\) the polynomial is \(\Phi_{13}\bmod2\), irreducible of degree twelve, and at \(p=13\) it is \((X+1)^{12}\), with the single simple root \(-1\).
On 26 indices let \(P\) be the forward shift.
For any \(\mathbb F_p\)-linear functional and \(e_i=\lambda(\alpha^i)\), the marked images \(P,\ P^{10}\operatorname{diag}(w^{e_i})\) are actual unitary representations at the \(p\)-th roots of unity.
Indeed the diagonal character at coordinate \(i\) evaluates on \(S^{-i}b\) for \(b\in E\); using \(t=us^{10}\) introduces a fixed nonzero multiplier in this functional.
This proves the orbit formula in the indicated order, including the two special characteristics.
In particular \(e_{i+13}=-e_i\bmod p\), with the same formula in characteristic two.

We use two certificates.
First, on \(0\le i<13\) put \(b_i=[(-1)^ie_i]_p\), using representatives in \(\{0,\ldots,p-1\}\).
If all \(b_i>0\) and \(\sum_{i<13} b_i\le3p\), use the integer exponents \((-1)^i b_i\) on these indices and their negatives on the second half.
Apply the [alternating-sign character calculation](Yin_C_A0210_v1.md#a-representation-test-for-a-single-finite-character): the negative source indices are preserved by addition of ten.
The constant positive columns come from \(B-sPD\), which is invertible over the cyclic field of \(s\) by evaluation at the formal value \(s=0\).
After multiplying on the left by its inverse and eliminating the positive columns, the remaining principal submatrix of \((B-sPD)^{-1}(A-sPC)\) specializes to copies of \(B^{-1}A\) at \(s=0\), before the invertible right permutation and \(t\)-translation.
The actual infinite order of \(s\) permits this field calculation in its regular representation.
The individual column widths yield \(26p\,\delta\le4\sum_{i<13} b_i\), so \(\delta\le6/13<217/442\).
At \(p=13\), taking \(\alpha=-1,\ \lambda(1)=1\) gives \(b_i=1\) and even \(\delta\le2/13\).

Second, use \(m=p\) and the initial centered weights if \(a=0\).
For a nonzero integer \(a\), take \(m=26p,\ w=z^{26}\) at \(z^m=1\) and tensor the representation with the cyclic character of weights \(ap,10ap\).
In both cases write \(q=ap\) for the exponent on \(s\).
The exponent \(v_i\) on \(t\) in source \(i\) is congruent to \(e_i\bmod p\) in the first case and to \(10ap+26e_i\bmod m\) in the second.
Arbitrary representatives of these congruences preserve every unitary evaluation, including the tested changes by \(m\) or \(-m\) at source zero.
For \(k=0,1,10,11\) the respective block offsets, exponents and ordered group-ring coefficients are
\[
     (0,0,B),\qquad(1,q,-sD),\qquad(10,v_i,At),\qquad(11,q+v_i,-sCt).
\]
They give a Laurent polynomial with all \(m\) true phase nullities equal to \(26\delta\).

## Full matched endpoints and coverage

The [finite verifier](../computations/programs/Yin_J_A0009/verify_phi26_remainder.mjs) computes minimum and maximum matching costs \(L,U\) for these 26 rows and columns and verifies an actual primal matching and feasible dual prices attaining equality at both ends.
At one end it checks each strongly connected component of the tight graph, identifying each matched row with its input.
A singleton has a translated invertible corner as its diagonal block.
For a complementary pair the offsets from one source are \(0,1\) and from the other \(10,11\) to the same two rows, with all four arrows tight.
Up to reordering, the block is \(\operatorname{diag}(I,-sI)\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\operatorname{diag}(tI,I)\), a group-ring unit.
Such components in triangular order give a boundedly invertible endpoint, hence an injective specialization at a nonzero parameter by norm continuity.
For the same weights the verifier checks \(884(U-L)\le217\cdot26m\).
The [two-end interpolation bound](Yin_C_A0219_v1.md#statement) gives \(26m\,\delta\le2(U-L)\), as required.

The [factor calculation](../computations/programs/Yin_J_A0009/phi26_factors.mjs) checks at every odd prime \(p\ne13\) in the interval that its list of monic degree-\(d\) factors has product exactly \(\Phi_{26}\bmod p\).
Since this polynomial is separable and every primitive root has Frobenius degree \(d\), this certifies that each possible marked irreducible factor appears exactly once.
Given one such factor \(F(X)=X^d+\sum_{j<d}F_jX^j\), prescribing the initial values on the basis \(1,\alpha,\ldots,\alpha^{d-1}\) defines \(\lambda\).
The verifier uses \(e_{i+d}=-\sum_{j<d}F_j e_{i+j}\bmod p\), checking periodicity and antiperiodicity.
The [retained computation](../computations/programs/Yin_J_A0009/readme.md#all-simple-factors-on-twenty-six-coordinates-through-725547) records the complete prime and factor counts and the two certificate types.

At \(p=2\) take the twelve initial coordinates \((0,\ldots,0,1)\), \(a=2\), and centered representatives modulo 52.
The two costs are \(-208,104\), with both endpoints certified, giving \(6/13\).
Together with the single \(p=13\) factor and the 194943 factors at the other 58455 primes, the full calculation treats 194945 marked factors at 58457 primes.
No bound on a simple module's size is used to omit a marking from this interval.

## Assessment history

### Decision the-full-finite-interval-of-twenty-sixth-components

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:44 |
| status | proved |
| reason | Independent full reproduction and proof review established the asserted bound at all characteristics and marked factors in the interval. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform finite-cutoff estimate and coefficient hypotheses. |
| argument | [Genuine orbit exponents](#genuine-orbit-exponents) | All field degrees, the two exceptional characteristics and the signed weights. |
| argument | [Full matched endpoints and coverage](#full-matched-endpoints-and-coverage) | Both types of certificate, exact endpoints and complete finite coverage. |
| review | [The full finite interval of twenty-sixth components](../audits/reviews/Yin_R_A0198_v1.md#the-full-finite-interval-of-twenty-sixth-components) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-full-finite-interval-of-twenty-sixth-components)

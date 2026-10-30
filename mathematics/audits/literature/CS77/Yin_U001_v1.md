---
author: Yin
---

# Fuglede Commutation for Bounded Maps from M to H

## CS77-U001

Source: [CS77, published article](../../../literature/pdf/CS77.pdf), Crabb and Spain, Glasgow Mathematical Journal 18 (1977), 197--198, DOI 10.1017/S001708950000327X.
The registry (private lookup: `../../../literature/registry.md#cs77-retained`) owns the retained artifact and acquisition facts.

Locator: opening Banach-space conventions, Proposition 1 and the immediately following kernel consequence, printed p.197 / PDF p.1.

Record: 2026-10-14, direct text reading and visual inspection by the authoring AI agent for Yin.
State: Read; the statement and bounded-map specialization are checked.
The published input is accepted for the specified use; no independent or full source-proof audit is claimed.

### Statement and hypotheses

For a complex Banach space V, an operator A is hermitian when exp(itA) is an isometry for every real t.
A normal operator has the form N=R+iJ with commuting hermitian R,J, with conjugate N^#:=R-iJ.
The source uses N^* for this conjugate; it is not the Banach dual operator.

Proposition 1 states that if Q is quasinilpotent, N=R+iJ is normal, NQ=QN and (N+Q)^2 v=0, then Rv=Jv=0.
Taking Q=0 gives the following consequence, also stated after the proposition: Nv=0 implies N^#v=0.

The opening definition prints "commuting normal operators" for R,J.
The application below uses commuting hermitian operators, with their isometry property verified directly, and therefore uses the standard Banach-space normality convention made explicit above.
No conclusion relies on an alternative interpretation of that printed phrase.

### Bounded-map specialization

Let M be a finite von Neumann algebra with faithful normal tracial state tau, and put H=L2(M,tau), with M acting by left multiplication.
Let x in M be normal and let T:M to H be linear and bounded for the operator norm on M and the Hilbert-space norm on H.
Put
\[
 h:=(x+x^*)/2,\qquad k:=(x-x^*)/(2i),\qquad
 V:=\mathcal B(\mathcal M,H).
\]
Define bounded operators on V by
\[
 (RS)(z):=hS(z)-S(hz),\qquad
 (JS)(z):=kS(z)-S(kz).
\]
Normality of x gives hk=kh, hence RJ=JR.
Moreover
\[
 (e^{itR}S)(z)=e^{ith}S(e^{-ith}z),\qquad
 (e^{itJ}S)(z)=e^{itk}S(e^{-itk}z).
\]
Unitary left multiplication is an isometry on both M and H.
These two transformations and their inverses preserve the norm of S, so R and J are hermitian on V.
Thus N:=R+iJ is normal in the source's Banach-space sense.

Assume T(xz)=xT(z) for every z in M.
This is precisely NT=0.
Proposition 1 with Q=0 gives RT=JT=0, and hence
\[
 0=((R-iJ)T)(z)=x^*T(z)-T(x^*z).
\]
This verifies the stated bounded-map specialization.
The source states a more general Banach-space result rather than this M-to-H specialization verbatim.
No bounded extension of T to H is required.
This specialization alone supplies no closability, closed-graph argument or Kaplansky-density extension for other operators.

### Inspection and limits

The proposition's proof was read for its reduction to a normal quasinilpotent restriction.
Its cited foundations in Bonsall--Duncan, Section 38, and Dowson--Gillespie--Spain, Lemma 3, were not re-audited.
In the Q=0 application, the latter commutation step is immediate.
The accepted published statement, rather than a new independent verification of those foundations, supplies the input.

The user's renewed search for a Fuglede theorem on bounded maps between the stated spaces led to the Banach-space formulations.
Queries included Fuglede, Banach spaces, hermitian operators and intertwining.
Search stopped after the published Proposition 1, its kernel consequence and the above specialization were checked.
No priority or literal-statement claim is made, and no computation or formal verification was performed.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | CS77, published Cambridge-hosted article, Glasgow Mathematical Journal 18(2) (1977), 197--198; retained as CS77.pdf. |
| source-locator | Opening conventions, Proposition 1 and following kernel consequence; printed p.197 / PDF p.1. |
| inspection | Direct statement and surrounding-convention reading, visual page inspection, partial proof reading, and complete check of the bounded-map specialization on 2026-10-14. Original cited foundations and the whole article were not independently audited. |

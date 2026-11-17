---
author: Yin
---

# Independent review of the linear survivor bound and short-cycle packing

At 2026-11-17T06:34 UTC an agent outside the development of the proof reviewed the complete statement and three proof sections of Yin_C_A0090_v1 for Sheng Yin.
The reviewer received the fixed argument and review assignment without development dialogue, author explanations or an earlier verdict on the claim.
The review includes the final wording specifying an ordinary outgoing stub in the fold conclusion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0090_v1.md#statement) | Survivor counts, fixed-tuple alphabet probability, disjoint cycles, fold count and the asphericity hypotheses. |
| [Whole-argument finding](#whole-argument-finding) | [Neutral occurrence folds](../../claims/Yin_C_A0090_v1.md#folding-all-neutral-occurrences-before-reducing-modulo-two) | Stub budget, homological edge-loss bound, parity losses and the separate ordinary outgoing folds. |
| [Whole-argument finding](#whole-argument-finding) | [Local degree average](../../claims/Yin_C_A0090_v1.md#averaging-the-local-degrees-when-the-subalphabets-are-free) | Hypergeometric isolation, convexity, exact numerical signs and conversion to survivors. |
| [Whole-argument finding](#whole-argument-finding) | [Packing](../../claims/Yin_C_A0090_v1.md#packing-cycles-with-one-sampled-alphabet) | Entropy, deletion losses, rounding, cyclic reduction and independence of the lifted classes. |
| [Whole-argument finding](#whole-argument-finding) | [Coarse types](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Private points, neutral inverse pairs and ordinary incidence on each side. |
| [Whole-argument finding](#whole-argument-finding) | [Thirteen-position populations](../../claims/Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms) | Recovery of the same coarse counts on projection. |
| [Whole-argument finding](#whole-argument-finding) | [Odd-stub graph](../../claims/Yin_C_A0085_v1.md#statement) | Actual original-group fibers, reverse stub bijection and nonemptiness. |
| [Whole-argument finding](#whole-argument-finding) | [Local degree bounds](../../claims/Yin_C_A0085_v1.md#the-neutral-degrees-on-the-four-lines) | Lower degree at odd and active even fibers, including the weight-256 equality case. |
| [Whole-argument finding](#whole-argument-finding) | [Sampling](../../claims/Yin_C_A0088_v1.md#sampling-inverse-pairs-and-counting-nonisolated-vertices) | Forest inequality and erased-fiber surplus expectation. |
| [Whole-argument finding](#whole-argument-finding) | [Surplus and short cycles](../../claims/Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets) | Fixed-tuple probability, entropy estimate and scope of the subalphabet event. |
| [Whole-argument finding](#whole-argument-finding) | [Lifted cone injection](../../ledger/Yin_L_A0052_v1.md#a-homological-rejection-test-under-the-source-safeguards) | Designated side, inclusion of a possibly disconnected subgraph and edge-kernel dimension. |
| [Whole-argument finding](#whole-argument-finding) | [Translated summands](../../claims/Yin_C_A0066_v1.md#the-finite-tensor-calculation) | Connecting isomorphism with both graph families at all actual deck indices. |

## Whole-argument finding

The complete argument proves the statement for the given tuple under its indicated hypotheses.
At each of the three even forward colors, exactly \(4\cdot126\) private signed ordinary points lose one copy while each neutral point initially has \(129n/(7\cdot16513)\) copies.
The six active and three mixed ordinary points are absent from this neutral total, leaving \(16504\) signed letters.
The finer state changes sum to the same private-point deficit on either side.
For an odd fiber, a minimum-weight line retains at least 124 neutral points and the next possible weight is at least 133.
For an even fiber of nonzero weight, equality at 256 gives a symmetric difference of two lines containing at most four active points and at most three mixed points.
The next possible weight is at least 258, giving the same lower degree 249 after all nine exclusions.
The parity of the total private-stub count ensures \(v>0\), even in a fully erased color.

The map of the full neutral source subgraph onto its image surjects on the two chain groups.
Asphericity makes the fixed side inject on \(H_1\) of the Cayley graph, so a nonzero element of the edge kernel cannot have zero boundary.
The kernel dimensions give \(E-E'\le M-f\), with all \(M\) occurrences still present.
Each preimage edge beyond the first contributes two signed-end repeats, including when its image is a loop.
For a multiplicity \(k\), loss on passage to parity is at most \(2(k-1)_+\).
Consequently the degree sum is at least \(16504(129/16513)(M+4)-504-4(M-f)>124M+4f\), since \(16504\cdot129>128\cdot16513\) and \(4\cdot128>504\).
Using \(f\ge v\) and the degree cap \(16504\) gives \(16500v>124M\).
Independently of this argument, an erased fiber contains two occurrences whose lines share an ordinary point, including when the lines coincide.
Their two outgoing stubs with that same signed label belong to different source edges because the reverse of a stub has a different formal label.
The resulting unoriented edge accounts for at most two fiber labels, proving the rounded \(f/2\) bound.
The reverse stub can be extra if the shared point is one of the three mixed ordinary points.

Sampling inverse pairs counts both ends of loops correctly in \(\mathbb E d'_g=62d_g/8252\).
For \(d_g<8191\), the exact probability of missing the incident pairs is the product of the successive conditional miss probabilities, each bounded below by \(1-d_g/8191\).
For \(d_g\ge8191\) the positive-part lower bound is zero.
In the freely marked case every sampled subgraph is a forest, so expectation followed by convexity gives \(\phi(\sum_g d_g/v)\le0\).
I checked by rational arithmetic that \(\phi'(124)>0\), \(\phi(124)>-3/10\), \(\phi(216)>0\) and \(\phi(249)>4/25\).
Thus the degree sum is below \(216v\), which gives \(v>31M/53\).
Separately, summing the two pointwise lower bounds for \(\phi(d_g)\) gives \(0>(4/25)(v-o)-(3/10)o\).
The final product of the two fractions is \(248/1219>1/5\).
The geometry and alphabet hypotheses refer to the one tuple and apply to all six color and side choices.

At full erasure the normalized surplus \(X\) of C88 satisfies \(\mathbb E X>1/16\) and \(X\le124\).
The probability of \(X\ge1/32\) exceeds \(1/4000\) because \(1/32+124/4000<1/16\).
Fix a draw on this event.
While the remaining surplus is at least \(v/64\), removing isolated vertices gives average degree at least \(2+1/64\).
Pruning leaves preserves a core of at least that average.
A loop or parallel pair supplies a short cycle directly.
In a simple core the uniform directed edge is stationary under nonbacktracking steps, and convexity of \(d\log(d-1)\) on \(d\ge2\) gives average conditional entropy at least \(\log(65/64)\) per step.
With the stated \(j\), distinct endpoints of every continuation from each initial edge would bound conditional entropy by \(\log n<j\log(65/64)\).
A collision of reduced paths yields a simple cycle of length at most \(2j+2=H\).
Deleting its vertices in the remaining graph removes at most \(124H\) edges, so the surplus falls by at most \(248H\), even after new isolated vertices are discarded.
At termination the total decline exceeds \(v/64\), giving at least \(\lceil v/(15872H)\rceil\) disjoint cycles from this single draw.

Each simple cycle, including a loop or parallel pair, reads a nonempty cyclically reduced null word because there is a unique outgoing edge with any given signed label at a Cayley vertex.
The disjoint edge supports give independent binary cycles in the graph, where there are no two-boundaries.
Under asphericity the universal cover has both \(H_2=0\) and \(H_1=0\), giving bijectivity of the relative connecting map and independence of the unique preimages in the full translated sum.
The size estimate \(v>31(n/7-4)/4125\) and \(H=O(\log n)\) give the asserted order of packing.
Independence concerns actual lifted chains, and the only probability in this packing argument is the probability of the alphabet draw on the fixed erased tuple.

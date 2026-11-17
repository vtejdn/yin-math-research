---
author: Yin
---

# Reviewing the 62-pair forest and short-relation test

At 2026-11-17T06:22 UTC an agent outside the development of Yin_C_A0088_v1 independently reviewed the fixed statement and all three proof sections for Sheng Yin.
The reviewer previously inspected the restricted-alphabet and marked-systole arguments in their respective claims.
The inputs here were the fixed proof, its direct mathematical references and the requested scope.
No proof-development dialogue, author explanation or earlier verdict on this claim was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0088_v1.md#statement) | Per-realization survivor, exponential-in-systole and short-relation bounds on either side, and the separate high-probability assertions. |
| [Whole-argument finding](#whole-argument-finding) | [Odd stub counts](../../claims/Yin_C_A0088_v1.md#the-graph-of-odd-stub-counts) | Projective line code, neutral inverse pairs and the graph of actual group labels. |
| [Whole-argument finding](#whole-argument-finding) | [Sampling and forests](../../claims/Yin_C_A0088_v1.md#sampling-inverse-pairs-and-counting-nonisolated-vertices) | Isolation estimate, numerical margins, forest surplus and breadth-first path count. |
| [Whole-argument finding](#whole-argument-finding) | [Finite relations](../../claims/Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets) | Positive proportion, finite marked word length, four prescribed pairs of inverse pairs, and transfer to the two laws. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line counts](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Inverse pairing, private-point counts and six forward-color choices across both sides. |
| [Whole-argument finding](#whole-argument-finding) | [Individual line code](../../claims/Yin_C_A0085_v1.md#projective-incidence-at-an-individual-group-element) | Odd blocking weight and minimum even line-code weight, independently checked from the direct polynomial argument. |
| [Whole-argument finding](#whole-argument-finding) | [Private-edge counts](../../claims/Yin_C_A0078_v1.md#a-finite-cycle-from-the-four-private-lines) | Odd total guaranteeing a nonempty graph in each selected color. |
| [Whole-argument finding](#whole-argument-finding) | [Restricted stages](../../claims/Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction) | First-power turn-weight saving and the modified pattern estimate. |
| [Whole-argument finding](#whole-argument-finding) | [Capped pictures](../../claims/Yin_C_A0059_v1.md#capped-pictures-with-an-outer-segment-in-the-chosen-letters) | Exclusion of arbitrary-length null words with a restricted outer reading. |
| [Whole-argument finding](#whole-argument-finding) | [Fine-state stages](../../claims/Yin_C_A0078_v1.md#excluding-private-relations-with-few-changes-of-line) | Fixed state size, deterministic propagation from initial states and subexponential perturbation factors. |
| [Whole-argument finding](#whole-argument-finding) | [Marked systole](../../claims/Yin_C_A0071_v1.md#short-words-separating-original-labels) | Logarithmic marked systole on the fixed-state high-probability event. |

## Whole-argument finding

The stated obstruction and bounds follow under their respective deterministic and probabilistic hypotheses.
Each line occurrence pairs oddly with every projective test line, including itself.
Consequently an odd multiplicity meets every line, and counting incidences gives at least \(\lceil16513/129\rceil=129\) support points.
A nonzero even line sum of weight below 256 has an empty line, since otherwise each line has at least two incidences.
In coordinates with that line at infinity the homogeneous sum of 127th powers vanishes there, and restriction to \((X,1,0)\) gives a zero polynomial of degree below 128.
Divisibility by the infinity coordinate leaves an affine polynomial of degree at most 126 with at least \(128^2-126\cdot128=256\) nonzeros.
This uses the individual word's membership in the line span.
Removing the six active points and three ordinary partners of extras leaves at least 247 neutral stubs at each nonempty even word, or 120 at an odd word.
Actual inverse-stub bijections give matched parities at both oriented ends of each retained edge, including loops with two signed ends.
The odd private-stub total \(n(129/16513)/7-1\) makes the graph nonempty.

Uniform sampling of inverse pairs gives expected degree \(62d_g/8252\), counting both ends if both local signs belong to one pair.
There are at most \(d_g\) incident pair types, so for \(d_g\le280\) the isolation probability is at least \((7911/8191)^{62}>7/64\).
Checking the constants by integer arithmetic, the two lower bounds for the expected local surplus are \(4921/66016\) and \(459/4126\), each strictly greater than \(1/16\).
The integrand is always at least \(-1\).
On a free selected alphabet each simple graph cycle would give a nonempty cyclically reduced null word, including cycles of one or two edges in the labelled multigraph.
In this forest the sum of degrees \(2|E|\) is at most twice the number of nonisolated vertices.
Averaging forces \(y\ge1/17\).
Distinct nonbacktracking paths from one start of lengths at most \(\lfloor(l-1)/2\rfloor\) cannot agree at their ends without producing a nonempty cyclically reduced null word of length less than \(l\).
The degree bound 120 gives at least \(119^{\lfloor(l-1)/2\rfloor}\) vertices before multiplication by the survivor fraction.

On a completely erased fixed tuple the normalized expected surplus exceeds \(1/16\).
Since \(1/32+124/4000<1/16\), more than a \(1/4000\) fraction of alphabet draws have normalized surplus at least \(1/32\).
Omitting isolated vertices only increases the resulting average degree bound \(2+1/32\).
Pruning leaves from a component of average degree above two, or from the full graph while counting the remaining vertices, preserves the positive excess and yields a nonempty core with at least that average degree.
The uniform directed-edge distribution is stationary for uniform nonbacktracking continuation in this core.
Convexity of \(x\log(x-1)\) for \(x\ge2\) gives conditional entropy per step at least \(\log(\bar d-1)\).
If the core has girth greater than \(2j+2\), all \(j\)-step continuations from a fixed directed edge have distinct end vertices, giving entropy at most \(\log n\).
The chosen \(j=\lceil\log n/\log(33/32)\rceil+1\) violates this bound, and \(2j+2\) is exactly the claimed word-length cutoff.
The four-pair inclusion union bound is \(3782/17021813<1/4000\).

For the original law the C59 event covers all the indicated alphabets.
For each fixed thirteen-position law, the eligible letters have trivial lamp and coarse increments on both sides.
Each allowed ordinary turn has limiting weight \(1/129\), hence the 124 possible starts and at most 123 continuations give exponential decay of the first-power word-weight sum.
This is the restricted-bin input to the dominant-block estimate of C59.
In the nonregular state systems the propagation from one initial state per component remains deterministic, and the bounded state powers and \(\exp(o(L))\) perturbation errors of C78 preserve that saving.
For an all-alphabet outer word the capped-picture estimate takes unrestricted outer length zero, precluding every nonempty cyclically reduced relation on the strengthened event.
There are only \(\binom{8252}{62}\) alphabets, independent of \(n\), and the marked-systole event has the same girth-conditioned law.
Their intersection therefore gives the asserted simultaneous polynomial survivor bounds.
The probability over sampled alphabets on a single erased tuple was derived before any law on tuples was introduced.

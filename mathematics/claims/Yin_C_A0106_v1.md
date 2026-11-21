---
author: Yin
---
# Outermost coefficients in the seven-generator normal form of Gardam's group

## Statement

Let \(\Gamma\) be the two-generator group identified with the seven-triangle presentation in [C_A0105_v2](Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
In this claim \(|g|\) denotes length in the **seven** positive triangle generators \(a,\ldots,g\) and their inverses.
Use the positive-then-negative normal words of the [complete rewriting system](Yin_C_A0105_v2.md#a-finite-complete-rewriting-system).
The right normal form for triangle groups of this building type also appears in [Cartwright--Młotkowski, §6, (6.1)](../literature/pdf/CM94.pdf).

Let \(k\) be a field, and let \(A=\sum_x A_x x\) have finite support in \(M_{d,n}(k[\Gamma])\), where \(d,n\ge1\).
Suppose its largest occupied length \(m\) is positive and that every occupied word of length \(m\) is purely positive.
Write \(T\) for this set of words.
For a first symbol \(j\), positive, inverse or empty, let \(T_j\) consist of the \(x\in T\) for which appending \(j\) is irreducible, and set \(T_\varnothing=T\).
If
\[
                 \bigcap_{x\in T_j}\ker(A_x:k^n\longrightarrow k^d)=0
                 \qquad\text{for every }j,                    \tag{1}
\]
then \(A\) has trivial kernel on finitely supported column vectors \(k[\Gamma]^n\).
For an empty family the intersection means the whole source.

For scalar \(A\), let \(L\) be the set of terminal letters of \(T\).
For a positive letter \(y\), put \(P_y=\{p:pyz\text{ is a cyclic triangle for some }z\}\).
Condition (1) holds if \(L\) lies in none of the seven sets \(P_y\).
Every support meeting this condition has a uniquely represented product with **every** nonempty finite right support.
In particular any element supported on four or more of the seven positive generators, or on three positive generators forming none of the sets \(P_y\), has this property.
The same criterion allows arbitrary lower-length terms and arbitrary nonzero scalar coefficients.

Over \(\mathbb C\) the proof gives an exact formula for the norm of the outermost layer of a product, with a lower bound uniform in the largest length of the finite input.
These statements concern finite inputs; the kernel dimension for general \(\ell^2\) inputs remains undetermined by this argument.

## Argument

The rewriting system terminates, is confluent and never increases length.
Its irreducible representative therefore realizes the seven-generator length.
The inverse-positive rule and cancellation prohibit every change of sign from negative to positive in an irreducible word.
At the boundary between a purely positive word and an arbitrary normal word, the only possible rules are a shortening positive-positive triangle or a cancellation of inverse letters.
In particular a reducible boundary shortens the word strictly even if subsequent reductions preserve length.

Write \(B=\sum_w b_w w\in k[\Gamma]^n\) and take \(B\ne0\).
Set \(h=\max\{|w|:b_w\ne0\}\) and let \(j(w)\) be the first symbol of the normal representative, with \(j(1)=\varnothing\).
For \(|w|=h\) and \(x\in T_{j(w)}\), concatenation gives an irreducible word of length \(m+h\).
If \(x'w'\) is any other pair of support elements with the same product, subadditivity forces \(|x'|=m\) and \(|w'|=h\).
Thus \(x'\) is also purely positive, and a reducible join would make the product shorter than \(m+h\).
The concatenation of \(x'\) and \(w'\) is consequently the same normal word.
Splitting it at position \(m\) recovers \(x'=x\) and \(w'=w\).
Conversely every product at length \(m+h\) comes from exactly such a pair, by the same length argument.
Hence its vector coefficient is precisely \(A_x b_w\).
For each occupied \(w\) of length \(h\), (1) supplies an \(x\) for which that vector is nonzero.
This proves finite-support injectivity and, for the scalar assertion, uniqueness of at least one product for each maximal \(w\).

For positive \(y\), the eligible terminal letters are precisely those outside \(P_y\).
For an inverse initial letter \(y^{-1}\), the only forbidden terminal letter is \(y\).
The cyclic shifts of \(acb,add,afg,bbf,cef,cdg,eeg\) give, in order of \(y=a,b,c,d,e,f,g\),
\[
    P_y=\{b,d,g\},\ \{b,c,f\},\ \{a,f,g\},\ \{a,c,d\},\
          \{c,e,g\},\ \{a,b,e\},\ \{d,e,f\}.                  \tag{2}
\]
Each letter occurs in a set in (2), so a terminal set lying in none has at least two distinct letters and there is an eligible one at each inverse initial letter as well.
For scalar nonzero coefficients this gives (1), including the empty initial word.
Each set in (2) has three letters, giving the asserted examples.

Finally let \(k=\mathbb C\), write \(\Pi_t\) for restriction to the length-\(t\) sphere, and put \(G_j=\sum_{x\in T_j}A_x^*A_x\).
The distinct normal words just proved give the identity
\[
    \|\Pi_{m+h}(AB)\|_2^2
        =\sum_{|w|=h} b_w^*G_{j(w)} b_w
        \ \ge\ \bigl(\min_j\lambda_{\min}(G_j)\bigr)\|\Pi_h B\|_2^2 .
\]
The minimum is positive under (1), since the list of symbols is finite and each Gram matrix is then positive definite.
Only the outermost layer of a finite input enters this calculation.

## Assessment history

### Decision outer-layer

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:20 |
| status | proved |
| reason | Independent verification covers the metric, the rewriting inputs, all first letters and finite-input layer norms. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Outermost coefficient formula, scalar unique products with every finite right support and matrix injectivity under the stated terminal condition. |
| argument | [Proof](#argument) | Classification of all maximal-length pairs and the exact Gram matrix formula. |
| review | [Whole finding](../audits/reviews/Yin_R_A0143_v1.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Exact normal forms](Yin_C_A0105_v2.md#decision-exact-balls) | The identification of the presentations and the length-nonincreasing complete rewriting system. |

## Current assessment

[Selected decision](#decision-outer-layer)

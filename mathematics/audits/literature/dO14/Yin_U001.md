---
author: Yin
---

# Local real solutions with an invertible partial Jacobian

<a id="do14-u001"></a>
## Real implicit function theorem

Let \(F\) be a continuously differentiable map from an open subset of \(\mathbb R^n\times\mathbb R^m\) to \(\mathbb R^m\).
Suppose \(F(a,b)=0\) and the partial derivative \(D_yF(a,b)\) in the last \(m\) variables is invertible.
Near \((a,b)\) the zero set is the graph of a unique \(C^1\) map \(y=f(x)\) with \(f(a)=b\).
In particular the solution exists for every \(x\) in one neighborhood of \(a\) and tends to \(b\) as \(x\to a\). [Theorem 5, printed page 214](../../../literature/pdf/dO14.pdf#page=8)

The hypotheses and the \(C^1\) graph conclusion were checked on the rendered page of the [journal edition](readme.md#journal-edition).
The source also gives the derivative of the implicit map.
The input accepted here is the local continuous solution for a finite-dimensional real system with nonsingular partial Jacobian.
The source's proof by induction on the number of dependent variables was not independently reviewed.

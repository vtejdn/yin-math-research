---
author: Yin
---

# Finite residue extensions at closed points

<a id="the26b-u002"></a>
## Residue fields of finite type algebras

Let \(k\) be a field and \(\mathfrak m\) a maximal ideal of \(k[x_1,\ldots,x_n]\) with \(n\) finite.
The residue field \(k[x_1,\ldots,x_n]/\mathfrak m\) has finite dimension over \(k\).
The theorem states the same conclusion for every finitely generated commutative \(k\)-algebra, by pulling a maximal ideal back to a polynomial presentation. [Theorem 10.34.1(1), Tag 00FV, item 00FW](../../../literature/pdf/The26b/00FV--20261125.html#00FW)

For \(k=\mathbb Q\), the residue field is therefore a number field.
If a proper ideal encodes polynomial equations, choose a maximal ideal containing it.
The images of the variables in its residue field give a simultaneous solution over a finite extension of \(\mathbb Q\).
A nonvanishing condition \(f\ne0\) can be imposed by adjoining a variable \(y\) and the equation \(yf=1\), provided the resulting ideal is proper.

I checked the statement, the quotient reduction and the source's induction on the number of variables in the [official tag edition](readme.md#hilbert-nullstellensatz).
In the induction the contraction to \(k[x_n]\) either produces a finite extension of the base field or gives a dominant map from the spectrum of a field to the affine line, whose one-point image contradicts constructibility.
I accept part (1) for these finite type residue extensions and use the constructibility theorem cited in its proof as an established input.

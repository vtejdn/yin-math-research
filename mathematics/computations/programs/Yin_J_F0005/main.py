"""Finite exact checks for Yin_C_F0096; see readme.md.
No truncation of intermediate word support is used.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
A=(F(2,3),F(-1,2)); d=len(A)
def add(*terms):
 out={}
 for v,c in terms:
  for w,b in v.items(): out[w]=out.get(w,0)+c*b
 return {w:b for w,b in out.items() if b}
def X(i,v):
 terms=[]
 for w,b in v.items():
  terms.append(({(i,)+w:b},1))
  if w and w[0]==i: terms.extend([({w[1:]:b},1),({w:b},A[i])])
 return add(*terms)
@lru_cache(None)
def W(w,v):
 if not w:return {v:F(1)}
 i=w[0];tail=w[1:];out=X(i,W(tail,v))
 if tail and tail[0]==i:out=add((out,1),(W(tail,v),-A[i]),(W(tail[1:],v),-1))
 return out
def ann(i,v):return add(*[({w[:-1]:c},1) for w,c in v.items() if w and w[-1]==i])
def formal(w,v):
 out=[]
 for k in range(len(w)+1):
  p,q=w[:k],w[k:];rv=q[::-1]
  if v[:len(rv)]==rv:out.append(({p+v[len(rv):]:F(1)},1))
 for k,i in enumerate(w):
  p,q=w[:k],w[k+1:];left=p+(i,);right=q[::-1]+(i,)
  if v[:len(right)]==right:out.append(({left+v[len(right):]:A[i]},1))
 return add(*out)
def H(w,i,v):
 suffix=(i,)+v[::-1]
 return {w[:-len(suffix)]:F(1)} if len(w)>=len(suffix) and w[-len(suffix):]==suffix else {}
words=lambda n:[w for k in range(n+1) for w in product(range(d),repeat=k)]
checks=0
for w in words(5):
 for v in words(4):
  assert W(w,v)==formal(w,v),('Wick',w,v,W(w,v),formal(w,v))
  for i in range(d):
   c=add((ann(i,W(w,v)),1),(W(w,v[:-1]) if v and v[-1]==i else {},-1))
   h=add((H(w,i,v),1),(H(w,i,v[:-1]) if v and v[-1]==i else {},A[i]))
   assert c==h,('commutator',w,v,i,c,h)
  checks+=1
print('Exact rational word-action checks:',checks,'Wick columns and',d*checks,'commutator columns; all passed.')

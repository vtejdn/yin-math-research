import random, math, cmath
random.seed(83925)

def U(z):
    d = cmath.sqrt(z*z - 4)
    g = min([(z-d)/2, (z+d)/2], key=abs)
    return -math.log(abs(g)) + .5*(g*g).real

worst = (-1e10, None)
for k in range(200000):
    p = random.uniform(-.999, .999)
    q = random.uniform(-.999, .999)
    if abs(p*q) < 1e-5:
        continue
    a = random.gauss(0, 2)
    d = random.gauss(0, 2)
    z = random.gauss(0, 2)
    bb = a*q + d*p
    cc = a*d - z*z
    dd = cmath.sqrt(bb*bb - 4*p*q*cc)
    roots = ((-bb+dd)/(2*p*q), (-bb-dd)/(2*p*q))
    potential = .5*(math.log(abs(p*q)) + sum(U(x) for x in roots))
    bound = -.5 + .25*(a*a/(1+p*p) + d*d/(1+q*q)
                       + 2*z*z/(1+p*q))
    gap = potential - bound
    if gap > worst[0]:
        worst = (gap, (k, p, q, a, d, z, potential, bound))
print(worst)

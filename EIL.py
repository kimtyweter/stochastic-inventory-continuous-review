import pandas as pd
import numpy as np
import scipy

# Input data
lb = 192
h = (1.5/7)
K = 85
L=3
mean = 192
mu = mean * L
sigma = 17.4
sigma = sigma * ((L)**(1/2))
p = 40

from scipy.stats import norm
def r(a):
    ans = 1 - (a*h)/(p*lb)
    ans = norm.ppf(ans, loc = mu  , scale = sigma)
    return ans

def f(d):
    f = norm.pdf(d, loc = mu  , scale = sigma)
    return f

def n_r(r):
    z = ((r-mu)/sigma)
    L_Z = norm.pdf(z) - z * (1 - norm.cdf(z))
    ans = sigma * L_Z
    return ans

def Q(a):
    ans = ((2*lb*(K+p*a) )/ h)**(1/2)
    return ans

def n(i):
    n = 0
    for xx in range(int(i), 1000):
        n += (xx - i)*f(xx)
    return(n)

# compute g(r,Q)
def G(a,b):
    ans = h*(a - lb*L + (b/2)) + (K*lb)/b + (p*lb*n(a))/b
    return ans

Q_prev = Q(0)
while True:
    r_prev = r(Q_prev)
    Q_prev = Q(n_r(r_prev))
    r_new = r(Q_prev)
    Q_new = Q(n_r(r_new))
    if abs(Q_prev - Q_new) < 0.00001 or abs(r_prev - r_new) < 0.00001:
        break

print('Reorder point: ',r_new)
print('Order Quantity: ',Q_new)
print('Expected cost:', G(r_new, Q_new))
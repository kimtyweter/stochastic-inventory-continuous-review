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
#calculate probability
def f(d):
    f = norm.pdf(d, loc = mu  , scale = sigma)
    return f

def n(i):
    n = 0
    for xx in range(int(i), 1000):
        n += (xx - i)*f(xx)
    return(n)

def nh(i):
    n = 0
    for xx in range(0, int(i) + 1):
        n += (i - xx)*f(xx)
    return n

def g(S):
    ans = h * nh(S) + p * n(S)
    return ans

def G(r, Q):
    sum_1=0
    for i in range(int(r), int(Q) + 1):
        sum_1 += g(i)
    ans = (K * lb + sum_1)/ Q
    return ans

Q = ((2 * K *lb) / h)**(1/2)
r = mu + norm.ppf(p/(p+h))*sigma
# compute g(r,Q)
def G(a,b):
    ans = h*(a - lb*L + (b/2)) + (K*lb)/b + (p*lb*n(a))/b
    return ans


print('Reorder point: ', r)
print('Order Quantity: ', Q)
print('Expected cost: ', G(r,Q))

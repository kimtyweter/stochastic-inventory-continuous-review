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

# computation for r
Q = ((2 * lb * K * (h + p) )/ (h * p))**(1/2)
ans = []
for i in range(0,1100, 100):
    ans.append([abs(g(i) - g(i + Q)), i])
min_value = min(ans)
min_index = ans.index(min_value)
min_lower = ans[min_index-1]
min_upper = ans[min_index+1]
# print(min_lower[1],ans[min_index][1], min_upper[1])
ans = []
for i in range(min_lower[1], min_upper[1], 10):
    ans.append([abs(g(i) - g(i + Q)), i])
min_value = min(ans)
min_index = ans.index(min_value)
min_lower = ans[min_index-1]
min_upper = ans[min_index+1]
# print(min_lower[1],ans[min_index][1], min_upper[1])
ans = []
for i in range(min_lower[1], min_upper[1], 1):
    ans.append([abs(g(i) - g(i + Q)), i])
min_value = min(ans)
min_index = ans.index(min_value)
min_lower = ans[min_index-1]
min_upper = ans[min_index+1]
# print(min_lower[1],ans[min_index][1], min_upper[1])
ans = []
for i in range(1, 201):
    i = i/100
    ans.append([abs(g(min_lower[1] + i) - g(min_lower[1] + i + Q)), min_lower[1] + i])
min_value = min(ans)

print('Reorder point: ', min_value[1])
print('Order Quantity: ', Q)
print('Expected cost: ', g(min_value[1]))

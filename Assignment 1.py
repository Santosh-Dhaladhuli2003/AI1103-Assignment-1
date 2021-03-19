# -*- coding: utf-8 -*-
"""Assigment-1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dP9yekjZMsQ_OR84k0LQa-5Q2S3bjOTR
"""

import math
import numpy as np
import scipy as sp
import random
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sn
import xlrd






print("Given, P(X=0) = 0")
print("Given, P(X=1) = k")
print("Given, P(X=2) = 2k")
print("Given, P(X=3) = 2k")
print("Given, P(X=4) = 3k") 
print("Given, P(X=5) = k^2")
print("Given, P(X=6) = 2k^2")
print("Given, P(X=7) = 7k^2 + k")


print ("\n Sum of probabilities in a Probability Distribution is always equal to 1 \n")

print (" \n So,  0 + k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k) = 1 \n")

print("\n Implies, 10k^2 + 9k - 1 = 0 \n")

print("\n This is quadratic equations , let a,b and c be its coefficients.\n")

a = 10
b = 9
c = -1

D = math.sqrt(b**2 - 4*a*c)

print ("Let p and q be the roots. ")

p = (-b + D)/(2*a)
q = (-b - D)/(2*a)





print("Since k = {0} is negative, its not possible".format(q))
print ("Therefore k = {0}".format(p))
 
r = 7*p*p + p
f = 0
g = 2*p
h = f + p + g
i = p + g
j = p*p
v = 2*j
t = h + g
u = t + i
z = u + j
w = v + z

print("P(X < 3) = P(X=2) + P(X=1) + P(X=0) = {0}".format(h))
 

print("P(X > 6) = P(X = 7) = {0}".format(r))

print("P(0 < X < 3) = P(X=2) + P(X=1) = {0}".format(i))

#plotting the probability








objects = ('0','1','2','3','4','5','6','7')
y_pos = np.arange(len(objects))
performance = [f,p,g,g,i,j,v,r]

plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.xlabel('X')
plt.ylabel('Pr(X)')

plt.show()

obj = ('0','1','2','3','4','5','6','7')
y_pos = np.arange(len(obj))
performances = [f,p,h,t,u,z,w,1]

plt.bar(y_pos, performances, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.xlabel('X')
plt.ylabel('F(X)')

plt.show()
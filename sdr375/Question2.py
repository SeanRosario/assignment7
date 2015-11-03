#__author__ = 'SeansMBP'
#code for question 2
import numpy as np
#@staticmethod
def q2():
    a = np.arange(25).reshape(5, 5)
    print a
    b = np.array([1., 5, 10, 15, 20])
    ans = np.arange(25).reshape(5, 5)
    print b
    for i in range(5):
        ans[:,i]= a[:,i]/b
    print ans


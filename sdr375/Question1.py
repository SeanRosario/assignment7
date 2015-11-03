#__author__ = 'SeansMBP'
#Code for question 1
import numpy as np
#@staticmethod
def q1():
    a = np.arange(1,16)
    a = a.reshape(3,5)
    a=a.T
    print "Initial array is :"
    print a

    arr_a = np.concatenate((a[1],a[3]), axis=0).reshape(2,3)
    print "Array for part A is {0}".format(arr_a)

    arr_b = a[:,1]
    print "Array for part B is {0}".format(arr_b)

    arr_c = a[1:4]
    print "Array for part C is {0}".format(arr_c)

    arr_d = a.T.reshape(1,15)
    arr_d = np.array(filter(lambda x: 11 >= x and x>=3, arr_d[0]))
    arr_d = arr_d.reshape(1,len(arr_d)) #Shape of the array is 1 x N
    print "Array for part D is {0}".format(arr_d)

#__author__ = 'SeansMBP'
#code for question3
import numpy as np
def q3():
    array1 = np.random.uniform(0.0, 1.0, size=30)
    array2 = array1.reshape(10,3)
    array3 = array2.copy()
    mask = np.random.uniform(0.0, 1.0, size=30)
    mask = mask.reshape(10,3)
    print "Initial 10 x 3 array:"
    print array3
    for i in range(0,len(array2)):
        array2[i] = array2[i] - [0.5,0.5,0.5]
    array2 = np.absolute(array2)
    DistArr= np.argsort(array2)
    DistArr = DistArr[:,0]
    FinalArray = np.zeros(10)
    for i in range(0,len(array3)):
        x = DistArr[i]
        mask[i,x] = 1
    mask = (mask==1)
     #print mask
    FinalArray = array3[mask].copy()

    #Fancy indexing idea taken from https://www.youtube.com/watch?v=WMI6sUptLXA


    print "The Elements in each row closest to 0.5 are:"
    print FinalArray

q3()

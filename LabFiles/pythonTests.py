import numpy as np
import pandas as pd
import random
x = 1
y = 10
print(random.random())    # [x, y)
print(random.randint(x,y))  #  integer numbers in range [x,y]
vr = [random.randint(0,3) for i in range(10)]
print (vr)

SetA = {1, 2, 3, 4, 5}
SetB = {-1, 1, 4, 5, 6}

#print (SetA | SetB)

myGlobal = "Hi"

def printStr():
    global myGlobal  # Hi
    print(myGlobal)
    myGlobal = " There!"   # local variable
    print (myGlobal)

#printStr()  # Hi \n There!

a2 = np.array([[1,2,3,4,5,6],
                [10,20,30,40,50,60]])
print (a2)
# a2.shape #(2,6)
# Note: shape is a 'tuple' object, 
#  not callable as an object: shape() -> TypeError

# Need to flatten the 2D array into a 1D array:
np.reshape(-1) 
# One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions.
# array([ 1,  2,  3,  4,  5,  6, 10, 20, 30, 40, 50, 60])



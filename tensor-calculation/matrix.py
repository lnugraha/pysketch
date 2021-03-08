#!/usr/bin/python3
import math, sys
import numpy as np
from timeit import default_timer as timer
from random import seed
from random import randint

def generateSquareMatrix(size):
    # include an assertion, such that size cannot be less than 1
    if size < 1:
        raise ValueError("Matrix rows or columns cannot be less than one")
    elif type(size) is not int:
        raise TypeError("Matrix rows or columns does not have proper number")

    M = np.ones( (size, size) )
    for i in range(size):
        for j in range(size):
            M[i][j] = randint(0,10)
    return M

def dgemm(A, B, size):
    C = np.zeros( (size, size) )
    for i in range(size):
        for j in range(size):
            totalSum = 0
            for k in range(size):
                totalSum += A[i][k] * B[k][j]
            C[i][j] = totalSum
    return C

def getMFLOPS(A, B, size):
    # confirm that size A, size B are identical
    # confirm that size variable is the same as A and B rows, cols
    start_time = timer()
    C = dgemm(A, B, size)
    stop_time = timer()
    # calculate time difference between multiplication
    timeDiff = stop_time - start_time
    # division and simplification to Giga (/10^9)
    estimatedGFLOPS = (size*size*size)/(timeDiff*1.0e6)
    return estimatedGFLOPS

if __name__ == "__main__":
    if len( sys.argv ) == 2:
        matSize = int( sys.argv[1] )
    else:
        matSize = 5

    print( "Matrix Size: {}".format(matSize) )
    M = generateSquareMatrix(matSize)
    N = generateSquareMatrix(matSize)
    O = dgemm(M, N, matSize)
    # check = getMFLOPS(M, N, matSize)
    # print(check)

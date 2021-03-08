#!/usr/bin/python3
import pytest, math, sys
import numpy as np
import matrix

def checkRunning():
    x = 2; y = 3
    assert x == y, "X and Y is not equal"

def checkElements():
    matSize = 0
    with pytest.raises(ValueError, match=r".* cannot be less than one .*"):
        X = matrix.generateSquareMatrix(matSize)

def checkElementType():
    matSize = True
    with pytest.raises(TypeError, match=r".* does not have proper number .*"):
        X = matrix.generateSquareMatrix(matSize)

def calculateElements():
    matSize = 5
    A = matrix.generateSquareMatrix(matSize)
    B = matrix.generateSquareMatrix(matSize)
    C = matrix.dgemm(A, B, matSize)
    C_np = A.dot(B)

    for i in range(matSize):
        for j in range(matSize):
            assert C[i][j] == C_np[i][j], "Incorrect element at index"




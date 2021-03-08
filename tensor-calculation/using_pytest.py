#!/usr/bin/python3
import pytest, math, sys
import numpy as np
import matrix

def testValueElements():
    matSize = 0
    with pytest.raises(ValueError, match=r".* cannot be less than one"):
        X = matrix.generateSquareMatrix(matSize)


def testElementType():
    matSize = True
    with pytest.raises(TypeError, match=r".* does not have proper .*"):
        X = matrix.generateSquareMatrix(matSize)

def testCalculateElements():
    matSize = 5
    A = matrix.generateSquareMatrix(matSize)
    B = matrix.generateSquareMatrix(matSize)
    C = matrix.dgemm(A, B, matSize)
    C_np = A.dot(B)

    for i in range(matSize):
        for j in range(matSize):
            assert C[i][j] == C_np[i][j], "Incorrect element at index"




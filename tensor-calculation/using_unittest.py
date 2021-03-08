import unittest, sys, math
import matrix
import numpy as np

class MatrixCase(unittest.TestCase):
    def test_size(self):
        self.assertRaises(ValueError, matrix.generateSquareMatrix, 0)

    def test_type(self):
        self.assertRaises(TypeError, matrix.generateSquareMatrix, True)

    def test_matrix(self):
        matSize = 10
        A = matrix.generateSquareMatrix(matSize)
        B = matrix.generateSquareMatrix(matSize)
        C = matrix.dgemm(A, B, matSize)
        C_np = A.dot(B)

        for i in range(matSize):
            for j in range(matSize):
                self.assertAlmostEqual(C[i][j], C_np[i][j])

if __name__ == "__main__":
    unittest.main()

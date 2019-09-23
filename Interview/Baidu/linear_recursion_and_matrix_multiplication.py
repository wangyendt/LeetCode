# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/23 21:56
# software: PyCharm


base_mod = 1000000007


class LinearRecursionMatrixMultiplication:
    def __init__(self, recur_vec, base_mod=1000000007):
        self.m = len(recur_vec)
        self.generating_matrx = [[0 for _ in range(self.m)] for _ in range(self.m)]
        self.base_mod = base_mod

        for i in range(self.m):
            self.generating_matrx[0][i] = recur_vec[i]
        for j in range(1, self.m):
            self.generating_matrx[j][j - 1] = 1

    # O(m**3)
    @staticmethod
    def mat_mul(A, B):
        ma, na = len(A), len(A[0])
        mb, nb = len(B), len(B[0])
        assert na == mb
        ret = [[0 for _ in range(nb)] for _ in range(ma)]
        for i in range(ma):
            for j in range(nb):
                ph = place_holder = 0
                for k in range(na):
                    ph += A[i][k] * B[k][j]
                ret[i][j] = ph % base_mod
        return ret

    # O(log(n))
    def mat_pow(self, A, n):
        if n == 1:
            return A
        else:
            half = self.mat_pow(A, n // 2)
            ret = self.mat_mul(half, half)
            if n % 2 == 1:
                return self.mat_mul(A, ret)
            else:
                return ret

    def calc_n_item(self, M0, n):
        if n <= self.m: return self.generating_matrx[0][self.m - n]
        return self.mat_mul(self.mat_pow(self.generating_matrx, n - self.m), M0)[0][0]


if __name__ == '__main__':
    # an = an-1 + an-2
    recursion_vector = [1, 1]
    mat0 = [[1], [1]]  # [[F1,F0]]
    lrmm = LinearRecursionMatrixMultiplication(recursion_vector)
    [print(lrmm.calc_n_item(mat0, i), end='\t') for i in range(1, 20)]
    print('\n')

    # an = an-1 + an-3 + an-4
    a1, a2, a3, a4 = 1, 2, 3, 4
    n = 10 ** 120
    recursion_vector = [1, 0, 1, 1]
    m0 = [[a4], [a3], [a2], [a1]]
    lrmm = LinearRecursionMatrixMultiplication(recursion_vector)
    print(lrmm.calc_n_item(m0, 20))

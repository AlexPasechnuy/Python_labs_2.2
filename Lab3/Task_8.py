import numpy as np
import scipy.stats


def matrix_normal_logpdf(X, m, U, V):
    return scipy.stats.matrix_normal.logpdf\
        (X, mean=m, rowcov=U, colcov=V).round(SIGN_TO_ROUND)


if __name__ == '__main__':
    SIGN_TO_ROUND = 3
    N = 5
    D = 4

    m = np.random.uniform(-1, 1, size=N * D). \
        reshape(N, D).round(SIGN_TO_ROUND)
    U = np.diag([x for x in range(1, N + 1)]).round(SIGN_TO_ROUND)
    V = 0.3 * np.identity(D).round(SIGN_TO_ROUND)
    X = m + 0.1

    print(m)
    print(U)
    print(U)
    print(X)

    print(matrix_normal_logpdf(X, m, U, V))
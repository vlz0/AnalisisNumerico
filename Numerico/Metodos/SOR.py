import numpy as np

def SOR(x0, A, b, tol, niter, w):
    c = 0
    error = tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, k=-1)
    U = -np.triu(A, k=1)

    while error > tol and c < niter:
        T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        C = w * np.linalg.inv(D - w * L) @ b
        x1 = T @ x0 + C
        error = np.linalg.norm(x1 - x0, np.inf)
        x0 = x1
        c += 1

    if error < tol:
        s = x0
        n = c
        return s, n
    else:
        s = x0
        n = c
        return f"Fracasó en {niter} iteraciones", n
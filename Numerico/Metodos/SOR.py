import numpy as np

def SOR(x0, A, b, Tol, niter, w):
    c = 0
    error = Tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, +1)
    resultados = []

    while error > Tol and c < niter:
        T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        C = w * np.linalg.inv(D - w * L) @ b
        x1 = T @ x0 + C
        E = np.linalg.norm(x1 - x0, np.inf)
        error = E
        x0 = x1
        c += 1
        resultados.append({"iteracion": c, "x": x1.tolist(), "error": E})

    if error < Tol:
        return resultados
    else:
        return [{"iteracion": "Error", "x": "Iteraciones insuficientes", "error": ""}]
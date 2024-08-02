import scipy.integrate as spi

def adaptive_integration(func, a, b, tol=1e-6):
    result, _ = spi.quad(func, a, b, epsabs=tol)
    return result

# passing values to the function.
print(adaptive_integration(lambda x: x**2, 0, 1))
print(adaptive_integration(lambda x: x**3, 0, 1))

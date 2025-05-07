import numpy as np

q = 3329
n = 256

def poly_add(a, b):
    """Add two polynomials modulo q"""
    return [(ai + bi) % q for ai, bi in zip(a, b)]

def poly_sub(a, b):
    """Subtract two polynomials modulo q"""
    return [(ai - bi) % q for ai, bi in zip(a, b)]

q = 3329
n = 256

def poly_mul_naive(a, b):
    """
    Multiply two polynomials a, b in Z_q[X]/(X^n + 1)
    using schoolbook multiplication and reduction mod X^n + 1.
    """
    if len(a) != n or len(b) != n:
        raise ValueError(f"Expected polynomials of degree {n}, got {len(a)} and {len(b)}")

    result = [0] * (2 * n)
    for i in range(n):
        for j in range(n):
            result[i + j] += a[i] * b[j]

    # Modular reduction: reduce mod (X^n + 1)
    for i in range(n, 2 * n):
        result[i - n] = (result[i - n] - result[i]) % q

    return [x % q for x in result[:n]]

def poly_zero():
    """Return the zero polynomial"""
    return [0] * n

def poly_random():
    """Generate a random polynomial with coefficients in Z_q"""
    return list(np.random.randint(0, q, size=n))

if __name__ == "__main__":
    a = poly_random()
    b = poly_random()

    print("a + b:", poly_add(a, b)[:10])
    print("a - b:", poly_sub(a, b)[:10])
    print("a * b (naive):", poly_mul_naive(a, b)[:10])
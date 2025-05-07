import numpy as np
from typing import List
from naive_kyber.parameters import q, n


def generate_random_matrix(k: int) -> List[List[List[int]]]:
    """
    Generate a k x k matrix of random polynomials.
    Each polynomial has n coefficients in [0, q).
    """
    return [
        [list(np.random.randint(0, q, size=n)) for _ in range(k)]
        for _ in range(k)
    ]

if __name__ == "__main__":
    k = 2
    A = generate_random_matrix(k)
    print(len(A[0][0]))
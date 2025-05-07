from secrets import token_bytes

q = 3329
n = 256
eta = 2

def cbd_eta2(n=256):
    """
    Sample small noise polynomial from CBD with η = 2.
    Returns integers in [-4, 4].
    """
    poly = []
    buf = token_bytes(128)

    for i in range(0, 128):
        byte = buf[i]

        # First coeff
        a = ((byte >> 0) & 1) + ((byte >> 1) & 1)
        b = ((byte >> 2) & 1) + ((byte >> 3) & 1)
        poly.append(a - b)
        if len(poly) == n:
            break

        # Second coeff
        a = ((byte >> 4) & 1) + ((byte >> 5) & 1)
        b = ((byte >> 6) & 1) + ((byte >> 7) & 1)
        poly.append(a - b)
        if len(poly) == n:
            break

    return poly

if __name__ == "__main__":
    poly = cbd_eta2()
    print("First 10 CBD coefficients:", poly[:10])
    print("Length:", len(poly))  # Should be 256
    print("Value range:", min(poly), "to", max(poly))
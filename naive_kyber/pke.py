import os
from naive_kyber.poly import poly_add, poly_sub, poly_mul_naive
from naive_kyber.cbd import cbd_eta2
from naive_kyber.matrix import generate_random_matrix
from copy import deepcopy

q = 3329
n = 256
k = 3  # Kyber512 setting

def keygen_internal():
    A = generate_random_matrix(k=3)

    s = [cbd_eta2(n=256) for _ in range(3)]
    e = [cbd_eta2(n=256) for _ in range(3)]

    t = []
    for i in range(3):
        acc = [0] * 256
        for j in range(3):
            acc = poly_add(acc, poly_mul_naive(A[i][j], s[j]))
        acc = poly_add(acc, e[i])
        t.append(acc)

    return (A, t), s

def encrypt_block(public_key, message_bits):
    """
    Encrypt a message (bit array) using public key (A, t).
    Returns ciphertext (A, u, v), where A is sent explicitly.
    """
    A, t = public_key
    A_T = transpose_matrix(deepcopy(A))  # Aᵗ for correct multiplication

    r = [cbd_eta2() for _ in range(k)]
    e1 = [cbd_eta2() for _ in range(k)]
    e2 = cbd_eta2()

    # u = Aᵗ · r + e1
    u = []
    for i in range(k):
        acc = [0] * n
        for j in range(k):
            acc = poly_add(acc, poly_mul_naive(A_T[i][j], r[j]))
        acc = poly_add(acc, e1[i])
        u.append(acc)

    # v = tᵗ · r + e2 + floor(q/2) * m
    acc = [0] * n
    for j in range(k):
        acc = poly_add(acc, poly_mul_naive(t[j], r[j]))
    acc = poly_add(acc, e2)
    v = [(acc[i] + ((q // 2) * message_bits[i])) % q for i in range(n)]

    # Send A explicitly (educational simplification)
    return A, u, v

def decrypt_block(private_key, ciphertext):
    A, u, v = ciphertext
    s = private_key

    acc = [0] * n
    for j in range(k):
        acc = poly_add(acc, poly_mul_naive(s[j], u[j]))

    diff = poly_sub(v, acc)
    m_rec = [((2 * coeff + q // 2) // q) % 2 for coeff in diff]
    return m_rec

def encrypt_internal(public_key, message):
    return [encrypt_block(public_key, block) for block in string_to_bit_blocks_256(message)]
    
def decrypt_internal(private_key, cipherblocks):
    return bit_blocks_256_to_string([decrypt_block(private_key, block) for block in cipherblocks])

def transpose_matrix(matrix):
    """
    Transpose a k x k matrix of polynomials.
    """
    k = len(matrix)
    return [[matrix[j][i] for j in range(k)] for i in range(k)]

def string_to_bit_blocks_256(s):
    """
    Converts a UTF-8 string into a list of 256-bit blocks (lists of 0s and 1s).
    Each block represents 32 bytes (256 bits).
    """
    byte_array = s.encode('utf-8')
    blocks = []

    for i in range(0, len(byte_array), 32):  # 32 bytes = 256 bits
        chunk = byte_array[i:i+32]
        bit_list = []
        for byte in chunk:
            bits = [(byte >> j) & 1 for j in reversed(range(8))]
            bit_list.extend(bits)

        if len(bit_list) < 256:
            bit_list += [0] * (256 - len(bit_list))  # pad

        blocks.append(bit_list)

    return blocks
    
def bit_blocks_256_to_string(blocks):
    """
    Converts a list of 256-bit blocks back to a UTF-8 string.
    Automatically removes zero padding at the end.
    """
    byte_array = bytearray()

    for block in blocks:
        if len(block) != 256:
            raise ValueError("All blocks must be exactly 256 bits")

        for i in range(0, 256, 8):
            byte = 0
            for bit in block[i:i+8]:
                byte = (byte << 1) | bit
            byte_array.append(byte)

    return byte_array.rstrip(b'\x00').decode('utf-8', errors='ignore')
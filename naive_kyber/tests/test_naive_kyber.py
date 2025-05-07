"""
Unit and regression test for the naive_kyber package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

from naive_kyber import keygen, encrypt, decrypt


def test_naive_kyber_imported():
    """Test encryption and decryption"""
    assert "naive_kyber" in sys.modules

    pk, sk = keygen()
    message = "hello sadfllsadkfjsalf, sadfklsafkasjflkajslkbjkejgioejgovasdf"

    enc = encrypt(pk, message)

    assert message == decrypt(sk, enc)

if __name__ == "__main__":
    test_naive_kyber_imported()
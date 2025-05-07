Getting Started
===============

Welcome to **naive_kyber**, an educational Python implementation of the post-quantum key encapsulation mechanism defined in [FIPS 203 (Kyber)](https://csrc.nist.gov/publications/detail/fips/203/final).  
This package demonstrates the core cryptographic operations: key generation, encryption, and decryption — in a readable, modular form suitable for learning and experimentation.

Installation
------------

If you're working with a local clone of the repository, install it in editable mode using:

.. code-block:: bash

    pip install -e .


Basic Usage
-----------

Once installed, you can use `naive_kyber` in your Python code as follows:

.. code-block:: python

    import naive_kyber

    # Key generation
    public_key, secret_key = naive_kyber.keygen()

    # Encrypt a message
    message = "hello quantum-secure world"
    ciphertext = naive_kyber.encrypt(public_key, message)

    # Decrypt the message
    plaintext = naive_kyber.decrypt(secret_key, ciphertext)

    print("Decrypted:", plaintext)


What’s Included
---------------

- **Keygen**: Generates a base64-encoded public/secret keypair
- **Encrypt**: Accepts a base64-encoded public key and a plaintext string, returns a base64-encoded ciphertext
- **Decrypt**: Accepts a base64-encoded secret key and a base64-encoded ciphertext, returns the original plaintext

This package uses pure Python and `numpy` to keep the code accessible and educational, rather than performance-optimized.
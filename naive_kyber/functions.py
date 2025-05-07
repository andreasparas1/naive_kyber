from naive_kyber.serialize import encode_pk_to_base64, encode_sk_to_base64, decode_pk_from_base64, decode_sk_from_base64, encode_message, decode_message
from naive_kyber.pke import keygen_internal, encrypt_internal, decrypt_internal


def keygen():
    pk, sk = keygen_internal()
    return encode_pk_to_base64(pk), encode_sk_to_base64(sk)

def encrypt(public_key, message):
    pk = decode_pk_from_base64(public_key)
    return encode_message(encrypt_internal(pk, message))

def decrypt(private_key, encoded):
    sk = decode_sk_from_base64(private_key)
    decoded = decode_message(encoded)
    return decrypt_internal(sk, decoded)

if __name__ == "__main__":
    pk, sk = keygen()

    enc = encrypt(pk, "hello sadfllsadkfjsalf, sadfklsafkasjflkajslkbjkejgioejgovasdf")

    print(decrypt(sk, enc))
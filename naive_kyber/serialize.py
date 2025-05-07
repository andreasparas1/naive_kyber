import base64
import pickle
from typing import Tuple, List, Any

# Type hint for clarity
NestedType = Tuple[Tuple[List[List[List[int]]], list]]

def encode_pk_to_base64(data: NestedType) -> str:
    serialized = pickle.dumps(data)
    encoded = base64.b64encode(serialized)
    return encoded.decode('utf-8')

def decode_pk_from_base64(encoded_str: str) -> NestedType:
    decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
    return pickle.loads(decoded_bytes)

def encode_sk_to_base64(data: List[List[Any]]) -> str:
    serialized = pickle.dumps(data)
    encoded = base64.b64encode(serialized)
    return encoded.decode('utf-8')

def decode_sk_from_base64(encoded_str: str) -> List[List[Any]]:
    decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
    return pickle.loads(decoded_bytes)


def encode_message(data: List[Tuple[Any, list, list]]) -> str:
    serialized = pickle.dumps(data)
    encoded = base64.b64encode(serialized)
    return encoded.decode('utf-8')

def decode_message(encoded_str: str) -> List[Tuple[Any, list, list]]:
    decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
    return pickle.loads(decoded_bytes)


# assert decoded == bitlists  # Should pass


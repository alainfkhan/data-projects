import requests
from _typeshed import Incomplete

GCS_HASH_HEADER: str
COMPUTE_HASH_CHUNK_SIZE: int
logger: Incomplete

def get_md5_checksum_from_response(response: requests.Response) -> str | None: ...
def update_hash_from_file(hash_object, out_file: str) -> None: ...
def to_b64_digest(hash_object) -> str: ...

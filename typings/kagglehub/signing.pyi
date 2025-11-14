from _typeshed import Incomplete
from kagglehub.handle import ModelHandle as ModelHandle
from kagglehub.models_helpers import signing_token as signing_token

logger: Incomplete

def sign_with_sigstore(local_model_dir: str, handle: ModelHandle) -> bool: ...

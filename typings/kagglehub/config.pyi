from _typeshed import Incomplete
from dataclasses import dataclass
from kagglehub.env import is_in_colab_notebook as is_in_colab_notebook

DEFAULT_CACHE_FOLDER: Incomplete
DEFAULT_KAGGLE_API_ENDPOINT: str
DEFAULT_KAGGLE_CREDENTIALS_FOLDER: Incomplete
DEFAULT_LOG_LEVEL: Incomplete
CREDENTIALS_FILENAME: str
CACHE_FOLDER_ENV_VAR_NAME: str
KAGGLE_API_ENDPOINT_ENV_VAR_NAME: str
USERNAME_ENV_VAR_NAME: str
KEY_ENV_VAR_NAME: str
CREDENTIALS_FOLDER_ENV_VAR_NAME: str
LOG_VERBOSITY_ENV_VAR_NAME: str
DISABLE_KAGGLE_CACHE_ENV_VAR_NAME: str
DISABLE_COLAB_CACHE_ENV_VAR_NAME: str
TBE_RUNTIME_ADDR_ENV_VAR_NAME: str
CREDENTIALS_JSON_USERNAME: str
CREDENTIALS_JSON_KEY: str
COLAB_SECRET_USERNAME: str
COLAB_SECRET_KEY: str
LOG_LEVELS_MAP: Incomplete
TRUTHY_VALUES: Incomplete
logger: Incomplete

@dataclass
class KaggleApiCredentials:
    username: str
    key: str

def get_cache_folder() -> str: ...
def get_kaggle_api_endpoint() -> str: ...
def get_kaggle_credentials() -> KaggleApiCredentials | None: ...
def get_log_verbosity() -> int: ...
def is_colab_cache_disabled() -> bool: ...
def is_kaggle_cache_disabled() -> bool: ...
def set_kaggle_credentials(username: str, api_key: str) -> None: ...
def clear_kaggle_credentials() -> None: ...
def get_colab_credentials() -> KaggleApiCredentials | None: ...

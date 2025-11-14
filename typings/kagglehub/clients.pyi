import requests
import requests.auth
from _typeshed import Incomplete
from kagglehub.cache import (
    delete_from_cache as delete_from_cache,
    get_cached_archive_path as get_cached_archive_path,
)
from kagglehub.config import (
    get_kaggle_api_endpoint as get_kaggle_api_endpoint,
    get_kaggle_credentials as get_kaggle_credentials,
)
from kagglehub.datasets_enums import KaggleDatasetAdapter as KaggleDatasetAdapter
from kagglehub.env import (
    KAGGLE_DATA_PROXY_URL_ENV_VAR_NAME as KAGGLE_DATA_PROXY_URL_ENV_VAR_NAME,
    KAGGLE_TOKEN_KEY_DIR_ENV_VAR_NAME as KAGGLE_TOKEN_KEY_DIR_ENV_VAR_NAME,
    is_in_colab_notebook as is_in_colab_notebook,
    is_in_kaggle_notebook as is_in_kaggle_notebook,
    read_kaggle_build_date as read_kaggle_build_date,
    search_lib_in_call_stack as search_lib_in_call_stack,
)
from kagglehub.exceptions import (
    BackendError as BackendError,
    ColabEnvironmentError as ColabEnvironmentError,
    CredentialError as CredentialError,
    DataCorruptionError as DataCorruptionError,
    KaggleEnvironmentError as KaggleEnvironmentError,
    NotFoundError as NotFoundError,
    colab_raise_for_status as colab_raise_for_status,
    kaggle_api_raise_for_status as kaggle_api_raise_for_status,
    process_post_response as process_post_response,
)
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    ResourceHandle as ResourceHandle,
)
from kagglehub.integrity import (
    get_md5_checksum_from_response as get_md5_checksum_from_response,
    to_b64_digest as to_b64_digest,
    update_hash_from_file as update_hash_from_file,
)

CHUNK_SIZE: int
DEFAULT_CONNECT_TIMEOUT: int
DEFAULT_READ_TIMEOUT: int
ACCEPT_RANGE_HTTP_HEADER: str
HTTP_STATUS_404: int
ADAPTER_TO_USER_AGENT_MAP: Incomplete

def get_user_agent() -> str: ...

logger: Incomplete

class KaggleApiV1Client:
    BASE_PATH: str
    credentials: Incomplete
    endpoint: Incomplete
    def __init__(self) -> None: ...
    def get(self, path: str, resource_handle: ResourceHandle | None = None) -> dict: ...
    def post(self, path: str, data: dict) -> dict: ...
    def download_file(
        self,
        path: str,
        out_file: str,
        resource_handle: ResourceHandle | None = None,
        cached_path: str | None = None,
        *,
        extract_auto_compressed_file: bool = False,
    ) -> bool: ...
    def has_credentials(self) -> bool: ...

KAGGLE_JWT_TOKEN_ENV_VAR_NAME: str
KAGGLE_DATA_PROXY_TOKEN_ENV_VAR_NAME: str

class KaggleJwtClient:
    BASE_PATH: str
    endpoint: Incomplete
    headers: Incomplete
    def __init__(self) -> None: ...
    def post(
        self, request_name: str, data: dict, timeout: tuple[float, float] = ...
    ) -> dict: ...

class ColabClient:
    IS_SUPPORTED_PATH: str
    IS_MODEL_SUPPORTED_PATH: str
    IS_DATASET_SUPPORTED_PATH: str
    MOUNT_PATH: str
    MODEL_MOUNT_PATH: str
    DATASET_MOUNT_PATH: str
    TBE_RUNTIME_ADDR_ENV_VAR_NAME: str
    endpoint: Incomplete
    credentials: Incomplete
    headers: Incomplete
    def __init__(self) -> None: ...
    def post(
        self,
        data: dict,
        handle_path: str,
        resource_handle: ResourceHandle | None = None,
    ) -> dict | None: ...

class KaggleTokenAuth(requests.auth.AuthBase):
    def __call__(self, r: requests.PreparedRequest): ...

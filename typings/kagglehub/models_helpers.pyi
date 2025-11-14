from _typeshed import Incomplete
from kagglehub.clients import (
    BackendError as BackendError,
    KaggleApiV1Client as KaggleApiV1Client,
)
from kagglehub.exceptions import KaggleApiHTTPError as KaggleApiHTTPError
from kagglehub.gcs_upload import UploadDirectoryInfo as UploadDirectoryInfo
from kagglehub.handle import ModelHandle as ModelHandle

logger: Incomplete

def create_model_instance_or_version(
    model_handle: ModelHandle,
    files: UploadDirectoryInfo,
    license_name: str | None,
    version_notes: str = "",
    *,
    sigstore: bool | None = False,
) -> None: ...
def create_model_if_missing(owner_slug: str, model_slug: str) -> None: ...
def delete_model(owner_slug: str, model_slug: str) -> None: ...
def signing_token(owner_slug: str, model_slug: str) -> str | None: ...

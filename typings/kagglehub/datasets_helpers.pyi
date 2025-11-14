from _typeshed import Incomplete
from kagglehub.clients import (
    BackendError as BackendError,
    KaggleApiV1Client as KaggleApiV1Client,
)
from kagglehub.exceptions import KaggleApiHTTPError as KaggleApiHTTPError
from kagglehub.gcs_upload import UploadDirectoryInfo as UploadDirectoryInfo
from kagglehub.handle import DatasetHandle as DatasetHandle

logger: Incomplete

def create_dataset_or_version(
    dataset_handle: DatasetHandle, files: UploadDirectoryInfo, version_notes: str = ""
) -> None: ...
def dataset_delete(owner_slug: str, dataset_slug: str) -> None: ...

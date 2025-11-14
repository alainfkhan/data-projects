from _typeshed import Incomplete
from kagglehub import registry as registry
from kagglehub.datasets_enums import (
    KaggleDatasetAdapter as KaggleDatasetAdapter,
    PolarsFrameType as PolarsFrameType,
)
from kagglehub.datasets_helpers import (
    create_dataset_or_version as create_dataset_or_version,
)
from kagglehub.gcs_upload import (
    normalize_patterns as normalize_patterns,
    upload_files_and_directories as upload_files_and_directories,
)
from kagglehub.handle import parse_dataset_handle as parse_dataset_handle
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK
from typing import Any

logger: Incomplete
DEFAULT_IGNORE_PATTERNS: Incomplete
DATASET_LOAD_ADAPTER_OPTIONAL_DEPENDENCIES_MAP: Incomplete

def dataset_download(
    handle: str, path: str | None = None, *, force_download: bool | None = False
) -> str: ...
def dataset_upload(
    handle: str,
    local_dataset_dir: str,
    version_notes: str = "",
    ignore_patterns: list[str] | str | None = None,
) -> None: ...
def dataset_load(
    adapter: KaggleDatasetAdapter,
    handle: str,
    path: str,
    *,
    pandas_kwargs: Any = None,
    sql_query: str | None = None,
    hf_kwargs: Any = None,
    polars_frame_type: PolarsFrameType | None = None,
    polars_kwargs: Any = None,
) -> Any: ...
def load_dataset(
    adapter: KaggleDatasetAdapter,
    handle: str,
    path: str,
    *,
    pandas_kwargs: Any = None,
    sql_query: str | None = None,
    hf_kwargs: Any = None,
) -> Any: ...
def validate_dataset_load_args(
    adapter: KaggleDatasetAdapter, **kwargs: Any
) -> None: ...

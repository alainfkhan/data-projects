from kagglehub.config import get_cache_folder as get_cache_folder
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    DatasetHandle as DatasetHandle,
    ModelHandle as ModelHandle,
    NotebookHandle as NotebookHandle,
    ResourceHandle as ResourceHandle,
)

DATASETS_CACHE_SUBFOLDER: str
NOTEBOOKS_CACHE_SUBFOLDER: str
COMPETITIONS_CACHE_SUBFOLDER: str
MODELS_CACHE_SUBFOLDER: str
FILE_COMPLETION_MARKER_FOLDER: str

def load_from_cache(handle: ResourceHandle, path: str | None = None) -> str | None: ...
def get_cached_path(handle: ResourceHandle, path: str | None = None) -> str: ...
def get_cached_archive_path(handle: ResourceHandle) -> str: ...
def mark_as_complete(handle: ResourceHandle, path: str | None = None) -> None: ...
def mark_as_incomplete(handle: ResourceHandle, path: str | None = None) -> None: ...
def delete_from_cache(
    handle: ResourceHandle, path: str | None = None
) -> str | None: ...

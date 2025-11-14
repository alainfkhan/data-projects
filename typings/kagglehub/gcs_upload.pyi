from _typeshed import Incomplete
from collections.abc import Iterable, Sequence
from datetime import datetime
from kagglehub.clients import KaggleApiV1Client as KaggleApiV1Client
from kagglehub.exceptions import BackendError as BackendError

logger: Incomplete
MAX_FILES_TO_UPLOAD: int
TEMP_ARCHIVE_FILE: str
MAX_RETRIES: int
REQUEST_TIMEOUT: int

class UploadDirectoryInfo:
    name: Incomplete
    files: Incomplete
    directories: Incomplete
    def __init__(
        self,
        name: str,
        files: list[str] | None = None,
        directories: list["UploadDirectoryInfo"] | None = None,
    ) -> None: ...
    def serialize(self) -> dict: ...

def parse_datetime_string(string: str) -> datetime | str: ...

class File:
    def __init__(self, init_dict: dict) -> None: ...
    @staticmethod
    def get_size(size: float, precision: int = 0) -> str: ...

def filtered_walk(
    *, base_dir: str, ignore_patterns: Sequence[str]
) -> Iterable[tuple[str, list[str], list[str]]]: ...
def upload_files_and_directories(
    folder: str, *, ignore_patterns: Sequence[str], item_type: str, quiet: bool = False
) -> UploadDirectoryInfo: ...
def normalize_patterns(
    *, default: list[str], additional: list[str] | str | None
) -> list[str]: ...

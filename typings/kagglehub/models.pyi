from _typeshed import Incomplete
from kagglehub import registry as registry
from kagglehub.gcs_upload import (
    normalize_patterns as normalize_patterns,
    upload_files_and_directories as upload_files_and_directories,
)
from kagglehub.handle import parse_model_handle as parse_model_handle
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK
from kagglehub.models_helpers import (
    create_model_if_missing as create_model_if_missing,
    create_model_instance_or_version as create_model_instance_or_version,
)
from kagglehub.signing import sign_with_sigstore as sign_with_sigstore

logger: Incomplete
DEFAULT_IGNORE_PATTERNS: Incomplete

def model_download(
    handle: str, path: str | None = None, *, force_download: bool | None = False
) -> str: ...
def model_upload(
    handle: str,
    local_model_dir: str,
    license_name: str | None = None,
    version_notes: str = "",
    ignore_patterns: list[str] | str | None = None,
    *,
    sigstore: bool | None = False,
) -> None: ...

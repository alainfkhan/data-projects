from _typeshed import Incomplete
from kagglehub import registry as registry
from kagglehub.clients import KaggleApiV1Client as KaggleApiV1Client
from kagglehub.exceptions import KaggleApiHTTPError as KaggleApiHTTPError
from kagglehub.handle import (
    UtilityScriptHandle as UtilityScriptHandle,
    parse_utility_script_handle as parse_utility_script_handle,
)
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK

logger: Incomplete

def utility_script_install(
    handle: str, *, force_download: bool | None = False
) -> str: ...

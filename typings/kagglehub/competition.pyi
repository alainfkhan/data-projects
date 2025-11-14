from _typeshed import Incomplete
from kagglehub import registry as registry
from kagglehub.handle import parse_competition_handle as parse_competition_handle
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK

logger: Incomplete

def competition_download(
    handle: str, path: str | None = None, *, force_download: bool | None = False
) -> str: ...

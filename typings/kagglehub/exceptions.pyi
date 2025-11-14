import requests
from _typeshed import Incomplete
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    ResourceHandle as ResourceHandle,
)
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK
from typing import Any

logger: Incomplete

class CredentialError(Exception): ...
class KaggleEnvironmentError(Exception): ...
class ColabEnvironmentError(Exception): ...

class BackendError(Exception):
    error_code: Incomplete
    def __init__(self, message: str, error_code: int | None = None) -> None: ...

class NotFoundError(Exception): ...
class DataCorruptionError(Exception): ...

class KaggleApiHTTPError(requests.HTTPError):
    def __init__(
        self, message: str, response: requests.Response | None = None
    ) -> None: ...

class ColabHTTPError(requests.HTTPError):
    def __init__(
        self, message: str, response: requests.Response | None = None
    ) -> None: ...

class UnauthenticatedError(Exception):
    def __init__(self, message: str = "User is not authenticated") -> None: ...

class UserCancelledError(Exception): ...

def kaggle_api_raise_for_status(
    response: requests.Response, resource_handle: ResourceHandle | None = None
) -> None: ...
def colab_raise_for_status(
    response: requests.Response, resource_handle: ResourceHandle | None = None
) -> None: ...
def process_post_response(response: dict[str, Any]) -> None: ...

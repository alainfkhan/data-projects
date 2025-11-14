from kagglehub.clients import KaggleApiV1Client as KaggleApiV1Client
from kagglehub.config import set_kaggle_credentials as set_kaggle_credentials
from kagglehub.exceptions import UnauthenticatedError as UnauthenticatedError

INVALID_CREDENTIALS_ERROR: int
NOTEBOOK_LOGIN_TOKEN_HTML_START: str
NOTEBOOK_LOGIN_TOKEN_HTML_END: str

def login(validate_credentials: bool = True) -> None: ...
def whoami(*, verbose: bool = True) -> dict: ...
def get_username() -> str | None: ...

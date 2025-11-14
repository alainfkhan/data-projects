from _typeshed import Incomplete
from kagglehub.clients import (
    DEFAULT_CONNECT_TIMEOUT as DEFAULT_CONNECT_TIMEOUT,
    KaggleJwtClient as KaggleJwtClient,
)
from kagglehub.config import is_kaggle_cache_disabled as is_kaggle_cache_disabled
from kagglehub.env import is_in_kaggle_notebook as is_in_kaggle_notebook
from kagglehub.exceptions import BackendError as BackendError
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    DatasetHandle as DatasetHandle,
    ModelHandle as ModelHandle,
    NotebookHandle as NotebookHandle,
)
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK
from kagglehub.packages import PackageScope as PackageScope
from kagglehub.resolver import Resolver as Resolver

KAGGLE_CACHE_MOUNT_FOLDER_ENV_VAR_NAME: str
ATTACH_DATASOURCE_REQUEST_NAME: str
ATTACH_DATASOURCE_READ_TIMEOUT: int
DEFAULT_KAGGLE_CACHE_MOUNT_FOLDER: str
logger: Incomplete

class CompetitionKaggleCacheResolver(Resolver[CompetitionHandle]):
    def is_supported(self, *_, **__) -> bool: ...

class DatasetKaggleCacheResolver(Resolver[DatasetHandle]):
    def is_supported(self, *_, **__) -> bool: ...

class ModelKaggleCacheResolver(Resolver[ModelHandle]):
    def is_supported(self, *_, **__) -> bool: ...

class NotebookOutputKaggleCacheResolver(Resolver[NotebookHandle]):
    def is_supported(self, *_, **__) -> bool: ...

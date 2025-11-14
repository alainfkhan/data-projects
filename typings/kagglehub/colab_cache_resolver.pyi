from _typeshed import Incomplete
from kagglehub.clients import ColabClient as ColabClient
from kagglehub.config import is_colab_cache_disabled as is_colab_cache_disabled
from kagglehub.exceptions import (
    BackendError as BackendError,
    NotFoundError as NotFoundError,
)
from kagglehub.handle import DatasetHandle as DatasetHandle, ModelHandle as ModelHandle
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK
from kagglehub.packages import PackageScope as PackageScope
from kagglehub.resolver import Resolver as Resolver

COLAB_CACHE_MOUNT_FOLDER_ENV_VAR_NAME: str
DEFAULT_COLAB_CACHE_MOUNT_FOLDER: str
logger: Incomplete

class ModelColabCacheResolver(Resolver[ModelHandle]):
    def is_supported(self, handle: ModelHandle, *_, **__) -> bool: ...

class DatasetColabCacheResolver(Resolver[DatasetHandle]):
    def is_supported(self, handle: DatasetHandle, *_, **__) -> bool: ...

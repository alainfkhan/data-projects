from _typeshed import Incomplete
from kagglehub.cache import (
    delete_from_cache as delete_from_cache,
    get_cached_archive_path as get_cached_archive_path,
    get_cached_path as get_cached_path,
    load_from_cache as load_from_cache,
    mark_as_complete as mark_as_complete,
)
from kagglehub.clients import KaggleApiV1Client as KaggleApiV1Client
from kagglehub.exceptions import UnauthenticatedError as UnauthenticatedError
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    DatasetHandle as DatasetHandle,
    ModelHandle as ModelHandle,
    NotebookHandle as NotebookHandle,
    ResourceHandle as ResourceHandle,
)
from kagglehub.packages import PackageScope as PackageScope
from kagglehub.resolver import Resolver as Resolver

DATASET_CURRENT_VERSION_FIELD: str
NOTEBOOK_CURRENT_VERSION_FIELD: str
MODEL_INSTANCE_VERSION_FIELD: str
MAX_NUM_FILES_DIRECT_DOWNLOAD: int
logger: Incomplete

class CompetitionHttpResolver(Resolver[CompetitionHandle]):
    def is_supported(self, *_, **__) -> bool: ...

class DatasetHttpResolver(Resolver[DatasetHandle]):
    def is_supported(self, *_, **__) -> bool: ...

class ModelHttpResolver(Resolver[ModelHandle]):
    def is_supported(self, *_, **__) -> bool: ...

class NotebookOutputHttpResolver(Resolver[NotebookHandle]):
    def is_supported(self, *_, **__) -> bool: ...

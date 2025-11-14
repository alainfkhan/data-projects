import pathlib
import types
from _typeshed import Incomplete
from kagglehub import registry as registry
from kagglehub.auth import get_username as get_username
from kagglehub.cache import get_cached_path as get_cached_path
from kagglehub.env import (
    is_in_colab_notebook as is_in_colab_notebook,
    is_in_kaggle_notebook as is_in_kaggle_notebook,
)
from kagglehub.exceptions import UserCancelledError as UserCancelledError
from kagglehub.handle import (
    PackageHandle as PackageHandle,
    ResourceHandle as ResourceHandle,
    parse_package_handle as parse_package_handle,
)
from kagglehub.logger import EXTRA_CONSOLE_BLOCK as EXTRA_CONSOLE_BLOCK
from kagglehub.tracker import (
    VersionedDatasources as VersionedDatasources,
    read_file as read_file,
)
from types import ModuleType

logger: Incomplete
PACKAGE_VERSION: str
PACKAGE_VERSION_NAME: str
PACKAGE_NOTEBOOK_DIR: str
EXPORTED_PACKAGE_ASSETS_DIR: str
KAGGLE_NOTEBOOK_ASSETS_STAGING_PATH: str
DEPENDENCY_MANAGER_HANDLE_NAME: str
DEPENDENCY_MANAGER_INSTALL_FILEPATH: str
KAGGLEHUB_REQUIREMENTS_FILENAME: str

def package_import(
    handle: str,
    *,
    force_download: bool | None = False,
    bypass_confirmation: bool = False,
) -> ModuleType: ...
def get_package_asset_path(path: str) -> pathlib.Path: ...

class PackageScope:
    package_module: ModuleType
    path: pathlib.Path
    datasources: VersionedDatasources
    def __init__(self, package_module: ModuleType) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def get() -> PackageScope | None: ...
    @staticmethod
    def get_version(h: ResourceHandle) -> int | None: ...

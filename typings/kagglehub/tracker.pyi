import pathlib
from _typeshed import Incomplete
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    DatasetHandle as DatasetHandle,
    ModelHandle as ModelHandle,
    NotebookHandle as NotebookHandle,
    PackageHandle as PackageHandle,
    ResourceHandle as ResourceHandle,
    UtilityScriptHandle as UtilityScriptHandle,
    parse_competition_handle as parse_competition_handle,
    parse_dataset_handle as parse_dataset_handle,
    parse_model_handle as parse_model_handle,
    parse_notebook_handle as parse_notebook_handle,
    parse_package_handle as parse_package_handle,
    parse_utility_script_handle as parse_utility_script_handle,
)

FORMAT_VERSION: str
FORMAT_VERSION_FIELD: str
DATASOURCES_FIELD: str
DATASOURCE_TYPE_FIELD: str
DATASOURCE_REF_FIELD: str
DATASOURCE_VERSION_FIELD: str
HANDLE_TYPE_NAMES: Incomplete
HANDLE_TYPE_PARSERS: Incomplete
VersionedDatasources = dict[ResourceHandle, int | None]

def register_datasource_access(handle: ResourceHandle, version: int | None) -> None: ...
def get_accessed_datasources() -> VersionedDatasources: ...
def write_file(filepath: str | pathlib.Path) -> None: ...
def read_file(filepath: str | pathlib.Path) -> VersionedDatasources: ...

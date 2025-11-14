from _typeshed import Incomplete
from kagglehub.handle import (
    CompetitionHandle as CompetitionHandle,
    DatasetHandle as DatasetHandle,
    ModelHandle as ModelHandle,
    NotebookHandle as NotebookHandle,
    ResourceHandle as ResourceHandle,
)
from kagglehub.resolver import Resolver as Resolver
from typing import Generic, TypeVar

T = TypeVar("T", bound=ResourceHandle)

class MultiImplRegistry(Generic[T]):
    def __init__(self, name: str) -> None: ...
    def add_implementation(self, impl: Resolver[T]) -> None: ...
    def __call__(self, *args, **kwargs) -> tuple[str, int | None]: ...

model_resolver: Incomplete
dataset_resolver: Incomplete
competition_resolver: Incomplete
notebook_output_resolver: Incomplete

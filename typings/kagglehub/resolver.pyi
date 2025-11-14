import abc
from kagglehub.handle import ResourceHandle as ResourceHandle
from kagglehub.tracker import register_datasource_access as register_datasource_access
from typing import Generic, TypeVar

T = TypeVar("T", bound=ResourceHandle)

class Resolver(Generic[T], metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta
    def __call__(
        self, handle: T, path: str | None = None, *, force_download: bool | None = False
    ) -> tuple[str, int | None]: ...
    @abc.abstractmethod
    def is_supported(self, handle: T, path: str | None = None) -> bool: ...

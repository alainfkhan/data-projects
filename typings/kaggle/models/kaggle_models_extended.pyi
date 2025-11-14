from _typeshed import Incomplete

class Competition:
    tags: Incomplete
    def __init__(self, init_dict) -> None: ...

class SubmitResult:
    def __init__(self, init_dict) -> None: ...

class Submission:
    size: Incomplete
    def __init__(self, init_dict) -> None: ...

class LeaderboardEntry:
    def __init__(self, init_dict) -> None: ...

class Dataset:
    tags: Incomplete
    files: Incomplete
    versions: Incomplete
    size: Incomplete
    def __init__(self, init_dict) -> None: ...

class Model:
    def __init__(self, init_dict) -> None: ...

class Metadata:
    id: Incomplete
    id_no: Incomplete
    def __init__(self, init_info) -> None: ...

class DatasetVersion:
    def __init__(self, init_dict) -> None: ...

class File:
    size: Incomplete
    name: Incomplete
    creation_date: Incomplete
    def __init__(self, init_dict) -> None: ...
    @staticmethod
    def get_size(size, precision: int = 0): ...

class Tag:
    def __init__(self, init_dict) -> None: ...

class DatasetNewVersionResponse:
    def __init__(self, init_dict) -> None: ...

class DatasetNewResponse:
    def __init__(self, init_dict) -> None: ...

class ListFilesResult:
    error_message: Incomplete
    files: Incomplete
    nextPageToken: Incomplete
    def __init__(self, init_dict) -> None: ...

class Kernel:
    def __init__(self, init_dict) -> None: ...

class KernelPushResponse:
    def __init__(self, init_dict) -> None: ...

class ModelNewResponse:
    def __init__(self, init_dict) -> None: ...

class ModelDeleteResponse:
    def __init__(self, init_dict) -> None: ...

def parse(string): ...

class ResumableUploadResult:
    COMPLETE: int
    FAILED: int
    INCOMPLETE: int
    result: Incomplete
    bytes_uploaded: Incomplete
    start_at: Incomplete
    def __init__(self, result, bytes_uploaded=None) -> None: ...
    @staticmethod
    def Complete(): ...
    @staticmethod
    def Failed(): ...
    @staticmethod
    def Incomplete(bytes_uploaded=None): ...

from _typeshed import Incomplete
from datasets import Dataset
from kagglehub.pandas_datasets import load_pandas_dataset as load_pandas_dataset
from typing import Any

MULTIPLE_DATA_FRAMES_ERROR_MESSAGE: str
DEFAULT_PANDAS_KWARGS: Incomplete

def load_hf_dataset(
    handle: str,
    path: str,
    *,
    pandas_kwargs: Any = None,
    sql_query: str | None = None,
    hf_kwargs: Any = None,
) -> Dataset: ...

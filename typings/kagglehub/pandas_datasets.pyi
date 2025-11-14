import pandas as pd
from kagglehub.datasets import dataset_download as dataset_download
from typing import Any, Callable

def wrapped_read_sql_query(sql_query: str, path: str) -> pd.DataFrame: ...

SUPPORTED_READ_FUNCTIONS_BY_EXTENSION: dict[str, Callable]
STATIC_KWARGS_BY_EXTENSION: dict[str, dict[str, str | bool]]
MISSING_SQL_QUERY_ERROR_MESSAGE: str

def load_pandas_dataset(
    handle: str, path: str, *, pandas_kwargs: Any = None, sql_query: str | None
) -> pd.DataFrame | dict[int | str, pd.DataFrame]: ...

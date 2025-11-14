import polars as pl
from kagglehub.datasets import (
    PolarsFrameType as PolarsFrameType,
    dataset_download as dataset_download,
)
from typing import Any, Callable

def wrapped_read_database(sql_query: str, path: str) -> pl.DataFrame: ...

SUPPORTED_READ_FUNCTIONS_BY_EXTENSION: dict[str, Callable]
SUPPORTED_SCAN_FUNCTIONS_BY_EXTENSION: dict[str, Callable]
STATIC_KWARGS_BY_EXTENSION: dict[str, dict[str, str | bool]]
MISSING_SQL_QUERY_ERROR_MESSAGE: str

def load_polars_dataset(
    handle: str,
    path: str,
    *,
    polars_frame_type: PolarsFrameType = ...,
    polars_kwargs: Any = None,
    sql_query: str | None,
) -> pl.DataFrame | dict[int | str, pl.DataFrame]: ...

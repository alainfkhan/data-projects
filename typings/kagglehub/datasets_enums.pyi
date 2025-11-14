from enum import Enum

class KaggleDatasetAdapter(Enum):
    HUGGING_FACE = "hugging_face"
    PANDAS = "pandas"
    POLARS = "polars"

class PolarsFrameType(Enum):
    LAZY_FRAME = 1
    DATA_FRAME = 2

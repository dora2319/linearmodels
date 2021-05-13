import sys
from typing import TYPE_CHECKING, Any, Hashable, Optional, Sequence, Union

import numpy as np
from pandas import DataFrame, Series

from .data import ArrayLike, OptionalArrayLike

NP_GTE_121 = np.lib.NumpyVersion(np.__version__) >= np.lib.NumpyVersion("1.21.0")


__all__ = [
    "ArrayLike",
    "OptionalArrayLike",
    "Numeric",
    "OptionalNumeric",
    "AnyPandas",
    "Label",
    "NDArray",
    "ArraySequence",
]

# Workaround for https://github.com/python/mypy/issues/7866
NDArray = Union[np.ndarray]
ArraySequence = Sequence[np.ndarray]

Numeric = Union[int, float]
OptionalNumeric = Optional[Union[int, float]]

AnyPandas = Union[Series, DataFrame]
Label = Optional[Hashable]

if sys.version_info >= (3, 8):
    from typing import Literal
elif TYPE_CHECKING:
    from typing_extensions import Literal
else:

    class _Literal:
        def __getitem__(self, item):
            pass

    Literal = _Literal()

if NP_GTE_121:
    Float64Array = np.ndarray[Any, np.dtype[np.float64]]
    Int64Array = np.ndarray[Any, np.dtype[np.int64]]
    Int32Array = np.ndarray[Any, np.dtype[np.int32]]
    IntArray = np.ndarray[Any, np.dtype[np.int_]]
    BoolArray = np.ndarray[Any, np.dtype[np.bool_]]
    AnyArray = np.ndarray[Any, Any]
else:
    IntArray = Float64Array = Int64Array = Int32Array = BoolArray = AnyArray = NDArray

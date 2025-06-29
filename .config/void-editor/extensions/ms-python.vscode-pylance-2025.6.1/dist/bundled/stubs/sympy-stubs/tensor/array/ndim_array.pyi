import sys
from collections.abc import Iterator
from typing import Any
from typing_extensions import Self, TypeAlias

from sympy import ImmutableDenseNDimArray, ImmutableSparseNDimArray
from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.core.kind import Kind
from sympy.printing.defaults import Printable
from sympy.tensor.array.array_derivatives import ArrayDerivative
from sympy.tensor.array.expressions.array_expressions import ArrayContraction, ArrayTensorProduct, PermuteDims, ZeroArray

if sys.version_info >= (3, 10):
    from types import NotImplementedType
else:
    NotImplementedType: TypeAlias = Any

class ArrayKind(Kind):
    def __new__(cls, element_kind=...) -> Self: ...
    def __repr__(self): ...

class NDimArray(Printable):
    _diff_wrt = ...
    is_scalar = ...
    def __new__(cls, iterable, shape=..., **kwargs) -> ImmutableDenseNDimArray: ...
    def __getitem__(self, index): ...
    def __len__(self): ...
    @property
    def shape(self): ...
    def rank(self): ...
    def diff(self, *args, **kwargs) -> ArrayDerivative: ...
    def applyfunc(self, f) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray: ...
    def tolist(self) -> list[Any]: ...
    def __add__(self, other) -> NotImplementedType | Self: ...
    def __sub__(self, other) -> NotImplementedType | Self: ...
    def __mul__(self, other) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray: ...
    def __rmul__(self, other) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray: ...
    def __truediv__(self, other) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray: ...
    def __rtruediv__(self, other): ...
    def __neg__(self) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def transpose(
        self,
    ) -> (
        ZeroArray
        | ArrayTensorProduct
        | ArrayContraction
        | Basic
        | PermuteDims
        | ImmutableSparseNDimArray
        | ImmutableDenseNDimArray
    ): ...
    def conjugate(self): ...
    def adjoint(self) -> type[UndefinedFunction]: ...

class ImmutableNDimArray(NDimArray, Basic):
    _op_priority = ...
    def __hash__(self) -> int: ...
    def as_immutable(self) -> Self: ...
    def as_mutable(self): ...

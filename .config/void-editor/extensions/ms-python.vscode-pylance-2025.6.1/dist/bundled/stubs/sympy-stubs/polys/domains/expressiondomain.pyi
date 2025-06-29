import sys
from typing import Any
from typing_extensions import Self, TypeAlias

from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.polyutils import PicklableWithSlots
from sympy.utilities import public

if sys.version_info >= (3, 10):
    from types import NotImplementedType
else:
    NotImplementedType: TypeAlias = Any

eflags = ...

@public
class ExpressionDomain(Field, CharacteristicZero, SimpleDomain):
    is_EX = ...

    class Expression(PicklableWithSlots):
        __slots__ = ...
        def __init__(self, ex) -> None: ...
        def __hash__(self) -> int: ...
        def as_expr(f): ...
        def numer(f) -> Self: ...
        def denom(f) -> Self: ...
        def simplify(f, ex) -> Self: ...
        def __abs__(f) -> Self: ...
        def __neg__(f) -> Self: ...
        def __add__(f, g) -> NotImplementedType | Self: ...
        def __radd__(f, g) -> Self: ...
        def __sub__(f, g) -> NotImplementedType | Self: ...
        def __rsub__(f, g) -> Self: ...
        def __mul__(f, g) -> NotImplementedType | Self: ...  # | Expression
        def __rmul__(f, g) -> Self: ...
        def __pow__(f, n) -> Self | NotImplementedType: ...
        def __truediv__(f, g) -> Self | NotImplementedType: ...
        def __rtruediv__(f, g) -> Self: ...
        def __eq__(f, g) -> bool: ...
        def __ne__(f, g) -> bool: ...
        def __bool__(f) -> bool: ...
        def gcd(f, g) -> Self: ...
        def lcm(f, g) -> Self: ...

    dtype = Expression
    zero = ...
    one = ...
    rep = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def __init__(self) -> None: ...
    def to_sympy(self, a): ...
    def from_sympy(self, a) -> Expression: ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_GaussianIntegerRing(K1, a, K0): ...
    def from_GaussianRationalField(K1, a, K0): ...
    def from_RealField(K1, a, K0): ...
    def from_PolynomialRing(K1, a, K0): ...
    def from_FractionField(K1, a, K0): ...
    def from_ExpressionDomain(K1, a, K0): ...
    def get_ring(self) -> Self: ...
    def get_field(self) -> Self: ...
    def is_positive(self, a): ...
    def is_negative(self, a): ...
    def is_nonpositive(self, a): ...
    def is_nonnegative(self, a): ...
    def numer(self, a): ...
    def denom(self, a): ...
    def gcd(self, a, b): ...
    def lcm(self, a, b): ...

EX = ...

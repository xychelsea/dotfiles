from typing import Any, ClassVar, Final, Literal, TypedDict, type_check_only

from .drawing import DeviceGray, DeviceRGB
from .enums import TextMode
from .fonts import FontFace

@type_check_only
class _TextShaping(TypedDict):
    use_shaping_engine: bool
    features: dict[str, bool]
    direction: Literal["ltr", "rtl"]
    script: str | None
    language: str | None
    fragment_direction: Literal["L", "R"] | None
    paragraph_direction: Literal["L", "R"] | None

class GraphicsStateMixin:
    DEFAULT_DRAW_COLOR: ClassVar[DeviceGray]
    DEFAULT_FILL_COLOR: ClassVar[DeviceGray]
    DEFAULT_TEXT_COLOR: ClassVar[DeviceGray]
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def draw_color(self) -> DeviceGray | DeviceRGB: ...
    @draw_color.setter
    def draw_color(self, v: DeviceGray | DeviceRGB) -> None: ...
    @property
    def fill_color(self) -> DeviceGray | DeviceRGB: ...
    @fill_color.setter
    def fill_color(self, v: DeviceGray | DeviceRGB) -> None: ...
    @property
    def text_color(self) -> DeviceGray | DeviceRGB: ...
    @text_color.setter
    def text_color(self, v: DeviceGray | DeviceRGB) -> None: ...
    @property
    def underline(self) -> bool: ...
    @underline.setter
    def underline(self, v: bool) -> None: ...
    @property
    def strikethrough(self) -> bool: ...
    @strikethrough.setter
    def strikethrough(self, v: bool) -> None: ...
    @property
    def font_style(self) -> str: ...
    @font_style.setter
    def font_style(self, v: str) -> None: ...
    @property
    def font_stretching(self) -> float: ...
    @font_stretching.setter
    def font_stretching(self, v: float) -> None: ...
    @property
    def char_spacing(self) -> float: ...
    @char_spacing.setter
    def char_spacing(self, v: float) -> None: ...
    @property
    def font_family(self) -> str: ...
    @font_family.setter
    def font_family(self, v: str) -> None: ...
    @property
    def font_size_pt(self) -> float: ...
    @font_size_pt.setter
    def font_size_pt(self, v: float) -> None: ...
    @property
    def font_size(self) -> float: ...
    @font_size.setter
    def font_size(self, v: float) -> None: ...
    @property
    def current_font(self) -> dict[str, Any]: ...
    @current_font.setter
    def current_font(self, v: dict[str, Any]) -> None: ...
    @property
    def current_font_is_set_on_page(self) -> bool: ...
    @current_font_is_set_on_page.setter
    def current_font_is_set_on_page(self, v: bool) -> None: ...
    @property
    def dash_pattern(self) -> dict[str, float]: ...
    @dash_pattern.setter
    def dash_pattern(self, v: dict[str, float]) -> None: ...
    @property
    def line_width(self) -> float: ...
    @line_width.setter
    def line_width(self, v: float) -> None: ...
    @property
    def text_mode(self) -> TextMode: ...
    @text_mode.setter
    def text_mode(self, v: int | str) -> None: ...
    @property
    def char_vpos(self): ...
    @char_vpos.setter
    def char_vpos(self, v) -> None: ...
    @property
    def sub_scale(self): ...
    @sub_scale.setter
    def sub_scale(self, v) -> None: ...
    @property
    def sup_scale(self): ...
    @sup_scale.setter
    def sup_scale(self, v) -> None: ...
    @property
    def nom_scale(self): ...
    @nom_scale.setter
    def nom_scale(self, v) -> None: ...
    @property
    def denom_scale(self): ...
    @denom_scale.setter
    def denom_scale(self, v) -> None: ...
    @property
    def sub_lift(self): ...
    @sub_lift.setter
    def sub_lift(self, v) -> None: ...
    @property
    def sup_lift(self): ...
    @sup_lift.setter
    def sup_lift(self, v) -> None: ...
    @property
    def nom_lift(self): ...
    @nom_lift.setter
    def nom_lift(self, v) -> None: ...
    @property
    def denom_lift(self): ...
    @denom_lift.setter
    def denom_lift(self, v) -> None: ...
    @property
    def text_shaping(self) -> _TextShaping | None: ...
    @text_shaping.setter
    def text_shaping(self, v: _TextShaping | None) -> None: ...
    def font_face(self) -> FontFace: ...

__pdoc__: Final[dict[str, bool]]

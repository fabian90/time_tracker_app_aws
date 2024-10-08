from collections.abc import Callable
from typing import Any

def construct_format_field_str(fname: str, fspec: str, conv: str) -> str: ...
def infer_positional_format_args(fstr: str) -> str: ...
def get_format_args(fstr: str) -> tuple[list[tuple[int, type]], list[tuple[str, type]]]: ...
def tokenize_format_str(fstr: str, resolve_pos: bool = True) -> list[str | BaseFormatField]: ...

class BaseFormatField:
    def __init__(self, fname: str, fspec: str = "", conv: str | None = None) -> None: ...
    base_name: str
    fname: str
    subpath: str
    is_positional: bool
    def set_fname(self, fname: str) -> None: ...
    subfields: list[str]
    fspec: str
    type_char: str
    type_func: str
    def set_fspec(self, fspec) -> None: ...
    conv: str
    conv_func: str | None
    def set_conv(self, conv: str) -> None: ...
    @property
    def fstr(self) -> str: ...

class DeferredValue:
    func: Callable[..., Any]
    cache_value: bool
    def __init__(self, func: Callable[..., Any], cache_value: bool = True) -> None: ...
    def get_value(self) -> Any: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __unicode__(self) -> str: ...
    def __format__(self, fmt: str) -> str: ...

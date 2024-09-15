from _typeshed import ReadableBuffer, SupportsWrite
from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Any, ClassVar, Protocol, SupportsBytes, SupportsIndex, final
from typing_extensions import TypeAlias

__all__ = [
    "PickleBuffer",
    "PickleError",
    "PicklingError",
    "UnpicklingError",
    "Pickler",
    "Unpickler",
    "dump",
    "dumps",
    "load",
    "loads",
    "ADDITEMS",
    "APPEND",
    "APPENDS",
    "BINBYTES",
    "BINBYTES8",
    "BINFLOAT",
    "BINGET",
    "BININT",
    "BININT1",
    "BININT2",
    "BINPERSID",
    "BINPUT",
    "BINSTRING",
    "BINUNICODE",
    "BINUNICODE8",
    "BUILD",
    "BYTEARRAY8",
    "DEFAULT_PROTOCOL",
    "DICT",
    "DUP",
    "EMPTY_DICT",
    "EMPTY_LIST",
    "EMPTY_SET",
    "EMPTY_TUPLE",
    "EXT1",
    "EXT2",
    "EXT4",
    "FALSE",
    "FLOAT",
    "FRAME",
    "FROZENSET",
    "GET",
    "GLOBAL",
    "HIGHEST_PROTOCOL",
    "INST",
    "INT",
    "LIST",
    "LONG",
    "LONG1",
    "LONG4",
    "LONG_BINGET",
    "LONG_BINPUT",
    "MARK",
    "MEMOIZE",
    "NEWFALSE",
    "NEWOBJ",
    "NEWOBJ_EX",
    "NEWTRUE",
    "NEXT_BUFFER",
    "NONE",
    "OBJ",
    "PERSID",
    "POP",
    "POP_MARK",
    "PROTO",
    "PUT",
    "READONLY_BUFFER",
    "REDUCE",
    "SETITEM",
    "SETITEMS",
    "SHORT_BINBYTES",
    "SHORT_BINSTRING",
    "SHORT_BINUNICODE",
    "STACK_GLOBAL",
    "STOP",
    "STRING",
    "TRUE",
    "TUPLE",
    "TUPLE1",
    "TUPLE2",
    "TUPLE3",
    "UNICODE",
]

HIGHEST_PROTOCOL: int
DEFAULT_PROTOCOL: int

bytes_types: tuple[type[Any], ...]  # undocumented

class _ReadableFileobj(Protocol):
    def read(self, n: int, /) -> bytes: ...
    def readline(self) -> bytes: ...

@final
class PickleBuffer:
    def __init__(self, buffer: ReadableBuffer) -> None: ...
    def raw(self) -> memoryview: ...
    def release(self) -> None: ...
    def __buffer__(self, flags: int, /) -> memoryview: ...
    def __release_buffer__(self, buffer: memoryview, /) -> None: ...

_BufferCallback: TypeAlias = Callable[[PickleBuffer], Any] | None

def dump(
    obj: Any,
    file: SupportsWrite[bytes],
    protocol: int | None = None,
    *,
    fix_imports: bool = True,
    buffer_callback: _BufferCallback = None,
) -> None: ...
def dumps(
    obj: Any, protocol: int | None = None, *, fix_imports: bool = True, buffer_callback: _BufferCallback = None
) -> bytes: ...
def load(
    file: _ReadableFileobj,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
    buffers: Iterable[Any] | None = (),
) -> Any: ...
def loads(
    data: ReadableBuffer,
    /,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
    buffers: Iterable[Any] | None = (),
) -> Any: ...

class PickleError(Exception): ...
class PicklingError(PickleError): ...
class UnpicklingError(PickleError): ...

_ReducedType: TypeAlias = (
    str
    | tuple[Callable[..., Any], tuple[Any, ...]]
    | tuple[Callable[..., Any], tuple[Any, ...], Any]
    | tuple[Callable[..., Any], tuple[Any, ...], Any, Iterator[Any] | None]
    | tuple[Callable[..., Any], tuple[Any, ...], Any, Iterator[Any] | None, Iterator[Any] | None]
)

class Pickler:
    fast: bool
    dispatch_table: Mapping[type, Callable[[Any], _ReducedType]]
    bin: bool  # undocumented
    dispatch: ClassVar[dict[type, Callable[[Unpickler, Any], None]]]  # undocumented, _Pickler only

    def __init__(
        self,
        file: SupportsWrite[bytes],
        protocol: int | None = ...,
        *,
        fix_imports: bool = ...,
        buffer_callback: _BufferCallback = ...,
    ) -> None: ...
    def reducer_override(self, obj: Any) -> Any: ...
    def dump(self, obj: Any, /) -> None: ...
    def clear_memo(self) -> None: ...
    def persistent_id(self, obj: Any) -> Any: ...

class Unpickler:
    dispatch: ClassVar[dict[int, Callable[[Unpickler], None]]]  # undocumented, _Unpickler only

    def __init__(
        self,
        file: _ReadableFileobj,
        *,
        fix_imports: bool = ...,
        encoding: str = ...,
        errors: str = ...,
        buffers: Iterable[Any] | None = ...,
    ) -> None: ...
    def load(self) -> Any: ...
    def find_class(self, module_name: str, global_name: str, /) -> Any: ...
    def persistent_load(self, pid: Any) -> Any: ...

MARK: bytes
STOP: bytes
POP: bytes
POP_MARK: bytes
DUP: bytes
FLOAT: bytes
INT: bytes
BININT: bytes
BININT1: bytes
LONG: bytes
BININT2: bytes
NONE: bytes
PERSID: bytes
BINPERSID: bytes
REDUCE: bytes
STRING: bytes
BINSTRING: bytes
SHORT_BINSTRING: bytes
UNICODE: bytes
BINUNICODE: bytes
APPEND: bytes
BUILD: bytes
GLOBAL: bytes
DICT: bytes
EMPTY_DICT: bytes
APPENDS: bytes
GET: bytes
BINGET: bytes
INST: bytes
LONG_BINGET: bytes
LIST: bytes
EMPTY_LIST: bytes
OBJ: bytes
PUT: bytes
BINPUT: bytes
LONG_BINPUT: bytes
SETITEM: bytes
TUPLE: bytes
EMPTY_TUPLE: bytes
SETITEMS: bytes
BINFLOAT: bytes

TRUE: bytes
FALSE: bytes

# protocol 2
PROTO: bytes
NEWOBJ: bytes
EXT1: bytes
EXT2: bytes
EXT4: bytes
TUPLE1: bytes
TUPLE2: bytes
TUPLE3: bytes
NEWTRUE: bytes
NEWFALSE: bytes
LONG1: bytes
LONG4: bytes

# protocol 3
BINBYTES: bytes
SHORT_BINBYTES: bytes

# protocol 4
SHORT_BINUNICODE: bytes
BINUNICODE8: bytes
BINBYTES8: bytes
EMPTY_SET: bytes
ADDITEMS: bytes
FROZENSET: bytes
NEWOBJ_EX: bytes
STACK_GLOBAL: bytes
MEMOIZE: bytes
FRAME: bytes

# protocol 5
BYTEARRAY8: bytes
NEXT_BUFFER: bytes
READONLY_BUFFER: bytes

def encode_long(x: int) -> bytes: ...  # undocumented
def decode_long(data: Iterable[SupportsIndex] | SupportsBytes | ReadableBuffer) -> int: ...  # undocumented

# pure-Python implementations
_Pickler = Pickler  # undocumented
_Unpickler = Unpickler  # undocumented

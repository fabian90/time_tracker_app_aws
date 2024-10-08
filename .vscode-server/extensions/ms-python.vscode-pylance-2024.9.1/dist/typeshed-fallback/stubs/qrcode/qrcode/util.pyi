from _typeshed import Incomplete
from collections.abc import Callable, Generator
from typing import Final, Literal, overload
from typing_extensions import TypeAlias

from qrcode.base import RSBlock as RSBlock

_MaskPattern: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]

MODE_NUMBER: Final = 1
MODE_ALPHA_NUM: Final = 2
MODE_8BIT_BYTE: Final = 4
MODE_KANJI: Final = 8

MODE_SIZE_SMALL: Incomplete
MODE_SIZE_MEDIUM: Incomplete
MODE_SIZE_LARGE: Incomplete

ALPHA_NUM: bytes
RE_ALPHA_NUM: Incomplete
NUMBER_LENGTH: Incomplete
PATTERN_POSITION_TABLE: Incomplete
G15: Incomplete
G18: Incomplete
G15_MASK: Incomplete
PAD0: int
PAD1: int
BIT_LIMIT_TABLE: Incomplete

def BCH_type_info(data): ...
def BCH_type_number(data): ...
def BCH_digit(data): ...
def pattern_position(version): ...
def mask_func(pattern: _MaskPattern) -> Callable[[int, int], bool]: ...
def mode_sizes_for_version(version): ...
def length_in_bits(mode, version): ...
def check_version(version) -> None: ...
def lost_point(modules): ...
def optimal_data_chunks(data: str | bytes, minimum: int = 4) -> Generator[QRData, None, None]: ...
def to_bytestring(data: str | bytes) -> bytes: ...
def optimal_mode(data) -> Literal[1, 2, 4]: ...

class QRData:
    mode: Literal[1, 2, 4]
    data: bytes
    @overload
    def __init__(self, data: bytes | str, mode: Literal[1, 2, 4] | None = None, check_data: Literal[True] = True) -> None: ...
    @overload
    def __init__(self, data: bytes, mode: Literal[1, 2, 4] | None = None, *, check_data: Literal[False]) -> None: ...
    @overload
    def __init__(self, data: bytes, mode: Literal[1, 2, 4] | None, check_data: Literal[False]) -> None: ...
    def __len__(self) -> int: ...
    def write(self, buffer: BitBuffer) -> None: ...

class BitBuffer:
    buffer: Incomplete
    length: int
    def __init__(self) -> None: ...
    def get(self, index): ...
    def put(self, num, length) -> None: ...
    def __len__(self) -> int: ...
    def put_bit(self, bit) -> None: ...

def create_bytes(buffer: BitBuffer, rs_blocks: list[RSBlock]): ...
def create_data(version, error_correction, data_list): ...

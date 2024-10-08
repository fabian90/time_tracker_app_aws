import datetime
from _typeshed import Incomplete, SupportsItems
from collections.abc import Generator
from typing import Final, Literal, TypeVar

from reportlab.lib.rltempfile import get_rl_tempdir as get_rl_tempdir, get_rl_tempfile as get_rl_tempfile

from .rl_safe_eval import (
    rl_extended_literal_eval as rl_extended_literal_eval,
    rl_safe_exec as rl_safe_exec,
    safer_globals as safer_globals,
)

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

__version__: Final[str]

class _UNSET_:
    @staticmethod
    def __bool__() -> Literal[False]: ...

__UNSET__: Final[_UNSET_]

isPyPy: bool

def isFunction(v): ...
def isMethod(v, mt=...): ...
def isModule(v): ...
def isSeq(v, _st=...): ...
def isNative(v): ...

strTypes: Incomplete

def asBytes(v, enc: str = "utf8"): ...
def asUnicode(v, enc: str = "utf8"): ...
def asUnicodeEx(v, enc: str = "utf8"): ...
def asNative(v, enc: str = "utf8"): ...
def int2Byte(i): ...
def isStr(v): ...
def isBytes(v): ...
def isUnicode(v): ...
def isClass(v): ...
def isNonPrimitiveInstance(x): ...
def instantiated(v): ...
def bytestr(x, enc: str = "utf8"): ...
def encode_label(args): ...
def decode_label(label): ...
def rawUnicode(s): ...
def rawBytes(s): ...

rl_exec: Incomplete

def char2int(s): ...
def rl_reraise(t, v, b: Incomplete | None = None) -> None: ...
def rl_add_builtins(**kwd) -> None: ...
def zipImported(ldr: Incomplete | None = None): ...

class CIDict(dict[_KT, _VT]):
    def __init__(self, *args, **kwds) -> None: ...
    def update(self, D: SupportsItems[_KT, _VT]) -> None: ...  # type:ignore[override]

def markfilename(filename, creatorcode: Incomplete | None = None, filetype: Incomplete | None = None): ...

__rl_loader__: Incomplete

def rl_glob(pattern, glob=...): ...
def isFileSystemDistro(): ...
def isCompactDistro(): ...
def isSourceDistro(): ...
def normalize_path(p): ...
def recursiveImport(modulename, baseDir: Incomplete | None = None, noCWD: int = 0, debug: int = 0): ...

haveImages: Incomplete

class ArgvDictValue:
    value: Incomplete
    func: Incomplete
    def __init__(self, value, func) -> None: ...

def getArgvDict(**kw): ...
def getHyphenater(hDict: Incomplete | None = None): ...
def open_for_read_by_name(name, mode: str = "b"): ...
def rlUrlRead(name): ...
def open_for_read(name, mode: str = "b"): ...
def open_and_read(name, mode: str = "b"): ...
def open_and_readlines(name, mode: str = "t"): ...
def rl_isfile(fn, os_path_isfile=...): ...
def rl_isdir(pn, os_path_isdir=..., os_path_normpath=...): ...
def rl_listdir(pn, os_path_isdir=..., os_path_normpath=..., os_listdir=...): ...
def rl_getmtime(pn, os_path_isfile=..., os_path_normpath=..., os_path_getmtime=..., time_mktime=...): ...
def __rl_get_module__(name, dir): ...
def rl_get_module(name, dir): ...

class ImageReader:
    fileName: Incomplete
    fp: Incomplete
    def __init__(self, fileName, ident: Incomplete | None = None) -> None: ...
    def identity(self) -> str: ...
    @classmethod
    def check_pil_image_size(cls, im) -> None: ...
    @classmethod
    def set_max_image_size(cls, max_image_size: Incomplete | None = None) -> None: ...
    def jpeg_fh(self) -> None: ...
    def getSize(self) -> tuple[int, int]: ...
    mode: Incomplete
    def getRGBData(self): ...
    def getImageData(self): ...
    def getTransparent(self): ...

class LazyImageReader(ImageReader): ...

def getImageData(imageFileName): ...

class DebugMemo:
    fn: Incomplete
    stdout: Incomplete
    store: Incomplete
    def __init__(
        self,
        fn: str = "rl_dbgmemo.dbg",
        mode: str = "w",
        getScript: int = 1,
        modules=(),
        capture_traceback: int = 1,
        stdout: Incomplete | None = None,
        **kw,
    ) -> None: ...
    def add(self, **kw) -> None: ...
    def dump(self) -> None: ...
    def dumps(self): ...
    def load(self) -> None: ...
    def loads(self, s) -> None: ...
    specials: Incomplete
    def show(self) -> None: ...
    def payload(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def __getitem__(self, name): ...

def flatten(L): ...
def find_locals(func, depth: int = 0): ...

class _FmtSelfDict:
    obj: Incomplete
    def __init__(self, obj, overrideArgs) -> None: ...
    def __getitem__(self, k): ...

class FmtSelfDict: ...

def simpleSplit(text, fontName, fontSize, maxWidth): ...
def escapeTextOnce(text): ...
def fileName2FSEnc(fn): ...
def prev_this_next(items): ...
def commasplit(s): ...
def commajoin(l): ...
def findInPaths(fn, paths, isfile: bool = True, fail: bool = False): ...
def annotateException(msg, enc: str = "utf8", postMsg: str = "", sep: str = " ") -> None: ...
def escapeOnce(data): ...

class IdentStr(str):
    def __new__(cls, value): ...

class RLString(str):
    def __new__(cls, v, **kwds): ...

def makeFileName(s): ...

class FixedOffsetTZ(datetime.tzinfo):
    def __init__(self, h, m, name) -> None: ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...

class TimeStamp:
    tzname: str
    t: Incomplete
    lt: Incomplete
    YMDhms: Incomplete
    dhh: Incomplete
    dmm: Incomplete
    def __init__(self, invariant: Incomplete | None = None) -> None: ...
    @property
    def datetime(self): ...
    @property
    def asctime(self): ...

def recursiveGetAttr(obj, name, g: Incomplete | None = None): ...
def recursiveSetAttr(obj, name, value) -> None: ...
def recursiveDelAttr(obj, name) -> None: ...
def yieldNoneSplits(L) -> Generator[Incomplete, None, None]: ...

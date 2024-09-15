import types
from collections.abc import Iterable, Iterator, Mapping, Sequence
from datetime import date, datetime, time
from decimal import Decimal
from typing import IO, Any
from typing_extensions import Literal
from uuid import UUID

import psycopg2.extensions
from django.db.backends.postgresql.base import DatabaseWrapper
from psycopg2.extensions import Column

logger: Any

# Python types that can be adapted to SQL.
_Mixed = None | bool | int | float | Decimal | str | bytes | datetime | UUID
_SQLType = _Mixed | Sequence[_Mixed] | Mapping[str, _Mixed]

class CursorWrapper:
    cursor: psycopg2.extensions.cursor = ...
    db: DatabaseWrapper = ...
    def __init__(
        self, cursor: psycopg2.extensions.cursor, db: DatabaseWrapper
    ) -> None: ...
    WRAP_ERROR_ATTRS: Any = ...
    def __iter__(self) -> Iterator[tuple[Any, ...]]: ...
    def __next__(self) -> tuple[Any, ...]: ...
    def __enter__(self) -> CursorWrapper: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None: ...
    def callproc(
        self,
        procname: str,
        params: Sequence[_SQLType] | None = ...,
        kparams: Mapping[str, int] | None = ...,
    ) -> None: ...
    def execute(
        self,
        sql: str,
        params: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> None: ...
    def executemany(
        self,
        sql: str,
        param_list: Sequence[Sequence[_SQLType] | Mapping[str, _SQLType] | None],
    ) -> None: ...
    # copied over from psycopg2 since Django uses __getattr__ to proxy calls
    @property
    def description(self) -> tuple[Column, ...] | None: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    @property
    def connection(self) -> psycopg2.extensions.connection: ...
    @property
    def name(self) -> str | None: ...
    scrollable: bool | None
    withhold: bool
    def mogrify(
        self,
        operation: str,
        parameters: Sequence[_SQLType] | Mapping[str, _SQLType] | None = ...,
    ) -> bytes: ...
    def setinputsizes(self, sizes: int) -> None: ...
    def fetchone(self) -> tuple[Any, ...] | None: ...
    def fetchmany(self, size: int = ...) -> list[tuple[Any, ...]]: ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...
    def scroll(
        self, value: int, mode: Literal["relative", "absolute"] = ...
    ) -> None: ...
    arraysize: int
    itersize: int
    @property
    def rowcount(self) -> int: ...
    @property
    def rownumber(self) -> int: ...
    @property
    def lastrowid(self) -> int | None: ...
    @property
    def query(self) -> str | None: ...
    @property
    def statusmessage(self) -> str | None: ...
    def cast(self, oid: int, s: str) -> Any: ...
    tzinfo_factory: Any
    def nextset(self) -> None: ...
    def setoutputsize(self, size: int, column: int = ...) -> None: ...
    def copy_from(
        self,
        file: IO[str],
        table: str,
        sep: str = ...,
        null: str = ...,
        size: int = ...,
        columns: Iterable[str] | None = ...,
    ) -> None: ...
    def copy_to(
        self,
        file: IO[str],
        table: str,
        sep: str = ...,
        null: str = ...,
        columns: str | None = ...,
    ) -> None: ...
    def copy_expert(self, sql: str, file: IO[str], size: int = ...) -> None: ...

class CursorDebugWrapper(CursorWrapper):
    cursor: Any
    db: Any

def typecast_date(s: str | None) -> date | None: ...
def typecast_time(s: str | None) -> time | None: ...
def typecast_timestamp(s: str | None) -> date | None: ...
def rev_typecast_decimal(d: Decimal) -> str: ...
def split_identifier(identifier: str) -> tuple[str, str]: ...
def truncate_name(
    identifier: str, length: int | None = ..., hash_len: int = ...
) -> str: ...
def format_number(
    value: Decimal | None, max_digits: int | None, decimal_places: int | None
) -> str | None: ...
def strip_quotes(table_name: str) -> str: ...

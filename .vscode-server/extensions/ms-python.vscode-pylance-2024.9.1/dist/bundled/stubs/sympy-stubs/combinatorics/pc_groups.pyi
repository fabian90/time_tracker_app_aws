from typing import Any, Literal

from sympy.printing.defaults import DefaultPrinting

class PolycyclicGroup(DefaultPrinting):
    is_group = ...
    is_solvable = ...
    def __init__(self, pc_sequence, pc_series, relative_order, collector=...) -> None: ...
    def is_prime_order(self) -> bool: ...
    def length(self) -> int: ...

class Collector(DefaultPrinting):
    def __init__(self, pcgs, pc_series, relative_order, free_group_=..., pc_presentation=...) -> None: ...
    def minimal_uncollected_subword(
        self, word
    ) -> tuple[tuple[Any, Any]] | tuple[tuple[Any, Any], tuple[Any, Literal[1, -1]]] | None: ...
    def relations(self) -> tuple[dict[Any, Any], dict[Any, Any]]: ...
    def subword_index(self, word, w) -> tuple[Literal[-1], Literal[-1]] | tuple[int, int]: ...
    def map_relation(self, w): ...
    def collected_word(self, word): ...
    def pc_relators(self) -> dict[Any, Any]: ...
    def exponent_vector(self, element) -> list[int]: ...
    def depth(self, element) -> int: ...
    def leading_exponent(self, element) -> int | None: ...
    def induced_pcgs(self, gens) -> list[int]: ...
    def constructive_membership_test(self, ipcgs, g) -> list[int] | Literal[False]: ...

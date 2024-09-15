from enum import Enum

class Reservoir:
    def __init__(self) -> None: ...
    def borrow_or_take(self, now, can_borrow): ...
    def load_quota(self, quota, TTL, interval) -> None: ...
    @property
    def quota(self): ...
    @property
    def TTL(self): ...

class ReservoirDecision(Enum):
    TAKE = "take"
    BORROW = "borrow"
    NO = "no"

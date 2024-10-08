from typing import ClassVar

from .core import UnitedStates

class Georgia(UnitedStates):
    include_confederation_day: ClassVar[bool]
    include_federal_presidents_day: ClassVar[bool]
    label_washington_birthday_december: ClassVar[str]
    thanksgiving_friday_label: ClassVar[str]
    def get_washington_birthday_december(self, year): ...
    def get_confederate_day(self, year): ...
    def get_robert_lee_birthday(self, year): ...
    def get_variable_days(self, year): ...

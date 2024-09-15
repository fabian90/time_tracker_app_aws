class HatchPatternBase: ...

class HorizontalHatch(HatchPatternBase):
    def __init__(self, hatch: str, density: int) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class VerticalHatch(HatchPatternBase):
    def __init__(self, hatch: str, density: int) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class NorthEastHatch(HatchPatternBase):
    def __init__(self, hatch: str, density: int) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class SouthEastHatch(HatchPatternBase):
    def __init__(self, hatch: str, density: int) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class Shapes(HatchPatternBase):
    filled = ...
    def __init__(self, hatch: str, density: int) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class Circles(Shapes):
    def __init__(self, hatch: str, density: int) -> None: ...

class SmallCircles(Circles):
    size = ...
    def __init__(self, hatch: str, density: int) -> None: ...

class LargeCircles(Circles):
    size = ...
    def __init__(self, hatch: str, density: int) -> None: ...

class SmallFilledCircles(Circles):
    size = ...
    filled = ...
    def __init__(self, hatch: str, density: int) -> None: ...

class Stars(Shapes):
    size = ...
    filled = ...
    def __init__(self, hatch: str, density: int) -> None: ...

def get_path(hatchpattern, density=...): ...

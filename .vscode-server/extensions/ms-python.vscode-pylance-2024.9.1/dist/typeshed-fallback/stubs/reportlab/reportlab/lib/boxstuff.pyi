from typing import Final

__version__: Final[str]

def rectCorner(x, y, width, height, anchor: str = "sw", dims: bool = False): ...
def aspectRatioFix(preserve, anchor, x, y, width, height, imWidth, imHeight, anchorAtXY: bool = False): ...

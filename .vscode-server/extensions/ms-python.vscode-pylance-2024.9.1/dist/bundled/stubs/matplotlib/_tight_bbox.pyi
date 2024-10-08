from typing import Callable

from .figure import Figure

def adjust_bbox(fig: Figure, bbox_inches, fixed_dpi: float | None = None) -> Callable[[], None]: ...
def process_figure_for_rasterizing(
    fig: Figure, bbox_inches_restore, fixed_dpi: float | None = None
) -> tuple[float, Callable[[], None]]: ...

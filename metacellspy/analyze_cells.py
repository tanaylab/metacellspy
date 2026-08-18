"""
Compute per-cell data. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_cells.html>`__ for details.
"""

from typing import Optional

from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_vector_of_total_UMIs_per_cell",
]


def compute_vector_of_total_UMIs_per_cell(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_total_UMIs_per_cell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_cells.html#Metacells.AnalyzeCells.compute_vector_of_total_UMIs_per_cell!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_total_UMIs_per_cell_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )

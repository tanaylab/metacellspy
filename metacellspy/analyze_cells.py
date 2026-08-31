"""
Compute per-cell data. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_cells.html>`__ for details.
"""

from typing import Optional

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_vector_of_is_base_outlier_per_cell",
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


def compute_vector_of_is_base_outlier_per_cell(  # pylint: disable=invalid-name
    *,
    cells_daf: DafWriter,
    metacells_daf: DafReader,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_is_base_outlier_per_cell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_cells.html#Metacells.AnalyzeCells.compute_vector_of_is_base_outlier_per_cell!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_is_base_outlier_per_cell_b(
        cells_daf=cells_daf,
        metacells_daf=metacells_daf,
        **_given(
            overwrite=overwrite,
        ),
    )

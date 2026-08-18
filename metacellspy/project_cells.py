"""
Project cells onto an atlas. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/project_cells.html>`__ for details.
"""

from typing import Optional

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_cells_projection",
    "compute_matrix_of_correlation_between_neighborhood_cells_and_projected_metacells_per_gene_per_projected_block",
    "compute_vector_of_correlation_between_cells_and_projected_metacells",
]


def compute_cells_projection(
    *,
    query_daf: DafWriter,
    atlas_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set [``vector_of_projected_block_per_cell``] and ``vector_of_projected_modules_z_score_per_cell``. See
    the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/project_cells.html#Metacells.ProjectCells.compute_cells_projection!>`__
    for details.
    """
    jl.Metacells.compute_cells_projection_b(
        query_daf=query_daf,
        atlas_daf=atlas_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_between_neighborhood_cells_and_projected_metacells_per_gene_per_projected_block(
    *,
    query_daf: DafWriter,
    atlas_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    min_neighborhood_query_cells: Optional[int] = None,
    overwrite: Optional[bool] = None,
    bin: Optional[int] = None,  # pylint: disable=redefined-builtin
) -> None:
    """
    Compute and set
    ``matrix_of_correlation_between_neighborhood_cells_and_projected_metacells_per_gene_per_projected_block``. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/project_cells.html#Metacells.ProjectCells.compute_matrix_of_correlation_between_neighborhood_cells_and_projected_metacells_per_gene_per_projected_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_between_neighborhood_cells_and_projected_metacells_per_gene_per_projected_block_b(
        query_daf=query_daf,
        atlas_daf=atlas_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            min_neighborhood_query_cells=min_neighborhood_query_cells,
            overwrite=overwrite,
            bin=bin,
        ),
    )


def compute_vector_of_correlation_between_cells_and_projected_metacells(
    *,
    query_daf: DafWriter,
    atlas_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set (in query) ``vector_of_correlation_between_cells_and_projected_metacells_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/project_cells.html#Metacells.ProjectCells.compute_vector_of_correlation_between_cells_and_projected_metacells!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_correlation_between_cells_and_projected_metacells_b(
        query_daf=query_daf,
        atlas_daf=atlas_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )

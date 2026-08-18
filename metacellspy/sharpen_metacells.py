"""
Sharpen the metacells by re-grouping the cells. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html>`__ for details.
"""

from typing import Optional
from typing import Sequence

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import _rng
from .julia_import import jl

__all__ = [
    "compute_matrix_of_n_cells_per_prev_block_per_block",
    "compute_matrix_of_n_cells_per_prev_block_type_per_block_type",
    "compute_matrix_of_n_cells_per_prev_metacell_type_per_metacell_type",
    "compute_vector_of_global_flow_order_per_type",
    "sharpen_metacells",
]


def compute_matrix_of_n_cells_per_prev_block_per_block(
    *,
    other_daf: DafWriter,
    prev_daf: DafReader,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_n_cells_per_prev_block_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.compute_matrix_of_n_cells_per_prev_block_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_n_cells_per_prev_block_per_block_b(
        other_daf=other_daf,
        prev_daf=prev_daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_n_cells_per_prev_block_type_per_block_type(
    *,
    other_daf: DafWriter,
    prev_daf: DafReader,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_n_cells_per_prev_block_type_per_block_type``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.compute_matrix_of_n_cells_per_prev_block_type_per_block_type!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_n_cells_per_prev_block_type_per_block_type_b(
        other_daf=other_daf,
        prev_daf=prev_daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_n_cells_per_prev_metacell_type_per_metacell_type(
    *,
    other_daf: DafWriter,
    prev_daf: DafReader,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_n_cells_per_prev_metacell_type_per_metacell_type``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.compute_matrix_of_n_cells_per_prev_metacell_type_per_metacell_type!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_n_cells_per_prev_metacell_type_per_metacell_type_b(
        other_daf=other_daf,
        prev_daf=prev_daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_global_flow_order_per_type(
    final_daf: DafReader,
    base_daf_per_round: Sequence[DafReader],
    *,
    output_daf: DafWriter,
    restarts: Optional[int] = None,
    rng: int = 0,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_global_flow_order_per_type``, a global order of the types minimizing the total weighted
    crossings of the type flow across the sharpening rounds. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.compute_vector_of_global_flow_order_per_type!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_global_flow_order_per_type_b(
        final_daf,
        jl.DafPy._to_daf_readers(list(base_daf_per_round)),
        output_daf=output_daf,
        **_given(
            restarts=restarts,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )


def sharpen_metacells(
    *,
    sharp_daf: DafWriter,
    base_daf: DafReader,
    prefix: Optional[str] = None,
    min_cells_in_metacell: Optional[int] = None,
    max_cells_in_metacell: Optional[int] = None,
    target_cell_total_UMIs_quantile: Optional[float] = None,
    min_metacell_total_UMIs: Optional[int] = None,
    min_migration_likelihood: Optional[float] = None,
    max_cells_dispersion_in_metacell: Optional[float] = None,
    min_cells_dispersion_in_metacell: Optional[float] = None,
    normalized_UMIs_quantile: Optional[float] = None,
    min_module_UMIs: Optional[int] = None,
    kmeans_rounds: Optional[int] = None,
    sharpening_round: int,
    improvement_half_life: Optional[int] = 2,
    gene_fraction_regularization: Optional[float] = None,
    std_UMIs_regularization: Optional[float] = None,
    min_outlier_fold: Optional[float] = None,
    outlier_UMIs_regularization: Optional[float] = None,
    rng: int = 0,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Given an ``base_daf`` metacells repository with a blocks structure and local gene modules that describe the cell
    state manifold, compute a ``sharp_daf`` metacells repository, which hopefully more faithfully captures this
    manifold. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.sharpen_metacells!>`__
    for details.
    """
    jl.Metacells.sharpen_metacells_b(
        sharp_daf=sharp_daf,
        base_daf=base_daf,
        sharpening_round=sharpening_round,
        improvement_half_life=improvement_half_life,
        **_given(
            prefix=prefix,
            min_cells_in_metacell=min_cells_in_metacell,
            max_cells_in_metacell=max_cells_in_metacell,
            target_cell_total_UMIs_quantile=target_cell_total_UMIs_quantile,
            min_metacell_total_UMIs=min_metacell_total_UMIs,
            min_migration_likelihood=min_migration_likelihood,
            max_cells_dispersion_in_metacell=max_cells_dispersion_in_metacell,
            min_cells_dispersion_in_metacell=min_cells_dispersion_in_metacell,
            normalized_UMIs_quantile=normalized_UMIs_quantile,
            min_module_UMIs=min_module_UMIs,
            kmeans_rounds=kmeans_rounds,
            gene_fraction_regularization=gene_fraction_regularization,
            std_UMIs_regularization=std_UMIs_regularization,
            min_outlier_fold=min_outlier_fold,
            outlier_UMIs_regularization=outlier_UMIs_regularization,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )

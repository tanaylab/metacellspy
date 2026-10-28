"""
Sharpen the metacells by re-grouping the cells. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html>`__ for details.
"""

from typing import Sequence

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import DEFAULT
from .julia_import import DefaultValue
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
    overwrite: bool | DefaultValue = DEFAULT,
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
    overwrite: bool | DefaultValue = DEFAULT,
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
    overwrite: bool | DefaultValue = DEFAULT,
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
    daf_per_round: Sequence[DafReader],
    *,
    output_daf: DafWriter,
    restarts: int | DefaultValue = DEFAULT,
    rng: int | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Compute and set ``vector_of_global_flow_order_per_type``, a global order of the types minimizing the total weighted
    crossings of the type flow across the sharpening rounds. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.compute_vector_of_global_flow_order_per_type!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_global_flow_order_per_type_b(
        final_daf,
        jl.DafPy._to_daf_readers(list(daf_per_round)),
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
    prev_daf: DafReader,
    prefix: str | DefaultValue = DEFAULT,
    min_cells_in_metacell: int | DefaultValue = DEFAULT,
    max_cells_in_metacell: int | DefaultValue = DEFAULT,
    target_cell_total_UMIs_quantile: float | DefaultValue = DEFAULT,
    min_metacell_total_UMIs: int | DefaultValue = DEFAULT,
    min_migration_likelihood: float | DefaultValue = DEFAULT,
    max_cells_dispersion_in_metacell: float | DefaultValue = DEFAULT,
    min_cells_dispersion_in_metacell: float | DefaultValue = DEFAULT,
    normalized_UMIs_quantile: float | DefaultValue = DEFAULT,
    min_module_UMIs: int | DefaultValue = DEFAULT,
    kmeans_rounds: int | DefaultValue = DEFAULT,
    sharpening_round: int,
    improvement_half_life: int | None | DefaultValue = DEFAULT,
    gene_fraction_regularization: float | DefaultValue = DEFAULT,
    std_UMIs_regularization: float | DefaultValue = DEFAULT,
    min_outlier_fold: float | DefaultValue = DEFAULT,
    min_foreign_outlier_fold: float | DefaultValue = DEFAULT,
    outlier_UMIs_regularization: float | DefaultValue = DEFAULT,
    outlier_min_significant_UMIs: int | DefaultValue = DEFAULT,
    max_modules_z_score: float | DefaultValue = DEFAULT,
    rng: int | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Given a ``prev_daf`` metacells repository with a blocks structure and local gene modules that describe the cell
    state manifold, compute a ``sharp_daf`` metacells repository, which hopefully more faithfully captures this
    manifold. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/sharpen_metacells.html#Metacells.SharpenMetacells.sharpen_metacells!>`__
    for details.
    """
    jl.Metacells.sharpen_metacells_b(
        sharp_daf=sharp_daf,
        prev_daf=prev_daf,
        sharpening_round=sharpening_round,
        **_given(
            improvement_half_life=improvement_half_life,
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
            min_foreign_outlier_fold=min_foreign_outlier_fold,
            outlier_UMIs_regularization=outlier_UMIs_regularization,
            outlier_min_significant_UMIs=outlier_min_significant_UMIs,
            max_modules_z_score=max_modules_z_score,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )

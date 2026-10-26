"""
Compute per-module data. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html>`__ for details.
"""

from typing import Optional

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_matrix_of_cells_dispersion_per_metacell_per_module",
    "compute_matrix_of_n_genes_per_module_per_block",
    "compute_projected_modules_z_score_cutoff",
    "compute_projected_modules_z_score_cutoff_per_metacell",
    "compute_stats_of_euclidean_modules_cells_distance_per_metacell",
    "compute_stats_of_linear_fraction_in_environment_cells_per_module_per_block",
    "compute_stats_of_linear_fraction_in_neighborhood_cells_per_module_per_block",
    "compute_tensor_of_mean_cells_z_score_per_block_per_module_per_metacell",
    "compute_vector_of_n_modules_per_block",
]


def compute_matrix_of_cells_dispersion_per_metacell_per_module(
    daf: DafWriter,
    *,
    normalized_UMIs_quantile: Optional[float] = None,
    min_module_UMIs: Optional[int] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_cells_dispersion_per_metacell_per_module``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_matrix_of_cells_dispersion_per_metacell_per_module!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_cells_dispersion_per_metacell_per_module_b(
        daf,
        **_given(
            normalized_UMIs_quantile=normalized_UMIs_quantile,
            min_module_UMIs=min_module_UMIs,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_n_genes_per_module_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_n_genes_per_module_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_matrix_of_n_genes_per_module_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_n_genes_per_module_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_projected_modules_z_score_cutoff(
    daf: DafReader,
    *,
    rejected_fraction: Optional[float] = None,
) -> float:
    """
    Compute a cutoff for the ``vector_of_projected_modules_z_score_per_cell`` of query cells projected onto this (atlas)
    ``daf``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_projected_modules_z_score_cutoff>`__
    for details.
    """
    result = jl.Metacells.compute_projected_modules_z_score_cutoff(
        daf,
        **_given(
            rejected_fraction=rejected_fraction,
        ),
    )
    return float(result)


def compute_projected_modules_z_score_cutoff_per_metacell(
    *,
    atlas_daf: DafWriter,
    calibration_daf: DafReader,
    rejected_fraction: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_projected_modules_z_score_cutoff_per_metacell``,
    ``vector_of_projected_modules_z_score_cutoff_level_per_metacell`` and
    ``vector_of_projected_modules_z_score_cutoff_n_cells_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_projected_modules_z_score_cutoff_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_projected_modules_z_score_cutoff_per_metacell_b(
        atlas_daf=atlas_daf,
        calibration_daf=calibration_daf,
        **_given(
            rejected_fraction=rejected_fraction,
            overwrite=overwrite,
        ),
    )


def compute_stats_of_euclidean_modules_cells_distance_per_metacell(
    daf: DafWriter,
    *,
    std_UMIs_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_mean_euclidean_modules_cells_distance_per_metacell``,
    ``vector_of_std_euclidean_modules_cells_distance_per_metacell`` and ``vector_of_metacell_modules_z_score_per_cell``.
    See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_stats_of_euclidean_modules_cells_distance_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_stats_of_euclidean_modules_cells_distance_per_metacell_b(
        daf,
        **_given(
            std_UMIs_regularization=std_UMIs_regularization,
            overwrite=overwrite,
        ),
    )


def compute_stats_of_linear_fraction_in_environment_cells_per_module_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_mean_linear_fraction_in_environment_cells_per_module_per_block`` and and set
    ``matrix_of_std_linear_fraction_in_environment_cells_per_module_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_stats_of_linear_fraction_in_environment_cells_per_module_per_block!>`__
    for details.
    """
    jl.Metacells.compute_stats_of_linear_fraction_in_environment_cells_per_module_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_stats_of_linear_fraction_in_neighborhood_cells_per_module_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_mean_linear_fraction_in_neighborhood_cells_per_module_per_block`` and and set
    ``matrix_of_std_linear_fraction_in_neighborhood_cells_per_module_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_stats_of_linear_fraction_in_neighborhood_cells_per_module_per_block!>`__
    for details.
    """
    jl.Metacells.compute_stats_of_linear_fraction_in_neighborhood_cells_per_module_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_tensor_of_mean_cells_z_score_per_block_per_module_per_metacell(
    daf: DafWriter,
    *,
    std_UMIs_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``tensor_of_mean_cells_z_score_per_block_per_module_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_tensor_of_mean_cells_z_score_per_block_per_module_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_tensor_of_mean_cells_z_score_per_block_per_module_per_metacell_b(
        daf,
        **_given(
            std_UMIs_regularization=std_UMIs_regularization,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_modules_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_modules_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_modules.html#Metacells.AnalyzeModules.compute_vector_of_n_modules_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_modules_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )

"""
Compute per-block data. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html>`__ for details.
"""

# Some computations here take the same keywords as ones in ``analyze_genes.py``, which makes the shared wrapping idiom
# look like duplicated code. The same disable is in that file, since the check needs both sides to report it.
# pylint: disable=duplicate-code

from typing import Optional

import numpy as np
from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import _to_julia_array
from .julia_import import jl

__all__ = [
    "compute_blocks_2d_umap_by_metacells",
    "compute_blocks_3d_umap_by_metacells",
    "compute_matrix_of_UMIs_per_gene_per_block",
    "compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_block_per_block",
    "compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_metacell_per_block",
    "compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_metacells_per_gene_per_base_block",
    "compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_punctuated_metacells_per_gene_per_base_block",
    "compute_matrix_of_correlation_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block",
    "compute_matrix_of_correlation_between_neighborhood_cells_and_punctuated_metacells_per_gene_per_block",
    "compute_matrix_of_correlation_with_most_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block",
    "compute_matrix_of_is_correlated_with_skeleton_in_environment_per_gene_per_block",
    "compute_matrix_of_is_correlated_with_skeleton_in_neighborhood_per_gene_per_block",
    "compute_matrix_of_is_environment_distinct_per_gene_per_block",
    "compute_matrix_of_is_environment_marker_per_gene_per_block",
    "compute_matrix_of_is_environment_specific_per_gene_per_metacell",
    "compute_matrix_of_is_in_environment_per_metacell_per_block",
    "compute_matrix_of_is_in_neighborhood_per_block_per_block",
    "compute_matrix_of_is_neighborhood_distinct_per_gene_per_block",
    "compute_matrix_of_is_neighborhood_marker_per_gene_per_block",
    "compute_matrix_of_is_strong_per_gene_per_block",
    "compute_matrix_of_linear_fraction_per_gene_per_block",
    "compute_matrix_of_log_linear_fraction_per_gene_per_block",
    "compute_matrix_of_mean_euclidean_skeleton_fold_distance_between_blocks",
    "compute_matrix_of_mean_euclidean_skeleton_fold_distance_per_metacell_per_block",
    "compute_matrix_of_most_correlated_gene_in_neighborhood_per_gene_per_block",
    "compute_vector_of_block_closest_by_pertinent_markers_per_cell",
    "compute_vector_of_n_cells_per_block",
    "compute_vector_of_n_environment_cells_per_block",
    "compute_vector_of_n_environment_metacells_per_block",
    "compute_vector_of_n_metacells_per_block",
    "compute_vector_of_n_neighborhood_blocks_per_block",
    "compute_vector_of_n_neighborhood_cells_per_block",
    "compute_vector_of_n_neighborhood_metacells_per_block",
    "compute_vector_of_total_UMIs_per_block",
    "compute_vector_of_total_environment_UMIs_per_block",
    "compute_vector_of_total_neighborhood_UMIs_per_block",
    "compute_vector_of_type_per_block_by_cells",
    "compute_vector_of_type_per_block_by_metacells",
    "compute_vector_of_type_per_cell_by_blocks",
    "compute_vector_of_type_per_metacell_by_blocks",
]


def compute_blocks_2d_umap_by_metacells(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_umap_x_per_block`` and ``vector_of_umap_y_per_block`` by taking the mean of the 2D UMAP
    coordinates of the metacells in each block. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_blocks_2d_umap_by_metacells!>`__
    for details.
    """
    jl.Metacells.compute_blocks_2d_umap_by_metacells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_blocks_3d_umap_by_metacells(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_umap_u_per_block``, ``vector_of_umap_v_per_block`` and ``vector_of_umap_w_per_block`` by
    taking the mean of the 3D UMAP coordinates of the metacells in each block. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_blocks_3d_umap_by_metacells!>`__
    for details.
    """
    jl.Metacells.compute_blocks_3d_umap_by_metacells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_UMIs_per_gene_per_block(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_UMIs_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_UMIs_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_UMIs_per_gene_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_block_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_confusion_by_closest_by_pertinent_markers_per_block_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_block_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_block_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_metacell_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_confusion_by_closest_by_pertinent_markers_per_metacell_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_metacell_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_confusion_by_closest_by_pertinent_markers_per_metacell_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_metacells_per_gene_per_base_block(
    *,
    other_daf: DafWriter,
    base_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    bin: Optional[int] = None,  # pylint: disable=redefined-builtin
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set
    ``matrix_of_correlation_between_base_neighborhood_cells_and_projected_metacells_per_gene_per_base_block``. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_metacells_per_gene_per_base_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_metacells_per_gene_per_base_block_b(
        other_daf=other_daf,
        base_daf=base_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            bin=bin,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_punctuated_metacells_per_gene_per_base_block(
    *,
    other_daf: DafWriter,
    base_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    bin: Optional[int] = None,  # pylint: disable=redefined-builtin
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set
    ``matrix_of_correlation_between_base_neighborhood_cells_and_projected_punctuated_metacells_per_gene_per_base_block``.
    See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_punctuated_metacells_per_gene_per_base_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_between_base_neighborhood_cells_and_projected_punctuated_metacells_per_gene_per_base_block_b(
        other_daf=other_daf,
        base_daf=base_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            bin=bin,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block(
    *,
    other_daf: DafWriter,
    base_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    bin: Optional[int] = None,  # pylint: disable=redefined-builtin
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set
    ``matrix_of_correlation_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block``. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_correlation_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block_b(
        other_daf=other_daf,
        base_daf=base_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            bin=bin,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_between_neighborhood_cells_and_punctuated_metacells_per_gene_per_block(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_correlation_between_neighborhood_cells_and_punctuated_metacells_per_gene_per_block``.
    See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_correlation_between_neighborhood_cells_and_punctuated_metacells_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_between_neighborhood_cells_and_punctuated_metacells_per_gene_per_block_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_with_most_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block(
    *,
    other_daf: DafWriter,
    base_daf: DafReader,
    gene_fraction_regularization: Optional[float] = None,
    is_relevant_gene_per_base_block: Optional[np.ndarray] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set
    ``matrix_of_correlation_with_most_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block``.
    See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_correlation_with_most_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_with_most_between_base_neighborhood_cells_and_punctuated_metacells_per_gene_per_base_block_b(
        other_daf=other_daf,
        base_daf=base_daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            is_relevant_gene_per_base_block=_to_julia_array(is_relevant_gene_per_base_block),
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_correlated_with_skeleton_in_environment_per_gene_per_block(
    daf: DafWriter,
    *,
    min_gene_correlation: Optional[float] = None,
    min_gene_correlation_quantile: Optional[float] = None,
    genes_correlation_window: Optional[int] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_correlated_with_skeleton_in_environment_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_correlated_with_skeleton_in_environment_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_correlated_with_skeleton_in_environment_per_gene_per_block_b(
        daf,
        **_given(
            min_gene_correlation=min_gene_correlation,
            min_gene_correlation_quantile=min_gene_correlation_quantile,
            genes_correlation_window=genes_correlation_window,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_correlated_with_skeleton_in_neighborhood_per_gene_per_block(
    daf: DafWriter,
    *,
    min_gene_correlation: Optional[float] = None,
    min_gene_correlation_quantile: Optional[float] = None,
    genes_correlation_window: Optional[int] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_correlated_with_skeleton_in_neighborhood_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_correlated_with_skeleton_in_neighborhood_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_correlated_with_skeleton_in_neighborhood_per_gene_per_block_b(
        daf,
        **_given(
            min_gene_correlation=min_gene_correlation,
            min_gene_correlation_quantile=min_gene_correlation_quantile,
            genes_correlation_window=genes_correlation_window,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_environment_distinct_per_gene_per_block(
    daf: DafWriter,
    *,
    min_distinct_gene_max_fraction: Optional[float] = None,
    min_distinct_gene_mean_fold: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_environment_distinct_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_environment_distinct_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_environment_distinct_per_gene_per_block_b(
        daf,
        **_given(
            min_distinct_gene_max_fraction=min_distinct_gene_max_fraction,
            min_distinct_gene_mean_fold=min_distinct_gene_mean_fold,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_environment_marker_per_gene_per_block(
    daf: DafWriter,
    *,
    min_marker_gene_max_fraction: Optional[float] = None,
    min_marker_gene_range_fold: Optional[float] = None,
    min_marker_quantile: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_environment_marker_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_environment_marker_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_environment_marker_per_gene_per_block_b(
        daf,
        **_given(
            min_marker_gene_max_fraction=min_marker_gene_max_fraction,
            min_marker_gene_range_fold=min_marker_gene_range_fold,
            min_marker_quantile=min_marker_quantile,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_environment_specific_per_gene_per_metacell(
    daf: DafWriter,
    *,
    min_rare_gene_fold_factor: Optional[float] = None,
    min_significant_gene_UMIs: Optional[int] = None,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_environment_specific_per_gene_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_environment_specific_per_gene_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_environment_specific_per_gene_per_metacell_b(
        daf,
        **_given(
            min_rare_gene_fold_factor=min_rare_gene_fold_factor,
            min_significant_gene_UMIs=min_significant_gene_UMIs,
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_in_environment_per_metacell_per_block(
    daf: DafWriter,
    *,
    max_environment_metacell_relative_distance: Optional[float] = None,
    environment_distance_base_quantile: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_in_environment_per_metacell_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_in_environment_per_metacell_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_in_environment_per_metacell_per_block_b(
        daf,
        **_given(
            max_environment_metacell_relative_distance=max_environment_metacell_relative_distance,
            environment_distance_base_quantile=environment_distance_base_quantile,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_in_neighborhood_per_block_per_block(
    daf: DafWriter,
    *,
    min_neighbour_confusion_fractions: Optional[float] = None,
    min_blocks_in_neighborhood: Optional[int] = None,
    min_metacells_in_neighborhood: Optional[int] = None,
    min_total_UMIs_in_neighborhood: Optional[int] = None,
    max_blocks_in_neighborhood: Optional[int] = None,
    max_metacells_in_neighborhood: Optional[int] = None,
    max_total_UMIs_in_neighborhood: Optional[int] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_in_neighborhood_per_block_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_in_neighborhood_per_block_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_in_neighborhood_per_block_per_block_b(
        daf,
        **_given(
            min_neighbour_confusion_fractions=min_neighbour_confusion_fractions,
            min_blocks_in_neighborhood=min_blocks_in_neighborhood,
            min_metacells_in_neighborhood=min_metacells_in_neighborhood,
            min_total_UMIs_in_neighborhood=min_total_UMIs_in_neighborhood,
            max_blocks_in_neighborhood=max_blocks_in_neighborhood,
            max_metacells_in_neighborhood=max_metacells_in_neighborhood,
            max_total_UMIs_in_neighborhood=max_total_UMIs_in_neighborhood,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_neighborhood_distinct_per_gene_per_block(
    daf: DafWriter,
    *,
    min_distinct_gene_max_fraction: Optional[float] = None,
    min_distinct_gene_mean_fold: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_neighborhood_distinct_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_neighborhood_distinct_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_neighborhood_distinct_per_gene_per_block_b(
        daf,
        **_given(
            min_distinct_gene_max_fraction=min_distinct_gene_max_fraction,
            min_distinct_gene_mean_fold=min_distinct_gene_mean_fold,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_neighborhood_marker_per_gene_per_block(
    daf: DafWriter,
    *,
    min_marker_gene_max_fraction: Optional[float] = None,
    min_marker_gene_range_fold: Optional[float] = None,
    min_marker_quantile: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_neighborhood_marker_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_neighborhood_marker_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_neighborhood_marker_per_gene_per_block_b(
        daf,
        **_given(
            min_marker_gene_max_fraction=min_marker_gene_max_fraction,
            min_marker_gene_range_fold=min_marker_gene_range_fold,
            min_marker_quantile=min_marker_quantile,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_is_strong_per_gene_per_block(
    daf: DafWriter,
    *,
    min_strong_linear_fraction: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_is_strong_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_is_strong_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_is_strong_per_gene_per_block_b(
        daf,
        **_given(
            min_strong_linear_fraction=min_strong_linear_fraction,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_linear_fraction_per_gene_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_linear_fraction_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_linear_fraction_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_linear_fraction_per_gene_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_log_linear_fraction_per_gene_per_block(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_log_linear_fraction_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_log_linear_fraction_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_log_linear_fraction_per_gene_per_block_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_mean_euclidean_skeleton_fold_distance_between_blocks(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_mean_euclidean_skeleton_fold_distance_between_blocks``, the mean Euclidean skeleton
    genes fractions distance between the metacells of the blocks, by reducing
    ``matrix_of_mean_euclidean_skeleton_fold_distance_per_metacell_per_block`` over the metacells of each block. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_mean_euclidean_skeleton_fold_distance_between_blocks!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_mean_euclidean_skeleton_fold_distance_between_blocks_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_mean_euclidean_skeleton_fold_distance_per_metacell_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_mean_euclidean_skeleton_fold_distance_per_metacell_per_block``, the mean Euclidean
    skeleton genes fractions distance between each metacell and the metacells of each block. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_mean_euclidean_skeleton_fold_distance_per_metacell_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_mean_euclidean_skeleton_fold_distance_per_metacell_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_most_correlated_gene_in_neighborhood_per_gene_per_block(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_most_correlated_gene_in_neighborhood_per_gene_per_block`` and
    ``matrix_of_most_correlated_quantile_per_gene_in_neighborhood_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_matrix_of_most_correlated_gene_in_neighborhood_per_gene_per_block!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_most_correlated_gene_in_neighborhood_per_gene_per_block_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_block_closest_by_pertinent_markers_per_cell(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_block_closest_by_pertinent_markers_per_cell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_block_closest_by_pertinent_markers_per_cell!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_block_closest_by_pertinent_markers_per_cell_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_cells_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_cells_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_cells_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_cells_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_environment_cells_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_environment_cells_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_environment_cells_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_environment_cells_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_environment_metacells_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_environment_metacells_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_environment_metacells_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_environment_metacells_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_metacells_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_metacells_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_metacells_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_metacells_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_neighborhood_blocks_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_neighborhood_blocks_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_neighborhood_blocks_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_neighborhood_blocks_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_neighborhood_cells_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    The total number of cells in the metacells of the blocks of the neighborhood centered at a block. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_neighborhood_cells_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_neighborhood_cells_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_neighborhood_metacells_per_block(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_neighborhood_metacells_per_block``
    DataAxesFormats.Computations.ContractDocumentation(1) See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_n_neighborhood_metacells_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_neighborhood_metacells_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_total_UMIs_per_block(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    The total UMIs of non-excluded genes per block. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_total_UMIs_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_total_UMIs_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_total_environment_UMIs_per_block(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_total_environment_UMIs_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_total_environment_UMIs_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_total_environment_UMIs_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_total_neighborhood_UMIs_per_block(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_total_neighborhood_UMIs_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_total_neighborhood_UMIs_per_block!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_total_neighborhood_UMIs_per_block_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_type_per_block_by_cells(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_type_per_block`` by using the type of the metacells grouped into each block. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_type_per_block_by_cells!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_type_per_block_by_cells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_type_per_block_by_metacells(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_type_per_block`` by using the type of the metacells grouped into each block. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_type_per_block_by_metacells!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_type_per_block_by_metacells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_type_per_cell_by_blocks(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_type_per_cell`` by using the type of the blocks the metacells of the cells belong to.
    See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_type_per_cell_by_blocks!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_type_per_cell_by_blocks_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_type_per_metacell_by_blocks(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_type_per_metacell`` by using the type of the blocks the metacells belong to. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_blocks.html#Metacells.AnalyzeBlocks.compute_vector_of_type_per_metacell_by_blocks!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_type_per_metacell_by_blocks_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )

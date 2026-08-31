"""
Compute per-metacell data. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html>`__ for details.
"""

from typing import Optional

import numpy as np
from dafpy import DafReader
from dafpy import DafWriter
from dafpy import Query

from .julia_import import _given
from .julia_import import _rng
from .julia_import import _to_julia_array
from .julia_import import jl

__all__ = [
    "compute_matrix_of_UMIs_per_gene_per_metacell",
    "compute_matrix_of_correlation_between_markers_per_gene_per_gene",
    "compute_matrix_of_correlation_per_gene_per_gene_of_subset_of_metacells",
    "compute_matrix_of_euclidean_skeleton_fold_distance_between_metacells",
    "compute_matrix_of_linear_fraction_per_gene_per_metacell",
    "compute_matrix_of_log_linear_fraction_per_gene_per_metacell",
    "compute_matrix_of_max_skeleton_fold_distance_between_metacells",
    "compute_metacells_2d_umap",
    "compute_metacells_3d_umap",
    "compute_vector_of_correlation_between_cells_and_projected_punctuated_metacells_per_gene",
    "compute_vector_of_correlation_between_cells_and_punctuated_metacells_per_gene",
    "compute_vector_of_n_cells_per_metacell",
    "compute_vector_of_total_UMIs_per_metacell",
    "compute_vector_of_type_per_cell_by_metacells",
    "compute_vector_of_type_per_metacell_by_cells",
]


def compute_matrix_of_UMIs_per_gene_per_metacell(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_UMIs_per_gene_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_UMIs_per_gene_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_UMIs_per_gene_per_metacell_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_between_markers_per_gene_per_gene(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_correlation_between_markers_per_gene_per_gene`` - the correlation between the log
    expression of pairs of marker genes across all the metacells. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_correlation_between_markers_per_gene_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_between_markers_per_gene_per_gene_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_correlation_per_gene_per_gene_of_subset_of_metacells(
    daf: DafWriter,
    *,
    metacells_subset: Optional[str | Query | np.ndarray] = None,
    matrix_name: str,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Correlate the marker genes by their log expression across a subset of the metacells (all of them when
    ``metacells_subset`` is ``nothing``). See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_correlation_per_gene_per_gene_of_subset_of_metacells!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_correlation_per_gene_per_gene_of_subset_of_metacells_b(
        daf,
        matrix_name=matrix_name,
        **_given(
            metacells_subset=_to_julia_array(metacells_subset),
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_euclidean_skeleton_fold_distance_between_metacells(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_euclidean_skeleton_fold_distance_between_metacells``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_euclidean_skeleton_fold_distance_between_metacells!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_euclidean_skeleton_fold_distance_between_metacells_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_linear_fraction_per_gene_per_metacell(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_linear_fraction_per_gene_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_linear_fraction_per_gene_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_linear_fraction_per_gene_per_metacell_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_log_linear_fraction_per_gene_per_metacell(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_log_linear_fraction_per_gene_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_log_linear_fraction_per_gene_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_log_linear_fraction_per_gene_per_metacell_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_matrix_of_max_skeleton_fold_distance_between_metacells(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    min_significant_gene_UMIs: Optional[int] = None,
    fold_confidence: Optional[float] = None,
    min_confidence_UMIs: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``matrix_of_max_skeleton_fold_distance_between_metacells``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_matrix_of_max_skeleton_fold_distance_between_metacells!>`__
    for details.
    """
    jl.Metacells.compute_matrix_of_max_skeleton_fold_distance_between_metacells_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            min_significant_gene_UMIs=min_significant_gene_UMIs,
            fold_confidence=fold_confidence,
            min_confidence_UMIs=min_confidence_UMIs,
            overwrite=overwrite,
        ),
    )


def compute_metacells_2d_umap(
    daf: DafWriter,
    *,
    prev_daf: Optional[DafReader] = None,
    min_dist: Optional[float] = None,
    n_neighbors: Optional[int] = None,
    rng: int = 0,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_umap_x_per_metacell`` and ``vector_of_umap_y_per_metacell`` by computing a 2D UMAP
    projection from the Euclidean skeleton fold distance between metacells. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_metacells_2d_umap!>`__
    for details.
    """
    jl.Metacells.compute_metacells_2d_umap_b(
        daf,
        **_given(
            prev_daf=prev_daf,
            min_dist=min_dist,
            n_neighbors=n_neighbors,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )


def compute_metacells_3d_umap(
    daf: DafWriter,
    *,
    min_dist: Optional[float] = None,
    n_neighbors: Optional[int] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_umap_u_per_metacell``, ``vector_of_umap_v_per_metacell`` and
    ``vector_of_umap_w_per_metacell`` by computing a 3D UMAP projection from the Euclidean skeleton fold distance
    between metacells. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_metacells_3d_umap!>`__
    for details.
    """
    jl.Metacells.compute_metacells_3d_umap_b(
        daf,
        **_given(
            min_dist=min_dist,
            n_neighbors=n_neighbors,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_correlation_between_cells_and_punctuated_metacells_per_gene(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_correlation_between_cells_and_punctuated_metacells_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_vector_of_correlation_between_cells_and_punctuated_metacells_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_correlation_between_cells_and_punctuated_metacells_per_gene_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_correlation_between_cells_and_projected_punctuated_metacells_per_gene(
    daf: DafWriter,
    *,
    gene_fraction_regularization: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_correlation_between_cells_and_projected_punctuated_metacells_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_vector_of_correlation_between_cells_and_projected_punctuated_metacells_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_correlation_between_cells_and_projected_punctuated_metacells_per_gene_b(
        daf,
        **_given(
            gene_fraction_regularization=gene_fraction_regularization,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_n_cells_per_metacell(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_n_cells_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_vector_of_n_cells_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_n_cells_per_metacell_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_total_UMIs_per_metacell(  # pylint: disable=invalid-name
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_total_UMIs_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_vector_of_total_UMIs_per_metacell!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_total_UMIs_per_metacell_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_type_per_cell_by_metacells(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_type_per_cell`` by using the type of the metacell each cell belongs to. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_vector_of_type_per_cell_by_metacells!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_type_per_cell_by_metacells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_type_per_metacell_by_cells(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_type_per_metacell`` by using the type of the cells grouped into each metacell. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_metacells.html#Metacells.AnalyzeMetacells.compute_vector_of_type_per_metacell_by_cells!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_type_per_metacell_by_cells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )

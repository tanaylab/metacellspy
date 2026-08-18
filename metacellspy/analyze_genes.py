"""
Compute per-gene data. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html>`__ for details.
"""

# Some computations here take the same keywords as ones in ``analyze_blocks.py``, which makes the shared wrapping idiom
# look like duplicated code. The same disable is in that file, since the check needs both sides to report it.
# pylint: disable=duplicate-code

from typing import Optional

import numpy as np
import pandas as pd
from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _from_julia_frame
from .julia_import import _given
from .julia_import import _to_julia_array
from .julia_import import jl

__all__ = [
    "compute_gene_report",
    "compute_skeleton_report",
    "compute_vector_of_is_correlated_with_skeleton_per_gene",
    "compute_vector_of_is_marker_per_gene",
    "compute_vector_of_is_skeleton_per_gene",
    "compute_vector_of_marker_rank_per_gene",
    "fetch_gmara_vector_of_is_regulator_per_gene",
    "fetch_gmara_vector_of_is_transcription_factor_per_gene",
    "rank_variables",
]


def compute_gene_report(
    *,
    daf: DafReader,
    base_daf: Optional[DafReader] = None,
) -> pd.DataFrame:
    """
    Return a per-marker-gene report as a ``DataFrame``, one row per marker gene, sorted by ``rank``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.compute_gene_report>`__
    for details.
    """
    result = jl.Metacells.compute_gene_report(
        daf=daf,
        **_given(
            base_daf=base_daf,
        ),
    )
    return _from_julia_frame(result)


def compute_skeleton_report(
    *,
    daf: DafReader,
    base_daf: Optional[DafReader] = None,
) -> pd.DataFrame:
    """
    Return a per-skeleton-gene report as a ``DataFrame``, one row per skeleton gene, sorted by the total number of
    markers most correlated with it (descending). See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.compute_skeleton_report>`__
    for details.
    """
    result = jl.Metacells.compute_skeleton_report(
        daf=daf,
        **_given(
            base_daf=base_daf,
        ),
    )
    return _from_julia_frame(result)


def compute_vector_of_is_correlated_with_skeleton_per_gene(
    daf: DafWriter,
    *,
    min_gene_correlation: Optional[float] = None,
    min_gene_correlation_quantile: Optional[float] = None,
    genes_correlation_window: Optional[int] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_is_correlated_with_skeleton_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.compute_vector_of_is_correlated_with_skeleton_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_is_correlated_with_skeleton_per_gene_b(
        daf,
        **_given(
            min_gene_correlation=min_gene_correlation,
            min_gene_correlation_quantile=min_gene_correlation_quantile,
            genes_correlation_window=genes_correlation_window,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_is_marker_per_gene(
    daf: DafWriter,
    *,
    min_marker_gene_max_fraction: Optional[float] = None,
    min_marker_gene_range_fold: Optional[float] = None,
    min_marker_quantile: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_is_marker_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.compute_vector_of_is_marker_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_is_marker_per_gene_b(
        daf,
        **_given(
            min_marker_gene_max_fraction=min_marker_gene_max_fraction,
            min_marker_gene_range_fold=min_marker_gene_range_fold,
            min_marker_quantile=min_marker_quantile,
            overwrite=overwrite,
        ),
    )


def compute_vector_of_is_skeleton_per_gene(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_is_skeleton_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.compute_vector_of_is_skeleton_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_is_skeleton_per_gene_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def compute_vector_of_marker_rank_per_gene(
    daf: DafWriter,
    *,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_marker_rank_per_gene``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.compute_vector_of_marker_rank_per_gene!>`__
    for details.
    """
    jl.Metacells.compute_vector_of_marker_rank_per_gene_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def fetch_gmara_vector_of_is_regulator_per_gene(
    daf: DafWriter,
    *,
    species: str,
    namespace: Optional[str] = None,
    version: Optional[str] = None,
    cache_dir: Optional[str] = None,
    timeout: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Fetch and set ``vector_of_is_transcription_factor_per_gene`` from ``Gmara``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.fetch_gmara_vector_of_is_regulator_per_gene!>`__
    for details.
    """
    jl.Metacells.fetch_gmara_vector_of_is_regulator_per_gene_b(
        daf,
        species=species,
        **_given(
            namespace=namespace,
            version=version,
            cache_dir=cache_dir,
            timeout=timeout,
            overwrite=overwrite,
        ),
    )


def fetch_gmara_vector_of_is_transcription_factor_per_gene(
    daf: DafWriter,
    *,
    species: str,
    namespace: Optional[str] = None,
    version: Optional[str] = None,
    cache_dir: Optional[str] = None,
    timeout: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Fetch and set ``vector_of_is_transcription_factor_per_gene`` from ``Gmara``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.fetch_gmara_vector_of_is_transcription_factor_per_gene!>`__
    for details.
    """
    jl.Metacells.fetch_gmara_vector_of_is_transcription_factor_per_gene_b(
        daf,
        species=species,
        **_given(
            namespace=namespace,
            version=version,
            cache_dir=cache_dir,
            timeout=timeout,
            overwrite=overwrite,
        ),
    )


def rank_variables(
    score_per_variable_per_observation: np.ndarray,
) -> np.ndarray:
    """
    Given some ``score_per_variable_per_observation`` matrix, return a vector of the rank of each variable such that the
    "most significant" variables are first. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/analyze_genes.html#Metacells.AnalyzeGenes.rank_variables>`__
    for details.
    """
    result = jl.Metacells.rank_variables(
        _to_julia_array(score_per_variable_per_observation),
    )
    return np.asarray(result)

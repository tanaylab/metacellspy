"""
Reduce a large set of metacells to a smaller, non-redundant focus set. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/focus.html>`__ for details.
"""

from typing import Optional

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_focus_metacells",
]


def compute_focus_metacells(
    *,
    full_daf: DafReader,
    focus_daf: DafWriter,
    max_redundant_fold: Optional[float] = None,
    n_neighbors: Optional[int] = None,
    gene_fraction_regularization: Optional[float] = None,
    max_fold_gene_fraction_regularization: Optional[float] = None,
    max_fold_min_significant_gene_UMIs: Optional[int] = None,
    max_fold_confidence: Optional[float] = None,
    max_fold_min_confidence_UMIs: Optional[float] = None,
    min_marker_gene_max_fraction: Optional[float] = None,
    min_marker_gene_range_fold: Optional[float] = None,
    min_marker_quantile: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Choose the focus metacells of the ``full_daf``, and create the focus axes and skeleton genes mask of the
    ``focus_daf``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/focus.html#Metacells.Focus.compute_focus_metacells!>`__
    for details.
    """
    jl.Metacells.compute_focus_metacells_b(
        full_daf=full_daf,
        focus_daf=focus_daf,
        **_given(
            max_redundant_fold=max_redundant_fold,
            n_neighbors=n_neighbors,
            gene_fraction_regularization=gene_fraction_regularization,
            max_fold_gene_fraction_regularization=max_fold_gene_fraction_regularization,
            max_fold_min_significant_gene_UMIs=max_fold_min_significant_gene_UMIs,
            max_fold_confidence=max_fold_confidence,
            max_fold_min_confidence_UMIs=max_fold_min_confidence_UMIs,
            min_marker_gene_max_fraction=min_marker_gene_max_fraction,
            min_marker_gene_range_fold=min_marker_gene_range_fold,
            min_marker_quantile=min_marker_quantile,
            overwrite=overwrite,
        ),
    )

"""
Reduce a large set of metacells to a smaller, non-redundant focus set. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/focus.html>`__ for details.
"""

from typing import Any

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import DEFAULT
from .julia_import import DefaultValue
from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_focus_metacells",
    "copy_focus_metacells_data",
]


def compute_focus_metacells(
    *,
    full_daf: DafReader,
    focus_daf: DafWriter,
    max_redundant_fold: float | DefaultValue = DEFAULT,
    n_neighbors: int | DefaultValue = DEFAULT,
    gene_fraction_regularization: float | DefaultValue = DEFAULT,
    max_fold_gene_fraction_regularization: float | DefaultValue = DEFAULT,
    max_fold_min_significant_gene_UMIs: int | DefaultValue = DEFAULT,
    max_fold_confidence: float | DefaultValue = DEFAULT,
    max_fold_min_confidence_UMIs: float | DefaultValue = DEFAULT,
    min_marker_gene_max_fraction: float | DefaultValue = DEFAULT,
    min_marker_gene_range_fold: float | DefaultValue = DEFAULT,
    min_marker_quantile: float | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
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


def copy_focus_metacells_data(
    *,
    full_daf: DafReader,
    focus_daf: DafWriter,
    excluded_contract: Any,
) -> None:
    """
    Copy the data of the ``full_daf`` into the ``focus_daf``, restricted to the focus metacells and cells, except for
    the outputs of the ``excluded_contract`` (a Julia ``Contract``, e.g. of ``prepare_metacells``). See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/focus.html#Metacells.Focus.copy_focus_metacells_data!>`__
    for details.
    """
    jl.Metacells.copy_focus_metacells_data_b(
        full_daf=full_daf,
        focus_daf=focus_daf,
        excluded_contract=excluded_contract,
    )

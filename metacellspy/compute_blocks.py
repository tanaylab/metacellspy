"""
Group metacells into blocks. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/compute_blocks.html>`__ for details.
"""

from dafpy import DafWriter

from .julia_import import DEFAULT
from .julia_import import DefaultValue
from .julia_import import _given
from .julia_import import _rng
from .julia_import import jl

__all__ = [
    "compute_metacells_blocks",
]


def compute_metacells_blocks(
    daf: DafWriter,
    *,
    n_blocks: int | None | DefaultValue = DEFAULT,
    max_block_span: float | DefaultValue = DEFAULT,
    max_fold_gene_fraction_regularization: float | DefaultValue = DEFAULT,
    max_fold_min_significant_gene_UMIs: int | DefaultValue = DEFAULT,
    max_fold_confidence: float | DefaultValue = DEFAULT,
    max_fold_min_confidence_UMIs: float | DefaultValue = DEFAULT,
    prefix: str | DefaultValue = DEFAULT,
    rng: int | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Compute and set the ``block_axis`` and ``vector_of_block_per_metacell``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/compute_blocks.html#Metacells.ComputeBlocks.compute_metacells_blocks!>`__
    for details.
    """
    jl.Metacells.compute_metacells_blocks_b(
        daf,
        **_given(
            n_blocks=n_blocks,
            max_block_span=max_block_span,
            max_fold_gene_fraction_regularization=max_fold_gene_fraction_regularization,
            max_fold_min_significant_gene_UMIs=max_fold_min_significant_gene_UMIs,
            max_fold_confidence=max_fold_confidence,
            max_fold_min_confidence_UMIs=max_fold_min_confidence_UMIs,
            prefix=prefix,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )

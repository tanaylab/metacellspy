"""
Group metacells into blocks. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/compute_blocks.html>`__ for details.
"""

from typing import Optional

from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "compute_metacells_blocks",
]


def compute_metacells_blocks(
    daf: DafWriter,
    *,
    n_blocks: Optional[int] = None,
    max_block_span: Optional[float] = None,
    prefix: Optional[str] = None,
    overwrite: Optional[bool] = None,
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
            prefix=prefix,
            overwrite=overwrite,
        ),
    )

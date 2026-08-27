"""
Run whole stages of the metacells pipeline. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html>`__ for details.
"""

from typing import Optional

from dafpy import DafReader
from dafpy import DafWriter

from .julia_import import _given
from .julia_import import _rng
from .julia_import import jl

__all__ = [
    "prepare_markers",
    "prepare_metacells",
    "prepare_skeletons",
]


def prepare_metacells(daf: DafWriter, *, overwrite: Optional[bool] = None) -> None:
    """
    Aggregate the cells of each metacell into the metacell. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.prepare_metacells!>`__
    for details.
    """
    jl.Metacells.prepare_metacells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def prepare_markers(daf: DafWriter, *, overwrite: Optional[bool] = None) -> None:
    """
    Find the marker genes, rank them, and correlate each of them with every other. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.prepare_markers!>`__
    for details.
    """
    jl.Metacells.prepare_markers_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def prepare_skeletons(
    daf: DafWriter,
    *,
    prev_daf: Optional[DafReader] = None,
    rng: int = 0,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Choose the skeleton genes and compute the distances and the layout which follow from them. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.prepare_skeletons!>`__
    for details.
    """
    jl.Metacells.prepare_skeletons_b(
        daf,
        **_given(
            prev_daf=prev_daf,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )

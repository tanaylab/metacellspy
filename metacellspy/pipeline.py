"""
Run whole stages of the metacells pipeline. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html>`__ for details.
"""

from typing import Collection
from typing import Optional
from typing import Union

import numpy as np
from dafpy import DafReader
from dafpy import DafWriter
from dafpy import StorageScalar

from .julia_import import _given
from .julia_import import _rng
from .julia_import import _to_julia_array
from .julia_import import _to_julia_scalar_or_collection
from .julia_import import jl

__all__ = [
    "analyze_metacells",
    "import_base_metacells",
    "prepare_markers",
    "prepare_metacells",
]


def import_base_metacells(
    *,
    cells_daf: DafWriter,
    metacells_daf: DafWriter,
    metacell_per_cell: np.ndarray,
    empty_metacells: Optional[Union[StorageScalar, Collection[StorageScalar]]] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Bring in the base metacells the sharpening pipeline starts with. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.import_base_metacells!>`__
    for details.
    """
    jl.Metacells.import_base_metacells_b(
        cells_daf=cells_daf,
        metacells_daf=metacells_daf,
        metacell_per_cell=_to_julia_array(metacell_per_cell),
        **_given(
            empty_metacells=_to_julia_scalar_or_collection(empty_metacells),
            overwrite=overwrite,
        ),
    )


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


def analyze_metacells(
    daf: DafWriter,
    *,
    prefix: Optional[str] = None,
    prev_daf: Optional[DafReader] = None,
    module_status: Optional[bool] = None,
    rng: int = 0,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Work out what a set of metacells says about the manifold - the skeleton genes, the geometry, the blocks and their
    gene modules - which is everything sharpening them needs. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.analyze_metacells!>`__
    for details.
    """
    jl.Metacells.analyze_metacells_b(
        daf,
        **_given(
            prefix=prefix,
            prev_daf=prev_daf,
            module_status=module_status,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )

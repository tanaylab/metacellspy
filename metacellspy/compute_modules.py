"""
Group genes into modules of each block. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/compute_modules.html>`__ for details.
"""

from typing import Optional

from dafpy import DafWriter

from .julia_import import _given
from .julia_import import _rng
from .julia_import import jl

__all__ = [
    "compute_blocks_modules",
]


def compute_blocks_modules(
    daf: DafWriter,
    *,
    max_clusters: Optional[int] = None,
    min_member_correlation: Optional[float] = None,
    min_orphan_correlation: Optional[float] = None,
    min_strong_UMIs: Optional[int] = None,
    min_strong_cells: Optional[int] = None,
    kmeans_rounds: Optional[int] = None,
    module_status: Optional[bool] = None,
    rng: int = 0,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Compute and set ``vector_of_anchor_per_module``, ``matrix_of_is_found_per_module_per_block``,
    ``matrix_of_module_per_gene_per_block``, and (if ``module_status`` is specified),
    ``matrix_of_module_status_per_gene_per_block``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/compute_modules.html#Metacells.ComputeModules.compute_blocks_modules!>`__
    for details.
    """
    jl.Metacells.compute_blocks_modules_b(
        daf,
        **_given(
            max_clusters=max_clusters,
            min_member_correlation=min_member_correlation,
            min_orphan_correlation=min_orphan_correlation,
            min_strong_UMIs=min_strong_UMIs,
            min_strong_cells=min_strong_cells,
            kmeans_rounds=kmeans_rounds,
            module_status=module_status,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )

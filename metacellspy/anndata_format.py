"""
Import ``AnnData`` based data sets. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html>`__ for details.
"""

from typing import AbstractSet
from typing import Any
from typing import Mapping
from typing import Optional
from typing import Tuple

from dafpy import DafWriter
from dafpy import StorageScalar

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "CopyAnnData",
    "import_cells_h5ad",
    "import_metacells_h5ad",
    "reconstruct_type_axis",
]

#: Which of the ``AnnData`` properties to copy, and under which name. Mapping a name to ``None``
#: skips it; mapping it to a name and a value renames it, using the value for entries the
#: ``AnnData`` does not have.
CopyAnnData = Mapping[str, Optional[Tuple[str, Optional[StorageScalar]]]]


def _copy_anndata(copy_data: Optional[CopyAnnData]) -> Any:
    # A Python tuple in a dictionary value does not convert to the Julia tuple the computation
    # expects, so the pairs are handed to Julia as parallel vectors for it to assemble.
    if copy_data is None:
        return None
    names = list(copy_data.keys())
    renames = [None if entry is None else entry[0] for entry in copy_data.values()]
    defaults = [None if entry is None else entry[1] for entry in copy_data.values()]
    return jl.MetacellsPy._copy_anndata(names, renames, defaults)


def import_cells_h5ad(
    daf: DafWriter,
    *,
    cells_h5ad: str,
    copy_data: Optional[CopyAnnData] = None,
    bestify: Optional[bool] = None,
    min_sparse_saving_fraction: Optional[float] = None,
    overwrite: Optional[bool] = None,
    insist: Optional[bool] = None,
) -> None:
    """
    Import an ``AnnData`` based cells dataset into a destination ``daf`` data set. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html#Metacells.AnnDataFormat.import_cells_h5ad!>`__
    for details.
    """
    jl.Metacells.import_cells_h5ad_b(
        daf,
        cells_h5ad=cells_h5ad,
        **_given(
            copy_data=_copy_anndata(copy_data),
            bestify=bestify,
            min_sparse_saving_fraction=min_sparse_saving_fraction,
            overwrite=overwrite,
            insist=insist,
        ),
    )


def import_metacells_h5ad(
    daf: DafWriter,
    *,
    cells_h5ad: str,
    metacells_h5ad: str,
    copy_data: Optional[CopyAnnData] = None,
    bestify: Optional[bool] = None,
    min_sparse_saving_fraction: Optional[float] = None,
    overwrite: Optional[bool] = None,
    insist: Optional[bool] = None,
) -> None:
    """
    Import an ``AnnData`` based metacells dataset into a destination ``daf`` data set. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html#Metacells.AnnDataFormat.import_metacells_h5ad!>`__
    for details.
    """
    jl.Metacells.import_metacells_h5ad_b(
        daf,
        cells_h5ad=cells_h5ad,
        metacells_h5ad=metacells_h5ad,
        **_given(
            copy_data=_copy_anndata(copy_data),
            bestify=bestify,
            min_sparse_saving_fraction=min_sparse_saving_fraction,
            overwrite=overwrite,
            insist=insist,
        ),
    )


def reconstruct_type_axis(
    daf: DafWriter,
    *,
    base_axis: Optional[str] = None,
    type_property: Optional[str] = None,
    type_axis: Optional[str] = None,
    empty_type: Optional[str] = None,
    type_colors_csv: Optional[str] = None,
    implicit_properties: Optional[AbstractSet[str]] = None,
    skipped_properties: Optional[AbstractSet[str]] = frozenset({"rare_gene_module", "is_rare"}),
    properties_defaults: Optional[Mapping[str, StorageScalar]] = None,
) -> None:
    """
    Create a type axis after importing data containing type annotations. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html#Metacells.AnnDataFormat.reconstruct_type_axis!>`__
    for details.
    """
    jl.Metacells.reconstruct_type_axis_b(
        daf,
        skipped_properties=skipped_properties,
        **_given(
            base_axis=base_axis,
            type_property=type_property,
            type_axis=type_axis,
            empty_type=empty_type,
            type_colors_csv=type_colors_csv,
            implicit_properties=implicit_properties,
            properties_defaults=properties_defaults,
        ),
    )

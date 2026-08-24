"""
Import ``AnnData`` based data sets. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html>`__ for details.
"""

from typing import Any
from typing import Collection
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Union

from dafpy import DafWriter
from dafpy import StorageScalar

from .julia_import import _given
from .julia_import import _to_julia_scalar_or_collection
from .julia_import import jl

__all__ = [
    "CopyAnnData",
    "import_cells_h5ad",
    "import_gene_masks_per_type",
    "import_metacells_h5ad",
]

#: Which of the ``AnnData`` properties to copy, and under which name. Mapping a name to ``None``
#: skips it; mapping it to a name and a value renames it, using the value for entries the
#: ``AnnData`` does not have.
CopyAnnData = Mapping[str, Optional[Tuple[str, Optional[StorageScalar]]]]


def _copy_anndata(copy_data: Optional[CopyAnnData]) -> Any:
    # A Python dictionary reaches Julia as a ``PyDict``, and the keyword it is passed to is declared
    # as a ``Union``, which Julia type-asserts rather than converts. Converting it here does work,
    # tuples and ``None`` included.
    if copy_data is None:
        return None
    return jl.convert(jl.Metacells.AnnDataFormat.CopyAnnData, copy_data)


def import_cells_h5ad(
    daf: DafWriter,
    *,
    cells_h5ad: str,
    copy_data: Optional[CopyAnnData] = None,
    type_colors_csv: Optional[str] = None,
    empty_type: Optional[Union[str, Collection[str]]] = None,
    bestify: Optional[bool] = None,
    min_sparse_saving_fraction: Optional[float] = None,
    overwrite: Optional[bool] = None,
    insist: Optional[bool] = None,
) -> None:
    """
    Import an ``AnnData`` based cells dataset into a destination ``daf`` data set. Giving a ``type_colors_csv`` also
    creates a ``type`` axis out of it, the file being the authority on which types exist and in what order; the
    ``empty_type`` value(s) are what the data spells "this cell has no type" as, which may be one value or any
    collection of them. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html#Metacells.AnnDataFormat.import_cells_h5ad!>`__
    for details.
    """
    jl.Metacells.import_cells_h5ad_b(
        daf,
        cells_h5ad=cells_h5ad,
        **_given(
            copy_data=_copy_anndata(copy_data),
            type_colors_csv=type_colors_csv,
            empty_type=_to_julia_scalar_or_collection(empty_type),
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


def import_gene_masks_per_type(
    daf: DafWriter,
    *,
    type_axis: Optional[str] = None,
) -> None:
    """
    Convert per-gene masks which name a type in their own name into a per-gene-per-type matrix. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html#Metacells.AnnDataFormat.import_gene_masks_per_type!>`__
    for details.
    """
    jl.Metacells.import_gene_masks_per_type_b(daf, **_given(type_axis=type_axis))

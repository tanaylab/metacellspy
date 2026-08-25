"""
Import ``AnnData`` based data sets. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html>`__ for details.
"""

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
    "import_gene_masks_per_type",
    "import_metacells_h5ad",
    "import_type_colors_csv",
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


def import_type_colors_csv(
    daf: DafWriter,
    *,
    type_colors_csv: str,
    axis: Optional[str] = None,
    property: Optional[str] = None,  # pylint: disable=redefined-builtin
    type_axis: Optional[str] = None,
    overwrite: Optional[bool] = None,
) -> None:
    """
    Create a ``type_axis`` out of a csv file, which is the authority on which types there are, what they are called,
    and in what order they are listed. An empty ``property`` value means the entry has no type; data spelling that some
    other way should be passed through ``dafpy.unify_empty_vector_values`` first. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/anndata_format.html#Metacells.AnnDataFormat.import_type_colors_csv!>`__
    for details.
    """
    jl.Metacells.import_type_colors_csv_b(
        daf,
        type_colors_csv=type_colors_csv,
        **_given(axis=axis, property=property, type_axis=type_axis, overwrite=overwrite),
    )

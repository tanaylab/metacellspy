"""
Fetch gene lists from the Gmara service. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html>`__ for details.
"""

from typing import AbstractSet
from typing import Optional

from dafpy import DafWriter

from .julia_import import _given
from .julia_import import jl

__all__ = [
    "CACHE_DIR",
    "TIMEOUT",
    "empty_gmara_cache",
    "gmara_genes",
    "normalize_gene_name",
    "set_gmara_genes_mask",
]

# These two are a snapshot taken when this module is imported, and are informational only. They come
# from the ``METACELLS_GMARA_CACHE`` and ``METACELLS_GMARA_TIMEOUT`` environment variables, and the
# wrappers never pass them on, so Julia always applies whatever value is bound at the time of the call.

#: Where the fetched gene lists are cached on disk.
CACHE_DIR: str = str(jl.Metacells.Gmara.CACHE_DIR)

#: How long to wait for the Gmara service, in seconds.
TIMEOUT: float = float(jl.Metacells.Gmara.TIMEOUT)


def empty_gmara_cache() -> None:
    """
    All requests are cached in-memory. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.empty_gmara_cache!>`__
    for details.
    """
    jl.Metacells.empty_gmara_cache_b()


def gmara_genes(
    *,
    species: str,
    namespace: Optional[str] = None,
    list: Optional[str] = None,  # pylint: disable=redefined-builtin
    version: Optional[str] = None,
    cache_dir: Optional[str] = None,
    timeout: Optional[float] = None,
) -> AbstractSet[str]:
    """
    Return the set of names of a ``version`` of a ``list`` in a ``namespace`` of genes of some ``species``. See the
    Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.gmara_genes>`__
    for details.
    """
    result = jl.Metacells.gmara_genes(
        species=species,
        **_given(
            namespace=namespace,
            list=list,
            version=version,
            cache_dir=cache_dir,
            timeout=timeout,
        ),
    )
    return {str(name) for name in result}


def normalize_gene_name(
    name: str,
    *,
    namespace: str,
) -> str:
    """
    Normalize a gene name in some namespace. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.normalize_gene_name>`__
    for details.
    """
    result = jl.Metacells.normalize_gene_name(
        name,
        namespace=namespace,
    )
    return str(result)


def set_gmara_genes_mask(
    daf: DafWriter,
    *,
    species: str,
    namespace: Optional[str] = None,
    list: Optional[str] = None,  # pylint: disable=redefined-builtin
    version: Optional[str] = None,
    gene_name_property: Optional[str] = None,
    property: Optional[str] = None,  # pylint: disable=redefined-builtin
    cache_dir: Optional[str] = None,
    timeout: Optional[float] = None,
    overwrite: Optional[bool] = None,
) -> int:
    """
    Set a gene property mask in ``daf`` based on some ``version`` of a Gmara ``list`` of some ``namespace`` for some
    ``species``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.set_gmara_genes_mask!>`__
    for details.
    """
    result = jl.Metacells.set_gmara_genes_mask_b(
        daf,
        species=species,
        **_given(
            namespace=namespace,
            list=list,
            version=version,
            gene_name_property=gene_name_property,
            property=property,
            cache_dir=cache_dir,
            timeout=timeout,
            overwrite=overwrite,
        ),
    )
    return int(result)

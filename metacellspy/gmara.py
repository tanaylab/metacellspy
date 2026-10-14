"""
Fetch gene lists from the Gmara service. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html>`__ for details.
"""

from functools import cached_property
from typing import AbstractSet
from typing import Any
from typing import Dict
from typing import FrozenSet
from typing import List
from typing import Optional

import numpy as np
from dafpy import DafWriter

from .julia_import import _from_julia_array
from .julia_import import _given
from .julia_import import _to_julia_array
from .julia_import import jl

__all__ = [
    "CACHE_DIR",
    "EnsemblConsistency",
    "GmaraEnsemblGenes",
    "TIMEOUT",
    "collect_ensembl_genes",
    "empty_gmara_cache",
    "fetch_gmara_ensembl_genes",
    "gmara_genes",
    "gmara_genes_mask",
    "normalize_gene_name",
    "set_gmara_genes_mask",
    "verify_consistent_ensembl_genes",
]

# These two are a snapshot taken when this module is imported, and are informational only. They come
# from the ``METACELLS_GMARA_CACHE`` and ``METACELLS_GMARA_TIMEOUT`` environment variables, and the
# wrappers never pass them on, so Julia always applies whatever value is bound at the time of the call.

#: Where the fetched gene lists are cached on disk.
CACHE_DIR: str = str(jl.Metacells.Gmara.CACHE_DIR)

#: How long to wait for the Gmara service, in seconds.
TIMEOUT: float = float(jl.Metacells.Gmara.TIMEOUT)


def _frozen_set(jl_set: Any) -> FrozenSet[str]:
    # Convert a Julia set of strings.
    return frozenset(str(value) for value in jl_set)


def _dict_of_frozen_sets(jl_dict: Any) -> Dict[str, FrozenSet[str]]:
    # Convert a Julia dictionary of sets of strings.
    return {str(key): _frozen_set(values) for key, values in jl_dict.items()}


class EnsemblConsistency:  # pylint: disable=too-many-instance-attributes
    """
    The consistency of the Ensembl identifier of a gene name with the mappings of Gmara, as returned by
    :py:func:`verify_consistent_ensembl_genes`. The ``normalized_ensembl`` is ``None`` if the ``ensembl`` is not in the
    form of an Ensembl identifier. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.EnsemblConsistency>`__
    for details.
    """

    def __init__(self, jl_obj: Any) -> None:
        self.jl_obj = jl_obj
        self.name = str(jl_obj.name)
        self.ensembl = str(jl_obj.ensembl)
        self.normalized_ensembl = None if jl_obj.normalized_ensembl is None else str(jl_obj.normalized_ensembl)
        self.name_ensembls = _frozen_set(jl_obj.name_ensembls)
        self.final_ensembls = _frozen_set(jl_obj.final_ensembls)
        self.is_consistent = bool(jl_obj.is_consistent)
        self.ensembl_is_normalized = bool(jl_obj.ensembl_is_normalized)
        self.name_is_empty = bool(jl_obj.name_is_empty)
        self.name_is_unknown = bool(jl_obj.name_is_unknown)
        self.ensembl_is_empty = bool(jl_obj.ensembl_is_empty)
        self.ensembl_is_invalid = bool(jl_obj.ensembl_is_invalid)
        self.ensembl_is_unknown = bool(jl_obj.ensembl_is_unknown)
        self.ensembl_is_retired = bool(jl_obj.ensembl_is_retired)
        self.ensembl_is_different = bool(jl_obj.ensembl_is_different)


class GmaraEnsemblGenes:
    """
    The mappings of gene names to EnsemblGenes of some version of Gmara for some species, as returned by
    :py:func:`fetch_gmara_ensembl_genes`. The ``ensembls_of_name`` and ``final_ensembls_of_ensembl`` are converted from
    Julia when first accessed. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.GmaraEnsemblGenes>`__
    for details.
    """

    def __init__(self, jl_obj: Any) -> None:
        self.jl_obj = jl_obj

    @cached_property
    def ensembls_of_name(self) -> Dict[str, FrozenSet[str]]:
        """
        The final EnsemblGenes of each name of the namespace.
        """
        return _dict_of_frozen_sets(self.jl_obj.ensembls_of_name)

    @cached_property
    def final_ensembls_of_ensembl(self) -> Dict[str, FrozenSet[str]]:
        """
        The final EnsemblGenes of each EnsemblGene identifier.
        """
        return _dict_of_frozen_sets(self.jl_obj.final_ensembls_of_ensembl)


def collect_ensembl_genes(
    *,
    names: np.ndarray,
    gmara_ensembl_genes: GmaraEnsemblGenes,
) -> np.ndarray:
    """
    Return the EnsemblGene of each of the ``names``, or empty if it maps to none or to several. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.collect_ensembl_genes>`__
    for details.
    """
    result = jl.Metacells.collect_ensembl_genes(
        names=_to_julia_array(names),
        gmara_ensembl_genes=gmara_ensembl_genes.jl_obj,
    )
    return _from_julia_array(result)


def empty_gmara_cache() -> None:
    """
    All requests are cached in-memory. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.empty_gmara_cache!>`__
    for details.
    """
    jl.Metacells.empty_gmara_cache_b()


def fetch_gmara_ensembl_genes(
    *,
    species: str,
    namespace: Optional[str] = None,
    version: Optional[str] = None,
    cache_dir: Optional[str] = None,
    timeout: Optional[float] = None,
) -> GmaraEnsemblGenes:
    """
    Fetch the mappings of gene names to EnsemblGenes of some ``version`` of Gmara for some ``species``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.fetch_gmara_ensembl_genes>`__
    for details.
    """
    result = jl.Metacells.fetch_gmara_ensembl_genes(
        species=species,
        **_given(
            namespace=namespace,
            version=version,
            cache_dir=cache_dir,
            timeout=timeout,
        ),
    )
    return GmaraEnsemblGenes(result)


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


def gmara_genes_mask(
    *,
    names: np.ndarray,
    species: str,
    namespace: Optional[str] = None,
    list: Optional[str] = None,  # pylint: disable=redefined-builtin
    version: Optional[str] = None,
    cache_dir: Optional[str] = None,
    timeout: Optional[float] = None,
) -> np.ndarray:
    """
    Return a mask with, for each of the ``names`` in the ``namespace``, whether it is in some ``version`` of a Gmara
    ``list`` for some ``species``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.gmara_genes_mask>`__
    for details.
    """
    result = jl.Metacells.gmara_genes_mask(
        names=_to_julia_array(names),
        species=species,
        **_given(
            namespace=namespace,
            list=list,
            version=version,
            cache_dir=cache_dir,
            timeout=timeout,
        ),
    )
    return _from_julia_array(result)


def normalize_gene_name(
    name: str,
    *,
    namespace: str,
    validate: Optional[bool] = None,
) -> str:
    """
    Normalize a gene name in some namespace. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.normalize_gene_name>`__
    for details.
    """
    result = jl.Metacells.normalize_gene_name(
        name,
        namespace=namespace,
        **_given(validate=validate),
    )
    return str(result)


def set_gmara_genes_mask(
    daf: DafWriter,
    *,
    species: str,
    namespace: Optional[str] = None,
    list: Optional[str] = None,  # pylint: disable=redefined-builtin
    version: Optional[str] = None,
    name_property: Optional[str] = None,
    mask_property: Optional[str] = None,
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
            name_property=name_property,
            mask_property=mask_property,
            cache_dir=cache_dir,
            timeout=timeout,
            overwrite=overwrite,
        ),
    )
    return int(result)


def verify_consistent_ensembl_genes(
    *,
    names: np.ndarray,
    ensembl_per_name: np.ndarray,
    gmara_ensembl_genes: GmaraEnsemblGenes,
) -> List[EnsemblConsistency]:
    """
    Verify that the Ensembl identifier of each of the ``names`` is consistent with the ``gmara_ensembl_genes``. Returns
    the :py:class:`EnsemblConsistency` of each name, in the same order. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/gmara.html#Metacells.Gmara.verify_consistent_ensembl_genes>`__
    for details.
    """
    result = jl.Metacells.verify_consistent_ensembl_genes(
        names=_to_julia_array(names),
        ensembl_per_name=_to_julia_array(ensembl_per_name),
        gmara_ensembl_genes=gmara_ensembl_genes.jl_obj,
    )
    return [EnsemblConsistency(consistency) for consistency in result]

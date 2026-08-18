"""
Test fetching gene lists from the Gmara service.

These tests reach the network, and use a cache directory of their own so that one does not see what
another left behind.
"""

# pylint: disable=missing-function-docstring

from pathlib import Path

import numpy as np
import pytest

import metacellspy as mc
from tests.utilities import memory_daf_of_genes

#: A list which exists for a species that exists, so fetching it succeeds.
SPECIES = "human"

NAMESPACE = "GeneSymbol"


def test_normalize_gene_name() -> None:
    assert mc.normalize_gene_name("MT-CO1", namespace=NAMESPACE) == "MT-CO1"


def test_gmara_genes(tmp_path: Path) -> None:
    genes = mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path))
    assert len(genes) > 0
    assert all(isinstance(gene, str) for gene in genes)


def test_gmara_genes_are_cached(tmp_path: Path) -> None:
    first = mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path))
    # The 2nd fetch is served from the cache, so it has to give the same answer.
    assert mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path)) == first
    mc.empty_gmara_cache()
    assert mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path)) == first


def test_unknown_list_is_an_error(tmp_path: Path) -> None:
    with pytest.raises(Exception, match="404"):
        mc.gmara_genes(species=SPECIES, list="no-such-list", cache_dir=str(tmp_path))


def test_set_gmara_genes_mask(tmp_path: Path) -> None:
    known = sorted(mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path)))
    names = [known[0], known[1], "NO-SUCH-GENE"]
    daf = memory_daf_of_genes(names)

    n_marked = mc.set_gmara_genes_mask(daf, species=SPECIES, property="is_known", cache_dir=str(tmp_path))

    assert n_marked == 2
    mask = daf.get_np_vector("gene", "is_known")
    np.testing.assert_array_equal(mask, np.array([True, True, False]))

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


def test_gmara_genes_mask(tmp_path: Path) -> None:
    known = sorted(mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path)))
    names = np.array([known[0], "NO-SUCH-GENE", known[1]])

    mask = mc.gmara_genes_mask(names=names, species=SPECIES, cache_dir=str(tmp_path))

    np.testing.assert_array_equal(mask, np.array([True, False, True]))


def test_set_gmara_genes_mask(tmp_path: Path) -> None:
    known = sorted(mc.gmara_genes(species=SPECIES, cache_dir=str(tmp_path)))
    names = [known[0], known[1], "NO-SUCH-GENE"]
    daf = memory_daf_of_genes(names)

    n_marked = mc.set_gmara_genes_mask(daf, species=SPECIES, mask_property="is_known", cache_dir=str(tmp_path))

    assert n_marked == 2
    mask = daf.get_np_vector("gene", "is_known")
    np.testing.assert_array_equal(mask, np.array([True, True, False]))


def test_fetch_gmara_ensembl_genes(tmp_path: Path) -> None:
    gmara_ensembl_genes = mc.fetch_gmara_ensembl_genes(species=SPECIES, cache_dir=str(tmp_path))

    ensembls_of_name = gmara_ensembl_genes.ensembls_of_name
    assert ensembls_of_name["SOX4"] == frozenset(["ENSG00000124766"])
    assert gmara_ensembl_genes.final_ensembls_of_ensembl["ENSG00000263255"] == frozenset(["ENSG00000256229"])
    # The mappings are converted once, when first accessed.
    assert gmara_ensembl_genes.ensembls_of_name is ensembls_of_name


def test_collect_ensembl_genes(tmp_path: Path) -> None:
    gmara_ensembl_genes = mc.fetch_gmara_ensembl_genes(species=SPECIES, cache_dir=str(tmp_path))

    ensembl_per_name = mc.collect_ensembl_genes(
        names=np.array(["SOX4", "MTRNR2L6", "NO-SUCH-GENE"]),
        gmara_ensembl_genes=gmara_ensembl_genes,
    )

    np.testing.assert_array_equal(ensembl_per_name, np.array(["ENSG00000124766", "", ""]))


#: The Boolean properties of an ``EnsemblConsistency``.
CONSISTENCY_FLAGS = (
    "is_consistent",
    "ensembl_is_normalized",
    "name_is_empty",
    "name_is_unknown",
    "ensembl_is_empty",
    "ensembl_is_invalid",
    "ensembl_is_unknown",
    "ensembl_is_retired",
    "ensembl_is_different",
)


def test_verify_consistent_ensembl_genes(tmp_path: Path) -> None:
    gmara_ensembl_genes = mc.fetch_gmara_ensembl_genes(species=SPECIES, cache_dir=str(tmp_path))

    consistencies = mc.verify_consistent_ensembl_genes(
        names=np.array(["SOX4", "SOX4", "NO-SUCH-GENE"]),
        ensembl_per_name=np.array(["ENSG00000124766", "ENSG00000263255.2", "ERCC-00002"]),
        gmara_ensembl_genes=gmara_ensembl_genes,
    )

    true_flags = [[flag for flag in CONSISTENCY_FLAGS if getattr(consistency, flag)] for consistency in consistencies]
    assert true_flags == [
        ["is_consistent", "ensembl_is_normalized"],
        ["ensembl_is_retired", "ensembl_is_different"],
        ["name_is_unknown", "ensembl_is_invalid"],
    ]

    retired = consistencies[1]
    assert retired.name == "SOX4"
    assert retired.ensembl == "ENSG00000263255.2"
    assert retired.normalized_ensembl == "ENSG00000263255"
    assert retired.name_ensembls == frozenset(["ENSG00000124766"])
    assert retired.final_ensembls == frozenset(["ENSG00000256229"])

    assert consistencies[2].normalized_ensembl is None

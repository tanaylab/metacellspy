"""
Test importing ``AnnData`` based data sets.

These use the data in the sibling ``metacells-test-data`` directory, which is not part of this
package, so they are skipped when it is not there.
"""

# pylint: disable=missing-function-docstring

from pathlib import Path

import dafpy as dp
import pytest

import metacellspy as mc

CELLS_H5AD = Path(__file__).parent.parent.parent / "metacells-test-data" / "pbmc.h5ad"

needs_test_data = pytest.mark.skipif(not CELLS_H5AD.exists(), reason=f"no {CELLS_H5AD}")

N_CELLS = 68579

N_GENES = 32738


@needs_test_data
def test_import_cells_h5ad() -> None:
    daf = dp.memory_daf(name="test")

    mc.import_cells_h5ad(daf, cells_h5ad=str(CELLS_H5AD))

    assert daf.axis_length("cell") == N_CELLS
    assert daf.axis_length("gene") == N_GENES
    assert daf.has_matrix("cell", "gene", "UMIs")


@needs_test_data
def test_copy_data_renames_a_property() -> None:
    daf = dp.memory_daf(name="test")

    # The mapping has to reach Julia as its own kind of dictionary, which is the one thing about
    # importing that needs converting rather than passing straight through.
    mc.import_cells_h5ad(daf, cells_h5ad=str(CELLS_H5AD), copy_data={"gene_ids": ("gene_identifier", None)})

    assert daf.has_vector("gene", "gene_identifier")


@needs_test_data
def test_skipping_a_property() -> None:
    daf = dp.memory_daf(name="test")

    # Mapping a name to ``None`` skips it, which is the other half of the conversion.
    mc.import_cells_h5ad(daf, cells_h5ad=str(CELLS_H5AD), copy_data={"gene_ids": None})

    assert not daf.has_vector("gene", "gene_ids")

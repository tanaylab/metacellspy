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


def test_import_gene_masks_per_type() -> None:
    # ``AnnData`` has only two axes, so a mask of genes per type has to be spelled as one property per type. This
    # needs no imported data, being about the masks once they are in the repository.
    daf = dp.memory_daf(name="test")
    daf.add_axis("gene", ["G1", "G2", "G3"])
    daf.add_axis("type", ["T1", "T2"])
    daf.set_vector("gene", "essential_gene_of_T1", [True, False, False])
    daf.set_vector("gene", "essential_gene_of_T2", [False, True, True])

    mc.import_gene_masks_per_type(daf)

    assert daf.has_matrix("gene", "type", "is_essential")
    assert daf.get_np_matrix("gene", "type", "is_essential").tolist() == [
        [True, False],
        [False, True],
        [False, True],
    ]


def test_import_type_colors_csv(tmp_path) -> None:
    # The file is the authority on which types exist and in what order: it may name a type nothing has, but a type of
    # some entry which it does not name is an error. This needs no imported data, being about the csv and the axis.
    csv = tmp_path / "type_colors.csv"
    csv.write_text("type,color\nT1,#ff0000\nT2,#00ff00\nT3,#0000ff\n")

    daf = dp.memory_daf(name="test")
    daf.add_axis("cell", ["C1", "C2", "C3"])
    daf.set_vector("cell", "type", ["T1", "", "T2"])

    mc.import_type_colors_csv(daf, type_colors_csv=str(csv))

    assert list(daf.axis_np_vector("type")) == ["T1", "T2", "T3"]
    assert list(daf.get_np_vector("type", "color")) == ["#ff0000", "#00ff00", "#0000ff"]


def test_import_type_colors_csv_missing_type(tmp_path) -> None:
    # An empty value means "no type" and is exempt; anything else has to be in the file. Saying "no type" some other
    # way is ``unify_empty_vector_values``, which is where that concept lives.
    csv = tmp_path / "type_colors.csv"
    csv.write_text("type,color\nT1,#ff0000\n")

    daf = dp.memory_daf(name="test")
    daf.add_axis("cell", ["C1", "C2"])
    daf.set_vector("cell", "type", ["T1", "Outliers"])

    with pytest.raises(Exception, match="Outliers"):
        mc.import_type_colors_csv(daf, type_colors_csv=str(csv))

    # Nothing is written until everything is verified.
    assert not daf.has_axis("type")


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

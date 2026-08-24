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


def test_reconstruct_type_axis() -> None:
    # The default ``skipped_properties`` is a Python set, so this failed before it was converted to a Julia one; the
    # function could not be called at all. This needs no imported data, being about what reaches Julia rather than
    # about what was read from a file.
    daf = dp.memory_daf(name="test")
    daf.add_axis("gene", ["G1", "G2"])
    daf.add_axis("metacell", ["M1", "M2", "M3"])
    daf.set_vector("metacell", "type", ["T1", "T1", "T2"])

    mc.reconstruct_type_axis(daf)

    assert list(daf.axis_np_vector("type")) == ["T1", "T2"]


def test_empty_type() -> None:
    # The value(s) meaning "there is no type here" may be given as one of them, or as any collection of them. Giving
    # only one of them leaves the other as a type of its own, which is what tells the cases apart.
    for empty_type, types in (
        ("Outliers", ["Doublet", "T1"]),
        (("Outliers", "Doublet"), ["T1"]),
        (["Outliers", "Doublet"], ["T1"]),
        ({"Outliers", "Doublet"}, ["T1"]),
    ):
        daf = dp.memory_daf(name="test")
        daf.add_axis("gene", ["G1", "G2"])
        daf.add_axis("metacell", ["M1", "M2", "M3", "M4"])
        daf.set_vector("metacell", "type", ["T1", "T1", "Outliers", "Doublet"])

        mc.reconstruct_type_axis(daf, empty_type=empty_type)

        assert list(daf.axis_np_vector("type")) == types


def test_properties_defaults() -> None:
    # A type axis created in advance may hold types the data does not use, and each reconstructed property then needs
    # a default for them. The defaults are a Python dictionary, which is not the ``Dict`` the keyword is declared as,
    # so passing any used to fail with a type error naming the keyword.
    daf = dp.memory_daf(name="test")
    daf.add_axis("gene", ["G1", "G2"])
    daf.add_axis("type", ["T1", "T2", "T3"])
    daf.add_axis("metacell", ["M1", "M2"])
    daf.set_vector("metacell", "type", ["T1", "T2"])
    daf.set_vector("metacell", "score", [1.0, 2.0])

    mc.reconstruct_type_axis(daf, properties_defaults={"score": 0.0})

    # T3 is used by no metacell, so it takes the default rather than failing for want of one.
    assert list(daf.get_np_vector("type", "score")) == [1.0, 2.0, 0.0]


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

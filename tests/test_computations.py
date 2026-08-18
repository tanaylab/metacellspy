"""
Test the computations on a small data set built in memory.

Only the computations a toy data set can actually satisfy are tested here; the point is that the
wrappers really invoke the Julia code and that the results come back as ``numpy`` arrays, not that
the algorithms are correct, which is tested in Julia.
"""

# pylint: disable=missing-function-docstring

import numpy as np

import metacellspy as mc
from tests.utilities import memory_daf_of_cells
from tests.utilities import memory_daf_of_metacells

N_CELLS = 20

N_GENES = 8

N_METACELLS = 4


def test_total_UMIs_per_cell() -> None:  # pylint: disable=invalid-name
    daf = memory_daf_of_cells(N_CELLS, N_GENES)

    mc.compute_vector_of_total_UMIs_per_cell(daf)

    totals = daf.get_np_vector("cell", "total_UMIs")
    assert totals.shape == (N_CELLS,)
    expected = daf.get_np_matrix("cell", "gene", "UMIs").sum(axis=1)
    np.testing.assert_array_equal(totals, expected)


def test_overwrite_is_needed_to_recompute() -> None:
    daf = memory_daf_of_cells(N_CELLS, N_GENES)
    mc.compute_vector_of_total_UMIs_per_cell(daf)

    # Julia refuses to replace existing data unless it is told to, and the wrapper has to pass that on.
    try:
        mc.compute_vector_of_total_UMIs_per_cell(daf)
        raised = False
    except Exception:  # pylint: disable=broad-exception-caught
        raised = True
    assert raised, "recomputing without overwrite did not fail"

    mc.compute_vector_of_total_UMIs_per_cell(daf, overwrite=True)


def test_marker_genes() -> None:
    # Marker genes are found from the metacells, so this runs the chain that leads up to them, which
    # is what a caller would do.
    daf = memory_daf_of_metacells(N_CELLS, N_GENES, N_METACELLS)

    mc.compute_matrix_of_UMIs_per_gene_per_metacell(daf)
    mc.compute_vector_of_total_UMIs_per_metacell(daf)
    mc.compute_matrix_of_linear_fraction_per_gene_per_metacell(daf)
    mc.compute_matrix_of_log_linear_fraction_per_gene_per_metacell(daf)
    mc.compute_vector_of_is_marker_per_gene(daf, min_marker_gene_range_fold=0.5)

    UMIs = daf.get_np_matrix("gene", "metacell", "UMIs")  # pylint: disable=invalid-name
    assert UMIs.shape == (N_GENES, N_METACELLS)
    assert UMIs.sum() == daf.get_np_matrix("cell", "gene", "UMIs").sum()

    is_marker = daf.get_np_vector("gene", "is_marker")
    assert is_marker.shape == (N_GENES,)
    assert is_marker.dtype == np.bool_

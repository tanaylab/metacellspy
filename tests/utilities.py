"""
Build the small data sets the tests compute on.
"""

from typing import Sequence

import dafpy as dp
import numpy as np


def memory_daf_of_genes(names: Sequence[str]) -> dp.DafWriter:
    """Return an in-memory repository holding just a gene axis with the given names."""
    daf = dp.memory_daf(name="test")
    daf.add_axis("gene", np.array(names, dtype=str))
    return daf


def memory_daf_of_cells(n_cells: int = 20, n_genes: int = 8) -> dp.DafWriter:
    """Return an in-memory repository of cells and genes, with a UMIs matrix and nothing excluded.

    The UMIs are a fixed pattern rather than random ones, so the computed results are the same on
    every run and can be asserted exactly.
    """
    daf = dp.memory_daf(name="test")
    daf.add_axis("cell", np.array([f"cell{index}" for index in range(n_cells)], dtype=str))
    daf.add_axis("gene", np.array([f"gene{index}" for index in range(n_genes)], dtype=str))

    # The matrix has to be in column-major layout, which is what ``Daf`` stores.
    UMIs = np.asfortranarray(  # pylint: disable=invalid-name
        np.arange(n_cells * n_genes, dtype=np.uint32).reshape(n_cells, n_genes) % 7
    )
    daf.set_matrix("cell", "gene", "UMIs", UMIs, relayout=True)
    daf.set_vector("gene", "is_excluded", np.zeros(n_genes, dtype=bool))

    return daf


def memory_daf_of_metacells(n_cells: int = 20, n_genes: int = 8, n_metacells: int = 4) -> dp.DafWriter:
    """Return an in-memory repository of cells grouped into metacells, in round-robin order."""
    daf = memory_daf_of_cells(n_cells, n_genes)
    daf.add_axis("metacell", np.array([f"metacell{index}" for index in range(n_metacells)], dtype=str))
    daf.set_vector(
        "cell", "metacell", np.array([f"metacell{index % n_metacells}" for index in range(n_cells)], dtype=str)
    )
    return daf

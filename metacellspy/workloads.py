"""
Make the calls of a typical session (for internal use).

The Julia package ``MetacellsPy`` runs this while it is precompiled, so the code these calls compile is cached, and a
session does not compile it again. It is not part of the API, so the package does not import it.
"""

import dafpy as dp
import numpy as np

from .analyze_cells import compute_vector_of_total_UMIs_per_cell
from .analyze_genes import compute_vector_of_is_marker_per_gene
from .analyze_metacells import compute_matrix_of_linear_fraction_per_gene_per_metacell
from .analyze_metacells import compute_matrix_of_log_linear_fraction_per_gene_per_metacell
from .analyze_metacells import compute_matrix_of_UMIs_per_gene_per_metacell
from .analyze_metacells import compute_vector_of_total_UMIs_per_metacell

__all__ = ["run_workload"]

N_CELLS = 20
N_GENES = 8
N_METACELLS = 4


def run_workload() -> None:
    """
    Make the calls of a typical session, computing the marker genes of a small fixed data set (for internal use).
    """
    daf = dp.memory_daf(name="workload")
    daf.add_axis("cell", np.array([f"cell{index}" for index in range(N_CELLS)], dtype=str))
    daf.add_axis("gene", np.array([f"gene{index}" for index in range(N_GENES)], dtype=str))
    daf.add_axis("metacell", np.array([f"metacell{index}" for index in range(N_METACELLS)], dtype=str))
    umis = np.asfortranarray(np.arange(N_CELLS * N_GENES, dtype=np.uint32).reshape(N_CELLS, N_GENES) % 7)
    daf.set_matrix("cell", "gene", "UMIs", umis, relayout=True)
    daf.set_vector("gene", "is_excluded", np.zeros(N_GENES, dtype=bool))
    daf.set_vector(
        "cell", "metacell", np.array([f"metacell{index % N_METACELLS}" for index in range(N_CELLS)], dtype=str)
    )

    compute_vector_of_total_UMIs_per_cell(daf)
    compute_matrix_of_UMIs_per_gene_per_metacell(daf)
    compute_vector_of_total_UMIs_per_metacell(daf)
    compute_matrix_of_linear_fraction_per_gene_per_metacell(daf)
    compute_matrix_of_log_linear_fraction_per_gene_per_metacell(daf)
    compute_vector_of_is_marker_per_gene(daf, min_marker_gene_range_fold=0.5)

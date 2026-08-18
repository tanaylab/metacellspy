"""
The default values used by the computations. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/defaults.html>`__ for details.

These are a snapshot taken when this module is imported, and are informational only. The wrappers
never pass them on, so Julia always applies whatever value is bound at the time of the call.
"""

from .julia_import import jl

__all__ = [
    "GENE_FRACTION_REGULARIZATION_FOR_CELLS",
    "GENE_FRACTION_REGULARIZATION_FOR_METACELLS",
    "MIN_SIGNIFICANT_GENE_UMIS",
]

#: The regularization factor added to gene fractions of cells.
GENE_FRACTION_REGULARIZATION_FOR_CELLS: float = float(jl.Metacells.GENE_FRACTION_REGULARIZATION_FOR_CELLS)

#: The regularization factor added to gene fractions of metacells.
GENE_FRACTION_REGULARIZATION_FOR_METACELLS: float = float(jl.Metacells.GENE_FRACTION_REGULARIZATION_FOR_METACELLS)

#: The minimal number of UMIs of a gene for its measurement to be considered significant.
MIN_SIGNIFICANT_GENE_UMIS: int = int(jl.Metacells.MIN_SIGNIFICANT_GENE_UMIS)

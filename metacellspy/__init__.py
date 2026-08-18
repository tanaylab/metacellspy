"""
Metacell analysis, wrapping the `Metacells.jl <https://github.com/tanaylab/Metacells.jl>`__ Julia
package. See its `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/index.html>`__ for
what each computation does.

The API is the same as the Julia one, with the following adaptations:

* The Julia ``!`` suffix, marking a computation which modifies its data, is dropped from the name.

* Every optional parameter defaults to ``None``, meaning "use whatever the Julia default is". The
  Julia defaults are therefore never restated here, which matters because some of them are computed
  from the values of the other parameters.

* The ``rng`` parameter is an ``int`` seed rather than a Julia random number generator. The default
  ``0`` means "use Julia's default generator", that is, do not force reproducible results.

* The computations which return a data frame return a ``pandas.DataFrame``.

* The contracts, which declare what data each computation reads and writes, are not exposed, as they
  are only usable from Julia. See the
  `contracts <https://tanaylab.github.io/Metacells.jl/v0.1.0/contracts.html>`__ documentation for
  the vocabulary of what lives in a repository.

This is unrelated to the `metacells <https://github.com/tanaylab/metacells>`__ Python package, which
is a separate and independent implementation.
"""

__author__ = "Oren Ben-Kiki"
__email__ = "oren@ben-kiki.org"
__version__ = "0.1.0"

from .analyze_blocks import *
from .analyze_cells import *
from .analyze_genes import *
from .analyze_metacells import *
from .analyze_modules import *
from .anndata_format import *
from .compute_blocks import *
from .compute_modules import *
from .defaults import *
from .gmara import *
from .julia_import import *
from .project_cells import *
from .sharpen_metacells import *

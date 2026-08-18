"""
Import the Julia environment.

The environment itself is set up by ``dafpy``, which this package depends on, so everything here is
taken from ``dafpy.julia_import`` rather than repeated. In particular, see it for the
``PYTHON_JULIACALL_*`` environment variables which control how Julia is invoked; they apply here
just the same, and have to be set before importing either package.
"""

from typing import Any
from typing import Optional

from dafpy.julia_import import _from_julia_frame  # pylint: disable=unused-import
from dafpy.julia_import import _given  # pylint: disable=unused-import
from dafpy.julia_import import _to_julia_array  # pylint: disable=unused-import
from dafpy.julia_import import jl
from dafpy.julia_import import jl_version
from dafpy.julia_import import use_default_julia_environment

__all__ = ["jl", "jl_version", "use_default_julia_environment"]

# Everything is imported rather than ``using``, so no package's exports leak into Julia's ``Main``.
# This keeps ``Main`` clear for other Python packages that wrap Julia packages and are used in the
# same session.
for package in ("Metacells", "Random"):
    if jl.seval('Base.find_package("' + package + '")') is None:
        jl.seval('Pkg.add("' + package + '")')
    jl.seval("import " + package)

# Unlike ``dafpy`` and ``somegraphspy``, this package needs no Julia code of its own. Every value it
# passes on is one Julia converts by itself, including the mapping of which ``AnnData`` data to copy,
# whose Python tuples and ``None`` become Julia tuples and ``nothing``.


def _rng(rng: Optional[int]) -> Any:
    """
    Convert a random number generator seed to a Julia one (for internal use).

    A zero seed means "use Julia's default generator", that is, do not force reproducible results.
    It is returned as ``None`` so that ``_given`` drops it and Julia applies its own default.
    """
    if rng is None or rng == 0:
        return None
    return jl.Random.MersenneTwister(rng)

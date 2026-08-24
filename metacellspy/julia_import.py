"""
Import the Julia environment.

The Julia run-time is obtained by ``dafpy``, which this package depends on, so everything here is taken from
``dafpy.julia_import`` rather than repeated. See it for how Julia is chosen and configured, which is by ``juliacall``'s
own environment variables, plus the ``@default`` value those variables accept here. All of them have to be set before
importing this package, since importing it imports ``dafpy``, which starts Julia.
"""

from typing import Any
from typing import Optional

from dafpy.julia_import import _from_julia_frame  # pylint: disable=unused-import
from dafpy.julia_import import _given  # pylint: disable=unused-import
from dafpy.julia_import import _to_julia_array  # pylint: disable=unused-import
from dafpy.julia_import import _to_julia_set  # pylint: disable=unused-import
from dafpy.julia_import import jl
from dafpy.julia_import import jl_version

__all__ = ["jl", "jl_version"]

# Everything is imported rather than ``using``, so no package's exports leak into Julia's ``Main``. This keeps
# ``Main`` clear for other Python packages that wrap Julia packages and are used in the same session.
for package in ("Metacells", "Random"):
    jl.seval("import " + package)

# Unlike ``dafpy`` and ``somegraphspy``, this package needs no Julia code of its own. Every value it passes on is one
# Julia converts by itself, including the mapping of which ``AnnData`` data to copy, whose Python tuples and ``None``
# become Julia tuples and ``nothing``.


def _rng(rng: Optional[int]) -> Any:
    """
    Convert a random number generator seed to a Julia one (for internal use).

    A zero seed means "use Julia's default generator", that is, do not force reproducible results. It is returned as
    ``None`` so that ``_given`` drops it and Julia applies its own default.
    """
    if rng is None or rng == 0:
        return None
    return jl.Random.MersenneTwister(rng)

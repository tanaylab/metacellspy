"""
Import the Julia environment.

The Julia run-time is obtained by ``dafpy``, which this package depends on, so everything here is taken from
``dafpy.julia_import`` rather than repeated. See it for how Julia is chosen and configured, which is by ``juliacall``'s
own environment variables, plus the ``@default`` value those variables accept here. All of them have to be set before
importing this package, since importing it imports ``dafpy``, which starts Julia.
"""

import builtins
import os
import tomllib
from typing import Any

from dafpy.julia_import import DEFAULT
from dafpy.julia_import import DefaultValue
from dafpy.julia_import import _from_julia_array  # pylint: disable=unused-import
from dafpy.julia_import import _from_julia_frame  # pylint: disable=unused-import
from dafpy.julia_import import _given  # pylint: disable=unused-import
from dafpy.julia_import import _to_julia_array  # pylint: disable=unused-import
from dafpy.julia_import import _to_julia_scalar_or_collection  # pylint: disable=unused-import
from dafpy.julia_import import jl as _dafpy_jl
from dafpy.julia_import import jl_version

__all__ = ["jl", "jl_version"]

# The Julia package ``MetacellsPy``, in ``julia/MetacellsPy`` beside this file, caches the code our calls compile. Its
# ``Project.toml`` lists the Julia packages we use. Unlike ``dafpy`` and ``somegraphspy``, this package needs no Julia
# code of its own. Every value it passes on is one Julia converts by itself, including the mapping of which ``AnnData``
# data to copy, whose Python tuples and ``None`` become Julia tuples and ``nothing``.
_GLUE_PROJECT_PATH = os.path.join(os.path.dirname(__file__), "julia", "MetacellsPy", "Project.toml")

# While ``MetacellsPy`` itself is precompiled, Julia may not import anything into ``Main``, so ``MetacellsPy`` hands
# itself over instead, and it binds the same names.
_METACELLSPY_GLUE: Any = getattr(builtins, "_metacellspy_glue", None)

#: The interface to the Julia run-time. This is Julia's ``Main``, as in ``dafpy``, except while ``MetacellsPy`` itself
#: is precompiled.
jl = _dafpy_jl if _METACELLSPY_GLUE is None else _METACELLSPY_GLUE

if _METACELLSPY_GLUE is None:
    with open(_GLUE_PROJECT_PATH, "rb") as glue_project_file:
        _GLUE_PACKAGES = tomllib.load(glue_project_file)["deps"]
    # Everything is imported rather than ``using``, so no package's exports leak into Julia's ``Main``. This keeps
    # ``Main`` clear for other Python packages that wrap Julia packages and are used in the same session.
    for package in ["MetacellsPy"] + sorted(_GLUE_PACKAGES):
        if package != "PrecompileTools":
            jl.seval("import " + package)


def _rng(rng: int | DefaultValue) -> Any:
    """
    Convert a random number generator seed to a Julia one (for internal use).

    A ``DEFAULT`` seed means "use Julia's default generator", that is, do not force reproducible results. It is
    returned as is, so that ``_given`` drops it and Julia applies its own default.
    """
    if isinstance(rng, DefaultValue):
        return DEFAULT
    return jl.Random.MersenneTwister(rng)

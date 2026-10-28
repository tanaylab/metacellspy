"""
Test the Julia environment this package adds on top of the one ``dafpy`` sets up.
"""

# pylint: disable=missing-function-docstring

import json
import os
import tomllib
from typing import Any
from typing import Collection

import dafpy as dp

import metacellspy as mc
from metacellspy.julia_import import _GLUE_PROJECT_PATH
from metacellspy.julia_import import DEFAULT
from metacellspy.julia_import import _rng
from metacellspy.julia_import import jl

#: Names exported by the Julia package we wrap. Importing (rather than ``using``) it keeps these out of ``Main``.
EXPORTED_NAMES = ("compute_metacells_blocks!", "sharpen_metacells!", "import_cells_h5ad!", "gmara_genes")


def test_shares_the_dafpy_julia_runtime() -> None:
    # There is one Julia in the process, so both packages have to be talking to the same one.
    assert mc.jl is dp.jl


def test_wrapped_package_does_not_leak() -> None:
    for name in EXPORTED_NAMES:
        assert not jl.isdefined(jl.Main, jl.Symbol(name)), f"the exported {name} leaked into Julia's Main"


def _glue_project() -> dict[str, Any]:
    with open(_GLUE_PROJECT_PATH, "rb") as file:
        return tomllib.load(file)


def test_glue_version_is_the_package_version() -> None:
    assert _glue_project()["version"] == mc.__version__


def _dependencies_of(package: str) -> Collection[str]:
    # The dependencies a Julia package's own ``Project.toml`` lists, if it is loaded in ``Main``.
    if not jl.seval(f"isdefined(Main, :{package})"):
        return ()
    directory = jl.seval(f"pkgdir({package})")
    if directory is None:
        return ()
    with open(os.path.join(str(directory), "Project.toml"), "rb") as file:
        return tomllib.load(file).get("deps", {})


def test_url_packages_are_glue_dependencies() -> None:
    # A package comes by URL when it is not registered. It is a dependency of MetacellsPy, or of one of MetacellsPy's
    # dependencies.
    with open(os.path.join(os.path.dirname(mc.__file__), "juliapkg.json"), encoding="utf8") as file:
        packages = json.load(file)["packages"]
    glue_packages = _glue_project()["deps"]
    for name, package in packages.items():
        if "url" in package and name != "MetacellsPy":
            assert name in glue_packages or any(
                name in _dependencies_of(glue_package) for glue_package in glue_packages
            ), f"the URL package {name} of juliapkg.json is not a dependency of MetacellsPy, nor of its dependencies"


def test_both_julia_packages_are_imported() -> None:
    for package in ("Metacells", "Random"):
        assert jl.seval(f"isdefined(Main, :{package})"), f"{package} was not imported"


def test_zero_seed_means_the_julia_default() -> None:
    # Zero is dropped by ``_given``, so Julia uses its own generator and the results are not reproducible.
    assert _rng(0) is DEFAULT
    assert _rng(None) is DEFAULT


def test_non_zero_seed_becomes_a_generator() -> None:
    generator = _rng(123456)
    assert generator is not None
    assert str(jl.typeof(generator)) == "Random.MersenneTwister"
    # The same seed has to give the same generator, which is the point of passing one.
    assert str(jl.string(generator)) == str(jl.string(_rng(123456)))

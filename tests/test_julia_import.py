"""
Test the Julia environment this package adds on top of the one ``dafpy`` sets up.
"""

# pylint: disable=missing-function-docstring

import dafpy as dp

import metacellspy as mc
from metacellspy.julia_import import _rng
from metacellspy.julia_import import jl

#: Names exported by the Julia package we wrap. Importing (rather than ``using``) it keeps these out of ``Main``.
EXPORTED_NAMES = ("compute_metacells_blocks!", "sharpen_metacells!", "import_cells_h5ad!", "gmara_genes")


def test_shares_the_dafpy_julia_runtime() -> None:
    # There is one Julia in the process, so both packages have to be talking to the same one.
    assert mc.jl is dp.jl


def test_wrapped_package_does_not_leak() -> None:
    for name in EXPORTED_NAMES:
        assert not jl.seval(f'isdefined(Main, Symbol("{name}"))'), f"the exported {name} leaked into Julia's Main"


def test_both_julia_packages_are_imported() -> None:
    for package in ("Metacells", "Random"):
        assert jl.seval(f"isdefined(Main, :{package})"), f"{package} was not imported"


def test_zero_seed_means_the_julia_default() -> None:
    # Zero is dropped by ``_given``, so Julia uses its own generator and the results are not reproducible.
    assert _rng(0) is None
    assert _rng(None) is None


def test_non_zero_seed_becomes_a_generator() -> None:
    generator = _rng(123456)
    assert generator is not None
    assert str(jl.typeof(generator)) == "Random.MersenneTwister"
    # The same seed has to give the same generator, which is the point of passing one.
    assert str(jl.string(generator)) == str(jl.string(_rng(123456)))

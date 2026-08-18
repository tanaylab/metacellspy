"""
Test that each wrapper matches the Julia function it wraps.

Every wrapper is the same mechanical translation of a Julia function, so what can go wrong is a
mistranslation: a misspelled keyword, a keyword that was added or removed in Julia, a name that no
longer exists. Comparing each wrapper against the Julia definition catches all of these.
"""

# pylint: disable=missing-function-docstring

import importlib
import inspect
from typing import Any
from typing import Callable
from typing import List
from typing import Mapping
from typing import Tuple

import metacellspy as mc
from metacellspy.julia_import import jl

#: The Julia submodule each Python module wraps.
SUBMODULE_OF_MODULE = {
    "gmara": "Gmara",
    "anndata_format": "AnnDataFormat",
    "analyze_cells": "AnalyzeCells",
    "analyze_metacells": "AnalyzeMetacells",
    "analyze_genes": "AnalyzeGenes",
    "compute_blocks": "ComputeBlocks",
    "analyze_blocks": "AnalyzeBlocks",
    "compute_modules": "ComputeModules",
    "analyze_modules": "AnalyzeModules",
    "sharpen_metacells": "SharpenMetacells",
    "project_cells": "ProjectCells",
}

#: The wrapper takes an ``int`` seed where Julia takes a random number generator.
SEED_KEYWORD = "rng"


def _wrappers() -> List[Tuple[str, str, Callable[..., Any]]]:
    """Collect every wrapper, with the Julia submodule and function name it wraps."""
    wrappers: List[Tuple[str, str, Callable[..., Any]]] = []
    for module_name, submodule in SUBMODULE_OF_MODULE.items():
        # The module is imported by name rather than fetched from the package, because a module and
        # the single computation it holds can have the same name (e.g. ``compute_blocks``), and the
        # re-export shadows the module with the function.
        module = importlib.import_module(f"metacellspy.{module_name}")
        for name in module.__all__:
            value = getattr(module, name)
            # Anything else exported is a constant or a type alias, and a type alias is callable.
            if inspect.isfunction(value):
                wrappers.append((submodule, name, value))
    return wrappers


WRAPPERS = _wrappers()


def _julia_function(submodule: str, name: str) -> Any:
    """Return the Julia function a wrapper invokes, whichever of the two spellings it has."""
    julia_submodule = getattr(jl.Metacells, submodule)
    for julia_name in (name, name + "!"):
        if bool(jl.isdefined(julia_submodule, jl.Symbol(julia_name))):
            return jl.getproperty(julia_submodule, jl.Symbol(julia_name))
    raise AssertionError(f"no Julia function for {submodule}.{name}")


def _julia_keywords(submodule: str, name: str) -> List[str]:
    function = _julia_function(submodule, name)
    method = jl.only(jl.methods(function))
    return [str(keyword) for keyword in jl.Base.kwarg_decl(method)]


def _python_keywords(wrapper: Callable[..., Any]) -> List[str]:
    return [
        name
        for name, parameter in inspect.signature(wrapper).parameters.items()
        if parameter.kind == inspect.Parameter.KEYWORD_ONLY
    ]


def test_every_wrapper_has_a_julia_function() -> None:
    for submodule, name, _wrapper in WRAPPERS:
        _julia_function(submodule, name)


def test_keywords_match_julia() -> None:
    for submodule, name, wrapper in WRAPPERS:
        assert sorted(_python_keywords(wrapper)) == sorted(
            _julia_keywords(submodule, name)
        ), f"the keywords of {submodule}.{name} differ from the Julia ones"


def test_optional_keywords_default_to_none() -> None:
    # A default of ``None`` is what makes ``_given`` drop the keyword so that Julia applies its own
    # default, which may be computed from the other keywords. The exceptions are the seed, and the
    # two keywords whose Julia default is not ``nothing``, where ``None`` is a meaningful value.
    exceptions = {SEED_KEYWORD, "improvement_half_life", "skipped_properties"}
    for submodule, name, wrapper in WRAPPERS:
        for keyword, parameter in inspect.signature(wrapper).parameters.items():
            if parameter.kind != inspect.Parameter.KEYWORD_ONLY:
                continue
            if parameter.default is inspect.Parameter.empty or keyword in exceptions:
                continue
            assert parameter.default is None, f"{submodule}.{name} defaults {keyword} to {parameter.default!r}"


def test_required_keywords_match_julia() -> None:
    # A keyword with no Julia default has to be given, so it stays required in Python too.
    for submodule, name, wrapper in WRAPPERS:
        function = _julia_function(submodule, name)
        method = jl.only(jl.methods(function))
        required = {
            keyword
            for keyword, parameter in inspect.signature(wrapper).parameters.items()
            if parameter.kind == inspect.Parameter.KEYWORD_ONLY and parameter.default is inspect.Parameter.empty
        }
        assert required <= set(str(keyword) for keyword in jl.Base.kwarg_decl(method))


def test_seed_replaces_the_random_number_generator() -> None:
    for submodule, name, wrapper in WRAPPERS:
        if SEED_KEYWORD not in _julia_keywords(submodule, name):
            continue
        parameter = inspect.signature(wrapper).parameters[SEED_KEYWORD]
        assert parameter.annotation is int, f"{submodule}.{name} does not take an int seed"
        assert parameter.default == 0, f"{submodule}.{name} does not default the seed to 0"


def test_every_wrapper_is_exported() -> None:
    exported: Mapping[str, Any] = vars(mc)
    for _submodule, name, wrapper in WRAPPERS:
        assert exported.get(name) is wrapper, f"{name} is not re-exported by the package"

"""
Run whole stages of the metacells pipeline. See the Julia
`documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html>`__ for details.
"""

from typing import Any
from typing import Collection
from typing import Iterator
from typing import Union

import numpy as np
from dafpy import DafReader
from dafpy import DafWriter
from dafpy import StorageScalar
from dafpy import wrap_daf

from .julia_import import DEFAULT
from .julia_import import DefaultValue
from .julia_import import _given
from .julia_import import _rng
from .julia_import import _to_julia_array
from .julia_import import _to_julia_scalar_or_collection
from .julia_import import jl

__all__ = [
    "analyze_metacells",
    "focus_metacells",
    "import_base_metacells",
    "prepare_atlas",
    "prepare_metacells",
    "qc_metacells",
    "sharpen_round",
    "SharpeningRound",
    "sharpening_rounds",
]


def import_base_metacells(
    *,
    cells_daf: DafWriter,
    metacells_daf: DafWriter,
    metacell_per_cell: np.ndarray,
    empty_metacells: Union[StorageScalar, Collection[StorageScalar], None, DefaultValue] = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Bring in the base metacells the sharpening pipeline starts with. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.import_base_metacells!>`__
    for details.
    """
    jl.Metacells.import_base_metacells_b(
        cells_daf=cells_daf,
        metacells_daf=metacells_daf,
        metacell_per_cell=_to_julia_array(metacell_per_cell),
        **_given(
            empty_metacells=_to_julia_scalar_or_collection(empty_metacells),
            overwrite=overwrite,
        ),
    )


def prepare_metacells(daf: DafWriter, *, overwrite: bool | DefaultValue = DEFAULT) -> None:
    """
    Aggregate the cells of each metacell into the metacell, and find the marker genes and how they correlate with
    each other. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.prepare_metacells!>`__
    for details.
    """
    jl.Metacells.prepare_metacells_b(
        daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def focus_metacells(
    *,
    full_daf: DafWriter,
    focus_daf: DafWriter,
    max_redundant_fold: float | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Reduce the metacells of ``full_daf`` to a non-redundant focus set in ``focus_daf``, which can then be analyzed and
    sharpened like any other metacells. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.focus_metacells!>`__
    for details.
    """
    jl.Metacells.focus_metacells_b(
        full_daf=full_daf,
        focus_daf=focus_daf,
        **_given(
            max_redundant_fold=max_redundant_fold,
            overwrite=overwrite,
        ),
    )


def analyze_metacells(
    daf: DafWriter,
    *,
    prefix: str | DefaultValue = DEFAULT,
    prev_daf: DafReader | None | DefaultValue = DEFAULT,
    module_status: bool | DefaultValue = DEFAULT,
    rng: int | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Compute more advanced properties based on the metacells, taking into account gene masks. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.analyze_metacells!>`__
    for details.
    """
    jl.Metacells.analyze_metacells_b(
        daf,
        **_given(
            prefix=prefix,
            prev_daf=prev_daf,
            module_status=module_status,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )


def qc_metacells(
    *,
    daf: DafWriter,
    score_daf: DafReader,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Say how well the metacells describe the cells they were aggregated from, judged in the locations of the manifold
    the ``score_daf`` repository laid out. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.qc_metacells!>`__
    for details.
    """
    jl.Metacells.qc_metacells_b(
        daf=daf,
        score_daf=score_daf,
        **_given(
            overwrite=overwrite,
        ),
    )


def prepare_atlas(
    daf: DafWriter,
    *,
    std_UMIs_regularization: float | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Prepare analyzed metacells to serve as the atlas that cells are projected onto. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.prepare_atlas!>`__
    for details.
    """
    jl.Metacells.prepare_atlas_b(
        daf,
        **_given(
            std_UMIs_regularization=std_UMIs_regularization,
            overwrite=overwrite,
        ),
    )


def sharpen_round(
    *,
    sharp_daf: DafWriter,
    prev_daf: DafReader,
    score_daf: DafReader,
    sharpening_round: int,
    metacells_prefix: str | DefaultValue = DEFAULT,
    blocks_prefix: str | DefaultValue = DEFAULT,
    module_status: bool | DefaultValue = DEFAULT,
    rng: int | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> None:
    """
    Run one round of sharpening: regroup the cells into new metacells, aggregate and analyze them, and score them
    against the ``score_daf``. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.sharpen_round!>`__
    for details.
    """
    jl.Metacells.sharpen_round_b(
        sharp_daf=sharp_daf,
        prev_daf=prev_daf,
        score_daf=score_daf,
        sharpening_round=sharpening_round,
        **_given(
            metacells_prefix=metacells_prefix,
            blocks_prefix=blocks_prefix,
            module_status=module_status,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )


class SharpeningRound:  # pylint: disable=too-many-instance-attributes
    """
    One round of the :py:func:`sharpening_rounds`. The ``index`` is the number of the round, starting at 1. The
    ``previous_daf`` is the metacells of the round before this one. The ``metacells_prefix`` and the ``blocks_prefix``
    are this round's prefixes. The rest are as given to :py:func:`sharpening_rounds`. See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.SharpeningRound>`__
    for details.
    """

    def __init__(self, jl_obj: Any) -> None:
        self.jl_obj = jl_obj
        self.index = int(jl_obj.index)
        self.previous_daf = wrap_daf(jl_obj.previous_daf)
        self.base_daf = wrap_daf(jl_obj.base_daf)
        self.score_daf = wrap_daf(jl_obj.score_daf)
        self.directory = str(jl_obj.directory)
        self.metacells_prefix = str(jl_obj.metacells_prefix)
        self.blocks_prefix = str(jl_obj.blocks_prefix)
        self.module_status = bool(jl_obj.module_status)
        self.overwrite = bool(jl_obj.overwrite)

    def run(
        self,
        name: str,
        *,
        metacells_prefix: str | DefaultValue = DEFAULT,
        blocks_prefix: str | DefaultValue = DEFAULT,
        module_status: bool | DefaultValue = DEFAULT,
        rng: int | DefaultValue = DEFAULT,
        overwrite: bool | DefaultValue = DEFAULT,
    ) -> DafWriter:
        """
        Run this round, creating a repository with the ``name`` in the round's ``directory``, and return it. Any of the
        round's parameters can be overridden for this round only. See the Julia
        `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.run!>`__
        for details.
        """
        sharp_daf = wrap_daf(
            jl.Metacells.run_b(
                self.jl_obj,
                name,
                **_given(
                    metacells_prefix=metacells_prefix,
                    blocks_prefix=blocks_prefix,
                    module_status=module_status,
                    rng=_rng(rng),
                    overwrite=overwrite,
                ),
            )
        )
        assert isinstance(sharp_daf, DafWriter)
        return sharp_daf


def sharpening_rounds(
    *,
    initial_daf: DafReader,
    base_daf: DafReader,
    score_daf: DafReader,
    directory: str,
    metacells_prefix: str | DefaultValue = DEFAULT,
    blocks_prefix: str | DefaultValue = DEFAULT,
    module_status: bool | DefaultValue = DEFAULT,
    rng: int | DefaultValue = DEFAULT,
    overwrite: bool | DefaultValue = DEFAULT,
) -> Iterator[SharpeningRound]:
    """
    Iterate on rounds of sharpening, starting from the ``initial_daf`` metacells. Each round is a
    :py:class:`SharpeningRound`, which must be run before the next one is taken. The iteration never ends by itself.
    The caller decides when to stop:

    .. code-block:: python

        for sharpening_round in sharpening_rounds(initial_daf=..., base_daf=..., score_daf=..., directory="dafs"):
            if sharpening_round.index > 2:
                break
            metacells_daf = sharpening_round.run(f"metacells.R{sharpening_round.index}")

    See the Julia
    `documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/pipeline.html#Metacells.Pipeline.sharpening_rounds>`__
    for details.
    """
    rounds = jl.Metacells.sharpening_rounds(
        initial_daf=initial_daf,
        base_daf=base_daf,
        score_daf=score_daf,
        directory=directory,
        **_given(
            metacells_prefix=metacells_prefix,
            blocks_prefix=blocks_prefix,
            module_status=module_status,
            rng=_rng(rng),
            overwrite=overwrite,
        ),
    )
    for jl_round in rounds:
        yield SharpeningRound(jl_round)

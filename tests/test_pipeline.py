"""
Test iterating on the sharpening rounds.

Running a round needs real metacells, so only what the rounds say about themselves is tested here: the round handles
come back as Python objects holding the values the Julia code gave them.
"""

# pylint: disable=missing-function-docstring

import pytest
from dafpy import memory_daf

import metacellspy as mc


def test_first_round() -> None:
    daf = memory_daf(name="memory!")

    for sharpening_round in mc.sharpening_rounds(initial_daf=daf, base_daf=daf, score_daf=daf, directory="unused"):
        assert sharpening_round.index == 1
        assert sharpening_round.previous_daf.name == "memory!"
        assert sharpening_round.metacells_prefix == "N"
        assert sharpening_round.blocks_prefix == "C"
        assert sharpening_round.directory == "unused"
        break


def test_round_must_run() -> None:
    daf = memory_daf(name="memory!")
    rounds = mc.sharpening_rounds(initial_daf=daf, base_daf=daf, score_daf=daf, directory="unused")

    next(rounds)
    with pytest.raises(Exception, match="the sharpening round: 1 was not run"):
        next(rounds)

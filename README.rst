metacellspy 0.1.0 - Metacell sharpening analysis
================================================

`Metacells.jl <https://github.com/tanaylab/Metacells.jl>`_ is a Julia package which sharpens metacells: groups metacells
into blocks, identifies the gene modules of each block, and sharpens the result by re-grouping the cells by these
modules. This package (``metacellspy``) is a wrapper around the Julia package that allows invoking these computations
from Python, using the `JuliaCall <https://github.com/JuliaPy/PythonCall.jl>`_ package.

This is unrelated to the `metacells <https://github.com/tanaylab/metacells>`_ Python package, which is a separate and
independent implementation used to compute the original (unsharpened) metacells.

Installation
------------

Just ``pip install metacellspy``, like installing any other Python package. This also installs
`dafpy <https://github.com/tanaylab/dafpy>`_, which the computations read their data from and write their results to.

Usage
-----

The Python package provides the same API as the Julia package, with the following modifications:

- The ``!`` suffix of the Julia name is dropped, so ``compute_metacells_blocks!`` in Julia is
  ``compute_metacells_blocks`` in Python.

- Every optional parameter defaults to ``None``, meaning "use whatever the Julia default is". The defaults are
  therefore never restated here, which matters because a Julia default may be computed from the other parameters.

- The ``rng`` parameter is an ``int`` seed rather than a Julia random number generator. The default ``0`` means "use
  Julia's default generator", that is, do not force reproducible results.

- Data is passed as ``dafpy`` repositories, and the computations which return a data frame return a
  ``pandas.DataFrame``.

- The Julia contracts, which describe what data each computation reads and writes, are not exposed; they are only
  usable from Julia. See the
  `contracts <https://tanaylab.github.io/Metacells.jl/v0.1.0/contracts.html>`_ documentation for the vocabulary of what
  lives in a repository.

Each function's documentation links to the Julia documentation of the function it invokes, which is where the details
live.

See the `Python v0.1.0 documentation <https://tanaylab.github.io/metacellspy/v0.1.0/html/index.html>`_ and the
`Julia v0.1.0 documentation <https://tanaylab.github.io/Metacells.jl/v0.1.0/index.html>`_ for details.

# The Julia side of `metacellspy`: the Julia packages it uses, and the precompilation of the calls Python makes.
#
# Python always loads `PythonCall` before anything else, so this loads it first too, and is precompiled the same way.
# Its workload runs `metacellspy.workloads.run_workload()` from Python, so this package caches the code those calls
# compile, and a session does not compile it again.
module MetacellsPy

using PythonCall
using PrecompileTools

import DafPy
import Metacells
import Random

# The code this caches depends on the Python code of `metacellspy`, which runs the workload. Julia only knows of its own
# sources, so this tells it to compile again when any of those files changes.
const METACELLSPY_DIRECTORY = joinpath(@__DIR__, "..", "..", "..")
for name in readdir(METACELLSPY_DIRECTORY)
    if endswith(name, ".py")
        include_dependency(joinpath(METACELLSPY_DIRECTORY, name); track_content = true)
    end
end

# Whether the Python that `PythonCall` runs imports the `metacellspy` this package belongs to. A precompilation started
# from plain Julia gets whatever Python `PythonCall` finds, which may lack `metacellspy`, or have a version of it without
# this package beside it. A directory named `metacellspy` in the working directory is also found, as a namespace with no
# origin.
function is_matching_metacellspy()::Bool
    spec = pyimport("importlib.util").find_spec("metacellspy")
    if pyis(spec, pybuiltins.None) || pyis(spec.origin, pybuiltins.None)
        return false
    end
    project_path = joinpath(dirname(pyconvert(String, spec.origin)), "julia", "MetacellsPy", "Project.toml")
    return isfile(project_path) && occursin("uuid = \"$(Base.PkgId(MetacellsPy).uuid)\"", read(project_path, String))
end

@compile_workload begin
    if !is_matching_metacellspy()
        error(
            "MetacellsPy could not be precompiled: the Python that PythonCall runs ($(PythonCall.C.CTX.exe_path)) " *
            "does not import the metacellspy that MetacellsPy belongs to.\n" *
            "This is harmless: MetacellsPy will be precompiled the first time you import metacellspy from Python.\n" *
            "To do it now, run: python -c \"import metacellspy\" (with the Python where metacellspy is installed).",
        )
    end
    # While this is precompiled, neither `metacellspy` nor `dafpy` below it can import anything into Julia's `Main`, so
    # their Julia packages are handed over here instead.
    pysetattr(pyimport("builtins"), "_dafpy_glue", Py(DafPy))
    pysetattr(pyimport("builtins"), "_metacellspy_glue", Py(MetacellsPy))
    pyexec("from metacellspy.workloads import run_workload\nrun_workload()", pydict())
end

end  # module

load("@lib//:requirements.bzl", "all_requirements")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

package(default_visibility=["//visibility:public"])

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
)

filegroup(
    name = "lib",
    srcs = glob(
        ["**"],
        exclude = ["**/*.pyc"],
    )
)

py_library(
    name = "py_lib",
    srcs = [":lib"],
    imports = [".."],
    deps = all_requirements
)
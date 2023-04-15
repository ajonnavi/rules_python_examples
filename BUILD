load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

py_binary(
    name = "main",
    srcs = ["main.py"],
    legacy_create_init = False,
    deps = [
        "@pypi_requests//:pkg",
        "//lib:py_lib"
    ],
)

py_binary(
    name = "main2",
    srcs = ["main2.py"],
    legacy_create_init = False,
    deps = [
        "@pypi2_requests//:pkg",
        "//lib:py_lib"
    ],
)

py_test(
    name = "test",
    srcs = ["test.py"],
    legacy_create_init = False,
    deps = [":main"],
)

# This rule adds a convenient way to update the requirements file.
compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
)


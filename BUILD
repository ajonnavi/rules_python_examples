load(
    "@pypi//:requirements.bzl",
    "data_requirement",
    "dist_info_requirement",
    "entry_point",
)
load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "@pypi_requests//:pkg",
    ],
)

py_binary(
    name = "main2",
    srcs = ["main2.py"],
    deps = [
        "@pypi2_requests//:pkg",
    ],
)

py_test(
    name = "test",
    srcs = ["test.py"],
    deps = [":main"],
)

# For pip dependencies which have entry points, the `entry_point` macro can be
# used from the generated `pip_parse` repository to access a runnable binary.

alias(
    name = "yamllint",
    actual = entry_point("yamllint"),
)

# This rule adds a convenient way to update the requirements file.
compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)

# Test the use of all pip_parse utilities in a single py_test
py_test(
    name = "pip_parse_test",
    srcs = ["pip_parse_test.py"],
    data = [
        ":yamllint",
        data_requirement("s3cmd"),
        dist_info_requirement("requests"),
    ],
    env = {
        "WHEEL_DATA_CONTENTS": "$(rootpaths {})".format(data_requirement("s3cmd")),
        "WHEEL_DIST_INFO_CONTENTS": "$(rootpaths {})".format(dist_info_requirement("requests")),
        "YAMLLINT_ENTRY_POINT": "$(rootpath :yamllint)",
    },
    deps = ["@rules_python//python/runfiles"],
)

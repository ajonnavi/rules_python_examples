workspace(name = "rules_python_pip_parse_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    # Bazel will print the proper value to add here during the first build.
    sha256 = "a644da969b6824cc87f8fe7b18101a8a6c57da5db39caa6566ec6109f37d2141",
    strip_prefix = "rules_python-0.20.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.20.0/rules_python-0.20.0.tar.gz",
    )

load("@rules_python//python:repositories.bzl", "python_register_toolchains", "py_repositories")

py_repositories()

# python_register_toolchains(
#     name = "python39",
#     python_version = "3.9",
# )

# load("@python39//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    # (Optional) You can set an environment in the pip process to control its
    # behavior. Note that pip is run in "isolated" mode so no PIP_<VAR>_<NAME>
    # style env vars are read, but env vars that control requests and urllib3
    # can be passed
    # environment = {"HTTPS_PROXY": "http://my.proxy.fun/"},
    name = "pypi1",
    # (Optional) You can provide extra parameters to pip.
    # Here, make pip output verbose (this is usable with `quiet = False`).
    # extra_pip_args = ["-v"],

    # (Optional) You can exclude custom elements in the data section of the generated BUILD files for pip packages.
    # Exclude directories with spaces in their names in this example (avoids build errors if there are such directories).
    #pip_data_exclude = ["**/* */**"],

    # (Optional) You can provide a python_interpreter (path) or a python_interpreter_target (a Bazel target, that
    # acts as an executable). The latter can be anything that could be used as Python interpreter. E.g.:
    # 1. Python interpreter that you compile in the build file (as above in @python_interpreter).
    # 2. Pre-compiled python interpreter included with http_archive
    # 3. Wrapper script, like in the autodetecting python toolchain.
    #
    # Here, we use the interpreter constant that resolves to the host interpreter from the default Python toolchain.
    # python_interpreter_target = interpreter,

    # (Optional) You can set quiet to False if you want to see pip output.
    #quiet = False,
    requirements_lock = "//app1:requirements-lock.txt",
    enable_implicit_namespace_pkgs = True,
)
load("@pypi1//:requirements.bzl", pypi1_install_deps="install_deps")
# Initialize repositories for all packages in requirements_lock.txt.
pypi1_install_deps()

pip_parse(
    name= 'pypi2',
    # python_interpreter_target = interpreter,
    requirements_lock = "//app2:requirements-lock.txt"
)
load("@pypi2//:requirements.bzl", pypi2_install_deps = "install_deps")
pypi2_install_deps()

pip_parse(
    name= 'lib',
    # python_interpreter_target = interpreter,
    requirements_lock = "//lib:requirements-lock.txt"
)
load("@lib//:requirements.bzl", lib_install_deps = "install_deps")
lib_install_deps()
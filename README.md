# Rules Python Playground

## Vendored Python or not

To use/not use Python being supplied by Bazel, simply comment out(or leave alone) the interpreter portions in the WORKSPACE file.

## Requirements Lock 

The requirements lock file can be generated using the Python utility `pip-compile`. This is part of the `pip-tools` package.

Simply run - `pip-compile -o requirements-lock.txt requirements.txt --generate-hashes`

# EECE 435L — Lab 6

AliRida Awad

## Contents

- `calculator_AliRida_Awad/`: graded exercise, including seven calculator operations, unit tests, and PyBuilder packaging.
- `my_python_project/`: optional exercise with greeting module, command-line application, tests, PyBuilder, and Makefile.
- `evidence/`: actual build output and terminal screenshot.

## Run either project

Open a terminal inside the desired project directory:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pyb run_unit_tests
pyb
```

On Windows, activate with `.venv\Scripts\activate` instead. Makefile commands require GNU Make.

`pyb` defaults to `publish`, which runs the unit tests and produces the distributable project, source archive, and wheel under `target/dist/`. Build dependencies are managed by the `python.install_dependencies` plugin. Neither application needs third-party runtime libraries.

For the calculator, the lab's direct unittest command also works from the project root:

```sh
python -m unittest tests.unittest.calculator_AliRida_Awad.test_calculator_AliRida_Awad
```

## Makefile targets

| Target | Action |
| --- | --- |
| `make install_deps` or `make install` | Install the tools listed in requirements.txt into the active Python environment. |
| `make test` | Run unit tests through PyBuilder. |
| `make lint` | Check source, tests, and build descriptor using Flake8. |
| `make build` or `make package` | Run PyBuilder publish, including testing and packaging. |
| `make clean` | Remove generated PyBuilder target output. |
| `make all` (also the default) | Run clean, dependency installation, tests, lint, and build in order. |

The all recipe invokes each stage sequentially, even when Make is invoked with parallel jobs. `PYTHON` and `PYB` can be overridden for a specific environment. A Makefile gives repeatable named commands, centralizes the workflow, and stops when a step fails. PyBuilder manages the Python-specific task dependencies, test discovery, and distribution generation.

## Calculator behavior

`add`, `subtract`, `multiply`, `divide`, `modulus`, `power`, and `square_root` implement the required operations. Division and modulus reject a zero divisor with ValueError. Square root rejects negative inputs with ValueError. Modulus follows Python's remainder convention, including negative operands. Power follows Python's exponentiation operator. Tests cover normal results, fractions, negative values, zero, and invalid inputs.

## Optional application

From `my_python_project`, run:

```sh
PYTHONPATH=src/main/python python src/main/python/app.py
```

It prints `Hello, World!`. The tests also check `Hello, PyBuilder!`.

## Verification

Verified with Python 3.14.7 and PyBuilder 0.13.24: 10 calculator tests and 2 greeting tests pass, both Flake8 checks pass, and both publish builds produce source archives and wheels. The calculator also passes the direct unittest command from the handout. `evidence/calculator-build.png` is an actual terminal capture showing BUILD SUCCESSFUL, the calculator base directory, finish time, and duration. Full publish logs are in evidence. PyBuilder publish creates local distribution files; it does not upload them to a package index.

The submission ZIP excludes temporary build environments, caches, and bytecode. Source code, build configuration, test reports, distribution artifacts, and evidence are included.

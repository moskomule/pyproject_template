# PyProject Template

This template automatically create a repository with [hatch](https://hatch.pypa.io/) using a given repository name.
For example, if you create a repository "foo" with this template and wait a few seconds,
the repository becomes something like below.

```
.gitignore
.github/workflows/...
docs/index.md
tests/...
foo/__init__.py
foo/__about__.py
mkdocs.yml
pyproject.toml
LICENCE
README.md
```

The created repository is ready for unit tests and document generation.
After cloning the created repository, edit the generated files according to your needs, e.g., appending dependencies in `pyproject.toml`.

To activate GitHub pages, go to `settings/pages/sources` and change it to `GitHub Actions`, so that the documents will automatically created.

To extend this template, fork this template and name it `*-template` to disable the [initializer action](.github/workflows/init.yaml).

The following section is the template of `README.md`.

---
# {repo_name}

**This project is work in progress**

![pytest](https://github.com/{owner_name}/{repo_name}/workflows/pytest/badge.svg)
[![document](https://img.shields.io/static/v1?label=doc&message={repo_name}&color=blue)](https://{owner_name}.github.io/{repo_name})

## Installation

```
hatch create env
```

or

```
pip install -U -e .
```
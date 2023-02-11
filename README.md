# PyProject Template

This template automatically create `hatch`-based repository using the given repository name.
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
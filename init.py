import pathlib

def pyproject_toml(owner_name: str, repo_name: str):
    content = f"""
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{repo_name}"
description = ''
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
keywords = []
authors = [
    {{ name = "{owner_name}", email = "{owner_name}@users.noreply.github.com" }},
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: Implementation :: CPython",
]
dependencies = [
    "rich"
]
dynamic = ["version"]

[tool.hatch.envs.default.env-vars]
PIP_EXTRA_INDEX_URL = "https://pypi.org/simple/"

[project.urls]
Documentation = "https://{owner_name}.github.io/{repo_name}"
Issues = "https://github.com/{owner_name}/{repo_name}/issues"
Source = "https://github.com/{owner_name}/{repo_name}"

[tool.hatch.version]
path = "{repo_name}/__about__.py"

[tool.hatch.envs.tests]
dependencies = [
    "pytest",
]

[[tool.hatch.envs.test.matrix]]
python = ["310", ]

[tool.hatch.envs.docs]
extra-dependencies = [
    "mkdocs-material"
]
[tool.hatch.envs.docs.scripts]
build = "mkdocs build --clean --strict"

[tool.hatch.build.targets.sdist]
exclude = [
    "/.github",
    "/docs",
    "/tests",
]
    """
    with open("pyproject.toml", 'w') as f:
        f.write(content[1:])

def mkdocs(owner_name: str, repo_name: str):
    content = f"""
site_name: {repo_name}
site_description: ...
site_author: {owner_name}
site_url: https://{owner_name}.github.io/{repo_name}
repo_name: {owner_name}/{repo_name}
repo_url: https://github.com/{owner_name}/{repo_name}
edit_uri: blob/main/docs

theme:
  name: material

  features:
    - content.code.annotate

markdown_extensions:
  # mathjax
  - pymdownx.arithmatex:
      generic: true

  # syntax highlighting
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences

nav:
  - Home: 'index.md'    
"""
    with open("mkdocs.yml", 'w') as f:
        f.write(content[1:])

    docs_root = pathlib.Path("docs")
    docs_root.mkdir()
    with (docs_root / "index.md").open('w') as f:
        f.write(f"# {repo_name}")

def project_dir(repo_name: str):
    root = pathlib.Path(repo_name)
    root.mkdir()
    (root / "__init__.py").touch()
    with (root / "__about__.py").open('w') as f:
        f.write("__version__ = '0.0.1'")

def readme(owner_name: str, repo_name: str):
    content = f"""
# {repo_name}

**This project is work in progress**

![pytest](https://github.com/{owner_name}/{repo_name}/workflows/pytest/badge.svg)
[![document](https://img.shields.io/static/v1?label=doc&message={repo_name}&color=blue)](https://{owner_name}.github.io/{repo_name})
    """
    with open("README.md", 'w') as f:
        f.write(content[1:])

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("name")
    args = p.parse_args()

    name = args.name
    owner_name, repo_name = name.split("/")
    pyproject_toml(owner_name, repo_name)
    mkdocs(owner_name, repo_name)
    project_dir(repo_name)
    readme(owner_name, repo_name)
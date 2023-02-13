import pathlib

def pyproject_toml(owner_name: str, repo_name: str):
    file = pathlib.Path("pyproject.toml")
    with file.open('r') as f:
        content = f.read()
    content = content.format(owner_name=owner_name, repo_name=repo_name)
    with file.open('w') as f:
        f.write(content)

def mkdocs(owner_name: str, repo_name: str):
    file = pathlib.Path("mkdocs.yml")
    with file.open('r') as f:
        content = f.read()
    content = content.format(owner_name=owner_name, repo_name=repo_name)
    with file.open('w') as f:
        f.write(content)

    docs_root = pathlib.Path("docs")
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

## Installation

```
hatch create env
```

or

```
pip install -U -e .
```

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
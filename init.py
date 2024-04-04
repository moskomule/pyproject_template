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
    file = pathlib.Path("README.md")

    with file.open('r') as f:
        content = f.read()

    content = content.split('---')[1][1:]  # to remove first \n
    content = content.format(owner_name=owner_name, repo_name=repo_name)

    with file.open('w') as f:
        f.write(content)


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

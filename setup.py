from setuptools import find_packages, setup

setup(
    name="pre-commit-hooks-poetry",
    version="0.5.0",
    install_requires=["poetry"],
    packages=find_packages(),
    entry_points={"console_scripts": ["poetry-export = pre_commit_hooks.export:main"]},
)

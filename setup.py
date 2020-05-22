from setuptools import setup


setup(
    name='pre-commit-hooks-poetry',
    version='0.0.0',
    install_requires=['poetry'],
    console_scripts={
        'export': 'pre_commit_hooks.export:main',
    },
)

from setuptools import setup

setup(
    name="pytest-mypy-testing",
    entry_points={"pytest11": ["pytest_mypy_testing = pytest_mypy_testing.plugin"]},
    classifiers=["Framework :: Pytest"],
    version="0.1.0",
    packages=["pytest_mypy_testing"],
    install_requires=["pytest>=7.0.0"],
)

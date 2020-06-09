import pathlib
from setuptools import setup

# The directory containing this file
BASE_PATH = pathlib.Path(__file__).parent

# The text of the README file
README = (BASE_PATH / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyloopia",
    version="0.1.0",
    description="python interface for Loopia API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pnx/pyloopia",
    author="Henrik Hautakoski",
    author_email="henrik@eossweden.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    package_dir={"": "src"},
    packages=[],
    include_package_data=True,
    install_requires=[],
    entry_points={},
)

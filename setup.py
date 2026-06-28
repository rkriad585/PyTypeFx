from pathlib import Path

from setuptools import find_packages, setup

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text()

setup(
    name="PyTypeFx",
    version="2.1.1",
    author="RK RIAD KHAN",
    author_email="rkriad585@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "typing_extensions; python_version < '3.8'",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"console_scripts": ["typefx = typefx.cli:main"]},
)
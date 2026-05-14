from setuptools import find_packages, setup

setup(
    name="typefx",
    version="2.0.1",
    author="RK RIAD KHAN",
    author_email="rkriad585@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "typing_extensions; python_version < '3.8'",
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"console_scripts": ["typefx = typefx.cli:main"]},
)

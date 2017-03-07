#!/usr/bin/env python
# encoding: utf-8
"""
快递鸟 Python SDK
"""
from setuptools import setup, find_packages

repo_url = "https://github.com/menduo/kdniao_python"
__version__ = "0.1.2"

setup(
    name="kdniao",
    version=__version__,
    keywords=("kdniao", "express", "Express inquiry"),
    description="Python SDK for Kdniao",
    long_description="see more at:\n%s\n" % repo_url,
    license="MIT",
    url=repo_url,
    author="menduo",
    author_email="shimenduo@gmail.com",
    packages=find_packages(),
    scripts=["bin/kdniao"],
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=["requests", "tornado>=4.0.2"],
)

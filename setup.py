# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="stacklogging",
    packages=find_packages(),
    version="0.1.0",
    description="Python logging integration with Google Cloud Stackdriver API.",
    author="David Gasquez",
    license="MIT",
    author_email="davidgasquez@buffer.com",
    url="https://github.com/bufferapp/stacklogging",
    keywords=["stackdriver", "logging", "google-cloud"],
    install_requires=["structlog"],
)

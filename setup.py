# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="stacklogging",
    packages=find_packages(),
    version="0.2.1",
    description="Python structured logging with Google Cloud Stackdriver API integration",
    author="David Gasquez",
    license="MIT",
    author_email="davidgasquez@buffer.com",
    url="https://github.com/bufferapp/stacklogging",
    keywords=["stackdriver", "logging", "google-cloud"],
)

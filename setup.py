import pathlib
from setuptools import setup

setup(
    name="python-cbr",
    version="0.2.0",
    description="Read the official exchange rates data from cbr.ru",
    long_description=open('README.txt').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/grunichev/cbr",
    author="Alexey Grunichev",
    author_email="grunichev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cbr"],
    include_package_data=True,
)

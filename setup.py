import io
import os

from setuptools import find_packages, setup

from thecut.ordering import __version__

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        filename = os.path.join(here, filename)
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read("README.rst", "HISTORY.rst")

setup(
    # General information
    name="thecut-ordering",
    version=__version__,
    # Packaging
    packages=find_packages(exclude=["docs"]),
    namespace_packages=["thecut"],
    include_package_data=True,
    # Dependencies
    install_requires=[],
    # Author information
    author="The Cut Creative",
    author_email="development@thecut.net.au",
    # Additional information
    url="https://projects.thecut.net.au/projects/thecut-ordering",
    license="Apache Software License 2.0",
    description="A reusable application.",
    long_description=long_description,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
    ],
)

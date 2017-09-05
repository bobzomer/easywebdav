import os
import functools
from setuptools import setup, find_packages

_IN_PACKAGE_DIR = functools.partial(os.path.join, "easywebdav2")

with open(_IN_PACKAGE_DIR("__version__.py")) as version_file:
    exec(version_file.read())

properties = dict(
    name="easywebdav2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.3",
    ],
    description="A straight-forward WebDAV client, implemented using Requests",
    license="ISC",
    author="Amnon Grossman",
    author_email="emesh1@gmail.com",
    url="http://github.com/zabuldon/easywebdav",
    version=__version__,  # noqa
    packages=find_packages(exclude=["tests"]),
    data_files=[],
    install_requires=[
        "requests",
        "six",
    ],
    entry_points=dict(
        console_scripts=[],
    ),
)

# Properties for development environments
if "EASYWEBDAV2_DEV" in os.environ:
    properties["install_requires"].append((
        "nose",
        "yanc",
        "PyWebDAV",
        "unittest2",
    ))

setup(**properties)

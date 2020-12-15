import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="secret_santa",
    version="0.1",
    description="Secret Santa Recipient Picker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Howard Taylor",
    author_email="hwtaylor@gmail.com",
    install_requires=[
        'pandas==1.1.5'
    ],
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    # packages=find_packages(exclude=['docs', 'testdata']),
    package_dir={"": "src"},
)

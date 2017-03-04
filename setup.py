import os
from setuptools import setup, find_packages

REQUIREMENTS = [line.strip() for line in
                open(os.path.join("requirements", "requirements.txt")).readlines()]

setup(
    name='happiness',
    version='0.1',
    include_package_data=True,
    install_requires=REQUIREMENTS,
)

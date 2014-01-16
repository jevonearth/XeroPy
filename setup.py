#/usr/bin/env python
from setuptools import setup, find_packages
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
        name="XeroPy",
        description="Pythonic ORM implementation of the Xero API",
        zip_safe= False,
        version="1.3",
        packages = ['xero',],
        install_requires=[
            'httplib2',
            'oauth2',
            'SocksiPy-branch',
            'python-dateutil',
            ],
        )

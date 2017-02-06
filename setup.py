#!/usr/bin/env python

from setuptools import setup, find_packages

# Dynamically retrieve the version information from the chatterbot module
HPALM = __import__('hpalm')
VERSION = HPALM.__version__
AUTHOR = HPALM.__author__
AUTHOR_EMAIL = HPALM.__email__
URL = HPALM.__url__
DESCRIPTION = HPALM.__doc__

with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='py-hpalm',

    # http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#choosing-a-versioning-scheme
    version=VERSION,
    url=URL,
    # download_url='{}/tarball/{}'.format(URL, VERSION),
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    platforms="any",
    packages = find_packages('hpalm'), # include all packages under src
    package_dir={'hpalm': 'hpalm'}, # tell distutils packages are under src
    include_package_data=True,
    # http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',        
        'Programming Language :: Python :: 2.7',
    ],

    keywords='HP ALM',
    license='BSD',
    install_requires=REQUIREMENTS,

)
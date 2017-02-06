#!/usr/bin/env python

from setuptools import setup, find_packages

package_requires = [
    'requests',
    'lxml',
]

setup(
    name='py-hpalm',

    # http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#choosing-a-versioning-scheme
    version='0.0.1',

    author='Mallikarjunarao Kosuri',
    author_email='venkatamallikarjunarao.kosuri@adtran.com',
    platforms="any",

    packages = find_packages('src'), # include all packages under src
    package_dir={'':'src'}, # tell distutils packages are under src

    include_package_data=True,

    # http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',        
        'Programming Language :: Python :: 2.7',
    ],

    url = "https://github.com/vkosuri/py-hpalm",

    keywords='HP ALM',

    install_requires = package_requires,

)
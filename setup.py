"""
:copyright: (c) 2014 Building Energy Inc
"""
from setuptools import setup, find_packages

from mcm import VERSION

setup(
    name='seed-mcm',
    version='.'.join(map(str, VERSION)),
    description='Map Clean Merge: Convert CSV Data into Python Objects.',
    long_description=open('README.md').read(),
    author='Gavin McQuillan, Aleck Landgraf',
    author_email='gavin.mcquillan@buildingenergy.com',
    url='https://github.com/SEED-platform/seed-mcm/',
    license='Modified BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.md']},
    install_requires=[
        'nose',
        'python-dateutil',
        'unicodecsv',
        'xlrd>=0.9.3',
        'jellyfish>=0.3.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Modified BSD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

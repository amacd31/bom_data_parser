import os
from io import open

import versioneer

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = ''.join([
            line for line in f.readlines() if 'travis-ci' not in line
        ])

setup(
    name='bom_data_parser',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Basic library for parsing data formats supplied by the Australian Bureau of Meteorology.',
    long_description=long_description,
    author='Andrew MacDonald',
    author_email='andrew@maccas.net',
    license='BSD',
    url='https://github.com/amacd31/bom_data_parser',
    install_requires= [
        'numpy',
        'pandas',
        'beautifulsoup4',
        'lxml',
    ],
    packages = ['bom_data_parser'],
    test_suite = 'nose.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

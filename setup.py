# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='checkrequirements',
    version='2020.0.3',
    description='Check that your requirements.txt is up to date with the most recent package versions',
    python_requires='==3.*,>=3.5.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/CheckRequirements/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/CheckRequirements",
        "repository":
            "https://github.com/FHPythonUtils/CheckRequirements"
    },
    author='FredHappyface',
    classifiers=[
        'Environment :: Console', 'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    entry_points={
        "console_scripts": ["checkrequirements = checkrequirements:cli"]
    },
    packages=['CheckRequirements'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'requests==2.*,>=2.24.0', 'requirements-parser==0.*,>=0.2.0'
    ],
    extras_require={"full": ["metprint==2020.*,>=2020.6.1"]},
)
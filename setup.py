#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'click_log', 'pycryptodome', 'requests', 'zeroconf>=0.23.0']
setup_requirements = []
test_requirements = ['pytest', 'tox', 'python-coveralls', 'flask', 'flake8']

setup(
    author="Matt Saxon",
    author_email='saxonmatt@hotmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Interface for Sonoff devices running R3+ Itead "
                "firmware.",
    entry_points={
        'console_scripts': [
            'pysonofflan=pysonofflan.cli:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pysonofflanr3',
    name='pysonofflanr3',
    packages=find_packages(include=['pysonofflanr3']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mattsaxon/pysonofflan',
    version='3.0.0',
    zip_safe=False,
)

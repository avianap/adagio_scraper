#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['setuptools_scm']

setup_requirements = ['pytest-runner','setuptools_scm']

test_requirements = ['pytest', ]

setup(
    author="Aviana Polsky",
    author_email='aviana.polsky@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Scrape information about teas from www.adagio.com",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tea_scraper',
    name='tea_scraper',
    packages=find_packages(include=['tea_scraper']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/avianap/tea_scraper',
    version='0.1.0',
    zip_safe=False,
    use_scm_version=True,
)

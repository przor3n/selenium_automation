#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    Readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Przemek Kot",
    author_email='przemyslaw.kot@gmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Selenium automation - automation made with Selenium",
    entry_points={
        'console_scripts': [
            'selenium_automation=selenium_automation.cli:main',
        ],
        'selenium_automation': [
            'selenium_automation.commands=selenium_automation.commands'
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=Readme + '\n\n' + history,
    include_package_data=True,
    keywords='selenium automation',
    name='selenium_automation',
    packages=find_packages(include=['selenium_automation']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/krisurban/selenium_automation',
    version='0.1.0',
    zip_safe=False,
)

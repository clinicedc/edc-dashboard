# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages
from os.path import join, abspath, normpath, dirname

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(join(dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = ['edc-appointment', 'edc-consent', 'edc-metadata',
                 'edc-device', 'edc-identifier', 'edc-model-wrapper',
                 'edc-protocol', 'edc-visit_schedule', 'edc-visit-tracking',
                 'edc-timepoint', 'edc-registration', 'edc-auth',
                 'edc_test_utils', 'edc-data-manager']
with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name='edc-dashboard',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    url='http://github.com/clinicedc/edc-dashboard',
    license='GPL license, see LICENSE',
    description='Dashboard classes, templates for clinicedc/edc projects.',
    long_description=README,
    include_package_data=True,
    zip_safe=False,
    keywords='django Edc dashboard classes and templates',
    install_requires=[
        "django-js-reverse",
        "edc-navbar"],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)

from setuptools import setup

description = 'Collection of fun git commands'
long_desc = open('README.rst').read()

setup(
    name='gitutils',
    version='0.1.2',
    install_requires=[],
    description=description,
    long_description=long_desc,
    author='Honza Pokorny',
    maintainer='Honza Pokorny',
    maintainer_email='me@honza.ca',
    packages=['gitutils'],
    include_package_data=True,
    scripts=['bin/blamer', 'bin/chart'],
)

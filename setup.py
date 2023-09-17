from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='Description of my package',
    author='Bohao Chen',
    author_email='chen.boha@northeastern.edu',
    install_requires=[
        # List of dependencies
    ],
)

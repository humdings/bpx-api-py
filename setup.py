from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='bpx',
    version="1.0.2",
    description='Backpack Crypto API trading stuff.',
    url='https://github.com/humdings/bpx-api-py',
    # author='David Edwards',
    # author_email='humdings@gmail.com',
    # license='MIT',
    classifiers=[
        
    ],
    platforms=['any'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
)

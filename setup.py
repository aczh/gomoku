from setuptools import setup

with open('.version', 'r') as f:
    VERSION = f.read()

setup(
    name='gomoku',
    description='Gomoku AI Implementation',
    author='Allen Zhang',
    version=VERSION,
    packages=[
        'gomoku',
    ],
    install_requires=[
        'pytest',
        'gmpy2',
    ],
)

from setuptools import setup

with open('.version', 'r') as f:
    VERSION = f.read()

setup(
    name='Gomoku',
    description='Gomoku AI Implementation',
    author='Allen Zhang',
    version=VERSION,
    packages=[
        'gomoku',
    ],
    install_requires=[
        'pytest'
    ],
)

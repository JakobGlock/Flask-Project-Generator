from setuptools import setup, find_packages

setup(
    name='fpgen',
    version='0.1',
    packages=find_packages('fpgen'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fpgen = fpgen.cli:main',
        ],
    }
)

from setuptools import setup

setup(
    name='fpgen',
    version='0.1',
    py_modules=['fpgen'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        fpgen=fpgen.cli:main
    ''',
)

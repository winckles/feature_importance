from setuptools import setup

setup(
    name='calculator',
    version='0.0.2',
    author="Lorence Cramwinckel",
    author_email="lorcr@live.nl",
    description='A simple calculator package',
    url="https://github.com/winckles/calculator_package",
    py_modules=["calculator_package"],
    package_dir={'': 'calculator'},
    python_requires='>=3.6',
)

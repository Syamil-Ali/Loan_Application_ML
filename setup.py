from setuptools import setup, find_packages

setup(
    name = 'loan_application_project',
    version = '1.0',
    packages = find_packages()
)

# run this pip install -e .
# -e = is for interactive installation
# . = is for all packages
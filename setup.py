from setuptools import setup, find_packages

setup(
    name='uluwatu',
    version = "0.1",
    description = ("Uluwatu: Solidity contract testing for Cloudbreak"),
    include_package_data=True,
    packages=find_packages(),
)
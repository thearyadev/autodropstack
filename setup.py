from setuptools import setup, find_packages

setup(
    name="autodropstack",
    version="1.0.0",
    description="filo stack",
    author="thearyadev",
    packages=find_packages(),
    package_data={"": ["*.txt", "*.md"]},
    long_description=open("README.md").read(),
)

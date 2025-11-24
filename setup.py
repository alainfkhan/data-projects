from setuptools import setup, find_packages

setup(
    name="data-projects",
    version="0.1.0",
    description="App to initialise online dataset installs.",
    license="MIT",
    author="Alain Khan",
    packages=find_packages(),
    entry_points={"console_scripts": ["dps = src.dps_launcher:main"]},
)

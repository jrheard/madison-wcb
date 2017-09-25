from setuptools import find_packages, setup

setup(
    name="madison_wcb",
    version="0.1.0",
    description="A library that allows users to directly control a WaterColorBot by writing Python code.",
    url="http://github.com/jrheard/madison_wcb",
    author="JR Heard",
    license="MIT",
    packages=find_packages(),
    install_requires=['requests'],
)

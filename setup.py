from setuptools import find_packages, setup

long_description="This library's source code lives at https://github.com/jrheard/madison_wcb and its documentation lives at http://madison-wcb.readthedocs.io/."

setup(
    name="madison_wcb",
    version="0.1.8",
    description="A library that allows users to directly control a WaterColorBot by writing Python code.",
    long_description=long_description,
    url="http://github.com/jrheard/madison_wcb",
    author="JR Heard",
    author_email="jrrrheard@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=['requests'],
)
